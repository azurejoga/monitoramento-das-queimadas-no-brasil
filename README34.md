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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3a687f4-03f8-395c-9da3-b4b9242c5100 | -4.12873 | -45.59115 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ccfc9074-c754-327a-8cfe-f19796fc52b9 | -4.12741 | -45.5999 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 8a28bb92-4070-366f-bd0f-715dc39c6211 | -4.12676 | -45.60427 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3b4215d-ec57-3381-8d76-5bc7589d0ac5 | -4.12559 | -45.58176 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a157eec-115d-3459-af67-0732d38ee449 | -4.12494 | -45.58613 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 28043ff3-9473-3fce-9111-ae79c42ca844 | -4.12232 | -45.60357 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0748b1f-dfed-3897-b81f-8be12de86221 | -4.11984 | -45.58984 | 2024-10-23 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa9648d0-9606-3c08-ba6f-76ae09c74458 | -5.76242 | -45.56045 | 2024-10-23 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d7c9b55c-9c2f-3bc0-a85b-91b916fb2bf1 | -5.76174 | -45.56506 | 2024-10-23 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6da1d4e1-c9b0-329a-a37e-883e7aef8a9e | -5.70805 | -44.99774 | 2024-10-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1479a842-43a4-364a-af7a-44e90723a754 | -5.7073 | -45.00296 | 2024-10-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed789c77-25a5-3ec0-9f54-0b6980f88888 | -5.7033 | -44.99709 | 2024-10-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5984abc-8d82-367c-b199-8ecfa15e1148 | -5.6858 | -46.36469 | 2024-10-23 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8257389f-e097-3e6a-8397-8af49857b0ab | -5.63966 | -46.48052 | 2024-10-23 04:51:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9931a82-cb55-3c16-b75b-37862cf34510 | -5.43908 | -46.28693 | 2024-10-23 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4d53d87-23e6-3e84-a456-f0daf2ce07b3 | -5.36776 | -45.08095 | 2024-10-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f53b09b-b68d-38bd-b651-d87173a55569 | -5.36706 | -45.08577 | 2024-10-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12ad92c1-779e-3666-8da9-b3c33118ace6 | -5.36307 | -45.08028 | 2024-10-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03a5946b-d1bd-36c3-8208-3fb3f0a31d60 | -5.36237 | -45.08508 | 2024-10-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dabaa83b-cad9-3081-8194-12e9baabf286 | -5.27981 | -45.90341 | 2024-10-23 04:51:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36dbd46a-44fc-3eb1-a591-3cf0e85ab74b | -5.27653 | -46.17593 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3de87b68-0a48-3ca0-9e3c-4fe6f21a3242 | -5.27217 | -46.17537 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c47603f7-d6b2-390f-99e4-6fafbe1eb1ba | -5.26071 | -45.56365 | 2024-10-23 04:51:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49bd1907-46ca-38ea-ae7f-df86c82dde0d | -5.24446 | -45.86679 | 2024-10-23 04:51:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a791ee0c-be9a-3efe-8b97-c05e4f71e2cb | -5.23301 | -46.00704 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 439a0930-a063-3115-a6d7-b9fad7111601 | -5.22795 | -46.16269 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdbd14cf-f07e-3d42-af5c-a3bf1293d6a6 | -5.22424 | -46.1578 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c90d516-2015-38f1-a332-302367ac2657 | -5.22362 | -46.16197 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88b1a6ea-3266-3a25-b335-b7d21d1c79f3 | -5.16445 | -46.13238 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c8aa838-bedd-3119-b14f-30a24794daa4 | -5.1615 | -46.1311 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6dbbfb1a-6224-394d-a02c-a881a381cf81 | -5.16094 | -46.13504 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dea2cc47-9705-3115-848f-ca4cdb0e958f | -5.1601 | -46.13171 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3dda235-3fc5-3065-9c22-1e510f0d92ec | -5.14518 | -46.17195 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fba1f02-07fb-3a6a-b0ae-a771f32cb6a3 | -5.13344 | -46.1018 | 2024-10-23 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2abaaf4-99be-3a30-9d0a-584ef6b4712f | -5.11173 | -45.32732 | 2024-10-23 04:51:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c080d950-d0dd-3820-82c8-4351a870ba53 | -5.10702 | -45.757 | 2024-10-23 04:51:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79753fba-2428-3131-8b16-a7b765c65e65 | -6.25677 | -45.83904 | 2024-10-23 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 156aaf18-e6bb-3f40-9bff-41cff43c738e | -6.25226 | -45.83839 | 2024-10-23 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6557973a-e164-3ecc-a4cb-d0b39160aed7 | -6.09739 | -46.12883 | 2024-10-23 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 997b1b4f-bdc8-377e-a908-f8ab4201c80a | -7.61074 | -46.83646 | 2024-10-23 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4afa161b-ba6f-31b2-930e-08a961edf7ff | -7.42655 | -46.61506 | 2024-10-23 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 362bfd5b-6882-3b9d-827a-b1b24a4840a1 | -7.4222 | -46.61444 | 2024-10-23 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f809d4aa-ab79-346c-a1da-46f0021cc098 | -7.42159 | -46.6187 | 2024-10-23 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19a34f59-46ef-3b32-b16f-b1b339b9bf99 | -7.42098 | -46.62294 | 2024-10-23 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5191e016-4336-315e-8c51-7aaa76598030 | -7.40721 | -45.5706 | 2024-10-23 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5384418-8769-3876-8687-793239372ef7 | -7.37015 | -46.56509 | 2024-10-23 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48e351ec-ec92-36cf-94a0-48d765e1066f | -7.19994 | -45.41412 | 2024-10-23 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e62adab8-6e7f-34cb-8a11-5c0620b075b2 | -7.09785 | -45.31652 | 2024-10-23 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10e9613d-b84a-3135-81c7-6f3f2098989d | -7.09657 | -45.31559 | 2024-10-23 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 160da3ef-8a95-3b21-986a-111608cd664a | -7.04634 | -46.44187 | 2024-10-23 04:51:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b1bfc61-bc95-3349-ab53-053ab026769e | -6.99193 | -46.41584 | 2024-10-23 04:51:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1f43caa-d4a6-3ff4-8223-796d87e857b3 | -6.95293 | -45.96021 | 2024-10-23 04:51:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77ef97d6-1b93-3a54-b34d-9298fe46dd16 | -6.70246 | -46.07705 | 2024-10-23 04:51:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5251d826-0ede-3b14-bd58-048d3048fbcc | -8.94366 | -47.05434 | 2024-10-23 04:51:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdbde8aa-da22-31f6-ab6a-f06853d69850 | -8.47321 | -46.52395 | 2024-10-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e11dfd9-324c-3fb5-9b77-1ee20d94555a | -3.11851 | -46.65259 | 2024-10-23 04:51:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65d87a2a-d8b5-3507-b433-32fb93e723f2 | -3.5516 | -46.40565 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfc6043c-a363-3b5c-9cfd-15c3061c189f | -3.55103 | -46.40944 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a7758d6-036f-399e-8e18-1827b5d1fb32 | -3.5216 | -46.29119 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5b2dc72-17e3-34ca-8ec3-ccf65f7f12c0 | -2.96094 | -47.36387 | 2024-10-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1791cb3d-de88-36b4-a650-b13cf9401f77 | -2.77191 | -45.97759 | 2024-10-23 04:51:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42dc7334-1523-3650-8a60-fd786eeb3f85 | -2.76768 | -45.97694 | 2024-10-23 04:51:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fa58a3c-0aec-3017-81e4-5d7b0f9c5d03 | -2.57508 | -46.1356 | 2024-10-23 04:51:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe6fc482-6eb2-3770-b19a-8cd4f7e1e99f | -2.52174 | -47.34681 | 2024-10-23 04:51:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34c249b0-1fd3-3be5-be93-dc86a7a0c976 | -2.51714 | -47.35109 | 2024-10-23 04:51:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90d344ec-a5ee-3315-88d3-5e056c380eba | -4.1653 | -46.86781 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9344086f-468f-3683-9693-7936da110aed | -3.54686 | -46.40881 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7310a634-ff5d-308b-9865-614cf2a6936c | -3.31262 | -47.18938 | 2024-10-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 841fded5-9c57-3274-bdbb-a65204cdcc66 | -3.31185 | -47.19446 | 2024-10-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0bb56d43-a999-36b9-bce2-601071cce702 | -3.30868 | -47.18878 | 2024-10-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 51848086-32c3-3358-9e47-87c52874ba68 | -3.30791 | -47.19387 | 2024-10-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 588eb55d-e194-3902-aa99-88ebf7f2d2ed | -3.30528 | -47.02191 | 2024-10-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e10c01a5-df19-3afd-900c-51131f184a6d | -3.30425 | -47.02881 | 2024-10-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd01608e-0a8e-3eca-a655-bf46b5f0474f | -3.30374 | -47.03229 | 2024-10-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 320bb672-a42b-3df0-b6b9-760f86d783dd | -3.2847 | -46.07879 | 2024-10-23 04:51:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24f0a6b7-34af-35ad-9f2f-04d70c74ec85 | -3.2841 | -46.08276 | 2024-10-23 04:51:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c08fc160-09ee-3024-b2d2-b20a4244ef86 | -3.11795 | -46.6562 | 2024-10-23 04:51:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7018b9ce-bca5-37e3-be35-486f8931942b | -3.05886 | -47.38069 | 2024-10-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ffcdd1a-d9a8-3c79-993d-b77a96385deb | -2.95706 | -47.36325 | 2024-10-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e1bb24e-cc2f-3dae-bb8e-2584dba61a2c | -2.80935 | -46.62843 | 2024-10-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bb50878-bc8b-3262-b7a8-ab457214b896 | -2.60131 | -46.13182 | 2024-10-23 04:51:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 014472ee-e301-39ac-9793-b4e6a09e1856 | -2.57926 | -46.13627 | 2024-10-23 04:51:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88261e90-6873-375d-9800-2dcd3f61fbb7 | -2.57869 | -46.14009 | 2024-10-23 04:51:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02976c10-864e-37ac-a5b9-5a8208c57305 | -2.521 | -47.35168 | 2024-10-23 04:51:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 277b4d02-5f34-3e9e-897d-d2db2fb18b67 | -4.60685 | -47.52753 | 2024-10-23 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 01c5f57b-6e16-3723-b760-40e7c361f252 | -4.60608 | -47.5326 | 2024-10-23 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 911bd0ce-c370-34b5-8687-b83e9a825d38 | -4.59899 | -47.52634 | 2024-10-23 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a733b187-5813-3241-88d5-d7048375f236 | -4.3428 | -47.6013 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e0a1c3ee-c312-3b07-b47c-a8b28ae41e77 | -4.33965 | -47.59575 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 77560f5f-aef8-310b-887f-d6a4907baaa1 | -4.33889 | -47.60078 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e440ba8a-0a01-3a07-afc0-4c1fa4d4f217 | -4.33499 | -47.60022 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0018aee-e17f-3221-8a57-88a432ee534d | -4.33115 | -47.32767 | 2024-10-23 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 078695aa-2937-3468-a37c-e8080a5c0a2b | -4.18936 | -46.62594 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf68a861-dfff-30d1-818e-1c4185d12ddb | -4.18677 | -46.86369 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30ee417d-50d0-3995-b519-9763982e45d3 | -4.18674 | -46.86285 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43914d8b-63f1-33a0-961f-27f0ca4a75e4 | -4.1827 | -46.86306 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 958ff8c3-7b45-3c9f-ae4f-ec5c88942e37 | -4.18266 | -46.86221 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72037310-5afc-3934-b371-a82c070966e8 | -4.17178 | -46.79765 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c4b1872-2e3f-3ece-bcdd-9ed7836b9ca8 | -4.16936 | -46.86852 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 801bfa23-58d0-36db-b13c-4397b5ed9e16 | -4.16181 | -46.86333 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README35.md)
