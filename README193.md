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

## Dados Diários - Página 193

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcbee06e-bb74-35ef-bd4a-6771a9b7657c | -11.9487 | -50.1402 | 2024-10-04 13:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 32f74c3d-1399-329c-9110-1fb21dccb2b3 | -12.7815 | -50.5758 | 2024-10-04 13:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 65842336-303a-348b-ae90-7d641440d3ca | -13.1595 | -48.6322 | 2024-10-04 13:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 425f3966-7c08-3045-b802-1d87d4361838 | -13.1443 | -46.3261 | 2024-10-04 13:36:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 64cd84ac-0bdc-3b9a-9baf-9779c6c8c723 | -13.1787 | -48.6295 | 2024-10-04 13:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 300552c7-a988-3cdb-8b0b-72a1ba8df58e | -13.199 | -45.492 | 2024-10-04 13:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a3e2c20e-e3a7-39cf-a7e6-40cefb8213bb | -13.1779 | -48.6737 | 2024-10-04 13:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 147.3 |
| d590a4e6-91f7-345a-97ee-00dfaba929cc | -13.5058 | -48.6268 | 2024-10-04 13:36:22 | GOES-16 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 7463cb1e-0091-37c5-9f10-0f8d450bedec | -13.5062 | -48.6046 | 2024-10-04 13:36:22 | GOES-16 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 928a27fe-5391-31d9-a10d-9cbf9bb63887 | -13.5255 | -48.6018 | 2024-10-04 13:36:22 | GOES-16 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 1746154c-679c-31f7-a38b-b2a52b2f4183 | -14.0382 | -45.1414 | 2024-10-04 13:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 211.3 |
| 78ce7a30-d3e0-3b2f-837a-01303d365e5b | -14.0378 | -45.1648 | 2024-10-04 13:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| e0f560f1-4850-3c94-81fe-a25f17ccc396 | -14.3199 | -44.6934 | 2024-10-04 13:36:26 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 8946cea2-a78d-3ee7-b7cd-e82c4443d2d9 | -14.5163 | -49.3148 | 2024-10-04 13:36:28 | GOES-16 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 5962f046-d7ef-3216-b159-cb5ccb316967 | -14.5168 | -49.2927 | 2024-10-04 13:36:28 | GOES-16 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| c4ed3d73-31f6-3464-a3ef-506e2d336c9e | -14.5362 | -49.2898 | 2024-10-04 13:36:28 | GOES-16 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 6eaa530e-0d5b-3b3a-9a59-1a46d1fd5902 | -14.6822 | -48.759 | 2024-10-04 13:36:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 99fc4d66-da32-30fa-93cb-cd1dbd43fa25 | -15.4247 | -47.6736 | 2024-10-04 13:36:32 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a130da89-163e-380f-a018-13687e245409 | -15.6107 | -47.2098 | 2024-10-04 13:36:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 2279eeff-a20a-34ac-8f09-6d1e8a89341b | -15.6304 | -47.2063 | 2024-10-04 13:36:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 67af666f-4cb3-3f4e-8a6f-0a3b0ab34652 | -16.9296 | -47.1455 | 2024-10-04 13:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 79.7 |
| edfb0188-4b20-33f6-9036-2886c46dd573 | -16.8055 | -57.3788 | 2024-10-04 13:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| b750f7a1-380c-3a88-96ec-a7d6e5bfe0e1 | -17.6074 | -46.9866 | 2024-10-04 13:36:44 | GOES-16 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 65dcc351-5526-3f9f-ac80-1d984b460930 | -18.8613 | -43.5837 | 2024-10-04 13:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.3 |
| 20f2bd3a-843e-326c-8534-60cbe997b344 | -19.1134 | -48.2833 | 2024-10-04 13:36:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 141.3 |
| a0327c0f-76a2-3454-b726-dc4f5ae62355 | -19.6122 | -46.2632 | 2024-10-04 13:36:54 | GOES-16 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 22268a9c-4e1d-3ade-bda3-40fa33dd4eec | -6.6377 | -44.9705 | 2024-10-04 13:45:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| b03a7142-b4a1-3ae4-a58e-9e4822f841ac | -6.6565 | -44.969 | 2024-10-04 13:45:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| f4d457c2-465d-3a0a-8d97-7e6a867fbecd | -6.6341 | -45.3339 | 2024-10-04 13:45:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c50d21e4-a393-3c89-8c7b-ae97a99c8991 | -6.9479 | -47.6668 | 2024-10-04 13:45:46 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 1197e627-ee0b-3ebf-8bd1-0ec4d761cdd0 | -6.9477 | -47.6887 | 2024-10-04 13:45:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| d76c251c-32b1-3388-a4c6-f708298fdc9f | -7.2565 | -45.0079 | 2024-10-04 13:45:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| a0f75d4a-e4ef-3654-bac6-ad7951d9d75a | -7.8353 | -50.5204 | 2024-10-04 13:45:51 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 29943c4f-c542-3184-b9da-5bfd4a8f648e | -8.1951 | -43.6703 | 2024-10-04 13:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| fecab13d-173f-3270-b4c3-f56d7a595653 | -8.1948 | -43.6936 | 2024-10-04 13:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 836a21db-1aa2-3d52-8aa4-8e34690127cd | -8.1241 | -44.8101 | 2024-10-04 13:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 527a473f-3624-327b-b85e-87d848ac7485 | -8.1759 | -43.6957 | 2024-10-04 13:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 401b299b-1ca3-346b-b19e-7bb209822d8e | -8.2859 | -45.4317 | 2024-10-04 13:45:53 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 096da13f-5f70-3b6c-a541-ef82a1d2b99c | -8.435 | -47.0977 | 2024-10-04 13:45:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 75db371b-4086-30fa-95e3-e402cbe10e41 | -8.5212 | -44.7225 | 2024-10-04 13:45:54 | GOES-16 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 5cb30188-cf75-3df4-918a-45c4b706163d | -8.6448 | -50.0518 | 2024-10-04 13:45:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 6b1f78ea-9568-3868-a5a8-233d3857f6c1 | -8.6636 | -50.0501 | 2024-10-04 13:45:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c99a243a-0548-387f-84c6-fcb3218de6f6 | -9.5641 | -50.1388 | 2024-10-04 13:46:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 89057981-f12e-343f-aa88-a05b6ddd2208 | -9.9822 | -42.0976 | 2024-10-04 13:46:02 | GOES-16 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 138.6 |
| 017a3d7c-42f2-32b3-939b-e9cad92e6db4 | -10.2574 | -47.6796 | 2024-10-04 13:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 12259289-58b4-3ac4-8496-42bd045e2726 | -10.2381 | -47.7038 | 2024-10-04 13:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 69a96058-f8e5-3e61-9d24-1b2522fcdb63 | -10.2188 | -47.7281 | 2024-10-04 13:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 46abc88e-31c7-37c3-b1b4-e27ff18b6d6a | -10.2192 | -47.706 | 2024-10-04 13:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 2821ebf7-7454-3dfd-b7c6-a576023bbcfd | -10.2378 | -47.726 | 2024-10-04 13:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 7d7c4330-03a3-3d00-8f5d-676fe2f2880f | -10.6367 | -45.2027 | 2024-10-04 13:46:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| db8d2c91-c81b-3f6b-a48e-5093328cbe77 | -10.6119 | -48.0575 | 2024-10-04 13:46:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| e81813f4-fbc3-3b70-862c-db21597932f3 | -10.7118 | -47.7149 | 2024-10-04 13:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 2a64bc58-d1e6-34c6-b2e6-6b401cb33397 | -10.8216 | -45.5444 | 2024-10-04 13:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 34ea75ca-0f6a-3440-ab24-798305ba7c02 | -10.8021 | -45.5698 | 2024-10-04 13:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| ee333cde-2dc6-3960-8af0-edc71ebfb782 | -10.7309 | -47.7126 | 2024-10-04 13:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 586fe5c3-2e38-3c1b-a5d9-a346dc6f353c | -10.8018 | -45.5927 | 2024-10-04 13:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 1f137866-9d61-3615-a1fd-eaf08d54d0b8 | -10.9187 | -46.6192 | 2024-10-04 13:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| e1afa63e-62a1-3a47-96bd-a2fa9600d984 | -10.9374 | -46.6393 | 2024-10-04 13:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 9727abc3-ff91-307e-962e-b4edcea40f8f | -11.2779 | -43.4118 | 2024-10-04 13:46:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| abaeaf8e-a61b-39d6-a611-eb62aaafefe3 | -11.2783 | -43.388 | 2024-10-04 13:46:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| f8fa90c4-e5b2-3a79-b317-414047e54299 | -11.1388 | -45.9577 | 2024-10-04 13:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 3f26926c-a1dd-36c0-a686-5872497a1e5e | -11.2971 | -43.4088 | 2024-10-04 13:46:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 209.8 |
| acf43b5d-4518-3f73-9de8-83604ee727b7 | -11.2369 | -46.9597 | 2024-10-04 13:46:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 08a03e68-a8b5-3714-a289-f439d7245870 | -11.2768 | -46.8424 | 2024-10-04 13:46:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| a502e0a2-12de-352e-b76e-8f9f5d774024 | -11.275 | -46.9548 | 2024-10-04 13:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| d66d28c1-edad-31b7-8002-4e1929819756 | -11.2959 | -46.8399 | 2024-10-04 13:46:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 3b098b6b-bf76-3bc1-9a7c-da65d1d2675c | -11.3853 | -47.2088 | 2024-10-04 13:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 6bef0141-caf6-3511-a57e-c6febfd18966 | -11.4746 | -50.0452 | 2024-10-04 13:46:11 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 272462dc-7af3-3aac-8af0-888bd8f35e1f | -11.6804 | -47.8156 | 2024-10-04 13:46:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 94f0685d-fd6f-3c84-a5f2-842efaef82c0 | -11.7205 | -47.6995 | 2024-10-04 13:46:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| c31a4894-5f69-3661-bd40-037a7cb0a01b | -11.7412 | -50.0141 | 2024-10-04 13:46:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 3970565c-c3aa-3930-a7b2-a491c854a6ee | -11.7415 | -49.9925 | 2024-10-04 13:46:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| deb6724a-0f15-3af8-a779-81d765b9a8c0 | -11.9105 | -50.1447 | 2024-10-04 13:46:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| fdc59725-fda6-3a89-b22e-e2fdac6b48eb | -11.9487 | -50.1402 | 2024-10-04 13:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| af473610-b4db-3a58-8bc7-99954426a8a6 | -11.9296 | -50.1425 | 2024-10-04 13:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| a076b8df-a4dd-3fcd-a892-e1f769f5c45d | -11.9862 | -50.1787 | 2024-10-04 13:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| cb4c76fe-3d60-317b-bf25-01b694eb6297 | -12.7815 | -50.5758 | 2024-10-04 13:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| e83f0432-8aba-3905-92e1-c033ede8d810 | -13.1779 | -48.6737 | 2024-10-04 13:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 0236bfb3-e0af-3104-a07b-bdc38244b763 | -13.1443 | -46.3261 | 2024-10-04 13:46:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 110.2 |
| d3e969d5-0db5-35d9-9919-b8d4984538e4 | -13.1787 | -48.6295 | 2024-10-04 13:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 3eb402cf-e567-3bab-9c25-6e76292ea8c7 | -13.5255 | -48.6018 | 2024-10-04 13:46:22 | GOES-16 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| b8859d40-ace4-3c66-b2e5-e8a0e97ae241 | -13.5058 | -48.6268 | 2024-10-04 13:46:22 | GOES-16 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 64f9187c-a2c3-309a-a3f3-a614edb02294 | -14.0378 | -45.1648 | 2024-10-04 13:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 20c178cb-55fe-3495-bf0a-141766c4e6df | -14.0382 | -45.1414 | 2024-10-04 13:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 242.2 |
| b6c6fc5d-2f81-3774-ba6d-3237ab6127ef | -14.5168 | -49.2927 | 2024-10-04 13:46:28 | GOES-16 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 7ce1eab1-5f86-37e2-a3d2-bee123fc8c14 | -14.5362 | -49.2898 | 2024-10-04 13:46:28 | GOES-16 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| b5b5e133-2e63-31b9-a260-ed834b25bb16 | -14.6822 | -48.759 | 2024-10-04 13:46:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| a67bc5f6-c617-3832-8cc1-83683345a857 | -15.4247 | -47.6736 | 2024-10-04 13:46:32 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d562472d-8679-3b36-8a12-37cb57235b1b | -15.6304 | -47.2063 | 2024-10-04 13:46:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| c9471e41-49b8-3c1f-93e5-26fa4817bb86 | -16.6518 | -57.2125 | 2024-10-04 13:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| ea1e120d-d0a6-31f4-874c-58ffd48b9342 | -16.9296 | -47.1455 | 2024-10-04 13:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 38230c72-c0bc-35e4-b9c3-3fd417d76080 | -16.8626 | -57.4744 | 2024-10-04 13:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 278828fe-2a65-3d7a-9a30-caadbf23aafb | -16.843 | -57.4767 | 2024-10-04 13:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 58765015-ed73-3c09-8609-3676edc2ff63 | -18.8613 | -43.5837 | 2024-10-04 13:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.5 |
| 789fb18a-d768-32e4-a0eb-ca59c071fc23 | -19.1134 | -48.2833 | 2024-10-04 13:46:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 79e9a0e4-3481-3db5-8fda-74d477641be7 | -19.6122 | -46.2632 | 2024-10-04 13:46:54 | GOES-16 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 5c091716-8c0f-34a7-a8da-447ee3e3815d | -6.7619 | -45.6621 | 2024-10-04 13:55:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| c19016a3-7060-3f7a-9b94-b1274800b881 | -6.6377 | -44.9705 | 2024-10-04 13:55:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| e2c7c7ca-3bb0-326f-8c83-5cb864a60549 | -6.6341 | -45.3339 | 2024-10-04 13:55:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 1e3091cd-78c5-3ef0-9902-266c8f588784 | -6.6343 | -45.3113 | 2024-10-04 13:55:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |


[Clique aqui para ver as próximas entradas](README194.md)
