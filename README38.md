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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c58ab72-e0df-3b34-9e9b-3b1c97ae2ae0 | -12.28417 | -48.06503 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9e4e3d4-9bf1-3fb5-9b6f-4474676c3dac | -9.88315 | -44.86349 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2aa8e65-2917-3e23-8579-9566cf28b9cd | -8.16485 | -45.5032 | 2025-10-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2c4b6d34-1e48-3db0-9a06-65eccbdf198c | -7.88717 | -45.69062 | 2025-10-31 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a89d3f44-0613-3812-92b8-b5344077870d | -13.51982 | -47.34626 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a288e33b-773b-378f-9ae0-49a8abb0172b | -10.15801 | -54.20702 | 2025-10-31 04:57:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e32654e-f1f4-3a81-b56c-f842bc15aaee | -12.10387 | -47.12924 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a88ccca-5b59-32f0-b4a2-02260960c31a | -7.31895 | -44.94532 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 8977a483-7ea4-3236-a305-9706be9c1599 | -10.42831 | -44.33029 | 2025-10-31 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f9a79b3-dd4c-3b92-8498-e9a0a351b715 | -8.16529 | -45.49986 | 2025-10-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc299d9b-14d4-3c9c-8ef4-bdced67b039c | -7.66835 | -43.58343 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f5c6da4-6535-3d75-af79-cd50626007b6 | -9.88266 | -44.86734 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5740d2ef-e4d9-3c91-b13b-831df98a5892 | -13.55835 | -47.36362 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eefcda4c-301b-32ca-8de7-4e06fc8b8db5 | -10.42319 | -44.329 | 2025-10-31 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 085c799e-8dd3-3adb-a6fe-a65544c3259c | -10.81384 | -47.58533 | 2025-10-31 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8242c360-d4ea-373f-aba3-c01f0f350c18 | -7.349 | -45.00614 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 037c00bf-d8d0-3973-ab00-d41a2254d0ca | -8.08925 | -45.13601 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41c2fce3-b3a6-3c0a-8969-a4cc3db61121 | -11.05642 | -44.02217 | 2025-10-31 04:57:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3af268d7-a08f-3968-b47a-d5178e608102 | -7.43826 | -46.88633 | 2025-10-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8e5c985-4ff0-3218-874e-fea4476512c3 | -8.09582 | -45.14822 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60861548-3890-37a1-b242-3a4c4120e359 | -6.84879 | -45.13221 | 2025-10-31 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c148eaa1-fa70-3f93-9753-c61399dfb0bc | -12.82553 | -43.48779 | 2025-10-31 04:57:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 592f8927-9e14-351d-8bc7-ed6ce79f2cdc | -12.28752 | -48.03928 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 587c1e34-050c-3f94-94fe-4195ceaa9270 | -11.01065 | -43.87848 | 2025-10-31 04:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2aa25d8c-851d-3c3a-89d7-f4b4603e6600 | -12.04529 | -54.24594 | 2025-10-31 04:57:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a68761ef-6fe5-3e3e-9ea4-b2c70e249573 | -7.80452 | -46.39743 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 536ba0d6-3bb6-3af5-89d7-68e7772ffb23 | -8.95715 | -47.51889 | 2025-10-31 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99e99939-94d9-3904-955d-60ec53ab304b | -7.318 | -44.9523 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 5a88e309-a61f-3c86-a9c3-262d43dd6e97 | -7.64356 | -43.58833 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1c21f86f-b0ab-3fe0-a2de-f12862f9e220 | -11.08314 | -51.54411 | 2025-10-31 04:57:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6dbf3759-0ed7-34e8-a462-21dd5e26ff61 | -9.87659 | -44.87019 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d398df05-c684-3da8-9cd9-747c34069ec8 | -7.66898 | -43.57875 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a768660d-5b39-3874-88ac-334ade5af2d3 | -8.32011 | -47.92603 | 2025-10-31 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 803e59f4-9b1b-39c9-b39d-6cf4b938a123 | -8.55997 | -47.78578 | 2025-10-31 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e844f4a4-ecb2-3f3c-9293-fbb4edcdbe5d | -10.4288 | -44.32618 | 2025-10-31 04:57:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbfa14ca-c746-39fb-98b8-03964474b0f8 | -5.74994 | -53.396 | 2025-10-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02976ef5-f87e-3bf7-9f40-5aebb2b11d31 | -8.17129 | -45.49497 | 2025-10-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e93ce1a1-1753-313d-8371-5fe66bdb9d26 | -9.52629 | -47.27044 | 2025-10-31 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f862bcde-3ca8-3205-b269-01e7f85727cd | -7.6229 | -43.56227 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8a84910-986e-3182-8a68-90630c1bee11 | -7.92001 | -46.79337 | 2025-10-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85113a75-2582-3d39-8e96-a06aabfd6fbd | -10.88523 | -44.36432 | 2025-10-31 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e8d3035-66fc-392c-b100-6587d623c776 | -8.5638 | -45.68726 | 2025-10-31 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0daca97f-4404-33ee-b8e9-c04eeb7b7d1d | -12.04474 | -54.24953 | 2025-10-31 04:57:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a405eab-8be1-30a2-86aa-ed6434e5c80f | -8.0522 | -49.63193 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd3161dc-a73a-3229-a5a6-32b0c208d64b | -7.33706 | -42.73199 | 2025-10-31 04:57:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2c32aa88-ce66-3129-856c-f8345093e9b2 | -7.76809 | -44.07425 | 2025-10-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29d2c3a3-4f0f-31ed-bf18-b197c87fbdcd | -12.27681 | -48.04834 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c85d7ca1-7986-340a-b6b0-dfd379645fb7 | -10.25839 | -55.26401 | 2025-10-31 04:57:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee9f6b9e-59b2-3a6a-96d2-7a51b0d724de | -13.39306 | -47.34055 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f452010-c42d-3914-9c2c-9b8428cc1b41 | -7.64334 | -43.57298 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f2c1ea6e-119d-3c9c-9d21-a5c711ce1782 | -7.81233 | -46.3934 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 24178aea-be6c-36b0-8bef-087905109421 | -13.38803 | -47.34018 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 298bc309-17b8-31e9-96f6-3cd210070240 | -11.12817 | -50.74828 | 2025-10-31 04:57:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2abc4a54-4208-3b98-a746-8715a058a671 | -8.09911 | -45.14442 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41294e00-9b0b-3dea-8bbb-247d8e7a3eb1 | -10.6437 | -45.24567 | 2025-10-31 04:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1edc7391-0019-3612-addf-99a3a0cecb9a | -8.09138 | -45.14063 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70279cd5-441f-3c6f-9812-7182d1214f1f | -12.56704 | -43.95968 | 2025-10-31 04:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0a97d0d-e4bf-36f2-8aff-e193dde0c4bd | -7.3142 | -44.98035 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 667b4639-89c7-308d-b0b5-1d1f63cadabe | -10.54454 | -44.7812 | 2025-10-31 04:57:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fd1a8240-e836-3216-9e43-7b48bf38fd10 | -7.5574 | -47.41563 | 2025-10-31 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12aecb8e-55c8-3465-b1cf-016457c4eaf1 | -8.09184 | -45.1373 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cd5c966-8e39-3319-8c89-d8963d487861 | -7.41407 | -43.34574 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08f8889c-4fcc-3107-b6e1-ccb08927ee1d | -9.86115 | -44.85667 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dff9e6cd-33a3-3509-b7cd-a18da0f22d8d | -9.34851 | -46.59646 | 2025-10-31 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c335086b-b8ef-3de2-b9f3-7242f2023391 | -7.80868 | -46.40349 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb478e84-6b71-3e37-a73d-3b386b7bbf48 | -7.81999 | -46.39441 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0cd87575-c3dd-3aa3-bd95-3a8fa2aadf43 | -10.53787 | -44.78829 | 2025-10-31 04:57:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| c72ad117-c2b4-3c61-87e5-1b87bbf8b351 | -7.79265 | -41.57343 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 45034e50-cc3a-3900-9f90-d543192a6fc8 | -5.13088 | -55.95597 | 2025-10-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e19955b1-ddaf-393d-9670-e186566265a8 | -9.46584 | -46.994 | 2025-10-31 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c12529e-9c65-3cdb-a7cf-2e2293f48c1c | -12.28679 | -48.04491 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d21c7717-54a4-39ce-a210-ded0d81f297a | -7.34057 | -47.63163 | 2025-10-31 04:57:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63afe061-2afe-3921-9a64-b15321215883 | -9.86491 | -44.87225 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e40e872-ca5f-374f-9f75-798cc2fe5af3 | -14.12991 | -44.18625 | 2025-10-31 04:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19e56928-3b51-3d6a-8a9c-56312be083a4 | -10.42245 | -44.32949 | 2025-10-31 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1021b66-d103-343a-a6b8-44549cde64ef | -11.11894 | -54.63298 | 2025-10-31 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3dcf716-1e91-3c04-b865-cd1676392788 | -7.35411 | -44.99166 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 9808b847-fd08-3fb0-82c9-340629de6a96 | -12.67542 | -52.61477 | 2025-10-31 04:57:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dff79ca-ca23-320f-a234-a1f2edbca954 | -10.64441 | -52.18558 | 2025-10-31 04:57:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9e9244c0-2bd6-3736-a6d3-83a16330f344 | -13.58998 | -47.35595 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a546bab-ec58-3f81-9ce4-9a0d7eae0b90 | -7.3504 | -44.99606 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ab1b66c2-0bba-32c2-846e-6a5ec08ccef6 | -10.89089 | -44.31693 | 2025-10-31 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e498789-8a73-30ad-b42c-b473372ae5aa | -5.75325 | -53.39651 | 2025-10-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b45d403-f5a2-334f-8d67-7569e7f89a92 | -12.28942 | -48.06135 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6561b5fa-1a49-3a13-81f5-a2cdfac112c9 | -7.66653 | -43.58037 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8ecc2602-5728-3884-8fc4-9f454c5ff382 | -12.30399 | -48.05926 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0a0bdd81-09ef-36c6-b517-d6dd43273a7f | -11.12116 | -54.64052 | 2025-10-31 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a40c5b4-55b9-3f38-9470-e0ce0b927e59 | -13.5109 | -47.33595 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b340a30-f977-334e-9d1e-c492e0cb675d | -7.81508 | -46.39362 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4c57aa54-0bdf-3730-82aa-efeacdda9d6c | -11.31657 | -51.44594 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9635b7fe-4300-35c0-bf86-be13ec7a9218 | -11.56307 | -47.08036 | 2025-10-31 04:57:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19b21f21-e490-3931-9df0-a4b4b980b28b | -8.09629 | -45.14482 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e308f91-a4cb-30b5-ba5d-ee8499773e2b | -10.64087 | -52.18504 | 2025-10-31 04:57:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a046a1d5-9c9e-3d17-b9c6-1a59ff5aae0b | -7.65886 | -43.59322 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fd8728e3-6b85-3f6d-8dee-95d53b4721ae | -8.71491 | -46.51769 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb103a38-c6e7-3ff9-b93d-e44a4e6e2006 | -12.17306 | -53.63072 | 2025-10-31 04:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ad39fff3-227a-3cc6-ba26-f94f83d19030 | -7.66483 | -43.59361 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e0d09b8b-c460-31b3-8b8c-7ef8fd46534f | -7.67258 | -43.58018 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a04d7dac-0b7c-3b88-a9f4-0697a7be2659 | -7.62234 | -43.56649 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1dddf124-58c1-3ab4-b1c2-3f05bdf1cdc1 | -12.28213 | -48.04409 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README39.md)
