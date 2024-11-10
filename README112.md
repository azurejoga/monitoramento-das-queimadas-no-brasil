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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25dc36d2-f7c8-30f3-893c-8e7ad40ebaa4 | -2.92634 | -51.48793 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 575f1022-dc1b-3453-be8b-efb43070203b | -4.80917 | -44.77547 | 2024-11-10 04:38:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa2ade29-e329-3f89-a6c1-901df5bb7fb5 | -2.3801 | -49.82725 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb71e47c-b9db-315a-818b-7e67966acea0 | -3.19689 | -46.49339 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce6c9329-acb4-3f39-953c-ca6e047ab437 | -3.02592 | -53.25974 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b539526-b7bd-3a90-bb22-437984e297ca | -4.36839 | -48.49267 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26703a6a-ff46-3700-8c14-9147aa4809af | -3.2185 | -50.3094 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7420e107-95dd-38eb-badb-b636f8890dd7 | -2.65455 | -48.48225 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c6ecbec-8b87-3d8f-8c62-b694bce22f29 | -1.75943 | -53.76033 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 497b4fc0-0d0f-3373-9c70-d2b2cd701e5c | -8.85016 | -47.69782 | 2024-11-10 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7843f4d6-0956-316b-81f1-4aa7da40c2db | -3.52924 | -51.63931 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 62eaa0c1-9c30-3fd0-b0e3-1e765266cbf4 | -4.43543 | -47.25845 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1279cf3-d712-332e-8421-aed3f0f8df19 | -2.92153 | -48.95923 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e771e239-6974-3d1d-aa4e-9edd869864b1 | -5.0854 | -47.79571 | 2024-11-10 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d9409f6-b074-38d4-af91-35ecc7d1965f | -3.24785 | -48.75513 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbbaf4d2-346a-3484-bab2-3a015d07d2c8 | -4.86438 | -48.11319 | 2024-11-10 04:38:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29237e2f-d85c-38f3-94f9-908855f0966e | -2.27088 | -50.66443 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66ab7a5b-2753-3a22-898d-4e1bee21bf9f | -2.87711 | -51.65698 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e466ff6a-b2ea-396e-b112-45fa0fe007bc | -2.95467 | -49.37009 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d669acef-d642-3be4-8af3-b85090872df7 | -2.86758 | -48.84814 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2aa173c2-b58e-30f2-ab22-07593a3c2fd8 | -2.79906 | -51.76963 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d331a6be-edf1-3092-9dfb-2ab38dd553f9 | -4.19499 | -51.01985 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62ee032f-90be-3f6c-a845-7c4ffbea9b45 | -3.22282 | -53.05872 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3dccfa41-8ac1-374d-b3f9-38e542206abf | -2.9532 | -49.50986 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fce0a46-2d1b-3fb9-af47-7176e1b6bfb9 | -3.22671 | -53.05938 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 90e9f402-a904-34dd-a781-a8334aec3fba | -4.19691 | -48.40154 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4b99fc1-6319-3bf7-b327-057803f83ba2 | -2.95264 | -49.51338 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a0eef67-f9b9-3e63-a666-f7b5605632e9 | -8.84899 | -47.70546 | 2024-11-10 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05e2b1df-0f1b-37b6-b521-4e2bbd1b3f37 | -3.35464 | -51.67716 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1ed7186-27c9-36ec-9fbe-497f9d414323 | -3.36657 | -49.92932 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aa2dd11-9d8a-39f6-8a3f-c83e2332adc8 | -3.58732 | -49.9897 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4aa7c8a8-1435-337f-b082-20303f8041de | -7.41021 | -43.09347 | 2024-11-10 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 167ab024-f730-3b21-a8e4-673229f56c83 | -3.23272 | -50.30789 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 52b467b7-03de-3c31-a151-a771f5b9febe | -5.69379 | -45.17574 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c79e19d5-e58b-339e-a5e0-cbb9877aa57a | -2.93312 | -49.50671 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08031b33-7bee-3ffe-9b47-1679d7eb2403 | -2.83727 | -49.23396 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e4af9d6-2e60-3601-b2cd-bf5db2d8f5eb | -3.19566 | -48.65895 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 625e10b7-fcd7-3395-97af-2b13d6ba4f47 | -3.62015 | -50.61664 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b0cf713-20ac-37f1-9f91-b39ce5200ca7 | -4.27843 | -50.67291 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e510fc90-b7de-3a85-bcfc-6df1c977b5c2 | -4.1726 | -46.59555 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8177a03-c80d-3a77-92f4-aa270c05fd10 | -2.63623 | -51.71553 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8a4cb8e-0532-39bd-9df0-716636320389 | -3.55024 | -49.98391 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64ef9a65-be75-31b7-a603-8b7868246f39 | -8.40726 | -44.1294 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c663f76-7203-31a0-b74e-62f314f5f2eb | -2.41214 | -48.84045 | 2024-11-10 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d70914a7-14e6-38ec-8655-8f3edb89a644 | -2.40804 | -50.39617 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c7a6a82-8760-301c-9e78-c186d5acd1bd | -4.61263 | -49.58401 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3295767e-acb2-3a73-a1ef-d12a335f802f | -3.87048 | -50.07736 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a0e6135-d284-39cc-a258-dcf1f88bbbcd | -4.38471 | -47.22453 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c57cceaf-a3c2-3ca0-9c19-95efed2cc3e6 | -2.31201 | -50.67482 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2cbaea6-7306-3231-87d9-32d7cb488bc0 | -2.47797 | -54.56324 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1db26274-1a35-3ddc-b318-2322ad564fd2 | -2.89779 | -46.82068 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1abd33a7-c37f-3759-a1ab-091398e7cec3 | -2.92281 | -51.67269 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f75c7c7-c375-307b-bf2d-b17f083995e3 | -8.41682 | -44.12286 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05f5c7cd-659d-30b5-a5e8-31190875a410 | -2.84521 | -49.82284 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 730c0ff1-34ad-34a8-a3a5-9f2d1d48e93f | -4.72225 | -48.78176 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ba9e78c7-de58-34e2-a3ac-921f9ebf17c8 | -4.41182 | -50.0816 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fef481e1-5759-303c-b6a3-59c380e35473 | -2.72063 | -48.34094 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b07ee03-15d9-3ab8-aed1-6ddcf72f2b0a | -4.11008 | -45.70957 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ec4aa8e-8219-3f13-8ec1-2a5d597130e7 | -3.10496 | -49.42186 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5223f7c1-eb41-3672-87dd-7ca7a09c56e9 | -3.03221 | -53.271 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2c5b22f0-6328-3a38-b839-33398899d238 | -3.95487 | -48.17206 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 35fdea06-31f9-387c-a9c7-a857f20887cd | -8.39154 | -44.11901 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9ba9aeb-679f-38e1-810b-1485a5c4c4bc | -3.018 | -53.25853 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f344288e-e9b0-3d87-a3a8-fd628c53e755 | -2.23485 | -53.78059 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b9d5c4e-bc1e-321e-b66f-a161b6d1af1b | -4.12252 | -48.50692 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 944792a9-debd-35d8-ab17-6dff27f79ed0 | -2.91021 | -50.40509 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5f0b555-4496-3940-ad7d-8870552f4823 | -4.88055 | -48.59384 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 164a2b09-0b06-377e-be07-9671c7952549 | -4.02517 | -48.28619 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bd268a5-6ad3-306b-b6a2-255d1179173e | -4.10265 | -49.10876 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc0de9f2-2b88-3c7d-b5c7-e15086cd37df | -5.56976 | -47.77459 | 2024-11-10 04:38:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 41dc0f1d-2b15-3c3b-8c5b-7cf897b34b5a | -2.69508 | -49.81749 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 029b8187-02ab-3852-8eb1-e21e0ec41bb4 | -4.34457 | -49.82133 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10f446a4-ec56-3fed-b5ae-97bc9da5efea | -2.93122 | -51.48037 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6b0e6789-bf9e-3ac4-b3eb-78d4ce89f879 | -2.4195 | -51.9516 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 516cfec8-6044-32db-bafe-9f1fd557fc02 | -2.43498 | -50.51531 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0161ab78-dd5f-31fa-8b17-f58815935992 | -8.40501 | -44.14495 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07fb85a5-d3e5-38eb-88a2-59919915060f | -2.87192 | -51.47163 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d89ea03-6976-3c16-acd0-e2ad7dbac74a | -2.90982 | -49.82933 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c064b78-91bd-3902-96f0-de4151055728 | -4.27421 | -48.18609 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a07a5a6-8477-3887-b735-b55a44a170e3 | -2.86151 | -51.80036 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b684002-ea1b-3d05-96bb-f11ff6b6f09c | -4.535 | -48.48635 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5ac8c0a6-527d-3413-8152-da38e2a67a7e | -4.31301 | -48.6505 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 405e2d16-7043-380f-957c-9b77d8790fc0 | -3.15615 | -54.48482 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb37d6b0-f63c-3fb9-a422-682662ed6db7 | -4.06236 | -48.30974 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d334f3e-d789-3c91-8438-0f7897ead6d6 | -2.93682 | -52.77357 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 199348d7-af85-3e96-81cf-27c40ab46367 | -2.2007 | -51.40207 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e21d4c8-993e-3e07-a529-a325d49df27a | -3.95875 | -48.16911 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 50fec9b5-a190-3ae7-b4fd-29670416d450 | -3.21974 | -50.27964 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 25fd18cb-3721-326e-b2ab-b0da603151ce | -2.6029 | -48.18848 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2809895-356f-3ede-9fee-051f330c75ad | -2.46977 | -48.58081 | 2024-11-10 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15abe068-d0f2-36dd-b131-48e707c2e2ba | -2.32797 | -50.5066 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d3aa33f-8f4d-3126-a5c3-47688ee4a97d | -3.22593 | -53.06425 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 479a6285-ab05-374e-a62c-9f7916c8bec3 | -4.45737 | -49.54145 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 079acbd2-3461-39ae-b21a-ddc0f859830d | -2.87065 | -51.47976 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 3ba0db09-9b12-3bf1-9c3c-fd0c384573b2 | -2.06141 | -52.28341 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44a5b7e9-a2c0-3168-b8fa-b781f05df2e7 | -5.27522 | -47.53756 | 2024-11-10 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f95f666d-6fba-35be-9aeb-1917e979a6b3 | -3.44302 | -50.30273 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13c8e6e9-2e00-3835-afdd-ba58bc46d916 | -3.23937 | -46.48455 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57877631-09da-3013-a823-7ba9a12aef47 | -3.67015 | -54.04 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6814a4e1-9d24-34f1-86c8-b2a8fe9606d8 | -2.01479 | -52.33231 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README113.md)
