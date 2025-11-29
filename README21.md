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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e65e90c-4b31-3320-a580-76b122ad24c2 | -3.24888 | -50.69673 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66cdcf07-66e3-34f2-a0b4-cf8c735d35b3 | -5.36076 | -43.02648 | 2025-11-29 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d63fef7d-bd7b-3b71-a315-3b1dc4a5402b | -2.78626 | -47.41325 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f011e2f6-2a53-319b-a855-e27069f4a35a | -4.20346 | -50.34058 | 2025-11-29 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35b818c5-f52a-3911-b219-a4aa4c266a28 | -0.78478 | -52.39591 | 2025-11-29 04:42:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f466d35-e143-3253-a2b4-7ffc43726970 | -2.93629 | -53.28029 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcee65fe-bc90-3e71-9421-8fe0850dd448 | -1.4847 | -45.78935 | 2025-11-29 04:42:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 13e1d3e2-7fbb-35dd-8568-1fa11aa94937 | -2.74369 | -49.32758 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 635442a2-92ee-33c4-a13b-d9b1255c98a7 | -4.76533 | -45.91438 | 2025-11-29 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca00a4fa-41ac-3ec2-a5c6-84675b38035e | -2.93033 | -53.27129 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f8732d9-1c46-3277-8a4c-eeef476414ae | -4.76895 | -45.91502 | 2025-11-29 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60ba745d-4c6d-3400-ae44-6de44ee5f286 | -1.3759 | -52.50856 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95ff1434-d7bc-3a00-b725-66715ee91d8a | -2.93427 | -53.27185 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 048e2b4f-a4a2-3ed2-8559-bf533b35e1fa | -5.57236 | -44.97573 | 2025-11-29 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e08905a-200a-3e0b-b10b-abeba42e0c90 | -2.30956 | -45.81635 | 2025-11-29 04:42:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68b73057-deb0-308c-be0e-8e63feb29383 | -3.77012 | -49.87982 | 2025-11-29 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d5b63c5-41e6-33f4-8bb6-5de71f718fc5 | -2.74963 | -47.14001 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0db3a7d0-f952-3693-918b-8ee469f8db03 | -2.74847 | -49.86785 | 2025-11-29 04:42:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cb09632-5de9-3d65-9364-704eb68bd4cb | -3.03514 | -50.97982 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d40b240a-5609-3f41-9dec-4d4bfcbb3e6b | -3.22141 | -50.32013 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36e3ced8-4a99-3c55-b71a-0cd83b46a044 | -2.74511 | -49.86732 | 2025-11-29 04:42:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c07e9965-351c-3255-a685-a3702f1ba363 | -3.43096 | -52.07157 | 2025-11-29 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a14837a-ad0c-3300-be87-633adeb8da98 | -2.64321 | -48.0374 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58718c80-132d-31f2-bf56-287bcbeb8163 | -3.63733 | -51.99487 | 2025-11-29 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68a14952-8c5d-3c66-a676-af4f5fb90db2 | -3.33423 | -42.49944 | 2025-11-29 04:42:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6764ccc6-40e8-36e8-82c4-e9aa2d1ff793 | -4.99946 | -38.54041 | 2025-11-29 04:42:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ee48b485-b6ac-39e6-bf93-dac4fc5a13f3 | -1.40923 | -55.39133 | 2025-11-29 04:42:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 052abcb4-3cd9-36bc-b323-8dfc6ba630f9 | -3.06185 | -50.35526 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b43a4f8-88a7-3e20-866e-5aaee5e19ffd | -4.63323 | -43.98859 | 2025-11-29 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cec2806e-661d-37e3-bf7f-f5c1cc6c81f2 | -2.38511 | -48.60192 | 2025-11-29 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c3f689a8-3221-3c2f-9bde-591ad5259bb8 | -1.08886 | -53.182 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6658e97-3a98-30bd-8fdb-f48fce79a14c | -2.79018 | -47.43205 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fe23732-2985-3838-8564-0c2c63c1bf7c | -2.8948 | -49.46543 | 2025-11-29 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd3e4b90-9197-3b3f-83fb-02182c19e289 | -2.64043 | -48.03341 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05aaf46e-bd66-37aa-84b5-2071e38ff119 | -3.20899 | -46.81688 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 542d72a7-d464-3827-9916-c9c09b61d038 | -3.32075 | -52.98982 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 312ad60e-ec8c-3e9f-8980-224c088edbcb | -3.33128 | -50.26666 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b97a87be-57b4-3edd-9726-c475f17221e1 | -4.08271 | -45.74683 | 2025-11-29 04:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdf4f1ee-8b3a-351a-aab8-96f5cba7bcd1 | -4.08553 | -50.75046 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbbf48be-9bfb-3e39-97e1-c9289836bc4d | -5.00303 | -38.54285 | 2025-11-29 04:42:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e5291c9a-d595-30be-9b1b-bb9e2bfe2d4f | -3.95229 | -44.76811 | 2025-11-29 04:42:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cde3ade2-9a52-35d6-abb6-a998b719835b | -2.79292 | -47.42503 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ee86a11-5200-36ae-acff-da2764a76d9c | -2.6413 | -48.54305 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47966580-ec90-376a-9c4b-be7dffdd14e4 | -6.78378 | -41.71142 | 2025-11-29 04:42:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8f9a3cd8-4b73-3538-ad35-b305c3fcde8e | -4.37567 | -43.74329 | 2025-11-29 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f05c6ca5-0bcc-3724-9e01-25a9f623b454 | -3.03227 | -50.97548 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9421930-7037-386e-a1cf-b0f32d537477 | -2.75035 | -49.32862 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f3f3d8c-bebb-38b5-a00f-fecfcafefc1a | -2.64764 | -48.03098 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15a092b6-ca91-3913-8b0e-01893c1e94be | -3.03575 | -50.97602 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76a63672-8701-3d08-8be0-0dbe8a75e151 | -3.58368 | -44.54494 | 2025-11-29 04:42:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d12af013-6192-37af-801c-50c5a7e20716 | -6.69673 | -41.45692 | 2025-11-29 04:42:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a185a914-740a-3b1c-aa19-2ae22d038f84 | -4.01309 | -49.11589 | 2025-11-29 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81b2a657-195c-3b43-b219-cadce5edf529 | -2.73875 | -45.25809 | 2025-11-29 04:42:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5f80860-89a7-3c38-b533-1e565defefa8 | -5.24076 | -41.24297 | 2025-11-29 04:42:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 76d13178-7e01-3db6-99f6-17beaf08d4fc | -2.22207 | -47.51469 | 2025-11-29 04:42:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b2d8d8b-17e3-3e9d-bbb7-cedb615385af | -1.76008 | -54.7788 | 2025-11-29 04:42:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9960a2c1-679b-3787-8064-7cc505ccee95 | -2.30849 | -48.40256 | 2025-11-29 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c89537bb-42a5-3b09-99e8-16d01254f3b4 | -1.35694 | -53.09481 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68ae4b97-46da-3f33-9873-052df54eb198 | -3.10968 | -50.21027 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06314252-f415-3bb4-baae-83783ece330a | -2.9034 | -50.40531 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32f6a758-515a-355f-9506-666c706c22dc | -3.3188 | -50.27949 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cbb7b53-8712-3587-8c92-df8357f94c71 | -4.64065 | -49.36412 | 2025-11-29 04:42:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aff0611b-f41f-395f-9951-6e505c54c7e0 | -3.37875 | -50.25199 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55bf01d9-7db2-3bfb-a70b-d0104fc7ab21 | -2.25483 | -51.93559 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20ad680d-1eba-328d-a3d3-15293d5a753c | -2.5392 | -45.39104 | 2025-11-29 04:42:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ab485c26-46a1-31ba-bd49-6df0c7ee22f2 | -2.4746 | -45.8489 | 2025-11-29 04:42:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b2bc3fc-95e5-36f1-8b82-cfb2d8866e1b | -2.93449 | -49.44668 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bb1aab7-ae83-3dc8-8de0-ff791f6c762a | -3.33186 | -50.26305 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b80e69e3-f22c-324c-8132-21c733516e1b | -3.22596 | -50.31343 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad79d7be-fc6e-3991-acb6-efa5075d4e79 | -2.41769 | -47.23247 | 2025-11-29 04:42:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0c601dc-fa58-3f56-a578-2e809ae5548a | -2.74624 | -47.1395 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1d1ed73c-c330-394b-98c6-149ac2365632 | -3.01101 | -49.58076 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea1440c8-2a37-3ab1-af9c-3b4c3636b902 | -2.30496 | -47.73893 | 2025-11-29 04:42:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcb4c159-760b-38db-a56e-cf166cddfb1b | -4.01032 | -49.11192 | 2025-11-29 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 521e1a93-68b3-37c7-92a2-b1a12a91207b | -4.85126 | -38.73779 | 2025-11-29 04:42:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| df4d01ce-fadb-3116-8b8e-ce6a25b1a41b | -4.24934 | -46.1157 | 2025-11-29 04:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 288d5978-4f8c-3863-a0ee-63798c488e6d | -1.28544 | -53.17406 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8802b1d-a238-35a6-941b-2ebf9ae3b210 | -2.30829 | -47.73945 | 2025-11-29 04:42:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00d09a68-85ec-3c9e-b192-5843365b2ca2 | -3.47267 | -52.9883 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7846a4c-7fab-399c-bdc9-21579cb384a8 | -2.64098 | -48.02994 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4abe48dd-fd47-3abf-b21b-089f1aed5f81 | -0.90738 | -52.43933 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9aaf6532-24ee-3f2b-8fde-a209d44d6947 | -2.60334 | -47.34164 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ade7133d-2cac-3832-a7cc-027a0f7bb052 | -2.83766 | -51.8136 | 2025-11-29 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1079fab-cf73-320d-842f-62396aa50981 | -4.93416 | -43.46508 | 2025-11-29 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7d78cc7-8604-37bb-b94c-873958188f83 | -2.64709 | -48.03445 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16df00f6-2379-3e89-af23-cdfe1a506636 | -2.42499 | -47.22998 | 2025-11-29 04:42:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b872bc4d-9cf5-36a0-abdf-a0666dbcd620 | -3.63837 | -53.98448 | 2025-11-29 04:42:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e00399d-df27-3c41-85eb-f841931e7998 | -0.90971 | -52.43752 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c85a3e2-dc55-3186-934e-ac846a104f2b | -3.40792 | -53.26335 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 289071b9-98aa-36eb-b507-5cf9c908da2a | -2.63711 | -48.03289 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dac75424-9b2e-3b93-9b5c-44232fc7bd12 | -2.96419 | -50.99299 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9491455e-2bc0-3ab7-af9c-867267082a71 | -2.63081 | -48.54494 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c96ee03e-4afd-3004-a0de-604c4efc35bf | -2.47268 | -50.23742 | 2025-11-29 04:42:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5e6cb08-e10a-3f52-ad96-f0b54b42eca6 | -2.7498 | -49.33209 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48211f22-fdd7-38ad-a8cd-89de2ade2fd3 | -4.42338 | -43.3088 | 2025-11-29 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 893e3f0b-cc83-3ca4-b119-8615de628141 | -0.8731 | -48.65746 | 2025-11-29 04:42:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 991359fa-5e35-33e1-8635-8138564bb9e3 | -4.5217 | -46.47657 | 2025-11-29 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a64f9a6b-6c7a-33fd-a9e8-08fea35689df | -1.28489 | -53.17753 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53700d40-d005-3bf2-a94a-b8689eb27b9e | -2.64818 | -48.02751 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 881a975e-51ab-3fc0-bd24-842e2ef775b0 | -2.95733 | -49.56123 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README22.md)
