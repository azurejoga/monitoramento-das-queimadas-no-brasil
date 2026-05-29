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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a4db9f0-e949-374b-8b58-7ca6111402d3 | -11.30109 | -54.03182 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae6122ae-4c8a-3f3e-a8d9-8ce5183b1d78 | -8.68657 | -48.30332 | 2026-05-29 05:14:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72c12373-7176-33ee-b205-383c85ca0776 | -8.09796 | -49.38331 | 2026-05-29 05:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5514eb9b-27ea-3349-a7f4-42663e9966bc | -8.71563 | -47.80073 | 2026-05-29 05:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c01d1d5d-61db-35dc-b1f2-111a76e4a02b | -11.30206 | -54.03319 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2547616-921b-37df-a5a1-44941a086440 | -11.29819 | -54.03262 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8099b22b-106e-3f29-a837-ba4fa741e592 | -6.24924 | -48.5704 | 2026-05-29 05:14:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b3ebfb3-933a-331d-b5a4-84f4074d2ac9 | -11.59101 | -47.44097 | 2026-05-29 05:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 49e503b8-c38e-3e52-8424-a6635767b04b | -11.27477 | -53.96766 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae2dc917-5217-31f0-ba51-d8ff0e9d406a | -11.96733 | -47.37429 | 2026-05-29 05:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93dbb5a8-4c20-37ee-984c-5e237a16eae3 | -9.88389 | -58.56436 | 2026-05-29 05:14:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 490fd3c2-1a8e-39b8-9444-34d5dbaba37b | -8.71259 | -47.79917 | 2026-05-29 05:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b68d5c1-265f-3a61-9629-f71cde555824 | -8.6861 | -48.30689 | 2026-05-29 05:14:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4997d8a-6d20-377b-9e71-d89d06c11a1f | -8.70693 | -47.79831 | 2026-05-29 05:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa8649e3-1306-31be-9dd9-841d06f2dc86 | -11.63688 | -56.86723 | 2026-05-29 05:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2400fae-9dd4-3797-8285-0bd83e07321f | -11.6267 | -56.86562 | 2026-05-29 05:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f8c9110-722a-3dfa-b6b8-5a9edc19c8c0 | -7.50376 | -55.00462 | 2026-05-29 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c79cac5-8edf-32f0-a65b-93137c63768a | -8.68562 | -48.31048 | 2026-05-29 05:14:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e49d5a0-50b4-35f1-b1e1-ba5264c6ec4e | -6.99819 | -44.99872 | 2026-05-29 05:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25db7201-1504-33a7-8fb7-0286d64b9f9c | -11.60155 | -55.33172 | 2026-05-29 05:14:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57a34785-cc8a-3d79-aee8-08c9e3113639 | -6.24284 | -48.57799 | 2026-05-29 05:14:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9654fb7-0a3d-318e-bd83-f473b5670263 | -10.90871 | -54.12054 | 2026-05-29 05:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e479ee1e-f1c4-3c94-a137-ec1da6f9ba3c | -11.56471 | -54.57995 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 928d5cbd-5d01-3eab-b3d6-ed2e5c7b35b9 | -10.49284 | -57.6112 | 2026-05-29 05:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23d663ab-0d91-386f-af4d-8ddd286c91af | -5.94894 | -43.48217 | 2026-05-29 05:14:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d1f02aa9-cd23-3bce-a2b8-5a52cbf1ac95 | -11.27406 | -53.97255 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47b0d05c-f30a-3e45-834b-e6a66093c07a | -11.96677 | -47.37215 | 2026-05-29 05:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fb28ad5-15f6-3159-9d46-10df71ddd1a6 | -10.12978 | -52.40365 | 2026-05-29 05:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3612c90f-a6cf-34b7-b841-bfcbc4ef94c9 | -10.77718 | -56.81885 | 2026-05-29 05:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f58f51d-40c3-3355-b4cf-06c401fb4c2a | -9.60316 | -58.34275 | 2026-05-29 05:14:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ee7bcf7-3171-3125-bfcf-51afc2ebac4e | -6.2503 | -48.56946 | 2026-05-29 05:14:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb8b252a-61fc-3049-a2ac-58d0979bc69b | -6.24808 | -48.5784 | 2026-05-29 05:14:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9529846c-6998-346d-b938-da9032e96c30 | -6.24968 | -48.56736 | 2026-05-29 05:14:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17236d45-543d-3d73-8bfb-6145bee9d08f | -10.98398 | -45.09391 | 2026-05-29 05:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3c8cb636-5f9b-3d91-b827-b2d25dd066bc | -12.00459 | -45.35723 | 2026-05-29 05:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc4e23ef-b648-33ed-927f-795beabe4bcd | -8.68062 | -48.3061 | 2026-05-29 05:14:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89c71b95-dea5-34da-80b7-c0bd92faf472 | -7.34817 | -46.21475 | 2026-05-29 05:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf4b4fc5-2c39-3c72-b28e-ad397fd5e4e4 | -10.98402 | -45.09383 | 2026-05-29 05:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aae96860-a24b-31d9-8db9-cc2c2c516761 | -9.16123 | -46.85821 | 2026-05-29 05:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 170d4290-6e88-34bf-acd8-ea5a4fddc819 | -10.12972 | -52.40416 | 2026-05-29 05:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87bae105-7591-3a41-a3be-c2e353cdbf20 | -7.19353 | -59.83802 | 2026-05-29 05:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ec3b75a-0fbd-3dc2-ad88-f701a2f83c18 | -10.13878 | -52.40095 | 2026-05-29 05:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55383109-71f8-31ed-8d10-b69709b6e738 | -11.5616 | -54.57479 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e7053ae-eebd-3abf-9b33-df9ff407fe93 | -5.03091 | -56.19252 | 2026-05-29 05:14:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b08c469-f24a-3767-9da2-05bdceb70b3b | -8.70432 | -47.79906 | 2026-05-29 05:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 598318fc-e0f8-3484-8a7c-269f7dab1cd1 | -7.6177 | -56.7402 | 2026-05-29 05:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 435f3f49-c62b-32a4-94a3-b626c3f0b43b | -11.56029 | -54.584 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5840f8dc-a8ba-3be0-a82a-64b4b96e2bd5 | -9.16262 | -46.85931 | 2026-05-29 05:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd2df264-76d3-3b4b-b3eb-641de9ee8079 | -11.96786 | -47.36969 | 2026-05-29 05:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7fba642-2ffb-3cb1-9b2b-870988cca617 | -7.00404 | -45.00536 | 2026-05-29 05:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4549a3bb-9614-333b-9c9f-3cc0e95d16e2 | -11.63825 | -56.86353 | 2026-05-29 05:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0adf1db5-bfd2-3890-a539-35c87ccc9d5c | -10.13032 | -52.39973 | 2026-05-29 05:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 255294d5-b9cd-382a-bf7f-42869dd29511 | -7.33567 | -49.86317 | 2026-05-29 05:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ada26763-ae99-37af-8e27-09990a1a4b4f | -10.4881 | -55.6075 | 2026-05-29 05:14:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d68e7a9-8583-306b-8d47-83d277da2ef2 | -11.30496 | -54.03239 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| caf321a1-bfd9-3a24-a6cf-0f272cf93bf8 | -11.78614 | -52.51344 | 2026-05-29 05:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2e4856e-c95a-3a96-9f66-d0b4067dd632 | -11.59648 | -47.44632 | 2026-05-29 05:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b337a990-f71c-3abe-b08e-375e38044c24 | -8.87431 | -48.49765 | 2026-05-29 05:14:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cc478f4-01fa-3a1d-9378-bc0536f39339 | -10.49163 | -55.60802 | 2026-05-29 05:14:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94837ebd-51d0-3fe0-9c64-dc6dfed68c1d | -11.59761 | -47.4371 | 2026-05-29 05:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| dac9791d-3d10-3b45-b6c6-592fcd75da4e | -10.65776 | -49.72283 | 2026-05-29 05:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a2845f5-ced5-32af-ad22-1763d6d378d5 | -11.63066 | -56.86246 | 2026-05-29 05:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f031e22-f5b3-3676-929f-68aff22a48b9 | -5.94802 | -43.48899 | 2026-05-29 05:14:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 07ccad25-1729-3fe6-8444-48b84f3247ba | -11.63349 | -56.86669 | 2026-05-29 05:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f8fdedf-c85a-3d3e-a6be-b1906f332318 | -10.82297 | -46.89191 | 2026-05-29 05:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4595ac6-c53c-352c-88df-c7211bf4bc98 | -11.58499 | -47.4402 | 2026-05-29 05:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5110ff63-980d-3c94-bedc-0a14e4053d74 | -7.62159 | -56.7372 | 2026-05-29 05:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9bd2063-3407-345b-9cd1-3bcea2ee7cd8 | -11.46353 | -52.92017 | 2026-05-29 05:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8abe6fad-adbf-396f-a974-bdd90c489fcd | -11.56094 | -54.57941 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8366891e-2506-3964-97c8-7040e415595b | -9.60703 | -58.33979 | 2026-05-29 05:14:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfb5d63c-3f6c-3a2a-8bb7-fc79eddacd07 | -7.34051 | -49.86386 | 2026-05-29 05:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 588b45bc-3635-352f-87f5-e1e27215a4ad | -11.29722 | -54.03125 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c98bf726-72e1-30c5-b5df-0c45fd19c27f | -9.16064 | -46.86262 | 2026-05-29 05:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fabadcb9-44bb-3a5b-849d-f62addd7add0 | -7.8092 | -61.46772 | 2026-05-29 05:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c721045-5933-31e4-8ec5-5e93705179a5 | -11.83009 | -49.79164 | 2026-05-29 05:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d6f573f-f3e0-330a-bd4f-e53ede19f1e6 | -8.68109 | -48.30256 | 2026-05-29 05:14:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7fa03c4f-77e8-3632-bcce-6938a6b03e40 | -11.78184 | -52.51283 | 2026-05-29 05:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 221a7e44-b410-3c60-bf94-da76ef36aa3b | -8.71616 | -47.79687 | 2026-05-29 05:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99ee45e0-37da-34ad-904a-a247c927bb51 | -10.97762 | -48.15516 | 2026-05-29 05:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3026ed17-5a57-3121-8d82-1d420f0ec699 | -11.63123 | -56.85875 | 2026-05-29 05:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 481c220d-f77c-3d56-bd2b-14bd8a32699f | -10.13455 | -52.40033 | 2026-05-29 05:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59feaa37-8d83-3b89-bb5f-307746bc28fa | -10.03389 | -59.34697 | 2026-05-29 05:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df6903be-5e1a-3f3f-a963-3913a6fb6ce3 | -10.81799 | -56.59498 | 2026-05-29 05:14:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5385b47c-5861-38aa-8f6e-1e03ad0cbf35 | -10.72029 | -49.03255 | 2026-05-29 05:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8135b63c-08f4-325b-accc-08868eaa09ca | -12.01147 | -45.35804 | 2026-05-29 05:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 414da9e2-24a6-3536-a90b-c2232da7887e | -7.0048 | -44.9996 | 2026-05-29 05:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 80b2e8b2-a602-3ab4-8ef7-9cc5f125bccb | -10.13028 | -52.40023 | 2026-05-29 05:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56805f57-2639-36ca-a0cd-3252661003e6 | -11.79045 | -52.51405 | 2026-05-29 05:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dccd421c-17bc-30ce-927c-8c1004d5f2d5 | -11.82969 | -49.79479 | 2026-05-29 05:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7309b800-f4a1-3d63-8734-526780139cd5 | -11.3018 | -54.02696 | 2026-05-29 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdcbd956-1dfa-3030-b348-5b973ed1b75d | -11.33358 | -51.403 | 2026-05-29 05:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 134a1c7d-8ff1-3793-a892-1810d219c712 | -10.71451 | -49.03509 | 2026-05-29 05:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9394f7fd-23ba-33d3-8cd9-c7c9c740b1f4 | -8.71957 | -54.99461 | 2026-05-29 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f35d4711-9d67-3d7c-b452-16c76d9b6289 | -10.82242 | -46.89637 | 2026-05-29 05:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d77ea7ce-374e-3fa9-a93b-2cab4f8b8804 | -11.44737 | -55.11063 | 2026-05-29 05:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| baf1ffe9-88b2-3e27-844a-b5cc5a148580 | -10.52359 | -48.10549 | 2026-05-29 05:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0749902d-241e-3716-8cf3-d8edc83eda77 | -8.09754 | -49.38636 | 2026-05-29 05:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea1cde97-f5ae-39d7-bac4-b738f2242939 | -7.35432 | -46.21567 | 2026-05-29 05:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0e0698f-0bac-3da7-88c0-248c84f2104d | -10.03331 | -59.35056 | 2026-05-29 05:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e21a29bd-bf16-3533-b5e7-afd63e6aec20 | -5.95513 | -43.49013 | 2026-05-29 05:14:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README10.md)
