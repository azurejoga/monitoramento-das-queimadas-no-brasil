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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b7a0b1f-5992-3b67-bdf3-5f67688451bb | -2.79134 | -51.80975 | 2024-10-28 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 007d51c1-1b61-3ee2-9d94-19b5bc3da75b | -2.57009 | -51.85404 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56a22959-5653-3f81-8fb1-9672c6eb78ca | -2.51937 | -51.1833 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3e77a85f-1c2a-35d4-8e29-09b2f0462d55 | -2.51282 | -51.18649 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 720442a0-1d26-3c7d-9e82-d8374449467e | -2.05255 | -52.1679 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7e68be97-7c8c-34cd-a927-b95dbe20e6f0 | -2.0517 | -52.17302 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 82702804-e5e6-323a-9df0-42bebd996f9f | -2.04623 | -52.09019 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5775a28c-bf7e-3c6e-8fe9-c096864cbc07 | -2.0454 | -52.09517 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5aeab23-7d7a-343f-8bc2-868b81b184d1 | -2.04163 | -52.07941 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| abd135c8-4581-3619-931e-a8a3d4b7b01e | -2.04081 | -52.08434 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4949b5a0-5737-34fc-983d-33b18e462a34 | -2.03998 | -52.08927 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5a67e92-37c5-3b7e-a6ac-b3d3f2290a0a | -2.03915 | -52.09424 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99d6ab95-8686-3f5a-a6ea-912271bdc51a | -1.98466 | -52.08834 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a00b8ff1-b242-35e1-b95b-845b1d74e6fe | -1.97924 | -52.0823 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c15e04bf-07a9-3df5-8b8b-d1e4e44a78e8 | -1.97844 | -52.0872 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 79a5ea7e-6a81-35fc-9576-a0bb91751eb4 | -1.97763 | -52.09214 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 96552be0-1069-3cc4-a51e-a4eed7052450 | -1.9722 | -52.08614 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95113ee3-4d6b-38a1-a73d-84302396c46d | -1.97138 | -52.09112 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9f3c29d-daa4-32c3-8bf2-8b5b25a5459c | -1.92571 | -52.13414 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26775070-2cce-346e-ae6b-209db0632a0b | -1.9223 | -52.1305 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c08bfba8-8380-3521-b84c-a07900222cdf | -1.9215 | -52.13552 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fca4e81-dda3-3762-830b-77c0af95d589 | -1.92091 | -52.05934 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2082f5c3-8fbc-301c-aae2-ba7e422bcf90 | -1.92069 | -52.14057 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89bb6f6a-27f4-393a-aff2-e6524ec8db5e | -1.92028 | -52.12811 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 15e0bdd3-143b-331c-a120-f4f7d421ffba | -1.91945 | -52.13309 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 723a4b66-9f42-3f53-9143-58d68272abb8 | -1.91936 | -52.05719 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 048db51f-253e-3526-8eaf-c5ce517a97cd | -1.91861 | -52.13807 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54a2463a-7d7c-3655-b9a0-608425ed3c6b | -1.91604 | -52.12946 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08d04370-e923-3308-bf48-180c73b57bbf | -1.91548 | -52.0533 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aeb45f7-d733-33e6-8134-1d27c9f51c98 | -1.91525 | -52.13442 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d637da9d-dbe8-31c2-ae0f-250380e4dd50 | -1.91469 | -52.05817 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4dca11d-b8e1-3e8f-b70f-c0b8810aa17e | -1.91316 | -52.05598 | 2024-10-28 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21bbac1d-644f-39b1-8c9e-ac46c8ec6b8e | -1.5476 | -52.11008 | 2024-10-28 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5819281-bbfe-3610-8ac9-53fc9d1a5668 | -1.54678 | -52.1151 | 2024-10-28 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64715205-b17c-3bf6-aedd-9203d12a4e8d | -1.54377 | -52.09398 | 2024-10-28 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53d8ae50-9ebc-3d93-8831-e326b9c6839a | -1.53832 | -52.08791 | 2024-10-28 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e149b6a-ffeb-3ae8-bea7-fb1c877a0991 | -2.8423 | -52.555 | 2024-10-28 04:04:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e6b46ee-a0a6-3fd8-a493-de9b3ca79054 | -2.83605 | -52.55339 | 2024-10-28 04:04:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 530088a5-c688-3276-a6fe-7615164f2055 | -2.20312 | -53.68777 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5d80457f-7779-3ff6-8f3e-da598e3f9ec9 | -2.20256 | -53.69438 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f99a56e-e1e1-3dda-84c0-e63a75460635 | -2.20204 | -53.69442 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b476998c-eb28-3e61-9284-64ccb9801dba | -2.201 | -53.70079 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fc332575-f420-3255-ad8e-a1a56579f237 | -2.19688 | -53.68638 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 85c09394-c487-3a57-ac8d-33debd307818 | -2.19579 | -53.69282 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6fdfa4fa-43f6-3515-bd90-39891fc98964 | -2.19526 | -53.69284 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c86b6dd6-c830-3e8b-bf74-af01bdce46b5 | -2.19466 | -53.69944 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 69d8e771-7459-3572-bf5f-9a99c30c1a41 | -2.19417 | -53.69948 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c6b0c7aa-4630-3a93-9863-976e2337e7d8 | -1.27111 | -54.13906 | 2024-10-28 04:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97b23182-7ccf-3812-90fa-fa5b03e0bda2 | -1.18482 | -53.50974 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99712d8b-1ede-31bd-b47a-733f2c6ae6af | -1.18361 | -53.51707 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81a39eb2-5b0e-3c9f-a6ab-39ba0d8e1e29 | -1.17795 | -53.50861 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d8a1f4fc-e7d0-339f-a9c6-05549d9d3319 | -1.1767 | -53.51616 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5a58e9f3-b5ef-3adf-aabe-ad68a1311b08 | -1.17109 | -53.5074 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 80b7c7a4-75f1-37a4-b3c1-a0da19cf2805 | -1.17091 | -53.50759 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0fac92ba-3432-3376-8f6b-05e421c77ec6 | -1.16986 | -53.51482 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7059abb4-8db2-3054-867b-285d4963f0cc | -1.16974 | -53.51498 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6838ed0e-d93e-3f78-bf7f-4f7e9bfb7ab3 | -1.1641 | -53.50699 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85bae8c5-147c-3468-902e-18cdd8dfe399 | -1.16393 | -53.50712 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9a65e30a-aa06-3440-97e9-183f11d4b467 | -1.08243 | -53.66105 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b480ab0-2837-3929-beee-47388f6fde56 | -1.08121 | -53.66858 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c14f25eb-4eac-39e4-ba99-6fc734ff1484 | -1.08011 | -53.67535 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1aa5336e-1411-31ed-81c5-5394e35f76cb | -1.07439 | -53.66667 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d827cd80-6a4e-3a21-bd14-502038f7ab14 | -0.98992 | -53.70907 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2260ebb2-bc6f-3a86-9f2b-b91cd546ebf0 | -0.98855 | -53.71034 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8333277-389a-3ba8-85aa-494e38460be0 | -0.98295 | -53.70792 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f2f04cf-cfc2-37b2-b679-5054d3b08b25 | -0.98199 | -53.71382 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a224735-deb2-3dc1-aebe-20432fcd9ee1 | -0.98157 | -53.70929 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 146de360-f627-3618-9fd5-0b76597c81c6 | -0.98057 | -53.71518 | 2024-10-28 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5e195db-a055-3231-bbec-1b3c28d1e542 | -2.27328 | -53.77985 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| cc267071-46c2-3a5a-b12f-376db92a2d83 | -2.27328 | -53.7777 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| f4f295a7-28ea-38a4-a259-97fe565e652b | -2.27221 | -53.78423 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| cb30f482-564b-391a-b0dc-d59131ced857 | -2.27216 | -53.78636 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 8d02a8e5-535b-3c71-af6b-4be4ca531ba3 | -2.27114 | -53.79073 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 35274db4-36a2-324d-ba5f-80ddb11e329b | -2.27104 | -53.79288 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 8e0b20e9-3f38-3615-a0b2-5c5b1e2b97f3 | -2.27006 | -53.79731 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| b6e18cfe-4833-39f3-bcdf-96ef861bda92 | -2.26993 | -53.7994 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 6d09edc5-49a9-3025-ac5c-26ce68787b66 | -2.26531 | -53.78318 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| af5700db-d075-3e8b-8486-2d5493f95597 | -2.26524 | -53.78546 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ff7e02c1-0787-3c9f-bfc4-5a4d639ddc39 | -2.2642 | -53.78993 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0988f45b-a10b-3d52-b135-9b2b5ef30e9c | -2.2641 | -53.7921 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 9215ae60-50c0-3f46-9f0b-0929326ee75d | -2.2631 | -53.7966 | 2024-10-28 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7d65a1ee-6f36-3c0d-ac22-cc698eea42ea | -2.6384 | -54.29611 | 2024-10-28 04:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ce58f93-4492-33ee-846d-c0b2e0dba6d2 | -2.63723 | -54.30294 | 2024-10-28 04:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 09f39468-f664-3f7d-91a4-1cc57bf4cb44 | -1.9763 | -52.0804 | 2024-10-28 04:05:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 81f8ad5f-1934-3f4b-ab6a-38c96b6112c8 | -2.2662 | -53.7825 | 2024-10-28 04:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 95cce49b-406b-364b-a075-15612795630f | -2.2846 | -53.7822 | 2024-10-28 04:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 1b0da19f-fd10-3ba0-9939-5d4b18bdd9cb | -2.4104 | -48.5479 | 2024-10-28 04:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 87886a12-32b1-36d9-ac56-cf4026822e27 | -2.833 | -49.2413 | 2024-10-28 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ea7e6cc0-2337-3589-a56b-3ff5e948a846 | -2.8699 | -49.2615 | 2024-10-28 04:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 69107bfc-a8a7-36c9-bda3-a220549e3ca1 | -2.87 | -49.2402 | 2024-10-28 04:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 33c8b563-bd9d-381f-85db-d648bf8befdd | -2.8884 | -49.2609 | 2024-10-28 04:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 13c769b5-b86c-342a-bd9a-d4e1144c4217 | -3.0317 | -50.4176 | 2024-10-28 04:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| ae91e5f1-8768-3351-93d7-dd0c98fc3dd2 | -3.0501 | -50.4171 | 2024-10-28 04:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 79e7cbed-04de-3d85-b32e-3b9111bbf315 | -3.5155 | -45.7964 | 2024-10-28 04:05:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| dca99d77-9f18-34c5-abcc-f8f264d2a367 | -3.6911 | -51.5622 | 2024-10-28 04:05:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 4792b688-911b-3b0a-9c59-a3cc66869cf2 | -4.1201 | -47.3169 | 2024-10-28 04:05:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| fc270614-c91a-3bd6-a8a9-9a047db091d3 | -6.68677 | -40.8881 | 2024-10-28 04:06:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7576226a-0454-3813-8425-82fda8f05cce | -4.65359 | -43.09542 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fecb2d9a-06ad-3513-b857-ad4a1256159a | -4.6301 | -43.11071 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cbc9dfc3-f290-37b6-a3a0-af02223ce85c | -8.00306 | -35.1339 | 2024-10-28 04:06:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README36.md)
