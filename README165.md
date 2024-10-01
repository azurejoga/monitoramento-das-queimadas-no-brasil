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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1a20c3a-197c-3275-be6d-5c2c2f6890b6 | -22.37 | -49.3477 | 2024-10-01 12:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.7 |
| 771340d0-8af7-32b4-867f-b71a422e9290 | -22.3498 | -49.3293 | 2024-10-01 12:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.6 |
| 4069c565-1b13-3840-8bc8-754dd1a3e762 | -22.3707 | -49.3244 | 2024-10-01 12:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 307.3 |
| 194c3955-3f7d-398f-84d6-54476f07b4dc | -22.3713 | -49.3011 | 2024-10-01 12:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 263.9 |
| e5057e91-7bee-30a6-91df-327f21fa352e | -22.3916 | -49.3194 | 2024-10-01 12:47:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.1 |
| 3395baa7-504b-33d2-b330-c35ddd06970c | -7.3078 | -43.7842 | 2024-10-01 12:55:47 | GOES-16 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 8990f039-df25-3a00-b214-4b7cc661d3ad | -7.3076 | -43.8074 | 2024-10-01 12:55:47 | GOES-16 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 0d1bdba8-4200-3a2b-baa7-2d08994c8a31 | -7.289 | -43.786 | 2024-10-01 12:55:47 | GOES-16 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 686162ac-db19-3b59-935a-9497d277848f | -10.052 | -50.2833 | 2024-10-01 12:56:03 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d2034a17-fc05-39de-8b37-9c420f06f7b3 | -10.0331 | -50.2851 | 2024-10-01 12:56:03 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 526d2665-61b1-3c59-8e3f-9cb16dd81fe2 | -10.6787 | -46.1538 | 2024-10-01 12:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| fc87618c-9565-32b2-bc5e-f82bae5096d6 | -10.6978 | -46.1514 | 2024-10-01 12:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 2423d886-ae63-387f-9970-841596591210 | -10.5746 | -48.0178 | 2024-10-01 12:56:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 4d5d167b-cab8-336d-b4a1-4d1211d5ac06 | -10.5743 | -48.0399 | 2024-10-01 12:56:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 0331be20-ff88-3377-98a6-cbe9f6784566 | -11.2584 | -45.6453 | 2024-10-01 12:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| d9178c09-3f65-31d2-ac98-d21938553110 | -11.158 | -49.6289 | 2024-10-01 12:56:09 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 84755c40-4c23-3674-9ffa-6a1d430b32fe | -11.1575 | -45.9779 | 2024-10-01 12:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 5332f893-fcf6-36d5-8f05-8bdca3047a1d | -11.258 | -45.6682 | 2024-10-01 12:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 2771bca7-e419-3ee7-b9cc-0c8eee7d3e7b | -12.1593 | -50.0717 | 2024-10-01 12:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 2d0bd408-72cf-350c-b2d9-4b848b795e30 | -12.2103 | -50.4741 | 2024-10-01 12:56:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 314a5583-3fe7-33fe-928b-9062a6e992f6 | -12.1402 | -50.074 | 2024-10-01 12:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| b4e696e6-4f10-355c-8c44-a59518cec586 | -12.1406 | -50.0524 | 2024-10-01 12:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 3883c0d9-b3ee-3b0a-9c33-e610991b37f4 | -12.3934 | -50.9658 | 2024-10-01 12:56:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 22b549dc-a7cf-3c3e-b789-b162a2e871c5 | -12.4125 | -50.9635 | 2024-10-01 12:56:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 199.3 |
| a04854da-e8d5-33b1-bc13-e46b398f9a51 | -12.9625 | -51.2169 | 2024-10-01 12:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| cae36589-97a6-38c0-945e-e8c28f1b394f | -12.9205 | -51.4563 | 2024-10-01 12:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 2c35c7f6-ba83-3678-8c5c-996287a556a5 | -12.7636 | -62.9036 | 2024-10-01 12:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| d045173a-8e9d-3d15-a5a3-70b9336326b1 | -12.9396 | -51.454 | 2024-10-01 12:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 78acde79-24c4-389d-ad57-a220f6788de9 | -12.9433 | -51.2192 | 2024-10-01 12:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| d2c8b992-9740-39c4-b039-87c4223559fd | -12.94 | -51.4327 | 2024-10-01 12:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| a0b17497-f52b-3437-be36-701db2f530ed | -12.9437 | -51.1979 | 2024-10-01 12:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 4054d625-97bd-3759-895a-dd1a7e6a5b14 | -13.1924 | -51.2097 | 2024-10-01 12:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| f9e1b2d9-37b6-314c-a2b1-037f54953657 | -12.9169 | -62.6829 | 2024-10-01 12:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 139.2 |
| e15803f8-bbdf-3e52-8cec-160ebf46b6e6 | -13.2112 | -51.2287 | 2024-10-01 12:56:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 232d7f4d-114a-38bb-83ff-70db4bd16874 | -13.558 | -51.1417 | 2024-10-01 12:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| dbc5c784-39b7-36fe-a95e-adad0f5a2eb2 | -13.5765 | -51.1821 | 2024-10-01 12:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 724f29b2-196d-3051-a33c-d8129fc52e5f | -14.754 | -48.0788 | 2024-10-01 12:56:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| cc3167b3-70d5-3f84-891b-855e41ba32b8 | -14.7735 | -48.0757 | 2024-10-01 12:56:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| dfba52c3-607e-3f21-9c48-09ff261c871b | -16.0906 | -50.4081 | 2024-10-01 12:56:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 55af2bb5-9952-37d9-9319-ca87bda44fb1 | -16.4939 | -57.3327 | 2024-10-01 12:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| a2069886-b588-3751-98cc-12feebc22111 | -16.474 | -57.3553 | 2024-10-01 12:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.6 |
| d201fdc6-19ea-30fd-ba35-21dc55359bc3 | -16.4536 | -57.4188 | 2024-10-01 12:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 364.7 |
| 0510b9bb-94f3-3d50-ae44-9e0576d3fa84 | -16.4743 | -57.3349 | 2024-10-01 12:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| de5d41bf-8f0c-378d-9c7e-aaf9365f445f | -16.6512 | -57.2535 | 2024-10-01 12:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 485fa631-754c-3718-8758-064256eeda06 | -16.6528 | -55.9373 | 2024-10-01 12:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 362d2890-1f46-3635-b879-4fb002b80128 | -16.6313 | -57.2762 | 2024-10-01 12:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| b69f061f-35eb-311c-973c-6f10f6e3076a | -16.6525 | -55.958 | 2024-10-01 12:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 128.9 |
| 703327c7-c60f-3b05-829a-64c75f7a02ee | -16.7532 | -55.7797 | 2024-10-01 12:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 66b3c178-e871-3706-837f-820322f7ee29 | -16.6259 | -55.2142 | 2024-10-01 12:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 116.3 |
| 80105bba-f206-34e4-8bc3-c83a3ed37fc0 | -16.7728 | -55.7773 | 2024-10-01 12:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 136.1 |
| 9de706cc-595e-3c13-8e34-f73e52351193 | -16.6117 | -57.2784 | 2024-10-01 12:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 225.7 |
| a2a27473-54da-37e8-b70f-e85a8d164d62 | -16.7528 | -55.8005 | 2024-10-01 12:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 59fedace-c748-34ef-80c7-c15613c43b21 | -16.6316 | -57.2557 | 2024-10-01 12:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 167.6 |
| 9bca9b29-b6f5-34bc-9cec-454609d4f6bd | -16.6455 | -55.2117 | 2024-10-01 12:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| 64ffeb11-90b9-3872-a5b6-56b06142c370 | -16.6263 | -55.1934 | 2024-10-01 12:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 83e20b25-68ee-321c-b3d1-592e9341b962 | -16.7724 | -55.798 | 2024-10-01 12:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 0715726c-c20c-31af-9816-6410b8a11b6c | -16.8787 | -57.6971 | 2024-10-01 12:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 153.7 |
| 84c8c641-0d72-39c3-a8e7-c5c5687919b8 | -16.8591 | -57.6993 | 2024-10-01 12:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| cfaeb32b-cf8d-3c0b-90ce-6f108d1bdc5b | -16.76 | -57.792 | 2024-10-01 12:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 996b099d-1ea4-306b-a701-8a0cfbfa2060 | -16.8784 | -57.7175 | 2024-10-01 12:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| de20a702-c4e9-3764-adf5-998a33090074 | -16.7796 | -57.7898 | 2024-10-01 12:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 92011775-50f0-30ce-8d8a-2eb02c04a0ac | -16.8983 | -57.6949 | 2024-10-01 12:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 7fdbde41-fca4-3114-a6dd-7ff4379b91c3 | -17.0892 | -56.7709 | 2024-10-01 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| dbe1c1a0-de11-3c2c-8347-aa48921d3161 | -17.1377 | -56.2076 | 2024-10-01 12:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 62decba5-71e9-3bbe-b202-2a8b62f01ef2 | -17.0705 | -56.7114 | 2024-10-01 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 2cd3f79b-37a0-30c2-afd3-813f70ee4581 | -17.0702 | -56.7321 | 2024-10-01 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 413e8f20-0866-3305-8e1a-0662d49a7e8e | -17.1381 | -56.1869 | 2024-10-01 12:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 609625aa-22c7-3c19-959a-c3862c53ef21 | -17.0699 | -56.7527 | 2024-10-01 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 2603e8bd-e006-34e0-b945-4da1e6017aeb | -17.0898 | -56.7297 | 2024-10-01 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 15ddc783-733a-3e5a-a0ca-0bf34f00d11b | -17.0502 | -56.7551 | 2024-10-01 12:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| f7459ca0-87b4-3ff1-9f6f-f3d7f9dedf73 | -17.1581 | -56.1637 | 2024-10-01 12:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 104.5 |
| e9f2cd32-1dca-3e43-8a1c-3ff0b8215206 | -17.157 | -56.2259 | 2024-10-01 12:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 7996c899-b557-3662-9343-7227665f9cf5 | -17.1964 | -56.2209 | 2024-10-01 12:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| 1a8d7643-5d38-3125-9ef0-52ae523f3bef | -17.2167 | -57.3718 | 2024-10-01 12:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| f434fe36-c17b-3e44-bfb4-20a5e43e6b37 | -17.1767 | -56.2234 | 2024-10-01 12:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 146.7 |
| e585687a-4e5f-34b3-bc14-39ce220ebb14 | -17.1778 | -56.1612 | 2024-10-01 12:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 3ea348fd-6549-3255-a736-54794ee573a9 | -18.1132 | -49.0757 | 2024-10-01 12:56:47 | GOES-16 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d9a702c1-fbff-3d58-aed2-29ae7b17890d | -18.5236 | -49.4241 | 2024-10-01 12:56:49 | GOES-16 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 911.0 |
| 4cb7d5f9-00bc-3323-a3f8-0b8fad5eb28a | -18.6973 | -57.333 | 2024-10-01 12:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.1 |
| b6696f21-ca3e-3144-9174-0ed7c212dbf6 | -18.6977 | -57.3123 | 2024-10-01 12:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.5 |
| 2d6212d9-691d-331d-9069-aea0c585e924 | -18.7176 | -57.3097 | 2024-10-01 12:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 06dd5382-9f3f-367d-a6ef-9f5cd9e4c0b6 | -18.8895 | -49.1942 | 2024-10-01 12:56:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 555d0f57-c81c-36f6-9f90-47e254022f30 | -18.9091 | -49.2129 | 2024-10-01 12:56:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 192.9 |
| 8e7fdbbf-0669-3b93-85e0-bc341875da14 | -19.7052 | -48.7757 | 2024-10-01 12:56:55 | GOES-16 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 89.9 |
| cbf7dade-88f0-3027-86aa-21540b4bcd18 | -19.7878 | -47.953 | 2024-10-01 12:56:56 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 9975e0fc-ebff-3eed-a633-bf1a986f3060 | -19.9921 | -55.4728 | 2024-10-01 12:56:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 58.2 |
| daad2c52-9568-37b6-921f-83c75f23d381 | -20.9359 | -49.1023 | 2024-10-01 12:57:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 281.3 |
| fa65b94d-abf6-3bb0-a531-da431a89cdd3 | -21.8445 | -48.2178 | 2024-10-01 12:57:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 155.1 |
| bdd879de-b2f7-3002-80ca-f7db13eb1052 | -22.3707 | -49.3244 | 2024-10-01 12:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 307.4 |
| 8d524ebf-41f5-3c24-91f1-33dd71804315 | -22.3498 | -49.3293 | 2024-10-01 12:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 134.1 |
| dd3c8549-cd6c-32ff-a25d-2827d82982fd | -22.37 | -49.3477 | 2024-10-01 12:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.8 |
| b341fda0-63b4-3ed4-a4f6-207af4212c87 | -22.3916 | -49.3194 | 2024-10-01 12:57:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 158.3 |
| aa1088a6-2396-3851-b914-74b2e1b04e05 | -22.3713 | -49.3011 | 2024-10-01 12:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 254.4 |
| 3434b84c-363f-3ca9-98a8-b93dbca61349 | -21.62 | -47.81 | 2024-10-01 13:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 97c8ec1f-c10a-3edc-8932-47493adca583 | -21.59 | -47.79 | 2024-10-01 13:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 192e27c1-06e7-3fbd-a876-31394b98db01 | -21.62 | -47.86 | 2024-10-01 13:03:22 | MSG-03 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 51613750-15f0-3271-8f29-f2ed2672b8f0 | -21.59 | -47.84 | 2024-10-01 13:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1376fd77-f484-3739-b6b5-fde0fd7cca33 | -18.86 | -50.85 | 2024-10-01 13:03:37 | MSG-03 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4bfc9a58-3d24-398f-804d-f4cc3449608f | -8.2364 | -44.8672 | 2024-10-01 13:05:52 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 2b93dfa1-ab42-38cf-b5d7-34bdb57346c9 | -10.5743 | -48.0399 | 2024-10-01 13:06:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |


[Clique aqui para ver as próximas entradas](README166.md)
