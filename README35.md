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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f402639-aed5-33d6-9991-0ee023716181 | -11.25016 | -51.35215 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2c32a112-6f3f-3f90-b54c-f12813658a85 | -12.32847 | -42.53368 | 2026-09-24 04:10:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f9602b07-54d4-3f28-ab6c-57e8f7f78ecc | -15.23412 | -43.26812 | 2026-09-24 04:10:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f6e8bf6-16d8-3a2c-a3f8-f9baa0a37949 | -11.10914 | -48.29752 | 2026-09-24 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e1c160b8-81a1-3ab8-89dc-f17f00846da5 | -11.12913 | -48.30468 | 2026-09-24 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a7d7ca6-eec6-3e32-9e17-352fc277485d | -12.4138 | -46.96145 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 72efcade-cfa2-3188-892d-b77085979648 | -11.48474 | -47.35212 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 042922ec-8bae-3223-8a10-10be2ccdb10f | -12.9268 | -50.91636 | 2026-09-24 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ccfcf26-9003-3663-bb21-a07284375832 | -11.23276 | -51.38918 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9dcbad0c-0c36-377b-a68c-66d7a195fd43 | -11.24568 | -51.37608 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f1a23c8-b114-304d-8902-7ceabdb5d371 | -11.24344 | -51.36018 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f60a2718-3050-3fbf-935a-796ca6332d1d | -13.54331 | -42.54641 | 2026-09-24 04:10:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 686d676d-450b-3f28-8e0e-64f3ef961484 | -16.61504 | -46.1999 | 2026-09-24 04:10:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc36183b-7834-365e-a05a-6ec92ff3374f | -10.09234 | -46.06351 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f60bf045-e7b8-3c63-b1b5-5be1080b954b | -11.92262 | -50.73668 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e1ebcf0f-1676-3468-93c7-87b770befdf8 | -11.39571 | -47.36038 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e97f202-9716-3ba2-97e7-e5ba172b1b2a | -12.11609 | -47.38807 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22717a4a-a107-3c17-8af8-655656682c67 | -11.2552 | -51.3531 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8d5fe33-5e77-396e-b808-63c86e219011 | -11.20643 | -54.12839 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 351f4a7b-4706-3a64-8c3a-628d4f3ad19b | -13.07455 | -47.40191 | 2026-09-24 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dc45f03-0590-3e3f-8e61-dd2578e7c813 | -10.08196 | -46.01374 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| f57246e8-6ded-303c-996e-21ef3921266f | -11.79137 | -50.99581 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e71bca2-f1e6-35fd-aa70-5790e14516b7 | -10.20599 | -44.16516 | 2026-09-24 04:10:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7293282-24aa-3163-ab23-23f91490cc03 | -12.10423 | -51.86065 | 2026-09-24 04:10:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63284c22-5b3f-319e-a647-6a81c13b8b5c | -13.70025 | -48.78672 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73933aaf-6b4c-325d-9c0e-5b542c334b34 | -11.94365 | -38.29731 | 2026-09-24 04:10:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1168a14a-caf6-364f-a781-898aae5a9ebd | -13.46388 | -46.26219 | 2026-09-24 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e878cdf-f378-337d-9004-71ccccf3ca11 | -11.35437 | -43.3694 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e0e1443-1cd6-3991-aef5-a1b2c95d9d3f | -12.3186 | -50.20262 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b25b81f8-574c-3f26-afdc-488003e6ea33 | -11.42485 | -47.39956 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7b3631b-33ed-39f3-accf-b05625057567 | -11.79035 | -51.00136 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8636377d-3f5c-3a55-8d0b-470f197893a0 | -13.38799 | -41.32285 | 2026-09-24 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3b98361f-ae16-33b8-92b4-15547f5c6d39 | -10.43513 | -46.26104 | 2026-09-24 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c37d5318-0ef7-3946-9626-3e6a334aaf09 | -12.41907 | -46.95294 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b330847f-a99d-316d-aa1b-f7cd8eb83e62 | -11.4795 | -47.33607 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6809cdf-9f32-3108-9750-5337c7c68089 | -11.69587 | -43.44681 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 200fb8b0-c872-39e0-be76-e26ddc7895e0 | -10.71626 | -48.7392 | 2026-09-24 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41f69548-259d-32ae-ba45-a42e535852fa | -11.43153 | -44.18925 | 2026-09-24 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83c2b7ae-b1e0-358f-8ad5-1e63f13d362a | -12.41753 | -46.9621 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d4975707-56cf-3933-bf51-03ef39cb693f | -11.40155 | -47.39572 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 84bcc51a-db7a-3072-9d48-bef3d82d30ca | -11.69531 | -43.45033 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7259eb80-e04c-31e8-a5f9-f4afdee803e2 | -11.22661 | -51.36631 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 31e0270d-c61b-3a75-a166-2e0b467233db | -15.2446 | -43.26616 | 2026-09-24 04:10:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b833d838-7bdc-35ce-9717-d42db953efe2 | -10.93987 | -43.85777 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 087aab22-43e5-3445-9506-baca983cebdb | -12.13785 | -45.63178 | 2026-09-24 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10c2e5ae-16cf-3210-a82f-0b582cb463db | -9.86176 | -48.5067 | 2026-09-24 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9b061c60-3ba2-376d-aa2f-394becdec4bc | -13.92226 | -46.90507 | 2026-09-24 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5114b625-efc8-30c9-96f8-3268888f5789 | -8.59399 | -54.62425 | 2026-09-24 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ae4290f1-8a34-3d0a-a72e-34887ef55274 | -14.75077 | -45.63082 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a450150b-0ba7-3e60-b19a-7155beeb07ef | -12.10997 | -50.73883 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcc7e767-f856-378f-88b6-e817ed583e2e | -10.93654 | -43.85722 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e0fe773-2a48-3e3d-83dd-64cc65f94632 | -10.07831 | -46.01318 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8e9c473d-c063-34a1-8696-1338ecce52c5 | -10.14577 | -50.2207 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e795ea77-51f4-363f-9246-6479938d16e1 | -8.58749 | -54.6231 | 2026-09-24 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 519f270f-6463-3c5b-8304-168c51e8d987 | -10.42139 | -49.37333 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 073993d6-15c6-394c-bfd5-2ae349fdbe74 | -11.68298 | -50.188 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6ddc11a-375b-3ac5-9fb7-75190e5985f6 | -14.63604 | -50.59731 | 2026-09-24 04:10:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4aa02e1f-bb0d-383b-a9f3-c65d9e856b23 | -10.93996 | -43.83578 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b9df68bd-daf1-3628-92a2-36597383275f | -15.24129 | -43.26562 | 2026-09-24 04:10:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2fa1c662-f927-3102-91c1-4b3d97eda9f7 | -10.41486 | -49.35815 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9464f5fb-76ff-3908-b22f-f70eba74c449 | -12.13719 | -45.63577 | 2026-09-24 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f12d5cb-738f-3e9a-9e18-54e57690fe82 | -13.7849 | -54.05254 | 2026-09-24 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60c920be-ecfd-38be-b642-09426620f9e0 | -10.08004 | -46.02523 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 647db703-d20b-3a85-9877-b53c73f07ba9 | -12.91826 | -50.90928 | 2026-09-24 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6053d28-670a-3264-b6ea-57b4480cc4c8 | -10.45844 | -44.94999 | 2026-09-24 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 095f31fd-260b-3802-9afd-31befede6aff | -11.69615 | -43.4685 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b94c51e-2a1e-3791-9592-37d0008d80ab | -12.11253 | -45.61109 | 2026-09-24 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4b97fb17-b8b0-3886-8e33-005017eb426e | -10.10589 | -50.19411 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 5ade223b-7f1e-3587-9457-a96604dcd261 | -11.69727 | -43.46146 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60c31d7d-5aaf-3c8c-b2b6-19ce318a4c3b | -14.74558 | -45.59859 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3bcb60ea-b245-353d-b7bb-79778c8646c2 | -11.23166 | -51.36725 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d0d8849-d688-3041-9b84-a92f17260452 | -9.84537 | -48.49974 | 2026-09-24 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0783dce-eba4-38ec-9d07-509c6d65f29d | -10.28187 | -49.9628 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 421771d3-ed76-3674-b36d-2db6a0ddecdf | -11.4986 | -42.33693 | 2026-09-24 04:10:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 158db520-f96f-3d84-9e65-170af9c89744 | -11.48393 | -47.35694 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 504b3a82-9a4b-30a3-b1e4-0bf049486bcf | -14.96492 | -47.52962 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ae27e7d-f2d0-356c-886e-0bbbad55ccb1 | -14.7243 | -45.5994 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a2ea389-2ae4-3b85-b7dd-86a6f883044f | -12.1052 | -50.73793 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 636c187b-3174-38c4-97a8-fad8dcda9e55 | -11.26018 | -40.93002 | 2026-09-24 04:10:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 88d482a5-ce07-39a5-89c7-c35c87ab9e57 | -11.12499 | -48.30405 | 2026-09-24 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9ce11589-f93b-347f-acf0-9e73aa049e35 | -11.20037 | -54.12745 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54929a6c-7767-377f-803c-38eab6b074a2 | -10.08369 | -46.02584 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5cee424-81a5-3554-9f61-d4709420ed94 | -11.39419 | -47.36919 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f57ea45-ebdc-3c2b-baaf-e1aaf243def0 | -15.16972 | -43.55338 | 2026-09-24 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ff3b5c0-dfc6-37f6-af37-d51cf32cf787 | -10.08363 | -46.00404 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3e08ce2d-fbc3-3ebc-b3cd-71c5f43b1339 | -10.27999 | -49.9601 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e986f986-0561-3750-86cc-5d441f9533d7 | -12.12903 | -50.74241 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 1912e74c-8929-3d53-8125-9bdaabac4b91 | -14.56706 | -54.12308 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b1daaa0-4213-3679-9009-7b0f3f465016 | -10.91177 | -53.9505 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 203197e6-969f-31d7-8a9c-d1f29c981955 | -10.27719 | -49.96195 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f745db78-6909-396a-a225-7b4a6a6e6233 | -11.23335 | -51.35828 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e6b8c8f-0b63-3444-88e2-2512a2bc6c6f | -11.40271 | -47.366 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4e33cbf-5531-3bf8-a668-b530e0a2a6ef | -11.23726 | -51.39311 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9552c10a-c259-3b41-9dfb-4e140f39f3aa | -11.22605 | -51.3693 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6a186503-9c2f-3bb1-8e55-0a190bd92966 | -11.65442 | -43.49428 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 38e88459-83e0-3839-a7c1-8787aef9937f | -10.84617 | -43.24686 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 36019ebd-f7b0-3842-95cd-50d11146432f | -9.85818 | -48.50194 | 2026-09-24 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9748df4c-3317-3ba7-8d01-bcf3c98cd1e5 | -11.48721 | -47.33748 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17597b37-5615-3f02-919d-8035783a06c6 | -11.65167 | -43.49022 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 52a06116-53b5-3dbe-b390-eeb073fe97b4 | -10.08803 | -46.00021 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README36.md)
