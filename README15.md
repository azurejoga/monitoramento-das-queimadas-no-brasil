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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ab1e60f-e3ce-3219-9597-e5de79d5fa60 | -16.3226 | -57.0662 | 2024-10-16 01:06:38 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.2 |
| ba434415-607e-3d04-9e55-9f69a198bb8e | -17.2439 | -42.6575 | 2024-10-16 01:06:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 109.8 |
| d9d88107-900a-3a4d-a933-6bd334f774cf | -17.2639 | -42.6527 | 2024-10-16 01:06:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 1390f066-ea2f-39ae-a549-bdff90ea7e8e | -17.3041 | -42.643 | 2024-10-16 01:06:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6acf2f03-62a5-3f8a-ac78-92caa6174d9d | -16.935 | -57.8538 | 2024-10-16 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 53a7e3d9-38c4-3aae-93e5-1a83f3e7de22 | -16.9546 | -57.8516 | 2024-10-16 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| f9e62d8c-69ac-3cac-9aca-a6e88a013748 | -16.9549 | -57.8312 | 2024-10-16 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 3350d0f3-4583-347f-a01a-cff889a9cbcd | -16.9742 | -57.8494 | 2024-10-16 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| c21dff44-62ed-33f3-a06e-a78649692dad | -16.9745 | -57.829 | 2024-10-16 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| e3d40a98-ced1-3774-98c8-af04b526dad3 | -16.9154 | -57.856 | 2024-10-16 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 051699fb-e76a-3854-ad08-0a433303533f | -17.0066 | -58.2934 | 2024-10-16 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| c35836ad-14a5-381a-93d2-8c43f8bcc9eb | -17.1951 | -57.4972 | 2024-10-16 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.9 |
| e4ef038c-55ef-374f-a5c7-52d7daeb8eb9 | -17.1954 | -57.4767 | 2024-10-16 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 63d2876d-3731-3f53-900b-0e700c141a8d | -17.1754 | -57.4995 | 2024-10-16 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 9b5e1dcb-4491-35c2-81dc-20414786228c | -17.2157 | -57.4334 | 2024-10-16 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 3326ae75-757b-38d5-83b4-034e42a98b07 | -17.2177 | -57.3102 | 2024-10-16 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| 8e8bc752-07f4-3971-a375-168c951feab1 | -18.2544 | -56.5821 | 2024-10-16 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 161.8 |
| 5f13dd61-ba73-317c-835c-ecc651156cd5 | -18.2548 | -56.5613 | 2024-10-16 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.4 |
| fb690fa4-063a-310f-bca3-b69f85e0ecd8 | -18.2739 | -56.6003 | 2024-10-16 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 7d66a159-9121-3aca-bd46-88473686ceae | -18.2742 | -56.5795 | 2024-10-16 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 291.6 |
| 554d71dd-1142-3e22-bb3e-200da340ff71 | -18.2746 | -56.5587 | 2024-10-16 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.4 |
| 6231406e-f401-3b07-afd5-b6d7cf436541 | -19.5615 | -56.968 | 2024-10-16 01:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.7 |
| 655e87e8-19f9-3f17-8f88-5ab176017c29 | -19.5619 | -56.9471 | 2024-10-16 01:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.2 |
| d3b3b174-fbb6-3684-8eb2-fa6039029c08 | -19.5812 | -56.9862 | 2024-10-16 01:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.5 |
| ad7cea98-e336-3833-b173-1b6306c67048 | -19.5816 | -56.9653 | 2024-10-16 01:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 162.5 |
| bdff9855-07d9-3205-bf3d-640847613c55 | -19.6013 | -56.9834 | 2024-10-16 01:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.6 |
| a03a211b-268c-3f51-b6cf-9ad6d55d632a | -20.8536 | -49.8742 | 2024-10-16 01:07:01 | GOES-16 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.7 |
| bc5dfd0f-b5a1-3348-a891-37620eb8a69e | 1.0016 | -52.2164 | 2024-10-16 01:15:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b293c104-2d46-34a0-ae2e-60632e089158 | -3.1098 | -54.2464 | 2024-10-16 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| b0a7dc8d-a5f0-327a-8030-b4099706eb52 | -3.1099 | -54.2263 | 2024-10-16 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 180.7 |
| 51ad192c-25a1-326c-b1ca-91c71baaae91 | -3.11 | -54.2063 | 2024-10-16 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f2a66342-8e66-3693-a56b-a1f1b13c1d90 | -3.1282 | -54.2459 | 2024-10-16 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 2e884e87-54a5-3e57-b833-6caff3516ba1 | -3.1283 | -54.2259 | 2024-10-16 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 5dfeee11-8fb8-39ec-b9e6-17a6bdd55543 | -3.2225 | -48.9306 | 2024-10-16 01:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 93b97715-df56-3daf-9b1f-232a59ec5deb | -3.2226 | -48.9092 | 2024-10-16 01:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 2485c72b-970d-3a18-b9f1-4f930f044d4a | -3.3918 | -44.5607 | 2024-10-16 01:15:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 9957304f-4375-3775-bb20-0891be7756aa | -3.4104 | -44.5599 | 2024-10-16 01:15:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 253a3a6f-7e31-3669-b3bf-5200ed27c6ff | -3.958 | -46.4442 | 2024-10-16 01:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 03de823c-72ff-3c3e-b5ed-9cca3426c15e | -3.9581 | -46.422 | 2024-10-16 01:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 96.0 |
| b6fbf03f-cf64-36fc-b25d-6cef15a57e9b | -9.1727 | -65.4132 | 2024-10-16 01:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| fe7f7a31-98c4-3640-93b1-dd5363d218ba | -9.1728 | -65.3945 | 2024-10-16 01:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 20db3914-19d0-3785-8970-8d0f84b87d70 | -9.9983 | -48.6295 | 2024-10-16 01:16:02 | GOES-16 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 811baf48-389b-3908-bac5-ab92237ac0ea | -10.822 | -49.256 | 2024-10-16 01:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 3d18a5dd-e5e3-315d-b21b-874c07d84710 | -10.8224 | -49.2343 | 2024-10-16 01:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| bc4a5c92-d426-3c3e-81a0-79d904f5d8b5 | -11.6915 | -65.2432 | 2024-10-16 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 516e54f9-c2e1-3fd1-acb7-f43f1995d271 | -11.6917 | -65.2243 | 2024-10-16 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 7bb79c06-e9ad-3eac-8899-ce19f714d2e3 | -11.6918 | -65.2054 | 2024-10-16 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| c2a0c9d1-9cc4-34a8-9ad3-87a45d1e2cd7 | -11.7103 | -65.2424 | 2024-10-16 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 5fa005a9-f963-3fb3-ba3e-7489e8385936 | -11.7104 | -65.2235 | 2024-10-16 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 171ce55a-d4a3-3c44-87a1-eabb1ba50818 | -11.7106 | -65.2046 | 2024-10-16 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| cd2fc18f-271f-39a2-b0cd-433193bc0aea | -12.4925 | -47.2818 | 2024-10-16 01:16:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 1fd12acb-7eae-3f08-bd30-9168d8a1f827 | -12.3795 | -63.7103 | 2024-10-16 01:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 923db442-7ef9-3111-9cfc-629b82d5b21c | -12.3983 | -63.7093 | 2024-10-16 01:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 699a9614-4304-3cdb-95fa-1edde83d46cc | -13.383 | -46.947 | 2024-10-16 01:16:21 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 71eb64f7-4439-3478-8dc4-5778ddf5b02b | -17.2439 | -42.6575 | 2024-10-16 01:16:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 104.1 |
| ce426890-c743-3660-a2b2-fca1541e3875 | -17.2639 | -42.6527 | 2024-10-16 01:16:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 7bffb012-44f0-31af-9816-dc21331f5d72 | -17.3041 | -42.643 | 2024-10-16 01:16:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 74a25063-a5f6-3d2f-b125-15a1ab98f6a2 | -16.9403 | -57.5063 | 2024-10-16 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 9770d2c2-f28a-301e-bd4f-e57a5f8aaa1a | -17.0066 | -58.2934 | 2024-10-16 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 78f74138-d4b0-3079-836a-fa249c33bea3 | -17.553 | -42.3096 | 2024-10-16 01:16:43 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0e964a92-44df-3c05-b97b-8f28340931a1 | -17.1951 | -57.4972 | 2024-10-16 01:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 1b56ced2-3df0-3a9a-a128-4583f4c1bf0c | -17.1954 | -57.4767 | 2024-10-16 01:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 595b5335-4159-3af3-ad4b-61ab6c9d23f4 | -17.2177 | -57.3102 | 2024-10-16 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 264f0cdf-73c8-3b34-b3e9-f685cc0e3e4b | -17.2373 | -57.3079 | 2024-10-16 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 7b7246c0-eb49-39de-b504-d653c449a23c | -18.2544 | -56.5821 | 2024-10-16 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 182.4 |
| 66815f3f-baf2-3a38-9612-e0069e737232 | -18.2548 | -56.5613 | 2024-10-16 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 0530ba1c-d10e-391c-9548-b8637f2992a5 | -18.2739 | -56.6003 | 2024-10-16 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.8 |
| 2c0d9c1c-51f5-36ab-8d94-4f2b6f69bfaa | -18.2742 | -56.5795 | 2024-10-16 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 341.0 |
| 6e2fde08-bda9-35ba-aff1-e473e2139d79 | -18.2746 | -56.5587 | 2024-10-16 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.3 |
| d02c3cc7-c45d-3e97-b195-6d2eb8e25d96 | -19.6987 | -46.7849 | 2024-10-16 01:16:55 | GOES-16 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c2f78c18-51ff-3c5c-888d-dab1ade07b08 | -19.719 | -46.7802 | 2024-10-16 01:16:55 | GOES-16 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 00a938b4-482c-365a-8abf-76c149ca9f9f | -19.5615 | -56.968 | 2024-10-16 01:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.3 |
| 326d67d6-91c1-3d92-beb5-6a55168f5f8b | -19.5619 | -56.9471 | 2024-10-16 01:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 82287bc1-fae5-3d4c-a687-dc0fefcade8a | -19.5812 | -56.9862 | 2024-10-16 01:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.3 |
| 40e4b1b6-ab57-3e77-a4de-fe646cf46cc2 | -19.5816 | -56.9653 | 2024-10-16 01:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.7 |
| 74ced445-4777-3dde-a6f6-2b56201371fe | -19.6013 | -56.9834 | 2024-10-16 01:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.9 |
| b1793614-bf73-3bdc-8e00-6136470e222c | -19.6016 | -56.9625 | 2024-10-16 01:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.2 |
| b6e1339c-8719-3912-8cb0-0be322485559 | 1.0016 | -52.2164 | 2024-10-16 01:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 544a1073-c371-3136-b19c-2e67be283cbf | -3.1098 | -54.2464 | 2024-10-16 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| d251e84e-8aa1-3fd3-bc4c-558957d6f0d7 | -3.1099 | -54.2263 | 2024-10-16 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 183.3 |
| b3340a6e-b644-3e71-807c-d5b07ab248c1 | -3.11 | -54.2063 | 2024-10-16 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 388c5f8f-066a-334d-8e60-cecfc11b751d | -3.1282 | -54.2459 | 2024-10-16 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| f91930de-8f02-38f8-92cd-cbbee681e936 | -3.1283 | -54.2259 | 2024-10-16 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 5927c1c5-e88d-3eea-98c3-e27df091958b | -3.2225 | -48.9306 | 2024-10-16 01:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3d2777a2-63ef-3e7a-b854-d3af0fae4496 | -3.2226 | -48.9092 | 2024-10-16 01:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 6ae1fbeb-885a-38fe-9466-8cd2dd0f984e | -3.3918 | -44.5607 | 2024-10-16 01:25:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 341266ec-de9f-3053-90cd-10329de6e41a | -3.4104 | -44.5599 | 2024-10-16 01:25:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 1bcf8b79-3bd3-3fae-908a-2f5716a909db | -3.958 | -46.4442 | 2024-10-16 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 315b92f5-c3cf-38be-8257-e40aa9d21086 | -3.9581 | -46.422 | 2024-10-16 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 699857f0-ae0f-3de4-adf6-9dcfb085afe3 | -9.1706 | -47.0014 | 2024-10-16 01:25:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 67ee5771-13d3-3eb4-8e0a-84e95b689587 | -10.822 | -49.256 | 2024-10-16 01:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 81f6b33a-8955-3926-8a1d-634e8f8d819f | -10.8224 | -49.2343 | 2024-10-16 01:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 322290f0-0ae3-374d-b077-b8fd072582b0 | -11.6915 | -65.2432 | 2024-10-16 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f6802fd3-1e6d-3cf1-a140-5d02dcec309d | -11.6917 | -65.2243 | 2024-10-16 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 48f4a18c-6c6d-35d9-a598-eabf02383b67 | -11.6918 | -65.2054 | 2024-10-16 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b7289ab9-ebfb-30b8-b364-6994517f267d | -11.7103 | -65.2424 | 2024-10-16 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 177197ba-a88f-3dda-b2fa-1ad68c068864 | -11.7104 | -65.2235 | 2024-10-16 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 4d941af5-e2e2-3ae1-8d52-2426b7099f60 | -11.7106 | -65.2046 | 2024-10-16 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| a67b2c1f-7aa6-3211-9dd0-8eb4d6f00f38 | -12.0427 | -46.7161 | 2024-10-16 01:26:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 30bed1aa-d2a6-3f7a-becc-3c78ccd64f3e | -12.0431 | -46.6935 | 2024-10-16 01:26:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |


[Clique aqui para ver as próximas entradas](README16.md)
