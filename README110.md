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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61171e98-2f4f-3171-aa84-d4f175612439 | -3.25627 | -52.85245 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55e1e506-73db-3023-b0d4-ce8c66b713a4 | -3.10655 | -52.22623 | 2024-10-07 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0080cdd3-347a-32c9-b665-fd82e879997b | -3.10593 | -52.23022 | 2024-10-07 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 63c72596-e7b2-3a8e-a7f8-734e0d7808a6 | -3.04169 | -53.03956 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6768e95-3a9a-3c84-8eef-7ee589f62dff | -3.04115 | -53.04309 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20297068-8fbb-34e0-b2e4-1c05652eb09c | -3.04061 | -53.04661 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5271ab3c-ec43-346f-8edc-b1c61d1f4023 | -3.03764 | -53.03893 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ed2c3c8-e522-3035-a7d8-fc56d21d0075 | -3.0371 | -53.04248 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ebe9b59-0326-375b-8b8c-7f4e9c5c6237 | -3.03656 | -53.04601 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faafcdb0-81b1-38c1-9a88-2bb2b83e87ac | -3.03359 | -53.03829 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe8295b6-1770-3421-acdb-9921c2112300 | -3.03305 | -53.04183 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab7164d3-d529-3593-93e7-98e8f46289c8 | -3.03251 | -53.04535 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67fe4d6e-eb58-3f69-badd-3b0d8cdcf3ea | -2.88418 | -52.90587 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b46c4416-f816-3eac-acb5-cffc87c9fbda | -2.88122 | -52.89799 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 959ea6f2-315e-32c5-ad25-28eaa7a7005e | -2.88066 | -52.90161 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 49b22c8b-985b-3690-99b3-0d4a80d09cdb | -2.8801 | -52.90522 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 807e0f83-1884-390f-9305-2741efd9f135 | -2.87954 | -52.90883 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 13f7d981-3083-3eeb-990d-6a04f8f85f47 | -2.87898 | -52.91244 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c350d37d-de0d-32ad-905c-dcc8b4cf5346 | -2.87842 | -52.91602 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88072063-0cb7-39e5-b3e6-122b7acbfd0f | -2.87772 | -52.89367 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ac3b5a3-6d7a-34cf-a2fe-c89069856fc5 | -2.87715 | -52.89732 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fc73c09-5442-355d-b139-1ae86f5bee99 | -2.87659 | -52.90093 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 479eea69-5f04-3d7e-afd0-cb11b607fe3b | -2.87603 | -52.90454 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 061f6887-1596-3892-a1de-6030f94d30a7 | -2.87547 | -52.90815 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ea9be2bf-c53f-3fa2-b3f3-ec6efad05959 | -2.87491 | -52.91175 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ddcc6b78-eba6-32f3-bb08-6502cba2a472 | -2.87435 | -52.91535 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a8f9335-f3ab-373b-81ab-cc226c42ec8a | -2.87308 | -52.89664 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 311fe6c9-5eb6-329a-b880-de13dd4cae16 | -2.87252 | -52.90025 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b36d698-e157-3871-9315-70f3ce6fa77b | -2.87196 | -52.90386 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2750c20-9379-3b17-a747-e9d44df460bd | -2.8714 | -52.90746 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f51f59c-9d87-36f6-91d6-a96554d66e64 | -2.87085 | -52.91106 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da5ebf3a-4ec3-378f-bbbc-9b2d848dbc59 | -2.87029 | -52.91467 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42dc6f08-9b24-34d7-a057-a7056ef66813 | -2.869 | -52.89596 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 184c68eb-cb7f-3024-8a3d-13d99ed6bfdb | -2.86845 | -52.89957 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c16b8056-7a9b-30b3-a9c0-62fe6f572610 | -2.86789 | -52.90316 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ca6a88a-888d-37c4-9fbb-b9c24b8b931e | -2.86733 | -52.90676 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 344a2e5b-06f5-3c44-b89e-6d55a0671f0c | -2.86678 | -52.91037 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee2c8108-cc1a-3be1-a27d-2fb9a9513225 | -2.86622 | -52.91398 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72152400-4b0c-3db4-99eb-2c9919b8c211 | -2.86493 | -52.8953 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48e43285-e6ec-38bb-a7a0-2749a1232f0b | -2.86437 | -52.89888 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db8e566a-f426-3786-9216-698ee7e8e547 | -2.86327 | -52.90606 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| befe86f6-34e7-3e67-b54d-a04d64059cab | -2.86271 | -52.90967 | 2024-10-07 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0f07a8a-0d21-3c3f-b902-1b67b125fe09 | -2.22708 | -53.69397 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64f4b489-55e7-3762-924c-4e3f1a1bebfc | -2.22637 | -53.69871 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d51578f-8feb-365b-a175-1b9e0135b1e6 | -2.22527 | -53.69671 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8238a6c-a0e0-3a0f-80a5-02f1cfb7bd94 | -2.22143 | -53.69609 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9475fe10-6bd5-3beb-8574-f612e656febf | -2.21994 | -53.70555 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b05bca3-3ef1-369a-a237-2b17df34c0bc | -2.21907 | -53.68604 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f823025-9e76-3c8f-971e-f593af49e32b | -2.21833 | -53.69075 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a3b1c04-2171-3741-9813-69f90db9c9fd | -2.21759 | -53.69546 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2dc8e024-b5ea-3c89-b1ee-7475ad34cc11 | -2.21685 | -53.70019 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3191a92c-9761-3ae8-8464-22beaadf5bb8 | -2.21611 | -53.70493 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7195b62e-426a-3aae-b60e-3d1b9732e7ef | -2.21536 | -53.70968 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9aa87dd8-494e-3745-b3d0-1ad9c17fdaf7 | -2.21522 | -53.68544 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 705ab7f7-d90f-3148-8d79-2d1debfbf770 | -2.21449 | -53.69014 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3361e0f5-65ad-3de5-8097-737a26bc46f1 | -1.22535 | -54.22088 | 2024-10-07 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ce94c124-c70e-3fdc-bd8d-e535c3ef92a5 | -1.13126 | -53.63617 | 2024-10-07 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 447b054a-eefb-3868-a6b5-6f03697cb9a0 | -1.12818 | -53.63101 | 2024-10-07 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 298a588d-d84a-3e44-b131-91fe5cf780b7 | -1.12509 | -53.62589 | 2024-10-07 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9182cd92-891e-36f8-bf92-54c2325f0354 | -1.12434 | -53.63068 | 2024-10-07 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efb8c4cd-d150-3c7c-8ab8-b89745d0844f | -1.12126 | -53.62547 | 2024-10-07 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a18ce5bd-a4b0-3c82-bac6-a59b93475067 | -1.04212 | -53.53917 | 2024-10-07 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc7ebeb0-e23a-3cb8-9364-aeeb3cfec4d3 | -1.0383 | -53.53859 | 2024-10-07 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 799bbbdf-d2bd-3232-bb8e-3ae9dc6ec663 | -1.03756 | -53.54329 | 2024-10-07 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78bad05a-f4e9-36ed-b004-9c34f0965f06 | -1.03101 | -53.73234 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aa9f5538-5ba3-379c-a8d6-2fc5e185e5d6 | -1.03024 | -53.7372 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 21796d20-5b0f-34f1-9b9f-387d3168039b | -1.02801 | -53.72691 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a3fc7d3a-e983-39e9-b724-ffb4b62c8ab9 | -1.02725 | -53.7317 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f4c859d2-d714-3b0c-97f6-c1f148e952e6 | -1.02648 | -53.73657 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 009c1d45-c1a8-345b-a86c-cc42b68c979d | -1.02419 | -53.72659 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80bffbd8-c845-392b-a351-b84c061216e4 | -1.02345 | -53.73128 | 2024-10-07 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06fea0b0-1885-3e3a-bb0a-1e73d88daa82 | -3.126 | -53.74213 | 2024-10-07 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bca1e8f-f0cd-3de1-a727-ab2efcfa0ff6 | -2.81214 | -54.3602 | 2024-10-07 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 54ee17eb-4ad9-3712-a5e6-ba3a539f0428 | -2.90003 | -59.21829 | 2024-10-07 05:14:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ec3d784-2609-30d5-82bb-29b6d6d35a02 | -3.54727 | -65.02197 | 2024-10-07 05:16:00 | NPP-375D | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5623869a-b547-31f8-b7bb-d2e327b7e20c | -3.54652 | -65.02663 | 2024-10-07 05:16:00 | NPP-375D | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5088647-2537-3eb9-85c3-57b54067a697 | -3.5427 | -65.02121 | 2024-10-07 05:16:00 | NPP-375D | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 180fa656-09cf-39cf-9920-06c5f39dfb6e | -3.54194 | -65.02585 | 2024-10-07 05:16:00 | NPP-375D | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f2a972a-c9d6-3cca-96dc-e446e5a1bea9 | -3.54119 | -65.03049 | 2024-10-07 05:16:00 | NPP-375D | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db98021d-e5d3-3138-9916-8734d1a504c4 | -3.53737 | -65.02508 | 2024-10-07 05:16:00 | NPP-375D | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb2b7707-d6e7-3a23-9854-36f15e8f82c0 | -3.53661 | -65.02971 | 2024-10-07 05:16:00 | NPP-375D | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bae08380-6139-3b1d-adb4-f132ba82b5a5 | -9.32139 | -46.71901 | 2024-10-07 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 21b3b184-d6c8-33a1-9556-ee82f1123781 | -9.32068 | -46.72493 | 2024-10-07 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9874258e-f4e4-35f1-8d24-9148aa4b59b7 | -9.31868 | -46.71883 | 2024-10-07 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f0a545ff-c3f7-3792-8962-5ce6e7e49946 | -9.31793 | -46.72473 | 2024-10-07 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 33597450-0260-3b20-b13f-81db478ab7e4 | -9.31717 | -46.73066 | 2024-10-07 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 35ef32ed-6b48-383e-82ff-5ef53a54b112 | -9.31394 | -46.72403 | 2024-10-07 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 98937a19-9e26-390e-a30b-fe4deee4fe38 | -9.31193 | -46.71799 | 2024-10-07 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5264d190-fe4a-3a27-871a-b0e83020044c | -9.31118 | -46.72389 | 2024-10-07 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcf65883-c121-31c2-a566-6b8b23cd7871 | -9.31043 | -46.72982 | 2024-10-07 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d937fbcb-53d0-39e6-9853-168d469aec1f | -9.3079 | -46.71733 | 2024-10-07 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6cbdbee-3b87-3966-b359-5ec44c6c7cea | -9.30719 | -46.72324 | 2024-10-07 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c68c45bf-d0a0-3959-a2e8-7589eafc15b7 | -5.38006 | -47.71799 | 2024-10-07 05:16:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7cf055e-be84-368d-84de-3fd4faf4a9d0 | -5.37575 | -47.71927 | 2024-10-07 05:16:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 393e7f38-fb59-3541-8839-81f8c50036f1 | -5.37404 | -47.71715 | 2024-10-07 05:16:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c07ca9a3-56d1-3133-8adb-af9ef58253d8 | -5.3734 | -47.7216 | 2024-10-07 05:16:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fe58a56-beaf-3bd3-a57d-42467784c62b | -6.63101 | -46.73546 | 2024-10-07 05:16:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 557518bc-8410-3ffb-b414-c9a5d122840b | -6.63028 | -46.74084 | 2024-10-07 05:16:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffafabfc-f446-3741-8505-a79caffcddb3 | -9.66666 | -47.81712 | 2024-10-07 05:16:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ffaa55d-59e6-38b9-b4a8-f5a8259d6c20 | -9.6597 | -47.82131 | 2024-10-07 05:16:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README111.md)
