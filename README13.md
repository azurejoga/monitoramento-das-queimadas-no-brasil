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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdf9746b-0cce-3321-b808-e3bbaf34f7ad | -12.533 | -48.2555 | 2026-07-22 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 654c8cea-bd72-343b-923c-719aee47c314 | -6.0487 | -43.8712 | 2026-07-22 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 130.7 |
| b55d06b1-2dd2-3b69-b5bd-893168971049 | -17.0609 | -45.043 | 2026-07-22 13:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e6830b00-6cd2-3d98-827f-d2ba3c084b24 | -6.03 | -43.8727 | 2026-07-22 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 5b44c7d2-b235-35d0-87cb-66bee23ff1d3 | -12.5138 | -48.2581 | 2026-07-22 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| df4d329a-d6e9-375f-b829-31ad85b42496 | -12.533 | -48.2555 | 2026-07-22 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 2d9ea46e-9e01-3341-93ee-c20c7569eda6 | -12.5334 | -48.2333 | 2026-07-22 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| e1f39996-12cb-35a6-acfb-5aff2054660c | -6.0487 | -43.8712 | 2026-07-22 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 221.6 |
| e7f83f2d-90ee-3e09-be53-524f50163b80 | -12.5334 | -48.2333 | 2026-07-22 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 86298132-113b-3184-9952-2595591f7c2b | -12.533 | -48.2555 | 2026-07-22 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| af9e28f7-158c-318f-af92-ac060e90eec1 | -12.5138 | -48.2581 | 2026-07-22 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 168.8 |
| d6250669-ca39-3940-90d0-34db882b8525 | -10.4305 | -50.2021 | 2026-07-22 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 4ce06c44-886b-347c-8f68-c20dfaf0c151 | -13.3361 | -54.32 | 2026-07-22 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 82fa18ed-86c2-3f8e-a310-7b9e40903ec7 | -10.8244 | -50.4385 | 2026-07-22 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| f8e26747-08f2-3017-af1b-e5d9a19fca7f | -11.7768 | -61.3247 | 2026-07-22 13:50:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 186.5 |
| fef254ea-d77b-32f2-8994-3e6ee4880fbc | -12.3321 | -50.0073 | 2026-07-22 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f073bfe6-f270-3799-b05a-0a4952d6de81 | -6.03 | -43.8727 | 2026-07-22 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 332b51a0-09d6-3495-9be4-a906cbb42ec8 | -13.3361 | -54.32 | 2026-07-22 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9764186b-2d8b-3f0c-b355-febc8ed0a346 | -10.4305 | -50.2021 | 2026-07-22 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| dc350a61-ebfa-3b41-97bd-0981aa0cc41e | -12.5334 | -48.2333 | 2026-07-22 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 142.8 |
| e717332b-7bde-36bc-b9b1-dbc624500816 | -13.4152 | -51.6506 | 2026-07-22 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| fd1ae70f-a251-3cba-8ff8-d7f952f7ad98 | -13.4156 | -51.6293 | 2026-07-22 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 5a96b36f-845b-30b1-8098-9e8a8feca096 | -10.8691 | -47.3632 | 2026-07-22 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 4054a535-e1f8-321d-bd43-c629d658e999 | -13.396 | -51.653 | 2026-07-22 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 04717563-2284-3eb6-baaf-518c917e7bdd | -11.7768 | -61.3247 | 2026-07-22 14:00:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 127.8 |
| f8fb867c-16d9-335b-ade7-225c319ba22b | -17.0609 | -45.043 | 2026-07-22 14:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c7954f14-1978-3fd3-9ffe-f3c2c882d5a2 | -10.85 | -47.3655 | 2026-07-22 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 947b907b-c1ed-3a88-8cfb-659c3c2d7257 | -6.0487 | -43.8712 | 2026-07-22 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 6e5555d6-1801-332b-b0fe-586828c4ce33 | -12.533 | -48.2555 | 2026-07-22 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 14218461-eacc-3a11-a196-b59804860927 | -6.03 | -43.8727 | 2026-07-22 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 21dc03ab-ddf0-3655-b9d4-d2c505e6c17d | -12.5138 | -48.2581 | 2026-07-22 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 865f382e-c392-3eff-8bd0-e9429afa2eb0 | -6.0487 | -43.8712 | 2026-07-22 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 202.2 |
| cd56dd4b-4758-3913-a3c0-f7a70b01959b | -13.3552 | -54.3179 | 2026-07-22 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 1ac56942-4a24-3f26-9eab-49d8e1c8b184 | -6.03 | -43.8727 | 2026-07-22 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 123009f0-2072-3c6d-abae-b41b76bc552c | -13.3169 | -54.3221 | 2026-07-22 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| f69b892e-273e-3d70-863b-0b34efc92f15 | -13.396 | -51.653 | 2026-07-22 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 2d90a1ee-4ce3-3b00-bc2f-4e8775c387d1 | -12.5334 | -48.2333 | 2026-07-22 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 38c52ab1-a78b-3efe-8da6-2de7ead5cbb0 | -12.533 | -48.2555 | 2026-07-22 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 4a99d143-8fc3-351c-a503-7486b95cb822 | -10.9026 | -50.2591 | 2026-07-22 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 97f3b382-eb0d-3161-ab8f-de1e2693e76a | -11.7768 | -61.3247 | 2026-07-22 14:10:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 135.2 |
| dd2a699a-c922-3d85-bf06-e1bc2915e9ef | -10.8244 | -50.4385 | 2026-07-22 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5aa6014a-9865-36a5-b9a2-4cf36f7eb3ec | -13.3743 | -54.3159 | 2026-07-22 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 16dfb024-68c3-36ad-8be3-9b728e5e120c | -13.3746 | -54.2952 | 2026-07-22 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6a189df7-de4d-35c9-9962-559c98426779 | -12.5138 | -48.2581 | 2026-07-22 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| d653c49c-d145-3f82-ac70-a56e69d39fb4 | -10.9216 | -50.2571 | 2026-07-22 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 7f156c07-caba-301a-bf73-8d217550e6b6 | -13.3363 | -54.2993 | 2026-07-22 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 9efc297a-f46a-31a8-b22b-c2f1de9026be | -13.3361 | -54.32 | 2026-07-22 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| c3d30867-6c83-330e-bd7b-dbb93def0d20 | -10.8691 | -47.3632 | 2026-07-22 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 612eceb2-bcd1-3a94-aa2c-00fea47b17c1 | -10.9029 | -50.2377 | 2026-07-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| fecaf282-427c-3586-9c03-4b09a469f6b4 | -10.9026 | -50.2591 | 2026-07-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| d411b85f-26a4-3f5a-a0fe-fa38d838b4bf | -13.3169 | -54.3221 | 2026-07-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| b397ba88-d91d-39cb-8584-17536ac55c50 | -11.7768 | -61.3247 | 2026-07-22 14:20:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 6c7c053a-74f0-3e5e-ada7-508bbe9452f6 | -13.4152 | -51.6506 | 2026-07-22 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 6b3bb9e3-8490-3832-b68e-aa7060721286 | -12.5334 | -48.2333 | 2026-07-22 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 9e1f4170-443a-3aae-b183-033d09f8f7ad | -13.396 | -51.653 | 2026-07-22 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 9d129fd2-00d5-3d7c-ac78-82f565d146a8 | -10.8451 | -50.3081 | 2026-07-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7a03cf7f-e9d0-3b37-8950-e2b871927a6e | -10.8244 | -50.4385 | 2026-07-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| e2cb154b-9141-3612-b981-fe33f0174e59 | -13.3363 | -54.2993 | 2026-07-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 493bfade-fd46-3fe3-b87e-c3bbb429533e | -12.5138 | -48.2581 | 2026-07-22 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 963293e5-60ae-3432-ac54-fbcc9e66ff4f | -12.533 | -48.2555 | 2026-07-22 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 4e8ffa3b-f870-3ded-9eea-ce2d96e49c8c | -13.3361 | -54.32 | 2026-07-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| aa387143-233d-3b88-a376-a2ff03afdd33 | -6.0487 | -43.8712 | 2026-07-22 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 4ba958c2-918e-3946-875e-b1845590a7e8 | -10.4305 | -50.2021 | 2026-07-22 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 158d8271-aa08-3575-81a1-a3dafd8f3983 | -10.9216 | -50.2571 | 2026-07-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 6b3587b2-e428-3d2e-aadf-7e796b0461f7 | -12.5138 | -48.2581 | 2026-07-22 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 0414b89c-742d-3f37-a44f-f9c0f3ec8bc9 | -10.8244 | -50.4385 | 2026-07-22 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 888b12a3-be94-307e-92f1-339416b6489a | -6.0487 | -43.8712 | 2026-07-22 14:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 381f5c64-a21c-3f3d-b2f9-a53e84f21ad6 | -12.5334 | -48.2333 | 2026-07-22 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 4aa53ffc-32f6-3686-a3d6-35e202ba9439 | -11.7768 | -61.3247 | 2026-07-22 14:30:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d15d1f05-9c78-3df1-9ce4-32381e5c0f7d | -13.3363 | -54.2993 | 2026-07-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 7ddef810-7368-3358-9d83-93fb09ea53e0 | -13.4152 | -51.6506 | 2026-07-22 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 079435b0-4e06-330f-bb0e-7fa8045f61e1 | -10.9216 | -50.2571 | 2026-07-22 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 1596a876-c2b1-38bb-b716-eedee7228865 | -12.3212 | -53.2894 | 2026-07-22 14:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 69099f55-0f58-3e6f-a9ad-35867223afe2 | -12.3215 | -53.2686 | 2026-07-22 14:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 46d04361-018c-34c5-9ab5-17e1905e2c80 | -13.3361 | -54.32 | 2026-07-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 3718e3bf-3173-3169-a345-705d7e4dc0f5 | -13.3169 | -54.3221 | 2026-07-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| c9189f6d-6930-3b2e-bf18-2276c1cac48d | -13.396 | -51.653 | 2026-07-22 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 63bd863b-cff1-3d73-9a62-953469a4da3d | -12.533 | -48.2555 | 2026-07-22 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 78f070bb-8db8-34c2-89b6-203f221836d8 | -13.396 | -51.653 | 2026-07-22 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 225dc497-d7d4-3f92-8215-0abf0e899245 | -13.4152 | -51.6506 | 2026-07-22 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3cf8b2b8-246a-3ab5-8ab7-22cbb801f3e8 | -13.3361 | -54.32 | 2026-07-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 19cdd5c4-a0c9-3d81-a0cd-193d108904aa | -11.7768 | -61.3247 | 2026-07-22 14:40:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d5c878f5-6fa1-394a-b4da-4650b889cf69 | -13.3552 | -54.3179 | 2026-07-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 4e846a54-6c81-342e-bcc6-7e883a2afa03 | -12.5334 | -48.2333 | 2026-07-22 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 279b8a15-4de5-3fa9-9570-82f8264493e7 | -17.5748 | -47.4996 | 2026-07-22 14:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a85104a2-69fb-36af-9930-f114c5a3b99f | -6.03 | -43.8727 | 2026-07-22 14:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 22d0c0b1-c870-3bcc-bea8-1879fe5d7c71 | -12.533 | -48.2555 | 2026-07-22 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| b0f62d38-139f-39e7-a376-e94336d59c7a | -12.5138 | -48.2581 | 2026-07-22 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 609691be-da35-3f2e-87c0-41c93551b948 | -13.3169 | -54.3221 | 2026-07-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a14ea6c0-8f5e-36b3-9037-74d94518e848 | -10.8244 | -50.4385 | 2026-07-22 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 4df18fde-8564-3203-b5fc-0b7746be2044 | -10.9216 | -50.2571 | 2026-07-22 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 24351fdb-43e3-3fa4-8d11-c17d9aa1647c | -13.3363 | -54.2993 | 2026-07-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 47efef3e-7e45-342a-8129-d4142fab3b73 | -10.8244 | -50.4385 | 2026-07-22 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 9b917970-6f4c-3a8a-bcc7-2beab97bbab6 | -17.5748 | -47.4996 | 2026-07-22 14:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| a6b766d6-d223-38c7-9b99-175e4b9a6a3b | -13.3743 | -54.3159 | 2026-07-22 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 54b0e2e0-86ff-3f07-9f52-86ab20a94219 | -12.5334 | -48.2333 | 2026-07-22 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| aa9dc9d4-2e69-308e-8e4b-4590e8b12383 | -10.8451 | -50.3081 | 2026-07-22 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| a51a22e1-319c-3823-82a6-65b68e7eff97 | -11.7768 | -61.3247 | 2026-07-22 14:50:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 95.2 |
| a362cb93-1396-303b-a517-a312e3b1cd38 | -12.5138 | -48.2581 | 2026-07-22 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 07df426b-743c-3219-acfb-2d1c3cf0e0e8 | -13.4152 | -51.6506 | 2026-07-22 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |


[Clique aqui para ver as próximas entradas](README14.md)
