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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c483cce8-f0a3-3dea-b8bf-db19c94198e4 | -3.51191 | -50.31615 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28e57c4b-c407-3512-89c1-59a16bbc62bf | -3.12791 | -51.73676 | 2026-09-28 05:27:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 247d0a95-51bd-37ff-bf3c-472bfa3a08c9 | -3.29232 | -50.31567 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07e1ba23-dd13-3fad-9693-92c04d7e06ce | -2.97836 | -54.1459 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dff4746b-5542-3d6f-9c28-9c5a6b57bc86 | -2.78664 | -57.7011 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20161fff-0f8f-31c8-b2bc-8c0bf190db9c | -3.36003 | -50.467 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 076719b9-65c8-3d26-a1d0-dbc8124aeb24 | -1.81121 | -54.8726 | 2026-09-28 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 246bbbe6-b294-3e9a-a0e9-05d9a93d4907 | -3.35947 | -50.47063 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6f9b740-2f87-3a2c-b915-258e2cf86c94 | 1.65082 | -55.92107 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5b1c65b-5c0f-3d05-b269-f9b80c9c7e76 | -1.77067 | -53.76537 | 2026-09-28 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c68477f6-88b5-376c-98e4-c0a9671f3156 | 1.6768 | -55.94611 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c41df06b-e4b0-34c2-8814-39d4a46022bb | -1.34637 | -55.47935 | 2026-09-28 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9df4a35-f8ee-3dc5-a5d5-5b027420583b | -3.20135 | -51.04048 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a2c9c80a-177f-3be6-b2da-f96fca90b1d2 | -1.48223 | -54.79456 | 2026-09-28 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e950f82-2591-3f9d-912e-bc8d6f8e2784 | -2.55841 | -54.73429 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| aa485007-1df8-3e06-a01c-a3288fd72ff0 | -2.98483 | -51.05342 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4355a90-e091-37d5-b58a-e66d355e565f | -2.66215 | -51.73489 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2fca813-2148-3c0b-b32e-62f87212086f | -2.8976 | -54.11063 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f21ea8c-2b55-38c3-bf8a-e7196f3d59e8 | -4.31632 | -50.40473 | 2026-09-28 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 589ff5d2-19bd-3901-bf6a-4eb9a4590188 | -4.31128 | -50.40014 | 2026-09-28 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 917101eb-a513-3b18-bb2b-6a5da56abc8a | -3.01088 | -54.21503 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f45c88c-480c-30a3-afeb-02e8318c6081 | -1.76895 | -53.76757 | 2026-09-28 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4fb32b75-6397-3cb6-a756-c37ca66f3b91 | -2.92566 | -54.20656 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74cd75f6-6577-3af8-aa76-07a0c466baef | -2.7855 | -57.69444 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86745f9b-760b-345a-aa29-e729fe54f546 | -2.5302 | -57.22639 | 2026-09-28 05:27:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f55e07f-5cc6-30bf-a043-ce8d1bfad562 | -2.89823 | -54.10665 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb0a004c-2e47-3e67-9dd6-bfd0606747e8 | -2.92626 | -54.20263 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b1c5e7a-68ab-33f7-8613-6b4ec69efb33 | 1.67194 | -55.93856 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19ef3890-5f0a-37a7-ad9f-aaa20393ba3e | -2.89707 | -54.08612 | 2026-09-28 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 709b6e51-efcc-3c47-8ab9-8cda2976c334 | -1.77496 | -53.76602 | 2026-09-28 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37dd9ab6-3358-37f4-bffe-3d78cfdb8f5a | -2.76826 | -49.48221 | 2026-09-28 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2fc37af-f627-3500-b95d-da0588cef1c7 | -2.91727 | -58.30484 | 2026-09-28 05:27:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97d36ef6-186d-3798-bcb9-c5c0b16de7cf | 2.3966 | -50.99208 | 2026-09-28 05:27:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 106d16e6-d154-3f60-b2a2-568546712f47 | 1.64755 | -55.90067 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c9903f4-e400-3f41-990c-6f2871d34785 | -3.23121 | -50.5785 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 719c15c7-8635-3338-beae-e3a6de8436d6 | -3.20184 | -51.03723 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7a865a8c-219c-3ef1-911c-bcd0fdcc3936 | 2.89971 | -60.27617 | 2026-09-28 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20c357b1-6ce7-3a64-b71f-fba483d83801 | -1.22884 | -54.10109 | 2026-09-28 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3537fd31-400e-3a43-b4cb-7168b2824d3e | -2.9084 | -54.11939 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c3cfd97-2e7b-3a4b-9206-1bc53cb89ca1 | 1.66155 | -55.91939 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9434ee66-c07b-3cb9-93f3-984278161a7f | -2.12051 | -56.88652 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 502bdd63-962e-399c-abb9-4f52292e96cc | -1.92511 | -52.14115 | 2026-09-28 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c235db8-b243-3036-82c0-da6e220c7014 | -1.92914 | -52.147 | 2026-09-28 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ced7042e-e6b9-38f1-b0bd-7c097e518edc | -2.90722 | -54.12731 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aec8705c-2cc1-36f3-9bd9-cf65eda2ab52 | -4.31688 | -50.401 | 2026-09-28 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa605496-3a31-3fcc-953b-6901ecd03fe2 | -3.14398 | -54.07576 | 2026-09-28 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1884d28-0037-3fcc-8edc-8211269c33cb | -3.20615 | -51.04453 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c5221ca6-17bd-313b-994b-e6dfe2286978 | -2.12113 | -56.88254 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b622aaa-8e25-32cc-80c0-9034a6c4852d | -3.09985 | -59.93348 | 2026-09-28 05:27:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25b9bca5-627c-3850-ae07-7654092b82a6 | 1.65178 | -55.90419 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50e781ed-fd3f-33d4-a6e7-f687b11737a4 | -2.93196 | -48.75542 | 2026-09-28 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4b158be-31b5-3208-bd9e-4be32ec54205 | -3.0448 | -51.3349 | 2026-09-28 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5565ca73-a97d-390e-9438-3afa855ae20d | 0.70218 | -51.4345 | 2026-09-28 05:27:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c6e4b9a-5c63-3764-a58b-fad7c10e2c6a | -2.89769 | -54.08215 | 2026-09-28 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30399622-1eee-35cc-99d0-0c4f278245d4 | -1.74086 | -57.18271 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 452a89ee-e05a-3b89-a475-dbfb83751306 | -3.14337 | -54.07978 | 2026-09-28 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68d408f8-a65e-3a9d-b1ae-6af2cc8e0317 | 1.65147 | -55.92514 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0ea8670-9879-3417-b016-4f222085702e | -2.92144 | -54.20589 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f7ceb4e-27b2-3c85-9e01-693917b69b88 | -1.76639 | -53.76475 | 2026-09-28 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddfe861a-c2e1-3566-a50a-f8c4ceeb730e | -2.86454 | -49.63412 | 2026-09-28 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6549493-2984-3ea5-a846-9d6fd0f4a639 | -3.15135 | -54.08497 | 2026-09-28 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2da5a0c-314e-325d-8edb-dc82b06fb84b | -2.66129 | -51.7406 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88952eee-26d9-305c-99a9-cb4d2bbd9daf | -2.89651 | -54.16997 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02b2fe94-8881-37ce-9762-e7380abbf0af | -3.09221 | -57.6577 | 2026-09-28 05:27:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0efc497-e039-3bfe-b568-4b6daa60d9e3 | -2.72751 | -54.20191 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d1410ef-c2a8-35cf-b09c-b8ade418ccef | -2.94243 | -57.71711 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 573cc512-fbcb-3f75-bcef-a9e07b0dec56 | -3.29286 | -50.31201 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93c03c10-09b9-34e9-8c7b-6e083c82e3e0 | -3.5164 | -50.32437 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39ea1ea2-ade3-3108-a2aa-ea98d9c05cbc | -2.44607 | -49.22233 | 2026-09-28 05:27:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 013fa16e-72de-36ba-af95-6f656e467ac7 | -7.55562 | -61.46347 | 2026-09-28 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e858bfb-da47-34e3-914a-6defd240c509 | -3.97006 | -59.34788 | 2026-09-28 05:29:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 39aea6f8-515e-30ac-a505-74f2c9391b8f | -10.89145 | -50.6885 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d6f85b4-22ce-3068-9aed-3bd56bdbb6f7 | -8.28305 | -64.03397 | 2026-09-28 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0345aea-c9f3-355c-8e24-381020479261 | -10.7054 | -50.4727 | 2026-09-28 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a46dc0fd-4938-3e0f-b468-35ef90ec38cb | -6.78596 | -59.38067 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1b655d7-4065-39cc-938c-6fe01237df9c | -11.1149 | -51.33104 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce91cc6c-6cd1-3b80-aae4-f0262696f631 | -10.22071 | -49.99712 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d720c94c-ed78-387b-bec9-2d4ecfbcfe13 | -10.20818 | -50.01015 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fa73a91-61a9-347b-8e35-8fd4e830d68f | -8.03903 | -54.89295 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d934cc1-1774-3eef-a9df-8b5130b7e195 | -10.80145 | -48.73353 | 2026-09-28 05:29:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1fdc0e9b-1d33-3d97-9c0d-f23f97ddd969 | -10.21129 | -49.98546 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6468ffe-54d0-3c5a-8be1-1a3f2cd4e070 | -4.98232 | -56.14783 | 2026-09-28 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 591413f8-5564-3178-a9d3-9cc772859318 | -7.05699 | -61.07382 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f518282d-0393-3def-9d90-d5ab3693f02f | -7.45208 | -64.34887 | 2026-09-28 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5a7d89e5-c93b-3e0a-b8d8-1a99abf8db1e | -10.41185 | -53.82133 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d76aec64-b2c4-3c79-81c5-9bb19fc45531 | -11.11342 | -51.34343 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54be8341-a2c4-3546-a315-5cdc14cadf68 | -7.06035 | -55.48251 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61c987ef-f15c-3f82-8bee-443dc4f26a75 | -6.07933 | -57.80664 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50524017-9394-3392-bedf-49bec389a166 | -7.5623 | -61.35763 | 2026-09-28 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37c3d78a-372f-3322-b5b4-58cd1f80b58d | -10.40214 | -53.81983 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3b2b24d-f4e7-3f3b-aaa4-d42e0a2ee9c2 | -7.56169 | -61.46801 | 2026-09-28 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d184a253-6f82-3480-9324-1770d7541744 | -10.20763 | -50.00044 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6135c160-9df0-399b-b318-acfcab0d7375 | -6.071 | -57.81351 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afc27263-166e-3f0d-b8f4-4e43da0ffb5f | -9.1645 | -61.40816 | 2026-09-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 72ebde1c-91e7-3d2d-8c87-6fc9a3e433b5 | -6.06806 | -57.80894 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f63ac509-397e-34df-9c13-0a6267fd99a0 | -10.21506 | -49.99138 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 634324b9-17a9-33c5-94e5-e312e8c90347 | -9.98551 | -50.14458 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| feb5a7d4-6680-3daf-a0c8-aa4b418d2780 | -9.9849 | -50.14937 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c3ca0b88-6945-322b-b8db-55c8eb4c2d75 | -7.27852 | -55.58273 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6294228-f8fb-33b5-85da-8fe70f896938 | -11.09793 | -51.32318 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README62.md)
