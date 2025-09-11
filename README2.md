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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57438939-7433-30be-8b28-c869da3e71a8 | -15.2529 | -44.0176 | 2025-09-11 00:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 60.8 |
| b31a8b0e-3d2b-3654-8d8d-bcf32e60ecd3 | -22.5894 | -51.8759 | 2025-09-11 00:10:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.7 |
| df306e79-190c-3c40-9e9d-5d98c7a5e64c | -15.9865 | -42.9719 | 2025-09-11 00:10:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 268.3 |
| 6bf9295f-ee84-3358-bbcf-c6ecf78b01cf | -19.2016 | -47.9889 | 2025-09-11 00:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 777ead90-ce45-3cd1-8839-ffe17b5b127f | -6.5706 | -44.1978 | 2025-09-11 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 9e94f073-8d3d-37cf-b1a5-0c6972925a3a | -22.5888 | -51.8985 | 2025-09-11 00:10:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| 95d1af66-57b4-3647-b662-9b59a230399d | -11.358 | -46.5393 | 2025-09-11 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 26051402-e13a-3d1a-ad81-ed877caa9fdf | -10.1637 | -68.1583 | 2025-09-11 00:10:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 35e6bc80-8f70-3a74-ac84-45dfbf3d9906 | -11.3397 | -46.4967 | 2025-09-11 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 2a9dae6b-1280-3caa-a8af-b79d9ebc698a | -23.3293 | -47.3379 | 2025-09-11 00:10:00 | GOES-19 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.5 |
| 8e03603e-f28f-3c37-8282-ebd321aa9e83 | -10.015 | -51.7451 | 2025-09-11 00:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 7df53a9f-ba8d-3b49-95d1-9743030bfea8 | -11.3397 | -46.4967 | 2025-09-11 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 21464045-c6c9-3a08-bb25-3139d276b9d7 | -12.864 | -47.9655 | 2025-09-11 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 47426e10-fb5f-3b5d-823a-924871e0266b | -13.1644 | -45.2897 | 2025-09-11 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 069d54a5-b235-367e-9a41-bfeea591c8ff | -11.3775 | -46.5142 | 2025-09-11 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 4a5ce144-4321-36dc-90d1-aa14d72dc3a4 | -11.7786 | -46.5047 | 2025-09-11 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 086f038b-7e27-3561-abd2-f31a10c3542b | -11.0201 | -45.059 | 2025-09-11 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 359e9d65-1968-3b4a-99d1-4837dbbea452 | -9.0232 | -49.7834 | 2025-09-11 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 99f97df6-b447-3e89-94b2-744e3c4456f6 | -10.034 | -51.7223 | 2025-09-11 00:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 9fc0e68d-8c01-309e-afd7-6d831e784b3c | -12.4164 | -63.8229 | 2025-09-11 00:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 04f4e9c4-ba70-3d62-976a-19935d53b02d | -9.4438 | -67.0264 | 2025-09-11 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| a5c4c483-1b31-3df6-a6f2-20040abaa42e | -11.3779 | -46.4916 | 2025-09-11 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| eaba9d28-abef-3ab7-908d-74cd15544aa9 | -11.0198 | -45.0821 | 2025-09-11 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| a70802e4-31e0-3391-bf75-f5628acf5da0 | -4.8783 | -45.2098 | 2025-09-11 00:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| a49a3d98-f1f1-3507-9b41-f3b63b74b985 | -19.201 | -48.012 | 2025-09-11 00:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4f5d8e0e-1a9a-368b-b44c-f6bc4854a662 | -15.9858 | -42.9964 | 2025-09-11 00:20:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 118.1 |
| d55c6f35-c7d6-3ca1-9081-ff7184b9fca6 | -9.0753 | -47.078 | 2025-09-11 00:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| b506b6c7-2fdd-3d3f-b3da-a70e66051c92 | -11.358 | -46.5393 | 2025-09-11 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 85d93367-5141-3f82-a999-24639fc4271e | -14.2881 | -54.7514 | 2025-09-11 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| f2756191-fe61-3d2b-b106-828047efd754 | -19.2016 | -47.9889 | 2025-09-11 00:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 132.2 |
| a463013c-2908-3550-aed5-a9f805dc46f4 | -11.1624 | -52.032 | 2025-09-11 00:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f59c3906-69fe-3b65-8efb-c2eb1d70a0e2 | -11.3588 | -46.4941 | 2025-09-11 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 22df267b-817a-31bd-aaae-7324f8fe8443 | -10.5482 | -49.8899 | 2025-09-11 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 701d36b6-39a6-3cea-925a-9ac8e616e1e8 | -10.1637 | -68.1583 | 2025-09-11 00:20:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 77e3f79b-2cf1-397c-80ca-8802a26bb8d8 | -4.8971 | -45.186 | 2025-09-11 00:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 280.6 |
| 7d3cf5f4-c8c0-3d72-8fa0-eaf4693ff53d | -15.9865 | -42.9719 | 2025-09-11 00:20:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 304.8 |
| 19db04c5-2771-39ce-9b21-3c0345d96bcc | -19.2218 | -47.9845 | 2025-09-11 00:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 38b33fd8-cf1d-3f4c-952a-cc09f1deb48e | -13.253 | -43.7758 | 2025-09-11 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 6d4d4350-4667-3edf-a36c-c22b918c7f20 | -9.0234 | -49.762 | 2025-09-11 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 76393052-15f9-3695-8ddb-35361cdbc63f | -12.4165 | -63.8038 | 2025-09-11 00:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 8d75a128-9178-3e20-a177-dedc073f3a28 | -12.3976 | -63.8048 | 2025-09-11 00:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 81.2 |
| d1943cec-6c84-39ee-bb0e-9ae2bbffa9bb | -22.5894 | -51.8759 | 2025-09-11 00:20:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.7 |
| 43ce35fc-4543-3f05-9c75-fa9b54c13f47 | -19.9994 | -47.6271 | 2025-09-11 00:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 06c56707-e10d-3e2a-b2fa-b6128bd9e8d7 | -11.1621 | -52.053 | 2025-09-11 00:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 3abdd286-00ec-38ce-a28e-8464ff9b36e6 | -6.5706 | -44.1978 | 2025-09-11 00:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 127736ca-15c2-3a46-b584-67710298edb6 | -15.1371 | -52.4252 | 2025-09-11 00:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 090da212-106b-3bae-ad59-b5fcd96f4fcc | -23.3513 | -47.308 | 2025-09-11 00:20:00 | GOES-19 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| 97790ee7-2048-3544-b3ed-291616a59336 | -10.015 | -51.7451 | 2025-09-11 00:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| f9c809f3-47b1-3375-8328-f870c4b4cc65 | -9.0579 | -46.9688 | 2025-09-11 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 6e190505-0f1b-36dc-8677-4106e76326cd | -20.4047 | -46.261 | 2025-09-11 00:20:00 | GOES-19 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 88.8 |
| b48c6c9d-9f7c-31e2-9b17-b985aa107eb5 | -12.0086 | -47.5945 | 2025-09-11 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 204616b2-ac2e-362e-9065-9f239e57d9d2 | -11.3584 | -46.5167 | 2025-09-11 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 219.0 |
| a8188833-cb12-398d-b0a5-29a64e1a9e4f | -13.317 | -46.3673 | 2025-09-11 00:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 11e55897-9e6a-3548-afef-dfad99c93b3f | -3.1771 | -42.8141 | 2025-09-11 00:20:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 9d3ed9f8-3cce-3d2f-9b3d-f9d522cafd01 | -19.2212 | -48.0077 | 2025-09-11 00:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 1e112a14-c8d5-3168-a192-6efebd2a0c62 | -12.3975 | -63.8239 | 2025-09-11 00:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 8a6661bf-2106-3bca-bcd2-15f9b062438c | -11.077 | -51.3462 | 2025-09-11 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 7e87fb6c-5c6f-38d1-a736-b651d0a7653d | -23.3301 | -47.3138 | 2025-09-11 00:20:00 | GOES-19 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.8 |
| c0767ce9-db02-30c9-a661-107cb4eeab21 | -20.6963 | -46.0688 | 2025-09-11 00:20:00 | GOES-19 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 9b4291ac-9e48-3bd8-b41f-d945d84ca249 | -15.2529 | -44.0176 | 2025-09-11 00:20:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 70.7 |
| aa3aec8c-9b6f-3dc5-b511-2200b2d4c794 | -14.3074 | -54.7492 | 2025-09-11 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 86034a1b-e166-3719-9670-3a33c48d68e2 | -10.0338 | -51.7433 | 2025-09-11 00:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 5219ed16-4235-306b-b775-784ac7cfad46 | -20.717 | -46.0636 | 2025-09-11 00:20:00 | GOES-19 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 985b0966-fd40-3dd5-ab04-80f864fec903 | -14.7527 | -60.2321 | 2025-09-11 00:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 6db236af-3d75-3fef-b0c6-a4bf3abb96ab | -13.1648 | -45.2665 | 2025-09-11 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 7ae0fcea-e1ed-3e54-9ce8-eacb340cff6a | -10.0152 | -51.7241 | 2025-09-11 00:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 4657e489-95fb-394b-9757-7bc77447d842 | -20.4039 | -46.2849 | 2025-09-11 00:20:00 | GOES-19 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 9e1f8023-adde-30b0-a37d-22fc4fc74592 | -12.8448 | -47.9682 | 2025-09-11 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 8efb940a-3a48-3630-808b-4585dc7e140b | -4.8785 | -45.1872 | 2025-09-11 00:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| d67ee4d8-2958-3917-a55e-4799e996a6cf | -4.897 | -45.2086 | 2025-09-11 00:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 137e6f2e-4438-3989-ad0d-e19f8cd737ae | -12.0086 | -47.5945 | 2025-09-11 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| fd82d2ff-631b-3a33-b3e3-ae3af47dc388 | -22.5888 | -51.8985 | 2025-09-11 00:30:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.5 |
| 07754755-640f-34f8-9e69-33d2e9213854 | -15.9865 | -42.9719 | 2025-09-11 00:30:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 257.0 |
| 2996d319-9b40-3a6f-aca3-c4b7bf9cdfc6 | -23.3301 | -47.3138 | 2025-09-11 00:30:00 | GOES-19 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| f66e3b78-209d-39cd-94f4-9d8a90979478 | -19.2016 | -47.9889 | 2025-09-11 00:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 62879c47-7249-3fac-93fe-ddefcbc39634 | -11.0201 | -45.059 | 2025-09-11 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 8857ff91-2d9f-3bec-be51-c95b5180dc57 | -4.897 | -45.2086 | 2025-09-11 00:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 046b680b-b1e9-34f0-902c-47e465d04c47 | -10.1637 | -68.1583 | 2025-09-11 00:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 72.4 |
| cbb42a06-4f6e-34d5-a48d-549008e32590 | -16.2939 | -50.0459 | 2025-09-11 00:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 53442010-431c-31dd-afd2-4be982b53f6d | -9.0753 | -47.078 | 2025-09-11 00:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b02da107-5299-314f-881b-c04d39381ce4 | -10.015 | -51.7451 | 2025-09-11 00:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 9156fda2-c2a4-3cbc-9a23-19bfb79ea3e2 | -6.3467 | -44.0782 | 2025-09-11 00:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| f69a76e3-40cf-3dcc-9850-bcb9d8417c50 | -4.8971 | -45.186 | 2025-09-11 00:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 334edfe0-e0fa-3cdb-8118-1391b12c72cd | -7.2374 | -55.0604 | 2025-09-11 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 6b6434aa-7e63-3cda-80c6-5d86b2ff603c | -19.9994 | -47.6271 | 2025-09-11 00:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 33a7e570-9d8a-3aba-ad1a-3702ea6247cb | -9.0232 | -49.7834 | 2025-09-11 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 151e7b94-7f73-344e-aca0-06319b94063d | -12.3975 | -63.8239 | 2025-09-11 00:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 93.8 |
| be1f4715-dbb7-39ed-abfe-66fe958f9eae | -20.4047 | -46.261 | 2025-09-11 00:30:00 | GOES-19 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 941ca72b-2dfc-3f93-bc95-61faf5fecc4e | -3.1771 | -42.8141 | 2025-09-11 00:30:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 76e16958-de97-3954-8908-d9c2f17223b1 | -15.9858 | -42.9964 | 2025-09-11 00:30:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 112.9 |
| f4ad4703-dda7-3e3b-ab5a-0d4cb7f35ecd | -10.034 | -51.7223 | 2025-09-11 00:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 44ca60dd-4310-381c-9214-cd9457c85c94 | -11.3779 | -46.4916 | 2025-09-11 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 43eac59f-095d-3566-a537-2de482f2db9e | -10.0338 | -51.7433 | 2025-09-11 00:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 74a6c936-fa6d-34ed-83e3-ad4005c43de2 | -13.1644 | -45.2897 | 2025-09-11 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 1b1596f4-a12c-3bc4-b202-fbc1c69eab34 | -22.5894 | -51.8759 | 2025-09-11 00:30:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.3 |
| bc05f1fb-c467-346f-b989-f86a1b9f6429 | -11.9895 | -47.5971 | 2025-09-11 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 77ebcc86-4705-39c6-a103-1f92f0e07ec6 | -16.3131 | -50.0648 | 2025-09-11 00:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 124.5 |
| eb914c1e-65eb-3847-8380-f14e9a5c70c5 | -9.0234 | -49.762 | 2025-09-11 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 019894dd-1a3b-3481-ab0d-357c3381a07f | -14.2881 | -54.7514 | 2025-09-11 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 00140fef-7dec-3a06-b250-b18b95ddc497 | -11.3584 | -46.5167 | 2025-09-11 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 213.7 |


[Clique aqui para ver as próximas entradas](README3.md)
