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
| 6a99169d-db90-3ec2-9a93-5db40f53b91e | -3.9957 | -47.673302 | 2025-11-15 00:18:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 201ff094-0c74-3a8a-9b68-a728d1ba1ca5 | -7.5163 | -47.186699 | 2025-11-15 00:18:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9eb13fd-a004-3149-99d2-90076e53afc1 | -6.0551 | -44.156898 | 2025-11-15 00:18:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b0ef39e-63b1-3fbd-a122-f8ac9d352f13 | -4.4673 | -45.6525 | 2025-11-15 00:18:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1769c3c4-545e-39bf-843d-7e207daf5d81 | -4.5326 | -43.2141 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 186a4393-d511-336e-bdf5-7c7c607088fe | -6.5364 | -39.254398 | 2025-11-15 00:18:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b4ca6350-d2c7-3d4b-835e-aa277f385b0b | -5.1776 | -44.102001 | 2025-11-15 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2aea12ff-8780-3601-a5bf-0bc26242f0af | -6.2542 | -41.411598 | 2025-11-15 00:18:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a55b220b-d003-3d8f-b594-c8a94d453fc9 | -9.7972 | -42.2076 | 2025-11-15 00:18:00 | METOP-C | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2112af05-d70f-3b71-bd8d-3d7d4c37d21f | -14.0376 | -43.2551 | 2025-11-15 00:18:00 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9218d2a2-0c1a-3525-8a05-422bf4adf329 | -3.9796 | -44.2705 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d7c6031-e693-331e-957d-27dca94e4f99 | -13.2859 | -44.201 | 2025-11-15 00:18:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8286c899-b7b0-3cbd-8d5a-5e94614983e2 | -4.6467 | -43.578999 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6ad1219-fc97-3ef7-aab1-0260a7b370f7 | -11.8499 | -49.218601 | 2025-11-15 00:18:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| faabd8ed-6b54-3f27-a20a-2024de5671dd | -5.2231 | -44.348499 | 2025-11-15 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 059b4cae-54f4-384a-bf0a-db4fbb1bf37a | -12.4702 | -43.742298 | 2025-11-15 00:18:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0f4bf7ce-6e15-31f5-85d8-529535f2178c | -3.47 | -45.656502 | 2025-11-15 00:18:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3920b58b-c71b-3bf3-bff7-33e312cde506 | -8.5849 | -46.069901 | 2025-11-15 00:18:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f605ef6-0f6d-30e9-9bda-90d8b3098e69 | -17.5728 | -46.679501 | 2025-11-15 00:18:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d498645b-ab37-3bbb-ab1a-847c6ea9d446 | -12.2253 | -49.377399 | 2025-11-15 00:18:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91450fdb-06b4-3c73-be7f-38b5bc6da966 | -7.4404 | -42.766399 | 2025-11-15 00:18:00 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5fa82156-0bbf-3a48-8d61-67b42d83516d | -3.3179 | -44.306198 | 2025-11-15 00:18:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8240357a-143d-30a8-b915-a65a22c530a3 | -4.5759 | -43.1325 | 2025-11-15 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7f9b6f4-3931-3043-8044-3f21bea27bfc | -4.5357 | -43.227798 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98e4878c-4fba-3b33-b029-b9335c67ecd5 | -6.8878 | -42.059898 | 2025-11-15 00:18:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0474b6bf-4182-343d-9dd1-0d126231215a | -3.6457 | -44.796501 | 2025-11-15 00:18:00 | METOP-C | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68b8ef4b-b8f1-3718-b559-46435d7e9491 | -9.4786 | -47.279598 | 2025-11-15 00:18:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f08a94b5-9c9a-3e00-8956-f19e4bb4cf26 | -6.0484 | -39.681801 | 2025-11-15 00:18:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fb9d1b90-e4ee-31cd-8445-206fd57d5b79 | -17.2635 | -42.660801 | 2025-11-15 00:18:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a1e21353-21d3-32af-91d9-aac8c6c9ed58 | -5.8844 | -42.271599 | 2025-11-15 00:18:00 | METOP-C | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 06a210ed-f7b5-33a6-a329-ca87730bbd53 | -2.9478 | -48.581501 | 2025-11-15 00:18:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce61219b-7087-3f4b-b9f8-2df9f72929f4 | -3.788 | -45.970699 | 2025-11-15 00:18:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1fe7d453-f560-38f8-873b-32912964f189 | -4.6637 | -45.336601 | 2025-11-15 00:18:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 787c72e6-b8b6-38b5-9ebe-ff4a7491d7b7 | -4.4595 | -45.389702 | 2025-11-15 00:18:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ace40a1-2021-3974-8400-669db8563518 | -4.5538 | -43.216599 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ccb8039-e0ef-3961-a69d-b6e7878d6abf | -3.2804 | -45.455502 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d98a402-5349-353b-b0ff-bcc2d3cdb5e8 | -4.6877 | -45.169399 | 2025-11-15 00:18:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6847f77d-2500-386e-8e33-45c508d7fdc5 | -4.5602 | -43.7878 | 2025-11-15 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bfbddf7b-dd2e-3eef-9129-69c90239537b | -4.1435 | -43.1357 | 2025-11-15 00:18:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68419bc1-4944-3520-9e60-020493e026a9 | -3.0487 | -47.114799 | 2025-11-15 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 534f0dbc-b82d-31e1-ae82-6535053a6618 | -9.1074 | -43.9576 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 976b0bb0-a9c2-3dd9-af95-cfb2c264ffe4 | -19.133499 | -42.698101 | 2025-11-15 00:18:00 | METOP-C | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd330c59-5de4-37e3-9b44-ea0f66f00a7f | -5.6887 | -45.964901 | 2025-11-15 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dec23468-44a1-391b-8ebf-ea59cd3053b6 | -9.1416 | -45.188099 | 2025-11-15 00:18:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1b9aa6b4-8aac-35a1-a2cf-84a92276e1e1 | -6.1551 | -48.031502 | 2025-11-15 00:18:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5a7f1d6-40f7-3bcd-ade5-a518bbe68fc0 | -3.2821 | -45.4631 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c308cb8-7836-37fd-9ec9-cca8dce11c92 | -6.7339 | -42.968102 | 2025-11-15 00:18:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08a0fee1-e370-3d19-b15a-d0621f0cd21c | -10.3062 | -44.599499 | 2025-11-15 00:18:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 68c33f46-4129-3c04-86c0-b1c3ab71fcf2 | -4.1041 | -48.020699 | 2025-11-15 00:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d41c41d-19d0-3e0f-9581-9950471393a6 | -20.1425 | -41.6306 | 2025-11-15 00:18:00 | METOP-C | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b3da37f-9d5d-3a67-9a24-10e1e4caf44f | -17.2439 | -42.665199 | 2025-11-15 00:18:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 145cba4f-9bea-314f-959a-ac2848d80c47 | -4.4188 | -43.347599 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63cccd4c-e282-3189-9e69-bd7eb67df5df | -4.2783 | -44.587898 | 2025-11-15 00:18:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6878bd7a-c9bb-3e60-a0c7-dc3036f81415 | -6.0567 | -44.1642 | 2025-11-15 00:18:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 066fee8e-7964-307f-888e-6ea23a034b08 | -7.5307 | -47.206001 | 2025-11-15 00:18:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7060a7d8-84ae-3253-a3cb-a406d2f4714e | -2.5145 | -47.797901 | 2025-11-15 00:18:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57d16b0a-8b8a-3ffc-9d6d-a0c3034945ed | -11.1566 | -48.145199 | 2025-11-15 00:18:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 885b60ba-6fe1-3290-a54b-ec414491c1b4 | -12.1474 | -46.673901 | 2025-11-15 00:18:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7d83a1d-7c90-3976-8d3b-bc0339c1d2f9 | -8.3164 | -45.402901 | 2025-11-15 00:18:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 327b89b9-58ed-368c-9ce7-7c981eda44b6 | -6.7308 | -42.9543 | 2025-11-15 00:18:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 31025143-6e24-353d-859f-7c2f321274a2 | -11.9486 | -44.848301 | 2025-11-15 00:18:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 550ba9b6-f25e-3737-9164-9b8458d121f4 | -3.4488 | -45.9268 | 2025-11-15 00:18:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 312f1e46-2c37-321a-9d9a-5f3a86963ce7 | -9.5177 | -42.935398 | 2025-11-15 00:18:00 | METOP-C | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b40839f7-fffc-3694-acc8-1876f45f637c | -5.6225 | -43.9286 | 2025-11-15 00:18:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c82de1db-75f6-30cf-a5b4-86f3b0c4bdec | -11.9506 | -44.8573 | 2025-11-15 00:18:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65508c93-3dc2-3f6d-abe0-7596c2d03b23 | -9.5177 | -47.2715 | 2025-11-15 00:18:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a582cd62-e04e-3366-9b0b-07a6bb68a450 | -11.8466 | -49.201698 | 2025-11-15 00:18:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8a5f08e-76f4-34f5-b728-6c644afa4ed8 | -2.4272 | -48.047798 | 2025-11-15 00:18:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7739ab8a-1d9a-3adf-b4fd-7bfe3703ed97 | -3.4548 | -50.1147 | 2025-11-15 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bea1061-d26d-366f-a32c-a1ae1c70deef | -5.4202 | -40.661098 | 2025-11-15 00:18:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cfc5a07e-1937-328e-b2ac-1680ce680319 | -2.7318 | -45.3078 | 2025-11-15 00:18:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 426568eb-baaf-3eed-824d-f2cfa9167a40 | -6.7324 | -42.961201 | 2025-11-15 00:18:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c0ca7652-7058-393d-8f60-b5a2c704d7e6 | -15.1289 | -43.6656 | 2025-11-15 00:18:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 41a386a6-a13f-3618-98f2-8d8aa058b84a | -7.3541 | -47.2883 | 2025-11-15 00:18:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 270c6bba-9b0f-3ca1-a6da-f9ab3390f25f | -4.0955 | -45.601101 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2092c2b1-95a0-3afc-a664-41078d610743 | -5.176 | -44.094898 | 2025-11-15 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d83ddd8-aabe-34c5-bc1a-288e18d4c742 | -5.5109 | -44.391899 | 2025-11-15 00:18:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11d7fe9e-f514-38bf-81d2-e89bb5131394 | -12.8322 | -46.435699 | 2025-11-15 00:18:00 | METOP-C | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c7356de-2b0e-3cb3-91bf-8c69b04f6e02 | -2.7383 | -45.290798 | 2025-11-15 00:18:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bade885a-0383-360b-94d4-4283a47ca99b | -2.5069 | -47.809898 | 2025-11-15 00:18:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8508b157-8472-3f3a-ad6d-4802e671d892 | -2.7301 | -45.300301 | 2025-11-15 00:18:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 67bb24c8-65d6-3b62-92e7-39ed53467ded | -6.0323 | -45.800999 | 2025-11-15 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a0f3c50-eda2-3c6c-92c8-003c7a624935 | -8.5792 | -46.0909 | 2025-11-15 00:18:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bbc621d-baff-3823-96db-5a383ae52c5b | -3.9934 | -47.6632 | 2025-11-15 00:18:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56907c3d-f42d-3e43-be2a-a12a1087263c | -4.5212 | -43.2094 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 198b155f-8da9-39db-9e72-7d00cb38fd5a | -10.7042 | -44.0704 | 2025-11-15 00:18:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a50c749-7613-3d90-b2bb-bc9f9da59c60 | -5.5074 | -40.547798 | 2025-11-15 00:18:00 | METOP-C | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 61cb79ec-2ea6-336f-9fa0-73a3fee0074f | -9.8591 | -44.7141 | 2025-11-15 00:18:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5f35a218-d7cd-3bc2-84c9-00d91a4e57b7 | -9.7472 | -43.969002 | 2025-11-15 00:18:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9c024d0e-b77d-37e1-b7ae-c3435b41a343 | -4.0519 | -46.412201 | 2025-11-15 00:18:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c4c0e33-f186-31af-9111-414abd86f16f | -3.6589 | -44.808899 | 2025-11-15 00:18:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0137e7a2-29cb-3653-942d-89fb3853c7e0 | -5.7495 | -42.718899 | 2025-11-15 00:18:00 | METOP-C | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 82157252-f1b7-33f8-b129-6a9ea6890e02 | -5.7511 | -42.7258 | 2025-11-15 00:18:00 | METOP-C | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0b89b000-256f-301e-95d5-6f9744631256 | -4.2134 | -45.484699 | 2025-11-15 00:18:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a4047b4-4e3e-35a6-83bb-193b1a599d56 | -6.6618 | -39.966 | 2025-11-15 00:18:00 | METOP-C | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ab110645-d838-3e22-b66b-bcad77a4dab1 | -3.2723 | -45.465302 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f4807d0-0282-3ed8-b6ee-75043aec4a4d | -6.8735 | -41.592602 | 2025-11-15 00:18:00 | METOP-C | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 248a1cf0-bd8a-31c1-a047-933ba1c99ac1 | -7.0942 | -39.081001 | 2025-11-15 00:18:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e81524f9-0df2-3b5d-8577-69ad331b62aa | -3.2233 | -45.476101 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ba56f1b-e6a2-3bd5-bde6-c28aeaaed836 | -13.2399 | -44.467602 | 2025-11-15 00:18:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
