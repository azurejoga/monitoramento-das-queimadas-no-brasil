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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e31b9ed-716d-3b12-8fad-ee0fb91d8044 | -4.92839 | -47.58166 | 2024-10-10 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51b7f357-1bb4-33c6-a3a7-b40c434b5323 | -4.84906 | -47.51846 | 2024-10-10 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43de03ae-fa83-308c-86ef-30e2ab5d397c | -4.8397 | -46.8606 | 2024-10-10 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f2cd58d-7cc0-302d-80a8-38c154c9a40f | -4.8368 | -46.85605 | 2024-10-10 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e4f25cd-9922-3453-9359-71c2d802fdd2 | -4.83616 | -46.86 | 2024-10-10 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16ce87eb-3ea3-3c16-9c46-9e82be7b70b2 | -4.83326 | -46.85548 | 2024-10-10 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c22844e-ad06-31be-889d-0b482908369d | -4.83093 | -46.50753 | 2024-10-10 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e5aeb12e-c655-3d2d-b235-fce6d81d3842 | -4.83066 | -46.78178 | 2024-10-10 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd599a64-06f0-3789-8e66-69feb7b5cf4f | -4.65852 | -46.44065 | 2024-10-10 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82e9b131-a7b9-3cb4-93b8-18b12933bf6b | -4.47471 | -47.73401 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a021fd6-9185-3d77-a650-f612b2bdae2f | -4.47398 | -47.73851 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b710d23-c020-3c22-8690-6338b37f23da | -4.47099 | -47.73343 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab9ec4fc-e1e1-3526-ad8c-7963cddb9e51 | -4.32129 | -47.70654 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22caa185-902a-3945-b91d-c46fe1595ebd | -4.32071 | -47.70395 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 924820af-9129-34ca-abc5-e61aec8262fb | -4.3183 | -47.70152 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ef839ce-47c3-3204-a9f1-9f4ce8d090fe | -4.31758 | -47.70588 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eea35e1f-13e3-3f8f-bcde-a8dde6961057 | -4.317 | -47.70327 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9811bdbb-fda1-3bd2-84bf-c321f27b763f | -3.93417 | -46.45679 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f6cebaf-eb51-3a2e-9783-ea3e5e85face | -3.93067 | -46.45619 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f144e4bd-b511-396c-9882-aa99475fa5ef | -3.93003 | -46.46016 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aec45131-f41a-33c1-9e10-a1958244d590 | -3.92841 | -46.44781 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 178ed727-fa94-30c0-8984-1dc83316673b | -3.92779 | -46.45169 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6406c4f1-6256-3c6f-9ec6-aa83b869e2ae | -3.92653 | -46.45955 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d6a42dd-29d5-3c74-af01-51ead11c3b28 | -3.9249 | -46.44725 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6f48e86-8834-34a4-b55a-39c769efafb6 | -3.92428 | -46.45113 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb747265-73d9-32d6-a1c9-d72f8f623918 | -3.92283 | -46.41528 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40a3fe73-6433-3db0-a66f-fe437de841b7 | -3.92223 | -46.41905 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1786ac93-0d64-3ee9-96a2-d99cea631485 | -3.91499 | -46.44168 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07590564-7227-3d8e-91e0-925fe0a1baa9 | -3.91312 | -46.45336 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 018cd49b-8894-32da-8d32-f2a5b3455e67 | -3.91249 | -46.45724 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0786f67d-d0cc-3685-9a40-e3a135e07b2f | -3.91211 | -46.43723 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd26947a-4b81-3450-a269-8f6a893ee71c | -3.91187 | -46.46113 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e342d1f7-519c-323f-a541-31fae8c243bf | -3.90898 | -46.45671 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36702449-5627-3e0d-8a9e-6c5650f25ac9 | -3.90835 | -46.46058 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 819407f3-cd51-3bc6-8902-f8c7f738d2f0 | -3.90546 | -46.45617 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6889ac21-7fd5-3010-9832-b87e95e45105 | -3.90484 | -46.46003 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4a4296b-3066-33c9-b47b-0b274495b39b | -3.90421 | -46.46391 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e5dbd04-61bc-3bd5-a5f6-12c854785835 | -3.90195 | -46.4556 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d997b26f-6198-3abf-9e6b-082767d29afc | -3.90133 | -46.45947 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c3316ca-82c0-3a9b-90d9-a45cbe63ea01 | -3.9007 | -46.46334 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce3352a5-3343-3889-b6b2-4becf03f323c | -3.89906 | -46.45116 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f61142e-6dde-3284-8ec8-f4e3ace20a19 | -3.89844 | -46.45502 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 321c58ed-d16c-39b8-ba6e-7b58a59f3ae4 | -3.89781 | -46.4589 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f18b5b9-d5c3-3bfc-b979-1eaa02b3a111 | -3.89719 | -46.46278 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da2fa8bf-b920-3f48-a6f6-5e8454906379 | -3.89205 | -46.45001 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f8208ac-1a7d-3811-bb9a-5bf64af733ed | -3.89142 | -46.45387 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6473a476-4e5e-3bf9-b75f-6769ec096797 | -3.87611 | -46.4594 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1554fa83-6e39-3a7c-b087-abff9f99e757 | -3.87548 | -46.46331 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20ab24b8-ec02-3936-a7b9-45bbe62c5581 | -3.85367 | -46.46511 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb529b99-a0a3-3317-916a-0ead2a68530f | -3.85304 | -46.46903 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6930f08-3b48-3c38-951f-1b27445b763b | -3.84953 | -46.46843 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c30466b2-c3d8-3276-9927-1394c3b5d459 | -3.84891 | -46.47237 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 395aef5b-2275-3710-9dba-2baeb21bc096 | -3.84665 | -46.46391 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec77366a-9460-3b08-917e-35fc2d888c1f | -3.84602 | -46.46783 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 231d3417-c5ac-36da-bed9-f386ec09c8a5 | -3.84375 | -46.45947 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ac71ab1-9ef1-3850-82f6-70f94d278a63 | -3.84313 | -46.46333 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93c2cc3a-deb4-3a00-8cdd-bc8dd91afd39 | -3.84251 | -46.46728 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbe99336-29d4-307b-b821-8973fcd84d24 | -3.83899 | -46.46672 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09faeb58-5d97-323a-85c4-b71aa0a42781 | -3.82292 | -47.49581 | 2024-10-10 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecc6818f-a0ef-350e-9eae-d0308843804a | -3.81922 | -47.49522 | 2024-10-10 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8981d805-d3f6-31c9-865a-5f406b161fef | -3.81254 | -47.48968 | 2024-10-10 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00a206a8-bb5a-333f-919b-afbe47a521b1 | -3.81182 | -47.49402 | 2024-10-10 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9f6c257-d478-3241-b009-c83cbf674a3a | -3.81085 | -47.4868 | 2024-10-10 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54f717ae-4163-3130-af68-716e9ec72daa | -3.81017 | -47.49115 | 2024-10-10 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3614ce0c-51ee-32c1-a181-b13fe8666ac1 | -3.80884 | -47.48907 | 2024-10-10 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81482755-8774-30b8-a5ba-c7a088084198 | -3.80813 | -47.49339 | 2024-10-10 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2038e4a-a082-32ed-be7b-4f0e4d55e958 | -3.80716 | -47.48619 | 2024-10-10 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c348d419-1886-31c1-8377-8d73bd3954b7 | -3.70352 | -47.60919 | 2024-10-10 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96d8ac4b-08cc-3958-b749-7e23b794de0f | -3.70051 | -47.60417 | 2024-10-10 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45810eae-f1ca-35f0-8f81-5029b4fb9136 | -4.55179 | -46.40837 | 2024-10-10 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3035138b-90da-3204-ad3a-2584a3ec6d78 | -4.55117 | -46.4122 | 2024-10-10 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e779b61f-9a6b-3dac-8777-a3170a19145c | -4.48182 | -46.59656 | 2024-10-10 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3569246b-6d8d-3365-bfd0-76577c7c0759 | -4.47831 | -46.59602 | 2024-10-10 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 60e9e868-11b3-3bbb-a222-1ba5743fb837 | -4.47479 | -46.59549 | 2024-10-10 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 01640282-be46-37c4-8c8d-9730e376fabb | -4.35223 | -47.29358 | 2024-10-10 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cec9368-899a-3c46-a7a9-d01c58c9a97a | -4.34925 | -47.28893 | 2024-10-10 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f17050e-1dec-326f-b2a3-3edea891a7fc | -4.34859 | -47.29303 | 2024-10-10 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9789e64b-cc2b-3cd6-a062-209e81ad0da4 | -4.33563 | -47.304 | 2024-10-10 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fd9f098-cc77-3207-bc1b-811e448bb1cd | -4.33132 | -47.30756 | 2024-10-10 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eac99592-7d9a-35b9-b331-20972fba66b7 | -4.33065 | -47.31168 | 2024-10-10 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5177fee6-ed88-385d-9fc8-7fd2aff1ce81 | -4.28167 | -47.29131 | 2024-10-10 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c54edf2e-d07c-3f8b-a57b-3fe97e340f1f | -4.27409 | -46.42969 | 2024-10-10 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c5058e4-345c-350b-968b-429c5455ddec | -4.25912 | -47.19831 | 2024-10-10 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2707b845-5d50-3fd0-b562-8533a0af7915 | -4.1254 | -46.68265 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83b132f4-fd9a-3f3f-acf9-7970ceeea347 | -4.12476 | -46.68666 | 2024-10-10 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae63492f-7740-3f24-8acc-0242edadf832 | -4.08429 | -47.19796 | 2024-10-10 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2218ba31-721b-3718-964f-1424ef38189b | -5.85443 | -46.60949 | 2024-10-10 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23d98aaf-2a5f-387e-9061-f49dad7c4237 | -5.84265 | -47.42237 | 2024-10-10 04:17:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6fb1eebc-b0af-3f64-bd9f-8ec472062d0f | -5.84131 | -47.43066 | 2024-10-10 04:17:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec0559e7-1841-3b1b-b393-d79124126a1c | -5.83972 | -47.41764 | 2024-10-10 04:17:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc84b9ba-de33-3bf5-b12f-2014602916e6 | -5.83612 | -47.41706 | 2024-10-10 04:17:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d36d59d-32b1-3492-9b9b-5417e5f8e27a | -5.83545 | -47.42119 | 2024-10-10 04:17:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 46bf2753-0637-3af4-b703-a4e25cb65fcc | -5.78319 | -46.51321 | 2024-10-10 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8633433a-f217-354f-9eb5-06fef2d06e91 | -5.54523 | -46.69141 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 141dc4d5-1038-3a69-bdb7-230d86321e6f | -5.54112 | -46.69471 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08f5459f-e876-354c-b854-62de7f95d22b | -5.52617 | -47.09847 | 2024-10-10 04:17:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cae2178-1ed1-35e9-b267-ae1378a309ae | -5.52198 | -47.10176 | 2024-10-10 04:17:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0627a047-2464-358b-9c18-d23c19d80e16 | -5.49493 | -46.91549 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5dc761f-9c46-358c-8a32-ce1a4f17e52e | -5.47625 | -46.85197 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e8f4f49-3011-3527-b81c-4844564cd8fa | -5.43665 | -47.82946 | 2024-10-10 04:17:00 | NPP-375D | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README63.md)
