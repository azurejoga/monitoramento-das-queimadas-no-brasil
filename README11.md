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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aae92df2-7033-3b2e-a860-117a46d928ad | -4.03604 | -49.77041 | 2024-12-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc9ad1a9-f199-3f01-9acc-d70b83a6ec44 | -5.48685 | -45.86848 | 2024-12-19 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4634607c-c19f-3460-b988-01ca9a8897bb | -7.78636 | -34.99371 | 2024-12-19 04:29:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| df72953b-a741-3fce-a1b3-d1ccc35b47aa | -4.33313 | -48.2994 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df358ca7-03c1-3537-9be4-3b239baad5dc | -4.15879 | -48.62865 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9883faf6-7d08-334a-bed4-87c05c0b355d | -3.87212 | -46.58854 | 2024-12-19 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7fa27a2-b5f5-374a-a1b1-16cbb7344eca | -3.98856 | -44.17162 | 2024-12-19 04:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d440b9a2-d8f4-3f49-862f-09bb308482e6 | -7.79229 | -34.99195 | 2024-12-19 04:29:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fc242788-c0bf-38dd-b27a-d804aaf9f891 | -4.66963 | -43.2972 | 2024-12-19 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a94ccaeb-1860-3f2d-be57-2f945dbe84da | -5.91008 | -46.23268 | 2024-12-19 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d8861da-d03b-3a78-a8f2-773d16458aee | -7.42512 | -35.24015 | 2024-12-19 04:29:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 90b53069-8165-3e8d-9b17-aa37de635bcd | -2.51865 | -47.269 | 2024-12-19 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c545a12c-2534-33de-b302-300a51a0d77b | -3.22051 | -42.08248 | 2024-12-19 04:29:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc0fa28e-5f32-331c-8ace-3357597fb70d | -1.6909 | -54.01092 | 2024-12-19 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 369c1324-e82f-3862-aa33-1d234514501d | -5.39267 | -40.67231 | 2024-12-19 04:29:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b99c9443-8c4e-34c9-92b4-9fefa0790848 | -9.68217 | -36.19352 | 2024-12-19 04:29:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| e57f875d-55d7-3d5d-ac18-6b92db2c5bbc | -5.38816 | -40.67383 | 2024-12-19 04:29:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 10f5ddc1-fec3-3217-be6c-3216db89fab0 | -3.86657 | -46.5806 | 2024-12-19 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| be23ad38-00af-32c1-9f63-776db8014a4c | -3.6726 | -39.57677 | 2024-12-19 04:29:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dafc02fc-baec-35f8-923b-cdaf24ac676b | -5.82797 | -35.48629 | 2024-12-19 04:29:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc73dc9b-3d08-378f-ba1b-3805951d0048 | -3.22105 | -42.07896 | 2024-12-19 04:29:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 864f5eab-844e-38de-b1f7-0cb19bbc92f1 | -2.47381 | -47.20905 | 2024-12-19 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 588fbabe-b0b4-3475-8c9d-41c29e0759ea | -5.09043 | -44.18106 | 2024-12-19 04:29:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0ca44d8-3cd5-3d44-aa30-ee0deff8c0b4 | -4.5943 | -47.9784 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62d9574e-d01a-3262-8ea2-aeb8c9f824f3 | -1.26939 | -54.13591 | 2024-12-19 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44e68dce-c89f-3002-86b2-4a19e9dc22f9 | -5.20719 | -43.29927 | 2024-12-19 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6873fa94-dde7-3b7e-9734-e6bf9cc84160 | -5.84755 | -49.81984 | 2024-12-19 04:29:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b2837b5-d860-3010-8234-48b4920d3bb0 | -4.35252 | -48.19812 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bb7a301-8310-337f-946a-b7a87ec6b19f | -3.23175 | -45.49689 | 2024-12-19 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 83c186b0-6dc3-3397-ba83-1bf2a575079d | -6.11945 | -46.65839 | 2024-12-19 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c722051-1dff-350f-ae8e-2c1046097000 | -5.70873 | -41.41286 | 2024-12-19 04:29:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 54422693-44c5-3132-abfb-c8acc2d2aec7 | -4.09415 | -44.81942 | 2024-12-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cc0c8e6-b920-3e16-aa0d-b90ae23e6f64 | -1.56668 | -53.7811 | 2024-12-19 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3387ec01-f50c-3987-85d8-047a1d0cf521 | -7.58612 | -38.31929 | 2024-12-19 04:29:00 | NOAA-20 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 938de35e-5c78-3ff3-929f-3a08d16e98f9 | -9.67492 | -36.19862 | 2024-12-19 04:29:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| dfc2165c-4738-3d95-b1b4-8d47af6a917d | -3.95661 | -46.54834 | 2024-12-19 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c9daace-5788-3a2c-98eb-1bfdd66a55e8 | -9.70488 | -36.11659 | 2024-12-19 04:29:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 81d5e95e-1b2b-3085-b534-9092eb475c6b | -3.99769 | -45.59513 | 2024-12-19 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0622ef42-ac04-3c25-b759-b911594a935e | -3.86989 | -46.58111 | 2024-12-19 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 86600776-e5fa-35c6-933c-ccc33c860fad | -2.55613 | -46.88015 | 2024-12-19 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3b12fab-8bbb-36b5-9dc4-72902a1b67a6 | -4.47997 | -45.42406 | 2024-12-19 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4d1e3bc-207c-30e6-8286-8f86394abd5d | -4.88808 | -41.40541 | 2024-12-19 04:29:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 795d0e99-e038-33f7-8ffc-69ba583aa360 | -5.17507 | -37.59652 | 2024-12-19 04:29:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 99a0c648-459a-33ed-8741-231902b5b302 | -7.4223 | -35.23936 | 2024-12-19 04:29:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1fada0bd-22c1-3ee4-b55f-462794cc3f3e | -4.79945 | -44.03255 | 2024-12-19 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a9cc39e-6777-392d-ba90-976f56d46309 | -3.23456 | -45.50101 | 2024-12-19 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2395e0c-4d45-3168-8cc8-4b50190e459e | -4.12253 | -43.56503 | 2024-12-19 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40eccb2f-2dbe-3c3d-a148-94dc31a8bf9a | -3.67185 | -39.58183 | 2024-12-19 04:29:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 59976603-7a18-3e52-95f9-cf482c05b689 | -4.26319 | -48.56801 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9512d3c0-36de-3edd-bfe1-8a9895fdee73 | -9.6808 | -36.20469 | 2024-12-19 04:29:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 067fdfac-e461-3817-8811-25659159f905 | -7.09365 | -39.03503 | 2024-12-19 04:29:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f8db52d2-acfd-3282-9125-6bc99527ff13 | -3.22837 | -45.49637 | 2024-12-19 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2683f1f1-1ca4-3e82-b2b0-2f1907964fd4 | -4.15346 | -50.10141 | 2024-12-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07dacb68-b7cf-33f7-ac84-cd52e93cc02c | -2.64091 | -45.75703 | 2024-12-19 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91c1be05-9798-3c71-a065-1301616006d2 | -4.11576 | -43.22529 | 2024-12-19 04:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e90d3ab9-5fa1-3603-a7ea-544713cc81b0 | -4.35221 | -48.47587 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 400c9b5a-0e62-378c-9bde-f20086b9cbe1 | -5.17615 | -37.58901 | 2024-12-19 04:29:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c699011f-ce8f-3043-b247-748802c8eb93 | -3.8749 | -46.59253 | 2024-12-19 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80afa517-7051-3f68-86b2-f46e572572c4 | -4.04017 | -49.76709 | 2024-12-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61d66b82-ced5-3dba-8590-8e68cadb353f | -2.44291 | -47.4908 | 2024-12-19 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5497fdc-ba75-3ae8-b350-dfad73b4d34d | -4.88379 | -41.40471 | 2024-12-19 04:29:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30f9707f-ab3f-3578-b4b1-a776fa89c027 | -7.42439 | -35.24593 | 2024-12-19 04:29:00 | NOAA-20 | CAMUTANGA | PERNAMBUCO | Brasil | 2603603 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1bc77937-6727-38c7-99e3-de3a26584e3f | -3.50149 | -53.9578 | 2024-12-19 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3d656b1-e7e2-3e87-b058-a846b558ce8d | -3.68319 | -49.57322 | 2024-12-19 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aca08bef-ca8c-3c6e-ab9b-14c54b194418 | -3.2197 | -45.4949 | 2024-12-19 04:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a8ad7187-bf49-3c94-8177-9649d3d33cb1 | -5.211 | -43.2833 | 2024-12-19 04:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| cb5f48d2-ac88-39fe-a118-0eb94acc620b | -3.2383 | -45.4941 | 2024-12-19 04:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 36b606ec-e5c2-3857-8288-9dad54223885 | -5.2108 | -43.3067 | 2024-12-19 04:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 1322c34b-df1e-3cac-aaba-844163704f0c | -12.23473 | -54.31199 | 2024-12-19 04:31:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acf482c5-93e7-32e7-9a45-4b5799922a12 | -10.50221 | -49.12987 | 2024-12-19 04:31:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa8476cb-0602-3575-b034-1b6727f4b6f9 | -10.50664 | -49.12338 | 2024-12-19 04:31:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cb518f3-b699-34ab-aac7-1e6574340297 | -13.92168 | -54.611 | 2024-12-19 04:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8bc4c41a-30c2-3d5f-85c6-3cea9a634f6b | -13.3716 | -54.25184 | 2024-12-19 04:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0207c07e-ded7-3e29-a5db-c649df230572 | -12.90971 | -55.04738 | 2024-12-19 04:31:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1989a81f-216e-3f1d-beb9-775ce2949645 | -13.36763 | -54.25114 | 2024-12-19 04:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 414d6a25-f0f0-3926-80b1-4f6fc01e72b9 | -10.50276 | -49.12636 | 2024-12-19 04:31:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 143ed6df-93c6-397b-b6c5-ec4a70295c07 | -13.48473 | -52.95032 | 2024-12-19 04:31:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2e846c2-6322-3ffa-8531-ecbf9d5ca7a6 | -12.22196 | -54.3133 | 2024-12-19 04:31:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 92c909ce-b05c-3308-8254-655740a53a67 | -12.90551 | -55.04663 | 2024-12-19 04:31:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96831839-11f7-334b-ae70-61b1fc7ffd21 | -10.19943 | -42.05412 | 2024-12-19 04:31:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 161e70ee-ae01-3408-87eb-49905d25dcd2 | -12.23069 | -54.31118 | 2024-12-19 04:31:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4deaeeac-75b9-3484-9700-827066424d2c | -11.85646 | -43.83065 | 2024-12-19 04:31:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95cd0e5f-88a6-313f-b77c-40da7cc28655 | -12.23005 | -54.31483 | 2024-12-19 04:31:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1e0cbfcd-9b82-311e-93e1-b91c1a0e80f1 | -11.85695 | -43.82703 | 2024-12-19 04:31:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4aa889ba-0f24-3dcc-8069-b9528cdf9034 | -13.92229 | -54.60749 | 2024-12-19 04:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 88f3174b-e802-3ec7-9ce2-dc5f319d3de8 | -12.55895 | -57.83277 | 2024-12-19 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5598ddb1-63e6-371f-948d-130f2120bed9 | -10.50608 | -49.12689 | 2024-12-19 04:31:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee077a82-f21d-32e6-91cb-e2976f93c1d6 | -13.92105 | -54.61456 | 2024-12-19 04:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3967655a-7251-3728-bc94-2765c4b49574 | -12.22601 | -54.31407 | 2024-12-19 04:31:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e08e097f-e62d-3f46-8e35-d5c99d2df5b5 | -12.78202 | -54.21965 | 2024-12-19 04:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7056ff7f-60ce-3bac-8505-1eb35fca72db | -12.78602 | -54.22034 | 2024-12-19 04:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b81e7a35-bfc7-3b2a-b9aa-195c4d995b33 | -13.4884 | -52.95099 | 2024-12-19 04:31:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d939d3a0-aa44-34f7-9b40-278cc13a0001 | -12.2109 | -54.87054 | 2024-12-19 04:31:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b77e90e3-3174-3110-88c1-dd6e21630d41 | -10.50332 | -49.12285 | 2024-12-19 04:31:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5f21434-d385-39f8-8a8e-673774eb860a | -12.55954 | -57.82965 | 2024-12-19 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfc3d212-0c5c-3501-ad58-0cf954792ff5 | -11.86051 | -43.83123 | 2024-12-19 04:31:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef71740f-b1ff-3ad2-aca8-34f59cf8d36e | -16.50903 | -52.44176 | 2024-12-19 04:33:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f14f7db3-215f-3024-989b-5e526b3ce42d | -17.97278 | -54.00443 | 2024-12-19 04:33:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0657767e-6595-3de7-9d0e-72a70fd6319c | -20.0492 | -54.9009 | 2024-12-19 04:33:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3df3cf8-269e-3f2c-aa25-5dbe1f01f67a | -19.12204 | -53.46062 | 2024-12-19 04:33:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README12.md)
