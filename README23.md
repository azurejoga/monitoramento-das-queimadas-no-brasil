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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c4cdc13-5f62-3735-bfe4-1ccbdc793874 | -2.43604 | -48.04697 | 2025-11-15 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f8daa22-69db-340f-bc87-7e30103eb3f7 | -6.55227 | -44.46497 | 2025-11-15 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb9a7685-3030-36f9-a484-ab932930dfda | -5.5923 | -45.17572 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb0033e7-25c9-3c9d-9369-027de42ebb68 | -3.90898 | -45.80317 | 2025-11-15 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f8a0de3-49ce-3653-a25d-800df9e2cdab | -3.28098 | -45.46651 | 2025-11-15 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee2ec165-a78e-3c5f-80f4-ce0174217d12 | -4.41877 | -43.35265 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c2b64fc-bacc-3a3e-8214-edc4a15e523b | -2.71605 | -47.39695 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4f42be2-d3ca-30c6-bf7b-b6128bdbccdd | -2.51725 | -47.81572 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 08004eb9-3e5d-313d-a16c-19a0e7e94cc7 | -6.73447 | -42.96859 | 2025-11-15 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c07a13d3-30ef-300e-bbae-17c959ca3f08 | -5.10091 | -37.78331 | 2025-11-15 04:04:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 392a4ce5-e01f-3337-8d6c-e25111e397c1 | -5.69325 | -45.96523 | 2025-11-15 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8237daef-4556-3809-9d57-141bd21a180f | -2.5131 | -47.80856 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| b10fff7d-08ac-3203-bbed-047e5523e15e | -5.88758 | -42.27344 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 051bd281-e441-3271-896c-a47031b9afba | -5.10775 | -42.78135 | 2025-11-15 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa420011-9b86-3666-8390-4ec0fcadb7cb | -5.48603 | -40.96849 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 43ad2db5-57a1-3741-bb93-52d5da99c6e1 | -4.87165 | -47.26907 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ff917c6-2a89-3a0f-8ac0-26982fcf622f | -5.5635 | -46.54106 | 2025-11-15 04:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c2a1996-686f-3fa8-b0a1-8b0a0556cefb | -5.52127 | -41.76945 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1e19bc6-6b0e-3b0a-958f-1613aea4c641 | -2.43074 | -48.04604 | 2025-11-15 04:04:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61e0f004-d0dd-37d8-8b47-2c2cfcd25c19 | -4.05593 | -46.41664 | 2025-11-15 04:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d1505ae-743f-3266-9bde-e5dd71654f2d | -4.72716 | -47.16193 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 9fe55431-1be8-307a-be22-0a4de189896d | -6.87547 | -42.94928 | 2025-11-15 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 02de6dee-acb6-3f94-ab5e-ceab2ce11f88 | -3.45933 | -40.50437 | 2025-11-15 04:04:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43b7d5e4-e05d-3581-858e-56c937f980fc | -4.46362 | -50.53745 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bedc88b7-2269-3be8-a0e2-fb1d5ec35bf0 | -2.87133 | -51.47251 | 2025-11-15 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2893311f-badc-3b17-9da3-a72ef3aa8e30 | -2.51767 | -47.81187 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| dc4fa529-e779-3555-9f02-b7373671af78 | -4.82178 | -47.09456 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a056c832-ddd8-36b5-816e-d20677a53610 | -5.99848 | -44.06082 | 2025-11-15 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f661953-75dd-3a07-be87-b8a46b739256 | -7.25838 | -40.17471 | 2025-11-15 04:04:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| df2989e5-6902-37fd-b067-6288b1285f0a | -4.6834 | -45.84877 | 2025-11-15 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db47ea5b-4ab0-3507-9b6d-a5ffb0e98c12 | -5.76216 | -42.73137 | 2025-11-15 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fa843d31-8ef5-30b9-b0b4-774e4f0677fe | -3.01427 | -49.43489 | 2025-11-15 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a4f264e-3470-36b8-b965-56a131bc4190 | -4.38696 | -50.43349 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5f62b24-5815-3cd0-b70d-8603bbbd1493 | -4.64063 | -44.60069 | 2025-11-15 04:04:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9bf3432-a6a8-313e-85b8-a341ec33dafb | -3.98848 | -47.99951 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76e02a1a-d55d-3754-a980-17ea98ca4ce7 | -6.15928 | -48.04918 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c35a69f7-132b-30dc-9fb8-646c0285d93d | -7.42867 | -45.23397 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5b4a1a4-58bc-3f9e-9f64-4bf3a5d0ab2b | -4.4724 | -43.42458 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31c10b42-e912-30b9-abe5-e219920a4bea | -4.18175 | -50.4208 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad8845d2-4d8b-3e2c-bfe8-9f785b48d871 | -6.7759 | -44.75978 | 2025-11-15 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1bc9bb7a-23de-3424-8b4a-2ad58f0dcf28 | -4.58085 | -38.35951 | 2025-11-15 04:04:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 065fcac1-37f5-35b4-ad1c-dce8b30737d4 | -4.00129 | -44.16937 | 2025-11-15 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d2d0496-f126-3c50-9a1a-bb0b9eb995a2 | -5.23348 | -44.35176 | 2025-11-15 04:04:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 28d24e3c-f716-3fe2-a28e-8d9d28dad3a1 | -6.88354 | -41.5974 | 2025-11-15 04:04:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4531c4ad-784b-319d-9c04-c0ef2b21d55c | -7.4003 | -41.00909 | 2025-11-15 04:04:00 | NPP-375D | BELÉM DO PIAUÍ | PIAUÍ | Brasil | 2201572 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 22a4824b-1a0c-318b-b3b5-10f9f8ff5c47 | -2.79492 | -52.96902 | 2025-11-15 04:04:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f6eb012-08a6-318e-9fc2-db1e8d5024ca | -4.24997 | -48.20277 | 2025-11-15 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f9936df-72f3-39d4-9448-e2a62f55feca | -7.29572 | -45.11262 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5ef1b71-e8dd-3ca3-830b-5c507fd6c7ec | -4.39725 | -44.07884 | 2025-11-15 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d77142e9-6c21-377c-a8a6-75ea919bc56a | -6.00078 | -45.39362 | 2025-11-15 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65f0d527-b9ef-30ab-963b-39990c9749bd | -1.32962 | -49.1394 | 2025-11-15 04:04:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fecf72e-8edb-3698-8e4c-dcf9059f4d5a | -7.49168 | -42.55223 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 3d39618c-ccdc-3b81-b563-5e054813e2f8 | -5.42741 | -42.57745 | 2025-11-15 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c3af4768-e8b3-3cbf-a904-7a66d930dc38 | -7.10463 | -42.73656 | 2025-11-15 04:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d6fd8841-75a5-3116-a83c-60fc6521e963 | -2.51202 | -47.81491 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c708b30f-b9e9-3bdc-a3e5-41da11e49c1c | -7.46376 | -42.54759 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 80cfbd7e-aad3-327e-82fb-70eb6a1f222b | -6.3023 | -41.82299 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6ebb620d-cb75-32d4-b8cc-b34187de196d | -6.25978 | -41.41328 | 2025-11-15 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c4ff753e-6525-36a2-a4e3-0fbcb5a979d9 | -3.22073 | -45.48044 | 2025-11-15 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b310bd09-a2f0-398b-a4b0-9078e8873c09 | -2.73665 | -45.30666 | 2025-11-15 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b88a38e-1919-36f8-adbb-2688c2f14b40 | -4.53698 | -43.21735 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2e1e2581-dd62-3c23-809c-d0be59558dd4 | -3.22473 | -45.47905 | 2025-11-15 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 181de8e3-9df5-3d2a-95b0-aad6546a14fb | -4.55457 | -44.59286 | 2025-11-15 04:04:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b7ba1d2-a5ee-3bd4-bc5c-186be756c3c9 | -3.86172 | -49.13329 | 2025-11-15 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32aa9039-eaa5-3d49-b381-8b33bb2287ef | -4.25751 | -44.19993 | 2025-11-15 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf624644-003c-39f1-a107-472a172467de | -3.38467 | -47.19235 | 2025-11-15 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ce585be-a0b4-3b85-8ccc-132b26ca5a38 | -5.03761 | -43.60942 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cac93ed2-6e97-35d2-b41d-12e6030f3bf8 | -5.16864 | -44.85241 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68bf3972-3b5d-3a12-a80b-7dda70f74773 | -3.81203 | -43.46894 | 2025-11-15 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcf7a656-e0e3-3071-89b6-557808c223cd | -7.45704 | -42.76647 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a74cefa7-0cec-3e22-879e-44fa67ea4b4f | -5.33448 | -43.03976 | 2025-11-15 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 508d8da4-bcad-304c-8407-e449fff59ebf | -5.51792 | -40.98473 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 51edddeb-4dd7-398d-b9bf-8700be2e5b15 | -7.31306 | -39.78493 | 2025-11-15 04:04:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b912bc6c-f3dd-36ea-afd0-c6cfb1229e77 | -4.4749 | -46.43278 | 2025-11-15 04:04:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 715aa84e-f7a3-3e28-aa63-6aa4380aa4ac | -7.21108 | -35.02872 | 2025-11-15 04:04:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fe182951-a8a2-3ecf-b628-6a6245d5adda | -2.80217 | -52.96981 | 2025-11-15 04:04:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a5cc04a-a6c8-35b1-8402-891ff97af91e | -5.36378 | -44.90326 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d61829f2-e1b4-359f-8a51-7fa7aaff7676 | -5.52412 | -41.77378 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 87c0f3bf-548a-3e30-85a3-74e2ddafefe1 | -8.10764 | -40.87765 | 2025-11-15 04:04:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 354bc008-1a22-35f4-9848-f4c8d62913ed | -4.91742 | -44.78531 | 2025-11-15 04:04:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca849a5e-ef3b-33e2-aa18-47951dcb1065 | -6.31548 | -41.8247 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5bcd9106-2ac8-3e27-812c-0e44df417107 | -3.01361 | -49.43892 | 2025-11-15 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8dafbd4-2a33-3742-aa58-cac0b24057da | -3.06785 | -44.74068 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9f86349-3c05-3bbe-bea1-0483a145fa65 | -5.7201 | -42.34766 | 2025-11-15 04:04:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e33699f4-dd02-3164-9702-b38f80c2ea0e | -4.00484 | -47.68027 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a333a719-0cd1-3fb8-a434-abc80a86f82c | -4.85556 | -43.25495 | 2025-11-15 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d70c82b9-618b-3b98-88c1-c91290443711 | -4.85857 | -43.25996 | 2025-11-15 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf19f13f-657c-3807-8cb2-e1ef10e3ca3f | -4.98333 | -47.23668 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 126d16b9-2a63-3e85-b2f6-aee4b8afcceb | -7.44287 | -42.76507 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7eca9383-a3ab-3766-b18f-937fcb8d728f | -2.86824 | -51.47762 | 2025-11-15 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f719281-e136-39b7-ac0f-1e2048468906 | -6.31487 | -41.82843 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf3f29ea-b4ee-3d8c-9158-7b2acc6408d6 | -4.48022 | -46.62557 | 2025-11-15 04:04:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4649db28-e619-3ca2-bae8-879ae7a53e8c | -5.59582 | -45.18017 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d1c0b98-0d82-3228-9dad-e88d8c12d3af | -7.29633 | -45.1091 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86fdbd6a-7558-37c9-ad46-70b58c30a4d4 | -5.3898 | -44.8438 | 2025-11-15 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a26bd60c-dec9-3a20-a454-e6b8331242b2 | -6.8229 | -48.82813 | 2025-11-15 04:04:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41e1f62a-5130-33c3-9cc8-fdb90bc0d658 | -5.12993 | -44.88345 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a956807-12e3-3791-a80c-0408eec58607 | -7.29231 | -45.10841 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99467860-6347-3a68-a36d-bf6d85d47504 | -4.98131 | -43.88467 | 2025-11-15 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a395e90-1da5-34c5-a04c-1d5dbd83c6e3 | -1.30212 | -49.05782 | 2025-11-15 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
