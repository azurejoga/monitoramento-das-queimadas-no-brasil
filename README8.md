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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c03589e6-f86d-3010-8f0c-64bb87e366c7 | -4.1111 | -44.766701 | 2024-10-29 00:28:11 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 39d2071f-eead-3c8c-aea0-24fd0c6ce4f7 | -4.2819 | -45.518299 | 2024-10-29 00:28:11 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1abc25e4-bc1b-3699-86f6-18dac74c01a3 | -4.1778 | -45.105202 | 2024-10-29 00:28:11 | METOP-C | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| daa1524d-cf78-3397-bacd-0d8c69305d67 | -4.4317 | -46.271599 | 2024-10-29 00:28:11 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9cf49595-91e2-37d3-90c9-46568b66d78f | -4.4335 | -46.2794 | 2024-10-29 00:28:11 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 47b3cc02-de5a-3440-877c-4e413cb49478 | -3.8635 | -43.999401 | 2024-10-29 00:28:12 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5640e49-c150-31ba-b23e-2b4f8f108d05 | -4.919 | -48.632099 | 2024-10-29 00:28:12 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df4e70af-e85f-304f-83f0-af3e059c166b | -4.9214 | -48.6427 | 2024-10-29 00:28:12 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e80b710c-6161-3344-8c2c-cb64eaee6be1 | -4.4494 | -46.623798 | 2024-10-29 00:28:12 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1f8b17a6-c1a7-37bd-9f89-159c3c8de2a9 | -4.4512 | -46.631802 | 2024-10-29 00:28:12 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ede195a-8894-33cf-a0be-b56d51abe240 | -4.4531 | -46.6399 | 2024-10-29 00:28:12 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 073666e5-bc1b-36d3-a5c5-3c78bcd659af | -4.892 | -48.648998 | 2024-10-29 00:28:12 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84d39480-0551-3ec9-9738-47445ea45bec | -4.8943 | -48.6595 | 2024-10-29 00:28:12 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31508f54-caf8-3ce8-8c05-d23fd287d7c0 | -3.8458 | -44.146702 | 2024-10-29 00:28:13 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eab3da66-cc8f-3295-bb50-cd892af8ee36 | -4.224 | -45.808399 | 2024-10-29 00:28:13 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5b4b5f90-9379-3410-abe5-12b55e43fc7b | -4.2257 | -45.8158 | 2024-10-29 00:28:13 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d6e95752-5356-3a2a-93ac-085e1192032f | -4.161 | -45.5756 | 2024-10-29 00:28:13 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffb8acd2-9271-3489-aa65-466218cfc5e1 | -4.2159 | -45.818001 | 2024-10-29 00:28:13 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a445a492-9ef3-3ca4-bf94-dfaf00d2894c | -4.2788 | -46.095699 | 2024-10-29 00:28:13 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c1aee32-5a7f-3ae6-bb34-8496da4bad48 | -4.2806 | -46.103401 | 2024-10-29 00:28:13 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 72a28a32-aa31-3173-8d03-49a0ae1ddb6f | -4.3628 | -46.7873 | 2024-10-29 00:28:14 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab12be0-6128-335f-ba57-5578aa284ba3 | -3.7762 | -44.248299 | 2024-10-29 00:28:14 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc2bda3e-b6d6-3931-99c6-2af254188c6c | -4.3409 | -46.689899 | 2024-10-29 00:28:14 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ea34885-8bbc-3d07-811f-5d6c9434d242 | -4.3427 | -46.698002 | 2024-10-29 00:28:14 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e69410d-7336-3abb-b62a-dcdd57f3bbc3 | -4.3591 | -46.770901 | 2024-10-29 00:28:14 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ec0a458e-1586-3085-9adc-5e87236d855e | -4.361 | -46.779099 | 2024-10-29 00:28:14 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff0d20b-20a5-3144-8710-90bcb85e0e0c | -3.7926 | -44.410099 | 2024-10-29 00:28:15 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98aa2cc0-db6d-378c-90a8-894b85555656 | -3.7941 | -44.416901 | 2024-10-29 00:28:15 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2b6ff76-c93b-31c0-b979-1f63080b6054 | -3.4334 | -42.98 | 2024-10-29 00:28:15 | METOP-C | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61cce37d-c7b4-38d9-a458-b1bf1c99d12e | -3.435 | -42.9869 | 2024-10-29 00:28:15 | METOP-C | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73829888-6eeb-3efe-9936-b21c31b253f4 | -4.4436 | -47.604801 | 2024-10-29 00:28:16 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64f6d164-c9a5-3631-bf1c-03aef919176a | -4.4456 | -47.6138 | 2024-10-29 00:28:16 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d2ad277-c3c5-3598-be51-f58bcd0eb33e | -4.4338 | -47.606998 | 2024-10-29 00:28:16 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc52c44-97e6-3300-968e-b25da0153017 | -4.2268 | -46.868599 | 2024-10-29 00:28:17 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5afda842-5d8c-3b69-aa41-14af27e53aac | -4.2286 | -46.876801 | 2024-10-29 00:28:17 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 717c8176-4ea8-338b-8e50-a4400c08d9e6 | -4.217 | -46.8708 | 2024-10-29 00:28:17 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17eb6e58-a7c3-3175-bdd1-e21b362b899e | -3.862 | -45.710701 | 2024-10-29 00:28:18 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3abe7e00-aaf5-334d-9b3e-ea1cf86262a3 | -3.8637 | -45.717999 | 2024-10-29 00:28:18 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b77cd1de-7fd4-303d-8f71-422bb3bb5058 | -3.8539 | -45.7202 | 2024-10-29 00:28:19 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6ef4eec9-7e9b-3e0b-ac0e-e45ae7b5eee5 | -3.8555 | -45.727501 | 2024-10-29 00:28:19 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73d7bebc-4b88-34ca-a420-adb1c0fe1603 | -3.9664 | -46.398499 | 2024-10-29 00:28:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d26119de-d5f3-37c5-ad5c-9e1b41b8d7aa | -3.9681 | -46.4063 | 2024-10-29 00:28:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e3dee64-321e-38a6-b860-2437519723cd | -3.9699 | -46.414101 | 2024-10-29 00:28:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d2f2510-4046-3099-b153-b93263429d9a | -4.3582 | -48.141399 | 2024-10-29 00:28:19 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c1844b5-6ba6-3f67-abd2-df2f37096892 | -3.8499 | -45.930099 | 2024-10-29 00:28:19 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a2a226a9-cac2-3f50-8376-8690812dcb23 | -3.8516 | -45.9375 | 2024-10-29 00:28:19 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28deecdb-eeed-36f3-8c0e-6301c56f9eb2 | -3.9566 | -46.4007 | 2024-10-29 00:28:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89f70b55-8d92-3a4b-9ce7-f90f024f2f25 | -3.9583 | -46.408501 | 2024-10-29 00:28:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f0ea2774-3a54-35b9-8c97-d3a9c4fd7945 | -3.9601 | -46.416302 | 2024-10-29 00:28:19 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 075b574e-5ba7-3786-a126-51e825a9bba2 | -3.2489 | -43.253899 | 2024-10-29 00:28:19 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ad34830-23b5-3229-b28e-f04d91adb1b2 | -3.2505 | -43.260799 | 2024-10-29 00:28:19 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 991861fc-017b-33bd-9963-e1a1cd70fbf2 | -3.8401 | -45.932301 | 2024-10-29 00:28:20 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 768565b2-319a-36d8-8a6a-ff9c229c3e7a | -3.8418 | -45.939701 | 2024-10-29 00:28:20 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26bed9ce-f069-3cc3-a8e6-15e7f9dcea0a | -3.8694 | -46.106602 | 2024-10-29 00:28:20 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1fdfa6da-8fcf-33f7-bc15-e8ebbbe53329 | -3.8711 | -46.114201 | 2024-10-29 00:28:20 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 150bb715-f378-359c-a850-5b8e8c709069 | -3.4281 | -44.304501 | 2024-10-29 00:28:20 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 024a6e13-0d99-3e8a-8831-710c5e68fc91 | -3.4297 | -44.311298 | 2024-10-29 00:28:20 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36f67eee-8223-30b1-b1ef-1140f90031cb | -3.9128 | -46.434799 | 2024-10-29 00:28:20 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 80d4d150-9011-3866-8658-95f69ff80356 | -3.9145 | -46.4426 | 2024-10-29 00:28:20 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96776b93-8e44-314e-a2e9-5739f7ec9cbf | -3.2939 | -43.539299 | 2024-10-29 00:28:20 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48a5b134-fcb3-3cda-add2-d065becd1407 | -3.7813 | -45.945301 | 2024-10-29 00:28:21 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3318cff-4426-32a6-95f4-64b1596c1c51 | -3.783 | -45.952702 | 2024-10-29 00:28:21 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a055b169-73a2-3b49-855b-b0059a17056d | -4.2325 | -48.038399 | 2024-10-29 00:28:21 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6c144e8-b126-3ca2-b53c-63be49ddf3b3 | -3.8396 | -46.475399 | 2024-10-29 00:28:22 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dde3511f-c1dc-3886-ab72-0474bc58e872 | -3.8281 | -46.469799 | 2024-10-29 00:28:22 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9a7ac78d-0f1a-36e8-a2a9-6c93e0c4a503 | -3.8298 | -46.4776 | 2024-10-29 00:28:22 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac1a512-5a15-3f8d-b70e-59644eb929b7 | -3.2829 | -44.300999 | 2024-10-29 00:28:23 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad436e0e-cb21-3f42-8270-96b2c9b9bbb6 | -3.2845 | -44.307899 | 2024-10-29 00:28:23 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad5a2fe4-65e9-3408-bb71-dd9999e85247 | -3.2184 | -44.380001 | 2024-10-29 00:28:24 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99e67938-a451-306c-8c48-80b46222c95e | -3.5458 | -46.178101 | 2024-10-29 00:28:25 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5146f69-3477-3f16-925d-6b6ce8954c60 | -3.5475 | -46.1856 | 2024-10-29 00:28:25 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f091889-2503-3cb8-b61b-8911c00e02d1 | -3.4568 | -45.8773 | 2024-10-29 00:28:26 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8cc5ee1e-20d4-3c90-93be-73f5b095115c | -3.4585 | -45.884602 | 2024-10-29 00:28:26 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5731cf8-c79e-3c8b-92de-b25f90b369bf | -4.4804 | -50.628101 | 2024-10-29 00:28:26 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e052bc6a-301a-3aef-993b-bafe47a5f0a0 | -3.9394 | -48.3344 | 2024-10-29 00:28:27 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73fb09c3-be8b-33ed-adf1-2184db41d156 | -3.9416 | -48.3442 | 2024-10-29 00:28:27 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b3a84f8-f8ae-3259-828a-3ade7d846eb8 | -3.9438 | -48.354 | 2024-10-29 00:28:27 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e61dd61-00da-3894-83d5-bf685581e937 | -3.9296 | -48.336601 | 2024-10-29 00:28:27 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09540d6c-e2d0-3d43-9397-7910ba00ebb0 | -3.9318 | -48.346401 | 2024-10-29 00:28:27 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b38abf17-59e8-30a6-be46-3909c965225b | -3.9122 | -48.350601 | 2024-10-29 00:28:27 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dbb1a37-4b2d-3941-85f2-bceabadf5369 | -3.9144 | -48.360401 | 2024-10-29 00:28:27 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb3101a-9e3c-33f5-9231-eb7e9586a0f2 | -3.3275 | -45.8521 | 2024-10-29 00:28:28 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c2675fd3-11b0-3566-97a3-b9b98114bd22 | -3.0617 | -44.731701 | 2024-10-29 00:28:28 | METOP-C | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0fa2041-0098-35d0-a628-163e7844309b | -3.6205 | -47.281502 | 2024-10-29 00:28:28 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f15cc386-bc9b-3b6c-89c2-cb65f6e54246 | -3.6224 | -47.290001 | 2024-10-29 00:28:28 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e3e8220-e1dd-3ade-8216-b75864538b9b | -3.6243 | -47.298401 | 2024-10-29 00:28:28 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04d214d5-2650-3ab8-bed3-b504035eb457 | -3.6107 | -47.2836 | 2024-10-29 00:28:28 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01fecf2a-453b-3ecb-a89d-0368f5790255 | -3.6126 | -47.292099 | 2024-10-29 00:28:28 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dd5f240-a1c7-3ca1-8994-85d49c6afa5a | -3.6145 | -47.300499 | 2024-10-29 00:28:28 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b127bbc-dfbc-39fb-a62f-fa06da87e396 | -3.599 | -47.277302 | 2024-10-29 00:28:28 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3d39ce1-251d-3166-91ac-fd5028375cc1 | -3.0708 | -45.042 | 2024-10-29 00:28:29 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 330a93bc-1ec3-3c04-b2be-6c7856089712 | -3.2672 | -45.9039 | 2024-10-29 00:28:29 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7417c74d-054e-316a-93e8-fac95b12a009 | -3.2689 | -45.911201 | 2024-10-29 00:28:29 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 749ddd7a-6de0-3ab6-b72d-2afaa3595c46 | -3.2705 | -45.918598 | 2024-10-29 00:28:29 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac6b5016-d3a0-31db-8f99-aac6836b9769 | -3.9936 | -49.264801 | 2024-10-29 00:28:29 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75a45aa0-d2c6-380c-b7aa-773a6b5761eb | -3.9961 | -49.276001 | 2024-10-29 00:28:29 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4248267c-5f8a-38d3-ab8f-9483df1d6748 | -4.1002 | -49.973499 | 2024-10-29 00:28:30 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f44abdd-3f97-32a7-88ea-d644a7007de0 | -3.8452 | -48.875999 | 2024-10-29 00:28:30 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 061e7ac1-c9de-3926-bc9c-e8e20cff7a84 | -3.8476 | -48.886501 | 2024-10-29 00:28:30 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3c53be-a407-3df7-9466-5ab455491ba6 | -3.8331 | -48.867599 | 2024-10-29 00:28:30 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
