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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31ad7e6a-64b0-374f-87b2-a90cf1daf92d | -11.38701 | -45.13215 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3a742de-2774-38df-8d83-1b11d4281df4 | -9.42535 | -51.58398 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05923581-f467-3b61-b01f-ac2f5fd5d141 | -16.35367 | -51.00195 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 410cc56f-a759-3678-90ad-596abea14e75 | -16.35712 | -51.0025 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff3d5e07-cc09-38f4-8bd3-81572ad0a66f | -9.15795 | -59.51512 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b5eee92d-b65c-308e-94c9-e5bf319127e6 | -12.69035 | -47.45611 | 2026-08-30 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 134d3748-5469-3abe-883a-1985d2054038 | -13.395 | -51.80352 | 2026-08-30 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a65a7a6-05c7-32fb-ae4d-0647a7ca33ed | -11.02976 | -57.22758 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bf3c2fb-2415-338e-b45c-9496c4c3324b | -10.74511 | -50.66241 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62c93c1a-dd0d-3d9f-b6a2-46b8a439b1f6 | -11.22523 | -54.00872 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a465f10-0fb4-3602-8757-ae95e0a72b17 | -10.94447 | -43.0293 | 2026-08-30 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01411bfa-b131-3d36-8953-a6ef10f95df1 | -10.56481 | -46.17089 | 2026-08-30 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7958fe71-15c9-38dd-8967-e70082f7673d | -10.56089 | -46.17398 | 2026-08-30 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4bfa3de-a144-364d-ba42-5d9c77f3ec42 | -15.49201 | -42.85616 | 2026-08-30 04:34:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25db4215-1839-3476-8adb-556f024e4023 | -15.13496 | -50.62889 | 2026-08-30 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 9774e168-1dd2-3708-a4b3-f4f93b1510a5 | -11.34338 | -45.16139 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8a7f5b51-59fc-3736-a4f3-b006ebb2a5fd | -11.25654 | -45.0649 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04a6bbe7-522d-3253-8f01-a22853fabf2a | -11.78876 | -51.0572 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7f73f7e-58df-36a2-bd20-6a240f78fb98 | -11.29301 | -54.03507 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9365b642-b87f-34ca-9375-38ddadb70828 | -11.79384 | -51.04926 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| f31224a4-10e4-3454-9d1a-691f2c4b52e6 | -15.13303 | -50.64049 | 2026-08-30 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37ffe29b-db9f-3f98-9777-b00a4a1306cc | -11.03796 | -57.21444 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e0fd2eb-cf88-30fe-a230-1c563cd67433 | -11.62974 | -54.59017 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 934622cf-d274-33e1-83cc-01b6abe08d5b | -9.93374 | -60.5228 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7c427b23-2d7a-3611-ab6a-c7750251a9cd | -11.82139 | -51.04401 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 5e5cd6c3-09cd-3b73-ad00-62a26485b4b4 | -11.36084 | -45.16399 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3ddbe42c-6604-321d-aaf3-f390b59b92ca | -14.19674 | -52.87352 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2e3bbb2d-4032-367a-b3e0-971c82a941a1 | -9.1604 | -58.31133 | 2026-08-30 04:34:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 962b9a9c-e8f9-3a3d-8a7f-83802e24be5e | -9.16401 | -59.51906 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3454c179-2288-3474-8ab1-d7698936c818 | -15.13023 | -50.636 | 2026-08-30 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8711920d-29a1-3c47-a142-cbeb624f8c2e | -14.4362 | -58.44426 | 2026-08-30 04:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53fe02e9-261d-3e29-ad6f-4ef13cce471d | -12.80017 | -46.45699 | 2026-08-30 04:34:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47e2f2cf-c666-35a9-b3b3-24d3a28aeada | -11.34509 | -45.14977 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31c4ae44-6959-3853-bbb0-44400f2d5dd5 | -9.42147 | -51.58337 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c83e1d89-ab5c-30c6-83c1-f997c247feda | -12.90138 | -45.87868 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0351aad-af81-334e-9080-6c1e1ec6d407 | -7.23139 | -60.62677 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4b26fc1-5799-3699-89c8-0889b5840860 | -14.15607 | -52.80908 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b21dcf77-9a4c-3814-8697-a9e194437760 | -9.93378 | -60.51601 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5ce57e1f-ada1-3111-b709-85d54a1f3f4f | -17.41918 | -42.63164 | 2026-08-30 04:34:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 0ae03fb8-c1e2-3b27-8980-8e0c89520156 | -11.04271 | -57.21906 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cac8414e-25e9-3336-9ab7-4bb662837a71 | -14.76343 | -48.7347 | 2026-08-30 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b203a372-452a-38ea-8cba-501b8b2ef530 | -11.15977 | -50.58682 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a5f9da4-a0c6-3c73-aeb6-575dd24360ae | -15.4038 | -52.68198 | 2026-08-30 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fb5af6b-d6a8-3419-8a44-9c8d7cb06de5 | -8.50455 | -55.2888 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c34eed4-ee66-33ea-b2e8-1241d5e92c6b | -9.93244 | -60.52915 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1ff17df5-202d-3e01-8c14-ffb7f6e9c17d | -11.80182 | -51.04625 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 18f93be8-a2c7-3b2a-85c9-c55190de1014 | -17.27818 | -46.00938 | 2026-08-30 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 482abb72-c3aa-3976-8e32-8e1516c67e2b | -16.33718 | -43.44376 | 2026-08-30 04:34:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 838e08ba-737a-3150-bf63-a60dd93b3858 | -11.51465 | -45.53899 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f09d67e-5ef7-3948-a296-abb31ceabdbb | -10.81594 | -45.32613 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2cf242d0-4ba9-3cca-af32-f08a555132c2 | -10.7362 | -54.03964 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a2b780a5-c444-32c1-9241-b577b7439ed6 | -11.2725 | -45.33921 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff25d52b-d5d0-3714-864e-625051b0850f | -11.33988 | -45.16088 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6945940-9d77-3db9-b566-1da630f6ce89 | -11.19362 | -45.04762 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 175de367-02c3-3557-9374-ddd0e21d1339 | -10.0576 | -48.68616 | 2026-08-30 04:34:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55182aa8-6cd0-3e19-8a0d-9df32b1097bc | -12.38235 | -48.18006 | 2026-08-30 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee322d12-8644-3fea-969c-851e5c5b1f97 | -14.4333 | -52.5628 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5fea4aba-97a2-3f01-b8c1-00ed5911f7a5 | -10.75182 | -50.86847 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a09d9697-78db-37ce-9c94-f76d93686b6f | -14.47635 | -52.14238 | 2026-08-30 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31b975d5-bbd6-38e1-8b37-02d90dc97e84 | -11.61365 | -46.72055 | 2026-08-30 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cce8a7f-bd0c-3ee7-95b6-7c6284330405 | -16.33968 | -50.97952 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c578be48-4a3f-3e0c-bf4f-6176b9bf8a61 | -11.23911 | -54.00706 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 41bccae0-cca8-30b5-b36c-06d395804dec | -9.16508 | -59.51351 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d775699c-0210-39d7-b019-e2de6de68d24 | -14.93857 | -56.3353 | 2026-08-30 04:34:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a869b483-7d32-3142-8519-8272ff28a46c | -12.08272 | -47.1956 | 2026-08-30 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d10bb6ad-ca0b-3cfd-971a-595dba97befb | -9.12364 | -50.58267 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf67600c-97f9-3af9-a1b3-5429d9249b4c | -14.20232 | -52.86457 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 851e7036-671a-3556-af71-f649781935b7 | -14.24599 | -54.67932 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 111f1a1f-4269-34a6-bce6-b452231a7497 | -14.44662 | -58.47865 | 2026-08-30 04:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82ca5279-9554-37e1-a710-5069144f7715 | -9.8907 | -60.27714 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5323c872-b770-326c-af51-07db32e99a23 | -10.75399 | -50.87771 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f9378a7-fd00-3601-9a21-c90364cb3784 | -16.36272 | -51.01152 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 000a0bc8-2da2-30f4-a67e-dcd5918c9c53 | -11.20873 | -45.06624 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08e4fc37-c4e0-3471-b948-4c7a6c241c0a | -10.95542 | -43.03593 | 2026-08-30 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| aa5ab3cf-b56b-3de9-afb4-c64993a123a9 | -14.45646 | -58.47975 | 2026-08-30 04:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a670d04f-8b7d-35e9-a936-f444946b99da | -10.77001 | -44.88534 | 2026-08-30 04:34:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b1c9961-b877-310c-ace1-e69bccf84449 | -7.23842 | -60.62856 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 567c75eb-8677-3837-bc5e-131672d40e78 | -14.20635 | -52.86741 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d52d467e-9c9d-3ca8-9cf6-93aa83ac8d29 | -11.24067 | -53.9984 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdbc34dd-508c-3eef-a63c-591110a0b14a | -9.66168 | -50.84175 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69e9e210-9b97-33cd-b38f-b834060244a8 | -9.88832 | -60.28891 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6d49bd3f-11a9-3ccc-8f85-6d753f12424b | -10.81651 | -45.32232 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 56275f67-d8e3-3278-88d2-7a9e183b76a3 | -16.73754 | -48.44732 | 2026-08-30 04:34:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30d56904-18ef-3368-ac8a-832b38f2e4a3 | -11.03309 | -57.23953 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41661a9d-3e5c-377b-af77-c6e47199746f | -11.18186 | -55.10772 | 2026-08-30 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ec65247-ba18-39e2-9d52-38d5e15543eb | -14.16768 | -52.81125 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c277156-6c4e-3065-a96b-3b218edc28cd | -13.39717 | -51.81311 | 2026-08-30 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26db5571-5986-3dac-bece-1667649e0f5e | -15.01954 | -49.90364 | 2026-08-30 04:34:00 | NOAA-20 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2812289f-d9f5-3108-8a27-d3961d69fad8 | -10.7542 | -54.05896 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cce31a09-5337-3e31-b347-6dca53c6ad36 | -9.84577 | -60.27802 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a1050ab-6fc4-34bc-a1fd-c39dfa32998e | -10.53814 | -50.77782 | 2026-08-30 04:34:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e36814e3-6769-348d-99b0-c79b73a9ae48 | -15.33565 | -43.67267 | 2026-08-30 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9797fae3-a96a-3515-b110-cdeeba8535b1 | -10.81259 | -50.51404 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dca2f5fc-595e-3817-8d25-e8b52f6f5bea | -10.4888 | -59.60957 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b6ca1f1-e769-3a5c-92e8-7d9cd2b66300 | -12.80356 | -46.45745 | 2026-08-30 04:34:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 679f29a0-32d4-3b25-9dc1-766f857cbc27 | -11.34916 | -45.14647 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58f9c703-7d43-318e-a9b6-335933838c75 | -10.48773 | -59.61492 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 142719e0-b6bb-3fce-8e04-df6552b773ca | -11.2414 | -45.09474 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3fbd058f-9faa-3467-bad8-869229835d67 | -11.33965 | -45.1545 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 878fd19a-24c3-37b0-beb6-aac373cd9b61 | -11.36316 | -45.17241 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |


[Clique aqui para ver as próximas entradas](README42.md)
