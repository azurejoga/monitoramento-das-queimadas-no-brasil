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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b9c8f18-08f5-3ef0-820b-ee4e9aa91e8e | -21.75675 | -45.50256 | 2025-09-15 04:23:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0a0db3cc-df0f-3bdd-a72b-4f5575354988 | -22.22721 | -48.61444 | 2025-09-15 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 06836285-f0e5-3e72-ba1f-e94bb902abce | -15.80118 | -53.51299 | 2025-09-15 04:23:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0caeb8a3-3a19-3658-abe9-5a608219646c | -18.6207 | -50.39404 | 2025-09-15 04:23:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5290a45f-051a-3726-a6c2-07f45232e93d | -18.5966 | -47.20551 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a0fd992d-aa86-3d71-8e3b-edf4e6f22ec0 | -22.29631 | -47.94776 | 2025-09-15 04:23:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5183d94-15ee-39c4-8897-90541dc2bf40 | -18.61631 | -43.96889 | 2025-09-15 04:23:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7dab1c4c-d080-3dd0-8ada-110a2ba4d1ab | -16.48856 | -55.10201 | 2025-09-15 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9bf842b1-f629-3294-aad8-e441e9793ee2 | -18.89867 | -46.62848 | 2025-09-15 04:23:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 750f354b-5eb0-3bc8-aa7d-f199fa0c321d | -21.80356 | -47.087 | 2025-09-15 04:23:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 882507dd-7f21-3bcc-ad8e-e4f5e4480836 | -18.63222 | -47.32734 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c65eea0f-5e15-3123-9102-cfac0e72dd10 | -17.40324 | -49.26297 | 2025-09-15 04:23:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 068e7626-92ee-3fa6-9656-6fda4aff53d8 | -17.84133 | -44.30428 | 2025-09-15 04:23:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fbd7153-99a2-38d3-8d17-073c75c6f922 | -18.16551 | -49.20452 | 2025-09-15 04:23:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7f496b11-4d39-3698-917f-5bd6940694c9 | -21.6335 | -46.81264 | 2025-09-15 04:23:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9710cd9c-a2c6-38f3-8b77-a0ed04c88d87 | -22.20078 | -48.3472 | 2025-09-15 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| daa9c2e5-42b4-3e3c-adf1-dcb6d840d67a | -17.35166 | -46.65729 | 2025-09-15 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f551c58-4520-35e5-b53f-4f201d478cf5 | -16.66702 | -49.77688 | 2025-09-15 04:23:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afb165ee-59ce-347d-8ac3-f2797851ba87 | -17.13018 | -48.51187 | 2025-09-15 04:23:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4afd7e1b-16ca-393c-a95e-680632b99b96 | -19.74775 | -45.12633 | 2025-09-15 04:23:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1ababd6-dc07-38cd-92d6-e31c8ab0a041 | -16.70714 | -54.96954 | 2025-09-15 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bae409e0-bdbe-3879-997b-533290997c1a | -18.26025 | -49.46103 | 2025-09-15 04:23:00 | NOAA-21 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0f3799a-60f1-3f28-8212-1ccdea0b2bd7 | -18.58427 | -48.1524 | 2025-09-15 04:23:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc68864b-a190-3011-9556-e4627f96cb42 | -18.46693 | -49.57315 | 2025-09-15 04:23:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f8382347-1ec0-302f-ab2e-4e12a3643eb0 | -17.1721 | -49.38454 | 2025-09-15 04:23:00 | NOAA-21 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eca0a93b-69d0-33df-b619-c394bed9e680 | -17.13352 | -48.51244 | 2025-09-15 04:23:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7861ef48-3374-347c-9557-729920468f0e | -21.61341 | -46.82151 | 2025-09-15 04:23:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 28e17db9-88ef-3af9-a64b-a633e20935b7 | -18.03276 | -46.95919 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbf31b62-9a0e-3aad-8f4b-b82d3baa4395 | -17.41005 | -49.26416 | 2025-09-15 04:23:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24998509-1867-3fc0-b754-efc2c2728192 | -20.82232 | -45.60482 | 2025-09-15 04:23:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38c1ead3-655b-3601-a476-b544f13ef933 | -17.31462 | -46.6102 | 2025-09-15 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| feedf582-86bd-3c54-a77d-8749af2fa17a | -22.17266 | -49.61148 | 2025-09-15 04:23:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2c9d706b-18f2-3681-bab9-fd3d64a6fdbf | -17.38015 | -53.25431 | 2025-09-15 04:23:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 446e58f7-b02f-3e19-b477-6a08e620c72d | -21.37403 | -49.75077 | 2025-09-15 04:23:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b533c9c0-618d-321b-a281-8c090806e509 | -20.19744 | -46.28669 | 2025-09-15 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f4d9625-f2f6-3fcb-b282-b1c5c3a8669e | -20.23414 | -46.17761 | 2025-09-15 04:23:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22516507-bf6e-3023-8945-0a8f38142e07 | -20.51818 | -55.63716 | 2025-09-15 04:23:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84e736ec-7dfe-32e3-ab96-c29af72f8436 | -17.14566 | -48.52222 | 2025-09-15 04:23:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 112babe7-cd00-3a02-bb9a-083d5b0a7686 | -19.0096 | -46.24403 | 2025-09-15 04:23:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d82ffa25-ebcc-36d6-961b-b9b93ba41ff5 | -19.03259 | -48.43614 | 2025-09-15 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cba52df-781c-33d1-82f3-d62523b9e07e | -17.39373 | -44.27567 | 2025-09-15 04:23:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f99fd7d-0f05-3bd4-ac97-72c05bcd34e0 | -16.62271 | -48.96555 | 2025-09-15 04:23:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ac42f8a-6215-3a22-9d5e-bfa7d4897922 | -15.79324 | -53.50709 | 2025-09-15 04:23:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97fdcecb-9f0d-3406-a462-15d39281b810 | -21.3713 | -49.74633 | 2025-09-15 04:23:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dadaeade-fcb5-35a9-9371-237490265870 | -16.7056 | -54.95214 | 2025-09-15 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| acb2427b-194b-3988-9beb-2cfce8efae5e | -20.51433 | -55.6347 | 2025-09-15 04:23:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e5e7528f-546b-3041-a7a6-ee08ca40f6d0 | -20.51796 | -55.6405 | 2025-09-15 04:23:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a11feb1f-a291-384a-a4c8-967eb44b14f6 | -16.70911 | -54.96635 | 2025-09-15 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8d541cc1-6ee3-3a41-8a7b-c5aaa5f8d65b | -17.27457 | -46.10851 | 2025-09-15 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b35152a1-7286-3ecb-8496-a2764d1baeac | -22.80057 | -47.80281 | 2025-09-15 04:23:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6af1a3ae-145f-316b-9014-16cc54187e60 | -19.30601 | -45.45875 | 2025-09-15 04:23:00 | NOAA-21 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4ba32fe-c814-354b-97b7-c3e64844a93a | -15.80174 | -53.51279 | 2025-09-15 04:23:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7a814328-73c1-3885-9f9a-60977bdd324c | -22.93504 | -46.44749 | 2025-09-15 04:23:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3e541889-b9fc-39aa-9578-ed29e7243a7e | -19.7448 | -45.12163 | 2025-09-15 04:23:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2f04793-cc69-30ec-a4db-959bb7a6dc71 | -17.49119 | -44.32733 | 2025-09-15 04:23:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb56eafd-0407-32a5-a9a9-954fa314d6bc | -18.61924 | -47.19077 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 803b41a6-8f2b-3346-af85-2776f40c181f | -20.57903 | -43.75148 | 2025-09-15 04:23:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e66d64af-f5d5-31e0-a8b8-cec073495a6f | -20.85538 | -46.21436 | 2025-09-15 04:23:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a34eb84a-26ae-37eb-b763-20b39e71c280 | -20.83799 | -46.47931 | 2025-09-15 04:23:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| e0e5f2f2-1407-3ff9-a4f3-ef0970353fe5 | -18.03607 | -46.95973 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 032b6f9c-c8c7-33b7-9162-2b90e2fc4c75 | -20.52278 | -55.63803 | 2025-09-15 04:23:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b34913db-4deb-32a3-adeb-9ced24076748 | -17.9974 | -46.94605 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ccec850-fb08-35c9-9e9e-e05ee87de27b | -17.14233 | -48.52161 | 2025-09-15 04:23:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f75e7a4-5f98-3887-bdbc-8692ed5e9493 | -19.97554 | -44.11652 | 2025-09-15 04:23:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c44afa81-eb98-3939-a63e-78311b933321 | -17.24288 | -49.46599 | 2025-09-15 04:23:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4d35e873-c6b3-349d-9cd1-084bb8847970 | -20.78757 | -56.93844 | 2025-09-15 04:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fe495997-900e-3758-a30c-2eba919b8907 | -18.44852 | -47.19579 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 936e5488-26b4-3ed9-9e5c-1f5f4257950a | -18.47041 | -46.94212 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0bc6a762-0efd-32d0-a274-37c2278a2ef0 | -22.2278 | -48.61074 | 2025-09-15 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a054d26a-5e7f-3847-b9ec-85828d5da3db | -22.30019 | -47.9446 | 2025-09-15 04:23:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f900ec3-8245-3f1c-81c9-43b67a21cacd | -16.67746 | -49.7789 | 2025-09-15 04:23:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76bfcee6-ffdb-378a-9afb-ae161a94aade | -19.97945 | -46.75897 | 2025-09-15 04:23:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0c6827a-9ae6-33fb-9430-ad3f47428f94 | -18.02944 | -46.95865 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e81130ea-745e-31a2-8895-436ea06ef74d | -21.12842 | -45.94305 | 2025-09-15 04:23:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 27852423-d0bc-3053-9cdf-3695d0d3e4a0 | -20.52355 | -55.63632 | 2025-09-15 04:23:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e01801e-e630-3f09-9f45-2579b319c9f9 | -18.03329 | -46.97787 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f60d2f83-76c8-3f47-93be-b5f3ae3f9c5c | -19.71975 | -45.45006 | 2025-09-15 04:23:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c658119-8b4c-30fe-b443-41b344744e52 | -20.77286 | -56.93188 | 2025-09-15 04:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f39bd673-46d0-3556-a2f6-0e509ebba7d0 | -18.75368 | -47.0233 | 2025-09-15 04:23:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da7f499c-522d-3658-9cdf-32832790652a | -16.28059 | -54.92187 | 2025-09-15 04:23:00 | NOAA-21 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0e1517e-ab9d-39f1-9b5b-3f5b985b8973 | -21.10306 | -47.99241 | 2025-09-15 04:23:00 | NOAA-21 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17331a70-717f-3c5c-87b6-81e5c0367bdb | -17.56631 | -44.35554 | 2025-09-15 04:23:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c1cf44e-9083-3ae8-bb95-9442f8e0ab7b | -17.67982 | -50.47122 | 2025-09-15 04:23:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4c4a881-6735-3ec4-9619-a1319c2749ac | -21.76027 | -45.52921 | 2025-09-15 04:23:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f154a466-4378-30ff-be34-26355878082c | -18.03053 | -46.9737 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09635392-9865-3ea1-9352-9761f09d71df | -16.70358 | -54.96261 | 2025-09-15 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4ed9f9a-9729-36f3-b86c-59e44e959cbe | -21.76301 | -48.1225 | 2025-09-15 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 482be19c-2abb-3442-b101-ce742dbb691e | -20.32964 | -58.08728 | 2025-09-15 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 95a53758-a73a-3cc9-97b5-e09c7dbf3287 | -20.73539 | -56.74268 | 2025-09-15 04:23:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b04a7f4e-c683-3460-b3a6-3df242c00d4c | -18.89811 | -46.63218 | 2025-09-15 04:23:00 | NOAA-21 | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5627f03c-bf95-3a57-a0ce-3121ff457397 | -18.89672 | -50.15828 | 2025-09-15 04:23:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 88e2c7dd-4479-35f8-806e-2d2edec31501 | -17.82784 | -47.77281 | 2025-09-15 04:23:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4274fccc-a01a-379d-a843-8a2ea579abad | -19.04325 | -47.28475 | 2025-09-15 04:23:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09308087-3a23-3ab6-82df-c0574f8b8751 | -20.3243 | -58.086 | 2025-09-15 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c2fa34c4-29a5-3d2b-83ec-6f6fc65125e9 | -18.01951 | -46.957 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18dd18ae-27bc-358b-9e46-4b38c7bfc2be | -17.29746 | -46.11596 | 2025-09-15 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 501b81d6-939f-30e7-9d6f-9f7c2d5c234b | -18.47318 | -46.94628 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52f4fd5d-7c79-386f-a646-7e23f32059c8 | -15.79733 | -53.51222 | 2025-09-15 04:23:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d294724d-e6c4-3560-a672-2944768b4bb5 | -22.61733 | -47.66673 | 2025-09-15 04:23:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 72671ea0-c6da-3816-9050-1c774cca961d | -16.70819 | -54.96407 | 2025-09-15 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README37.md)
