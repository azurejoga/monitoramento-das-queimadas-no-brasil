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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9da74e94-9405-3b2e-b253-3c1410ce748e | -4.06 | -46.218498 | 2024-10-14 00:38:49 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6607e891-f8f0-39bb-a573-7a0ac5452119 | -4.0616 | -46.2253 | 2024-10-14 00:38:49 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f87e028-6784-3547-98e5-4e8a9610e587 | -4.3488 | -47.5728 | 2024-10-14 00:38:49 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db383d78-ac2f-3b78-b92e-135d565003bf | -3.4055 | -43.345299 | 2024-10-14 00:38:49 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b5de661-b05c-39d7-9eba-026bac3d6a5a | -4.3192 | -47.307201 | 2024-10-14 00:38:49 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de5eb6ba-0419-3d76-98a6-3a03a6a3616d | -4.3208 | -47.314201 | 2024-10-14 00:38:49 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2990186c-8e44-320b-a2ba-86d0ac3d6346 | -4.1789 | -46.7374 | 2024-10-14 00:38:49 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab97186d-79a7-3cec-928a-7ce26ce1fc43 | -3.8979 | -45.692799 | 2024-10-14 00:38:49 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c0495ec0-e0dd-3f94-9932-47fece8bb310 | -3.8995 | -45.6996 | 2024-10-14 00:38:49 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c86e265-f693-3763-a828-d90879674ac1 | -3.7234 | -44.980999 | 2024-10-14 00:38:50 | METOP-C | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69525f80-1f96-36ee-af54-1e3bf927116f | -3.8897 | -45.701801 | 2024-10-14 00:38:50 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d013154d-82ac-3fe7-92a1-0a2990832a3a | -4.145 | -46.8601 | 2024-10-14 00:38:50 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 135a0fef-ab91-3112-aea1-60d42c9cce02 | -3.6663 | -45.224998 | 2024-10-14 00:38:51 | METOP-C | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37c0b5e5-e633-307d-b186-2351c00b6bd0 | -3.8795 | -45.9715 | 2024-10-14 00:38:51 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43cc0dc6-0743-3f18-b4fe-e6188aee7461 | -3.8682 | -45.966801 | 2024-10-14 00:38:51 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1cfd4534-b87d-38b0-8b57-a524ce1628d3 | -3.8697 | -45.973701 | 2024-10-14 00:38:51 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b65f87a-7ab6-3efc-aa61-c7fc2e9ddae7 | -3.8584 | -45.969002 | 2024-10-14 00:38:51 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28d96783-5101-3ece-8171-24b2b5dee2c4 | -3.6761 | -45.222801 | 2024-10-14 00:38:51 | METOP-C | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5f1d4050-a371-329f-9127-8cdcc6dc3445 | -4.2173 | -47.855301 | 2024-10-14 00:38:52 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e92635d-ad03-36bb-bedc-f909e369ad2e | -4.2189 | -47.862499 | 2024-10-14 00:38:52 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cecbea8b-3f9f-3c85-8e47-96c78119eea1 | -3.9277 | -46.405998 | 2024-10-14 00:38:52 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 60fe4127-1b9f-37dc-be67-5e6d121bc27d | -3.9293 | -46.4128 | 2024-10-14 00:38:52 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2df0b510-20c3-38b0-8a88-3ec6d8d852e4 | -3.9308 | -46.419601 | 2024-10-14 00:38:52 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 24b9190b-0fc9-3827-833d-a0fcf925d4ec | -3.9324 | -46.426399 | 2024-10-14 00:38:52 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d081f1b6-af64-3030-87d3-1dd89a4582fe | -3.934 | -46.433201 | 2024-10-14 00:38:52 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f213d88-3927-3341-8113-630ed7e3448a | -3.8963 | -46.448898 | 2024-10-14 00:38:52 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94ecb531-c852-380b-b93f-733a5ca1ee23 | -3.8684 | -46.462299 | 2024-10-14 00:38:53 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4e184b6-3e05-3c6b-b92f-dcd1344e4a07 | -3.87 | -46.469101 | 2024-10-14 00:38:53 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5704c0f-a34e-31ae-add2-23462211d547 | -4.2683 | -48.216099 | 2024-10-14 00:38:53 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f02d1597-c689-3acf-8a49-78c15f31f121 | -4.27 | -48.2234 | 2024-10-14 00:38:53 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 178662cc-a481-328e-a031-45da82081393 | -3.8586 | -46.4645 | 2024-10-14 00:38:53 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9782b48d-c1c8-3c0f-ac9c-c21e4359f52d | -3.8602 | -46.471298 | 2024-10-14 00:38:53 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01307eda-f5af-31bd-a0ee-af7cdcdf2772 | -3.8504 | -46.473499 | 2024-10-14 00:38:53 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c36aa17a-582e-3bbf-bcca-45b744545168 | -3.839 | -46.4688 | 2024-10-14 00:38:53 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 48d88b13-42ab-3ec1-bddb-b373002015fb | -3.8406 | -46.475601 | 2024-10-14 00:38:53 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da6cb361-7360-3363-a385-9352ab96a36a | -4.1829 | -48.021301 | 2024-10-14 00:38:53 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2844c06-1519-384b-87f5-e5fa1298a21c | -4.1846 | -48.0285 | 2024-10-14 00:38:53 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef6fddb3-3ce4-37cb-b1b2-e794697951de | -4.3201 | -48.626801 | 2024-10-14 00:38:53 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7d90c32-440b-32dd-8138-d978d14383a5 | -4.3103 | -48.629002 | 2024-10-14 00:38:54 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a498f7e-f36c-3de2-a07c-9a1acebf9331 | -4.2805 | -48.587898 | 2024-10-14 00:38:54 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c7fa3f8-9293-31aa-a789-6b0f63a4c50a | -3.8446 | -46.898399 | 2024-10-14 00:38:55 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66281a8b-eebd-3020-9456-47a94285e22a | -3.8461 | -46.9053 | 2024-10-14 00:38:55 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fda5a938-e26b-3068-bd23-7894113a0139 | -3.8477 | -46.912102 | 2024-10-14 00:38:55 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 027cb5c6-df41-38c2-8555-691da5653769 | -3.8493 | -46.918999 | 2024-10-14 00:38:55 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e3efd12-8b32-3c21-834d-f6ee3f1530f3 | -3.8508 | -46.9258 | 2024-10-14 00:38:55 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04e4d7f7-2428-380a-856f-bde919a585a4 | -3.8348 | -46.9006 | 2024-10-14 00:38:55 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 14ad4dc5-6942-34b5-810e-218630f365c1 | -3.8363 | -46.907501 | 2024-10-14 00:38:55 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c4c1bc3c-c632-3ca4-9437-9ae1d68d3981 | -3.8379 | -46.914299 | 2024-10-14 00:38:55 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d73da5f7-3a99-3db8-b091-d1734a5246a0 | -4.0555 | -47.9137 | 2024-10-14 00:38:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e5ea5be-fcc3-3611-adcf-3e7ae5b15b3b | -4.1179 | -48.234001 | 2024-10-14 00:38:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b59c7071-aa4d-34e1-8a39-b8376de25dcb | -4.1195 | -48.241299 | 2024-10-14 00:38:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcf56ae2-18b9-35f0-9d22-d1e9ae76696d | -4.1064 | -48.228901 | 2024-10-14 00:38:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b37df20-a001-3274-960a-795e4b57415b | -4.1081 | -48.236198 | 2024-10-14 00:38:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e72c833c-0ac5-3464-ad4f-68eb7e0adf0d | -4.1097 | -48.2435 | 2024-10-14 00:38:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b6e8480-b125-384d-b2c1-6f258bd129c6 | -4.1114 | -48.250801 | 2024-10-14 00:38:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65179ca3-88cd-3670-bd54-c7892ae20968 | -4.1147 | -48.265499 | 2024-10-14 00:38:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5756164-d1c6-3b3e-9db9-4e41cdea1a8b | -4.1164 | -48.2728 | 2024-10-14 00:38:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c826bacb-1ff2-3b4c-806e-1ab58b98aa8e | -4.1181 | -48.280102 | 2024-10-14 00:38:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f8acc60-7701-3147-8a65-ed04a6f19cef | -4.1197 | -48.287498 | 2024-10-14 00:38:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e50e749f-6cbc-3d37-a49f-1fca1729b848 | -4.0983 | -48.2384 | 2024-10-14 00:38:56 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79657c0b-f7c8-352b-a63a-44e6a8c6a35e | -4.0999 | -48.245701 | 2024-10-14 00:38:56 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 218686a0-c62b-3300-80bd-c86f575ace8d | -4.1066 | -48.275002 | 2024-10-14 00:38:56 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3e3a190-444c-30ce-8e52-c4f4df7bba0b | -4.1083 | -48.282299 | 2024-10-14 00:38:56 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2428ebb9-5282-3941-9013-3481d52bddb9 | -4.1099 | -48.2897 | 2024-10-14 00:38:56 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 228c4d9c-b04e-36b1-bd2b-c82f8a633297 | -4.4227 | -49.720699 | 2024-10-14 00:38:56 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32adc837-1df2-3403-a5fc-c0cd26454ae2 | -4.4246 | -49.729198 | 2024-10-14 00:38:56 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9201149-ac0b-3a3c-89f4-6463fe21bc9f | -4.4265 | -49.737801 | 2024-10-14 00:38:56 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eb373cb-9d23-318a-b58a-a7cf26bebd13 | -4.0705 | -48.252201 | 2024-10-14 00:38:56 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1602d85-e339-3636-b28d-1b47f33ae412 | -4.399 | -49.752701 | 2024-10-14 00:38:56 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0faebb5-b6ed-34bf-b025-55ee64b4770f | -4.046 | -48.2346 | 2024-10-14 00:38:56 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89400b69-ef7e-3192-ba2d-354efb85dbe3 | -4.0476 | -48.241901 | 2024-10-14 00:38:56 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d177e88-fb06-3969-9a44-1e2166d2567a | -4.0493 | -48.249199 | 2024-10-14 00:38:56 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcad46be-f353-3fc4-9aad-231886db9b9c | -3.9525 | -47.959202 | 2024-10-14 00:38:57 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 837ce1c5-8bca-3d56-9a05-90e60119071a | -3.8169 | -47.499599 | 2024-10-14 00:38:57 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfad569c-7182-3c9e-981b-683f9e1408cd | -3.8185 | -47.5065 | 2024-10-14 00:38:57 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf9cbc07-2ed9-3f29-9b37-dcf1078961d3 | -3.0572 | -44.464298 | 2024-10-14 00:38:58 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1113513a-7fca-3ffb-9b03-f72f1cfbab06 | -3.059 | -44.471802 | 2024-10-14 00:38:58 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99c53d46-8c84-35b2-9a24-c0b4252102cf | -4.4305 | -50.534401 | 2024-10-14 00:38:59 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a7a47e9-58be-311d-a7d9-714dea67570d | -4.4326 | -50.5438 | 2024-10-14 00:38:59 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9325861-8178-3024-821a-de15705ba5a1 | -3.9155 | -48.340401 | 2024-10-14 00:38:59 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 652e8358-90fd-3355-8e7c-f7f7d1ce8400 | -3.9171 | -48.347698 | 2024-10-14 00:38:59 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da1ac1c0-950d-340f-a1f2-35f77bab927c | -3.9188 | -48.355099 | 2024-10-14 00:38:59 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60b7aa81-3eaf-3636-97da-a7900628e46d | -3.9205 | -48.362499 | 2024-10-14 00:38:59 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed65698d-35db-30d7-bda9-6f7cca9f72d8 | -3.9057 | -48.342602 | 2024-10-14 00:38:59 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1bbdd18-1912-3cae-810d-df5dec824abc | -3.9073 | -48.349899 | 2024-10-14 00:38:59 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3442284-0039-324c-87b2-6f4464a07218 | -3.909 | -48.3573 | 2024-10-14 00:38:59 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8644681-56b0-3728-b663-c44cf515d13d | -3.9107 | -48.364601 | 2024-10-14 00:38:59 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b716564-4d44-3d12-ab81-a25b032c31a4 | -3.8975 | -48.352001 | 2024-10-14 00:38:59 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4ddcccb-1c1b-3e42-8952-47920603beee | -3.8992 | -48.359402 | 2024-10-14 00:38:59 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5368593e-219e-394b-92fd-c85c48da6f01 | -4.3396 | -50.495098 | 2024-10-14 00:39:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 158e2079-ea7d-3e22-a77e-16a4eb3a8243 | -4.3416 | -50.504398 | 2024-10-14 00:39:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dba32d2-39e8-3cda-bfeb-2c9c66dcd345 | -4.3437 | -50.513802 | 2024-10-14 00:39:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0737df55-d8a6-3cf7-8645-f5e1a3316ff0 | -4.3214 | -50.459999 | 2024-10-14 00:39:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50983b99-4f2a-3bd3-b116-db02e3e82c82 | -3.0688 | -45.944199 | 2024-10-14 00:39:04 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 107249d3-660d-3ca7-9c04-56d996331a9a | -3.3515 | -47.311699 | 2024-10-14 00:39:04 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6e76186-88e4-3ef9-995b-760c0164fbf1 | -3.6895 | -50.116402 | 2024-10-14 00:39:09 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4eccc77-8e36-3679-94e7-900d33b0820d | -2.3975 | -44.777401 | 2024-10-14 00:39:10 | METOP-C | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 056e5947-d0b7-345d-87c2-17861ab589d5 | -3.3372 | -49.149899 | 2024-10-14 00:39:11 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ccb6d20-bbcb-34f7-b063-dc326dc511b3 | -3.3292 | -49.159801 | 2024-10-14 00:39:11 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86473eee-5eb5-3b79-bc82-6f4b43851dd5 | -2.7483 | -46.7486 | 2024-10-14 00:39:12 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
