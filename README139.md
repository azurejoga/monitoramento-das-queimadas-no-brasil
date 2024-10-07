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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d9a9faa-37f8-3c0f-95b3-df2e3c94ea93 | -16.62886 | -57.131 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a42a4f8c-c678-3d60-9121-5a67440a7801 | -16.62843 | -57.1351 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 56a54d64-899d-3036-8e84-0ef2dced85dd | -16.62801 | -57.13917 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 44f124f0-905b-3b4c-b0eb-67fa5fc396fc | -16.62758 | -57.14324 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1bad1d9c-047a-3141-9bdc-5b7f80b38885 | -16.62716 | -57.14731 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e9f0755c-906f-3f7c-aa87-ca3ca036f32a | -16.62674 | -57.15136 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 792323df-f827-3ad7-b61b-0a930a916c7d | -16.62672 | -57.13337 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 49644401-0ed5-3012-8bcb-c767aa39cbd3 | -16.62631 | -57.15541 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8d22b2ed-4da9-381b-92a0-fccfbe73a8ae | -16.62626 | -57.13745 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6fddd170-a653-336e-91bd-2036bfaa4493 | -16.62581 | -57.14151 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e00de32e-9247-30f9-b800-61105f448f39 | -16.62536 | -57.14557 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c98fb543-e82a-3671-8d16-19dfa24bfc8f | -16.62491 | -57.14961 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b945eab3-6cf9-3213-9ad7-f974fc225f40 | -16.62446 | -57.15366 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 28899d2e-e974-3327-9b79-cccc2519d1c1 | -16.62229 | -57.13849 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| cbe667af-8b06-3189-a689-3ed33c60e390 | -16.62187 | -57.14256 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| dd5578ab-ca7f-30a7-8c0b-2baafc9598eb | -16.62144 | -57.14663 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cb962ed5-2d77-3435-a331-56b2bc4ba0cd | -16.62103 | -57.15068 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9248890b-ab8e-351b-bda8-e878f54b37d1 | -16.6206 | -57.15473 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6c44fe2f-784f-32c0-858e-3187c768c64e | -16.62009 | -57.14084 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 72e19146-8b92-3849-9d80-5342904bdba1 | -16.61964 | -57.14491 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e7a8fbff-5283-3284-b7e3-5536351d267d | -17.84026 | -53.79158 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 935129cf-fa55-300b-98ea-ddda20e47ff0 | -17.83309 | -53.792 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7a8071e9-8cae-3a24-9299-377f556b0846 | -17.77254 | -53.77866 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2bb380fe-b49e-32d9-be88-5f96010c9f8a | -18.46694 | -53.51497 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 880192b7-d5e0-3a3f-989e-3dd2c72ad4d5 | -18.46644 | -53.52125 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2ef07d3d-7aef-34c5-87c6-9b5cf3f20858 | -18.46086 | -53.50006 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 745858e2-418a-3c41-9dd0-de423c2938d7 | -18.46034 | -53.50654 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b63bfe94-308a-3ac3-8460-8c11ba1f8479 | -18.4598 | -53.51326 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5816df47-6c36-3578-b663-2736947afcbe | -18.45925 | -53.52008 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3009059a-e7c0-3dcc-a996-6ea04b64cae2 | -18.45816 | -53.50524 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6ba72ea5-ccf7-38b4-b56c-0fe315d44df6 | -18.45757 | -53.51197 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| de1be1f7-897b-3bdf-ae6e-4f24b8f23200 | -18.45697 | -53.51892 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 10b1a4a8-72e6-3a03-9e4e-f1fa30a2a362 | -18.45366 | -53.49887 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 08d24757-0a5a-347f-84a4-d9969a72707d | -18.45319 | -53.50483 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5e703acb-4baf-312a-b2bd-c734b2356a1c | -18.45263 | -53.51181 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c8d53ac4-b493-39f5-9dd7-a51af0728466 | -18.45098 | -53.50397 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9662aa5f-c7f3-3824-b32c-a6ab4a9354ab | -18.45037 | -53.51097 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bae2a48f-8953-3fb1-b1f7-cf001bbf19ea | -18.44537 | -53.51146 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b6f2b9a-8095-3655-8157-3fa3ac8f3ff1 | -18.44314 | -53.51043 | 2024-10-07 05:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 23e6183d-1e2e-3be1-b5df-41c6fa906f35 | -16.49478 | -53.95713 | 2024-10-07 05:44:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39c3a5c5-8097-316a-8e8e-a53e631b2e1a | -16.49427 | -53.9626 | 2024-10-07 05:44:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9acf1485-8693-3b73-8cc1-401388677184 | -16.48729 | -53.96252 | 2024-10-07 05:44:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93ccd007-ab3d-3c63-9357-a25c63b45d3e | -16.4872 | -53.96391 | 2024-10-07 05:44:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6322777-a298-3f3a-8b4e-690f937f1d02 | -16.48669 | -53.96882 | 2024-10-07 05:44:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e158ee9-b84a-3839-9344-48d7e831ee48 | -16.48083 | -53.95698 | 2024-10-07 05:44:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15e39c40-620e-3b71-941f-2df07c919257 | -16.48033 | -53.96229 | 2024-10-07 05:44:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c9fb1d9-5a54-309e-a063-0db6316c4d6c | -16.48024 | -53.96364 | 2024-10-07 05:44:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bf80a4c-0b9a-3e48-9d49-6c67c6ee6b5b | -16.45901 | -53.96622 | 2024-10-07 05:44:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9bca4336-db4d-3aae-8931-09802c80b88f | -16.45845 | -53.97216 | 2024-10-07 05:44:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 713a2416-dbed-3408-9527-90752ba64ea6 | -17.83978 | -53.79715 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 86af8728-d350-3f19-ab06-3a1089124ddc | -17.83916 | -53.80428 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9365407d-0dec-37a7-a675-619bc88f6baa | -17.83266 | -53.79692 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 66bb3f20-3c9d-315d-9ff1-47e8271580a6 | -17.8321 | -53.80346 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5b52656b-80ba-3305-ae72-19a96aa818d3 | -17.82555 | -53.79666 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 77d3f6cd-a1b0-3158-bfdc-f9e3148f3370 | -17.79611 | -53.80735 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c6e3c0af-ff49-35b4-9eb9-f9279b127f16 | -17.79317 | -53.78731 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7b2a6820-b81e-36bc-96be-7343b301701d | -17.7926 | -53.79364 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9eb2e742-c1d7-31ec-948f-edd92bffc6b9 | -17.79205 | -53.79976 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf4f2d41-4a16-3bb8-acbd-2f0c0abcf864 | -17.7915 | -53.80596 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1a0bbff3-5f0a-3a4e-ba45-e9977bdc1559 | -17.79089 | -53.81267 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 73a315c2-09e9-3d87-b230-3d6c4d1a03d0 | -17.79052 | -53.78907 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 321e0ce1-d9b8-3ff5-9002-9b78da69798b | -17.79027 | -53.81954 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f7886a4-ea65-31ae-b448-f7b456d7362b | -17.79003 | -53.79494 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 47c8eb5d-2c94-38c6-83a7-2a440ec3e8a8 | -17.78954 | -53.80069 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7ea68840-4ada-39a3-9d47-7396135cd99f | -17.78903 | -53.80676 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6e9a468d-1030-3af2-81c7-3789f403f36f | -17.78847 | -53.81349 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 41e10678-ae07-3e40-99b8-37f5113dc488 | -17.7879 | -53.82033 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a1f67c12-8358-3be6-a8c3-31aa0dcb968d | -17.78491 | -53.79986 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 340a0d79-a533-3731-a4f8-34d544fb1c5b | -17.78438 | -53.80575 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b4e3e1d9-d1b7-337d-9958-c6141a2430d1 | -17.78381 | -53.81219 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f8f4c3bc-5f5a-38fd-b22b-cbec8ccfa61f | -17.7832 | -53.81895 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dc7ca18d-128c-3957-9ef4-a33a3fc0d9b0 | -17.78242 | -53.80061 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c71f5686-cc82-30b9-bc00-9038c0418363 | -17.78191 | -53.8067 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3f74f089-b881-324d-9388-2b7d7d4d6f84 | -17.78139 | -53.81298 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| feb6be3e-e356-3139-9f9c-61b149bf886a | -17.78082 | -53.81978 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b2f253b7-4313-322d-9932-f2bbd664dae0 | -17.77782 | -53.79943 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ce196a97-e44b-30b7-b945-10a68c6342de | -17.77727 | -53.80556 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ecbfd8d4-cf7a-3e7a-ba76-140cd3e77bd7 | -17.77672 | -53.81171 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b945abb-9d20-30c6-abfb-fd7aedc4f7d4 | -17.77638 | -53.78745 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c1c08c73-8081-3bc6-922f-67a7459d3433 | -17.77612 | -53.81846 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcc50772-da28-3803-b5e6-a40e87daeb79 | -17.77586 | -53.79376 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6af6802f-75f2-3310-883f-f8efc66b7087 | -17.77535 | -53.79993 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 202c4f7a-c8aa-31fe-994d-7537095f9980 | -17.77484 | -53.80602 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5b60914b-f8ec-32ab-b80c-475b1efd4ddf | -17.77194 | -53.78529 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1fcc012c-65ab-364e-8da8-a9a244cf2b78 | -17.77133 | -53.79219 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e35479fc-4aa1-3187-97b3-9757d6129f16 | -17.77076 | -53.79865 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2974c16e-0716-342d-a56d-0b4ca2ae2cea | -17.76993 | -53.77922 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 569b7559-0107-3307-ba75-bd3042b6f989 | -17.76937 | -53.78603 | 2024-10-07 05:44:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8bd4fc89-0343-3bd6-97a3-5cfb225165cd | -17.18043 | -53.92945 | 2024-10-07 05:44:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5abdbbc-9ca1-32c6-9cd2-0473b989aa82 | -17.17349 | -53.92828 | 2024-10-07 05:44:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34f58f5b-1eaa-3d34-8fde-ce55c775dcff | -17.17293 | -53.93469 | 2024-10-07 05:44:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e16090c-ea9f-31c5-a8b0-51277f7c5374 | -17.16656 | -53.9271 | 2024-10-07 05:44:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d7c5aef-ce72-3c83-bc71-67ea13d03c53 | -17.16539 | -53.94033 | 2024-10-07 05:44:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e86b72f-e2c5-320c-a778-8849c402d49f | -17.32777 | -55.04547 | 2024-10-07 05:44:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 91a92584-7f83-3f5f-92c9-67995988e5d6 | -17.32682 | -55.04332 | 2024-10-07 05:44:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 90ba51f8-f430-3a14-b819-f730564feb3f | -17.32176 | -55.03904 | 2024-10-07 05:44:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c77703fb-e89a-39d1-8424-266c6d87175d | -17.32121 | -55.04479 | 2024-10-07 05:44:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4fbd599e-fa8b-3bee-bb62-df8993a746fa | -17.03007 | -55.06721 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 65f27582-6e58-35a6-8f2d-8969d6ddfc3d | -17.02962 | -55.06943 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e3691ad6-237d-367a-8ab8-5aa90c68caf9 | -17.02951 | -55.07283 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README140.md)
