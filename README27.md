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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6572bd2c-1bd4-3cac-afa9-473c112d4955 | -6.1501 | -41.77776 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e03f77d-2b81-373b-ad8f-7db5ff6970f2 | -5.43531 | -44.21925 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bea2264e-57d1-3140-bcec-538a2e92ade2 | -6.22607 | -41.55556 | 2025-10-15 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 620e3e40-8300-37ff-855d-486adfed3ebd | -3.07586 | -49.50042 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbde468e-8029-3b68-b9ac-bfdc88e1214f | -5.8666 | -43.86625 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73debc21-e2c9-3e34-8e4c-be74f6e36bcb | -3.57004 | -49.44139 | 2025-10-15 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff7da237-539f-3fff-b212-b76dfee8fc79 | -3.56952 | -49.44452 | 2025-10-15 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8fde4afc-04bb-3166-b348-4c1a2b388a89 | -4.14097 | -41.65539 | 2025-10-15 04:06:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a757513c-6a36-3af1-91a5-67d5e7bbca49 | -9.16239 | -46.19607 | 2025-10-15 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aaa15f6e-b2d1-3e6a-96db-7219a083abeb | -4.8057 | -45.71537 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69f493dc-dead-33cf-baed-0f4c2b2e934a | -4.65167 | -43.13426 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfc98a6d-2ab9-3621-8b00-ba14299ffbcf | -5.90587 | -42.81636 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf45a170-ede5-3348-ba92-e7ded65f004e | -8.24422 | -43.34607 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e759e623-ad04-3165-9000-9d391afa6278 | -3.40731 | -46.89965 | 2025-10-15 04:06:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d9ab965-de83-3f12-86f3-e9c6278f2415 | -4.85703 | -43.20914 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cce170d4-b27c-3ba4-b199-12e456792074 | -5.03985 | -42.57613 | 2025-10-15 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0042015d-d9ba-37ce-a153-c2d4ebec41e0 | -9.15334 | -46.88717 | 2025-10-15 04:06:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b09fc08-90ec-3574-a43f-682954a5f1cc | -8.46178 | -44.19491 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 877369e8-bfb9-38ac-82d4-584f64da808f | -5.89267 | -43.74944 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 302e6b56-ef00-3de6-a610-91592c3d3f71 | -5.4544 | -44.64859 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 763fa681-65eb-3b3b-983b-f66449cbee1e | -4.90222 | -43.46831 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 14829516-44f7-3927-a90d-cb964a8ca284 | -5.53802 | -41.32912 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f8c03eb4-4f52-34f7-9ea8-f0572d4bbb12 | -5.88916 | -43.74888 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e6549858-7bbd-34b2-87c6-30143fc10e8d | -6.20205 | -43.28733 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d66f36c-bbac-3172-9681-0e4587ff9ac5 | -3.43114 | -50.25301 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4088bc3-81c3-3ea5-89c8-15074a52fff7 | -5.37121 | -46.65953 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0a79084-3bc7-3a3b-a38e-3f4dfe33b9e0 | -7.48222 | -42.65159 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9967aa77-8622-3920-bbcd-63cacc25141d | -8.22006 | -44.08033 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6a14196-49a9-342c-9bfe-5cdb08a33ed3 | -7.39489 | -46.78703 | 2025-10-15 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1da41093-c0d8-3cee-8a95-ec95ec20db56 | -7.16 | -42.49878 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 71c274bd-8c67-304b-8856-bbdd149f1f26 | -4.39198 | -43.46297 | 2025-10-15 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ad363f1-3b01-3ade-9b5c-d15755e30064 | -7.54141 | -43.93428 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a609d802-d52a-30c3-93c0-76b5b79ad155 | -7.00672 | -38.35844 | 2025-10-15 04:06:00 | NOAA-20 | CARRAPATEIRA | PARAÍBA | Brasil | 2504108 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b5297b77-43b2-36c5-9247-32e479920f3c | -5.16435 | -46.27689 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05dce59f-0072-3661-b7f1-959f055673c0 | -5.16786 | -46.28106 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4066e022-1b7c-34d6-8cd0-57ee50415858 | -7.75636 | -42.446 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9389cc97-e88b-3acf-b583-6572e18ea7e4 | -6.45827 | -41.89068 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d0643fb-8dd2-3fdc-9565-7ed717793570 | -6.19599 | -42.60022 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fb67ced8-d3ea-37a5-a0fd-f56ad826ed7e | -5.5641 | -43.0006 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1f577ad9-5041-3835-bf44-8d18a381b0eb | -5.43046 | -41.34389 | 2025-10-15 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a7126031-c1e6-3831-929b-579f16e0b2b2 | -5.09939 | -42.63783 | 2025-10-15 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ec25da6-ce23-3379-98e6-3c0c662b253f | -5.39214 | -41.15767 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c31ece05-8cda-39fc-8524-fb001dac9d8c | -5.25676 | -40.98113 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c7380c23-9777-3dea-b0b6-fdfeb3dd9a00 | -4.87178 | -45.77591 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77dfe221-026d-3d39-a119-f197f974269a | -3.83579 | -44.54794 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 40bccbb7-ecfb-394a-a6b0-3f06a8889721 | -5.42695 | -44.42897 | 2025-10-15 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 515906fc-348b-3e3a-80da-8218ca341c73 | -8.19137 | -43.97293 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1fa849b8-85fe-316f-87ee-ad74fe9455ba | -8.24143 | -43.34185 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4a00da4d-05ae-37f3-8773-7d6b6d25ab2a | -6.40653 | -45.36327 | 2025-10-15 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28cab3c4-777c-3d92-8684-0b7e35959c1a | -7.56764 | -43.83971 | 2025-10-15 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c4a0255-5447-33a8-a042-6301ec1855c6 | -5.26735 | -43.22984 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 871c13e5-f33e-3d49-bfb3-4d837a16121e | -4.35667 | -46.78491 | 2025-10-15 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51052bde-7754-3d2d-a03c-2b37bafad7ba | -7.16498 | -42.51046 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a8103ad-d8de-3b91-84ad-c868b458d430 | -5.88565 | -43.74831 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 22bfa40f-7b1c-38b1-9487-270acd89b974 | -5.31082 | -42.91867 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b605ef45-b13e-3f0e-b7c5-12012fb19e6a | -7.49595 | -42.13853 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6dd6ba5f-11ea-3e7e-a9f0-36f6dae55a93 | -5.40042 | -41.16956 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fa6d10bf-5577-3963-888b-3ef3b174c3b8 | -5.51903 | -46.47526 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf55dd89-60b2-3804-8a6b-3333f9520b0c | -6.1084 | -46.34558 | 2025-10-15 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d01335e8-5525-3e54-afab-59a5c3730b32 | -4.38445 | -41.98193 | 2025-10-15 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3747194c-097b-34c6-9d21-00fc67013e8a | -4.45877 | -44.36995 | 2025-10-15 04:06:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00daa8ef-8eb4-337d-84c6-71e2918e07c9 | -5.32164 | -42.91665 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86c7d083-f63a-3bc6-8594-690123a127c7 | -5.56247 | -42.98891 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2962c553-5fc9-33a6-adb9-f039a53c1519 | -6.34186 | -42.65982 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a42df91-af0a-34c2-8279-4b53be5cfb58 | -8.20994 | -44.01144 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f15aca71-1da9-3191-b3cf-e3ae8f5e0002 | -3.83722 | -44.54528 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a323eed6-3824-3403-812d-67d57954e40c | -5.61741 | -42.68969 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3d87bc3c-aa1a-3cae-990f-2b6864c9b506 | -4.36161 | -46.7817 | 2025-10-15 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e7ac898-42bb-3bb0-be06-b9e4999f3ab4 | -6.40497 | -42.56709 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 41f5027f-65d9-3cd7-ae01-caa3481cdb09 | -5.97541 | -42.80167 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 17fc4e94-3c39-33b2-9a76-fb04a5d0e2fb | -6.28478 | -43.90205 | 2025-10-15 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f3d3516-f6cb-38d3-943c-589fd6755add | -4.13743 | -42.20957 | 2025-10-15 04:06:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1cb015ea-437c-3a74-b2aa-48222495c18b | -4.13265 | -41.64339 | 2025-10-15 04:06:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0aca908a-f7d2-3cfb-95fc-26a4c046178f | -8.23863 | -43.33763 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a9b13641-14b9-3e84-8d26-82123becb613 | -7.03365 | -42.73708 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9cbec3cc-8286-3018-b973-14d00e8505cc | -5.82063 | -43.61018 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 801f5115-2ea0-350c-8ce3-11ee21b87af4 | -4.27606 | -44.36671 | 2025-10-15 04:06:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dcdca35-b390-3da3-acdc-f08a0c71d300 | -8.2849 | -43.42338 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40d29397-321c-33d3-a970-1980397eaa1c | -7.81679 | -42.10801 | 2025-10-15 04:06:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9b52d301-a870-351d-90d2-e04f72ea073d | -6.1821 | -41.72599 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67afd1eb-9447-3f06-8eef-488f8dbdd7dd | -3.94217 | -47.56638 | 2025-10-15 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31ee8ab3-823d-3878-afae-a5bc150d876f | -4.8965 | -43.45936 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 042ede5b-1a5f-31c4-8333-4db37617f628 | -3.76054 | -44.24268 | 2025-10-15 04:06:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd6a8ad7-e3de-3bf4-84ec-cd67f0c4bc3c | -5.14277 | -46.28047 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4267187e-8600-3ed5-b56c-1a98f2d76643 | -5.42991 | -41.34734 | 2025-10-15 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a3c66aab-83bc-3b2c-ab58-bda94e29450f | -6.32809 | -44.01403 | 2025-10-15 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62bbdb7a-dbe4-3e48-ba82-4d230a23a2f1 | -5.49585 | -43.78399 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4abc864b-8698-3f38-9fa2-c3c7a54addbf | -5.8823 | -42.79022 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| af53c2ba-db6b-3157-ab81-755e6e5eeaa0 | -5.1813 | -39.38373 | 2025-10-15 04:06:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b25b4c12-c5d0-3dcf-9395-fd44a7c84458 | -7.7447 | -42.45493 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cabb94f-a363-31ba-b25b-fc445063e671 | -5.42878 | -41.33304 | 2025-10-15 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f42a8b89-cdd7-3fc9-92af-d463802042a0 | -8.21817 | -44.09193 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3925a54f-697a-3d6a-9a73-3be43164618f | -6.1694 | -41.72043 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 98b7870a-959c-3f0d-a737-54e07b44e95d | -8.21731 | -43.31913 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5257d963-e753-3cf6-8eb5-b3a379c2f48f | -7.2587 | -44.91353 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 783b978a-e92a-3b1a-b024-258e711a0dd6 | -6.22773 | -44.16298 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be004abb-b86f-3ee8-bad2-fa4026f21b11 | -5.24374 | -44.4731 | 2025-10-15 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b50c0eb-145a-3867-af45-ffddb71c7b47 | -3.67262 | -45.22169 | 2025-10-15 04:06:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbc67f6e-d550-3318-a6e2-458f8a45c1b4 | -8.21531 | -44.0439 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d52040a3-c797-32de-a99c-291f66ba55ac | -7.51564 | -42.95015 | 2025-10-15 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
