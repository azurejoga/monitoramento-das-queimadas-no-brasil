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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1e51e95-d275-307a-b9c5-008580a41a22 | -7.86587 | -44.54376 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b67870f4-356c-331e-9a76-0fefb2687f22 | -7.1633 | -40.21372 | 2025-07-24 04:14:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 07d6c68b-df7e-3742-a0bc-0b71da7d2c4c | -8.08687 | -42.95947 | 2025-07-24 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9734009-3609-31a0-a3e5-dee495e58be8 | -8.92507 | -47.34722 | 2025-07-24 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13ee1074-a48e-3cd8-9337-788c744d67f2 | -7.26005 | -43.07238 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| ae6d4326-e81c-3e44-b663-5988a76de141 | -7.26994 | -44.35453 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09214971-065f-3128-a868-00fa1ff13395 | -6.85723 | -42.79874 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 25c85de7-b0b9-39a8-94e4-4561310dc975 | -3.18158 | -49.45564 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 70882fd1-d856-3fdc-ad6d-0dc12c44ce44 | -9.59737 | -43.87365 | 2025-07-24 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 87e39126-5676-31a3-b999-ae3e39a11241 | -4.31529 | -47.98342 | 2025-07-24 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 213996cd-b75e-34d5-b6e7-8affae3cb81d | -7.30666 | -49.57609 | 2025-07-24 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16180e11-7556-350a-9b37-91533fca0659 | -3.11885 | -47.01007 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57a29abe-cc6a-3850-8300-854d41cfb9c5 | -5.68117 | -43.66521 | 2025-07-24 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb2e696d-2c83-378c-b1dd-f7dc3588adac | -3.58703 | -47.52745 | 2025-07-24 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a2f11ba-b282-3e1d-999f-38531aa9a47f | -8.29784 | -44.97013 | 2025-07-24 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ad32a8f-3a90-3c02-b9f9-24d67bb92b5d | -7.25127 | -43.08522 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 786bb804-8312-347e-819f-173c6f969f7d | -7.24188 | -43.0802 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| bc4531a8-2005-3130-9140-59b5df1cfb72 | -7.83084 | -42.92284 | 2025-07-24 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fac62b06-d02f-37f9-9e17-79aa176fbae3 | -3.22366 | -46.78912 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 6b6d7f45-da79-3da3-b131-5f8f7780769c | -5.89375 | -45.19558 | 2025-07-24 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b488ab9-f844-339d-a3f4-0da85444c314 | -3.94939 | -41.4862 | 2025-07-24 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9c0d5151-e42b-3190-9eff-09942af6471e | -7.84481 | -44.5043 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22580a81-6f00-3a27-9ef2-872efee7d1cc | -7.2595 | -43.07585 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| cb575d6f-d136-32d6-b295-2472ba655e0a | -6.922 | -43.95159 | 2025-07-24 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a24e2f19-b8ef-3ea1-80f4-91a762fa5863 | -5.4819 | -42.15206 | 2025-07-24 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 34f3a832-e5e3-341d-9b73-ceaaa232b246 | -3.17244 | -49.4541 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| cc25931d-646f-366f-bca3-1e17d340574a | -3.36175 | -47.62993 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45a2c155-19d1-3e51-8dae-9547dc968f45 | -6.26427 | -45.27262 | 2025-07-24 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e746f000-c2ff-3932-8d24-9b9db0d1b39f | -6.57383 | -41.50187 | 2025-07-24 04:14:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8fca7f27-d449-366e-999e-e36909da835d | -9.33089 | -44.8521 | 2025-07-24 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cea790f-6c07-3bfb-b45b-44c89d1320d1 | -3.03638 | -49.42367 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca95ca38-1a36-3399-9cb7-7a43bc8aadfa | -7.28103 | -44.3491 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e584b06-7dd2-3f18-9900-c090213b4b9d | -7.55189 | -44.48611 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40e9c49a-9b27-3990-ad12-bb4f6f02d9c4 | -5.61493 | -45.18296 | 2025-07-24 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd90c964-b88e-3118-a8a1-19953c85e071 | -3.46275 | -47.67636 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75779e98-c81a-39df-b51a-6b20ffd22de3 | -4.3042 | -48.10033 | 2025-07-24 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 46df7788-c505-3121-9b25-5995ee5e855a | -4.06045 | -42.52291 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 28478e06-2a43-3615-8d17-269c1661eff3 | -7.27049 | -44.35104 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6728f53f-eb9f-338e-9a02-ccfa33d7834d | -8.49662 | -47.23721 | 2025-07-24 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38172843-8df9-3a44-bbaa-282b43523e11 | -8.49735 | -47.23286 | 2025-07-24 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0631387a-8c17-36c0-82f3-834f2c57b273 | -5.69277 | -50.04855 | 2025-07-24 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2ad1670-9a7c-35ab-b3e2-f9b989090b9b | -6.90925 | -42.79309 | 2025-07-24 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e89c63f5-c65f-3582-aab0-98a4c87e02b1 | -9.32423 | -44.85103 | 2025-07-24 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 080dfc38-bfc8-3065-9797-4b28775f1eb2 | -4.58901 | -43.31875 | 2025-07-24 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b7ae27b-c497-3368-8317-b8a20ee6fafa | -7.25012 | -43.07083 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 03250e0b-7fdc-329f-a0fc-4f8701b68560 | -3.92193 | -42.40982 | 2025-07-24 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 31ebb0a2-2376-35a5-91ab-36a7ae229854 | -6.13811 | -42.96254 | 2025-07-24 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 667b99c2-36bd-31de-879c-9ea5aff1ed72 | -3.03562 | -49.42833 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a1e6dae-565b-33a8-aa44-b24f810f28ea | -9.32756 | -44.85156 | 2025-07-24 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5da3dc02-45b6-3c06-be53-2412b4e9f9a2 | -7.05451 | -40.32495 | 2025-07-24 04:14:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2d0ff21a-7b4d-38a2-abc2-7585e450d311 | -7.72134 | -43.95129 | 2025-07-24 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c35a21ad-4d57-3c31-9038-b14a207c3218 | -5.89434 | -45.19186 | 2025-07-24 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfa5c30f-4004-3ae6-b5e4-4cc07a81b3d9 | -3.16786 | -49.45336 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| d68934f6-31bc-3636-af30-0c5b1d485732 | -3.79587 | -41.00215 | 2025-07-24 04:14:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| dbcd6ba3-22d9-3f1a-b6bd-3c19257797d7 | -5.88688 | -45.19448 | 2025-07-24 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccf6249f-ddc5-32dc-b94a-d1357b489e34 | -4.77867 | -45.3382 | 2025-07-24 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 618aee2f-74d1-32b8-a1e8-0783d4ce2655 | -5.90592 | -42.72762 | 2025-07-24 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d40077ad-0e56-3156-9217-dfea88c03b8e | -7.07327 | -43.91908 | 2025-07-24 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b281efcc-03e6-3773-bb27-030d4d5597c9 | -9.31757 | -44.84996 | 2025-07-24 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc3f5408-b60e-3eea-b0a7-36cf1534b3d6 | -2.58433 | -51.92094 | 2025-07-24 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39fb74ae-61f9-3461-8c89-389e03eb6e21 | -6.81628 | -43.9957 | 2025-07-24 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b13a9294-f31b-3746-adc6-e3464b08ff2f | -3.93436 | -41.49476 | 2025-07-24 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4909dab1-48f6-386a-8e72-c855237e17c5 | -3.18234 | -49.4509 | 2025-07-24 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 4e42e18b-7eb8-33d2-bb20-f296585b4b85 | -9.58741 | -46.32974 | 2025-07-24 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf18b4e8-a971-325d-96ea-6fc71b8bc544 | -7.16822 | -44.37444 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f43bfa2-f95c-36a1-8281-c50eb480842a | -7.24735 | -43.06684 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5381d3c6-00b7-37b6-b907-37b26181f8f6 | -4.17189 | -42.02707 | 2025-07-24 04:14:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eb1406cb-c13a-35e6-b4c9-5fa280c0a327 | -3.05598 | -47.37699 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ecc40307-a294-3a46-9623-eb0aa0007404 | -2.45839 | -48.15187 | 2025-07-24 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 330aaa28-6745-374e-8255-7b3572656e69 | -4.05384 | -42.52188 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e08198bc-ea9e-3fb0-90d7-3a37cf9f3343 | -7.27715 | -44.35209 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65a39c1d-4351-38db-b367-1a0292abdc6b | -6.01586 | -42.91873 | 2025-07-24 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aced1220-6d42-3c73-807c-92b706625714 | -6.8751 | -43.10032 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e081a0e-d0f0-3d7e-b65a-e86e886b8234 | -7.2777 | -44.34858 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a761ae7-60b1-3f82-9376-e193ed472c47 | -3.65045 | -48.32078 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a19a7fab-0d31-3b8c-9b81-f05893e76d7a | -7.55133 | -44.48963 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd7e2911-c30f-3ab2-bf8e-46e3a3584ce1 | -7.54634 | -44.47801 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0b5c773-5c45-325c-a7ac-540177706c56 | -4.91256 | -45.31512 | 2025-07-24 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe3e6f85-b032-34c5-b04a-13ab8e62f7a9 | -5.18416 | -44.95506 | 2025-07-24 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fd6fa81-28f5-3c4a-ab3b-897c75643b18 | -7.25343 | -43.07134 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 5bf740cc-8f93-33d9-90af-ccb86bba69c0 | -6.82665 | -43.06037 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c459ce2-cc19-3f83-bb2c-70194ef6db91 | -6.89438 | -44.21179 | 2025-07-24 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8547d6e6-5715-3893-bc4b-668da5820546 | -4.05661 | -42.52584 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| d6ea058a-1ae6-3e94-a650-dea48e4735bb | -4.78216 | -45.33876 | 2025-07-24 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| fbfc5388-049a-3609-855a-cc4abaad8d90 | -6.81573 | -43.99918 | 2025-07-24 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40972233-17e0-355b-87a9-4a52eaa400a2 | -2.45775 | -48.1558 | 2025-07-24 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bf0e7fc-3374-38a4-89a1-410a87325323 | -4.06152 | -42.51603 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e6f4182b-e3f8-30b9-bbda-f06be1c3cf1d | -7.06996 | -43.91856 | 2025-07-24 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25709a17-9b7f-37b3-8b47-dc5013b1043d | -5.68062 | -43.66867 | 2025-07-24 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e3cf49d-ea5b-318c-af58-0158cc12412f | -6.89494 | -44.20827 | 2025-07-24 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bc9f437-fa09-397e-93ba-b4c90895b0dc | -3.05199 | -47.37636 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5c3f1494-579a-356f-b3b7-8e57838cac3f | -2.58924 | -51.92532 | 2025-07-24 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 493e3422-f2c4-3070-b132-a9ae83e35508 | -4.0483 | -42.51398 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 48aac46d-d8b2-38fd-9793-6ea3ca3fbfcc | -4.80654 | -43.21196 | 2025-07-24 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89f416d8-50df-3cad-aeda-0972fc664f3a | -5.68394 | -43.66918 | 2025-07-24 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ac06d3b-f3ac-320b-be2b-c5f1e974dfb7 | -7.46461 | -49.40575 | 2025-07-24 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0d30eecd-1c19-30a9-b84f-a4e4d2c52e38 | -8.49296 | -47.23661 | 2025-07-24 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb70a123-b8bd-3b16-bec9-5940de9b8e14 | -7.13012 | -44.84587 | 2025-07-24 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32a5f271-41d3-3da7-abd6-476c11fadd25 | -6.39009 | -45.31889 | 2025-07-24 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5000801-4f9c-3e12-81f4-95326445cfee | -7.89211 | -45.54544 | 2025-07-24 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README8.md)
