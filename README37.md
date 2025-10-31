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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54567b76-ba75-3902-975c-3e1c7d4181c8 | -6.81176 | -44.45054 | 2025-10-31 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9b1543d-770f-3575-9680-74fbe531c152 | -12.88501 | -54.75567 | 2025-10-31 04:57:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fed1f076-5a9b-354a-8cd4-eb82296ebc64 | -7.44285 | -44.2397 | 2025-10-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75557dc1-63b7-33a6-b314-fadd3a8f2a10 | -6.90975 | -45.5098 | 2025-10-31 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0465d9c4-1c74-3222-a1dd-34e7b03e4aa2 | -9.51679 | -47.26911 | 2025-10-31 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 899a8076-711e-3dee-8c46-40781ab24f17 | -9.52716 | -47.27149 | 2025-10-31 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 238d5bd8-29ae-3375-8a36-abc108820587 | -9.52166 | -47.20191 | 2025-10-31 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d31f68c-75a3-378c-82a5-fc6adc8e0527 | -7.81091 | -46.40409 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92df373d-4377-3c77-a242-f774d1e2c280 | -7.41348 | -43.35026 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c4c8656-5774-3ad0-bcec-fad92ad74933 | -7.35368 | -44.995 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 60e5164d-dda4-3835-9ded-3eb3ecfdc8af | -10.63792 | -52.18046 | 2025-10-31 04:57:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc93cd70-4120-383e-9054-4726bfb3794f | -11.12723 | -54.64507 | 2025-10-31 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2821791-4b7f-3f26-842c-74760b787b05 | -7.67441 | -43.58322 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c87608bf-7aa3-3d25-b92b-03ab4a41f39e | -7.65832 | -43.59741 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1fe764d2-298c-30e0-a84b-eeef17f51847 | -9.24592 | -47.53413 | 2025-10-31 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f439e528-3ca1-3c49-8ff1-a98ab646dc57 | -9.28519 | -47.65459 | 2025-10-31 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4700f813-0120-347b-9da3-0d9aa9b34bb6 | -5.71998 | -53.47983 | 2025-10-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d159a1d-e5c6-37f0-833a-245a0e181322 | -8.31933 | -54.95829 | 2025-10-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b19d4caa-05cd-3c78-9c46-db5b17640614 | -7.55823 | -47.41365 | 2025-10-31 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cdef456-d07a-3074-a1bc-53a89122089c | -8.57886 | -48.65979 | 2025-10-31 04:57:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d71a70c8-f372-3332-9fc7-1cd1e29a4ceb | -7.67198 | -43.58487 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fd78a266-a523-38be-81de-2c61477cc413 | -8.09331 | -45.14693 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7711f77-0961-352c-ad65-c0f0ba3f63d3 | -7.31942 | -44.94182 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 44186ba1-d28b-3815-9286-985619057f40 | -8.55859 | -45.68648 | 2025-10-31 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5568d43-7da8-3a5b-99e5-76e507b2e301 | -10.5572 | -48.99751 | 2025-10-31 04:57:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eed734e0-a4a3-3a16-a39a-017454e9d0a4 | -8.26045 | -46.35605 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 220530c3-5aaa-32fd-b7ad-a8ed2fc4cba0 | -7.64654 | -43.59527 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 60ba4fe2-03cf-3140-820f-a3985068005e | -7.66379 | -43.60169 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e3320f2c-cecf-30b0-a9f5-32d4814463b3 | -5.13149 | -55.95221 | 2025-10-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d25c6fc2-f61c-3871-9362-7906fbe41f21 | -7.81724 | -46.39419 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 548646bd-64b4-321d-8e39-ba261a0c6150 | -7.81433 | -46.39899 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1025e8c9-9113-3d66-b4de-2bc6e6ecbd9d | -12.15542 | -48.00931 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5686d080-eddf-352e-8b04-288194ba6d0c | -12.03107 | -44.81224 | 2025-10-31 04:57:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28791671-6800-3931-90a0-6852cb73de2e | -7.64518 | -43.57625 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 24480429-dfa2-3337-9818-6ae0a4d50e0c | -8.08693 | -45.13314 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b75ed098-c2bf-3cd1-9577-558a3ca1fff4 | -8.09675 | -45.14147 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 168a641a-b9e4-3609-a2e1-12e4fa6930c3 | -8.0923 | -45.13395 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3ec64d2-fbaf-34fe-a1de-4f603940841a | -6.90933 | -45.51289 | 2025-10-31 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e7138c9-c4a4-3730-aeaa-26f2c87c26e5 | -9.80103 | -46.96793 | 2025-10-31 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c05b9742-bf0d-3450-8b22-68d7610816f7 | -9.86538 | -44.86852 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8185c68-aa04-31fb-a762-6ac5812e76bf | -7.2541 | -45.57505 | 2025-10-31 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2610fca-e1b6-342b-8a3c-ab2f6e990abf | -7.61182 | -46.47277 | 2025-10-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bad98fc3-d31e-3f3e-a722-11659d40a9cd | -9.87707 | -44.86637 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d99572ad-6f62-38ef-8aae-f2ba1853474d | -7.65941 | -43.58892 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8fc91af4-0be8-3eab-9886-f4455466bb9b | -7.82214 | -46.39498 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a97926f5-6b63-33e4-a546-c9c9aa5ca4e2 | -8.16659 | -45.48995 | 2025-10-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd8b0517-50d4-3ee0-b196-89ce7d26de55 | -9.87052 | -44.87306 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da5d5203-4f03-3d88-98fb-d713aa271881 | -12.19144 | -47.03709 | 2025-10-31 04:57:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72e04681-ca07-3ff9-a2b2-5feae0dfe215 | -7.61971 | -43.63159 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0afcd622-0f09-34e7-94bf-35c7f937ed68 | -12.87614 | -54.74696 | 2025-10-31 04:57:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdb0b0f7-dc61-3cb1-ae26-d212795bbb11 | -10.89037 | -44.32125 | 2025-10-31 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75d12a78-4922-37fc-9e57-fc51032eb2bb | -10.53885 | -44.78038 | 2025-10-31 04:57:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f8f10de1-774c-3066-a1f0-4cc69416e16e | -12.16011 | -48.00996 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9549cf02-0c8a-3a89-bc8b-87c6264b1e6d | -12.5367 | -44.88315 | 2025-10-31 04:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 230f167d-e21b-3b4d-aa42-94d21a3694bf | -14.08301 | -44.15537 | 2025-10-31 04:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61694a71-bccb-30ce-9166-6409985a9c54 | -12.83189 | -43.4886 | 2025-10-31 04:57:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f122f2a8-4a3c-3ec5-9c22-7d3330a18ea4 | -12.53105 | -47.5461 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ae7b116-b7e9-32fb-b8ff-1983c57a9900 | -10.54405 | -44.78514 | 2025-10-31 04:57:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1731658e-52da-3c02-9a5e-70dd524a49c4 | -13.59552 | -47.35202 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd8c1ddc-c202-3948-a121-e3d6d2b60559 | -8.56273 | -45.68813 | 2025-10-31 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba0e2093-23af-3fbc-9e90-9426976eb7fd | -13.51056 | -47.33876 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fdb5d93-4654-33c4-8195-a8a5bc1cb3d6 | -5.17986 | -56.10778 | 2025-10-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9af0d542-5ac2-36a7-b7db-b1624a19981b | -7.60621 | -46.47754 | 2025-10-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 462ad6a0-8aad-34dc-ad0e-addb3aadf7a2 | -9.52241 | -47.27082 | 2025-10-31 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6570a3b5-c062-3377-8851-88957d21aa97 | -10.9335 | -44.16227 | 2025-10-31 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ecb2d00-108b-3a39-a20f-6f36e1108acb | -8.32052 | -45.37866 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8267b13-5dba-3b7a-a07a-88ce59296dae | -7.66605 | -43.60034 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e814007d-74e2-339d-af7d-7dbcee435c1a | -12.02578 | -44.80718 | 2025-10-31 04:57:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff51c473-ac2e-3b1c-8f7b-f76681d9454d | -8.55544 | -47.7852 | 2025-10-31 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3d405de-f617-3e7d-aba4-bede5288a2e7 | -5.13493 | -55.95275 | 2025-10-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b16c317-529a-3b3e-8448-31adac45e52b | -10.42197 | -44.33359 | 2025-10-31 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7bd3703-123b-3860-9ca0-95c272996196 | -12.3047 | -48.05383 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 07def7a2-0b33-382e-95c7-a37a721283da | -12.80646 | -43.48531 | 2025-10-31 04:57:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f59db1e-a030-3cb8-b6b4-6cf7a84c11d5 | -13.59537 | -47.35205 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a3cc9b7-35ac-34f2-80fa-7a2fcdf9d609 | -8.33224 | -47.93672 | 2025-10-31 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8d531b8-88a7-363d-992a-d16fd50d3795 | -7.37896 | -46.22149 | 2025-10-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7bb4ddf1-fce1-3de5-b5b5-4675c1825855 | -7.34993 | -44.99944 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eaf14c3a-9a60-3b66-b6a4-eebea6f62ec2 | -9.51832 | -47.26509 | 2025-10-31 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dac7c968-8799-3327-bade-37c14e5ac41f | -9.03134 | -47.45992 | 2025-10-31 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 57c98052-b618-303d-9582-5cbf440490bd | -7.81305 | -46.38799 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a43bbcb7-bfb8-3774-bb95-965ec6cba4cc | -12.94119 | -47.92863 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59b572e7-3867-305c-a44e-4fedf15bbd95 | -13.58979 | -47.35601 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2f12327-3fa7-301c-b1a3-0e050dae20a1 | -11.94357 | -60.48349 | 2025-10-31 04:57:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec0125fb-8fee-3e53-aa03-df16f1386547 | -12.28146 | -48.04925 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7b956cb9-35e6-3d5f-9796-cffa944d6473 | -10.42268 | -44.33309 | 2025-10-31 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 78367b16-3a73-3af1-a8bd-e058431c69e9 | -7.31263 | -44.95139 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 77456b3d-1c44-34ec-aca3-ca8e5ae3cfb4 | -7.66114 | -43.59211 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d37365e0-0254-3a71-9de8-4892e23c57ec | -8.06988 | -45.13754 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15017598-899a-3f2b-a07a-0193e989965d | -7.4485 | -44.24053 | 2025-10-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d75850b4-5198-3904-ad36-13a1b739c29d | -12.27216 | -48.0474 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a34b37f5-7e72-3155-a065-7a0c711dafbf | -12.93645 | -47.92778 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1ccdeba0-152d-363b-a9e3-d927378fa8ce | -7.64298 | -43.59263 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8d1299e5-88b1-313b-9e20-8c7807770b28 | -12.28821 | -48.0706 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea5744f8-a8cc-368a-9875-08189ffe3cd5 | -7.8018 | -46.39716 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 284f4378-6925-30ea-90be-bab7d46273d6 | -9.86023 | -44.86401 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0871c61-7ea1-3289-af19-fdc4fd920cd2 | -10.93296 | -44.16675 | 2025-10-31 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6df1fca-32f6-31ef-a45a-6ce3cda5f1dd | -10.53325 | -53.71265 | 2025-10-31 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b1abb86-0fc6-3869-bbd5-fdbbf4fe5220 | -7.62617 | -43.62824 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93407d27-8df0-3424-b9c3-45eb41b38f2d | -10.53934 | -44.77642 | 2025-10-31 04:57:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 862c3dd8-10bd-353d-9ab5-14ca58f51f36 | -5.85226 | -51.95697 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README38.md)
