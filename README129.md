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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e18a8d9-7ce4-3c01-ab38-21b7e462cbd1 | -3.27187 | -50.56549 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cd08efc-e85a-39f2-bf26-15a9b3b2a3c0 | -0.26894 | -51.6287 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3df37557-21ac-316e-9f02-78f7ea7dd56f | -2.69606 | -52.91487 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 786256d3-bf7a-3693-bc48-a75cc4f4bd4f | -2.14112 | -54.88851 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 49a97871-a066-3a2d-9040-0528ce9d31a1 | -3.34217 | -50.52288 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a4e6b63-3dfb-3a53-acf0-e813a30d2df7 | -4.19859 | -50.68597 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b27d030-19aa-3042-aa7f-97998a34134c | -1.07001 | -53.64443 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93a53403-0ba9-3e5a-bf10-abad0f651aef | -1.33033 | -55.84801 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1c18543b-dd8f-3f50-8d9b-c2a0b2aaf7c5 | -4.45907 | -56.18098 | 2024-11-30 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf90090e-3830-3f13-8a1e-a3ee7ff67627 | -2.53304 | -54.04313 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3051b43-aa1f-380e-bf29-d56f3acea18c | -1.67853 | -52.50737 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03834fdd-e91f-362a-b5b6-12d5f8390ce0 | -3.54235 | -50.1896 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8ccdce7-ba5a-3974-a335-481478bb6cb4 | 1.43006 | -60.80372 | 2024-11-30 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f87726c8-c298-39b8-9f80-d56dba01ef82 | -3.38478 | -50.1105 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a74a4fb-94ba-3e37-91e8-ad15a7cffbab | -2.61862 | -51.81277 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fd770b5-34bc-37b4-8202-8ab5f5441cc2 | -2.72118 | -52.98146 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afaff74a-55e9-37c9-96b0-546e871b9a97 | -3.48245 | -53.81116 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 63e95c98-91f9-3a04-a34e-f9326ec28fda | -3.3488 | -50.51946 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59e95e17-8878-371a-a7ce-d3b7f3a2b366 | -1.06611 | -53.6386 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35886eba-8e90-36c8-a9cd-240abaf7084a | -3.49281 | -53.80757 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbd2859a-179a-3fed-87c0-cbb8619a76b3 | -2.72913 | -54.14162 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9b838e6-7d42-3598-9dd8-90d825b33197 | -3.5024 | -53.80909 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30564c82-c07e-3928-b6e5-8b06634ecbdc | -2.02981 | -52.08142 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7970366a-d4cb-3ed0-81f5-0477284bbccf | 0.97553 | -50.1272 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8c2ba04a-81d3-30a2-b825-889d52a6e42d | 1.10006 | -59.59068 | 2024-11-30 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48a8e9ee-7daf-3d05-8313-313118499f86 | 1.19187 | -55.95832 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be443911-0015-345b-9b10-633ff8e545a0 | -1.19958 | -51.7539 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43c9aa54-78aa-35a0-a7d3-f3ac43f8b704 | -2.63368 | -51.7506 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9c98504d-ae55-3bdf-a522-0de17c62dbe4 | -3.95565 | -50.1881 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 03f0863f-d4f5-3b56-a12e-7c9d73f2cb12 | -2.02051 | -48.06472 | 2024-11-30 05:27:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 864beb2b-3fc2-33fe-bc3c-f107e5a44057 | -2.92471 | -52.69127 | 2024-11-30 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5eab3efb-87bf-3d3d-b39c-bfa0d6b92e20 | -3.29249 | -53.83935 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 287fed1e-eb58-31d0-bb4a-e0ed3d12a5eb | -3.41458 | -50.32786 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72824df6-4435-3c18-a0e4-25a3bb77e832 | -2.66337 | -48.78553 | 2024-11-30 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 02ac3cfa-2fd9-3f02-be0f-4b8c11f70e11 | -1.36842 | -53.63688 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a588a2c5-e504-3087-989b-ac33e28df1f9 | -1.20525 | -53.87009 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8398f964-16d2-3bd8-82ea-618b93d552a4 | -1.43598 | -55.25121 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 42bf2aed-5cf2-33b3-be6b-1899d93cf4af | -2.32699 | -54.50251 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab78535d-f39f-3a63-b9ce-29283a5416ce | -1.64702 | -52.40645 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 751c257e-53b3-3a95-ad6b-a0af447c9aec | -3.49358 | -53.80247 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4127fbc0-c0bb-350d-854f-df24829f6ffb | -3.30322 | -50.27814 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90a635d7-f455-3672-81f4-fcec0545afe3 | -2.35168 | -49.01355 | 2024-11-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0c4a6407-96ac-3f0c-943a-f3143a5a6045 | -2.69533 | -52.91277 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 565951ba-7c5b-3685-a272-302e148048cb | -2.5222 | -48.46729 | 2024-11-30 05:27:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a63205b-1d9c-380d-9e40-f035a585b3ce | -2.37837 | -47.88798 | 2024-11-30 05:27:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1764e014-47e2-3d8e-987b-36af0f3e80f0 | -2.85806 | -53.99889 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bdfa63c-0443-3ff4-8d8a-629b5dbad4d6 | -2.15287 | -56.02286 | 2024-11-30 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e036fc36-18cf-36e5-a407-2a63ac52bff5 | -2.86773 | -54.0307 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e8c07d0-734f-3ede-b7d9-3116d3d9bbe3 | -2.69561 | -52.9178 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 013119ce-a81c-33ad-a68b-54716382e6cd | -1.09853 | -53.39069 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a3c70cc7-982e-3a63-b740-7754f94a2882 | -2.01209 | -51.19975 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fa3c9d0-ef35-3103-8d13-fa7cf33591fe | -3.11039 | -53.81334 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e2e92014-b643-3e40-9297-b39368cfae90 | -1.07039 | -53.62703 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 96502589-939d-3f6c-9bc5-306d3b0274d2 | -1.48864 | -52.3244 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60395943-8283-3d2e-9762-1c5c4e5d5b30 | -1.06881 | -53.63699 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7b99438e-6d48-34aa-8193-9b4a19557916 | -1.30947 | -52.86248 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58e9a36b-ce3a-3302-888b-5e9ae52d9c49 | -1.09844 | -53.38892 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| befa411b-b19f-34de-ae89-763695003803 | -3.05648 | -54.04845 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7acd6e0-9e67-317e-9e3f-3f4e02d6ea59 | -3.29324 | -53.83419 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1f14bf99-3158-38ed-b5c1-948af25b5ad9 | -1.18737 | -51.76226 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 974bfd77-561c-37d6-b383-1226c8d48154 | -2.80325 | -53.04966 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dfb6583a-5879-3b49-9819-83ab6d557dba | -1.30361 | -52.86743 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d84b935-579f-3de9-882c-d7b88d91ec82 | -1.07266 | -53.64289 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dd0e4050-8d0d-3e4d-b01e-b2bb4cd1b398 | -2.02502 | -52.07738 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 750a013d-3f39-3281-a22b-6b45411b3970 | -1.62441 | -53.88879 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7650f735-6604-3879-b3a9-45ea07f66f2d | 1.90097 | -55.71823 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5ff28e6-fa63-3914-a1b9-3f50d2361fe5 | -1.33088 | -55.84447 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c5392e2e-e296-3528-a568-9ab5a05c99fd | -1.60004 | -52.29843 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1f8efd0-98f0-3a14-b81e-ca9714c1d505 | 0.94161 | -50.74837 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88a91321-135f-325c-839e-5b97077cad1c | -3.2738 | -50.61504 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fdc5c6b-630b-3961-80d6-5bdf2819b9ad | -1.66728 | -59.88066 | 2024-11-30 05:27:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c58dc49-b2ea-3107-bfe4-fea3e4745979 | -3.15074 | -60.68922 | 2024-11-30 05:27:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd947dd6-abfa-328c-8606-49e716686854 | -3.35934 | -49.76091 | 2024-11-30 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e02d4660-4800-3830-8aca-cc28b2d82ade | -3.31307 | -53.70248 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 013db930-b7dc-361b-9950-b8f39d021fc9 | -2.76734 | -55.33611 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 336c4ce3-1049-36e2-bd92-27ee3bb66f07 | -3.25141 | -50.62008 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2268fee0-f58d-314e-b13a-98e33b86d2e4 | -4.18907 | -50.69011 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 565679d3-fca6-3979-adc6-3e58b757b021 | -0.95273 | -51.65825 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75fcaae0-bf43-3a2c-834a-71b5d475434d | -3.2495 | -53.86322 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7970fb61-716c-3192-ae56-a256c57e998a | -3.30178 | -50.3805 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a17c8126-5e16-3ab8-b837-7a2e8680f2c8 | -1.16039 | -53.58745 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b9b1422-dc6e-37b0-9c7a-58135dc8da43 | -3.04681 | -50.27658 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47fd10fb-24a4-3ddb-a4eb-225fd9414fc1 | -3.40049 | -53.027 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8cdfc609-6f27-3f6c-a7c7-90ff6a36e424 | -2.61142 | -54.21252 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5875ef6e-fea1-3d89-8ab2-677b9282f178 | -1.15635 | -53.58247 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01e2d161-ccd9-3fee-95fa-0381e2687027 | -1.35252 | -54.6306 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ce59998-3b7e-340f-a47b-755478543707 | -4.03051 | -54.17512 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e344159c-8876-34e4-9c5f-6b014e7cc48a | -2.11584 | -50.34505 | 2024-11-30 05:27:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 404b5672-c22c-36df-96ea-792b305dc507 | 1.89709 | -55.71883 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5667812-3dcc-3c38-9995-754defe64bf0 | -1.76047 | -53.64073 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9bd569d-0864-3c01-8f2d-547704b4e9bc | -1.50083 | -54.94846 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 17998677-b2a6-3dcd-ba1c-accdf6363f67 | -1.83189 | -54.52648 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| a11fb87c-9f0f-30d5-a921-1e42b9fb6bba | -3.08563 | -51.40786 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 293608cf-9413-3183-a1a9-fa9a0595e871 | -3.09692 | -51.40921 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9e8ba986-d0bc-3bf5-8440-83af3c50bdd7 | -3.19616 | -51.42163 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf43463f-2ef0-3247-b858-580fa6eed708 | -1.64611 | -53.8713 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 195a2f5c-2975-3675-90c8-a0e6c1d34433 | -0.99483 | -51.72467 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e84cdd5-b928-3e89-a0b7-843564ecf47a | -3.30884 | -51.10796 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae119cba-94d9-3164-b408-7a58ab295a19 | -2.8383 | -52.91791 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e7b5140-9179-3ab5-873a-2a9c390475ec | -1.73899 | -53.75002 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README130.md)
