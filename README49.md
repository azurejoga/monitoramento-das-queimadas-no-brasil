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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b3d343f-20cc-3924-a7c0-f78c7305060f | -2.80154 | -53.01242 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19f22cc4-3033-3201-8f61-d2b84f8c1404 | -1.63076 | -54.46173 | 2024-11-25 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ca2b06a-7694-371d-972d-27fca0d4cfdd | -1.21399 | -51.74104 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de86058c-8c5b-37eb-9a2c-bb775b527342 | -1.59285 | -52.58661 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab86de7a-2698-3877-b39d-ffa798033c89 | -1.19723 | -51.7602 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5fae39a1-f732-3325-8a0f-f69a8952356f | -4.20526 | -48.12506 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b2ffb67-e6b0-34bd-aadd-4807f7a2791d | -1.77135 | -52.72086 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc17f946-c926-3ab4-8c3d-04cc6ba7bf41 | -1.77581 | -52.73569 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c3abd307-7d56-34c9-90cc-12f0a20f7b54 | -3.23224 | -53.3906 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2984cf0d-b89f-3fe4-b69c-c8e473282161 | -3.26505 | -53.26854 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34c2af9b-a0e9-31cb-90c4-0e3f7de23373 | -3.61415 | -54.21309 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dbd9fc8-5f45-3a23-b5eb-28146dc41614 | -2.17625 | -53.77759 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5b1c6a3-54b5-3143-ab71-05184ef850a5 | -3.52169 | -53.81097 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c68ec27f-fc3a-39f3-b673-7d89d4dd38cd | -2.85817 | -53.96238 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ee47316-64df-3f36-bd6c-583279a0cdbe | -3.57906 | -53.53346 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 148cc79e-8bb5-3789-828b-b88a30499ef1 | -3.36732 | -51.42982 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42d796a0-e5dd-39a4-b7d2-23ecc5c5bbaa | -3.29756 | -45.67806 | 2024-11-25 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 12e8761c-1cc0-34ba-a34d-4bbfb54ad952 | -3.1044 | -53.96925 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47fda0c4-6881-329d-af66-3605c75f2bd4 | -2.33518 | -53.86629 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 26d77a44-bca3-337c-bbdb-cf50e10caf44 | -0.3418 | -51.97641 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f94e2b8-b964-320f-840c-b4334176bb97 | -1.62594 | -52.26855 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47c3e71a-4956-3c20-ad41-73e180e77a4e | -1.62538 | -52.43902 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6aa5d8c4-1eeb-38e3-9112-aa01d624c438 | -2.8061 | -54.07563 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 534bc890-3ed1-3c9c-b4c2-c03e55845400 | -1.23702 | -51.79172 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9855a396-023d-3c43-9480-556fa87b6497 | -3.6136 | -54.21657 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8b71b8d-594e-3558-b49e-1908dda33d57 | -2.79074 | -51.68118 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2259e171-6491-3632-b88e-926d73800316 | -3.7804 | -51.87211 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b841a472-c978-3b92-ba9c-f2afbde40dbd | -2.04111 | -52.07819 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0275b909-11f8-31af-849f-acea51aacb95 | -1.9397 | -52.09864 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8d2c762-346a-3c64-870a-610aacc8a4dd | -4.09065 | -53.82941 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad603db6-cd47-3a11-90f9-d9c3d5490b46 | -3.39136 | -50.32052 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe2c9bd6-da76-3218-b490-317a0ae5198f | -2.14049 | -52.08969 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f60c128-55fa-348a-a34a-4043e1f41318 | -4.58436 | -46.09034 | 2024-11-25 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91bd7e8a-e671-3ab5-9b00-0e917fecf064 | -2.8105 | -54.02628 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd3da997-3917-3776-8058-0bad8b5f5bab | -3.37249 | -53.05894 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cdee02e-0fb2-3001-8c94-8f295cb63d1e | -2.78717 | -54.04407 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0629f8a-fe0f-315d-8cc7-0dc9309336ba | -3.06313 | -53.28312 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9de05bd8-efed-3920-9ebb-432ef135754a | -2.96183 | -53.92557 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31b49241-8ad8-3bf7-8ab8-c5ae95caba86 | -2.43929 | -54.14434 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9585c9e4-827d-38dd-b061-17a2020aba53 | -1.26163 | -51.76656 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6288098-a45c-346c-9f8c-c4e908f4e935 | -0.95942 | -51.64419 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edeed947-9a53-3d00-a404-81d6d7455706 | -3.27688 | -48.75647 | 2024-11-25 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc6cf7e8-6883-35e6-a5b9-a1cc65161b96 | -5.48037 | -51.17199 | 2024-11-25 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23c3e815-adbe-3592-8485-4a9ca4506b99 | -2.17014 | -53.77308 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e165ac8-e642-319b-bba9-ec7b7b328f52 | -1.09008 | -54.03482 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47d77fb0-b7ac-35e7-971c-de30d1bf0be3 | -2.39362 | -53.71182 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a21e7c6e-1e04-3228-9dfd-95b70b9d25d6 | -3.7587 | -52.07976 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e87b2e4-0e9b-3e94-97b8-3f7440dd0d2e | -1.47854 | -51.74217 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd4c5c72-eba2-321f-a590-794033bb2aa8 | -3.41908 | -53.28191 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41526ac8-7f7f-38fa-98c7-6e26d5ad15c9 | -3.19222 | -46.36552 | 2024-11-25 04:55:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9daedeb3-f7ff-36af-bff6-78b1e8a5c1b7 | -1.31576 | -51.86869 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1e645fd-0713-3583-baaa-d562c77eb6cb | -1.10669 | -53.39317 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bae2fc3-0491-3e26-9aa5-8d15a2da79a2 | 0.63209 | -50.57421 | 2024-11-25 04:55:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b943af9-f570-3b69-803f-e09a1062cc2e | -3.71288 | -52.41907 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3b34888d-3ac2-35a8-bdc6-00f257c58621 | -3.22865 | -53.92802 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4efdc6e0-605f-31af-82e4-9a8edda706aa | -3.71343 | -52.41555 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 66fd3932-4fd3-38ac-9046-43cc36a710e2 | -1.73597 | -52.7295 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aaa506c1-1634-3941-835c-981f9f0bd6b0 | -0.91849 | -51.64147 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75d38a73-c692-3ffd-a2cc-d81ed383d2ef | -2.81545 | -54.71917 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f8bbd7a-5ed8-3f94-8144-f27f5ea8a424 | -5.45455 | -50.63748 | 2024-11-25 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfc9dd2a-72fe-351c-bcf6-fee001b5b43f | -3.84952 | -49.89981 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90597ade-e311-39b1-bdba-2e48067231c6 | -2.2486 | -53.62193 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7dbb5f0d-68a1-3aee-9625-9d3f589cce7c | -1.06648 | -53.17839 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fec2e533-dad2-352d-83da-4523a7f35f9d | -1.47087 | -51.96534 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c8517fe-9dd1-341d-880b-d42691399280 | -0.68911 | -51.87645 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30c5bf45-83d3-36d3-ad2e-d5fee1685813 | -2.61946 | -54.25507 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bece0bec-cf38-3aaa-abd0-9d3f88002464 | -2.59227 | -46.55755 | 2024-11-25 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a29e949-e6bd-36b0-baed-17c501ea1aa7 | -0.88098 | -52.76522 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb8aba30-2a9b-386d-9c10-4418e016b39e | -3.86861 | -52.35595 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ab6de33-fa73-3b46-8c5c-504ba552f936 | -4.31122 | -48.0777 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5627a8cb-0520-3509-b696-338d6c568185 | -2.84378 | -53.98865 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52ce0043-e792-3d6d-86f6-1ad1c3c6fd80 | -0.96505 | -51.71761 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c37e1542-1fbb-3851-bf27-7f74281b5f0e | -2.27302 | -51.23882 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4faa0859-0dd3-3cc9-b91f-0134ffdb7d8f | -1.35895 | -52.24162 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97e27baa-a06e-36e5-982c-28ee867054ad | -2.5802 | -53.96196 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cb75ba9-99ac-33b0-8293-adf45b8c0670 | -0.88894 | -51.72029 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fd3351e-a584-30cb-830d-ff59d95a3faa | -1.73651 | -52.72605 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0b1d451-6b26-3ec0-8a25-355e5aa5fa37 | -9.81798 | -48.16902 | 2024-11-25 04:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e31a0ff-5512-35ec-8f8a-cfbb66c3096e | -7.09773 | -49.21749 | 2024-11-25 04:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e351bbce-7900-3bf6-bfba-ccdb5cdea58d | -8.89265 | -46.63871 | 2024-11-25 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 70186048-1735-31b6-a4e7-351821ee7a3d | -8.0505 | -49.69307 | 2024-11-25 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f73dcc01-c219-3fe3-8582-48b80d0c9862 | -9.46193 | -47.34735 | 2024-11-25 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f25b05f0-2aae-3044-bd44-13131eb70155 | -8.7423 | -50.4093 | 2024-11-25 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2e52e7e-793f-352e-be4b-1c2d9d976336 | -11.55316 | -61.91853 | 2024-11-25 04:57:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddfe1d48-8e9a-3e0d-b6d5-c9101757e9fb | -9.91588 | -64.05131 | 2024-11-25 04:57:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 984a59b4-6be0-36a8-83f8-55023c788e27 | -10.84604 | -56.41196 | 2024-11-25 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbb585ff-d484-310b-b0c9-69016e6be968 | -9.96249 | -48.07055 | 2024-11-25 04:57:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7db4ff41-96b6-30bd-97f9-fe00a6cb54d8 | -9.81851 | -48.17099 | 2024-11-25 04:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cf5c7eb-8226-37ab-9f3f-7787fe74328d | -10.62901 | -54.6097 | 2024-11-25 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2fc28bfa-66e8-3b4d-985a-85dce7aaf1f5 | -7.57479 | -49.40584 | 2024-11-25 04:57:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cffb7e8-7473-36b0-bc39-c68bfb6cac56 | -7.30846 | -55.30514 | 2024-11-25 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac208828-3c4b-34ba-b456-4d38493e37c3 | -11.42499 | -54.29529 | 2024-11-25 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95daedaa-270a-3e6f-8c3d-fb2f15d4cade | -7.57881 | -49.40645 | 2024-11-25 04:57:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c05b54e4-a685-3610-8949-da8db2e06d74 | -8.79446 | -47.59649 | 2024-11-25 04:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80844391-5f06-3264-bccc-d16430c08b84 | -11.86986 | -63.83727 | 2024-11-25 04:57:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dbcb11c-16e5-3963-a4b9-1c6dc06a0f22 | -7.8093 | -50.77304 | 2024-11-25 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d5e9df0-1a95-35b8-b942-9766759706ce | -8.89837 | -46.63377 | 2024-11-25 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 091df7c4-3509-3860-be1e-97cd3a6ad135 | -8.50415 | -47.06141 | 2024-11-25 04:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 021c9167-34da-33e7-8c5e-3436baced3df | -9.82302 | -48.17169 | 2024-11-25 04:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 128abf2a-060d-3681-a854-7b512d3cf3ea | -7.26253 | -49.5111 | 2024-11-25 04:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README50.md)
