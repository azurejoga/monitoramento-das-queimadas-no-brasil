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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11b16823-c0ae-3713-bf33-6ba17465c2d7 | -3.51264 | -53.82308 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6375a53f-2132-3d3b-b5bd-ee42f658104a | -4.11428 | -48.48759 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8181ebf-45c1-3f45-a75c-db1134d8c438 | -2.17759 | -53.80075 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb943c86-5244-330c-b36b-5ebf6293bfdb | -3.03824 | -48.50659 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05a077a4-2feb-37b5-bb25-a0b615246873 | -2.69915 | -51.9942 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 237bca24-d976-3085-a1dc-7a42eeb7d692 | -3.2904 | -53.85395 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87dfc49a-754b-33d1-9436-fb167da4d521 | -2.16259 | -53.26881 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ec22ae4-bcc1-3f85-9b16-b7ece6d4cfec | -3.32596 | -50.06006 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6183f8ed-af1b-3517-b885-bf6604aea929 | -2.24744 | -53.46504 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75208a3e-0b44-3c26-88c7-c26128bbaec7 | -3.2591 | -53.27253 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e051779-a8d7-3b4c-9720-d05e44dc79e0 | -3.38849 | -44.17265 | 2024-11-26 05:01:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 14109f2c-2719-3aa2-81e1-762b1ac686c1 | -3.42602 | -54.02629 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cfd45d8-e78a-3312-8805-053353702933 | -1.88408 | -53.32908 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 322fd303-f917-30f9-9bc0-dbb5bfd23240 | -3.9692 | -48.06758 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 313dde02-70d7-338c-9cb7-6d1c0bc79a13 | -4.03273 | -45.54346 | 2024-11-26 05:01:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cd8e38b-8a1c-35f4-a4b8-ef67529a4538 | -3.41786 | -53.88085 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f59c246d-2e44-3c07-a829-8b2549c051f7 | -2.93242 | -48.8232 | 2024-11-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78f7e60b-7293-376e-a786-66762592e6f7 | -3.42378 | -54.0188 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bde7146-38ec-37ce-9a2d-f62a6f5081e9 | -2.98962 | -49.59125 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb976ccc-0a6c-3aa6-9519-0ab8cd2aaef9 | -3.13514 | -50.56643 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3948961-8b69-36a3-8fa5-9bd9a8612544 | -3.51768 | -50.22052 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be6081bf-6260-34e1-a743-6164e485bfaf | -1.99196 | -53.29035 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eaafebf0-6488-3309-8e49-5b82cd7b2638 | -3.50423 | -53.81102 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 48375a00-cada-30fb-b2cb-48c42d0314f1 | -3.97527 | -48.05854 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 3f538fd8-9f1d-357c-a568-037cb6ae0e15 | -3.26808 | -53.82147 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9de8fb88-76fe-33f1-a71b-d6e5b6df7f90 | -2.44723 | -53.9209 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39cb26da-d0ee-3052-a430-7fc79c64cd46 | -4.31312 | -47.51952 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f3293132-a315-38b0-8bab-d2d06632b3aa | -3.23318 | -53.93509 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbc17131-30dd-3458-af08-3457e9ced94d | -3.22163 | -53.62138 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32f27814-f49e-348b-b22c-3e66562c5c21 | -3.26844 | -50.55884 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dab9df7-d707-32a7-905e-046c7f083cf4 | -2.45179 | -50.36978 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96bcc287-6863-3a3e-b644-4ae020eb356b | -3.97038 | -48.07064 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 4ab823db-92b7-33e3-aefb-5de48472541f | -4.31392 | -47.51407 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ef8d6a2-ae28-39fc-abdd-2d5dc9330541 | -3.24663 | -53.2855 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f8ac8ab-513d-3216-8e34-751939658224 | -2.41267 | -53.9054 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e85f5c42-978c-3b0f-b856-e15523c72811 | -2.43906 | -53.97319 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9a8666b-e697-3773-8f17-969bcaabf75c | -3.42269 | -54.02579 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de009132-90ff-35ee-b7ff-f9880643beb3 | -3.22999 | -50.77912 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8763b50-ed45-38f3-b0c8-5940a3f115c0 | -2.21968 | -53.78937 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a0247c4-0b11-3f6c-b711-37f04fc86d79 | -2.46497 | -53.6975 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed8017bb-0afc-3433-9ed7-4b201774b5ce | -2.6329 | -51.74708 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32c4d983-c75d-3439-bea7-5f57c6cb9ce6 | -3.09756 | -53.73341 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e3ef3cf-f863-350b-8d68-63560865eaee | -3.73372 | -49.95404 | 2024-11-26 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42095801-dbd3-308b-97d5-4ee719ea806e | -8.26679 | -49.54169 | 2024-11-26 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a472ae9a-28af-31af-88be-61e1c57936b9 | -1.68124 | -55.01251 | 2024-11-26 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a67caac-7cb9-3d5e-9525-53a09b493ec5 | -4.31552 | -47.50322 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dff4c4b-0257-3a7d-9682-2553d4724771 | -3.3403 | -50.51212 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea737733-90e0-3069-8f8d-c5dc4d1e1aa2 | -3.0604 | -53.22037 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d5f6115-aff0-3b49-8037-ee7fa5b4e120 | -4.54115 | -43.26545 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c54a63b-077c-3f0e-8450-dd5ced9cb73c | -1.93229 | -53.35112 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92867393-b383-33f9-9e98-5dbe7221b096 | -5.76487 | -47.81785 | 2024-11-26 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 354bfbaf-7c46-3fda-a951-7ba7a4871655 | -4.54146 | -43.27085 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d62a8052-a933-3f46-842e-9d085fca2faf | -3.50703 | -53.81503 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| bfe6301b-f5f3-3b8b-90d0-a1add0868c1c | -4.54645 | -43.28235 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f9192e2f-bee0-3080-92ac-776a2e218c58 | -3.24205 | -53.6357 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6f55984-4938-3006-b7ba-a4d3999dc28b | -2.45664 | -53.70703 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08a13a58-1af2-3b12-8c92-26dc84ab447f | -3.99325 | -48.0655 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01175097-6596-3aca-942f-a40268ed3715 | -3.9685 | -48.07238 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 54318cc9-e648-3bc0-b6fe-fb1f4ede4db1 | -3.23373 | -53.9316 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ff448fa-6785-39b5-b7a7-27a090a7c1a3 | -6.64025 | -47.34559 | 2024-11-26 05:01:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b37ed5b9-e199-3198-b2ce-9a92609d0393 | -2.33269 | -53.87163 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e58ebb4d-e370-311d-913d-917ab90457d8 | -4.30066 | -48.23748 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaea33c3-4e67-3a66-96b0-5e4d62b46509 | -4.3783 | -48.13002 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66dddf14-b26e-3276-93b5-0853a1bfd38e | -3.18131 | -48.57578 | 2024-11-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f43ece-0f52-3bf9-bfc5-815ddc6fa2a2 | -2.45718 | -53.70351 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca1a8a0a-74b9-3ef5-81bf-0bbaec0f1330 | -2.16596 | -53.26934 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9c61d6a-88eb-3426-98a0-8ce9862c1e7f | -4.54497 | -43.29305 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c1f06d97-9877-328f-a46d-0baea31306f2 | -2.98116 | -53.34965 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f03cef2-ef57-3866-8254-c567e7a8ba14 | -6.69836 | -43.06545 | 2024-11-26 05:01:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c89045e0-1557-37f5-a6ae-e9a708a123d1 | -2.79151 | -53.01417 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d45a8bb7-28d0-35ad-9019-bccca31cd6fe | -4.54038 | -43.27079 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 443d1f72-ca04-3e09-9480-ffb5f60648d3 | -1.77066 | -53.62315 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67039903-af5b-30b3-821a-75e7a238eeb1 | -3.68861 | -50.2248 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a9cc4187-6fc2-38c9-8cf4-f096124962af | -1.44435 | -55.20108 | 2024-11-26 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5d87d18-d336-3923-9cd7-f3a5e10c0875 | -3.47139 | -47.68311 | 2024-11-26 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7acdb9fa-4839-3b23-9797-ddf0cb067f59 | -2.82348 | -51.79865 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e3cd1f4-7852-3a4c-885d-6ceca2797234 | -1.99729 | -53.02581 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02dc8d37-dc05-3fc3-a233-c7dd21d90e8e | -2.86164 | -51.57748 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ff29465-2e9b-366e-9046-a747eed76e2f | -4.31472 | -47.50863 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8abf137-4cd0-3627-b465-06708f0db3bb | -3.39386 | -44.17783 | 2024-11-26 05:01:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8054cb4f-6b84-3590-abcd-d7ebcb1eca1e | -3.07468 | -49.50491 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4e69189-2119-3119-8511-e2f2c3073085 | -4.17816 | -48.79105 | 2024-11-26 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbe6d0c4-ebaa-3c0e-a2e1-5c827cd842eb | -2.69148 | -51.71261 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93b13dc8-399d-3be4-9d75-9da8011afd65 | -3.55714 | -49.88435 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d09fc44c-35c0-3efd-b693-116d81215d30 | -3.9664 | -48.08688 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 17e69405-fea1-3928-b62f-811c9e0df416 | -3.22125 | -53.83594 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cd0529f-1791-35e7-ba9b-e35604f5c903 | -6.08078 | -48.03592 | 2024-11-26 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 477baff6-826e-3106-99dd-9f2b859a1021 | -3.22896 | -50.77674 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f31f1a0f-05cb-38f6-8e6f-247d4c76e5cd | -3.98786 | -48.06991 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b602d95-f0c2-30cf-adf2-9c344d42a9b3 | -2.17426 | -53.80023 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b41f1893-bd9c-30b0-b6dc-5503a7369978 | -3.33034 | -53.72193 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60b4d699-d452-38fa-85a1-ae3e076e5c61 | -3.2865 | -53.85696 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6391fb80-14f1-3a9e-b3cd-7cf962235ad3 | -2.90153 | -49.79 | 2024-11-26 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b62562b-7e8e-31e7-8716-7d18803ca48d | -2.79094 | -53.01786 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bac99651-88fb-36d8-a2f7-22e8d33bb3c8 | -3.22261 | -53.93705 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e776a86-feee-3aaf-9fe7-7376edb02ea3 | -2.8623 | -51.57324 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| add705b9-2558-37f8-989f-a02fb1688c3e | -3.03918 | -48.50865 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 732cd8d4-cb3d-37b4-829a-9ffb4fb77ae4 | -3.97384 | -48.06834 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 90d5c61b-6d74-324d-8ad2-edbebd46675a | -3.97059 | -48.05802 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 08005483-f557-32a6-b6d7-74bbb52e32c2 | -3.96458 | -48.06667 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |


[Clique aqui para ver as próximas entradas](README38.md)
