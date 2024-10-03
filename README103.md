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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d22c6b5d-0e5c-33d4-a661-1adc60837a5c | -16.55999 | -58.22134 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7f0f69e5-7ebf-3473-b9eb-70fa814dc87d | -16.55928 | -58.2248 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| f000ac9c-94ce-3360-98e7-f11d5702e13b | -16.55857 | -58.22826 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 310cca51-a20a-36f7-9e84-c61e1f83dc5c | -16.55786 | -58.23174 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 756c45de-8aae-369a-8efa-9fdd9c6db16f | -16.5575 | -58.26068 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2b07232a-2c6c-3d34-954c-1928be37b6de | -16.55678 | -58.26417 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7a1bc081-fd62-37a0-9feb-d71dd1aaea12 | -16.55469 | -58.22017 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 75370409-5a3e-34bc-8056-aa716754ea10 | -16.55431 | -58.2491 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1447c7e0-cab9-3d95-893b-87af0e66b195 | -16.55398 | -58.22364 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d2c198e5-3c0e-3e3e-867e-4bd40b330531 | -16.5536 | -58.25256 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f0701879-e9e6-302e-ad4c-1d19f518571a | -16.55327 | -58.22712 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9255db73-49f4-3855-9c25-f2f714298a65 | -16.55289 | -58.25602 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| bd3559b2-b888-3b5c-9c57-48331bb6f987 | -16.55256 | -58.23059 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9a238cf8-cb22-35b9-a4fd-36b992bdd9b3 | -16.54903 | -58.24781 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 517bc9ce-2f78-3dfe-887e-55dd3ec0598e | -16.54341 | -58.2212 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3a32dd4c-9a04-369a-9d02-a3832bd11dcc | -16.54269 | -58.22469 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0aa0e8a0-7fa4-3027-8039-eb3225038955 | -16.54262 | -58.27907 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 1c662b32-f4b7-3ab3-b1f7-c93c1efe4b52 | -16.54191 | -58.2825 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 35d341b4-fe77-3d9f-9c0d-4d8afa8e49f4 | -16.53659 | -58.28131 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bfb75077-59db-3494-90ad-d5f8163a34ca | -16.53588 | -58.28476 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d61a54c4-e5fa-3787-966e-3d0c7c4235d5 | -16.53343 | -58.26965 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 099eb615-0d69-33d6-8a9e-0e9f964bdc5a | -16.53271 | -58.27314 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a6ce649e-b976-3d15-bfd2-31c79eb17e5e | -16.53199 | -58.27666 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b7fcf6d2-b210-3d79-815c-f1d08ac62284 | -13.41535 | -61.92903 | 2024-10-03 04:29:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ecba4842-c72f-3fc4-a906-264c2974d1e6 | -13.41319 | -61.92945 | 2024-10-03 04:29:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf2f186a-aa38-3958-b666-dd13a726082d | -12.69433 | -60.81238 | 2024-10-03 04:29:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ba7b4f8-cb91-3d01-a669-5a0a7f4be89f | -16.64664 | -44.36532 | 2024-10-03 04:29:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a612cb10-ac88-3ce7-974c-06c070a9350f | -17.93248 | -44.56322 | 2024-10-03 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fda5ef4-bfdf-3cbb-ad31-ac512191dccc | -17.67264 | -44.68418 | 2024-10-03 04:29:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b6a4dfd-d22d-355f-9b89-16ba4e1fe8bf | -16.90744 | -45.30807 | 2024-10-03 04:29:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e5e4473-0901-36d2-95ed-ee163d666051 | -16.90381 | -45.3075 | 2024-10-03 04:29:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca0c23a0-bed9-3338-902d-e2342e07e000 | -19.05962 | -45.55942 | 2024-10-03 04:29:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33e97917-3252-3466-97c6-fda760d4d431 | -19.0479 | -46.1629 | 2024-10-03 04:29:00 | NOAA-21 | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a444875-e591-3238-b52c-66e36cb62234 | -19.0473 | -46.16721 | 2024-10-03 04:29:00 | NOAA-21 | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6433ca0e-5312-3c9a-ae59-e23f14da1215 | -18.93391 | -46.30698 | 2024-10-03 04:29:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6481920b-5ccf-3df4-9432-66ff7bb3b5c4 | -20.07922 | -46.14797 | 2024-10-03 04:29:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0faa6bc-39dc-3716-b251-6acda260580b | -19.79356 | -45.01212 | 2024-10-03 04:29:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ee7eca3-5bf6-36bd-9243-ea34b562bc3e | -19.72358 | -45.07201 | 2024-10-03 04:29:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80c394f0-616b-3254-99a2-ba7518cdd122 | -19.72295 | -45.07681 | 2024-10-03 04:29:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b74114c1-8147-3956-9232-8c7378e00a11 | -19.71977 | -45.0715 | 2024-10-03 04:29:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bafe952-9310-31e0-b07d-26f99c8d81d6 | -19.66533 | -46.23698 | 2024-10-03 04:29:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c70df563-efc7-3d91-9749-690beddf1351 | -19.66257 | -46.23872 | 2024-10-03 04:29:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a03a666d-a558-363f-925e-284d373f0cef | -19.66174 | -46.23653 | 2024-10-03 04:29:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35436d14-13bb-39dc-86ef-76b1919033c4 | -19.58529 | -46.26984 | 2024-10-03 04:29:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a965270-213e-3d0d-96c3-013c37372d5b | -20.77053 | -46.30906 | 2024-10-03 04:29:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ccad08e-2b1c-39f2-a63f-7f5833b27f0d | -20.76693 | -46.30849 | 2024-10-03 04:29:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f34e390e-9f8b-3ec7-a082-82fb2f8c9717 | -20.53572 | -46.25531 | 2024-10-03 04:29:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45a38c7c-0d3b-3273-a8a6-b07c7572c0cc | -20.53512 | -46.25971 | 2024-10-03 04:29:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5a9fc88b-c163-38c4-ac01-5e6acc23999a | -20.80887 | -45.29532 | 2024-10-03 04:29:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bfcbd3bf-fdd4-3797-b2bb-f01373ef9416 | -20.30473 | -45.40229 | 2024-10-03 04:29:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f30fad76-1487-36f5-a1fd-75fbe743cd80 | -21.55819 | -46.05194 | 2024-10-03 04:29:00 | NOAA-21 | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 09c09333-750a-3cc0-a467-86e58fc27f84 | -21.54591 | -46.0596 | 2024-10-03 04:29:00 | NOAA-21 | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a59b6905-d57a-33c3-84bf-8b0ad4e1fdda | -21.37747 | -46.45707 | 2024-10-03 04:29:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 8e1ad238-fd15-30af-be20-fc77eadbac88 | -21.37387 | -46.45649 | 2024-10-03 04:29:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c4e239e3-4713-357a-989b-e1b95c8a9c05 | -21.37328 | -46.46086 | 2024-10-03 04:29:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| fddc409a-fdb3-3d25-90f7-1b2b98a89219 | -21.37027 | -46.45591 | 2024-10-03 04:29:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 17528eef-2a83-3cf9-81ff-bc34b9c0ed66 | -21.36968 | -46.46028 | 2024-10-03 04:29:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0947c77e-891c-3003-8891-89443ed91012 | -15.7613 | -46.16459 | 2024-10-03 04:29:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8440960c-ab5d-3b12-bfbd-0282b0379348 | -15.76073 | -46.1685 | 2024-10-03 04:29:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40065119-580a-33f5-9dc1-53c1ebed88dc | -15.73242 | -46.87698 | 2024-10-03 04:29:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cf25dfa-76b0-3616-a111-f597062b4e6c | -17.12036 | -47.13289 | 2024-10-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 07e3a468-0ad8-37a6-ab0f-05c5aa08bc36 | -17.1198 | -47.13663 | 2024-10-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5acd509e-17c2-3456-84bc-705fe9caf7b2 | -17.11358 | -47.13191 | 2024-10-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 550a7116-2bf5-33f3-b650-424588494adb | -17.10965 | -47.13511 | 2024-10-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f409f5e-02d6-3568-95d3-90fd10830652 | -17.60511 | -46.95894 | 2024-10-03 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4827246-116e-36c4-904f-5c0ff0c93db2 | -17.60462 | -46.96583 | 2024-10-03 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 160cb5d7-d659-36de-bfe3-12fcfbef3f78 | -17.60395 | -46.96678 | 2024-10-03 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e3ec0c0-b86c-3de2-afdd-31d48429b334 | -17.60171 | -46.95842 | 2024-10-03 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00c5d407-a930-31af-8e32-d17e101099c8 | -17.60113 | -46.9623 | 2024-10-03 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad6815f2-3e62-3157-b40a-df977225e6ad | -17.60055 | -46.96618 | 2024-10-03 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| baeb18f3-c47a-3d75-bd76-1ebb43c8167c | -17.59998 | -46.97003 | 2024-10-03 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 859866ee-5118-3ae4-836f-3f3dda36da33 | -17.5983 | -46.95789 | 2024-10-03 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c317fc1b-515b-3dde-8b31-2b89236adaec | -17.59715 | -46.96558 | 2024-10-03 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 951985fc-9229-3149-a323-d13b56225118 | -17.59602 | -46.9732 | 2024-10-03 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da3d9553-2642-36ff-8fb5-3981fdfae63d | -17.59375 | -46.965 | 2024-10-03 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b5f3910-25e5-3125-9213-954a869199ff | -17.41532 | -46.31487 | 2024-10-03 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 306dfca1-0afb-3325-99ca-828565e6e8f0 | -17.41474 | -46.31889 | 2024-10-03 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 577d901e-6c2e-3048-bdf8-bd8ecc640c14 | -17.11642 | -47.13612 | 2024-10-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 90f62a27-ca53-3ca2-946f-d125ef75889c | -16.71763 | -46.03706 | 2024-10-03 04:29:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 168c7a18-7da8-323e-bf84-3c44ec8da5f1 | -16.71705 | -46.04114 | 2024-10-03 04:29:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb5ea166-42d0-3433-81be-e746bc5da6b0 | -17.12374 | -47.13339 | 2024-10-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5f899719-dc42-3356-a090-4ec233856867 | -17.11753 | -47.12866 | 2024-10-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2d8be86a-2d87-3557-9e5a-5bb97c1a616d | -17.11697 | -47.1324 | 2024-10-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cac45801-b092-373e-9f52-cb1aa49e7cd7 | -17.11303 | -47.1356 | 2024-10-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 375c4743-eb31-390d-b3a7-a15d07507b7c | -17.10682 | -47.13089 | 2024-10-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dde2071-5574-3814-9c89-f7b47e9b5415 | -17.1102 | -47.1314 | 2024-10-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de36c218-7bad-377d-8f49-4c1844846820 | -18.81853 | -46.63397 | 2024-10-03 04:29:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b7f7e8c-9172-3121-86e7-7d777d394c69 | -18.81504 | -46.63343 | 2024-10-03 04:29:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2593ff17-b4c4-3ba7-8d94-0cfd16ff7702 | -18.81446 | -46.63746 | 2024-10-03 04:29:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 228ec340-3d13-378f-aac5-6452c25a90a1 | -20.08463 | -47.81382 | 2024-10-03 04:29:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a1cc3fb-9da6-3ffc-b598-2830733bcfc1 | -19.8963 | -46.93966 | 2024-10-03 04:29:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a5368f5-ba0b-35fd-a23d-fda0f4cd58c3 | -19.76297 | -46.60062 | 2024-10-03 04:29:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77801e6e-aaa3-3f30-b2af-fb8036fe4aed | -19.73626 | -47.91843 | 2024-10-03 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a056e8b-79e4-3ffa-9a47-3c30a761d76b | -19.61893 | -47.17223 | 2024-10-03 04:29:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 24b2d604-e7f1-3289-8e5f-c01bcf17db97 | -19.62237 | -47.17278 | 2024-10-03 04:29:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0b13b404-e98f-30c5-91c6-2fdfe545d474 | -20.95586 | -47.02615 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d480c891-ae1f-3c14-979d-baca8ccc4d76 | -20.88892 | -47.12027 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c1fc877-31e4-39a4-a9de-e083cd7335c7 | -20.87248 | -46.93147 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11fe76ec-58df-3d37-b760-78d44bd750c0 | -20.86898 | -46.93088 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 84ec3952-51ee-375d-a6ce-7c85a26ed232 | -20.86679 | -47.07503 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README104.md)
