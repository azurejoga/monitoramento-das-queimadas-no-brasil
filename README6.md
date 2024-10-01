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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9a2d3da-27b3-371f-a9f0-6366dee58bd7 | -21.56654 | -47.8406 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 44.5 |
| c7132af3-0e51-3529-9da6-149956e3842f | -21.56514 | -47.81921 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 135.8 |
| f0b269fc-3d6a-3d08-9a04-a279a16bf655 | -21.56474 | -47.82503 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 2de5a99e-bbdc-3c57-a889-7a68212e9fdb | -21.56349 | -47.80401 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 30.5 |
| bd704b0d-153e-3e97-aa46-f22d3b3c6db8 | -21.56296 | -47.80964 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 5ba18bcc-a297-37bc-a64f-f9080f5d2aa9 | -18.9156 | -49.22944 | 2024-10-01 00:45:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.3 |
| 07334f5c-54f1-3944-b5e4-9c1373db8555 | -18.91368 | -49.21189 | 2024-10-01 00:45:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 1d79c49e-6b8f-30f8-8ae3-c251ce084496 | -19.69914 | -48.78532 | 2024-10-01 00:45:00 | TERRA_M-M | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d5003401-f3c1-3dab-ad7d-6f954610c8ee | -19.67588 | -48.78801 | 2024-10-01 00:45:00 | TERRA_M-M | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 9fa9549b-9101-3899-9f01-0d0aa6e69ea4 | -19.66795 | -48.79431 | 2024-10-01 00:45:00 | TERRA_M-M | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5a5da4c5-4b9e-3573-b63b-0c459b6d5e8a | -21.37424 | -48.48063 | 2024-10-01 00:45:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 52094f06-4b3f-38ac-a423-70b30ac3abf1 | -18.51884 | -49.43468 | 2024-10-01 00:45:00 | TERRA_M-M | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 0a83661e-be6a-3735-bf44-f152cb2fe935 | -20.18077 | -50.01063 | 2024-10-01 00:45:00 | TERRA_M-M | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.2 |
| 5cb07d3d-2a0b-3923-8576-538b7f2d78c4 | -20.16883 | -50.01734 | 2024-10-01 00:45:00 | TERRA_M-M | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.0 |
| 636783fd-1e17-34de-a878-170947c0a65e | -20.16786 | -50.01192 | 2024-10-01 00:45:00 | TERRA_M-M | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.3 |
| 03d3dc31-8d8d-38e5-b1b6-6c30c62f14f7 | -20.16652 | -49.99601 | 2024-10-01 00:45:00 | TERRA_M-M | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| c835b5ff-6b0b-356e-8dee-65a7cd534466 | -2.4048 | -50.3085 | 2024-10-01 00:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 8765b410-69ae-37f7-bdd7-cc17a67aae0d | -2.4047 | -50.3295 | 2024-10-01 00:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 270.9 |
| 00cec920-8bd1-39ad-ac84-465f043dc9db | -2.4046 | -50.3505 | 2024-10-01 00:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 6f85db27-840f-3aa1-9bb6-9a5d8ffb5d36 | -2.3863 | -50.3299 | 2024-10-01 00:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| ed7ea7e4-b57b-3011-90e7-38548d187c9a | -3.0282 | -51.3345 | 2024-10-01 00:45:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 307d9e1f-f89a-301c-891d-372fc3af87d1 | -4.6987 | -49.8062 | 2024-10-01 00:45:32 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8d1ecdba-ab0a-318c-8222-f6e75d9a3b79 | -4.7172 | -49.8053 | 2024-10-01 00:45:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 14a2e885-4c29-3a8c-82ff-4219061a16f7 | -5.7715 | -45.5574 | 2024-10-01 00:45:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 4ac7a0f8-09be-3117-9a1e-65632ea7adf0 | -5.9786 | -45.3847 | 2024-10-01 00:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c2b7e33e-9477-376d-ad57-a2db1c8effb9 | -5.9788 | -45.3621 | 2024-10-01 00:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 7ce0303e-cadd-3487-bf73-ae4832c6deab | -6.2524 | -44.132 | 2024-10-01 00:45:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| ca6c8887-da9e-311e-bad6-c5496851508b | -6.6953 | -43.0474 | 2024-10-01 00:45:43 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 256de5cf-c3c9-3e20-b0a1-9424bb8e0102 | -6.9671 | -47.6215 | 2024-10-01 00:45:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| e305748a-befd-3e56-951d-cc1d2e852cf4 | -11.1249 | -45.6407 | 2024-10-01 00:46:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 1fc966f1-50f9-30c2-96ef-512c34fd5b1a | -11.1054 | -45.6662 | 2024-10-01 00:46:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 59f58a3b-b460-398e-9ce0-d2b85c0cdb24 | -10.9429 | -50.0833 | 2024-10-01 00:46:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| a5ba8cd1-70ab-3319-98f6-9a7194ae8e18 | -11.1253 | -45.6178 | 2024-10-01 00:46:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| b5e6b637-745f-3ba5-aa92-803268b590d1 | -12.5848 | -53.4899 | 2024-10-01 00:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 844995a8-bda9-372e-ae23-903d6c859d64 | -12.6039 | -53.4879 | 2024-10-01 00:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 154.7 |
| d91c354e-aed6-3c7c-873b-663a432df390 | -12.5135 | -53.1441 | 2024-10-01 00:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 34378462-2d7d-3578-9baf-92b39bb5b695 | -12.5132 | -53.165 | 2024-10-01 00:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 5517116f-ebfb-3fa1-8ead-cbccaad8eb3a | -12.4945 | -53.1462 | 2024-10-01 00:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| ba262c0e-6259-3aaf-9a9e-ced9d13db768 | -12.4942 | -53.167 | 2024-10-01 00:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 215f0078-2472-3f0b-854b-67fc2e676d4f | -13.2493 | -51.2452 | 2024-10-01 00:46:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| fe1c48f2-00c0-3c1f-bfc1-5ced748b271c | -14.7406 | -48.7498 | 2024-10-01 00:46:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 4d86d834-32c6-3782-b468-05f004e761fb | -14.7211 | -48.7529 | 2024-10-01 00:46:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| bde540b9-ab7f-30ef-845c-814b7b2823b8 | -15.6372 | -57.447 | 2024-10-01 00:46:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 8f9c244f-ef76-3388-9cf2-444bed23c065 | -15.6179 | -57.4491 | 2024-10-01 00:46:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4af87516-a056-38c8-99eb-420ec7f2cbb9 | -16.6267 | -55.1725 | 2024-10-01 00:46:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 5653d4ac-5af4-35a5-a01d-4acae1b0eacb | -16.6459 | -55.1908 | 2024-10-01 00:46:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 189.6 |
| f6b95c8c-e5d3-3724-a1b7-d16f74586e5e | -16.6455 | -55.2117 | 2024-10-01 00:46:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 124.8 |
| a257c558-bbc9-38ff-9f12-78649c54549d | -16.6263 | -55.1934 | 2024-10-01 00:46:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 240.6 |
| 16878292-c6d0-3620-8400-106baa022358 | -16.6259 | -55.2142 | 2024-10-01 00:46:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 108.1 |
| 730d7d2a-da7b-3b06-a602-1233660f04f7 | -16.5134 | -57.3305 | 2024-10-01 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.7 |
| 64ff1015-9c97-34e3-b31f-4441996af804 | -16.5131 | -57.3509 | 2024-10-01 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 2ca968a6-b55e-3e69-9fad-a6d02eaae74e | -16.4939 | -57.3327 | 2024-10-01 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.5 |
| 05732856-a449-32ac-9213-0ad098e012e5 | -16.4935 | -57.3531 | 2024-10-01 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.8 |
| 2234870f-4902-3996-b22a-e128e451ad64 | -16.4743 | -57.3349 | 2024-10-01 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.3 |
| 44cc0854-533c-3279-853c-6de3ef05700d | -16.474 | -57.3553 | 2024-10-01 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.5 |
| 01d05ecb-0d8a-301d-889c-1eb9f480f527 | -16.9919 | -57.9696 | 2024-10-01 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 25217caa-87be-3cec-82eb-82baa271e385 | -18.6011 | -53.0412 | 2024-10-01 00:46:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 13ceb5d9-a685-3e3f-a013-058a0ce937f4 | -18.6006 | -53.0628 | 2024-10-01 00:46:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b5695d01-afeb-348a-aa8b-64e7d28d4e15 | -19.1329 | -57.4628 | 2024-10-01 00:46:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.2 |
| 75f7ce98-acd8-38b9-a5ff-0bc5f62bf164 | -19.1325 | -57.4836 | 2024-10-01 00:46:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 0974ecff-616c-3329-a58c-1ecd221584de | -20.1793 | -49.9937 | 2024-10-01 00:46:58 | GOES-16 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| 8956b8f0-901e-3b53-906e-2881f1cc2fc8 | -20.1788 | -50.0164 | 2024-10-01 00:46:58 | GOES-16 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.3 |
| 4ec19a4b-35f8-33b5-9a59-2e8882bd801e | -21.7122 | -54.8253 | 2024-10-01 00:47:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 565b4d34-43a9-31ef-a483-93e68b8106e1 | -21.7117 | -54.847 | 2024-10-01 00:47:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 4d66b997-76fb-313a-94be-9f485a7c1861 | -21.6917 | -54.8288 | 2024-10-01 00:47:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 4706d8a1-a22a-3880-b72e-edd181cb145e | -21.6912 | -54.8506 | 2024-10-01 00:47:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 182.0 |
| a31cffef-3a7e-3474-8085-ce609944262f | -22.3922 | -49.2961 | 2024-10-01 00:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| 92d36415-7f00-3940-9769-419cb0c3c89b | -22.3916 | -49.3194 | 2024-10-01 00:47:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.0 |
| a2719538-0800-3571-ab7b-649e0698f9f2 | -22.3713 | -49.3011 | 2024-10-01 00:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.5 |
| 3ecf2811-a43e-396f-8b7e-059910587376 | -22.3707 | -49.3244 | 2024-10-01 00:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 166.6 |
| ab9b5110-bd81-36b1-a90f-adcd0766f94d | -12.14526 | -50.08514 | 2024-10-01 00:48:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4387447d-d9c6-39c1-ba47-e5d17bb7037d | -12.14299 | -50.07968 | 2024-10-01 00:48:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 8f865d76-a85c-3464-b91b-4af17890115a | -12.14132 | -50.05415 | 2024-10-01 00:48:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| b9fcc7ed-6514-3dc4-972e-8db4c4c296d1 | -12.14113 | -50.06416 | 2024-10-01 00:48:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 6de8476d-b057-3efa-8d7e-801d7f7f22cf | -12.13928 | -50.04865 | 2024-10-01 00:48:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2740277b-5eed-3a9b-9963-26a1c22c3c0e | -12.00059 | -50.31909 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2797ea1d-83c2-3b5f-90e2-57d9b809f196 | -11.0999 | -49.59677 | 2024-10-01 00:48:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b6eed1fb-374e-3094-95de-08eb11113f12 | -10.98742 | -50.16586 | 2024-10-01 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3c4d08e2-5b40-3a7f-beed-3a60c2c0e9d0 | -10.94444 | -50.09517 | 2024-10-01 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 2fbf882f-5d0e-3f48-a916-241a6a1b8fb3 | -10.94306 | -50.08656 | 2024-10-01 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 8823b200-c0fa-3690-8f1d-f12e654cabd9 | -10.94264 | -50.08028 | 2024-10-01 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 4997dd1a-b45c-35ac-b424-b53683757d8f | -10.94116 | -50.07175 | 2024-10-01 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 405ea917-1c15-34ff-a09d-97f16b0e4300 | -10.93374 | -50.10289 | 2024-10-01 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eb8b42e8-bbee-38d1-a5e9-bf70bd1c8cf3 | -10.93184 | -50.08801 | 2024-10-01 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| ffea040f-4c7d-3ee2-b133-92ec615916cb | -10.92251 | -50.10435 | 2024-10-01 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 505ff5e3-7995-36ef-9be3-3edd49fda0bc | -10.92062 | -50.08947 | 2024-10-01 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| b40e9cde-fb2d-3aac-acb0-004da266ad55 | -13.63708 | -51.16465 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 0a2ac1b9-a77f-3f62-aeaf-3e2214d94840 | -13.62666 | -51.18616 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 389b0201-25c0-3f04-93c6-23fae5b31ce7 | -13.62622 | -51.17989 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 3ee5175a-6fe0-33e5-9556-a644181e43dd | -13.6243 | -51.16619 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 92ed685c-972e-35d5-8709-b9c5fca9c7ab | -13.6174 | -51.10028 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4e086276-9348-3f75-81f7-4a6c34f9172a | -13.61724 | -51.10666 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a7cbcb04-e90d-389f-a614-3091e6878725 | -13.58596 | -51.17084 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 4745a6ba-09ad-3bbd-824b-506dbe30dabf | -13.58367 | -51.1509 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 6a02c3f4-2bff-3691-9583-18adbf6d929b | -13.57547 | -51.19239 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5aa94c6c-16db-37e5-9ca2-8154658c70e2 | -13.57319 | -51.1724 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 5db530fc-9505-3d0e-827e-c623e3ab4a4e | -13.57091 | -51.15247 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 424.3 |
| 92ee6b5b-87c4-3bb3-b1ab-2d04a1934769 | -13.56864 | -51.13259 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 1cb1761d-4f13-3a4b-9429-94e7d36f11c2 | -13.55591 | -51.13415 | 2024-10-01 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 91998f0a-9ff2-3ac4-b200-3744406c35c2 | -13.64953 | -50.35915 | 2024-10-01 00:48:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |


[Clique aqui para ver as próximas entradas](README7.md)
