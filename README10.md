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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47ed6165-b951-3081-98fa-de5db6a9a9a5 | -9.73358 | -48.34704 | 2025-07-05 04:19:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab8fbd00-e432-3bdb-842f-bfb961072e40 | -10.37142 | -47.55648 | 2025-07-05 04:19:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfb52c0f-8292-3d12-afdf-ba4e7a39d4fa | -13.12308 | -46.91732 | 2025-07-05 04:19:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27b1d826-bded-344c-9e14-12c81db468b3 | -13.02692 | -46.30371 | 2025-07-05 04:19:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 677db18b-5432-3e4a-a72b-cd520921b6b3 | -7.30498 | -45.36247 | 2025-07-05 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a305aeec-9fd0-354a-a8fe-64c7538f9067 | -7.2981 | -45.36104 | 2025-07-05 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 235fc575-8faa-374d-b289-e4e065e22325 | -13.02967 | -46.30778 | 2025-07-05 04:19:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a441dfb-e90c-32ed-91e5-fcd3a281a61d | -6.69728 | -44.06236 | 2025-07-05 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f33a785-917b-33d1-b85d-a0d35f9d66a8 | -10.37483 | -47.55706 | 2025-07-05 04:19:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fce1673e-e605-3ab2-995e-b26d51ca4de5 | -9.57484 | -49.10238 | 2025-07-05 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41b618f3-4f80-3ede-920e-d4c8c159176c | -12.75205 | -44.41443 | 2025-07-05 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fb241c6-bae5-384d-b184-5d0b4090a8ae | -9.58326 | -44.60973 | 2025-07-05 04:19:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dfc4ceea-6e70-3610-ba09-8c82dceefb04 | -7.22659 | -43.08852 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b11f98cd-c059-363c-9d83-528e05106d05 | -8.39941 | -43.79421 | 2025-07-05 04:19:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cf8f6fd3-4180-3380-b2e4-a2f43daabc2b | -7.15619 | -44.31993 | 2025-07-05 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0fe5fd3-d6dd-308f-b16a-a0db68c382f9 | -5.72473 | -49.10973 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b81835e0-da45-3049-8a3a-98e2d2ba9b1f | -12.01186 | -47.76111 | 2025-07-05 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a9d18539-1b42-361d-bfd8-406f44744458 | -7.24822 | -43.08425 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ff8cf81f-57f4-32cc-aead-70e5d583ae5b | -6.29058 | -44.23037 | 2025-07-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfd07956-4356-3634-8dff-5c18ec07febe | -5.99624 | -43.74473 | 2025-07-05 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f72f68c-4159-371f-a013-893a9619e0f8 | -9.75797 | -48.26458 | 2025-07-05 04:19:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6ba4fc6-09fe-3bdd-b31e-2ca2e0553883 | -8.99693 | -47.44274 | 2025-07-05 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c66aeff-b940-36e8-9781-576cce5522be | -5.72134 | -49.11115 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 624081c9-4b11-38bb-8236-f0d6e1c328e1 | -5.72215 | -49.10629 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18235c99-20e5-3f4e-a4be-cbe8e5cdecfc | -10.3004 | -57.14001 | 2025-07-05 04:19:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfb5febc-4a09-3f39-9909-80d7f4ea6513 | -12.76114 | -44.40049 | 2025-07-05 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a38c4f86-0ad3-3ba6-ab8b-a5d3ae6421d3 | -7.29786 | -44.69488 | 2025-07-05 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9b2219b-1e12-3432-ba23-4826e0b6d044 | -8.99227 | -47.4497 | 2025-07-05 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c367126-a6b8-3af7-b22d-2c0146a0ab6b | -10.63904 | -46.4697 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2128748d-7476-3077-a78b-60033b2fffdc | -6.75915 | -44.62026 | 2025-07-05 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e686d21f-d45d-3fdd-ab9a-a14ae3e427a9 | -6.67571 | -43.8721 | 2025-07-05 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5257eec-6a1d-309c-8d0d-66358e7edcb3 | -7.34751 | -49.63495 | 2025-07-05 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f632b5f1-ccc2-340e-a058-fd6054314aaf | -7.5628 | -49.90648 | 2025-07-05 04:19:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb267f5d-c0eb-31b0-984e-6d5de7459399 | -7.94675 | -44.84686 | 2025-07-05 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 663e01ce-895a-327f-ab71-bbaaf0f5958a | -13.12365 | -46.91378 | 2025-07-05 04:19:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3969972b-4c0a-3d8f-adef-ce6af5346d0b | -12.69158 | -44.60708 | 2025-07-05 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ba58f38-e070-3907-8ea3-0414794d6cfc | -7.44954 | -43.07262 | 2025-07-05 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 26a5cdec-e80a-3bb0-8698-f4c509e398fa | -8.3856 | -44.05367 | 2025-07-05 04:19:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a1cfcd4-9945-3901-8d5d-ccff88aadc90 | -12.75262 | -44.41068 | 2025-07-05 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd4e619d-198b-3838-bc31-6890d366a0c4 | -6.28727 | -44.22985 | 2025-07-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98833ae1-0c70-38e9-b643-e16279155951 | -5.72552 | -49.10487 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9d4c541f-6323-3780-9846-a696d0c29a01 | -7.90234 | -55.42223 | 2025-07-05 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f209b57-d093-3a62-9faa-cf480d6feec0 | -11.87736 | -44.87332 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b99859b9-c6a5-3008-996f-017e56db7aad | -10.65363 | -46.39977 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 676f4a36-946e-3b8b-9dfe-00d8d9f42589 | -11.30884 | -42.13099 | 2025-07-05 04:19:00 | NOAA-20 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8aabab40-f554-30ed-aa99-fbf8d83ec42f | -12.01804 | -47.76596 | 2025-07-05 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1f3147d-649b-3691-8855-35ad924dc0ef | -7.87123 | -44.91663 | 2025-07-05 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60c81177-25cf-37e7-9ad9-2cda24d7bd2d | -10.89379 | -56.45829 | 2025-07-05 04:19:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97122a3c-c20a-3c6c-8719-9719b4c68c97 | -5.99455 | -43.73365 | 2025-07-05 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b295638d-25a4-3105-b38f-3c1252319c7f | -5.99679 | -43.74121 | 2025-07-05 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ffbf0fef-886c-35f2-9f2c-c3e2b56a66ac | -7.0209 | -44.0334 | 2025-07-05 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 112320df-67e7-31a9-bbe4-5d90bc8e91e6 | -11.43689 | -45.11222 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6730088-3ec3-3c9d-ad50-7548efd727f3 | -11.44021 | -45.11275 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d376c328-ceb6-3f47-9c7d-5f8315e0b0a3 | -7.96479 | -47.23146 | 2025-07-05 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d612b4f5-68f9-3cb1-b400-2c5d1133d9c0 | -9.08831 | -47.07207 | 2025-07-05 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9848b8e9-db3d-3950-b8d0-ec6c86c692de | -6.89037 | -43.97717 | 2025-07-05 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 30ef51ce-89e9-3f76-9d69-1e22132f1cb4 | -6.74886 | -46.46108 | 2025-07-05 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b03e0ab-f9a9-3ecc-994d-b9c36710ca2a | -10.99966 | -42.79449 | 2025-07-05 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a1533f51-b731-35b8-9f90-3c24ac9e0034 | -7.18815 | -45.32635 | 2025-07-05 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d94ffb5a-1331-3250-9ae3-3febf3c4a015 | -10.6558 | -46.405 | 2025-07-05 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 52460a5f-46ff-3519-91c7-9f0f24a455e3 | -10.6174 | -46.4323 | 2025-07-05 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 90f0bc29-bb77-324a-b202-6d1c6837e35c | -19.07645 | -43.87365 | 2025-07-05 04:21:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1a41f5a1-f432-397d-8b13-70ac63c4a211 | -18.33662 | -52.04474 | 2025-07-05 04:21:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79c6b68e-b70a-36b1-acea-bc39c0fd098b | -20.76393 | -46.77045 | 2025-07-05 04:21:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3abd5729-b19f-3572-9d96-88bd1c167b3b | -14.6687 | -45.36941 | 2025-07-05 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eac01448-f54b-3f2c-8bcf-9bdb484d6ebe | -18.45419 | -51.23574 | 2025-07-05 04:21:00 | NOAA-20 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 735a4b89-0763-38ac-b92f-0a09882206a8 | -20.08413 | -50.56093 | 2025-07-05 04:21:00 | NOAA-20 | PARANAPUÃ | SÃO PAULO | Brasil | 3535903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c56e2a45-4a67-3cb1-b5f3-1569dba6f512 | -15.61747 | -46.45799 | 2025-07-05 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e29863e-6188-3045-8599-ffbe66ac789d | -18.92634 | -48.34601 | 2025-07-05 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ca35815-2e44-38bd-a085-e56ae1524be8 | -15.81263 | -48.17577 | 2025-07-05 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1943bc4f-300d-3b53-ac8b-a6da7f1a5df1 | -17.92007 | -45.52959 | 2025-07-05 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be2bb0f2-3abf-3fda-8179-9857bf71246a | -18.84526 | -47.48751 | 2025-07-05 04:21:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db2061e0-7077-3a59-8acf-2fb87acd9b09 | -14.67878 | -45.37102 | 2025-07-05 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b6130f3a-e62d-3038-853f-4fa9174e5859 | -17.87202 | -45.54679 | 2025-07-05 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c4357dba-1294-3baf-adcc-08907a10100b | -18.33752 | -52.03976 | 2025-07-05 04:21:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dec8a7b4-dab5-33d2-b104-353bba739bc4 | -15.62022 | -46.46212 | 2025-07-05 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8465a614-eb59-302a-a90e-6404a4c112c8 | -12.57473 | -56.97147 | 2025-07-05 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a2a0430-4f7a-38e7-9c19-085fd061ea3a | -19.16476 | -49.1388 | 2025-07-05 04:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45a40801-e32c-3f2b-9497-8180245d3d35 | -20.42671 | -47.42461 | 2025-07-05 04:21:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d3b9615-e5d5-3344-8a3c-6a8e7cad539e | -19.74994 | -53.99804 | 2025-07-05 04:21:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 26a5bd56-a818-3b76-9e3f-c0f50d66b610 | -15.75175 | -47.75417 | 2025-07-05 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b4a50e23-3c83-3827-8122-06ee80fa2018 | -16.29466 | -45.10072 | 2025-07-05 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ada5e38a-df08-3aaf-a61f-4a92a734cb02 | -19.74899 | -54.00287 | 2025-07-05 04:21:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0bce7ff-4aa6-399f-8882-a3421a58d60b | -17.09327 | -43.80326 | 2025-07-05 04:21:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a93d7a8-f2dc-387c-89a6-2e5942d87199 | -13.64967 | -46.81197 | 2025-07-05 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bba6a48a-ed40-33e0-912a-c6a771a878ab | -20.17361 | -43.70893 | 2025-07-05 04:21:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f24c1776-95e6-3072-bb6f-826b787d9580 | -19.74915 | -54.00208 | 2025-07-05 04:21:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65bc199d-f2bf-381a-bf09-87ba8d77990a | -19.12762 | -52.69265 | 2025-07-05 04:21:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 708e8dcb-6a4e-3c3b-96d4-99f7d6604dc1 | -19.98229 | -47.17953 | 2025-07-05 04:21:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8d33795-e77f-3b42-be18-709c331dddae | -18.66443 | -55.74074 | 2025-07-05 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| dfb450d7-f5f6-30a3-a8c2-2c943227fcdf | -17.76222 | -52.44734 | 2025-07-05 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93acc0a9-feb0-324e-b5a4-24ddb692ecf1 | -15.92242 | -43.51395 | 2025-07-05 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d1c16a2-c173-3670-8a0c-5938146ddb01 | -17.91986 | -45.53072 | 2025-07-05 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| faec5b17-85a4-3fd9-9b73-8482e3c495d5 | -19.07707 | -43.86908 | 2025-07-05 04:21:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 31a83e9d-53b9-385e-bb6e-cddcffd85e96 | -19.45218 | -45.30658 | 2025-07-05 04:21:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5ac4886c-c968-3fca-9219-b590332ae24e | -17.67769 | -43.69831 | 2025-07-05 04:21:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 868dfb60-1470-3789-b90b-cdcf3f4f0f0c | -17.75826 | -52.44658 | 2025-07-05 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61cc6fd3-ab09-38db-912a-80307ed08978 | -14.92173 | -46.91024 | 2025-07-05 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7cf3dfb6-9aff-3616-b838-ce51a7f580d0 | -18.92575 | -48.34966 | 2025-07-05 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 123879c3-7b41-36b6-86ab-b4133ad54d68 | -15.56883 | -47.85694 | 2025-07-05 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README11.md)
