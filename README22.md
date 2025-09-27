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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02bcf2a0-4bf9-33fb-b209-cc125ffb0183 | -13.62919 | -48.07471 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d892e9f5-99b7-30d3-8591-e5a907e8b6ee | -19.47719 | -45.80573 | 2025-09-27 03:57:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bea6569d-2648-3f5f-b7f1-7881d5d8be4d | -14.59057 | -48.24623 | 2025-09-27 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81ec129b-13b1-3a96-b3ea-fe37d8a9c946 | -15.67356 | -43.59182 | 2025-09-27 03:57:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0500672e-a94f-359d-bf69-8d8d18d784e5 | -15.43162 | -48.22216 | 2025-09-27 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97b79061-b887-36e5-ac93-d77d50c031bb | -15.55723 | -47.91079 | 2025-09-27 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9e37396-4979-3c72-a886-7035c33cf3b9 | -14.84786 | -45.6061 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01d00971-d57e-3169-8137-e72713452686 | -12.65282 | -51.67063 | 2025-09-27 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed5f0cc0-746c-3226-b43d-a3d0a48bece4 | -17.54898 | -44.81241 | 2025-09-27 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96fd1ebc-8571-3e2d-bcea-8723b4cb913f | -14.60025 | -48.24531 | 2025-09-27 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccb9f4a0-0ea7-38be-9646-b5793fa5505d | -15.27255 | -46.44523 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6867c42e-eb5f-3e2f-892f-08efc0df5ef6 | -13.51609 | -47.41164 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c154e6d6-561b-329d-920c-029e4d78d584 | -14.88438 | -45.54894 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 619ba969-9153-33d1-be7d-3c1b7779214b | -19.92643 | -43.61671 | 2025-09-27 03:57:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aae4cb1f-6d2a-3190-9a32-8e98e81fc0e9 | -14.6362 | -48.29094 | 2025-09-27 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f189afcc-2072-3e9c-a9ce-92c7ecae146b | -13.50983 | -47.41951 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83fdd8a4-0285-3d67-94fa-a3f349fa8715 | -15.00702 | -49.23239 | 2025-09-27 03:57:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0dc79a36-6490-35a5-a49a-f54a1f1c5422 | -19.19901 | -44.05976 | 2025-09-27 03:57:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ac89d5ea-5a74-3881-b039-1254ec1fff8d | -16.91451 | -45.94828 | 2025-09-27 03:57:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02d44475-af29-3c67-91f6-ff6ca0347506 | -15.28043 | -46.42635 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 306c55fe-b312-3335-b83c-98d7ae075455 | -15.28313 | -46.43522 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 293b0101-050b-38f5-bdc6-10a342a41ee5 | -19.69901 | -45.89572 | 2025-09-27 03:57:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60f35fc0-0424-3213-83fd-59c8d11baf92 | -21.11332 | -42.92154 | 2025-09-27 03:57:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8f58d847-7e84-3f1c-b967-dbfffaa54223 | -15.04863 | -48.35969 | 2025-09-27 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76ac216f-7a8c-360c-b972-88433dde1148 | -15.57007 | -51.71068 | 2025-09-27 03:57:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7ffe3e39-4fde-3d62-97a0-80db0bdbb949 | -15.56188 | -47.91147 | 2025-09-27 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be9afdae-92a7-3dd0-8bfd-b1c3b777854a | -13.51691 | -47.40724 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b5d7e31-7088-3b21-ae81-68a687b96361 | -15.32269 | -47.87754 | 2025-09-27 03:57:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff0a33d5-f6e0-31d4-851b-5919aff3c918 | -19.63559 | -45.57565 | 2025-09-27 03:57:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11a3220d-28c9-3d10-b34f-dd151599aab8 | -19.93257 | -43.62194 | 2025-09-27 03:57:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f815d56f-6912-3a42-9b4a-287f35409fc9 | -15.99081 | -48.32552 | 2025-09-27 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a0cc21a-04d8-3aa8-97d4-0d9cbde2039c | -15.21472 | -49.41701 | 2025-09-27 03:57:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7bad10c2-8072-30c5-8f71-895c1825055a | -17.50601 | -46.74225 | 2025-09-27 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bb79fc5-cb22-3b6e-902c-558250182d7c | -15.53327 | -44.32905 | 2025-09-27 03:57:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d30ce406-64d3-3125-8801-b58ccb3d505d | -15.14517 | -46.4257 | 2025-09-27 03:57:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2e86fa1-ac04-3332-87ce-58bc63c641de | -20.36437 | -46.70543 | 2025-09-27 03:57:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8657b2c2-a07c-3c49-a14b-b44fd3168006 | -20.84026 | -46.36058 | 2025-09-27 03:57:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13f28a76-57ad-3790-a615-fc23cbf1eafd | -15.29604 | -49.28906 | 2025-09-27 03:57:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23b6e50a-a997-3fab-97de-6d0f6e6a5a00 | -14.60025 | -48.24766 | 2025-09-27 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc631b61-2a3c-3f14-8972-3d097941b10d | -15.11067 | -42.47222 | 2025-09-27 03:57:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 245b0399-31ce-3006-9fc9-75472cda6b73 | -15.42102 | -48.22638 | 2025-09-27 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3353aa98-8c20-33b2-8a85-cb3aac3619fe | -15.20188 | -48.46159 | 2025-09-27 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 86767b6c-cadc-34ec-9fbd-704acadd7071 | -20.27956 | -45.2809 | 2025-09-27 03:57:00 | NOAA-21 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2902f5fd-217a-3b92-b91f-7b26b38f24fa | -15.5371 | -44.33662 | 2025-09-27 03:57:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 74a78db4-1c6a-3b8e-9acc-a07599c361be | -21.18935 | -45.58862 | 2025-09-27 03:57:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9d9ba01e-5ff6-39ed-9025-0ebb1dc8b54f | -14.0675 | -48.81739 | 2025-09-27 03:57:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 730cb871-c675-3590-bfcb-3c38c742197c | -14.43101 | -44.87934 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d792645-16d7-3cb0-ab47-5aad83ab4f81 | -17.73505 | -46.70967 | 2025-09-27 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8ba6ea1-34ea-39cd-b0ef-e5617f8258ee | -14.85188 | -45.60686 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db6e735f-2103-363a-aeb2-727dda4e3900 | -20.27955 | -46.00775 | 2025-09-27 03:57:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fbc6bfd-f5a7-3d9e-9f2e-46cb59b39da9 | -15.53905 | -44.33948 | 2025-09-27 03:57:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cecb10d3-8188-39b8-a263-71057a29b72d | -19.41095 | -44.30604 | 2025-09-27 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 353c3a7a-28b3-3178-944e-8d2121a01f96 | -19.18352 | -46.04409 | 2025-09-27 03:57:00 | NOAA-21 | MATUTINA | MINAS GERAIS | Brasil | 3141207 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e27f9a6-528a-3773-83be-4cfe24c50e68 | -14.94875 | -47.49635 | 2025-09-27 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 123a476f-40ac-3735-b510-b8557db210ce | -15.42894 | -48.21066 | 2025-09-27 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22ac9b26-0d37-315c-bf47-d789f729e4b0 | -15.55357 | -47.90503 | 2025-09-27 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f368143-2526-36ea-9e53-6c20a66f6866 | -21.193 | -45.58928 | 2025-09-27 03:57:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5a6d599e-2158-372a-95a4-abadfc3bf422 | -14.06135 | -48.8221 | 2025-09-27 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c36388a-1394-3d5b-b3db-e8412376f75a | -13.51228 | -47.40639 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86a04d24-7182-3361-8a69-b1035e76a365 | -16.12546 | -47.39289 | 2025-09-27 03:57:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c771bc67-323e-3135-a922-db957b582fb7 | -13.83379 | -47.95916 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5feb4fcf-e912-3011-bb2c-0f377b5b1867 | -16.40423 | -43.72141 | 2025-09-27 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f92612f-2156-3f1d-8968-ac5e31116462 | -13.64389 | -48.07628 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1b87a7f-47c4-32a3-ab1d-57c31b99bbb1 | -15.03609 | -46.94973 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8875fb60-fb8a-3e39-bdfe-4bdbcd749d8d | -15.45597 | -49.63118 | 2025-09-27 03:57:00 | NOAA-21 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 091b9be5-1a9e-3eca-baeb-8c154b8af5be | -16.91386 | -45.95182 | 2025-09-27 03:57:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5d865e9b-113f-39a1-b226-77eea6fc340d | -15.57689 | -51.70745 | 2025-09-27 03:57:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 674ebf3f-91b5-328b-9004-b36867d9e880 | -14.97502 | -46.76245 | 2025-09-27 03:57:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af0c43f7-2075-3e0e-a1fa-d31ed17c47b1 | -15.279 | -46.43403 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d60ccb3e-e88c-35da-86fc-788397584d89 | -15.27176 | -46.4491 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66afec84-7acf-30c1-b282-4a4038d1c4d4 | -14.88286 | -45.54883 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d6f4491-e8b4-373d-b0d8-0e905ad1609c | -19.04886 | -48.1357 | 2025-09-27 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06a56e9f-7811-3ebb-8feb-6326d694326b | -15.19865 | -50.10291 | 2025-09-27 03:57:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2293300-b854-3513-9be6-eef4ba555e14 | -14.0658 | -48.82603 | 2025-09-27 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66c1ff35-4ba8-3b71-8eea-fcf64487f7f3 | -15.19732 | -48.46328 | 2025-09-27 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6312a79-7e81-3864-9f63-c7afe16407c9 | -15.26576 | -51.46887 | 2025-09-27 03:57:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 472504b6-d2dc-32f4-94f2-cafcec67b0e0 | -13.76494 | -47.8779 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 25c724cd-8851-3fdb-bcb0-228e5a7f7c24 | -15.27333 | -46.44106 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca18d9ff-2f99-378c-82cf-0acb2a8cf6d1 | -15.03535 | -46.95376 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| e81367c1-5bbf-3e54-b928-25298b54ab56 | -15.55258 | -47.91011 | 2025-09-27 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 15d0fa5e-bb20-37ed-b933-af2d274b8d38 | -15.2839 | -46.4311 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b40ca8f-e57a-32b8-8636-b9d330414b8a | -14.85374 | -45.57306 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a6ebb90-91d0-3d29-a415-ab812fc833c6 | -15.43265 | -48.2168 | 2025-09-27 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdec5de8-2b71-39fc-a8d9-4587682c3dc8 | -15.27244 | -51.46582 | 2025-09-27 03:57:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e3dcee49-55d8-3ae2-ae07-0e3c32af318c | -22.13144 | -42.32411 | 2025-09-27 03:57:00 | NOAA-21 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 939b4b44-caf7-3333-8740-54e468fa35c6 | -14.83744 | -45.64124 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbbccd33-8b73-39a5-b965-a62bc3661bd3 | -20.16973 | -46.2033 | 2025-09-27 03:57:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce7df6e7-1c55-397e-ba8e-97c05f986371 | -15.21017 | -49.41314 | 2025-09-27 03:57:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d26dd505-5c9d-377a-b7ac-268b33c1f2ff | -15.42688 | -48.22136 | 2025-09-27 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 745f6478-9c18-3f35-8527-a525d1788629 | -15.89082 | -46.19445 | 2025-09-27 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b9553772-0271-313b-a55e-2532c584c80b | -15.56912 | -51.71518 | 2025-09-27 03:57:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ff739c67-66eb-37e3-9419-5c5707e9bed0 | -20.05387 | -47.59085 | 2025-09-27 03:57:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 979f9d9a-77da-3164-bb92-41d67bc3a224 | -13.63906 | -48.07538 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cc9e6356-0b5f-307a-a49e-ee076cea03fe | -15.03964 | -46.95506 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0f9cd2e5-8953-314b-9d12-fe942cc69058 | -15.27974 | -46.43007 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 273764a0-6dcc-342d-9753-c5a4a03c1343 | -18.25093 | -47.00599 | 2025-09-27 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6d12714-a0d6-3141-885b-77a599cfb734 | -14.84594 | -45.61688 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fb70f55-95ac-3d4f-b5b5-c3a979109686 | -13.50606 | -47.41399 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11959a8b-2721-3ed8-8c63-4e3f00a0488f | -14.88474 | -45.53813 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5a86e0f-9aca-35b3-95eb-5584588a8c4a | -15.3273 | -47.87852 | 2025-09-27 03:57:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README23.md)
