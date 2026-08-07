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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb933757-a532-3764-b145-8bfbd9aa1229 | -16.6863 | -51.362701 | 2026-08-07 00:07:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 82e1247d-89cc-3742-8500-63650ac79bb6 | -22.6096 | -42.095402 | 2026-08-07 00:07:00 | METOP-B | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 98a8ae0b-cd4a-3a86-9739-2d1366157dec | -20.622499 | -43.9645 | 2026-08-07 00:07:00 | METOP-B | SÃO BRÁS DO SUAÇUÍ | MINAS GERAIS | Brasil | 3160900 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbeb6537-4fd3-3379-bd5e-790b366df410 | -8.4743 | -49.5644 | 2026-08-07 00:07:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 661824dc-1e3c-30ed-991d-992898f6686b | -13.833 | -53.700802 | 2026-08-07 00:07:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d68e715-6be3-3fc3-a48a-48c6129bd39f | -11.1259 | -54.885502 | 2026-08-07 00:07:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0c52df0-9997-33cc-a3ab-e52bd13d36d9 | -11.3177 | -45.199501 | 2026-08-07 00:07:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6072d8ff-aa32-383e-8562-9df4fee9f30b | -14.424 | -45.651001 | 2026-08-07 00:07:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37ef573a-93f6-3fad-851e-b89c10025753 | -12.0091 | -49.280201 | 2026-08-07 00:07:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a50661e2-b9f0-37ed-b870-a422df4e3fa9 | -12.8711 | -52.802299 | 2026-08-07 00:07:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7aa27f-80e1-3402-9716-c27554203321 | -4.2725 | -48.1898 | 2026-08-07 00:07:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8a953c-b70f-3fbb-ad43-63441ea915fc | -10.6351 | -47.487499 | 2026-08-07 00:07:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9814cacd-e61a-377e-babf-a8086a5fcd36 | -12.4154 | -50.504799 | 2026-08-07 00:07:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8468091f-75c6-3333-a8b7-8795d61ef2fe | -13.8304 | -53.6875 | 2026-08-07 00:07:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e19dde3f-57f1-3a72-a087-86c996e21dba | -9.1361 | -50.047699 | 2026-08-07 00:07:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fda9a828-59df-38c9-8cdb-36b92e3379d0 | -12.6142 | -46.898602 | 2026-08-07 00:07:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2112d30-0ab9-3ddd-9365-d61baaf7f299 | -6.4776 | -42.231499 | 2026-08-07 00:07:00 | METOP-B | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 06384749-80e2-3c9d-b05a-998a3f35de4a | -15.9279 | -43.983898 | 2026-08-07 00:07:00 | METOP-B | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6dee2acf-4dd5-3773-8a1c-462e05e5f81d | -15.9227 | -43.522099 | 2026-08-07 00:07:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e5c1aec5-732d-3b19-b113-681fd353d6e2 | -15.1178 | -53.5826 | 2026-08-07 00:07:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f171aba6-524f-37dc-bf71-050a5d510cef | -12.5618 | -46.940498 | 2026-08-07 00:07:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05e085ed-64a5-3f65-bb1d-8eea806f4fae | -11.4592 | -44.5686 | 2026-08-07 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8ebe913-b6cb-3ad5-a45e-504e3b59bf67 | -18.154301 | -47.978901 | 2026-08-07 00:07:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d2a500a6-9a2b-3f91-82ba-51be17b2b253 | -4.2709 | -48.1828 | 2026-08-07 00:07:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e364e016-8213-3233-8319-8316dfd0614c | -6.6416 | -56.388699 | 2026-08-07 00:07:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b73e34d-83bc-3b3a-9439-45966bb86fa7 | -4.8425 | -45.202099 | 2026-08-07 00:07:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3dfd796-e3c3-39f2-84b5-a34ce8df7765 | -9.6449 | -47.8013 | 2026-08-07 00:07:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c180d93e-6fcd-33bf-be33-9f59f171461e | -12.3479 | -48.1987 | 2026-08-07 00:07:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab9e3b8a-613d-3d1b-9071-2987696363af | -9.818 | -45.228401 | 2026-08-07 00:07:00 | METOP-B | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 641342de-c80a-336e-84a0-4d7c6ecf2e35 | -16.1752 | -47.887299 | 2026-08-07 00:07:00 | METOP-B | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cf1289e4-8122-3aa6-934d-4ce265f8cc24 | -11.1883 | -54.842701 | 2026-08-07 00:07:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23093743-335f-367e-aa9b-e6039260cb56 | -4.4563 | -47.9109 | 2026-08-07 00:07:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f972bf8b-a570-33bd-a5fb-64d34f292dc0 | -12.5552 | -46.956699 | 2026-08-07 00:07:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac6a886b-2c96-35ea-b127-6755f1347873 | -8.5429 | -49.549198 | 2026-08-07 00:07:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 513079c5-837e-36df-a9d9-a98b7469c94f | -13.7862 | -49.721298 | 2026-08-07 00:07:00 | METOP-B | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 72b8e139-23b3-3a6f-8de3-eba6cc1be05f | -16.399099 | -49.933102 | 2026-08-07 00:07:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2eb0be20-12f6-3389-863f-b06b160dc503 | -15.5327 | -49.9949 | 2026-08-07 00:07:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 71395a24-272a-3c52-b53c-46d236ff5136 | -6.8629 | -46.003399 | 2026-08-07 00:07:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f56ec54e-9973-3948-9fb4-99697f04662e | -4.2643 | -48.199001 | 2026-08-07 00:07:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de638087-4c50-33c6-bd41-ed2d118de8d8 | -11.1481 | -44.474998 | 2026-08-07 00:07:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 472d1fda-a833-3a72-9e15-ec7416c3478b | -16.694 | -51.350201 | 2026-08-07 00:07:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9bbc5009-e5f3-34ce-bc33-a8ff324c645f | -3.8333 | -49.159901 | 2026-08-07 00:07:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39b85958-585d-32c6-bae8-f39f3d4b92a9 | -11.469 | -44.566299 | 2026-08-07 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 11e9fca4-400c-33b6-bd26-4d67041fe708 | -21.501699 | -45.515598 | 2026-08-07 00:07:00 | METOP-B | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ca9fa790-a75f-3f9e-befc-852e6e43c6c7 | -2.691 | -47.3536 | 2026-08-07 00:07:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4de723a8-64ab-3f18-828d-efb7ff57c8e0 | -12.4171 | -50.5131 | 2026-08-07 00:07:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90136fbe-6f26-38bc-b663-86708fda3ff1 | -12.0075 | -49.2728 | 2026-08-07 00:07:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07a79c2c-1df9-3344-86c0-b6f416c49cf3 | -11.1756 | -54.8302 | 2026-08-07 00:07:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ed47b15-09a3-3b5b-9a4e-bdfe7e825c76 | -6.5371 | -46.960602 | 2026-08-07 00:07:00 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00577ea9-87f9-3144-b3ae-245058b06b1c | -22.611601 | -42.103901 | 2026-08-07 00:07:00 | METOP-B | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de5cbfc6-de70-3398-9798-300dd0e26b6f | -14.2774 | -45.280998 | 2026-08-07 00:07:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e63e85fb-8089-31ec-a3c5-e9b22e8fabc6 | -3.8431 | -49.1577 | 2026-08-07 00:07:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c804865-4bed-3a45-a9ea-f552d6ab511a | -5.5522 | -47.700901 | 2026-08-07 00:07:00 | METOP-B | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 352779b8-e5a1-3ff4-9976-3a1463ebfda8 | -11.1599 | -44.481098 | 2026-08-07 00:07:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cfb8b431-b6f2-361f-a7b6-51f272181ec3 | -12.593 | -46.896198 | 2026-08-07 00:07:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f567c6f-2fdc-3009-a6fb-c2df78a340d4 | -2.48 | -49.325001 | 2026-08-07 00:07:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d70ce931-c2cb-3ec5-b0f1-cd8f1aa7148d | -12.1454 | -48.259399 | 2026-08-07 00:07:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 391949fc-c3bb-36d2-909c-16168d03056c | -6.6449 | -56.4044 | 2026-08-07 00:07:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81a1bf68-1e66-31e2-b62f-48381b51a583 | -15.1152 | -53.568901 | 2026-08-07 00:07:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bb3b01ee-d130-30c8-9147-1e13e7dc2b8d | -2.4785 | -49.318199 | 2026-08-07 00:07:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96ce1f4c-7d26-3da0-aac7-7e0eec3354e9 | -5.1054 | -49.3652 | 2026-08-07 00:07:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bfdb597-8270-303f-b87d-26909a732178 | -12.5734 | -46.9007 | 2026-08-07 00:07:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9df34d3-d3a4-3d2f-a03a-abddd46369f7 | -2.885 | -48.069 | 2026-08-07 00:07:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb1f9e0d-70f5-3521-9bda-1d9860b78545 | -12.8733 | -52.813599 | 2026-08-07 00:07:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4e668f0-63e6-3d0e-8c78-2faf11aae892 | -13.8232 | -53.702801 | 2026-08-07 00:07:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a8f8729-aae4-366b-afe6-87879ab3b6b4 | -11.085 | -47.794498 | 2026-08-07 00:07:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97af0591-e122-3507-8469-587110e11770 | 2.5282 | -60.6031 | 2026-08-07 00:07:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c1d8a32b-4b2c-3a00-8149-d5165206f394 | -6.9118 | -41.941101 | 2026-08-07 00:07:00 | METOP-B | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d07d40a7-92c8-34d3-b121-b55b0d3be7de | -16.173599 | -47.880001 | 2026-08-07 00:07:00 | METOP-B | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 29f2998e-4420-3964-8db8-406235a403bb | -16.471001 | -43.437099 | 2026-08-07 00:07:00 | METOP-B | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| acfb3d1f-a9c5-391c-b396-0aa3c038516c | -16.4009 | -49.941799 | 2026-08-07 00:07:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f79042f7-2ca2-3286-8be6-6e286797cc34 | -18.477301 | -47.226002 | 2026-08-07 00:07:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e019a1c1-49db-360f-90e5-76b223cec6bc | -14.2676 | -45.283298 | 2026-08-07 00:07:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 399e01e2-08a9-304c-9014-dbbb27194d8a | -7.0909 | -46.544102 | 2026-08-07 00:07:00 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b9de153-95f0-34a7-aba6-e2bf2c9133b9 | -10.6335 | -47.480598 | 2026-08-07 00:07:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1817075-867e-3719-8ede-538783ccf0e8 | -7.7163 | -46.216099 | 2026-08-07 00:07:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8078b83-d5c7-3fac-931a-c0c58e487a90 | -6.9885 | -42.902199 | 2026-08-07 00:07:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7f2df2f9-6d81-35cb-816d-94af67aa7436 | -6.5386 | -55.138 | 2026-08-07 00:07:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c26d84e-cb90-32a4-9ab2-11dac727e8f4 | -11.1727 | -54.8158 | 2026-08-07 00:07:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| daf6db98-89ad-3638-9a06-937d3de2a971 | -14.4274 | -45.6656 | 2026-08-07 00:07:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2820fb09-519d-3274-88ad-4bc02b028d16 | -6.4274 | -47.246201 | 2026-08-07 00:07:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad5d9071-2f47-31c9-83e5-edb5b2a5f4be | -6.7074 | -58.929199 | 2026-08-07 00:07:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d474bbb-b930-3a3a-b8cb-21cf201d6b46 | -14.2693 | -45.290798 | 2026-08-07 00:07:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 041bf59c-bbba-36e2-85fe-cf3866e023cd | -14.4257 | -45.658298 | 2026-08-07 00:07:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bd11f1f1-323c-3477-aeb1-2ec0d61dc657 | -11.4681 | -44.5558 | 2026-08-07 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 153e0f80-3b26-329c-b818-88e43ac4e56f | -11.1443 | -44.4865 | 2026-08-07 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 6fdc79b5-746c-3e3f-882d-4ca9efbe678c | -15.1169 | -53.5898 | 2026-08-07 00:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| a4c77688-76e3-3a5c-a103-52dcc399049e | -15.5327 | -49.9927 | 2026-08-07 00:10:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 60c188b9-009e-3911-8e9c-a65a69994ae2 | -22.6082 | -42.119 | 2026-08-07 00:10:00 | GOES-19 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 88.1 |
| 394954c0-2894-32be-b583-db0f9d028fd0 | -16.6984 | -51.3576 | 2026-08-07 00:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 86d66969-54c8-3695-b35f-82eb5de854e8 | -15.5132 | -49.9958 | 2026-08-07 00:10:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| b6f812d4-1e57-3577-813e-83277c2ab456 | -16.3941 | -49.9412 | 2026-08-07 00:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 042e3e1a-3da2-3a82-a6ba-376eb6851687 | -11.1635 | -44.4838 | 2026-08-07 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 19831a45-f108-341a-8257-92e6d0fbd556 | -15.5323 | -50.0147 | 2026-08-07 00:10:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6f186504-8cb2-3694-ac84-bc61f03905ce | -16.6984 | -51.3576 | 2026-08-07 00:20:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 988fadcf-26f1-3ae0-a1f6-fdde3aca6abd | -7.09 | -46.5526 | 2026-08-07 00:20:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 06b963c7-7bbc-34b9-83cc-72283aabcd09 | -11.1835 | -54.8584 | 2026-08-07 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 3194f0c1-2639-31e8-af75-83e34d611282 | -13.8236 | -53.7264 | 2026-08-07 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 8fa55a78-7ad6-38d0-87b1-65ad6fe06ae4 | -11.4677 | -44.5791 | 2026-08-07 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 3367a670-e392-39d6-b4c1-c50007dd89c5 | -13.8239 | -53.7055 | 2026-08-07 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |


[Clique aqui para ver as próximas entradas](README3.md)
