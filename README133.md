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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82948e53-8e27-38a5-935c-31d5652dc546 | -6.3772 | -44.7868 | 2024-11-10 14:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| ce6dbfee-322c-37de-b1f1-a9000bea4198 | -3.2533 | -42.5288 | 2024-11-10 14:20:00 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 6b390802-9a69-3193-b6d8-092695a3b016 | -2.931 | -52.7753 | 2024-11-10 14:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 24c1f518-a211-3538-9458-c6c29ac496e4 | -2.2803 | -48.744 | 2024-11-10 14:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 610c9f35-7fa2-367f-a550-5983829e8ee2 | -5.4501 | -41.6575 | 2024-11-10 14:20:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 94d591f2-b576-31d3-bb4f-68f2fabf5bf4 | -4.3979 | -41.8987 | 2024-11-10 14:20:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 126.1 |
| e0e01ad4-7a28-33ec-9ada-d4abb46b841f | -2.1952 | -46.397 | 2024-11-10 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 8c65120d-e3fe-323c-95c0-e9a63376e799 | -3.6888 | -44.7295 | 2024-11-10 14:20:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 9562144a-da3b-3fed-aa13-b27bdffee6b6 | -5.865 | -41.5036 | 2024-11-10 14:20:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 700ae705-eea4-30ef-b42d-9b878035853a | -5.4544 | -43.2893 | 2024-11-10 14:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 7d052c6f-a817-32d5-95a2-9c563ed27b13 | -23.9089 | -54.083 | 2024-11-10 14:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| 4632e0d7-e5b4-346c-bd64-d3a4a2800c6a | -3.2243 | -53.0727 | 2024-11-10 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a31acd62-027d-3ffb-a2ed-b98a65e44e66 | -2.4365 | -46.3019 | 2024-11-10 14:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 0daea554-72f5-33da-b8db-87ed2580eb44 | -2.418 | -46.3024 | 2024-11-10 14:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 95a21c14-d018-3737-bc69-d39797687b2a | -2.4365 | -46.3241 | 2024-11-10 14:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 6a19fdec-9150-3743-bbf8-fad37edad2d9 | -5.9289 | -42.6661 | 2024-11-10 14:20:00 | GOES-16 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 36a46f78-2203-3ef1-b274-0f5cce12a3d9 | -5.7287 | -41.9942 | 2024-11-10 14:20:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 6c3ae15f-feb4-36cb-b5bc-421b565f2c78 | -2.931 | -52.7549 | 2024-11-10 14:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 5c6db004-c506-3ccc-b4a9-d30f0d24a7bb | -5.4927 | -43.1931 | 2024-11-10 14:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| f94aae1c-2913-375f-ac6c-fd9792f87d85 | -1.4009 | -55.4518 | 2024-11-10 14:20:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5761afbc-c744-3da4-bc22-61fe7a5cf8d1 | -6.2564 | -45.6795 | 2024-11-10 14:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 7521c54a-e103-3374-9113-6a1172acb5ee | -2.5119 | -45.9888 | 2024-11-10 14:20:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| efc8b41e-e239-3418-bbf5-fed093c11292 | -3.2521 | -46.4739 | 2024-11-10 14:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 24a0ac76-0892-3cbf-9c2b-c08b965f0d48 | -1.9192 | -52.9187 | 2024-11-10 14:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 4ea17d0e-c132-3411-9952-a84deccc624b | -5.7475 | -41.9927 | 2024-11-10 14:20:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 02a1142b-ea99-394c-8223-24efa9e67fb3 | -2.0769 | -48.8129 | 2024-11-10 14:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 34e2e385-f808-3d45-9de4-5bd9395b0279 | -0.3768 | -51.9331 | 2024-11-10 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 6fa60221-a1bb-3ae4-bcfa-a35ffeb8bcfd | -17.293 | -57.5062 | 2024-11-10 14:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 729a0bf2-9e09-3f17-bfb6-3aae16a1839b | -2.1021 | -46.532 | 2024-11-10 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 15e54786-6323-3f74-830a-937f582910bc | -3.8194 | -44.6778 | 2024-11-10 14:20:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| dbc340d0-d11b-3748-b4e3-19ea0cc0b496 | -6.3689 | -45.6483 | 2024-11-10 14:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| afe3300d-2e5b-3c98-843a-648ad6078107 | -2.2619 | -48.7231 | 2024-11-10 14:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 72d2499b-b93b-32db-a4cd-9c86190ca08e | -6.1366 | -42.5544 | 2024-11-10 14:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| cd9e2554-f8d4-30b9-8ed3-7cfd73d54755 | -0.3401 | -51.9127 | 2024-11-10 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8f1c3d13-a893-31e2-8dca-e210d440b5d2 | -5.7661 | -42.0151 | 2024-11-10 14:20:00 | GOES-16 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 66063ccc-9f6d-3eb4-9fb6-d5f0d2044516 | -3.6701 | -44.7303 | 2024-11-10 14:20:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 7110dacc-34ff-340e-a711-0a19efeea1fc | -3.9483 | -48.1724 | 2024-11-10 14:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 35fdae0c-e205-323d-86ba-3021439fd48d | -2.0656 | -46.3339 | 2024-11-10 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 343a3224-f758-382f-bc13-60595ba0c3db | -1.1672 | -52.0918 | 2024-11-10 14:20:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 107.4 |
| d43d0baf-9d6d-3038-bf4c-e73068144d33 | -5.4689 | -41.656 | 2024-11-10 14:20:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 30554233-fae8-31f0-820d-0533da30c1de | -4.0915 | -49.111 | 2024-11-10 14:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| b0d25787-1660-3218-a5e2-2b01309371a8 | -3.7853 | -47.4629 | 2024-11-10 14:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| acbfa330-c040-3456-950c-32720ed89f9f | -1.9726 | -46.4467 | 2024-11-10 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| f08874c1-cabd-3f18-af4f-eb571ec02cf5 | -2.3076 | -46.0614 | 2024-11-10 14:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 58f63724-9e94-30a3-8566-915a8e10810f | -5.7789 | -42.6546 | 2024-11-10 14:20:00 | GOES-16 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 96ec1f7e-3f07-31ce-b38f-47f4569a2515 | -2.2619 | -48.7445 | 2024-11-10 14:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 7045340c-aaeb-3256-b317-8f522340e34f | -2.1931 | -53.6428 | 2024-11-10 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 55a535f5-d2a8-392b-820a-77a789954f54 | -2.0841 | -46.3556 | 2024-11-10 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 4bf4a06c-6323-3889-a20e-5584b646534f | -5.2485 | -48.0641 | 2024-11-10 14:20:00 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| ac13c059-9c59-33c5-aabc-296539a99abb | -4.1565 | -44.4099 | 2024-11-10 14:20:00 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 8c1f374e-fb84-363c-8ed4-d6cf97ab1ca2 | -8.7562 | -44.0965 | 2024-11-10 14:20:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 04aa7e23-7a70-310e-aaa0-8e2893567e1f | -1.5163 | -52.2106 | 2024-11-10 14:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2c3f369b-b564-3305-a124-f47bfd4e4e37 | -2.3075 | -46.0836 | 2024-11-10 14:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| f9800c33-d5b4-3d40-abd5-c8068884fed3 | -2.4191 | -45.9915 | 2024-11-10 14:20:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a9d11974-5309-3d66-be1b-d58d06a97bbc | -16.679 | -55.5402 | 2024-11-10 14:20:00 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| fc803e5f-c94a-34a1-b56d-b017ebe577c9 | -2.326 | -46.0831 | 2024-11-10 14:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 71392498-9b32-3cea-a006-9af8c56e68fd | -4.4167 | -41.8975 | 2024-11-10 14:20:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 4a8972fd-152b-37e3-905d-c7c5837ea811 | -1.718 | -52.4736 | 2024-11-10 14:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| dd03324e-b23c-3ebb-9cf4-8f1ac5c8c1f4 | -2.2804 | -48.7226 | 2024-11-10 14:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 5a89ffe7-a19e-3257-8d97-1920be0360f3 | -3.9486 | -48.1291 | 2024-11-10 14:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 6b0f7a88-bf6d-3793-abd6-b7088629ffbf | -2.3261 | -46.0609 | 2024-11-10 14:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 8e14618a-f44b-3e6a-b97e-54ede3654354 | -6.1361 | -42.6017 | 2024-11-10 14:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 162.7 |
| f367329d-b11f-366c-852e-18aff2faf0f1 | -2.6574 | -46.7591 | 2024-11-10 14:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 4515b0b7-13f6-3bb7-a102-9169ffeb4e9b | -16.6787 | -55.561 | 2024-11-10 14:30:00 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 92ff7050-181b-3a79-9f11-f654df99c297 | -2.2509 | -46.3513 | 2024-11-10 14:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 65a67194-43ba-3ef9-a178-d7d38e024333 | -2.0768 | -48.8342 | 2024-11-10 14:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| fbad3743-a338-37a7-a832-c71d82a528aa | -5.5815 | -41.6711 | 2024-11-10 14:30:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 3e7af442-88bc-3dba-bcac-2ebd72028dbb | -2.047 | -46.3565 | 2024-11-10 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| ea025678-22cb-3cde-860d-165e1e162756 | -1.7816 | -48.7333 | 2024-11-10 14:30:00 | GOES-16 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 226dee56-cc14-3d54-959b-9b86992136c6 | -5.7473 | -42.0166 | 2024-11-10 14:30:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 4a876dc3-0d68-38ff-8797-c4fdb4345482 | -5.8462 | -41.5052 | 2024-11-10 14:30:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| fd866ce7-f39d-3e83-a643-9f3795b137b5 | -0.3034 | -51.7071 | 2024-11-10 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 7fd9ac20-b0b1-30cf-96de-0de204e7a495 | -5.9925 | -41.9246 | 2024-11-10 14:30:00 | GOES-16 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 5286971d-ceb1-3345-bc14-0f0f88119c85 | -2.4365 | -46.3019 | 2024-11-10 14:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| a7d6805c-7902-30a7-aaa6-a2303f5b8fae | -2.2505 | -46.484 | 2024-11-10 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 21689b30-94e0-3918-b12b-6ff5df873390 | -4.3059 | -44.379 | 2024-11-10 14:30:00 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 81eb83f0-8611-3a5e-8a77-8ec27b7175dd | -4.3724 | -48.5844 | 2024-11-10 14:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 79641e5c-7167-3cc4-bea9-977fbcd61bb7 | -5.7475 | -41.9927 | 2024-11-10 14:30:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 3ac6c82b-cb78-3d2c-b8b0-733f460af970 | -5.4689 | -41.656 | 2024-11-10 14:30:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 5638b38a-8500-3d74-97dd-0dda31d340df | -5.1126 | -41.611 | 2024-11-10 14:30:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| f464db71-3d44-345d-ba35-5d7f779be29f | -5.9289 | -42.6661 | 2024-11-10 14:30:00 | GOES-16 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 75162567-9bcb-3570-b9b3-bb3a8bcad3cd | -2.2876 | -46.483 | 2024-11-10 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 1a3331e8-356a-3730-9d94-7a6981b7aff6 | -3.3172 | -41.0945 | 2024-11-10 14:30:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 3dde69f9-a39c-3dda-bc1b-7dc1d1fd56bd | -5.1128 | -41.587 | 2024-11-10 14:30:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 3573fa10-caf2-3cf2-83d1-62589804f0aa | -3.9483 | -48.1724 | 2024-11-10 14:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 2c2c83d9-32e4-3302-b81f-4d99a8afc5a6 | -6.1551 | -42.5764 | 2024-11-10 14:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 340.7 |
| 02a796fc-f575-356c-a23f-79d4ead3ba13 | -2.0953 | -48.8338 | 2024-11-10 14:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 193.6 |
| a61a88c4-2196-3f21-aa40-db5978671184 | -2.0769 | -48.8129 | 2024-11-10 14:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| a27ce049-fe47-37e6-a7de-60273a0d2be0 | -2.2504 | -46.5061 | 2024-11-10 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| ee855af6-3b88-36cd-af0d-adf69b677ae8 | -8.7562 | -44.0965 | 2024-11-10 14:30:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| a2b47293-cf1a-3276-8603-41d0104e3eeb | -1.4009 | -55.4518 | 2024-11-10 14:30:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 0a8dad5d-a736-3c46-897b-c32ed3bb837c | -3.2244 | -53.0524 | 2024-11-10 14:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 9919f388-782a-3f7e-8ea3-b2545ac3e694 | -3.4842 | -44.6933 | 2024-11-10 14:30:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4e93a83b-df2b-39c6-9576-fe0e4cbd8f19 | -2.1562 | -53.7039 | 2024-11-10 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 25cb527a-4151-34a8-83f9-1fd13268abdc | -2.2803 | -48.744 | 2024-11-10 14:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 39698405-42f1-355f-9f8c-81bfdefd93a7 | -3.4654 | -44.7168 | 2024-11-10 14:30:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| cdaca13c-1cea-37b1-927a-65d7838058fd | -3.2521 | -46.4739 | 2024-11-10 14:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 93.4 |
| dc097a89-f8bf-3ecd-9fe9-b0cb626e0065 | -1.5163 | -52.2106 | 2024-11-10 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| de8e8bbe-31a7-3ce4-a4cc-cc8f9a3b5c1d | -3.7853 | -47.4629 | 2024-11-10 14:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 6da8312d-90fa-3ab6-898c-8e608b003627 | -3.8185 | -44.8369 | 2024-11-10 14:30:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 144.8 |


[Clique aqui para ver as próximas entradas](README134.md)
