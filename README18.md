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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0f9430b-f7c8-32bc-9f23-adaf7f4823ac | -3.99274 | -43.31804 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8034405-0a39-32f9-a52d-5a8bc98be7fe | -3.14058 | -50.16063 | 2025-10-28 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9367ae67-03f2-3564-8901-ec7e5e196e27 | -5.89696 | -37.82199 | 2025-10-28 04:12:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e81cacb7-8704-39eb-8e4a-6c30ef520c9c | -3.5445 | -49.43553 | 2025-10-28 04:12:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d0bad1a-62a1-3407-8106-f1a233ed278b | -5.43481 | -40.8769 | 2025-10-28 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a84047f-a64f-391d-b068-4b73ef30986a | -2.91477 | -48.72378 | 2025-10-28 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 537b4c55-cc8c-3ad1-b355-05ba365fa528 | -6.12546 | -41.70924 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| afd98e67-626f-3a2e-b24b-c74b8dbae595 | -3.58936 | -43.63247 | 2025-10-28 04:12:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 62a54aac-85fe-3566-b281-c6cb78726e45 | -6.11218 | -41.72894 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5e3457a8-e36f-3732-9623-13daf4750422 | -5.66134 | -41.14312 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 893ac3a8-9fee-3540-8195-d0fd190f3fe5 | -3.5782 | -43.61622 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0becdd8-9827-3f7d-b9ef-4c93ca6e61ac | -5.46203 | -40.88128 | 2025-10-28 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43fba5eb-7e0d-3d68-bf65-6607dd5288cc | -6.1538 | -41.68076 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 56bc259a-7d01-3b40-8123-03ec42a4518a | -4.80572 | -43.42904 | 2025-10-28 04:12:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be2e2359-61af-3580-b985-955f1e7fe67f | -5.22006 | -37.39008 | 2025-10-28 04:12:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 653e6a07-a26b-32be-bf7c-652f2bd9dcad | -3.70544 | -41.56763 | 2025-10-28 04:12:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ea7054af-a329-300d-9bf0-0003ccdf75a3 | -5.62047 | -42.66003 | 2025-10-28 04:12:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3038663b-3017-3f27-8978-98cf5d038e70 | -4.4442 | -45.98045 | 2025-10-28 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd17a40f-df37-349f-8e56-8bd9a55b25d4 | -5.58357 | -45.33923 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a25c5442-accf-330b-95a3-3d64c930a6f6 | -4.7268 | -43.19616 | 2025-10-28 04:12:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb6bd3cb-aa3d-3d0e-8126-f2347b070d77 | -6.1045 | -41.75668 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f5699121-3507-3087-acf0-2d40848a513c | -4.3426 | -41.8233 | 2025-10-28 04:12:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3f19d9b2-6f95-307a-aab5-cd4eb2762104 | -5.58644 | -45.34368 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43fefe6c-a9cb-3ca8-a7fb-b96bb297cd42 | -5.7697 | -42.98997 | 2025-10-28 04:12:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e1c5e1ef-d1b3-3c2a-8829-42c33ba62957 | -4.35915 | -48.65026 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25f693c2-e169-39b6-97d8-da9d7891b99a | -5.41951 | -35.66905 | 2025-10-28 04:12:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4942466c-d292-3355-89bb-17501e5bca6a | -2.44024 | -49.75759 | 2025-10-28 04:12:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5208a844-807d-3ff7-9931-0e1965e83e48 | -3.97487 | -44.3071 | 2025-10-28 04:12:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09d73bf3-4717-3acd-82f3-0aa46d225c5d | -4.5197 | -44.03468 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b878e18-138a-3bf9-a09d-ee20a049e5ed | -6.28994 | -40.85979 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec62f015-4519-34b8-b8a4-0f11238fbf79 | -3.13393 | -53.00483 | 2025-10-28 04:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d68c408-c09e-3b0a-a8a2-e3d67db0bec5 | -5.9769 | -42.73394 | 2025-10-28 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a21284a7-9295-3e54-a1b9-7c22d5325546 | -3.57406 | -49.02433 | 2025-10-28 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78af301b-15aa-34f9-b029-a557bacd7d9f | -3.71207 | -41.56865 | 2025-10-28 04:12:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f692aebe-5caa-3ba8-90cc-207658e888d8 | -4.23649 | -47.57911 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12da5aac-9c51-3a92-9e28-d1dc0f6f6f62 | -6.17811 | -41.58966 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bb432732-c216-3f66-be55-d35bfd06576d | -4.03363 | -50.44736 | 2025-10-28 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2dbd3914-8749-34f9-add4-8dad7c04b5eb | -3.72231 | -44.34738 | 2025-10-28 04:12:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1f81cad-ed74-3d27-a796-8946dde9ad11 | -3.57875 | -43.63447 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 208be064-2524-3fb1-8b8d-498f6816704f | -3.25987 | -44.07577 | 2025-10-28 04:12:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f47c14a-e3fa-3403-a749-366035be91bd | -6.11326 | -41.72187 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| af4cc256-0522-34b0-afc2-172433c1e017 | -4.87385 | -47.54404 | 2025-10-28 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e3ddd41-c736-3054-8d6c-86edf362b8fe | -2.75683 | -47.75808 | 2025-10-28 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| be51de1c-c72f-3dd4-9bf6-af260e036f54 | -5.84694 | -40.82071 | 2025-10-28 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ab1fd243-fee5-3393-8115-e1f1cd081d5f | -5.41439 | -44.83914 | 2025-10-28 04:12:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a83d2df4-dc76-3f9b-8e6d-4558e50c8b8f | -5.46143 | -40.88514 | 2025-10-28 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d6040eb3-975f-369b-9812-17dfbcfc0c6a | -3.70413 | -47.64055 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4b7fc56-c15c-3896-bc30-c4bef5d68c90 | -2.4228 | -48.44031 | 2025-10-28 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8db55c0f-3ac1-3d57-956d-b76820b7acb9 | -2.746 | -45.40783 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 352100d8-c93a-3e20-8b23-96e64b9bc8ab | -4.87669 | -43.27999 | 2025-10-28 04:12:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c916529-624b-38f6-95ef-d3018979fe4b | -5.4098 | -45.28814 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41c868ba-fed3-3b52-a7a6-2bb9bd6b12ed | -4.87328 | -47.54748 | 2025-10-28 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfa5e788-493e-3864-8867-21ce97fb1d5b | -3.11377 | -51.28866 | 2025-10-28 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27515e62-b6ef-3da2-8179-a3d2e26291f3 | -3.59271 | -43.61123 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e724833-e8e2-397a-92e7-8ea4fb5dd411 | -6.17613 | -41.69143 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ae8973b1-f593-33c5-9668-c82f0fd55f0d | -4.45781 | -43.65004 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2b48602-5e8f-3a7e-83ea-2e2cc4f4d5a1 | -5.06908 | -47.55527 | 2025-10-28 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99843bf0-c3ea-3604-a677-578bb48b904f | -2.43644 | -49.75493 | 2025-10-28 04:12:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24c46f82-416c-381e-bb85-0afc83226162 | -3.24944 | -50.03683 | 2025-10-28 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 710e19fd-968c-3dfc-99d3-598ff84028d3 | -3.01746 | -45.37108 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9958e42-08d4-352b-bad0-5651d51dcbd6 | -3.5351 | -50.31531 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4daeb8b1-9e99-365f-822d-48d7957d8ed7 | -4.43559 | -43.44547 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fadb4b4-ce57-31d7-9b24-200a028fe69c | -4.76784 | -49.52829 | 2025-10-28 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ea3daff-cc0e-3341-ad64-8c3bae18c7be | -0.90633 | -47.5499 | 2025-10-28 04:12:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65b38179-2dcd-3b67-adb4-db86b54eec77 | -2.7604 | -42.8425 | 2025-10-28 04:12:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdcb9601-915d-32dd-828c-cd811b154ed7 | -4.71235 | -46.42702 | 2025-10-28 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a5499646-4002-3d08-af9e-d09baa7ff907 | -3.7076 | -47.64501 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7189ecf6-2bc5-33a0-ae2f-6c4a92af96ac | -3.47259 | -49.97081 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b33b304-17b1-307b-857b-5be24247ba53 | -4.50675 | -42.8398 | 2025-10-28 04:12:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 180e8cd1-d6b1-33ba-a765-e944e2f1ae39 | -3.08853 | -44.4448 | 2025-10-28 04:12:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4bb39b7d-4216-3b1e-b40a-812d0f9a636e | -4.50951 | -42.84375 | 2025-10-28 04:12:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8efa048-9961-3d7b-8e13-36ea56ca0bc5 | -2.43543 | -49.75682 | 2025-10-28 04:12:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 774539a3-e506-39ab-81ed-1f3d0dadc941 | -3.57168 | -49.43755 | 2025-10-28 04:12:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 62572e53-caca-3f78-8e28-9d9a8099b337 | -4.02099 | -42.87908 | 2025-10-28 04:12:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5feb5be7-e19e-3b95-a3c0-bbb17b851240 | -5.83817 | -43.26955 | 2025-10-28 04:12:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04237422-ac36-32be-a7f9-fb773eb5a17c | -4.31272 | -48.06227 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 678bdda9-fb6f-3712-8b85-ed7eec6ead58 | -6.13776 | -41.71827 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8415d4e0-6b12-3337-8308-0c5849332b7e | -6.10069 | -39.66294 | 2025-10-28 04:12:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 815b3249-998d-3722-84a2-d4b7cb7380f8 | -5.58007 | -45.33867 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56416f39-8cf2-3728-aa0c-f498c8ff6233 | -3.19803 | -41.43856 | 2025-10-28 04:12:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3ee863ba-ae22-34cf-9e6a-7244e1c5221c | -3.99588 | -43.77329 | 2025-10-28 04:12:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bebc2470-2631-3a8a-96fa-1b2bc607661d | -3.70436 | -41.57458 | 2025-10-28 04:12:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a68538fe-71e8-3ad5-bd38-f58ec1fca5e9 | -3.49879 | -50.04794 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe306c03-24b4-3a36-a2ae-a09a4d0cf9ba | -3.05484 | -53.01739 | 2025-10-28 04:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1326588a-adfa-30b9-b353-429d1518e170 | -4.79321 | -46.59703 | 2025-10-28 04:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b51eaba4-dbd2-3809-9759-3a02a3c32997 | -3.31653 | -42.35965 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3304d7e3-fdad-3640-98c3-6f3f4368f456 | -3.58266 | -43.63143 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9c6cd01e-2046-3378-aa20-24b778bc42fe | -5.66189 | -41.13949 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d8765dfc-8145-3077-b0c2-6a739732f10c | -5.86943 | -43.22515 | 2025-10-28 04:12:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17db5bce-fa4d-32b9-9614-80e5fa8ab9cf | -3.4185 | -50.36909 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fb9dbc1-d83b-332f-bba7-5ad7a209e8ee | -3.89558 | -42.6833 | 2025-10-28 04:12:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| da9df188-ada8-3241-bdce-3f0b348a2088 | -4.46441 | -43.50009 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5473113-2b34-32da-ba53-d2df104e27ff | -5.6601 | -41.10573 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 364837a7-2bea-3bd5-b114-75f3f3175617 | -3.57596 | -43.63041 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a621e22e-cd7f-3b68-a5e7-8ceb98e88af1 | -5.65513 | -41.13845 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a96e303-029c-370e-b298-050ee188eb39 | -5.65458 | -41.14206 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 54842fcb-ca2b-3b83-9c20-a6625fe643e8 | -4.97575 | -44.87908 | 2025-10-28 04:12:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 74badfb9-2789-3026-a81d-473e1d43b6c1 | -4.64789 | -48.64533 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5f9b690-b6fc-3dbe-88e7-17e849e04e36 | -4.63344 | -47.41933 | 2025-10-28 04:12:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13818222-e3e7-3675-a28e-a1b7974172b9 | -3.44167 | -50.2249 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README19.md)
