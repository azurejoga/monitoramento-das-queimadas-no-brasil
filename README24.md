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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f41e04e-3d00-38f1-818c-98de7c353d3d | -11.79685 | -56.99873 | 2026-07-02 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 60871436-c75b-3e54-a759-8ee26512ad54 | -11.79669 | -57.00198 | 2026-07-02 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| eb9f65a3-a791-3d0b-9343-1188ef0cee83 | -11.41718 | -56.05802 | 2026-07-02 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 339469db-ddd3-3765-870b-7adee6017416 | -11.62884 | -59.02246 | 2026-07-02 05:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14878946-415a-3ce1-a2eb-aa301f1dbf5f | -9.18709 | -58.05775 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a14de0e-1fa8-3c79-92e1-da8b099302cb | -9.18758 | -58.05403 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83d44038-4469-3bac-abfd-3786a7d58026 | -10.81718 | -58.02169 | 2026-07-02 05:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 578eeeea-e555-35c5-9206-bed710e86127 | -11.79726 | -56.99736 | 2026-07-02 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b4a36723-cc62-3417-aad8-efef4b6bb960 | -11.62969 | -59.01572 | 2026-07-02 05:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f93252da-f386-355b-9206-ecc544c1723c | -11.41656 | -56.05844 | 2026-07-02 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a08791c6-2b16-3ace-a9f3-24d9d9dd96eb | -9.2052 | -58.049 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1bfd649-ab48-3cb2-bd8e-c3361421a88e | -11.42299 | -56.0643 | 2026-07-02 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 77a3b0c7-495a-3141-80c4-91cf6a267e4d | -10.66974 | -54.53609 | 2026-07-02 05:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f963ab74-1849-3a9e-80ef-d1109b61226c | -12.8741 | -44.3593 | 2026-07-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 9fb4302d-d22f-3c59-8d54-e2858f0492bb | -12.8552 | -44.3389 | 2026-07-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 298.7 |
| 02f0f872-c1b7-3e32-9faa-ad54956e30a4 | -12.7751 | -44.4927 | 2026-07-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 9c961d4a-af79-3ca7-9531-147076fdaa4a | -12.7562 | -44.4724 | 2026-07-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 273.3 |
| 6449fed5-3735-3928-ba66-2299a73fcc8e | -12.7557 | -44.4959 | 2026-07-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 193.3 |
| 8c7303ca-ae35-3b95-802a-ec5eb8b90a10 | -12.8548 | -44.3625 | 2026-07-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 0ff3ca03-d5f9-315f-bf42-91d05bf6805a | -12.7566 | -44.449 | 2026-07-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 5c274d58-1d28-3900-a12b-866d65f12be6 | -12.8746 | -44.3357 | 2026-07-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 237.4 |
| 6fdf2f93-aa3d-3bca-bb83-57a1bd2b6ab3 | -12.7755 | -44.4693 | 2026-07-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 83d08b77-566b-3640-8ee7-7fea5a0a185f | -12.8557 | -44.3154 | 2026-07-02 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| f00e6c76-f9a3-3827-8966-02fcfd5fcbd0 | -21.7823 | -56.2976 | 2026-07-02 06:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 003ecc3b-2e53-398e-9fba-b22bdc3d324e | -21.7716 | -56.29494 | 2026-07-02 06:03:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bc85a023-9fa4-3d03-b237-634964b118b3 | -21.77926 | -56.28823 | 2026-07-02 06:03:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 991d8acf-0043-3bac-83a8-59f9726c456e | -21.76447 | -56.29451 | 2026-07-02 06:03:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 70c3f643-c3f8-3ce4-acf4-d0dee18fd6c6 | -21.77874 | -56.2953 | 2026-07-02 06:03:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67fba37c-f7f8-3059-8acc-4b76d6689298 | -21.77211 | -56.28789 | 2026-07-02 06:03:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 415944de-0da0-3b40-9f92-287a8450f8ee | -12.8741 | -44.3593 | 2026-07-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| be5bad30-91aa-31cc-90ee-a154a224bdb1 | -12.8557 | -44.3154 | 2026-07-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 4cc19ebd-7451-3aa8-bd1e-ad3ad5995f35 | -12.8746 | -44.3357 | 2026-07-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 272.6 |
| dc0e642f-fe6c-3627-bfb1-4c4203b610aa | -12.7369 | -44.4756 | 2026-07-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 429a0708-ea06-3b91-8590-b96bd566a05d | -12.875 | -44.3122 | 2026-07-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| ad6b59d6-9dad-3a0f-95f7-4ad20396cbfd | -12.8552 | -44.3389 | 2026-07-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 267.4 |
| f597e130-135f-3519-aa67-b4619c79b5e6 | -12.7557 | -44.4959 | 2026-07-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 187.6 |
| db944ced-b58c-3446-b8ad-6284e02d29fd | -12.7751 | -44.4927 | 2026-07-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 7feed0ac-1bd7-3267-b19a-79391846aae8 | -12.7755 | -44.4693 | 2026-07-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 9d655073-4ef7-348c-804c-1a8d07e35f52 | -12.8548 | -44.3625 | 2026-07-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 623e2472-f532-37d9-b86c-3b1be6ea0927 | -12.7562 | -44.4724 | 2026-07-02 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 249.4 |
| a5d2ad4f-28bc-3669-89d3-4fdb9fdebd4e | -12.8557 | -44.3154 | 2026-07-02 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 219ba874-4e35-3aa6-b4b3-011875d7deee | -12.8548 | -44.3625 | 2026-07-02 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 480efd76-eee4-3dff-abf3-0b985bc1f67a | -12.7755 | -44.4693 | 2026-07-02 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 93596654-1085-318e-81ee-5bfecafd9941 | -12.7557 | -44.4959 | 2026-07-02 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 5fcfdbea-1c31-3872-b432-3a1baea8f9ed | -12.7751 | -44.4927 | 2026-07-02 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| e631e319-6195-355a-b8d8-c640c2ea04e2 | -12.8741 | -44.3593 | 2026-07-02 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| f5ee7924-7f82-35cc-9c10-cb850f6f19e8 | -12.8746 | -44.3357 | 2026-07-02 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 224.0 |
| 034c5f0b-d9f9-3083-b7ed-eb4c58a3a65d | -12.7562 | -44.4724 | 2026-07-02 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 263.2 |
| 39d0484b-6e27-38d8-9ace-2aa3c0b373ca | -12.8552 | -44.3389 | 2026-07-02 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 282.4 |
| 43511f35-564d-3d57-93c5-e8de95161446 | -3.41422 | -41.71101 | 2026-07-02 06:27:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 0d841760-36c6-362d-8a65-84437188c2e9 | -4.00838 | -48.05089 | 2026-07-02 06:27:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 21d7b24f-fd22-3fa0-8f46-fd40c92b514f | -3.50576 | -48.04014 | 2026-07-02 06:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2d5e60e8-25ab-3564-ad65-7bd73d3852c4 | -3.50746 | -48.02894 | 2026-07-02 06:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 83db9736-2285-3d12-96e0-332fe0c9809b | -3.51912 | -48.02584 | 2026-07-02 06:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7ec82864-79eb-362a-afc2-0b24fe01edb3 | -3.50753 | -48.03553 | 2026-07-02 06:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| cf0ff16f-64b0-3a3c-9426-c4f1874ed5e8 | -3.51737 | -48.03699 | 2026-07-02 06:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 35180908-4b28-3113-9b18-b202a39214ce | -3.4159 | -41.69969 | 2026-07-02 06:27:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 9c9bb27c-b1b5-37ed-b3f3-9629b791e10b | -4.00665 | -48.06206 | 2026-07-02 06:27:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 2a437b8a-e744-30a4-ae59-d7bbac8a18b3 | -12.77574 | -44.52217 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 17343efe-4035-30a4-85e2-0eb59014f2cd | -6.92313 | -43.71493 | 2026-07-02 06:29:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| f77ad869-289f-35c3-80d9-7b5ce9d39445 | -12.84345 | -44.35517 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6fead34b-fb62-3101-bed5-5baba01824e9 | -12.52001 | -48.2847 | 2026-07-02 06:29:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9d51226b-2ac0-37b3-b575-8dc2906c9fbd | -6.92169 | -43.72464 | 2026-07-02 06:29:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fee7de36-387d-358d-923b-1c7d0d5823d9 | -5.79194 | -45.03702 | 2026-07-02 06:29:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 22818e02-950a-3fb5-bdd0-a8e754805570 | -12.76632 | -44.52082 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ce72281e-235d-341e-a773-52e2494339ae | -10.94563 | -43.04661 | 2026-07-02 06:29:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 018daa57-1a10-37d8-b4fc-245e46a3ccf4 | -12.8625 | -44.35789 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e64edf7f-b492-3899-b95e-2ba29b635c6e | -12.84492 | -44.34452 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| fcd0a89d-1744-3499-9c48-7169c3b6240f | -5.81212 | -43.79235 | 2026-07-02 06:29:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| eb3cc7de-b090-38ac-9570-8531f21f2a4b | -5.34693 | -45.17885 | 2026-07-02 06:29:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c70c5398-d932-3e47-ab92-6d1f79bf6e6f | -12.85445 | -44.34589 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 836469a5-4f38-319d-a98e-b33a3a292bb4 | -12.87203 | -44.35924 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c0ef4716-83b3-351b-879d-077a2fbe77a7 | -11.85089 | -48.24062 | 2026-07-02 06:29:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| f1a17ae2-617d-3bc7-8b63-d4618cf4d6fb | -12.87502 | -44.33781 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9fe3f505-1082-3e89-9c07-3dac9a66fbc4 | -12.77072 | -44.48958 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 900c35a4-b05f-35a5-9c4b-48051b5557f2 | -12.74385 | -44.47507 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c596e3f1-6430-3be9-97ec-4e95dbf9a150 | -12.85297 | -44.35654 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| df546dfa-e453-3ec0-9895-821e32ea7133 | -12.86398 | -44.34723 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 310.5 |
| a958b715-1784-3ddf-9fd2-f94659376167 | -5.79062 | -45.04578 | 2026-07-02 06:29:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5bac7b51-8453-3344-936a-75633a74964b | -11.00616 | -47.18567 | 2026-07-02 06:29:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9de8a82d-18cc-3cb9-999c-3ae54585b7ef | -12.85593 | -44.33522 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| c311cb81-a12f-3a69-8f45-ce0eae65c364 | -12.87352 | -44.34856 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 4c92a6a7-b55a-3350-a12e-5ba1a6a6f5ab | -8.71925 | -48.33141 | 2026-07-02 06:29:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3fa01f63-dfb7-3dac-937f-11aacf9695db | -12.76275 | -44.47779 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 6e691f87-e22d-3d93-b2db-5432bba795dd | -12.76128 | -44.48824 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| afdbddff-47bc-3aeb-ad45-8e325a1df545 | -5.3742 | -43.37643 | 2026-07-02 06:29:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 27a7c35b-2e2f-3459-9f9f-91693ca83c71 | -12.76925 | -44.50001 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 7e99104e-31c0-34c4-804b-1379a531affb | -12.74239 | -44.48551 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 8ef63ef1-632b-3592-bedf-ecf61e5bc58d | -12.8515 | -44.36717 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f82ecad3-9dd1-3d2c-b27d-b51bf8a93fad | -11.00753 | -47.1767 | 2026-07-02 06:29:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ef5666d5-56fd-3a80-9eca-e606f5a1ec0c | -11.85989 | -48.24209 | 2026-07-02 06:29:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b3c75c14-8f2b-3125-b61e-261194340cb6 | -12.51104 | -48.28326 | 2026-07-02 06:29:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 81623386-3284-3808-8abd-41ccd68fbe53 | -12.86547 | -44.33652 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 7378b341-1a20-3b26-a691-ec551b59c675 | -8.65628 | -49.71288 | 2026-07-02 06:29:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 99686d5d-1477-3ef1-a431-2789f3bf19a6 | -12.75981 | -44.49867 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 26ff82c0-64ef-3f10-bf7b-5cf59196a066 | -12.7533 | -44.47644 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 218.5 |
| e6b87c68-3a82-3824-ae14-4fdc6ce15467 | -8.71769 | -48.34143 | 2026-07-02 06:29:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c9c74459-97fb-39ed-8c40-aa4789f81369 | -10.12656 | -52.09336 | 2026-07-02 06:29:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| e171908c-7185-3f76-9295-1ee44782af14 | -12.75183 | -44.48688 | 2026-07-02 06:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| a02697e9-c3d5-354e-b83a-948ab2558aaa | -12.8548 | -44.3625 | 2026-07-02 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |


[Clique aqui para ver as próximas entradas](README25.md)
