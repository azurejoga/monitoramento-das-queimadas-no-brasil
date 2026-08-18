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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df09287f-8a25-3d0c-802b-960ee65db98d | -7.61699 | -55.63139 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b0e11a1b-cb80-3ec1-af7c-5d8c01359de2 | -10.41429 | -61.21172 | 2026-08-18 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a457fb8b-a894-3285-a297-5d1131adce15 | -8.95723 | -60.52159 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ea81578-13f6-3b67-8712-fc8cea002791 | -8.73249 | -62.89814 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 513c21df-5903-3de0-88ee-82cf321e021c | -7.60484 | -60.82811 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 81fc6227-ad49-33e6-961b-d615a50e2f83 | -9.42884 | -60.44981 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0fa298db-ba0e-38bc-9d8f-a11f28b1de00 | -12.46846 | -54.18617 | 2026-08-18 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a951f11b-f88f-34f1-932a-b3fb72de3d18 | -7.6117 | -60.94962 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c6d3745-13d1-3253-b339-cbab22a02c96 | -7.4582 | -59.99762 | 2026-08-18 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31a7ffb3-0f5b-37cb-a68c-28f72eff3e8c | -8.57692 | -54.71568 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 9deb32cc-ecbc-3bf5-b9d8-cd8999db3ff3 | -9.83265 | -55.16041 | 2026-08-18 05:44:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92f23b9b-13df-3463-a56a-070bfb66d5d9 | -8.59092 | -54.703 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2bb8367-c6cc-3516-b0ed-318fcd984e46 | -7.61491 | -60.95532 | 2026-08-18 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b396fc80-335b-3e3c-876e-a1c512ce63da | -8.89976 | -60.55219 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25358334-e750-3d7e-968c-0ea0076ffc6f | -8.95618 | -60.5291 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2a412e0-3420-3ddf-8a6b-cffd8ac3dc34 | -10.41025 | -61.21115 | 2026-08-18 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4192bf1-302d-3c37-8bba-426c42d1780c | -9.18455 | -56.9894 | 2026-08-18 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 01d307f5-5fbf-334a-9a71-da998a22a9b5 | -7.91564 | -61.73376 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c4f9f217-5610-3ac9-9e84-4115cf4ff1c3 | -8.57203 | -54.70551 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a5a22727-a9fd-3123-94e2-9f1ce5510644 | -12.46906 | -54.18035 | 2026-08-18 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b764b0e7-e517-3355-bff7-0060d67902d3 | -8.21734 | -55.02996 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 072e5cbf-5ec5-3794-8734-67346c066311 | -8.56105 | -54.69443 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8340a063-7bf6-3e72-8747-11f8916377ad | -8.21623 | -55.03854 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6b0e8835-eb5e-3ba7-a108-bb7fe4e493fe | -9.83682 | -65.06342 | 2026-08-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f35cb4e6-1c91-3fd6-b7c0-88aa63b45eb8 | -7.88474 | -63.76844 | 2026-08-18 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 880b16a7-4986-3861-af27-68182695187a | -13.02014 | -56.58538 | 2026-08-18 05:44:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aee54105-3506-32b1-bafc-bc29e4c0cbec | -9.83792 | -65.05627 | 2026-08-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d7554ff-4568-39c2-9de8-b73a7b4833d1 | -10.57796 | -63.5266 | 2026-08-18 05:44:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14b0cbe3-e28d-3507-a053-5cd4e9e3b1c6 | -9.20097 | -60.88932 | 2026-08-18 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77ebe6e4-006a-3738-a5f7-03af686321ca | -15.23229 | -57.65897 | 2026-08-18 05:46:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a4295a7-f691-30aa-b395-c50074c5bbbb | -16.25138 | -57.65548 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ae3cdebd-bff4-3caa-aaab-b0ce8cc86c1d | -16.25068 | -57.65669 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3812ba3e-86c0-3199-9c9d-f457d9771e58 | -15.89147 | -55.55205 | 2026-08-18 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58b8c0d8-9c00-35d2-abb7-01a993e91395 | -16.23363 | -57.6583 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b9f4b57f-6d88-3571-9de7-33df16dd2427 | -15.78421 | -55.56841 | 2026-08-18 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1af03953-11a7-37c9-9e2d-986c9d240bc7 | -22.07377 | -55.9886 | 2026-08-18 05:46:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78360c8f-c56a-30c1-ad56-c3901b5d4fc6 | -16.21771 | -57.65451 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 172ec70b-8b45-32c1-a358-f80bb7322954 | -15.29416 | -56.44495 | 2026-08-18 05:46:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6e007b1-fa0c-3500-801b-645ecc1bfbd1 | -15.29964 | -56.4498 | 2026-08-18 05:46:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 476c2493-46af-3638-be89-b50dde59e3dd | -15.27129 | -56.49005 | 2026-08-18 05:46:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d03038b3-e7d4-37cb-9041-e075291173c5 | -15.22802 | -57.64743 | 2026-08-18 05:46:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bcd40a7-d226-392b-bdcc-53f1b872b309 | -16.22323 | -57.65547 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ff33488d-468e-35fa-bed7-e2cdfcb36d53 | -17.34529 | -54.93509 | 2026-08-18 05:46:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6ae556e-8f69-3fae-a3ed-e671812fa9b2 | -16.24509 | -57.65633 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| eb17ab50-84e7-3db6-b3e0-6ab25953ff50 | -15.24812 | -56.4826 | 2026-08-18 05:46:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1af3ac71-17a7-32b7-be21-6900d7fb4b9e | -17.33905 | -54.92997 | 2026-08-18 05:46:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63ae36d6-4fc8-3b35-aafb-6ecbd52a8151 | -15.22761 | -57.65105 | 2026-08-18 05:46:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 971ada6c-2ea8-3833-adf2-d1fc6c11f8fd | -22.07288 | -55.98946 | 2026-08-18 05:46:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7c891e71-fc99-3c0a-b5bb-c07f15ba9f3f | -15.88474 | -55.55551 | 2026-08-18 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8acaced-f029-3560-9028-cd65683370c8 | -16.2339 | -57.66074 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| de5ce4ed-b408-33c3-89c0-d5e8918aec0a | -15.24406 | -56.46428 | 2026-08-18 05:46:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee1dab8d-0705-3afe-a0a2-8ae83887900d | -15.2937 | -56.44914 | 2026-08-18 05:46:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca9854ce-1812-3f5e-9041-f5c1938d10da | -15.29758 | -56.44994 | 2026-08-18 05:46:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e3b7b51-129f-35ef-bd47-45da11689b1a | -15.78462 | -55.56437 | 2026-08-18 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03c42a99-9b38-3a25-b660-168d3ea92ce0 | -16.24473 | -57.65974 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 391f943c-7362-34ab-abbd-3c321fe3955f | -16.22284 | -57.65909 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2dda9f9b-2408-3b2b-8d11-6f0c9c0cc332 | -22.06721 | -55.98799 | 2026-08-18 05:46:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74b553cb-2d63-3444-9636-1c7d8af5200c | -22.07252 | -55.99454 | 2026-08-18 05:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21e715ea-c0ef-3bb8-83a8-1248717884cc | -16.23327 | -57.66171 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 89e60b77-db01-3e69-8943-5076d00a3b92 | -15.25308 | -56.49226 | 2026-08-18 05:46:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3630870c-4c60-3c25-a1fe-2200dd3c3ff8 | -22.07338 | -55.99373 | 2026-08-18 05:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76c9d138-3dae-36ac-bda2-ad4d1f486619 | -15.26585 | -56.48494 | 2026-08-18 05:46:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81cce35d-cca8-37ee-956f-0210bf4e9b96 | -15.27033 | -56.49895 | 2026-08-18 05:46:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53cfae88-590a-3995-9ce4-5252cbe6f053 | -16.24577 | -57.65528 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 45fe7f86-8d71-3051-8fda-b38c8135e81b | -16.24538 | -57.65878 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 0f513d7c-c0cf-3ae2-a722-a8219fdd7a36 | -15.30441 | -56.44189 | 2026-08-18 05:46:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bcd4f101-75d7-38ed-ac7b-2f4a4ebb6980 | -16.22836 | -57.65998 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 79422024-c589-30f5-bc40-202f9254ddaa | -16.25093 | -57.65949 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c292328a-1462-3080-a3c7-4ecc01aa96e0 | -22.06682 | -55.99305 | 2026-08-18 05:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd41e1fc-ba2e-381b-a805-f07acd82d579 | -16.245 | -57.6622 | 2026-08-18 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c499b6af-dc14-3b59-abcf-c7a140213a19 | -14.2017 | -52.9065 | 2026-08-18 05:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 125.9 |
| d43fb1bb-13f7-3646-9843-21c3a7fe81d8 | -6.841 | -59.0132 | 2026-08-18 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 47951dda-82d2-3c1f-a30b-0107135349b2 | -14.8033 | -46.6453 | 2026-08-18 05:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 6578ee05-dbfb-3766-b2ed-c889ab491843 | -14.2014 | -52.9276 | 2026-08-18 05:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| b52eb753-8f55-3e3b-bf64-f56382dd0d15 | -14.1828 | -52.8878 | 2026-08-18 05:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 0b8a5c15-ef39-36e1-911b-7eaed697754b | -14.1821 | -52.93 | 2026-08-18 05:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 187.4 |
| b639148b-2e67-304f-802c-6532cbc4a706 | -14.1631 | -52.9113 | 2026-08-18 05:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 42a3d24b-5968-3568-96c8-ba7461f393fc | -6.7478 | -59.1716 | 2026-08-18 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 1be4ac66-7639-3826-ba23-b36bb7c07b74 | -14.8228 | -46.6419 | 2026-08-18 05:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 8d9284d7-b546-3f52-9d66-39da81faf531 | -14.1824 | -52.9089 | 2026-08-18 05:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 437.6 |
| 78bc960d-855f-35c2-9f83-dec942232d14 | -6.7478 | -59.1716 | 2026-08-18 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d2219e24-99d0-39c9-bce4-1c7be05c1844 | -8.222 | -55.0418 | 2026-08-18 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e89416c5-b6e9-33ba-982b-94b15a4f7fba | -14.8228 | -46.6419 | 2026-08-18 06:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 0b515492-d424-3c56-95ac-d8182ab63aeb | -14.8228 | -46.6419 | 2026-08-18 06:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 125.3 |
| b7324c7f-49a2-3636-85d4-7fc2198eadda | -14.8033 | -46.6453 | 2026-08-18 06:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 87f4e3b4-34e9-3a92-9a42-50ec8baf3619 | -6.7478 | -59.1716 | 2026-08-18 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f0280266-75ef-3b95-bb8e-25701a745029 | -14.1828 | -52.8878 | 2026-08-18 06:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 1464bae5-c69f-3b0c-9f1c-2c444f9bcd52 | -14.2014 | -52.9276 | 2026-08-18 06:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e3bdc4a4-daa4-32fb-93a4-89d707f218ec | -14.1821 | -52.93 | 2026-08-18 06:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 32074304-7516-3aeb-ad16-b390a319f81a | -14.1631 | -52.9113 | 2026-08-18 06:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 81233c15-de8f-3fac-b451-31f0ff4b2154 | -14.2017 | -52.9065 | 2026-08-18 06:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 82124441-c06c-3a8e-84ea-28a88f42cda3 | -14.1824 | -52.9089 | 2026-08-18 06:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 343.6 |
| 632dffe6-d42a-31c8-8678-0d1bb94d0156 | -14.8233 | -46.619 | 2026-08-18 06:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 3d2fb3cd-8f5c-36ea-ad90-6aff7f0bf774 | -8.57 | -54.73 | 2026-08-18 06:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc4b4cbb-ccca-3d89-b406-e62e642d7808 | -14.19 | -52.93 | 2026-08-18 06:15:00 | MSG-03 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 86c9ee60-c619-3756-98e2-e49e06c6804f | -6.75608 | -59.16446 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1f1b541a-0616-3768-8966-b23d38111759 | -6.84707 | -58.99849 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67074531-9a51-3b56-9fff-a79324053076 | -6.74143 | -59.14934 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f79cb1c-0f36-3c5c-80be-e9dd37290c57 | -6.71584 | -58.93068 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e288add4-6a44-3727-b4c9-e1ca8fe69d3d | -6.85305 | -59.00552 | 2026-08-18 06:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README59.md)
