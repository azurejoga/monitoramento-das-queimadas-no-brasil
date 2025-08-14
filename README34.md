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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 819963a9-7740-35b8-9535-b3bc080e3041 | -18.54455 | -46.06266 | 2025-08-14 05:14:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf44ec4d-ef8f-3b8a-b0a6-a8fa5024099e | -19.28993 | -57.58778 | 2025-08-14 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| a0c5b989-4b10-35bc-975f-417010f4c545 | -18.53432 | -46.05534 | 2025-08-14 05:14:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3c136c8e-b3e5-3989-be9f-dbd8521f7046 | -18.2473 | -47.25979 | 2025-08-14 05:14:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d8b2798-c630-360f-a953-8a1d8176c61b | -22.77863 | -50.20021 | 2025-08-14 05:14:00 | NOAA-20 | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a22e2b7b-69a9-32a2-978e-cefb0d2aca9a | -22.61944 | -47.38897 | 2025-08-14 05:14:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e5630fc1-3e7f-31dd-80ea-5a9ebebf0372 | -22.67585 | -47.46646 | 2025-08-14 05:14:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 373dbf19-7684-3bb1-bc78-f7a9bcd434a4 | -20.62061 | -55.48655 | 2025-08-14 05:14:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7be8fe90-db2d-3a97-aaf1-5c42c57fdaf7 | -22.66996 | -47.45294 | 2025-08-14 05:14:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5bf7eae1-bb27-30fd-b166-897d0c7e73b6 | -17.87169 | -52.19754 | 2025-08-14 05:14:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 331f1b81-af45-390a-a933-4f16ceff2ad5 | -18.53801 | -46.05488 | 2025-08-14 05:14:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 370ed0c5-0db2-376e-b9aa-92231adee70b | -21.00944 | -48.92495 | 2025-08-14 05:14:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 93afadb2-2e49-3a3f-84ec-c0bcbe4a999e | -18.54514 | -46.05541 | 2025-08-14 05:14:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0b957b9-1c25-353c-bde6-6be3f9a79e04 | -22.77942 | -50.19817 | 2025-08-14 05:14:00 | NOAA-20 | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2ac75abc-e149-3694-9459-eb3f8428ef92 | -22.6258 | -47.39664 | 2025-08-14 05:14:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9900222f-f7de-3b51-a25d-e27f0d1c5365 | -22.55262 | -49.77071 | 2025-08-14 05:14:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0fefce9-19ac-3762-bc3c-592a87ca1226 | -18.5309 | -46.05421 | 2025-08-14 05:14:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c38fd9ad-54ad-3baa-a107-1e5d57b43df9 | -22.67115 | -47.45432 | 2025-08-14 05:14:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 75d88813-4f75-3699-8ef9-bd8d496c936e | -23.57342 | -47.24247 | 2025-08-14 05:14:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 14392e74-7f53-3d51-93c2-c4a5cf553e74 | -22.67757 | -47.46114 | 2025-08-14 05:14:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5e9f527e-0732-3e08-822a-eb5c7296a21d | -22.85827 | -49.22369 | 2025-08-14 05:14:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 656626ae-bee7-3acd-9d00-0f6ca7e025bd | -6.8771 | -59.147 | 2025-08-14 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8e09631d-bbc5-3ccd-8e2a-dfe95e39065e | -6.914 | -59.1455 | 2025-08-14 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| b6e6dcb0-14db-3a2f-bd88-8a9a15c74860 | -6.8956 | -59.1462 | 2025-08-14 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| bd85d576-d8bd-3de1-b49d-c620147737ee | -6.8955 | -59.1655 | 2025-08-14 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d44a85c4-6c1b-3a65-aeff-6bc95499854a | -6.877 | -59.1663 | 2025-08-14 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 602afcc8-235e-343c-94ee-68cc68789fd1 | -6.94278 | -44.54633 | 2025-08-14 05:23:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| c101c1b4-5c77-355c-b956-5fb8bd26f16f | -4.13891 | -38.26858 | 2025-08-14 05:23:00 | AQUA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| d505766b-b4f4-3441-93a7-e210b8a4d477 | -6.94049 | -44.56062 | 2025-08-14 05:23:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 0617c975-0622-3f91-9ab5-f16a09af98bb | -3.81749 | -41.56028 | 2025-08-14 05:23:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 95a2cbec-bb23-3deb-a307-5c0c4a20ab83 | -6.61071 | -43.87505 | 2025-08-14 05:23:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b85046c9-31f5-3d2e-8b7c-e201c6c24ca0 | -6.95401 | -44.54768 | 2025-08-14 05:23:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6c20d7fc-d12d-36ae-a03c-b02094d5ffc4 | -5.98063 | -44.14682 | 2025-08-14 05:23:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e41e9c21-ccde-35be-a7c1-9e07c707f127 | -5.78796 | -43.60971 | 2025-08-14 05:23:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cc89795c-6e90-3b12-87b3-f83a6d0ad86b | -10.53346 | -42.54889 | 2025-08-14 05:25:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9121481c-4b38-3311-ab99-5a8401c393ec | -8.52322 | -43.32985 | 2025-08-14 05:25:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d7921b16-3d07-38dc-b551-abcff5549c5d | -9.26565 | -40.2575 | 2025-08-14 05:25:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| b0642557-c1b5-3f23-bac0-66dd4292edcb | -8.51693 | -43.30549 | 2025-08-14 05:25:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| bd39389c-e326-3c6e-abca-f0cd36ed0515 | -8.74069 | -44.01816 | 2025-08-14 05:25:00 | AQUA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9ef88c2e-1054-3b7b-bd17-5226d8c03c1d | -8.51873 | -43.29413 | 2025-08-14 05:25:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.3 |
| 6eb9e525-3a0b-34b8-95f8-8e8794b511f3 | -8.52503 | -43.31844 | 2025-08-14 05:25:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| b626783d-a4e8-358d-bf50-3171349ccdbd | -11.80272 | -44.27356 | 2025-08-14 05:27:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8f603e80-0044-3a0e-8a2a-1d7a7fa51f3d | -11.80464 | -44.26168 | 2025-08-14 05:27:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 9adc2ddd-a6cf-3c9c-b8c9-e263026484b5 | -21.01435 | -48.91284 | 2025-08-14 05:29:00 | AQUA_M-M | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.3 |
| 9d2ecb96-4c66-3b26-9506-33c5b62d9811 | -23.68254 | -51.63618 | 2025-08-14 05:29:00 | AQUA_M-M | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 41.3 |
| b0aac625-c63f-35b5-8e5a-66b655dae4bd | -23.67068 | -51.65494 | 2025-08-14 05:29:00 | AQUA_M-M | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 30.6 |
| 217f47ac-3abb-3e06-aee4-878ad00db4f9 | -22.66869 | -47.44715 | 2025-08-14 05:29:00 | AQUA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 312e31ae-23bf-36de-988a-3d51950b2e6a | -21.01106 | -48.93073 | 2025-08-14 05:29:00 | AQUA_M-M | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| 892ed1c2-57d3-3eed-92f1-2b77fd95ba8e | -6.914 | -59.1455 | 2025-08-14 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 05d4203b-674f-3706-ae41-957925a9d4d9 | -6.8955 | -59.1655 | 2025-08-14 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| ddf9c403-dd90-3719-b125-1d5b6595b507 | -6.8771 | -59.147 | 2025-08-14 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a06c69f1-77a6-3b7c-9751-2a64060afbdc | -6.8956 | -59.1462 | 2025-08-14 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |
| b68e8bce-cacf-34ae-9324-b6df4f54ea3e | -6.9139 | -59.1648 | 2025-08-14 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 8cf6e72b-f581-3fdb-8446-a51d3b002af9 | -6.877 | -59.1663 | 2025-08-14 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| ce3aa9c9-70f7-38e6-b5c2-c62f9044f467 | -21.0234 | -48.8986 | 2025-08-14 05:40:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.5 |
| 5dae3f99-59e9-35e4-8fb2-2383b3ede202 | -6.914 | -59.1455 | 2025-08-14 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 22685fb5-dd15-38ef-8b27-888123d78dfd | -6.8955 | -59.1655 | 2025-08-14 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| e3b1b97e-a251-37e3-860b-df3f59dca4db | -6.8771 | -59.147 | 2025-08-14 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d8f3ca4c-f682-39a4-8a33-e74d44416869 | -6.8956 | -59.1462 | 2025-08-14 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 26192a95-88c4-35c3-adce-e6c9c907210a | -6.8771 | -59.147 | 2025-08-14 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| ac50bb4d-13d8-3faa-b3ca-dd0cf240911a | -6.914 | -59.1455 | 2025-08-14 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5463a9c6-b190-37b0-9a5e-bdaa2a1d40f7 | -6.8955 | -59.1655 | 2025-08-14 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 15959201-fb63-3d2c-b0cb-9b89316f79a9 | -6.8956 | -59.1462 | 2025-08-14 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| a273e150-8014-3e7f-a62d-7946c2031aa0 | -6.8771 | -59.147 | 2025-08-14 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| f79c1333-9f10-3553-b96b-747b14f48dca | -6.8956 | -59.1462 | 2025-08-14 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 3dd16ae2-30c5-31d8-b25b-571bb924652c | -6.8955 | -59.1655 | 2025-08-14 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| ef69efcb-4e56-3de0-a0b2-05234a25e5fd | -6.914 | -59.1455 | 2025-08-14 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 6e6fe699-fa46-312e-84d5-504f010c52b5 | -6.87583 | -59.15804 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 96273a29-737a-33e5-98da-d397a6b75850 | -6.90144 | -59.1521 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 79755614-3010-338a-b4e8-00d5fa61ed5e | -9.05795 | -60.64812 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bad3882b-e5ad-388b-beb1-2670969daa1f | -6.87654 | -59.14624 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fbfe6617-96fb-337f-bc86-828994d1a276 | -6.07474 | -59.94259 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d7f5fed-e6c5-34ca-9477-4723437638b5 | -10.47882 | -67.76465 | 2025-08-14 06:01:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 906b7e37-336a-3b2b-9b05-bea2b294f3d5 | -6.90936 | -59.13897 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 14a15c27-a588-3306-82be-fcaffa3683df | -7.0948 | -60.02477 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66ef3575-296a-387e-9dc6-454bdb4a738f | -7.87709 | -61.80679 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3b2ac43-89b2-33f4-905c-3491b26b69aa | -10.02529 | -67.64349 | 2025-08-14 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8fcaf57e-b617-32ea-9b6b-81c68894f7d7 | -7.13467 | -59.6451 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb3ed111-0249-33c2-b3fc-ca014bfbc9b1 | -6.92702 | -59.14658 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ffcd28df-f039-3e40-b13e-45afa5c75ded | -6.9077 | -59.14568 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b5f4cc97-fc23-3ac6-99d3-bde15b99c9c2 | -6.91364 | -59.1538 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b524b428-ee3f-339f-9489-1f79afd34711 | -5.76187 | -59.88963 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6ba5a1c-4f8d-3fc5-a6a9-5ea11867181e | -7.88489 | -61.82735 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d1646f1-a60e-330e-8382-67552cd35b84 | -6.91484 | -59.14464 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 314009c1-4e12-37ce-ad0f-dca7462bcb81 | -7.14003 | -59.65012 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16a7184b-0cff-3760-b700-a1d8fa88f8ba | -6.89129 | -59.12919 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 890c52da-87f2-3b35-9a9a-1431c441e5e0 | -6.9096 | -59.13184 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| abf3ffea-7869-3a24-acbd-a13177479375 | -7.88228 | -61.80758 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48d2b1d4-79f4-359b-acb2-2d41213ce66c | -8.1083 | -61.20961 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 037c8f26-fd08-34b1-a14c-4bfb6d9d5931 | -9.16004 | -59.67522 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5adeac0-6798-3718-aedc-688dffe53715 | -6.90386 | -59.13343 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f979cb31-202e-351d-b7d9-a763f6cdb114 | -6.88456 | -59.1329 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a16164d-e218-3c8b-af19-dcb859069f97 | -6.85973 | -59.96737 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7690a383-4cab-39ec-846c-c9f7731ac20c | -5.76078 | -59.89756 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7691c12f-c826-3d61-b003-ae46aaebee3a | -9.05746 | -60.65204 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6abb7642-cf96-3c04-bde0-7bc9c44c6124 | -6.65122 | -58.81829 | 2025-08-14 06:01:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a169663d-e2a2-3308-8350-c8317993fc7d | -9.37547 | -67.77095 | 2025-08-14 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4630d996-10dc-3055-b9bf-02b8711eb989 | -8.1062 | -61.18432 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13c5cf01-d1c9-3080-a0b5-904b4fbe394f | -6.10043 | -59.92587 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ac0040c-82cf-37de-a797-92a4b9e7b28e | -9.37607 | -67.76678 | 2025-08-14 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README35.md)
