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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43a573d0-c99b-3ac5-ad12-75d629aa9a21 | -4.25877 | -48.66777 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0bc6c8c-818d-3216-9c54-d23259339207 | -3.76211 | -43.25291 | 2024-11-26 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6859c36a-7230-356b-a876-b5f354b8fc34 | -3.17804 | -48.43106 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a027d2cb-1a27-3def-8463-a26a195144b3 | -3.18527 | -48.44028 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 7ea87c1a-b129-352d-ba15-69725aa593fa | -3.95962 | -48.05968 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94697c1c-6ba3-3e39-94e8-7d853269fc93 | -3.65852 | -50.23331 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b09ee7b-ae18-3f9f-934b-2cd41f34cb4d | -5.8539 | -39.42644 | 2024-11-26 04:14:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5944576a-7667-3a8d-b93c-0bfc5d87e28d | -1.13426 | -48.33649 | 2024-11-26 04:14:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d4cdb7b-3608-32aa-95eb-884aa5ed3d94 | -2.93869 | -48.82618 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da93ed3b-9120-3ed5-9a2d-7d0a76b48f4a | -3.39246 | -44.17456 | 2024-11-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fa334746-a0f0-3400-b9cd-9693a2f74d4b | -6.2374 | -37.23121 | 2024-11-26 04:14:00 | NOAA-21 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a9b0aaee-f2a3-3b72-8304-8ac49b24144c | -3.98125 | -48.0557 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 321aad3f-b148-3bb5-b1ac-b8312b61724a | -1.93373 | -45.75295 | 2024-11-26 04:14:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1802da65-9d9a-3d21-88dc-facb14df7d76 | -3.97186 | -48.0876 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16fa327f-30e3-3e67-8c85-371e6ce930b5 | -2.29035 | -45.72641 | 2024-11-26 04:14:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cbb295b-b00d-3413-85a7-4a8bc71ae54c | -3.9578 | -48.07079 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3fde32c3-173b-37c3-b8df-97aae2ff7f08 | -3.44967 | -50.00844 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa70a76a-0db5-33fa-8cb8-5230fa4dc90d | -3.96251 | -48.06768 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0c47c05d-6917-3a70-9b78-a94057349a17 | -4.66289 | -47.94663 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7ec2254-8013-3ec7-bd07-c93d23b8e6c3 | -1.93305 | -45.75721 | 2024-11-26 04:14:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 230458e1-5b3b-3c82-a567-2985dcf486bb | -1.6888 | -52.60904 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f704dd57-50f2-39e8-80ed-f09228813a8b | -3.59939 | -50.38383 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d1bb16de-8888-3794-947e-43a0509d407f | -3.95661 | -48.07802 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 94979dda-ca34-3a1d-b1bf-ea8fc5ca826a | -2.91729 | -48.7323 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9aeacc0-f6c3-3cc8-990f-cf41584e265f | -3.41626 | -50.44574 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c76c1fa5-bb54-3dfb-a140-a6341255431b | -1.99135 | -53.29679 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e69fa0d-0303-35bf-9e13-2b569c63994f | -4.26236 | -48.67231 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 71274974-d4fa-3528-b10e-fdfdeb360ca3 | -4.25858 | -48.67132 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ec7f2e4-6401-3ee6-84db-63e007b7529e | -1.06189 | -48.0249 | 2024-11-26 04:14:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f45649cc-5cb4-3ea4-a2ef-68df4119a20d | -4.32373 | -47.533 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 71fd50a2-741b-37ca-ae13-02ecc921658c | -4.66041 | -49.72014 | 2024-11-26 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a9e00df8-aba3-3022-b6fa-4d52e32d8c56 | -3.58911 | -44.92606 | 2024-11-26 04:14:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 108868f3-b13f-3d5d-9daa-751661caa7de | -3.99288 | -48.06155 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60ab6e74-1d10-31b6-ae04-167f7a45cc06 | -3.19015 | -48.43697 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a0e5d67-498b-30da-adb5-11c03d8b330d | -3.34717 | -50.51005 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc4f45ab-19cd-31a0-870b-89c9a92830b1 | -1.60131 | -47.46231 | 2024-11-26 04:14:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ac7d44c-8fb1-39cc-ab0a-b02e00d7bca5 | -3.9554 | -46.51788 | 2024-11-26 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f93b44f-516d-3d2d-b4c0-1e30778a81d7 | -4.37255 | -48.50212 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7121e842-5f75-3f30-bbb9-6d4772651cf6 | -1.82813 | -45.58742 | 2024-11-26 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57c150ee-644e-398b-a41e-faa72ec28cf9 | -5.45295 | -36.87482 | 2024-11-26 04:14:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c619baa9-fe57-3794-a785-dc5a4f934db9 | -3.44332 | -50.01767 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 031c3ac0-8c83-3c6e-b465-3e9c5c230595 | -3.95542 | -48.08528 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e2be572-78df-3d17-8c1e-a59d456d277f | -3.34138 | -50.5147 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3ee4de0-b91f-3690-8113-5a70cfcf2eea | -4.10903 | -44.05593 | 2024-11-26 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9747e44-a5ab-3843-9c92-5da1f72989b6 | -4.65888 | -47.94595 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9925c26-ae7c-30bd-9639-8cf160b01a24 | -3.83755 | -41.56694 | 2024-11-26 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 22648a83-627c-33ef-8354-60f853ef0dd7 | -3.07622 | -49.50063 | 2024-11-26 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee894e1e-52f9-3fa3-9e69-8ca8af675eed | -3.97596 | -48.0882 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1acbc8e6-a7a4-39c9-9f33-abe6593afb1f | -5.07004 | -46.77453 | 2024-11-26 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35650d86-9c21-34cb-84e0-ec23a36a3f79 | -3.38528 | -50.09827 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5b87994-f2eb-3d2e-b481-b45f54f2cff7 | -3.18165 | -48.43566 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 9cd95aef-f840-38a4-b8cb-7eecc3e57b30 | -3.35889 | -41.64848 | 2024-11-26 04:14:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 975aae7b-41a4-38c8-b444-07775ad76050 | -3.97014 | -48.07236 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 8b4ce147-0909-3f3b-954c-5ed07564655c | -1.92112 | -50.57784 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef8e35b0-54a2-3c5d-a25e-b9752c3fb0d7 | -4.43065 | -48.70614 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8515f861-950c-365a-8ddd-49b5c0e66012 | -3.53766 | -50.45612 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e8ec0ea-e404-32c4-9bf0-5d36931537ea | -3.37948 | -42.21699 | 2024-11-26 04:14:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f25c012-7873-3386-ac81-e35f12c9c13c | -3.9125 | -42.41981 | 2024-11-26 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| aaaf8f91-73fa-38bc-b6cf-724f854ee551 | -3.96073 | -48.07856 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3e73d380-c4c3-30f4-9fff-0637f01a2dc4 | -3.96775 | -48.08702 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c2e8fe47-7be1-3295-80d9-64f51b03a0d6 | -3.41793 | -50.44426 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0553d0c7-e7f5-3461-baf8-ffc3d7848e2b | -4.53902 | -43.28725 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a256a23f-f4c0-3ba0-b70b-0c39b0bfac63 | -3.96424 | -48.08276 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0d08acbf-2210-35f6-bfe6-4c7e7a7d5fd1 | -6.83378 | -35.34495 | 2024-11-26 04:14:00 | NOAA-21 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a08c2988-dd62-3f6e-971a-b3d7552484eb | -2.45684 | -46.55859 | 2024-11-26 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1fba602-1951-3255-a004-df60ad18a1f8 | -1.78132 | -52.73534 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ff75040-31ed-3562-bf9f-935ea0514a7a | -0.87848 | -51.7223 | 2024-11-26 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf865a7d-225d-319d-91f0-12066ad1038f | -3.5394 | -50.45425 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38facb16-1fe1-3ae9-9ef1-2040596ae5af | -3.97775 | -48.07722 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4f26d790-2225-36e9-a2d9-4fcba57ff7a5 | -3.95192 | -48.08102 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f146f742-50e3-3144-a321-d8c3d25870c7 | -2.09536 | -45.96716 | 2024-11-26 04:14:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5285cf5-e22e-3982-bcaa-2a686895b85e | -3.99229 | -48.06519 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 874e5ff4-5d24-3fe3-a32e-b0e05c0b2edf | -4.17817 | -48.78959 | 2024-11-26 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daac5be5-df37-38ec-8013-5bfe704079ed | -3.97194 | -48.06138 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| ca7cde06-f55e-3c6d-bff0-3c8a4decbf11 | -2.71094 | -46.25974 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e96f4c1a-004f-3ec4-8b97-0b699013d2bd | -4.54125 | -43.29466 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 55a373b3-f5d5-3e7a-85c8-f8681e19f1ca | -3.6854 | -49.01124 | 2024-11-26 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6948980e-78ab-3a8d-8089-533cfef5b74d | -4.66634 | -47.95078 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d96854b9-bf05-3538-a283-214f19baee3e | -4.35711 | -43.31836 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcb1db3a-1d8d-3532-9758-af46eab6c467 | -4.65831 | -47.94945 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b29f327-c08c-397b-bded-80d341f2c304 | 0.48752 | -50.94964 | 2024-11-26 04:14:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91bf7ec7-a7c9-3959-b34e-ac26ad588310 | -3.65979 | -41.54711 | 2024-11-26 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0b8a8786-c91f-3bd8-a519-ac28ad61512d | -2.54289 | -46.89622 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34e7a1f4-149e-3ddf-9ea5-9d78ac8b313b | -4.37675 | -48.50275 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d93fc91-5bcd-3a2c-be3a-bb5c8e40d053 | -3.18653 | -48.43238 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| a2612cf7-93c7-33c6-92b6-3c0da33d60b0 | -2.58745 | -47.4519 | 2024-11-26 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90057c8f-c158-3de6-a697-dc80c4203ff8 | 0.67355 | -50.79803 | 2024-11-26 04:14:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80459fbc-2b8e-3b62-a67d-7b4c9601bb08 | -3.98008 | -48.0629 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c920ff4a-3661-3e8f-ba47-8c7035d5d8c3 | -0.94038 | -46.78192 | 2024-11-26 04:14:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db60c26f-ae5d-3773-8c3e-f120945f3167 | -3.1774 | -48.435 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bca470f8-0df3-34e8-8f17-1f3249a3ec5f | -2.60252 | -45.40551 | 2024-11-26 04:14:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 664188ea-6f82-340e-87b8-66ca0fb16188 | -3.39207 | -50.09256 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4049336f-3b48-359d-9c81-affb6fe2b003 | -4.31826 | -47.51681 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 53e6488c-1448-3a98-98fc-c49d42578ba1 | -3.86241 | -49.14339 | 2024-11-26 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48bc6392-cb64-33ab-a0a3-c7bdac39ed41 | -3.38648 | -50.09688 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e485fb6-f0f2-31cc-ab16-8ea70c71ad4e | -3.95894 | -48.08949 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9476db75-b885-3bf6-8069-827b97518eb8 | -3.47329 | -50.25451 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0da8c428-edc7-3397-98ba-7e19c8599461 | -4.32867 | -48.5864 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5117dd6c-4023-36d6-a72f-d4686dd62401 | -4.25238 | -48.73181 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f5c3404-e772-319b-9304-f539bd56e5ee | -3.80973 | -46.5938 | 2024-11-26 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README18.md)
