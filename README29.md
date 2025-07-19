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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2f080f5-527e-3b72-a36e-e6abadd814b1 | -14.70282 | -45.06846 | 2025-07-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df45c6d5-db21-3d71-848a-915d8f0ba20a | -10.98053 | -68.52312 | 2025-07-19 04:59:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e49c8dc3-5764-36d2-9eae-b96d40870562 | -10.98253 | -68.52615 | 2025-07-19 04:59:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83b5b9a2-ceb8-3dfb-83d2-1e6fb1476ea2 | -14.70229 | -45.07327 | 2025-07-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04b6388e-9cce-397b-8bdd-dc84d17a230a | -14.16927 | -58.19993 | 2025-07-19 04:59:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69c41d49-e2a5-3e02-9e56-1f9d6c1a86cb | -14.1802 | -58.1979 | 2025-07-19 04:59:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f05f30d0-b47e-3ee5-853d-8c0919b44ffd | -14.48281 | -46.35941 | 2025-07-19 04:59:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7efd7bd-66b5-3e10-9407-83ed304b67b6 | -18.65777 | -55.72449 | 2025-07-19 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b65b3374-9a21-3d01-9c3b-92e772707f9a | -14.70389 | -45.05886 | 2025-07-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b38bc90-665a-3ff9-98ee-21bf82b589b5 | -14.70937 | -45.06434 | 2025-07-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a92e3cc-b1b6-3e02-8123-41840f9bf9a2 | -14.83635 | -49.12034 | 2025-07-19 04:59:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31f0e6c9-f8ea-324e-b5fd-1afdf718a8b3 | -14.69787 | -45.0581 | 2025-07-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0df0b8d-d58e-34c4-9322-f2351b9f7664 | -14.84036 | -49.12575 | 2025-07-19 04:59:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6d093b0-b39e-326c-b279-9a89857abdee | -14.69631 | -45.07222 | 2025-07-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de750563-5517-30cc-9a1d-16d39a7b2543 | -18.65721 | -55.72827 | 2025-07-19 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0235534e-7ebe-34ed-b4e0-ca561fc45e9b | -16.89915 | -52.67812 | 2025-07-19 04:59:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a819343-c6b9-34d9-a58b-4cc9cacac2ba | -16.89953 | -52.67542 | 2025-07-19 04:59:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dae96c1a-19db-39be-ab8e-1fb91829bfca | -14.1727 | -58.20053 | 2025-07-19 04:59:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 180e1375-c359-3cef-ac3e-8625d9f6b7fb | -14.77896 | -48.29475 | 2025-07-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b449f6f7-c59a-31ab-b235-fb6ab7744a01 | -14.47728 | -46.35872 | 2025-07-19 04:59:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 949d9660-e612-30fc-9438-e7c6b96e785a | -14.77702 | -48.29614 | 2025-07-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6654685-9382-3984-aef9-1f22e0fb7a91 | -19.51164 | -43.89087 | 2025-07-19 04:59:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bebb6dd3-51b7-39fb-8844-931265b723f0 | -14.70174 | -45.07815 | 2025-07-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1329e3ea-e555-31c8-a602-be553a0f8b50 | -11.84267 | -63.22658 | 2025-07-19 04:59:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 246e4042-60e4-3943-98a1-85ecd73c2496 | -11.7317 | -48.1849 | 2025-07-19 05:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| f7a16041-7a83-37ab-9c6f-d7146b9c105f | -5.6567 | -43.7161 | 2025-07-19 05:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| e5e6f7e4-a5e6-3e96-8e26-9265544bd244 | -2.9109 | -48.2325 | 2025-07-19 05:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 7a5153e0-2421-37d4-add6-32f5064c5d88 | -2.9108 | -48.254 | 2025-07-19 05:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 5c1ce053-a4fe-3b6c-a479-7047e08d6718 | -21.50017 | -57.0667 | 2025-07-19 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed2dcfae-8333-3fa1-95eb-0a5a197ed1da | -21.04233 | -55.98439 | 2025-07-19 05:01:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 275e966d-509e-3ad9-91d9-2b1624d63175 | -23.32763 | -50.1321 | 2025-07-19 05:01:00 | NOAA-20 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 41f399ea-c8ca-3cb0-ba2c-60c08409a63f | -23.61046 | -49.01211 | 2025-07-19 05:01:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e0e0a36-d067-3855-a890-1d176801e814 | -21.50074 | -57.06297 | 2025-07-19 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a550f898-2da0-3812-a315-6dd6f6ac4a1c | -21.75163 | -52.443 | 2025-07-19 05:01:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d36d2c83-c110-3ac3-a9c3-e4714b38aea5 | -22.50494 | -47.12109 | 2025-07-19 05:01:00 | NOAA-20 | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a95762c-5077-39bb-a76b-8eb60a523683 | -22.9829 | -49.17702 | 2025-07-19 05:01:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5b16c72e-5d51-3efb-be9c-dbb49c9d07a9 | -23.32704 | -50.138 | 2025-07-19 05:01:00 | NOAA-20 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8e1b8f97-180f-39e5-aa8b-74ee52d645ce | -21.03892 | -55.98382 | 2025-07-19 05:01:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2eb7b3fb-fb52-3b5f-a0cf-947220f6e879 | -22.98256 | -49.18031 | 2025-07-19 05:01:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ff30ede-bc4f-3056-923c-5fc588240a7a | -21.86854 | -56.73724 | 2025-07-19 05:01:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6daaa5ca-3300-3de2-9134-7a234ae01be9 | -21.49741 | -57.0624 | 2025-07-19 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba52c19c-fb56-3f2a-9cd6-38abf2536e3c | -22.98323 | -49.17373 | 2025-07-19 05:01:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 47ac538f-bf33-33b8-94fe-6b392e6879e7 | -23.32812 | -50.13632 | 2025-07-19 05:01:00 | NOAA-20 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4cbcf75f-81db-3369-8e30-614a757fe64f | -21.04175 | -55.9883 | 2025-07-19 05:01:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee113626-6c5f-31ee-8a2d-a006653d7204 | -25.96879 | -48.95278 | 2025-07-19 05:01:00 | NOAA-20 | GUARATUBA | PARANÁ | Brasil | 4109609 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3ced2555-e4e2-356b-ae48-698b9e3b9d10 | -21.04573 | -55.98496 | 2025-07-19 05:01:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5255100-2dd7-3181-ba12-beacbab432f6 | -22.97814 | -49.17293 | 2025-07-19 05:01:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9feba2b6-37fd-3b71-88eb-4a6bdb77ac02 | -22.9778 | -49.17627 | 2025-07-19 05:01:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2ed380d-7be4-3390-b0c4-5ad50490fc9e | -22.83338 | -46.84768 | 2025-07-19 05:01:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b09cf2b0-ba9d-3a06-835e-fd9e5c7f53ff | -19.75075 | -53.99959 | 2025-07-19 05:01:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54782868-dbee-3865-9733-6dc9e1bcb0ce | -23.76646 | -49.6354 | 2025-07-19 05:01:00 | NOAA-20 | SANTANA DO ITARARÉ | PARANÁ | Brasil | 4124004 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9d8d154c-8738-3a89-ab6a-c30ec372fba3 | -5.6567 | -43.7161 | 2025-07-19 05:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 493dfcfa-fe85-3697-9b52-8bd45d14153f | -2.9108 | -48.254 | 2025-07-19 05:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 47af53b5-c0b1-3137-91f1-1a61098f054b | -11.7317 | -48.1849 | 2025-07-19 05:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 0512fe7e-999c-375a-ba7e-7dbba5a4a13d | -11.7317 | -48.1849 | 2025-07-19 05:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| f6f02040-f69a-3ed4-9523-2bf165322fb1 | -5.6567 | -43.7161 | 2025-07-19 05:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 08aeb857-447a-3abd-b75c-703f1062db1e | -2.9108 | -48.254 | 2025-07-19 05:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 4a905432-a3e0-3ffe-87c1-81543cf1e8f1 | -2.9109 | -48.2325 | 2025-07-19 05:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| cb28151d-095a-3af1-95e1-b5ad117a5a89 | -2.9109 | -48.2325 | 2025-07-19 05:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 6d4da344-cb6f-31aa-91ef-6bd385ea27dc | -11.7317 | -48.1849 | 2025-07-19 05:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| f30e1624-ea4e-371e-ba8e-d2f9d1d2f7ad | -5.6567 | -43.7161 | 2025-07-19 05:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 8cafa309-c418-3506-b1c4-0f702a87c1bf | -2.9108 | -48.254 | 2025-07-19 05:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 102f50ed-946b-3098-938e-cd8d57b4fe15 | -2.9108 | -48.254 | 2025-07-19 05:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| a4735df2-7176-3981-b1d9-d1cb36a56dea | -2.9109 | -48.2325 | 2025-07-19 05:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 24ca307e-6a36-3522-a9bb-87a599f6ebd7 | -5.6567 | -43.7161 | 2025-07-19 05:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 42d42cfa-29de-38f4-83bb-e676b4e18cf4 | -11.7317 | -48.1849 | 2025-07-19 05:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e16a5252-4c77-3d41-a460-4d03df0c9e7c | -6.78362 | -58.63194 | 2025-07-19 05:48:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13bc15d0-df45-37d4-834a-50d12fd34ae6 | -6.78872 | -58.63272 | 2025-07-19 05:48:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 160d0be0-3abe-3408-a2db-eff663926973 | -2.9109 | -48.2325 | 2025-07-19 05:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 656bafbf-a875-3c3c-86d9-188b18f0c729 | -2.9108 | -48.254 | 2025-07-19 05:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 6e04f6f3-793a-3c86-81b2-34c341c7723f | -5.6567 | -43.7161 | 2025-07-19 05:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 8cd794d3-52b8-368a-833a-aafb8d84c0fc | -11.7317 | -48.1849 | 2025-07-19 05:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 85513e63-3d77-3ff6-9977-674cc9616139 | -8.97055 | -61.50621 | 2025-07-19 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 619eddd5-0f49-365e-9b89-20be27714bb5 | -14.16866 | -58.20251 | 2025-07-19 05:50:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b76ee576-4a69-3a2a-94da-464b2b9c249b | -10.04278 | -67.82308 | 2025-07-19 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6355cdc-b21b-31cf-91f0-5188bc2a920f | -9.02362 | -61.22305 | 2025-07-19 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bec9c2b0-4fbd-3b77-853a-0e97fc6dd966 | -7.90767 | -61.51242 | 2025-07-19 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d231d095-9944-36fe-9b95-f072dff47973 | -14.17494 | -58.19905 | 2025-07-19 05:50:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9c8a2567-50cf-3a2c-a26f-43061c10d695 | -8.49482 | -70.97249 | 2025-07-19 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fef30df-61c6-30d7-8890-6f99b0e728b8 | -11.8948 | -55.45138 | 2025-07-19 05:50:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d07817dc-d005-36c5-a7d3-87adc9d48fb1 | -8.30513 | -55.11005 | 2025-07-19 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5cf5496d-6900-3e26-b70b-76e5863eeabb | -11.845 | -63.22751 | 2025-07-19 05:50:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92a19235-e950-39e2-9a71-c8575be3319a | -9.53622 | -66.13815 | 2025-07-19 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb62a025-afee-3bb7-a18b-051d08a9d92c | -12.25952 | -63.82138 | 2025-07-19 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f5b9021-86bd-3e84-99a0-87c8af237dc2 | -9.01737 | -59.76915 | 2025-07-19 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5adf2fc-0b43-35dc-9320-67ea2e68136f | -9.02441 | -59.7697 | 2025-07-19 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c337604-4258-3bf8-8456-a89130685b8f | -10.04224 | -67.82657 | 2025-07-19 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d66fd172-1c38-35dc-b89e-506927bc58b1 | -10.98381 | -68.52294 | 2025-07-19 05:50:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44ab2a2e-305c-3d10-999f-13440fd4fffd | -14.16913 | -58.19827 | 2025-07-19 05:50:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8cf231b4-3467-3c21-aa36-5f21c668386e | -9.71136 | -63.308 | 2025-07-19 05:50:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dec5dbbe-2d28-3789-aa3a-5c3cc769777f | -9.01467 | -59.76823 | 2025-07-19 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 784a599c-7e16-3453-a671-fbaf53ec3fa7 | -7.48997 | -63.82273 | 2025-07-19 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b10af709-eb8a-32fc-849b-393c9fe3ae6b | -10.03893 | -67.82605 | 2025-07-19 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e64188e5-69c1-319b-bad6-0cf0a3bdab5a | -12.2583 | -63.82407 | 2025-07-19 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ca7c2c8-0a33-3970-b478-1482a5f19147 | -7.49048 | -63.82058 | 2025-07-19 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5f0a661-c101-3211-9dd5-3135f97dcade | -9.02224 | -59.76992 | 2025-07-19 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd0f8a80-b0cb-33e1-bb65-fc9f8c1af7c7 | -9.02423 | -61.21867 | 2025-07-19 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a16ef82-84b3-3be5-be03-6c7eecb48963 | -11.89548 | -55.44541 | 2025-07-19 05:50:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33064097-6f28-3db2-a6ea-972007e14cd4 | -14.18075 | -58.19982 | 2025-07-19 05:50:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 59a6ee39-e2f8-3313-ae98-3d1144b00ad8 | -9.01953 | -59.76907 | 2025-07-19 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README30.md)
