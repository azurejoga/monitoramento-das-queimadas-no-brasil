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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3c1998c-6a80-3148-9005-46c040b64fc6 | -13.03375 | -45.18156 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6f21c953-ba14-3156-bbb6-e7ab2211a08f | -13.8669 | -45.5598 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a344167-ce7f-35b7-ada9-28f9940012ce | -14.84924 | -47.94203 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c099b2c5-030c-3c2b-8ef8-918a598b18af | -13.04272 | -45.16838 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| f50236ad-0965-3745-84a5-74054b5187fc | -12.9581 | -46.22644 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4d01c3d-206c-3976-a428-b07cf5b18828 | -13.03547 | -45.17083 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 75f4642f-a398-389e-9218-14d062d9ffa4 | -13.02995 | -45.16256 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 59c4e749-d0d8-3b9e-9394-360d77a28125 | -12.91004 | -46.09542 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 562cb10d-c445-3e66-8d89-b383e2f6a67f | -13.32415 | -54.42792 | 2025-08-21 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73cf34e3-b4cd-329b-b917-c88e23ec60d4 | -13.04059 | -46.81973 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8932b6cb-63c9-3014-a41e-7c6c4843e35c | -15.54488 | -42.27085 | 2025-08-21 04:19:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73bc3185-72a5-3ab7-b79e-049de5be12bc | -13.03813 | -45.19697 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a8a9037-a550-339a-ae57-60e5dc66a760 | -13.1664 | -46.90948 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45d7777d-aea0-3226-9a6a-ac8aa2060001 | -13.87148 | -54.06659 | 2025-08-21 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d178078-40b7-33ac-9447-74236ad939ce | -13.49393 | -47.06702 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fda6a169-3106-3a48-b53c-21d638a1d957 | -12.94382 | -46.18534 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff318c24-57d1-33ff-8803-ff441508fb65 | -14.50199 | -45.95649 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afd578b5-288a-3e7b-bb78-5e37e0559dc8 | -13.03328 | -45.16312 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a4ca050b-544a-3724-9206-444bef6a2d70 | -13.15591 | -46.90775 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd706924-45cc-33d9-99e5-828eeae96408 | -14.8986 | -48.07141 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c627965-4cb1-34c4-8fbe-078955821698 | -12.94883 | -46.24003 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1c617069-6528-31c6-9b61-074939700d65 | -12.95686 | -46.23397 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7a51a3a-16cc-3f59-b3f5-91b71d64ddde | -12.94607 | -46.23547 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1a2ec6c-103e-35e1-ab67-f74505044459 | -14.87841 | -48.05929 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bcd649b-c6f8-306e-9769-ed1ead2aa706 | -13.02937 | -45.16613 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 625289fa-8d38-378d-bafd-6832e3541ea3 | -13.14258 | -54.91677 | 2025-08-21 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0c3a2362-d10b-3a48-9648-ca66e08af5f5 | -12.95624 | -46.23773 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc6ad1fb-bbc7-34fd-a2ac-a3b6ae074d4e | -14.49131 | -45.95844 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 189fb59b-af89-3e84-ab5f-fde268a886d8 | -13.14014 | -54.92906 | 2025-08-21 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7ca4bbc-00dc-368a-a1ae-fb0d4c5324f2 | -12.94785 | -46.18222 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0cdd866-d18b-3a80-942d-c7f38193bb7a | -14.85706 | -47.96117 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d4a0b5d9-439a-3a98-a398-bae64ccae508 | -13.53849 | -47.04105 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d19006f1-b83f-3e5e-afa3-80c2e8231c7b | -13.04341 | -46.82427 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c067876-350f-3df0-9a46-1cbe8aeb596b | -13.64747 | -45.71261 | 2025-08-21 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57fa88a9-58a9-371f-b4e6-2d5d4fa5cdd6 | -13.64554 | -43.80734 | 2025-08-21 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58369a68-8c0d-397a-a8ee-d837f7d1a30f | -13.03651 | -45.18569 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b7ea5ca6-1a49-3746-810e-8058f34afef7 | -13.33551 | -54.39935 | 2025-08-21 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eca8c90c-1467-3dd0-9590-b2865dd41ba0 | -12.93922 | -46.19198 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c9e9a56-5973-35c5-854d-137ae54a28e7 | -13.02363 | -45.20188 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 02b0ee7e-d3e2-3d28-b0f0-661110a1d54e | -14.84783 | -47.92863 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ce09eae-fb0a-3d78-8e01-c72e2d12277f | -14.49743 | -45.96325 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ff29537-2581-31a5-98b0-6a2003ad33fb | -13.86683 | -54.06202 | 2025-08-21 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f94f5185-a156-3f17-9813-88089a8bf858 | -13.02916 | -45.21015 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 22f9d5a5-6747-3b4e-8f65-3a949b6e8910 | -13.63323 | -46.88273 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3e5b026-e85f-33c2-9f5d-8665a0dd133b | -13.55451 | -47.03156 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5b0a16c-3733-3260-a1cc-75b5667fdfe7 | -13.03594 | -45.18927 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8712a04a-7f40-38c1-9291-e3dcde7605f4 | -13.65023 | -45.7168 | 2025-08-21 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e404fe9-5edb-3a28-ac9b-626d618a4955 | -13.04472 | -46.81644 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d380acc-43d4-35b8-b27e-a1860477dffa | -13.04125 | -46.81576 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b55ccbcc-fee8-3a76-bfc6-eed949fcd50c | -13.32858 | -54.4055 | 2025-08-21 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6c832ac-4cab-32b8-b03d-f5eceea0f3b0 | -14.49586 | -45.95169 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f527cbf-cbdc-3fd5-9864-a3285775d2ea | -13.19827 | -46.89068 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50b110ef-8fba-3bd6-80dd-19e5a44483fc | -13.03881 | -45.17139 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 2f271030-a120-3a05-846f-4e4ee0c5b92a | -13.03766 | -45.17855 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e323bbdc-e6c1-3030-ab18-3886b3e97d89 | -12.94481 | -46.24309 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aa821699-31a6-33b3-b537-18b3197d9ecb | -13.87081 | -54.07005 | 2025-08-21 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 166ffa0e-cb2b-3a7d-ac94-2dec4a81caa5 | -14.87365 | -48.06003 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4919c09-d37a-30b6-932d-78e8023860b1 | -13.3293 | -54.40189 | 2025-08-21 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fd42f26-4463-3780-97c8-35d7a1532a3c | -14.4919 | -45.95479 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e0475d1-6e05-38aa-b472-8a25185e8f64 | -13.04548 | -45.17252 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4479ac8f-c226-3a00-b3c8-5f68d8aee395 | -13.13935 | -54.93307 | 2025-08-21 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eaadd84-3573-3f04-bf33-ecd06a412da0 | -14.85069 | -47.93353 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ba8878a3-b278-3850-80e5-525fe20efbf7 | -13.38571 | -47.49324 | 2025-08-21 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e5af170-9bc6-3234-adb6-6942999ab7ff | -12.9433 | -46.23103 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53e5b3b0-6e0a-35c3-8c29-7616640efc75 | -14.47332 | -48.37045 | 2025-08-21 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47589284-7db4-3462-937f-70c44ff40a8c | -14.87481 | -48.05863 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98bf02f1-ed31-3aa4-80f4-77fc4447534c | -13.02639 | -45.20602 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d918f71c-c553-3ca5-b330-e48bcbd9dfa6 | -14.85639 | -47.94344 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ca5cd75c-92fa-3917-b707-6b5fa308d4c5 | -13.02434 | -46.80571 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42c4e119-f8cb-355f-b916-f8c8f7f70c75 | -14.85209 | -47.94696 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7723255a-d19f-31f1-aec2-27204746ccf2 | -14.12471 | -45.38848 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 689175b3-b4a5-332a-9c40-7ff74b067f8c | -13.47908 | -47.04796 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67935333-dc64-3a59-82be-89eaa8810e2c | -13.54482 | -47.04624 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be99c695-1be4-34f1-836f-e8bfa8bcc51f | -12.94946 | -46.23625 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 477f49f1-2ed3-3cc3-8f68-3928108f2b1b | -12.89546 | -46.07765 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 163e6e6a-0495-3a1c-a753-82525f386345 | -13.3304 | -54.42524 | 2025-08-21 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d971f5d9-c1dd-3c35-a5a8-70679d27b513 | -13.04157 | -45.17553 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7c80f23c-972e-3c01-b94d-5df61d193c37 | -12.94392 | -46.22726 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f755547-19ee-3e3d-9351-3670594b4444 | -13.19893 | -46.88668 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29f88d51-0f7f-3c18-b4dc-f18a1d94a70d | -13.65418 | -45.71373 | 2025-08-21 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93b08fbd-04a6-33a8-bd6e-5ac68f9831e8 | -13.15872 | -46.891 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a7d433c-472c-3c73-89ef-3e0d62938562 | -13.15732 | -46.89935 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00692b4d-18ba-3ab0-b0ed-f0763a2a5e97 | -13.04406 | -46.82037 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7aa31fd-df0c-36cb-8fb2-4000dd852bb4 | -11.31914 | -55.2184 | 2025-08-21 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36177f4f-2e56-39d5-8260-b616a5f31533 | -14.87725 | -48.06068 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b95af75-1456-356c-8859-b24cc9b3905e | -13.558 | -47.03216 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1fbdc89-39ed-3739-afdd-e5142717ae3f | -13.5665 | -47.04585 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c65cf112-5178-3d35-be24-4d2d76b828eb | -13.14584 | -54.9302 | 2025-08-21 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae9d8d80-bffe-3fcc-ac69-d4699986f0ad | -14.46592 | -48.36939 | 2025-08-21 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 132fe84b-cbc3-3b82-8eff-6172122fc49f | -14.46963 | -48.36983 | 2025-08-21 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f9cb992-e2db-32f7-beda-1d317627998c | -12.94731 | -46.22796 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcb36133-2fe4-3b60-81a5-fd3316bb47f2 | -14.12705 | -45.38541 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c5ca2f2-f5a9-33bd-bc0a-573be623d9c8 | -13.16289 | -46.88754 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66143916-35c7-36be-9a9e-6abda83716d9 | -13.65524 | -42.47782 | 2025-08-21 04:19:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dcd63aeb-cc4e-3139-ae0c-092d7faa65ad | -14.93109 | -40.92123 | 2025-08-21 04:19:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a6109846-2f8a-3ffc-82e6-a576879851e3 | -13.75297 | -41.79058 | 2025-08-21 04:19:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6ee71ff2-dbcb-36c2-92fe-535ca84f8e01 | -13.03052 | -45.15899 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2dc1a531-317a-3d56-a49f-070272a2e6d2 | -12.9346 | -46.19871 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e8328c0-85c3-3cc1-a349-156db9bdf8f6 | -13.04192 | -46.81181 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0788af6b-aa3f-3108-a59a-0a5d168afee0 | -13.5735 | -47.04701 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README35.md)
