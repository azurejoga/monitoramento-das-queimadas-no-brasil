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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 284931e8-1aef-3b0e-9adb-3f8654c6d8ca | -3.67052 | -50.29395 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5b1a58a6-6722-30ad-bcd2-0b634cb86ff5 | -3.66987 | -50.29814 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 85d9d360-aa3d-3e5f-90c5-e50fdcadbfd2 | -3.65511 | -50.12725 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8f0d68c-55ba-35c2-abed-404fdf7c1047 | -3.65422 | -50.15771 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0875c85b-7a0b-343f-8770-01d2ec47f890 | -3.65123 | -50.15285 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ab7e306-374e-3b57-a5dc-c86908d481c9 | -3.60462 | -50.57882 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58e3cab5-b483-35cd-99c2-696638e1d917 | -3.96087 | -49.96656 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90c4e08f-e8a0-31c8-8754-b22af55c296a | -3.93466 | -49.89045 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f6b8023-d30d-33f2-9d10-f34e76c846b5 | -3.93398 | -49.89491 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6babde9e-0231-34f3-a92e-f7747dc91f88 | -3.88051 | -50.04788 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0953c569-5eda-36b5-a219-57e83dd09275 | -3.8734 | -50.02016 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82a98b94-76dc-3709-81ed-f152997e12cb | -3.85281 | -49.98136 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16edab2a-70e7-3883-b232-45f8b96ccda5 | -6.40383 | -50.79187 | 2024-10-28 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d0c1fa7-a375-3eee-bc1f-ebb0ac0d91fb | -6.21462 | -50.85228 | 2024-10-28 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85b5b49e-bff9-3dfd-825e-a05d838244d8 | -6.21397 | -50.85649 | 2024-10-28 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cb866ab-7665-3d73-9b62-c7bf9d3da86f | -6.211 | -50.8517 | 2024-10-28 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26a9cfff-17ff-331b-83df-3847c0415794 | -6.21036 | -50.85592 | 2024-10-28 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 315b05c0-b50c-36d9-9c90-dc7b23cf63f2 | -6.20014 | -50.85001 | 2024-10-28 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd5ca633-84ea-35fc-9edb-711cac3f364d | -6.19652 | -50.84948 | 2024-10-28 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95699c7f-87d7-309e-b234-3f2246af751a | -6.1929 | -50.8489 | 2024-10-28 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5af6d5d3-39ff-31bf-a7d4-ae3809257542 | -6.18929 | -50.84831 | 2024-10-28 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cedf4c8e-1190-317c-b47f-ce6394ae8520 | -6.18567 | -50.84774 | 2024-10-28 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 083341db-407f-3c6f-a1da-11c7ac887a02 | -6.18503 | -50.85196 | 2024-10-28 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dbe2a64-7a3a-36d4-acf4-b61db4c1c0f1 | -6.18141 | -50.85141 | 2024-10-28 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6c10ad4-f652-39eb-a6f2-9c9b14336f88 | -6.02459 | -51.09694 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df9bd0c2-fd9b-3471-9fb0-8064613a8f09 | -6.02402 | -51.10072 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f88d359-c699-314e-98c3-ceb915edb6bd | -5.95542 | -50.88517 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4c5a96e-de91-36a4-839c-3585fbfac826 | -5.91027 | -50.13253 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 852fe9f2-7bf0-3090-ba98-2dbe8f07862b | -5.90652 | -50.1319 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 499ace18-2e32-383d-b2a5-e865bf34f50e | -5.74045 | -51.11013 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d0d1438-1e85-361f-b293-006e80aa5b99 | -5.66163 | -51.10221 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07d7c2cc-3896-378a-9f80-4e8d2ae2ef15 | -5.61074 | -50.13973 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef97d6c8-2d52-3960-90db-4a8a8bb7c690 | -5.56638 | -50.93933 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc8cf4ed-53ad-3d08-8f0a-57617e48180b | -5.51809 | -49.80204 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60c5c169-721d-397e-a2bd-c4226bf10b77 | -5.51784 | -49.79922 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1c2c388-6e7e-322f-9df2-60e093f0b399 | -5.38923 | -50.96474 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaee87c0-e504-334c-8186-5c7201550037 | -5.33922 | -50.98194 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d8c2e49-0047-37f1-982f-bf3b2ff22ace | -5.17745 | -49.98124 | 2024-10-28 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46dd65fb-09cc-36b7-a634-f3fd493df5d1 | -5.16412 | -50.32434 | 2024-10-28 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 255dd7d9-fa67-3ed4-bb62-3a9a000239c5 | -6.96559 | -50.99298 | 2024-10-28 04:57:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 957bd16a-d83e-3eea-9ee4-0cdedfc4b645 | -6.96491 | -50.99053 | 2024-10-28 04:57:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39407daa-c464-3576-84ff-4389e74ea195 | -6.67877 | -50.90686 | 2024-10-28 04:57:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 591c99fc-16ca-3bab-8d3f-8f64b5140fc1 | -6.4921 | -51.04818 | 2024-10-28 04:57:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4a7a388-56c8-36bf-a459-282b66a582c2 | -2.24623 | -50.45725 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7857aac9-70f6-31ea-9a3c-daed2b119bc1 | -2.2427 | -50.45671 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 45fcb385-2c5a-303f-91fa-7805c9c56b2e | -2.19906 | -50.75826 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a53f432a-2853-38b1-bd4a-43a7d7cce1bf | -2.19593 | -50.59479 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c48cd73-7177-330b-8f3e-12f90cf2d70d | -2.19533 | -50.59869 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28c6c1f0-4f77-34c7-8145-a3b9d0fd4b16 | -2.19242 | -50.59424 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3fb34507-3c20-37c5-a5d3-0a9f99b8f73b | -2.19182 | -50.59814 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb0ddfd4-1223-3de9-98e9-52f60edcb4f9 | -2.18892 | -50.59369 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6fbd1f99-2870-3df0-9805-33c9eaa2486c | -2.18831 | -50.59759 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8894bd58-4ab6-3ac5-b898-3d84768d6208 | -2.1871 | -50.60539 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8895940-f114-3406-b932-3849ae9e23ff | -2.1865 | -50.6093 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 806f4511-566d-3c48-a328-7d2535c12795 | -2.1842 | -50.60095 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a89c7023-8ed2-3149-b684-19484f15a6c8 | -2.18359 | -50.60485 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d58dcf44-d700-3aa7-9b09-6d37c6ef63bd | -2.18299 | -50.60875 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54e133fd-22ea-3bd5-9afb-c4bb891e4182 | -2.18179 | -50.49999 | 2024-10-28 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5222a1f1-eb39-3f98-99dc-890dc22dc151 | -2.17948 | -50.60822 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86829bac-fd9f-30e5-9ee5-31ba7a9f0758 | -2.17744 | -50.78251 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 898d71f1-e953-3885-bf85-da301246d0a2 | -2.17396 | -50.78197 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16c31e45-7eb0-30ea-9731-281811728ad4 | -2.17336 | -50.78581 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 067a17bf-2bba-3ad8-b79c-59a2997a6b25 | -2.16194 | -50.74463 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ee6fd08-faae-3fe1-8395-9469fbc23cfb | -2.16093 | -50.97894 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c408656-71b4-335d-89e7-3bf584352fdf | -2.15647 | -50.80286 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e7f468e-6368-3c6d-acad-78bbc3fe7b81 | -2.15587 | -50.8067 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac6c2218-52eb-3470-b282-bb3d689d1db5 | -2.1493 | -51.00804 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32d8b444-37f9-3763-beae-311db9054303 | -2.14586 | -51.00751 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb3e219e-b912-35a0-897a-a107213653ab | -2.10697 | -50.91631 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 914e8d79-f26b-32ce-8ec9-4cc1f07453c6 | -2.10077 | -50.84127 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07fbe1b4-ea8d-31b9-a930-d4b9242e5941 | -2.0973 | -50.84073 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df760035-035b-374c-898c-0e5206de97f9 | -2.07309 | -51.40612 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a350823-0df6-3c03-82b8-4638c53a9b31 | -2.0697 | -51.40559 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b101e00-f1ce-3225-ba12-8b879e5c9bf5 | -1.65441 | -51.75433 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc403e38-78da-3410-b72e-9fe93037918e | -1.55507 | -51.62634 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9c7e9cd-3530-3fc8-8b73-10ffabfca359 | -1.52466 | -50.62275 | 2024-10-28 04:57:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e1d7f24-d99c-3b3f-9ab0-027ce469fd6d | -1.45116 | -51.68343 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78c0f5f7-3671-334e-b271-e9d7b56698c3 | -1.36191 | -51.42366 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c4be01e-69a3-3d3a-ae57-ebcb8eb90879 | -1.36136 | -51.42727 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2b16a8b-2c73-3e35-aafb-5454bb764052 | -3.53125 | -51.57809 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 021962ba-a1fb-362a-8bc9-5393ac62abb2 | -3.52729 | -51.6492 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b4825d4-20b5-3a49-a407-057211e0f4b1 | -3.48126 | -51.62751 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a697363-480d-37ab-8165-19588ea635ab | -3.46028 | -51.58285 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f11a957-28a4-3367-bb43-f64ef871855e | -3.45852 | -51.63908 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3abfed8e-d0b4-3670-8649-48d75ec86a80 | -3.45795 | -51.64274 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d60483d-1c25-306c-81ad-ae8b043039f1 | -3.40168 | -51.53202 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4afa495-b3d7-3bf4-9640-b8be2eb9ff34 | -3.40127 | -51.532 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 184b2676-d1a8-364c-b20f-e04b060387bf | -3.37385 | -51.5732 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f616fed-ccdb-3914-bc9e-7dbe36994172 | -3.35188 | -52.16941 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25a9217e-d0a4-3e7b-84c7-57c2c7714d28 | -3.34604 | -51.52728 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e90fc283-0f8c-3552-a6ac-2a1ac730e601 | -3.34262 | -51.52674 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92956520-eb04-3fba-b993-8fa8c57e31d9 | -3.33574 | -51.61629 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 067c2718-0062-38eb-ab7a-3299a7911eec | -3.33517 | -51.61996 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d08c484c-2309-3786-9d27-346c45613b18 | -3.33177 | -51.61941 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 314a508a-7344-3ffd-87bd-1920368535fe | -3.27259 | -51.61447 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 175cbb7f-5c2c-3c50-a7a2-9852de242bee | -3.26245 | -51.56775 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a0f5cb0-d7b4-3532-b87d-c8594330d6a7 | -3.25904 | -51.56723 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b49a90c-78eb-3938-945e-a44923a0bd23 | -3.24371 | -51.55358 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e84893dd-f551-32ec-9be3-c05b3ed0e446 | -3.24314 | -51.55725 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59ecdf55-ea05-3aba-8cdb-f1d123f56d3f | -3.24087 | -51.54936 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README59.md)
