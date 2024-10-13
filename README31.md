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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02f1cea6-c5ec-3132-a6e3-5752f61b1118 | -10.5286 | -49.9349 | 2024-10-13 02:26:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 089f5f3c-57a8-3d12-ae27-fa2ba4913c75 | -10.9502 | -44.6762 | 2024-10-13 02:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 95ee95f2-51c9-3767-85e9-09cc67c12e7d | -10.9506 | -44.653 | 2024-10-13 02:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 6a045379-5d5b-3b38-a2dc-d8ba4838ee9b | -11.6334 | -48.3736 | 2024-10-13 02:26:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 8909d2e7-82e9-3eec-8089-905229b79202 | -11.7308 | -64.9769 | 2024-10-13 02:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| fd9691e4-cc23-354f-9554-f1da19c96a58 | -12.2754 | -47.6473 | 2024-10-13 02:26:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e4e4277d-39ad-334d-8996-5f49ba1ebc94 | -12.3982 | -63.7284 | 2024-10-13 02:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 07b50508-af18-3fb4-a48a-76625ecfc492 | -15.6419 | -59.9767 | 2024-10-13 02:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 43129915-180c-3404-b428-6a74cbfa808b | -17.2639 | -42.6527 | 2024-10-13 02:26:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 94abe7ba-9279-3df4-b9b2-f30d40d7b2df | -17.284 | -42.6479 | 2024-10-13 02:26:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 7d113fba-d34c-356c-868f-039ec88e4be0 | -16.9995 | -57.4791 | 2024-10-13 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 8ecd9d2f-2ef4-3ffb-84c0-e5689f207617 | -17.1758 | -57.479 | 2024-10-13 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 87c8e428-93cd-3f12-a67c-d0ddea2b609f | -17.1761 | -57.4585 | 2024-10-13 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 162.7 |
| c076d140-3c2c-39d1-b8da-c6a8141d3dd2 | -17.1764 | -57.438 | 2024-10-13 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 6adc72a3-cf51-320f-8e95-2ec703a6410f | -17.1954 | -57.4767 | 2024-10-13 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 9008fe7e-5282-3a9e-9088-e2aff1e345b3 | -17.1957 | -57.4562 | 2024-10-13 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.3 |
| 9486f9b3-f697-3a19-85a0-309796184fc9 | -17.6478 | -56.2668 | 2024-10-13 02:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.9 |
| dccedb87-7d1e-3e68-960f-9ae8c2c61b11 | -17.964 | -57.3843 | 2024-10-13 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.9 |
| 57851d5f-6bca-325b-9455-3dd804eb29bc | -17.9643 | -57.3637 | 2024-10-13 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.0 |
| e289a4a4-e3fe-34c6-a099-eca29b8a464f | -17.9837 | -57.3819 | 2024-10-13 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| af61e1fb-9be8-3e13-9662-eae3aef90c0c | -17.9841 | -57.3612 | 2024-10-13 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.7 |
| e991d00f-ebc7-35e2-bf14-a9f4e3e72341 | -18.2151 | -56.5665 | 2024-10-13 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| e681cae3-b6ea-3873-be73-8765c84c9dce | -18.2155 | -56.5457 | 2024-10-13 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 928dd8d1-2d97-38e0-bdb1-44df81dbba92 | -18.2166 | -56.4832 | 2024-10-13 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| b94f585f-0112-32a0-9d87-3a10ddf88e98 | -18.2169 | -56.4624 | 2024-10-13 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 61327075-bc4f-3988-807c-fe1f08a57763 | -18.236 | -56.5014 | 2024-10-13 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.2 |
| ee597fab-a81d-3a23-80d1-60d34d9e49c2 | -18.2364 | -56.4806 | 2024-10-13 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| db27283a-24a8-34c9-830e-33f2cc73b245 | -18.2368 | -56.4597 | 2024-10-13 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 247dc066-eadf-317f-9980-d33ba785ce1a | -1.733 | -54.173 | 2024-10-13 02:35:16 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 83840c14-a1f7-3e74-ad16-c9645915ed4e | -2.1693 | -48.8108 | 2024-10-13 02:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| fbb6c8fa-b06c-3fae-bb8e-959fbe02e36a | -3.0731 | -54.2473 | 2024-10-13 02:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 82e6a90e-b33a-39d3-9d7c-2b9666decec0 | -3.0915 | -54.2469 | 2024-10-13 02:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4cdac4fa-0cec-3677-a07e-e4e65a64ac02 | -3.0956 | -53.0559 | 2024-10-13 02:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| d7bcfe56-792b-3151-a78e-5b73f47d54a7 | -3.0957 | -53.0355 | 2024-10-13 02:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 777c871a-1739-32a2-b0ff-39877c1497de | -3.114 | -53.0554 | 2024-10-13 02:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| c1287a11-4bd1-3f91-be14-100d5f066695 | -3.1141 | -53.0351 | 2024-10-13 02:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| dfebdd91-5d4b-3e0d-82dd-0604a3ab0399 | -3.1607 | -50.4556 | 2024-10-13 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2a8f5956-e3e7-3ef3-a953-acfddd378ecf | -3.1791 | -50.476 | 2024-10-13 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 8e2218e1-aed4-319e-ba23-e194eb47061b | -3.1792 | -50.4551 | 2024-10-13 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| fed49cf3-6089-31e4-a965-c386fd5d34e6 | -3.1976 | -50.4545 | 2024-10-13 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a0df70c5-9452-3fc9-b962-727d08b7da58 | -3.3594 | -47.3271 | 2024-10-13 02:35:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 3a2b88c0-8f01-3c72-922a-e7e8481a054b | -4.1148 | -48.2515 | 2024-10-13 02:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 690ea401-1d60-3683-9323-74d7da3d88c1 | -4.1149 | -48.2299 | 2024-10-13 02:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b765244c-6f9c-3ae4-b088-dcf2b97f72db | -4.3985 | -44.4881 | 2024-10-13 02:35:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 4272e844-8964-3130-8468-1dabc40f7e78 | -4.3986 | -44.4652 | 2024-10-13 02:35:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 176e18d2-ec2a-3900-afcc-54afbfc9481d | -5.1381 | -45.3969 | 2024-10-13 02:35:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 2cfb5df0-30d1-33eb-a21c-a7e8af90d2c6 | -7.6627 | -47.3229 | 2024-10-13 02:35:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| a9d89674-9448-328b-91c3-4891aa855efd | -7.6815 | -47.3213 | 2024-10-13 02:35:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| f21dbea8-a5dd-3aa6-a523-4492a2d22d36 | -8.2352 | -64.0961 | 2024-10-13 02:35:54 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1e5f05da-c2e9-3f89-a219-08128181e1c0 | -9.7359 | -64.2295 | 2024-10-13 02:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a74f6933-1550-3c5c-b2fc-8764d5a78054 | -10.5097 | -42.5023 | 2024-10-13 02:36:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 81.3 |
| b6a8fcd1-be5b-3984-aac9-cf2dc3460aff | -10.5091 | -49.9798 | 2024-10-13 02:36:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 24709b64-318e-381a-be55-b9a105df954e | -10.5094 | -49.9584 | 2024-10-13 02:36:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 2a38486e-ea1b-3824-99aa-779dcea2e378 | -10.5281 | -49.9778 | 2024-10-13 02:36:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 9d27c7b3-c984-324a-bba1-cddeadf9044f | -10.5283 | -49.9564 | 2024-10-13 02:36:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 151.8 |
| b727126c-1b62-36a0-a155-432846b77280 | -10.9311 | -44.6789 | 2024-10-13 02:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| da19c936-f5fd-31a9-a611-d8581013533c | -10.9502 | -44.6762 | 2024-10-13 02:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 35dcb169-7373-3f45-96db-ffe4d5738cd1 | -10.9506 | -44.653 | 2024-10-13 02:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 917b9cdc-dcaf-3bba-b1e3-db18e3334ac2 | -11.6334 | -48.3736 | 2024-10-13 02:36:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| f5130dab-b4cf-329a-96d0-c7bcc4589a9c | -11.7308 | -64.9769 | 2024-10-13 02:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9bcb2e04-62e3-34d6-a772-02d3ffb961c4 | -12.2754 | -47.6473 | 2024-10-13 02:36:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 7e11e96d-4316-32ba-8b72-7ba83b6af34b | -15.6419 | -59.9767 | 2024-10-13 02:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| d4417dcd-9001-3397-967b-2b97d6656a6b | -17.2639 | -42.6527 | 2024-10-13 02:36:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 114.8 |
| fbe0b6af-fd1a-34dc-aad4-4dfd8919a941 | -17.284 | -42.6479 | 2024-10-13 02:36:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 107.7 |
| d096e57f-d2f6-3dd8-8078-da469db5c74b | -17.1957 | -57.4562 | 2024-10-13 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| de6e1340-8ec9-37eb-ba8f-fa120564b6f6 | -17.1954 | -57.4767 | 2024-10-13 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| f8cc8e09-c4be-3925-b075-6e4b0a901e94 | -17.964 | -57.3843 | 2024-10-13 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.8 |
| e2679c99-c6a8-3ced-9b3f-8a6ddb6a32c0 | -17.9643 | -57.3637 | 2024-10-13 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.6 |
| 2555f02c-1abd-3bd3-9e4a-1313c44b3e59 | -17.9837 | -57.3819 | 2024-10-13 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.6 |
| b38362a9-dd85-3ff8-98f9-d79db3a09958 | -17.9841 | -57.3612 | 2024-10-13 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.0 |
| abd7826a-7975-36d0-9fef-280f39dd473d | -18.2151 | -56.5665 | 2024-10-13 02:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 82ccd434-0388-3db1-b0c1-6644ba2fc744 | -18.2155 | -56.5457 | 2024-10-13 02:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| d9953f20-ec88-308a-86c6-f3e9e1897a6d | -18.2166 | -56.4832 | 2024-10-13 02:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 1bf1d716-d3af-3051-b16f-99ad3e5fb44a | -18.2353 | -56.5431 | 2024-10-13 02:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 252d6a9f-3b67-350c-b934-a9dbb9370717 | -18.2364 | -56.4806 | 2024-10-13 02:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.2 |
| f94ac7ce-21a4-3988-a9ef-71f718c6765c | -18.2368 | -56.4597 | 2024-10-13 02:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 2a5cd415-c0e9-3c88-bad4-99a3e49fca2f | -12.3891 | -63.714699 | 2024-10-13 02:38:03 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9284b8c8-4202-3f3a-89a3-3eacd5058df2 | -12.3967 | -63.7421 | 2024-10-13 02:38:03 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 00043148-f1ad-3bda-a3df-c9dec6e4a37f | -12.3796 | -63.7174 | 2024-10-13 02:38:03 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b7e079c2-aa8e-3e7d-ab09-cb7153df9051 | -12.3871 | -63.744801 | 2024-10-13 02:38:03 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ee18adcb-18ee-3ce7-8259-63ead6b51933 | -11.7269 | -64.960899 | 2024-10-13 02:38:19 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4a0a372d-c79f-363f-8407-79bbfdbe25c2 | -11.7173 | -64.9636 | 2024-10-13 02:38:20 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 07df70db-7231-3e27-9154-14e65f40f2f7 | -8.0301 | -71.391197 | 2024-10-13 02:39:45 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ab5c22f1-0c7b-325b-8468-b2b05c2c3318 | -7.5065 | -72.698898 | 2024-10-13 02:39:59 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f58f113-957e-3eb6-a214-0388a6eb3fd8 | -7.5085 | -72.707497 | 2024-10-13 02:39:59 | METOP-C | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| bc853df1-8efc-37f7-920b-1bcba11a0ceb | -7.3177 | -72.642899 | 2024-10-13 02:40:02 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1fdca2e3-98b7-3f8f-9322-93a0df73df95 | -7.3375 | -72.900497 | 2024-10-13 02:40:02 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ea19eb1-2203-32fc-be6c-491074f64867 | -6.9753 | -71.768997 | 2024-10-13 02:40:04 | METOP-C | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04a7dc4b-a290-3f90-870a-1a60247f97bd | -1.733 | -54.173 | 2024-10-13 02:45:16 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 26308ba3-580c-311b-83e9-378183a80d68 | -2.1693 | -48.8108 | 2024-10-13 02:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 4d4f2593-036d-33ac-9a0c-7374dcb813bc | -3.0731 | -54.2473 | 2024-10-13 02:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| ab80a5dd-6f4c-31c8-83d7-cf1dfae36131 | -3.0956 | -53.0559 | 2024-10-13 02:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 8cce7d4f-557c-3a16-b070-be53e309ea25 | -3.0957 | -53.0355 | 2024-10-13 02:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 175.3 |
| 8fee51e1-e0f2-3455-869e-f5631776af03 | -3.1141 | -53.0351 | 2024-10-13 02:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 40c4391b-ffdf-3a81-a052-03ea3c071d34 | -3.1607 | -50.4556 | 2024-10-13 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 8b80a7ab-a67a-3db3-b6f2-84a68ec4d268 | -3.1791 | -50.476 | 2024-10-13 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| bc120386-ad2a-3aaa-a18d-d0cce8718ed5 | -3.1792 | -50.4551 | 2024-10-13 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 017e01f0-44e7-3b0c-aaa6-5eb02e14a10d | -3.1976 | -50.4545 | 2024-10-13 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 15feb5b2-68ac-3919-a714-37a3fee80c60 | -4.1148 | -48.2515 | 2024-10-13 02:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| eeb38d37-fa1f-32da-bc9f-41476fce5209 | -4.1149 | -48.2299 | 2024-10-13 02:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |


[Clique aqui para ver as próximas entradas](README32.md)
