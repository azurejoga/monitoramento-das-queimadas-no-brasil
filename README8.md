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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a998b909-e015-3448-8f8c-d16a5d33699d | -15.6945 | -51.7868 | 2025-09-05 00:36:00 | METOP-B | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bb0448c0-f9c9-3c52-8833-e1361c276be5 | -6.6729 | -52.830101 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 201239e6-4c9f-3ce8-8d2e-8d9f8c1a5f67 | -10.3306 | -53.646 | 2025-09-05 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2401ba9a-9d94-3d24-9945-970ec5c82fa4 | -5.8521 | -46.7089 | 2025-09-05 00:36:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c3b12e8-1fc6-3b2c-90ac-22436eb412c5 | -6.1266 | -53.464199 | 2025-09-05 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e5fb57a-bdcb-3621-a209-778a24c833c9 | -8.7205 | -52.045601 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2b77b1f-fb20-36eb-b845-a132265aa255 | -11.4852 | -52.230202 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d6aa68f-0ce8-3688-801f-b0ae179cc0f9 | -5.444 | -45.0326 | 2025-09-05 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39250ff7-300c-3736-83ab-2df87ec84036 | -15.0576 | -52.395599 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5c2b0e5-7047-3245-bbe1-d2f33dbe891b | -9.1135 | -57.098801 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d42b6130-7356-34fe-a686-f3749932cb7a | -8.7877 | -48.682499 | 2025-09-05 00:36:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7fb715d6-d1ed-31f7-8946-c9b7db1ad7cc | -3.181 | -54.929199 | 2025-09-05 00:36:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d23b5f2f-99f3-396e-8ad4-6fe7851ed497 | -6.125 | -53.4571 | 2025-09-05 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 581f8b4b-84d2-3f66-8fa1-4697f12efd92 | -5.4551 | -45.0779 | 2025-09-05 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afbf83cb-e790-36ae-9562-3f283268d1c7 | -15.0819 | -52.4123 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d9931b8-b66e-3732-b401-adac5c3b586f | -11.4395 | -52.2103 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a8480b6-42ff-3621-aebe-1f2e14391ba1 | -8.7948 | -48.6688 | 2025-09-05 00:36:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb4400e-ef6e-3728-9693-af092b34ea8c | -15.3167 | -53.057301 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7690b8c-e1ac-33a0-a441-c9c78e88e33e | -11.4476 | -52.200699 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57d07eed-96c8-3c4a-bda8-c366d5aa0e35 | -17.521799 | -52.318401 | 2025-09-05 00:36:00 | METOP-B | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c10b1c7a-5fe7-3bfa-930b-2a4f32aeb69f | -6.6746 | -52.837399 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31d24c9f-8578-351e-97b0-3ed26c0648c0 | -23.2278 | -47.216599 | 2025-09-05 00:36:00 | METOP-B | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 577b1b47-b866-38c4-bb51-cf3ca9ada799 | -10.3787 | -57.7948 | 2025-09-05 00:36:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24be1fd3-504b-33cc-bace-f220f0db14b2 | -7.1108 | -57.565102 | 2025-09-05 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f822ed1-cb95-3810-8713-dda0f757cd5d | -10.0023 | -55.184898 | 2025-09-05 00:36:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 73f45776-86ee-3150-a941-0966053dfc93 | -2.284 | -49.331402 | 2025-09-05 00:36:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fde3a91e-1c3e-32e3-bcb3-7e4a10368146 | -17.517099 | -52.297001 | 2025-09-05 00:36:00 | METOP-B | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d8972b5f-dbf0-3d55-818e-574e5b0176db | -7.856 | -45.458801 | 2025-09-05 00:36:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d7239744-237a-31ad-b1b5-e15af02d886e | -6.7301 | -52.809299 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5078605f-ccfb-371d-a42b-bf2bd13cc137 | -15.5985 | -53.644699 | 2025-09-05 00:36:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 38c1a38f-1cd4-31e4-a8a1-4d07be3f9b32 | -11.5007 | -54.561298 | 2025-09-05 00:36:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 606a2169-5b30-31ae-b60b-9951d61c459b | -3.7594 | -54.706902 | 2025-09-05 00:36:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df23e654-8556-3434-9179-9542be44ccf9 | -16.3445 | -43.763699 | 2025-09-05 00:36:00 | METOP-B | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6a99098f-5a2b-3228-8802-1bb1be960ad8 | -15.3999 | -48.429901 | 2025-09-05 00:36:00 | METOP-B | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be04acb2-fe3b-30f3-8ef1-9b817b74e1d1 | -9.1019 | -57.0928 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f8fd7f3-7b9e-39cb-a863-ab0fb30c7b63 | -15.7113 | -52.324501 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3e753fa-1e74-39cb-bc0b-f7b6a5643e28 | -6.7294 | -45.594299 | 2025-09-05 00:36:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 653f0ef8-e158-3ce1-a94f-d586a3783067 | -11.1762 | -55.242001 | 2025-09-05 00:36:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb7461b9-1c02-30a2-87ba-b843e11f6eee | -10.3436 | -50.457901 | 2025-09-05 00:36:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41ca0929-1469-366c-86c3-469d13e89b96 | -11.446 | -52.193501 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71991bda-33f0-328e-98f2-cebae47d1808 | -9.9464 | -54.790001 | 2025-09-05 00:36:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf06fb1d-61d7-3ab6-9bca-881a54e176c6 | -8.2053 | -52.542198 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c01f4b54-9c83-3f75-afe2-a5cb070e2485 | -16.1821 | -52.969299 | 2025-09-05 00:36:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06aed4dd-055e-3753-aacc-757bdc1487b7 | -9.5633 | -51.0942 | 2025-09-05 00:36:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 661c1730-a3d6-388f-a23c-37efc365024a | -8.3737 | -51.346901 | 2025-09-05 00:36:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03f95e1c-66ee-345f-bbd5-69c513eb06c3 | -15.4046 | -48.4492 | 2025-09-05 00:36:00 | METOP-B | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a5ff5858-2fbd-378d-8c0b-54cc9235859d | -10.6162 | -48.306801 | 2025-09-05 00:36:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bc2df7f-0cc7-33d5-bf61-ba2a3b54e50b | -6.4243 | -51.121799 | 2025-09-05 00:36:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3114be0c-ecfd-3135-a9e7-3409cc205c0d | -6.904 | -50.879601 | 2025-09-05 00:36:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f84a9077-9d3d-38d3-a255-dd6d62260911 | -5.5767 | -49.303001 | 2025-09-05 00:36:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a32e52e8-750f-3e0e-9b50-2c8dda908f02 | -17.5186 | -52.3041 | 2025-09-05 00:36:00 | METOP-B | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37364554-435f-375a-a117-72bb560ae098 | -6.2006 | -47.131302 | 2025-09-05 00:36:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38528ec2-0db8-3b90-9346-21ea2344c9c5 | -2.2019 | -47.6078 | 2025-09-05 00:36:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72298fc2-f811-3dda-bc46-10478d38f2bb | -15.4728 | -52.9244 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 522e7499-826c-375f-9520-bf17a8b276c2 | -15.7097 | -52.317402 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be7e781b-994e-317d-bff0-ae4371a22b95 | -12.3434 | -53.855099 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4fd5577b-bc56-3cde-8e76-4f57fd97c9b5 | -10.2843 | -60.745399 | 2025-09-05 00:36:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c43ce3b2-1eb4-320e-b966-3f6803536978 | -7.9272 | -52.363499 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c70d903e-74f9-3e3e-b634-842b04eeef0e | -9.1244 | -56.911598 | 2025-09-05 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c61aa6f0-adba-3bae-9f1a-90cbcedc8f3a | -7.2979 | -49.004799 | 2025-09-05 00:36:00 | METOP-B | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e6fffe57-ebb8-3e19-8b2d-f8850abbf4a0 | -5.7107 | -57.784 | 2025-09-05 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e249871-2dc3-3489-b808-31a5778a0846 | -6.2065 | -47.112999 | 2025-09-05 00:36:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0da25f99-17c2-364c-82af-660b050561b2 | -15.0803 | -52.405201 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea251f8c-27b4-347c-bf9d-164fa4babc3e | -15.4466 | -52.9454 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0316b156-c09d-3095-a621-86e511918d85 | -8.4773 | -55.080002 | 2025-09-05 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 993fe6e0-f754-3246-8954-efc16c33e117 | -11.7164 | -51.481899 | 2025-09-05 00:36:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f97d2ffe-4760-3539-a392-189ceca46521 | -9.1881 | -55.223999 | 2025-09-05 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41b0975d-bd70-3f28-b3c6-22c631607c9f | -9.1117 | -57.090698 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8729aa-5f24-3e5e-9da8-2ed88d35b66b | -8.2103 | -52.564301 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47a6c878-d430-3bae-b97b-968fc66f7180 | -9.183 | -55.247299 | 2025-09-05 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32c1ea4d-cedf-3011-ab23-d1b376197102 | -8.911 | -50.465099 | 2025-09-05 00:36:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24e045eb-911f-325f-9e7b-b30cb859fb14 | -11.4541 | -52.183899 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce810ef8-ffc5-3611-b03a-1b200dfbb31c | -23.4627 | -52.897202 | 2025-09-05 00:36:00 | METOP-B | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3e227444-af01-316d-8078-a8a664b63fff | -11.4836 | -52.2229 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ecccf13-b946-30a9-9938-99c5c022eed6 | -22.129499 | -47.175598 | 2025-09-05 00:36:00 | METOP-B | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d1a141b2-f5a4-38b5-abde-935875039c3a | -9.11 | -57.0826 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d04503a8-cdb9-3bee-9d0c-03c502c86db5 | -15.4481 | -52.952499 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4dc1f03-0d41-3794-8099-40f3f074fb43 | -6.1348 | -53.454899 | 2025-09-05 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| babc352a-aaf3-3abd-a194-9045f9ac5890 | -11.4574 | -52.198399 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3240ab81-33b9-3b39-b0c0-29d707b25869 | -8.9261 | -47.042198 | 2025-09-05 00:36:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30a44b7a-5977-3b95-9b79-3bfeb4c0b735 | -9.1564 | -56.8218 | 2025-09-05 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb9f1118-ae8a-3d9a-b3e6-f95433a81580 | -7.9477 | -45.373402 | 2025-09-05 00:36:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 82f9f8d9-78d5-3f99-b1d6-3ce99077379f | -19.545799 | -54.834702 | 2025-09-05 00:36:00 | METOP-B | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f75f54af-edb8-3bcf-9fa3-5b1594ef42d8 | -6.1001 | -43.312199 | 2025-09-05 00:36:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 72fc4a4d-6ee9-3428-bddd-2a5febc4c2b4 | -5.3899 | -57.2603 | 2025-09-05 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c3d6db4-01e3-3788-8b81-d6ae47ceab5b | -7.0916 | -56.865898 | 2025-09-05 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 524423e8-a565-3b74-9cbd-276b7281f812 | -16.4534 | -50.854599 | 2025-09-05 00:36:00 | METOP-B | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4324a1e7-9042-3832-b0cc-44a15a0d8f70 | -11.4885 | -52.244598 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae77ec89-e6a5-39bd-88bb-4ada8238bfd4 | -8.9322 | -47.0252 | 2025-09-05 00:36:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2fafff12-eb4d-344d-9d29-6094939e7569 | -6.5348 | -49.7859 | 2025-09-05 00:36:00 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdfc7885-1597-3595-bf6a-ebfca9b00be0 | -16.1723 | -52.9715 | 2025-09-05 00:36:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7f66e055-d54c-3436-a553-25c7a5ddbf91 | -10.8257 | -49.7868 | 2025-09-05 00:36:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7a949a9-ae61-31ae-a18f-efab16ad03ab | -9.0743 | -57.1073 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e0417c5-1754-388b-932a-d3d0f2898021 | -7.5711 | -50.3368 | 2025-09-05 00:36:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cee8f37-61b1-377f-8058-f95e0f93e6cb | -12.3563 | -53.866901 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b50a8fd-a935-329d-a46b-39f3ac076532 | -10.158 | -54.165501 | 2025-09-05 00:36:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8592df-cc71-39cf-9484-36b8a51861d5 | -12.9711 | -57.130299 | 2025-09-05 00:36:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0357bad7-c16c-31df-bf6a-292350a35d69 | -7.5493 | -50.332001 | 2025-09-05 00:36:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b3b1c8b-2eb4-3298-b589-b6daed46e2ce | -16.173901 | -52.9786 | 2025-09-05 00:36:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc249392-cf12-32ab-a4e7-d8c16cf6aa3c | -11.4525 | -52.176701 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
