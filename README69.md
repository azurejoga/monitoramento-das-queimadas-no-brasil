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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 325ff54c-6af8-3258-b381-ec9ee0880c5c | -3.51498 | -51.67385 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7aae34d3-dc2c-36be-91ee-d8f4224e6b7b | -3.51197 | -51.669 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e623999a-0b8c-3c2e-8647-53dc248beed0 | -3.51132 | -51.67328 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a5edcbf-8997-3f6e-bb5e-825585fadcbb | -3.50032 | -51.1811 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8bc8c510-6952-3227-a488-2af99569b9e7 | -3.49962 | -51.18568 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 46d961e6-b5a1-3aaa-aded-278e26e50194 | -3.44119 | -51.51876 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 597656b1-ef3f-398d-b085-4a96efb1a513 | -3.44053 | -51.52311 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f893e95-01c4-3afc-b9f5-f3d41069f8c9 | -3.43684 | -51.52256 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5063bcc4-f901-3ddc-af17-1e82a8899bb7 | -3.41767 | -51.21947 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d77357e-903f-33ac-92eb-4978665a271f | -3.41704 | -50.93925 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bc04db4-320b-3fbc-9cd0-5c82b72c9a2e | -3.40933 | -51.50483 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a389e95-e7b6-3c2d-af8b-a58f947e3996 | -3.35964 | -52.17137 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae147d2f-eeb0-3ef3-b30d-3fac9170c49e | -3.34492 | -50.75105 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 325938f4-5174-3411-a4ee-57f0c552fe40 | -3.2956 | -51.20053 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| aebd88b6-c2f5-31cd-a391-23683e95acd2 | -3.292 | -50.89339 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df773f38-4533-3154-bbb8-bbb28d64f75d | -3.28916 | -50.91225 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b36fa47e-705c-39bf-954f-abd617caf3e0 | -3.28846 | -50.91692 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b70f52b9-06df-36c6-84fe-041a3d4866a5 | -3.28818 | -50.89281 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0eb2e580-22cf-378c-9d68-05b3d3733b3d | -3.28535 | -50.91165 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 08054627-0d32-365e-b6b5-75925c19af06 | -3.28465 | -50.91634 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9ba6349f-9a0d-3559-8a73-7d8873dc1b82 | -3.27298 | -51.07112 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 538e087c-2a44-3a4e-9c15-7137b23b34e6 | -3.26798 | -50.77663 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 667f8da4-03aa-3ab6-8757-422dff21dc4f | -3.25509 | -51.13859 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e1fb689-77d1-37f1-a78e-b8428dc44b5c | -2.42533 | -50.50795 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6492a942-0a97-3ef5-baa6-bd3858594c67 | -2.42222 | -50.50253 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86c1050d-de6b-3c81-90e0-f4d03a582802 | -2.42147 | -50.50735 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2facde3-3afa-36d3-8ae3-01d0e9666eaa | -2.41955 | -50.44265 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7978925-4f50-3efd-a239-2f13a9a6e7ba | -2.41909 | -50.49712 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9a41c6a-16fd-36f4-801a-261ac733509f | -2.41835 | -50.50195 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 220bb980-a2a9-3bcd-bfff-674e3fcc8614 | -2.41523 | -50.49651 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f70b0d7-7eb0-3b78-abe4-0e74936b4585 | -2.41449 | -50.50135 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0dced9c9-7c1c-3b91-9da3-fabe48b1eeaa | -2.41328 | -50.43177 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 827041b1-b0fa-3902-9392-9d809c748cbb | -2.41258 | -50.56493 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68fff8ff-b7c8-3a7c-a6a1-acc0b93e71c0 | -2.4094 | -50.43116 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a98b715d-4cac-3371-89dc-a9766804fa4c | -2.40552 | -50.43055 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4dcdaf2-1a24-32c5-a99f-125b3468e097 | -2.32622 | -50.44651 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45ae39df-8839-3fdb-9205-5333dacaf23c | -2.3256 | -50.47609 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8042ddd8-b2ad-305a-8163-7644a5a83894 | -2.3231 | -50.44107 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5a355b9-bb7f-3589-ba8a-421189ab6d4c | -2.32086 | -50.45559 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc9661c6-b705-3514-aca2-0c19d2c134f4 | -2.30866 | -50.48333 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a6fdcbf-4131-3bde-a26a-b9c6f512f581 | -2.30332 | -50.49237 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66d1f088-8829-3861-85fe-c2c510f42531 | -2.26807 | -50.5164 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50ed51b1-6738-3829-adbd-d89138f942df | -3.17963 | -50.59393 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2efdd399-0a74-3297-b282-83fa55c95d4b | -3.17575 | -50.59333 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70f45506-4ed0-30f8-89dc-877f6e8f6ef0 | -2.58267 | -51.35274 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42ed4b38-0456-3450-b4aa-dee362b3e08e | -2.56908 | -50.65204 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcdd59a4-1809-3a1b-b413-46650b6da758 | -2.55552 | -51.23219 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1354690-68b3-31eb-8dc4-8f5eb460f22f | -2.51774 | -50.70707 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5100e0df-4f79-3be9-9d2b-2b09217d1553 | -2.4802 | -50.98512 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb40d56d-9fe1-3304-829e-14d5827f1871 | -2.47882 | -50.98746 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b380baf-b5f8-3330-a512-ac219ae2128f | -2.40759 | -51.29894 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0d8e64a-0625-347b-be43-7185a522d431 | -2.40691 | -51.30329 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4d25f14-6d0e-3927-b571-94ac2c6c3b01 | -2.40323 | -51.30273 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8e6934d-e1d7-3ee2-8237-55edae79c0a2 | -2.39134 | -50.60068 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3c8aa24-cf1d-37f6-8da7-2491cb93c021 | -2.31488 | -50.62106 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 278ab3fb-b6f0-396a-a06b-2409b0d943ea | -2.31347 | -50.62262 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59472384-e58e-381f-a1a7-fb2400681bec | -2.31105 | -50.62048 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1aa81c7a-d5aa-3688-9d7f-55878af71477 | -2.30964 | -50.62202 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 271a0b8c-26be-3df5-85f8-35cefcbd4361 | -2.29608 | -50.66642 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6478b861-3c41-3424-8374-1e3107dc5444 | -2.29298 | -50.66117 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01bd964c-207e-30e8-8a1a-f41cab5a54b0 | -2.29153 | -50.67052 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 68e33c3c-138a-3f35-8b79-29b260625a8e | -2.29081 | -50.67523 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 135ead25-5fdf-3d9e-b50d-6209b1af0e6e | -2.28224 | -51.13737 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9148df5d-352a-3d5e-a4bf-fb56eb63d71e | -2.27852 | -51.1368 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07f63491-40eb-32ab-a206-aa9bc1177520 | -2.27785 | -51.14123 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d06a9552-ab7f-315c-8f1b-3d0aa63d208b | -2.27717 | -51.14567 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41434907-c492-3821-b39a-6babf17791d9 | -2.26575 | -50.68577 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0703af6-88d9-32ec-a5de-fd444d48fc94 | -2.26503 | -50.69046 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 294ac8c5-b775-30c6-a3a1-484f358157ae | -2.26181 | -51.24662 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15be6d30-4eaa-359b-84da-73702b2327d8 | -2.24694 | -50.70681 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8633562a-5504-32cb-aa96-1c76215e0697 | -2.24598 | -50.68755 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06e920d3-8822-3d59-8885-2f0b416c4a03 | -2.24526 | -50.69222 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c94c45eb-d540-3c29-b42f-b3f6a0387907 | -2.23861 | -50.71032 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ff1efd8-c87f-3e86-89ff-149e4456a64e | -2.2379 | -50.71498 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57803aa3-075f-372d-9983-5f7e96639746 | -2.23551 | -50.70507 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff9c93e6-9c69-32ea-9e5a-0f3843ce6c1f | -2.23481 | -50.70974 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 779e7784-5b78-3623-96f3-a8998011f361 | -2.2341 | -50.71439 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbf05a62-6ac3-306a-be34-e9c374430639 | -2.17086 | -51.42438 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bca4087d-ba44-38c8-a28a-1dbfc59c1180 | -3.22131 | -51.18447 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32991691-1435-3cec-b3e3-5d5186fdfdcf | -3.21757 | -51.18384 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d4f4ee0-3b1d-3140-b7f4-c7f87a1d8c04 | -3.20459 | -51.16795 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 490f87df-973a-322a-9ac5-18155b489856 | -3.20394 | -51.16574 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 897790f2-b7d2-3803-a656-da0448ec1512 | -3.20324 | -51.17024 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51c1a7a6-fbdd-3f00-a32a-1fc269cbcf50 | -3.2003 | -51.03911 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cad1007-cfec-36d9-83e2-307f71d7030a | -3.1828 | -51.15337 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b60c844-eab3-3933-ab05-28dd4a1a85f8 | -3.18211 | -51.15788 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2683a35e-9b94-30da-be22-5e5e5d776005 | -3.17887 | -51.07822 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab60afcb-7395-3195-819f-7953a54e8483 | -3.17818 | -51.08278 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8547de92-26bb-3eb7-ac60-3ca360131872 | -3.1758 | -51.07306 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4352e6b9-750c-3cca-9934-84d3fb537e52 | -3.17511 | -51.07762 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| febb2479-76d5-33d1-a128-f61d93851351 | -3.17441 | -51.08218 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8e2af171-8c9f-32c1-abdd-37bd2f9827ed | -3.17372 | -51.08675 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eefaa479-e70b-39a1-9b60-3fde9fddaf7d | -3.17203 | -51.07247 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 22730ef7-eb47-37c5-befb-8964b2af3f93 | -3.17134 | -51.07702 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c5f575fd-a097-39c1-a651-d37857417a34 | -3.17065 | -51.08158 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8b72b196-458a-3d12-8cc9-a086df7689f3 | -3.16826 | -51.07188 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 10455c50-ec5f-3b1a-8d7f-afdb26fc469a | -3.16757 | -51.07645 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85b770fd-3cda-34da-a369-821feb60d73f | -3.16688 | -51.08103 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b6e18ff-6cdc-312f-b7d7-34082409c61e | -3.16066 | -51.12204 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f90cc576-6d06-3484-9ff7-f8d674ad94aa | -3.15928 | -51.13113 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README70.md)
