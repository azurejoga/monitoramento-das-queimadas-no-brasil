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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4c6595b-cafe-3ec6-8178-d8f0700020a8 | -13.1932 | -47.8288 | 2025-10-02 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 84d2679a-774c-362e-ac96-78470aeeda31 | -7.6144 | -46.5966 | 2025-10-02 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| ba64d2a1-ff9a-389e-b583-7a623225f3c6 | -13.1739 | -47.8317 | 2025-10-02 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0312afce-3e74-3d32-acc4-d787c0d1085e | -6.6978 | -42.8118 | 2025-10-02 13:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 125.1 |
| db4dffbf-5b29-39ae-8e18-0396d3ad2400 | -14.3179 | -41.3645 | 2025-10-02 13:40:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 112.9 |
| 9c604120-97c1-3158-8446-d894e476d700 | -10.1837 | -50.3128 | 2025-10-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 1c6aaa2e-1aec-32d6-8ac4-2a5348664eb8 | -9.4083 | -47.5742 | 2025-10-02 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 090d8c41-40df-331b-8ce6-51ba8fbe3bcd | -18.2171 | -53.3392 | 2025-10-02 13:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 245.4 |
| de13a69b-e9f8-3841-a8d7-fd735b3a17a9 | -9.8331 | -48.276 | 2025-10-02 13:40:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 57978c74-1722-3db9-913e-6211740c5b6d | -10.1462 | -50.2952 | 2025-10-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| d23620f5-035a-32c8-8e13-fc119cfa3515 | -18.2375 | -53.3145 | 2025-10-02 13:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 0dee166a-f862-3eb0-9afc-f9ad327731d5 | -14.5937 | -48.3281 | 2025-10-02 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 159fee5a-1b1e-3567-9e87-37eb00da5404 | -8.5013 | -47.8404 | 2025-10-02 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8a4d5d4b-6626-312d-a350-cb755049941e | -13.1542 | -47.8568 | 2025-10-02 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 11c19df6-c34f-3da1-83c8-68e3fefe44fd | -8.8929 | -46.6072 | 2025-10-02 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 1019ee13-1e85-3c01-9048-b67c21339352 | -11.8238 | -45.0132 | 2025-10-02 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 288e7d54-15ee-354c-afb9-149a87f145af | -13.9585 | -48.1376 | 2025-10-02 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 1d466cd7-fc84-30de-b58d-f7ce735a059b | -8.5204 | -47.8167 | 2025-10-02 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| c482fe12-7113-37a1-b880-cb2f5e1b7c6e | -14.615 | -48.2355 | 2025-10-02 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 7b10cf12-a351-3762-a8c2-ad63dec59b0a | -8.527 | -47.2658 | 2025-10-02 13:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| dff1849c-ede4-39c6-b719-4bb87b7b5744 | -13.3001 | -47.2529 | 2025-10-02 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| bc17bdf7-a293-3252-92bc-d3f10d7c5186 | -7.8692 | -47.3048 | 2025-10-02 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e28e2e90-a396-3f32-9ff2-bf56444d3539 | -8.1702 | -44.1377 | 2025-10-02 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| fd04cd3b-ac1e-3a72-8218-6306ae4f86da | -6.7814 | -45.5929 | 2025-10-02 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 4f78852d-c60f-3286-8ddb-a4504663095f | -5.9858 | -44.589 | 2025-10-02 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 364ce6a4-c533-3884-8f19-89a50850cde4 | -10.8421 | -46.6514 | 2025-10-02 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| f3a8ab7b-0f4f-3c38-8399-fae32021db69 | -6.7626 | -45.5944 | 2025-10-02 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 570f9d92-ce76-3088-8756-98f381f1feed | -6.6602 | -42.8153 | 2025-10-02 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 2728f9d6-f7bc-3bd4-8338-122997a48d08 | -12.719 | -48.5832 | 2025-10-02 13:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 67bd5cc5-838a-3524-bea4-ed988e5acefb | -13.7864 | -48.0524 | 2025-10-02 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 146.4 |
| a4ba01f2-1a58-3efc-a6b4-aff91ec848b1 | -9.9182 | -43.7212 | 2025-10-02 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 170.2 |
| 746139e3-1ff9-35dd-b280-206e304eff5a | -6.4945 | -44.2962 | 2025-10-02 13:50:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| c75847ad-a13f-3232-90c0-82b3bb3f17b0 | -14.5937 | -48.3281 | 2025-10-02 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4b284b53-4a4f-327d-81c8-6d01b73b7253 | -9.4083 | -47.5742 | 2025-10-02 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 65e54bef-d333-3eff-8e6f-3b63884b44b6 | -9.9372 | -43.7187 | 2025-10-02 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 195.9 |
| 7466a1cd-6aa9-33f0-a5dc-68727644034d | -7.8882 | -47.281 | 2025-10-02 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 21c2b33c-e08c-34f1-b227-92a305ab506f | -8.6534 | -47.6943 | 2025-10-02 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ea33419c-805d-3ace-be99-9e45adb6b0ae | -5.6236 | -43.23 | 2025-10-02 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 84d885b4-ab5d-3b2c-a9fc-192e21428597 | -9.4086 | -47.5521 | 2025-10-02 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| b710b2c3-c86d-3997-8eeb-75973796e934 | -11.8242 | -44.9901 | 2025-10-02 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 0a3bd687-d7b6-3a5d-8d01-e9a21e0da359 | -11.8489 | -48.0151 | 2025-10-02 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 3e10a11f-1fc9-3b54-b076-7cad6b4b87a6 | -6.7814 | -45.5929 | 2025-10-02 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 1deae62d-cc27-3f7a-b11f-659aa390eae0 | -13.155 | -47.8121 | 2025-10-02 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 477ca6e8-765c-35cf-a0c5-99071cadd508 | -15.5379 | -45.2375 | 2025-10-02 13:50:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 151.7 |
| c1d042ce-0712-387b-ac2c-27f2bbab54b3 | -8.8932 | -46.5848 | 2025-10-02 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 21f2c32c-4df7-3de3-8e5b-a249d0bd5400 | -13.1743 | -47.8093 | 2025-10-02 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| f9bc1e90-0382-3157-809c-37355be44971 | -11.6059 | -50.159 | 2025-10-02 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| aeaddb50-6187-3a1e-be01-41f607108975 | -13.7876 | -51.1974 | 2025-10-02 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 7242fea2-9302-3cd8-8b39-cbc4fba7fdb1 | -11.8238 | -45.0132 | 2025-10-02 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 6ea63fed-d4d4-351d-9e1b-bb2bb8bdc71c | -6.679 | -42.8136 | 2025-10-02 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 117.9 |
| 3fda48eb-3d2e-36cb-b6f2-64dbec94fdd4 | -9.8896 | -46.9226 | 2025-10-02 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 60746dc1-7f31-380b-b505-23a762f8d070 | -9.336 | -45.9305 | 2025-10-02 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 239.1 |
| 26dd9327-8be1-3011-afe2-d73dfc6ee134 | -12.6998 | -48.5858 | 2025-10-02 13:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 2c2f238d-b8c5-3e33-8355-54fecaf958a8 | -14.7043 | -49.616 | 2025-10-02 13:50:00 | GOES-19 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 154.4 |
| d49f6ce5-67a1-3908-94e5-9ff08430905f | -14.3309 | -45.9933 | 2025-10-02 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 134.2 |
| b5f9e800-54df-3bb8-b959-bcd92ac68ee9 | -9.9376 | -43.6953 | 2025-10-02 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 0e2fb9ca-d2db-3514-88c2-768cc6e1c1b6 | -13.9779 | -48.1346 | 2025-10-02 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| d1ba149b-abe8-3f6b-b938-2cb5bb919f04 | -14.1917 | -46.1552 | 2025-10-02 13:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 235.8 |
| 29f83b7c-f198-34b8-aaa9-9596afcdd7df | -13.1735 | -47.854 | 2025-10-02 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8fc91545-c2ea-3e36-acaf-f206738dc356 | -14.425 | -46.1381 | 2025-10-02 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 186.7 |
| f494ca5d-3ccc-3f48-944d-5428d88121de | -8.1702 | -44.1377 | 2025-10-02 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 233.5 |
| 9b87d786-81a6-3cf0-b1bc-c4b842bdf554 | -10.9748 | -46.6794 | 2025-10-02 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 418f64e4-ad5b-3ad7-8ab0-af094830cfc4 | -11.8101 | -51.7957 | 2025-10-02 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 88c4d90d-6c72-37b0-9ba0-f32b4c815303 | -9.3199 | -45.7288 | 2025-10-02 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| cdef2564-e4cc-3728-956c-7b3153646702 | -13.1538 | -47.8792 | 2025-10-02 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| db1d79f5-d282-3ffd-be1c-c1b0eaeaf077 | -11.5869 | -50.1612 | 2025-10-02 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 77a8a6a6-09b3-30fb-9cd5-d62852037c31 | -13.3089 | -47.8118 | 2025-10-02 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 7ef4ea2f-5242-3f66-ae8a-ce8a405a027f | -16.0567 | -45.7204 | 2025-10-02 13:50:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 8626c31c-bf57-351a-83d4-8c9ff5b6d955 | -7.7944 | -42.5132 | 2025-10-02 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 236.4 |
| 232bff26-eeb0-3e97-be23-8dc6e7a5b576 | -14.4065 | -46.0953 | 2025-10-02 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 126.5 |
| c2d0f201-7ef4-3642-b6e5-1b43b969c6a3 | -10.937 | -46.6618 | 2025-10-02 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 1f3cf009-4c25-34a1-9f80-ce564ef6e3f3 | -15.3269 | -45.0439 | 2025-10-02 13:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 9e6589fc-cc34-3e51-936e-e84ce9cecfb3 | -14.615 | -48.2355 | 2025-10-02 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 3d9bc838-494a-3132-ae02-d4023618a19d | -13.1739 | -47.8317 | 2025-10-02 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ca54a9b2-0e91-3126-9716-21172e110010 | -6.6978 | -42.8118 | 2025-10-02 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 137.3 |
| 9d084216-0a21-33f0-9800-3f8263a07f9b | -14.5743 | -48.3312 | 2025-10-02 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 650cc240-24a9-348d-b7a9-a5a77d14bbdc | -11.8485 | -48.0373 | 2025-10-02 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 6fba99e7-9ec3-3895-820e-a353e6afe6ab | -8.9115 | -46.6276 | 2025-10-02 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| b87f8bf4-9236-3362-962a-ea4444425f5f | -6.7656 | -45.3004 | 2025-10-02 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 663d3715-1ce5-3649-8133-559c75fa8330 | -12.9851 | -44.5983 | 2025-10-02 13:50:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| c4720c25-f59c-361d-b8a2-a82ce0360bc1 | -10.8237 | -46.6088 | 2025-10-02 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 4aadadc9-a571-3e96-8dff-4381809a0930 | -16.023 | -50.8553 | 2025-10-02 13:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8dd3d9e1-b79f-338c-9d3f-b6fb1c561f13 | -7.8879 | -47.3031 | 2025-10-02 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 63ef3591-1f48-35c7-944a-bb12b0a2abe5 | -6.6604 | -42.7917 | 2025-10-02 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| d44f6553-db41-3f48-ab2a-89cb753ee588 | -9.3364 | -45.9079 | 2025-10-02 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 1452614c-ab09-33c4-82b4-9c881704b7d6 | -8.5962 | -44.7603 | 2025-10-02 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 0731a662-4e29-3abd-9844-dc9c2e49292a | -7.7941 | -42.5369 | 2025-10-02 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 298.1 |
| bede35d5-4a8b-3187-b079-b1caa64619c8 | -12.7627 | -50.5567 | 2025-10-02 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 162.2 |
| c3b4cc6b-13c5-309a-b8c7-ccdb9cf9ebee | -13.1932 | -47.8288 | 2025-10-02 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c92085ca-228e-3f29-bc2f-ac02c7db1471 | -6.6976 | -42.8354 | 2025-10-02 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| ed59ae41-1561-33a3-8e6a-45e0d985d2af | -13.1349 | -47.8597 | 2025-10-02 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| be631eea-9860-3c07-8558-3cacab675bbc | -11.854 | -47.7041 | 2025-10-02 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4f62b15a-0d07-3bd8-a851-b74122871848 | -14.2924 | -45.977 | 2025-10-02 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 6b352094-7cdf-384f-b8e3-4f220321977f | -11.4796 | -44.9943 | 2025-10-02 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 199.1 |
| b2037d0c-9725-335f-bb6d-e1cec1079b29 | -16.0561 | -45.7438 | 2025-10-02 13:50:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 301.9 |
| c617908b-90e1-39b3-9c92-c572cf81c0b7 | -13.7859 | -48.0748 | 2025-10-02 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 77637de7-75dd-336b-a4ef-263fd9a1c495 | -14.4055 | -46.1414 | 2025-10-02 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 7b363af2-bf2d-3f8a-a4dd-b770e20a1dbe | -13.767 | -48.0553 | 2025-10-02 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 41b4bb53-9db3-34c4-9738-cbc6cfb82d1c | -14.4757 | -48.4137 | 2025-10-02 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 922db304-66e0-375a-a352-daa125da50b2 | -5.7035 | -42.6841 | 2025-10-02 13:50:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |


[Clique aqui para ver as próximas entradas](README157.md)
