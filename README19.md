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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d58b17e3-5770-3b97-aecc-535c25bc11ac | -6.15551 | -41.69189 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 35f0051c-248b-3d2b-8dce-a568c392fa94 | -2.74896 | -45.41256 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 138bf7ad-297c-3ea1-943b-0d5a799b47a9 | -3.58044 | -43.60202 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdde5aa4-6495-3b54-864d-0445d345fbfd | -5.57944 | -45.34258 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6fa1e59-d4d7-3253-8818-0a5226c4d115 | -6.16859 | -41.58458 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 07567d9c-3d14-3bc2-bcb7-30b63ca1ad1e | -3.58992 | -43.62891 | 2025-10-28 04:12:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dc24a121-820a-3501-bd28-f83d73dcae2f | -3.41575 | -41.33043 | 2025-10-28 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0bbb889b-c124-3b6e-a5cb-d27e25a745d2 | -4.96654 | -47.59091 | 2025-10-28 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e68a7b9e-bd51-320e-acb4-3458ec3bb9f8 | -2.75753 | -45.40529 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 90c10735-724f-3e74-9b02-26039dc04d5d | -6.11443 | -41.73656 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 120a5a94-c945-34f6-9fd2-eada6d908740 | -4.69202 | -46.44876 | 2025-10-28 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb9a60ff-444c-3c07-97b9-2c89d227e75e | -3.93402 | -42.50294 | 2025-10-28 04:12:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 293470ed-c2ad-3bd1-993a-9648671cb7eb | -5.04133 | -41.94662 | 2025-10-28 04:12:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cc9ee756-bed4-3f3d-81bf-687551a075cc | -6.09684 | -41.78434 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f506a24-35ca-3500-a586-7db508962dd6 | -3.44573 | -42.50986 | 2025-10-28 04:12:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3672eca9-1578-36e3-8bc6-58bc4f01d857 | -4.86846 | -47.35698 | 2025-10-28 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c427fa4a-3a05-3751-abd4-23fbc2dffec4 | -5.19757 | -46.14802 | 2025-10-28 04:12:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c4962b3-c294-323a-bcac-4f8f3315818e | -3.58601 | -43.63194 | 2025-10-28 04:12:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 816a2b44-98b7-3409-8d93-a81e1ab30d51 | -5.01744 | -41.04122 | 2025-10-28 04:12:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9e091de4-45ff-37d9-8aa6-2f602be9e08c | -5.80024 | -35.60046 | 2025-10-28 04:12:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4f7dac54-9065-3a68-95ff-e0221be33111 | -3.02297 | -45.37138 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c3f51252-a6c9-3d90-adca-50974e0dfb45 | -4.10178 | -48.02466 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3852bb4f-9a48-35e3-866e-e7b10ad234bb | -3.12942 | -50.15164 | 2025-10-28 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a7c8ea5-973f-3088-9b08-abda8fac6ef6 | -3.5748 | -49.01982 | 2025-10-28 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a794521a-6e74-3552-ba6f-c7e3e2c83faa | -3.58936 | -43.6107 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a02fead4-a129-31d1-8457-acdbe7760b26 | -4.46671 | -43.70202 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb764e1e-96f3-328d-973e-da5d8771d7df | -3.89748 | -45.17079 | 2025-10-28 04:12:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8f83bc3-5778-32fb-b317-4a47e5dd43be | -5.81269 | -40.81544 | 2025-10-28 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7ee75028-0b92-312c-bc44-47fbcd9dd648 | -3.60776 | -43.55917 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbab5814-e2b3-388f-b2c1-047fa4dd8202 | -5.16873 | -45.41223 | 2025-10-28 04:12:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3d100bac-97e6-3db6-899c-e1d43bbc8beb | -5.54937 | -43.13538 | 2025-10-28 04:12:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c80b3ccc-15ef-38bc-8f41-a091ae60820d | -4.24904 | -48.3757 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4883c4c5-d9a8-39db-8f7e-5a0905481e3f | -3.91747 | -43.32061 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca2aea75-9e9d-3331-8b85-ad070919e10f | -3.02657 | -45.37194 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 64909a7b-d37c-336b-90b3-3d0f83b49339 | -6.10668 | -41.74248 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 085825a8-1c24-3c7f-b2b9-394b76483e50 | -5.13608 | -44.97856 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aae37c90-96ca-3e47-b7e7-ae8f9f8fdfa0 | -3.40332 | -50.27521 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c157ae2-cf5b-345d-8617-4ace5ae2a1f0 | -4.46587 | -43.23279 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a7e1eff-db16-30d9-a9bf-f525374d0b8c | -3.03017 | -45.37249 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| fe90f90f-da35-397e-9abf-75344050fdb4 | -5.04378 | -45.1327 | 2025-10-28 04:12:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4ce446a0-c3ca-3d09-9201-93ecb5dee00f | -6.17475 | -41.58915 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6015314d-8c50-3e09-a9cd-5214ef5c1258 | -5.59535 | -41.3138 | 2025-10-28 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b84dffa1-a318-3d95-a384-2bf84cb07a8d | -3.70821 | -41.57162 | 2025-10-28 04:12:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e84c1af8-61ed-3797-9df6-611f61abb575 | -3.58155 | -43.61673 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cb6a064-c06d-3425-b92c-81278a4d9752 | -4.68771 | -48.26804 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2415d21-bcdd-3ff4-a38e-16f01f2678b9 | -3.65205 | -49.9253 | 2025-10-28 04:12:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b5ed065-6144-32a2-b855-4f7b5ccb6e38 | -3.8617 | -43.35112 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2a0fc4b-d12c-3f6d-8f90-bd64291c4494 | -5.65955 | -41.10936 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6f443007-bca8-3ed9-9a1c-544d4cc321fe | -3.21213 | -48.95441 | 2025-10-28 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 024dd841-c89c-3e5e-b897-4f8755434a54 | -4.45447 | -43.64952 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49cac688-4472-359e-b39f-c35a09a04aed | -4.87125 | -48.52549 | 2025-10-28 04:12:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfbf183d-6fef-3c1d-ac5e-fb6f9b27acd3 | -4.45836 | -43.64651 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc8dbd95-c40d-3860-b1b2-cfa247e61ab2 | -6.13441 | -41.71782 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9a7d3af4-9383-3683-8b23-770da1e64b18 | -3.17802 | -52.49705 | 2025-10-28 04:12:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0181231a-d5b1-3ec7-884c-5c55bdd64f4d | -2.64642 | -48.50887 | 2025-10-28 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bddd7e63-09d6-38ec-be53-7e521433e14b | -5.80576 | -40.81483 | 2025-10-28 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e25f14cb-294b-32f8-ad02-563af785599f | -3.24048 | -48.77598 | 2025-10-28 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0621c4db-6d4c-38b4-a913-2aaa45eab8ad | -6.21153 | -41.52893 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6d81ac0b-a876-3e76-9f19-1086b7b19a41 | -4.87784 | -47.54468 | 2025-10-28 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e50bad1-1346-3433-8e7f-136643e92b99 | -4.19501 | -43.17921 | 2025-10-28 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 580077b9-6e64-3930-b488-f55748cc43a3 | -3.70767 | -41.57509 | 2025-10-28 04:12:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3860c159-392d-3319-b86c-4d58981d9e83 | -5.43363 | -40.90722 | 2025-10-28 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e62b5b1f-a90c-313b-97db-bcbab3db4e6c | -3.57031 | -49.01908 | 2025-10-28 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef39bb86-ac32-36de-b409-6ba8c0cc005b | -3.94824 | -48.09098 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0755b0dc-7737-35e1-abc3-8edf456ac413 | -4.36217 | -50.51307 | 2025-10-28 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f535f3c-6917-3095-a34f-16cc1f50391e | -4.52505 | -47.6303 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 085f758f-19f1-3860-ba94-0f176488f74c | -6.18475 | -41.5688 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 04bd766e-8c16-338d-8dc6-ca2c0841579f | -3.91415 | -43.3201 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cc7b84c-6ce9-3fd0-9c47-5cc0800358d1 | -5.84719 | -42.47306 | 2025-10-28 04:12:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cfeb986d-6081-31ac-b5d4-295087fc442d | -4.90256 | -47.41982 | 2025-10-28 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d6b2225-8a42-35b6-90f0-aca976cc1bfa | -3.69377 | -43.20714 | 2025-10-28 04:12:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9969c0b-085f-395f-b225-1bc23c30635e | -5.64296 | -41.09553 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6aca65a3-56fe-33bf-bce3-68a2081f2145 | -3.08508 | -44.44426 | 2025-10-28 04:12:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eaa25100-69ab-3de1-b11b-3bc8562b0725 | -1.14119 | -48.09579 | 2025-10-28 04:12:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8ef40eda-f11d-3c7a-9cb9-06c9ba71c739 | -6.15769 | -41.67772 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 72103311-4622-34a9-be35-988cad24618f | -3.0259 | -45.37605 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 2703f00b-d822-3683-8b15-2663d8c92143 | -5.84665 | -42.47651 | 2025-10-28 04:12:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fef79e0d-8cc9-36c6-af57-af5179991800 | -3.04822 | -53.02054 | 2025-10-28 04:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e66c8f43-a173-3ccd-86d5-0681b6678e24 | -3.71166 | -47.64579 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 09f45c09-68ba-3740-9ca3-876f5c639ae4 | -4.9178 | -42.99632 | 2025-10-28 04:12:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf959dac-be2e-3257-9f35-f3f459a5ee65 | -3.58992 | -43.60715 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64b8e547-4a35-3920-8172-f8a8bb6a7949 | -5.0332 | -47.166 | 2025-10-28 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4bd1306-4c5a-3167-b7ae-8302afe6a211 | -3.57151 | -43.61518 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4bfd1f8-d2f1-353d-ab82-2015a1fb167c | -6.17448 | -41.70206 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2a6a8ff8-4e55-36ab-9bb5-74bec1dd4406 | -4.45924 | -43.23176 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| b5c376c9-605c-3984-8894-84f5f793f3c9 | -6.1138 | -41.71833 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e7c439ca-e260-38d7-8c8a-cd83194c16a0 | -5.86551 | -43.20314 | 2025-10-28 04:12:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9f021998-1666-30d1-b4a5-e018ba298325 | -2.75258 | -45.41312 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0534aa53-402e-3291-af22-40dfda446a8a | -3.47268 | -49.96759 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ffa6a58-3bea-3683-8bd4-242efa3ae0a8 | -5.26016 | -42.48677 | 2025-10-28 04:12:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| de28a8f6-abf9-362d-98e0-b1620eecd6e8 | -3.44377 | -41.84864 | 2025-10-28 04:12:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1cde23cb-4e96-3e61-9d62-2cc76e1f7a24 | -5.63958 | -41.09499 | 2025-10-28 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d2ca8bf-5156-3155-a2eb-abef51eabedf | -5.80634 | -40.81109 | 2025-10-28 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| add2708b-6cd0-3900-b0f4-ffaf6a65be64 | -3.707 | -47.64871 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 33d35a10-46af-3a57-aaff-7d3447453e5e | -5.58294 | -45.34312 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| feabdd5e-065f-316e-9252-4d722f9fc69f | -5.41098 | -46.33537 | 2025-10-28 04:12:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 423a79d4-049e-371c-bbd1-91014118feee | -4.22068 | -43.9253 | 2025-10-28 04:12:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12344450-012d-3ded-9d7b-caefe933a227 | -3.71225 | -47.64213 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59f7ec0c-8ea0-3245-b42f-c4e1997d5d94 | -9.89111 | -44.90832 | 2025-10-28 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4356c94d-139e-3c2a-ab1b-dba60174767e | -7.30982 | -42.47581 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README20.md)
