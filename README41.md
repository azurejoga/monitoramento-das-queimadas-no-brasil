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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9ab560a-88d0-399f-b01d-344900a65112 | -3.25268 | -54.2373 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9fe9a825-805e-31da-926f-27daf5add1ca | -3.252 | -54.24138 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 696a6d98-e4a8-32d8-bc99-d00bd22b479d | -6.50287 | -47.04451 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 49cbb9eb-735b-37b8-a0e6-d1c7620f2216 | -3.24483 | -54.24893 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5f84dea-5fe4-3653-b6f1-9a81438e3f57 | -5.35854 | -49.61262 | 2024-11-23 04:18:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1decf85c-6f48-34d6-a96e-aea247e70adf | -3.4674 | -48.2528 | 2024-11-23 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 11abbf3e-7956-344d-b83a-a0a2e6160b19 | -3.96014 | -46.72906 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce146e9d-6639-362d-9309-628544552e9c | -4.54755 | -45.8732 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16c50ec7-d186-3aea-b140-bfdfae87a78c | -6.83248 | -39.29456 | 2024-11-23 04:18:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc0f884b-f396-3d25-9ed5-992802ca197a | -4.26233 | -48.70791 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cec9307-e253-3956-abed-d196b1a6116c | -2.57545 | -51.8888 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 830675e4-00aa-3882-8f7e-8f0c11f79f60 | -5.48619 | -46.25312 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a162106d-863d-3812-b618-cc1be9cb15e9 | -4.53848 | -42.91885 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 288304d8-0f32-341a-a1e9-32c4c677214c | -4.97647 | -49.82238 | 2024-11-23 04:18:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 171909c8-1aad-3b5f-9754-e5884d29700f | -6.63174 | -47.34881 | 2024-11-23 04:18:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ea32811-e414-3e6a-a859-15678f4aeee8 | -4.36961 | -48.56698 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8123e8e5-485c-3b39-8e37-40a3fef9da82 | -4.38825 | -45.90107 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17fc99e5-02a2-31c9-99a1-8171f460b339 | -3.46432 | -48.24739 | 2024-11-23 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5f2c40f2-cc68-3371-9df0-ae4b9393a310 | -4.96422 | -49.99706 | 2024-11-23 04:18:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e99f196-82d8-3df3-937c-0fe808a68f82 | -4.72306 | -45.49985 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 398221d1-4088-3323-b282-d984a097894f | -5.48797 | -46.41689 | 2024-11-23 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b04ff7fa-c9a1-326d-b65d-a96f1c44d9f6 | -5.45164 | -48.9348 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3d5a757-c74c-30b6-b304-02a198ab2d98 | -3.41929 | -49.23099 | 2024-11-23 04:18:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d2429d7-aee9-315e-b496-4a8b61d155ae | -4.69847 | -45.84872 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 89da31d0-06ef-3bf4-b3c6-ef3b0352746d | -3.75331 | -50.01205 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f0e1b99-f443-3c3d-a2ec-315e484b8e58 | -7.21135 | -47.06055 | 2024-11-23 04:18:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c983fc0-a446-36c5-9703-608c4a6a9fe6 | -6.23332 | -39.62955 | 2024-11-23 04:18:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 98c09ca7-9ac4-3a64-aa7b-3267c7737698 | -3.992 | -43.71798 | 2024-11-23 04:18:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcbbdcd9-ae8d-3630-b5d8-e2de15b7f6a1 | -6.05705 | -44.0449 | 2024-11-23 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0eda6604-6b36-372d-8e9a-cb0bffb0d0cc | -4.37531 | -46.02675 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a87a5e91-20b2-3db3-b179-5c6057498e25 | -5.74616 | -46.271 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 759b04b7-05b8-3477-b495-1d9b719dde40 | -4.70186 | -45.84922 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fc347e34-2d4d-3f9c-9929-778706765e7e | -3.80628 | -51.99635 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7325f452-7415-3c0c-9d65-c3ddb7869f6a | -9.72508 | -37.03141 | 2024-11-23 04:18:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d63357b7-e94e-3ece-a0f8-6d7eeafa991b | -6.95504 | -46.29702 | 2024-11-23 04:18:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3afc3837-4525-3540-b1eb-08fa736e1fc4 | -3.24415 | -54.25308 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| caefd635-c228-3de4-946a-ab1ec0fb2fe9 | -3.7477 | -50.01962 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15aaff7f-b7ef-3d9d-9c13-277f5077081d | -7.01158 | -39.22809 | 2024-11-23 04:18:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33ebecb9-368d-3364-8576-cb7c0e5886da | -6.49877 | -47.04781 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e584febe-16db-3821-a427-61e73ccb854b | -3.24114 | -54.23551 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3413b04e-e3b6-38c0-86a5-c68bc5e6f6de | -4.53568 | -42.91477 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 41a1075f-c51a-336b-bbe8-56d43c1e952a | -4.61211 | -46.50064 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ec2c4863-e37c-3afd-b1a9-4e6b004ba75d | -3.24982 | -54.22453 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ab13857-e198-3717-8ba7-06d1ea2956cf | -3.90827 | -46.53373 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e769f0b5-41f2-300c-bd42-8d0968ef4862 | -7.50739 | -47.02935 | 2024-11-23 04:18:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a9bf5f65-f3ae-3d7c-aa1d-b367ffaa7252 | -5.27936 | -45.18723 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1574b238-d506-3c5d-81e6-0012b96382d5 | -4.40879 | -44.11486 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82fe18f9-a9c8-3816-b5e2-6721e9e348c4 | -3.24045 | -54.23962 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2af651d3-3629-324e-a7b0-3eaf9f70b28f | -3.25132 | -54.24554 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dc0e935a-030a-3276-bac0-47bc0cec80d3 | -4.64613 | -46.42038 | 2024-11-23 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7daecab8-4fee-3000-89ea-d091643361ee | -6.25265 | -42.14068 | 2024-11-23 04:18:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c0f3154b-7c24-3791-99fe-b61ee4b385b2 | -3.20241 | -54.25444 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6d50012-b707-3361-a98d-6175b0f3029b | -5.74674 | -46.26733 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be5f9938-fee2-3ab8-9760-7294d3652dcb | -3.77677 | -45.20984 | 2024-11-23 04:18:00 | NOAA-20 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04fbed45-cc32-3c3b-b281-a4fadf3221b4 | -6.04652 | -44.82529 | 2024-11-23 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a34eefa9-3871-3e3f-b68b-75a4a0fd1f64 | -3.58267 | -46.20679 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 50f02d9d-1db0-3113-bdd3-e73e4c3a2cb2 | -5.58579 | -45.20378 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 73d3a60a-f83d-3201-a0f8-ac664d268fef | -3.11511 | -53.11431 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4adb972b-9bff-3bfb-9687-1226eb86308a | -3.74169 | -45.58107 | 2024-11-23 04:18:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1927c900-61ae-33bf-afa2-dd08ffcd190a | -6.03648 | -42.22812 | 2024-11-23 04:18:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 95e7d747-5589-37c1-8ea7-9be39d13cf3c | -4.09033 | -46.84265 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f860ea4f-71c4-357d-8a80-29fcc7dfe1cb | -6.25418 | -43.56381 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 515beb70-5a14-3bea-9b1c-fc12ffc36f4a | -4.52207 | -43.65201 | 2024-11-23 04:18:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fad8d73b-0c04-361b-adf5-76d30f29607c | -5.4896 | -46.25364 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 178d3e2e-81b9-3748-b099-e8a9301e8d5e | -6.03242 | -42.23143 | 2024-11-23 04:18:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a0c712a3-47b7-360c-807a-a12d3b38951d | -6.1514 | -46.67306 | 2024-11-23 04:18:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1cf5aff-ce8a-346f-b461-54e543b7de4e | -9.73013 | -37.03204 | 2024-11-23 04:18:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5c2dec90-11f7-303b-b9a9-7470dfc7c5e6 | -3.97558 | -49.01451 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c589ace9-ea39-320b-9a0e-7ebd777fb8dc | -3.80719 | -51.99085 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e92f276-b4c5-3a93-93f1-e6d3221e6930 | -5.45138 | -48.93227 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f9d969d-031f-3bd9-a24f-837384360c5c | -3.00148 | -51.54988 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 911365b0-8e8d-3a8d-aeff-4014477c39fc | -3.11734 | -53.11803 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d18fd004-cd59-3a7d-8de4-f84f23ae29e5 | -3.67319 | -51.73647 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 990853c1-cb39-36d8-bc68-1c57ff5ae34a | -2.19447 | -53.65403 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f0a5add-bd8a-31a0-9f29-3aa90803f257 | -4.07543 | -48.96634 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1842614f-e881-32d0-ac78-d4c37326b145 | -4.90383 | -47.41747 | 2024-11-23 04:18:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b498843-bef1-3fd3-a0eb-f9bf85db3865 | -5.94119 | -46.19328 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ae998f1-5915-3a12-9ca1-cdb3166ce6ef | -7.5942 | -45.54471 | 2024-11-23 04:18:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aaae975e-dbe5-3792-a6e8-6d31acf2f697 | -3.05999 | -53.28102 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e6daf391-a4e8-37a0-94bc-87f5bb265a46 | -4.75333 | -45.78675 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 111d33ac-a1d5-3bbc-8fb1-6ea943711d5e | -2.7882 | -51.4139 | 2024-11-23 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 246dc455-67b0-3681-aa14-5e152840484f | -5.22948 | -45.11508 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f95f8e1-6616-3d02-84f6-7ba1a0b6250a | -3.84852 | -43.9386 | 2024-11-23 04:18:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b2c07aa5-3c92-3830-878c-3976930c957b | -3.85556 | -46.95081 | 2024-11-23 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c978c02d-b685-30d6-9eaa-06c5c45acc7b | -4.25922 | -48.70236 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5fc70a41-79c7-37ca-a0b5-c0342a4181fe | -4.09561 | -51.07333 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a4e3297b-6ebd-3ffe-9454-d1d368b09d70 | -2.73907 | -54.02888 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06a418b1-753a-3000-8b0c-d3ebd3c9a8f5 | -3.22704 | -53.93551 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d7dba46-2935-38d5-89b2-1df2c937504e | -5.74732 | -46.26367 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f021bc2-59d7-3eaa-b200-e82af52c5976 | -2.9579 | -53.72373 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b0bd7ab-3b97-3150-822c-d3dd11095928 | -3.24489 | -54.25303 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b87541a-c4c5-3fa5-a995-16e96f9b0248 | -2.87737 | -51.58805 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2d67291b-6b6a-35fd-b80e-c4e09f44518a | -3.23604 | -54.23056 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6da01c96-24e3-34ec-8af8-d0e57c2bd616 | -4.17654 | -48.64093 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f79e6137-1d0b-3e58-b807-8533382bbe4c | -3.12159 | -53.10831 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6caa788e-23fb-3de3-8e79-44d57dde4806 | -5.11461 | -45.83613 | 2024-11-23 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b5f1c383-d839-3330-b23d-da701f8581d5 | -3.24622 | -54.24056 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3663f08d-0ecd-37c7-8754-7a7660075df6 | -4.70325 | -43.6664 | 2024-11-23 04:18:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a255de9a-7aef-3d1c-9e82-8338b752f97a | -6.63948 | -41.44202 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea6f8c11-23a8-3455-b968-48e08483d24c | -3.80611 | -52.36661 | 2024-11-23 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README42.md)
