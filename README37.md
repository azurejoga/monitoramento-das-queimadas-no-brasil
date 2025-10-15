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
| 43b8bb0e-d70c-31a0-b6f2-56139c421c51 | -10.13649 | -44.55033 | 2025-10-15 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f01e8ab8-0093-355d-a4dd-29e16cc66828 | -12.23155 | -50.41274 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ade7e9d-86f0-3f9e-99b8-87c6ce38b693 | -12.25067 | -50.41653 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30fe75ea-a446-3e51-bc44-0fe541e5549e | -10.04717 | -43.82864 | 2025-10-15 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 111d05ea-e981-3524-b482-07a02f0d1569 | -10.14408 | -44.54758 | 2025-10-15 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d44c774c-ba2c-3efa-8732-72f6f8ebbaf1 | -12.23829 | -50.40308 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 0fdfce72-ea4b-3db5-8bf9-2bfde910cead | -15.11147 | -42.47535 | 2025-10-15 04:08:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 675c98f8-71b1-3ef0-8246-c855fd61eda0 | -10.8462 | -42.75838 | 2025-10-15 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 292bf0d3-99b4-3ae3-88c5-020a78825d65 | -10.797 | -44.24178 | 2025-10-15 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7edc277-dfb6-30f7-a80b-2497da94779d | -14.27818 | -42.3341 | 2025-10-15 04:08:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 913b97e0-937b-361e-9ddf-84cdadb70bff | -12.22495 | -50.39495 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8d2debd9-f8bd-38f0-9060-9613da2f5514 | -15.41947 | -42.01664 | 2025-10-15 04:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 80255d72-250a-3c42-bd3e-036fba50486e | -10.14505 | -44.55087 | 2025-10-15 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0e273f97-cf7c-34a0-9190-2b882d69b4f9 | -13.20081 | -42.49558 | 2025-10-15 04:08:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7e781871-31d7-3ad1-82ef-9c976e2854a3 | -12.24404 | -50.39873 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 3af78f86-642c-3eb1-9ecf-e8cf7722df49 | -14.53553 | -41.66606 | 2025-10-15 04:08:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eee45bc7-47db-3ed1-ac76-c432ccec4432 | -12.22874 | -50.4012 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8db405e4-6488-3858-8b3e-be01007eed31 | -12.24295 | -50.43152 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11eef801-f7b9-31ce-b46a-01cabd825c4e | -12.24111 | -50.41463 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| c8987832-2ea3-325c-921a-7b61d56d9f11 | -11.91025 | -44.83484 | 2025-10-15 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e5c3da5-6c1b-3119-a56c-e828c74267ec | -12.24969 | -50.42183 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 335f5252-49cf-322f-a74a-69e1f137f14a | -12.22677 | -50.4118 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65cd7bd9-af51-3f85-bedf-a1984c7539c9 | -13.67204 | -42.49987 | 2025-10-15 04:08:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2bff0b30-2729-3d6d-ab5b-cdbce4c8f863 | -10.84013 | -42.7538 | 2025-10-15 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2de5f86c-7cff-3325-9631-afb300d729e4 | -13.76144 | -42.55731 | 2025-10-15 04:08:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cea28f3e-ae9a-3b65-9c94-577419223efc | -12.23253 | -50.40744 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a959ba22-b8b0-3c5c-ab2e-1b8f7173aae8 | -11.77731 | -43.73487 | 2025-10-15 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a062f167-0ceb-3188-858c-a8e99042e3cc | -12.04089 | -44.2507 | 2025-10-15 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e587367-90af-38c3-ad5e-b590294780df | -10.5175 | -43.36853 | 2025-10-15 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2527c8ff-7423-3bda-b6fc-bacd1eed3999 | -12.24687 | -50.41027 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5af93b2-b8fa-3157-96b0-6bf5d329067f | -13.92325 | -42.34674 | 2025-10-15 04:08:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 02bb251b-a9a8-3175-8d9c-40c2855e62ce | -13.87858 | -45.53962 | 2025-10-15 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 03489fd9-b0b5-3ba3-858b-7e99f94f7ba1 | -11.7178 | -44.27743 | 2025-10-15 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c157e83b-b5e0-34eb-bb03-531768eb404f | -13.55352 | -43.69741 | 2025-10-15 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4b14fdd-ea46-344e-ac38-3044fb72dfae | -13.47462 | -43.70328 | 2025-10-15 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8614cf06-d8c1-3ed7-ade9-658e60dcfda5 | -12.22972 | -50.39589 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d328ae4-ce8c-38d6-8129-d75704f643a6 | -10.04439 | -43.82439 | 2025-10-15 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8065cfc0-7c32-3814-957a-f08f80e764f6 | -10.49134 | -44.41744 | 2025-10-15 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1803bb1-7e21-3ac7-a95b-f9622f7315ca | -11.9068 | -44.83425 | 2025-10-15 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 138ad2ab-9557-3357-81fe-6b6995c816ea | -12.21144 | -50.41428 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e2b01768-d830-3680-88e0-ef13f0ef8c07 | -10.14157 | -44.55029 | 2025-10-15 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b9c86a39-01a9-3834-8187-7cd60969cc62 | -12.2345 | -50.39684 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c562451-6ee4-357b-aa1f-076d1713c8cc | -13.28007 | -43.43314 | 2025-10-15 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2c0543b-7a13-326d-9432-e56e35d56df5 | -12.21622 | -50.41523 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c735cc65-7f07-3d36-a83b-531453ac0e52 | -12.23535 | -50.41899 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c683dcba-ebc5-3a85-a5ac-5d4b44857bba | -11.979 | -44.79852 | 2025-10-15 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d617c8ee-20ee-3b76-88d1-e8a2dcba49df | -10.41137 | -42.5657 | 2025-10-15 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69f129af-1f38-329d-89c8-dd63b5531637 | -10.14223 | -44.54637 | 2025-10-15 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f488c94-5c04-3d4b-9631-9fee0076b41a | -12.6525 | -41.27283 | 2025-10-15 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0b1c4dbf-009d-376a-93de-7bd10cfe69c7 | -12.21161 | -50.38684 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9999c3ad-8ccd-3f07-b79f-15c2838d0f5c | -11.85544 | -47.14209 | 2025-10-15 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d53d2ae-a40b-36fa-84d1-949ca9d12138 | -13.28064 | -43.42958 | 2025-10-15 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b995b4b4-6a57-34e2-9375-532c99cf7ade | -11.53823 | -43.50702 | 2025-10-15 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b943202a-cbe6-3f0b-8caf-646f865764f0 | -12.24589 | -50.41558 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 767a0e5a-cf5e-3088-bb0b-8a63ad9d9d27 | -10.80103 | -44.23859 | 2025-10-15 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0f72c66-4b7c-3f1e-b597-5dd1843de3b4 | -11.53489 | -43.50646 | 2025-10-15 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97a5840f-58ad-3b12-8347-3e2d43c4b5eb | -12.22593 | -50.38966 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46882bd7-5197-39bc-989c-8094564e57d0 | -12.20666 | -50.41334 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fcdd306b-58c3-36d5-90f4-cdc6a2a80310 | -12.24784 | -50.40497 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0384451c-ecc2-3aeb-a19e-7bc389b4be99 | -12.24774 | -50.43246 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 060efa05-4327-37fc-a75b-5c5c4413ed11 | -10.51415 | -43.36799 | 2025-10-15 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24583585-1954-3907-b9ba-318814930931 | -10.52141 | -43.36552 | 2025-10-15 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76f78c21-dd45-336c-9d42-a0b0309b2a59 | -14.80145 | -41.88964 | 2025-10-15 04:08:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0c9061fc-ec16-34e1-abe1-d246a996bb16 | -13.66872 | -42.49932 | 2025-10-15 04:08:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 920597c5-8910-34ba-9566-0be8cb3c0cfd | -12.22578 | -50.41711 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d3956982-f398-3243-bf1d-b394ce555691 | -12.24872 | -50.42714 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 743ba02c-f7af-3329-be79-6add7bc15309 | -10.1457 | -44.54696 | 2025-10-15 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dfde16a0-65a7-33d6-a717-753db3b341da | -12.21639 | -50.38779 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4dfd3924-ace3-3b78-9a09-8d7eea5a8a50 | -12.38297 | -49.41156 | 2025-10-15 04:08:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c027e43-29ce-3cb5-acf2-b2dcc56069e9 | -13.47852 | -43.70026 | 2025-10-15 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f1c284d-5d4e-374a-8834-b81741350730 | -11.53765 | -43.51059 | 2025-10-15 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e33a6697-70ac-3e06-a863-31d8a3d9c787 | -15.8802 | -41.74835 | 2025-10-15 04:08:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9b532204-7023-3e85-890a-d0108836e662 | -12.22116 | -50.38873 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22f09522-1feb-3189-b549-86021e9eb160 | -12.23927 | -50.39778 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 58dc3817-a3dc-3313-b310-36c4e83fbd06 | -12.04185 | -44.25072 | 2025-10-15 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 736b74c9-50c7-3108-87f7-9b94f1b50c5f | -12.18345 | -47.75936 | 2025-10-15 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0844283e-89c0-3269-b09a-431e07326a4d | -12.23633 | -50.41368 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| d9d28fb7-cb88-359e-96e2-e76dc3642d4f | -11.23094 | -39.24162 | 2025-10-15 04:08:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bc1d146f-09c8-386f-8fd6-f9ffb3870b75 | -14.83614 | -40.98195 | 2025-10-15 04:08:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a91fe5d7-299f-3333-993c-d158967b7a18 | -12.24182 | -49.36292 | 2025-10-15 04:08:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f20dd3a1-22fa-3b97-be88-43abe0a25eef | -12.9424 | -42.43211 | 2025-10-15 04:08:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c924b24e-53b8-3aa8-88a1-b6f1fac42faa | -13.38323 | -43.65845 | 2025-10-15 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cc389a3c-64ca-3d76-af5f-36e7606bdf40 | -11.53432 | -43.51004 | 2025-10-15 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0368cb6c-f547-3e6f-9bba-9cc84adece54 | -13.38655 | -43.65901 | 2025-10-15 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6ad59977-ced6-369b-814b-1a4d531c9f19 | -13.4752 | -43.6997 | 2025-10-15 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d494c2c-78bb-3424-9005-3bc38a07f83a | -4.8916 | -43.4446 | 2025-10-15 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 73d7e263-295a-33ef-8808-c9d37a7a006e | -7.9439 | -44.1381 | 2025-10-15 04:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 88c64a9c-907c-3b6e-9fb0-5540010a7b22 | -5.4465 | -44.2159 | 2025-10-15 04:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| fd524bcc-be41-36e0-b90b-3c0ef0b04241 | -5.4278 | -44.2172 | 2025-10-15 04:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| b729109a-8b0f-36e8-ae6c-167f118a45fe | -4.8915 | -43.4678 | 2025-10-15 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 54fc15c4-b7a6-3fec-9adc-ad58f059b025 | -5.4276 | -44.2402 | 2025-10-15 04:10:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6bef385c-955d-38da-8430-8e3aa98904ee | -4.9104 | -43.4434 | 2025-10-15 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 0642aa34-a36e-353c-9345-00f677a6627a | -4.6509 | -43.1337 | 2025-10-15 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 682b4741-8a64-3b9c-b098-5ee86a3a5ead | -4.9102 | -43.4666 | 2025-10-15 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 271.4 |
| 65bc7d91-8cbb-322b-aa23-c039bb9de755 | -18.19562 | -50.74374 | 2025-10-15 04:10:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb0ef2a5-8707-35b6-9283-36dd432299b4 | -18.19465 | -50.74592 | 2025-10-15 04:10:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37537bc7-1cdf-3e16-a1b9-0a3321bb55f5 | -19.05119 | -47.20478 | 2025-10-15 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e72cce08-6b41-32c3-9654-2876190978d6 | -16.87718 | -49.01363 | 2025-10-15 04:10:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2a99280-2b0b-32ad-abf2-74600912231f | -18.26236 | -48.24864 | 2025-10-15 04:10:00 | NOAA-20 | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0451e474-df75-37ea-98e3-fd09537aa073 | -23.58319 | -46.43424 | 2025-10-15 04:10:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |


[Clique aqui para ver as próximas entradas](README38.md)
