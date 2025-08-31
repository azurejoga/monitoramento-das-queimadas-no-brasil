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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 226a5be7-76e7-3611-9086-a8bc92a12d91 | -5.70109 | -49.13954 | 2025-08-31 00:33:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 99075a76-b333-3f98-9460-d2e0a97dfbf5 | -6.33377 | -53.43779 | 2025-08-31 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| baa1968f-47ee-39a8-a19a-46cb90927745 | -5.80334 | -43.86292 | 2025-08-31 00:33:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7be8190f-664c-3f6d-9a16-14a7c972d366 | -7.21027 | -45.44207 | 2025-08-31 00:33:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fe9a9481-58e9-3763-9c66-fd7e9a7e9af7 | -4.94207 | -47.58463 | 2025-08-31 00:33:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d7273d95-36be-38ac-8833-9798c276618c | -5.48122 | -44.40006 | 2025-08-31 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| ca85b6ac-826d-303f-88e6-224843a65b93 | -3.19983 | -49.10881 | 2025-08-31 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e92be556-fcec-348c-8d8f-442950a805f5 | -4.22521 | -47.20437 | 2025-08-31 00:33:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fc186d4c-6145-3abe-a290-a63817a5db3f | -6.70533 | -51.43186 | 2025-08-31 00:33:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fd983c39-535b-3347-91e5-f1b2b17d991d | -4.31456 | -48.2454 | 2025-08-31 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f48c12ad-401e-34b6-aeab-c5319457512c | -7.74674 | -50.26259 | 2025-08-31 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 2ac442fe-f287-3e35-bb96-42fd5edfb80c | -3.85073 | -49.28191 | 2025-08-31 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a7f0554a-c90a-3ce1-ae91-daea460c3cad | -3.20975 | -52.25191 | 2025-08-31 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 95732931-2917-3980-9acb-89479ab13dae | -7.45908 | -49.60344 | 2025-08-31 00:33:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 53308e9c-a8ba-365a-adf9-2a0b223041a8 | -3.58528 | -49.42854 | 2025-08-31 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 713bf80d-7099-301d-ac3a-00ec55bd6be3 | -4.26848 | -48.64329 | 2025-08-31 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2d58e377-b677-3863-9cf5-3cb9aa62b191 | -6.43113 | -43.96907 | 2025-08-31 00:33:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fcb4951f-f7e9-3217-aecf-8fdfaaaa77b9 | -6.17206 | -43.31639 | 2025-08-31 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c606cbc6-b7d5-3188-accb-987c5d797119 | -3.21139 | -52.26382 | 2025-08-31 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 0e32bbc1-01d9-3b8b-80ca-09754391d9d1 | -7.49317 | -45.05405 | 2025-08-31 00:33:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e4831210-2f85-3fa2-a165-784d723e5b52 | -7.74322 | -50.26849 | 2025-08-31 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 33de74ad-ed8e-3339-b20a-bf65a1d3b153 | -7.71588 | -50.2824 | 2025-08-31 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 75282838-b114-3c6d-abf6-205a69fd6580 | -7.331 | -44.08913 | 2025-08-31 00:33:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 59f3ed7a-fc7b-3dd9-9ed0-7c9522eee83f | -7.41056 | -49.52175 | 2025-08-31 00:33:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| f1a3cc78-2706-3968-95ac-a9a615b06698 | -7.6368 | -46.55495 | 2025-08-31 00:33:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3e97ea89-9d78-3511-a361-18953fcb9223 | -4.48154 | -48.11998 | 2025-08-31 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 8c1723e2-455c-3a1e-9b08-295a335886db | -7.20877 | -45.43173 | 2025-08-31 00:33:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3ca92498-36fe-3367-a8cf-6dfdaa91b33f | -3.59848 | -47.53128 | 2025-08-31 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3d148aa5-bd83-3dfc-ba68-00a5d1c55e36 | -4.15544 | -46.77621 | 2025-08-31 00:33:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 9e94bf70-4826-365a-b28a-a8b35bcdc98a | -4.2265 | -47.21354 | 2025-08-31 00:33:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e948d534-0e5d-3362-a875-09cad6042209 | -5.68828 | -45.95663 | 2025-08-31 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d1724ecf-6028-3993-9559-041065ba8e7b | -3.20104 | -49.11763 | 2025-08-31 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bdb4f24f-aab1-326a-88aa-065046bdd53e | -7.71446 | -50.2718 | 2025-08-31 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 2a1521a5-427b-3ebd-ba9f-b7ee6193301f | -6.86533 | -47.96461 | 2025-08-31 00:33:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 29811110-2abe-330e-8832-9907d6d8b437 | -4.15813 | -46.79511 | 2025-08-31 00:33:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 63149a81-8feb-3c78-b900-28373a4f3494 | -7.09561 | -44.31079 | 2025-08-31 00:33:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 578f3067-3688-38c5-8e99-562b63c7e49a | -6.70371 | -51.41994 | 2025-08-31 00:33:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| bbd21106-cf6e-36dd-a99c-b77825819ad0 | -7.09806 | -44.31631 | 2025-08-31 00:33:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| af888334-26ca-38d6-8e4c-7fa44fdc3075 | -4.14763 | -46.78693 | 2025-08-31 00:33:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c0562bc9-684a-33e8-a14c-06c656348181 | -4.07247 | -47.95929 | 2025-08-31 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b4d23cef-1a55-320c-b3d4-dec23efeeb68 | -6.70174 | -51.41386 | 2025-08-31 00:33:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a1cf17f3-f1b1-3e05-bee6-4f4195096379 | -4.74174 | -44.45557 | 2025-08-31 00:33:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 9b00ed71-778d-38c3-8604-7ebcc541f909 | -7.12865 | -44.60102 | 2025-08-31 00:33:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 197eead2-45cf-3e99-890a-fdd7d07ca40b | -6.86076 | -44.45063 | 2025-08-31 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 14342685-bae5-354f-b374-ab5f3636bec7 | -4.30263 | -48.09456 | 2025-08-31 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 25182001-7daf-3abf-8102-0b74de96a8ae | -7.40926 | -49.5121 | 2025-08-31 00:33:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| f10d7748-e685-3db8-aa94-4a909e7cd321 | -6.86411 | -47.95579 | 2025-08-31 00:33:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b4aa1526-674a-379c-b492-61bf55c556f2 | -6.61405 | -43.73988 | 2025-08-31 00:33:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 9ac4e1ee-1c2f-37b4-a6e1-84e2717c5e4e | -4.41897 | -47.60447 | 2025-08-31 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f968efcc-0730-37e5-b7ca-f2facb32113e | -5.70233 | -49.14859 | 2025-08-31 00:33:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 66198797-9f09-3f23-a8b0-653589ca792d | -4.27608 | -48.63325 | 2025-08-31 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a57753b7-63bf-3ee7-9955-7735f4fca239 | -4.31023 | -48.0845 | 2025-08-31 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1536e946-5425-3ce6-a718-ea732e065023 | -3.8157 | -48.96151 | 2025-08-31 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 1400c086-b9c3-3294-b8c1-74c367cb60d2 | -5.48188 | -51.22978 | 2025-08-31 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 07d2c274-a9ef-3cef-84a1-008133fefd39 | -6.17008 | -44.00031 | 2025-08-31 00:33:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0f37ddc1-093d-3054-9864-fd118b2ced6f | -6.25203 | -43.38761 | 2025-08-31 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| bba3eb52-0f31-3f21-bf29-a12b250b9132 | -6.859 | -44.43881 | 2025-08-31 00:33:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a7bc0d51-c4e6-3d29-b5b3-02a88de32326 | -7.22702 | -44.22323 | 2025-08-31 00:33:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bc223fcd-1bba-3e3f-b48d-d31e582b74ed | -4.55601 | -50.47713 | 2025-08-31 00:33:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 55b96228-e1ca-3d4f-a9f5-cc18e6919d99 | -5.81411 | -43.86137 | 2025-08-31 00:33:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4cb53271-3aa5-33a2-a285-4fa0921a3143 | -6.70328 | -51.42579 | 2025-08-31 00:33:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 5b1c051a-b8b1-3127-8fe6-9a4ce53ec181 | -7.09739 | -44.32265 | 2025-08-31 00:33:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| cdac652e-6f81-365c-a2ac-93cd9b12e81b | -6.7119 | -51.41247 | 2025-08-31 00:33:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9a754046-f1de-3edd-adeb-aae860fdf358 | -6.17534 | -43.56519 | 2025-08-31 00:33:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5c744b89-8bd4-3d74-b578-1915105b7606 | -2.78268 | -49.62265 | 2025-08-31 00:33:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 79aa8898-92a7-30de-8c01-a340928ecf2b | -5.8053 | -43.87638 | 2025-08-31 00:33:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 31a47366-5821-337e-ab69-df32173099d4 | -5.55682 | -44.21384 | 2025-08-31 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9f8aff29-d4e7-399b-84fc-bbc3642ac355 | -6.1787 | -44.13136 | 2025-08-31 00:33:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8adaca67-107f-33ed-b855-f9d81185ecef | -7.43754 | -50.26529 | 2025-08-31 00:33:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 43bf5c2f-db51-339f-b465-9a7d874caaa5 | -5.69764 | -45.95526 | 2025-08-31 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 9fae86ca-6ba2-3aa6-b166-d3be046278a8 | -6.18537 | -43.32931 | 2025-08-31 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 32b84387-0acb-3fe1-b5be-6458a902eb80 | -5.69908 | -45.96528 | 2025-08-31 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 21300e6c-2933-32ee-8995-5839d4e99195 | -6.12955 | -42.95147 | 2025-08-31 00:33:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 826244ab-ec72-3b7d-b096-cfb89f07b11d | -3.80566 | -48.95393 | 2025-08-31 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0ad2e0ea-13ba-3e02-bf67-f2e338e9e891 | -6.17424 | -43.33108 | 2025-08-31 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| befcf732-e3cb-30db-9740-6b1e173020b7 | -4.14721 | -46.45193 | 2025-08-31 00:33:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| f0758c66-9afb-3e6d-bde8-913cfd32cabc | -7.40139 | -49.52303 | 2025-08-31 00:33:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0ac4541a-9464-3491-aaec-a6fab419b59b | -3.42072 | -49.04762 | 2025-08-31 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aa8fe65a-53de-31ef-92b2-91f94198ca10 | -6.28659 | -43.54352 | 2025-08-31 00:33:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 2ed57988-7678-390e-a270-ee7945d38230 | -7.43615 | -50.25489 | 2025-08-31 00:33:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 50365237-9623-3fa2-a94a-5e474985b55c | -13.3636 | -46.95 | 2025-08-31 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 82f7f623-2b78-3237-9147-154610b24640 | -6.1665 | -43.3273 | 2025-08-31 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 515110d6-879d-3ea0-891d-402663676b5b | -11.8373 | -46.4287 | 2025-08-31 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 38e9e7d3-3e8e-32bd-86ef-34b3bf9ad771 | -16.2217 | -52.6992 | 2025-08-31 00:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 31b71e65-0824-31fb-8563-71eb9d0b1081 | -12.3099 | -45.7 | 2025-08-31 00:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| a585f271-0a0d-36b5-b040-c989d375b874 | -16.2417 | -52.675 | 2025-08-31 00:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 03385755-bd9a-334b-a2db-50c8a716d528 | -13.3443 | -46.953 | 2025-08-31 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 5594f642-4538-38ad-91c6-268aa3ed0efa | -9.0614 | -65.4355 | 2025-08-31 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 73391a34-1d8f-3077-96c9-5791fec6ea12 | -6.1853 | -43.3257 | 2025-08-31 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 66de3233-52f5-35aa-87bd-d47976eb3f53 | -9.2745 | -67.6433 | 2025-08-31 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 411e5e26-9d2d-3db1-9a69-fa059865b1a5 | -7.0951 | -44.3128 | 2025-08-31 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 00cd1e2b-2688-3834-92b1-fb0f69634175 | -16.2221 | -52.6778 | 2025-08-31 00:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 277da4cd-5ee6-368d-88dd-d7aaf5ab26bb | -12.0976 | -44.717 | 2025-08-31 00:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2a05b09a-65af-399e-ab97-aad7db0281be | -8.7439 | -62.3979 | 2025-08-31 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 617c2aea-5bae-32dc-8ab6-84d89b31fcb0 | -3.8146 | -48.9515 | 2025-08-31 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| eccfabef-09ca-3b7e-8add-01571dd5aab8 | -7.1139 | -44.3111 | 2025-08-31 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 7f172fa4-9f83-3029-b483-c440321fe89a | -7.0948 | -44.3358 | 2025-08-31 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| bc5a81ea-3ca1-306c-b170-cd82dc57ea3e | -10.3126 | -59.2023 | 2025-08-31 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7d412855-5c2b-374c-8674-c78f0dff1983 | -12.3291 | -45.6971 | 2025-08-31 00:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8d5a770f-ac07-3a77-9d01-b121bab32c14 | -7.0774 | -63.1948 | 2025-08-31 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |


[Clique aqui para ver as próximas entradas](README7.md)
