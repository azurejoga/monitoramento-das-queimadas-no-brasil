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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45809d82-2826-3cc0-9803-cd75265eb914 | 1.8398 | -55.9204 | 2024-11-25 00:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 65cc7aca-507e-3278-8385-5e101ff54e8d | -3.0359 | -45.0515 | 2024-11-25 00:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 15a52a60-86a4-393f-86df-fa660e1f295b | -3.0734 | -49.2127 | 2024-11-25 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 6e51db54-9e2b-31c0-b953-b9742aaf8197 | -3.0735 | -49.1914 | 2024-11-25 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 01c44efd-64bb-3461-8cb8-f61151dd05df | -2.3211 | -53.8821 | 2024-11-25 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 179.9 |
| 41bcec6b-43e7-3d12-b1be-04ff6ac7ef39 | -3.0358 | -45.0741 | 2024-11-25 00:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 466cea5a-fbb4-3684-b0d6-b842252802c2 | -3.2872 | -51.1194 | 2024-11-25 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 6e63f717-9c92-3baf-a811-9f2af2f4c044 | -4.0231 | -48.061 | 2024-11-25 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 9fe905c9-0ad2-38dc-b16f-2b18cfdd71cb | -3.9494 | -47.9776 | 2024-11-25 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 01d661c4-18d2-30b6-82a2-336102bd1b60 | -4.0415 | -48.0818 | 2024-11-25 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 747bdfb8-c89f-3e3b-a103-cacb8b94c452 | -4.466 | -45.5263 | 2024-11-25 00:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| c132ba7e-2e36-3642-b960-a7f943e74671 | -4.4845 | -45.5478 | 2024-11-25 00:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| c60d7fab-894e-39bb-8b30-058111a177ed | -4.4659 | -45.5488 | 2024-11-25 00:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 676eeb0d-8c44-3d04-a840-1b1aa19cc76e | -3.7129 | -47.116 | 2024-11-25 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f07ed5e2-72bc-3bfe-b55e-e06fb48aad87 | -3.185 | -49.0386 | 2024-11-25 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| cc3e193d-4643-38a6-a241-cb954be2ffcf | -3.7057 | -52.426 | 2024-11-25 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 5172c8d6-c2f7-36e2-a661-ec07b52c2213 | -4.0045 | -48.0835 | 2024-11-25 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| ab839d8b-ce70-32a5-b395-c9516ef5044d | -3.4581 | -50.0047 | 2024-11-25 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| b54c0628-37b9-3cba-9978-c060fdb14a3c | -2.3394 | -53.8818 | 2024-11-25 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 190.9 |
| c54199e1-245a-3056-8b93-be882bffb4bd | -2.3211 | -53.862 | 2024-11-25 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 356.3 |
| 6663e589-1bd4-36dd-9acd-641ef3724f8b | -3.7058 | -52.4055 | 2024-11-25 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| b342e189-b381-37ea-95b0-17ad0d15c3bb | -4.4847 | -45.5253 | 2024-11-25 00:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| ab34fb31-f59d-3c8e-ab0c-4a6caf1eda57 | -2.2483 | -53.6216 | 2024-11-25 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| a4d21dbc-8418-3f11-96b1-304833612634 | -3.185 | -49.0599 | 2024-11-25 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0c2b34ea-5129-3430-b234-e8e09d00188b | -3.9493 | -47.9993 | 2024-11-25 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 8dc7b5d5-019f-3beb-8f44-9912410e8a83 | -3.4396 | -50.0053 | 2024-11-25 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 41d1771d-3069-357c-b687-40036faba19c | -2.3395 | -53.8617 | 2024-11-25 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 367.6 |
| 142f10db-a4ca-389a-9311-309e40efa72f | -4.2604 | -48.7184 | 2024-11-25 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 26b2de66-fd3f-39de-abcd-5cce34abfa52 | -0.0644 | -50.8171 | 2024-11-25 00:00:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| b632655a-b0cf-3441-a9d4-d837bb3d4018 | -3.5159 | -53.8132 | 2024-11-25 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d0c0977d-419d-3b77-9936-8929710d04c1 | 1.8581 | -55.9004 | 2024-11-25 00:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a0f81eec-9bea-3065-a662-f5872981f661 | -0.046 | -50.8171 | 2024-11-25 00:00:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 70d76df8-8897-35bd-aa9e-63b4cf7eb011 | -4.023 | -48.0827 | 2024-11-25 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 91efa02b-dbe3-34b8-9275-42f4d0037c78 | -3.1369 | -44.343102 | 2024-11-25 00:00:00 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 19e02f5b-2989-39af-b22d-ccd566d3f765 | -4.3164 | -45.8908 | 2024-11-25 00:00:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c35a5e9f-1387-314c-8b8a-8436f02faae8 | -4.3007 | -46.887501 | 2024-11-25 00:00:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4374ace2-209c-3bc8-989b-8ae736602ffc | -6.1763 | -35.270302 | 2024-11-25 00:00:00 | METOP-B | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1f3b1ed4-8de7-3dba-8907-4ba824d0b0c9 | -2.8293 | -45.129902 | 2024-11-25 00:00:00 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62296f8a-be09-3197-a313-f9f7ba42093a | -4.5683 | -46.285198 | 2024-11-25 00:00:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2822a596-2d79-3181-b20d-f680e0beddcd | -2.32 | -53.86 | 2024-11-25 00:00:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d22aef4c-8b1f-38e1-87b6-78d45708dfa7 | -5.9088 | -45.559799 | 2024-11-25 00:00:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0295a04d-9a61-3e3b-87d3-7324b25e6cdb | -4.3026 | -46.896198 | 2024-11-25 00:00:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6d40c07d-bb68-35cf-883c-dc0d645fb972 | -5.5823 | -45.198601 | 2024-11-25 00:00:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30e3dff7-16c6-3975-a848-ca4cb26489bd | -3.9436 | -47.967999 | 2024-11-25 00:00:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4886620-50da-396b-bb09-8297a857d392 | -4.8548 | -38.3731 | 2024-11-25 00:00:00 | METOP-B | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 533b3ed9-760b-3c98-bdcc-af720aa1ba92 | -5.9105 | -45.5676 | 2024-11-25 00:00:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ed3df1e-f4c7-3982-a011-06ff80c77924 | -4.5326 | -42.899502 | 2024-11-25 00:00:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a17d22fe-f00d-3602-8a4c-907660f4ea78 | -5.6175 | -43.4622 | 2024-11-25 00:00:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72077dd6-8cbb-3b44-90aa-a88431be2c82 | -4.3372 | -45.984402 | 2024-11-25 00:00:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b83eefc7-e4cd-33df-b233-17dc83d122f4 | -5.8112 | -39.205502 | 2024-11-25 00:00:00 | METOP-B | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 779a1a69-9df7-3f28-98b0-dd70ea8c601f | -4.1956 | -50.6637 | 2024-11-25 00:00:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19d6b4e3-679b-342f-ae05-9f66e52fee99 | -3.6966 | -42.301998 | 2024-11-25 00:00:00 | METOP-B | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7cd87192-1741-366b-8d82-6eed590710f3 | -4.2909 | -46.889702 | 2024-11-25 00:00:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 132c5768-9a5b-3a0a-811f-31140c1fc611 | -5.821 | -39.203201 | 2024-11-25 00:00:00 | METOP-B | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4714704d-9a1e-3d08-9c92-2d1611e27da3 | -4.7822 | -44.469601 | 2024-11-25 00:00:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b960b44-a25b-34dd-9ec6-165ea44c903e | -4.7806 | -44.462601 | 2024-11-25 00:00:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68ca6351-2041-3b66-a541-3a4c83c01bab | -3.6998 | -52.365501 | 2024-11-25 00:00:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bd1fcd8-3bfd-395f-90f3-425e8d51f133 | -2.897 | -45.431702 | 2024-11-25 00:00:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| adafeada-20a8-36b8-be89-01634c8dfcf5 | -3.6775 | -45.885101 | 2024-11-25 00:00:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6880eebb-5151-3dc9-ac99-51906873a0ef | -4.5476 | -42.8745 | 2024-11-25 00:00:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23b438e0-f587-3b25-a135-0d119a47d62a | -4.5352 | -43.551399 | 2024-11-25 00:00:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e19612d-67ef-3c68-bc99-987099f1a847 | -3.9939 | -44.030899 | 2024-11-25 00:00:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07ef490f-a1e4-3a12-9764-60c36117e70e | -3.5432 | -43.950699 | 2024-11-25 00:00:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25af84cc-af90-387f-bf72-c43520fa37fb | -5.6206 | -43.475899 | 2024-11-25 00:00:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d84fadfe-b724-333a-889d-473ac0290e5a | -4.5688 | -38.4716 | 2024-11-25 00:00:00 | METOP-B | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 963f46be-2477-3a14-8f21-3516e0a4e436 | -3.9479 | -47.987701 | 2024-11-25 00:00:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98731e90-c541-3ac0-ab6d-458104941e50 | -3.2897 | -43.419701 | 2024-11-25 00:00:00 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f99971a-0d67-3f79-a316-2ffe383c96b9 | -5.6511 | -46.631401 | 2024-11-25 00:00:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e626a9d0-34b6-3b84-ab56-3749b0a8dc5e | -3.9587 | -50.840599 | 2024-11-25 00:00:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a9b7f77-c73d-3c90-9369-b671d264bd91 | -3.3644 | -44.026199 | 2024-11-25 00:00:00 | METOP-B | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8769a45e-3e8d-39bc-8388-be39fa83a19a | -6.1801 | -35.2859 | 2024-11-25 00:00:00 | METOP-B | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 508b98ad-a1bf-39b9-8130-42ea4ac632ba | -3.3851 | -43.477299 | 2024-11-25 00:00:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d0723ec-c6be-3f28-b323-df4f46d9ad77 | -4.5466 | -48.9426 | 2024-11-25 00:00:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4324830a-a2a2-319e-9d23-460ed916050d | -4.3147 | -45.882999 | 2024-11-25 00:00:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b9a6a29-bf77-347a-bb38-052df2771d39 | -4.5712 | -38.4818 | 2024-11-25 00:00:00 | METOP-B | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8b637808-12a5-330e-af22-ce8f820f11fb | -2.7871 | -52.978401 | 2024-11-25 00:00:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8da9018c-3f87-37ce-8493-c44b78394fd9 | -4.5362 | -42.8699 | 2024-11-25 00:00:00 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74cf8896-129a-370c-ac09-71bc508a5959 | -6.73 | -43.5555 | 2024-11-25 00:00:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6c4c373-9ab2-340c-8105-4a31f12caf86 | -5.1571 | -44.5354 | 2024-11-25 00:00:00 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2faf4e37-cd14-3ad0-bfe1-46ab1bc6433a | -4.08 | -46.8186 | 2024-11-25 00:00:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37808523-4f47-338e-a63c-ae694c26d2ba | -5.6092 | -43.471199 | 2024-11-25 00:00:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c9d9879-2bed-3452-8d55-91352e0ed889 | -3.3866 | -43.4841 | 2024-11-25 00:00:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3534264a-b92a-3233-a27a-e24dd7009289 | -2.7968 | -52.976299 | 2024-11-25 00:00:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d5dfad4-c3bc-32b6-a844-f60510ab9029 | -3.2234 | -46.293701 | 2024-11-25 00:00:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba3b9b7a-6759-343f-8851-b1f35e846487 | -4.8032 | -40.689899 | 2024-11-25 00:00:00 | METOP-B | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8b344801-e9fe-3c2b-aa39-9f7adcccc2a4 | -3.2882 | -43.412899 | 2024-11-25 00:00:00 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e070278-4f25-3e7d-96c0-a68d9919cd52 | -4.4762 | -48.105099 | 2024-11-25 00:00:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d21a86c1-082e-3a00-9268-6bfd2f5d58f9 | -4.6344 | -43.946999 | 2024-11-25 00:00:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 374bf315-ee19-3e6a-a6bf-2cb476061e7e | -5.692 | -43.887299 | 2024-11-25 00:00:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d2edeb0-9a81-3bb4-a07f-49a76c29e6fb | -3.7022 | -43.4212 | 2024-11-25 00:00:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ad8fab8-fbac-3fe2-9081-4440f5df540b | -4.7095 | -45.715801 | 2024-11-25 00:00:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 727cbd26-2688-33c9-8c7b-f48982fbf6b6 | -6.754 | -46.513 | 2024-11-25 00:00:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ab00c49-268b-32ea-8a21-4375e6dd0908 | -4.4708 | -45.5205 | 2024-11-25 00:00:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6558d1cf-2d07-30d0-ab1c-0275a6650529 | -4.3874 | -45.9324 | 2024-11-25 00:00:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17231b33-cf97-31b2-8506-8d1b5e5e4c3f | -3.0306 | -45.063202 | 2024-11-25 00:00:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc95a0a1-57cc-3a74-a391-9c81c7e94fe4 | -5.902 | -43.398998 | 2024-11-25 00:00:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd36bd18-65f5-3beb-a757-09df44ddb896 | -4.5845 | -46.079399 | 2024-11-25 00:00:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7a1a847-6138-3c2d-8911-35f22e57212d | -4.1525 | -44.2785 | 2024-11-25 00:00:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90cfc863-73f3-3b66-a5a2-87a7c44adb95 | -4.6359 | -43.953899 | 2024-11-25 00:00:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1125b011-bced-307d-9a9a-11663c7436d7 | -4.313 | -45.875301 | 2024-11-25 00:00:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
