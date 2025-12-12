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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be044506-cd0f-3af6-95bf-d88eae6c5cbc | -2.4183 | -51.9278 | 2025-12-12 08:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 65d1577a-ba5c-3e04-ad7e-47ded65e4e66 | -2.4183 | -51.9278 | 2025-12-12 08:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| d8e06b61-7695-370c-8a00-b34c20ae8a10 | -2.4367 | -51.9274 | 2025-12-12 08:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 6d5d2b76-31ee-3926-b25e-10ff1cf3e291 | -8.62603 | -40.19465 | 2025-12-12 11:36:00 | TERRA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 5cabc9ba-8a68-3830-8580-aa69f4580e82 | -7.04356 | -38.44217 | 2025-12-12 11:36:00 | TERRA_M-M | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 396d527e-5658-3752-8763-9a1d412c9e69 | -5.93645 | -38.89399 | 2025-12-12 11:36:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 3f8d507a-07c7-32a1-a306-b95e20af78ce | -9.09978 | -40.17215 | 2025-12-12 11:36:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 31bf94ff-53a2-375b-b2d6-b94c0b8ad71a | -5.36455 | -38.1309 | 2025-12-12 11:36:00 | TERRA_M-M | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 1378ab46-b66d-366d-8b70-5359e55cf143 | -8.24548 | -37.77555 | 2025-12-12 11:36:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 33.6 |
| cc802631-7029-33bc-b631-33618222cf98 | -5.79323 | -36.53477 | 2025-12-12 11:36:00 | TERRA_M-M | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 91ca085a-dd7b-3ae0-a2a2-f1c286795cb8 | -4.99615 | -38.0635 | 2025-12-12 11:36:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f552dc1e-e90d-39de-931f-5398201e9ef3 | -6.05833 | -38.11017 | 2025-12-12 11:36:00 | TERRA_M-M | FRANCISCO DANTAS | RIO GRANDE DO NORTE | Brasil | 2403905 | 24 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c76137c8-4034-32d1-8bfd-7e395026211f | -7.866 | -37.98933 | 2025-12-12 11:36:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| c7b6de12-3cb7-38c4-8089-d6d6b46721a8 | -5.88433 | -38.36655 | 2025-12-12 11:36:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 54e9928d-a2f5-3ae6-9164-bd74d94c136b | -9.33646 | -37.09342 | 2025-12-12 11:36:00 | TERRA_M-M | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 3c65cc3c-28ac-3ed3-b985-e4bb0348c426 | -2.90771 | -41.94509 | 2025-12-12 11:36:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 351ef109-c0e2-30f4-aedf-b4e4d1e63fc9 | -6.39588 | -38.90831 | 2025-12-12 11:36:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 4b370948-31ee-3313-964e-1495cc8cc67b | -4.69441 | -37.59291 | 2025-12-12 11:36:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a3149bc1-6b67-35ff-b638-d4169aba9860 | -6.18193 | -38.47196 | 2025-12-12 11:36:00 | TERRA_M-M | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 5af75b3b-69e4-3515-add0-ae4b4528ada4 | -5.79456 | -36.52523 | 2025-12-12 11:36:00 | TERRA_M-M | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 12.7 |
| f7d108ae-bacc-37bb-bc09-ad1e012c5a52 | -6.46842 | -38.40503 | 2025-12-12 11:36:00 | TERRA_M-M | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| b23bc40c-0789-3492-9c5d-6ca499df1aa3 | -7.63798 | -37.70976 | 2025-12-12 11:36:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 4ab3cd0f-be64-3aa5-b568-fb41a6fcd575 | -7.63925 | -37.70069 | 2025-12-12 11:36:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 824fa4b9-b8f4-3885-828e-b0c45bc4a7a8 | -4.99741 | -38.05471 | 2025-12-12 11:36:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 96.3 |
| e2044930-a1d7-39b8-8dbc-75eb334ec566 | -7.42088 | -38.00518 | 2025-12-12 11:36:00 | TERRA_M-M | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 22469240-e5b4-3ca6-ae43-f7147efa97de | -9.30812 | -41.20107 | 2025-12-12 11:36:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 0237ed65-5818-3517-b1c1-2550abf48844 | -7.67245 | -37.5941 | 2025-12-12 11:36:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e46bae62-bba1-3599-909d-cc68987ba964 | -10.64288 | -40.22219 | 2025-12-12 11:36:00 | TERRA_M-M | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 65985fdd-203a-35b0-b78c-36543ee0e4a3 | -6.78369 | -38.32425 | 2025-12-12 11:36:00 | TERRA_M-M | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 2bfe0c4a-4181-31f8-a7fb-ad17b13d362a | -7.91671 | -37.62836 | 2025-12-12 11:36:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| ae1d3bc3-b6c2-3902-9d4d-8dba52cdfaa8 | -8.99198 | -37.58179 | 2025-12-12 11:36:00 | TERRA_M-M | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5dc54d2d-e89d-38de-bb93-93685cdc51fd | -8.30931 | -37.91089 | 2025-12-12 11:36:00 | TERRA_M-M | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 68c1aac9-7ac7-3c39-847d-13302563c47e | -7.67373 | -37.58498 | 2025-12-12 11:36:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| af3843ad-1a23-3fb0-9891-db5185a79e47 | -8.92236 | -37.94693 | 2025-12-12 11:36:00 | TERRA_M-M | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 6c1219c8-8f48-37b7-922e-17e0dbfc10fb | -7.66464 | -37.84211 | 2025-12-12 11:36:00 | TERRA_M-M | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| df515f7b-6145-3fed-bdad-e0ae6c10a01e | -7.39152 | -35.98594 | 2025-12-12 11:36:00 | TERRA_M-M | QUEIMADAS | PARAÍBA | Brasil | 2512507 | 25 | 33 | nan | nan | nan | Caatinga | 7.6 |
| a80bb2dd-d84c-397c-9346-224f2511e19a | -6.62344 | -36.92631 | 2025-12-12 11:36:00 | TERRA_M-M | OURO BRANCO | RIO GRANDE DO NORTE | Brasil | 2408508 | 24 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 781eea53-71b1-3190-8d1b-55f8aa60e96a | -4.8635 | -38.20267 | 2025-12-12 11:36:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 85884372-db4f-3a30-9576-0c82387ffc8d | -6.22597 | -35.47493 | 2025-12-12 11:36:00 | TERRA_M-M | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 10.6 |
| fe0aa98d-9b5b-3a4e-9bd6-6ee39fd804b6 | -7.94871 | -37.59537 | 2025-12-12 11:36:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 9a218063-80a5-3d4e-b752-afecc2b39157 | -5.87552 | -38.36531 | 2025-12-12 11:36:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 29.6 |
| 197daa2e-00f4-303f-83a0-93c45ecc6df1 | -8.36729 | -36.84489 | 2025-12-12 11:36:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 160fdd65-4b70-31f3-a76a-19bfa2407ba7 | -6.30813 | -38.56508 | 2025-12-12 11:36:00 | TERRA_M-M | VENHA-VER | RIO GRANDE DO NORTE | Brasil | 2414753 | 24 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 6b4f8c0a-8956-32d5-b0af-f379c905e053 | -6.36126 | -37.92788 | 2025-12-12 11:36:00 | TERRA_M-M | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b8ec6d9f-dd36-3a7f-a7ad-c0c397c249a7 | -5.88559 | -38.35775 | 2025-12-12 11:36:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 5da41c29-06fd-3e0f-aa88-2e743b503488 | -5.87678 | -38.35652 | 2025-12-12 11:36:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 9a061e98-9a14-335c-9a4b-917bc4ff537b | -16.39897 | -42.53582 | 2025-12-12 11:38:00 | TERRA_M-M | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d40eebed-adaa-3bd7-b100-a5e3b9c4ab25 | -17.10286 | -39.19587 | 2025-12-12 11:38:00 | TERRA_M-M | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 8070a1d3-f488-3ca6-ae70-8214c177a638 | -17.98572 | -40.20803 | 2025-12-12 11:40:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 1e6b1d78-725b-31d5-a027-7fb27a5aea38 | -20.33917 | -41.73729 | 2025-12-12 11:40:00 | TERRA_M-M | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 6839d4a7-2afd-3893-9c10-151b000408f6 | -17.98703 | -40.19868 | 2025-12-12 11:40:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 2b55fe13-dac5-3d14-8f03-64e434c608d1 | -17.99462 | -40.20935 | 2025-12-12 11:40:00 | TERRA_M-M | PEDRO CANÁRIO | ESPÍRITO SANTO | Brasil | 3204054 | 32 | 33 | nan | nan | nan | Mata Atlântica | 36.0 |
| 9cb4f403-4ea6-3ad6-b0f9-2651b94b4e88 | -18.99517 | -39.89734 | 2025-12-12 11:40:00 | TERRA_M-M | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e8c6566b-89dd-3eb9-b808-f31dd0c699bc | -19.24069 | -40.1192 | 2025-12-12 11:40:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 4e4d6337-5224-3086-ad41-36930509c6bf | -17.99593 | -40.20001 | 2025-12-12 11:40:00 | TERRA_M-M | PEDRO CANÁRIO | ESPÍRITO SANTO | Brasil | 3204054 | 32 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| 00ef7b4b-66e5-3bb6-8088-39cb857c6852 | -8.3681 | -36.8323 | 2025-12-12 12:00:00 | GOES-19 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 8853d1ec-2d5b-3bb4-884a-d1d961bbf028 | -7.3251 | -37.8105 | 2025-12-12 13:20:00 | GOES-19 | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 115.5 |
| de804868-a7e7-333e-8bc3-96244b69d604 | -8.386 | -36.9092 | 2025-12-12 13:30:00 | GOES-19 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 108.8 |
| 14f06cde-4c08-3303-8a94-c2795f222747 | -7.8845 | -37.2693 | 2025-12-12 14:10:00 | GOES-19 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 110.1 |


