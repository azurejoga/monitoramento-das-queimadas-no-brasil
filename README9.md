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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fbd2567-61c4-3441-a9da-9f7a30930630 | -15.43625 | -56.32784 | 2026-01-16 04:48:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a94ac156-24d3-3be6-a251-802b6044c424 | -20.09537 | -44.07426 | 2026-01-16 04:48:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 64a89c3f-0836-37ec-88ac-20bbfe84dc20 | -20.42521 | -57.82019 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 77244418-58f2-3e58-ad2a-333972146780 | -18.82505 | -51.61756 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 783d601a-d0cd-325e-8270-248cd8fff0ce | -15.59238 | -57.34586 | 2026-01-16 04:48:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30c74497-cd6c-3901-9f70-c8edfbd6120e | -20.43792 | -57.86169 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 68edd900-200e-390e-ab65-1f8be617db23 | -20.41627 | -57.84598 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6849a409-7dfd-3e01-8b8d-4bc5da62a4a7 | -16.1068 | -56.75597 | 2026-01-16 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36fcebfe-f281-3e5a-866a-54861affbd84 | -18.82227 | -51.61329 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e664fa7-2064-3959-a9a1-4cbd80b3b9e4 | -16.10284 | -56.75517 | 2026-01-16 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43bed76f-fae4-310f-8057-509537574a58 | -20.43003 | -57.86002 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3216ed9a-3bc6-3339-8b00-e81bfff0df7d | -18.81891 | -51.61271 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87d7d00d-3ee9-3805-a05e-22fb8b2ad63f | -20.84211 | -51.74127 | 2026-01-16 04:48:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 44f9fe43-712c-344d-aa1a-e467418eb55a | -15.61484 | -57.32137 | 2026-01-16 04:48:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76a3733f-77a3-3495-af6b-f6870ae542d8 | -18.82562 | -51.61385 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b34c0649-7fd1-36a3-a601-57bd2f7f688f | -18.81557 | -51.61214 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6851770-1b30-338b-aac4-79181ee95e4f | -20.71062 | -56.45139 | 2026-01-16 04:48:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd88e5fb-834f-3e7e-8bd1-966ba19a7b63 | -16.11172 | -56.75146 | 2026-01-16 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7d729848-6c6a-345e-933d-66518ef8b597 | -18.81613 | -51.60843 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9c766ada-5ad1-3c0a-bd30-78d2320ae241 | -16.11076 | -56.75677 | 2026-01-16 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cbe539ec-380a-313e-9769-666ec4cc2680 | -20.43602 | -57.82801 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fbefdd05-faff-3b91-9ce4-5e1ad756b4ee | -18.81392 | -51.60044 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7abc1d0a-8748-38c7-93c4-670254d1d1ec | -16.11567 | -56.75227 | 2026-01-16 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2221fe6c-a9f7-3c48-a95e-0224ec6294e3 | -15.44328 | -56.33114 | 2026-01-16 04:48:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 051df277-a18b-3ae8-be98-2c153431c9ec | -18.83118 | -51.62241 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa576b1c-f1f8-3531-aa79-4c6be66c8584 | -15.43926 | -56.33366 | 2026-01-16 04:48:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8396d84e-db1d-322e-aee4-224859a231e8 | -18.82398 | -51.60216 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a34c815-0d6c-35d3-b41e-980c25886a27 | -15.96782 | -56.27414 | 2026-01-16 04:48:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 189f701a-b4f7-328d-b78a-b6340b98de95 | -15.58891 | -57.34126 | 2026-01-16 04:48:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b62b4758-ffa6-31ce-a61a-f3b209a1bfe1 | -20.44975 | -57.86422 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7dcca432-ec43-3b9d-9ea2-99aaf2e8ac03 | -18.81 | -51.60358 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d71079e7-d409-3593-a0c6-e7aa0baf9783 | -15.97169 | -56.27486 | 2026-01-16 04:48:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8385d244-6c8f-35f9-9685-61180c1da39b | -15.59327 | -57.34488 | 2026-01-16 04:48:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc2c33cc-e923-302a-b7da-bf4b08300cbc | -17.62301 | -50.3576 | 2026-01-16 04:48:00 | NPP-375D | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3a420cd-25cc-3244-9a85-59b7bc839f5d | -15.43536 | -56.3329 | 2026-01-16 04:48:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f852d18-6eb2-3ba4-8660-952ee274b75d | -19.17741 | -57.54187 | 2026-01-16 04:48:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fc36adc0-0761-3947-a52e-39ebbd772ef9 | -20.41741 | -57.79645 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| baf03296-50dd-3f1c-a9f6-7f32f26bb08c | -15.43235 | -56.32707 | 2026-01-16 04:48:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0f5f865-dd47-3a38-b57f-582b2afc8472 | -20.72904 | -55.16041 | 2026-01-16 04:48:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3324282-e174-38f0-bd9d-9e55293d91cb | -20.0961 | -44.06747 | 2026-01-16 04:48:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c45236b5-7b9f-33fc-b4f3-60c0b9102938 | -17.62157 | -46.65832 | 2026-01-16 04:48:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2f0a841f-1af4-3650-900b-019b281a6d4e | -20.43502 | -57.83334 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e436e3b7-5796-3661-9f65-aa16dc9452c9 | -20.40955 | -57.79478 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e7795cfa-8f61-3ef1-bb4e-166e3b9324a0 | -16.10585 | -56.76129 | 2026-01-16 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 546b5296-61ee-3099-b5da-2e7d5f199fb5 | -18.82726 | -51.62555 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 33a0ec60-d0e6-38f9-a031-1532bf1b56aa | -18.81221 | -51.61156 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0f705d4-151d-3694-ad06-9885392383c1 | -16.44593 | -58.16587 | 2026-01-16 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 28dfec65-a7fe-3577-ab35-cade3229f078 | -20.43692 | -57.86703 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ab88af95-9fb9-3d92-af7b-657bf4b50ab6 | -18.82783 | -51.62184 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c1095c84-197f-3a85-967b-a23bffe6d2a5 | -15.43145 | -56.33213 | 2026-01-16 04:48:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6d3fc9f2-9e76-3d1d-b7a0-d762c8dc8500 | -15.59306 | -57.34206 | 2026-01-16 04:48:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c9517ac-12a0-3052-ae53-445e5a2dfcc3 | -15.44406 | -56.32937 | 2026-01-16 04:48:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa3579ec-15ed-313e-a5fb-6ede8f9407ea | -16.09888 | -56.75437 | 2026-01-16 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b576ec06-dede-3589-b0da-02b62e066e88 | -20.73181 | -55.16515 | 2026-01-16 04:48:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 794f80ca-9d3e-31a0-b03b-bc0d5cf67231 | -16.40733 | -54.53614 | 2026-01-16 04:48:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0201491-2929-386a-8cfc-d4668be4553e | -19.34452 | -54.17854 | 2026-01-16 04:48:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bd9c12b-4d94-3f60-ab8b-532c14d23e94 | -20.45369 | -57.86506 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5026e657-b6a6-3985-bb2d-dfd2f6b6dac4 | -17.61743 | -46.65771 | 2026-01-16 04:48:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9985a88b-f152-39b9-abad-38a83552e609 | -18.8217 | -51.617 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4940921-4f9f-32b0-bc86-739876f86224 | -15.58912 | -57.34407 | 2026-01-16 04:48:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 416aae9e-4818-34c5-b47f-a5898d837743 | -20.84269 | -51.73746 | 2026-01-16 04:48:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a8e301cf-a9cf-3ae4-976d-4c90228cc96c | -20.42134 | -57.79729 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b2939484-b4a7-3c90-84d2-b464166df107 | -18.81278 | -51.60786 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b81e2c4a-532a-304d-9698-24458599f096 | -18.81335 | -51.60415 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5c937c92-6182-327c-95a7-999624fe8c97 | -18.81057 | -51.59987 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9052e25-78e8-30fe-a13b-9de5dbcfe5d6 | -18.82284 | -51.60958 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cdf44bdf-9bf6-31c1-a9e6-12576240834d | -18.82341 | -51.60587 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f55c2d6a-7fde-3a02-9cca-29333f6eb6e2 | -18.82006 | -51.6053 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4154cf6-77b3-356d-ac1a-a3663f7a7409 | -20.43398 | -57.86085 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5ea09f6f-fd42-357e-b5c1-77d2730a2bfc | 2.7633 | -60.334 | 2026-01-16 04:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 35.2 |
| dbd8551d-2513-3fd6-aa94-d6f751ef2734 | 2.7634 | -60.315 | 2026-01-16 04:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 71638b53-966f-317b-a5e4-dd22c61b442a | -18.8124 | -51.5914 | 2026-01-16 04:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 6ab89825-01da-382d-bb48-7689ae1c2aab | -18.8119 | -51.6134 | 2026-01-16 04:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 2b5332ab-5ebc-3edf-80f3-ee48fb8fe5d9 | -22.03199 | -56.30448 | 2026-01-16 04:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 847bc3ca-47f3-37e2-a9e0-98ce7935d85a | -26.93078 | -51.2141 | 2026-01-16 04:50:00 | NPP-375D | VIDEIRA | SANTA CATARINA | Brasil | 4219309 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7ebf09e7-8f20-3de5-92fc-53bfdd6e667c | -27.68692 | -48.75246 | 2026-01-16 04:50:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e2e5c9f8-e768-3e1b-aee0-e0c7811db3d5 | -27.66702 | -51.24777 | 2026-01-16 04:50:00 | NPP-375D | CELSO RAMOS | SANTA CATARINA | Brasil | 4204152 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5c4a1238-a1e0-31d3-84f6-061e763a3b0f | -21.22901 | -56.25243 | 2026-01-16 04:50:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e233d4d-f5d6-36fe-939b-415c5230f2b8 | -22.02766 | -56.30809 | 2026-01-16 04:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01f76b4b-8393-3ee6-90be-461afec9c7f4 | -22.02843 | -56.30373 | 2026-01-16 04:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be9ee843-26e2-3f41-a302-cdb3b4dd21bd | -27.66763 | -51.24314 | 2026-01-16 04:50:00 | NPP-375D | CELSO RAMOS | SANTA CATARINA | Brasil | 4204152 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 591c6fcc-02cb-3734-a444-0701305f2070 | -24.96013 | -49.28715 | 2026-01-16 04:50:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6c760109-ccf7-38c9-a59c-dab5ef476afb | -22.03555 | -56.30524 | 2026-01-16 04:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 158df943-36bf-38b8-98c7-21a906fefa9a | -29.84135 | -50.98964 | 2026-01-16 04:53:00 | NPP-375D | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| f5c6c8ce-e4f9-31ee-8013-fa281301a93c | 4.26345 | -60.79608 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 751b0cdd-76dc-30f9-a586-9c557f8f6943 | 4.39468 | -60.92565 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1f1ab4e-a362-3502-8e4c-7764ed1990bc | 4.38998 | -60.92671 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5fba359-48ca-3afb-a3ad-04bbec840807 | 4.2455 | -60.78659 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d84c050b-04bc-34fb-a73e-75172c3b3fdb | 4.45725 | -60.64868 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 170b6f1d-3dfb-387a-ae00-81499f4cc769 | 4.46586 | -60.64233 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d2b1a84-14bd-3cd9-bf74-9450155a0248 | 4.05367 | -61.46802 | 2026-01-16 05:01:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ff19792-71d7-374c-a7c2-5500033560b1 | 4.24626 | -60.79156 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbe42542-8ac8-3ad4-867f-8f70965eb79c | 4.0635 | -61.46656 | 2026-01-16 05:01:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6c3f9ed-bfe4-3925-a5b9-1fb7deeab09a | 4.2433 | -60.78957 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5ef64f7-cd3f-34a6-843d-8cd67c1e70b8 | 4.24727 | -60.78384 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0566da56-5b6e-3999-b734-fa5284cf7727 | 4.05778 | -61.4618 | 2026-01-16 05:01:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee6790f4-29ba-3c03-aead-3f08d1b67c84 | 4.24871 | -60.79381 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62f47a27-54d1-3976-841d-7a28996d5252 | 4.25653 | -60.78148 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4fffc546-f9b6-3959-ab32-22e70f9a6abb | 4.24702 | -60.79657 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95397a79-f5f2-3710-b984-67bdf1971401 | 4.46121 | -60.64315 | 2026-01-16 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README10.md)
