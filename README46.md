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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee35d252-4cb0-386f-8bf7-ba6d0a4cc088 | -5.57857 | -60.19254 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dc1dadf-72a3-334a-9e68-539949ce3ed6 | -6.94843 | -56.46117 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f75ef862-1913-36e2-8878-ec4f43d53a93 | -3.97279 | -55.64106 | 2026-09-02 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 442dc1af-4e5a-3c9d-b05d-b93164456391 | -1.47595 | -54.23717 | 2026-09-02 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee553feb-60ed-30c5-bc08-75dabb43c37a | -3.24404 | -47.25554 | 2026-09-02 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec161bdd-997a-3fdf-bf53-909de2fba8ea | -6.14077 | -57.77382 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1873886-f8f2-363c-b4e5-ddfff8bc117d | -7.3526 | -60.57775 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20d4cceb-cdff-3e8c-b340-86f1d7114d5e | -7.31299 | -60.57518 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d934840-a91d-3958-a8b7-9668e0ccff29 | -9.00328 | -50.78085 | 2026-09-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d177ed36-622c-3bc8-a0e8-cc10bbb9f63a | -5.2459 | -55.90234 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2bdf8b7-1374-3a39-ab49-44383566a210 | -6.04792 | -57.73752 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69f6fd4a-ad30-3e77-9c23-c3dcbede9e0b | -4.34611 | -55.44725 | 2026-09-02 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c22c1596-22c4-37f8-b9db-2228e0443a2a | -6.94283 | -56.45301 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 001d5ccf-58bf-3e7e-9ce6-854cb363fb79 | -6.18982 | -55.28276 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ef9c4e1-8940-304b-a19b-fb824535d585 | -4.12061 | -51.02694 | 2026-09-02 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15ed7c92-6a23-3aff-b061-5e9e7d1c9351 | -5.88393 | -57.76425 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 710fbe91-d239-38e7-805c-9b7d2ceab50a | -3.59831 | -54.55197 | 2026-09-02 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b197e0ff-f7be-369d-aea4-58fe9ee11cae | -6.10539 | -57.86715 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13067427-64b1-34b2-a5d2-3c6dc52b16ed | -7.3484 | -60.58114 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b619803e-1ef8-3a38-bb88-5a66fe2a9306 | -3.09537 | -61.21869 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf3de9ea-ee02-3c69-b1b5-5daf88aa06f0 | -7.19885 | -60.67375 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 178f01aa-049b-3c68-9d0f-e044c9c74e63 | -4.96525 | -55.85619 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23e5265f-81c8-34f0-9793-a646bfc3aa89 | -8.4417 | -54.70418 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cea79d9-8e6b-38a0-aa0e-043119d04bd1 | -3.12011 | -61.23762 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd32da4c-9342-38c9-81b6-22dc217efa69 | -6.80837 | -59.09848 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 681e73d1-f49d-304b-b872-98c3565305d4 | -3.85236 | -44.05347 | 2026-09-02 05:16:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2a0ae1b-21d6-3250-b879-d8adadb2396e | -8.447 | -54.72003 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2dd92ba-7b7b-32b0-8580-ea14ccb0e4dc | -7.29346 | -49.81406 | 2026-09-02 05:16:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6aca28e-1a50-3c82-ade6-d57f12b54536 | -6.91283 | -62.9082 | 2026-09-02 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1f5738b-14fb-312f-ac58-8f69c461eff9 | -7.35129 | -60.58571 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1f493d5-f433-389f-a41a-bd4d17821ea4 | -3.12168 | -61.22795 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e47828b-89fd-3cfc-a85c-509a7c33230b | -3.65969 | -58.91717 | 2026-09-02 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44f87abd-a02e-3806-b410-930dca611d9a | -8.44221 | -54.70193 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cfc99b1e-6f5c-3644-9691-efc28914d8dd | -6.00549 | -57.83353 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31bf3d21-0fac-357f-88d9-75d109be1972 | -8.1136 | -54.95255 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8db90d15-984e-32c5-a1a3-94b5fde9b7c3 | -7.52764 | -47.33583 | 2026-09-02 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f38a5d9a-9d99-3cf8-8d5b-f4ac1d63d7d9 | -6.95289 | -56.45459 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcb07f60-fa69-3c52-ba0a-16175512a73a | -6.94563 | -56.4571 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac71303e-6613-3420-abe1-754b89813c24 | -6.19042 | -55.27897 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02345ad7-5a42-383f-8a5d-38e49ec14cab | -6.80895 | -59.09489 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0121935e-9fff-3d5e-8199-286d689a2df8 | -6.76792 | -59.73735 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 693485e9-5514-3afb-8529-f604f2e5b4f1 | -8.44876 | -54.73336 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fa7267fa-07a0-33b3-b9f5-59ca9f478408 | -5.24534 | -55.90593 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18304330-8b12-3fe6-b1d8-64f735d833d1 | -6.15677 | -57.77991 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45707a02-806c-366f-8bda-a217109a5822 | -6.1843 | -57.7347 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6ce069b-68c5-3e54-be78-cb664703160c | -5.97272 | -53.59073 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e6c11dcf-6cec-37b4-b00f-d2a855a417a7 | -3.62048 | -60.5727 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cef6b058-759f-3be4-aefd-43cbdd06c3e4 | -7.5746 | -61.29848 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04590dac-109e-360d-824d-477478624134 | -8.4603 | -54.73079 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4c771ae-dd92-3ef9-8511-179f66bce108 | -7.64654 | -45.87622 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 507e06d5-03ad-3e67-a7cf-0a1590ba2b0f | -9.22856 | -47.97653 | 2026-09-02 05:16:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2dfa9a16-3387-3ff6-a16a-4033dad957f0 | -7.35903 | -60.5829 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 199b89bb-e0af-326a-bbac-f12e66a47d4c | -1.51298 | -54.9621 | 2026-09-02 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02baa2bd-d380-3156-9df6-9931b5b59a91 | -6.14791 | -57.7502 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 55638f4c-5813-31ed-9411-8267cec432c3 | -6.1025 | -57.71427 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb1a081c-24ac-370c-adbf-4e275632aed6 | -5.96841 | -57.68236 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2adc694-3a8c-3621-810d-4e50aa345ef9 | -6.64834 | -59.43505 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10e95730-f1c9-3bae-a570-2225118d925c | -6.11396 | -53.44963 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ba5272a-d426-3298-ba70-bfb87ce0b7f7 | -6.09422 | -57.70233 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 111b01e9-0735-311a-8b50-a8f91d34098b | -7.56752 | -61.36403 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a480bb84-0699-3860-a8db-411c85789462 | -6.37817 | -54.77026 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f10df22-f2e6-3738-97f8-032ef7d6a3e0 | -5.88448 | -57.76078 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b97c39b8-d834-31d6-b7e7-a9c0c78d8801 | -3.07054 | -61.22463 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f785297c-4b06-3225-899f-824c7b04b5a8 | -5.948 | -57.68267 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b7c1b6b-4216-3c1e-9bc7-159e74e2b96d | -4.51796 | -48.75263 | 2026-09-02 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 744f5666-cf1a-3789-9f06-6d9ac2c0f7a8 | -6.85854 | -59.48003 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2f13de90-b511-3d28-b73b-2f4a526f8246 | -5.21255 | -60.05801 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1603c9f-2083-38be-998b-e6954b7acda5 | -6.15947 | -57.72013 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a45f44f8-5655-3a6d-bc81-62ed863e6ebe | -3.84475 | -44.05817 | 2026-09-02 05:16:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f81311e-7161-33b2-8ce9-3bf4f14f0641 | -3.52623 | -50.53186 | 2026-09-02 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ab1940e-2dee-33ad-8ceb-9bba9a77373a | -3.65685 | -58.9129 | 2026-09-02 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02a11b21-e8f1-3085-bcbc-a0c9d01ca198 | -5.17588 | -60.28944 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0ad7f89-9cbe-360e-a7f0-631063da1ee8 | -7.32631 | -61.14585 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1569ca1-4a6f-31f0-a391-a68bc9c6a2c3 | -8.44283 | -54.69773 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3bbadaa0-9aa7-35be-811e-74cf612cd9ce | -5.86197 | -51.70774 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d58ef70e-5b65-3579-a328-b33c36556eff | -6.0905 | -53.80311 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 884b1bab-c53e-3546-832f-90d832c291f1 | -5.25206 | -55.88488 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23f03349-352a-399b-b82b-6b0d259821ac | -3.86527 | -52.15085 | 2026-09-02 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21a749c6-95b8-3042-b1b2-66b6f2e2a7aa | -6.42899 | -53.56623 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68235600-604b-3ab5-8c20-a6797b316d1e | -6.95621 | -59.78657 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e3c430d-40c1-3539-9b5e-c577957dde19 | -5.58436 | -60.20171 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee9de3b4-fdea-31b9-9ea3-ebb6785f423d | -3.19359 | -61.13794 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1b6ca9c-80f0-3445-9722-fe1de916c55e | -6.80284 | -59.43362 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 311f66e1-2057-31e4-ab30-d47f2f52f98e | -3.12555 | -61.22859 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0d54162-09d1-3e73-9ead-01ebfdb33e85 | -8.44638 | -54.72429 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a080ad8-403d-3918-9bf9-9c1eddefa6d1 | -4.96581 | -55.85261 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b9932c8-e014-3fdb-ba4c-4112806ba637 | -6.03016 | -57.67797 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51c0e697-480b-3515-b9ba-d778a95da4fc | -6.15346 | -57.77938 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d37f5e5-5705-3cc8-90d8-9dd823a9581b | -8.42648 | -54.70627 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ee298705-26d2-32aa-9530-b0fee03623fc | -6.15286 | -57.71908 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91e7010d-cc34-3ca9-a3fd-f19e7d2f8414 | -6.08057 | -53.66886 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfde9090-351d-32e5-8eb6-3e1ee712d055 | -6.56105 | -55.13585 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fd7da34-bdd8-3d16-b294-dd93ef3d7c57 | -3.46621 | -59.65784 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 456df3f1-2c12-3a34-b85a-f6af6e074d9c | -7.53889 | -61.37708 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1878987-3b63-34e8-9179-b020a0abcea4 | -5.94855 | -57.67921 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce25b8d7-8bdc-3c26-8c87-f4fd060b9536 | -6.81058 | -59.10622 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bddbdb8f-ed95-3f8b-9d50-1f7efc5fd77c | -3.06903 | -61.20248 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a4815ca-b807-3a8b-b6ed-112037eb5339 | -8.47612 | -54.72446 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 57f15330-0200-35b8-8030-d717a09d1d20 | -4.16044 | -47.83414 | 2026-09-02 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbd2e5ca-f186-3831-b80e-312cd8e78150 | -8.45741 | -54.69987 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README47.md)
