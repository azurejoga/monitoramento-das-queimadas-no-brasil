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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b3240a2-d0a3-33e7-b49c-2f23e6aba04c | -12.55128 | -54.58629 | 2026-06-19 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c525ffd6-478a-3fe7-b99f-96aab6bd2a71 | -13.50096 | -56.57246 | 2026-06-19 05:23:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c59b96df-34ff-3435-b701-2ed372365c6e | -11.48508 | -52.91977 | 2026-06-19 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe019a2e-4b2d-3aeb-867d-b813104adf14 | -10.05675 | -48.09014 | 2026-06-19 05:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 804b46ba-6f23-32e4-b446-5f95b2f2b0e4 | -10.76873 | -54.10673 | 2026-06-19 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3feb208-b50c-30ff-8011-96e81a5b9e0e | -13.64917 | -60.61934 | 2026-06-19 05:23:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d05da0f9-fbde-3b33-ad8d-0cdf154c2240 | -18.97546 | -52.45423 | 2026-06-19 05:23:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a602d6c-38bf-3214-9313-f62cbf67421b | -12.55183 | -54.58228 | 2026-06-19 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4b348e2-9b33-32b2-a9fd-0e202485998e | -16.26447 | -59.99905 | 2026-06-19 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ba1bbb23-4cde-32ec-9d0e-bc67ba583057 | -17.10911 | -49.75678 | 2026-06-19 05:25:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4079c83c-3029-3635-b83d-e7d6d828514c | -15.6463 | -58.01709 | 2026-06-19 05:25:00 | NOAA-20 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11a2a9f6-6c0d-3b4b-a932-b18039af672f | -22.78073 | -49.34933 | 2026-06-19 05:25:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 035fe0b0-5ea8-3597-8f0a-a1e7397b470f | -17.11011 | -49.75408 | 2026-06-19 05:25:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08c68400-27b7-3569-8fd3-bd357d42d6a4 | -17.34735 | -53.8137 | 2026-06-19 05:25:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30d59359-8ab8-3bf2-9825-59e8503e814c | -16.26629 | -59.99923 | 2026-06-19 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 281a3a0b-a9d9-36de-ae16-4d1e329105fb | -17.10961 | -49.75156 | 2026-06-19 05:25:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c6b5b41-2bf8-355b-b402-fae438a4874d | -17.11065 | -49.74878 | 2026-06-19 05:25:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b07be04e-e05e-37f9-a950-cc36f2fa3ffc | -16.26574 | -60.00293 | 2026-06-19 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecca0e60-31a0-3695-a948-dd88723849a5 | -22.78745 | -49.34982 | 2026-06-19 05:25:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbeb8929-b486-3047-aa70-e734afc4c065 | -12.8741 | -44.3593 | 2026-06-19 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 5d7d64ad-8291-3099-9906-b22525efec40 | -12.8736 | -44.3828 | 2026-06-19 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| aab38db6-aa29-3931-acfc-6eeee32f96a4 | -12.8741 | -44.3593 | 2026-06-19 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 40cd7f6b-b556-35c4-98ec-0786fa59a63d | -12.8736 | -44.3828 | 2026-06-19 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 774a5db9-7a8a-3fbf-8f21-09a804d075c9 | -12.8736 | -44.3828 | 2026-06-19 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 62523a25-c9cb-3c68-be77-ecc4a5acb438 | -12.8741 | -44.3593 | 2026-06-19 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| aec822da-f864-3a5f-ab3d-9f45eaa1dbea | -12.8736 | -44.3828 | 2026-06-19 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| bb1a94ca-1483-3f7f-a583-62281acd00ae | -12.8741 | -44.3593 | 2026-06-19 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 4d426f5a-a04e-30b5-9d63-c8dbdc62e906 | -12.8741 | -44.3593 | 2026-06-19 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 2daa30ee-dfa1-3bc9-96b2-eb8042163233 | -12.8736 | -44.3828 | 2026-06-19 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 84356af3-ba60-391a-87c3-c425bd941f61 | -12.8741 | -44.3593 | 2026-06-19 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 6f6592ce-a7e1-316b-9bcf-b3a76469aa5d | -12.8736 | -44.3828 | 2026-06-19 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c7f9c967-a46f-35d2-81a6-223295aa7444 | -7.80075 | -46.45636 | 2026-06-19 06:25:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| be29e1bd-02ce-36f6-be2e-e281bfe3f034 | -4.35088 | -47.75502 | 2026-06-19 06:25:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9b8a471b-84bf-387b-ad32-d66e188606e8 | -7.80214 | -46.44736 | 2026-06-19 06:25:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 21f04eb0-b62b-371f-a553-4631ae82c015 | -6.64769 | -43.91718 | 2026-06-19 06:25:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 47c09d52-6ed0-3a84-8976-e6a4b22862b5 | -4.34917 | -47.7659 | 2026-06-19 06:25:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| cf6179bf-7c09-3fea-b426-b393e31cb02b | -10.55296 | -46.34619 | 2026-06-19 06:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e4979d7c-f54e-3e10-90af-61a105cc8d9c | -10.05254 | -48.09375 | 2026-06-19 06:27:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c34560ac-8a76-39ad-a3a8-d14be624101d | -12.85918 | -44.36935 | 2026-06-19 06:27:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 92a36a2b-7bce-3f8c-9624-0a66ac5b64b6 | -12.87002 | -44.36043 | 2026-06-19 06:27:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2023bff1-6da7-321c-8422-cfb2c6c7d947 | -12.49304 | -43.77653 | 2026-06-19 06:27:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 17cad8a9-798a-35b8-9013-042d558a1060 | -16.02994 | -43.41772 | 2026-06-19 06:27:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 29.8 |
| d61ec9f8-15dd-359c-8da9-7fbf7b39e7db | -12.86855 | -44.3707 | 2026-06-19 06:27:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| a45b1b01-fb25-3741-a74d-6c1ad60aadfe | -12.87792 | -44.37202 | 2026-06-19 06:27:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 0fb121db-8700-3d29-9dc7-5aaf1b0f5a8b | -12.84044 | -44.36664 | 2026-06-19 06:27:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| f190062c-9ba7-3a4c-a0d4-06870abfb6a3 | -12.1368 | -48.25978 | 2026-06-19 06:27:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| faba0aab-8457-3bca-932b-3c179f30480e | -12.49459 | -43.76559 | 2026-06-19 06:27:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 468bc8c9-806f-3ab0-b296-2a77a536271b | -12.83108 | -44.36526 | 2026-06-19 06:27:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| efb6bb40-ebe0-35ec-b7bb-72edc65c7061 | -10.06329 | -48.08543 | 2026-06-19 06:27:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| ebbd005d-976a-36ca-a552-21e00b689304 | -12.86707 | -44.38095 | 2026-06-19 06:27:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7914b332-6a90-393e-b8bc-e66ee465703f | -10.06173 | -48.09537 | 2026-06-19 06:27:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 81332ace-0cab-3417-81d0-c208814c5a9e | -13.93519 | -53.55504 | 2026-06-19 06:27:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 6052c8d7-6605-38c4-843c-4536a9e037d4 | -10.53937 | -47.70816 | 2026-06-19 06:27:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 41185022-35d3-3cea-afa4-c58277a9aa68 | -10.90662 | -46.33429 | 2026-06-19 06:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ac556347-93f4-3082-869c-0c2b12b98d5d | -12.13526 | -48.26946 | 2026-06-19 06:27:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dcdc53e2-f7c0-3533-a3ae-15bceea5b98c | -12.8736 | -44.3828 | 2026-06-19 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a3a20929-53b5-3c61-9315-8d2af44180bf | -12.8741 | -44.3593 | 2026-06-19 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 89612df6-1bc9-3bab-be89-0db2ca340240 | -12.8741 | -44.3593 | 2026-06-19 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 21ea47bb-af36-3804-a49f-ec862ee8bfb0 | -12.8736 | -44.3828 | 2026-06-19 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| db44f7df-986e-3613-b0ea-c56212afcd6f | -12.8741 | -44.3593 | 2026-06-19 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| f782728c-4b4f-381b-9845-8556e5284cfa | -12.8736 | -44.3828 | 2026-06-19 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 73840c1b-f506-3933-8f35-643fd7b4890b | -12.8736 | -44.3828 | 2026-06-19 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 158ad9cf-ee4f-3aa7-b288-1e32cc7a7395 | -12.8741 | -44.3593 | 2026-06-19 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 626f922a-e6d6-39f4-987d-284993c75eff | -12.8736 | -44.3828 | 2026-06-19 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| b164974b-ea22-3d99-9c10-4edb895e0916 | -12.8741 | -44.3593 | 2026-06-19 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 3cc4dfd6-1082-362f-a4f9-63b3a87ff5d9 | -12.8741 | -44.3593 | 2026-06-19 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| bffa7728-8017-3921-9ca6-dd483039457a | -12.8736 | -44.3828 | 2026-06-19 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 9425826e-97de-334b-9f64-776d1708fe29 | -12.8741 | -44.3593 | 2026-06-19 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| bb8be5c6-7424-30db-9ec9-d60dd809d703 | -12.8736 | -44.3828 | 2026-06-19 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| dd56dfc2-72bb-3f4c-a5b7-b5e977e7a23c | -12.8736 | -44.3828 | 2026-06-19 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 2e98aa0e-f148-32ac-82c5-8fac78eed6f2 | -12.8741 | -44.3593 | 2026-06-19 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3fc24cdd-ac46-33d0-bf3e-4718307bd66d | -12.8736 | -44.3828 | 2026-06-19 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 671726b4-9c1f-3624-9035-c88f8d7d20fd | -12.8741 | -44.3593 | 2026-06-19 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 3b8617d4-ce54-387a-ab53-4f8ce54256a0 | -12.8741 | -44.3593 | 2026-06-19 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 8371ee17-050a-3b33-961f-6685ca423ffa | -12.8736 | -44.3828 | 2026-06-19 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| ce834057-4072-315a-8818-d4c6bed9b476 | -12.8741 | -44.3593 | 2026-06-19 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 92bb113c-4e42-3d69-aaae-a5b3f40951d2 | -12.8736 | -44.3828 | 2026-06-19 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 1ddba9a8-66d6-3f6d-8adb-39e244f1d07d | -12.8741 | -44.3593 | 2026-06-19 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 8d26a95b-2d59-37ff-badf-a044687f505b | -12.8736 | -44.3828 | 2026-06-19 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| cf30bf40-9753-3221-9cd6-de92c83970e2 | -12.8736 | -44.3828 | 2026-06-19 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 4b8d3309-0700-3d6e-8cd0-69737cc4ecea | -12.8741 | -44.3593 | 2026-06-19 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 1bcf79f8-6ce1-351d-9de6-ee05444c10f0 | -13.3217 | -45.1479 | 2026-06-19 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 442e77f7-bcda-33cd-80cd-8a39fc12de87 | -13.3217 | -45.1479 | 2026-06-19 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 5d9b12ab-4df2-349e-8bae-9b134fb59768 | -13.3217 | -45.1479 | 2026-06-19 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 346.7 |
| 69e35ea9-2131-396e-97af-ac4ff34611e6 | -13.3212 | -45.1712 | 2026-06-19 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 8b9179ff-20a5-3593-b912-db4877625690 | -13.3212 | -45.1712 | 2026-06-19 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 71c14799-bcc0-3dd7-ba25-065cfef6a5d9 | -12.7939 | -44.513 | 2026-06-19 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 4f3c203a-0cc6-3f5b-b1f7-b404b4f62a1c | -13.3217 | -45.1479 | 2026-06-19 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 312.5 |
| ef7fe07b-19c2-3a66-8c5b-8ebe6d6a45f6 | -12.7939 | -44.513 | 2026-06-19 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 01db8d0e-460f-3ede-954d-9928511727fd | -13.3212 | -45.1712 | 2026-06-19 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| b5aad93a-a42b-3f1a-a0b9-b28ff03f4cb3 | -13.3217 | -45.1479 | 2026-06-19 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 219.7 |
| d0ea13d9-4f34-3a62-b23e-0de0a10ab8ad | -7.66833 | -47.60655 | 2026-06-19 12:08:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 498fe34f-c690-32ca-ac11-179c17fa21ee | -6.91245 | -42.84105 | 2026-06-19 12:08:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 7d5f1964-7b6a-3ee7-afe1-c2fd000018fd | -6.15403 | -48.49857 | 2026-06-19 12:08:00 | TERRA_M-T | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 054042bc-fb14-39af-b22b-9c5d7c27366e | -7.80266 | -46.44398 | 2026-06-19 12:08:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fdaa7bdc-fbcf-35b8-abbd-860c9bfed6fb | -7.18766 | -48.27952 | 2026-06-19 12:08:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a55e91f0-20e8-3f6a-b451-4dcb91e0a0fb | -6.9112 | -42.84724 | 2026-06-19 12:08:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| e71d4dcd-5045-3404-9b8d-6c230514cf1c | -7.80069 | -46.4589 | 2026-06-19 12:08:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 156d2f98-00cc-3f4b-ad0b-698e2f35314b | -13.3212 | -45.1712 | 2026-06-19 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 1998d146-b234-3c36-8ec5-94a26899c67c | -13.3217 | -45.1479 | 2026-06-19 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 197.1 |


[Clique aqui para ver as próximas entradas](README13.md)
