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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 411b354f-9be3-3dbc-975e-492a476985df | -12.21437 | -56.55798 | 2026-06-30 04:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 734dfc40-4569-3584-b4cb-1dd58cf6bda6 | -11.32099 | -54.46586 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 012cf6a7-848f-3655-b640-d5e7e9795df8 | -11.92022 | -57.39912 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fad853c-909e-3077-96fa-60c76040394a | -11.90508 | -57.41129 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acac2687-f7f8-3327-8d21-3d78b8d647ae | -9.91277 | -46.29195 | 2026-06-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4a18507a-34e0-3742-a4c6-7cdabfb78c24 | -13.25993 | -56.80649 | 2026-06-30 04:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 929b1b14-d4ac-3b47-bed0-283f48f4402e | -11.63449 | -59.013 | 2026-06-30 04:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a894d69d-7d28-3e29-ad3e-adecfa0f46a2 | -13.69821 | -47.8681 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 727d0c2f-e1da-3608-aecb-4ed8ff9aea25 | -10.12276 | -52.41273 | 2026-06-30 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9d73743-c3a0-3d08-bdf0-459587dcd9c6 | -12.20657 | -52.86721 | 2026-06-30 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 42f4ecfe-1086-3802-9e54-4e5ed9ad7376 | -11.88932 | -57.13861 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 80053e40-4166-3e0c-99ad-68518fecd17c | -12.19751 | -52.86557 | 2026-06-30 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ed893308-4d84-3ea9-a359-143a135c89c9 | -9.60858 | -56.92403 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e33446d9-e67c-3d7f-b2ba-9995b2a7ba71 | -12.85851 | -44.34249 | 2026-06-30 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6f4dc173-6ef5-3550-87eb-84b50a77a08e | -11.90382 | -57.384 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7523e1f5-ddc3-3c4d-98f4-98d2a4830496 | -10.86539 | -44.32151 | 2026-06-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18686482-bf71-3759-983f-7e0d6b9ed996 | -9.91553 | -46.29602 | 2026-06-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c6608592-72f4-33e6-9e2c-fa09c0e3c4c2 | -10.94145 | -43.04335 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 0a53e452-f03e-348d-b3d1-8ed8608748c1 | -11.3153 | -54.46798 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42e52223-49e2-3e84-ab19-a170773302aa | -12.51176 | -48.26677 | 2026-06-30 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3d23816a-32ff-39cf-b9d9-90eb89c1132f | -10.85626 | -56.66264 | 2026-06-30 04:21:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd79e190-4100-34f3-b70b-60866e8d0e8b | -11.11154 | -54.14538 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9f42337-112f-3a08-8e91-a7c9cd47502b | -11.90481 | -57.38131 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97402851-a143-3d6b-ab38-7a624c42d52a | -11.22409 | -54.31963 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 609f69e3-ae8b-3009-b6f0-c4d37abfb2bb | -10.78879 | -54.10679 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02302e3c-8d7d-39b2-874e-db41e9edb7d7 | -15.70518 | -43.75744 | 2026-06-30 04:21:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 70b559a9-a7b2-3f8a-9838-30a56f2204f8 | -13.72389 | -47.86822 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3a4433a-413d-3e50-9d90-299799323633 | -13.71111 | -47.87409 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9fbfa34-0959-3013-bfbf-dae0dc91fe9f | -9.39654 | -47.36685 | 2026-06-30 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fb393fb-ab89-3f10-8207-94b34b3388ec | -13.72083 | -47.85683 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fced9b64-40fe-38fe-8815-06f91b4244bc | -10.29793 | -57.12872 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 26d2d588-3c6e-3ea4-b221-1f366181c3e7 | -16.7513 | -45.81904 | 2026-06-30 04:21:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfd996cf-36ab-3a3b-a9e3-c18ed08eb119 | -13.72025 | -47.86037 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91c29250-b7c4-3df7-bb52-7a544dc9c2c0 | -12.22015 | -56.55897 | 2026-06-30 04:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f87746a9-2eee-32fa-91f9-74b889049749 | -10.72254 | -56.22769 | 2026-06-30 04:21:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85560b25-dde8-3e83-a618-edc485504982 | -10.13356 | -52.40492 | 2026-06-30 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3969cee8-7729-3a92-84fc-93b9be1b372b | -11.90474 | -57.37927 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79979316-e614-3bc3-8e59-050cee81428e | -11.38058 | -55.8075 | 2026-06-30 04:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 685197b3-83b1-3718-8b33-854565bbd08c | -11.79618 | -57.00137 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 75a9c6d7-8cce-3755-a107-454b90bd32e5 | -12.52522 | -48.29293 | 2026-06-30 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3823ac06-8aac-3a2e-aca3-fd003f0488cd | -10.94203 | -43.03939 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| c5a44a1f-b323-3d9c-8e4f-cea2e472cfa3 | -11.77729 | -46.40334 | 2026-06-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd466325-6848-374b-8045-5f309f4a7cd6 | -10.32392 | -46.5112 | 2026-06-30 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19f63288-1f22-3ea7-a348-70536b4985cf | -11.22466 | -54.31657 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8d23acde-f0e3-31e7-9d9f-44e0bc125262 | -11.22579 | -54.3105 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2026e848-08f9-3867-8f33-72079624faf2 | -13.71968 | -47.86394 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a0fe910-c3e9-3a0e-bba9-cacb72fac687 | -13.26239 | -56.79421 | 2026-06-30 04:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c0219931-30fb-3f9a-8f32-7c468ecae335 | -9.32611 | -58.01328 | 2026-06-30 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c226ab9b-d6bf-3410-9ae9-a80430cf6d73 | -11.90315 | -57.13177 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7334b5f1-95ca-3716-9b52-aedafe11412f | -14.63215 | -54.45933 | 2026-06-30 04:21:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b2ec89f7-8036-3366-9ba5-8c2567cd08a4 | -12.85765 | -44.33934 | 2026-06-30 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14c4d8ee-43a3-3cb1-992c-1f15c5ad37f9 | -9.81289 | -46.4687 | 2026-06-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9df77f92-fb82-3357-8d36-e2712820f270 | -10.78429 | -54.10282 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16e33c9f-fdf0-3ad7-b1d5-1cd731f715bd | -11.88515 | -57.12823 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f498e90a-0995-31e4-863d-e8da89314d28 | -11.91812 | -43.39667 | 2026-06-30 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 60cadd9f-31fd-321b-9db5-f939b2da9a15 | -11.77342 | -46.40634 | 2026-06-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09645168-18f8-369d-a2c5-cce3f26e58ae | -15.75851 | -42.53772 | 2026-06-30 04:21:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 963d214d-8fe8-3a5b-90ba-c481be7121b8 | -14.63089 | -54.46069 | 2026-06-30 04:21:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fefb61ba-1f2c-32f8-89da-f43f6a95da9a | -9.45334 | -50.84131 | 2026-06-30 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e81b3600-29ae-3add-8688-02d27fb31118 | -13.2748 | -49.77013 | 2026-06-30 04:21:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f392ab6b-c56a-3ca8-8598-5544d6d0339f | -12.52586 | -48.28905 | 2026-06-30 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00b869d8-e08b-39f7-9c9f-a5ebb7c3ccdc | -10.17734 | -48.34445 | 2026-06-30 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35158dad-448b-391e-92af-98b3da9d7940 | -12.21936 | -56.56302 | 2026-06-30 04:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 21cb3552-e30e-378a-80ab-41c0d4288c10 | -10.29701 | -57.13353 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e70b9dfc-080d-3afa-9c94-9574090258de | -11.78517 | -47.57008 | 2026-06-30 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1485017c-da7e-3572-ac3a-bffe4f3642c2 | -9.45268 | -50.8451 | 2026-06-30 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0df834b-3efb-3246-9e0d-9aba53548433 | -13.23838 | -51.56433 | 2026-06-30 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c523b847-ef06-3b29-b336-de1a04fdeb61 | -10.93854 | -43.03887 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 55d470c4-df90-3eb6-a8d3-79459a6b4abc | -13.26319 | -56.79016 | 2026-06-30 04:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e00d18c2-7c2a-3ebf-b875-47d86a18c052 | -10.80527 | -48.5663 | 2026-06-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4edff68-e135-3e5b-b156-687b54e0ae22 | -11.9041 | -57.41615 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85e24357-fc17-3e4d-b71b-e813695c844f | -11.23481 | -54.31843 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2a9b1f2-4ffe-3973-8518-1c48d04607f7 | -10.9103 | -56.85801 | 2026-06-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8886a99f-270d-3013-8871-aa44f543f706 | -10.58811 | -55.42227 | 2026-06-30 04:21:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32240e3f-80fc-3ec3-a65a-41f94976db41 | -12.37092 | -43.8937 | 2026-06-30 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 019125d0-aa9d-3cb3-9ded-2ea5e8f321f9 | -12.60331 | -57.88649 | 2026-06-30 04:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d2c186a-57e0-3aab-8910-41d575b8f2aa | -11.58345 | -47.9244 | 2026-06-30 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6749410b-0413-37d3-bba0-d10632a220bc | -11.89893 | -57.12159 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 066dbf53-0a06-35af-b55b-74eb6d63889f | -9.91221 | -46.29549 | 2026-06-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ef793e21-1fbd-34fc-a09f-c1c43763d5a4 | -12.20204 | -52.86639 | 2026-06-30 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f9c5bc4f-6713-31d7-a007-c81d4bb668c9 | -10.78787 | -54.10635 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b98a590d-0372-32fb-beca-e1d6c1c37c55 | -10.85363 | -56.66091 | 2026-06-30 04:21:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd4f8bd3-7ba0-39b2-a9ea-1505b545920b | -11.88424 | -57.1328 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 981af5ab-7b03-3008-be8a-735cb1172b9d | -10.78932 | -54.10384 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71682088-c035-3b2d-b008-5b61e4a876b8 | -11.21503 | -54.33996 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffa65282-6a8d-36e0-9427-718fca373bf3 | -10.69852 | -49.61148 | 2026-06-30 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9f86cc7b-9ccd-30aa-a6b6-c16848b98899 | -12.8509 | -44.36108 | 2026-06-30 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a87e279-d7c8-35cb-ad6a-c4350998a847 | -13.71747 | -47.85613 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16450dcd-0234-37c6-8cd9-f6047a705c4a | -10.14352 | -52.40178 | 2026-06-30 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b321eda1-4440-3eb1-a9ba-4d3b8835605c | -13.25504 | -56.80114 | 2026-06-30 04:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 19aee0c4-d56c-3b7d-826a-801c56137ddb | -11.89966 | -57.37548 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae9b5342-3c49-34ac-846b-d625117cebf4 | -9.2926 | -48.18369 | 2026-06-30 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73cbbb63-85cf-37dc-a89d-b22969845bb4 | -12.85709 | -44.34306 | 2026-06-30 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 512f9a06-7f99-3a74-adfe-7415d5a1479a | -11.93451 | -57.71208 | 2026-06-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9e5ec8ce-71ff-3ea1-a2aa-3faaf35cf194 | -12.20964 | -52.86981 | 2026-06-30 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99bbf1dc-b051-3d6e-8613-ff52ac6faadc | -10.8039 | -48.57452 | 2026-06-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94fbb011-2804-37ac-8bf7-3d6d0684ebf5 | -11.47325 | -47.4123 | 2026-06-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e58a2dc3-04da-3a68-8dbd-fdb42ddc6626 | -12.21517 | -56.55392 | 2026-06-30 04:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1b1409f1-e4df-3786-a853-f6c4ab8b0a00 | -11.21446 | -54.34299 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 016d3afd-095e-3d9b-a919-1e7f8611f95a | -11.93927 | -57.71071 | 2026-06-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README8.md)
