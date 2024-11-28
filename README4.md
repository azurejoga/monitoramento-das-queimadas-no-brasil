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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfc504fa-38f0-3a17-9844-0c3f2c832a6a | -3.497 | -40.374199 | 2024-11-28 00:03:00 | METOP-C | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9f0e259f-1e72-3f0f-89c7-cb408fd67ddc | -4.7613 | -43.297298 | 2024-11-28 00:03:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 121efaaa-ec44-308a-b166-fc5a9ad2f46a | -3.3441 | -50.113602 | 2024-11-28 00:03:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49be66b7-16f6-3e47-8c45-0ae13a6ab53e | -3.1463 | -46.571301 | 2024-11-28 00:03:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96898c8d-914a-3ccb-86d0-e558fb4bb0aa | -3.6187 | -44.472698 | 2024-11-28 00:03:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4631c5a8-fbbb-3035-9f9e-ae621811c90e | -3.9541 | -44.276798 | 2024-11-28 00:03:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9db6c46-667b-33df-b691-0f4f00ccc877 | -8.8579 | -35.947201 | 2024-11-28 00:03:00 | METOP-C | SÃO BENEDITO DO SUL | PERNAMBUCO | Brasil | 2612901 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de146e7b-c17b-317e-ad22-1f6cf3a99d47 | -3.4189 | -43.535198 | 2024-11-28 00:03:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4f356bb-a8aa-35c2-938f-47a938d62cc2 | -2.6542 | -45.925598 | 2024-11-28 00:03:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d055d59-44df-3cae-880d-b6c0e20b81bc | -4.731 | -44.408798 | 2024-11-28 00:03:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9222db5d-1097-30da-bbf5-3aee5ce0c21a | -3.8112 | -40.441799 | 2024-11-28 00:03:00 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7e7b94be-a07d-3fff-a71b-6ae1ab270d71 | -2.8383 | -45.378399 | 2024-11-28 00:03:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d50bf083-f11b-3c56-9c12-23995c48009b | -6.0202 | -48.001301 | 2024-11-28 00:03:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95aa41d9-f59c-37ae-864a-77ddced11ddc | -6.3648 | -38.615501 | 2024-11-28 00:03:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 385e53c7-b40e-3434-af6d-5bedd012429c | -6.7828 | -44.394501 | 2024-11-28 00:03:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| adc1e849-5d18-3050-9ff2-f1458d1ef542 | -4.1056 | -43.8069 | 2024-11-28 00:03:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed371531-cebf-3153-8fe1-1d93546cb022 | -4.7239 | -44.423199 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1dae456-358d-3097-a3f6-b2d80f445284 | -2.436 | -45.410801 | 2024-11-28 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bcdd647d-c3d3-36cf-bf4f-27e636ea21af | -8.8563 | -35.939999 | 2024-11-28 00:03:00 | METOP-C | SÃO BENEDITO DO SUL | PERNAMBUCO | Brasil | 2612901 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2ddd6392-6daf-3aa1-b271-9c74293c623a | -4.0867 | -46.118401 | 2024-11-28 00:03:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5618715-b108-36b4-b1c1-f6361f011814 | -2.7839 | -46.8223 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44dc81bc-4ae7-3278-b04c-d19596068cfb | -3.5757 | -42.4049 | 2024-11-28 00:03:00 | METOP-C | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| acaba2b1-09f0-3990-be59-7798b4f41d9c | -4.7169 | -44.4375 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f281a986-7900-3aa0-8eb7-6ec4977c1adc | -9.7913 | -36.188801 | 2024-11-28 00:03:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c4ba18d-ded9-34f7-9d61-2d3317265334 | -5.443 | -35.602699 | 2024-11-28 00:03:00 | METOP-C | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 633c2f19-1fb0-3428-92d3-028ecee98a4c | -9.7881 | -36.174702 | 2024-11-28 00:03:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4500bd1e-4e65-3e73-9d93-f02dc995511c | -3.6522 | -43.430698 | 2024-11-28 00:03:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 964d5d25-15db-38a0-bf25-397fc03f75d0 | -9.1224 | -44.709702 | 2024-11-28 00:03:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 753c5fe7-68e5-332f-9dcf-455fa3046a40 | -4.7321 | -44.459999 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdd08203-470e-3059-a592-0fcf41d5f1f5 | -6.539 | -44.164799 | 2024-11-28 00:03:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21e9668d-1ca7-318f-a659-a5634a795a8b | -9.9653 | -36.4515 | 2024-11-28 00:03:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2f372b7e-74e2-36f0-933b-1256096150a2 | -7.6422 | -42.9786 | 2024-11-28 00:03:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 939f9467-57ae-33f6-9488-831947345e11 | -9.0688 | -35.389 | 2024-11-28 00:03:00 | METOP-C | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e865d25a-0784-347e-88d0-fcd4b5003e91 | -8.4557 | -35.1087 | 2024-11-28 00:03:00 | METOP-C | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3f1a6d63-fcfd-3132-94f2-0acc951bd631 | -2.4576 | -45.188999 | 2024-11-28 00:03:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8a3b29aa-afdc-3d34-95b4-dc96a66c57ae | -2.4949 | -45.990601 | 2024-11-28 00:03:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d119e664-76ad-3e0d-b98d-6a912e008574 | -2.7899 | -46.8036 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2819cee-0580-3ef8-946d-9a59504924a7 | -5.4609 | -46.249401 | 2024-11-28 00:03:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ccb9bb8f-0fee-34ff-b9d5-e117ca33d075 | -2.248 | -47.8409 | 2024-11-28 00:03:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70f4f811-71a9-3524-b964-fd5dfff40552 | -2.0028 | -47.116199 | 2024-11-28 00:03:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 918ad77c-4875-3d12-809f-b3fd26642619 | -3.4166 | -43.524899 | 2024-11-28 00:03:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1eed59c-115f-3e24-81ce-b3b14ffa7223 | -5.4808 | -38.266602 | 2024-11-28 00:03:00 | METOP-C | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 50e4e671-f269-31ff-b785-2fefe334e7f0 | -1.9037 | -46.542999 | 2024-11-28 00:03:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57b1b3bc-e20a-3bd8-9816-765f6b2e5aff | -5.9206 | -45.362099 | 2024-11-28 00:03:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9191bc5b-aa5c-3e9b-824f-f6fe426bef3b | -2.7914 | -46.855801 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41186591-9ff2-3e4f-ac04-4b414445aecc | -2.7607 | -46.809898 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cf9cbef-2271-3109-acd9-20f0e262ca14 | -3.289 | -44.053398 | 2024-11-28 00:03:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb757e67-06aa-384f-83f7-15f0432b8d13 | -2.2342 | -47.101299 | 2024-11-28 00:03:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36a64b89-92fb-3118-b6b4-d432221e6d22 | -2.5958 | -49.479099 | 2024-11-28 00:03:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fce045d-07cf-3569-87e9-3ffbaea3ff12 | -4.4554 | -42.065102 | 2024-11-28 00:03:00 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 838246fd-63f2-30f8-b999-2b68fcc2c01f | -10.5386 | -37.064499 | 2024-11-28 00:03:00 | METOP-C | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7848c81e-e55b-3399-9915-1eda0c7f344d | -5.9024 | -39.667702 | 2024-11-28 00:03:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 59a837f6-7748-3c3a-8a0a-d06f1af77626 | -3.2865 | -44.0424 | 2024-11-28 00:03:00 | METOP-C | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c777aef4-3139-300f-9aa4-49c653931204 | -3.6089 | -44.4748 | 2024-11-28 00:03:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26303809-d8a0-397b-af7c-caed06dbf5fe | -5.4412 | -35.594898 | 2024-11-28 00:03:00 | METOP-C | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| ca53a66e-d329-39ad-95dd-a798b1031946 | -2.7937 | -46.820202 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b161e22e-07be-370c-a290-5b636609accc | -5.1649 | -41.285099 | 2024-11-28 00:03:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 46926c0c-4e57-30ff-9b4f-9eb4bae03944 | -6.8576 | -38.1082 | 2024-11-28 00:03:00 | METOP-C | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 1c63070e-4173-3f42-b4fe-1ba7a8065c32 | -3.9033 | -41.485901 | 2024-11-28 00:03:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a8caaa77-89d8-3f21-a4e9-7dad15461071 | -3.3314 | -50.056 | 2024-11-28 00:03:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ff2ac6f-2be1-3517-92ac-dcfc135da2c0 | -5.9174 | -45.347301 | 2024-11-28 00:03:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5da41f9-a936-3895-bf9c-a4a4c307f9d7 | -6.0348 | -48.022099 | 2024-11-28 00:03:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a672df8f-9366-3fab-b01c-333fcb592c43 | -6.0396 | -48.044899 | 2024-11-28 00:03:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebe8fd1b-4709-3adc-b33a-67a0c73e77b8 | -6.0395 | -47.997299 | 2024-11-28 00:03:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d7676b7-29b4-36ae-9e81-8f519a273802 | -10.17653 | -36.3625 | 2024-11-28 00:09:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| d847d52d-832b-3780-a1c7-faf64fa14653 | -9.83067 | -36.19157 | 2024-11-28 00:09:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 35.2 |
| a0c10201-029c-3af9-87d3-1984f2705c91 | -7.26294 | -39.74933 | 2024-11-28 00:09:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 14.8 |
| aea299d1-1813-3b5e-95e3-6242d7f342de | -7.69661 | -37.52195 | 2024-11-28 00:09:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 612eb959-c8c5-3553-8f6e-542aac31bfc2 | -6.92451 | -38.13805 | 2024-11-28 00:09:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 55af7439-4d0d-31e0-be6b-e89312dbe1d2 | -10.86514 | -40.30603 | 2024-11-28 00:09:00 | TERRA_M-M | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 0fb118a0-7ec8-35bb-b61e-ed34ca7c1a47 | -6.41181 | -38.62307 | 2024-11-28 00:09:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| d355afa9-f169-3ae7-9130-fcbd08e21fd4 | -9.86386 | -36.23299 | 2024-11-28 00:09:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.1 |
| e5400c1b-9b5e-3022-bea7-9052138fe842 | -10.67314 | -37.01039 | 2024-11-28 00:09:00 | TERRA_M-M | CARMÓPOLIS | SERGIPE | Brasil | 2801504 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 5204c321-0620-3b69-8610-b7ea45cb3622 | -9.00761 | -35.97644 | 2024-11-28 00:09:00 | TERRA_M-M | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 8847dd20-b998-3085-9ddb-846c09c4666a | -9.36353 | -35.82291 | 2024-11-28 00:09:00 | TERRA_M-M | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 81646abc-f2bc-3429-99c6-812b93006e05 | -8.44309 | -35.07375 | 2024-11-28 00:09:00 | TERRA_M-M | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 85d46d1a-0add-3b1a-a9fc-74148c501dc1 | -10.02494 | -36.45513 | 2024-11-28 00:09:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 03aafb0f-f8fb-38e3-b7ec-92dda74343d2 | -9.36221 | -35.81362 | 2024-11-28 00:09:00 | TERRA_M-M | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 74e76450-2a29-3e81-9768-e3f3f03b45db | -9.57771 | -36.16393 | 2024-11-28 00:09:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 2932083f-318d-3fe5-859a-9418be094cbf | -9.72196 | -36.46893 | 2024-11-28 00:09:00 | TERRA_M-M | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 49c84818-4c73-3885-a7c5-bafe9b2dd154 | -10.2257 | -36.6488 | 2024-11-28 00:09:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| da8826ce-e898-31c8-8883-eed607096557 | -10.64295 | -36.92317 | 2024-11-28 00:09:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7babad4a-665c-3934-8d9c-a706f603bae0 | -8.90489 | -35.45256 | 2024-11-28 00:09:00 | TERRA_M-M | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| c4fbc089-2379-36b9-801f-16c6a18ba254 | -9.82939 | -36.18249 | 2024-11-28 00:09:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| 51d1ba2e-b882-3f3b-a2a3-2d2a3fd188e7 | -6.66407 | -34.97665 | 2024-11-28 00:09:00 | TERRA_M-M | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 0a4ff60b-96f1-33cf-9cc9-fc1713436d94 | -6.90818 | -42.4895 | 2024-11-28 00:09:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 89feec84-7dc2-3309-b3da-95a5ebfac994 | -6.73214 | -35.01439 | 2024-11-28 00:09:00 | TERRA_M-M | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 58.2 |
| fde227f7-5cb7-3e46-af01-77f151e0bf4c | -8.49732 | -35.11712 | 2024-11-28 00:09:00 | TERRA_M-M | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 1a5f3e9d-ae66-3466-819e-818130f39597 | -10.57978 | -37.06687 | 2024-11-28 00:09:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 0731d158-e554-3e21-8a52-5c92c54e6a2f | -9.18247 | -44.74365 | 2024-11-28 00:09:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6b571b20-55b2-3bc0-a05c-54075da387a2 | -10.67438 | -37.01937 | 2024-11-28 00:09:00 | TERRA_M-M | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| e68510d9-e27c-3b36-8915-824bf411f4fc | -9.57642 | -36.15482 | 2024-11-28 00:09:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 39.1 |
| a190a43e-8522-38bd-9123-f4f09425674d | -9.87405 | -36.24072 | 2024-11-28 00:09:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 211cfeb7-df36-3d8d-aeeb-21b3db7351c8 | -8.44458 | -35.08385 | 2024-11-28 00:09:00 | TERRA_M-M | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| ed602a3f-3228-397c-be45-b89def86cdb5 | -6.92575 | -38.147 | 2024-11-28 00:09:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 758b973d-b7a5-3e4f-8009-3c3deaffb358 | -10.0142 | -36.45373 | 2024-11-28 00:09:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.3 |
| 32ef9be6-3d82-31f1-be87-00f7aaaba17f | -7.51261 | -35.11442 | 2024-11-28 00:09:00 | TERRA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| df8167ab-2f33-364d-814a-fd5785abef09 | -7.26432 | -39.75967 | 2024-11-28 00:09:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 18e4b6f4-e305-3be0-9f6d-1e07caa60af4 | -10.58865 | -37.06559 | 2024-11-28 00:09:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| d33b53eb-a7cc-3f64-98fb-a75706f0580b | -9.8396 | -36.19024 | 2024-11-28 00:09:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 101.0 |


[Clique aqui para ver as próximas entradas](README5.md)
