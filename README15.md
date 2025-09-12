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
| 3a4cade3-6761-3df0-b77c-1b34491304e3 | -5.94383 | -42.7892 | 2025-09-12 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2306c678-6710-3fe4-a6f0-da0907b001dc | -7.08004 | -43.89077 | 2025-09-12 03:36:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7966c4b-9876-3345-9d77-03dacadb5ec5 | -7.17462 | -44.87358 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 984ddcd8-9bb0-3aee-9cbb-a8a950a8bed3 | -6.68065 | -44.13831 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ad217698-6685-3c66-b681-a553c8d57a7d | -7.2488 | -44.47724 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27b630d5-41af-328f-b10e-f433176c73e4 | -4.47186 | -38.72057 | 2025-09-12 03:36:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 97e16bdd-5387-3382-8808-1340c8054a8b | -8.18898 | -46.10899 | 2025-09-12 03:36:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 984b1d54-c0df-3d68-bae2-7e6365fd310f | -7.32167 | -44.37368 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7e1a32ad-a027-33d2-9277-ae473eecfeb5 | -6.15083 | -43.36959 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 89f238ef-f1f0-3669-a129-a4b11d06da6c | -7.24948 | -44.47344 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1e9b02a-d2ad-319e-ac2e-9f0dd2260d0d | -6.28082 | -43.66295 | 2025-09-12 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb8d5a0a-c2cc-3c2d-b47c-f709c92fb5e2 | -6.88035 | -42.83701 | 2025-09-12 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dce72a69-3a88-3a89-816e-50258e1f937b | -5.94489 | -42.56176 | 2025-09-12 03:36:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b6c72015-01c8-34f2-8ca0-f37258d5acc5 | -6.96836 | -44.82438 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 456cc17c-93bf-3360-9d41-15542c5e83af | -6.40776 | -42.60227 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9c069de7-0021-3948-b7af-2bf8954c2113 | -9.05651 | -40.52581 | 2025-09-12 03:36:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c285504d-f3c2-3979-9a6c-dae2ee51315e | -5.82895 | -39.65086 | 2025-09-12 03:36:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 753eaec5-e3c0-3efc-a0bb-24f9b71a7e4d | -5.94933 | -42.78044 | 2025-09-12 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3b4f91a9-8413-3fef-ac1d-346ceeeb9cf1 | -6.83082 | -45.6601 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 44dec6d4-82fb-3447-b7f7-0f0d4e8808a6 | -6.47696 | -45.14894 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca4a48cf-95de-341f-83e8-ee4a13b0951b | -6.24886 | -43.4268 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2960b258-147d-3508-bb55-7f31d897c055 | -6.40308 | -42.59828 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 17918125-00d9-3659-b119-6e745c9591cf | -6.26146 | -43.4855 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae47499f-e511-30c1-b698-7b2eeff4aad3 | -7.32238 | -44.3698 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5a666800-2e54-3d45-8754-d49171648254 | -7.72875 | -44.8697 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8dd7b28c-b99d-3fb2-bc48-b658c94df125 | -6.16864 | -43.36487 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b640668-826f-3ccc-a0cc-bcb8a9a1b146 | -7.84781 | -44.80629 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3de8cc4-8c23-352d-ab95-9e7ea6b22dc9 | -6.81917 | -45.65295 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dd9b26f-fa6d-394d-81eb-6c9b327f2ea9 | -8.18261 | -46.10809 | 2025-09-12 03:36:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2eb7276a-c3e1-3fd0-9865-f7d1ef8f22ce | -8.15059 | -39.89556 | 2025-09-12 03:36:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 16fa71e6-a8c9-3bdc-bc01-069dc4ec6ce7 | -7.46882 | -45.29379 | 2025-09-12 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12cdedf3-3c68-3924-b199-8c5292710b25 | -6.33968 | -43.04705 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d333c6c-3e3c-33a6-bf33-3bbdd947f256 | -6.68218 | -44.13753 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1c306cb2-acfa-3d43-931c-f5cb9294510d | -7.85234 | -44.80777 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3a75b67a-979d-3631-b78b-3bd6b54b0149 | -6.82547 | -45.65398 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ec6f1d1c-5b38-3772-ad0a-4e24cc787374 | -7.55797 | -44.39072 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 324b80a3-7145-3d31-a259-d969bca2b2d7 | -6.3117 | -42.22495 | 2025-09-12 03:36:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 55bcd7f3-59f9-3af5-82e9-9107a3308c24 | -6.15494 | -47.27562 | 2025-09-12 03:36:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 92fdf01d-e19a-313f-83e1-f49692b99ae3 | -7.72694 | -44.86814 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e4b5d08-e8c1-3963-b832-8c8f6fbdce30 | -6.32241 | -42.22355 | 2025-09-12 03:36:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d70865a6-97af-3a2d-8be9-d91a5213de4a | -6.49682 | -44.49396 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a0fea32-106c-39f9-aa16-9dd2c30a6569 | -7.45236 | -45.0033 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 82eb57e7-5bfc-341d-8da0-0d64e201e6f4 | -7.29535 | -44.48481 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e551af9d-2e79-3bcc-919a-295341a4f158 | -6.3168 | -42.22573 | 2025-09-12 03:36:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c8c73790-5584-3bf2-a0a5-11cae87a59cc | -6.4815 | -45.15893 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6f07d264-e3b0-3599-85f7-ff992985067a | -6.45247 | -41.76426 | 2025-09-12 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0e8999c5-f45e-34f0-a7e3-26be45a9a25c | -6.26027 | -43.48883 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cbc18d95-965a-3414-a9c9-544e267fa7a5 | -6.21797 | -43.37637 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e9b9eb2-31a7-3f77-a030-8846717ac25e | -6.67368 | -44.14429 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 06ae5451-7115-36a3-8a0e-b7c500bad156 | -7.84856 | -45.39521 | 2025-09-12 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3272b75-c986-390b-a34a-205cecef6d7e | -6.29814 | -44.23954 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1b0fd73e-61bd-3589-94d0-f5224bcaeada | -8.37233 | -44.84708 | 2025-09-12 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2dd1dd4b-a8f8-3b30-a3cb-e0bac6a5bbea | -7.91295 | -44.87393 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| abd4b1c0-1e8e-342a-877a-5973256efcd8 | -6.24822 | -43.43046 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 18373560-f4f1-36c2-b90d-fefa3da30ac9 | -6.65899 | -44.127 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d65c680-348b-31fa-a2f2-c833b1df9211 | -7.45429 | -44.40057 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d83c0a49-7b78-3a98-bde2-7321fe9c4748 | -7.84237 | -45.39464 | 2025-09-12 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ebd6772-0caf-3e9e-bb3e-a9fd090b3f37 | -6.53629 | -43.11035 | 2025-09-12 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 915dbe72-2707-3f95-a7a7-3aee79ba02e4 | -7.44749 | -44.43811 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c15ee8e-1e9a-31f5-97c9-130ac73ea1de | -6.4871 | -43.88015 | 2025-09-12 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 98f27915-1621-36cc-ab14-c3c803a796b8 | -7.44847 | -44.39989 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39441317-40ee-3489-8deb-2e5b4d9ed95c | -6.31201 | -43.32686 | 2025-09-12 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38f24782-c8e3-3b88-92ea-7ae26dbc457a | -8.37305 | -44.84329 | 2025-09-12 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3deacf98-a87f-3e40-afed-c8724fe53ab3 | -5.49768 | -42.68224 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2b445e07-e0c9-3891-9fff-c27f2dab369d | -8.08658 | -42.56614 | 2025-09-12 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 53216ac9-4cb0-3f9a-81d8-a447ad89fb83 | -6.67865 | -44.14968 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| eb6e3047-7713-384d-b155-ebb93363978e | -7.21846 | -43.97919 | 2025-09-12 03:36:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cfd51607-e287-34ae-a702-ab55e3cfe000 | -6.708 | -42.05059 | 2025-09-12 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6e020ce5-3f5b-31b0-8f0e-8e23b509a2a7 | -6.68426 | -44.15142 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 67ef7b80-efd6-356e-ad0e-cdf07848e1a1 | -5.95967 | -43.22773 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 582e1c5d-a38c-388d-8e4b-7d43b2cc6f11 | -3.89776 | -40.92045 | 2025-09-12 03:36:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e0f7eaf-7c89-3f99-9cf2-4f5710a082a9 | -6.15184 | -42.61477 | 2025-09-12 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5ae8ba97-22c1-35e1-9466-551331cb3713 | -6.65652 | -44.14094 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7c7493f9-53ba-3c5f-9f6b-1a67467e224c | -6.2932 | -44.23364 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b9ae2a3-c0dc-3229-a349-25c3fe125a99 | -8.18356 | -46.10311 | 2025-09-12 03:36:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8559d7e2-b1b4-3d30-9d6f-3936fc86c2fe | -7.15307 | -44.34455 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7196edd3-8a49-329c-835d-e91de0091e94 | -6.16761 | -47.28513 | 2025-09-12 03:36:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e1d9a5f-cc99-3fb5-81e5-c09f94d8681f | -6.30524 | -44.23326 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a92c2414-2852-3946-80f1-0b9c5dcd031c | -6.47536 | -45.15786 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c20a6cd-2a6b-394d-8bdb-ee78b4096b93 | -6.25487 | -43.42414 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f0da05c-765f-3337-b3f8-7b7ff6703237 | -6.34183 | -43.05069 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b1face50-90fa-3430-b95c-f8f5c22d3ef2 | -6.26579 | -43.48988 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ddd8e53-17d2-35ba-a845-ba7a96b6df93 | -7.31924 | -35.04178 | 2025-09-12 03:36:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c846c4c6-dfcd-3152-91a9-c497b3084f54 | -6.10642 | -45.94313 | 2025-09-12 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c8227e7d-2aba-391f-a01a-46d3d19ad353 | -6.32041 | -43.43904 | 2025-09-12 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72541609-cc36-3eac-8aab-86260605acfa | -6.15701 | -43.36658 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1bb703b-f644-3c5e-9cfe-62f071da3910 | -6.25435 | -43.42789 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| da4d4378-f813-3c33-9321-562426deccf3 | -8.18563 | -42.41623 | 2025-09-12 03:36:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2fe9eaac-f57f-3ed5-96f0-11f17fe23ab8 | -7.24968 | -44.47249 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 46faca5e-7ba3-35f0-b7af-ee1aa93143c9 | -8.36726 | -44.842 | 2025-09-12 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dfacfff-ea7f-3b45-b3e0-63c937dd7d9a | -6.54763 | -43.10878 | 2025-09-12 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| faaba5d2-c58a-3ed7-9877-d37ac0c9f443 | -4.93746 | -45.59445 | 2025-09-12 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fb20a19f-57b9-35df-860f-80ca64d7e7f5 | -6.83478 | -45.6546 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 21a58581-30e9-3ce8-b97d-5b031ec8b520 | -6.197 | -42.66528 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ebad901d-fbe7-39de-af86-098ecd7105a3 | -7.85493 | -45.39808 | 2025-09-12 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e96bf64-6cb8-3220-937d-9ad058fc3629 | -6.56552 | -43.14798 | 2025-09-12 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 543f7091-72b4-3244-8cdf-8ab102477a37 | -6.17316 | -43.50053 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06c9380a-6cde-359e-8483-ae81a7e9099f | -6.83391 | -45.65942 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d748ec6e-73a6-34a2-815b-6cf07d653694 | -6.27509 | -43.66268 | 2025-09-12 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fec9319-b8e9-3ee7-8392-583404a4c2ea | -8.18304 | -42.43055 | 2025-09-12 03:36:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README16.md)
