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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1189e06-55c2-36d1-9831-7a2ae49d0a67 | -4.27941 | -46.36422 | 2025-07-16 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42bb71c1-ff8c-3575-8873-e1736a777f42 | -4.30069 | -48.10397 | 2025-07-16 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 43e4494e-9f27-3428-bca3-35497b773b96 | -2.92185 | -49.06348 | 2025-07-16 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d09ab56-dbb2-3b33-ba44-35e3ab18a173 | -5.53635 | -43.88534 | 2025-07-16 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6c58b8d-0406-33e3-9839-7b8540729255 | -3.38052 | -47.48189 | 2025-07-16 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0735ab77-d62b-372f-b031-53e33b76f51d | -6.13054 | -44.08025 | 2025-07-16 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8e31ffc-7c28-3d0c-90fb-7bc8db2f5214 | -4.58597 | -47.26091 | 2025-07-16 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2d55bdab-ef85-340b-9601-432a7b052e03 | -4.4068 | -42.14915 | 2025-07-16 04:12:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cf07d308-ec89-3ed1-8c17-33c64cbc9d49 | -6.43435 | -42.67203 | 2025-07-16 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b83eb4b-377b-3615-93c7-2c4b7ea74b97 | -3.03528 | -47.86044 | 2025-07-16 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f7251fdc-eafc-396f-9c24-68a5f3ce3712 | -5.5358 | -43.88884 | 2025-07-16 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4cf86d4c-ef48-3190-8137-94ab6353276b | -6.43821 | -42.66908 | 2025-07-16 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 084e480c-c4f3-3c00-a38f-7446e089841f | -3.31986 | -40.00631 | 2025-07-16 04:12:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d31914a6-8106-34e0-b26b-1d4f98ea7136 | -5.36191 | -36.89184 | 2025-07-16 04:12:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0c0eb9e-49c3-3c96-9ea0-f0b577696cd8 | -5.46223 | -45.33707 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 914955af-56c8-3214-8684-1d4f929b2f9c | -3.51883 | -48.43688 | 2025-07-16 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dbee700-d421-394a-bf5a-f0c24860c45f | -4.03476 | -48.0684 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdd2d6b5-4c7f-3b84-b99a-9cf17a35d73a | -4.02653 | -48.06707 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b1054b3d-be9f-322e-8701-4c4b8a01ad17 | -5.78046 | -45.08457 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26437196-e06d-39df-b7c4-ca1e0915fd47 | -6.45952 | -42.81459 | 2025-07-16 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 640edbc7-96af-338f-a45b-45df0e5f9c87 | -3.03055 | -47.86354 | 2025-07-16 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5315b137-80f1-35fd-91a3-c6941a0c3e12 | -6.39738 | -42.45292 | 2025-07-16 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 87cdda18-d1f8-32c4-aa88-a53a9294f78b | -2.58028 | -51.92318 | 2025-07-16 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45e2e4ac-3c43-3a50-884a-2df839600753 | -5.3731 | -43.92734 | 2025-07-16 04:12:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab046053-b23d-3314-9f33-496626edf1be | -5.7879 | -45.08194 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ca3cd85c-2b71-3579-ba70-be79e98b4a34 | -6.39405 | -42.45243 | 2025-07-16 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d05b214b-6be2-3ee1-a90a-a3687a696c91 | -5.78329 | -45.08885 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 177f8d80-9398-34c7-8f15-de561a93618c | -4.78031 | -45.34182 | 2025-07-16 04:12:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 49dfcdb7-63cc-34fd-bb85-0a8673b39b8f | -5.35697 | -36.89536 | 2025-07-16 04:12:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2010a171-a1f8-3ed5-90c2-e92c6db2df68 | -2.92634 | -49.06419 | 2025-07-16 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21dd874a-9dc3-3c7c-af9b-7463a3ef1f1a | -7.83868 | -44.19477 | 2025-07-16 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3da6291c-847e-36e4-a841-182ad8171481 | -6.90742 | -52.85921 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9785386d-0699-3653-9c82-e4476ca4268e | -11.1863 | -48.62782 | 2025-07-16 04:14:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 451e7286-f779-3626-b1ad-3fdf530f0b55 | -6.6649 | -43.04222 | 2025-07-16 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3673248-9b87-37fa-b630-037b24798902 | -14.15694 | -42.85019 | 2025-07-16 04:14:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f81a3579-ba8e-3eff-91a0-214467d5726c | -6.70349 | -43.91731 | 2025-07-16 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b09b4b76-3637-389c-94ed-876df52be8f1 | -6.94911 | -42.37685 | 2025-07-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fbadf852-1b61-3771-a6a0-e7b554fc4e0e | -12.47579 | -46.92732 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02faed70-f6b0-33df-942f-d82009457882 | -13.02267 | -45.05838 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0bf8863b-a641-37a1-b46b-880b2cbd373f | -7.18705 | -43.11425 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ea95a1d4-4913-38b0-bc41-78cfd13e4c0a | -10.95932 | -49.2522 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3871265a-dd55-3133-be66-462ff3b99f88 | -13.6492 | -45.7303 | 2025-07-16 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7bf75c0f-348c-3e24-860c-fab69202c39e | -10.32307 | -49.92017 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e825b6ce-0614-3524-852e-793fceed99f1 | -8.65097 | -47.75069 | 2025-07-16 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59a5b1b7-e2c6-3dd8-a0f4-572439d65339 | -10.65053 | -44.4836 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31f19eb7-d5bb-3465-b09a-37de1f9a6526 | -7.18981 | -43.11823 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 86422ae9-a0c9-3acc-97c8-43ab5c590611 | -12.07456 | -43.98026 | 2025-07-16 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3171a22b-5e1f-37dd-bd99-32ceb2e71138 | -7.18596 | -43.12117 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fd729f56-e0f5-3199-85a9-881789f61fba | -14.15465 | -42.84189 | 2025-07-16 04:14:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b92e55af-e1ce-335d-8d51-33a50bd4de0a | -12.14696 | -44.81697 | 2025-07-16 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52ad3558-cde8-3bda-8d56-d313a48a3944 | -10.31816 | -49.92334 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5eb8a1d-d37b-3a84-8060-bd7412e78e5c | -12.58469 | -44.79887 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2be45c2c-0595-36fb-9ae9-2548650fc312 | -10.32377 | -49.91623 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| deecd4dc-b63a-3218-9e44-e3d057acb0a4 | -13.01606 | -45.05729 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 05223f3b-80ae-3695-af31-0622e7b603eb | -9.66387 | -49.88876 | 2025-07-16 04:14:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1a51c86-899f-3de4-b059-a5b208d243d4 | -9.70025 | -56.18834 | 2025-07-16 04:14:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95061cb8-a263-31af-b0d6-1ae3373b4ea3 | -6.86692 | -42.75109 | 2025-07-16 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ac3fe96a-badc-3ffb-9cc6-072ba038d7e9 | -7.31514 | -45.77152 | 2025-07-16 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fea0e8a-1007-35fb-87a4-fa6661a51433 | -6.44084 | -44.96876 | 2025-07-16 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e1c788d-97c0-3fa6-aeb1-502699d5cce1 | -13.01824 | -45.06489 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1736f798-d6a5-3bf8-a4c1-85e29cf9ed97 | -7.31229 | -45.76711 | 2025-07-16 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4749784-dffa-3732-aa3a-2a235ec56f5c | -8.76113 | -46.59967 | 2025-07-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 836d3c49-0f68-3758-b275-b5b142f2bf6b | -9.80753 | -47.7505 | 2025-07-16 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc08e9b3-c187-3db0-b981-134b08ec9557 | -12.48206 | -46.93238 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df44344c-08e8-31e0-91f8-0dd82a98c471 | -7.18374 | -43.11372 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| af4978db-be66-31f2-8779-11f1631b3de9 | -12.42754 | -43.71961 | 2025-07-16 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be978626-673a-380b-bd93-ae3b17e199b2 | -7.1026 | -43.65019 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6b24b810-8cc6-38ce-9469-8aa45a5e9daf | -13.65252 | -45.73086 | 2025-07-16 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d0d1b45-2200-34be-b688-95fb53b34fcf | -13.0155 | -45.06081 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6e65b6ba-af7e-3155-ae12-3c812af71e8b | -7.18872 | -43.12514 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00c9b12e-8450-3936-af92-7444c666a3d2 | -7.34126 | -49.60435 | 2025-07-16 04:14:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38672fa1-5431-384f-9f44-b9b37c6a14ad | -6.72842 | -44.33713 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5affd7ba-3b2e-3eea-84e5-b494ba1dff47 | -13.02323 | -45.05486 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5a30ea3f-3157-3324-a30f-21a924d38aa2 | -12.47168 | -46.93061 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 905d7e26-3769-3f41-8e01-33f281c3b755 | -9.66687 | -49.89291 | 2025-07-16 04:14:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efa5a20c-c154-3d97-a571-e9e85e5d4db0 | -13.35736 | -43.78548 | 2025-07-16 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f14807ea-d64b-3ccf-a7cd-72707bb3fc85 | -13.02541 | -45.06246 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9315f8b-26ba-31db-8f5e-f45c69151416 | -6.91892 | -52.85752 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2c6a4d9-6a97-324e-8f2c-cf4cd37cfa90 | -6.90804 | -52.85572 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03a3af56-3dd5-3155-8a5e-06fe6eac6a09 | -6.49726 | -43.48286 | 2025-07-16 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d262a306-f09a-390a-8b52-ea16955ce449 | -12.48336 | -46.92463 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e2c8e66-bb82-3195-bb36-5c61a7683687 | -8.6472 | -47.75005 | 2025-07-16 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4aad08ac-8daa-3d93-93ef-0a0472a5e466 | -8.50906 | -43.30524 | 2025-07-16 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 07ace607-8142-3a27-9ae6-bc154793a55c | -7.94254 | -46.02445 | 2025-07-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2eaaa77-05f8-32f4-bc63-1916ea0be995 | -12.58855 | -44.79589 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15517f08-e7f5-34ef-9b28-70995caea72c | -8.5096 | -43.30176 | 2025-07-16 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a48ad3e6-df8e-3242-8e81-ad15b87a9948 | -7.10976 | -43.64777 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dc09d5a-dfe5-3fb2-a6c9-6c427ca9f076 | -6.48425 | -44.87102 | 2025-07-16 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d8af5b8-251d-3afd-b47a-317e55de3c74 | -10.32269 | -49.92055 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 244402d6-da99-31a0-ae72-529a854ec2eb | -9.43251 | -40.36732 | 2025-07-16 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 92f3747e-d205-33b8-9d13-28ae5fc60e97 | -11.99256 | -43.36855 | 2025-07-16 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53af8759-c97a-388a-b29c-faf8d5de17b0 | -10.32337 | -49.91661 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48b53a05-ae7c-3bef-b5cc-74c67e86e7bc | -12.47514 | -46.9312 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 080d16af-73fd-363b-80c4-2a93f571cb07 | -10.56533 | -49.1345 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8026642c-e379-37b6-ad05-951d62153f04 | -8.50571 | -43.28331 | 2025-07-16 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a0bc2d9d-412a-3273-8283-648a8ee82201 | -9.29845 | -44.84452 | 2025-07-16 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3510ff6-61de-3b3b-afd3-551680435d56 | -8.75538 | -46.59047 | 2025-07-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 351fcc1a-51f2-3ba4-8026-1f04eb42d133 | -7.1865 | -43.1177 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b8f70473-5dbf-31c4-88e5-af392b6a3c2d | -10.64667 | -44.48656 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65faa136-8a58-356c-a3b6-e4a78569e91f | -12.47925 | -46.92791 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README15.md)
