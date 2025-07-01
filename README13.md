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
| 44e97382-b75a-376f-9700-f5a90441eedb | -7.54418 | -48.58636 | 2025-07-01 05:12:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24810c23-1e4a-3497-a649-02a189b6aff4 | -8.72816 | -47.99152 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43368916-1997-3a4e-b016-358e891ac91d | -6.21248 | -43.36227 | 2025-07-01 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4728c48b-ad28-36c4-b6e5-5f81258f4718 | -5.56902 | -45.21352 | 2025-07-01 05:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ca48974-48e3-3b82-9f70-f887b86e914a | -8.67191 | -51.46962 | 2025-07-01 05:12:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28bc8cc8-ac59-3ad6-b88c-31e2344769ca | -8.85912 | -47.95377 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3cf7661-dd7c-334f-89b9-3f69ee3cb299 | -6.2105 | -43.36371 | 2025-07-01 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| cd8c6808-1065-3d0b-8d67-a0cae37bd0df | -9.68742 | -48.33889 | 2025-07-01 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29e79e56-f816-3421-8b07-5a7978106b10 | -6.21156 | -43.35609 | 2025-07-01 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a0c7b6c0-d8de-34fb-ab3e-33ae6243b552 | -9.18021 | -48.84405 | 2025-07-01 05:12:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d81bf908-4aeb-34d0-980b-ba3d9ca8cef4 | -8.72604 | -47.98814 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d156e02-1faa-3203-8cd5-1fdbab4ca012 | -6.2135 | -43.35455 | 2025-07-01 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ce792c3c-07ba-368e-9075-9bc8c214fa64 | -6.17731 | -47.27472 | 2025-07-01 05:12:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 360e77a1-1858-38ff-99a2-ead36e5ce915 | -8.85704 | -47.95494 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c82c8ae2-1616-324d-b3d5-6767e9a80a0a | -6.57002 | -47.3751 | 2025-07-01 05:12:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff57ca3f-3548-3daf-8c1f-4a6871386258 | -6.17159 | -47.27399 | 2025-07-01 05:12:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab080da9-b699-3692-b15e-ca4015f18fd1 | -4.37738 | -48.0852 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbfa1369-5877-3d48-971e-2093a75a8948 | -8.72302 | -47.98701 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8d37300-5e89-3308-bb54-70c91321cd3f | -7.61386 | -45.75381 | 2025-07-01 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 85cad057-750e-3b1c-be92-fd7d212475a9 | -4.5498 | -48.00716 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7981877-22d2-33f4-8419-08a4a100d3a6 | -2.90779 | -54.48707 | 2025-07-01 05:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4397fc0a-fe10-3446-860d-c04f22437afe | -8.72556 | -47.99189 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 941ae4de-194a-3038-adbd-9e931a1f33f9 | -4.54258 | -48.01941 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bc1ce60d-5a1a-374c-88e6-055d95fbd562 | -4.5421 | -48.02266 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 038f95a1-ae27-3c8d-8469-10ac7e118c20 | -6.54178 | -54.96997 | 2025-07-01 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a63e186-7ace-371b-802a-fa17f16972d1 | -9.57169 | -49.10664 | 2025-07-01 05:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6af15f8c-14f7-3574-9ade-a0082cdcffeb | -9.57698 | -49.10742 | 2025-07-01 05:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 121e5388-cb82-3395-b908-be5bed617178 | -6.48296 | -43.74574 | 2025-07-01 05:12:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ca99d36-888b-3d2d-a442-e53facc7a5d5 | -8.30698 | -55.10557 | 2025-07-01 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c5cd332-c74e-3ab7-a18f-8643976ae862 | -8.72202 | -47.9945 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7080cdb-31f9-384e-8f58-3705ff4f7dc9 | -6.48096 | -43.73975 | 2025-07-01 05:12:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 664f7bce-ad7e-3de2-92ab-c201ae1560a2 | -4.3721 | -48.08451 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43de5d04-964d-30bb-aaff-17c7d5e64793 | -7.16158 | -49.51241 | 2025-07-01 05:12:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f74a373-5656-375e-bc9f-1e4b594f82e0 | -8.37927 | -51.07318 | 2025-07-01 05:12:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ca3a8ca-5481-361e-b919-cf2a6f8624a6 | -9.18066 | -48.84062 | 2025-07-01 05:12:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| afa0c3bd-3aeb-3ffd-84c3-217d1b4ec3cc | -4.54163 | -48.02592 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 271f4755-2aae-318d-be12-a83db4846a16 | -4.5373 | -48.01853 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c64c3d08-ebcc-3e4c-9412-e7ae054264aa | -5.56827 | -45.21888 | 2025-07-01 05:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c4f97ea-eee2-3a81-a708-4f4ea01c1cba | -4.55028 | -48.00388 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e7d3c55-f0d7-35b1-becc-84a10e5bb6d0 | -6.4757 | -43.74578 | 2025-07-01 05:12:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8085543-739d-30e0-a359-074cfb7332c7 | -8.37472 | -51.07253 | 2025-07-01 05:12:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d203aa05-e8b8-3b6c-86a7-8fa688219050 | -6.54529 | -54.97052 | 2025-07-01 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa562e20-eba1-31e2-92d8-83c18c737a8d | -9.12727 | -49.67749 | 2025-07-01 05:12:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 674b02c3-f978-3a21-8781-b69bb052f066 | -7.24735 | -46.40134 | 2025-07-01 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c6267b5-4193-38d9-aecd-49011eb4ec89 | -6.2053 | -43.3607 | 2025-07-01 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02b10428-b69a-3947-96b2-59dc0899cbb8 | -7.09394 | -49.16681 | 2025-07-01 05:12:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fe3674b-3094-3c14-9d57-08703b378a5d | -9.02778 | -49.58941 | 2025-07-01 05:12:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaa2a573-74f5-37df-9dfb-1fc78ccfe964 | -7.09436 | -49.1639 | 2025-07-01 05:12:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30bed740-4830-3778-a56d-291d30e0ce19 | -9.02818 | -49.58644 | 2025-07-01 05:12:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0527ab6-58ad-366f-9b82-cd38faee3348 | -7.61454 | -45.74868 | 2025-07-01 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f68db4ab-a7de-30df-9595-9c885956115e | -9.57211 | -49.10336 | 2025-07-01 05:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3bf90572-2f34-39e0-b96d-325acf9e88dd | -4.53682 | -48.02179 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1ebcc66-cdfc-3690-bf25-e20993e651c9 | -6.57055 | -47.37128 | 2025-07-01 05:12:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 42a8d547-7e05-3fde-9491-57f0a2e426b8 | -6.28834 | -43.68724 | 2025-07-01 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 459cf0ce-7a15-3558-84c1-b5218b3bddbf | -6.54409 | -54.97831 | 2025-07-01 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e13bb4bf-11cd-31c0-9dda-de97dd97954b | -8.67635 | -51.47024 | 2025-07-01 05:12:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 787a5fdd-7417-31a6-afac-d1eeaae911c9 | -7.09762 | -49.16454 | 2025-07-01 05:12:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b3b68f7-b32c-32db-8f87-febaf4522c6d | -7.62025 | -45.75483 | 2025-07-01 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a3f286fd-d72b-3e41-9206-2e8c717ee95c | -8.86319 | -47.95212 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cdd43d2-86f5-3b93-b233-737deed6d8b5 | -8.97512 | -49.86246 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbdf4eff-2fdd-336a-b2a2-36e2bcee99a7 | -4.31466 | -48.08004 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17400c67-f867-3503-b887-5c11b495846a | -6.17647 | -47.27246 | 2025-07-01 05:12:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fec75fd5-7ea8-356e-86ef-c1006e4d4285 | -7.09214 | -49.16665 | 2025-07-01 05:12:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 905910c4-656b-39ba-840b-6961b2e8c9ce | -4.37965 | -48.0694 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0dc148b-f9d8-3adb-b065-0d69d47b428c | -4.32474 | -48.08456 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd65d9a9-545f-3f9b-94df-29d10e7de33c | -4.31897 | -48.08723 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0f8e642c-db08-350a-827e-e384560e8f01 | -4.53634 | -48.02506 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bf49a2e-a502-37dd-8dd4-cf9ebd263575 | -6.29552 | -43.68779 | 2025-07-01 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 256d2f2b-3205-3877-b666-14c222fbd411 | -8.85755 | -47.95117 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66a5555c-7b30-3745-a607-f15c161174d9 | -8.85961 | -47.94995 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff666a01-2cd2-3693-b8cc-924520422db5 | -4.54883 | -48.01371 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ba4dc2a-1f0c-31d9-9ad0-3e2ad324224a | -6.47995 | -43.74708 | 2025-07-01 05:12:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 339909e8-2e5d-33b3-9d44-8a8c4da31a91 | -8.72652 | -47.98442 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ab24413-1142-30c1-86d4-a19e1f229b25 | -6.2964 | -43.68118 | 2025-07-01 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| a652805c-6fee-3cac-b205-04364bb61cfa | -7.24797 | -46.39681 | 2025-07-01 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6063bf04-b5e9-34fa-b149-54fd540a269c | -4.37438 | -48.06862 | 2025-07-01 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35757d75-3ade-306a-88b8-f0b8e5e16ccc | -9.6818 | -48.33838 | 2025-07-01 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c791729-fcce-33f5-970b-0c2b538b9db4 | -6.54469 | -54.97441 | 2025-07-01 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1caeb519-91f7-3146-b4ff-32dbb4f4695e | -8.72252 | -47.99075 | 2025-07-01 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cac09172-e570-37d1-980e-b50710e0f604 | -12.62893 | -54.22661 | 2025-07-01 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 809a1101-b6f3-37d1-9616-362fefc0ee1e | -11.57235 | -48.14211 | 2025-07-01 05:14:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5b5ed23-f8f9-3769-ac96-b91e8781b597 | -12.98001 | -54.68233 | 2025-07-01 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 344a0cff-cfca-36c1-be24-0616a2fd2192 | -12.29158 | -48.81002 | 2025-07-01 05:14:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23c2eedd-9957-3ef9-8162-bd6b5f165d24 | -14.44202 | -48.87409 | 2025-07-01 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1d8e52a-a463-305e-bca9-3894b1bc7c77 | -10.02614 | -54.31699 | 2025-07-01 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 450b09fe-0f7b-37b8-84f6-8b678aa2fdf0 | -10.12287 | -52.34399 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1f2f4b5a-c0a3-3592-bd5b-a9af5bbece7c | -10.87639 | -56.4361 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df3f0cdf-2831-30ba-9b6f-f8819e1e5e1f | -10.12834 | -57.78112 | 2025-07-01 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6c1bedb-b4c1-3aae-bc21-6be68ae9764c | -9.09128 | -59.47448 | 2025-07-01 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40a858cd-4f2a-320d-8b47-cee4790fcd68 | -10.11859 | -52.34338 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36dcc33d-3aa1-3211-8f08-43544b13f491 | -11.19795 | -55.91642 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b903308a-594e-32c5-9782-566c337b3b23 | -10.12601 | -52.35275 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17bf3b78-a2aa-3d4e-9000-d20f64d1afba | -9.24563 | -58.75736 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bf3821d-591d-375d-b4f5-6855b18a08ab | -10.87391 | -53.7629 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8fc0867-c21b-3832-a4fd-8c30a0b0cd87 | -11.14175 | -53.9256 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23ae0900-32d6-3524-aaed-7e0590789234 | -9.25343 | -58.75138 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16428cd0-a3de-3612-93d2-7f3a24c7245e | -9.25117 | -58.76549 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52e4e503-9e60-340c-85dc-6c25eee8b51a | -10.88101 | -56.45232 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8479140-6298-31ca-9144-3ca48e707b5b | -10.86925 | -53.7674 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f9e5c79-d0f6-387e-bd93-2d67d8d2fb4c | -10.89363 | -56.46204 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README14.md)
