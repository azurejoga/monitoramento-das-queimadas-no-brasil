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
| ee74237b-4b72-32ef-a0a3-1d0a42d8c582 | -6.8061 | -58.6663 | 2026-08-23 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 561e9fde-81a2-3823-97ae-ef92efd386c8 | -10.8361 | -50.9691 | 2026-08-23 03:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 61aa9566-b311-3dc2-9da1-876ae237dcf4 | -21.454 | -46.1371 | 2026-08-23 03:40:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| 1c5dec84-241e-3753-b6b0-d9db861d28ef | -9.4578 | -40.3392 | 2026-08-23 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.1 |
| ba4da5e4-3341-3d23-afee-552ff2feffd7 | -6.9699 | -59.0658 | 2026-08-23 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| d9982379-ce7c-33dc-9b2b-3fb365372d20 | -9.4582 | -40.3143 | 2026-08-23 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 171.7 |
| 72096d6c-ad2a-3cc3-9962-4cf891c68559 | -9.4391 | -40.3171 | 2026-08-23 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.7 |
| dc58f3f6-36e0-32cb-bd67-7ac0d7d32fa3 | -6.8027 | -62.9024 | 2026-08-23 03:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 7123593a-9b02-3ff9-8a1c-09fe5320855d | -6.8062 | -58.6469 | 2026-08-23 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 924bd189-dd9e-3497-a51f-8a46383651a2 | -16.0509 | -50.4363 | 2026-08-23 03:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a1efbed6-a9bc-3ec1-ba24-b5c683bc24de | -9.4582 | -40.3143 | 2026-08-23 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 277.8 |
| a176ca29-e54e-329c-a582-a77e346cf171 | -10.8358 | -50.9903 | 2026-08-23 03:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 84fb6d20-b747-3986-8a74-eff14eaaa4fc | -6.8027 | -62.9024 | 2026-08-23 03:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e9e26be1-b069-39b0-a97e-149bfe041dae | -9.4578 | -40.3392 | 2026-08-23 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 130.9 |
| 33dec821-c702-3e82-bea6-fbc54fb501ae | -9.4391 | -40.3171 | 2026-08-23 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 0783faf7-dbec-380e-981e-de470e8c30a1 | -6.1285 | -57.8393 | 2026-08-23 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| bbd95465-2906-348e-a013-2c3bceefd6df | -6.8188 | -59.6696 | 2026-08-23 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 03291437-00d9-3fb9-b10f-def51ede910f | -10.8361 | -50.9691 | 2026-08-23 03:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 26747373-11da-3fcd-b4cc-2d0e5a1e3e36 | -6.9699 | -59.0658 | 2026-08-23 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 1456b018-69d2-3e96-85f2-dba597c1c569 | -6.8062 | -58.6469 | 2026-08-23 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 1d86f22e-9b3f-3591-abe7-6cd6e62000f2 | -6.9514 | -59.0666 | 2026-08-23 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 48442919-4242-3d2e-8073-8268607c646a | -6.8062 | -58.6469 | 2026-08-23 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a039d22f-42ff-37cf-a9b8-0fab67ab27ab | -6.9513 | -59.0859 | 2026-08-23 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e0d05dc7-3e96-34b8-b370-933324ff81d2 | -6.658 | -58.75 | 2026-08-23 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 400a26b6-e1d3-358f-a99e-4adcb78dbec2 | -6.1285 | -57.8393 | 2026-08-23 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 0890732e-63fa-3fde-b506-4d8a40461469 | -6.1101 | -57.84 | 2026-08-23 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 48c74df3-5375-30e8-a7eb-0d869d130214 | -6.695 | -58.7291 | 2026-08-23 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| b5b551de-769a-3db8-b7c7-d162d5932e72 | -6.6765 | -58.7492 | 2026-08-23 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 146.0 |
| a3684e6c-10d0-39f4-9a48-8b8d7e408548 | -6.9699 | -59.0658 | 2026-08-23 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| ee436bd6-8226-3e1a-bdfe-d92c36016495 | -6.9514 | -59.0666 | 2026-08-23 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 81c0d21f-29fb-3226-92b2-e0e22816927a | -5.7799 | -57.58 | 2026-08-23 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| af837643-cebe-31b3-9f39-480dae63e5b9 | -6.1286 | -57.8198 | 2026-08-23 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| f5461b57-6235-3633-bfca-f1961a655107 | -6.6766 | -58.7299 | 2026-08-23 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 3eb81218-0e7d-3fb7-bc7a-785b49daf421 | -6.6949 | -58.7485 | 2026-08-23 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 50a5b2c7-d71c-3809-b4cc-5ba60139d9be | -6.8188 | -59.6696 | 2026-08-23 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0045855a-674b-3c27-bdb8-471acc2007df | -2.10724 | -47.0535 | 2026-08-23 04:06:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 749ef7da-4b7b-32a9-8233-f1886239ba60 | -1.32959 | -47.95906 | 2026-08-23 04:06:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a326bc9f-179f-3aae-aa2b-9f1227586db4 | -1.87047 | -47.98383 | 2026-08-23 04:06:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e38114ce-31af-3c04-a07c-2a51e8099af4 | -1.80369 | -47.19716 | 2026-08-23 04:06:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89b5c013-104e-3a7b-8b46-a989c2ef3e68 | 2.79112 | -50.94858 | 2026-08-23 04:06:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fd770ed0-e25f-3ad9-8c99-cfd7ff846771 | -1.33435 | -47.95982 | 2026-08-23 04:06:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e03eaec-5ef8-35b1-95f8-03531375ee72 | -6.89826 | -55.71112 | 2026-08-23 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b11f0412-9924-378e-a64e-437ab4d60faf | -5.1784 | -44.65641 | 2026-08-23 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be1ac67a-30b4-32c5-8e05-b0c40d537bef | -7.73573 | -46.1418 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f428c43f-3cd0-382a-8375-7563ad66d767 | -7.06475 | -44.98682 | 2026-08-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1db5dcc8-aa56-3c9c-9af0-08464614479f | -6.19363 | -53.52493 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c66f8465-447c-39a6-a305-220745eaab76 | -8.47057 | -46.98919 | 2026-08-23 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7f655c5-440d-3f8b-be6b-78442a624737 | -4.49407 | -42.88006 | 2026-08-23 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 240de55d-17f2-3adf-97a5-6eb98435f6f3 | -6.91692 | -44.96841 | 2026-08-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bba0f27-406b-37bc-bfa5-755497d816f7 | -6.50093 | -49.90348 | 2026-08-23 04:08:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 900f83c4-0617-3efd-9581-340e2f69b331 | -8.99192 | -50.76451 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1a8dde9-c468-3665-870d-e44724007372 | -6.78128 | -42.67633 | 2026-08-23 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f748acf4-d812-3b8f-9ce1-da1eb6505e08 | -9.7951 | -46.61143 | 2026-08-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 42c65839-d076-3c8c-abe8-30cf798e2e94 | -4.31392 | -46.42055 | 2026-08-23 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66e73ed2-7230-3166-8939-186abe9ecf89 | -6.86638 | -45.97882 | 2026-08-23 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05ee551e-0523-37a4-a82b-aaf8bb929cfd | -2.91294 | -48.87323 | 2026-08-23 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 35cf89b2-251d-3631-acb4-14e6fc51b6bf | -6.92025 | -46.41359 | 2026-08-23 04:08:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c610e333-b0c2-3980-bf5e-1894326bf082 | -8.51521 | -40.63852 | 2026-08-23 04:08:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a54b6ecd-54ed-3d72-b627-02ac44992806 | -8.37605 | -46.47532 | 2026-08-23 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e398422-ab5f-3587-bb6a-41242086189f | -10.34921 | -42.56679 | 2026-08-23 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8e4f2f85-8fa6-3d36-b10a-9ad405a77e3f | -6.72789 | -39.27396 | 2026-08-23 04:08:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c88347a-3b8e-3e0a-b3f7-542b5d2dd40d | -6.8971 | -55.69637 | 2026-08-23 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1a1ff7e6-72a5-3bac-9313-c00593b17889 | -6.52192 | -51.44954 | 2026-08-23 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6f1ae72-6a4c-3ff0-bd0d-bff766159b70 | -7.72808 | -46.14065 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eff7528b-c03e-3507-acf1-b4fd1657e978 | -2.91712 | -48.87043 | 2026-08-23 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9809294f-452e-3166-b0ef-4942a68c2e6f | -7.99182 | -45.23935 | 2026-08-23 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3985bc8-a5b7-364b-a9bd-f57c0ae4bb64 | -8.96693 | -50.76721 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11dbbe2e-709e-3795-93a8-b9dd2160badc | -3.70199 | -53.69071 | 2026-08-23 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ee8ad4a7-0f99-33c3-bf93-566502978d27 | -6.77456 | -43.08703 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34a2ca27-77d8-357f-8bb7-4531df7d058b | -6.55564 | -55.09768 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 464b1f55-0d5c-340b-a042-635e5a5de89d | -6.19457 | -53.51971 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e05c20b-e542-391f-8ede-0b88daf2440b | -9.44256 | -48.23497 | 2026-08-23 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7799700f-e134-3095-b8a8-81850327e24f | -5.01817 | -47.06713 | 2026-08-23 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 135115e8-fa6c-3c39-aa6d-0cd6a4b931db | -7.26838 | -49.90394 | 2026-08-23 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0de4a0ca-d32b-371c-9af3-e37967b0a003 | -8.97832 | -50.75303 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1495e992-0a83-326d-b488-bba890298870 | -8.81487 | -46.61964 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3cc3d7b4-53f7-3f32-ac8f-2da2de8348da | -7.16882 | -42.74502 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0747a392-7d7b-3c13-a47b-753e291c41b3 | -8.10293 | -50.05532 | 2026-08-23 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 70e3e1a1-1f8c-3c01-a816-48b40584aa06 | -5.91572 | -43.63306 | 2026-08-23 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f97bb1c8-abfb-3e66-a8b8-f9523cafccae | -9.79053 | -46.61532 | 2026-08-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e326e53-11af-34a6-9d17-345e1169c2de | -6.79796 | -42.67894 | 2026-08-23 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 04bc5db0-5dcb-3791-947d-bc4f5f8e587b | -5.05264 | -39.17678 | 2026-08-23 04:08:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8bcd1688-eb23-3a2d-b7b4-2f7d06336619 | -7.18993 | -42.7592 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b1ed69a6-5ee4-3bed-95ea-4d80ea1dbb03 | -7.19049 | -42.75568 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4c6d1b80-729a-3afd-b60b-c7c2fc059166 | -7.98751 | -45.24294 | 2026-08-23 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e531a697-db70-3720-8751-b4a8eadd1ce4 | -5.62117 | -45.703 | 2026-08-23 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30aa2bfa-d765-313e-b748-b1575f915346 | -9.01711 | -50.77003 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49209c57-fa08-3582-b298-01a1264050fd | -6.19171 | -44.85978 | 2026-08-23 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 692fb6ca-9af2-3673-8f01-8b96543a2ab8 | -4.74122 | -40.43284 | 2026-08-23 04:08:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 540c8c68-4c51-3769-8a3c-e0f5434e0ced | -10.46052 | -37.14249 | 2026-08-23 04:08:00 | NOAA-21 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7dce7c4b-c7dc-3714-bf85-22a2b67bcd79 | -4.17211 | -42.4458 | 2026-08-23 04:08:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e9444cec-98f3-39e8-8dc4-ee0930248a4d | -6.02455 | -43.01259 | 2026-08-23 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 60af9fd9-b081-3912-b22e-90eec4c6afda | -7.4692 | -45.12994 | 2026-08-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5820fb43-e61e-37f7-911a-d4a15a9d7013 | -5.77644 | -50.19182 | 2026-08-23 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb69c526-c427-3b3a-abba-abb9bf98a308 | -9.01258 | -50.76617 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0d1a2e19-9c41-32c8-b449-5b2e67098d37 | -7.29862 | -42.97623 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a8a8b057-7dd7-3e5b-a6aa-dbd902577291 | -9.4468 | -48.23576 | 2026-08-23 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| cb707268-2047-3478-97a8-9f94128b1c76 | -5.53229 | -46.60724 | 2026-08-23 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 079be4b7-d930-39ef-87f0-1fb3caaa39ba | -6.20089 | -53.52094 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c285b48a-fd2c-363c-b184-ee27a5af1be9 | -7.37179 | -55.6772 | 2026-08-23 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README11.md)
