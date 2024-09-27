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
| 4623e1b2-45a3-3ecb-9e52-3e9b87178dab | -12.7014 | -54.6949 | 2024-09-27 00:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2eb54101-f965-37f5-bd33-2c502a8bde07 | -12.8437 | -54.0422 | 2024-09-27 00:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 0fb894e5-6df9-3ef4-b805-68ca5e6fd68e | -12.844 | -54.0215 | 2024-09-27 00:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| d8e5cde1-5ab8-3855-9d03-2d76ec5b5344 | -12.8628 | -54.0402 | 2024-09-27 00:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 182.0 |
| 78b36e16-68b1-375a-9bcc-76b2c73fb645 | -12.8631 | -54.0195 | 2024-09-27 00:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.0 |
| b1361994-5336-38c3-8771-296114b22dc3 | -13.4413 | -44.0267 | 2024-09-27 00:26:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b7459822-8b6e-3dd6-a61c-83c4b7140479 | -13.4418 | -44.003 | 2024-09-27 00:26:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8201c2d1-28a8-34bd-8b28-51e25ff6e4b6 | -16.7329 | -55.8237 | 2024-09-27 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 127c3a9a-c6b5-319c-9c42-b8143a830ed4 | -16.713 | -55.847 | 2024-09-27 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 682ab669-9d80-39c9-add4-24d3ebbd1d6b | -16.7133 | -55.8262 | 2024-09-27 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 193c29b9-d9d5-3b27-93e1-6129d5085881 | -16.7325 | -55.8445 | 2024-09-27 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 72d431cc-8ae9-325b-a807-2c2f03172e18 | -19.6136 | -42.8159 | 2024-09-27 00:26:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| 0c8038b0-332f-3b98-854c-94a30bf74a20 | -19.5266 | -47.8952 | 2024-09-27 00:26:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 957ed9a5-4b53-3a95-bfec-4f083b8d2ede | -19.5272 | -47.872 | 2024-09-27 00:26:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 82cf0125-2b7e-30cd-abb9-5e319806d01b | -20.5432 | -41.8685 | 2024-09-27 00:26:59 | GOES-16 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| c93501e0-0076-3f12-a264-568180f9a798 | -20.7597 | -42.7675 | 2024-09-27 00:27:00 | GOES-16 | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.2 |
| 676ab223-1c20-3260-a23b-f63bfd54166c | -21.4132 | -42.9523 | 2024-09-27 00:27:03 | GOES-16 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 710fbb08-0988-3076-a459-fc890c712f04 | -21.3314 | -48.8742 | 2024-09-27 00:27:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b6d90311-a86e-30c6-a166-c3333274955e | -22.7442 | -44.7785 | 2024-09-27 00:27:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.2 |
| b64d2401-c9b9-3a63-b581-e07fbf8e9f31 | -23.5808 | -47.365 | 2024-09-27 00:27:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.2 |
| ab949d9b-653d-3fa8-b6e8-cfe89466296a | -23.5816 | -47.3408 | 2024-09-27 00:27:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 172.2 |
| 248471d5-5ea9-3b1a-8e92-b4df71b8c4c7 | -22.6745 | -42.8433 | 2024-09-27 00:30:52 | METOP-B | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a23046ba-f386-3150-aabf-ffec1401b7c6 | -22.6763 | -42.851101 | 2024-09-27 00:30:52 | METOP-B | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba41be55-dbae-38ed-8525-0c2db8649cb1 | -23.584 | -47.338699 | 2024-09-27 00:30:53 | METOP-B | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1a1ddac-7635-3f1b-86ac-ae8de0c7f735 | -23.3603 | -46.2687 | 2024-09-27 00:30:53 | METOP-B | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7c51d590-cd9c-3f9f-a8e3-54ff92f3819f | -23.3619 | -46.276501 | 2024-09-27 00:30:53 | METOP-B | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b893b668-7d26-346e-9d59-fd18f180cebe | -23.572599 | -47.332401 | 2024-09-27 00:30:53 | METOP-B | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc3dd2c4-fc55-3238-901b-7404e73a9de5 | -23.574301 | -47.3409 | 2024-09-27 00:30:53 | METOP-B | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a419f222-1ac8-31c4-859f-48aaa9e11cb1 | -23.576 | -47.349499 | 2024-09-27 00:30:53 | METOP-B | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a87328ba-cc95-307f-87c7-8abf483838d4 | -23.5776 | -47.358101 | 2024-09-27 00:30:53 | METOP-B | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f49ebced-4fe6-3603-a4c5-537d663cb2c9 | -23.444201 | -46.992001 | 2024-09-27 00:30:54 | METOP-B | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7d13fb25-d3e3-3ecf-a85c-7e38c4c47907 | -23.445801 | -47.000301 | 2024-09-27 00:30:54 | METOP-B | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c09dd3a7-4541-3bbc-97e3-db939f4420e5 | -23.434401 | -46.994202 | 2024-09-27 00:30:54 | METOP-B | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6a3941cd-facd-377a-944d-3864a6305d86 | -23.436001 | -47.002499 | 2024-09-27 00:30:54 | METOP-B | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9d3742b2-b9c3-3917-9121-587fc1ff1334 | -23.4377 | -47.010799 | 2024-09-27 00:30:54 | METOP-B | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b332fa90-e0de-3a25-929d-dd7a838c4fd9 | -22.9055 | -44.729599 | 2024-09-27 00:30:55 | METOP-B | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e0807590-412f-3b88-968c-020ad7d4af5b | -22.907101 | -44.737 | 2024-09-27 00:30:55 | METOP-B | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5915fcd7-7d77-3bcf-9da5-fa1f175ff8d0 | -23.218201 | -46.426102 | 2024-09-27 00:30:56 | METOP-B | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f26bcce3-5f1f-3fe1-80ac-be9524c5722f | -23.164801 | -46.3148 | 2024-09-27 00:30:57 | METOP-B | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 972be065-76e2-33a9-acd2-f73ba1e18276 | -22.7425 | -44.785702 | 2024-09-27 00:30:58 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a7a418dc-6408-3954-b558-f7af5385c8ed | -22.744101 | -44.793098 | 2024-09-27 00:30:58 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc3cbb10-9232-3558-a831-1c5ff44b28bf | -22.7313 | -44.780701 | 2024-09-27 00:30:58 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 50d49baa-8688-3351-a477-b9c7ae05228f | -22.7328 | -44.788101 | 2024-09-27 00:30:58 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e4f563bd-1946-3192-b9d8-7f74435452e6 | -22.7344 | -44.795502 | 2024-09-27 00:30:58 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34c6bf9a-754c-31ca-9479-86e3e6c80199 | -22.736 | -44.802898 | 2024-09-27 00:30:58 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0b43a26-8868-3e8c-a535-6dae0401e81a | -22.561899 | -44.095299 | 2024-09-27 00:30:59 | METOP-B | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9228be21-c653-335c-b95d-00773c946cd8 | -22.955099 | -45.9417 | 2024-09-27 00:30:59 | METOP-B | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff0ce3c8-0b51-3cc8-a13d-bec977faed5a | -22.956699 | -45.949402 | 2024-09-27 00:30:59 | METOP-B | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 662cb988-af29-306d-ae47-2cfb6fd257d0 | -22.9582 | -45.9571 | 2024-09-27 00:30:59 | METOP-B | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0573291b-ae63-3a79-95e2-da1381a68655 | -22.643101 | -44.8493 | 2024-09-27 00:31:00 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e2b3856-763e-3332-b5e4-1e075627d1c1 | -22.644699 | -44.856701 | 2024-09-27 00:31:00 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1e0199c-592e-3670-bf49-40eeba488fc4 | -22.646299 | -44.864101 | 2024-09-27 00:31:00 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b3a4bed3-5012-3cc8-a031-2cb66e037ed9 | -22.634899 | -44.8591 | 2024-09-27 00:31:00 | METOP-B | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| db05dffb-00f5-36fd-bef3-89477b8d955a | -22.393999 | -43.941002 | 2024-09-27 00:31:01 | METOP-B | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3204f18b-eca7-3298-ac5d-c5a950fc3da0 | -22.395599 | -43.948502 | 2024-09-27 00:31:01 | METOP-B | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d413a10c-7d54-3e8a-adf6-df41015111b3 | -22.3843 | -43.943501 | 2024-09-27 00:31:01 | METOP-B | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac5df944-1280-36ea-b2fb-6e121795c30b | -22.3859 | -43.951 | 2024-09-27 00:31:01 | METOP-B | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ad2c11c-c49f-304f-a16b-4ca0bf432985 | -22.434999 | -44.127399 | 2024-09-27 00:31:01 | METOP-B | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4a6c2fe4-0615-300b-b3e8-679f44507f2d | -22.4366 | -44.134899 | 2024-09-27 00:31:01 | METOP-B | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e9566c72-b0db-320d-8302-833f91d9cbef | -22.425301 | -44.129902 | 2024-09-27 00:31:01 | METOP-B | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b6fcea63-a304-387d-8d11-39a59ac30de8 | -22.370001 | -44.112598 | 2024-09-27 00:31:02 | METOP-B | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85bc56d0-7b26-3ae6-a809-3f5434b94faf | -22.2425 | -43.908501 | 2024-09-27 00:31:03 | METOP-B | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 111ae2fb-6f88-3891-9189-be8f6e6f59a8 | -22.3125 | -45.469601 | 2024-09-27 00:31:08 | METOP-B | PEDRALVA | MINAS GERAIS | Brasil | 3149101 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 43f9bb37-f16f-3663-95d1-49a6e3fea346 | -22.3141 | -45.477001 | 2024-09-27 00:31:08 | METOP-B | PEDRALVA | MINAS GERAIS | Brasil | 3149101 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2e36bd7d-90ce-3248-9d25-84c17e59cee0 | -21.8687 | -44.223202 | 2024-09-27 00:31:10 | METOP-B | ARANTINA | MINAS GERAIS | Brasil | 3103603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6898013-79b2-3459-bde9-6b3c3c8765a9 | -22.1604 | -45.820999 | 2024-09-27 00:31:11 | METOP-B | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe58fa06-d06d-32cc-9d42-0c9ac48b9e17 | -22.5357 | -47.719799 | 2024-09-27 00:31:11 | METOP-B | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 376c417c-dc66-3d7b-9474-00a27f6b9477 | -21.3958 | -42.945 | 2024-09-27 00:31:13 | METOP-B | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2bd12d02-0af4-36de-978f-88b92a684368 | -21.3976 | -42.9529 | 2024-09-27 00:31:13 | METOP-B | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 39892699-e4ac-3f0b-9e1b-c1c76c7b021c | -21.399401 | -42.9608 | 2024-09-27 00:31:13 | METOP-B | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e966a9bf-6610-3237-a3a4-1c931f0f8e4b | -21.401199 | -42.9687 | 2024-09-27 00:31:13 | METOP-B | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84cd2407-60a9-3a17-929b-8a9a3c7dee26 | -21.403 | -42.976501 | 2024-09-27 00:31:13 | METOP-B | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2cd2f70-f24d-36fa-933c-1ade92a37011 | -21.654699 | -43.955002 | 2024-09-27 00:31:13 | METOP-B | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 96ec98e8-d602-3c32-a5a9-6ea1d9f74ea0 | -21.386101 | -42.947601 | 2024-09-27 00:31:14 | METOP-B | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 871781bb-9e9b-307a-a325-e311fb5dabae | -21.387899 | -42.955502 | 2024-09-27 00:31:14 | METOP-B | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de264aa5-62e2-3787-b621-1a3d2dea7314 | -21.3897 | -42.963299 | 2024-09-27 00:31:14 | METOP-B | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 44f46d30-fc6e-35d3-abd0-3d6ef9d2fc85 | -22.3367 | -47.7467 | 2024-09-27 00:31:15 | METOP-B | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b8da2586-e8c0-3199-8431-e05d3b3c822b | -22.3384 | -47.755199 | 2024-09-27 00:31:15 | METOP-B | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e38c8582-9f59-3ed2-8e39-cc2cfee0dcd6 | -21.952299 | -45.807701 | 2024-09-27 00:31:15 | METOP-B | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0aa511d2-d2df-326e-b51a-580999abe262 | -21.953899 | -45.815201 | 2024-09-27 00:31:15 | METOP-B | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa24291f-5094-3476-9a37-41a3dcdb6932 | -21.9555 | -45.822701 | 2024-09-27 00:31:15 | METOP-B | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 967501cf-9973-3967-9aac-c1457f36dc1d | -22.2075 | -47.301701 | 2024-09-27 00:31:15 | METOP-B | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7503ac0e-6a7f-3116-bcf5-11bfe7786889 | -21.8713 | -45.764301 | 2024-09-27 00:31:16 | METOP-B | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4dfc7f3f-d172-3996-88c5-24218bcb6ccb | -21.8729 | -45.771702 | 2024-09-27 00:31:16 | METOP-B | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e753a7da-3782-329c-8db2-f4852c46caaa | -20.640499 | -41.0578 | 2024-09-27 00:31:18 | METOP-B | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 109bdf42-a3f0-395c-863e-287c5f0fa15d | -20.642799 | -41.067299 | 2024-09-27 00:31:18 | METOP-B | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 631b7c6f-0091-306e-a362-526cee2f66c6 | -21.020599 | -42.662498 | 2024-09-27 00:31:18 | METOP-B | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d2864f8-0fad-35f6-bb1b-c59e02811fe1 | -21.846201 | -46.3815 | 2024-09-27 00:31:18 | METOP-B | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 78a5d97c-3e52-37a7-9445-8c495e24112e | -21.847799 | -46.389198 | 2024-09-27 00:31:18 | METOP-B | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f06cc25e-9e3c-3d10-b7d0-979dac018d74 | -21.007099 | -42.648998 | 2024-09-27 00:31:19 | METOP-B | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c7bcfe87-c04d-37a0-b055-e2b8420ee08a | -21.009001 | -42.657001 | 2024-09-27 00:31:19 | METOP-B | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2c617556-403e-34e2-aa7e-fcf4ddf36663 | -21.0109 | -42.6651 | 2024-09-27 00:31:19 | METOP-B | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b210280-1242-3037-8c3f-d95f83656b75 | -20.999201 | -42.659599 | 2024-09-27 00:31:19 | METOP-B | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c952d84-06ca-37bb-8abb-7a0d491c5ead | -20.587099 | -41.2234 | 2024-09-27 00:31:20 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 360ee982-1da1-3267-a634-4d403f22b7e8 | -20.589399 | -41.2328 | 2024-09-27 00:31:20 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 97f20414-a2b5-3e52-8485-2a1ea1350e67 | -20.5916 | -41.242199 | 2024-09-27 00:31:20 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd5bacaa-4eef-3551-b2f0-0c6bda99dee4 | -21.7838 | -46.926399 | 2024-09-27 00:31:21 | METOP-B | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| de997e78-7e34-3958-8dc1-100398375c57 | -21.7854 | -46.934299 | 2024-09-27 00:31:21 | METOP-B | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 309173a7-8abf-39b2-9199-60bf95448e24 | -21.787001 | -46.9422 | 2024-09-27 00:31:21 | METOP-B | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0aa68b3b-e083-3099-b9ed-7af043a317ca | -20.534599 | -41.177601 | 2024-09-27 00:31:21 | METOP-B | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README6.md)
