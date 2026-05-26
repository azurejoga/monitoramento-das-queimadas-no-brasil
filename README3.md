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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1791d628-1d9e-378e-baf5-0a6697270340 | -11.3584 | -52.9514 | 2026-05-26 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 9c73ea35-ab9e-3f1c-97a5-d8b9ee0563c1 | -5.7939 | -45.1267 | 2026-05-26 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4692dbbc-d9b1-3221-9abc-0dbaabf36f43 | -9.5534 | -40.3254 | 2026-05-26 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.4 |
| be33739c-8a22-36b0-b8e8-7130c49acba9 | -9.5339 | -40.3531 | 2026-05-26 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 44c110a7-bb95-3f1f-b19c-26fa151bae4d | -11.3584 | -52.9514 | 2026-05-26 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 166.5 |
| 0ffa407e-e63a-316b-8a93-254357b4825d | -11.1714 | -55.9117 | 2026-05-26 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| f3a4795e-01a3-308a-bbeb-9893098c7127 | -11.1903 | -55.9101 | 2026-05-26 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 4d05aa25-8318-3a28-9e1c-d4f18cec7f31 | -11.3581 | -52.9722 | 2026-05-26 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 7d79ef21-7425-30e0-88df-f550b24086c7 | -11.3773 | -52.9496 | 2026-05-26 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 3c65d60b-03ce-31c9-a651-99a3319881aa | -9.5343 | -40.3282 | 2026-05-26 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 141.4 |
| 84ffaa5e-1171-34ca-8118-7dd996ddd94d | -7.1355 | -44.0553 | 2026-05-26 00:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| e2f338df-88d7-3c58-aa94-f0cf73bc26df | -11.3581 | -52.9722 | 2026-05-26 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c7545bd6-c285-31b4-9fa6-a744afe3660b | -11.1714 | -55.9117 | 2026-05-26 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b72d9b0b-0617-32bf-a39a-388a1be23d0c | -9.5343 | -40.3282 | 2026-05-26 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 120.8 |
| e8e6230d-3ea3-32a8-aa95-76718a7ef92d | -11.1903 | -55.9101 | 2026-05-26 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| cd1bb8ec-57f4-3b29-b3c1-502b90560c8c | -11.3773 | -52.9496 | 2026-05-26 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 86f971ba-0f6e-38e0-9884-ac7019892769 | -11.3584 | -52.9514 | 2026-05-26 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 98fc6641-97ff-3913-ae0b-b2320233a6b2 | -11.3584 | -52.9514 | 2026-05-26 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 188.6 |
| bd8685ec-eedd-3368-b374-e41348d36f13 | -9.5534 | -40.3254 | 2026-05-26 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 169d129e-42fc-32dd-964a-2de9fe3b8034 | -11.3581 | -52.9722 | 2026-05-26 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 317c3e18-b6d8-3697-a1c0-47d217c0e0da | -11.1903 | -55.9101 | 2026-05-26 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 580ce271-8226-39e4-a610-3e40cc45c3a2 | -11.1714 | -55.9117 | 2026-05-26 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 60964c7e-7356-3587-b497-88a19ba1c528 | -11.1714 | -55.9117 | 2026-05-26 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1d410ebd-d9bc-350b-96a9-966d3654aa2e | -11.3584 | -52.9514 | 2026-05-26 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 163.7 |
| b36f0d3c-f465-32a1-a1f2-0978b08d6d76 | -11.1903 | -55.9101 | 2026-05-26 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 90c5fdd6-9c0c-3278-b200-f175bf6faa85 | -11.3581 | -52.9722 | 2026-05-26 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 98d86ec8-d1be-3c5e-869e-780a6e1dc37d | -11.1714 | -55.9117 | 2026-05-26 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 9bef70c8-22cb-3aee-b184-8fdf5bc711d4 | -9.3613 | -45.4744 | 2026-05-26 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.9 |
| d68aaa43-977a-339e-a0ac-d2bd3d91e4c7 | -11.3584 | -52.9514 | 2026-05-26 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 9b751248-adb7-3a65-822c-9894fd80378f | -11.3773 | -52.9496 | 2026-05-26 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 822e582a-77a7-30af-8287-5a00a7a3fca5 | -11.3581 | -52.9722 | 2026-05-26 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| f0450491-3700-3fb3-86ef-e3b0599f1ce0 | -11.1903 | -55.9101 | 2026-05-26 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 9f493bb4-4097-3d4c-886f-2985c8d1f8b0 | -11.1903 | -55.9101 | 2026-05-26 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7cb3f385-b107-3712-9e05-a13195feeb03 | -11.3584 | -52.9514 | 2026-05-26 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 797f4e1b-6fb8-3298-abf1-23108f03dcc9 | -11.3581 | -52.9722 | 2026-05-26 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| a7e22373-b109-3a50-bdbe-109ac4bd11ba | -11.1714 | -55.9117 | 2026-05-26 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 47218c6b-4f2f-31cf-82be-439204789087 | -11.1903 | -55.9101 | 2026-05-26 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 57c56b78-fb1a-3dbd-914d-15e90d5e9e40 | -11.1714 | -55.9117 | 2026-05-26 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 78cc1e6e-059f-3d49-b549-96dcd78d3a2c | -11.3581 | -52.9722 | 2026-05-26 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 7befd2ab-f3f0-3303-bc1f-cb54606e66a1 | -9.3613 | -45.4744 | 2026-05-26 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.6 |
| d6f15330-acf4-3db3-b222-7255f4fe1220 | -11.3584 | -52.9514 | 2026-05-26 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 69a53488-83c0-3e1a-8bc7-174282b6a4b3 | -9.3613 | -45.4744 | 2026-05-26 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| a4f43b5e-d2ac-367b-ae5d-4a6e02a36d1f | -11.3773 | -52.9496 | 2026-05-26 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 7d56c6e5-213f-3538-a3b0-651f01e58175 | -11.1714 | -55.9117 | 2026-05-26 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 79c548ae-ad25-3be1-b8d1-6327d9e42ebf | -11.1903 | -55.9101 | 2026-05-26 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c5bc671a-c83e-3c1f-88ab-9e6b1bc983a2 | -11.3584 | -52.9514 | 2026-05-26 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 4b8df84d-9927-37a4-867b-1a51e74a67dc | -11.3581 | -52.9722 | 2026-05-26 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a328e557-c125-369d-8c6a-d336b0526633 | -11.1903 | -55.9101 | 2026-05-26 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e497e813-1032-3a52-8a8c-19655c849daa | -11.3581 | -52.9722 | 2026-05-26 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 7c0947da-8bbf-3482-9c4a-bf1dca31fae3 | -11.3773 | -52.9496 | 2026-05-26 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 42c1e125-8e6c-3905-b181-d100607bde5f | -11.3584 | -52.9514 | 2026-05-26 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 93b9410f-f04e-329a-bffc-01d4dc6af4cd | -9.3613 | -45.4744 | 2026-05-26 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 57fdaf79-977e-365b-844d-b4cc4bbec42f | -9.3616 | -45.4516 | 2026-05-26 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| ccdef841-ce58-3775-bd10-d705f806ad52 | -11.3584 | -52.9514 | 2026-05-26 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 9272877b-a6c8-3e54-ac56-41d90aceb214 | -11.1714 | -55.9117 | 2026-05-26 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c6cd915d-ede7-36aa-90f3-f48a4d5cb88e | -11.1903 | -55.9101 | 2026-05-26 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 7dfe58e5-ccf5-315c-a1ab-7f078c58dc73 | -9.3613 | -45.4744 | 2026-05-26 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c6b761cd-a703-3aeb-b1ae-c92b651e1716 | -11.3584 | -52.9514 | 2026-05-26 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| dc28da55-2cea-3863-9b3f-fa7e5166d624 | -11.3581 | -52.9722 | 2026-05-26 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 6a1edd7f-e40e-3ec0-8ecb-c5adce29b522 | -9.3613 | -45.4744 | 2026-05-26 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d8e4f67e-6432-3478-b3cf-8a7a1e78f362 | -11.1714 | -55.9117 | 2026-05-26 02:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a3332ee1-2119-388a-965e-bcfa27e9de1d | -11.1903 | -55.9101 | 2026-05-26 02:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| aef1a2b6-728b-31f9-89a6-dcd61cc78888 | -9.3613 | -45.4744 | 2026-05-26 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 79daeab4-36aa-3f6f-83c5-ec5a4630cc5f | -11.3584 | -52.9514 | 2026-05-26 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 390bf97b-d343-31e6-96fa-bc59ecf8b06a | -11.3581 | -52.9722 | 2026-05-26 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| afc06add-9ab0-3182-992f-2e9225584d90 | -11.3773 | -52.9496 | 2026-05-26 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 892f93a1-06ef-3a06-8103-eb21094f2be0 | -11.3584 | -52.9514 | 2026-05-26 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| a5aa196e-5ba9-360b-bbf7-d5f0d5a7c376 | -19.7597 | -54.0782 | 2026-05-26 02:50:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 58.4 |
| fbd44f6e-8d81-3cff-9c2b-61f8869ec10c | -9.3613 | -45.4744 | 2026-05-26 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 0e4e494e-0918-3df0-bf8b-6a00b19845d5 | -11.3584 | -52.9514 | 2026-05-26 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| a3dc2e92-f8a2-38ed-b5ad-fe82f2674a01 | -11.3581 | -52.9722 | 2026-05-26 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b2c3d36a-4080-3f28-bcf6-1706fb336ec5 | -11.3584 | -52.9514 | 2026-05-26 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 697ad8f4-92d8-357e-9d1a-97a27856383a | -11.3584 | -52.9514 | 2026-05-26 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 0c6104bf-da02-3939-97b6-74b324ac4b48 | -11.3584 | -52.9514 | 2026-05-26 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.5 |
| aeaba62f-f3c6-3a7a-9a7c-a2db1e1b9d2a | -11.3581 | -52.9722 | 2026-05-26 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 0dae2304-b3b6-31ef-a9e5-82de61d1334b | -5.80962 | -43.20789 | 2026-05-26 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6147676-f7fb-3b0f-a320-1545a518085f | -7.13316 | -44.06277 | 2026-05-26 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c753076b-ab13-33a0-ae7e-bc55927c27e8 | -5.79172 | -45.12918 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 293efc47-a571-3579-a86b-a9244933a881 | -2.96371 | -39.9216 | 2026-05-26 03:36:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3233a354-d817-335f-a1b6-5c15fcb8904a | -7.13742 | -44.07208 | 2026-05-26 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35864a46-7f16-358c-8fae-f5680e7abaaf | -5.53781 | -35.52316 | 2026-05-26 03:36:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b917b25e-c36f-3c31-afdf-91ff5b42ba8e | -7.01341 | -45.00593 | 2026-05-26 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ab02384-59f1-38a0-9645-5f9d704fbfc6 | -5.78966 | -45.12561 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7c4f823f-d946-3493-9c2e-06ea80608c22 | -5.50773 | -35.60044 | 2026-05-26 03:36:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c4a5465c-476b-33ae-82c7-cbeb5c3d742d | -7.13893 | -44.06369 | 2026-05-26 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d2405bc-85d2-3e96-bd79-5e9118b3ff28 | -5.79264 | -45.12397 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c8ddafa6-fa25-3c89-bee6-e9050a2baea3 | -6.08421 | -44.00661 | 2026-05-26 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02c71f70-65ce-3396-b0e8-245eb018a022 | -7.01517 | -44.99648 | 2026-05-26 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60dcfc2e-4d34-35d4-bd6b-1103150c55b9 | -6.72984 | -44.37299 | 2026-05-26 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11e1a205-8c17-348f-b99b-7586b9dc7ed1 | -5.81519 | -43.20882 | 2026-05-26 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb6d96b5-ef96-3c4c-877e-ed7f1eb90968 | -5.30693 | -43.0595 | 2026-05-26 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72c20069-b96f-3264-966d-18cafde9a510 | -5.30732 | -43.06198 | 2026-05-26 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38941529-060b-3583-b5a2-6d2ea37e66d3 | -5.30626 | -43.06332 | 2026-05-26 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6423870d-01f1-3694-960a-42fc10d957bd | -5.81471 | -43.20497 | 2026-05-26 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b61a83ff-aa94-370f-9cc2-6499b6e6a3b8 | -7.01427 | -45.00072 | 2026-05-26 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 626e951a-6a2d-3943-a76b-e86407733f1b | -5.30112 | -43.06484 | 2026-05-26 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 19c203d5-6644-3702-9c5d-b824436d9730 | -5.5372 | -35.52695 | 2026-05-26 03:36:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d3ddeb69-6662-3afc-99ae-fba63fb3ccd6 | -5.79356 | -45.11877 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| ce0f7540-3f84-3fc7-9b9e-dc9c5c74e951 | -5.30049 | -43.06855 | 2026-05-26 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| de942059-aab4-3601-8920-ad32574171e5 | -5.78871 | -45.13079 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README4.md)
