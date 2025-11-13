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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bb27b9a-fadf-3e0e-867a-cb785ab68b78 | -4.7206 | -46.4276 | 2025-11-13 04:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e9fa9aac-f8ca-31fd-a120-32e781b86be8 | -3.0916 | -49.2759 | 2025-11-13 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| de63e02a-df78-3215-b34c-fbf467719637 | -4.7204 | -46.4497 | 2025-11-13 04:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 459ea817-13e3-3d8d-bf9a-57a066d76f92 | -4.2056 | -48.5706 | 2025-11-13 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| e44c73d3-0691-376e-9030-0916acec1d39 | -12.6557 | -46.7407 | 2025-11-13 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 8722b0d4-8ccf-354b-ae50-0c05912ec22b | -12.6749 | -46.7378 | 2025-11-13 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 67576c8e-5016-3a2c-b6d6-413f5d291f72 | -4.7206 | -46.4276 | 2025-11-13 04:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 438b652c-02d0-3126-8b5d-d1261c5a9f35 | -3.0916 | -49.2759 | 2025-11-13 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| f4eba065-fcc0-34b8-b2aa-dfb86d55d592 | -4.7204 | -46.4497 | 2025-11-13 04:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 5608b91f-74bc-3087-b520-bf76d5d1b3da | -12.6557 | -46.7407 | 2025-11-13 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 3b5416ab-b28c-3a91-bb59-8d4934e7b6e1 | -4.2056 | -48.5706 | 2025-11-13 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| ff6b9faa-b5b0-3fea-8423-17b805505a0c | -2.82653 | -52.87419 | 2025-11-13 04:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c262a51b-dd8f-3480-ba2c-a3235cc9336a | -5.35782 | -45.40762 | 2025-11-13 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc9cf036-a151-37d6-8f39-83686de460a2 | -5.71783 | -42.76183 | 2025-11-13 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2127c0b9-b73f-3c72-a1d2-07b867eeb741 | -2.15916 | -47.55668 | 2025-11-13 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 582d344c-6636-3ce2-8428-315ce0c65ccd | -6.67378 | -35.1538 | 2025-11-13 04:12:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8ac1312e-5efe-32cd-b81b-ec3ccc2bd41a | -3.78592 | -42.75599 | 2025-11-13 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 95cf4ebb-37c3-3dc1-923b-2a254bcaff05 | -3.44007 | -45.58211 | 2025-11-13 04:12:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efc70a34-cecf-39eb-9eb6-cd13292a9c45 | -5.09004 | -40.23993 | 2025-11-13 04:12:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 779887fd-db37-3f1f-b0a0-bcb9cb9bad8d | -4.94272 | -37.82154 | 2025-11-13 04:12:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b597d4de-71e1-38cf-819b-011f8d5b5476 | -5.40629 | -44.00248 | 2025-11-13 04:12:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d18381cf-84a1-3e4a-a5f2-057761f6aa00 | -4.28592 | -46.06459 | 2025-11-13 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a16c3fc-03c5-3be1-b431-e4cd104fc729 | -3.15496 | -45.81607 | 2025-11-13 04:12:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bbeb5ae-d751-3699-93f9-2b639be0bc82 | -2.87007 | -51.48057 | 2025-11-13 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76e63aa5-9009-395b-a554-128db95de618 | -3.29607 | -52.1119 | 2025-11-13 04:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b31797fc-581f-3333-9004-87aea1f7539f | -3.3526 | -49.83487 | 2025-11-13 04:12:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b35040e-5c73-3912-b422-38ddf981af6f | -2.29101 | -47.87113 | 2025-11-13 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4807a9e-03a9-3dfe-885b-6afd998c2f4a | -4.92873 | -40.1413 | 2025-11-13 04:12:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bf0b494f-b910-3561-b155-c6f12eb95fe1 | -3.26148 | -50.0309 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0625102a-3917-3a57-b153-ecdbdbb50ed3 | -3.66909 | -45.93005 | 2025-11-13 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0fabb72d-c87f-3988-a83a-612d3e0c2af4 | -5.64798 | -41.08226 | 2025-11-13 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 246eeadf-f49e-3d72-b7c7-a6bf23be2723 | -5.06663 | -40.47801 | 2025-11-13 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0120cbf8-f458-36b9-9f43-d4a31a57f879 | -5.60326 | -41.07154 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 493290b6-433e-370c-a028-be1d2a76ad19 | -3.86597 | -49.79323 | 2025-11-13 04:12:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8386e80d-cf24-3763-a62b-1c745f0c5537 | -2.31392 | -48.45432 | 2025-11-13 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06855d5e-3996-37f0-bdb2-c54dd7afb15c | -3.2287 | -45.59034 | 2025-11-13 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 0ac1c25e-9921-39c4-9547-f9441b6e4cf4 | -4.56686 | -48.49701 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1018b83-77b2-3450-9b35-2471aeb93c71 | -4.52106 | -46.42067 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9750a5be-0d1e-340f-bd86-09ed23f94ec8 | -4.54062 | -46.56618 | 2025-11-13 04:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b12404d5-8b01-3c7b-8cb1-bdbfd0a25e18 | -4.26846 | -42.10997 | 2025-11-13 04:12:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e8a4c0d2-4366-3806-9f4f-575b00180efb | -5.18965 | -44.27719 | 2025-11-13 04:12:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f269d7a0-22dd-3df7-aacc-ba266375d61f | -6.08694 | -41.63115 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9eac3533-0e6d-3ee7-b4fc-6177a0c545d2 | -3.34524 | -48.3843 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6292e7ec-e3cc-3db0-9867-2712ecba03e5 | -3.22802 | -45.59456 | 2025-11-13 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b17e8449-00ec-3f63-b72f-4b882dc90c7c | -3.86514 | -49.79826 | 2025-11-13 04:12:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 23cc6d6f-424a-3018-97a5-c101796d13dc | -3.5321 | -44.84793 | 2025-11-13 04:12:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef73b774-a16b-3c1f-b3e1-5949bc729bf8 | -2.45467 | -49.26291 | 2025-11-13 04:12:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e0b628e2-e7bc-3caf-81f8-7a23fc2f964a | -3.40524 | -46.9037 | 2025-11-13 04:12:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a46d92c-2a1d-3331-93c3-6443139bb60b | -3.40082 | -50.17701 | 2025-11-13 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 457aca98-498e-3a96-9209-393a1ba5cc57 | -4.20453 | -50.09639 | 2025-11-13 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cb80b75-758e-3632-a952-1e13c99a3dc2 | -5.84904 | -40.23095 | 2025-11-13 04:12:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4bf1a2f7-5630-3f8d-9779-eee52ac040ee | -3.09323 | -49.27956 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 616ccd66-037c-357b-963d-f509fcf4b5b8 | -3.40306 | -50.1792 | 2025-11-13 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3a68119-749c-3e0f-964b-89584ca21937 | -5.26634 | -42.99326 | 2025-11-13 04:12:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67abfb28-78e9-3cae-9aac-7f9b14515b5a | -5.84339 | -38.35385 | 2025-11-13 04:12:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 80e06c9b-d377-3d67-a8f2-22f771f92bb7 | -4.70618 | -48.12233 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42779a8f-35bf-3668-8bf9-87231db26590 | -4.30985 | -48.24066 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3e96a224-bc18-3f69-b234-28feff2122a5 | -4.28537 | -46.06298 | 2025-11-13 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6387fef-2933-3c85-be8e-fb247f1d9f79 | -4.89487 | -48.96891 | 2025-11-13 04:12:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb8e234f-22df-3a1d-80c7-b905eb8965d4 | -4.93135 | -44.29213 | 2025-11-13 04:12:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59a83e57-fd12-309b-b279-598af8e0d024 | -5.31125 | -40.92293 | 2025-11-13 04:12:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 781fd22b-fcd5-3ab6-a40b-4a961cd40360 | -4.71879 | -46.44801 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2fcf2139-998a-3202-86f8-732eefaab266 | -5.64626 | -41.07081 | 2025-11-13 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ba803031-6330-328f-befa-4f0e9eaca515 | -3.05821 | -40.81232 | 2025-11-13 04:12:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9b6111d2-cd96-344e-afa0-3cdbba59e395 | -3.37041 | -48.4053 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3df7d882-086f-3e8b-a1d0-33b9c7142c3d | -3.36975 | -48.40929 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c40b4f80-2f53-3f34-89bd-1cfca5b37952 | -3.78646 | -42.75254 | 2025-11-13 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7c08b854-fa76-37f1-9311-ffd4a9a69b01 | -3.67323 | -45.69464 | 2025-11-13 04:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48b04ce3-1777-3ddc-bc51-1913b7ec9074 | -5.74633 | -42.73098 | 2025-11-13 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f3859a46-a3c1-30ea-805c-86511027b3fd | -4.04061 | -42.26136 | 2025-11-13 04:12:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18c44988-ba99-345b-a657-2f007dad1252 | -3.23354 | -42.13387 | 2025-11-13 04:12:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 944e68db-eec6-3d17-807c-ec9181b76d0d | -4.0137 | -48.8046 | 2025-11-13 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5d20232f-8cc0-37c6-b74e-4f4c6e378429 | -6.10557 | -41.53189 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bbb70754-b776-362f-9600-b292d6a4d5b7 | -2.63366 | -52.08538 | 2025-11-13 04:12:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5b16c84-3505-3687-a183-a05d5734f86a | -3.23166 | -45.59513 | 2025-11-13 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8db59827-b43d-3e03-b2ee-c32bdb5575c4 | -3.4017 | -50.17158 | 2025-11-13 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d05f7cc4-7a0f-3d5d-b634-230ce079429a | -4.71188 | -46.39605 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 620c3919-48d9-3c5d-827b-89438bc9dcb8 | -4.53392 | -46.43635 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb1e8ed6-9f35-3836-a3dd-8c07b7045c3c | -5.44232 | -44.65438 | 2025-11-13 04:12:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 211bf406-cfba-38fa-8b03-1cf560f3a5cb | -6.08748 | -41.62762 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c7d29cda-ec53-3d19-a1c6-2bd31e5ea860 | -5.61117 | -41.06529 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a4e7cf56-bd1d-3da1-b553-5096bc780e8b | -5.64682 | -41.06716 | 2025-11-13 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 32318559-9d28-399a-a1c0-db40960e1bb8 | -2.45548 | -49.25806 | 2025-11-13 04:12:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d88b0875-7cd6-3b21-b5af-4027f9c0128c | -4.25757 | -44.59574 | 2025-11-13 04:12:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a14af869-37d9-3c0c-9ca4-baeb22c89553 | -3.31105 | -49.46692 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0840c85c-4042-3401-be77-339870c6a8ed | -4.30919 | -48.24468 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a4939f4e-3d92-35a2-94eb-cf17608d00c9 | -4.0086 | -48.80816 | 2025-11-13 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ea3d8c3-d84f-3cbb-b8f4-33f3e9f4c53e | -5.61858 | -41.0702 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3d38d4d9-d259-3d36-b77e-93c45b650b35 | -4.93416 | -44.29626 | 2025-11-13 04:12:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02e53707-dd99-3d76-816b-c7758a6c4840 | -3.36425 | -48.40427 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34fca15b-2d32-362f-9e2a-c4c8c6fa15e1 | -3.48112 | -45.86357 | 2025-11-13 04:12:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd7e5b38-4a86-372b-af76-5dde9b1b766c | -1.14274 | -45.71815 | 2025-11-13 04:12:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87d95d3e-bad7-3b93-b273-816727a33a08 | -3.39434 | -41.14784 | 2025-11-13 04:12:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba7cd6f9-8512-3249-85bc-95f0be296bd7 | -5.74855 | -42.73839 | 2025-11-13 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 87344f26-9f77-3720-84fe-b17cc4a3d0cd | -4.69188 | -48.63719 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 048fddb3-bf91-3774-979f-3d1d6ac472dd | -2.73172 | -45.48318 | 2025-11-13 04:12:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b9e86e0-fd79-3c87-93c7-47427733f9c8 | -4.25319 | -43.78447 | 2025-11-13 04:12:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdd4cc59-e804-3553-a180-41e9502b72c9 | -5.89444 | -42.26238 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a5a4403c-e001-3567-b8d7-06c6533d25b6 | -4.7113 | -46.44684 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 945f59ea-8c15-3d52-a05f-1723e7bc9e73 | -4.62801 | -42.79002 | 2025-11-13 04:12:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
