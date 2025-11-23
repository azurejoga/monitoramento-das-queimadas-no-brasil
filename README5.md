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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4be4cd2c-4f3c-37be-8d31-993cf427f8fc | -4.39437 | -45.73451 | 2025-11-23 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae77bddc-e33b-31e9-b6d5-3fb86b90eb41 | -5.57663 | -42.30028 | 2025-11-23 04:25:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 55314f3b-130f-31b0-a4be-b6f949dcf62b | -4.17359 | -47.53978 | 2025-11-23 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 28b6f422-9ebf-3653-9518-398097c71085 | -1.88774 | -50.97406 | 2025-11-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdc66f90-1045-3328-8133-9d144b5cf3cd | -4.5604 | -45.49953 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93addc7b-8b25-3ab2-add8-15be6ca89c97 | -1.6715 | -52.04623 | 2025-11-23 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b1809da-afd5-31e4-b655-358f90257158 | -5.44299 | -46.89708 | 2025-11-23 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 2a09525c-3fcf-37f6-a34f-6319b83c5b24 | -6.37994 | -46.32738 | 2025-11-23 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3a57cee-1f43-3f85-b9e5-a05d5e4b3aaf | -2.88919 | -45.28964 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3568cd3d-7999-3de0-ae94-87b443afe17c | -2.63847 | -47.29795 | 2025-11-23 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf315daf-8743-3bc9-9bb4-b3614f14aec7 | -4.56424 | -45.4966 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62309aa5-dae2-3c2c-a7ab-77b7950362de | -2.69813 | -49.51139 | 2025-11-23 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92f27571-32cf-3105-a58b-4e86b2b4978e | -5.67714 | -48.79361 | 2025-11-23 04:25:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e0f7788-f0d6-3d3f-850e-e04f88b3b077 | -4.55898 | -48.48373 | 2025-11-23 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f15f12eb-dbfe-394d-8ccc-d5cc51798575 | -2.44543 | -49.09845 | 2025-11-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08e5dcf3-aa06-35f0-8961-f2eb17585908 | -5.5448 | -41.04288 | 2025-11-23 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 16dadae3-925e-3405-9741-821f8a3962fc | -2.47265 | -45.42795 | 2025-11-23 04:25:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5debdc5c-5742-3ec9-81ab-ac9cd78c72ff | -5.97602 | -40.38299 | 2025-11-23 04:25:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cd81ee5f-752c-3e87-a91f-19dd28e1bc23 | -1.74079 | -52.02607 | 2025-11-23 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 70433586-f804-3ffa-b292-c78e008dfdd7 | -1.74536 | -52.02676 | 2025-11-23 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 199001a6-39f7-3a09-9e06-18de0bb0f889 | -4.91705 | -44.52096 | 2025-11-23 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86150df8-fe65-33a0-b99c-a17e95676792 | -4.64323 | -45.47071 | 2025-11-23 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f8cdb33-748d-3f71-9bb8-b89fa6d3a47d | -2.8842 | -45.27832 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29cd3372-a772-3a7c-a458-b89087526945 | -7.4091 | -40.06312 | 2025-11-23 04:25:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 698ddfc3-d584-3f9f-9a96-22f664206a60 | -2.96183 | -45.43506 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee8b8065-ff5f-31fe-be0c-2f63065a8c6e | -4.80438 | -45.61585 | 2025-11-23 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bf4ecbda-1730-38dc-84cd-5737b4ccd769 | -4.71207 | -46.46294 | 2025-11-23 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c65e612a-3735-3dcc-92ec-82842b4beaaf | -4.75612 | -47.51862 | 2025-11-23 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20c14089-109e-3f9b-939e-a6829eb2d392 | -3.05223 | -45.66018 | 2025-11-23 04:25:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2e0c98f-e844-317a-90f0-3fafa3cc2336 | -2.87 | -45.45535 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 56150554-8e79-32f8-8711-a7a936ce3aae | -6.38521 | -39.67923 | 2025-11-23 04:25:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5e5d4777-7db1-3972-89ce-c6cc7668f2e8 | -2.95799 | -45.43798 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| acc46bf4-2f16-3b74-a206-83b0d6850990 | -2.38958 | -45.78469 | 2025-11-23 04:25:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5865c52a-1066-3dc2-b3d1-67ca8b36cc52 | -6.41263 | -39.79918 | 2025-11-23 04:25:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c2d8aa2c-9abf-3230-a5f3-a78278f458e5 | -4.55817 | -45.49213 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2a6cc8c-e85c-31f1-973f-59753dc7961a | -2.8875 | -45.27884 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bbf3a424-08d5-3979-a59e-c60dd6f98af6 | -2.88973 | -45.28621 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| bed2a25e-102c-31b5-b4e0-14e34b1c635b | -4.04203 | -42.51604 | 2025-11-23 04:25:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7030b79f-a126-38c1-ab05-5e5285ccb1d2 | -4.55487 | -45.49162 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3b00ae9-58fe-32c2-a887-714558ce5de4 | -4.60168 | -43.28464 | 2025-11-23 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b590d731-b2d7-398f-a956-5d6e4c93ba4b | -5.59807 | -47.23184 | 2025-11-23 04:25:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56ca1eab-db1d-3f7c-9343-aba350653f6a | -5.75884 | -46.38496 | 2025-11-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7c5f8b2-2328-38c9-8e4d-e33a7aa81982 | -5.14367 | -47.47142 | 2025-11-23 04:25:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b474142a-629c-3561-91fa-8e3df7fa0fa8 | -2.8908 | -45.27934 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 18d01dd9-5ae9-3519-a7fc-1b3fd2044ece | -3.9228 | -45.89986 | 2025-11-23 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f35fd2d1-5f55-37cd-bbbf-671bbb57e0f8 | -2.95193 | -45.43353 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 593c8ad7-1bff-3f6b-b924-31d1816ebe67 | -3.97071 | -43.28753 | 2025-11-23 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 630efaf2-8e2f-32f1-b9e9-5291941c8b17 | -2.88366 | -45.28175 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| b226f79c-a424-3a50-9919-f2aaf6b726f3 | -7.41289 | -40.06807 | 2025-11-23 04:25:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| e3f4e910-6797-3d51-96b5-ccc988d8e710 | -2.88696 | -45.28226 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 27843238-aa50-3aa4-be64-2b995972f583 | -4.71925 | -46.4605 | 2025-11-23 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| b95d4411-da6d-3a03-93cd-3487d8d7d22a | -2.89026 | -45.28278 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| a5165fee-28d6-3af5-bf9e-0c056630e5fa | -4.57018 | -45.45868 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc2852a4-52bf-3dd4-b2df-5c9dcf39e8a4 | -9.554 | -47.77264 | 2025-11-23 04:25:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fada3799-8dc1-3bfc-b1f6-30cef3952c24 | -2.95523 | -45.43404 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 191b85f2-9be7-3879-b046-7699c88ea0c3 | -3.69819 | -47.67887 | 2025-11-23 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 396e0c8d-2803-3f38-a506-c16db58e060a | -2.87982 | -45.28468 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 9f9d6da6-3a6b-3970-8d05-4a8dbdc8d7d5 | -2.28751 | -50.43753 | 2025-11-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a40f76e8-19b7-3b0e-bdb4-05de70eb8e55 | -2.73367 | -45.21621 | 2025-11-23 04:25:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62ab60e8-dd12-31d6-9092-f096afe08e10 | -5.41999 | -46.13627 | 2025-11-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9795b6b-4fde-32c4-b3f3-9402f7b4877d | -4.14385 | -46.76683 | 2025-11-23 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 673591e9-7efb-33d0-8fe2-e81fb8bb90fb | -3.29511 | -45.73734 | 2025-11-23 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aac8e38-3d5c-337f-bddc-9bd43f2be0ae | -3.86804 | -40.63997 | 2025-11-23 04:25:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e752fe12-f911-3953-800d-7fb4638037c1 | -6.93703 | -39.22746 | 2025-11-23 04:25:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cf5f16c5-9376-3f0c-a946-f7dc9d682239 | -4.95355 | -40.90959 | 2025-11-23 04:25:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0dc023a2-1c95-3588-9978-25e857125ed3 | -4.4619 | -44.10495 | 2025-11-23 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6793b7f3-c26b-3544-b235-fcdf9d8924f0 | -2.89134 | -45.27591 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9f08097a-89f7-3614-a8fc-93362a0354ec | -2.80869 | -45.23838 | 2025-11-23 04:25:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64bbc546-f5bf-39c6-9b9c-6a45843cf2ea | -6.11335 | -45.83621 | 2025-11-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f5769cd-d71f-3efe-92dc-9129e727b0d7 | -3.01232 | -44.43352 | 2025-11-23 04:25:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c26b570-8790-3ba5-bc64-72b3208bf531 | -2.72109 | -45.86163 | 2025-11-23 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6507fd1-ca69-3b5c-9e63-a6a6dcb64535 | -6.31593 | -43.81986 | 2025-11-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ceab083-0c9b-377b-9f1d-03ad33063e1a | -3.40735 | -45.10714 | 2025-11-23 04:25:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e61fc73-9a23-3188-9d83-9d318a3176ea | -2.96129 | -45.4385 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbdd37aa-8270-3a4c-b5b0-714aad146ee6 | -2.46988 | -45.42401 | 2025-11-23 04:25:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e16bfa46-434c-379d-8b10-46895b790fa9 | -2.87375 | -45.28022 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ceaec52-4fd0-3d29-9e22-94414377afc8 | -3.86101 | -51.13953 | 2025-11-23 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5f9f801-b9ce-35d9-8079-9842a3914832 | -4.34323 | -45.5857 | 2025-11-23 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4934ebba-a4b9-333d-bd8d-91f26a49457f | -4.58757 | -39.97246 | 2025-11-23 04:25:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c9551853-ec62-358e-bbe4-0de2f06ff293 | -4.36997 | -44.84526 | 2025-11-23 04:25:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33ed4ce0-c703-3ab0-85eb-94d9c8e151bf | -6.73351 | -46.52568 | 2025-11-23 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d753a729-2d8f-341b-a14a-1c4d93175443 | -2.8941 | -45.27985 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 13a74d21-325e-3000-afbf-a03e36b5dafa | -2.87874 | -45.13666 | 2025-11-23 04:25:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c7bd08c-826d-3679-ab6d-6de7dec48648 | -2.88589 | -45.28913 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33e68065-f04a-3815-8eba-8e8f1d09c97e | -4.83321 | -44.06773 | 2025-11-23 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e2deffbf-eeae-30e7-a277-8c7ffcb17da2 | -3.94108 | -46.97016 | 2025-11-23 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1013ef40-e6bd-3b7b-b9e8-cebebf70db8f | -3.45914 | -40.53255 | 2025-11-23 04:25:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ef1ef3eb-328f-301b-ae42-5ca30c702742 | -2.87107 | -45.44849 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 8e672694-6bc2-3a54-9336-6a335f99ba0f | -6.1095 | -45.83915 | 2025-11-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05a48c94-7ce9-33d8-a543-f88039c5844a | -6.03911 | -45.83166 | 2025-11-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6388ffed-8c22-3290-8fc0-75e0cae407cc | -5.43599 | -40.59397 | 2025-11-23 04:25:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bf016a3a-74a3-3d50-a109-5fea39402526 | -1.67151 | -52.04868 | 2025-11-23 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93b41571-ab4e-381c-b1ce-fc6269e2bf31 | -2.7012 | -49.51664 | 2025-11-23 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94e01a2d-2c53-3606-a43e-ba19c401c992 | -4.5548 | -48.48722 | 2025-11-23 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9e1f82c-3d35-3162-86dd-70cf0f0af168 | -4.04796 | -42.52543 | 2025-11-23 04:25:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f09cd48c-e613-3a6c-a578-f2322f5df07d | -1.67228 | -52.04401 | 2025-11-23 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87fa7dad-3c85-3c38-b526-672682bfce27 | -2.87652 | -45.28416 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4aaced8-1936-3348-85a8-eb8d87494dbe | -2.6428 | -47.38231 | 2025-11-23 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2da953c4-085d-386c-b3db-f5180f67bf61 | -2.44241 | -49.09342 | 2025-11-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84ffb7fd-78ca-3037-81b5-d60489d34de3 | -4.0486 | -42.5213 | 2025-11-23 04:25:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |


[Clique aqui para ver as próximas entradas](README6.md)
