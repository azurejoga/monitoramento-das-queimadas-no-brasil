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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01b1a2c9-2acc-3cae-8d8c-c95091a57e4e | -4.22536 | -48.58053 | 2024-09-29 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebe3e057-478a-36ee-99c5-a29d44d0febc | -4.22535 | -48.5789 | 2024-09-29 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44a2428a-96ba-3b87-8e43-96ad5020aa82 | -4.22408 | -48.58738 | 2024-09-29 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6489d135-90be-3aed-a60b-0f1cb3b392c0 | -4.22405 | -48.589 | 2024-09-29 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a507e19-504e-3309-b43b-c389358a58e9 | -4.22344 | -48.59162 | 2024-09-29 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b21a867b-cef4-35c6-a9b6-ca2b1f2e1edc | -4.19488 | -48.63247 | 2024-09-29 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb89fa97-011b-3d2a-9ec7-fc21cea70f52 | -4.19188 | -48.62775 | 2024-09-29 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8d8082b-48f4-3514-ae21-932b89d39229 | -4.11555 | -49.09837 | 2024-09-29 04:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e844c4c-2c7c-3706-943c-3aea7c134082 | -1.38097 | -49.33858 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36c4487e-0e8e-3c66-9e8e-c2ca8af708fe | -1.37921 | -49.34973 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4142bb8c-9200-3159-8cfa-b3a0774d8cc6 | -1.36096 | -49.33169 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 009a42cd-a866-3940-ab8f-94d57ab87bba | -1.35811 | -49.32745 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82e2a335-3eff-3190-b327-b0e9097de92b | -1.35293 | -49.13459 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6703fac5-c8e5-3aec-9cf0-816e6a12ce71 | -1.34787 | -49.30298 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09a6ba73-79d9-3434-8c18-1b65a8214e6b | -1.34502 | -49.29872 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7e715dc-e390-3342-bd84-673592b98817 | -1.34216 | -49.29446 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90c9e139-f1ed-39c7-b67d-7e1077fed841 | -1.33873 | -49.29393 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2ccacfb-fef9-3876-b83f-b2cbcaf82ef5 | -1.33587 | -49.28967 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f1ac098-a481-3b87-866a-8a135d73aa0c | -1.33302 | -49.28541 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d215ddcf-422f-3144-b738-803add32b5d1 | -1.33244 | -49.28914 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6f09fc3-3378-37b4-bdea-ba673ef3bced | -1.32614 | -49.28435 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0dd4e87-74cf-3a9f-bcbc-977b27c5c00f | -1.29132 | -49.10632 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 374e3baf-a5e3-3d4b-9568-1860de48f83c | -1.28786 | -49.10579 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4bb8402-6906-3615-9864-7c609649058e | -3.14546 | -50.27065 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a42739f-a3c7-3768-8a27-2557b197ba77 | -3.1449 | -50.27425 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 49ee9885-fb1f-337a-8fd8-a80bfdacc92a | -3.14208 | -50.27014 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c596ea55-4be7-3c2f-abcf-9144737a932d | -3.14152 | -50.27374 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70389166-7fbe-36db-a296-e1b9e093a219 | -3.13985 | -50.28451 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06ac2d17-d03b-32b7-a3d6-9846daa608a6 | -3.13703 | -50.28041 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4f38cf6-d042-3365-9504-08e4139ac076 | -3.10878 | -50.48433 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43bc7f14-1016-3554-b584-675a77fc2116 | -3.10822 | -50.48789 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9771ee26-3dac-3893-a21b-e652b254ba36 | -3.10597 | -50.48026 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c779f378-ac69-3ad3-8c29-264724b3a6f8 | -3.10542 | -50.48382 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22370299-5af9-36af-b667-8e661121a88e | -3.10487 | -50.48737 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a32a7d0d-be49-3508-a127-4c35c91c922a | -3.10151 | -50.48685 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b54a723-72ec-3e29-bc15-9286bfcbbcf4 | -3.09255 | -50.4782 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| e9e20955-551c-34f9-8d9e-aece7a3c7eec | -3.092 | -50.48175 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 045beb40-34dd-333c-b029-be4a6a7e7ebe | -3.09145 | -50.48531 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49467038-766c-3032-84b6-54bf173eb59e | -3.0892 | -50.47768 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 10c8f43c-d1be-37c9-88d8-bc195045873a | -3.08864 | -50.48124 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 34a7c258-0acb-33d0-8cc7-2270c697d87d | -3.08809 | -50.48479 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d7b272d-5498-3473-a9eb-f09b7b0589d6 | -3.08529 | -50.48072 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| f616ae42-23e5-3402-9a8b-89f7c09b4163 | -3.08474 | -50.48428 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccd1b6f0-c316-30ac-bfc5-62c9ff2d444a | -3.08248 | -50.47665 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c1c73c0-d413-3cb4-8991-5d63fcb01393 | -3.08193 | -50.48021 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aafb22cc-77b7-3eac-85aa-fd661b8bd0d8 | -3.07913 | -50.47614 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14798506-2fcb-3bec-b63f-4c95a89387ff | -3.07858 | -50.47969 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cfc0a09-6dd0-37c6-8727-f4d1b7fbb666 | -3.07577 | -50.47562 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a94c6016-0b8c-3600-bad1-096b3ca1e467 | -3.07522 | -50.47918 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33f13c0b-d4e0-34d7-8a45-3454ffc83454 | -3.07467 | -50.48272 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b3b210c-3efd-3fc8-8594-0faf0840c671 | -3.07412 | -50.48627 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60ebc3f3-e614-3458-99c3-9a5978c701ab | -3.07187 | -50.47866 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dab191f5-1202-38c0-a287-6f2a159e2477 | -3.07132 | -50.48221 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a7cfec9-575e-3cf3-8b3b-cc860d8a5640 | -3.07077 | -50.48575 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbf89c34-9f18-3432-84e8-9a34de13c437 | -3.07022 | -50.4893 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a3cdb93-1721-3960-aa5c-ea0d2a229264 | -3.06797 | -50.48169 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0f1984b8-63bc-31ad-94c9-2ee8a3063d0a | -3.06742 | -50.48524 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 92a3b4c8-4813-3e8e-b8f0-b31fa3a4d730 | -3.06687 | -50.48878 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83203f45-574b-3841-a4c7-0cf150a6cf17 | -3.06461 | -50.48117 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 91256215-00e7-3869-b083-d128682e1b66 | -3.06406 | -50.48471 | 2024-09-29 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ef05cc3d-0cd2-3403-a9a4-f033068e004e | -3.29216 | -49.50726 | 2024-09-29 04:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1edd4d9e-1fc1-304f-a1c4-28d49e81d7b8 | -3.27495 | -49.1292 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ecea6fd-9f4e-3f14-b0a2-b06ab5c364c2 | -3.27473 | -49.13229 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdc292a1-90c1-3253-a82d-14c28e50025e | -3.27433 | -49.13314 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a4316c4-7745-3fff-9fe4-0a9b38324602 | -3.12943 | -49.20372 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4648c3b-4000-3529-8e0f-6f6cae85b6af | -3.05942 | -49.56172 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0616f95b-beec-3f0c-ad82-00a992ba07dd | -3.05767 | -49.36682 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b88d5f38-1c8e-3470-ab7d-4002f825e2a4 | -3.05597 | -49.56117 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d60fd577-37e2-336a-8776-eddd3488a676 | -3.05539 | -49.56493 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af7c2956-ea7d-3821-b3e4-d6edc9814cff | -3.05252 | -49.56064 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d7f7a16-d394-3a58-bca1-215fc76e4f3c | -3.05193 | -49.5644 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6989448d-0d6b-3dce-9e2d-fe54aa34b196 | -3.03759 | -49.54292 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6450acb5-b555-31a3-9f6d-0404b97403b4 | -3.037 | -49.54669 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4a50e777-6cc7-3b50-947e-daf5689248de | -3.03643 | -49.55044 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eeacde37-f27f-3877-b223-128f5167a7d7 | -3.03413 | -49.54239 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 440be8d7-5656-3ffb-9847-b294452421d2 | -3.03355 | -49.54615 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| da388f39-5197-3206-9511-483f6ef79d8b | -3.03297 | -49.54991 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 627d7e4e-92a0-38cc-81a0-b8a663770393 | -2.90215 | -49.55744 | 2024-09-29 04:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 869ffc65-bc20-38ab-a4e2-eb370ffe49f7 | -2.90157 | -49.56121 | 2024-09-29 04:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae9ca26d-ad4a-36aa-84b0-b5f233103515 | -2.89695 | -49.11759 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0987551c-bfd5-3afe-aa2a-a1240f239139 | -2.89405 | -49.11314 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7b471d5-cfeb-3d0d-af36-616c847da69d | -2.89344 | -49.11705 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6d3f75a-bc5d-319f-9da3-2cd11bf53612 | -2.49042 | -49.05473 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 215081dd-1d03-3bec-874e-1e7f8ca0d19a | -2.47759 | -49.15993 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79b1077a-0123-37de-b34a-8655a0d525ac | -2.47699 | -49.16379 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f89f455-ad96-3121-808e-80be11d7b5bf | -2.4747 | -49.15554 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b4e2a277-93f3-3c48-9e87-dc70c7cbbfee | -2.4741 | -49.15939 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2bbc2521-22b7-3939-982a-b255c50323a0 | -2.4735 | -49.16325 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6265b441-a4be-3d25-aa58-f8af70d6be91 | -2.47121 | -49.155 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f05fee89-e1cc-36e9-947e-6e7b3afb1a82 | -2.47061 | -49.15886 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 50ccd07e-a4f2-373a-9600-0b4ae5b5fb19 | -2.32138 | -49.16834 | 2024-09-29 04:46:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fd5f0b5-0f5b-369b-9c34-93e40250284f | -3.40389 | -50.36114 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d6fc5c7-8a99-3d4a-996f-1074aaa4db83 | -3.39996 | -50.27589 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f2fd011-0f5d-3740-8ab6-f0529821537d | -3.35115 | -49.78133 | 2024-09-29 04:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a46f1dd-e3f1-32e4-a400-7f4eab2bed2a | -3.34772 | -49.7808 | 2024-09-29 04:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92844fbc-8dfb-38b4-bd7c-9d386cf1232d | -3.33357 | -50.30253 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 378be993-2211-3581-a8fe-e228998bef7f | -3.33302 | -50.30612 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 700ea8de-4139-3664-903e-04f90898c002 | -3.32964 | -50.3056 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2bf405c1-2f0e-3231-b724-594c88a50038 | -3.32909 | -50.30919 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59a8d0b1-5082-3066-9324-92987b285840 | -3.32571 | -50.30866 | 2024-09-29 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README38.md)
