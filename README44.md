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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50cb1543-afd7-3f7f-af07-85e73dd1c89d | -2.15016 | -48.53828 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df0ccaf6-e047-3c73-a483-d202a05c2180 | -4.08747 | -40.87733 | 2024-11-17 04:29:00 | NOAA-20 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e282a6d2-32be-3efe-8eec-723f54edd409 | -0.83956 | -47.47331 | 2024-11-17 04:29:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67f7eb3e-4991-3add-ab1f-3e185adf2943 | -3.1555 | -46.61876 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94e32fbe-a4aa-3b6b-a794-b1dc5f9c8a25 | -5.63053 | -46.36372 | 2024-11-17 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28d41438-237c-3269-af84-eeaf7884a6ed | -2.53288 | -46.21338 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91e60aa5-fa31-3b78-874a-3b8e73b5fda2 | -2.93207 | -53.30499 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22ec8180-3eb2-33a3-bcab-ca3c0c729084 | -3.58238 | -50.52115 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cbee768-4275-3405-b7f2-5baf7f91f16e | -3.12902 | -45.90016 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4053ad93-55f8-3366-8c8b-27bd1851c645 | -0.85804 | -47.22741 | 2024-11-17 04:29:00 | NOAA-20 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3e89ed9-a233-35c9-af31-10116cb7c3d2 | -0.77849 | -49.47687 | 2024-11-17 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a3daaa1-de22-3890-a997-d813b876fb78 | -3.69948 | -51.07815 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 160832d4-84e4-3ebf-b263-0805ce30e299 | -3.55811 | -50.25676 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30ec7a93-5978-3979-af9b-435ff9bd20bd | -2.84263 | -42.8839 | 2024-11-17 04:29:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 34bd9af9-eb91-338a-ae1f-581f3a2beea5 | -3.81024 | -46.5152 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c89b3ff-89ed-3cf3-baf2-fa32de71048b | -3.10903 | -45.98376 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8e45044-1db1-3230-9244-2a3d18b3eeda | -1.14127 | -51.6965 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 08fc60c2-7cb5-3bb0-8fed-35f9099ac4ee | -4.32073 | -48.60439 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6545167f-8042-38d8-8c8e-0ab0755daa39 | -6.3871 | -45.68389 | 2024-11-17 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b5183de-67e4-3e11-96b5-48de4310a95a | -2.05945 | -46.54628 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9efe6c0-e939-33f4-904c-1bff23c6133b | -4.53812 | -45.25227 | 2024-11-17 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b8dc2c05-9f46-36e5-8702-c2c536c982d7 | -3.46035 | -49.98954 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9b077d4-ebf5-3ed5-97af-f6b69d838128 | -1.50395 | -45.88623 | 2024-11-17 04:29:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dede5752-35a3-3d57-8842-6498b0fee7d6 | -2.8609 | -46.72063 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 5e50ae77-c579-36ac-ae43-ea7fccf131cb | -4.17023 | -48.71558 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eed06e9-b2a2-3722-ba86-db054138691a | -2.66148 | -46.21581 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e93acf80-6a7d-32d5-acb4-6cba4c961c1c | -4.82206 | -47.32101 | 2024-11-17 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc591a0b-7acd-3121-857a-60eeb9284369 | -2.23894 | -48.68623 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1926721-e60c-3a55-a893-e99fab4f253b | -4.16204 | -43.91996 | 2024-11-17 04:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 621efb14-078e-3f52-85c3-69de1d688b4a | -0.78307 | -49.49414 | 2024-11-17 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a33097d-2815-38f8-84cb-c8cd9c30092d | -5.82723 | -46.47424 | 2024-11-17 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b86bac0-d69b-3d37-8f04-94b44f2638a8 | -2.62606 | -48.57068 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9d0be260-ccca-3978-a7c1-f719eb51c58d | -4.719 | -46.89452 | 2024-11-17 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1773074d-1965-3054-b045-1286cdc22b15 | -5.69411 | -46.56629 | 2024-11-17 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a47c056-1e03-3b48-b233-80d40302d000 | -4.63673 | -50.42191 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60492064-e765-3db7-8684-bb17d07a512e | -0.10604 | -51.60016 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e61c1e14-bd9f-3eb2-9e9f-2fa99f0eb566 | -3.12623 | -45.89611 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ead6d7d-e179-36ca-94d7-f79cace830ed | -2.08805 | -50.33577 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8acfebc7-5c70-341c-a03f-714ff45a897d | -2.90085 | -53.0545 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d460ec8-f875-39e5-90bd-40485e0284dd | -2.08123 | -48.5349 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce73565e-4d2f-3294-99ee-5a7a87fb9e4d | -1.5034 | -45.8897 | 2024-11-17 04:29:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78d8f0a8-d4b8-3d95-9bb1-03f057840f28 | -2.1757 | -48.39798 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92cc33a9-c654-3a40-bdd7-044252a7e626 | -3.03651 | -47.97789 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0cdbc04-3095-3bc9-a11c-69087503939e | -2.47852 | -48.58918 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8b0fb8f-de4a-313c-b331-47caa8c53840 | -7.65802 | -38.84285 | 2024-11-17 04:29:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ed8d9ef-004d-329b-aff4-14345888c941 | -4.55397 | -48.00983 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b88b5ea5-d1bb-3e0d-a0f9-ff29b6b13e22 | -2.64208 | -46.14481 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59d8188e-8fdd-37af-9b06-c32098a5b63e | -4.24939 | -48.535 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24dd7414-b657-3d9a-8303-37c71f4efb9b | -2.75032 | -46.08326 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2b368ae-f59b-32a1-a3b2-e8bd9d49be67 | -2.67579 | -46.18953 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| deab9fe0-f173-3fb9-8fa4-119410e622a5 | -3.12958 | -45.89663 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 543a89fe-fa16-3517-ae4a-54dc9c1f3664 | -3.12567 | -45.89964 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef056cf9-6a81-324b-9641-c05cd4c967f9 | -3.18779 | -46.5424 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 769695b4-cbe5-3a06-b158-8bbd8408ff83 | -3.24736 | -46.53039 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4a42586-ba5a-3d75-935d-66e85dbdba6a | -2.60746 | -46.25694 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 86124693-94d7-322b-a2aa-8fcd4253f922 | -2.13206 | -49.50293 | 2024-11-17 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93e1fe53-2a29-33ec-aa0c-64b20a17a628 | -3.32804 | -52.77212 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 59be1ebe-0c28-3bed-892c-ee70fe337630 | -3.89437 | -45.91607 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa5716b5-bccf-370f-ac7c-991ba5fdf112 | -2.12172 | -48.38951 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d237242-f769-3163-82d3-55fdfcba3044 | -2.22365 | -46.81837 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36d76d43-2003-332b-b239-7a0959bbb5ba | -1.36696 | -52.25626 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| beff4f7b-fd6c-385c-a4b7-d28f899640a9 | -2.11247 | -46.42413 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58aba808-7b41-318c-a487-32440e376a04 | -2.64162 | -46.55982 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8eebb07f-ce86-3364-91ff-0af0670c9d0b | -2.57475 | -47.56732 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b31db0fa-ed23-3daa-9b7f-96dc98439698 | -3.94352 | -46.70619 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6647256-4e84-3c81-b603-8d57f6fa0d9c | -2.16082 | -48.76047 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d16c9d1-dc0f-3b9a-bc15-6a51ef164ba3 | -3.02254 | -47.44319 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a664318a-e71a-316e-a902-a8ca119179cd | -3.73099 | -51.17318 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb2eebb2-b932-34d9-96c2-4fe6c5b5806c | -1.13804 | -51.68478 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73837fec-a6d2-3e4d-a8ca-77be10d540ec | -3.09509 | -45.96355 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a01c9eb8-f6ab-369d-b209-c6793f300795 | -3.25236 | -46.54179 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7c6fc85-49aa-3f3f-a984-990bbd75b682 | -2.73566 | -48.56582 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df95763d-b6e8-3c82-80df-6781afaa23d9 | -3.3452 | -53.31299 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 990a23a3-111c-31a0-adff-c61a238a35a2 | -2.60894 | -46.18245 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21f816c4-d389-3e3a-bff4-d70f1371e42f | -3.0354 | -47.98486 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15bcf1bb-e2f5-3e81-a799-3351af769d3c | -4.22844 | -50.67546 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d973e56-2743-30ec-bc47-b1c999f64a44 | -4.27793 | -48.20794 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9bef2d0f-ef8d-3ac7-9c60-0c73a0905c63 | -1.48267 | -55.34737 | 2024-11-17 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 09756f96-62dc-3132-9a03-c810eb826bed | -2.13941 | -46.4036 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9df8b2a4-7780-36d9-b8c4-5e91ff0a0284 | -2.68312 | -46.05496 | 2024-11-17 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 028ace9b-d9cf-34c1-bea2-b3440c397651 | -2.80163 | -52.99842 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd5fbc1b-65f2-353e-b5d0-dc1a24221cb8 | -2.21986 | -48.41201 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b53acf5-2fe5-3af4-92b4-8d3e9484c717 | -4.18022 | -46.82122 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23e1a3f5-455c-3f39-9812-3a2bd4fe6eba | -2.67077 | -46.17807 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06a59ff3-026f-3a7b-a2dd-8adcbc3d9e1f | -2.23517 | -46.83375 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aedefe29-7cc9-3708-92cb-6a83f3e37c44 | -2.67307 | -46.20692 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ccb44f1-536c-3efb-a7fb-50bbb19cb5cf | -4.28457 | -48.20899 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 59f3d7ca-cbed-3e14-ba02-64be35f26459 | -3.94629 | -46.71016 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6655db9-25ce-32d6-b5d7-bb86f9352020 | -3.78585 | -43.91037 | 2024-11-17 04:29:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 90b5a911-b265-34aa-a520-6f7bc897872d | -4.37656 | -48.56956 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65ea06e6-a3cb-3a4e-b688-0b17d8c525c6 | -0.31355 | -51.50148 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06778b75-bb37-30c6-8af3-68e111b1cbf2 | -4.03733 | -45.47464 | 2024-11-17 04:29:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc449068-d619-3309-a93d-5fb1da6d9447 | -3.0746 | -45.46726 | 2024-11-17 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8e444e7-0ea0-3a02-9014-b708c8ffac05 | -2.08537 | -50.47312 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 684c15b1-3418-3276-bb65-ea2e4cfd49d1 | -5.27068 | -47.19007 | 2024-11-17 04:29:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1817a8e1-decf-369d-a0a6-dad5d1b80a6a | -2.47846 | -45.40602 | 2024-11-17 04:29:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8c93c14-1b0c-3dbb-b34a-08c82c46897f | -3.85096 | -46.64595 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e9f513f-4a2d-3c7a-b639-d6fc9a347215 | -2.07792 | -46.47166 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 773d7ddb-4484-3b2b-a444-f9a9836c0057 | -2.36127 | -48.53401 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ac5c2d3-d521-3832-9caf-7eabae4668f0 | -3.52622 | -50.80331 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README45.md)
