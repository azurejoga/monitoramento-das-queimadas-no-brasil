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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06ee21c2-149e-3a94-bcbc-78f34ffc528b | -5.94935 | -44.46643 | 2024-11-23 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 77a2b793-98f9-3303-a508-bc49f2a21bf9 | -5.57435 | -46.28832 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be2f9125-2b2f-3942-9a25-94a977439cd5 | -6.6396 | -41.44219 | 2024-11-23 03:55:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e498fc0-d562-34c9-a6d4-3f4f83d7c2f7 | -4.60848 | -46.49971 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| d40e75bd-983d-396d-a00e-b402699e7c23 | -3.67719 | -47.13815 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0c2d11c-f3aa-3d59-b0d9-55eac59394b1 | -3.89362 | -46.66228 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f972db67-49ba-31cc-ac3c-b5a5ee505788 | -5.97175 | -46.30425 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed769175-9b57-3673-8339-23d375146bcd | -6.35001 | -39.79399 | 2024-11-23 03:55:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0f1673cc-55a3-3d84-a714-0fac2310c471 | -4.2626 | -44.69798 | 2024-11-23 03:55:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dff650c9-eb54-35d8-b2b0-f6a6b1cf4472 | -4.47899 | -45.65633 | 2024-11-23 03:55:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 259e65e7-2dbe-32bc-a551-e8aee668198d | -4.47406 | -45.65561 | 2024-11-23 03:55:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9f0f429-826d-384d-b7c8-eb711b2e7150 | -5.47566 | -39.64892 | 2024-11-23 03:55:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e693274-377e-3a6f-9ff3-19556c7083ea | -4.60274 | -46.50208 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 29b87c73-d902-3708-970f-bb58f938da9f | -6.09887 | -41.80241 | 2024-11-23 03:55:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0c7088df-1357-3d3b-86bb-f2129edcc3b9 | -5.44509 | -45.58506 | 2024-11-23 03:55:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47c462ca-d463-39a8-b4be-7254f8e7d95a | -3.67168 | -47.13728 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a6c57b9-fd25-3922-87de-7a42d26551b8 | -5.4336 | -45.33901 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28169621-958e-3d93-ad31-b8f975b56594 | -4.53283 | -42.91964 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76106fa5-722a-3b8c-a232-4288c7329878 | -11.77974 | -44.63137 | 2024-11-23 03:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b84bc78-7adf-3185-9983-5ae27188eb57 | -3.54927 | -50.51677 | 2024-11-23 03:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30ab1553-8548-339c-805b-604151a6b71c | -3.54219 | -50.51341 | 2024-11-23 03:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a7b1819b-2a58-36f0-9743-fef805b81d4b | -4.34738 | -45.8856 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9dece93-81f8-3b3c-bc06-5e6cd0a5f2cf | -4.12795 | -43.22946 | 2024-11-23 03:55:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7719aa8f-e5f1-36aa-942a-811489c2c747 | -3.77667 | -45.20846 | 2024-11-23 03:55:00 | NPP-375D | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c1c8859-1a3a-37e5-9add-61c4a982bf17 | -4.12251 | -43.23632 | 2024-11-23 03:55:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7c9cb8f-437d-3764-ab3f-f6ac77a999c2 | -6.06057 | -44.04621 | 2024-11-23 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 73be2c28-a7f6-3c1f-8fd4-2d52826a6e56 | -4.70861 | -45.81105 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73cbf51c-8c79-3813-bc16-a1a49e8ff3d9 | -3.67106 | -47.14086 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b1d52d1-8d56-3ae7-a43e-74219d5b75a4 | -5.15597 | -45.38841 | 2024-11-23 03:55:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71428fad-1c51-3eb1-8780-4a96f91fc5e3 | -5.22384 | -44.91135 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b033a4d7-6bc7-310f-be1c-e1f3794a4d8b | -4.41902 | -49.69145 | 2024-11-23 03:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49973e0d-9b31-3741-9e87-e8aa1087b3eb | -4.90802 | -47.85665 | 2024-11-23 03:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5bb0b6a-c98b-3081-8028-c392e57f90ea | -3.7783 | -45.20747 | 2024-11-23 03:55:00 | NPP-375D | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d108cc6-79fc-3a12-bd94-3c2d619cb9aa | -6.16219 | -44.42675 | 2024-11-23 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a081fb78-90ba-3ffe-afb1-d5ebe2ccc99d | -3.4653 | -48.24422 | 2024-11-23 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2c7be14-3fc7-3ea3-ae85-dd2a50fc397f | -4.90739 | -47.86032 | 2024-11-23 03:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8516dc50-9371-31d5-aeee-56cc3c279e04 | -5.74755 | -46.26835 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a1338b5-5ab6-309b-bc68-1978236191eb | -3.96546 | -46.64537 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2d8d14d5-4d52-312c-9091-d4d5f51937bb | -4.59257 | -46.07598 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae942761-7ba1-3d4b-ba8a-a659388758e8 | -5.75201 | -46.26464 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 103527f2-c87d-33d9-a788-9b6a990cd60e | -5.747 | -46.2638 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5888c9c3-d188-3a23-87d3-6c74c9df1ced | -3.46654 | -48.25278 | 2024-11-23 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 38df0103-2b44-3ae5-bf6f-5f8af4a34d18 | -3.89307 | -46.6655 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2c116e9-ba89-3957-bf81-0bec86c1a2e3 | -5.94995 | -39.67507 | 2024-11-23 03:55:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a279bd49-9348-34ff-b490-298d85e29096 | -4.02424 | -48.87117 | 2024-11-23 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b33afe5-b81f-37ad-8c8c-14159ec0329e | -5.13054 | -41.56084 | 2024-11-23 03:55:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b739a38f-6a6b-30db-a40a-1a5fa33d86fc | -3.68704 | -50.11957 | 2024-11-23 03:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8cc60290-3cea-34d3-ab06-ed1a021ec3d6 | -5.56986 | -46.28433 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80f2c0d6-a178-3041-ba4c-1177874919c8 | -5.27728 | -45.18896 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58d7100b-88b1-39ec-9e4e-bfcd3648e109 | -4.72747 | -45.49176 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67d87a71-fe85-3708-9a08-cd26d2733c4b | -3.70815 | -47.61468 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12bf82ef-e24f-33ce-93ae-662179f01b54 | -5.746 | -46.26949 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 414f5493-bbe5-3937-9b1a-4b4f0c268a0f | -3.66358 | -51.57952 | 2024-11-23 03:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83c367e4-f4b2-3dd5-acf3-68e63a311f80 | -3.68519 | -50.11499 | 2024-11-23 03:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1b1b986f-e3fa-39fb-ba67-5c42ac8426e3 | -5.94549 | -39.65937 | 2024-11-23 03:55:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2cf0ed1-e31d-31b6-8428-57bb6e0ba912 | -6.83239 | -39.29318 | 2024-11-23 03:55:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 312c9366-9e12-3694-ab1e-f1447924c68e | -4.74401 | -49.09901 | 2024-11-23 03:55:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93a8c330-5563-330a-8821-cdbeba350fce | -3.89695 | -47.93279 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 04bd00ae-8608-3c7c-a0ea-430ab3b21930 | -4.52876 | -42.91893 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16019de4-c5f9-3492-9892-937114f483a4 | -4.09025 | -47.02975 | 2024-11-23 03:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 047238b5-a262-3a76-bdf0-8d692413a4af | -5.1036 | -43.16073 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0a5572e7-9adc-3235-a107-87d09723c35f | -5.74799 | -46.25818 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6e98d07-6577-3a52-a708-723b4b141837 | -5.66408 | -47.34021 | 2024-11-23 03:55:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48a8fc33-d2d8-3a1f-88c0-b6de9e9475e5 | -4.42097 | -44.11275 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dd34e35-a741-35d4-8608-a58917297e22 | -4.15349 | -44.28461 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b408ae0-1723-3372-a917-fab3400a8ee0 | -4.41949 | -44.1216 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2d906bde-13d2-34c2-8bb3-a24a28a7c4e2 | -4.48307 | -48.11878 | 2024-11-23 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 302fc6a9-2952-3a82-bd24-5dfb2efc2c3c | -4.69114 | -44.40551 | 2024-11-23 03:55:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4d04fc7a-6e0f-3e22-b61d-4d4f41a13ed5 | -6.64027 | -41.43806 | 2024-11-23 03:55:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a21e94fd-c0dc-35a8-9319-90ed708e3a27 | -6.77633 | -39.51392 | 2024-11-23 03:55:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d722d0fd-7478-31f8-a458-0af152f90766 | -4.51066 | -44.55654 | 2024-11-23 03:55:00 | NPP-375D | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b68aa85-4462-3b76-b9f0-7182af4336a5 | -4.89916 | -47.41619 | 2024-11-23 03:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 546d1f57-d186-3a0d-b4f5-48ee53c029fd | -3.95059 | -46.8918 | 2024-11-23 03:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 51ef2736-0228-349e-80f1-a21ff04cb74e | -5.04253 | -37.77484 | 2024-11-23 03:55:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e970797b-50cc-35b6-9b01-89e4038a11e2 | -3.96725 | -46.64579 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ceeca659-e0b0-3368-8562-0393a790960b | -6.00328 | -44.62753 | 2024-11-23 03:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e11ada9-9cd8-36ea-a29b-aa657751951c | -6.50603 | -41.48629 | 2024-11-23 03:55:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 12acb1c4-7c35-331c-bb1a-cf74e1a532b8 | -11.90847 | -44.17944 | 2024-11-23 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01028c9d-74e3-3a44-86e4-298a051049ac | -3.94439 | -47.96634 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 16d73c0e-1f1c-317b-ad5b-459c8b2837ef | -4.41811 | -49.6966 | 2024-11-23 03:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0db04dfb-48d1-3c6b-8b12-c14bfcf7f768 | -3.68799 | -50.11399 | 2024-11-23 03:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb958099-9688-3c66-a475-6bc0c9361545 | -3.46461 | -48.24833 | 2024-11-23 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80971d2d-258b-3191-b32e-259819ecfbf5 | -5.66255 | -47.33669 | 2024-11-23 03:55:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f079bec-200e-3e8e-ba65-c2852b4256cf | -4.03201 | -46.19789 | 2024-11-23 03:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc2f79c3-257c-3015-9856-c1ca2a4e33ab | -6.03644 | -42.2263 | 2024-11-23 03:55:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1c1fb60a-6f7a-3170-80cc-7ccda07927fd | -5.44154 | -46.58921 | 2024-11-23 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae361d84-c89c-36f8-8ba1-bc248c9b7a21 | -3.90208 | -47.93752 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a7ed9783-d1cd-3be4-9963-e9608e9403d1 | -4.60947 | -46.49377 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 07b269b8-49e0-3e25-8dbd-b021ad08aed8 | -4.20037 | -46.81445 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c368f40c-8d5e-3e9e-a72b-0584b2848db3 | -4.60695 | -46.50877 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 998ed235-eff5-3a5c-ad7d-b27fb5382016 | -5.12877 | -47.03397 | 2024-11-23 03:55:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c8e9c37-1fff-3af8-a0ad-8b68f59deff7 | -7.01689 | -39.22107 | 2024-11-23 03:55:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e568d772-caf5-38e4-ac53-0db34597965c | -3.97159 | -46.65254 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc3a4704-13fe-3ef8-b44d-162e15f44a7f | -3.46796 | -48.24459 | 2024-11-23 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56c0ec96-e9d8-3d6e-a4f0-d766efb34127 | -4.35086 | -46.01804 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31ba1a8a-ece9-3fdd-be39-53d9014defb8 | -6.83234 | -38.56821 | 2024-11-23 03:55:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ce03e07d-175a-3bfe-949e-0d5a8f645f70 | -4.70195 | -45.85067 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a458b4c4-7609-385a-86ba-3d3e53dd3912 | -4.6132 | -46.50335 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 3a3bc10b-8445-3476-96c3-bc749b4b74a4 | -4.70596 | -45.85712 | 2024-11-23 03:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c1e422d7-bb2f-35dc-a7cd-82707153c322 | -4.67519 | -45.66812 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README25.md)
