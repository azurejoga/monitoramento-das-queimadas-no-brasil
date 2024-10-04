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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69865d8f-63b9-3ce5-b0b3-fbad61dfb693 | -2.90061 | -50.74843 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 756e2ede-7e80-3ac1-9998-1e37d9beb284 | -2.89512 | -50.7109 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2db331d5-4082-31bd-b734-4e6eebb91748 | -2.8944 | -50.71536 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0ed981d8-e8d3-3571-ab20-b78fe36c698d | -2.89383 | -50.74276 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ef3e0e5-bd32-3df1-bf8f-3905f35548b0 | -2.89137 | -50.7103 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8581ed33-7549-394f-8e52-d6a38809225f | -2.88763 | -50.7097 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cce43f88-0afd-34b6-a120-fc5196b79063 | -2.88619 | -50.71864 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9197a0df-9f66-3aaa-bff4-b062e57ebe47 | -2.88461 | -50.70465 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4f6720e-c825-357b-9497-808035ced6a0 | -2.88389 | -50.7091 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50396417-2afc-3fcb-b86d-98c13e10e267 | -2.87943 | -50.71296 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 215a1657-611d-352e-be4c-74c1526a6664 | -2.86529 | -50.72906 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8637c1c6-2a06-367b-837a-6d07f5484fff | -2.863 | -50.71951 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e93539c-2036-347e-a200-70b587c43189 | -2.85551 | -50.71833 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8eec834-d3c3-336d-a94b-9bb71fe7e5a8 | -2.85104 | -50.72219 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7ffdc9d-fea5-3801-8f15-51e6f5cda856 | -2.84995 | -50.72398 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5fa4e0a-88c4-38b8-8e90-6bc4c587a726 | 3.23455 | -51.20723 | 2024-10-04 04:29:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d5980ea-ae82-3c4b-8a6b-2f8e18fc3a91 | 3.23396 | -51.20337 | 2024-10-04 04:29:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c48970f2-24a1-3f17-bdb3-489a9cd4c89a | 3.23034 | -51.20787 | 2024-10-04 04:29:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 15cf64c2-d70c-364c-b82c-a74f5d08a114 | 2.58175 | -50.94505 | 2024-10-04 04:29:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c013f428-59b6-3a72-9c6d-01f31a30c82d | 2.58075 | -50.94552 | 2024-10-04 04:29:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a4c96e1-4c6f-3013-80ec-a1bfa2d418ff | 2.57765 | -50.94568 | 2024-10-04 04:29:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88781adc-69f2-3bca-94ea-7ce8414b11ba | 2.40142 | -51.67749 | 2024-10-04 04:29:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85664682-1924-31f1-8574-863d1341905b | -2.13735 | -53.65243 | 2024-10-04 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24932363-67f7-3587-80a2-03948c97e6bc | -2.0528 | -54.36839 | 2024-10-04 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d237bf83-ef28-33b0-96a6-872af340b69e | -2.05193 | -54.3661 | 2024-10-04 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca393b86-6545-3482-9db6-b4a27f586c4f | -2.048 | -54.36743 | 2024-10-04 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e83e192-49d4-3f97-b018-77238c7b446d | -1.75605 | -54.44668 | 2024-10-04 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41652d82-fe26-3bdf-9f0b-6b888b03051c | -1.04871 | -53.52897 | 2024-10-04 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 233ee931-4599-39e0-9ca7-6b984f23e10c | -1.04407 | -53.52833 | 2024-10-04 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2fbaf01-464c-351d-b75e-6385ac3422f9 | -18.51099 | -41.29126 | 2024-10-04 04:32:00 | AQUA_M-M | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 0a986bb0-4097-3861-b87a-e3f55224975d | -18.50858 | -41.29775 | 2024-10-04 04:32:00 | AQUA_M-M | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| d2fafbd6-bbe3-374c-a912-f1a9361142fd | -17.37915 | -42.61934 | 2024-10-04 04:32:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 55d0e9e6-df95-328c-bccd-8ada7b2c40f5 | -19.3303 | -42.5823 | 2024-10-04 04:32:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.1 |
| fb6dd8b0-a713-3126-b70f-9a09bb70048e | -19.32705 | -42.59991 | 2024-10-04 04:32:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.2 |
| 603b7768-f609-39c1-abdb-5de03a955f06 | -19.31807 | -42.58021 | 2024-10-04 04:32:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.0 |
| 4cea9900-5f9f-37c2-8e71-1accab33b8cd | -19.31491 | -42.59721 | 2024-10-04 04:32:00 | AQUA_M-M | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| 60eebebb-7507-3cc8-aff9-d14915dd6393 | -19.28954 | -42.87191 | 2024-10-04 04:32:00 | AQUA_M-M | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 2a71e0be-2a24-3c82-9c0c-11ec3da83b33 | -19.2771 | -42.86937 | 2024-10-04 04:32:00 | AQUA_M-M | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 91e4c8f7-e556-37c3-9869-8caa84365d54 | -19.03343 | -43.18259 | 2024-10-04 04:32:00 | AQUA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 94c33be8-848f-3a83-926e-9e25db0b6445 | -19.02084 | -43.17882 | 2024-10-04 04:32:00 | AQUA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.5 |
| 29ab427f-9772-3d93-bde3-ab85bcfe054b | -18.91894 | -42.02876 | 2024-10-04 04:32:00 | AQUA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| ff0d1589-c567-3d9b-8322-1aa4f8d6b35e | -18.91412 | -42.0206 | 2024-10-04 04:32:00 | AQUA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| e0480255-7f17-338e-a14a-63c5c8ea180a | -18.84938 | -42.89727 | 2024-10-04 04:32:00 | AQUA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| b516bfba-a5b7-3062-bf35-c40b350d8608 | -18.84813 | -42.89211 | 2024-10-04 04:32:00 | AQUA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 92eac2fe-33d0-3b3a-aad4-ed184f5b9b9a | -18.84451 | -42.91188 | 2024-10-04 04:32:00 | AQUA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| 322451b6-ae60-32fd-8fd4-e61b6f4ad9bc | -18.83385 | -42.9787 | 2024-10-04 04:32:00 | AQUA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 995721ee-571f-391b-b95d-fcc04d7f9152 | -18.83325 | -42.97334 | 2024-10-04 04:32:00 | AQUA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| c8223b2e-d795-3c17-98c0-8ce3fe8b9ebb | -18.43553 | -42.20963 | 2024-10-04 04:32:00 | AQUA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.8 |
| e4b5a3b0-f8c4-32ac-ae9e-156c36372ee4 | -18.43067 | -42.20256 | 2024-10-04 04:32:00 | AQUA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.2 |
| 48cac751-40ba-301e-b4ac-1994ae843602 | -18.42732 | -42.22141 | 2024-10-04 04:32:00 | AQUA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 2dbb5419-6eab-37f7-85a0-01d756ef4395 | -18.42353 | -42.207 | 2024-10-04 04:32:00 | AQUA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 23330f2c-fe3c-35ef-9df2-32db5dad210d | -18.0867 | -42.58034 | 2024-10-04 04:32:00 | AQUA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| fb2f79cf-08aa-353a-aeaa-0b4879322ac6 | -18.08626 | -42.58754 | 2024-10-04 04:32:00 | AQUA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| a551914b-2ab1-3374-912a-a13a86fab7e0 | -18.08324 | -42.59953 | 2024-10-04 04:32:00 | AQUA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| 1a5bee39-471b-3fe6-a7b4-fd97084405f6 | -20.23635 | -43.18173 | 2024-10-04 04:32:00 | AQUA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 3635bea5-9db1-3332-a3a3-e1ef43cdc381 | -20.10044 | -43.41615 | 2024-10-04 04:32:00 | AQUA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.0 |
| 3b7aac47-df1d-3ea6-8c3f-4ec64e84e1c4 | -20.09756 | -43.43127 | 2024-10-04 04:32:00 | AQUA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| fbd1715f-e86a-3b2d-91f6-c7b33f22ab12 | -20.08418 | -43.43188 | 2024-10-04 04:32:00 | AQUA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| e77befb2-bedb-374c-83f9-2ae2447521e0 | -19.85658 | -42.36724 | 2024-10-04 04:32:00 | AQUA_M-M | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.4 |
| 63625567-9f1b-38a1-b35c-6d1579f4c605 | -19.85309 | -42.3865 | 2024-10-04 04:32:00 | AQUA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| d79268ba-b153-35cc-907b-334a9ad62773 | -19.84479 | -42.36454 | 2024-10-04 04:32:00 | AQUA_M-M | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 383.1 |
| 6e32076a-1a80-38b0-a6dd-74442e5b1636 | -19.84128 | -42.38382 | 2024-10-04 04:32:00 | AQUA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| 8b6c1369-4378-38d5-8d90-4bac4c402527 | -19.6899 | -42.92668 | 2024-10-04 04:32:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| c48c1519-dc59-3e6a-9587-07aa61eeb1b0 | -19.56683 | -42.73182 | 2024-10-04 04:32:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| c5abccae-4091-3761-b7cc-ef9a03325249 | -19.50198 | -42.87232 | 2024-10-04 04:32:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.7 |
| a5f2cd94-b5a9-3e47-aa54-ffed6a571f58 | -19.49835 | -42.89137 | 2024-10-04 04:32:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 245.8 |
| 767f99cf-20d2-35d9-a39e-c9abfee63261 | -19.49832 | -42.88347 | 2024-10-04 04:32:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 368.0 |
| f108b7ab-c82a-36d9-839e-b7313d940887 | -19.49448 | -42.9045 | 2024-10-04 04:32:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.2 |
| b5cf2e9b-1140-3e50-beb8-79aeb8e0380d | -17.74998 | -43.79496 | 2024-10-04 04:32:00 | AQUA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 4c2a6e4d-b6c5-3a0d-92df-9103012dfb74 | -17.74487 | -43.82108 | 2024-10-04 04:32:00 | AQUA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 49.2 |
| b96b06b5-d4cd-351d-af9e-c81560cc650b | -17.74346 | -43.7888 | 2024-10-04 04:32:00 | AQUA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 2d52f352-c93e-318f-bac2-6c250f279b03 | -17.73867 | -43.81424 | 2024-10-04 04:32:00 | AQUA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b4f061c0-9180-30a1-91e9-452c1fc8d33e | -19.23685 | -43.37047 | 2024-10-04 04:32:00 | AQUA_M-M | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d5baf4ff-ee0d-3174-aced-a191340ccdae | -18.8632 | -43.58756 | 2024-10-04 04:32:00 | AQUA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.8 |
| 35efc43a-4da0-389a-8300-3d663d903ed4 | -18.84975 | -43.5859 | 2024-10-04 04:32:00 | AQUA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 48b9b47c-667e-311f-b79f-bd86eaf5fa50 | -20.1074 | -43.51995 | 2024-10-04 04:32:00 | AQUA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 9dac5896-6c98-3737-93a3-b4268898f743 | -13.99514 | -44.01762 | 2024-10-04 04:32:00 | AQUA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| c72ae094-51e2-341c-b851-bf7f38663a58 | -7.68794 | -42.98937 | 2024-10-04 04:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 8ed202e9-0ae4-3b6d-b412-f5c60fb7cf58 | -8.13125 | -44.81317 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 146ffb0b-0965-3463-96f0-d97231a83c54 | -4.86666 | -38.43447 | 2024-10-04 04:32:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b17d0a32-76b3-3689-b381-ec881afca02f | -5.22896 | -38.17624 | 2024-10-04 04:32:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 14a35427-2ca3-3006-bd02-3be0cf2fbaac | -5.22352 | -38.17544 | 2024-10-04 04:32:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c434d8d5-e8db-39d8-b9a1-4efcf88685ad | -5.18121 | -37.99582 | 2024-10-04 04:32:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a560bf2b-f525-3944-873d-f62050728589 | -5.1807 | -37.99939 | 2024-10-04 04:32:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d2160b83-fe51-3c94-8890-6fd582b0436d | -5.17571 | -37.99503 | 2024-10-04 04:32:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 71ba15b5-08ba-3d76-88f9-09436b7934ef | -5.1752 | -37.99858 | 2024-10-04 04:32:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f96f6536-90b0-3893-ada4-d3a8ac16bdab | -7.30642 | -38.13816 | 2024-10-04 04:32:00 | NPP-375D | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3fe0aad9-97d0-3545-8dae-0092e79dfbdb | -7.30078 | -38.13756 | 2024-10-04 04:32:00 | NPP-375D | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c65715f7-404b-393f-97fa-3e3d22b0dabe | -7.06338 | -40.35532 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 625d9023-d85f-356c-a23d-3a73ddbc8f69 | -6.86111 | -39.61522 | 2024-10-04 04:32:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 17b2d5ed-ea1f-399d-822a-29b2ad56d0fc | -6.86071 | -39.61805 | 2024-10-04 04:32:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 23d685c6-c1dc-3abe-aad1-c6266ed01573 | -6.86031 | -39.62088 | 2024-10-04 04:32:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1ab53747-5c9a-3dce-8b9f-065b96894d0f | -12.1411 | -40.8921 | 2024-10-04 04:32:00 | NPP-375D | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 21b639c3-ac6a-34a3-b4ab-be05d495dc5b | -12.14037 | -40.89777 | 2024-10-04 04:32:00 | NPP-375D | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dcea472e-54d6-3150-ba99-06ecce3c9df9 | -11.10756 | -43.33578 | 2024-10-04 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f00fabe-3885-32b1-8b3d-046f9e8cb238 | -11.10702 | -43.33963 | 2024-10-04 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1a5c93b4-7175-3478-b029-764a0ee26291 | -7.34755 | -41.94912 | 2024-10-04 04:32:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7edb396d-e1be-3893-9f3c-fc705a3f40a5 | -10.2356 | -42.38912 | 2024-10-04 04:32:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3aecfb27-58b3-3385-8e0d-8c673a76e794 | -11.24326 | -41.64214 | 2024-10-04 04:32:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50044a88-c565-3fda-8f35-4a748d11adf5 | -11.24179 | -41.64058 | 2024-10-04 04:32:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README95.md)
