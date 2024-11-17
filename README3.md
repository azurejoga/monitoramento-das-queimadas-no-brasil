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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de39719c-8051-39ad-a8fd-e9284db30b45 | -2.341 | -47.4715 | 2024-11-17 00:28:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b5f3935-1e75-3406-8b84-f7af8d840d1c | -2.0724 | -46.4772 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dff312d8-ecf8-3c3c-acfd-2e2d38c510cc | -1.5138 | -47.460999 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8771b284-f01e-3430-b0cf-13ee8a16a55c | -1.6979 | -46.238499 | 2024-11-17 00:28:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f2fb0e4-b090-33bc-927c-eaddfe6692b2 | -3.752 | -43.3764 | 2024-11-17 00:28:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 754b2504-ea51-3b9f-b40d-5f1193a5f0ac | -5.3345 | -45.002499 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf909887-e46d-3ba0-beb4-34c53a6f7278 | -5.4209 | -45.334702 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c84e16a8-9a7f-3c87-b5ae-ed522e79e692 | -2.8265 | -46.662998 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6a42ebe-9952-338a-a151-ece3fac7beec | -10.5405 | -44.6819 | 2024-11-17 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| abbab320-e456-3f7c-8c28-e855c06bf642 | -2.057 | -46.5453 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb45248-62bd-3243-9eff-a903caa12b27 | -4.4551 | -46.571201 | 2024-11-17 00:28:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30849eac-b6a4-34b5-823b-c84af7f7a51f | -1.128 | -51.677299 | 2024-11-17 00:28:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2401eb05-3d6f-38d6-a7d7-fb54dae36de2 | -3.6903 | -50.1124 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 443774a0-d34e-3a63-9d7b-a572c8c7788d | -2.0944 | -45.269299 | 2024-11-17 00:28:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 671dc374-c275-3647-b31a-8c291cf56f1e | -4.031 | -45.481201 | 2024-11-17 00:28:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e28e981-66b2-374c-8fd7-8b0cfb6e2887 | -29.866301 | -51.3605 | 2024-11-17 00:28:00 | METOP-C | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 9bc69864-d4f2-3e86-a089-7e3f9c9da5c7 | -3.1551 | -46.611599 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ace85cfe-6787-3048-a230-b26de2ee0dd7 | -3.9166 | -46.514999 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff809a56-ebab-3980-ac8a-471a803602a0 | -5.198 | -44.229599 | 2024-11-17 00:28:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa1b6ac9-4ec1-3b23-90c1-d6f73544065a | -1.9083 | -46.571201 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92f0b483-a780-339b-9bfc-9315ae24db4e | -2.6355 | -46.1437 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d9dc7ce-1c3c-348c-9994-ce9c18dfb007 | -2.8669 | -45.398201 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a85c1815-a62a-32d6-9bff-f66cd75fcf9f | -5.624 | -46.363098 | 2024-11-17 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8514a1f-6498-3b4a-ab8a-70ab06aa01ca | -1.7886 | -48.438301 | 2024-11-17 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ac69a91-935e-3c68-b26f-4020cca8ab53 | -0.1041 | -51.603199 | 2024-11-17 00:28:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9aeb03-873f-3433-9b1c-cb6c3720d887 | -8.4566 | -40.253502 | 2024-11-17 00:28:00 | METOP-C | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 22cd07bb-20c0-3b31-b028-79bd29a90cc1 | -2.5798 | -47.569599 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4ee712a-bf29-3093-9fdb-727109dabe9b | -4.5138 | -46.602299 | 2024-11-17 00:28:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3809c9d5-8329-34b4-a98d-d2f05e7e5521 | -2.5978 | -47.557999 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf7e9c3-d33f-3e6e-900d-ee067003b7dd | -15.3358 | -42.863098 | 2024-11-17 00:28:00 | METOP-C | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 122cb9f5-956d-37bd-83ab-dbfb659dbe6e | -1.9067 | -46.5644 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3acc6b5f-1a36-3764-8c00-d5287409fd9d | -3.1823 | -53.243301 | 2024-11-17 00:28:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 638b86ce-9b85-371d-8f2a-91646e755a65 | -0.9031 | -51.727001 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 662171b8-499b-35a4-811e-fc4e5733f505 | -3.0329 | -45.761799 | 2024-11-17 00:28:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9f63801f-c74d-342f-b3f9-0e04c1b9c38c | -4.8151 | -43.599899 | 2024-11-17 00:28:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22ee2c8e-b926-395b-9c2f-f6a271cb6b8f | -2.8365 | -45.491001 | 2024-11-17 00:28:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d28bed9c-b6eb-3fb3-9e8f-e4947c16a02f | -2.6578 | -46.196098 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 662f35f6-cfb5-3c90-b79b-ac4386ddaa0b | -3.0131 | -47.4356 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dee9355-78c2-3f57-9033-4111949b23cc | -2.6371 | -46.150501 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9f49e67b-ed90-357c-8892-d84b3e753464 | -3.2949 | -45.510101 | 2024-11-17 00:28:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 570cf26b-e592-3f92-97ad-0192d7980b64 | -3.7787 | -46.046501 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 87b32aa7-2657-36e4-aadf-5eee02e84260 | -2.2204 | -53.600498 | 2024-11-17 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34d415e7-0bfd-3a79-a18d-e365e1edf793 | -1.2856 | -51.737999 | 2024-11-17 00:28:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a30e3da-3310-3e38-8504-f4c5b2343b34 | -3.2052 | -46.469898 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f14bfab5-17c7-3c82-a7bd-79b561fc1271 | -2.5294 | -45.366199 | 2024-11-17 00:28:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0388f13-f2d3-3a2b-9d6c-0bad64f821a6 | -3.1129 | -45.077099 | 2024-11-17 00:28:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5f9117b5-3bef-3887-8091-8cbcc8e0cd01 | -3.0313 | -45.755001 | 2024-11-17 00:28:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ad2a8b9-e51e-3471-8ab1-a1b4e1721439 | -6.4695 | -47.5116 | 2024-11-17 00:28:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04ef14f4-b2b5-3338-95eb-bbc721c3e3cb | 0.6291 | -51.767101 | 2024-11-17 00:28:00 | METOP-C | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0095e642-8fbc-3a0e-88b0-8227131187de | -2.3492 | -47.4622 | 2024-11-17 00:28:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd577618-cdf7-3a9c-b30c-335b8c0148fe | -3.9068 | -46.5172 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d6747ee2-1c70-3a9a-a0b1-8dfce550d44b | -2.096 | -45.2761 | 2024-11-17 00:28:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0af30419-57e1-360d-bc9f-5c3599096878 | -3.5604 | -50.265099 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47800562-d646-3380-a83c-bd0a4333ac8f | -6.859 | -38.895401 | 2024-11-17 00:28:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 18a2c0fa-fbbb-3a43-b15d-513248edce68 | -2.835 | -45.4842 | 2024-11-17 00:28:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 406d3179-0dd3-348a-8f34-b698807b22bd | -1.8384 | -46.536499 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd7c0684-6713-39e0-9062-3bd7c092a0a9 | -6.0881 | -41.933899 | 2024-11-17 00:28:00 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1e7c9e7b-55c3-39cd-b62a-23684d7b22eb | -2.2406 | -46.851501 | 2024-11-17 00:28:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62731d22-18f0-37ff-bdd0-babfcd8499a8 | -3.6289 | -43.1572 | 2024-11-17 00:28:00 | METOP-C | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 979d992b-5334-3f22-a991-3c2b2df84653 | -7.5268 | -35.198101 | 2024-11-17 00:28:00 | METOP-C | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc31d6cb-ad0f-3a4b-96bb-101813bdf697 | -2.1391 | -46.498199 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11da130e-4b03-38dd-9daf-9a5c3b4f90d4 | -4.1363 | -44.189499 | 2024-11-17 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3deed66c-5482-35c9-b2ee-66f7bfd84a2e | -3.4448 | -49.1129 | 2024-11-17 00:28:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bf5035a-5356-3838-a3e7-1088456c3b33 | -4.8204 | -47.319 | 2024-11-17 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96741fb2-8cb7-35f9-be5d-f8f3c420ac65 | -6.9359 | -42.821098 | 2024-11-17 00:28:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 19da8f38-98a8-32e5-ad5f-7d32b1870afd | -3.1447 | -45.98 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e89f15a9-1165-37ef-a693-1a7f67ca929c | -2.5271 | -46.210899 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8856307a-3e5c-35f4-bd72-31877d7d3c07 | -2.322 | -45.182201 | 2024-11-17 00:28:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 569372d9-7455-39e5-ae79-c0f721a94c03 | -1.0172 | -52.271198 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 91a666c7-b56c-3704-ac13-b8c4e82e71f3 | -3.5758 | -50.517101 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff413f66-bb01-33f3-a861-6425c14fd0ff | -1.2542 | -47.0928 | 2024-11-17 00:28:00 | METOP-C | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2acd025d-7730-3d57-ae92-20a519c1776d | -3.0669 | -45.460899 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b514f26-e90d-3ba3-8b80-1a45131b45be | -5.4052 | -46.352699 | 2024-11-17 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e222bc1-a13c-35fa-a5e3-add47072d0b9 | -2.5912 | -47.5746 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b20520d3-864d-3121-a274-309c69e07825 | -2.6527 | -46.2187 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c36b559-0f58-39d7-aad4-ec2f11a5a5d3 | -0.9253 | -51.734001 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| db07c646-1ba2-3f0e-b83a-8d11a74e8b0d | -0.3151 | -48.709599 | 2024-11-17 00:28:00 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e24bb7e3-7a48-312b-9e4c-6ca14620666f | -2.6707 | -46.2075 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 317a35a0-cabd-33c7-bf50-a75ee9a3b346 | -4.5576 | -44.629398 | 2024-11-17 00:28:00 | METOP-C | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60a31bbc-1ec9-3bb1-850b-ffc38acf2ebc | -2.6505 | -46.840401 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44e45489-bdd3-31c9-a6e8-c0cec1c6d604 | -3.032 | -45.5331 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b081608-d626-3722-bc22-601817474a4a | -2.6013 | -51.794701 | 2024-11-17 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1fba71b-df3e-3afb-85b9-2ae09aaab47c | -0.9227 | -51.722698 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad94759-a795-306e-b267-4484848be50c | -1.3244 | -51.863098 | 2024-11-17 00:28:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d840e43-47cb-39ff-b4ab-4b4009deb555 | -1.5154 | -47.468102 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc375cff-9d8c-398b-a7ee-a1c66e999e14 | -2.3866 | -47.9426 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0a3be67-b424-3494-aced-f2e16aed8c27 | -15.3343 | -42.855999 | 2024-11-17 00:28:00 | METOP-C | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 645bc9da-2932-3453-9415-17a22e4b2444 | -2.6774 | -46.1917 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c771215-54da-3c71-8e3f-e8eccb193c20 | -4.8199 | -42.91 | 2024-11-17 00:28:00 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 79449a6b-71bd-3c49-995c-7b1a4d4e630f | -9.8655 | -47.5355 | 2024-11-17 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31263ce4-ba85-33ae-a2bb-00235293df51 | -2.6902 | -49.278801 | 2024-11-17 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1234b12e-96d4-3345-95f9-49cfd9f6017a | -2.6651 | -46.8591 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dd58d09-0298-382f-a1cb-84f2fc611035 | -2.1923 | -49.533199 | 2024-11-17 00:28:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b36ee229-b9cd-3bcd-917e-9352f31d106c | -4.4413 | -42.923698 | 2024-11-17 00:28:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ee4163c-ff90-3fa0-a2ff-b16deb4dbcf6 | -2.6255 | -45.200802 | 2024-11-17 00:28:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4575cc7-8901-31fd-911a-83367a994c10 | -4.4009 | -45.520199 | 2024-11-17 00:28:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6af01b7a-defc-3111-832e-31adb81d51ca | -0.9452 | -52.404598 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3a946af9-73bd-3d10-96a2-005d960b609b | -2.6784 | -46.827 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 751ae714-56e3-3f43-890d-e02ad0ac0223 | -4.1811 | -46.8167 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a674aa0f-b0f7-315a-b400-cb49b6f6e1a5 | -8.4459 | -44.219799 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
