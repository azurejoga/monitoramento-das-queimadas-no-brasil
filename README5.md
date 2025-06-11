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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb9b6ae1-c0c6-33a8-8293-add14c2e22f1 | -22.40846 | -45.95913 | 2025-06-11 03:32:00 | NOAA-20 | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7b16d85c-b930-3b74-9a64-230f6c926177 | -22.90255 | -43.75416 | 2025-06-11 03:32:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f2242d20-e8eb-389a-a3fe-5ce46d7f9a1e | -15.37366 | -47.9021 | 2025-06-11 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03cea5d5-8605-38a2-a540-c4fc4ae351f1 | -22.78474 | -43.75801 | 2025-06-11 03:32:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 43f8b4d4-573e-3a47-9c79-3da13691a28d | -22.41023 | -45.95994 | 2025-06-11 03:32:00 | NOAA-20 | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2492db9a-302f-370b-b010-6cc764c2bf05 | -20.75953 | -48.53035 | 2025-06-11 03:32:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 03fadfae-c38a-3e9f-b87d-37bb5672d15a | -15.38048 | -47.90378 | 2025-06-11 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61ce3f54-9695-31ed-b8e6-f3cde22a22e0 | -22.40492 | -45.9584 | 2025-06-11 03:32:00 | NOAA-20 | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d75ebc2d-7fd4-3d78-8fba-deb9a2d44c9d | -22.78166 | -49.34285 | 2025-06-11 03:32:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bcf6faba-2427-35a3-9c3c-aa6d3a260ee8 | -16.58109 | -43.6469 | 2025-06-11 03:32:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30725ea7-5580-31e1-9317-9b90b17c23a4 | -16.58118 | -43.64627 | 2025-06-11 03:32:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28f7cad4-32b8-390d-80cc-1a072aa85373 | -16.58174 | -43.64367 | 2025-06-11 03:32:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9d23ecb-9cd5-377c-8fbf-c096ed53ea32 | -25.19042 | -49.32828 | 2025-06-11 03:34:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 27bc8593-d14b-3109-8508-9e5ba4479d80 | -23.97833 | -48.91822 | 2025-06-11 03:34:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 512c950c-0b2b-3cb3-bdfb-5cd6db0abd6e | -23.98446 | -48.91994 | 2025-06-11 03:34:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13357a44-e9e6-3984-83db-8edb341a5203 | -10.6492 | -49.4267 | 2025-06-11 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 56bd7df8-c4ea-30b6-a614-90ce0cdc4e6e | -7.4575 | -45.5116 | 2025-06-11 03:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 91590d4c-b564-3371-b632-472e2ca2c535 | -10.6492 | -49.4267 | 2025-06-11 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 366ead4b-e245-3c37-a055-82be71461248 | -8.16974 | -46.50777 | 2025-06-11 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 184e8c77-5927-3425-b07f-5667495678b1 | -8.17478 | -46.50135 | 2025-06-11 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8372031f-4986-3927-b4c8-c673474b022d | -8.11885 | -45.35303 | 2025-06-11 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0ce22ad-28eb-3c3d-aa7e-89a3c5d658d7 | -5.6442 | -48.60714 | 2025-06-11 04:46:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd8f1cbe-224c-352d-a75c-7dccbcdaabb4 | -2.44985 | -47.48037 | 2025-06-11 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ab597c5-6d9c-3d2e-84d3-706b355fe217 | -2.91817 | -48.23948 | 2025-06-11 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7aa1dff0-2e70-32cc-9695-ce9a8445a12f | -3.57158 | -49.49817 | 2025-06-11 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8f6e5d1-6b91-33d9-b4af-98ba5fdf265e | -8.11447 | -45.89936 | 2025-06-11 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48924ae1-ce5b-3ccd-85e4-eeff6848941e | -3.58436 | -49.43885 | 2025-06-11 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1362d464-3abf-3f5e-8bac-1c5d94631c33 | -2.4463 | -47.47981 | 2025-06-11 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc90fe95-18c4-3832-b3bf-6a130071ea14 | -6.95285 | -44.56054 | 2025-06-11 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a43ce168-38a3-3648-b9a5-a1d2d6323840 | -2.92004 | -48.23896 | 2025-06-11 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da870c75-5719-38e8-807c-b105412a961d | -6.94899 | -44.55525 | 2025-06-11 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c74f5b6d-8704-3c81-a2c6-8470407ca31c | -4.56916 | -43.09343 | 2025-06-11 04:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f08d723-960d-3dd4-bdb7-6842279d6cf0 | -7.4218 | -47.71294 | 2025-06-11 04:46:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a949da30-9f57-3f34-805c-24943e783c5a | -3.32153 | -48.71228 | 2025-06-11 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82b279f1-2eeb-3eab-9955-9445c5537de3 | -3.57604 | -49.49166 | 2025-06-11 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e60ab319-740e-3ba5-860c-9f58cc70b471 | -2.91531 | -48.23519 | 2025-06-11 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bd59f70-08a0-3d18-aa74-3fde2d1043dd | -3.62719 | -47.50956 | 2025-06-11 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c44101aa-0da9-38e7-8131-7c0b72644fb6 | -6.24566 | -43.36573 | 2025-06-11 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ef722d5-1a5a-3aa2-9481-a90a3110c438 | -2.91717 | -48.23466 | 2025-06-11 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56a5062d-630b-3a74-8266-5fcd975629d8 | -3.61939 | -47.51252 | 2025-06-11 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29fce270-d610-37d8-974c-3f3215383540 | -3.6236 | -47.50901 | 2025-06-11 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 826a5707-2274-3ce5-af86-6b5a88f36e04 | -4.49256 | -43.77521 | 2025-06-11 04:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8ec35341-05dd-38e6-8296-24ce1fa6d6e2 | -5.77799 | -43.61314 | 2025-06-11 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 938386d6-1224-3c26-bde7-920c858695fa | -5.02794 | -56.19295 | 2025-06-11 04:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fead9b9-a075-3fc8-be55-d730603d03e7 | -3.57493 | -49.49869 | 2025-06-11 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bcb70ad-2ceb-3f73-bdc7-43ac8a7036b2 | -1.41138 | -48.38492 | 2025-06-11 04:46:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bdf78c0b-e039-31c2-b72a-5e3aeba35c52 | -8.11452 | -45.35225 | 2025-06-11 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f83b6f5-8ece-3df5-ab67-d95a4b154b56 | -7.41987 | -47.71402 | 2025-06-11 04:46:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3870607-4098-39e5-8df0-9a336fa134ef | -5.64774 | -43.60118 | 2025-06-11 04:46:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8fc84478-0568-3989-9c1d-aba219c6cb83 | -3.98946 | -48.40634 | 2025-06-11 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b260d1a0-1977-37f8-be74-0581ad5191f6 | -4.24848 | -47.58855 | 2025-06-11 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b01a350-9cc8-34f9-b42c-3c97e702d1f4 | -4.24488 | -47.58801 | 2025-06-11 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79553d87-ece1-37ed-8ce2-e584a164d448 | -2.91353 | -48.24644 | 2025-06-11 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2f6a32a-c4a7-3117-a260-a20dba27209d | -4.54924 | -48.02292 | 2025-06-11 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca190440-6353-3a77-9ef2-279cbec14d09 | -3.49655 | -47.17378 | 2025-06-11 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 582d476d-5e39-3f12-bc60-60dcb6215a33 | -6.1676 | -48.06335 | 2025-06-11 04:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47bac7f8-ecff-3277-b006-281354a6e81e | -5.77728 | -43.61814 | 2025-06-11 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b987d25-3840-3397-a747-ba405fcbbe6a | -7.46968 | -45.51238 | 2025-06-11 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20319e36-35c9-3c95-a131-382702c0655f | -4.13047 | -54.89821 | 2025-06-11 04:46:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1d42e07-d913-341d-9c07-f88bf4166eb9 | -8.2815 | -44.95836 | 2025-06-11 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d5c4a00-ae4a-3e1d-9662-3ba4199aa828 | -7.24474 | -49.53317 | 2025-06-11 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3eac289-e0fd-31b0-b557-d2da185b9a7c | -7.28341 | -49.28377 | 2025-06-11 04:46:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d63a32bb-8868-30bf-81dd-3d01c142e1d7 | -8.07987 | -47.13043 | 2025-06-11 04:46:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7f43247-fac6-3e06-aace-769252035d13 | -3.03188 | -47.86168 | 2025-06-11 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 919ec12c-cb66-389e-ac5e-c971776c979e | -6.49593 | -47.48724 | 2025-06-11 04:46:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63171ce0-3b88-35da-a9f1-a81c7be5ca7d | -4.24912 | -47.5844 | 2025-06-11 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1d34ba9-e161-3d45-b725-fe82ecfb483e | -7.00951 | -44.61461 | 2025-06-11 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ae0a65e-db99-3cdc-8743-f80aa21120b0 | -7.00913 | -44.63037 | 2025-06-11 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c019508b-baf8-3c6e-9480-deca8c642660 | -4.24551 | -47.58385 | 2025-06-11 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6e74f08-0cde-36f7-a8b3-64f4309d3fc5 | -4.55278 | -48.02345 | 2025-06-11 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63ccd1f0-188f-300d-a96f-9a1e95e7930c | -4.57398 | -43.09416 | 2025-06-11 04:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df4e91e3-82f8-3aa8-a40f-c4fe992843ea | -4.57225 | -43.09501 | 2025-06-11 04:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68367dcf-305c-38eb-b94a-21da09f2beaf | -3.57549 | -49.49518 | 2025-06-11 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a53f8ae0-bc5a-35ed-8e2d-875d9951922f | -7.87312 | -47.88544 | 2025-06-11 04:46:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c2fb4f4-1fe9-36bf-a84f-f63c7207483a | -8.27701 | -44.95772 | 2025-06-11 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae173064-64b7-397c-8b4e-3619cff7e47c | -7.46599 | -45.50776 | 2025-06-11 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| feffd8aa-9f50-3af7-a89e-85e2e3bb020e | -4.15796 | -46.18444 | 2025-06-11 04:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d42ecb84-5866-3fe8-82b5-9def850adc65 | -6.14728 | -46.15372 | 2025-06-11 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7e34896-f6f1-3b2e-bb42-fbce624f9da9 | -7.01099 | -44.61695 | 2025-06-11 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6801b34-e1dd-3924-8f2b-e1f24d3aede2 | -7.41557 | -49.37181 | 2025-06-11 04:46:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60c09b58-58df-36bd-af0b-a84a700b64cc | -6.9535 | -44.55597 | 2025-06-11 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0d4d174-0cf2-3bf4-9f7d-45bc82233d29 | -2.91659 | -48.23842 | 2025-06-11 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f377006-cafa-3c66-a16d-29ee1a58aac5 | -4.48797 | -43.77453 | 2025-06-11 04:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b3c4e73e-d688-3061-92ac-ee22665490fd | -7.00975 | -44.62591 | 2025-06-11 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5f1d3f7-1eba-3437-9b10-e0d1ce237902 | -8.16571 | -46.50714 | 2025-06-11 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 503c79db-10f1-3319-93af-84ce2aea8086 | -7.01801 | -44.59961 | 2025-06-11 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 296a12cc-e89d-30d4-8922-2017b46d091c | -1.41478 | -48.38544 | 2025-06-11 04:46:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79ba1e42-477b-3d7a-a9f8-e4683e5c5ade | -3.32835 | -48.71332 | 2025-06-11 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f3ded93-f217-364c-a2a8-2e8ac7a65046 | -4.42017 | -47.66226 | 2025-06-11 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da2c0cce-d9a5-3596-b7f9-1674e6394261 | -6.49452 | -47.48857 | 2025-06-11 04:46:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a98e8856-4bcc-3649-bb58-5eaa5de9465f | -5.77313 | -43.61107 | 2025-06-11 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66ff7f25-4213-3fb0-9adb-70440bbefaff | -6.99022 | -47.08267 | 2025-06-11 04:46:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 763f6197-c3a7-3be7-9f39-6a6c5c027553 | -6.49521 | -47.48413 | 2025-06-11 04:46:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49dacab9-77eb-32a4-bc13-0f583fa04def | -4.41658 | -47.66167 | 2025-06-11 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9920ca9-720a-31be-bbeb-6e842f1cdc52 | -6.84886 | -47.8463 | 2025-06-11 04:46:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a553c0d1-f0b5-3778-8a0d-c495799b6180 | -7.01399 | -44.61548 | 2025-06-11 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b85dbb2f-b1e6-3d43-94f5-30f7764b9537 | -3.986 | -48.40582 | 2025-06-11 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da8bf8ac-01f8-3683-a2fd-204df15a836c | -3.83254 | -49.06099 | 2025-06-11 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9452a3d3-c75d-3462-9831-33a58dd8cf99 | -5.77786 | -43.61182 | 2025-06-11 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d6f3cd3-a1af-3dd9-8afe-600d332f401c | -6.49221 | -47.48666 | 2025-06-11 04:46:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
