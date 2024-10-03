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

## Dados Diários - Página 213

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3d40a05-e2cf-369e-b8c5-8cef85618e65 | -7.8245 | -61.3709 | 2024-10-03 13:25:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 5e976572-f0d6-3224-b0cc-05a360f26256 | -8.1756 | -43.719 | 2024-10-03 13:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| 70c04b18-691a-3708-a667-efde7d216f86 | -8.157 | -43.6977 | 2024-10-03 13:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 151.8 |
| f771742b-e4de-3e90-b20f-4ad0f89f14b6 | -8.1567 | -43.7211 | 2024-10-03 13:25:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 158.9 |
| 8c18204a-e7d9-3a38-bfd2-36dd3c4c2ad6 | -8.1937 | -46.8324 | 2024-10-03 13:25:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 30840314-7648-333a-ab94-f83dbe2bd476 | -8.1951 | -43.6703 | 2024-10-03 13:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 497a9061-588a-33b2-b56d-06093bd979ab | -8.1759 | -43.6957 | 2024-10-03 13:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 1569ee70-ae09-3c5c-a030-ac6175b896f1 | -8.6113 | -46.5243 | 2024-10-03 13:25:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 3d21f9e0-3abe-3b96-9c22-e75a9d9bbbcc | -8.7225 | -45.204 | 2024-10-03 13:25:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 7c34eaa0-f15b-399c-91d4-d916c89bc172 | -8.7036 | -45.2061 | 2024-10-03 13:25:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f84d9871-a499-33b5-8682-e82a51dcb090 | -8.9055 | -45.6387 | 2024-10-03 13:25:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f18124f9-9bda-326b-a7c1-4323dc97b400 | -8.8356 | -45.2145 | 2024-10-03 13:25:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 2d82c70e-e801-3108-9b1d-a1d42627c370 | -8.8362 | -45.1688 | 2024-10-03 13:25:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 58283ab0-9125-3484-b868-8d13a95da007 | -8.9244 | -45.6367 | 2024-10-03 13:25:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 7ad3617f-4278-3f38-9457-41d8010a6cd9 | -9.0229 | -49.8048 | 2024-10-03 13:25:57 | GOES-16 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 2a8dae6b-fd92-3155-a0fa-da8a60a737f9 | -9.0149 | -67.7423 | 2024-10-03 13:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 096e1f98-7ae4-3ba8-91a9-8c83f55a8abc | -8.9791 | -67.4099 | 2024-10-03 13:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 96102e19-33a3-3461-a248-4e9f245ee70f | -9.0515 | -67.871 | 2024-10-03 13:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| aeb6ee27-7fb7-30e8-8477-40b1ef24ea9f | -9.3833 | -68.3256 | 2024-10-03 13:26:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 85523bc3-8e18-3c39-be8a-4d954fd000bf | -10.5926 | -48.0817 | 2024-10-03 13:26:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 34e10a18-a4b9-3dc7-88f7-807eb2fed0df | -10.7161 | -46.1942 | 2024-10-03 13:26:06 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 75d64fb8-26de-312e-85c1-010779ccb1e9 | -10.8906 | -45.9905 | 2024-10-03 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 2db1a346-7205-35ce-856d-7be989b365dc | -10.7122 | -47.6927 | 2024-10-03 13:26:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b0350961-a499-3c08-a3cb-32f9cf8bdcb2 | -10.7456 | -47.9978 | 2024-10-03 13:26:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| ffcb592e-8bed-3b2e-b7d2-2481f0d46a84 | -10.7834 | -45.5495 | 2024-10-03 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 1e67d5a7-4588-3e3f-80a2-ac5aa2b110cc | -10.7459 | -47.9757 | 2024-10-03 13:26:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| d92666fd-6fcd-3479-9990-63fb3b4e3c6e | -10.7831 | -45.5724 | 2024-10-03 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 75a72952-52e6-3120-9532-fc117e7b4bc4 | -10.7309 | -47.7126 | 2024-10-03 13:26:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 557a70d0-ee91-3402-9286-7503fe5f9b44 | -10.7312 | -47.6904 | 2024-10-03 13:26:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| c125e979-9bb0-3e72-ae64-4f12820f653f | -10.7352 | -46.1918 | 2024-10-03 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.3 |
| e16b155d-af46-3023-a5d0-f1d8b829521a | -10.876 | -48.1584 | 2024-10-03 13:26:08 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| bed09827-84c6-3b08-a731-bfd7876f2b9e | -11.0345 | -46.5143 | 2024-10-03 13:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 9a6d6073-b9ca-3187-8647-6fd3422f1f0d | -11.2783 | -43.388 | 2024-10-03 13:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 04eec828-2585-3739-9a63-2d32a15a8770 | -11.2779 | -43.4118 | 2024-10-03 13:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 39fc27d6-1a31-337a-8b00-d5d3d51b3df2 | -11.2758 | -46.9098 | 2024-10-03 13:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 8af1ace8-9eed-32e4-9cd6-49876872a759 | -11.9671 | -50.181 | 2024-10-03 13:26:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 23283375-93c7-33a8-b4d3-496cdffc9dbc | -12.0128 | -47.3486 | 2024-10-03 13:26:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| e99b3a22-05fa-37cb-8ae5-504ab32472fe | -11.9737 | -47.3986 | 2024-10-03 13:26:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| a3cdf225-4f8a-3b82-b778-e3d5a8f59df7 | -12.1406 | -50.0524 | 2024-10-03 13:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 0d87b9ee-d6f1-32db-bec9-e28f6924310d | -12.7812 | -50.5973 | 2024-10-03 13:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1d4dbf1f-c853-3af2-be2d-e85bf59a2b3b | -12.762 | -50.5997 | 2024-10-03 13:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 2e38b4db-7378-368e-9cfa-c8338b7b500d | -13.0017 | -44.7357 | 2024-10-03 13:26:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 3ef5f7be-9565-32c2-8547-524e9f6f9386 | -13.0021 | -44.7123 | 2024-10-03 13:26:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 50623ba8-56ad-3f6b-8e34-6b263ffe211a | -13.1351 | -51.1955 | 2024-10-03 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 165d8931-7ca9-38fa-b117-c35c22b23721 | -13.198 | -48.6267 | 2024-10-03 13:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 79ef7ea7-1a36-3a2b-bee7-6e8529a7908a | -13.0591 | -51.1623 | 2024-10-03 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 10676aa2-b69e-3485-86dd-8d4dfb6e0679 | -13.0402 | -51.1432 | 2024-10-03 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 178.8 |
| e1637d29-8852-39e3-9715-fafcccbd7eed | -13.1801 | -45.472 | 2024-10-03 13:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| b97b5e3e-39a1-3167-974c-0ed180254b21 | -13.1976 | -48.6489 | 2024-10-03 13:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 7ac988a8-9c1d-3d1f-bc7d-4684aaa6f9ba | -13.0399 | -51.1646 | 2024-10-03 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 24795e27-95d2-3bab-ab23-8dad54807d83 | -13.0406 | -51.1218 | 2024-10-03 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 4a9e9b41-9948-3f20-b02f-bd24c3730190 | -13.0975 | -51.1575 | 2024-10-03 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| f71501d8-2062-3f6d-91fa-f1a019245a9f | -13.1805 | -45.4489 | 2024-10-03 13:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| f4dd7c0e-126f-3074-ad62-b3344b497567 | -13.1924 | -51.2097 | 2024-10-03 13:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 005af8a5-a38f-3289-8f45-b280ad327fd2 | -13.1927 | -51.1883 | 2024-10-03 13:26:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a55404d5-c313-37b4-a603-2fbf137723c0 | -13.5387 | -51.1442 | 2024-10-03 13:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 5fce1b94-1e50-3726-97f7-5f1b88f3d6dd | -13.5195 | -51.1467 | 2024-10-03 13:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 9ef043a8-16be-37e4-9041-27ec75ec65ef | -14.0392 | -45.0947 | 2024-10-03 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 84a5813f-cc1f-38f8-a0fc-e16a02447b1b | -14.7935 | -48.05 | 2024-10-03 13:26:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 14a89013-9424-3ff5-89d5-edb51a1164a0 | -14.7017 | -48.7559 | 2024-10-03 13:26:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 5f8bc43f-e90e-30ec-9d64-fbc12f06bab7 | -18.3079 | -43.2326 | 2024-10-03 13:26:47 | GOES-16 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| 7d55ee32-f739-3db6-b328-e20949cb2574 | -19.0141 | -43.1998 | 2024-10-03 13:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 142.5 |
| 055ce9c9-1cbf-3cdd-8261-5b5ad1f898e4 | -19.0344 | -43.1944 | 2024-10-03 13:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 139.9 |
| e3c36eea-5c8e-3908-930c-3df90c77f65b | -19.2962 | -42.5779 | 2024-10-03 13:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 167.7 |
| bf22ca4f-7247-327e-b434-ba6603e93b03 | -19.2954 | -42.6032 | 2024-10-03 13:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 150.9 |
| 0ce11534-afa4-3516-aa7a-8b61d2e5acbe | -19.0932 | -48.2876 | 2024-10-03 13:26:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 148.9 |
| a91c8acb-8a28-3880-bb09-37b7f73464db | -19.744 | -40.6685 | 2024-10-03 13:26:54 | GOES-16 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 130.3 |
| 5f1fcf2d-d486-3eea-abb9-fcb0db0aea9e | -6.9075 | -44.2836 | 2024-10-03 13:35:45 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 194.5 |
| 14fc0e98-b84f-3cc1-ac45-b969272b7169 | -6.8887 | -44.2853 | 2024-10-03 13:35:45 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 355.8 |
| 60769aaa-5c4c-39f7-a7e5-c26c323aff51 | -6.9979 | -42.9016 | 2024-10-03 13:35:45 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 56b5cb65-8053-3816-93e7-cdf5bcdb4fea | -6.8885 | -44.3083 | 2024-10-03 13:35:45 | GOES-16 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 42b14f17-b006-3135-aa9d-0198376025ff | -6.9791 | -42.9034 | 2024-10-03 13:35:45 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 59b13754-df71-3325-9f87-54b2545c77b6 | -7.0364 | -42.8272 | 2024-10-03 13:35:46 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 567a5b10-308b-3567-8630-e66e2b11290c | -7.2011 | -46.6766 | 2024-10-03 13:35:47 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 33e7f070-e08b-3345-885c-088d922fca0a | -7.2199 | -46.6751 | 2024-10-03 13:35:47 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 83049f10-d3c8-389d-8d91-02c51debc2f0 | -7.6444 | -42.4342 | 2024-10-03 13:35:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 08d2233a-4de8-34cf-a8e0-72af73dfaacb | -7.4587 | -64.4388 | 2024-10-03 13:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 4317290c-dbb1-3444-a3de-40c082687907 | -7.6441 | -42.458 | 2024-10-03 13:35:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| c479ec72-c1e9-389e-9e3c-87c34fb316e1 | -7.8629 | -43.0733 | 2024-10-03 13:35:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 99042343-56e0-3e1c-b5f5-483c3d7b4a80 | -7.8149 | -45.4782 | 2024-10-03 13:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 45c7dff7-42f0-3ad2-a6e9-d0d28dab6633 | -7.8245 | -61.3709 | 2024-10-03 13:35:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 139a281f-9ec6-3bc0-bc73-eb5f0bcb5f08 | -8.1937 | -46.8324 | 2024-10-03 13:35:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 53eb6d4f-d34d-3a01-8f70-fb46c37217a4 | -8.1859 | -44.3901 | 2024-10-03 13:35:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 47.4 |
| b10c10ad-ea09-3619-ae30-16af9b0dbc8b | -8.157 | -43.6977 | 2024-10-03 13:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| ede5b348-5efc-30bd-9d62-b5b74106723e | -8.1756 | -43.719 | 2024-10-03 13:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 9139acaf-b98e-3102-9c5f-3eadaa28fe97 | -8.1759 | -43.6957 | 2024-10-03 13:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| f266d7bb-f99d-34e9-940e-d866bf41d259 | -8.1567 | -43.7211 | 2024-10-03 13:35:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 157.2 |
| a7b1c80a-e534-3070-b521-b2475d3d6af5 | -8.2239 | -44.363 | 2024-10-03 13:35:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 9c615c8a-d807-3fe6-a922-0c88e61491d1 | -8.4259 | -46.2968 | 2024-10-03 13:35:54 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 49c2c976-64f5-33cb-a376-7eb76fa6f1cf | -8.7225 | -45.204 | 2024-10-03 13:35:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 73fa7df8-26f0-38cf-bca6-f495eaf2f769 | -8.7036 | -45.2061 | 2024-10-03 13:35:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 22ccb4f5-abe4-3832-8005-942fd31aa1b7 | -8.7228 | -45.1812 | 2024-10-03 13:35:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 3d842f6d-84e9-3c9d-a41e-238848218d17 | -8.8356 | -45.2145 | 2024-10-03 13:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| e938bc96-1acf-3d48-9523-4ea16204355f | -8.8362 | -45.1688 | 2024-10-03 13:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 69c37f06-f2ac-378e-bfe0-7f53c8b5382f | -9.0229 | -49.8048 | 2024-10-03 13:35:57 | GOES-16 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 90c5aea4-f738-3331-b636-a0826570214c | -9.0227 | -49.8262 | 2024-10-03 13:35:57 | GOES-16 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 21c5c780-30b9-3d43-bc5f-a5a1163010eb | -9.0149 | -67.7423 | 2024-10-03 13:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 306e980b-85de-3ee9-8ddf-7d09f2730ff9 | -9.0515 | -67.871 | 2024-10-03 13:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 3b9d24d1-2e9d-37d0-83ab-e3dfd74ffeed | -8.9791 | -67.4099 | 2024-10-03 13:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 4ed36726-9758-395d-a4ca-e49ab112d146 | -9.3833 | -68.3256 | 2024-10-03 13:36:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 84.8 |


[Clique aqui para ver as próximas entradas](README214.md)
