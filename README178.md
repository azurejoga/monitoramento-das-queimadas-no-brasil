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

## Dados Diários - Página 178

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b0a3a40-ef30-3aea-bc79-896df2db31d1 | -10.032 | -53.5065 | 2024-09-26 12:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 1710abe2-7b20-3767-8bb1-c36b1b2af10c | -10.8714 | -51.1561 | 2024-09-26 12:46:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5168979b-9e75-3f27-93c4-4dc6a533bdc4 | -10.8525 | -51.1581 | 2024-09-26 12:46:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 9eb3fec0-a42d-3d69-ae99-77f721552a97 | -11.1351 | -46.185 | 2024-09-26 12:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 284.0 |
| a9878533-23f8-3450-b234-ee9e8cf5540d | -11.1542 | -46.1824 | 2024-09-26 12:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 1371abdf-75f3-367d-9df5-37156f4743a4 | -11.1545 | -46.1597 | 2024-09-26 12:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 19e79ba6-1722-3aa4-938a-f8d7bad512ad | -11.1354 | -46.1623 | 2024-09-26 12:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 262.5 |
| f5d53a58-49a4-305d-bc58-905a291015b5 | -11.212 | -51.1627 | 2024-09-26 12:46:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 52638f65-3f91-3da3-8b9a-0518c340a86b | -11.2123 | -51.1415 | 2024-09-26 12:46:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| fd53ece3-5960-30c2-b2ae-3c42c2784616 | -11.7179 | -47.8551 | 2024-09-26 12:46:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 12e61203-0396-3a60-b8bf-ebb9cc472810 | -11.8613 | -49.6327 | 2024-09-26 12:46:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 3f638cf6-8098-3762-8273-04ca5f6175ba | -11.8419 | -49.6567 | 2024-09-26 12:46:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 9c07552a-f82b-3a62-b200-d8db24ef02c8 | -11.8422 | -49.635 | 2024-09-26 12:46:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 148332a4-15d0-3eb9-82d8-61997c1e2e2b | -11.8609 | -49.6544 | 2024-09-26 12:46:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e25909f3-975e-342d-a4b8-b8924bb34d05 | -11.9365 | -47.3367 | 2024-09-26 12:46:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 8ce33e95-36c9-35e5-acd6-4040cade3f73 | -12.2179 | -45.4844 | 2024-09-26 12:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 207.9 |
| 3ce87f05-1d03-34d1-9274-38331a1ccf52 | -12.2367 | -45.5045 | 2024-09-26 12:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 235.0 |
| ad4703a3-c021-3676-afb6-413128a5e73b | -12.5026 | -48.9198 | 2024-09-26 12:46:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| e92e5376-d6ec-348b-8cdc-63ab783ba68d | -12.5464 | -53.5147 | 2024-09-26 12:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 184.3 |
| 5748e191-bb68-391d-a0bd-a27a97c10e13 | -12.9714 | -45.2979 | 2024-09-26 12:46:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| c309d752-7209-32f0-a18e-5d574093f53b | -13.1607 | -45.4752 | 2024-09-26 12:46:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 5218a721-b9e7-3b81-b738-81797eaa8abf | -13.1796 | -45.4952 | 2024-09-26 12:46:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| efdc4a1d-8034-38a2-bf79-b30898a8af80 | -13.1963 | -45.6308 | 2024-09-26 12:46:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 757a720b-ea7f-38c9-88fc-df3f8f155c67 | -13.1603 | -45.4983 | 2024-09-26 12:46:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 9e68820f-1fc2-3cca-bed5-71f429616411 | -13.8053 | -48.0718 | 2024-09-26 12:46:24 | GOES-16 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 87944571-8ce9-3299-82ce-24790bcd1aed | -13.7859 | -48.0748 | 2024-09-26 12:46:24 | GOES-16 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 90859a45-ad20-3a9c-998b-3bd1204fafe9 | -13.8057 | -48.0495 | 2024-09-26 12:46:24 | GOES-16 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| e33d4c08-ed96-348d-97b0-931b1866a784 | -14.571 | -45.674 | 2024-09-26 12:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6bf865e0-a7db-37ae-beb2-70787e3c8fd2 | -14.5705 | -45.6973 | 2024-09-26 12:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 5461afab-93af-325d-ba94-774476901523 | -16.6067 | -54.086 | 2024-09-26 12:46:40 | GOES-16 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 139.9 |
| cf7208ef-2063-37e8-9cc6-5c2be518c8ea | -17.9929 | -44.4514 | 2024-09-26 12:46:46 | GOES-16 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 2ac88d6d-9a77-3c0c-97fc-f56f36e03cf2 | -18.9102 | -49.1674 | 2024-09-26 12:46:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 115.3 |
| ce21a018-1502-3ce0-8475-6214c05fde2c | -21.2733 | -51.0061 | 2024-09-26 12:47:04 | GOES-16 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 426.6 |
| 2122ae64-fbdf-3fe7-a7f7-b7c111715d11 | -21.9374 | -48.5688 | 2024-09-26 12:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 9ffdb0b7-e9a0-3a89-93c4-be8c31c171f8 | -21.9583 | -48.5638 | 2024-09-26 12:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 43e15238-92f5-38a7-89d4-2276b7b32a93 | -21.9381 | -48.5453 | 2024-09-26 12:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 5a664c6e-bf1f-3cf4-b8c5-78662f68670d | -22.2243 | -48.6625 | 2024-09-26 12:47:09 | GOES-16 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 307.4 |
| 3fb25518-6cc8-350c-9cc4-45478ffbbc89 | -5.8808 | -48.0908 | 2024-09-26 12:55:40 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 317bf4fe-14d3-393e-ad4d-c53e184427c2 | -6.8024 | -59.3044 | 2024-09-26 12:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| b0883d78-05f9-3477-8d23-f17e975a4081 | -6.7908 | -41.2254 | 2024-09-26 12:55:45 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 0f6d50ea-b7ab-31d1-8192-15a89a21483c | -7.2906 | -61.0869 | 2024-09-26 12:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ffa7fe91-62b8-38cb-8b9d-33abcb405b4e | -8.3155 | -54.9956 | 2024-09-26 12:55:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| a7111d21-1dfe-3f1a-989c-7abd36c2535d | -9.4165 | -51.4846 | 2024-09-26 12:56:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| bd9ff40e-290a-393a-bc60-001866eaccd2 | -9.4168 | -51.4636 | 2024-09-26 12:56:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 198.2 |
| 5749ce1d-019c-3636-b3e5-129c7509ce62 | -10.0134 | -53.4875 | 2024-09-26 12:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 2318937a-355a-35a4-b00c-250faf65649d | -10.2224 | -46.188 | 2024-09-26 12:56:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| bd4a136c-4839-326d-a966-63fe33329edc | -10.032 | -53.5065 | 2024-09-26 12:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 2ae8f5f9-dc5b-38c0-a304-2741a5ff7da7 | -10.2034 | -46.1904 | 2024-09-26 12:56:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 640eab35-e31b-3229-81dc-e3e071dbb6b4 | -10.6073 | -51.1196 | 2024-09-26 12:56:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 800eb336-30a2-393c-80be-4b2778d5aa90 | -10.8525 | -51.1581 | 2024-09-26 12:56:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| af1e9409-65bc-3b40-b116-bb129cbec4e1 | -11.1542 | -46.1824 | 2024-09-26 12:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| e9f9e573-0587-397f-a791-732899bdd605 | -11.1545 | -46.1597 | 2024-09-26 12:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| cf0c8e31-651e-3bf0-b820-6f1342acd330 | -11.1354 | -46.1623 | 2024-09-26 12:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 10840c63-a43a-36c9-ada5-148fa611aae5 | -11.2123 | -51.1415 | 2024-09-26 12:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 24e0bda8-81d1-3cac-b2b4-0efba21a7998 | -11.212 | -51.1627 | 2024-09-26 12:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 78c2dd93-0482-3b1d-bf98-0934737dc682 | -11.7179 | -47.8551 | 2024-09-26 12:56:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| d2ab5b81-9332-307f-8808-959ceb1f718d | -11.8613 | -49.6327 | 2024-09-26 12:56:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 672e99a2-bffe-38cc-82a9-5d13cd5b2f12 | -11.8422 | -49.635 | 2024-09-26 12:56:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 7a52de77-cb70-3655-b11d-262415f827e9 | -11.9365 | -47.3367 | 2024-09-26 12:56:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 658963be-798c-3b92-ba21-8693b378cec6 | -12.2367 | -45.5045 | 2024-09-26 12:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 4574343c-b723-3d92-96ef-c03619d645e5 | -12.5026 | -48.9198 | 2024-09-26 12:56:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| bdd79d5f-4a58-3850-b8ed-ed7d86ed9b34 | -12.7158 | -45.569 | 2024-09-26 12:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 5f64dea4-b9bf-3ef3-9970-a7d81125e66f | -12.5464 | -53.5147 | 2024-09-26 12:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 116.9 |
| c578f877-029d-3251-a67e-747d2d6a205f | -12.9516 | -45.3242 | 2024-09-26 12:56:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 430001ec-cb75-3a0c-be47-97ccd9cb68e4 | -12.9714 | -45.2979 | 2024-09-26 12:56:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 92618660-638b-34a0-b74c-882cad03e721 | -12.9318 | -45.3505 | 2024-09-26 12:56:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| a9346d3b-e47a-3a1c-af5d-1120fe42adeb | -12.9323 | -45.3273 | 2024-09-26 12:56:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 56de1638-cec4-3609-a2c1-590920212b36 | -13.1796 | -45.4952 | 2024-09-26 12:56:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 47a95f51-866e-3217-9a30-1348ae474eda | -13.1603 | -45.4983 | 2024-09-26 12:56:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 6e69972f-9329-3b58-ac29-825fac2ac0a9 | -13.1963 | -45.6308 | 2024-09-26 12:56:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 2507ae5d-bf1f-301b-8fa7-b060c2d816f9 | -14.6924 | -45.4665 | 2024-09-26 12:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 7ea475a7-1a7b-3474-9603-9bbe933ed238 | -14.571 | -45.674 | 2024-09-26 12:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 8f35a1b2-aa94-3063-93ab-391f41ab954a | -14.5705 | -45.6973 | 2024-09-26 12:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 3ef063d7-f35b-3ad3-8534-b8e4a97a468d | -15.6998 | -41.0835 | 2024-09-26 12:56:33 | GOES-16 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 128.7 |
| abf9707f-f52e-3d6b-8bee-fae7bb77a54a | -17.9929 | -44.4514 | 2024-09-26 12:56:46 | GOES-16 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 137.3 |
| b69efdea-9e16-342b-9b6f-94b2da112f86 | -18.9102 | -49.1674 | 2024-09-26 12:56:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.7 |
| 5d5132f8-1724-3aa4-9c7d-a4711f9a2960 | -21.2733 | -51.0061 | 2024-09-26 12:57:04 | GOES-16 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 479.9 |
| 3d849b9e-7c0f-31e3-8f18-2f1780418b28 | -21.9576 | -48.5873 | 2024-09-26 12:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 122.2 |
| cb345f9b-5dbf-3269-b56e-4d7c5948699c | -21.9374 | -48.5688 | 2024-09-26 12:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 257.7 |
| 5add6197-f869-3808-a712-fee15daa0533 | -21.9381 | -48.5453 | 2024-09-26 12:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 483ff03c-c642-3d8d-955d-2bd303895db2 | -21.9583 | -48.5638 | 2024-09-26 12:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 240.3 |
| 277cd73e-fa5f-3261-8b93-28098c64b78b | -22.2243 | -48.6625 | 2024-09-26 12:57:09 | GOES-16 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 365.5 |
| 09c8435d-84c8-32df-927c-9e2726a6c8b2 | -15.71 | -41.1 | 2024-09-26 13:03:53 | MSG-03 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a6a82fb8-cdce-33df-a2c3-c87ca74838c2 | -13.23 | -45.75 | 2024-09-26 13:04:09 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 674f88ce-49b8-3548-8cef-edf072aae765 | -12.83 | -51.15 | 2024-09-26 13:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 901005b9-9f09-31d8-b891-b8f955c2fb4e | -12.8 | -51.14 | 2024-09-26 13:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56ed0c03-6567-3e7a-8cb3-9f9883f27d21 | -10.83 | -45.9 | 2024-09-26 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3a69729e-9aa3-3d80-aee3-32a4e6c095bc | -10.83 | -46.0 | 2024-09-26 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| af8be5fb-1475-3c87-ba94-251f54fe9f4e | -10.8 | -45.94 | 2024-09-26 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb51a62c-8be1-3a42-a23b-6a25ebc5c001 | -10.8 | -45.99 | 2024-09-26 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 92fba8cf-8874-3523-9230-985c533a9af6 | -10.04 | -53.48 | 2024-09-26 13:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1eb2e87-f41b-3dae-9181-7c3def79bcfc | -10.01 | -53.48 | 2024-09-26 13:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10b671c0-d7bb-3212-bd92-bcb2c9f6ccee | -8.81 | -40.48 | 2024-09-26 13:04:35 | MSG-03 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| c35bdc87-ca52-36bd-bd6d-45645b2cf3a8 | -5.8808 | -48.0908 | 2024-09-26 13:05:40 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 01e397f4-4540-30c6-85dc-531d0dfe1465 | -6.8024 | -59.3044 | 2024-09-26 13:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| d7248c98-0d06-3410-b8ca-452c86e60dc3 | -6.7908 | -41.2254 | 2024-09-26 13:05:45 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| d861893f-a6ca-3b27-8593-b124e6f50348 | -7.2906 | -61.0869 | 2024-09-26 13:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 213857db-71e5-3af3-9c0f-e4cf54cd9aa2 | -7.3637 | -55.5134 | 2024-09-26 13:05:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 0c4fa862-3777-3430-9419-52eb3b1b0a88 | -8.073 | -42.8855 | 2024-09-26 13:05:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| f13230c2-f1cc-3996-850c-a4139e0cc6b3 | -8.3155 | -54.9956 | 2024-09-26 13:05:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |


[Clique aqui para ver as próximas entradas](README179.md)
