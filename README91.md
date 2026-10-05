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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a2a24f2-6100-32d4-93ae-be6618adc1ed | -5.52117 | -41.01233 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| 2260fc0b-891c-3cc4-afb3-87333656e0cd | -3.03735 | -57.41935 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bfc0d9f9-6408-3949-a87c-30874a556343 | -3.68393 | -54.53638 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a7ce5159-425f-3708-9759-7ac596e92115 | -3.77506 | -39.84838 | 2026-10-05 16:39:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 6a0d491a-79c9-3473-9072-e936153c5a91 | -2.31252 | -50.98492 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c0b848c5-a421-3ec5-a9e5-cfc924274bb7 | -3.64788 | -58.62343 | 2026-10-05 16:39:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 95444b56-69d1-3399-af4d-746f63060b27 | -3.07594 | -54.17989 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 84a9c12f-b189-350f-a0f8-24f561559bfd | -4.30891 | -46.55928 | 2026-10-05 16:39:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45d5f95c-d828-3b43-be53-75f94e753852 | -3.68702 | -42.95674 | 2026-10-05 16:39:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0f1f0db6-cd1a-3c08-b57e-ccb270111b75 | -3.87711 | -41.02676 | 2026-10-05 16:39:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| bc089ce6-1169-3a32-8e4d-11724fbb035d | -3.74582 | -39.53956 | 2026-10-05 16:39:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bde73e69-b424-3d87-8191-835a57237d3d | -2.97377 | -58.45255 | 2026-10-05 16:39:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7de5101c-f300-3a9b-a0f6-776c5c2b90af | -3.0453 | -57.52173 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0949ad1a-f308-38cd-9086-ab2c4da9f087 | -4.85812 | -39.58957 | 2026-10-05 16:39:00 | NOAA-21 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 34aec84b-ec29-3071-98a3-f98829516662 | -2.99882 | -57.79056 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f7d29b2a-b3a6-390b-8e56-eb21108bfae4 | -4.17795 | -44.30607 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 89f9aeff-c3b4-32d4-b8d1-6b1e18aab237 | -6.32491 | -43.8143 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9e2b5713-a4fc-355e-8333-a422f992a8a6 | -2.93545 | -54.11047 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b9ac4ce6-a770-35c6-8bdb-eee8d444b41f | -6.34765 | -44.09486 | 2026-10-05 16:39:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 771ba0ed-6248-323b-bda0-78e1ec5e0444 | -4.91246 | -41.74125 | 2026-10-05 16:39:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 423d3a45-46d9-3ec1-b338-e273f1dd5d2a | -5.13476 | -60.3203 | 2026-10-05 16:39:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| dda6faf0-d4e6-32f6-a4f6-dc0b870f11da | -3.5042 | -59.55547 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 65011c35-93e0-3f49-a78d-6715f7eaa00f | -5.89438 | -43.30393 | 2026-10-05 16:39:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 9242dc6a-754a-3539-98fb-de7deeac6669 | -5.82641 | -53.86152 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 43b6568c-0d5e-3dcb-b1ce-62f448c48db3 | -2.90492 | -42.35128 | 2026-10-05 16:39:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3393111b-e561-3f33-9fd0-d7d471d2fe82 | -5.40266 | -39.10669 | 2026-10-05 16:39:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 4a090a78-033a-3a7e-bea0-b694db0852c7 | -2.90757 | -42.35131 | 2026-10-05 16:39:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 936ca5eb-fba1-3e6a-9292-0c6f6cc3658e | -5.83476 | -45.00923 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a7477d60-7a35-38b7-a4ea-5011d0c1f43e | -1.32963 | -46.82629 | 2026-10-05 16:39:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 33df4655-7033-375f-bf58-ca37b2cf25c8 | -3.27667 | -43.07852 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 35b3f45c-6a12-3441-9834-a45b81ef108c | -5.48641 | -39.55944 | 2026-10-05 16:39:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 45.6 |
| 80ff3b85-d97d-384d-ad8d-cbac73f8d4e4 | -3.17116 | -41.4071 | 2026-10-05 16:39:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 88432b84-4559-3635-9668-fe82907a4ad4 | -5.83602 | -45.01711 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| aee15d2d-2c49-3517-8409-6be89e131041 | -6.17927 | -55.35829 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 7893eed0-15aa-3a1c-9a15-fb5a8115fb39 | -3.47615 | -54.68213 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 8f667921-4412-39ee-b118-b9a9098506ba | -3.92081 | -44.14917 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5e90afcc-4fc3-343b-ac05-bbbe48acfa43 | -4.1854 | -44.3049 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2e240f20-61d7-39c0-83fa-3fb36d81b791 | -5.8513 | -53.81961 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 604ced71-62df-34fa-9962-ffde91255b14 | -4.50583 | -45.99282 | 2026-10-05 16:39:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| da471266-4448-3d0f-823c-882e393610b1 | -1.80758 | -53.75708 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4d522401-8599-3f88-bb90-affbaa4c3934 | -5.44368 | -42.64074 | 2026-10-05 16:39:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 3dd12ac7-29dd-335c-9c85-8da4574011fa | -2.06988 | -48.21192 | 2026-10-05 16:39:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 72c0989d-525d-3d4c-9f2c-a307accae7d3 | -5.71107 | -40.1214 | 2026-10-05 16:39:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| f4bdf510-c8ef-3599-970f-2d3b4083f431 | -6.08086 | -47.65492 | 2026-10-05 16:39:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dd8012c-2a18-351c-8025-4b0aeb868353 | -3.21447 | -57.87894 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 9cdd388c-88a6-391b-affe-d4a1878b893e | -1.4792 | -54.52793 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 3d0aaeb0-998e-3d97-9a03-9e0b748e35bc | -3.17144 | -60.06293 | 2026-10-05 16:39:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 36b11fec-43bb-3797-ad95-c5288881be0d | -1.46069 | -55.26522 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 11fb6986-213c-3f56-8a9d-fc1cf78c0454 | -1.97676 | -56.05299 | 2026-10-05 16:39:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8dfac2f9-f905-39fe-89c2-183e012e44e6 | -6.05714 | -45.13617 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 257ec825-8662-384f-a091-87fe4b53d5d6 | -3.11648 | -44.28875 | 2026-10-05 16:39:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2a69c023-c9c5-3027-b60b-821be8b14513 | -5.38693 | -38.27874 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| b18d8abc-cae9-30a1-91da-fb22aa620cce | -3.21377 | -42.76655 | 2026-10-05 16:39:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ea1cecf2-815b-3901-be3b-0c6d25220dfc | -5.40782 | -39.10583 | 2026-10-05 16:39:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 13b1f01f-df80-319b-b9a0-9534c105b6b1 | -5.74074 | -45.05628 | 2026-10-05 16:39:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c44e0c50-3ac3-35f4-b24a-706f603081b0 | -2.98218 | -54.04468 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dcbdda0e-42e4-38e1-8c50-2837da94ca59 | -5.38786 | -38.27766 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 14190a29-e132-3f2d-bf3f-671101ffb4e2 | -4.79779 | -43.23246 | 2026-10-05 16:39:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4e9157e0-96bc-3a7c-92f6-6609de372692 | -2.9236 | -53.94615 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7dc448e5-a9fe-37fe-a7d4-52b7a481c2d8 | -4.32711 | -43.82045 | 2026-10-05 16:39:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 450d94d8-26f5-3a43-a27d-0f40a5453493 | -3.13487 | -53.71534 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 6dee893a-d4b5-3ea9-86e2-35f6bfa45957 | -3.21568 | -42.87326 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 1712e964-8566-3cdf-a170-e749e663eaa0 | -6.05654 | -45.13227 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 279375ab-ae5a-39c6-8cb3-6d0b15591ddf | -5.98884 | -43.70513 | 2026-10-05 16:39:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1af6ea63-c4f9-3854-8ad6-f16eaaa5c29d | -0.38188 | -52.07616 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5d08fcff-9aaa-3609-bd39-ac70c8264ea2 | -2.68035 | -57.15747 | 2026-10-05 16:39:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5cc45900-a410-3138-a743-815146d7afc6 | -4.37339 | -43.92076 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6b1000d0-7abd-307d-9768-9947f88d4832 | -4.80535 | -42.14654 | 2026-10-05 16:39:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 19091123-f0cb-3325-abd8-e76f13dcbcbb | -5.4032 | -39.10979 | 2026-10-05 16:39:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 27.2 |
| fe9500b7-d877-3256-8e6b-ed1def58a4f2 | -4.11993 | -54.90152 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a43c4048-13e3-3b47-8618-17354b61fa81 | -2.82687 | -43.68671 | 2026-10-05 16:39:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 45131f13-e330-31d8-9390-35f7c6adfd44 | -4.4447 | -54.97292 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 0e4ba31d-86d6-3261-8844-dc45839e88ba | -3.8889 | -39.19247 | 2026-10-05 16:39:00 | NOAA-21 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 5d32d72d-e55d-3455-88e1-3e52e2662b59 | -1.51888 | -50.53275 | 2026-10-05 16:39:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6040bb5-8f2b-30b2-9d2f-90d1d8ce1e1e | -2.97955 | -43.88829 | 2026-10-05 16:39:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 87fb8843-f0eb-3465-b15c-f1db00391583 | -0.38782 | -52.08067 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ac498c19-a849-3e3e-b673-c968f93b11a6 | -3.0818 | -58.08844 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c8fa8eb2-9768-35b9-b40b-9890e4e9aac4 | -3.11153 | -40.15962 | 2026-10-05 16:39:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| edfc8508-8972-3a1e-bf21-e9f5cf5c2e95 | -2.23654 | -48.70298 | 2026-10-05 16:39:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2492d00b-4cb1-3844-9199-4c3e54ca9735 | -3.87027 | -40.20266 | 2026-10-05 16:39:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e64e99b9-7f6e-3a9c-ad60-cfdd2012143c | -1.80703 | -53.7535 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ff8e38de-7f8c-3e50-a162-523c59bc1df5 | -1.95103 | -54.04227 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e1dd6cb0-497d-3f70-a360-d5b55f78e14c | -5.99612 | -53.63305 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| f53e460e-2b8b-31f7-9d0c-cc08a9d9848f | -3.97002 | -38.51392 | 2026-10-05 16:39:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8a0073d2-a08e-316f-8181-dd601b8816c9 | -3.3068 | -43.94771 | 2026-10-05 16:39:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5f32194f-07dc-3c96-aa52-b01e2893f881 | -3.21347 | -56.83251 | 2026-10-05 16:39:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d448bc97-115d-3649-b45e-d9bc61e3b059 | -3.32431 | -59.48032 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 74457407-08ad-333b-821b-e052b0e13a2a | -4.49447 | -43.0472 | 2026-10-05 16:39:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 87079bb2-548c-3cea-83c8-6b9eeb1c0e51 | -1.63082 | -56.00868 | 2026-10-05 16:39:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| eeaaadfc-b891-3872-ba83-9413038c6a8d | -7.21319 | -55.20188 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e8cdce45-4eee-3336-a4c7-3c6ff78c6885 | -2.82543 | -54.12639 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| fe86fc27-2dc0-3fad-a1b8-93bfe6371011 | -7.23037 | -55.18307 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 56040a49-d287-38ba-959b-6960c2ae3532 | -3.21393 | -57.87534 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8f0cd5d5-9cf5-34d1-85e4-7a40c6cd7189 | -5.43962 | -42.64136 | 2026-10-05 16:39:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 3c39a919-b0c1-3581-826d-1013b3649b2a | -1.69998 | -55.05833 | 2026-10-05 16:39:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97ae27ac-f330-35bf-8fe0-0adeb21f2a7c | -5.11783 | -42.63881 | 2026-10-05 16:39:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8119b2c4-d363-3578-861c-eba0bf4acce7 | -6.45971 | -55.48002 | 2026-10-05 16:39:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 911fb702-007d-367a-9159-5268d757cba0 | -1.63267 | -55.53503 | 2026-10-05 16:39:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 85882629-cb62-3f17-8f84-20ad61527246 | -4.00053 | -38.35513 | 2026-10-05 16:39:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| fe5ae7da-2646-3646-8e35-c5330a7bb434 | -4.4624 | -54.96563 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |


[Clique aqui para ver as próximas entradas](README92.md)
