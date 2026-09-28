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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d763513-1fba-3720-acc6-0412407295d6 | -7.05821 | -55.47912 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dade3776-95d5-30c2-b5f6-a87e401c15fb | -3.27159 | -50.14206 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dbb4c50-f10b-34c4-b8e7-d5aa87bddb35 | -10.22441 | -50.00099 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a2cd932-5ebd-3d4c-90f3-6f5f51bafd0f | -8.96739 | -44.15374 | 2026-09-28 05:10:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69200c2c-7c09-312d-bacc-1fe2f78e6c76 | -7.3805 | -42.10165 | 2026-09-28 05:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7bb63c70-1079-3e10-9228-7f16359e7453 | -4.79131 | -49.11243 | 2026-09-28 05:10:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcc0fb22-efdd-3131-842c-64e5dd427557 | -2.6619 | -51.73318 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 466580c6-d73c-3766-b993-a5c8a2eada21 | -2.06136 | -56.86819 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f2f9ef9-7333-3c0f-9cf1-948e10deb8ff | -8.42743 | -44.86124 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfc3f81e-0652-3379-afb6-4bf4e3592e22 | -3.51608 | -50.31946 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd1c247b-015e-31e7-bf61-559ae7acb334 | -10.24881 | -44.61599 | 2026-09-28 05:10:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e80add7e-bae0-339a-9ea8-2d47bcfe3386 | -9.08119 | -49.87189 | 2026-09-28 05:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b003c002-c886-3e31-ade0-2876081dba87 | -2.91942 | -54.20273 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4eaf0efd-8782-3af7-8bc1-916d469f2857 | -8.25609 | -54.78658 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e5bcd4f-df0e-3ca7-b5d7-cdb27405e0d9 | -6.48459 | -55.97642 | 2026-09-28 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9631a40d-8386-34ce-ad85-7e97182ecf3e | -8.66056 | -45.41445 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4db380c6-7a4a-3de8-8578-83943e2efe19 | -7.71051 | -54.76731 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b91f0cd-6891-34c3-9423-2a99b68320bd | -2.99634 | -54.75534 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bdedb42-70af-34d0-8d6f-5ff6811b2f41 | -4.84584 | -42.88713 | 2026-09-28 05:10:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b86b5197-d300-3f27-b8f9-ec7201f25816 | -9.77361 | -48.21186 | 2026-09-28 05:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a18cae3-dc7f-33b0-a6c1-e2813a3fe114 | -11.18423 | -44.80009 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 22351660-6e9a-3ae1-8066-0ea7ec003aaf | -10.4535 | -45.09026 | 2026-09-28 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c0d3054-2ef7-326f-8195-05d21d96b364 | -7.83146 | -55.13826 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fc9167e-85fd-3f7b-ae72-4603fbd4785f | -8.23057 | -45.4427 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a564fea9-eb42-3a0c-8ec0-5aa059031e26 | -9.1501 | -45.64269 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce523dab-ec6a-3110-8399-7b475de8fa8d | -10.8009 | -48.73046 | 2026-09-28 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f923233b-effc-3b5a-b6e2-899cbf68719c | -11.18853 | -44.8134 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 5348a777-bca2-37a8-a8c2-153e79f1ac0a | -11.1832 | -44.81083 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| eab11b02-d4ee-3fc8-81c3-01b659f9f72e | -8.03863 | -54.89883 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64bebe92-8edf-35f6-8463-4292a99d85de | -10.16418 | -46.57651 | 2026-09-28 05:10:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d9b85d3-c619-3314-9124-0828756de69d | -7.94254 | -61.52678 | 2026-09-28 05:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31676f2f-18ec-3dd0-9e49-b506f26c4904 | -5.89131 | -42.43315 | 2026-09-28 05:10:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2b8871cb-c388-3030-8962-82f5f4bffdcb | -9.99443 | -50.13331 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e5ff9e5d-341b-3a9b-8cde-f2bd270971df | -7.05762 | -55.48269 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71c174d4-cfa4-303a-b226-6bb9e78cc157 | -8.42033 | -44.87201 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21ffbbde-a0ac-31aa-9637-33d374d3de69 | -7.28309 | -55.57721 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2887f95-b598-318f-95ed-29520f3cdfcd | -9.82238 | -45.26643 | 2026-09-28 05:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79eb1418-5599-3fa5-8980-db924867e3e1 | -7.3507 | -42.07434 | 2026-09-28 05:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d020712c-c535-3fc9-87be-23b56c8e77cf | -2.91328 | -54.19817 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13d59cfa-eceb-3826-8ad7-ad08bbfdf798 | -6.92893 | -42.85877 | 2026-09-28 05:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9c1244a8-dac6-3c70-b56a-acfa7a3fc4d6 | -6.7435 | -55.08664 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a10693f-65ac-3d86-8a14-9f4cb7c5fb01 | -8.72934 | -47.98174 | 2026-09-28 05:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d6095af-a1af-3eef-a8f1-fc86dd3f5474 | -6.63838 | -59.94997 | 2026-09-28 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac4cea8d-7f2a-39cc-807d-8bc0e462a78b | -3.01583 | -54.21428 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d67148af-861d-3253-9fee-5c6b0c52f513 | -8.73011 | -47.97907 | 2026-09-28 05:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7870fe5a-00e8-378c-9d88-35604fd33b5e | -9.19239 | -45.75814 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9724484e-23d2-36f6-b980-3df5539391c8 | -3.20201 | -51.03354 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3be54c6a-e053-373b-91d1-c45349334304 | -2.93142 | -56.57483 | 2026-09-28 05:10:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 133418a8-a62e-35c8-9d9e-9dc8a872f3d3 | -10.38052 | -44.97119 | 2026-09-28 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15978573-64b7-3fd2-be22-2bbbcd766afb | -3.01192 | -54.21726 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd091f4b-d3a6-32d6-8c0f-a63a4a1eaef4 | -9.17301 | -45.78174 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c138c833-518a-3607-8206-2ab019c36fd8 | -8.13939 | -44.4511 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bd4c5ea-bafd-3e70-a0b0-fff663cff1e2 | -6.00302 | -47.39474 | 2026-09-28 05:10:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| a3ebb492-7c77-30a3-b48d-a976fbce6045 | -8.28217 | -54.70849 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7e4890b-4830-3c53-9cef-73f30e1c5349 | -10.2224 | -49.98613 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e03ff002-bcc7-310b-91e4-79c4d4ca1481 | -2.9179 | -58.3064 | 2026-09-28 05:10:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 151408a5-7733-31ee-9d20-8119d17728ba | -8.23297 | -45.44195 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a167ed2a-0821-3183-868c-2c7f7ada6eab | -9.94294 | -50.23664 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 01ceaa62-af0e-380c-b3a1-e0bd842d963b | -2.91997 | -54.19923 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6509c08a-f6bc-3dbf-a134-a54285c0bf74 | -3.14904 | -54.07758 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4bc5d709-b3f1-3ecf-bae2-8cd2e343a687 | -2.67351 | -56.463 | 2026-09-28 05:10:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6dd2262b-c64e-3fb7-ab06-f551b8e721e7 | -7.88811 | -45.44707 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c607857-9c8c-3265-8917-ebcd6981b1b5 | -9.98418 | -50.14774 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cdddd0bf-c229-3d9a-b541-c2d9d3dca0ff | -3.5088 | -50.31836 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb68bf7f-3ef5-37c9-9ab1-c5a485f9796c | -4.98692 | -56.15125 | 2026-09-28 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e3202f7-573f-35c2-950a-90351d5b0d21 | -10.21025 | -49.98433 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de80cd3c-bc35-380b-ab55-e56674374b03 | -7.71384 | -54.76785 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3915982-2fe5-3b44-81a9-55f1c13956a2 | -3.00913 | -54.21324 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66023d4b-0e0a-32a9-b11b-c33f77cb9af0 | -10.21379 | -49.9885 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7b8d5c4-3dc9-3925-abc3-4ac3570f1d08 | -6.35581 | -45.78982 | 2026-09-28 05:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a73777af-9cbc-3425-a6ee-29e5a608db04 | -6.76284 | -45.37023 | 2026-09-28 05:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fab8bc36-0ea4-32cf-a69c-0d943f414d54 | -3.29285 | -50.31753 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f33eedd-97b5-397d-8f5e-690057fbda8f | -2.65849 | -51.73265 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c02ee31-1477-3fd4-a20b-e6a3963b6030 | -7.37845 | -47.0201 | 2026-09-28 05:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 384e320e-9e88-3661-8885-cfc85f7b2410 | -2.55287 | -57.41077 | 2026-09-28 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf67b5ec-327d-303a-a436-76e23c507336 | -10.00319 | -50.12927 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4a759b28-25df-3b55-a848-262ce48fcf13 | -2.72593 | -54.20076 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2246980-bfda-30f9-8f6d-32c45743dab9 | -6.59961 | -47.16544 | 2026-09-28 05:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41541036-b0d4-38c8-8e4b-47387b473d5d | -3.07027 | -51.20665 | 2026-09-28 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a7a4bfe-4405-398a-8a5b-3aa1ac07f9c3 | -2.05692 | -56.87206 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c26f964-abea-3708-803d-1aa57386c739 | -3.14849 | -54.08105 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96dfce82-0ea3-3ef3-9b4d-5a42f94ce3aa | -5.97939 | -57.69194 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87560ede-6154-3e9a-b86f-420b4bd09cc3 | -2.54825 | -56.28883 | 2026-09-28 05:10:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfb84423-3ad3-39bb-a87a-1557062c9e14 | -3.36303 | -50.46656 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6b6bafb-836d-3c72-99f2-63d9a2dadbb5 | -5.6389 | -50.03861 | 2026-09-28 05:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb63874a-6064-3e6a-bb9d-a70ee00cbae6 | -2.9501 | -54.08929 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a1aacb24-9c23-356d-ab53-b9d4b197510b | -8.23012 | -45.48476 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b97ae349-5723-307f-8378-204ef3d76df0 | -7.62693 | -45.52071 | 2026-09-28 05:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ebfe80c-8495-3e79-9851-15880d1f520a | -7.3832 | -47.02075 | 2026-09-28 05:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95b21580-b88f-3a18-adf7-0e3c7d9d098d | -6.60029 | -47.16061 | 2026-09-28 05:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f5e65c1-7f15-30f5-ad0c-64e1aa3e182f | -7.69502 | -54.76507 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a697969c-acb8-359d-8b48-388c90659dc7 | -8.89979 | -46.1937 | 2026-09-28 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eb2c91b-870f-3033-bffb-9deb460ba3d8 | -7.82144 | -55.13664 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c29c1bd-889b-34bd-bc08-6eacb4acf353 | -3.195 | -51.03247 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd668855-9c8b-305d-8dd0-ef7ed03bb372 | -7.06099 | -55.48323 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2be98e36-bbb1-3d5f-a307-85c6d5c7998f | -7.06436 | -55.48378 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1426c74-8319-368b-94b4-c27e41df13b5 | -2.90879 | -54.11858 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5127a9f3-d85d-3c29-acb1-33fbb4b55f37 | -7.99134 | -44.81841 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc3165ea-e158-3fa3-970a-b7c1a99a64fe | -3.20293 | -51.1941 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b3af128-c62f-3699-b595-54a56cd3d0f7 | -7.72049 | -54.76891 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README52.md)
