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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c5c2ab4-ab68-35c8-b99c-124fa0b57e4a | -6.9527 | -43.585 | 2025-02-04 00:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| b93976cd-9b21-3c6d-a452-743858972944 | -6.9715 | -43.5833 | 2025-02-04 00:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| a8c3aa56-13ea-36a3-b698-2838b6f5f1ea | -6.9718 | -43.56 | 2025-02-04 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 148.4 |
| e3579829-7bfb-3211-b575-314048f1b678 | -6.9529 | -43.5617 | 2025-02-04 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| bd8c6657-0e8b-3bc6-bb2a-5180a9fc2326 | -6.9527 | -43.585 | 2025-02-04 00:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 3417f808-99f0-3321-911f-b10a9edce052 | -6.9718 | -43.56 | 2025-02-04 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 68f54509-30b5-3276-a653-174ddd6e547f | -10.2391 | -36.2586 | 2025-02-04 00:10:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 275.4 |
| 4f3cc3ed-ca2b-39c4-a7f7-be1be17b58fb | -6.9715 | -43.5833 | 2025-02-04 00:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| b24add6b-ca64-3aa7-b3ee-4b1192142f5c | -6.9529 | -43.5617 | 2025-02-04 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| b606aa64-f4f5-3395-8718-a751310353f7 | -6.9718 | -43.56 | 2025-02-04 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| f0491262-e9fc-3e3b-9bf2-2aaa6de66b99 | -6.9529 | -43.5617 | 2025-02-04 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| efcf7668-41cc-34a3-b4a1-7aa4b38413bc | -6.9715 | -43.5833 | 2025-02-04 00:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 2b6e1bda-323f-38e4-a23b-6b346d285ac3 | -6.9527 | -43.585 | 2025-02-04 00:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 0ad74d2d-bd70-3b98-8080-b07cb35db666 | -6.9529 | -43.5617 | 2025-02-04 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b724de5b-aa39-3f13-b069-c6ba6a6f9f38 | -6.9715 | -43.5833 | 2025-02-04 00:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| ed7449e6-c041-39a7-a2b2-9a594ca04fa0 | -6.9718 | -43.56 | 2025-02-04 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 142.2 |
| d70f037e-fdf5-3aa2-b7f6-6affddedc665 | -6.9527 | -43.585 | 2025-02-04 00:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 0c128c47-5079-3728-a492-e68e5f0d4b16 | -6.9554 | -43.528 | 2025-02-04 00:37:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 00acf795-b994-3b47-b417-8ef2f39298a5 | -6.9502 | -43.548801 | 2025-02-04 00:37:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d2950b72-e1c3-30c5-be21-996f4acb61f6 | -6.9457 | -43.530399 | 2025-02-04 00:37:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4f8a181-097f-36d1-8d54-f22f02600c88 | -21.082701 | -56.352001 | 2025-02-04 00:37:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a62996a5-add4-33d0-b9c0-54af1dd52470 | -6.9599 | -43.546398 | 2025-02-04 00:37:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1a64e39-8829-3b87-8375-5b9bfaf8d48f | -6.9529 | -43.5617 | 2025-02-04 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b7460363-8a1c-3c88-9d79-6053016bcc10 | -6.9718 | -43.56 | 2025-02-04 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 9c815e90-30f1-3b91-ae59-f988a6b135d4 | -6.9715 | -43.5833 | 2025-02-04 00:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f2f39bb3-d777-3799-b271-ca8126750cd5 | -6.9718 | -43.56 | 2025-02-04 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d72cbb13-716f-33f3-8048-b287169e60fd | -9.97 | -36.46 | 2025-02-04 01:00:00 | MSG-03 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f1720f8-1b30-33eb-a747-e9774db3bff9 | -10.0 | -36.47 | 2025-02-04 01:00:00 | MSG-03 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5391c61e-c5ad-3f76-af9e-926e4afdbd14 | -21.084101 | -56.393101 | 2025-02-04 01:32:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a7f4a097-ac7c-3235-b751-be66393800eb | 1.9316 | -60.380199 | 2025-02-04 01:32:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| eb8cb7de-20b9-3390-afb9-9999f39ad611 | -21.0823 | -56.385399 | 2025-02-04 01:32:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9b1ddcae-bfe9-3587-b83e-e110ccf1760f | -6.9715 | -43.5833 | 2025-02-04 01:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| c951cae5-7d07-3708-8218-df93bba0bc32 | -6.9529 | -43.5617 | 2025-02-04 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 051aa8c1-44f5-32da-9165-e296218ef16a | -6.9527 | -43.585 | 2025-02-04 01:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| bdf297d9-e374-3ffb-8485-c13f4d43ff54 | -6.9718 | -43.56 | 2025-02-04 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 98a9ba9e-ee24-3b7f-86da-b17fcbb6d6a3 | -6.9715 | -43.5833 | 2025-02-04 02:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 5e4b038c-0e36-38d7-81ae-55c63f73c3a2 | -6.9529 | -43.5617 | 2025-02-04 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 8d713779-ce62-3c22-a954-127cdab562a4 | -6.9718 | -43.56 | 2025-02-04 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 4f5a8586-9be2-367d-ab03-f904a6dc9b95 | -6.9527 | -43.585 | 2025-02-04 02:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 23148130-4ced-3868-aa37-8ad8268e8539 | -15.5216 | -42.6588 | 2025-02-04 02:50:00 | GOES-16 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| de09e995-e00b-32a5-9f34-a3b4fdf6cfd3 | -15.521 | -42.6833 | 2025-02-04 02:50:00 | GOES-16 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| d1118723-5ac5-3e9d-b2cc-d8ccbb75dc69 | -5.13596 | -37.59993 | 2025-02-04 03:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c56a5a25-1080-31b8-826d-3b890292f0e4 | -5.13506 | -37.59925 | 2025-02-04 03:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d8a84fd0-8d7d-3d8c-882c-e917c021728a | -7.20517 | -35.22566 | 2025-02-04 03:10:00 | NOAA-20 | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e8b46603-6731-34ea-8197-dd02650da450 | -10.52034 | -42.4314 | 2025-02-04 03:10:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| df2a00e4-7f84-3556-849e-7a85118b078a | -9.07855 | -40.25723 | 2025-02-04 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 267f0490-bd7e-3a3a-8e1b-81bf17c2b8d3 | -15.51554 | -42.67831 | 2025-02-04 03:12:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| d0ca9e59-b3ad-3667-a97b-9c82c7c95122 | -15.51396 | -42.68547 | 2025-02-04 03:12:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 12218635-7973-3fa9-98bb-c42be30c3baf | -22.6737 | -42.86124 | 2025-02-04 03:14:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9217b4b6-b0b1-3bfd-a381-e0d01566eb1a | -22.67479 | -42.85667 | 2025-02-04 03:14:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e6742655-3a66-33bc-94d0-64206fa87134 | -6.9718 | -43.56 | 2025-02-04 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 2aef8f13-7f63-39ea-99e9-81b68cdc28d4 | -6.9529 | -43.5617 | 2025-02-04 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ce7026ea-f1dc-37b7-8958-d31f26c1d84b | -6.9532 | -43.5384 | 2025-02-04 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 163d2f07-ae25-35b1-8f8f-e008e4da7a88 | -6.972 | -43.5366 | 2025-02-04 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| f923cc92-295d-3e4c-b217-af3e39d9dfae | -6.9718 | -43.56 | 2025-02-04 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| aa526301-5839-3ece-91dc-80449a681d76 | -6.9718 | -43.56 | 2025-02-04 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 2b2f2cfa-a032-36cb-9455-df6c77c6bda2 | -6.9529 | -43.5617 | 2025-02-04 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| ef3f8185-5b2b-3868-bec6-3c9a7dc94bdd | -6.972 | -43.5366 | 2025-02-04 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 8a0de7ec-13c8-3a6e-a5e5-a78347a428e0 | -6.9532 | -43.5384 | 2025-02-04 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 205.5 |
| df6abcd2-1f1e-35a0-9b90-207347020987 | -4.4058 | -38.04241 | 2025-02-04 03:59:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2504d6f5-901c-36d0-a1b5-68da07fd457c | -5.13763 | -37.59983 | 2025-02-04 03:59:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0fe94cc9-8849-33e2-8e8b-a639ebf8f7f4 | -7.20718 | -35.2235 | 2025-02-04 03:59:00 | NOAA-21 | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 15752161-aabd-39c9-9e57-e5e8e726ac1b | -5.13421 | -37.59931 | 2025-02-04 03:59:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e2c32a0a-0eec-3c9c-bd43-ec784938cccd | -4.88349 | -38.0276 | 2025-02-04 03:59:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e177ebc6-6724-3578-97ae-31f4538d803f | -5.7802 | -42.59941 | 2025-02-04 03:59:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dd1a9021-ea80-3e56-bd18-f11544f23085 | -5.47594 | -40.60479 | 2025-02-04 03:59:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f8918b9f-8b86-3761-821e-3815b861ffea | -6.43814 | -39.89849 | 2025-02-04 03:59:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f02cd7fa-024e-354f-9506-ad57522f9a0e | -4.69157 | -37.79131 | 2025-02-04 03:59:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3d51008e-c5a5-3e73-9c5d-5150e8ac8ca1 | -5.78057 | -42.59966 | 2025-02-04 03:59:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0a142307-ff18-344b-8fd8-d113cd514d01 | -6.39742 | -38.90979 | 2025-02-04 03:59:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c5f81ab0-28f5-3c99-a2ef-49bd03dc6a8a | -5.08496 | -37.89579 | 2025-02-04 03:59:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9477ba75-4332-3cee-b7e8-3d266da68eeb | -4.58751 | -37.80553 | 2025-02-04 03:59:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ce1e9879-242a-3f47-9e21-d3230fcd014d | -3.35184 | -39.13054 | 2025-02-04 03:59:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dac85924-f2bd-3848-9282-e69ddb80d4ce | -6.972 | -43.5366 | 2025-02-04 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 3ed602ac-5522-38e1-8031-690bd571ff8b | -6.9529 | -43.5617 | 2025-02-04 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| f9679cc0-b3c8-3886-a41d-ff310bf49989 | -6.9535 | -43.515 | 2025-02-04 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0517f292-e8e9-344b-a3e1-f3dc9579376f | -6.9532 | -43.5384 | 2025-02-04 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 4b54463d-e103-30ad-897a-167a1bca9b14 | -6.9718 | -43.56 | 2025-02-04 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| dd66883a-296e-3b37-88fb-a70c90da323b | -6.9344 | -43.5401 | 2025-02-04 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 19e53a47-313c-3def-82a7-de7a04d3a664 | -6.94698 | -43.53975 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8fb16a55-e77d-3a43-a9dd-93a787caf23f | -12.91073 | -41.50124 | 2025-02-04 04:01:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb32522c-081c-385d-b1fe-9e3da309d195 | -6.95066 | -43.54033 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| bf9574fd-cff5-3767-a920-4cb9b62dce84 | -7.60092 | -39.24402 | 2025-02-04 04:01:00 | NOAA-21 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 38120efd-509c-36ae-87d3-96e359c5b9b4 | -6.95507 | -43.53653 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 4e521dec-d253-3172-99c1-9cb330537034 | -6.9728 | -43.56626 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84131e68-9a40-3ac3-a86b-2e109e1ae3a9 | -6.95657 | -43.55022 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9e8c19c7-baa0-3296-8f8d-2ecd38187b7e | -10.5269 | -42.42448 | 2025-02-04 04:01:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 805c9908-25a2-3d76-9f6d-076e51cd5d69 | -6.9684 | -43.57002 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| fbd69a57-4b4b-3b5e-908c-0f83758d6803 | -6.95579 | -43.53217 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d10846f-32f6-359f-a6aa-76be2e39420e | -11.89332 | -40.9801 | 2025-02-04 04:01:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6a4a3f7a-43f9-3edd-a564-8c30e98bcd1a | -6.95434 | -43.5409 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 85e152c3-7454-3411-8966-d0633a2d2c23 | -6.96544 | -43.56506 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b4de5e0a-78d3-3c1a-9228-247646538093 | -6.91451 | -43.55762 | 2025-02-04 04:01:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1766db34-700c-32de-a711-4ebb23264e32 | -9.08421 | -40.25127 | 2025-02-04 04:01:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fee3e3df-b86f-335f-9c92-32170e25dd72 | -7.87441 | -38.01009 | 2025-02-04 04:01:00 | NOAA-21 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a787e47f-5aaa-3848-bb38-34af75cbeb99 | -6.95289 | -43.54964 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 65309fcf-083d-3fa4-b5f5-691f58e6b6d4 | -9.5646 | -35.69146 | 2025-02-04 04:01:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9f452436-4eae-3b10-a616-bc0162ec3885 | -6.95802 | -43.54148 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| f9a2ac84-5b5b-31fe-a3f4-8fb11c02dd0a | -6.96097 | -43.54642 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f65d2c95-1c51-3366-ab1f-7e356f8794ca | -8.93752 | -44.24302 | 2025-02-04 04:01:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README2.md)
