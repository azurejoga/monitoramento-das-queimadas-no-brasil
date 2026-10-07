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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ed999e5-ba1d-3bdb-ac1d-ba95038c27f5 | -7.40506 | -45.63199 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e2dca487-53ff-33c8-b85f-9428fa8e81ce | -8.00723 | -47.17104 | 2026-10-07 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 048f1de8-f024-38c2-ab66-690d3d044b89 | -5.68178 | -49.21505 | 2026-10-07 16:03:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 472f4564-c4f6-38c9-89e6-e6ca17e1c6a6 | -5.64375 | -42.78779 | 2026-10-07 16:03:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 102409e3-4319-3c0e-acfd-7f5d751029bc | -5.94937 | -43.03676 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 82c0a7ab-cc7b-38f6-93fd-9743aa40eb94 | -3.17886 | -49.4512 | 2026-10-07 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b5bd68dd-fc8b-3232-b3c9-89ba0f7242fe | -5.97034 | -40.92393 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 9b57d0c7-5aa2-33ac-84cc-1c190a933119 | -5.72604 | -41.74024 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 02bd5bd5-6a53-37aa-974b-c0680d622b2e | -3.18811 | -50.54818 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 001a5c7d-76db-3f5b-bc76-d8b9d371f188 | -5.81513 | -43.85267 | 2026-10-07 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4320776e-e25a-3e2a-8159-dccd653e1faa | -6.9797 | -43.22337 | 2026-10-07 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a163af20-64bc-3cf9-a4c0-64a00ed93e46 | -6.86953 | -39.09738 | 2026-10-07 16:03:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 22.8 |
| b91db8d9-549e-36c4-929c-ff1c04a1d51f | -7.20188 | -44.29779 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b40123d4-9b64-3dc5-9819-5d46e723be4f | -5.97313 | -40.94381 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 5a16609c-e539-3f3d-ae35-3da425787212 | -5.73469 | -41.74787 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 7f5bbe25-3e24-38e3-876c-f13705f6f18f | -6.68356 | -44.96693 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0a946e0e-3718-31a8-9604-96f1637df502 | -4.96604 | -40.56725 | 2026-10-07 16:03:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| de943fa8-74c9-3e96-9179-e2cc5cb42ab3 | -3.88842 | -44.10447 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 20bd1024-0c89-35a3-b37a-765146a2d051 | -3.89616 | -44.09943 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0cdb23d5-1efa-350f-9465-85cdabb285bb | -6.61723 | -44.20301 | 2026-10-07 16:03:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9bf8298c-753e-3d60-8186-0656b0685f54 | -3.87736 | -42.21093 | 2026-10-07 16:03:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 75e75764-ef1e-310f-8b02-518ec1abf913 | -5.8973 | -44.03467 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 978f2824-9026-374b-9c9a-675e62033802 | -3.50546 | -41.95688 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 8f4e0077-b3c7-3f5f-a978-b90c225ec814 | -3.76672 | -44.65673 | 2026-10-07 16:03:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 880fe228-0979-3958-8e51-268b9facbd1b | -5.72802 | -45.16692 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 9dd1a5a0-6703-3e50-a7dc-9143525fc215 | -3.51769 | -44.98308 | 2026-10-07 16:03:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e7407c6c-b73a-3789-999a-8c88f8440d73 | -8.11038 | -50.92586 | 2026-10-07 16:03:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 541df7e7-13df-3271-ab9d-295f938d53a8 | -5.98386 | -40.9423 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| b2c8dcdb-6432-38b3-80e4-fcfe24ff97ba | -4.23576 | -49.98636 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 7ebb44d9-a804-3159-9879-809dd7e64242 | -5.95285 | -43.03278 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 00d8897c-3466-3564-add9-f1986095ded3 | -3.92623 | -40.38833 | 2026-10-07 16:03:00 | NOAA-21 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| c80361a2-67af-3bf0-b319-cc4d483fb13a | -5.49168 | -42.84608 | 2026-10-07 16:03:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 296.4 |
| 2c2fe93f-44dd-35a5-b571-6c046da4cded | -2.42418 | -49.75748 | 2026-10-07 16:03:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 63032861-c095-3329-9c10-f5c518283a63 | -3.05626 | -44.44548 | 2026-10-07 16:03:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 1d77288b-982c-3944-b914-f93a73e2dd96 | -5.22968 | -50.9 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4012c437-d230-3ae1-9f9b-d9269015e8bf | -5.26203 | -47.92889 | 2026-10-07 16:03:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 70681671-1304-30c7-861c-4821fe5c858a | -3.18545 | -50.5497 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| e0901367-f2b9-38bc-b59e-e6345e9262d1 | -7.2962 | -47.2887 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 51b1c105-ca3d-3cf1-a63a-9d3dbabf54f6 | -6.58876 | -44.19009 | 2026-10-07 16:03:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6793c673-c61e-3063-b665-7d6575fd704d | -3.86693 | -40.22593 | 2026-10-07 16:03:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 06554522-83cb-3b45-b537-0d13e241cae1 | -5.76853 | -38.55672 | 2026-10-07 16:03:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 135.2 |
| 3d738ee7-732f-3a67-9ba3-d201eac403ba | -4.88713 | -38.90737 | 2026-10-07 16:03:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 83724651-ed9d-3f16-b834-de09b3ed4286 | -6.99487 | -43.9771 | 2026-10-07 16:03:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f31ec50b-d85d-3dd6-ab18-71748592891a | -3.86372 | -44.13882 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 62ce5532-4b60-33b4-812d-733954a94467 | -5.24921 | -50.91121 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 4f336cef-95b7-303c-a3da-3f58e3c5fac0 | -2.97451 | -41.41742 | 2026-10-07 16:03:00 | NOAA-21 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 1abfb397-d03f-30ac-9a4b-5558674f7c5b | -6.63878 | -43.77906 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e378f44e-5821-3f78-bf62-ef8a285c9587 | -7.81815 | -45.49878 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| c9d634c2-78de-374b-b6ef-e0e3ce5b6c36 | -3.68378 | -38.81681 | 2026-10-07 16:03:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a4be096e-e407-36dc-aab7-2ba9158fa1db | 3.52345 | -51.4636 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b232c439-8c11-399b-ab16-532c1341013a | 3.51382 | -51.26199 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1c40d9a6-b5ba-3f3e-8064-bb0b08149e19 | 2.45327 | -50.82324 | 2026-10-07 16:05:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5bfa3786-e18a-31b2-a5ba-7b41336abb98 | 0.71926 | -51.36708 | 2026-10-07 16:05:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1acca851-6b31-33f0-a8b2-3ae49b180566 | 3.21178 | -51.30209 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ec47ebf8-88b5-3b98-851b-ae21c4da1995 | 3.22547 | -51.29478 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cfae9d9b-0fc8-3a86-9b31-6ef9880c938b | 0.72944 | -51.38427 | 2026-10-07 16:05:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4961ae93-5270-3ef6-93f4-1cb36395b72b | 3.5356 | -51.27916 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 5d8f00c5-5972-384f-9322-ea49b3c791c0 | 1.09197 | -50.73341 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cd5891cf-6acd-3e7a-a98a-5a5d7fffbe4a | 2.1174 | -50.83135 | 2026-10-07 16:05:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.1 |
| dd509d7f-0287-3501-bdc3-237f5225cf7d | 2.12125 | -50.82728 | 2026-10-07 16:05:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 8734e23c-1c88-3f8c-b494-0d6cb1426b34 | 3.52884 | -51.28269 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 122781ae-f83e-3d09-bf48-c4384d1f5bd1 | 3.21389 | -51.32576 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 48276920-7dfc-367c-9bf6-99558a9120f8 | 3.21791 | -51.29107 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 47e9a2f3-9f64-3988-8d7d-576285b9379d | 2.18075 | -50.96793 | 2026-10-07 16:05:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7dbd3245-b8bf-37eb-b00f-f7a1552c3e1e | 2.17473 | -50.96698 | 2026-10-07 16:05:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 09da9b9d-693c-3308-b493-07bfa7d1a942 | 3.22773 | -51.30668 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a9b8990c-2e53-3f9a-98c4-48246df0c7da | 1.46625 | -50.75016 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0dd9fb64-09fe-349f-8517-06979509c60a | 3.211 | -51.3066 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 421d48eb-3140-3a85-8670-108e54fc878b | 3.21564 | -51.30476 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 7d4f60fc-be09-3d66-a2bb-2905b4678a46 | -0.77759 | -49.2654 | 2026-10-07 16:05:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d82aad16-53e9-3b25-8739-6718ce7d5ae9 | 3.22019 | -51.31478 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 61.6 |
| b403cd59-3d80-37b0-a70a-d50001d0f04e | 3.22389 | -51.3039 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d744c048-3e5e-3433-b0c6-5a998fe04954 | 1.47298 | -50.74654 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9a375a77-5e85-3f73-924e-5c09af15eb89 | 2.07552 | -50.91977 | 2026-10-07 16:05:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7601fd7c-4e3e-33ba-a27f-945fadc016ac | -1.10472 | -49.92176 | 2026-10-07 16:05:00 | NOAA-21 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| fac01290-1ef9-3f44-8ac9-c82e7b9991ba | 1.47694 | -50.77481 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 24.9 |
| a65f1917-f6a9-3d46-a00c-3e50874bbe2f | 1.19942 | -50.71702 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e378b13d-81b0-3daa-b07a-2423efef6776 | 1.47612 | -50.7653 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 395e0ac2-8b64-38d2-80c5-c4aca171028e | -1.41874 | -52.84784 | 2026-10-07 16:05:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 17afa38c-6231-349f-8e9b-3b30571d806b | 1.20179 | -50.71774 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 64e597e8-0d7c-3e10-b546-d6227cb42bee | 3.36834 | -51.34035 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5dd1c877-3363-3ebb-a267-48dbbda1631e | 3.39865 | -51.30795 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d821de74-7915-3480-b67c-9dccdaf17e25 | 0.95799 | -50.2032 | 2026-10-07 16:05:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a9d84af-4c6e-3c61-af42-69a94e55aba4 | 3.52433 | -51.27281 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 312991f9-55cd-3e64-a691-89b714124833 | 1.34918 | -50.84955 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7019a1d4-1dcd-35bd-a3ab-48bee785235a | 3.22244 | -51.30114 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 3cb9a826-a77f-36c9-bf77-bbcb04cfbb68 | 2.12054 | -50.83167 | 2026-10-07 16:05:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 671aead6-93dd-3ef7-9c30-bf2154345bbb | 0.80367 | -51.22622 | 2026-10-07 16:05:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c36ed53b-5717-353e-a863-7e39089d431a | 1.46553 | -50.75461 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d6a9ede3-332b-3e4a-846a-9e176c826473 | 1.34846 | -50.85409 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 68f36f4b-e167-3969-91f5-3fa7d39c7a6d | 3.21705 | -51.30753 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f88a37fc-09b5-31e8-b890-cd7427d63055 | -1.10337 | -52.26051 | 2026-10-07 16:05:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 192fa3ea-22f1-322b-bb3e-d706577b9d97 | 0.95858 | -50.20303 | 2026-10-07 16:05:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f3561f1-545c-311c-a5ab-419945240785 | 1.4754 | -50.76974 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 1f4341d1-f4e7-3f00-bff2-c9fee79b1cac | 2.32746 | -50.8768 | 2026-10-07 16:05:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 881c047d-90dc-3fa5-846d-44c2d69863ed | 1.33488 | -50.8614 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 748ef9a4-cba1-3ba7-92f0-a4823f9a310f | -0.77817 | -49.26921 | 2026-10-07 16:05:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 358487f1-b5fc-3a0b-9466-d58686a24503 | 3.47166 | -51.47431 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a9b3be18-8bf7-3305-a09f-e644164f25ca | 4.02282 | -51.60723 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| efccd3ca-3d65-3f92-a881-7ae0ee1a6413 | 4.02389 | -51.60736 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README174.md)
