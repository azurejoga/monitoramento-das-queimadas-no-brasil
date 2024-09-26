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
| 75491f67-d57e-307f-bc15-f77540366b04 | -20.02942 | -43.1893 | 2024-09-26 00:41:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 65fd19a8-b68a-35db-ae9c-9c682af2cf26 | -20.02813 | -43.17965 | 2024-09-26 00:41:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 65e5c39c-971e-3ebe-9968-93fd76b41e0d | -19.99302 | -47.16082 | 2024-09-26 00:41:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| bcdf1783-1ab3-3f48-9955-9638ac6431f6 | -19.98849 | -42.34654 | 2024-09-26 00:41:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| d3bce812-043a-3d5f-99bb-cc1758e9c825 | -19.97523 | -45.5591 | 2024-09-26 00:41:00 | TERRA_M-M | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 22f25ded-ae6a-3eef-a876-4ae46a704935 | -19.97374 | -45.5469 | 2024-09-26 00:41:00 | TERRA_M-M | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 02d7e47f-58b4-39a9-a4c9-518d8796a046 | -19.95498 | -44.97248 | 2024-09-26 00:41:00 | TERRA_M-M | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 34.5 |
| d2a1ed1e-7a38-3e73-90a2-cecfdc074e14 | -19.95359 | -44.96115 | 2024-09-26 00:41:00 | TERRA_M-M | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| a0b8d9db-17eb-3184-a8b8-fe79c2d01614 | -19.93523 | -43.79556 | 2024-09-26 00:41:00 | TERRA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.4 |
| ef721314-4d93-3eee-b4c6-0176a51c979d | -19.93389 | -43.78537 | 2024-09-26 00:41:00 | TERRA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 9df80386-60bf-32da-80d8-735a13cb64e2 | -19.93257 | -43.7753 | 2024-09-26 00:41:00 | TERRA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a2c1c9cb-f1a0-3832-a97c-d680eac2286a | -19.92609 | -43.79696 | 2024-09-26 00:41:00 | TERRA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| e5987f4d-5b6e-338a-a67d-794578c3cfd5 | -19.92477 | -43.78684 | 2024-09-26 00:41:00 | TERRA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| 3e3dae34-1349-33ca-af74-1dcadcae287b | -19.92342 | -43.77659 | 2024-09-26 00:41:00 | TERRA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 0702ca1c-0e37-3634-b6ec-08c779f95fa5 | -19.91867 | -41.65602 | 2024-09-26 00:41:00 | TERRA_M-M | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 1fb2d275-11f4-3c1f-943a-04dd9fad5537 | -19.91733 | -41.64657 | 2024-09-26 00:41:00 | TERRA_M-M | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 9efd862a-0ec8-3ff5-b534-ba30fb470f82 | -19.91697 | -43.79845 | 2024-09-26 00:41:00 | TERRA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 2a9d9f75-87dc-39c3-9e97-51833ef0af41 | -19.91598 | -41.63712 | 2024-09-26 00:41:00 | TERRA_M-M | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 7b678ea4-93b3-33a8-a9b2-ea3c43f7ed4a | -19.82248 | -41.94784 | 2024-09-26 00:41:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 383676bf-83c7-363a-8573-a88855401d5d | -19.82116 | -41.93848 | 2024-09-26 00:41:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 7c7d63be-2e72-3ba2-947e-027a5de85737 | -19.789 | -51.49155 | 2024-09-26 00:41:00 | TERRA_M-M | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 6a9e4b76-742a-3631-b8e0-6a765e966cab | -19.78694 | -44.13937 | 2024-09-26 00:41:00 | TERRA_M-M | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 58fe1a76-5a62-3f4a-947c-9dc1dee37538 | -19.78563 | -44.12917 | 2024-09-26 00:41:00 | TERRA_M-M | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ecf97b81-6c84-332c-bf38-f22a27ba92b1 | -19.77825 | -51.49763 | 2024-09-26 00:41:00 | TERRA_M-M | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 1213149f-9f1c-3ce2-9ad7-e5a7ddc7af44 | -19.75664 | -43.97799 | 2024-09-26 00:41:00 | TERRA_M-M | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 54a254aa-c6ab-388a-9c7e-5dd161358f41 | -19.7218 | -41.9508 | 2024-09-26 00:41:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 3e108104-e041-3dae-85aa-05be63783661 | -19.70932 | -42.39027 | 2024-09-26 00:41:00 | TERRA_M-M | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 9d2691dc-7068-315d-b035-3c2fdc689814 | -19.68483 | -42.41919 | 2024-09-26 00:41:00 | TERRA_M-M | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| fab1f0d7-65a5-3be9-812b-dcf79a048678 | -19.67855 | -42.43935 | 2024-09-26 00:41:00 | TERRA_M-M | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 97667c9c-4cbb-3c30-8650-668c4bdf1fa5 | -19.64531 | -44.17228 | 2024-09-26 00:41:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a789a0ba-4c4e-383e-a9e9-8ac1ba70f112 | -19.64396 | -44.162 | 2024-09-26 00:41:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 364b57c6-c558-3bad-966b-f9bdd8fada32 | -19.64386 | -43.81681 | 2024-09-26 00:41:00 | TERRA_M-M | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7b358ffa-1be4-3b71-9d4a-a1cc92f76c22 | -19.64256 | -43.80691 | 2024-09-26 00:41:00 | TERRA_M-M | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2fe262b1-c24f-3151-b53a-3d635b5a543e | -19.63736 | -44.18369 | 2024-09-26 00:41:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4cf84d74-d13e-3250-9bcc-e5d95a116c23 | -19.63472 | -44.16338 | 2024-09-26 00:41:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 14091561-9253-3082-9479-385ec34ea746 | -19.63426 | -40.21391 | 2024-09-26 00:41:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 95fe1525-4a03-357c-953f-bb33417e3aa1 | -19.62817 | -43.83929 | 2024-09-26 00:41:00 | TERRA_M-M | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| de7d599e-8c94-3930-b586-4029850a26d4 | -19.62812 | -44.18519 | 2024-09-26 00:41:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 02dde3c0-e2a2-3cb2-82a7-ac506947d7de | -19.61936 | -42.81017 | 2024-09-26 00:41:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d4e59ea0-9aa0-3ab5-82d2-ad94267a7008 | -19.6181 | -42.80088 | 2024-09-26 00:41:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.9 |
| 0a5aa024-08f7-3d90-85a4-255acebdc27e | -19.61682 | -42.79151 | 2024-09-26 00:41:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| f03b5f99-ff80-3a6b-9732-b2d36d093035 | -19.60299 | -44.93281 | 2024-09-26 00:41:00 | TERRA_M-M | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| f4418f41-5d8a-3417-9ef3-fb86621f3728 | -19.60159 | -44.92157 | 2024-09-26 00:41:00 | TERRA_M-M | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 795d0599-99e4-3961-b759-c50c8a661a7c | -19.57898 | -43.53417 | 2024-09-26 00:41:00 | TERRA_M-M | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 1faa9f27-8eef-37a8-a38d-32d60db8d71a | -19.5714 | -44.9146 | 2024-09-26 00:41:00 | TERRA_M-M | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6d1681ff-bdb5-3f4d-8bcd-693e3da4de08 | -19.52156 | -44.51468 | 2024-09-26 00:41:00 | TERRA_M-M | FORTUNA DE MINAS | MINAS GERAIS | Brasil | 3126406 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 29a5284e-8575-366d-a8fb-b3aabe1c84d3 | -19.52022 | -44.50405 | 2024-09-26 00:41:00 | TERRA_M-M | CACHOEIRA DA PRATA | MINAS GERAIS | Brasil | 3109600 | 31 | 33 | nan | nan | nan | Cerrado | 54.2 |
| a4a266a9-b376-3f5b-afdf-aaf855185c4c | -19.45803 | -49.15013 | 2024-09-26 00:41:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 5085fd72-c85e-3588-bc5f-10403829c5d4 | -19.27511 | -49.13947 | 2024-09-26 00:41:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 28c07437-3949-3901-b72f-b3d5d3947259 | -19.26701 | -42.72609 | 2024-09-26 00:41:00 | TERRA_M-M | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 9a19ce75-7b8d-3c9b-8723-b8c677260a69 | -19.25813 | -42.72751 | 2024-09-26 00:41:00 | TERRA_M-M | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| c34b5196-cdcb-3474-887b-2492cdcac7bb | -19.19179 | -42.57535 | 2024-09-26 00:41:00 | TERRA_M-M | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 80e30be5-db4b-3aa6-ab73-5dcc6507fa5b | -19.18524 | -41.87203 | 2024-09-26 00:41:00 | TERRA_M-M | ITANHOMI | MINAS GERAIS | Brasil | 3133204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| bf868238-3393-333c-ab69-bc5e4739af0d | -19.1842 | -42.58607 | 2024-09-26 00:41:00 | TERRA_M-M | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| b8dea6ee-51f6-30bd-bc52-33054a59913a | -19.18291 | -42.57674 | 2024-09-26 00:41:00 | TERRA_M-M | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| cd3a1db9-8899-3ee5-bc6f-708e91cdd644 | -19.17234 | -42.43514 | 2024-09-26 00:41:00 | TERRA_M-M | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| e6f9c150-2009-37c9-a6f6-3608d5332ab0 | -19.14024 | -42.47469 | 2024-09-26 00:41:00 | TERRA_M-M | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.3 |
| 884ec626-8d3c-3bac-8d7b-f9d9aa8fc31d | -19.13894 | -42.46534 | 2024-09-26 00:41:00 | TERRA_M-M | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| c896bcf8-ef36-3655-81fa-f33cdc0a1d69 | -19.09174 | -45.08704 | 2024-09-26 00:41:00 | TERRA_M-M | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 67673180-4a72-34db-b598-bb793e001204 | -19.07228 | -47.29245 | 2024-09-26 00:41:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| b7f963e8-7271-385b-b778-76b427b5a3af | -19.04777 | -42.73409 | 2024-09-26 00:41:00 | TERRA_M-M | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| ab66531a-a728-3e67-b069-918202674467 | -21.00708 | -49.07188 | 2024-09-26 00:41:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.3 |
| a2e67a28-63c5-3eb1-a0f0-08b647d2c48c | -19.04649 | -42.72479 | 2024-09-26 00:41:00 | TERRA_M-M | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 7b238f30-acc5-3953-bb96-013b844dd5d8 | -19.00179 | -42.598 | 2024-09-26 00:41:00 | TERRA_M-M | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| acf1b5d8-492f-310b-b9fd-15be64c67bc0 | -18.98301 | -41.11184 | 2024-09-26 00:41:00 | TERRA_M-M | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| c550706e-e1f4-364f-8617-07cd3457ac01 | -18.85824 | -43.43657 | 2024-09-26 00:41:00 | TERRA_M-M | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 17880c79-f6d9-389b-b658-c897c3fd077c | -18.8099 | -43.62571 | 2024-09-26 00:41:00 | TERRA_M-M | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 55d70281-ce3a-3c3b-98c7-c308dbb17e61 | -18.61582 | -43.41379 | 2024-09-26 00:41:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 262d2153-77fb-39ad-9326-2ffde1fb1597 | -18.58225 | -41.64953 | 2024-09-26 00:41:00 | TERRA_M-M | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| 3640f63d-35fb-3244-97b0-1784e0333fb9 | -18.58089 | -41.64009 | 2024-09-26 00:41:00 | TERRA_M-M | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 2f30f275-1e9a-347c-8cf5-a31e43c7d65b | -18.51274 | -47.09768 | 2024-09-26 00:41:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4a92ccd0-76cf-35c1-982e-cc286c940ae7 | -18.43152 | -45.09853 | 2024-09-26 00:41:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ad2a1ef6-1d12-367d-86f1-e1f183f5b163 | -18.38465 | -42.79382 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 3840ddef-31dd-3ddf-94d2-fa0a0782184f | -18.28684 | -44.04866 | 2024-09-26 00:41:00 | TERRA_M-M | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 859609a5-a8d4-31ef-977a-01f0d5d349d2 | -18.26847 | -42.68526 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| cc71cb68-b6eb-32de-ba72-0f581c091170 | -18.26718 | -42.67597 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| ada4047c-9fd2-34e0-9153-71677d40891f | -18.15209 | -42.78176 | 2024-09-26 00:41:00 | TERRA_M-M | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 5be47d91-cd60-3a02-b7e9-0bbbbd4753e0 | -18.1508 | -42.77248 | 2024-09-26 00:41:00 | TERRA_M-M | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.2 |
| 9e9b1f9e-fd1e-3dc9-aa4a-81d6ea4e94af | -18.02736 | -44.38708 | 2024-09-26 00:41:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e8791d1c-5b52-3e8b-bfc5-17406a6395e1 | -18.0208 | -44.39421 | 2024-09-26 00:41:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b5eaa000-83a5-3f94-ac36-87123430cca8 | -18.0195 | -44.38435 | 2024-09-26 00:41:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4003fcba-9cff-3753-aa32-31971ecb7728 | -17.99413 | -42.31009 | 2024-09-26 00:41:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 8399a179-0372-397f-a26c-29d5a078aefe | -17.99322 | -44.4702 | 2024-09-26 00:41:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| b46ad5b6-5bc9-3537-a69d-2e9d6ed06dc4 | -17.99282 | -42.3008 | 2024-09-26 00:41:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 55f33fc9-84e6-329c-bf42-9a8ed8157fcd | -17.98527 | -42.31151 | 2024-09-26 00:41:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 97cbf75d-0afa-3f42-ac34-40b3510fd95b | -17.984 | -44.47158 | 2024-09-26 00:41:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0fdf1311-8130-315a-8d39-50a2ca79da0a | -17.98396 | -42.30222 | 2024-09-26 00:41:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.8 |
| 9efb20c5-ea05-3adb-93c1-43f61fe9a302 | -17.92906 | -44.2652 | 2024-09-26 00:41:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a0a1a667-ce1f-3d7e-848b-88486de175db | -17.91582 | -42.14176 | 2024-09-26 00:41:00 | TERRA_M-M | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| dac834ca-6f1f-33b9-a8ff-92cf2880d480 | -17.79404 | -43.2507 | 2024-09-26 00:41:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 70.2 |
| d98a58bf-6489-352d-ad9a-1685ee82a850 | -17.79277 | -43.24138 | 2024-09-26 00:41:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8842d84b-9b9c-3ba8-90c3-85678edbd0cf | -17.64192 | -46.4423 | 2024-09-26 00:41:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 99efbfee-391d-3099-9ded-156d19c032b4 | -17.64034 | -46.42962 | 2024-09-26 00:41:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b6162bec-4cc8-3393-97fb-a7ccddd11963 | -17.63856 | -46.43694 | 2024-09-26 00:41:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 30.4 |
| d3e66169-6f35-3a32-b65c-87c05175b6bc | -17.63005 | -46.431 | 2024-09-26 00:41:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 77fe58d2-0203-308f-88f7-231862c84942 | -17.23596 | -46.29292 | 2024-09-26 00:41:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6e046ef2-46e2-3f1e-90b2-a7b757bf2d52 | -17.23444 | -46.28072 | 2024-09-26 00:41:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| cb382efa-a2ea-3408-b822-f6010f4f6448 | -17.05363 | -41.15863 | 2024-09-26 00:41:00 | TERRA_M-M | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 436f1eca-641d-3a69-a181-e81bcccc5b8b | -17.05215 | -41.14871 | 2024-09-26 00:41:00 | TERRA_M-M | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 74027b76-8f4d-3db2-80bf-aa8a08686726 | -16.65518 | -41.90046 | 2024-09-26 00:41:00 | TERRA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |


[Clique aqui para ver as próximas entradas](README11.md)
