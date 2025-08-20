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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 160d6846-7b4f-3faf-9550-0a1312167b11 | -20.4858 | -42.275501 | 2025-08-20 00:14:00 | METOP-C | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0bf773fc-4de3-3d74-8b22-ba48be130e85 | -21.7278 | -46.512699 | 2025-08-20 00:14:00 | METOP-C | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a63bd0fa-8f64-31df-8ae4-fea95b8cb6b5 | -6.9247 | -46.990501 | 2025-08-20 00:14:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33207be9-6a79-3b43-ab4b-c079ef55f1db | -6.8627 | -43.6124 | 2025-08-20 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 879df69d-7e81-3ffe-9569-7be36f8485e2 | -5.2844 | -44.195301 | 2025-08-20 00:14:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7eacd94-5845-3314-b49e-f2e1a47362a7 | -5.9887 | -42.849098 | 2025-08-20 00:14:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 50f1888c-0c12-3b96-86c4-10996def36d9 | -13.0351 | -46.8041 | 2025-08-20 00:14:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bfc3930b-16bb-3629-8a99-cc9fec743ace | -5.8818 | -48.120701 | 2025-08-20 00:14:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab66d279-ba14-36fa-96a0-1c52de49ea69 | -11.7487 | -48.183102 | 2025-08-20 00:14:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f57acc79-a1f9-33eb-9240-605aed15282f | -5.7818 | -43.889801 | 2025-08-20 00:14:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33eae44b-fdcb-3e4b-9012-515767c551b0 | -7.5851 | -44.400902 | 2025-08-20 00:14:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6418347e-d817-3952-b381-a7bc274fb92b | -22.714701 | -42.133301 | 2025-08-20 00:14:00 | METOP-C | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85a14f09-9584-31b3-875e-aafd7fe82b23 | -6.9607 | -42.858 | 2025-08-20 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 52236d15-0ad8-389d-933d-7db1b0e491a0 | -4.4331 | -47.76 | 2025-08-20 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2a87f074-6a0b-3820-8297-f2e969e6a5ba | -8.6343 | -62.1367 | 2025-08-20 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 46cae33a-4489-353f-a1cf-1c07372cc08b | -12.9775 | -56.8816 | 2025-08-20 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| eba276d1-166f-32dd-9e98-d2d2846a3f6c | -12.9778 | -56.8614 | 2025-08-20 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 6de7a7b1-83be-3d2e-ab0c-ac3d8caa0d23 | -8.0152 | -47.6656 | 2025-08-20 00:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 017b8e45-3b76-3762-8484-c5d444dfe5e8 | -7.2787 | -50.1812 | 2025-08-20 00:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 62032f13-9bd3-357d-871c-ebced026ff39 | -20.3385 | -51.7284 | 2025-08-20 00:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 004e0750-9efc-3c0d-9d69-04fab2050396 | -2.3763 | -47.6636 | 2025-08-20 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 92619511-a0cc-3b10-9b57-7afd8db047a8 | -12.955 | -46.1504 | 2025-08-20 00:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| cd10d960-a773-3d20-81e8-be6e35d96d26 | -13.3346 | -54.4233 | 2025-08-20 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 26c6ad53-33aa-3e58-8bcc-d6abb9e3bd32 | -13.1364 | -54.9376 | 2025-08-20 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8ed498dd-d279-3377-913f-dc59c9fcbf76 | -6.1476 | -57.7215 | 2025-08-20 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0c825c0f-5c95-31e9-8cfa-7893af3243ac | -15.0002 | -54.8135 | 2025-08-20 00:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 1e859b28-d67a-3bb4-9231-5b8eb3183f45 | -20.3594 | -51.7023 | 2025-08-20 00:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 6fe6e71e-52a4-3b2e-91ce-fe830e9cd80d | -3.982 | -42.516 | 2025-08-20 00:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 47.9 |
| afec840b-5728-30a7-8765-a7a7a0c6a84c | -7.26 | -50.1825 | 2025-08-20 00:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a83be4dd-3241-383d-9c40-03dc3f688413 | -6.9605 | -42.8816 | 2025-08-20 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| e2c42f2f-d572-3a3f-9bdb-a6122d4ed300 | -20.339 | -51.7062 | 2025-08-20 00:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e9f557dc-7fc7-3d98-b6ed-a9f9d1509256 | -3.232 | -46.8056 | 2025-08-20 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 8118641a-c10a-377a-a60b-38a611d600e0 | -13.1558 | -54.9151 | 2025-08-20 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 866209c1-f9bc-3b22-8cbf-2cc4fd3209d5 | -8.034 | -47.6639 | 2025-08-20 00:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 2b103673-303e-3566-96d8-ee693ab2a54d | -4.912 | -43.2337 | 2025-08-20 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 841c6a6d-d0aa-3e6b-a3ed-bef47f61e604 | -8.6342 | -62.1557 | 2025-08-20 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 998e07d9-c62a-32e0-abb5-0cb795f6dc41 | -13.1555 | -54.9357 | 2025-08-20 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 2f0028c2-3e62-37eb-a739-83b6f7ca0468 | -6.9605 | -42.8816 | 2025-08-20 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 11706e00-361c-3d9b-aaf9-b25aa506fdfb | -7.26 | -50.1825 | 2025-08-20 00:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a795ffe2-7923-3cb1-9a82-891b45e9e7a1 | -12.955 | -46.1504 | 2025-08-20 00:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| d83f2336-170e-373f-a97a-2fe5dcc29ff1 | -20.339 | -51.7062 | 2025-08-20 00:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 23e92d2e-42c0-3a30-a575-2006dc04cad8 | -6.8586 | -43.5936 | 2025-08-20 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 46.7 |
| c913c103-efb8-3d4b-907e-b9547858587c | -13.1364 | -54.9376 | 2025-08-20 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b62b82ec-88a6-3d9e-9f5f-fc6c9d5f83c3 | -6.9607 | -42.858 | 2025-08-20 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 942960b7-c572-33c9-a238-a02555c296ff | -3.232 | -46.8056 | 2025-08-20 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| ae0d7b88-a020-3c5e-a451-9649807df41f | -6.8583 | -43.6169 | 2025-08-20 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 37b6f46b-3938-3d4c-8895-13bcb0fab43c | -15.0002 | -54.8135 | 2025-08-20 00:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| c510b989-f1cc-3a6e-aa78-84442b6a6f1b | -13.3346 | -54.4233 | 2025-08-20 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 087342b5-0ed0-3359-951c-bca2bd50b361 | -8.6342 | -62.1557 | 2025-08-20 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5f8a1259-de54-338d-b8d2-a2f394a6b86f | -20.3594 | -51.7023 | 2025-08-20 00:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7d9d38a1-274a-3014-aad2-414471e20f34 | -6.1476 | -57.7215 | 2025-08-20 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e154c1e0-5570-3a54-8187-d99874745c14 | -13.1555 | -54.9357 | 2025-08-20 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 178.6 |
| 2b2bfbaa-87e0-3e18-97af-596c4dce2a7a | -7.2787 | -50.1812 | 2025-08-20 00:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 74c66c5e-0a2f-3f93-8415-a8637ba4cf77 | -12.9775 | -56.8816 | 2025-08-20 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| f043fcaf-8ba7-3b93-95b6-f25070b73cb0 | -4.912 | -43.2337 | 2025-08-20 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 9b4036d9-914f-339d-af90-30b260c12544 | -13.1558 | -54.9151 | 2025-08-20 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 078c569c-aee8-3c33-8b65-1dc46dcf8ca0 | -3.982 | -42.516 | 2025-08-20 00:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 40.5 |
| 013f2f8b-cd1c-3d31-8f2e-6e3abf8255bf | -8.034 | -47.6639 | 2025-08-20 00:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| f7ab73d2-8105-3870-8679-4af84757a18e | -12.9778 | -56.8614 | 2025-08-20 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 62162928-5353-3484-9a55-effedab9e18c | -13.1364 | -54.9376 | 2025-08-20 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 872e1240-f04a-3011-9e45-2ab3f4b72c8d | -12.955 | -46.1504 | 2025-08-20 00:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| cad29d27-4788-3cfb-8ab2-a0c4dc9d86e4 | -12.9775 | -56.8816 | 2025-08-20 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 32d46c76-51e6-3803-8e01-2d640bdac38b | -7.2787 | -50.1812 | 2025-08-20 00:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 2acbd834-47db-3e70-9dfc-5c56d0fe4c98 | -8.034 | -47.6639 | 2025-08-20 00:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 79007fda-5fa4-304a-8244-49a938499ce4 | -4.4331 | -47.76 | 2025-08-20 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e73f3890-4097-3d8e-b05a-c5408629d63e | -6.9607 | -42.858 | 2025-08-20 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| 6e05404e-c4e2-37cb-98fe-b5cacb5ebf9a | -20.3594 | -51.7023 | 2025-08-20 00:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 3a71374f-de85-3f9a-a911-c4b7e7029834 | -15.0002 | -54.8135 | 2025-08-20 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 4c5c1048-60aa-32cb-b4ad-23a8b6f3a6d0 | -4.912 | -43.2337 | 2025-08-20 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| ace08f84-2392-3417-87ae-cbbb79a8abf8 | -20.339 | -51.7062 | 2025-08-20 00:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 150c474d-820a-31f9-9120-e3092c46b0a6 | -13.1367 | -54.9171 | 2025-08-20 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 20e646bf-070c-31c2-b2d9-04e20ef35e00 | -3.232 | -46.8056 | 2025-08-20 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| b16ea28a-5a82-3f9d-832a-56b76533d449 | -13.1558 | -54.9151 | 2025-08-20 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 1913db5b-009d-337f-aac6-80bb20196b49 | -6.1476 | -57.7215 | 2025-08-20 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 5d7ebec1-6b31-3c1b-81b6-ab2e9e330076 | -12.9778 | -56.8614 | 2025-08-20 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e2e084fd-242b-3547-86ee-f5deca11afa7 | -13.3346 | -54.4233 | 2025-08-20 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| bf1af94c-7acb-30da-8abd-ef9ecd9ac361 | -13.1555 | -54.9357 | 2025-08-20 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 3c9bb21c-ddf3-3edb-a75f-4fdb65a04de6 | -6.9605 | -42.8816 | 2025-08-20 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| d0e94380-9af3-3fd4-a863-a2707a36784d | -3.982 | -42.516 | 2025-08-20 00:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 53.9 |
| bb2701b3-9dd2-381f-bc32-89d1f5be3f15 | -11.7508 | -48.1825 | 2025-08-20 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 1ea1326a-93af-3426-8fbf-1a8ea63daef5 | -18.9816 | -50.3437 | 2025-08-20 00:50:00 | GOES-19 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 162.2 |
| 3311c00c-1c9d-345f-a814-d7473eb31a5e | -13.1364 | -54.9376 | 2025-08-20 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 4f84efa3-2876-3140-bdad-c6d078d6d63d | -20.339 | -51.7062 | 2025-08-20 00:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 137.7 |
| ac996137-1c55-3469-b4af-64f7cef71816 | -8.034 | -47.6639 | 2025-08-20 00:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b5124c26-07ca-3770-a722-baed788a8611 | -8.8736 | -62.4115 | 2025-08-20 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c885372c-8268-300c-a54c-b02fa9f40088 | -15.0002 | -54.8135 | 2025-08-20 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| adfc1fee-b417-373d-a0bf-ea7269d92b54 | -18.9822 | -50.3213 | 2025-08-20 00:50:00 | GOES-19 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| cd74368f-281c-3a5c-9768-9d6a0280408b | -3.232 | -46.8056 | 2025-08-20 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| ae018435-4448-388e-ab12-dcc4653178fd | -12.9357 | -46.1534 | 2025-08-20 00:50:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 6c069a45-01e0-3589-b497-4c5fc717b3f1 | -13.1555 | -54.9357 | 2025-08-20 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 147.7 |
| e16d599a-770f-3df4-93c1-b9d5b7d873bc | -9.2216 | -60.3302 | 2025-08-20 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 9741e705-dc6f-35cb-9c77-14b542f2be80 | -12.9778 | -56.8614 | 2025-08-20 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| c6e865ae-d48a-3ce2-9032-7cd6db40450d | -13.1558 | -54.9151 | 2025-08-20 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 6a0caceb-74d3-325e-aa64-07d06b393cd2 | -9.1895 | -59.6364 | 2025-08-20 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| b7bbe76e-d023-35fe-9b4e-4fb359eba0af | -4.912 | -43.2337 | 2025-08-20 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| fd630142-6baf-3cd6-a483-d9b92b8e8d4a | -6.9605 | -42.8816 | 2025-08-20 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 37.2 |
| 6e92a7b7-de7e-397e-ab30-723815a576d2 | -18.9615 | -50.3475 | 2025-08-20 00:50:00 | GOES-19 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 115.7 |
| 7048d9f2-01aa-318d-b015-236c2aaba2aa | -8.0152 | -47.6656 | 2025-08-20 00:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 8c9c19d9-f499-3896-9b19-fcee6a0f8a70 | -13.3349 | -54.4027 | 2025-08-20 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| e9dd1a38-1d8d-308f-8b83-7e8e31f8365e | -18.962 | -50.3251 | 2025-08-20 00:50:00 | GOES-19 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.6 |


[Clique aqui para ver as próximas entradas](README5.md)
