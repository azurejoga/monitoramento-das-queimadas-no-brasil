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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 910c4829-977c-3838-9821-915917f692c9 | -1.79007 | -50.60052 | 2024-11-03 05:08:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9499e698-b537-306a-8f74-ad70ffaf8554 | -1.2933 | -51.46546 | 2024-11-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e955767b-35f7-38be-8bf8-a695daaf6aaf | -1.20439 | -51.38079 | 2024-11-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd8ed664-76c1-34e5-8f20-c1baf564f52f | -1.20358 | -51.38583 | 2024-11-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 944547b1-faca-3b18-b110-e9fa0b5d6ba1 | -1.18932 | -51.37323 | 2024-11-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60e16ee9-600a-3d5b-b4f7-8c582ae68be3 | -1.18687 | -51.37457 | 2024-11-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef50286e-b6ef-3a7f-83e0-6cefa0ee914d | -1.18454 | -51.37769 | 2024-11-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 167ed50f-eb7e-37e3-a94e-2bf8a0d1265c | -1.18057 | -51.37709 | 2024-11-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36c29443-03d6-3427-9c0e-5eedaa2f5918 | -1.17977 | -51.38216 | 2024-11-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49a672c4-9ac3-346f-896a-cdcc842dcf4f | -2.10827 | -51.88594 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7500f862-fb05-344a-80b8-ae7ce38920e5 | -2.10437 | -51.88533 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bc59a16-6240-3e2e-b2c3-d10c258ddf56 | -3.3837 | -51.3141 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef9bc782-abe4-3314-8040-e336074d8496 | -3.37453 | -50.83097 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a840a6d1-b98a-379b-8d84-e5d82fed12a7 | -3.37028 | -50.83034 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f80b95a8-f24a-3cde-8f63-7a0b5e68eb59 | -3.36969 | -50.83424 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eeaeda7-69ea-3d5c-9a1b-c3b30aa2ac30 | -3.34727 | -51.29051 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35600dea-1e84-3a08-923e-cfc1f85c4c08 | -3.34449 | -51.63108 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee3c59c0-1188-32d3-ad9a-1e0d5be35963 | -3.20683 | -50.91607 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e3ca27bc-4a50-343f-b6e6-a816c71e24f6 | -3.20588 | -50.9186 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0f74f2d-c277-3e40-beaf-e73125637838 | -3.38425 | -51.31039 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bc957e1-1cf0-3f05-ac35-9d8fc3203a07 | -3.37394 | -50.8349 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0eab3f8-7ab3-3a72-865e-937b165c6583 | -3.34852 | -51.6317 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d043114c-5fca-3b40-90b4-1480cbd0346c | -3.34784 | -51.28681 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90ba2dd1-64c6-3de7-bef8-5636f2f114b0 | -3.34315 | -51.2899 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 121871f0-056a-34d8-8f6d-e6f86bd1ef58 | -3.27564 | -51.08202 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d582e91-aa3b-3020-9fce-fdb6ae125a0e | -3.21105 | -50.91669 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6bf178d0-e44b-3ff3-811f-c0f9b32ddfef | -3.2101 | -50.91922 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6c7b5a0-fb47-37d0-998f-815eec88d1ba | -3.20623 | -50.91993 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a52eaf10-8ba2-3cd1-8557-5c43bb2589e1 | -3.61558 | -51.28835 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2714518d-7c8b-334c-b2f3-2bba928dfaeb | -2.83614 | -51.54042 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffb9aeb5-f2c5-38cf-a1a9-4d4a7759b3e9 | -2.83561 | -51.54391 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f979fbd-3f22-3354-a326-4235f1415d1c | -2.83265 | -51.53632 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 046d2abc-e08d-399a-ba66-ab72752048b1 | -2.83211 | -51.53984 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f347711-1022-3611-a0aa-37882a641cc0 | -2.83158 | -51.54332 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 841a5423-24fd-3c24-a739-7a7d25457142 | -2.83105 | -51.54681 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaaef34f-d937-3967-bfd5-647297a18a87 | -2.82808 | -51.53926 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6de9f3f-2d65-3ba1-836c-6bc27ecd1038 | -2.82756 | -51.54273 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a6fa4cc-91c7-380a-9f71-91076a272048 | -2.76057 | -51.74278 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09754985-3a31-3e05-9c43-4e61c1274254 | -2.75837 | -51.7406 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c68cdd3-6ba4-3e77-9003-10829b6da161 | -2.75661 | -51.74216 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b05b7589-0c50-3105-a405-fca0647b446c | -2.73739 | -51.4248 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6757fda9-3daa-3aff-a059-baca4429f9cf | -2.73684 | -51.42838 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 761a4940-885c-3049-98df-3eb5122e124e | -2.73279 | -51.42776 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd162a39-059a-3572-8405-30165080322b | -2.73058 | -51.73638 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbdefe5a-52f7-3266-8d1b-ef03cea546a3 | -2.7298 | -51.74145 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e0e114b-8e4f-3e62-beee-fe5c15275fa7 | -2.72874 | -51.42715 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df7e5b89-b3b7-33dd-8dcb-ce9369c2f36d | -2.72821 | -51.43069 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b455163-fa06-351a-b5f0-599e62c81665 | -2.71467 | -51.70781 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2be41c48-4076-3b02-80a7-f1d2fc576482 | -2.71069 | -51.70721 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff791e41-c558-3463-a535-a35925dec6a6 | -2.70633 | -51.84076 | 2024-11-03 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2e698bd-fb09-3617-b9ee-cc686364319a | -2.661 | -51.76706 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b5ecc64-fdd5-314c-9378-7af9536df0bc | -2.65704 | -51.76644 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 629bbba6-7752-3ccf-b6ab-107296f49c95 | -2.63346 | -51.56332 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73c36754-5596-3556-aecd-60a871b4bc51 | -2.63292 | -51.56677 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ff72529-20b3-384c-a864-2aa0e744edf1 | -2.62945 | -51.5627 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47bc6cbc-2f0b-399b-abd9-ccc5a731ac95 | -2.62892 | -51.56615 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 233f5891-acac-3337-98ec-8d7ef9838cd5 | -2.62839 | -51.5696 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c06d37b0-7201-3fec-a875-32c12d4dd666 | -2.62597 | -51.55864 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ae7624e-1fce-39ee-a424-a7e32ab11e74 | -2.62544 | -51.5621 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0db0811c-dd0a-3cbe-a7c7-eda1a43aaebc | -2.62491 | -51.56555 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 365057f8-a0c7-3f87-af8c-c5244aa9707e | -2.62438 | -51.569 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb99427b-f725-3952-a78e-bd271e436a06 | -2.62385 | -51.57245 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 30bdbbad-9c37-36ff-a055-ac0386dfcbda | -2.62143 | -51.56149 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f7c0f93-e359-37d2-b325-bda243d57e63 | -2.6209 | -51.56495 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b236fcfc-15c3-3ce6-90bd-ae1d4d437f9e | -2.62037 | -51.5684 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5c7893eb-9535-38fb-b8ad-aa0ee1e53081 | -2.61985 | -51.57185 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5b0092a8-c9d8-371a-a61e-90d534f1da9b | -2.61932 | -51.57528 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 09e905df-9a54-3a1e-997f-6824454987c0 | -2.61743 | -51.56087 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0803769b-a3be-306e-8722-268f7e75d87f | -2.6169 | -51.56432 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e81a6f5d-92ae-33d1-9abf-9353cdcb1702 | -2.61637 | -51.56778 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 18cc079d-6b8c-3474-a5d1-318fe61ebbec | -2.61584 | -51.57123 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c1ab0a1e-8a8d-33ad-9f47-6fde77e45612 | -2.57177 | -51.69998 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 888e53e1-1eb6-3444-9aca-0f3a0f62e11e | -2.5678 | -51.69938 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f17c10c-8da0-3169-91c8-a6340f38847b | -2.56704 | -51.70441 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0778c295-245f-3e29-9d37-bb949bd12ea5 | -2.56459 | -51.69373 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1343862e-d854-3422-9e11-34cbae01e06d | -2.56383 | -51.69879 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aef3e88c-5d6b-3e59-a1fa-ce9002a5be98 | -2.56062 | -51.69312 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 822ea0f6-0d6e-3ef4-aa66-adb9a6521e1d | -2.54107 | -51.95516 | 2024-11-03 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ff2cfee-3ede-3c5c-b5df-38b713f5359a | -2.47927 | -51.67809 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6c0df4f-0af4-3ae9-b800-03f7567824ce | -2.45191 | -51.88375 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16d97aed-55e3-3183-8125-6f0a48f42849 | -2.4352 | -51.72821 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82f1ff15-3c2c-3974-b674-aeb065c53efe | -2.41233 | -51.82705 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1095ffa-bc45-3d23-8f95-6bc9772a0410 | -2.41201 | -51.88269 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb0c3a84-b686-3b0a-98ef-405336b5f3a8 | -3.62895 | -52.15657 | 2024-11-03 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdd9e6de-7666-363f-95ec-6ec7cb4dc8cf | -3.94682 | -50.94875 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 944cb70d-23d2-3468-a072-51cc1c308e48 | -3.80488 | -51.03278 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1f3146e-3bec-3c84-a3d5-fad46d0e8162 | -3.68993 | -51.246 | 2024-11-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46d5230f-2b1c-3270-9a92-7fa5d3524ebc | -3.95032 | -50.94817 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e293958-4f3a-3543-a8fe-ea88c9756fc6 | -3.94743 | -50.94475 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 221a8306-a054-3963-b32b-0a5925953cfe | 2.92324 | -51.0381 | 2024-11-03 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e46e7a9b-7531-39ce-ba86-b1d9cddcb362 | 2.72686 | -51.064 | 2024-11-03 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 704e5151-4073-30a4-ae6e-d264585b4950 | 2.72304 | -51.06464 | 2024-11-03 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9ddbde4c-81e8-333a-bb43-c06fa5fc9e45 | 2.72229 | -51.05993 | 2024-11-03 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f5b2fe6-c7b0-337f-a457-245a162cc74c | 2.71846 | -51.06055 | 2024-11-03 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b580d669-764c-3405-956a-d7c97cf305ef | 2.71388 | -51.05646 | 2024-11-03 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d2611e3-997f-3369-9f9d-2a48b6982269 | 2.71005 | -51.05708 | 2024-11-03 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73dc8a05-222e-36d1-8b92-352b3ea963d3 | 2.70546 | -51.05297 | 2024-11-03 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10613f4f-458b-3076-a7ca-9b1a9a465381 | 2.50771 | -51.60628 | 2024-11-03 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76a78d3e-18d1-3e09-9f3b-2cb657967007 | 1.24294 | -52.50562 | 2024-11-03 05:08:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7007ad7-e18e-305e-bddf-61532b81e3d6 | 1.18093 | -52.18027 | 2024-11-03 05:08:00 | NPP-375D | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README80.md)
