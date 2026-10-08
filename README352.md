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

## Dados Diários - Página 352

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f41c5ec2-dbf6-3379-851f-268d0cf2a61e | -6.51333 | -55.40603 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b4ed0194-3433-3956-ac2f-5dd131d4f9b0 | -6.24403 | -52.68287 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b3fd9d85-1f12-3c6a-aa2f-b797ade05637 | -1.28046 | -56.00377 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 46fd5e44-e055-3904-aa16-40270fa9e456 | -5.05678 | -45.13039 | 2026-10-08 16:39:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e5cb0aa3-5ca1-3866-a520-73368e40dbb7 | -5.38625 | -45.92433 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2f101352-30be-325e-b2a3-164db25d0a7b | -3.01409 | -54.05529 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 2d054d85-0813-3f11-9ba7-31d9673d3517 | -4.07292 | -51.03485 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4ba143b6-94e5-3138-92ed-1d78638f0c4d | -2.57025 | -56.17729 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 80299f02-a831-3766-bf97-d5cb1152e8cb | -5.43246 | -42.64992 | 2026-10-08 16:39:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9ceb952c-0ca0-351c-935a-a23689fb075b | -3.5116 | -59.32539 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 982bc15c-51f9-3d78-a1cd-2d10d4359bcb | -4.66437 | -56.21895 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 67ddf91d-a4c6-3b53-877f-13aaa3217edf | -0.84584 | -48.59904 | 2026-10-08 16:39:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 763682d7-7b13-329c-b1ff-7eb738361d26 | -2.09931 | -54.84042 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 993ec316-d5a5-32f0-be73-d0814af6278f | -3.46601 | -39.49232 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e16de717-9d91-3498-91ca-837eef29ac6c | -3.44431 | -56.93737 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7d3b843f-a70f-3715-8bd5-9208d2a0bc4d | -1.85562 | -57.04519 | 2026-10-08 16:39:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| b66c2147-9014-3a7d-ba24-cd069869d8df | -2.58745 | -56.14297 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 43b40e8a-6fde-39f3-be4d-b7736318e2a3 | -5.28212 | -42.7385 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 6cc50e1c-5f9d-32c3-bb48-3721cbc6b010 | -3.45265 | -59.5561 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 4423e90c-d33d-3188-83ea-21208e800492 | -6.18158 | -53.435 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| a0a38900-5ae9-3c4e-b562-d052f8735a6f | -5.48536 | -45.2243 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 28d6f5f6-e00a-3f2c-a649-055fad258e25 | -4.76872 | -42.6681 | 2026-10-08 16:39:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7342b6bf-1493-3811-a26a-85e7f71acdcf | -6.45081 | -55.03655 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 82a690fc-da73-3be9-bf60-7b8e509b5dae | -5.47943 | -44.60932 | 2026-10-08 16:39:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 868fbcc5-a9b0-37ce-9b87-ab78ed4eae76 | -2.73573 | -44.32515 | 2026-10-08 16:39:00 | NOAA-20 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 92614ec7-c3dd-3656-a700-05ff07428c7a | -5.09065 | -46.2109 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 08fead55-544c-3e4b-966c-3ac02c5d0a1d | -0.40459 | -51.72511 | 2026-10-08 16:39:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4802ed5c-71d4-36d9-8a63-817bd70f1b85 | -5.27409 | -55.95628 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| cc38aedd-ed20-34ec-8c56-95f2129bce72 | -4.73559 | -55.65468 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 6145afcc-c845-3f13-a80c-b0fda09d0e76 | -1.84164 | -44.95924 | 2026-10-08 16:39:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7cffcfff-516c-3690-98c7-ade316cb052c | -5.37648 | -44.19293 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 73fae0ef-a7eb-34dc-9a21-9f93b22ee028 | -5.17594 | -48.96319 | 2026-10-08 16:39:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ccf43781-6dde-3c72-8608-0d0648735c54 | -3.23429 | -57.83832 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| af7a1ba3-c989-3682-8db0-9483e5d7b5a9 | -2.95077 | -45.38295 | 2026-10-08 16:39:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a4d6d4be-b060-3fb2-ac36-b8795dfd8277 | -4.27951 | -39.17928 | 2026-10-08 16:39:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 306faf8b-bcf6-3059-9e2b-35b40d9f15dc | -3.29632 | -53.69842 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 2f23867f-5e8d-31a8-8c1d-e1aeee150a20 | -3.17402 | -50.59074 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| cbfd51b2-cb93-3715-be0b-87d55b6832f0 | -4.69368 | -56.22333 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 03cc2776-7cd3-3aa9-9945-c109a57deb65 | -3.07317 | -53.95718 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 8501f18a-9296-335a-9688-0de15da5fe31 | -4.31902 | -41.2389 | 2026-10-08 16:39:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| b0f2ba71-419d-3c1f-a664-b8c9621e7958 | -3.58463 | -49.88599 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 84c8852d-6992-3825-9b4f-7c265078630f | -2.52014 | -56.61232 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8145a366-7464-3463-949b-5334cede5ff1 | -2.73624 | -54.12238 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 197.5 |
| 7d842fbe-c836-35df-adcf-c933993e8f4c | -3.21367 | -57.87159 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1432ac3e-8252-3a7b-99e7-63f4ce3d2081 | -3.28277 | -45.15449 | 2026-10-08 16:39:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b0d2d09e-07b7-32e8-b3b1-462f0855931e | -2.84181 | -57.47656 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2679ed42-ba50-3386-bea8-b41e53f62241 | -1.83218 | -56.16488 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e26e0f10-cd8a-38ea-933b-6d9df4614769 | -5.70073 | -53.45824 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a19e383f-87c7-3ab0-b523-345a4c99ec90 | -1.00151 | -47.7734 | 2026-10-08 16:39:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 02dc2c19-7e8a-3221-9626-0147fb473a64 | -5.70548 | -53.45772 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 50d5f48d-281a-31a7-9309-9fc43b3c5a70 | -7.31324 | -55.0065 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f1b9e63e-45b4-3f6d-a125-2a51e0426c04 | -5.78147 | -45.38198 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 3c4f4cd0-6211-33c0-932f-ee56136f5438 | -3.53019 | -59.55179 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 8276d331-75ce-34f9-b956-f950706f4acb | -3.38591 | -59.42855 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 95da66e9-d52c-344f-8973-225d060ef06a | -5.74088 | -53.46064 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 59093a4d-fb70-319a-9959-978ae8fcae6b | -5.43685 | -45.6795 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e4d69a46-b245-3858-804e-4d3dbbfb8c4e | -2.86985 | -54.16767 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 665477c5-f7cd-3b56-a18f-a2d5e63fb642 | -6.22741 | -52.79282 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| eec5a597-9b15-39d0-a9de-8ea71dd5de6c | -6.73164 | -55.06131 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6b29b009-3c31-3901-b6d0-5c4f1f54a0ad | -2.9958 | -53.85407 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| bea0cc53-59c4-30fc-b5cb-00fa139cc357 | -5.26603 | -45.40705 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5db29afd-6121-3be3-9058-6b0461306229 | -2.16526 | -54.46217 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 1dff01df-cfe7-302b-bc29-d5126d1065c6 | -6.85185 | -59.29594 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7b67f64c-78b4-3130-be52-79110fcc404f | -2.85241 | -57.46626 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ad24486d-a6b3-39b0-bf26-c33506654ef4 | -2.86516 | -60.2557 | 2026-10-08 16:39:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 6752b6d6-ceaf-3d81-a98d-a1e709082003 | -1.60448 | -55.15939 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 63c90411-0da5-3484-8960-8ced3a8b96e0 | -5.3748 | -44.20462 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 1dffe226-95eb-3012-855c-166d482ac5da | -3.10892 | -52.37931 | 2026-10-08 16:39:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 73776355-6e2c-3aba-a845-abab2fefe97f | -7.23055 | -55.12883 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 44fdf4f7-e041-38c7-9473-ba7299d3fb26 | -3.5237 | -44.31097 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2f001522-9665-3bf0-a4ba-ee53cce6c9cc | -4.74075 | -54.60569 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 2d90df43-5d6b-3980-ad38-7d183bf6530a | -5.34993 | -45.7318 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3237765b-db00-377a-8509-24b1ab0d10d0 | -3.46757 | -39.53175 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 25022703-161a-31ac-9511-c8c8254471d7 | -3.91739 | -59.10595 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 41c0efe2-06bc-3a81-b9bc-05e3321b69f2 | -6.24309 | -52.83765 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 58cbaf0d-0075-3208-8e3c-bfebf32a5b87 | -5.3046 | -45.72492 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f3af72f7-18b2-34b7-9649-af029bbae6de | -5.28194 | -45.73192 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 686d22c9-5507-33b8-af1b-0e2e72753884 | -4.09127 | -44.12598 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| d69f9cda-864f-3398-9b01-a5a2a31b6314 | -5.51335 | -42.85213 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| ba3ee0f6-9b68-364e-98ae-d376ca85edc5 | -1.54479 | -52.75735 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f7f7d124-a9bb-35cc-ba25-d78e4caee0f7 | -2.39689 | -57.89465 | 2026-10-08 16:39:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3b824d76-b9d7-375d-9622-e81bd1b76662 | -3.31228 | -49.69151 | 2026-10-08 16:39:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09d1bf5f-6348-3101-ae71-0f759688737c | -6.80803 | -55.29795 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 509bfff0-f07c-3eb0-9638-6c140ddb14bc | -3.94748 | -40.71931 | 2026-10-08 16:39:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b25920fd-241f-325b-a27e-dcc74f302cc2 | -5.70291 | -53.47337 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 169.4 |
| b7655e81-0315-3f42-93be-4692b9c2436a | -6.85595 | -59.39551 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 2b23fbe9-6c56-307c-b9e3-21bb6c7cbefe | -2.50275 | -56.63768 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 07df85e3-d4b5-35ab-86fb-abce7f2d5a8b | -6.10906 | -53.50985 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 03a1826c-a4fd-3a19-925c-eabfff113f21 | -3.08656 | -53.95041 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| cfd61dbb-9f7c-3e53-81a9-9fe53a350de2 | -0.09079 | -49.48061 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| f286e852-8aa3-3659-83cc-e98897aec352 | -6.24554 | -51.44213 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 1f6af7d3-4bc7-3aa1-a329-fe201c468c89 | -5.42505 | -45.71322 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47781c7c-1286-3fb2-9621-3d751efa9010 | -3.00601 | -54.09774 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 32da941a-f512-3b53-9a67-8d3236afa8a2 | -2.21857 | -56.9228 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 07bd61c3-0ac4-3582-b1b2-78610c26ed8d | -2.95348 | -43.51688 | 2026-10-08 16:39:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 843150da-83fa-36d4-b6bf-312ba1a12a20 | -2.37668 | -45.70928 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 41e51d04-3ec3-36c8-baa3-df19a25f90f8 | -3.45618 | -43.7648 | 2026-10-08 16:39:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e01ec08c-93af-3c7e-8e6a-26752bd5f13b | -3.45922 | -59.98586 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3d59a076-d706-3b17-b4d2-c96ccca15f45 | -4.91647 | -46.02746 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 691dd775-2a81-3485-889f-7b6d7950f8ed | -2.46837 | -56.06206 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |


[Clique aqui para ver as próximas entradas](README353.md)
