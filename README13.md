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
| ccfa8699-31f4-3109-8840-338d9441930a | -4.65135 | -44.1272 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9cd7d04-c381-30f1-872f-0563d45f6953 | -5.37586 | -36.85363 | 2025-10-16 03:25:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db82f625-7443-340c-b944-002f5f82e451 | -5.43368 | -40.98682 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d1022e62-33f8-36a4-b61d-1dcf36331504 | -4.66263 | -44.10012 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| fdb5cc42-0510-3375-a799-b82199b23f0e | -5.4517 | -41.02308 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 74e585bb-4153-3350-b00a-0465e7e8131a | -6.37531 | -41.48287 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 7f174fab-ae10-3235-b94f-075aa737d8b8 | -5.44813 | -41.0087 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52beb161-5b97-3d9b-b5a4-269042d6b41c | -4.36529 | -43.41018 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e4a2fb2d-e3d2-3dc7-bc2e-c32dc58109e6 | -4.3688 | -43.39073 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 477d2997-b708-309d-8a37-6c8b3c29557d | -5.45759 | -41.02437 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ca35978-4436-3e94-bf34-5a576a3a0c84 | -4.36254 | -43.39842 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| eb397be5-ed78-3125-8aa5-d0205e863080 | -4.77614 | -43.92919 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 585b1304-f2e6-3e9a-aa68-54b8de691d0b | -5.40337 | -41.15597 | 2025-10-16 03:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fa443bbd-c1db-328e-a249-27639d121e50 | -5.87759 | -43.85275 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abef1a46-e6e0-3e00-b92f-3abb9586b6c3 | -4.36371 | -43.39173 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 66475aee-e19c-39eb-bed7-e9ea20a256b5 | -6.36987 | -41.48352 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 930e60a4-4789-3a00-af34-26934dd00de0 | -4.66985 | -44.10771 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 8563d1cc-80f9-3eff-a3da-f6ad9e4fa4cd | -6.0996 | -40.88831 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 058a3a9c-6757-3a57-bd36-260707e26839 | -6.12964 | -41.7616 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 47de6f40-c5ac-3daa-b3b8-52f7cf10594e | -7.18993 | -42.36651 | 2025-10-16 03:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f074cc7-df16-34d7-8476-a09927a994f3 | -4.37123 | -43.37722 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 73f23fb0-793f-3711-bf16-7fdca1ee268b | -7.39819 | -39.70012 | 2025-10-16 03:25:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 13209f47-8d81-37c2-a463-6f1b50ad5542 | -4.36031 | -43.41125 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1bed73c-e6f2-3bfe-a261-525ec1cccf55 | -6.13892 | -41.75372 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2010d1b7-cb8e-31a3-9c56-0bd807fa8ed5 | -6.41583 | -39.60091 | 2025-10-16 03:25:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0caa68c9-c7f0-356b-b0b1-96733545ebc2 | -6.38885 | -41.48183 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 017380b1-df4f-3a54-9b81-1bd586420697 | -7.30071 | -41.9638 | 2025-10-16 03:25:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c98c703f-1b40-3afe-aebf-53e14cafe403 | -4.36642 | -43.4039 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a5d55f34-0947-3041-aa1d-5db0bc4991b9 | -5.06751 | -40.47351 | 2025-10-16 03:25:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 093bd1ab-5e0a-38d1-9991-86e3c6a0dfb1 | -4.38635 | -43.37303 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23447f5e-7ef4-3c33-9d92-be49f72b0d11 | -6.16291 | -40.90413 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 358ee7e7-97ca-3e32-9c1c-ebef1657c68f | -5.87074 | -43.85065 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7e9e5c2-1abf-3a86-aa9a-da9700662087 | -4.65673 | -44.09791 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 78983a37-96e3-3791-aaa6-6281615d9d83 | -4.55803 | -44.00783 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a6a3a7b-397c-3edf-88ff-722b21a3b369 | -6.38819 | -41.48035 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9e1cc622-b206-39da-b180-b9a08444056e | -5.56956 | -41.31676 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 29a427d9-0c6e-3861-9737-3b828849cbe7 | -7.28324 | -41.95581 | 2025-10-16 03:25:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1f188e12-0d1d-34ab-9cf6-890bfda94455 | -5.60122 | -44.26566 | 2025-10-16 03:25:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07a7e51f-1552-35be-855e-c1017a6a76cc | -6.56468 | -42.97494 | 2025-10-16 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 347f3cbb-760b-3af2-8e7d-d70ea540078e | -4.39088 | -43.3878 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8b803a8-b4ab-3f89-8eeb-96d3f3acc37c | -5.85663 | -42.88316 | 2025-10-16 03:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e2818e0f-fc77-345b-9ec6-e238168a477a | -7.47176 | -41.51878 | 2025-10-16 03:25:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9ad62280-17ac-3708-80dd-89a3239f9e46 | -4.67383 | -44.08585 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fa547a21-ba8d-3d6c-870e-f9b370ba72c0 | -4.37229 | -43.41125 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4454d9b2-bc80-3bd9-abf3-80a333306ddb | -6.36849 | -41.48626 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4f3e9911-3396-311f-bfb1-9171fff3790f | -5.38706 | -42.80202 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e1ce4433-9edd-30b5-b5c3-48a47d19235d | -6.03852 | -41.92236 | 2025-10-16 03:25:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ff6208df-3734-3035-af69-bbbab6421a54 | -5.06138 | -40.47243 | 2025-10-16 03:25:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 274b91dd-1468-3caa-8abf-af122b7620d1 | -5.45092 | -41.02747 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 56ed3599-43ef-3878-a65b-e064170e45f6 | -4.37064 | -43.39316 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 43ab86e3-c4a7-332c-be86-dddd6335fba2 | -4.35922 | -43.41751 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d47b0a5-3852-3d9c-a4eb-650e4b6699aa | -6.5681 | -42.96974 | 2025-10-16 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 596c4f56-697b-36c5-af70-3a01ae329afc | -5.06174 | -40.47247 | 2025-10-16 03:25:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5f41d8ac-d4f2-3501-bdfa-8ad7e4d90f14 | -4.37925 | -43.41257 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8d39e2f2-62c9-320b-8426-d9753ab1949d | -7.39174 | -39.7057 | 2025-10-16 03:25:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1b0cd876-ff9b-30ab-8ebc-6d6075ee2e80 | -4.38277 | -43.393 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b3b9e5f0-cb1b-39ea-baf4-e8eb2e9fe679 | -4.65874 | -44.12222 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01620669-2b02-3d8f-b1c7-5fb81caacc3d | -5.45014 | -41.03188 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 254259cb-acaf-37fb-a9dc-675657acc358 | -5.45682 | -41.02875 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1f462a0a-b5ef-3469-ad8e-224443463936 | -5.47488 | -42.9459 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 97466897-fd10-3c13-98ff-c96c4fc3ab48 | -4.65941 | -44.08325 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1306b46-ad01-3327-ad12-31e409d91cca | -3.84897 | -41.5667 | 2025-10-16 03:25:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| ad970c84-9cf6-3987-bdd1-5a04445b14ca | -5.87956 | -43.86986 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67efb670-529d-3379-85d4-24108090b07d | -5.45246 | -41.01877 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| efba4a65-3813-3d34-b475-bbf02924b677 | -6.44587 | -43.38451 | 2025-10-16 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9f554635-2a31-30a0-a177-10a7ac697e46 | -6.03762 | -41.92731 | 2025-10-16 03:25:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dfc593b9-b1c4-3ca2-9ba0-dd9d6dc88a18 | -7.39702 | -39.70666 | 2025-10-16 03:25:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1597c0c9-7c86-38d8-b878-c5529efba414 | -4.39208 | -43.38113 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c3ea2c4f-3674-30c5-91d0-cb1c2cbe5789 | -5.48366 | -42.93534 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c3a6c0ca-2d91-39d9-8029-6f9feced5bd1 | -5.47039 | -42.9325 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| dd2f3f83-0c27-307d-ad76-f055fc4e48e4 | -6.04919 | -41.93445 | 2025-10-16 03:25:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e2fbd2fd-447a-3cc8-b088-dacbee5378b1 | -6.42824 | -41.88953 | 2025-10-16 03:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8afa5361-7436-34e7-b92b-96dd2cbc6172 | -7.1865 | -42.3675 | 2025-10-16 03:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0a9981c8-7740-3b34-a2b7-ec6438e11306 | -6.90461 | -38.2629 | 2025-10-16 03:25:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e9ba3911-662b-3417-b6e1-293e05de52dd | -7.39409 | -39.69264 | 2025-10-16 03:25:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 10.1 |
| c9a1c246-c256-3d1e-a9eb-a060fd2695b8 | -6.51601 | -42.19392 | 2025-10-16 03:25:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 889b7e4c-e83b-3fe5-893f-6552a01dfabd | -7.17519 | -42.20021 | 2025-10-16 03:25:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 408a671c-7b3f-343c-b247-78867dbdfff1 | -4.66532 | -44.09169 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6537c2a2-e140-3c16-aecc-93545511d0a7 | -6.99033 | -38.44472 | 2025-10-16 03:25:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ee66fb15-8492-3f4e-88d8-3580cba958ee | -6.56573 | -42.96934 | 2025-10-16 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 441a1a06-a0bb-3da8-9811-7d8208ce8a73 | -4.65407 | -44.11238 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32b2c921-597c-34d6-88eb-3c4422ed2734 | -5.79564 | -35.59986 | 2025-10-16 03:25:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 0f9c5d68-7beb-3aa4-988a-b6f9119c4ed8 | -4.78328 | -43.93048 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ac3750d-eba6-3c47-b9b1-b0b79081f542 | -5.87503 | -42.81996 | 2025-10-16 03:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5fee23e9-d486-3dfe-b52f-e9a471907e8f | -6.14994 | -41.78961 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dfd3fdec-a69c-34c8-85dc-6ee0ac071f1a | -6.14544 | -41.77945 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 667a4562-ac7f-3ebe-8247-df10a28fc402 | -4.65154 | -44.12073 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2474fc2c-16bd-3332-bb50-a9fb61a61b29 | -4.66137 | -44.11328 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e141f0f-f28d-324c-a8ec-c3e8c66834c5 | -4.92318 | -41.55745 | 2025-10-16 03:25:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9f12977c-6700-36e0-bee8-5dcc49a30db3 | -5.4227 | -40.97987 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f78d648-b9b3-38cf-8c73-9969d2170a58 | -6.16366 | -40.8999 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6f5e4fbc-e218-3f35-8c25-b6245ef2f37e | -5.53577 | -41.3281 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 03edc478-ab6b-3d7d-8ad6-74614b8444cf | -4.37342 | -43.40497 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 30d4522a-bdaa-3b5e-ad55-0e048bd98018 | -4.39319 | -43.41511 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55ce0ad7-65ba-306b-8f0c-6c99e8a0cccf | -6.16066 | -40.91698 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| bc5c0959-75f5-3190-a7c1-cf1b9d6fffe9 | -5.45603 | -41.0332 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 02ff561d-fc95-3674-a6b1-555aaa2e5cad | -4.658 | -44.08419 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e42ab07-16d6-343b-bc5d-9ff7e1001e23 | -5.47306 | -42.93269 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 82f49ac8-d749-34ca-8a2b-d288bf94bd97 | -6.75278 | -44.38152 | 2025-10-16 03:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d10e6bd-66b9-38f7-ace2-a1bb443fcb8f | -5.86914 | -43.88692 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README14.md)
