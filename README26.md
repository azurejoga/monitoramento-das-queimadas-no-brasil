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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 682bc9d3-5d5b-311c-a34d-0f74eeacb327 | -10.5773 | -49.1533 | 2025-07-10 05:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| da3125e6-d916-383b-93e7-bf58da8ff510 | -10.5776 | -49.1316 | 2025-07-10 05:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| e4e0c8b0-0de5-377d-b9c3-7484e4d7e787 | -8.5018 | -43.332 | 2025-07-10 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| a538df44-b3a3-36f9-a13b-f72041ce086d | -8.49335 | -43.28514 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| fa4ca2ea-d407-3db4-ae26-4155c65e5203 | -8.50761 | -43.31768 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 8ad7cdf3-fcf9-3ac3-8981-dbe88ce1c304 | -8.4948 | -43.27514 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 136dd9fa-1cbc-3419-9a10-bfea89911c53 | -9.82994 | -41.50017 | 2025-07-10 05:42:00 | AQUA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| fe443771-d166-395c-87e4-ff4b25ebf54b | -10.56926 | -49.14442 | 2025-07-10 05:42:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 560b6b9e-4d12-3052-b419-1a07b814743d | -7.23205 | -43.07775 | 2025-07-10 05:42:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ba36e503-d703-3053-be84-938accbd5024 | -8.50121 | -43.29644 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 177.1 |
| 5b13a10b-f48d-3856-ae33-349af00acc27 | -7.48441 | -43.93539 | 2025-07-10 05:42:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7bbd3f27-bd8e-3746-bfc5-6b8db6fc5a6b | -8.49686 | -43.32629 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 7de930c2-b446-3bdf-a516-35e3b3bd94aa | -10.61648 | -45.23073 | 2025-07-10 05:42:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e71ed18e-734f-3c72-918d-a583dcfda0e1 | -10.62532 | -45.23204 | 2025-07-10 05:42:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 036946a1-d7b3-3955-b7ca-93114e4cbac2 | -8.50267 | -43.28647 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.7 |
| 9545205a-7136-3cb8-91e6-df95fff27539 | -4.21961 | -47.20395 | 2025-07-10 05:42:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| df853fa8-8f43-3591-bbba-508a9541c450 | -8.49626 | -43.26509 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c819f495-c5f0-3427-a009-4502bb4ca3d7 | -9.29762 | -44.84178 | 2025-07-10 05:42:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c65a46c2-4b32-3812-a324-476be26966fa | -4.21799 | -47.21459 | 2025-07-10 05:42:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b982890d-62a2-3c3c-a45b-dffcc5a2ccd5 | -6.85636 | -42.79543 | 2025-07-10 05:42:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 90f33252-807d-3782-ae5e-7111aacce63f | -7.70098 | -45.77013 | 2025-07-10 05:42:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c6c68fc6-beb4-3dd1-96c6-781bf3b5c816 | -8.50616 | -43.32763 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 74ae29a3-e972-37e4-bf2e-b06f362d5fe4 | -6.84552 | -42.80432 | 2025-07-10 05:42:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 29306c6d-c3fe-3c91-bf30-77826c0fe765 | -6.57371 | -42.89994 | 2025-07-10 05:42:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2e4b04f5-ba4e-31cf-a6cd-c07ebb435134 | -6.99569 | -43.49394 | 2025-07-10 05:42:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d0a7f99f-055c-32f6-b46d-0757f6837c38 | -3.75108 | -47.11432 | 2025-07-10 05:42:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5fcbf819-495d-3c76-aa31-47e1401d2591 | -6.124 | -42.95443 | 2025-07-10 05:42:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1dc73e00-df97-3db6-990e-da72d470900f | -5.55041 | -43.89473 | 2025-07-10 05:42:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bcd6b306-be56-3af1-88b6-0f614c5331b1 | -8.49976 | -43.3064 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 443273f4-55a9-3a5b-83d2-9ea5de3e3cf1 | -8.50412 | -43.27647 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 66db4827-2cdf-3243-ac90-3ea222712840 | -6.84697 | -42.79417 | 2025-07-10 05:42:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 93705950-2a47-3e60-8342-c7ff62bee677 | -8.50559 | -43.2664 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 1639ab55-2c5b-3d26-9b71-533505e6d9ae | -8.49831 | -43.31636 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 29fc705e-1b17-3d5f-b56a-7f27a513c208 | -10.57109 | -49.13291 | 2025-07-10 05:42:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 0285bb3c-e988-3569-adcb-bf1c36523f0d | -8.51052 | -43.29778 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a29c89d6-08a8-3fbc-aac0-118b78acd13e | -8.4919 | -43.29512 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| bcd10096-bd28-3c4e-b56b-ec9b02eccdef | -8.50907 | -43.30774 | 2025-07-10 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 3412c466-f43d-3510-83a0-2e34ddf17c66 | -6.99708 | -43.48448 | 2025-07-10 05:42:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1ab5d0f5-da03-3fb0-a20b-6b9b2e794b6a | -3.74944 | -47.12501 | 2025-07-10 05:42:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c2cb9828-1d7c-356e-b6e1-066146b39466 | -10.57294 | -49.12125 | 2025-07-10 05:42:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3e2e1990-7c9b-355c-b942-11e235d8985f | -6.85491 | -42.80559 | 2025-07-10 05:42:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 689f36b6-299f-3de9-8e8f-c3008ce1aba5 | 2.7526 | -60.36771 | 2025-07-10 05:42:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da8c100b-ea23-3dfa-a958-3adc207d5fcb | -12.42382 | -43.71506 | 2025-07-10 05:44:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 80e8c473-a978-32b8-a8d0-61974f31a1ed | -13.03232 | -46.30997 | 2025-07-10 05:44:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7ab97bb8-e59c-377e-a5c0-9fa47641e7ee | -13.15268 | -47.28024 | 2025-07-10 05:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b9c0cce4-3336-3791-a25e-68abe769c9cf | -11.82504 | -48.21489 | 2025-07-10 05:44:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c6b6f788-8f99-3f6f-beb1-11086a0968d2 | -13.01875 | -46.28038 | 2025-07-10 05:44:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 99f8c450-b0d2-3fea-b9ce-74ee8bf215ba | -10.66146 | -49.46406 | 2025-07-10 05:44:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 148d3dcf-6e2e-37f2-a176-3559fef33acd | -11.45754 | -45.09713 | 2025-07-10 05:44:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| aed6fb88-d8dd-3425-8e31-27a4a882c1e0 | -11.43973 | -45.0945 | 2025-07-10 05:44:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a746b1e6-59d2-3afc-b59d-6c8bb427a53d | -12.57166 | -48.87748 | 2025-07-10 05:44:00 | AQUA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 12b605bc-79f1-33dc-a190-98dd0dd2a56b | -11.4651 | -45.10758 | 2025-07-10 05:44:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bb65e6cc-7409-314e-951c-78227926a1df | -13.03366 | -46.301 | 2025-07-10 05:44:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 4ee2c97f-1679-3c2c-8a41-a5e80ea7d50c | -11.45619 | -45.10628 | 2025-07-10 05:44:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 72dd2edd-a32c-3189-9bd2-182342f39ab6 | -10.65129 | -49.46242 | 2025-07-10 05:44:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 9167bcce-5d77-39e7-b650-1083f713ec19 | -13.37255 | -47.89471 | 2025-07-10 05:44:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d181f362-b6af-3642-8de4-69994367696f | -12.42802 | -43.7213 | 2025-07-10 05:44:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d6bf5228-a2a9-3dc0-931c-338bd2dd9b6e | -10.65328 | -49.45024 | 2025-07-10 05:44:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d3f1759e-fe1f-39df-8ec5-47b7cc7b344d | -10.66343 | -49.45191 | 2025-07-10 05:44:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| b14dcd7e-cee3-3b19-8aaa-c86b060b98a5 | -11.46645 | -45.09842 | 2025-07-10 05:44:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 96b0d1ea-0c74-3231-9185-7e81d2910b37 | -13.37399 | -47.88547 | 2025-07-10 05:44:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 17a72edd-c158-3663-9ee8-c1b3587528ef | -6.26817 | -57.40537 | 2025-07-10 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85a2ae04-ba31-3246-924a-618d8688a374 | -7.91538 | -70.92707 | 2025-07-10 05:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4d0778c-53a9-3436-9851-c7551a95841c | -9.28579 | -64.56168 | 2025-07-10 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eba85cde-47d9-39d5-a0ce-5b052f2e549c | -6.80261 | -59.04689 | 2025-07-10 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e371b2c0-8080-38f7-96fb-d13db6a405c1 | -6.62713 | -56.28072 | 2025-07-10 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf0ebc41-815d-31e8-89ac-b1a36d5c2024 | -8.70148 | -64.12062 | 2025-07-10 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a13d1c37-d26f-3035-ac89-e8e585d49264 | -6.62761 | -56.27736 | 2025-07-10 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4cb799f-0395-3998-9432-eddaaabe3cc8 | -10.13257 | -57.77825 | 2025-07-10 05:44:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 575c71c6-a60c-3c1a-8b0d-32a89cd0a9ef | -9.4827 | -62.555 | 2025-07-10 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8edddf67-e7e3-3fdd-b198-5b18aceee764 | -10.23214 | -56.76867 | 2025-07-10 05:44:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56fefec5-14a5-3af4-9941-eae0738f6ede | -10.29766 | -60.54599 | 2025-07-10 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 337ff0fd-c530-37c7-8681-423ecb0463d7 | -9.71837 | -62.16206 | 2025-07-10 05:44:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8c141724-8966-3fdd-a1c3-45c9a386b65a | -9.88079 | -63.1089 | 2025-07-10 05:44:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36b7498c-210a-3591-8418-d160e67aa6d2 | -9.92328 | -59.90281 | 2025-07-10 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b3eb42c-eee5-3541-86c7-f50e99b57a62 | -6.6218 | -56.27992 | 2025-07-10 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9535c28b-5e21-3ffe-8b16-879361bd0dab | -10.22669 | -56.76805 | 2025-07-10 05:44:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 721a0926-c19d-36df-b72c-b2cc078e2ca0 | -10.13218 | -57.78122 | 2025-07-10 05:44:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a4e43424-dd7d-322f-8439-d807cfc5104e | -9.4563 | -63.20843 | 2025-07-10 05:44:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e0b9470-abbb-3aa7-a007-3581832ff0c4 | -9.08869 | -68.47826 | 2025-07-10 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13e2635f-b7ee-3fd8-839a-99e38ee610ce | -7.93218 | -61.55825 | 2025-07-10 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b67c5ccf-ab49-3e99-8a36-dd6862241d6d | -7.89062 | -61.47778 | 2025-07-10 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40dc3547-472d-3eae-a201-74098e09e7e9 | -9.92794 | -59.93347 | 2025-07-10 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae7e6032-92d0-3ff0-b9a3-6d3b75bf6eb3 | -7.89963 | -61.52245 | 2025-07-10 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a6ce8a0-d63d-3f1b-88cf-adad9c7686b3 | -9.73239 | -61.40575 | 2025-07-10 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88c89f53-4dd1-3688-bca5-0ec53c5c3085 | -9.28241 | -64.56116 | 2025-07-10 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17172adc-901b-3a6f-bcf6-39741d1df208 | -8.69807 | -64.12009 | 2025-07-10 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 13b690a7-5ed0-3636-8ebe-fd572b07060b | -15.03207 | -57.19192 | 2025-07-10 05:46:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a719e226-ec9f-3967-9e02-9d66d7588ef4 | -11.78436 | -64.98809 | 2025-07-10 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76acd9a3-133e-389c-9faa-64f6530cbea4 | -11.87514 | -58.713 | 2025-07-10 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2dba8a2-f1db-3a7a-bafe-3182290dec6f | -10.52786 | -68.05171 | 2025-07-10 05:46:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68c11e0c-c1b7-35ba-8610-75f18b6756b9 | -15.03253 | -57.18807 | 2025-07-10 05:46:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f237864d-f856-3c16-bc9a-2be7a6d54f0a | -11.87445 | -58.71843 | 2025-07-10 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5624945c-686e-3304-ae55-1c0f9998a71c | -12.09765 | -64.248 | 2025-07-10 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0b121bf-47ee-37b4-917a-e5f1836cacb6 | -13.33991 | -52.90195 | 2025-07-10 05:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 569294c5-e757-3369-ad55-87bdc415be11 | -12.10929 | -64.02322 | 2025-07-10 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 185af364-9aea-3e1d-a5d3-fb8c901a0727 | -12.10871 | -64.02723 | 2025-07-10 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65f53840-3b37-3384-885a-45c004fe9668 | -11.78493 | -64.9844 | 2025-07-10 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ea861e4-6354-3c33-af14-419648765130 | -18.6521 | -55.72472 | 2025-07-10 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d5eab510-6bec-3b40-ba87-da496ae7bc3a | -18.64566 | -55.72405 | 2025-07-10 05:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |


[Clique aqui para ver as próximas entradas](README27.md)
