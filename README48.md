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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f15d1c4-08fb-3ed0-b3ba-deb88df8bd0f | -9.44872 | -67.14636 | 2024-10-19 06:10:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c4ef7d5-068d-3750-9304-0108fcfcb430 | -9.5658 | -66.1774 | 2024-10-19 06:10:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c16a705-dad6-399f-a1af-e4c4b5832369 | -8.92702 | -68.70182 | 2024-10-19 06:10:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f811222-ba39-3153-b311-355a3b9fc100 | -9.14052 | -68.8017 | 2024-10-19 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8938f88b-1cfa-3fe8-80d7-1829bfc73e07 | -9.13687 | -68.80115 | 2024-10-19 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b242ae9c-f4b0-36e3-86f0-3a37bd5786f6 | -9.083 | -67.83883 | 2024-10-19 06:10:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1ad0c49-2d81-369c-8d65-1f66508df449 | -9.61107 | -67.43157 | 2024-10-19 06:10:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d37753e-d4be-39bc-83f2-dec3d5520a4f | -9.86519 | -68.80367 | 2024-10-19 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8a8fc880-16c3-3cf7-8df8-7d6cde91976c | -9.45084 | -68.87844 | 2024-10-19 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bdc289d-9c1f-3f77-8ce4-0adf89495690 | -9.44735 | -68.57484 | 2024-10-19 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 803d8ebb-4a10-34e9-be96-e600c6a13ad7 | -9.44364 | -68.57425 | 2024-10-19 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cb56064-f20b-31d6-a95f-4a8a388f5042 | -9.7515 | -67.56504 | 2024-10-19 06:10:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe207dc1-c16e-3a8f-bb42-90a4a20b0b9e | -9.60456 | -67.47649 | 2024-10-19 06:10:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5cb9fda-474c-3b0a-aad8-b68f7cc6efec | -9.43926 | -68.57814 | 2024-10-19 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9cd45294-c6fc-39ff-9cf6-7e8ff204fbe7 | -9.34599 | -68.6729 | 2024-10-19 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8a919b5-d0bf-3488-86cf-85c288c41ceb | -10.76532 | -68.80819 | 2024-10-19 06:10:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1f24af57-8434-3d7c-9d92-1d74dc7717c7 | -10.76159 | -68.80762 | 2024-10-19 06:10:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dbfd220-eb9d-3ecd-8b2c-49d796c12b5d | -10.56237 | -68.8185 | 2024-10-19 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 572a503c-4116-3f63-955b-8b67298c1f82 | -10.55281 | -68.85836 | 2024-10-19 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b92a3846-76be-3cf6-a250-8085d2cec13b | -10.632 | -69.11207 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 365c9487-43d2-3a25-a836-501ae5f90b8b | -10.53802 | -69.06384 | 2024-10-19 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 135cf930-65c6-32fc-8af6-dc029cd44112 | -10.9999 | -68.54622 | 2024-10-19 06:10:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5660ebe0-be39-3e8c-bcf4-8da89891c9eb | -10.8815 | -68.56378 | 2024-10-19 06:10:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eada6dc-900e-3dd0-bb96-c8d9c0bbd9a5 | -10.79364 | -68.84924 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6358e85-b7a5-3a36-8612-a4564609d6b5 | -9.69729 | -64.19048 | 2024-10-19 06:10:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3d1c6c36-37e9-3f47-9433-10a04cb1bf35 | -9.69653 | -64.19619 | 2024-10-19 06:10:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8b24637-1fda-3faa-8ac2-0820be2ea3fa | -12.01043 | -63.51118 | 2024-10-19 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dcfbc335-d3b5-3f2f-a266-ead9dcd116f9 | -9.76168 | -65.24054 | 2024-10-19 06:10:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eae947e5-9dd6-3256-b4e6-75fbde61f55a | -9.6649 | -65.75163 | 2024-10-19 06:10:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cef8183e-0009-3487-a827-458470eab76e | -10.12675 | -65.03307 | 2024-10-19 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69c26d09-205c-3159-ac9e-44c87231ea00 | -10.91812 | -65.10982 | 2024-10-19 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 027cf81d-c3f8-3f08-816e-7e874bb4e27a | -10.91725 | -65.10913 | 2024-10-19 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d45d2bd0-bf02-3076-9a4c-d1f8c55378f9 | -10.91337 | -65.10904 | 2024-10-19 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc781af6-57bd-33e4-8268-5dcf5b0bd319 | -10.91251 | -65.1084 | 2024-10-19 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b3611a1-ddf2-3bd9-92b7-97327a69064e | -8.99158 | -69.41953 | 2024-10-19 06:10:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 681cfbb0-6a76-3a90-8fc9-6095e48d9fa1 | -8.87739 | -69.3367 | 2024-10-19 06:10:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35387294-755c-3814-ba50-800b3904f210 | -8.87384 | -69.33617 | 2024-10-19 06:10:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c405825-5ebd-3fdb-8aa3-1e6976bd74c4 | -8.85229 | -69.43184 | 2024-10-19 06:10:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a49c923-17c7-3683-ad81-042b4d4b5492 | -10.89284 | -69.42693 | 2024-10-19 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4c46a1c-2433-3aef-98ac-18c59a27a0c4 | -10.88923 | -69.42638 | 2024-10-19 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c41a9b2-6d2b-3c81-af52-7b3fb5171427 | -10.88662 | -69.69441 | 2024-10-19 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38ae773b-b2b0-385b-ba86-2b62515dcff4 | -10.86832 | -69.31449 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a88ba9e-ac2e-3903-8a2e-ee9ad2871fd5 | -10.8653 | -69.30968 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44891141-42ef-3005-babf-9e67e5b17785 | -10.86405 | -69.36302 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da33c39f-96ec-38b7-bd28-184cd90c92bb | -10.83836 | -69.31123 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b8222a4-bd8c-397f-a7fb-0c57a3aeb1a5 | -10.78963 | -69.41673 | 2024-10-19 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1008c295-044f-3dab-86d9-1dae10964f3f | -10.78641 | -69.66325 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bc00765-6f3f-35df-8f7d-2e683540542b | -10.77764 | -69.39764 | 2024-10-19 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83c616dc-b3c8-31f0-a445-2cd3a517ccdf | -10.77175 | -69.33595 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11a97dfa-e385-3eb4-859d-c1a93538212f | -10.77114 | -69.34019 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef6b89cb-18ab-3c6d-b46f-eae34c2b27b0 | -10.77053 | -69.34443 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ea4cbe7-4156-3e4a-9214-28e9819b0f05 | -10.75786 | -69.32952 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de50ff21-dd87-3d2a-98e2-63da097bc332 | -10.75648 | -69.33134 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 379032eb-9a43-374f-adbc-752e003e1903 | -10.74869 | -69.44495 | 2024-10-19 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6d2b2c4-85b7-353c-b231-24615d4c60c5 | -10.74192 | -69.61849 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdc1544e-dab3-31eb-b9de-98cf95662911 | -10.71951 | -69.35609 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ef397d0-7527-3043-8b77-152af61b9fee | -10.667 | -69.61311 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cc96096-5016-3960-b113-29b1861206bd | -10.64012 | -69.28498 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba1c4f59-66ae-35d7-b06c-0de8c58f89c9 | -10.63949 | -69.28926 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58004d27-8e21-3149-80e1-25d8491b1984 | -10.56091 | -69.29465 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ac0bd91-649e-35ee-8cb3-39bda22222da | -10.53368 | -69.35561 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aeb9403-bee3-3d52-a0fd-465f7f2b34ab | -10.48324 | -69.18398 | 2024-10-19 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f27e7214-d6ad-3cd6-ae3c-2e8ab0bc7fa9 | -8.93509 | -71.84624 | 2024-10-19 06:10:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd807b09-ada0-37c1-a997-ee7a9c42c30f | -8.85788 | -71.3361 | 2024-10-19 06:10:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8aa69f4-fa37-3502-ba65-c23b0351e1d2 | -8.85734 | -71.33961 | 2024-10-19 06:10:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c13a44a-0b1a-39dd-ab01-85bd797450ae | -8.85401 | -71.3391 | 2024-10-19 06:10:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56b9cda0-46f1-3867-be45-bc303cdb93ad | -8.85198 | -70.5508 | 2024-10-19 06:10:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7daea2d1-d8ee-3cfc-b625-2a217d200b5c | -8.74411 | -70.59063 | 2024-10-19 06:10:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec5f3e24-5c56-3b06-b473-d324f77edda0 | -8.65503 | -71.61283 | 2024-10-19 06:10:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 318732ca-3744-3104-8a65-1f64d3cb9b37 | -8.33483 | -72.61397 | 2024-10-19 06:10:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11100d5f-5537-3ad1-b794-f918809c9222 | 0.99922 | -59.44145 | 2024-10-19 06:16:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5f94a841-2e38-35f5-bf29-ce416c121d4f | -3.43633 | -50.21352 | 2024-10-19 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8dac09f2-7584-34fe-8182-0bbc4e4e365e | -3.42351 | -50.21569 | 2024-10-19 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| ce4ae0a3-860a-3f68-8938-8e9ec665a669 | -2.83862 | -51.28923 | 2024-10-19 06:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| d60b4951-75f7-3af0-9a6d-3ca72c016abc | -2.79926 | -51.34589 | 2024-10-19 06:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 62220c4b-87b2-3b88-93ab-2a39a551be98 | -3.71581 | -51.10788 | 2024-10-19 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 4743f647-2be3-330b-a416-148664926c4a | -2.9817 | -52.84153 | 2024-10-19 06:18:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| cfd2601f-fd12-33dd-9786-b9898c31f912 | -2.9735 | -52.84771 | 2024-10-19 06:18:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| bb432e48-3c26-3fd2-9595-0ee467eb89c2 | -2.95784 | -52.90904 | 2024-10-19 06:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 3a78094b-219a-3315-9cc1-e63c1184806b | -2.95343 | -52.89183 | 2024-10-19 06:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| fba28257-e41f-3c92-8c39-ea3a97517902 | -2.95024 | -52.9151 | 2024-10-19 06:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 5c9399c4-b0c2-3865-a7ec-fad1978ec7a2 | -2.94418 | -52.90698 | 2024-10-19 06:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ff946bd6-17cd-3069-b13f-ae131f595379 | -2.85757 | -53.32003 | 2024-10-19 06:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 1a45b365-2f07-3ef2-b779-d239ebfd4eaf | -2.85459 | -53.34097 | 2024-10-19 06:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 71200275-97bb-3dec-90b0-9f773f6dd6cf | -3.43187 | -54.14771 | 2024-10-19 06:18:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 085d2b26-9c8c-3741-810b-9b742190c288 | -2.80282 | -53.98519 | 2024-10-19 06:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b812e7bc-3ce2-373b-900d-ee0a8f2c1f3a | -2.80194 | -53.97797 | 2024-10-19 06:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 824dab91-114d-3382-b392-be314d1319f1 | -3.06285 | -59.18807 | 2024-10-19 06:18:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 08c36a78-d6ee-383c-80ee-cf1ab1ceaff3 | -3.99042 | -60.39269 | 2024-10-19 06:18:00 | AQUA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f91daf20-42e7-32a8-bf13-f4871f76d1f5 | -3.05157 | -61.66869 | 2024-10-19 06:18:00 | AQUA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 84d0cd79-7f50-397c-99bf-c86b4b7d0f0d | -3.05016 | -61.6781 | 2024-10-19 06:18:00 | AQUA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 02b7b963-4a57-3ed0-a739-753161a59227 | -6.62713 | -62.9306 | 2024-10-19 06:18:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5a793da8-ea70-3e48-ad56-e2c1c7ab04e0 | -9.03666 | -67.44168 | 2024-10-19 06:20:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 19385ae0-e2d1-3191-bd16-87f9badb96bb | -9.03362 | -67.46008 | 2024-10-19 06:20:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 2158e721-a083-3e04-8f01-8110fb4543fd | -8.69764 | -63.21003 | 2024-10-19 06:20:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 04683fc0-3681-348b-81b5-46577cb3f27b | -9.69755 | -64.18645 | 2024-10-19 06:20:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f5d2609d-e4a9-34d9-a8a4-c4128f4f3906 | -10.91427 | -65.107 | 2024-10-19 06:20:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 563152f2-409c-3611-a79a-3828c517c5ff | -12.01352 | -63.50767 | 2024-10-19 06:22:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 5aceaa6c-36a9-3bdb-a08f-a791ced4348d | -12.01206 | -63.51718 | 2024-10-19 06:22:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| b371ef61-4e4f-351b-8072-b2b2adbc07cb | -12.00444 | -63.50623 | 2024-10-19 06:22:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |


[Clique aqui para ver as próximas entradas](README49.md)
