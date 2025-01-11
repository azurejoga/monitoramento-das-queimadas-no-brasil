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
| a7438555-2435-31fe-9e7a-1c2caceb6d4f | -30.483601 | -55.459499 | 2025-01-11 01:28:00 | METOP-C | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | nan |
| ab3e88b5-e9a8-3f92-a641-d90387919e52 | 2.2941 | -60.4645 | 2025-01-11 01:28:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 16d6b9a4-ee08-31ad-8579-8df72165aa41 | -19.141899 | -55.400101 | 2025-01-11 01:28:00 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 08e4028a-1087-3c45-89ab-5b55b99eaf11 | 3.9356 | -60.5825 | 2025-01-11 01:28:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2c0dc129-7b7b-3515-b1e8-642a2a2bfba7 | 2.2958 | -60.457001 | 2025-01-11 01:28:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 737db21a-f4ef-31b6-9d70-6f95a29415d3 | 2.2843 | -60.462299 | 2025-01-11 01:28:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d7b37460-7bef-3b5d-8ca5-0b24064bac00 | -19.3172 | -54.481602 | 2025-01-11 01:28:00 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7f58e436-2389-3848-b850-19992f264d58 | 3.7645 | -60.110802 | 2025-01-11 01:28:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 025a2dd0-f435-36fa-9068-4529728b1f2d | 3.029 | -61.2183 | 2025-01-11 01:28:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4fd5e351-5f81-355d-b358-e79866ea1f48 | 3.7314 | -60.3022 | 2025-01-11 01:28:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 917a394b-1e3b-3da1-bcf4-9c093e010127 | -15.7585 | -58.244999 | 2025-01-11 01:28:00 | METOP-C | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dad1875a-11f0-3f35-826d-80737f27fa72 | -22.001101 | -57.316799 | 2025-01-11 01:28:00 | METOP-C | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6be03c3d-45ad-3f95-a118-157fcf07811f | 3.0388 | -61.220402 | 2025-01-11 01:28:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d6081def-1ea3-3945-a1fa-9bdd4c1497ea | -15.7601 | -58.252102 | 2025-01-11 01:28:00 | METOP-C | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df8b8502-215f-321d-b0d9-163934a51ac3 | 1.6686 | -60.4967 | 2025-01-11 01:28:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 14c17227-e3cf-3923-ad2c-71d750d408fb | 2.286 | -60.4548 | 2025-01-11 01:28:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fa344594-4a8f-3681-884c-31518ba4711b | 1.6703 | -60.489399 | 2025-01-11 01:28:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 93e15113-f119-3c29-81ca-0a3b806ce630 | 2.3384 | -61.399601 | 2025-01-11 01:28:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e21c5dde-7394-3021-af0b-a5e73cbc26dd | 4.0075 | -60.992699 | 2025-01-11 01:28:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9fbd269c-3c60-3cd6-9930-f6bdefe7ae0e | -19.139999 | -55.3922 | 2025-01-11 01:28:00 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b9e97208-badb-34fe-b233-0418fe79fc06 | 1.6605 | -60.487202 | 2025-01-11 01:28:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3b415769-7fcd-38b5-abe4-b2083a289cb1 | -20.8304 | -49.2901 | 2025-01-11 01:28:00 | METOP-C | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a3701c4-daed-3282-b015-bb884742174c | 3.0372 | -61.2276 | 2025-01-11 01:28:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e186d899-13ec-3e24-9866-6787bc93363f | -21.66645 | -56.93125 | 2025-01-11 01:28:00 | TERRA_M-M | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1e6f25e1-bd1e-37a6-b99a-ee6ffb97321d | -25.64563 | -50.18003 | 2025-01-11 01:28:00 | TERRA_M-M | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 4228ad67-c9ea-35cf-bf5d-602a6dc91923 | -21.17148 | -49.22165 | 2025-01-11 01:28:00 | TERRA_M-M | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 3a322a33-ae78-32d2-8443-5092606ab4ea | 2.6703 | -61.169 | 2025-01-11 01:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 98fd3a24-627b-3607-b146-d7cedd716592 | 1.9236 | -60.4019 | 2025-01-11 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 2e8ab489-8d41-3a4a-9d7f-e959af0a0859 | -19.7026 | -58.0309 | 2025-01-11 01:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 5d9fc3aa-630a-3c2c-b6fd-324b77040ba2 | -19.71516 | -58.02954 | 2025-01-11 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 3fb7152a-28e6-375c-b932-189e74024181 | -19.7073 | -58.02619 | 2025-01-11 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.7 |
| 4ca3fe52-f5d7-3431-885f-f8dc860f9d48 | -19.66365 | -54.41556 | 2025-01-11 01:30:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 39a6bfab-0713-3666-b70c-eee97b71f713 | -19.16285 | -54.83432 | 2025-01-11 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 00885c06-321d-3dc4-87a3-82a13e7d8ef6 | -19.66215 | -54.40543 | 2025-01-11 01:30:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0add42cf-b679-3488-ab79-61bfd766208d | -19.49273 | -55.32719 | 2025-01-11 01:30:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| a17c7a82-9e86-359f-b553-45530026324d | -19.66995 | -54.40801 | 2025-01-11 01:30:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 420375af-2d25-3b37-ae66-29fb898c5b87 | -19.1643 | -54.84424 | 2025-01-11 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b930e79d-534e-3140-8e7a-f264c1fe9aec | -19.48516 | -55.33822 | 2025-01-11 01:30:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| b64cdec6-4c9d-3940-9adf-f6ca4c63f4ac | -19.49411 | -55.33675 | 2025-01-11 01:30:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 495f2bd8-89ca-3c4c-8bf2-af320bbf8ef3 | -16.10738 | -58.19349 | 2025-01-11 01:32:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| f69776a6-5cef-302d-9b64-0234501f73ff | 1.31136 | -60.44781 | 2025-01-11 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 38d7e48a-8ac3-3999-8e36-b952772945fe | 1.17545 | -60.50301 | 2025-01-11 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 65022bcd-5eb0-3e58-b322-e48381249a4d | 1.92509 | -60.41517 | 2025-01-11 01:34:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0ecc22b9-1232-3c20-8c16-118c71bbc755 | 1.31259 | -60.43902 | 2025-01-11 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7270c949-421a-3593-958f-d7f734f7de35 | 1.93516 | -60.4076 | 2025-01-11 01:34:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 14d7ee5b-d1c1-3f7c-a58f-7e59f9b39f92 | 1.93638 | -60.39878 | 2025-01-11 01:34:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6794cc29-7e3d-3bed-a435-1faa0b26b6d9 | -3.46219 | -53.95901 | 2025-01-11 01:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5f822458-6500-3cf7-8cfd-53f2a8a37d8c | 1.31381 | -60.43023 | 2025-01-11 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| d2f63b9a-b927-3de2-aa95-7a45679b1e78 | 1.92632 | -60.40634 | 2025-01-11 01:34:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| fb72bf0f-7c04-3c7f-b584-b785457c4468 | 1.93393 | -60.41644 | 2025-01-11 01:34:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6aaa89df-f335-35c6-874f-08bd3609fa70 | 2.67721 | -61.16716 | 2025-01-11 01:36:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| d25e7f51-a7e6-3461-a4a3-df42689d0825 | 3.39975 | -60.2848 | 2025-01-11 01:36:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 99c669db-d092-3d61-9cb9-4161b221bf55 | 3.37672 | -60.25407 | 2025-01-11 01:36:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 17.1 |
| b75f2a89-9c7c-39c6-b3bc-238f2fcb48d4 | 3.41295 | -60.05622 | 2025-01-11 01:36:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 48b477cf-f34c-3cdd-8d48-04722a8a5667 | 3.57837 | -60.52272 | 2025-01-11 01:36:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 62c35b02-d9fc-3cb9-9812-a94cf60f3ddf | 2.67599 | -61.17593 | 2025-01-11 01:36:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 109.6 |
| ac150fbc-2c51-3e84-90ec-408f8cd576d3 | 3.31063 | -59.99248 | 2025-01-11 01:36:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32cd8502-1659-309f-86d6-6cda98e5a2d0 | 3.65061 | -60.94185 | 2025-01-11 01:36:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 22f94bc8-ea4e-397c-8252-de43166f337f | 3.40099 | -60.27581 | 2025-01-11 01:36:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d9ba1014-201a-3848-bffe-b273f2b6dcd5 | 3.37548 | -60.26308 | 2025-01-11 01:36:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ae9bc5d2-2a84-3c58-b7a5-474ae154f068 | 2.20683 | -60.24781 | 2025-01-11 01:36:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0cfe7fc1-a393-342d-aa11-9115ee06345e | -19.7026 | -58.0309 | 2025-01-11 01:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 14303c33-45f0-375a-8ab5-abaa8871f551 | 2.6703 | -61.169 | 2025-01-11 01:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c6e54468-6c5c-3baf-9b77-e5bf3578b4c9 | 1.9236 | -60.4019 | 2025-01-11 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 818f3cf7-cb04-34d3-ba04-f680e3548d79 | 1.9419 | -60.4017 | 2025-01-11 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d0f44ec1-f3db-3a44-8826-c0b7045113f6 | 2.6703 | -61.169 | 2025-01-11 01:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 60609d15-b25d-34c8-856d-0bcf5602da5f | -19.7026 | -58.0309 | 2025-01-11 01:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| ae3f51dc-fba0-31ea-aa94-bee21a415512 | -19.7026 | -58.0309 | 2025-01-11 02:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 44f5154b-e4b1-3273-908e-792026057bd2 | 2.6703 | -61.169 | 2025-01-11 02:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| adabce0a-605b-3974-8c17-2414f8799727 | -19.7029 | -58.0102 | 2025-01-11 02:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.3 |
| f0d01d0a-9020-365d-9d4e-f0c90ccb4055 | 1.9236 | -60.4019 | 2025-01-11 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 550ca153-5d8e-30f5-a40d-fb00c4313e44 | 2.6703 | -61.169 | 2025-01-11 02:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 717c924b-9d42-365c-8eb8-659fa9625833 | -9.259 | -60.309 | 2025-01-11 02:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 9c27f67f-79b5-3c82-9cdd-0117e922f005 | -19.7029 | -58.0102 | 2025-01-11 02:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 656f9583-c26b-315e-a918-0aa8bd55147e | -19.7026 | -58.0309 | 2025-01-11 02:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 4673a9fc-bca1-35d2-b404-437a5049d900 | 1.9236 | -60.4019 | 2025-01-11 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| cea69714-30cb-3709-997c-a0fa6fa1f9a6 | -19.7026 | -58.0309 | 2025-01-11 02:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.5 |
| ff53a42c-493e-37a9-b21b-6967c4ef8200 | 2.6703 | -61.169 | 2025-01-11 02:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ee76e9a5-fb41-39cf-b21a-7b6292b85922 | -19.7026 | -58.0309 | 2025-01-11 02:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 50f9d0ed-dded-3507-b25f-cdace4a435d9 | -19.7029 | -58.0102 | 2025-01-11 02:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.3 |
| d6bf4625-c0db-3883-823c-14818cd1fa45 | -19.7026 | -58.0309 | 2025-01-11 02:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| d1716d95-fd5e-3dbd-a910-5816f668660d | -19.7029 | -58.0102 | 2025-01-11 02:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| d9a7bf8d-18ca-3dc1-b978-e01cd2ead1d1 | -19.7026 | -58.0309 | 2025-01-11 02:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.8 |
| 49133c86-36fb-3326-9989-cbef986b2eee | -19.7029 | -58.0102 | 2025-01-11 03:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 136f5921-11b9-3b75-9e5e-ae6df22e1b6f | -19.7026 | -58.0309 | 2025-01-11 03:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| cd079cb3-1cda-32dc-978d-fa2210bb5f19 | -19.7029 | -58.0102 | 2025-01-11 03:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| ce37ec51-286d-3764-81f1-b370ab6d8614 | -19.7026 | -58.0309 | 2025-01-11 03:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 44014f37-5307-39f2-b301-1abac0d1fc35 | -5.40305 | -35.69312 | 2025-01-11 03:10:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 78cbca21-da77-3813-87e0-2b488d05bb1e | -22.7418 | -42.95859 | 2025-01-11 03:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a91607fe-5809-3ae4-8007-f4bb476af572 | -22.74071 | -42.96325 | 2025-01-11 03:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3017b0bc-110b-3875-8115-377b652f797c | -22.73487 | -42.96169 | 2025-01-11 03:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbd0a77e-cc8b-3248-82c7-bb79b5ff1d74 | -22.73596 | -42.95704 | 2025-01-11 03:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b9cd8296-3fe3-39b8-86a2-f49e0b8250f8 | -20.41628 | -43.55586 | 2025-01-11 03:17:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 600e5422-a9d5-3841-90cd-7b68ec377b0d | -19.7026 | -58.0309 | 2025-01-11 03:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 372e9bea-7770-3c43-b53a-5d83faa2fad5 | -19.7029 | -58.0102 | 2025-01-11 03:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 076cdecd-5d88-30e8-bc90-a9ea1404fec2 | -19.7026 | -58.0309 | 2025-01-11 03:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 15fcd42f-a959-3d13-b8e8-1edde0f70cac | -19.7029 | -58.0102 | 2025-01-11 03:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| da88b305-fcf4-3ed8-b5bf-9764340de4dd | -4.5324 | -42.93713 | 2025-01-11 03:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44b10c95-e295-323e-a033-1514c40a8bd0 | -4.52688 | -42.93618 | 2025-01-11 03:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70b44cb0-f8de-3abe-be49-a8164c505bd8 | -2.91859 | -40.42635 | 2025-01-11 03:36:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
