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
| ba819722-981d-3cf3-add6-fd2197e532ec | -5.12718 | -55.94851 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6951ca99-f931-3a20-8f40-044f1791ab12 | -9.25529 | -48.54473 | 2026-09-15 05:18:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42fdf0c7-38fd-3cc5-b367-464eae78c70d | -6.27963 | -59.91946 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7043e811-67b5-31db-aa68-22914dae6474 | -5.84247 | -52.05475 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c46315af-9963-3731-89b5-ccfd4ce98624 | -8.79222 | -45.88176 | 2026-09-15 05:18:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e7dc75ec-fd74-3c64-bd1d-ad6d5633fc01 | -10.68501 | -54.18081 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de6bf287-14eb-3109-86a2-49bcc2a99679 | -7.46356 | -46.14639 | 2026-09-15 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f54dadb1-ac79-383d-a047-0522aa67c4b7 | -5.44646 | -60.218 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e0c24a31-b973-3bab-95ac-9d9cf3b6f3f9 | -9.12647 | -65.83851 | 2026-09-15 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c189fee-719f-3dad-b546-2f1cccea98b0 | -8.54101 | -54.69969 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51984f36-5115-3254-8a5e-35632c2ee90c | -6.01904 | -59.9318 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 945b9d73-7b3c-3173-a626-8b54b50de7af | -6.84011 | -55.55439 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 56258dec-7ae7-32fd-b338-e75baff80912 | -6.3578 | -55.82824 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e43b0e0-864d-3c6d-b906-28a60886f91a | -8.4106 | -54.72445 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a09c9fac-4dcc-301d-983b-90d6735244f7 | -9.1045 | -65.56103 | 2026-09-15 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8a7f47a-d8af-3393-bbbd-acc9667f8840 | -9.2559 | -48.54001 | 2026-09-15 05:18:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9105f9d2-7c83-31b5-aec1-c9d4c7a99694 | -6.10566 | -57.62868 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c6a7095-27a5-3720-b257-8bc0a764c099 | -7.87395 | -54.72029 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 570d5be7-53d5-3ad5-9e9e-05a508776f04 | -6.11251 | -57.69594 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d025b74-eb78-3c07-8046-f1867d8c9c65 | -6.09233 | -57.69291 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f05b45b5-8b6f-3d85-a887-b8b29aa46568 | -10.67713 | -54.14242 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0fc43c09-9f87-33a9-8841-dba7cb2f6510 | -9.42139 | -50.10366 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8aa374b8-dc50-39d6-9a70-72e5b7a147a8 | -9.12576 | -65.84266 | 2026-09-15 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf1a415f-ca3b-3a61-a1ac-33e8660544a7 | -6.69131 | -58.70042 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89fac648-b7c0-3c42-b3ce-a991473c13cf | -6.67369 | -58.70477 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c085a507-d441-3681-99bd-879f0fa73883 | -5.13134 | -55.94504 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f35414f3-2e22-327f-af50-f53de6dabb22 | -6.67807 | -58.69835 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68d2d036-fac1-3530-a12c-39120434db0d | -10.98057 | -48.32797 | 2026-09-15 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5259ac26-491d-3903-820c-e1207d4b5c68 | -10.67231 | -54.1459 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c098ba9b-2f73-320c-9b3d-5dc6d348e224 | -7.87226 | -54.72681 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 066e9e0d-cb25-302f-b725-7cda386b2185 | -7.30943 | -55.61016 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec9ef906-24f8-319d-a04d-39b7f7311261 | -7.24425 | -46.15677 | 2026-09-15 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42f9f24f-3848-3e7a-be87-159e5b51a5cb | -6.69078 | -58.70388 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08ea9c54-c67d-3d2c-bb97-7007f155fca2 | -6.02463 | -51.78792 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f939303-280f-3bcd-969d-2f8ec654a849 | -5.44589 | -60.22157 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b61c2c73-57b1-3a0c-90c4-94167d60c37c | -10.24229 | -50.90925 | 2026-09-15 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b75adcc5-6599-3fe4-af17-265565d75785 | -6.37288 | -58.29756 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc50e0dc-0da0-35fa-83c5-7ed83cdea306 | -10.03433 | -52.12496 | 2026-09-15 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b978d5a5-1088-3f4c-a2bc-bd80ad458bf1 | -6.16019 | -59.94372 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46fe70f6-69cc-3a64-97fb-071261b9e7c8 | -9.15991 | -49.99413 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 429d37fe-997d-3fec-b3db-673526a72cb8 | -6.10965 | -57.66985 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d208c81-7a95-3863-a7d4-ab767e8f580e | -9.6453 | -59.60774 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d7f42c9-30d4-37c1-9694-8ca95ccff565 | -6.84513 | -55.54607 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 1bd0f9e1-ef74-368c-b774-5753f6a6ad04 | -9.58825 | -60.51345 | 2026-09-15 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec7c82db-9b25-355c-ad2f-a108ac87df15 | -5.35991 | -55.89346 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6fe43190-cdf3-3083-8e7b-745dca8baccb | -10.89823 | -51.56484 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb7eb0b4-8d5a-3c1e-828c-8eedf2b84396 | -8.06708 | -61.53449 | 2026-09-15 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6337c6df-e19e-3f0e-9c72-e4820d2f27b9 | -8.54003 | -54.70669 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa253d23-a190-3fcc-9a34-247146355e07 | -7.55752 | -62.32666 | 2026-09-15 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e83ce88b-9622-3426-8f30-f60b5c25f2dc | -7.23655 | -46.16242 | 2026-09-15 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86fba392-e860-31cc-853b-acf7d82d88e7 | -8.30783 | -50.89216 | 2026-09-15 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed05de49-d4ca-36a2-8711-c04d7aeaf024 | -9.10065 | -65.55713 | 2026-09-15 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 855181e6-eea4-3c67-83aa-6b5e20c72162 | -10.88404 | -51.55344 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e1b2fea-e25d-3909-b80e-67e62eb22144 | -6.7477 | -59.43143 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0adb4637-f51c-3392-86d1-60e87c418903 | -6.11302 | -57.67035 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb6173d0-ff44-346a-ac7f-11b93a118b38 | -10.58249 | -47.7404 | 2026-09-15 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 086f09ce-7a34-3ac4-906e-e1d62436c111 | -9.35475 | -50.14258 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc3bf7f4-3423-34cb-bf79-90411a345781 | -6.69409 | -58.70439 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cef7d46d-2dd9-3f0a-a9f6-19a260c8e4b6 | -6.8458 | -55.5416 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b2cf65c2-82b1-3d6a-a6c7-40b115e2987b | -10.66003 | -54.1401 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1003e75e-3b25-30d1-bbc3-d8c54324c619 | -10.69408 | -54.17794 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d05c7b5-1f98-3e21-8d27-33455c901076 | -8.53751 | -54.69559 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6e66402-284e-3a81-a1a0-f65ff381b369 | -5.18141 | -59.76371 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 264b98b6-43d6-3aed-a6ba-bb933dfc0f22 | -6.27133 | -59.92891 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d92c5a4-1b20-36e9-9b77-3ad236aa0423 | -10.66858 | -54.14126 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7762a2cb-be4e-313f-aecb-9d9d13dfb214 | -9.3594 | -50.19479 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f63843c-4f53-3454-ac2e-c8231905992d | -8.53653 | -54.70257 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 180f1903-7d4a-3770-a2ec-b03ed415c307 | -6.01294 | -59.94881 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c2a7988-10cc-39cc-a5da-6b84c641b7f6 | -8.4099 | -54.71931 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0414c568-8660-3091-8556-e7efabd4abcd | -9.02516 | -61.03749 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8fa18b7-0752-3c0d-9497-63bc016d658b | -10.66076 | -58.76768 | 2026-09-15 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5756075d-4edb-391e-a22f-dfce7be09586 | -9.41634 | -50.09925 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7f79fed0-f21f-3d43-afa1-91af55004d1c | -6.2935 | -59.93951 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 557d056a-5781-37d2-add9-3c1290a53f6c | -5.20099 | -60.03004 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca9dcc43-7308-34f7-948d-c42cabe7fd28 | -6.10016 | -57.68678 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 65791219-e2ff-3a62-9614-5b474e7cc028 | -6.83706 | -55.54937 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 4e9ed996-58c3-3d99-8b30-7a0d4616f7e3 | -7.61527 | -47.29417 | 2026-09-15 05:18:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7ff3c0e-b40d-37ec-964c-fc995df3e9d4 | -9.53017 | -63.62684 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 235d978d-c669-3b32-bd4e-c3637a3ab87e | -9.67678 | -65.79775 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76498118-b728-351e-8168-450dda3ae447 | -6.11196 | -57.69952 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b37775b-ec6c-38ad-88dc-9cf5da64ccbe | -10.94833 | -57.19081 | 2026-09-15 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb9cea0c-4eb5-3a1e-9cf2-0daa4206c0f6 | -9.3544 | -50.14396 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3547d33e-41c0-34aa-91f2-960114b6cd7c | -9.07392 | -61.01217 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c0a3639-895e-37a8-8882-9275cb6eb8c8 | -10.50651 | -53.56963 | 2026-09-15 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb6ab196-a271-3743-acf9-b1a06dfc21fa | -6.22353 | -56.04828 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fba33a4-aa75-3fee-a8ec-c3152fad9dae | -6.1385 | -57.69669 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ec24852-582d-3736-8829-8b5d6d31c2db | -9.35824 | -50.11491 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 200ba555-4a80-3766-8cf9-0f6c8c27ded8 | -8.53604 | -54.70606 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92750564-63a7-3fb0-886e-e5cd61128e73 | -6.68362 | -58.70632 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1c12c5b-7be5-3ef8-ae59-5db644919bd3 | -9.85389 | -65.17883 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5deacea3-8092-3e2d-8d76-1334bf65aa19 | -10.23658 | -50.91183 | 2026-09-15 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b8127f4-2434-3013-bfd7-aac55c220efa | -8.37331 | -54.72949 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e29a3c4d-533e-3d45-9781-75c4915df360 | -7.55396 | -62.32608 | 2026-09-15 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 207cc8c0-591c-3a05-bee9-b603e00d53d7 | -7.32188 | -59.5652 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec425356-0e2e-3623-88a7-7deb82d416eb | -7.31083 | -55.61269 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c41d7960-a5cc-321d-b8f7-aa7eedd8aed5 | -9.13147 | -65.8351 | 2026-09-15 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 38bc471a-8b6c-3fdb-bf97-b52ee65b1255 | -10.94363 | -54.08918 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52f6c133-e22e-3a53-a643-fb9dd115b54a | -6.11472 | -57.68163 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c0132ca-3ff4-3be6-b134-fd2121640227 | -7.23372 | -46.17696 | 2026-09-15 05:18:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 952a874b-6de0-3eec-810f-cd0266edd4e5 | -9.4102 | -62.7113 | 2026-09-15 05:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |


[Clique aqui para ver as próximas entradas](README62.md)
