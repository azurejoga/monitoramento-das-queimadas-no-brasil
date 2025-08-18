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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66882d43-b998-3910-b613-60b615dd94ce | -5.7912 | -43.883202 | 2025-08-18 00:09:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51170969-ae5d-3060-872a-a48452bd1771 | -17.1625 | -46.211498 | 2025-08-18 00:09:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fb3ae6b0-fcd3-305d-99b7-ea6490df31e9 | -4.7819 | -45.318699 | 2025-08-18 00:09:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1de0e4c-31ff-30f2-a341-0322e4515b16 | -6.082 | -44.606998 | 2025-08-18 00:09:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39d77c61-8519-3ba7-b0af-f40ef18df781 | -3.7871 | -40.984798 | 2025-08-18 00:09:00 | METOP-B | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9c58a151-876f-3bef-8b7e-af48ac9a4616 | -6.5659 | -44.470402 | 2025-08-18 00:09:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f779f855-2516-34ef-a851-e5edee59e5bd | -10.953 | -45.168301 | 2025-08-18 00:09:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2e3298b-5455-352d-8d4b-54ee865112a7 | -17.6299 | -44.291199 | 2025-08-18 00:09:00 | METOP-B | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 48e1f1c3-6a44-32d2-a8af-d4592bc9f9f0 | -6.5561 | -44.472698 | 2025-08-18 00:09:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0eccaf7a-68dd-3dba-967f-2c99e1ee2c89 | -15.0072 | -54.774899 | 2025-08-18 00:09:00 | METOP-B | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 63f62065-07bd-37fc-bbdb-3a76acf14471 | -3.5907 | -47.516499 | 2025-08-18 00:09:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6390899c-4742-32f9-b9fa-3c2a8030762f | -6.4327 | -44.7869 | 2025-08-18 00:09:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92c57220-29af-3f7d-8161-95346f254bca | -18.0494 | -43.8148 | 2025-08-18 00:09:00 | METOP-B | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ad848d11-0821-3a9a-b38d-a10ff563e5ec | -3.971 | -42.5177 | 2025-08-18 00:09:00 | METOP-B | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 91820dd0-9da1-382b-b525-7342d5e85bd2 | -23.133801 | -46.943699 | 2025-08-18 00:09:00 | METOP-B | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 16d580be-d318-32e9-b59e-ccae6ad53cb6 | -9.8757 | -44.6945 | 2025-08-18 00:09:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d7986079-fc4e-323c-9a58-76101c34a08c | -6.1924 | -53.502201 | 2025-08-18 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c36a4a0-1fe6-328f-a458-0e065083db85 | -18.614201 | -42.4384 | 2025-08-18 00:09:00 | METOP-B | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aaa7d587-3722-3a99-bec7-14de094efa4f | -3.5923 | -47.523399 | 2025-08-18 00:09:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a09196e3-b2b5-3a4f-9362-0871d0b2f22a | -7.5707 | -45.435299 | 2025-08-18 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efbe0eed-155c-3681-a48f-1ec6b1616e0c | -18.6124 | -42.4305 | 2025-08-18 00:09:00 | METOP-B | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 65cb62c0-ee88-3b71-9546-31468b2b1b0c | -12.4938 | -45.558102 | 2025-08-18 00:09:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a8ef9a5-20f2-3135-adfc-a72fea0c091b | -7.5511 | -45.4398 | 2025-08-18 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3886ae2c-5798-30dd-bd41-915054e3c7cb | -22.145901 | -44.823299 | 2025-08-18 00:09:00 | METOP-B | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6e7d2839-aa9f-3217-b36e-77a14ac32b1a | -13.1728 | -54.915901 | 2025-08-18 00:09:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c23030ac-8a47-321a-b924-120685be2e50 | -28.844801 | -54.041599 | 2025-08-18 00:09:00 | METOP-B | JÓIA | RIO GRANDE DO SUL | Brasil | 4311155 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 9a95d676-412c-3b76-8407-45d94fd3c30b | -22.8193 | -45.054199 | 2025-08-18 00:09:00 | METOP-B | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c141d5af-e568-3808-96a2-960df1a29dea | -3.5938 | -47.5303 | 2025-08-18 00:09:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b58f529-cbdd-3f0e-aabf-653979414772 | -23.316099 | -46.884499 | 2025-08-18 00:09:00 | METOP-B | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 93c5b754-172f-3fcf-af30-bcc80c18d0ce | -22.715099 | -47.417099 | 2025-08-18 00:09:00 | METOP-B | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a5bc09d-9762-388c-8b37-5660528634ea | -12.6354 | -46.8969 | 2025-08-18 00:09:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41829f02-bf43-3a59-885a-d5cbb29c3b6d | -11.333 | -48.3759 | 2025-08-18 00:09:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db70c8bf-4e31-39b5-9c89-f7b4a8d6afa9 | -3.9762 | -42.5401 | 2025-08-18 00:09:00 | METOP-B | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 566a1630-5cde-321f-b4e1-21f3cdd13fdc | -11.0001 | -45.650398 | 2025-08-18 00:09:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e21f525-de6c-38ef-a33f-15fb79b78dfe | -6.7384 | -50.951099 | 2025-08-18 00:09:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7062d1a1-83c1-3df1-b75a-03ca40339a8c | -10.9969 | -45.636299 | 2025-08-18 00:09:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f4c3ef6-c3e8-389e-b070-cd4ebffe850a | -6.5622 | -44.454102 | 2025-08-18 00:09:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebfae46d-34f8-3e45-acd4-c9ef1ae7d650 | -5.9905 | -44.120998 | 2025-08-18 00:09:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 984e1d64-6b1e-3ed5-98e6-a609773d2ed5 | -10.9985 | -45.643398 | 2025-08-18 00:09:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 33b7362d-ee89-365e-b4ba-10ce47fb4dd5 | -23.3144 | -46.8755 | 2025-08-18 00:09:00 | METOP-B | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ff86c4f-da10-3834-a712-78a24e63fb46 | -13.5906 | -47.7528 | 2025-08-18 00:09:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3f8e16f9-fbea-372a-bd58-402ba733a5d1 | -17.1656 | -46.2262 | 2025-08-18 00:09:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 542384e5-e87e-3124-9b10-a89993883104 | -7.5495 | -45.432499 | 2025-08-18 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe3bad90-6091-3e5a-8f02-81f98f29ee83 | -7.8042 | -45.1488 | 2025-08-18 00:09:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 64058972-dabb-3c4c-b097-b70c20dd5f32 | -22.853701 | -46.240398 | 2025-08-18 00:09:00 | METOP-B | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e36bee74-60a6-3e6e-bfee-86fb48078e8c | -13.2239 | -50.762299 | 2025-08-18 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f4061bc-d56a-3130-b7f5-5e0d44c6fefa | -17.162901 | -43.359699 | 2025-08-18 00:09:00 | METOP-B | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 21952794-8eb2-3d96-a1be-be2930d500f8 | -13.1655 | -54.876999 | 2025-08-18 00:09:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25c45afe-2d70-3255-8c1f-5841968c33c8 | -7.5691 | -45.428001 | 2025-08-18 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fce01fa7-191e-3e8f-9615-045f78df0f4a | -6.6359 | -43.8815 | 2025-08-18 00:09:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b80e35a6-29c1-3b1a-bce6-03fdfbeb06a3 | -13.2533 | -50.756199 | 2025-08-18 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e73c5180-4f76-313e-a90d-e67ea0c9630d | -3.9807 | -42.5154 | 2025-08-18 00:09:00 | METOP-B | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3a486468-f45c-3ae3-ad3c-71443869c6db | -8.0323 | -47.668201 | 2025-08-18 00:09:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f45a55a3-bf26-3fa7-a64c-631a96be8045 | -10.9513 | -45.161201 | 2025-08-18 00:09:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 639e70c5-b8d6-3427-aea5-91e1f42f76ab | -5.1529 | -48.097 | 2025-08-18 00:09:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 18bf6c12-13c3-3191-885e-e0a34b07dff7 | -3.7774 | -40.987099 | 2025-08-18 00:09:00 | METOP-B | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6db46952-c8b0-33ee-9a9f-06b917ede561 | -3.9833 | -42.5266 | 2025-08-18 00:09:00 | METOP-B | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2b8ba4af-f13f-3947-bcae-cec08791cc92 | -13.226 | -50.772701 | 2025-08-18 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 86da1a26-2805-3430-9ca2-ada3e30eddb7 | -4.921 | -43.240101 | 2025-08-18 00:09:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e844e524-8a0c-3fe4-8a57-5531c2532aa7 | -3.7905 | -40.999199 | 2025-08-18 00:09:00 | METOP-B | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 62cd08ce-d5f2-3613-8a81-a89ddb04f935 | -13.1324 | -57.0923 | 2025-08-18 00:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b75272f5-ad17-383b-b5e7-e2780c1556f2 | -7.5593 | -45.430199 | 2025-08-18 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 263d749c-9104-3085-8b4a-a9cd08747be4 | -12.9823 | -56.815102 | 2025-08-18 00:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31836ebd-5e5c-3ee8-8e71-5d900215d694 | -13.1789 | -54.894501 | 2025-08-18 00:09:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 363e816f-ba41-3fb8-b32f-4854a9b54206 | -11.3314 | -48.368401 | 2025-08-18 00:09:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 952c2342-a3da-3fe3-b896-93d384eafa8b | -11.8493 | -51.5728 | 2025-08-18 00:09:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea73d2f9-0ebd-3ed7-a578-1e1b66b9aa7e | -12.1328 | -47.8951 | 2025-08-18 00:09:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0528e8f5-51a0-3cf1-a4ae-f2c11e91d56b | -18.551001 | -43.984901 | 2025-08-18 00:09:00 | METOP-B | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e8eedcb0-2104-36cb-8c79-cd4b89185c8c | -17.856701 | -42.512402 | 2025-08-18 00:09:00 | METOP-B | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a1180c8-b85f-3d63-8a00-fa4ecbd832eb | -13.9822 | -48.099899 | 2025-08-18 00:09:00 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9ff7f0bb-733e-3f32-a03c-ff15c906aee7 | -7.5251 | -45.461102 | 2025-08-18 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b8fa44e-0d41-392c-b87d-6039d1d83d82 | -8.2263 | -47.291401 | 2025-08-18 00:09:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0669cd7-dd0c-38b9-aacc-585b5a2ac16a | -17.098499 | -49.859001 | 2025-08-18 00:09:00 | METOP-B | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 245c1d75-342f-348a-b5d3-65629f68a406 | -5.665 | -43.383202 | 2025-08-18 00:09:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f4218d0-6323-30cc-bcf5-fe9b55bc12f6 | -18.337601 | -49.428299 | 2025-08-18 00:09:00 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7a14ada8-9cac-3451-a239-f27034d27e33 | -7.5234 | -45.4538 | 2025-08-18 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a5dfd97-40eb-3783-97cf-1e456738f3fb | -21.4305 | -43.874599 | 2025-08-18 00:09:00 | METOP-B | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 705525f7-b997-3ba6-a22b-610b82ab6e63 | -13.1374 | -57.1199 | 2025-08-18 00:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14223448-4f35-3917-ae47-9b2ef422f36f | -4.9112 | -43.242298 | 2025-08-18 00:09:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 739e9427-d444-3d0f-aa4e-906dfeed084b | -6.4335 | -44.7822 | 2025-08-18 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 52b8a59a-d504-3c0e-a3fc-19f3df2c14cc | -21.4785 | -54.3025 | 2025-08-18 00:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 117.1 |
| fbbedacd-0d58-3bc5-bf8b-926a78c75f30 | -3.9819 | -42.5396 | 2025-08-18 00:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| f96d1ec4-85ad-35eb-8580-2ad98eb0fa71 | -21.4585 | -54.2843 | 2025-08-18 00:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 615.7 |
| 5e35a517-790c-38fe-a1de-f33023404db3 | -13.2378 | -50.7756 | 2025-08-18 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 86b4e621-31c9-3e15-a0b8-8d912a1a308f | -12.9971 | -56.8395 | 2025-08-18 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| b795228a-07e4-3e8a-829d-205c1e42532b | -15.0006 | -54.7928 | 2025-08-18 00:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 6e39f960-a484-3ef7-8903-7c483ec8a379 | -4.912 | -43.2337 | 2025-08-18 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 58b50fb7-55e8-3756-beed-bd86f421c127 | -28.8503 | -54.0861 | 2025-08-18 00:10:00 | GOES-19 | JÓIA | RIO GRANDE DO SUL | Brasil | 4311155 | 43 | 33 | nan | nan | nan | Pampa | 69.9 |
| 19613544-3222-3d20-800a-59cfce9cf599 | -11.3114 | -55.2128 | 2025-08-18 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ea983137-3e9e-3219-9d5d-0c6aac4a7d26 | -3.982 | -42.516 | 2025-08-18 00:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 4ccb9081-fd73-30a8-bb3e-fd1659d5e86c | -21.4374 | -54.3098 | 2025-08-18 00:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 53.8 |
| c90d5a4d-f6a2-3bfb-ae3a-0bb3b8fa2485 | -21.479 | -54.2807 | 2025-08-18 00:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 5220a625-7216-349c-a32e-53f5cf8d046d | -21.458 | -54.3062 | 2025-08-18 00:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 402.0 |
| b096d870-7bfd-3e43-bb5d-20d377e66503 | -12.9968 | -56.8597 | 2025-08-18 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| de55dd52-eb7d-3446-97e9-28f1ea48cf1a | -6.5678 | -44.4738 | 2025-08-18 00:10:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e0d84cc3-6982-34ad-997d-9594ad24d02e | -21.4379 | -54.288 | 2025-08-18 00:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 3e5d4fe6-e0b8-37a5-a2a5-5f7bd049f4a2 | -3.79668 | -41.011 | 2025-08-18 00:11:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1195b5d6-414e-3324-8b28-0afe11ba4d2b | -3.58739 | -47.52161 | 2025-08-18 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9f0fd9c1-aebc-3383-a9ee-66169c7bda6f | -3.37996 | -47.61028 | 2025-08-18 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| b4d1cf4e-cf73-34fa-8bcf-406ba1e61a0f | -3.38316 | -47.61842 | 2025-08-18 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README4.md)
