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
| eb4f630b-12c2-3184-9ca6-fc8c9e558cfb | -15.5656 | -48.3918 | 2025-09-02 03:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a6acabec-d4dc-3c29-a170-1529a228a91f | -3.2305 | -47.135 | 2025-09-02 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a072504c-67cf-3b17-b1ab-8df014b2a440 | -6.7909 | -52.8165 | 2025-09-02 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| ae8fce43-98bb-313a-a13a-5ada77b0bf11 | -15.5661 | -48.3694 | 2025-09-02 03:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| aad0d0f4-d6c7-3a3c-af46-4afa126c2401 | -5.6081 | -45.0038 | 2025-09-02 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 543a4746-7ee1-32e8-a3c0-409324e827ed | -7.5476 | -61.3437 | 2025-09-02 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 461dfa32-a94b-32cb-ab9d-8714318ac6fc | -15.5857 | -48.366 | 2025-09-02 03:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ff8c8849-0642-377b-a15c-1a01b88b92e0 | -9.1207 | -61.4864 | 2025-09-02 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| cf13a10b-9f3a-3205-a85e-32e9aa3d8511 | -6.8095 | -52.8154 | 2025-09-02 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| be388053-3dfe-3c3f-97b5-f2e2ec7dfaf8 | -15.5852 | -48.3885 | 2025-09-02 03:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1b9473a9-a90f-323c-a5a7-a123cbad9a44 | -11.6647 | -57.3533 | 2025-09-02 03:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d67f60d8-c306-359f-ad34-fe7c45ee3b11 | -15.5857 | -48.366 | 2025-09-02 03:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 3fb260a6-0ebc-331a-ac13-d4445215422f | -12.6302 | -48.1757 | 2025-09-02 03:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 57f2964b-9742-3cd2-b4ad-bf87d58b671c | -6.7909 | -52.8165 | 2025-09-02 03:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| cc4dfb48-ae51-3c65-8996-11dbfff58893 | -11.1037 | -44.6315 | 2025-09-02 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 532.7 |
| 594d0719-21b3-3a9d-a811-d7da4c7c093b | -11.6458 | -57.3548 | 2025-09-02 03:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 1de36e5c-506e-38a0-b2b2-f06c463d227d | -11.6644 | -57.3733 | 2025-09-02 03:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 6da39c06-c2df-3ae5-9e6a-bde158c8781a | -9.1207 | -61.4864 | 2025-09-02 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| de911733-ef64-30c9-87a8-65b4f167808a | -12.611 | -48.1784 | 2025-09-02 03:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a89ee57a-ca2f-324c-8e6d-2a2042896804 | -11.1041 | -44.6083 | 2025-09-02 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 418.7 |
| 3ed3bebb-8505-3377-918d-64f1437b01a8 | -11.1228 | -44.6288 | 2025-09-02 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 9c445abd-352a-367a-9314-b63da81eab46 | -11.0845 | -44.6343 | 2025-09-02 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 270.2 |
| cae2c2c9-7921-356c-a83b-c0bc0e79fad7 | -15.5671 | -48.3244 | 2025-09-02 03:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| df83de8b-c36c-31cc-8998-04487495cfd8 | -15.5661 | -48.3694 | 2025-09-02 03:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 7100cc5e-5472-37df-93c3-874ff71a75b2 | -6.8095 | -52.8154 | 2025-09-02 03:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 05cf86af-6a55-300a-bb18-8fb210877b40 | -11.0849 | -44.611 | 2025-09-02 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 218.9 |
| 005a4ca5-1158-367c-a6a4-9a23c0ca2c2e | -15.5666 | -48.3469 | 2025-09-02 03:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6bd42c95-f8a0-31f3-872b-d5452637908a | -10.062 | -48.1197 | 2025-09-02 03:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| fe824591-e9b1-3264-8ce4-ec5074f7fa48 | -12.6298 | -48.1979 | 2025-09-02 03:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 67764168-a6de-3465-b5d4-42a0a6aaf28c | -7.5476 | -61.3437 | 2025-09-02 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 1e96857a-78f8-3afc-913e-f5b1a3bdcc13 | -7.5477 | -61.3247 | 2025-09-02 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 2a7d65f0-e704-3a6d-90dd-7233da860699 | -3.2305 | -47.135 | 2025-09-02 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9c1b068b-1949-304e-8f4a-ecbfdff4ecfb | -11.1033 | -44.6548 | 2025-09-02 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 4732f80a-b683-310f-891a-ad346f4602ad | -7.5477 | -61.3247 | 2025-09-02 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 516942e3-d278-3151-8f69-0688df528e8f | -6.7909 | -52.8165 | 2025-09-02 03:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| bacebcf0-764b-3354-903f-40e66358964f | -10.0623 | -48.0978 | 2025-09-02 03:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 4b1fd5fa-eee3-35fd-836a-6f53e0579116 | -6.8095 | -52.8154 | 2025-09-02 03:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 917822db-61ab-3267-a460-0f8c53da814f | -7.5476 | -61.3437 | 2025-09-02 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| be2997a0-2a0f-3a3c-8698-7ed6fef7dcfa | -9.1207 | -61.4864 | 2025-09-02 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| dbcb0573-3e6a-3014-8090-16ab08152a8a | -11.6647 | -57.3533 | 2025-09-02 03:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 842cf6c4-50fb-39b3-b65c-b96c105c9f2e | -10.062 | -48.1197 | 2025-09-02 03:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| f88c0528-c14a-3067-ae7c-2623d011be4a | -8.9664 | -65.9796 | 2025-09-02 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| de873b0a-b601-3ce6-89b1-9a6732b0b06a | -12.6302 | -48.1757 | 2025-09-02 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 8a978bec-f2ac-3d3a-8a10-55dc21c7e437 | -15.5666 | -48.3469 | 2025-09-02 03:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 367bca8d-8f7e-3318-b430-8ea13c409717 | -3.2305 | -47.135 | 2025-09-02 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 24e1b168-39f8-358b-83f6-f475b9096864 | -15.5671 | -48.3244 | 2025-09-02 03:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 105.4 |
| d4fd786b-0cc5-335f-8ab8-69f610b8a455 | -4.82272 | -37.80813 | 2025-09-02 03:21:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ffd466de-8339-3ce2-b06b-59285bb6b5b6 | -9.59369 | -40.34643 | 2025-09-02 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| fd9de1b5-459e-3a17-b65c-c64899687933 | -7.05903 | -44.3407 | 2025-09-02 03:23:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7abf599d-c63f-34c6-a2ed-c70053a8adc9 | -7.62309 | -42.65355 | 2025-09-02 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c218437c-ce43-30bc-88d4-4ba3a814ef4f | -6.72196 | -42.26021 | 2025-09-02 03:23:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f75b800a-72c7-3e9f-aad6-bc0490c5b207 | -6.54088 | -43.1072 | 2025-09-02 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6fdbb6b8-4966-380e-9c21-8edffc7f7f4f | -6.22185 | -43.35855 | 2025-09-02 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c4b0e30a-7d7c-37eb-b303-89e50bbb7102 | -7.63647 | -42.65118 | 2025-09-02 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f58974d2-32b1-3f5e-b2e4-3b6da9f77046 | -6.72081 | -42.26653 | 2025-09-02 03:23:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 863177e7-7bc6-31d2-9edd-3352ad6a4285 | -6.99202 | -43.23517 | 2025-09-02 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f6e4b09f-b583-3f05-a464-25385053ec98 | -6.21719 | -43.36467 | 2025-09-02 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8bf5fdd8-d534-372e-89a7-bc77c6f15c72 | -6.97897 | -44.30658 | 2025-09-02 03:23:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0f1e345-dcde-3317-bdf0-fa906d324798 | -6.25033 | -42.61507 | 2025-09-02 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3ce1dffa-f958-31ed-9ed6-b46a8c759be6 | -7.99206 | -44.04666 | 2025-09-02 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c4c2849-9795-3b6e-ab6e-c67fb308a874 | -5.16242 | -37.98123 | 2025-09-02 03:23:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f1785871-4e75-37ae-b472-ece2eb57c486 | -7.00376 | -43.53557 | 2025-09-02 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 527a5f15-9339-3d49-84f5-537653d4bbe6 | -4.91973 | -43.19896 | 2025-09-02 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f4b4f7e2-03b0-36dd-95c7-11b165251f39 | -6.225 | -43.35986 | 2025-09-02 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dffcc874-8aad-35a4-8290-c4c8889a3e5a | -7.62244 | -44.03489 | 2025-09-02 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 09703f83-398a-380c-a269-f21781ec95cd | -6.21606 | -43.37069 | 2025-09-02 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 72459ce0-4247-360a-a422-fbabe949e15a | -6.9834 | -44.32096 | 2025-09-02 03:23:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4bb3f13-41ba-398d-b622-bc4b56a00303 | -4.91299 | -43.19769 | 2025-09-02 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c151d0d1-af96-31a7-9b84-6d5abfa0f779 | -6.72287 | -42.25514 | 2025-09-02 03:23:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 87b36128-67f8-3243-94af-d4595e53be32 | -6.22391 | -43.36567 | 2025-09-02 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 18b7ed0c-657e-38e2-b000-ddd3b3f7f332 | -6.33842 | -42.56553 | 2025-09-02 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6b9ff7b6-2401-3023-a98a-9f5ae197ce72 | -6.98469 | -44.31429 | 2025-09-02 03:23:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e966263b-ca82-3211-af46-0bfe7cc1a41f | -6.99438 | -43.22851 | 2025-09-02 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f302034f-e0d8-3d7e-bf6e-b0d9f3c75a4e | -7.63024 | -42.64989 | 2025-09-02 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dfe3fb60-73fa-31a2-8475-117c8ad2bd96 | -6.42413 | -43.89079 | 2025-09-02 03:23:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22d66ca8-b30d-3589-b5c4-e3460b5a3f89 | -7.59662 | -37.80547 | 2025-09-02 03:23:00 | NOAA-21 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 97155569-0ce4-3f95-8ced-fe3f006dda28 | -6.25775 | -42.61065 | 2025-09-02 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 25d21be4-1843-3b45-832d-54848af74ca9 | -6.33942 | -42.56004 | 2025-09-02 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e0cf3e80-d521-3205-a9ba-1e2a52c45b42 | -6.901 | -44.23108 | 2025-09-02 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4662d93c-3ef1-3e54-b838-97a622db3937 | -9.59308 | -40.34968 | 2025-09-02 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5ba3fd26-eb19-3c2d-90af-c2654b163ae6 | -6.90168 | -44.23355 | 2025-09-02 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cfe2ca72-0719-30f2-9d91-f428294235e5 | -7.46677 | -44.80869 | 2025-09-02 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5d7a18c6-9220-357a-86c1-c020b089b1ac | -7.61625 | -44.03774 | 2025-09-02 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ff2fc3e-86de-3798-baaa-15dcaf717460 | -6.2602 | -42.6234 | 2025-09-02 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b3b25933-f36f-326d-be81-d8f5bb1703ea | -4.90734 | -43.1904 | 2025-09-02 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 82792cf0-6d3d-3f5a-87cd-d0f39c2cbeeb | -5.16724 | -37.98204 | 2025-09-02 03:23:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 82900cb7-930a-3532-8272-f0c27ca6c5ad | -6.99333 | -43.23422 | 2025-09-02 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2010c8e0-4ef1-3087-8afa-4d927bc4cc19 | -6.19609 | -43.3485 | 2025-09-02 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 89eb49db-9f66-35d0-8432-27b30cd698f4 | -7.9989 | -44.04748 | 2025-09-02 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 952dc5ef-6abb-3e57-a446-01fc1a49936f | -6.19504 | -43.35424 | 2025-09-02 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 946ff898-f7c5-3290-ac7e-f866cd931c12 | -6.21828 | -43.35891 | 2025-09-02 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b72608d4-313c-3693-b061-39d3487badba | -6.22081 | -43.36428 | 2025-09-02 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c3632f88-776a-3e2f-9088-f3db86103b05 | -7.46979 | -44.81342 | 2025-09-02 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd22acd2-d155-3ae2-8bc2-9067c7814ba6 | -7.06598 | -44.34211 | 2025-09-02 03:23:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 967d4723-a164-3038-9ae0-f4066da1f09f | -6.99542 | -43.22282 | 2025-09-02 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 51e7f557-f90e-3eea-8258-cee38f9d2711 | -7.46281 | -44.81134 | 2025-09-02 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0ba2c94-bdf8-389c-806a-92d637fca6fa | -6.21973 | -43.37025 | 2025-09-02 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dce7a6e7-2e45-3d24-9e27-9d1c4b2db6bb | -7.62416 | -44.0332 | 2025-09-02 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65031b01-dfb8-3579-bf70-1a3ff5b191ca | -6.26215 | -42.62246 | 2025-09-02 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f9aa8c14-f37c-3a14-852e-3f80e05410ab | -7.70686 | -44.6105 | 2025-09-02 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README13.md)
