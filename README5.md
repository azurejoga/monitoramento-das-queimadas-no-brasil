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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8d87f87-fcba-30bb-9ef1-edaac1aab25b | -20.7948 | -41.12775 | 2025-01-25 04:40:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ebf10d1d-b5bd-3628-a6d6-c9ecc923aef6 | -16.68112 | -43.88569 | 2025-01-25 04:40:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9b03037-9463-3d3e-8358-e8fde40b2201 | -20.40405 | -49.83968 | 2025-01-25 04:40:00 | NOAA-20 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c93284e3-1190-3748-97a9-ecab80816f4e | -18.84123 | -52.49594 | 2025-01-25 04:40:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 230b5fcb-9afa-3ffa-91b0-da285488b97f | -17.22664 | -52.94712 | 2025-01-25 04:40:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b58f099-1e0e-3b47-9075-7f9e73b8a2ac | -16.39904 | -49.19549 | 2025-01-25 04:40:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bccf5dfc-53ba-3a30-a3e8-ee7e08a53952 | -13.21776 | -50.46565 | 2025-01-25 04:40:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f42e725b-4285-3601-9432-b284b86245db | -13.9082 | -50.34536 | 2025-01-25 04:40:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c48f8bd-ec62-3791-b4e2-53c3c06181d4 | -18.83849 | -52.49174 | 2025-01-25 04:40:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9933eb36-ce3e-3adc-adf5-46f9165b52b9 | -20.40345 | -49.84396 | 2025-01-25 04:40:00 | NOAA-20 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1ea9edc-775e-3e3e-a2aa-0707809b6b95 | -22.69777 | -51.80512 | 2025-01-25 04:42:00 | NOAA-20 | SANTO INÁCIO | PARANÁ | Brasil | 4124509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 818c9a60-b4ad-37d2-a8da-400d91ccb28c | -22.28159 | -48.57382 | 2025-01-25 04:42:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| c50a0d3f-6002-3643-8535-373b4936c43f | -21.07474 | -56.39471 | 2025-01-25 04:42:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e4aed627-22c9-35d3-b5d7-578b635f53b1 | -20.63193 | -55.71246 | 2025-01-25 04:42:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b9678257-617b-38fd-847c-f5087a71ad93 | -22.27771 | -48.57323 | 2025-01-25 04:42:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| fc2af2a1-122f-34cb-b2e7-54ea9a29c7da | -20.63619 | -55.70895 | 2025-01-25 04:42:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 00441410-f18d-351b-b198-d47d06a142ec | -21.0598 | -56.05218 | 2025-01-25 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a7379ae-0d3d-3ea5-a611-be50c5065c22 | -21.28473 | -55.90762 | 2025-01-25 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f7805ca-44fb-36d1-93e7-09fd90264aaf | -20.63545 | -55.71319 | 2025-01-25 04:42:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f2f4dd7-6048-3ef4-b92b-031383219f40 | -20.63416 | -55.6997 | 2025-01-25 04:42:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28d1b44c-1ea3-3822-aabc-01cd49f0f67a | -22.53903 | -48.81148 | 2025-01-25 04:42:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21ae2ab5-45af-3a36-b573-be6132830edb | -21.26452 | -54.8165 | 2025-01-25 04:42:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8174c8f8-4050-3a4f-b439-40fd13a86d27 | -22.11878 | -56.67684 | 2025-01-25 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3eedcb8-fd31-3698-8872-7d2cc2d87e27 | -20.63267 | -55.7082 | 2025-01-25 04:42:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f03160c2-6e51-3054-97ba-414a49ea485d | -22.28225 | -48.56864 | 2025-01-25 04:42:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| d9d955d9-0e86-3f62-a80f-c9133a23bee9 | -21.26919 | -50.65246 | 2025-01-25 04:42:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 085cf87d-da39-3393-bd6f-c56e2a5810b5 | -20.9959 | -51.79305 | 2025-01-25 04:42:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4a801153-ab34-3033-b583-5b8794a513bb | -22.67647 | -42.85275 | 2025-01-25 04:42:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 2592eccc-1bea-3179-8579-c797ecd1e302 | -22.27837 | -48.56806 | 2025-01-25 04:42:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 589e4015-f7c6-31a4-baff-1622de0f5ade | -21.18503 | -48.63554 | 2025-01-25 04:42:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fec42187-8c56-3d9b-9f43-ec70d7170080 | -22.67611 | -42.85675 | 2025-01-25 04:42:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d6c89ee2-7fbe-3ea3-85f1-14e3074c5a4b | -30.24424 | -54.99714 | 2025-01-25 04:44:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| c2cb14bb-759f-3ae5-b8c7-078b6ea3c3ef | 3.79699 | -60.02497 | 2025-01-25 05:27:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94e8e25e-8218-34cb-9d95-0378db6c2199 | 3.80028 | -60.02446 | 2025-01-25 05:27:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 198b3585-c52d-380f-ad9c-e066039562a8 | -9.65039 | -65.73987 | 2025-01-25 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0cadf8b1-c83c-30fb-a1e8-bbc117422b65 | -9.26017 | -60.31636 | 2025-01-25 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 9120df04-e6d4-3cd4-ae0f-cc95ffebb5c4 | -9.26076 | -60.31248 | 2025-01-25 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1882018c-fdd2-310a-9c6f-5601c54c78b5 | -16.21777 | -60.13737 | 2025-01-25 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8dcd9c5-7867-3967-a2c4-d6a58ff8f07b | -16.20195 | -60.13992 | 2025-01-25 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdfc132b-d3b7-3bd3-9a6a-966a541ed73f | -16.21398 | -60.13679 | 2025-01-25 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b352029e-44d0-3a60-ba9a-a4d140966660 | -19.1228 | -56.22526 | 2025-01-25 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4e9d4d00-1bf2-355e-9625-f8d425e096c6 | -16.2026 | -60.13517 | 2025-01-25 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e1b7d58-9816-3ff9-ae6b-ef76eea8a228 | -20.63823 | -55.71183 | 2025-01-25 05:33:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 93ad020a-3763-3bc3-bb65-6569efa8b6e5 | -20.63527 | -55.70635 | 2025-01-25 05:33:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d1a8e81b-7da7-3e2b-91cb-190cf6b84088 | -20.63319 | -55.70788 | 2025-01-25 05:33:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3ccc476f-a98a-3da0-9812-2ab9d6808421 | -20.63856 | -55.70832 | 2025-01-25 05:33:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 10e0a627-62f1-33ad-ae4e-86a7b450d2c6 | -20.62919 | -55.71283 | 2025-01-25 05:33:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3726894-79d4-3e93-826f-9d5f3ea91dd1 | -21.07534 | -56.39371 | 2025-01-25 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e0a6977-eda6-368a-997b-979140c16f02 | -20.63491 | -55.70983 | 2025-01-25 05:33:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d6e8c076-d0fa-330f-b686-fadae3056a4e | -20.63286 | -55.71135 | 2025-01-25 05:33:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c01230e-3673-3c64-9f34-34c542542491 | -20.63252 | -55.71482 | 2025-01-25 05:33:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f3496aec-eff7-3f78-bdef-3401953a82ab | -21.075 | -56.39701 | 2025-01-25 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d5e84ca-b15d-3922-9f55-51b1160f0a94 | -20.63455 | -55.71331 | 2025-01-25 05:33:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7c8519ed-3aae-303e-b06d-1f2b123d7940 | -8.11751 | -43.12204 | 2025-01-25 05:40:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| ba773649-bda3-3527-8e65-0b61667e3599 | -8.19438 | -46.30064 | 2025-01-25 05:40:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f5a637fa-b53e-3b62-8813-8a4dc9618dcd | -12.91049 | -45.0896 | 2025-01-25 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c9a2a5c1-bf04-3a0f-9d27-eb543c23c2f7 | -22.69482 | -51.79993 | 2025-01-25 05:44:00 | AQUA_M-M | SANTO INÁCIO | PARANÁ | Brasil | 4124509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| cf716a3f-8b63-3cfd-a37c-3a401046e1b2 | -20.63902 | -55.70362 | 2025-01-25 05:44:00 | AQUA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 9f437ce5-7bcc-3433-8550-155d2fc495e3 | -22.27618 | -48.56287 | 2025-01-25 05:44:00 | AQUA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| b3f47196-97f1-35e4-9eaf-a4eb926acb82 | -20.6283 | -55.70864 | 2025-01-25 05:44:00 | AQUA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 69305e93-b501-3aca-aeb7-c8ce2db96a88 | 3.79953 | -60.02578 | 2025-01-25 05:52:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86373b73-fdc2-3510-b621-2040cd0330c1 | 3.79881 | -60.02144 | 2025-01-25 05:52:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a896e85e-63f1-3749-b3c4-d4301240e5bc | -11.87148 | -63.96105 | 2025-01-25 05:57:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fbbe069-3c9b-3482-a350-931fb4408d7c | -9.26014 | -60.31488 | 2025-01-25 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d1057628-3c73-3f86-b665-9902bd6882f0 | -9.26059 | -60.31157 | 2025-01-25 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbab0de4-1b64-36d0-a471-b8b1d37d7313 | -9.25969 | -60.31816 | 2025-01-25 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6b254b0a-8c26-3ae1-a342-f4687398628d | -9.26366 | -60.31493 | 2025-01-25 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38c67d81-a6a4-351f-8017-d390d86f5a7b | -9.25794 | -60.31752 | 2025-01-25 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87007c53-e555-3a92-af24-1dc36f8d7363 | -9.25836 | -60.31424 | 2025-01-25 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7f8ac7f7-85b0-3bc7-acf6-e7d6d96b6697 | -9.76831 | -66.61269 | 2025-01-25 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| afb1dcf0-c7ba-3ae5-acbd-d17a09fabc84 | -17.37 | -44.92 | 2025-01-25 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4c511036-810e-370a-a701-a786329ac08a | -6.86781 | -35.00097 | 2025-01-25 11:44:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| e2be569c-3b2b-3fca-97f1-e5030bdb5d2d | -6.93186 | -35.75676 | 2025-01-25 11:44:00 | TERRA_M-M | AREIA | PARAÍBA | Brasil | 2501104 | 25 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 1ac4cc7a-ac63-3f84-974c-8fcd1d51f7ed | -15.73 | -45.95 | 2025-01-25 12:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |


