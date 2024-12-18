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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d005aba2-a018-3776-84d7-bad480675df9 | -4.61104 | -44.57722 | 2024-12-18 04:25:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14a98693-bcc7-3f8a-aec6-65f34e2060d7 | -4.01028 | -47.0409 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45f8e270-0b36-33ea-b93b-ad5ab869bbda | -2.73225 | -46.20267 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2811345-9a5e-30d9-8e8a-a36bd6489484 | -3.33221 | -46.82906 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7695a0e4-c93b-30e0-ba63-8d2beda842d2 | -1.5238 | -46.05262 | 2024-12-18 04:25:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8196cf2-2ffd-3a94-9f60-cf48054272fd | -3.06813 | -40.04318 | 2024-12-18 04:25:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f7c5ad59-3596-3603-b807-ab9a9f73bff6 | -4.11257 | -48.1242 | 2024-12-18 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e6c4354-a83d-3605-bbc4-076b34736e2a | -4.26088 | -48.56741 | 2024-12-18 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 468360eb-1b98-3b41-becf-b0399580adfe | -6.1477 | -42.66883 | 2024-12-18 04:25:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d0cd34b2-eae8-3df2-948e-19927e1306b7 | -3.48804 | -44.9049 | 2024-12-18 04:25:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf3d7609-6800-3e6d-9bbb-cf96e2c6eaa8 | -3.92349 | -46.92864 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9cd47f8-30e8-3cf4-a935-df70e8b2e04e | -4.88246 | -41.40233 | 2024-12-18 04:25:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a95e7519-7e7f-331a-9d66-600398f32b70 | -3.84414 | -44.88073 | 2024-12-18 04:25:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0d8fb50-7c2e-3b67-9886-bbb60609d35b | -4.41121 | -43.56923 | 2024-12-18 04:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 949d4311-bbe1-3993-9bb1-1646c0d9f71b | -5.13212 | -46.15358 | 2024-12-18 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d88e5435-2688-31b9-9ebf-11fe5d417b92 | -3.15826 | -45.96745 | 2024-12-18 04:25:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 382add49-1586-33c8-81e4-c5ffeac1156a | -3.02414 | -45.23133 | 2024-12-18 04:25:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6d824c6-9c34-333e-9e0a-ccc513b6f3b9 | -5.97374 | -42.31356 | 2024-12-18 04:25:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a66c45b6-de36-3c94-9ae3-5cadd284141a | -3.24402 | -46.8775 | 2024-12-18 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 643bac4f-7d06-36e5-bead-f56e207baaae | -3.90908 | -46.67326 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67c9a5c3-dbaf-32f3-b1d9-ea92fe0bd595 | -1.37606 | -46.91665 | 2024-12-18 04:25:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99c70395-760f-330a-8d98-401efdb321fb | -3.16605 | -45.98284 | 2024-12-18 04:25:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04eb132d-cd09-37d4-9243-37e0306a3e9c | -4.446 | -38.06287 | 2024-12-18 04:25:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5c051cfb-31b4-3180-8192-8b49520710d4 | -4.9224 | -41.32577 | 2024-12-18 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e1c6e9ed-ce66-3fb1-8f18-d652d3b93755 | -3.95572 | -47.05802 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b12fa31-e3dd-33fa-b993-7c3344a8b8e7 | -2.92703 | -45.24822 | 2024-12-18 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ce4dc1e-35f5-351b-a7e9-7279e1d142da | -5.68227 | -46.50293 | 2024-12-18 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 720781c0-276b-3918-86d6-45436ccd8a51 | -4.01039 | -46.93166 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48fac484-e7e8-32da-8bae-376dfeca7eb9 | -1.79326 | -47.0595 | 2024-12-18 04:25:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3be745c3-7faf-3fdb-9312-3c6052313e0e | -4.52543 | -44.0494 | 2024-12-18 04:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92c55d6a-ca58-3e92-97f5-1a5e4cfcda73 | -4.54247 | -43.29769 | 2024-12-18 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 69e7e2df-6912-350c-90c0-44c81a6e57c1 | -5.99913 | -44.62865 | 2024-12-18 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a400d82-d66e-39cd-ae73-53570dcf595e | -2.66291 | -45.31286 | 2024-12-18 04:25:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07522d9f-cae3-3600-8f0b-f4d8826f89e3 | -6.49377 | -47.89232 | 2024-12-18 04:25:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f7efbf7-a042-3b9d-aa5b-2075c9e96477 | -3.23728 | -46.87644 | 2024-12-18 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3d7efa9-15a8-39e7-81cf-2d149a139569 | -2.5356 | -45.54042 | 2024-12-18 04:25:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a361f2a6-8d01-3652-8954-4bf5cf111a44 | -7.19847 | -44.92575 | 2024-12-18 04:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80d5aab9-687e-38fd-8361-f802caf519c5 | -2.92425 | -45.24424 | 2024-12-18 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9aa1118e-0214-3e34-bbf3-1ab3528c3a26 | -2.8009 | -46.71366 | 2024-12-18 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c46e8e7b-111e-3e89-99e2-ba1b0bbbc764 | -4.08688 | -46.62249 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c817eeb-d87e-335e-9855-798a94fbe9e1 | -3.24346 | -46.88105 | 2024-12-18 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 00578d4f-cefe-3653-b748-5eaa57216c5f | -1.6307 | -45.85174 | 2024-12-18 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cc28540-ea09-3352-9b13-f3b000521dd4 | -2.87275 | -45.24685 | 2024-12-18 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c414eb11-1dc3-3e93-8962-1163c1f85cb6 | -3.91781 | -47.00797 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fa397f0-fa46-3641-9b02-04c9bb3ee763 | -5.96044 | -42.55377 | 2024-12-18 04:25:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 55548a56-d456-36bb-9bc5-287f77764cf8 | -4.07774 | -47.10276 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4d7d3b7-cf00-37d5-ba9d-71725fc191d4 | -5.95704 | -43.37276 | 2024-12-18 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e441bdc7-832e-32d2-aa45-fff4c5f99225 | -1.90707 | -45.40678 | 2024-12-18 04:25:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35803234-647a-373b-a72a-3eaa79aae9db | -2.69703 | -46.59962 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40c6ec16-a935-3bf7-b6ba-138b9e790505 | -3.64779 | -53.46095 | 2024-12-18 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29570471-9ef4-38f9-b714-f5b81bd94f76 | -4.01365 | -47.04144 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85c3478f-e5de-3156-8e26-09ce508a389c | -4.98289 | -43.71254 | 2024-12-18 04:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eefb0b4c-4430-326c-bf20-49ff8b83ac73 | -1.7064 | -45.77833 | 2024-12-18 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9cef571-0c9f-3bb8-8f46-3e5f897d138d | -4.46182 | -44.64256 | 2024-12-18 04:25:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2ef952d-2a8a-3355-a614-637ab53eb277 | -5.94951 | -48.06212 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d02b6cb3-4ded-3d51-aea0-228f156c6d85 | -6.007 | -42.34425 | 2024-12-18 04:25:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 26748b7e-4cfa-3d59-a20d-5c0cf1ae24bd | -5.99164 | -43.48106 | 2024-12-18 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c142d358-f97b-3fd4-a766-8b89f0c50082 | -3.80094 | -46.71397 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 990c59c5-8fc7-38a0-a236-7371cf773e12 | -4.14768 | -43.56678 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2a94dc6-2109-3d1c-bbfd-a6735294b076 | -3.06754 | -40.047 | 2024-12-18 04:25:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b18d233e-36a6-34da-9491-ad67b75a44fa | -1.70253 | -45.78128 | 2024-12-18 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 193d2d77-2090-3016-8409-0e2c04c38ae5 | -3.80206 | -46.70693 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df5ea3fc-31b8-392e-8ffe-a56b4d7e26ea | -5.29462 | -44.942 | 2024-12-18 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c3a217e-4a71-3fb5-b29a-61336f423399 | -5.61126 | -42.82784 | 2024-12-18 04:25:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 28deb152-e9bc-3cc9-a6e1-3097e43a5e19 | -2.72947 | -46.19867 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64c2117f-9851-31ea-8bbf-224df65150cf | -5.94567 | -48.06983 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a1c226b-b408-3043-b0dc-790065c497c4 | -6.99034 | -43.55838 | 2024-12-18 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d1fedac4-78bc-377c-93e3-eabf342f4196 | -3.64932 | -53.46514 | 2024-12-18 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5060c199-918f-3327-b6df-eedab3a46ce4 | -5.94656 | -43.77361 | 2024-12-18 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca88d5c9-4ea6-3217-8619-9ba7ab35a2a5 | -4.03162 | -47.03701 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e9e3c45-78fd-3e55-bd07-e753860c17dc | -5.93941 | -48.06499 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92cc1336-4334-3d71-b8e8-f69ae3f0f24e | -4.07437 | -47.10222 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5751db2-637d-3751-b904-158a95b6f0d9 | -3.83053 | -46.67899 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f68c462-51ce-32e4-a25b-ada5985636e4 | -6.99332 | -43.56302 | 2024-12-18 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 338bfc52-ce5a-3b16-9a7d-03fd700f8efc | -4.04397 | -47.02437 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c03a66e6-9f5a-3926-a2d9-534742342e3f | -3.8734 | -47.02663 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 283f5ef1-32f1-3e9a-9482-2ef05f9683c5 | -5.92162 | -42.9393 | 2024-12-18 04:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b94dd0c5-60c4-30c7-9144-532cc0ea1fda | -4.17136 | -43.97408 | 2024-12-18 04:25:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ccd6ba3-1b2b-33c7-bc80-96a01d0f8030 | -4.03948 | -47.03094 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 933932cb-4293-3836-a817-36c45cea25af | -1.62404 | -45.8507 | 2024-12-18 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6a9d624-8ccc-30d4-b45c-850bcadf325c | -3.24617 | -42.41682 | 2024-12-18 04:25:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2a61605c-1642-3d35-a015-3b23056f78ba | -1.62683 | -45.85469 | 2024-12-18 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bea9f3f8-6955-35e4-87de-221d6f7b2b78 | -3.90851 | -46.67678 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d8c52bf-2205-3a73-a92f-7cce892055af | -4.18515 | -48.13961 | 2024-12-18 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc702ecf-9767-3e33-899d-1fe745736a30 | -4.06081 | -46.91777 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82650c16-4991-33c9-954a-fbd382905b45 | -5.95233 | -48.0664 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80a87e1d-bcd2-34df-9b12-73c3b55c63ae | -1.62737 | -45.85122 | 2024-12-18 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b413455-34f2-373e-b487-1fd328c3fbeb | -4.52435 | -45.86618 | 2024-12-18 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6b41a3b-6968-3c0c-9a59-611057847ab7 | -4.07494 | -47.09864 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 557d854e-e411-3b29-80d9-d1887f4fb362 | -4.38359 | -42.14794 | 2024-12-18 04:25:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 776dd79e-06fc-3127-ac43-7104d807c3c3 | -3.06695 | -40.0508 | 2024-12-18 04:25:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| babe699e-bd5c-38ae-978b-4775b6637ea3 | -4.03505 | -46.90649 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5c2f013-3fca-39df-adde-3337983200b7 | -5.94685 | -48.06237 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccd97b97-1638-38d0-8822-8e05894fd232 | -3.15771 | -45.97091 | 2024-12-18 04:25:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ac584ec-8405-33c8-b72d-c5b1661a5a8d | -4.54367 | -43.28975 | 2024-12-18 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daf90213-ed82-388c-9ec3-7bda2bb30d32 | -3.24796 | -46.87448 | 2024-12-18 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 507d632c-c7c1-39d3-9643-c8488e8f64af | -5.94803 | -48.05497 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b61c505b-9003-3576-aed0-7e64e8949c23 | -5.94224 | -48.06927 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 338718c5-8680-3ff5-8719-f36b621db410 | -5.70644 | -41.41132 | 2024-12-18 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a591eefb-aa9a-3652-97db-474dd08e3166 | -5.73085 | -39.53629 | 2024-12-18 04:25:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README14.md)
