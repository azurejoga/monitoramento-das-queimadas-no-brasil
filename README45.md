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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 766b0019-64b6-35a1-ae33-017e0edbbd3f | -10.67528 | -58.74549 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a693bb0-deb2-3efa-97fb-5e19cef0179a | -10.67487 | -58.7527 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2c3ffe5-93e6-30fb-acb9-c58274d6c216 | -10.67468 | -58.74906 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aba54dc9-a3fc-3ef1-abd6-29523f4584d7 | -10.67407 | -58.75262 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6e531ce-07c7-311d-b0aa-e721f3203110 | -10.67185 | -58.74123 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ea74e25-e42e-3d3d-9264-fceaf1523710 | -10.67063 | -58.74841 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2c67721-82c9-3c68-ad23-1e1e37c3921b | -9.97739 | -58.78822 | 2024-10-23 04:53:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52c72415-f036-371b-8d92-fa33c8b06f4e | -9.87948 | -58.32004 | 2024-10-23 04:53:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aeacad6-7ec4-33a7-aa99-a630551e54d5 | -9.78024 | -59.2739 | 2024-10-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| faae75ef-042e-389b-a258-c8e154d08d40 | -9.73718 | -59.31984 | 2024-10-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9650167a-897d-3ce3-8510-3e5d2129eb0f | -9.56411 | -58.92061 | 2024-10-23 04:53:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28b7a431-1fab-3718-ad47-e7469f3d1b9d | -9.56216 | -58.92085 | 2024-10-23 04:53:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc2f5aea-1bd9-34fa-9b97-8f2009d8616a | -10.64924 | -58.75187 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f320d037-89a9-34c0-820b-5eb2536b2175 | -10.64864 | -58.75541 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6345ec2e-1dcc-3875-80a5-120b057ed0fe | -10.4315 | -58.82548 | 2024-10-23 04:53:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41e09247-e038-393a-84f1-b0acaf8c1520 | -10.43088 | -58.82908 | 2024-10-23 04:53:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec25322c-737a-3236-bc6b-a25f80ab5d38 | -16.09599 | -60.13186 | 2024-10-23 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4e8fea9-f2f0-32ea-98de-9f809b81215b | -16.09262 | -60.1274 | 2024-10-23 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4ab674d-92ba-3e4e-8d71-f4d5ee3328b8 | -16.09196 | -60.13107 | 2024-10-23 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14a8c618-e576-347b-9251-cbcc7873f537 | -18.30904 | -56.21527 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.2 |
| a5ee9fdb-9d4e-34e7-a76a-83708d66b5a8 | -22.46024 | -47.77036 | 2024-10-23 04:55:00 | NOAA-21 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aff9ab6d-3da5-3adf-964a-07976fa7238f | -22.45962 | -47.7766 | 2024-10-23 04:55:00 | NOAA-21 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 72cbc89a-1f4b-395c-aeae-c658f921e313 | -22.4591 | -47.77068 | 2024-10-23 04:55:00 | NOAA-21 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 471f4252-300e-36a6-9ee5-3e1e43a97c1d | -22.45843 | -47.77702 | 2024-10-23 04:55:00 | NOAA-21 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e89f97df-e09a-3d62-90e7-64312831c9be | -22.24358 | -49.17259 | 2024-10-23 04:55:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18319dec-40bd-379a-b305-effeba5b6127 | -16.49997 | -51.28857 | 2024-10-23 04:55:00 | NOAA-21 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9f72812-0a69-3c1c-b7dc-27972597175c | -16.16949 | -50.94651 | 2024-10-23 04:55:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 537f5e43-ea2c-334b-a175-0776685a8e53 | -16.10098 | -50.79644 | 2024-10-23 04:55:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2db7fb3e-551a-32bb-b4b2-3d9f0725eb2f | -16.00121 | -51.01138 | 2024-10-23 04:55:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 196e6568-1db0-3833-8911-6a2e6da16309 | -15.90855 | -51.74389 | 2024-10-23 04:55:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0feb45c3-ae1d-32ed-bda3-67e2c8babf12 | -15.90794 | -51.7481 | 2024-10-23 04:55:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5ab70ccf-a00b-360f-9b80-d638a4da3c50 | -15.90498 | -51.74334 | 2024-10-23 04:55:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8b9143f4-d5df-3f08-a743-cb4867ecb020 | -15.90437 | -51.74754 | 2024-10-23 04:55:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 81c74c3e-29ff-35d3-8d2a-0da8c1b2c4b1 | -16.72013 | -51.52802 | 2024-10-23 04:55:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e624df62-f137-3832-9b4c-3c76b4e8abe0 | -18.16826 | -51.63529 | 2024-10-23 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2e7caf6-4ef1-3c16-b39f-c36235dc5517 | -20.79386 | -51.65643 | 2024-10-23 04:55:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 019cbd0f-6caa-3154-a06f-b90bf7772302 | -18.30844 | -56.21893 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.2 |
| d2e8bc80-d320-330f-a627-7122bbf9043a | -18.27364 | -56.11918 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eb0cdd47-436a-3a87-b098-86cde149a1ca | -17.02658 | -56.00003 | 2024-10-23 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f430bc04-10ba-3dfd-9749-83c75e711e7b | -17.026 | -56.00367 | 2024-10-23 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 56c03967-f4d6-3cf1-a9b2-8674a9d5d7d7 | -17.02541 | -56.00733 | 2024-10-23 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 49ee136a-6cdb-3c18-817a-296a9d25e1b1 | -17.02267 | -56.00309 | 2024-10-23 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 067834fc-a118-3b3a-b9a5-13d8ca84e33e | -17.02208 | -56.00675 | 2024-10-23 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0f6eb45d-379b-36a2-9d19-d2b2b4b9217e | -17.01483 | -56.00925 | 2024-10-23 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 096efdc4-dbae-3eab-8c68-182e3c21d682 | -18.30352 | -56.12443 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4b11b081-49b0-3cec-b184-dca6e512b83a | -18.27189 | -56.06631 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6b4b57c4-10eb-30c6-bf86-7ea5db02721e | -18.26916 | -56.06208 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a41fc8d7-9a19-396f-84b1-1667f7a277cc | -18.26682 | -56.07668 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 060f534f-88e5-3560-9abd-5a6c920be4eb | -18.26643 | -56.05785 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0acf444e-b264-3d65-a6a0-f6fb9c5be359 | -18.26467 | -56.0688 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5b48e1ab-150b-3ae6-bce2-5a9c4a2cd7e3 | -18.26408 | -56.07245 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c4d1fc6f-66ab-3d10-9f0b-4a0f5f30053a | -18.25862 | -56.06399 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 35859031-df10-3fff-87e5-f25b3c1f4f51 | -18.16954 | -56.32298 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bc8fdd47-5063-3019-aca1-1fc8798a539f | -18.31236 | -56.21585 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.2 |
| e4e73168-8964-3d00-b3e6-c27f57a66ca2 | -18.31177 | -56.21952 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.2 |
| 9ea9eee6-16cc-36e1-9138-ba182bd8832c | -18.3069 | -56.20736 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 701c7202-6ee0-3aff-a42b-ab73116625a8 | -18.3063 | -56.21102 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1832230c-46de-3479-b28f-bf195cd1fdc7 | -18.30571 | -56.21468 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 816107de-b3f7-3d02-881b-5dda883c15d4 | -18.29415 | -56.11902 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d48b4473-fc82-3033-b591-acbbc7384e77 | -18.28965 | -56.12574 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 182d1c9e-0716-35b2-8564-dd7ccdfea8e8 | -18.27463 | -56.07055 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e7aba3cb-84b2-3412-b239-90a2b86f3fc1 | -18.27307 | -56.05902 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 8de8588c-0d16-3a4b-8c20-8c8059de5f72 | -18.27248 | -56.06266 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 2a831ad9-b33b-3dbd-96a3-8e7229117a41 | -18.26975 | -56.05843 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7aba7a22-471d-385e-8a0c-e6c84db61d44 | -18.26858 | -56.06573 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c323a06c-d087-31d7-9abb-287e518b40c2 | -18.26253 | -56.06092 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bc9ea104-3578-3c56-9784-4ddebf550f16 | -18.26194 | -56.06457 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f8949590-cf0d-364f-9116-5cc37e28ad87 | -18.26076 | -56.07187 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7ce562c9-a727-3a46-b395-dc5236d93ab0 | -18.30963 | -56.21161 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f6a908c1-c13d-31ae-a223-79cf24c4dd9b | -18.30411 | -56.12078 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 71fe384d-4a2f-3d2f-92ed-3566eec86686 | -18.30298 | -56.21043 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fadcbb1c-c9af-324c-a593-d57e0d99e5fc | -18.30079 | -56.12019 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ddd1f630-044a-367c-87d8-11b3c498a9f2 | -18.2791 | -56.12765 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 374e9ae8-c792-3080-9031-aa832932de34 | -18.26623 | -56.08033 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 87fe69ee-9bba-31cf-bdf1-df74c029e26e | -18.26135 | -56.06822 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 62a1d8f1-6d08-3dc0-9a94-fef0e2340cf8 | -18.26018 | -56.07552 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b7113050-4e06-3ef7-838f-e19a8f1c8dbf | -18.25354 | -56.07435 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5346f9c3-081b-3ed3-8495-7960ad2a307b | -18.16621 | -56.32239 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e66a6bc0-530c-35f3-8b0e-33cfc2a78f05 | -18.31295 | -56.21219 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b3ccb5f2-7c0f-33c9-9b73-a11117823ece | -18.31117 | -56.22318 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 1f1b8dcf-a9e3-3274-b5d2-712aa8de57d2 | -18.31022 | -56.20795 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6d814b2b-cbf2-3e57-bbb5-43450d91c397 | -18.30626 | -56.12867 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3fb1fcb5-c6c4-3d93-ac67-9a10c45de5e2 | -18.30137 | -56.11654 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 891afa67-b05b-3428-8107-e3102f439721 | -18.29473 | -56.11537 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8a67a621-790a-3dbc-bd92-4b8e1940296b | -18.29239 | -56.12998 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 482faf7f-1caf-31a6-9c49-95a95cae71c4 | -18.27404 | -56.0742 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 83119654-101a-3458-9e85-cb6ef732b3d5 | -18.26799 | -56.06938 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ce1b12ff-6c97-375f-864d-e8879a8351eb | -18.26584 | -56.0615 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3e57fac7-060f-31bf-ac53-389c80364d54 | -18.26526 | -56.06515 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fb918a04-9942-3ed8-8ee0-9c24c923a706 | -18.2635 | -56.0761 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5063d2da-f92a-35a1-b0be-b0db6679b1c3 | -18.25686 | -56.07493 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 87b6dd7d-a9ba-3b8b-8a84-0e9704e4f189 | -18.17228 | -56.32724 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3e2bbd37-8a96-385c-956a-5d69c1540e08 | -19.64341 | -56.99343 | 2024-10-23 04:55:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2fe00976-035b-3da1-bf49-56c7bdb6e623 | -19.56914 | -56.67671 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ed30a46a-f90c-3980-9bd6-382747d8e4ca | -19.56854 | -56.68042 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ffee7422-0b41-30c5-9558-83691f6799de | -19.56793 | -56.68413 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 829a2cde-ce29-3fdf-8477-449aafd3ce87 | -19.56762 | -56.66499 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 6a77f2d3-ee2b-3e0f-8ee6-107524c72802 | -19.56702 | -56.6687 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9fb2a591-66c4-33ae-a68c-53c04b22c09c | -19.56641 | -56.6724 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e24540cf-3ee8-3c5f-a36a-a61a4b140423 | -19.56581 | -56.67611 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README46.md)
