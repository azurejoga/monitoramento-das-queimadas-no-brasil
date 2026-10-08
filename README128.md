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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afb44340-9845-3227-af88-9ef3ebcf607f | -3.08991 | -53.93586 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a382e88a-091c-3e93-b618-e8560ef379f6 | -8.71968 | -45.18799 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ecd47596-d49a-3109-835b-88b2a665e561 | -6.95257 | -45.27018 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83e6552a-86ef-3407-b453-76e885911d6f | -2.84247 | -54.13363 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9854770d-cd35-3978-81fa-9fd544eaaf9a | -4.92049 | -55.855 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e8a7448-8bf6-33be-bb74-8eb729f3c72c | -2.05281 | -56.38664 | 2026-10-08 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 465947cd-76cd-304a-b9fd-66f618e7ccd4 | -3.20934 | -50.55753 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8082debe-566e-3ecf-bce9-55fd55806db5 | -1.21675 | -55.64279 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10734fe7-5d74-3cd1-9431-589607da0eba | -3.28736 | -54.03259 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1d5a956-1094-3d34-8559-0afed6c43e94 | -3.01913 | -54.08875 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 87ac68eb-8c44-3f1d-92ba-3c428d0886e0 | -4.28993 | -49.09369 | 2026-10-08 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce99f768-a1be-33da-a346-f025e641dd89 | -2.89399 | -54.08139 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c185ccb4-c139-312a-b50d-5246e398ec3a | -3.9566 | -56.11491 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ea14c22-9a60-3e71-aeab-f01445966c82 | -4.06141 | -54.03662 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f630b45-bacd-3c37-a1cb-cc9816e69e2c | -3.52617 | -54.66542 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a204c0e-392f-3fa2-9c60-e43d7386d7ee | -2.47909 | -56.10702 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e59b8d0c-a796-3552-8f49-0e994355d8b5 | -3.29802 | -61.01271 | 2026-10-08 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b080555-dbb7-3094-8c3e-19e4addf6466 | -3.26086 | -54.04047 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a4a31a6a-4684-3257-b9bc-1c4c3199caee | -3.00479 | -54.76049 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdf8a454-5f77-3ade-a881-21cd2b135c64 | -3.05759 | -54.20918 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 602f2383-628f-3c02-95d3-8ab940b2a62d | -2.76358 | -54.08284 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80429848-9b82-3207-9b78-c55fbc550d00 | -4.37395 | -54.75453 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5e43beb-074f-36bc-9850-3e567295d149 | -2.87876 | -54.87637 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6042a4d5-2cf9-33b2-b2ae-948196ce9f78 | -3.97516 | -56.12131 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d0b7499-cd17-3e47-a164-704af551c99d | -3.0985 | -53.742 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bdc8da0-db0e-3706-9286-7fc9f77e7cc9 | -3.12684 | -53.70113 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31ac5402-1a00-3511-88a6-dc6f78856aa5 | -3.10637 | -54.1524 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6b84546-4aeb-3bd5-899b-fddb9b5ddb0a | -3.54422 | -54.65621 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f600f703-25e8-3aa9-b779-14535b1e3291 | -3.01151 | -54.09153 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 2217a043-a16c-3711-96a9-0af6283158dd | -3.76446 | -51.33337 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 252666b0-871c-3620-b5ba-203128b32e5f | -3.21372 | -57.87048 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ef9ec02-28d5-35fc-9a9f-5f13fefe9640 | -3.01382 | -54.0998 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 5daed62e-ac15-3e4d-9a30-9e9abf65fcda | -3.28418 | -57.84845 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70060ec1-cfe6-3792-923d-a827e0a83978 | -2.99107 | -54.08437 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 98d1b5c6-0d16-319f-9fa5-98f6826038e9 | -9.54435 | -64.81289 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f592f49-2ac3-3024-a2c6-49370dc6512e | -3.30272 | -53.86522 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d6c5261-df58-37cc-a5cb-9c6507c69275 | -3.30092 | -54.67692 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c65c6bfd-ab99-3960-ae61-32351b16a937 | -3.67431 | -59.63363 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 051afa2d-c1b3-393c-91f0-9fd1526de533 | -2.95343 | -54.11429 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2a4a932-1cc0-3eab-9677-664c2d0d4100 | -3.08589 | -58.01661 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e228e08-501f-3eaa-b797-131b3e587edd | -2.84307 | -54.12979 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59e863c7-c631-3a00-8124-de2df28d6d60 | -11.02311 | -65.21078 | 2026-10-08 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53d704a0-3ee0-31ca-895d-f7da45ce1480 | -3.27127 | -54.06612 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f528076-b35a-3cd2-bdb0-dd2b1b0d4dc3 | -6.89307 | -43.68332 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fd4e3ab-f5e2-3fa8-a7b7-37142001df7a | -3.00519 | -54.06276 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 794dce45-5291-329a-8fbb-cde072d90ac3 | -3.96405 | -56.12671 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f708330b-189b-3e1a-ad56-9d8f0127fa35 | -4.84098 | -55.84628 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e548c3af-9687-3f93-8967-aa524d0d601e | -6.24194 | -52.8754 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7dd0984-be15-3d71-ab12-262fb5ba7895 | -2.7663 | -54.11082 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a0d43302-79b0-3f23-9ed4-58ae3c12a181 | -3.62091 | -55.28171 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c13fc483-d041-3f31-b40e-6f820d5de388 | -3.72154 | -54.22799 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b42f255-2933-3d69-a58f-de1a03e320d8 | -3.02012 | -54.12849 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72e2445a-4aa9-3ca1-8d97-5407dd18199f | -3.2639 | -54.02095 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| a0d36422-8128-3a66-9fef-d6e728203301 | -3.81374 | -52.19847 | 2026-10-08 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f861bd8-6bfa-3661-8db3-7367076b19bc | -3.43328 | -56.93741 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c3b3b72-8672-3eb6-88ed-079dd4298a58 | -3.01262 | -54.10753 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 32d37584-8e43-3c58-84bd-58576c75e523 | -3.06169 | -54.20589 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54fc4d83-033a-37bc-a990-a11dcc72674b | -10.72097 | -56.04683 | 2026-10-08 05:23:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad99b6d6-6d60-32d8-b175-905431328824 | -7.22826 | -55.12516 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9c1eae2-f368-309b-92b8-790418764baf | -4.35063 | -43.79395 | 2026-10-08 05:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3050395d-ec45-36a2-9ad1-cd7d153d03b5 | -3.5118 | -54.66701 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9ec0edd-8677-39ce-b2d4-360f2b07208a | -2.76684 | -54.09036 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a1f267b-3f7e-3752-b495-62752ed9abec | -2.39759 | -57.23411 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df138987-fbab-34ba-8f1b-93a8b49078cc | -4.75337 | -55.65105 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e5e05e3a-33a4-3589-9b71-fc5ac8efe8d9 | -3.75032 | -60.59392 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5f6f335-c1a9-3bc0-b713-910e9219ab15 | -2.79783 | -54.07542 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0046197a-148a-3d16-80ac-1e68a7b507bc | -3.24861 | -46.95962 | 2026-10-08 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4fbfb0e-9822-3f51-9406-ba9a0af4787e | -3.2044 | -50.56095 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 86b15d17-8007-36be-862e-78a8707680c4 | -3.31722 | -54.04924 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 46fb68d4-3fd7-3091-9d4d-8d9afd10f283 | -11.78499 | -46.78165 | 2026-10-08 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cb430d5b-316c-3f94-8b5d-f24ba97f2974 | -3.72454 | -55.97534 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abcbe77f-1b7c-3272-b0ec-4fd46c94e547 | -2.98972 | -54.13955 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83574e6e-3f29-35b8-8efe-8c06970eb60d | -3.0488 | -54.2196 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f8e5cb4-995c-3436-935b-442c11e290c3 | -10.61791 | -60.48629 | 2026-10-08 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5e0ad16-9e44-309b-89f5-2cd4cdf33969 | -2.49076 | -56.11947 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e04df8d7-fe3f-3a00-8b60-aec8db4c849b | -3.68387 | -55.95107 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51915c78-9a2d-37cf-a3d0-1def374710a2 | -6.24097 | -52.85528 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00ae5bcb-78e5-3ae1-9a2c-0bf4553273ab | -3.63855 | -58.93945 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50a1daee-58f0-35a3-9892-b16a59875b52 | -8.62268 | -66.9998 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5b99ae3-5499-3566-b66b-efcb4cc959ba | -2.96844 | -56.62645 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eca4f298-0ea8-32a1-8190-4e27dd4198a0 | -3.01095 | -50.47232 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b7ce39e-68dc-3426-a703-8e0f9fd3df08 | -3.02214 | -54.06937 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c17f9fc7-3bb3-34cf-967d-8231d2b50d7b | -3.84816 | -51.92624 | 2026-10-08 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b6c704c-b579-3285-b40c-b3683e856895 | -3.63414 | -55.51394 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a1195e0c-6e15-3e21-8ffc-995c81c38b1d | -1.22841 | -54.12182 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7cd3f9a-86ea-3c13-9f3c-300c7bf48995 | -2.93976 | -54.1556 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bb1c2e2-91d6-3bba-b7fa-325be7687d35 | -3.27985 | -54.01138 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a4dd0ee-27b4-3c6b-b291-c8a5fdb6c1bb | -5.23933 | -50.90833 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f058208-f04e-3ac1-abf6-ae11b8040fac | -3.11005 | -53.78473 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6fa37b23-8634-3178-a9d0-b5acbb202a38 | -4.80446 | -54.67766 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63b904d2-b60c-326a-a7fa-16887d26afff | -3.07283 | -54.25359 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7198db2e-d1d2-3e4b-ab11-786538e470fa | -5.7022 | -53.49464 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76a782bc-e4a9-39f1-9fc8-80bc75ec249e | -2.9438 | -54.06135 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfabde89-90b3-302e-a728-7303d2cc775c | -3.28137 | -54.04772 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccd1f4ce-63f2-300a-bc0a-0749690a18ba | -7.21879 | -55.16332 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c11cd91-7fce-395f-a4c4-30cc1a720c9a | -5.70058 | -53.48007 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 323b515d-b725-3d36-82bf-f692cb035565 | -3.1939 | -50.56519 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f07e6eac-c926-3bc5-982d-f661abf561eb | -2.99808 | -54.08546 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 679f7da5-a9ed-31e7-9bec-f7b943c82321 | -7.23214 | -55.1694 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 44c18818-594f-3403-a9d3-df1d56df4c88 | -3.05091 | -53.95396 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |


[Clique aqui para ver as próximas entradas](README129.md)
