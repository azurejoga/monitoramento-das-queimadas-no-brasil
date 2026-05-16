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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1220b5d-e31b-364c-a7b8-2a66f57069fe | -8.0757 | -44.115299 | 2026-05-16 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fd5a2b23-b65a-3646-a288-86a2e4ff6997 | -8.079 | -44.128601 | 2026-05-16 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a71166bb-447b-3c2b-a4bc-0a775b013166 | -8.0822 | -44.141899 | 2026-05-16 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f62ad71d-5b32-3656-b204-bfe83ec435f4 | -14.1831 | -52.8667 | 2026-05-16 00:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 0bb3add8-d402-387e-b220-1c1cce87b33b | -14.1828 | -52.8878 | 2026-05-16 00:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e8aeca15-69c2-3ab9-89d9-3f106d6f3cb6 | -8.0761 | -44.1244 | 2026-05-16 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| d32b0d0c-9a54-3fe0-b8cd-e465d9fe3f03 | -14.1828 | -52.8878 | 2026-05-16 01:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 072cc4ee-8fbb-3363-bea4-b3224359fd3c | -8.0761 | -44.1244 | 2026-05-16 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 58dc7a74-41b6-376a-a207-2d07a0e9e315 | -9.5725 | -40.3227 | 2026-05-16 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.5 |
| cbdb3bf8-a0f1-3d99-a054-16a254ed28ac | -9.5721 | -40.3475 | 2026-05-16 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 115.5 |
| a050d541-8bce-3354-ac31-04ef126248c1 | -9.4769 | -40.3365 | 2026-05-16 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 474adc57-252d-3f91-8fc9-b45a025644eb | -9.4769 | -40.3365 | 2026-05-16 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 957380ae-1afb-3f15-a45d-b6f8a0abb99b | -9.4769 | -40.3365 | 2026-05-16 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.0 |
| e24b0014-4011-34be-bc74-da8b95932754 | -9.4769 | -40.3365 | 2026-05-16 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 58b4031f-0171-3f68-abcb-274240e19e7a | -9.47526 | -40.34139 | 2026-05-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 0bc47152-10af-37f7-8dd8-8bb74e073d0c | -9.48059 | -40.34235 | 2026-05-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.2 |
| fd26546d-b6cc-3679-b362-8de5d8af025c | -9.38948 | -37.81001 | 2026-05-16 03:23:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5073582d-2e4b-31fc-95bd-81fc5f957826 | -8.07638 | -44.13174 | 2026-05-16 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 996939e0-88cc-3f3e-a270-c886667769a0 | -9.47588 | -40.33801 | 2026-05-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 1ead0b4c-4e17-3de5-8be3-9c300fa5e940 | -9.56651 | -40.34413 | 2026-05-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| abb0f576-51a6-3798-b1ce-a9018c422822 | -8.08306 | -44.1349 | 2026-05-16 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38a445d3-04bf-3fb6-833d-4213b237a452 | -8.10473 | -43.1579 | 2026-05-16 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| d00f5d1c-93e1-3d0a-b49d-50dbee33b05a | -8.08327 | -44.13301 | 2026-05-16 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94b133b9-8f85-31ae-8cff-02cadcd29349 | -8.08204 | -44.13934 | 2026-05-16 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f301c8c7-8141-3103-9f2c-ec026f910141 | -8.08187 | -44.14124 | 2026-05-16 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8fc223ea-26ce-3684-b662-b2573462ed0e | -9.47997 | -40.34575 | 2026-05-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 00743b92-6e46-3937-962f-892dfe546c87 | -9.48122 | -40.33897 | 2026-05-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 45.7 |
| f95be008-6893-3ef3-8b1b-54f93e72c2da | -8.07762 | -44.12541 | 2026-05-16 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f695a16-0517-34a6-9526-b5dd44315431 | -8.07737 | -44.12727 | 2026-05-16 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cdbcc16f-5de1-3960-8205-40eb9676c43a | -11.75017 | -44.51831 | 2026-05-16 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 134634dc-7e5e-378b-b522-b0320e1c49d6 | -11.74231 | -44.52284 | 2026-05-16 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a3f58aee-be70-3001-bf57-369cf720f017 | -12.85513 | -43.76313 | 2026-05-16 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 759302b6-9cab-341f-86f9-155bdc26e83c | -15.91498 | -41.85714 | 2026-05-16 03:25:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e806a668-eb63-363b-a5ef-cc264350913b | -14.65532 | -41.00011 | 2026-05-16 03:25:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 73e2d7c3-9148-3eeb-a313-2ee93c4d815a | -12.85245 | -43.76494 | 2026-05-16 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fee3d6bc-1e6d-3d95-98c1-6746a017be93 | -12.10962 | -43.65007 | 2026-05-16 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 54c631ff-92d9-3e21-ac37-5a72aa82b322 | -15.91433 | -41.86036 | 2026-05-16 03:25:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d61f6fa-589e-38cc-b464-4a6fb6917c6f | -14.65589 | -40.99719 | 2026-05-16 03:25:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8469f469-6182-3575-b4cc-b0aa2310d88b | -12.85349 | -43.75994 | 2026-05-16 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 552b42db-a241-3b69-a137-064d7bd9c302 | -12.8489 | -43.76188 | 2026-05-16 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a8833aca-e409-3ba1-a933-7a269c1132bb | -12.15645 | -38.09417 | 2026-05-16 03:25:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1918f5c6-9d61-31d7-b98f-a75eaad6cb98 | -12.2603 | -38.24743 | 2026-05-16 03:25:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 96ae265f-b0aa-3bca-b65a-ec8856e8e3ea | -12.05359 | -45.29159 | 2026-05-16 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6de4d6a5-ed09-390c-ba60-f56d1b4350fb | -11.74629 | -44.51687 | 2026-05-16 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b6f7e41-6ce0-3d83-ab38-62b5419725e4 | -12.11334 | -43.65009 | 2026-05-16 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c77712a-e877-38c8-8059-e694f8fd311f | -12.84726 | -43.75871 | 2026-05-16 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f23a6209-9f5d-3c8f-9fa3-605b01c69ce6 | -11.7451 | -44.52278 | 2026-05-16 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43250fce-a5cb-3b67-a008-3e0f267f4a5a | -12.04668 | -45.29025 | 2026-05-16 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 55f7b5a2-10f2-32ae-8de5-fe131e44d21b | -11.7439 | -44.52873 | 2026-05-16 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2bf8db7-0db0-340d-8560-350cadd48271 | -17.57692 | -44.94751 | 2026-05-16 03:28:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb0d214f-3ff2-3263-b304-4dbe0c449525 | -17.5758 | -44.95246 | 2026-05-16 03:28:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9156c384-025e-3388-be5c-124a1ee822c8 | -17.34667 | -42.62081 | 2026-05-16 03:28:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f221ec3c-ca71-3bad-bdff-a84e8daa894a | -17.35202 | -42.62193 | 2026-05-16 03:28:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13d1d722-18a6-35c4-b7a1-704da89e991f | -17.57805 | -44.94549 | 2026-05-16 03:28:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b9547cf-1354-3d7a-91c8-154d9d86bb13 | -17.57697 | -44.95043 | 2026-05-16 03:28:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88119381-1653-3cec-b2f7-8ee518bbd895 | -21.93208 | -41.33686 | 2026-05-16 03:28:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 43e9b68e-4683-312a-b786-ce260c0f1d46 | -4.36463 | -37.8978 | 2026-05-16 03:55:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f3ec560a-0a2a-31b6-b251-ea63afd4fa63 | -11.79649 | -43.62095 | 2026-05-16 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1bbe708-96d9-320f-8956-ba8c693e0172 | -12.04708 | -45.29578 | 2026-05-16 03:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 083cda0e-804a-3aa0-9043-ee9c42e55481 | -12.05339 | -45.2871 | 2026-05-16 03:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e39e1b1-4c66-3869-a44f-2e4f4ae7087e | -8.10174 | -43.15427 | 2026-05-16 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c5288ca1-dbab-3221-89ae-31ef8a87c87e | -8.07584 | -44.12873 | 2026-05-16 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d33f0ae2-f888-32b0-9e56-164440d9fb89 | -9.23423 | -46.64997 | 2026-05-16 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e768d87-64bc-316b-b06d-14547aa506b3 | -12.02275 | -47.80308 | 2026-05-16 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de31efe6-13af-3ddb-a4ea-99c06d2a490f | -11.59415 | -48.03345 | 2026-05-16 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15a4806c-8a4f-3a5f-a025-944c65585d37 | -10.49964 | -42.40797 | 2026-05-16 03:57:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 04e1b788-da08-3639-80c5-14970ae04e05 | -8.10599 | -43.15502 | 2026-05-16 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 62c5e085-222e-3877-97ac-7d7407bfe15d | -11.04142 | -48.92466 | 2026-05-16 03:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c174d74c-9763-3afe-aa43-7349684a7fc3 | -12.05146 | -45.29399 | 2026-05-16 03:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4ea48fa-3490-3f4b-9c4d-96d4dbcaa167 | -8.26407 | -48.23481 | 2026-05-16 03:57:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e09ce956-62de-38f1-8c4a-6d0c67c82733 | -9.48133 | -40.33978 | 2026-05-16 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 6c2fb9e2-b914-32a4-88f7-623dae16f0b7 | -12.02474 | -47.80185 | 2026-05-16 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87595150-6a95-3188-8478-43adb2ab21de | -11.86983 | -43.86657 | 2026-05-16 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ce280788-3271-3bdc-8b2d-9b1880a11246 | -11.74009 | -44.52223 | 2026-05-16 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 61f14bbe-133b-34af-aa0d-500c113666d8 | -11.97665 | -47.36714 | 2026-05-16 03:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a288a2d-8ae3-38fd-b55a-a1340091c436 | -11.74447 | -44.52306 | 2026-05-16 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 736ffcda-2afb-3e12-869b-7ae5f6185340 | -10.49574 | -42.40728 | 2026-05-16 03:57:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 39ab4e6b-85ae-351d-83de-4f5f6e6b7093 | -10.66506 | -49.70964 | 2026-05-16 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b87a5c7d-732d-3568-9ecf-f96a4985c209 | -12.05236 | -45.28924 | 2026-05-16 03:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdb0764b-b3a8-3c59-89a7-7dec3dcda720 | -9.23362 | -46.65319 | 2026-05-16 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c367a4c-cc63-324b-bdc7-6d02ced01e9a | -11.59488 | -48.0297 | 2026-05-16 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29eedc7a-7f7b-341e-821a-e0aba6952d0b | -10.65883 | -49.70833 | 2026-05-16 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53a02fd9-01a6-38b4-a5de-c9367068ab81 | -11.5956 | -48.02601 | 2026-05-16 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ab136cf-25a3-3a35-b58c-078194dd7b88 | -8.0833 | -44.13947 | 2026-05-16 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39afca7d-65e8-39b0-bdec-2a8818650589 | -12.11168 | -43.64991 | 2026-05-16 03:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 501af6a9-c93c-39b2-8c02-dba8757f5aad | -10.66159 | -49.70975 | 2026-05-16 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 793d36e9-93ab-35b7-8106-1c1fe1fc05e1 | -10.97908 | -45.09531 | 2026-05-16 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25e89d97-8325-3e33-8f49-f739ff1a72db | -11.04423 | -48.92753 | 2026-05-16 03:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b75ad55d-742c-358d-a5e1-cb069266e82c | -12.02214 | -47.80628 | 2026-05-16 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66194531-b2e6-385e-b113-86b049f70bdd | -12.02408 | -47.80522 | 2026-05-16 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e0758bf-0deb-33e2-914e-8fc8bb6b8826 | -12.25802 | -38.24517 | 2026-05-16 03:57:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8dcc08af-7986-3173-b71e-24cced488c59 | -12.04795 | -45.29099 | 2026-05-16 03:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e732b4e7-09c7-3e6b-9ade-c5c8dddb09db | -11.82581 | -38.26168 | 2026-05-16 03:57:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 473ac04d-1776-341d-a383-e095327550dd | -8.08038 | -44.12953 | 2026-05-16 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e64a0c4-ca99-3c78-8de6-fc2fae69c4a6 | -11.74523 | -44.51877 | 2026-05-16 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44d90301-924b-3c69-a130-88ad378a2a28 | -9.7915 | -48.08112 | 2026-05-16 03:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9199766c-03c6-38f4-bb87-c5f566e51113 | -10.66604 | -49.70466 | 2026-05-16 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 454dd32d-13fe-31cf-b1f9-d0eb092de1d0 | -12.26135 | -38.24572 | 2026-05-16 03:57:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9eead777-ab05-37f1-9f42-fcff73c6b13a | -9.47779 | -40.33918 | 2026-05-16 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 325c6f5c-c332-3294-89d3-6585fbab2a8f | -9.47425 | -40.33859 | 2026-05-16 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README3.md)
