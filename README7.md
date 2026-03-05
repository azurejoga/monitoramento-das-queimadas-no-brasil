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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4904c1dc-0a44-32f3-8580-2c097885379f | 3.28131 | -60.7406 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 51a63603-e3c2-32b5-816f-ec654ef5f438 | 0.76057 | -59.89821 | 2026-03-05 05:03:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 777a88cc-4501-37bb-a2b6-fe6a0f6b7fe0 | 2.6633 | -60.40619 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d0dfae2-08f6-32a8-920a-1f3f4173d87f | 0.49555 | -60.50453 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 888d80dc-437c-3f44-a84a-56d1055af511 | 4.81245 | -60.68105 | 2026-03-05 05:03:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a972bab0-1485-337b-917c-166aabc9f344 | 0.03567 | -60.99502 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6db46417-64ba-3ba8-a9e3-778ee2aaf776 | 1.0804 | -59.25275 | 2026-03-05 05:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a9bedab-5628-3d75-aca0-22056a7cb5c6 | 3.02695 | -60.64037 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd101b46-011e-3768-a5f3-694f997b2461 | 2.78835 | -60.33937 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 4b005e13-18bb-3b3d-a0f7-f19af7db020a | 2.78634 | -60.32627 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c50ed555-d484-3010-a4f8-7e943f424433 | 2.77879 | -60.33638 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 0fe90c84-16d2-3ef7-a816-f5f9cc56ae53 | 4.53963 | -60.56782 | 2026-03-05 05:03:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28f9229a-e618-3cc6-afae-f5ebc2aeb1a1 | 2.8759 | -60.26452 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e0e8b1e-7ccc-3441-9236-85572a94e007 | 4.96382 | -60.26586 | 2026-03-05 05:03:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de4ef141-7a2a-3638-9f60-57d3c809e1e7 | 3.03155 | -60.82762 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 83bb5d73-cafa-319f-a1b0-8cf004a7cbf3 | 0.4726 | -60.32745 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bc4bbd9-d917-3973-a50a-949772abafab | 2.78458 | -60.34448 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 44fd8444-8786-31db-b399-4d3081537d65 | 3.02694 | -60.82835 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c2330dc3-7e8c-39ca-8d04-4b8e68c9bb75 | 1.00374 | -59.50965 | 2026-03-05 05:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1e57d19-f4e0-3adf-8d09-cabc5d6a4154 | 1.50681 | -59.90921 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 09d4440f-f0d4-3c8f-93e2-f5f589e954f7 | 2.78256 | -60.33131 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e6fc0a6d-4289-3ed4-90a7-a54df75d5ab9 | 1.00782 | -59.50896 | 2026-03-05 05:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71fb8039-d92d-3924-8bc9-ceec194d3d37 | 3.28203 | -60.74535 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5f15e38e-f74b-3c4e-b936-73a4ff506eef | 3.02834 | -60.11306 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fd8ee39-cf30-37ea-aa6d-9cce020a3b8a | 1.06739 | -59.4883 | 2026-03-05 05:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de6b9eb2-7a06-3948-8c9d-fa0489a92907 | 0.58419 | -59.84321 | 2026-03-05 05:03:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c855f1d-6318-3dcd-9d0b-556a13176e2c | 2.78323 | -60.33568 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 25.0 |
| cb68bbeb-5bee-3cac-8089-42ae2913243e | 3.28447 | -60.73042 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9b5fc447-10d5-3d10-a7fd-3777c34f54e0 | 0.05207 | -60.98302 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bff1cd18-6c50-3ee4-a5b0-93c12bb2218e | 2.72494 | -60.65982 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 682ece8c-748e-37d9-b111-e84ed83a94c1 | 0.47688 | -60.32676 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1af475ff-142e-374d-92ec-2a2b694559a3 | 2.69416 | -60.70245 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6872e2f0-1f3b-30bb-ae15-61241c844c62 | 2.98961 | -61.04363 | 2026-03-05 05:03:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 105d298c-ba83-3d70-93f6-c3b9369b22c5 | 3.18871 | -60.56538 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a49e142-3e6b-3475-a57a-51af34221429 | 0.66375 | -60.30754 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44ef8c50-0a7e-3db6-ad6b-fc57faf1134d | 0.49619 | -60.50869 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98300f16-ffcf-3651-8c8c-6802d835ecb1 | 0.66805 | -60.30685 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81ea3b7b-3859-3331-ba27-caf30cb7a417 | 0.46176 | -60.40002 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f01a1ca6-86d3-39bf-a45e-23ec8172191e | 2.72564 | -60.66443 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cebc008-d68b-33b3-a51a-ae41ad40b705 | 3.18416 | -60.56606 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6931be10-74cf-31d9-a75f-d5a978e6e1e0 | 3.05744 | -60.62622 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5a85ed1-864b-3202-8b79-3b39a799fed3 | 0.31501 | -60.44944 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 164080dd-b9fe-3860-b789-a563a783fc1c | 4.96312 | -60.26404 | 2026-03-05 05:03:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37ab92dc-bbe1-35f7-830e-2242cfcca213 | 3.03014 | -60.81811 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd6d6c56-d741-3446-8d30-8428f93cfbd8 | 0.46368 | -60.39896 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a64e476-878a-3da8-a8e8-e62cced70163 | 1.50804 | -59.91719 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d6b80dd-b770-3dac-8595-cfbffc5a4e44 | 2.78701 | -60.33063 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d16e3d7a-f5e9-38d0-aa1d-cc4467a7a7e8 | 0.4562 | -60.39249 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11cbf795-4eb1-31c2-9678-7c93bcc6f20b | 3.03475 | -60.8174 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63dfc157-254a-3b77-b52b-dfb58056c2d2 | 2.70047 | -60.68247 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26152467-f531-3b3f-bb5e-06ff0133935a | 0.04013 | -60.9943 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d0f21f4-5aaf-3b54-89ae-da6f832fecaa | 2.78526 | -60.3489 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 325f8941-88c1-361c-b56e-bf884e0609e1 | 2.78013 | -60.34517 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4fb5c754-49c3-316a-a97f-f6815417d670 | 0.47625 | -60.32272 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccd48315-5af3-32de-a06b-6cd823c8070b | 0.48054 | -60.32206 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccf8b6e9-b2e9-383d-9e9a-4213600accc2 | 0.04181 | -60.97582 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d8b38eb-dfd3-394a-9d34-dd5429882a02 | 0.03804 | -60.9809 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 771f6581-3412-380e-b235-543c486cb784 | 3.03537 | -60.63433 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 986f3fef-50b2-33f1-9fc5-c83292c3230d | 1.21442 | -59.97717 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c63f549d-12cc-3e68-ac77-17409024e1f2 | 2.77946 | -60.34078 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 4c15969b-93ee-36af-bf31-f2e95d140bc1 | 3.16932 | -60.24389 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87eec34e-86ef-38d5-8630-d66a43e3bf6f | 2.69731 | -60.69242 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0bd6e36c-bf4f-3a1a-bd02-a6062f1f54e0 | 2.99748 | -61.03233 | 2026-03-05 05:03:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1098c374-8f27-3032-8f4c-9ce1eb9d5c46 | 2.69661 | -60.68779 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b44cca1-d441-395d-b9da-eafa73d93075 | 0.49684 | -60.51288 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a1c18e0-3f8c-3d73-8e0e-aa2ae5970ca6 | 0.83749 | -60.27723 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b1c213f-81a0-3fdc-94c5-7cdceee7568b | 4.95099 | -60.27665 | 2026-03-05 05:03:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0da8157-88d6-35a8-a793-a52bbfadea2a | 0.66468 | -60.30258 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 9bc35fe5-f767-3976-b94d-20aa07aa3579 | 3.02765 | -60.83311 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d99829ce-cc33-39ba-9afc-e6bee6b10b07 | 0.07372 | -60.54414 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f3db28c9-88c0-384a-af66-10b440dffb7c | 2.78593 | -60.35333 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19c1ee85-f328-3915-bfab-0da158a5a751 | 3.03085 | -60.82288 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 971b7552-a66d-3d91-829c-9dfb5e2d58a8 | 3.98721 | -60.17221 | 2026-03-05 05:03:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 413450d8-40f4-36aa-ba1b-ad9d64bdcdff | 0.07804 | -60.54342 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0dd746b-2274-37e9-ad8b-ac58af3e2ba6 | 0.30273 | -60.45562 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac31c507-263d-3818-b0e1-c6ec4bd101b5 | 3.18941 | -60.56993 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d54c4f4-680f-3a61-aa4f-06ed7e58a743 | 2.96272 | -61.08833 | 2026-03-05 05:03:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bad9eeb4-0591-3aa6-977f-902934c86b57 | 0.46113 | -60.39592 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c7c52f4-3b89-3a11-b765-7df6abb7e852 | 0.04388 | -60.98907 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d03d6553-721c-39a5-a6bb-c4916f83cca7 | 2.9642 | -61.09826 | 2026-03-05 05:03:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f1114ef-3297-3164-94ec-2a118ac3fb72 | 2.7839 | -60.34007 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 66751176-301f-399d-9287-834bcae616f1 | 0.76833 | -59.89305 | 2026-03-05 05:03:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fdfc1af-b6cc-381a-a9e7-9d1273b7a2fd | 0.47197 | -60.3234 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20d6b478-1824-3478-b5b2-b57c6521d15f | 0.76893 | -59.89687 | 2026-03-05 05:03:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10db0514-f409-3453-8f0e-375e8e75d892 | 2.78189 | -60.32693 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 084f8c79-9111-3872-9162-ba2180f3773a | 0.4925 | -60.5136 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eff8ee1-52bc-36bf-85ea-0fce60af32fa | 1.51162 | -59.91233 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f755e293-b717-3fbd-a85c-77f6457ebcb8 | 3.28835 | -60.72496 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b75d13be-3540-3a39-bf37-6c94e48fc4a7 | 4.96242 | -60.2594 | 2026-03-05 05:03:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7806c82f-2a58-391f-a1c8-cc966b8c0f49 | 3.07254 | -60.63339 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7f48348-ced3-3ad6-831e-0439c96a1c3a | 0.45938 | -60.39964 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cae0f589-a0d5-30a2-9d4a-808dd3e2b6ff | 0.31436 | -60.44534 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d991067d-f4b9-389a-99fe-9f6eb0a07bd4 | 3.51333 | -61.90216 | 2026-03-05 05:03:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbdf6359-30c1-3206-82e3-91bef1e5caaa | 1.06797 | -59.49192 | 2026-03-05 05:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10c714cf-e3bd-3512-8bb5-3e218e9a2f18 | 1.5062 | -59.90525 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 17e2debb-e950-3e74-adf5-55c67dd3941d | 2.78971 | -60.34822 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f49615f4-74f6-316e-b9b5-4b8ceecb7281 | 2.6903 | -60.7078 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6c33840e-ebea-3fdd-bee5-f298bc48430c | 2.23009 | -60.2213 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 42195aa8-d0c0-3437-a062-1e44c3a69877 | 2.68961 | -60.70314 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba02f6ff-c13b-37f8-95ba-58f28253e6d2 | 1.51101 | -59.90836 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |


[Clique aqui para ver as próximas entradas](README8.md)
