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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 395bbf38-e236-34a4-b196-28ae68bcbc5b | -5.19311 | -45.03808 | 2025-11-16 04:06:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40c910f0-c5b3-35a3-b4b8-eab510d17bf0 | -4.31462 | -46.54479 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf464901-d2fd-3798-93cf-0aea0ce5a77b | -3.04826 | -46.93166 | 2025-11-16 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f4abcc9-f297-3c25-bb1e-a7ce4c5b0ee6 | -2.8012 | -52.97173 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 35401925-5586-3a6b-8673-2e39d5cf94f9 | -5.717 | -41.40362 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9d89cc11-8593-3c16-94c6-51871eaed0bd | -4.62121 | -47.41178 | 2025-11-16 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 759c57ea-4cf0-3ae4-87fe-4f8d67d202d7 | -2.9907 | -43.2336 | 2025-11-16 04:06:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c6b37b5-418c-3965-9d37-81e5b19528e1 | -4.54456 | -43.22548 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ea02bd0-f8e2-330f-91d2-04815da4799a | -5.42289 | -43.17572 | 2025-11-16 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56915ba9-15e4-3a55-b79a-132f204c8851 | -5.24489 | -43.90978 | 2025-11-16 04:06:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 16863bca-017e-381e-998a-f872061c4352 | -3.58291 | -41.66039 | 2025-11-16 04:06:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e9ef402e-b933-3d3d-ab9e-fc5c746bccda | -4.45924 | -41.7919 | 2025-11-16 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| baf7e760-9c8a-3d4c-8626-356ded3a7256 | -5.15939 | -41.12465 | 2025-11-16 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e807a841-44a8-3402-8039-119a97283903 | -5.43007 | -42.58683 | 2025-11-16 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4830b8cc-4e95-3f64-998a-9483a008a768 | -4.35244 | -44.35102 | 2025-11-16 04:06:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0c8e84a-7dbf-3663-a03d-ee522c188e2f | -4.20799 | -48.56438 | 2025-11-16 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32f84db6-e77c-3fcf-8204-d8ed3cef41e6 | -5.09018 | -41.47713 | 2025-11-16 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 877b0b6a-7888-3fa8-97e1-b79b7a4669ff | -2.52481 | -47.81437 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 2a9a13fc-5ae0-3e75-8484-7ee89d9fe86c | -1.16978 | -49.20658 | 2025-11-16 04:06:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec4768fb-17a2-39e6-a06e-076ef2688c2a | -4.45592 | -41.79137 | 2025-11-16 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 56ee0200-b59e-37a4-bdcc-6948b811e144 | -4.45261 | -41.79085 | 2025-11-16 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f40c34a5-ccd5-3cbd-abed-1083f97dae19 | -5.20267 | -43.47517 | 2025-11-16 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 104ef3f6-fd8f-30fa-9045-3ecd4393f357 | -4.39594 | -49.66354 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44c27d4e-c745-32a2-a663-cd775329f23b | -3.41892 | -46.14898 | 2025-11-16 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bb374c8-18aa-36f5-9dca-0596e09a0c3c | -4.94076 | -44.53732 | 2025-11-16 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 131d7023-6cb2-3c82-ad47-929ce0f0a0d6 | -5.52886 | -41.77692 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6e479345-f165-3e54-aea4-31bc31020212 | -2.89362 | -50.40873 | 2025-11-16 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bb35bfc-e82d-36ce-8be6-9d4e5569ac46 | -3.32914 | -45.85558 | 2025-11-16 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a49e7bc5-ce43-3d78-813e-7afad126ab36 | -3.89482 | -47.18943 | 2025-11-16 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4590989-3cdf-32a4-8d85-c129a5f7d827 | -4.66507 | -45.27902 | 2025-11-16 04:06:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c0b7b6e-6231-3872-b663-0b3a999a5868 | -5.03051 | -42.84755 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4213f14c-31b1-3c4d-a69d-00381e4885ef | -5.47672 | -40.96647 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 32b62dc7-e801-3366-8678-b740364e8a44 | -3.82357 | -46.0233 | 2025-11-16 04:06:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f59fa0c-757f-3081-ad97-9787da22b8ab | -2.41186 | -46.30709 | 2025-11-16 04:06:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 284ea798-afd3-3c55-9568-fc629f65ead7 | -5.59338 | -41.06604 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2dd720cc-e697-3237-9e15-0739c332b531 | -4.69776 | -46.31477 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 362e6394-1b22-3861-a862-012ee6c68800 | -3.8861 | -47.1879 | 2025-11-16 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc4722ab-4f74-37c8-9d5a-baaa2e78d7b7 | -4.09687 | -43.34695 | 2025-11-16 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0f2d24b-c349-389e-9851-38d741b15b7e | -4.42915 | -43.39814 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d675a2f0-9d66-3184-93d2-6bacfddda10f | -5.5253 | -41.77599 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4d6e84f2-0045-3df5-81eb-d001ef49e305 | -3.54643 | -41.99512 | 2025-11-16 04:06:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 96c4ee00-c2f8-3a92-9590-df8be547bcce | -5.46957 | -40.96888 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3ec25cbb-2e80-3a38-bed0-c1253dd111e0 | -2.89343 | -53.28673 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a3f12d2-ec77-3f72-a613-b0099880dc3a | -4.44542 | -41.79327 | 2025-11-16 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b942b66c-c262-35ba-aa96-e058573626e3 | -4.60391 | -41.73645 | 2025-11-16 04:06:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e65f1e77-d913-3cc3-b814-8822373dacea | -3.38591 | -47.18613 | 2025-11-16 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dc093bc-40c3-3d9f-89cc-4a649d1e9341 | -2.582 | -51.83235 | 2025-11-16 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3457e949-e374-3623-ba47-04af37617720 | -5.05977 | -44.70307 | 2025-11-16 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 46e319d9-07db-3662-98c7-515e67ec3de7 | -5.00562 | -41.96746 | 2025-11-16 04:06:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 89ffca34-64cb-32d0-9e1e-cda3e44635f2 | -4.76909 | -38.71114 | 2025-11-16 04:06:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2749e56e-6e57-30ad-8384-178dafca57a9 | -3.79109 | -43.37555 | 2025-11-16 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c783db4-38c3-36ed-804e-f00c93c3a647 | -4.84184 | -45.42885 | 2025-11-16 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1bfec1ab-77ac-3109-af35-70fb15d518a8 | -5.24777 | -43.91428 | 2025-11-16 04:06:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82a0fa07-600e-39f1-a688-ecfbbd485b5e | -5.20206 | -43.47897 | 2025-11-16 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfe5868a-943a-39e2-bb40-00dbebc79090 | -4.4263 | -43.39377 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a1ee084-fcfc-33b3-a1dc-2c23d9ce9ffd | -4.01267 | -42.89113 | 2025-11-16 04:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 59542e17-2c00-3656-8a4b-fa5731a56f99 | -5.34213 | -43.0465 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6c707930-d90d-3bce-9134-b945c02bb0b4 | -4.53086 | -43.22774 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30eb8658-5b51-32fe-a0ff-c9d5eb582547 | -3.02202 | -51.62798 | 2025-11-16 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63ff2811-2dd7-3506-8026-2cde307243c6 | -4.8637 | -44.15903 | 2025-11-16 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a199617-0712-38a2-97e9-8395139252f0 | -4.72886 | -46.37909 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6caef87-ad7b-3350-a061-7a8a94cb26cc | -5.53327 | -41.77053 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc8faceb-1553-337b-b5af-a25b47356188 | -5.42272 | -43.26313 | 2025-11-16 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b052f91-f82f-33d1-aa79-22f3749a7057 | -4.11209 | -50.73369 | 2025-11-16 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dea4778b-40ab-3266-b91b-4fd1264d6557 | -3.99385 | -44.27581 | 2025-11-16 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c37280b-acec-3f86-9918-41b57af683a6 | -4.43014 | -43.41398 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a516ab16-6d91-3ba0-a400-bf5bd5922648 | -4.73639 | -46.38422 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8e077f7c-34b3-3404-87c7-bb7c8ba96a3a | -4.40994 | -43.40683 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 924c3df8-94fe-3e1b-9988-1d7ae8498347 | -4.10656 | -50.73274 | 2025-11-16 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24502234-e2d9-3851-bf31-eacd8527ef05 | -3.48555 | -41.50283 | 2025-11-16 04:06:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c868238e-26a5-3c8d-9b4d-61fd0b628d42 | -4.13185 | -43.19665 | 2025-11-16 04:06:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac8e2a1f-56c6-38b6-bafd-46c90eee64de | -3.21767 | -49.22173 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d3dcdb13-3bec-3baf-a36e-e017e6fbcfaf | -5.17615 | -44.31145 | 2025-11-16 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43e0ee37-33dc-3631-8c72-f9357de7f4e6 | -3.58163 | -50.4238 | 2025-11-16 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57370812-b09a-3398-8758-277b3bee3ea7 | -3.7889 | -44.24544 | 2025-11-16 04:06:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1aa49f38-749e-3bfe-889e-7294ec3e84b6 | -4.93713 | -44.53666 | 2025-11-16 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6eff0dc9-cff7-3687-bcf5-a63ce29380fa | -3.4462 | -40.7416 | 2025-11-16 04:06:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8321b0a7-4ca3-3dbe-acb9-841a7f4fa450 | -4.90777 | -42.58095 | 2025-11-16 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db5ce2cf-eb8b-3652-a3c2-e496f237cdd8 | -3.53432 | -44.84167 | 2025-11-16 04:06:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73e5c0a8-4ee8-35c3-a540-02ae81893de1 | -4.3067 | -40.69356 | 2025-11-16 04:06:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 19451f28-eadd-3355-8eec-57991342602a | -4.86436 | -44.15497 | 2025-11-16 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e333b8c-88e6-3d3f-adc9-435771db1adc | -3.81433 | -46.0291 | 2025-11-16 04:06:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bfdc4e7-2daf-3b72-bbf7-a219b6ca664a | -5.52888 | -40.8932 | 2025-11-16 04:06:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b6acbb1-26e1-323f-af67-80e4ce2c649b | -4.16294 | -46.84102 | 2025-11-16 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 517a65ed-c96f-38ab-923d-305c0fd3b714 | -4.42791 | -43.40579 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 449a8dfe-c328-3656-89d3-ba9a33948821 | -2.17476 | -52.09011 | 2025-11-16 04:06:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5290e437-633d-3404-98ac-be00e6120673 | -4.52 | -42.17781 | 2025-11-16 04:06:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e7d69252-05d6-36f5-a5c7-9d1d3f30bbe8 | -3.21897 | -43.35144 | 2025-11-16 04:06:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 070cc22e-d7b1-3c73-b081-7fc094aa51a1 | -4.88927 | -45.02153 | 2025-11-16 04:06:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a386d8c8-af37-3c8b-a13b-e997abc68711 | -4.35326 | -44.34959 | 2025-11-16 04:06:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea10a3bf-7b9a-350c-873e-3221bd41dfd2 | -1.93635 | -47.03573 | 2025-11-16 04:06:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 906a2a48-5e84-3eb3-9802-86c2798c002c | -6.04427 | -39.65985 | 2025-11-16 04:06:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bda682cc-6fad-3287-92d5-931615b4e640 | -4.26453 | -42.65319 | 2025-11-16 04:06:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba623c95-e1a1-3c08-95c2-b123881accd9 | -4.48908 | -43.35686 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bedbe190-26ec-367e-af40-d6f536a381f8 | -3.56637 | -41.72197 | 2025-11-16 04:06:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 19131986-caa8-3979-a008-8398b60b2d22 | -4.72827 | -46.38268 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 629f3582-1395-3501-ba67-aa3cbb85552b | -3.66603 | -44.81798 | 2025-11-16 04:06:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fc965c3-834c-382b-b5a1-6cbe77f02c74 | -2.72296 | -45.04677 | 2025-11-16 04:06:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e4ec63b-5920-3ab2-9845-f7ce8dd20393 | -3.99453 | -44.27158 | 2025-11-16 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17d931ee-d0a5-3429-8401-0a991bd141c7 | -4.6937 | -46.31409 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README28.md)
