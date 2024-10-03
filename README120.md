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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed0df3c4-b8cb-3fe7-83ba-38681a3ce592 | -3.45316 | -53.98179 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab180e14-6642-3d36-85b9-c1fe10eb86b1 | -3.4497 | -53.98123 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dda86fe-a9de-302d-8b46-a94c21f3a0e7 | -3.38085 | -54.11464 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fe4c071-ac67-3435-95c2-3e2ce49ae4da | -3.38025 | -54.11842 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3626edbe-3dba-3f68-ae5a-fe5ca7681235 | -3.37965 | -54.12221 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dc07759-e37f-3300-908c-32d85fdcf779 | -3.37858 | -54.10643 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48d434c2-f9d5-380a-a34e-a0b4502f371f | -3.37797 | -54.11027 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 265c8a71-039f-3eaa-ab54-83b4c5625500 | -3.37737 | -54.11409 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df25641c-9848-3a7d-914f-f37621efb0e7 | -3.37677 | -54.11786 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8f13918-3616-3a94-9b85-406091084923 | -3.3763 | -54.09827 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9999803e-fd15-31f9-8576-258b18d3c804 | -3.37617 | -54.12165 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61fd625c-0a7c-3b73-aa48-7577b0a0d8ca | -3.3757 | -54.10205 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aac12310-3e32-3c8b-927c-2375517e90e2 | -3.3751 | -54.10586 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6df41636-b246-30fc-a11b-336b094f2847 | -3.37449 | -54.1097 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41b6255e-56f4-35ae-8db5-7252629b0e8a | -3.37389 | -54.11352 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a11e5ed-d1ab-344a-a6cf-61528378ff10 | -3.37329 | -54.1173 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7799fc31-53d1-3180-a74c-e3fdd0bacb45 | -3.37223 | -54.1015 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1490c753-67d5-32c1-bc8f-0e70fc5255e0 | -3.37162 | -54.10529 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6dfcad3-a221-34f7-abd8-062c6dc0c7ad | -3.37102 | -54.10912 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd6236d2-dbc4-3937-beee-6e5bdfaa6115 | -3.33081 | -53.76751 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8fd75ed-0c70-3683-b070-c6b5e8c2456e | -3.32796 | -53.76322 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 858da4b1-1eb1-36fd-9aca-01fcdbd1abbd | -3.32737 | -53.76698 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1943e742-9850-3445-9d5e-6e3c5c030fe7 | -3.32452 | -53.7627 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7914c02f-1b79-3b89-8db4-f692e0b55b15 | -3.32393 | -53.76645 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8c97c92-3943-3086-9886-c36f1c7f38ee | -3.13267 | -53.74109 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84c6ebe6-492b-310d-9313-fae8a14567f1 | -3.13191 | -53.74047 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94f6abca-a25f-33dd-bebd-e47a396e5194 | -3.12353 | -53.73201 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cb15710-3536-3423-93e4-a96e960028fe | -2.98479 | -53.97997 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b677021-5a98-3ed9-9821-802b8fb64081 | -2.98361 | -53.97999 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c56aa1aa-4209-399e-ab9e-b7a29ccc2ffa | -2.97959 | -53.73613 | 2024-10-03 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0521f33e-c77c-364a-9970-ad5ea58ea4e8 | -2.95277 | -53.70518 | 2024-10-03 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cc5163e-be25-3694-8ac1-5cca0eeadb4b | -2.95217 | -53.7089 | 2024-10-03 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a8a7e15-1d48-3765-bf12-757043636fb5 | -2.94648 | -53.70037 | 2024-10-03 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55b72a43-154c-3a73-b12b-05a180b36300 | -2.93616 | -53.69876 | 2024-10-03 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e34106d-061a-32ef-b665-86d8f151a89d | -3.90898 | -54.56008 | 2024-10-03 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3cc3c1f-509d-3a5b-a1dc-17273cecd9cf | -3.79337 | -54.42545 | 2024-10-03 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6992479-1042-3f8a-8556-30eb7576ae48 | -3.78987 | -54.42485 | 2024-10-03 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 351d52d4-1eaa-3f2b-b37b-afccef002a51 | -3.73645 | -54.35382 | 2024-10-03 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 399e738a-e188-356d-bd5e-10d775d2b9ea | -3.73294 | -54.3533 | 2024-10-03 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dfae404e-eca8-3f1f-a274-48364df57eab | -3.66829 | -54.37159 | 2024-10-03 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90bac9b6-2c90-3931-943b-96e477b31c9b | -3.6654 | -54.36711 | 2024-10-03 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 665092d3-5879-373c-ac9c-2de6c1ed4730 | -3.66478 | -54.37105 | 2024-10-03 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38af6afd-2c6a-3758-8c4c-088180a971b3 | -3.66002 | -54.31046 | 2024-10-03 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 532c09a7-c452-36da-b148-d3bd74211246 | -3.65941 | -54.31429 | 2024-10-03 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1120cbd-ec45-3ae8-a8c9-9cc751d45cef | -3.65651 | -54.30993 | 2024-10-03 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7dedebad-291a-3f5b-b1a2-d76d105205fb | -3.6559 | -54.31376 | 2024-10-03 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 707d91bb-05e9-3dec-9fa4-1f39eda4e988 | -6.89968 | -55.05422 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bade3ef-e8a1-3ab5-85fd-04f7001a05cb | -6.64956 | -54.95152 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 64b89ab7-fc24-32dd-8521-e0571a9bc155 | -6.6467 | -54.94706 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dab2fd5c-481e-3461-9212-440a07ef0aef | -6.64606 | -54.95096 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f4860a71-df97-313c-b4de-bfe9756cca56 | -6.64542 | -54.95487 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d28e8812-8198-38c3-843f-c5e121e66663 | -6.6432 | -54.9465 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7115fcf5-617e-3432-a457-fd4bf26a0d53 | -6.64257 | -54.95041 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8651272d-96b0-3585-ab81-0e979104109c | -6.64193 | -54.95431 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99eeb1a2-8780-3bba-b1d0-526c233257e6 | -6.63907 | -54.94984 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 255a144d-72bc-342b-8e2b-2a31931ef395 | -6.63843 | -54.95375 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 333d0b93-eadb-39ca-a557-16148030b594 | -1.62931 | -54.9377 | 2024-10-03 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00850b6f-3a12-3a82-b53a-253267d00352 | -1.62766 | -54.92411 | 2024-10-03 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f70f8c61-a2bd-3403-96b1-761369806e17 | -1.62563 | -54.93711 | 2024-10-03 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4304c1db-5bdd-30e6-8080-eb973ea4071e | -1.62397 | -54.92354 | 2024-10-03 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50fc05ea-f18b-3c0b-8098-a5f48310f035 | -1.62194 | -54.93653 | 2024-10-03 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1009fc6-f4c3-35fa-8b8e-d28407e5932d | -3.8228 | -55.78474 | 2024-10-03 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84c21a09-b638-3534-820c-5500d51432d3 | -14.50573 | -45.22367 | 2024-10-03 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4102279-8fb9-3bdd-9733-edac12e84cb1 | -14.50534 | -45.22703 | 2024-10-03 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 603f869c-b1dd-356e-8ee2-1d48773850b3 | -14.50496 | -45.23035 | 2024-10-03 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd023174-51eb-3d7b-af83-1cc262a7db42 | -14.19032 | -46.45679 | 2024-10-03 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a39203a-ead3-320c-9e6e-9caf522f06c9 | -14.18838 | -46.47222 | 2024-10-03 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c12ee8a-1696-3d21-891d-e3d337a77967 | -15.25564 | -47.50001 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46cd33e6-7940-33a0-8170-aef3b2664fc4 | -9.16691 | -67.31493 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76cb92d5-0ee3-3c2c-9249-2e9d013945ce | -9.16548 | -67.32202 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 93d3c4fd-fbd7-3491-88ea-69d2bb157917 | -9.16484 | -67.31468 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3500b3c2-1437-30ad-b06b-3caef9ceb913 | -9.16346 | -67.32169 | 2024-10-03 04:51:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94d5d8b1-8bea-3071-83fd-4dbb4d3fa243 | -8.6703 | -67.02651 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8ebf791-4964-36cc-935f-78321cf68c8a | -8.65826 | -66.67633 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1dff7496-c16f-3968-8bc9-2c1ae5be1525 | -8.65709 | -66.60689 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9637c3e8-71be-37ef-b8c0-e6d10517ba49 | -8.65697 | -66.68303 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a2e301d-8288-3a14-9f2f-48f2d0315467 | -8.65622 | -66.67552 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| edcfa849-b0e6-3b1e-b4ad-a5b13b06dfc0 | -8.65546 | -66.6064 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7c1fc112-6902-3e3c-a486-f5e460c17f51 | -8.6549 | -66.68221 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4d6b2340-63fb-34b4-be27-6b42e8276fea | -8.65014 | -66.60545 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08896a63-0df9-3ae7-8b07-58f1e30237c4 | -8.64851 | -66.605 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e149fb5-b72b-3a18-ae22-4c7ab7a6fb92 | -8.64824 | -66.71577 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 206a8395-6d1d-3073-83de-ccf891f47828 | -8.64356 | -66.71516 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a197584c-ee3b-3a4c-ad72-a5dd5c136d65 | -8.64125 | -66.71435 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6c32ff07-725f-3518-b320-e1885f6882ee | -8.6399 | -66.72119 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ad1ee94a-3bed-36e1-9c27-d61c3984f6c0 | -8.63658 | -66.71368 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b06a457d-b680-3119-baca-715abcf8796f | -8.63524 | -66.7206 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 475b2ca9-c98f-3e6c-90d8-54d52f1e753b | -9.36875 | -65.83762 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19af5abd-71f5-34d9-bc19-593bd1ef7fc9 | -9.31226 | -66.62783 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1511e9c-2cef-3679-ba40-d947522786f4 | -9.31095 | -66.63436 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a408dd6e-ab3e-3d8b-93fd-5fe8559eec70 | -9.98823 | -66.87614 | 2024-10-03 04:51:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bdb4d1a-2cc8-3851-9d25-e26ecd6a32ba | -9.98676 | -66.87474 | 2024-10-03 04:51:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11f7d38c-e251-34aa-a876-1c1b76087554 | -9.98132 | -66.87471 | 2024-10-03 04:51:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b03f218b-f30c-3548-87d4-236c6a37f0bb | -9.97985 | -66.87334 | 2024-10-03 04:51:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24454b2f-6b83-3eaa-a47b-1a4d619e901a | -9.90405 | -67.33862 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf3af7cc-44b1-3306-8d0e-37bc7e5f52e8 | -9.89969 | -67.33588 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 257e1cad-13d3-361c-a919-f60f5f90670b | -9.89823 | -67.343 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1cb7850-176e-3c23-bc7f-19f3376b989b | -9.89697 | -67.33706 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 49f8c8c0-d825-38dd-931f-d29cf6460459 | -9.89555 | -67.3442 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 216c2dcf-ea04-3324-9b69-39893d575991 | -9.89259 | -67.33442 | 2024-10-03 04:51:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README121.md)
