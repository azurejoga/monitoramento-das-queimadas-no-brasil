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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40e9ed03-f162-3554-abbd-1cc5ad97b0ee | -6.10088 | -41.57815 | 2025-11-13 04:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3c179e14-f3ea-30ed-a25b-d7dc85e561fb | -3.29422 | -50.0763 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5efc6f7-cd23-350f-b0de-3b363d871e13 | -7.06305 | -41.58931 | 2025-11-13 04:42:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0cab70db-1b13-3507-a1c3-a202eba408a0 | -6.34986 | -39.79226 | 2025-11-13 04:42:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6064fc09-04b7-3064-86e1-df440bab240c | -3.76595 | -47.72588 | 2025-11-13 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbb36717-9a1a-3126-b49a-34834c10756a | -3.06623 | -40.08154 | 2025-11-13 04:42:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| cf064e6d-1e93-3ac1-949d-a4a272fdd293 | -3.7693 | -47.7264 | 2025-11-13 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b2fcdd8-868b-390b-92a0-31a9032c0ebd | -4.57342 | -46.93875 | 2025-11-13 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| efaeb472-df20-3c4b-a338-1502941a25bf | -4.25731 | -44.59943 | 2025-11-13 04:42:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| feca6c61-c8c6-36b1-a09a-232076714912 | -4.93418 | -44.29804 | 2025-11-13 04:42:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ceef8bcd-d9e9-35df-895a-a5b29d169915 | -4.93926 | -48.54729 | 2025-11-13 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8be23a71-90e8-3c51-8dd5-5f4bb21eadbb | -5.64785 | -41.08652 | 2025-11-13 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d7ad84f1-f30c-32d1-a801-12aa1884098d | -2.92445 | -51.75668 | 2025-11-13 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 307d8104-c69c-3942-a4fb-803cd304fb14 | -5.42376 | -44.65075 | 2025-11-13 04:42:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e80d8e5b-4cfa-34e9-a7bb-0f9dbde5a3a6 | -4.56795 | -48.49632 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 940303fa-bd4b-3cb7-abe0-96f795ce3e3c | -4.21681 | -46.35136 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e05149c9-0f5a-32a7-a0c5-f95cad9ae52c | -6.10496 | -41.58438 | 2025-11-13 04:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 942bb86a-aa82-334f-941a-0fab197965e7 | -4.71501 | -46.44019 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 81af65cb-bbc7-3b0d-a437-e200f3f81161 | -12.10945 | -43.6484 | 2025-11-13 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da7a0fa1-6b5c-3e56-86ff-1ddf254d1a12 | -12.66712 | -46.75105 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 943a7961-c7f0-3f6d-8030-51802b32ae59 | -13.78036 | -49.40022 | 2025-11-13 04:44:00 | NPP-375D | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7aa1d8c3-b02b-38f4-ae13-306b34e8a94e | -10.64297 | -45.03405 | 2025-11-13 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4de1b709-4ce9-3bda-b944-4d205ba85b3b | -10.35315 | -47.70555 | 2025-11-13 04:44:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e4c46c5-dcf7-38b1-ad63-af266a025662 | -12.41643 | -45.79142 | 2025-11-13 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82f3e2ff-306e-3ae7-8974-6aee58d0c723 | -9.66906 | -43.89427 | 2025-11-13 04:44:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bf10c1bd-432f-31d0-8971-0eba53fe37c8 | -8.64596 | -45.66311 | 2025-11-13 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cfa278ee-2611-3cec-814f-fa31a769ebb9 | -8.71301 | -44.25749 | 2025-11-13 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7695f2aa-9ae5-3442-b163-17c5503b7929 | -15.07546 | -46.46627 | 2025-11-13 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7d9cc2c-66bd-3847-9213-c929f0ebc2fc | -11.73325 | -48.5331 | 2025-11-13 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30f4fda7-bf6a-325e-904e-2ef27b616de1 | -10.82548 | -44.65305 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3209887-00dc-391d-89af-e377fecde505 | -9.64305 | -44.54308 | 2025-11-13 04:44:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca1740cf-955b-3eab-8eac-3598ab179bad | -12.06602 | -48.21033 | 2025-11-13 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 328166e8-82e3-3e36-b400-38eedb697fd8 | -9.34807 | -46.59237 | 2025-11-13 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 35b1f096-72f9-35bd-8645-9be8d4294405 | -10.91892 | -44.62843 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a254dd58-3f06-36e7-bce0-e16fada44bdd | -10.37 | -45.05731 | 2025-11-13 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74926254-f458-3082-b072-609be94eae53 | -8.25919 | -48.12628 | 2025-11-13 04:44:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58b2663a-118a-3e68-b208-bcd338ac616b | -12.65949 | -46.74989 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| a9fe1a0e-ddcf-3f6c-af90-1f575c5dcf5e | -15.01558 | -46.68667 | 2025-11-13 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dd63cbc-2748-3569-b221-090022aacbeb | -10.42331 | -44.67597 | 2025-11-13 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fe0c700-5a27-3e02-94f6-b9e649846365 | -12.95405 | -51.61168 | 2025-11-13 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bbaf30f-dfba-308f-afd4-9768abba1b67 | -8.86825 | -50.19495 | 2025-11-13 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a55856f-a0d1-3adc-aa59-2002996311bb | -10.61421 | -52.18016 | 2025-11-13 04:44:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc599696-966b-321c-8756-2776f5975dc9 | -13.37391 | -46.346 | 2025-11-13 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eaf6d10c-4d17-3351-946b-541ba4957e72 | -9.32141 | -47.83646 | 2025-11-13 04:44:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c460e7e-e9ea-38b9-9eb4-4136b1ac4937 | -10.62862 | -45.24673 | 2025-11-13 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51668045-4b41-3b89-82de-75f938043fba | -10.35668 | -47.70608 | 2025-11-13 04:44:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1036f07-2414-3f35-b9a7-a001f5a40bfd | -10.91997 | -44.62902 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1626e266-5b0d-34c7-987b-d416122a2c14 | -10.69186 | -45.00189 | 2025-11-13 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c46e25a3-cfbf-3780-9b71-d7ad9f98ceab | -12.66261 | -46.75524 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c9abaac5-beb2-34d7-a19d-2c2f1d2263c7 | -14.01287 | -44.08443 | 2025-11-13 04:44:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 269f67cb-6f0f-3f35-9051-e10d98b97420 | -9.35176 | -46.59294 | 2025-11-13 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30ad7cfa-235a-3cc2-90a7-dfc1b9b94923 | -12.03674 | -43.87714 | 2025-11-13 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a949815-1f60-3808-abfe-3f1d3683c153 | -15.39938 | -43.06728 | 2025-11-13 04:44:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b6b9bbeb-5ad6-3685-8e7c-86aa20e33bf6 | -8.24955 | -44.36793 | 2025-11-13 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71ab5b1a-7519-3cdd-b644-0fb6020dc7a6 | -9.91261 | -50.50264 | 2025-11-13 04:44:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b353d084-7b61-393a-b0ad-a3357c4efbdc | -12.06191 | -48.21377 | 2025-11-13 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e3c50dde-0bc3-33ed-9e56-827f0395a8fb | -14.9491 | -42.36579 | 2025-11-13 04:44:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f05bdb22-148e-3f9f-9466-61d6064db62c | -8.39426 | -49.61556 | 2025-11-13 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9aa83885-bab3-32b7-9785-e085724a7c45 | -12.06543 | -48.21431 | 2025-11-13 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 300517fa-120e-37f8-b5c1-d708b2e28d69 | -9.44103 | -44.87764 | 2025-11-13 04:44:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61737459-dda4-36ad-a0b4-791aeda5db9f | -12.43492 | -43.75773 | 2025-11-13 04:44:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f09274af-0334-30e1-8c7c-765e2e314e0c | -9.01767 | -45.43361 | 2025-11-13 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 318e3ecc-d2e4-3374-9d22-edab8dc38ed4 | -9.34741 | -46.59674 | 2025-11-13 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1de2c469-3f48-3a0a-be15-8783d012f00a | -14.94982 | -42.36791 | 2025-11-13 04:44:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 23081575-5afa-34de-83e6-16a8b38019e0 | -12.41544 | -45.79858 | 2025-11-13 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7497060-9034-38d4-918f-cd00c473b3f2 | -8.86369 | -49.94401 | 2025-11-13 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12fc96ab-5c28-331d-af00-16cf8c79cb01 | -13.77694 | -49.3997 | 2025-11-13 04:44:00 | NPP-375D | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 173393e5-090a-3916-94b9-2e5846dc133c | -15.2967 | -43.89468 | 2025-11-13 04:44:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed56a791-5b04-307e-bfb0-f61f5bfe04b5 | -10.78012 | -48.14434 | 2025-11-13 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf24fe2c-fbf6-389a-b4f5-90852d886966 | -7.51512 | -49.14079 | 2025-11-13 04:44:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fa18c13-9fa1-3079-9b99-88f17a00ffde | -12.66136 | -46.75205 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| f0f0ed10-ed62-3a49-b40e-863a10361f75 | -14.98615 | -42.4143 | 2025-11-13 04:44:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8c59c981-ab8b-306e-9540-fec90961331a | -15.39432 | -43.06663 | 2025-11-13 04:44:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 03ec3cb7-a9ca-39bb-bbf9-56e92d0bdf71 | -9.62879 | -44.55265 | 2025-11-13 04:44:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e2199ed1-8dea-3810-9e4c-0d702b84f7f1 | -11.73459 | -43.84208 | 2025-11-13 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd9556da-d8f1-3f02-b79b-5feba6e41cc6 | -10.49826 | -44.94116 | 2025-11-13 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32393de4-add7-3849-9e8e-cfaff053baf5 | -10.62455 | -45.2461 | 2025-11-13 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8335b8fd-0093-3350-bff6-fe3e9ac73614 | -9.19735 | -49.48068 | 2025-11-13 04:44:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be2fbdff-2707-39f2-8a02-0366966651e3 | -10.7807 | -48.14048 | 2025-11-13 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e5a37db-deff-3a0d-a2aa-33d8f6dfad22 | -12.66518 | -46.75263 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| cde77b73-715e-3ba5-b6d7-3cb624806165 | -15.07877 | -46.4721 | 2025-11-13 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03b8d574-8ddd-3ca2-9dd3-27600e786363 | -10.62912 | -45.24309 | 2025-11-13 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 269f27f3-1531-3eda-8812-10fae75a9898 | -10.35729 | -47.70209 | 2025-11-13 04:44:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2bd75d8-77fa-35a1-bbb7-81a76817c8d5 | -9.9235 | -48.14167 | 2025-11-13 04:44:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a398adb6-6a19-3173-8789-08e73ac8df19 | -11.79709 | -44.20369 | 2025-11-13 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d02d8a9-438a-3e3e-af84-6ea6b8e53ead | -9.32431 | -47.84085 | 2025-11-13 04:44:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 464e7188-7991-3006-9574-fb16ba87d003 | -10.54839 | -48.0829 | 2025-11-13 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f27edd1a-a675-3cd5-b23a-1107f8e39a82 | -10.9157 | -44.62844 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f81d53cc-0b95-348e-84e5-c1f442ef8939 | -12.43353 | -43.75541 | 2025-11-13 04:44:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 155a122f-e80d-377b-87c6-7832e675e1f9 | -14.17167 | -43.58522 | 2025-11-13 04:44:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cbf6959-55e8-32d4-b0e9-3863e57ada44 | -10.76328 | -48.13777 | 2025-11-13 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8012cc3a-b7dc-3671-ba8a-ba1deb71908b | -11.73613 | -48.53748 | 2025-11-13 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20f43ace-967e-3342-9828-6e25e71dbcea | -11.81326 | -44.25083 | 2025-11-13 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebe28344-723b-3d3c-a45a-6617f872b0fa | -10.76677 | -48.13832 | 2025-11-13 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4fa5782-b70c-3411-8cc3-eeab84267eed | -15.39991 | -43.07159 | 2025-11-13 04:44:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1fbd6a8a-c13a-3da1-8609-9ca1919e38c6 | -9.20068 | -49.4812 | 2025-11-13 04:44:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c7391c9-cc74-36b6-ba6b-77738db25c79 | -9.45423 | -49.65083 | 2025-11-13 04:44:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 181b37dc-d4a8-3f8c-b058-463964d965f6 | -12.59518 | -48.33108 | 2025-11-13 04:44:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52e6e195-08f4-3805-a5f3-1b7bded050ae | -10.92373 | -44.625 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f6bdc1a-62b0-31e5-b8d3-207911acbee0 | -10.37463 | -45.05417 | 2025-11-13 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README31.md)
