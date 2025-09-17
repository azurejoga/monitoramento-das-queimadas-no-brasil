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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bafe8320-a22d-3fbb-adbf-bc4ccbf6b068 | -7.25924 | -46.59578 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92e36b19-2e8a-3570-9287-423329d9e9fb | -5.80305 | -45.70832 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba246433-212d-3516-9dbd-0329851f8fce | -7.26599 | -46.59676 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e6c9007-f0e6-3905-a663-511faaf68331 | -5.80706 | -45.70516 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04fb441d-0936-31d0-adc9-1d756c8bc1a8 | -7.09348 | -44.54384 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f3bc6f1-8dfd-38a7-b3c4-d6744e3ceae9 | -9.09266 | -44.93531 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6b323e3-a781-3021-8576-bb2389030409 | -6.95848 | -44.54852 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24d3e077-fe83-3c54-98ff-655bc5acc7d2 | -8.02972 | -49.84256 | 2025-09-17 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5570976b-ece2-32ec-8564-3b16ea1553ba | -8.15947 | -46.75865 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc9408dc-d636-3dc5-b897-954c8505f1cf | -3.80384 | -48.63713 | 2025-09-17 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b393201-53f1-3764-abb3-cdfc32a977e7 | -6.74372 | -43.72297 | 2025-09-17 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37be3454-7636-323f-ba60-b0d0ee678f21 | -6.19366 | -45.12616 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ed35de4-41f1-31d1-a553-298bbaa6afd2 | -6.52137 | -41.81663 | 2025-09-17 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aea54b92-e726-3126-a9b1-ca371a4beecd | -6.39628 | -43.34479 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 852f71d8-6b68-397e-ba5f-5665a1493cde | -9.04441 | -44.88482 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9bf7effa-29b8-30d5-aae6-42196807cc12 | -8.96854 | -44.19009 | 2025-09-17 04:32:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba60e2a4-4d12-3507-a62f-75d27d9d3452 | -5.78205 | -43.94817 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f2fb0298-b72f-37f5-9296-9cccb2c6793c | -8.66341 | -46.39011 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6d86601-2e1f-3f46-b509-a8e006804553 | -5.61711 | -51.72651 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73bc7acc-f87b-3aa0-82b8-a7501a4f707d | -7.25812 | -46.603 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 876403b0-f972-3551-8f1c-4ab75b68ff20 | -5.77991 | -43.91131 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0670feae-fb31-3f2b-9b5b-6a4d5e5a17f1 | -6.9642 | -44.53471 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cbb7cb8f-e3bd-35f4-bf90-a39464844f5c | -8.14323 | -44.84283 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85a806ae-257f-301c-8a68-9d1ef26cac60 | -10.39909 | -50.63154 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2a33d80-06e1-3b93-8111-c4481e01b1d1 | -7.60875 | -47.46936 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99e6d326-75a2-3fe3-b9fe-38f2be9d9a29 | -9.05215 | -44.83274 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa06cf57-431f-311a-bb5b-1be264788858 | -8.1645 | -46.74837 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbdfcf08-e8d1-385d-9ffb-2f057734e5de | -7.20707 | -44.38036 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 808acb35-3fae-3edd-805b-713422a02452 | -7.97816 | -45.68022 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59f56a3b-de55-380f-b88d-2825d0224d6a | -8.63664 | -46.42813 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a39197d5-d1b7-3e2e-b603-34968a98b983 | -8.89184 | -46.14902 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80ca6a28-9bd8-3bae-b866-ee209cd8f6d3 | -5.80021 | -45.70402 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2714b028-e677-33d5-8f1e-a6abde649246 | -5.3282 | -44.99319 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41199706-033e-318c-9320-935c4e3baef6 | -7.82317 | -46.16212 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1599e815-dc0f-3cc5-8352-e9d8640b7220 | -4.60513 | -48.7844 | 2025-09-17 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e717cdd2-45a2-30f3-88a5-f698c74c728f | -10.8702 | -45.43763 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e808ecd0-39c2-3a78-922b-989cd7775021 | -5.31024 | -47.2294 | 2025-09-17 04:32:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bfa15f3-7a78-3b61-8ac7-fef2cd5f81a3 | -8.95744 | -45.75578 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e1a0440-f34f-3f4e-89e1-65368153b45c | -5.78711 | -45.94781 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56cb36a9-43d3-368a-be6f-e9b59971d409 | -9.07574 | -50.31347 | 2025-09-17 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df9c556f-ae89-3c68-a025-06bfe686cfa8 | -9.04569 | -44.95184 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceaf66d8-9c49-32ec-bbcf-29822d09587b | -7.65304 | -44.47187 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fe449c18-0fe5-3dc5-a945-0d338ea5953b | -5.44677 | -46.68019 | 2025-09-17 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f6ce879-4cc3-3cd0-bec1-5d583def3538 | -6.39755 | -43.3329 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| faa2f634-82d9-30bb-ac0b-c6a90d0cfb60 | -7.38659 | -50.00206 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e296aeb-48e2-36af-8fd4-099bd784ac9a | -4.66157 | -46.31734 | 2025-09-17 04:32:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93b36afa-5c31-3ce7-bb20-5931afa0b259 | -5.9188 | -45.91109 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd75e995-b13d-3599-ab5e-cfc51383c12d | -3.6463 | -48.32426 | 2025-09-17 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41f71eea-92e2-358c-99d7-183c0dd0f2bd | -11.46705 | -43.56147 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eef90a68-450b-3627-85fd-391f0745cbb3 | -6.46692 | -43.68235 | 2025-09-17 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4ddb415-d5f2-38a6-b8c0-5a39c82613a1 | -10.79401 | -50.72659 | 2025-09-17 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 327183ac-5155-3d23-a644-aa54f6aeb3cb | -8.41933 | -47.20929 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daf0f44e-c83b-3b4b-b135-95ed5f354c4d | -8.56526 | -46.3445 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5c14da5-052e-3376-86de-603badedf5fb | -8.14989 | -46.75349 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69101507-6ebc-3791-9175-191ddf052b41 | -8.90209 | -47.8839 | 2025-09-17 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f0082210-0ba2-399b-a3dd-7cf5f9e38bf5 | -8.92247 | -46.20441 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15c958a4-4072-3421-9135-55ef293a9a33 | -6.8654 | -38.43689 | 2025-09-17 04:32:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a18da1ab-e403-3050-9b89-7993e38ea272 | -8.63604 | -46.40885 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c74d8c5-6fa0-3e7c-becf-71c56961abb2 | -8.1634 | -46.75558 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2c5512c-73e5-3a23-b9d7-6a521affc0ef | -6.87087 | -38.43766 | 2025-09-17 04:32:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a9980db-e70f-3a07-898c-5100efae7f48 | -6.16738 | -44.49243 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71904475-5e30-3ced-a8a3-6a5373b3b187 | -5.45224 | -50.82261 | 2025-09-17 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23fe9234-fafb-351e-b889-8deb07bbd4fb | -8.77502 | -46.09702 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb3c13a5-4cc0-3f7b-a41a-c66259d1bf76 | -7.38376 | -49.99778 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b88f7965-f144-33f0-a102-3835ee1f2052 | -9.75704 | -47.33959 | 2025-09-17 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d9e84ce-840a-33ea-b063-99969e231d9c | -10.87448 | -45.43389 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6bd516f-91a0-33d8-9d5c-e45bc254808c | -5.34662 | -44.82561 | 2025-09-17 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df5f225b-6245-3089-9f66-43c6353c9ed0 | -6.67333 | -46.3062 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c997af7d-87b4-3589-83fc-938e07e2018a | -9.12008 | -44.87644 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f74ea2f-4e56-37a8-b26b-e71dad3ddd4f | -8.98109 | -45.03421 | 2025-09-17 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 157cc928-328f-3389-acb7-9d771170bd9c | -9.10435 | -46.92115 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 463e717b-b962-3bdb-959d-36d7b82e66ae | -4.0429 | -49.0747 | 2025-09-17 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20465d37-ba24-3075-83dc-2e09c0304631 | -6.87648 | -43.97104 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b73549f-1f8b-3543-86e4-e13d2727902a | -8.98975 | -45.75665 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 211dd096-b82f-3c98-bb6a-27f633d91cc1 | -6.77377 | -44.7088 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd8c3404-20f9-3d24-8af3-d5e9e6642d15 | -7.57519 | -44.59615 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 681e8db5-ef26-3dd3-b0bf-b615b2311227 | -7.64934 | -44.4713 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dc3dbd0-2024-362d-ab8b-33780b9fba69 | -7.72201 | -45.29882 | 2025-09-17 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d35fa572-25ff-3f73-9465-4127de3082a1 | -6.98759 | -44.6039 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63a46b15-c368-38a4-8ae6-f69bfc488890 | -9.04874 | -44.88103 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f8faca2-be75-3705-b255-18de06c6e8c1 | -8.68966 | -46.37898 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acb9fd7c-9c42-3e0f-9660-82748bf386ae | -11.46345 | -43.55706 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8b43c41-c16c-36e5-b3c0-116c42212cfc | -8.97242 | -46.01494 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff38ae9d-643f-32ba-82e3-943f73957a04 | -5.24686 | -49.85633 | 2025-09-17 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c92bdcdf-fee3-3fe9-824a-3b3818f44587 | -7.98322 | -43.93517 | 2025-09-17 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc0f230d-6400-3bdc-80d3-c9a863360f21 | -6.16229 | -44.52595 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e2bd97c-1ecc-381b-9587-1e9777814284 | -8.34915 | -44.71764 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78554811-bd25-3c37-b37c-f888f77d05bd | -7.03396 | -44.1625 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64324e18-78e1-393b-a5a0-f6b6693bf815 | -10.62904 | -48.75737 | 2025-09-17 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f6d44890-335f-3bb1-95ad-020f321f0c91 | -7.88618 | -48.16839 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7da9dbd7-5a52-3dd6-a1ee-1b219391ea7e | -11.02897 | -45.06057 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 86e85fb0-4775-387e-af1d-f0f4777c6e2c | -7.81093 | -46.12949 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 715c522e-ae45-335c-b853-c61c04b0136e | -9.09824 | -44.92283 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e97b4dde-5293-31ea-bd67-d0a6a70d4212 | -5.6427 | -48.60674 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a45313b1-9c9f-332d-a4b3-8d12da3abf3e | -6.40347 | -42.66509 | 2025-09-17 04:32:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9b761e69-75a5-32aa-bd76-3519717510a4 | -8.90747 | -46.28036 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 641b5443-a3ad-36df-9d62-565f12082d76 | -8.39751 | -47.24668 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b1bf07a-78bc-3102-a03a-e6314edf69b7 | -10.4019 | -50.6358 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76ac3c72-e6c6-33b7-aa85-b994f815f9d5 | -8.20659 | -49.4852 | 2025-09-17 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcbcbd50-6050-3c3f-bc6a-751d497f4a06 | -6.46055 | -46.00755 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README43.md)
