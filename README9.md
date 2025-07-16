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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a17f8233-1421-3e0d-83d4-a5b5a700d11b | -7.19665 | -43.12551 | 2025-07-16 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5b327c12-5078-3349-be4b-0feb0c0e30aa | -8.25459 | -46.36474 | 2025-07-16 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab457869-d731-38f6-a118-17df1cf75091 | -5.78695 | -45.088 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2636564-2101-3e42-96b8-326ff088bb87 | -6.72674 | -44.33544 | 2025-07-16 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f95c865c-9317-3e10-bc0e-950e11dca861 | -7.30907 | -45.76782 | 2025-07-16 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9ddee77-c48f-34f9-a6b8-e6520b2451db | -7.10305 | -43.65145 | 2025-07-16 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 896303d9-c35f-3e5d-bc72-e8db2aedc6a0 | -7.83924 | -44.19709 | 2025-07-16 03:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79e6cf73-a37b-39a9-8e55-6a543b2160eb | -5.78235 | -45.08408 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de62a9bc-4b3f-371b-83e7-4c8fd1076f9d | -5.53494 | -43.88623 | 2025-07-16 03:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60d41b35-7e9c-3990-bd8a-ce3697f269e1 | -7.10836 | -43.64762 | 2025-07-16 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa306005-7f2c-3ea5-b024-e4823575f066 | -5.78184 | -45.08709 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d8bf8b0-ab42-3e39-a292-4c188a0f0e22 | -7.27261 | -45.29409 | 2025-07-16 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36c04daf-5e8f-33a5-b18a-cdeb7873bc15 | -7.32069 | -44.21666 | 2025-07-16 03:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a92f14ea-8b61-3c06-97a5-ffc7e5156b8e | -6.3334 | -42.37513 | 2025-07-16 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fe0f9fc0-0838-36b9-8443-e71166677f7e | -3.03404 | -47.86054 | 2025-07-16 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 51de4bf4-01c0-33fc-abec-39e3383a2e37 | -2.92766 | -49.06681 | 2025-07-16 03:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 041539fe-ec6f-37df-9b7c-7c98e62bb19b | -4.77797 | -45.34156 | 2025-07-16 03:49:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe7ff7fb-d383-33c6-b4cc-efdfb80eefe5 | -5.66673 | -43.71706 | 2025-07-16 03:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 24370ce9-bbbd-3400-ae2b-93bfe02097f8 | -2.92276 | -48.23876 | 2025-07-16 03:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ee1730a-fe82-3d88-aa52-f7cb72b49781 | -5.53581 | -43.88111 | 2025-07-16 03:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d208d64-55c2-33a8-8d42-aa1311bf51bc | -7.46501 | -43.83951 | 2025-07-16 03:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8d7efad-5d25-3081-8fd5-05be5ef13e4a | -6.71809 | -44.32862 | 2025-07-16 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b78b12d8-51c5-32c6-a6e1-5897fe13e640 | -5.54791 | -45.19878 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f163938-f823-3ff1-b7d0-2887108c065d | -9.59884 | -40.60757 | 2025-07-16 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d147a176-5278-31b8-a0e0-9e85a679a709 | -5.87846 | -42.40744 | 2025-07-16 03:49:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ca956c9-9806-3ea3-bc77-65ef38ead082 | -3.38358 | -47.49353 | 2025-07-16 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2bb000da-144a-32dc-b82a-af2a8b72753c | -7.27614 | -45.29575 | 2025-07-16 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c73783a0-a16e-3e53-85d0-5f6b5dd340d9 | -7.31428 | -45.7687 | 2025-07-16 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb0007d6-a1aa-33d2-897e-988a5616c7c7 | -7.83378 | -44.20092 | 2025-07-16 03:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cdae3e9-851b-397d-9065-abc1a9fe2a0b | -6.44549 | -42.80913 | 2025-07-16 03:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 03344e66-8e3b-31ac-9a05-f23491bca778 | -9.43393 | -40.3653 | 2025-07-16 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f90ac28a-1e72-3e48-a1fb-a6ee391aea38 | -4.30465 | -48.09958 | 2025-07-16 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51710838-8c0f-3496-8814-e0e0cd3b1ca9 | -8.54326 | -36.50988 | 2025-07-16 03:49:00 | NPP-375D | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5dc6d71d-a24d-3a98-a7ca-1919729b1bb6 | -4.58597 | -47.262 | 2025-07-16 03:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b690a3a7-ae77-3a65-b37f-ae8c773dc83d | -7.05715 | -38.8598 | 2025-07-16 03:49:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 19f770e6-a034-3a77-9472-54ac02c301a4 | -5.78933 | -45.08929 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bacb2132-fee6-3ea3-9549-65d52e8b56fe | -5.79308 | -45.08282 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6aa41ef2-6633-3893-8ea5-2da618ffe1ca | -5.36031 | -36.8903 | 2025-07-16 03:49:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9170603b-1920-3c68-a00d-c3b1d3f255de | -4.78379 | -45.33921 | 2025-07-16 03:49:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4abb4ee7-864a-30ea-ba29-a717e0b0bee4 | -7.19807 | -43.11713 | 2025-07-16 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c780d188-6c4b-3685-9712-57ff3e45c130 | -5.78132 | -45.09014 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b59bf0b3-3671-3f9c-807d-2159a01f41c5 | -9.5906 | -40.36074 | 2025-07-16 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c068e099-99d4-3ed0-ac43-c567f067d807 | -5.78987 | -45.08625 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3ed94db1-501d-3b4d-a6a8-7d6077d34270 | -4.03753 | -48.06324 | 2025-07-16 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a356b3d-31e5-3929-843a-413ea951d721 | -5.5302 | -43.88552 | 2025-07-16 03:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4fd11932-b0ab-333b-954c-086a78234a3a | -7.94263 | -49.65528 | 2025-07-16 03:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a92c1d26-531c-3573-ba6f-89725d333f01 | -6.34356 | -43.43219 | 2025-07-16 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d25c9c4c-846b-359f-a5b4-1aa4c493f2ae | -5.96666 | -44.16976 | 2025-07-16 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6176577-0fe2-37f8-9bbb-63a21961bb9a | -7.20172 | -43.12206 | 2025-07-16 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 45dcd937-e70d-3ea1-a023-ce093dcd9d28 | -6.73151 | -44.33627 | 2025-07-16 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f9393a30-5954-3b6d-be29-5095e8afc796 | -4.78231 | -45.3384 | 2025-07-16 03:49:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5fae3a7d-ac7e-3db1-b876-6c52efd544b8 | -3.8487 | -47.7555 | 2025-07-16 03:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd601f33-e7eb-34e6-aacf-048402c606e1 | -9.60372 | -40.55678 | 2025-07-16 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0726e1a8-16bd-3731-a3c3-bf41dc45e50f | -2.9168 | -48.2419 | 2025-07-16 03:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9d50aacc-9523-314d-b6ac-dfde59893056 | -2.44004 | -47.32834 | 2025-07-16 03:49:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d84c6b27-bec2-3e1c-8ac9-1ed7d83cc5ff | -7.34838 | -45.6683 | 2025-07-16 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ff25632-3a2a-30c8-a7c2-b70a66d166d9 | -6.304 | -38.91159 | 2025-07-16 03:49:00 | NPP-375D | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 137cd564-071c-3242-8c32-515062f10f42 | -5.46439 | -45.34198 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e02412c6-6952-3db6-b753-096c86d388d1 | -9.3659 | -37.9698 | 2025-07-16 03:49:00 | NPP-375D | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 111e821b-af66-3f49-87d1-f92f09e0afdf | -6.71332 | -44.32777 | 2025-07-16 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| aef221bb-e9a3-3471-9c0c-8973b97c7512 | -6.8693 | -41.72995 | 2025-07-16 03:49:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7ce94063-0c89-33ab-972e-05fe793eb851 | -9.43325 | -40.3694 | 2025-07-16 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| e69c7b0b-8f11-378a-8105-30656efed682 | -5.54739 | -45.20186 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f28e6e8-e715-3b69-8aa2-41ae81832813 | -6.63767 | -44.57449 | 2025-07-16 03:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aeeda86b-26b9-30e2-8649-e8043c93b162 | -6.37775 | -44.75093 | 2025-07-16 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6abc478-e26e-3395-a2bb-c298158e8bbb | -7.945 | -49.654 | 2025-07-16 03:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dd7c4467-b285-35e1-a930-1ff88387addc | -6.63283 | -44.57352 | 2025-07-16 03:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93085520-9a43-338d-ad28-980ef2eb04b9 | -8.25988 | -46.36592 | 2025-07-16 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 582cc92b-665c-384f-b106-41c7c4ccf826 | -5.97052 | -44.17587 | 2025-07-16 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a9b5039-65ae-395b-8ad0-1d13d58f02d1 | -5.52934 | -43.89061 | 2025-07-16 03:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 745be0d4-8f5c-349a-8681-325a8e3ca1ea | -2.91622 | -48.23762 | 2025-07-16 03:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5be6bdf-28be-3cd8-8424-ab9c7106607a | -7.18936 | -43.11557 | 2025-07-16 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f0ec0e79-b1c6-33d9-b5ab-b3719da983a7 | -6.87331 | -41.73057 | 2025-07-16 03:49:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf18b8fc-afff-35f2-9b19-53a321d312b2 | -9.42967 | -40.3688 | 2025-07-16 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 7874f3c1-254c-34f0-bb07-3caa0ea1576b | -7.05857 | -38.85617 | 2025-07-16 03:49:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4ddb7555-bd7a-3842-a9c9-bb945bfeb5a4 | -7.34147 | -49.60741 | 2025-07-16 03:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26bfd70f-a770-30e8-ba55-040e4851ab07 | -5.71832 | -44.82987 | 2025-07-16 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79bd6a1d-a9d2-32e7-a373-d3bf649c5c18 | -7.83841 | -44.20183 | 2025-07-16 03:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e15822d9-a2f1-3f8b-982b-4ad943fbbece | -7.31371 | -45.77188 | 2025-07-16 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b24cd815-9d41-3cea-b104-5faa7490e9f6 | -6.947 | -42.37743 | 2025-07-16 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a6132c3b-b539-3913-ae38-f3e3d8eaa6f6 | -5.79096 | -45.08015 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00f65f1a-d37c-3548-9cea-714e3fe2c791 | -3.21186 | -48.97271 | 2025-07-16 03:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a3491ae-b1f4-3249-87c3-ddaf1018f5f1 | -8.50858 | -43.30186 | 2025-07-16 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 386adf7e-e4c9-3128-af14-65a0ca978231 | -2.91525 | -48.24318 | 2025-07-16 03:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba829eb7-902e-30f4-9113-5dba5b3c0f4a | -7.04472 | -43.47914 | 2025-07-16 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f16342da-b174-377c-b463-1e14d4ffb48a | -4.60277 | -43.32551 | 2025-07-16 03:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8563121-5dfa-3367-bba2-97680af8b01e | -3.03313 | -47.86591 | 2025-07-16 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ba9ff18e-effa-329d-87f2-42531d67d24e | -4.30329 | -48.09898 | 2025-07-16 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 303ae64c-4424-38de-9c78-2d620ea48c8d | -6.63468 | -44.57637 | 2025-07-16 03:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a8bf84ff-9776-3c7c-bac2-1e71d3d922db | -7.19371 | -43.11636 | 2025-07-16 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| bc19bbcd-9df9-342d-9b49-d15af30cd83c | -7.27109 | -45.2949 | 2025-07-16 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6111631b-679c-30ac-97aa-83338f28941b | -8.87263 | -37.02084 | 2025-07-16 03:49:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 666af21c-9e46-366a-a7c7-17181bb796be | -3.37991 | -47.47773 | 2025-07-16 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fef9e968-46e6-343d-a368-dae7cd280d5d | -5.7888 | -45.09231 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95b945ed-017a-3bea-9cc3-073732193300 | -2.92077 | -49.0657 | 2025-07-16 03:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a67099fd-0c70-3eda-964f-df0519bfc656 | -6.46426 | -42.82962 | 2025-07-16 03:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 74762dd2-2634-3a07-b7b6-ec7b0e310df1 | -6.4362 | -42.8114 | 2025-07-16 03:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7767ba2c-43e0-3dec-9815-8ce8005a0f44 | -4.77853 | -45.33818 | 2025-07-16 03:49:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8569e197-f2ae-393d-a7ae-a84ed1fc6464 | -7.18864 | -43.11978 | 2025-07-16 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 584a2eb1-6029-3627-91d6-3fcee614431a | -7.19736 | -43.1213 | 2025-07-16 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |


[Clique aqui para ver as próximas entradas](README10.md)
