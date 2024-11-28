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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97825cc1-265a-301b-b728-94a35d113ce7 | -2.04932 | -47.35521 | 2024-11-28 12:33:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b9681e52-494b-328e-9236-3d8f89f7f599 | -3.0584 | -42.01108 | 2024-11-28 12:33:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| ae18bf4e-d3b9-33bf-9f1f-7cc9226108e4 | -4.81218 | -43.29947 | 2024-11-28 12:33:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a6bb2b4a-579b-3763-be0a-d6f0b062b293 | -3.65237 | -41.99935 | 2024-11-28 12:33:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| a85a32c0-6564-3149-be02-b852d437514c | -4.48456 | -42.8733 | 2024-11-28 12:33:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 6c3c7645-6ac8-3552-bc72-294b859a8051 | -3.97022 | -43.70599 | 2024-11-28 12:33:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 96ec7ad1-5f89-3980-a0cc-6d95e98e2cdc | -4.7791 | -46.09261 | 2024-11-28 12:33:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 2598c40d-c0cb-3e0f-9cfd-6287a1ca2d42 | -5.26852 | -43.19717 | 2024-11-28 12:33:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 059789e2-d781-3a6d-ad18-d17b484ba959 | -5.11954 | -45.14648 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 21efca1a-5a00-35d7-a5c5-c4f091d96672 | -2.76032 | -47.60766 | 2024-11-28 12:33:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 392e6c36-8c1c-3e75-b413-6a24d93c7387 | -2.41223 | -45.23346 | 2024-11-28 12:33:00 | TERRA_M-T | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 5c63a11c-c59e-3675-8642-365f50896240 | -2.80566 | -46.82978 | 2024-11-28 12:33:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 63f8f151-4b2f-39a6-9f48-006d926d2bfe | -6.35921 | -43.3718 | 2024-11-28 12:33:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4f298dd2-0cfc-33e6-a3f6-c1d7ff6e103f | -3.48119 | -42.2805 | 2024-11-28 12:33:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| ac959e7b-cc79-309f-b855-f6d4fea1c560 | -3.84427 | -43.93995 | 2024-11-28 12:33:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4594e428-a421-30b1-aa10-1a180eeda1da | -2.58304 | -46.98665 | 2024-11-28 12:33:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 363ab3f7-cae6-3a86-98e8-98085c794cf3 | -8.33048 | -42.26086 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 033ce382-698f-3ae5-a3db-8ca26d3b2adf | -6.47257 | -43.42325 | 2024-11-28 12:33:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 738b8d97-fade-33b0-8e05-de964872245a | -4.39708 | -42.45771 | 2024-11-28 12:33:00 | TERRA_M-T | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 9832adab-cece-371b-9403-2685b8d7d13a | -3.51947 | -45.11202 | 2024-11-28 12:33:00 | TERRA_M-T | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 29a2ef35-fc4e-3e41-90d2-b0aefc26ae9f | -6.35818 | -42.92514 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 14.8 |
| b3829b00-e89a-3111-9506-2ca6179b3889 | -6.06481 | -44.15517 | 2024-11-28 12:33:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 362872cb-40b4-3583-8c8a-da803b3f5933 | -3.923 | -42.4146 | 2024-11-28 12:33:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| c9994738-7d4e-36b5-a2f1-96d0672303f7 | -3.29622 | -41.98051 | 2024-11-28 12:33:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2078c514-1acf-3d78-a6ac-a5746d733a67 | -6.3156 | -39.28624 | 2024-11-28 12:33:00 | TERRA_M-T | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 38.3 |
| a0b81b14-2a12-3673-849f-adc1be0fc209 | -6.18612 | -42.02911 | 2024-11-28 12:33:00 | TERRA_M-T | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 7d005d19-7ac9-3c0a-a13c-29331084c5f4 | -3.83563 | -42.78481 | 2024-11-28 12:33:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1f7e0506-3747-3364-84fd-dece3d26880f | -6.04937 | -45.79663 | 2024-11-28 12:33:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 10e5ca3d-d1ce-39aa-a4a7-d9e8659ecb96 | -1.77847 | -47.67071 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 0544dd47-0e01-39e8-ada5-d43445130f93 | -3.49116 | -41.97596 | 2024-11-28 12:33:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| f1db2b51-8425-31da-8838-da2579c64ce6 | -3.30743 | -41.9712 | 2024-11-28 12:33:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 09f6aba9-cb5f-332e-8a91-1f78979c00b7 | -4.15568 | -43.83345 | 2024-11-28 12:33:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f14c311a-0227-337b-b974-db64d6dc61b7 | -3.47167 | -42.27922 | 2024-11-28 12:33:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 3ed193d2-4454-3d28-932b-b35880fb2934 | -4.92261 | -48.50946 | 2024-11-28 12:33:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 42541f92-0edc-39b9-a8cc-04af754549c7 | -5.02637 | -38.8598 | 2024-11-28 12:33:00 | TERRA_M-T | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 21.5 |
| a676a3b2-2bb6-3326-b6e0-5b00dde84036 | -3.55971 | -40.7091 | 2024-11-28 12:33:00 | TERRA_M-T | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 24.5 |
| e6c9378d-5c4c-38b5-8a46-7c4a09d95a61 | -3.56171 | -43.14644 | 2024-11-28 12:33:00 | TERRA_M-T | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 74423c4a-3249-35db-b0d5-cd94d1d310ac | -3.59998 | -43.07458 | 2024-11-28 12:33:00 | TERRA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| fe570f4c-161e-3cff-851f-a112da489702 | -3.97081 | -48.08742 | 2024-11-28 12:33:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 855dd467-e095-3c9a-ac1c-c515299cef47 | -5.15416 | -43.16908 | 2024-11-28 12:33:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3fd14617-9959-3677-a65a-54e3e0f6cf6a | -8.34713 | -43.92093 | 2024-11-28 12:33:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1625e688-5848-35b7-a30c-75338560c377 | -5.98356 | -45.36639 | 2024-11-28 12:33:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0b483906-f2f6-3b73-ac27-af73a2f282fc | -3.34409 | -50.50346 | 2024-11-28 12:33:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 6812bcaa-d6dc-30ef-9b44-67a94153c868 | -3.02305 | -45.66426 | 2024-11-28 12:33:00 | TERRA_M-T | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| e0e9462f-4148-3a24-86ae-f05224a4ba2c | -5.08959 | -44.71437 | 2024-11-28 12:33:00 | TERRA_M-T | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 481dc67e-dfc2-332d-8d19-a93043bba383 | -7.80134 | -46.5651 | 2024-11-28 12:33:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| cee6d999-d085-30fe-b0e0-3b797977bed5 | -4.01723 | -43.2503 | 2024-11-28 12:33:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 572a92b9-9bdf-3c4a-acca-83a24ea2e5e7 | -4.73695 | -42.97725 | 2024-11-28 12:33:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fede306c-8ed8-3be5-a8c6-da76735223a4 | -6.66041 | -43.05379 | 2024-11-28 12:33:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 27882f20-0b56-304e-9820-ff9b02a53928 | -4.66407 | -42.38547 | 2024-11-28 12:33:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 162.7 |
| ee9a15fc-d604-3c61-90bb-d73aeecab19e | -8.0605 | -43.79245 | 2024-11-28 12:33:00 | TERRA_M-T | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 04489ba4-d604-3f1f-9b9d-21cf551d5914 | -6.68458 | -43.0881 | 2024-11-28 12:33:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ca3dee8d-ff86-3ea4-a821-4b940a80bee3 | -2.98913 | -42.29715 | 2024-11-28 12:33:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 60a3faa6-867e-34ca-9158-4a45328c1e2d | -5.16011 | -44.92797 | 2024-11-28 12:33:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3ba95588-1952-387e-aa9e-8fb0d5e0c3db | -4.17729 | -48.63577 | 2024-11-28 12:33:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 0ea6c977-d7f0-3723-b159-dcbc4ce13b06 | -4.24789 | -41.92439 | 2024-11-28 12:33:00 | TERRA_M-T | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 3b07fdb9-0c4d-33cb-9d01-3dff960003af | -5.97474 | -45.36515 | 2024-11-28 12:33:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| db764b66-7fcd-3e87-9114-8fbd2de257b7 | -3.52703 | -45.12206 | 2024-11-28 12:33:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| c347bf8c-80ac-371a-a242-c6705200d5b6 | -2.58857 | -46.98293 | 2024-11-28 12:33:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8895396d-bbab-3b16-b90f-1cb9e8e9751f | -3.8344 | -40.56289 | 2024-11-28 12:33:00 | TERRA_M-T | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 57145475-b5ee-3bfd-beea-e06005dd784a | -5.94886 | -43.99589 | 2024-11-28 12:33:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2620adb4-741b-3b3f-bd07-2c5e304cfe1b | -5.00296 | -43.83992 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 8199a0f2-9a9a-39ae-968a-9fdeaee8c939 | -3.66074 | -42.10448 | 2024-11-28 12:33:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| ea731e09-9582-3427-b2ba-63e12cac241e | -6.26525 | -46.09145 | 2024-11-28 12:33:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4403245a-a038-3931-b5f5-0d95cda31c83 | -3.26394 | -42.13715 | 2024-11-28 12:33:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 84fdc11d-5ccb-35ce-b2f6-9c489a40c39e | -6.31987 | -43.39972 | 2024-11-28 12:33:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| cda9974d-b70b-359c-b3c7-1858d0a3cf70 | -7.1725 | -44.98668 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c1e2fdcb-bdd8-3522-b401-706d80b156d1 | -3.84139 | -42.79205 | 2024-11-28 12:33:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 10e104ff-260b-3a24-9c9f-98cbe86e70c1 | -3.51711 | -41.65575 | 2024-11-28 12:33:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 32.9 |
| f509dcb2-d6e1-3001-a4eb-ff4271124661 | -5.45278 | -43.26483 | 2024-11-28 12:33:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 471ca09a-2799-31a2-9bef-04a6b00d3e6f | -3.56037 | -43.15586 | 2024-11-28 12:33:00 | TERRA_M-T | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 27753429-b86f-3852-998a-ea2f7e1920ca | -3.49479 | -44.70803 | 2024-11-28 12:33:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8100fcad-f215-3499-abd0-6b046709a321 | -2.82528 | -41.77508 | 2024-11-28 12:33:00 | TERRA_M-T | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a6a6c507-94aa-3859-b50e-7b4e52e11cfc | -5.52573 | -39.33802 | 2024-11-28 12:33:00 | TERRA_M-T | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 6982e048-2c7d-30cf-bb7f-6d2bdcb21a38 | -4.76409 | -44.80264 | 2024-11-28 12:33:00 | TERRA_M-T | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9c210b0c-5fc0-3513-8b5f-b0ef432ebf23 | -3.75349 | -44.56862 | 2024-11-28 12:33:00 | TERRA_M-T | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 462d0b2a-5219-3194-a108-ea9a38187047 | -5.46604 | -47.25982 | 2024-11-28 12:33:00 | TERRA_M-T | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bf99f3f2-c6d3-38ed-97a9-7b4312fdf04f | -7.17123 | -44.99554 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 478555b8-2bde-3f2b-964c-3316fa16f99e | -4.9332 | -44.64403 | 2024-11-28 12:33:00 | TERRA_M-T | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d246ab32-24ac-333b-8691-4389667d0f5d | -2.53473 | -47.32271 | 2024-11-28 12:33:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c0e3df4b-d428-3e2c-a1f0-0211e2ab8ef0 | -3.69582 | -43.43422 | 2024-11-28 12:33:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| db131ced-95ed-31b6-8748-caebffb6e521 | -3.14212 | -42.20917 | 2024-11-28 12:33:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 8b47e877-6b69-34c0-9913-3601c4a266f6 | -6.51487 | -44.03627 | 2024-11-28 12:33:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 33713b3f-7c93-36a7-9744-3b7b99ed7d6c | -4.78673 | -46.10292 | 2024-11-28 12:33:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 66d501ac-fcd2-35fc-a185-8f489ea6ca4e | -4.96092 | -39.89454 | 2024-11-28 12:33:00 | TERRA_M-T | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 68a00183-158a-3ec2-b32f-85e34b537d75 | -6.30673 | -46.68864 | 2024-11-28 12:33:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c2642d1a-5f91-36a3-b2dd-f1c56fc0e3b1 | -3.26792 | -45.37337 | 2024-11-28 12:33:00 | TERRA_M-T | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| f910383a-724b-36f3-9e41-b6d38f34eb8b | -5.53737 | -39.13029 | 2024-11-28 12:33:00 | TERRA_M-T | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 8ab7f737-0c86-3c74-9628-ebcd2698ce47 | -5.4675 | -47.2499 | 2024-11-28 12:33:00 | TERRA_M-T | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d30415b7-928b-33f8-91c5-5082961c545b | -6.09008 | -44.87781 | 2024-11-28 12:33:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ee294ee0-a344-321b-a5ed-b3430b58f47e | -3.81173 | -47.64268 | 2024-11-28 12:33:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a703669b-c533-3827-a9e7-e43eb2250eb8 | -6.55454 | -42.17424 | 2024-11-28 12:33:00 | TERRA_M-T | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 879fcc73-d514-3ee9-944a-94a1d0b1e10f | -5.10927 | -43.15296 | 2024-11-28 12:33:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ffb9a1ef-a4df-36fc-a51d-fe75e6bbe51f | -8.1515 | -44.06765 | 2024-11-28 12:33:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 857c1f9c-55e4-35a8-b388-cab3878046ea | -2.99703 | -45.4682 | 2024-11-28 12:33:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a5dfc823-9aee-36ac-8c29-d9f8b9c36631 | -4.06666 | -46.54335 | 2024-11-28 12:33:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 01a10b7a-2026-365d-869b-c7b6900dce40 | -2.04773 | -47.36619 | 2024-11-28 12:33:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| dc23214f-8a3a-39ec-be54-cdb1cccad627 | -6.17707 | -42.62146 | 2024-11-28 12:33:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| f3b6d9aa-bda6-3e50-a965-556bfc4444f0 | -2.60499 | -46.83405 | 2024-11-28 12:33:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 1b54d9b7-1dbb-3d2d-8846-a2171cdd42c6 | -5.7632 | -44.8496 | 2024-11-28 12:33:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README101.md)
