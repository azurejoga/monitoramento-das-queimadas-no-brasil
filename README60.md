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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70d5b465-3d9b-3061-b9d9-153979db6878 | -2.68261 | -49.33046 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1139451f-ce27-3086-aae9-c6855fb8bad3 | -2.65681 | -49.25493 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fcab53e-a413-3acc-85c0-d5f3d2f802eb | -2.65627 | -49.25843 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72eb5ca8-a908-3092-b1b7-68400f6fefb6 | -2.59395 | -49.33464 | 2024-10-30 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4861d33e-5e16-3965-8fe8-7a48041615f1 | -2.58855 | -49.75635 | 2024-10-30 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21da2915-cafb-3e58-a588-1a515fd0a467 | -2.58657 | -49.66049 | 2024-10-30 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49161fe0-b281-38b4-b6d3-ddc2339348c6 | -2.58523 | -49.75583 | 2024-10-30 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb74189d-c99c-3bc3-a90a-153c43239754 | -2.5615 | -49.45432 | 2024-10-30 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be450cf9-a6bc-31aa-899e-21250c98f94e | -2.54699 | -49.80643 | 2024-10-30 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ed7eee4-8c16-3641-8faa-26614f7b20ab | -2.49127 | -49.30048 | 2024-10-30 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62dd6484-a01e-3578-87f5-d407697e3185 | -2.39056 | -49.38111 | 2024-10-30 04:44:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d52ec3a7-99a3-34b1-96f2-55c9f5ff129b | -2.45719 | -48.91428 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a84a3c8e-b60a-37be-bc37-96b8535fc04b | -2.45529 | -49.15894 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b01a6302-8407-3c1e-adb3-54e315b4d4bd | -2.42692 | -48.88786 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3478a5c6-0c49-3fd1-8c56-0d8ddbf6e7e7 | -2.40295 | -49.81893 | 2024-10-30 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4a198ac-3c2e-331b-8263-a9624f9141a0 | -2.40202 | -49.02495 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90950809-53b6-3b1a-8508-febeaab13bad | -2.38842 | -49.1773 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a737cf85-482f-3d5e-9705-41bd5e5815b5 | -2.38513 | -49.19827 | 2024-10-30 04:44:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16415e51-4448-3374-80c6-72b9956752a2 | -2.37412 | -49.02784 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0a8b607-76d1-3800-a711-5a0f4e2fba3c | -2.3648 | -49.08755 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b4cea35-7d32-3880-a06f-b6330386afdb | -2.36091 | -49.09054 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbb526fe-4c9a-3feb-8b1f-5c263d6d125e | -2.34271 | -48.91135 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e557e779-c354-3c8c-861e-99db4f56b722 | -2.3368 | -49.1014 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 067c6700-5261-3103-a9b5-cd6c1cc48034 | -2.21464 | -49.57405 | 2024-10-30 04:44:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50efa5e4-d7ed-3d26-ae1f-984449a8f8e4 | -2.21077 | -49.57699 | 2024-10-30 04:44:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1635c75e-3a86-3dcb-bade-7197725cc5b8 | -3.17847 | -50.5905 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 05d928d5-0bab-3613-9615-35b0048e003e | -3.17569 | -50.58652 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e062559f-6b83-3d95-b64c-bb826ff8eb88 | -3.17514 | -50.58998 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2be17f5b-fc1c-3669-8476-ea9f2fe8557e | -3.17237 | -50.58601 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49264299-e843-3122-b580-d77f70a5e0ab | -3.17182 | -50.58947 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ac740f65-39e1-34d5-8c53-1a6748e7fe63 | -3.16904 | -50.58549 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61e89b58-55cf-30bf-9d92-0e4e881eece0 | -3.1685 | -50.58895 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8434b4ca-c0ce-35c9-bc85-8d7f02caea99 | -3.16518 | -50.58843 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 77e6ddbd-ef95-353f-b6a7-84783d57d366 | -3.18398 | -50.3826 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 728e7dd3-18a8-3b28-9412-3a0b2c618900 | -3.18344 | -50.38605 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb00d2b8-9e1d-3819-bc4c-8870d956e2b2 | -3.1829 | -50.3895 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c88244b8-9d37-31d3-81d8-11acb5f838fa | -3.18235 | -50.39294 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b696fe5-a698-30df-ae94-ff787f382230 | -3.18066 | -50.38208 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30f3e196-2def-3ac8-b02d-a5b9f7d4c137 | -3.18012 | -50.38553 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe9295f6-d02b-3c9c-9405-7f7b546ffc9f | -3.17958 | -50.38898 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0b9aaf1-2825-32d1-a955-9b49abfbbee2 | -3.17903 | -50.39243 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c95eafe-c18c-328e-8836-0903a2cbcf9f | -3.17849 | -50.39588 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 378e2f36-c717-39b0-9e2c-90d1a30d2058 | -3.1768 | -50.38501 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fee94af4-96f0-3dae-ad85-461d47dbc7b9 | -3.17571 | -50.39191 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 076ad642-2f4e-3164-930f-e2ddd926dd65 | -3.17517 | -50.39536 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c360f91-98b0-3c7d-89ac-c82481cdd23d | -3.17458 | -49.53492 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f1eb503-abd1-342c-b9fc-89516ec5977d | -3.17291 | -50.58255 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a27a52f1-a25c-3743-b163-8f97b6de1651 | -3.13384 | -49.17043 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab60e9a6-8485-3813-9926-956d1ac4f03e | -3.13329 | -49.17396 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1264fb91-4c76-3dce-8596-c6ae4532005b | -3.12532 | -50.36639 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bcbfc4e7-09f6-38ff-a4aa-e1da656476e3 | -3.12478 | -50.36983 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ab0cac5-4f27-3d17-b518-587ae213ba57 | -3.12465 | -49.29492 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72816c04-dbb5-3854-851e-5e56f5108b22 | -3.12411 | -49.29843 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e5facba-83ef-311d-93fd-55f69599d99d | -3.122 | -50.36587 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2499e9e-d708-3ce2-a1a5-4fb158c19cb6 | -3.12146 | -50.36932 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a19fb20-9b06-3159-a680-e5fa1507d757 | -3.12131 | -49.2944 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 197f61a4-79a0-3ac8-9da0-303ef63a5afe | -3.12076 | -49.29791 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8435d945-1647-3f07-8312-51d0026a7074 | -3.11797 | -49.29388 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5ac10a4-7b63-3488-a9a1-a9b3735bf4fc | -3.11742 | -49.29739 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14b4b8fa-d1ea-3718-b0e8-26d5422d6a58 | -3.11599 | -49.39392 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f567784-4d73-33b2-88af-ff1a28af8677 | -3.09265 | -49.21453 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b96f61f8-ceb4-32da-bedf-f4d970dac1e6 | -3.2358 | -50.5887 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58909f90-0f60-394f-a50a-23449459adc2 | -3.23302 | -50.58473 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 57ece03c-2246-3f1f-9a6c-8d1e41e79898 | -3.23247 | -50.58819 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fde3af38-fb79-3961-8bb4-7608f9cca9e7 | -3.23193 | -50.59164 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8730bb2a-89de-3149-b7a8-2f94e92993f7 | -3.2297 | -50.58421 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b3aed35b-494c-3aef-bdca-c04b1e592f35 | -3.22915 | -50.58767 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 80520ffd-6521-30df-a964-26ceeb37e91e | -3.22638 | -50.58369 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06acb3fc-8909-3bf0-ac0e-2cea6341c83e | -4.52544 | -50.41269 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc19e9da-c336-3e2c-a68a-cc949ce26a48 | -4.5249 | -50.41614 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af3eadd6-f60f-3028-8f1e-80c3aec3f141 | -4.50341 | -50.18982 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e4d69f2-4492-3961-80ff-701cf392eed9 | -4.50009 | -50.1893 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45ab249a-ce7c-3cba-8ca7-ee36b27d8858 | -4.47209 | -50.25934 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0f49e59-7f7d-3e66-adde-f9ebddab5519 | -4.43069 | -50.15719 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed1a8da1-2469-3f70-86ec-58b4b3e00b78 | -4.43015 | -50.16064 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00102083-974f-39ab-a45a-4ca46272524e | -4.42623 | -50.46453 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b136295-238c-3a15-b453-656b7638cf7d | -4.40507 | -49.63241 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd955fe7-b550-3a30-b37c-840362703d1e | -4.40172 | -49.63189 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ef6c252-9d0a-3ecc-8810-d20afabe68e9 | -4.39797 | -50.32207 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9df1d73e-4823-3911-be09-b91284993492 | -4.39465 | -50.32155 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d892189c-2bd9-327f-91e5-2ccf683432b8 | -4.29788 | -50.74168 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93e2d8e3-d9d9-331a-b202-23a9d45fea0a | -4.29456 | -50.74116 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1474488f-a19a-3031-94fc-e9f02a539da7 | -4.28298 | -50.43102 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f78f27e5-4d6c-35a0-b0a7-38fb017251d3 | -4.26839 | -50.66982 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 2bc66c75-961c-3007-b6cb-96b60c8b46b0 | -4.26785 | -50.67328 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| fca02bd9-213f-3ad4-8af8-a443c923f820 | -4.26773 | -49.96455 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df5293d1-774d-30ee-85ab-95e8863549a5 | -4.26562 | -50.66584 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 9364f3d1-0bb0-3873-a9f3-e7a60f7ab4c7 | -4.26507 | -50.6693 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 05961fe4-5313-3bc9-bafc-260dff48852f | -4.26453 | -50.67276 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| aea199f5-0384-3e19-9c16-395dcc7bf555 | -4.26398 | -50.67622 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4f51f478-39c1-3154-97f1-dc27c339cc25 | -4.2623 | -50.66533 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e87b56d8-3490-3ab6-aa0f-124fbbaaf722 | -4.26175 | -50.66878 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 45ddca05-c384-3250-b141-2bd072f58ddf | -4.26121 | -50.67224 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| aea0daf4-d63b-3a03-a55d-9837c916acb4 | -4.26066 | -50.6757 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 661eace3-7734-3830-aaac-21c7bf7de1ab | -4.25898 | -50.66481 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 182cfef1-5cd8-318c-a0b6-04f3dbc7b34b | -4.25843 | -50.66826 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e5315d15-d075-3e2f-9276-8665d81bce09 | -4.25789 | -50.67172 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2cbf8ef6-9816-3325-9631-0c457f3650d1 | -4.25706 | -50.66051 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 215e8f2b-3000-3b84-89b2-3bffa7fe4187 | -4.25652 | -50.66397 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd437318-a6b4-36dd-91fd-71a68b3a0456 | -4.23834 | -50.69296 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README61.md)
