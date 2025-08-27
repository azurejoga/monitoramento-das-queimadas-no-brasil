# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1a7b0e8-ea1a-31a8-9788-f803336bbc4e | -9.07897 | -49.55674 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c08ab16-f519-3473-b807-38634a852cb4 | -6.76937 | -59.67924 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4b6f0c8-46eb-3591-b1ee-cedd45701948 | -9.27282 | -56.91203 | 2025-08-27 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfd36cdf-5ffb-37a9-8eef-930ec0df9e7d | -5.87931 | -46.40516 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a4881d2-03a2-3175-b0bf-eed1877bba64 | -8.07869 | -44.82492 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7358ddad-6cb9-3511-aa2b-79c512b31e67 | -10.87192 | -45.23262 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d720d16-a97a-365a-9f9e-5ebda3aa190c | -8.48261 | -43.65268 | 2025-08-27 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 719cda6f-2ebe-3cce-b4ef-c58c8a06e0cf | -9.18068 | -59.45879 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 344ea344-e713-31b1-b535-8e75de081e76 | -6.2362 | -60.02418 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93de44c2-3481-3f62-b6c8-ba333a50f752 | -10.71525 | -47.09794 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e7f350d-c56f-34bc-9b0d-6db08abac630 | -6.96337 | -44.10741 | 2025-08-27 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cba6343d-6b3a-3e17-affe-fbc63e0b7f29 | -9.95061 | -46.49464 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b293483-7174-381f-8a96-1b58a966c91b | -6.80159 | -44.34037 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41f8e213-7e7f-3090-9ad2-a4d5b37a67ed | -6.12721 | -42.94668 | 2025-08-27 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 87331d32-4bdf-3944-b23a-c8cdb92d8c22 | -11.07561 | -44.78487 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 949d985e-6476-3e96-9830-e15b773a1da1 | -6.81495 | -58.97917 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f42b45f-ab7f-3edc-934f-0d1c6563fd86 | -7.88204 | -45.87078 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a16e951-65fb-33b5-8511-e03e2c6db670 | -6.91412 | -59.3688 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40523a69-7d56-38ac-b773-b5cbc5e42b76 | -9.09442 | -49.57452 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ebcbdd41-3576-3c79-bb68-3b1e0c8ed48d | -7.73975 | -50.2796 | 2025-08-27 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ac669bc3-6a48-3076-be4c-e5ae1ffbf81d | -9.27781 | -59.78946 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a98aa107-3883-3e17-8952-ecc25de8d5e5 | -9.57938 | -55.37742 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c059e1d-fbab-3af6-a8f8-ce9ad63f2fc7 | -7.73606 | -50.27891 | 2025-08-27 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eebf680e-2836-3fff-8f06-e8088ea42cc3 | -10.63092 | -47.48238 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1958a16b-0a82-3389-90ed-443789327516 | -10.7893 | -46.38047 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 473f5955-773f-3795-96dd-b191c6d548f9 | -10.93456 | -47.43069 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88a2d62c-6750-339a-9ecd-2bc378ee1ebe | -5.90496 | -45.52963 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2e5e0ba-2ac5-34b9-a91e-79873a1f25d2 | -5.78488 | -46.14233 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74bebe0c-94fe-3f1a-9303-778b56cd0a77 | -6.32371 | -42.88106 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e5f1267-d9e4-383d-9a97-cfe048adc4e0 | -5.54756 | -42.62792 | 2025-08-27 04:25:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 33f3de0e-b2b1-3776-9dfa-f96294e8b60a | -8.89089 | -60.77552 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71ba0bc3-8619-3a79-bb08-4f8703425544 | -7.70356 | -45.775 | 2025-08-27 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 12266bf1-85f8-301c-bc1f-95dc0281cca7 | -7.89202 | -45.87234 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7beec07-3fe8-3cfe-8a45-8c85055d3b50 | -6.96743 | -44.10415 | 2025-08-27 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf4af1d7-b461-36db-86cf-95fc2e33fe38 | -9.27837 | -56.91311 | 2025-08-27 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dd1453b-4a06-3b27-aa8a-167ec2deff7c | -6.80504 | -44.34084 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12f713bd-5b66-34cf-94cd-7637b113f44b | -5.95185 | -42.49238 | 2025-08-27 04:25:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 395e5d7d-68cf-30a2-8b79-52b0c256c2a6 | -9.50599 | -46.71117 | 2025-08-27 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 636ecf61-a05e-3e52-884e-c86b8b0f4f24 | -7.74413 | -50.27604 | 2025-08-27 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f56a9be3-ed0e-35a4-905a-0cf5d877665f | -9.07768 | -49.56467 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a02a963-573c-3d2f-a6e3-c25984044b3c | -5.76024 | -43.39196 | 2025-08-27 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ccdd3fe-729b-3e08-b1cd-8bfdf0f1225f | -9.15546 | -59.55276 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11674a70-a35a-3a37-b0da-b839ace545dd | -8.47983 | -43.65498 | 2025-08-27 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67c067c8-2867-39f3-9bc5-a2a3dc55c42b | -6.69854 | -58.56089 | 2025-08-27 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47ab5661-cffb-39c3-adc5-fc461b9a6075 | -6.76116 | -43.82267 | 2025-08-27 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 823559b2-e31a-374e-9527-67945e85097c | -4.49767 | -46.37805 | 2025-08-27 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b8d01f5-3ff1-35a4-a758-7c7b9d4e7f77 | -9.17391 | -60.86838 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d43ea181-dfdd-33c4-93ea-7d4a5b3b7caf | -4.95681 | -55.81417 | 2025-08-27 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07c804eb-952a-3d76-952d-f59ff0621fd5 | -11.14937 | -44.77488 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d132a18-826e-32fa-b4c7-d3a45c9421b6 | -9.46812 | -57.82481 | 2025-08-27 04:25:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57b1e25c-b070-39af-bebd-87cc06008211 | -6.18786 | -43.01268 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac99dfef-a301-3e82-a918-261ba084fd06 | -8.26085 | -45.12395 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa4e309c-cc9c-3042-b380-8c8c66cccc67 | -6.81812 | -58.96218 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c79d9af0-c652-3c9c-ae97-04233a3e47a1 | -5.95362 | -42.49427 | 2025-08-27 04:25:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6162d0b3-c2ef-3ccd-af6a-7ea95f41330f | -7.64907 | -42.66854 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 54a8e9b2-b0da-3bd6-ab12-d1ab1fbb5e0b | -8.8633 | -47.16855 | 2025-08-27 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f31322d2-6704-3ad5-8960-750be7356fdc | -4.49436 | -46.37753 | 2025-08-27 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a5dcfd6-81e0-34fe-a873-1746d5717e4e | -10.65683 | -47.18894 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0c55eaa-2e61-3aaa-b09c-fea71928f2a8 | -10.7158 | -47.09443 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ead5619-c1f2-3a94-96ae-76b497014868 | -9.58831 | -55.38525 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69325e51-636c-3494-bde4-f8fb377f5495 | -11.26136 | -44.99305 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a26dd71-3e4a-370c-9920-5b45090eeb00 | -9.30049 | -48.27761 | 2025-08-27 04:25:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3fc10c2-2547-319a-bd9a-78c25a5a52b4 | -11.2567 | -44.97638 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaa4f877-6425-36a5-90e5-0a3ff7c1b060 | -9.09508 | -49.57056 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 78dbf8c3-6b53-3050-b534-70a1e2be828e | -7.17144 | -45.15084 | 2025-08-27 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8ea6103-1db6-3b1f-98de-49724be04e24 | -6.82256 | -58.9748 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8a942aa-d819-3e92-bf0d-f87979a18a63 | -10.78253 | -47.0585 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11b543f7-3879-358d-b30d-9b3eddab1f35 | -11.15523 | -44.80834 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b2866b8-84e9-367f-844e-d77fdf8bc651 | -6.52216 | -42.97827 | 2025-08-27 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cb49abe-628a-3a87-be66-0a1b1e26f9d1 | -6.29 | -43.78009 | 2025-08-27 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5c93a6f-436a-31a0-abed-560aa96677b9 | -6.84084 | -42.82324 | 2025-08-27 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dd30dc9f-05c5-3559-a9d2-330502670fea | -8.09526 | -44.83074 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b0a926f-ece7-3c46-a073-f18e04f0d8e5 | -7.05016 | -44.29597 | 2025-08-27 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 308dd13b-759e-352b-8e1e-7e7bb2a914bf | -7.34706 | -57.63526 | 2025-08-27 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38677ddc-ca53-32f2-86f4-3712d1053210 | -11.45553 | -47.3134 | 2025-08-27 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| beb48c2c-5615-39bb-aa89-8cdc58a31507 | -7.34998 | -57.63031 | 2025-08-27 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2237eb6-87ee-3b23-8c1f-105b47137ef1 | -9.58589 | -55.36988 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c53e679-28fe-3020-9a24-2e15c2b1adb7 | -11.07972 | -44.78144 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b3dfa7c3-5eb2-3e92-be74-a11d888d4afe | -9.16313 | -59.54833 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f6e157d-0553-3c9d-b32d-ac8299011864 | -6.90128 | -44.39748 | 2025-08-27 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf15cf61-9706-3e99-b8ad-418ef52b3afa | -11.15934 | -44.78048 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 169f5b85-4c15-3888-9740-1429f579ba2e | -9.0909 | -49.57395 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6c4b768-10b6-3892-94ab-cf12a4aeeb1b | -4.96175 | -55.81877 | 2025-08-27 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdafc3e4-c196-3236-b13c-4ad76dda57b2 | -6.80446 | -44.34465 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 630b661f-6564-3ff4-8063-952dea0631b6 | -10.31198 | -46.81122 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1c53dd5-1bd5-39e3-bbe9-0f0eaee1c303 | -8.27157 | -45.12194 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3310dd0b-a9f8-3588-8c2c-10334253f32a | -8.09497 | -45.01619 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c57a51c-515f-3981-bd78-dd22d45e8c28 | -7.57721 | -47.50008 | 2025-08-27 04:25:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12cc67ab-bfc9-3268-bbbc-85906f1de835 | -9.95339 | -46.49868 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f25348c3-8a35-3dae-bc97-991154c712f9 | -8.26108 | -45.11696 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bd26e5b-d8b8-365d-aaef-afdc135c98c4 | -8.37665 | -47.43044 | 2025-08-27 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 576ffe5a-1dd8-3bec-b7b1-c6dc31b75df2 | -9.07684 | -49.57162 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e45b491c-7ef4-3563-98ec-f39093ba9eca | -9.56836 | -55.38131 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb55ef04-2b7d-398d-b7d1-7b5966498c11 | -7.88924 | -45.86832 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4955ebc-7282-32bc-a79e-6cd78e62f49e | -9.94506 | -46.48657 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dfc125f-eb01-37f9-ae63-cdfc8f364598 | -5.62586 | -45.72825 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61457f11-2079-3465-bd2e-fff4190b5abb | -6.76252 | -59.678 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9eb8c59-9371-328c-b4f5-670a7c0060b3 | -9.07571 | -49.60001 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ee29735-0844-32bd-a7dd-9798bd52d83e | -6.30192 | -42.8039 | 2025-08-27 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 222913c0-0e17-3396-be44-e47753fb053d | -6.62468 | -53.32412 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README36.md)
