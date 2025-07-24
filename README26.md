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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81a09f77-b477-3335-95e4-54be0c6e74d6 | -3.58686 | -49.55108 | 2025-07-24 12:29:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2d356c96-8f69-32a1-8be2-b383e90cec2f | -4.04237 | -42.52257 | 2025-07-24 12:29:00 | TERRA_M-T | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| b05db6d0-f862-36ec-a0d6-98d4a2b158b4 | -3.16734 | -49.45119 | 2025-07-24 12:29:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 36b3b238-b81c-39c9-a1a1-d98a44098028 | -4.80608 | -43.2055 | 2025-07-24 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| a936289b-0414-3bc6-8a54-fa329508d7bb | -6.99297 | -42.78965 | 2025-07-24 12:29:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| b29788eb-715c-3881-8ba7-dcbcf82aab26 | -3.1863 | -49.45102 | 2025-07-24 12:29:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1a475bc8-5ca5-375e-8290-e3ac322a7e0d | -7.33596 | -45.29436 | 2025-07-24 12:29:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4421fa0e-9ddd-34fe-a60c-33ec9a2568d5 | -4.05461 | -42.52423 | 2025-07-24 12:29:00 | TERRA_M-T | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 8bd108ec-f812-38ab-bf50-84e2b4cc748d | -7.95798 | -46.28781 | 2025-07-24 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 46744ba9-51be-320a-ad74-2bc78df99a80 | -6.5737 | -49.51167 | 2025-07-24 12:29:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6228c73a-cd67-355c-9320-0acad34170bb | -7.63642 | -44.26637 | 2025-07-24 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e17c6845-45f4-35db-9eb9-ddc286ef8ede | -7.45871 | -49.40138 | 2025-07-24 12:29:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6bba9395-efbc-3827-9fa0-fa6eb92a5260 | -6.99545 | -42.77048 | 2025-07-24 12:29:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 131.6 |
| 7c9be791-0ed4-31a1-b63b-638fbbfc1979 | -7.95309 | -46.30367 | 2025-07-24 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 2567e5f8-7931-3f79-bd79-2e60ef350be6 | -7.25632 | -43.06998 | 2025-07-24 12:29:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.7 |
| cccc5eaa-732f-38a7-b8e8-986165c3efcc | -7.95651 | -46.29883 | 2025-07-24 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 59cfb936-9a07-3b55-bd74-968f7654ef3a | -3.9974 | -43.25326 | 2025-07-24 12:29:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6516aca5-9b01-385a-9433-c9ab024ab0db | -4.05711 | -42.50635 | 2025-07-24 12:29:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| cf98d72d-d98f-31ae-a440-9296c2634db8 | -7.95616 | -46.28168 | 2025-07-24 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 45f95c5c-e17c-3304-beda-8961d2b68e70 | -3.17597 | -49.45891 | 2025-07-24 12:29:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 4c24e32f-f214-36d6-aa8b-2e07fe7eb984 | -7.34633 | -45.2957 | 2025-07-24 12:29:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f45e51fb-0d1f-3fdd-b648-aff8b7ffe877 | -6.56842 | -45.59595 | 2025-07-24 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8d17a708-1a84-34fb-bb00-36a3cbdaa4cf | -5.81868 | -44.12725 | 2025-07-24 12:29:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a46dfebe-27c8-38bb-9cac-4c04568e1225 | -6.89491 | -44.14894 | 2025-07-24 12:29:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 768034bc-0c49-3bf6-ac75-00d938101b4b | -7.8928 | -45.54892 | 2025-07-24 12:29:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5044725e-2139-3a26-a98e-a68a665b08ba | -4.8394 | -45.30325 | 2025-07-24 12:29:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9a56dca8-f59f-382e-a84b-7aa9b8a5a094 | -6.58636 | -49.50139 | 2025-07-24 12:29:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 3f8b0711-4549-31be-afad-a58c964cb604 | -3.93023 | -43.15838 | 2025-07-24 12:29:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 6399382e-55f3-3ad0-9fc1-f0b49b649433 | -3.56657 | -49.50154 | 2025-07-24 12:29:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fe1e2288-d854-3e66-9804-3e3a335ffe96 | -7.94487 | -46.29137 | 2025-07-24 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 330481a2-b99f-39dc-b47b-3ba4e5e20a3c | -4.41395 | -48.87685 | 2025-07-24 12:29:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 309e5053-f857-3b4e-bf54-b4679cca16e9 | -4.04484 | -42.50474 | 2025-07-24 12:29:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| c0e11ba2-d742-3c78-bdc0-e8ad690d4430 | -7.95462 | -46.29267 | 2025-07-24 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| a6514e84-0bf3-3651-b59f-fbb8a035c4c5 | -4.06069 | -42.51252 | 2025-07-24 12:29:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 55.6 |
| 772eddf2-b092-344e-a323-01cb149e8126 | -2.99234 | -49.32114 | 2025-07-24 12:29:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2be75369-2ce1-36ca-8509-734a9c8819dc | -3.19893 | -43.46616 | 2025-07-24 12:29:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ecb109a0-694c-3d82-a5f2-a2859bf8064e | -7.63444 | -44.2813 | 2025-07-24 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 4ec8e234-4b5c-3afd-b97f-86e4ff6c5410 | -6.47088 | -44.57669 | 2025-07-24 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 76730b72-e235-39d3-900a-451d93105fdd | -6.98284 | -42.7689 | 2025-07-24 12:29:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| e9bf4d6b-c6a5-346a-98aa-5a8d1b0b29fe | -3.57554 | -49.50281 | 2025-07-24 12:29:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1aa3743c-10ca-3bfb-8c49-e5ffeb6555a3 | -4.04843 | -42.51091 | 2025-07-24 12:29:00 | TERRA_M-T | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 919fbf1b-2333-3ea9-b1e1-3a96a577fb78 | -4.0569 | -42.5118 | 2025-07-24 12:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| ccf2a3d0-6d76-3158-854a-f299e747dfe4 | -6.9992 | -42.7836 | 2025-07-24 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 147.4 |
| d12fc755-900c-397d-b7f9-ac2ececffb39 | -6.9804 | -42.7854 | 2025-07-24 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 250e7b21-0889-3b3b-aa77-9eceebd33cec | -11.27812 | -42.32877 | 2025-07-24 12:32:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 69f71f9d-9bcd-362f-9275-623618bfe2f4 | -14.10237 | -46.34636 | 2025-07-24 12:32:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4887a8e5-03e1-3366-b8c5-e2e5b5a4db18 | -8.82999 | -44.52253 | 2025-07-24 12:32:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 38.9 |
| b2a7c78a-e798-3b3f-aeb8-5c3e3e5cb072 | -7.90644 | -47.61589 | 2025-07-24 12:32:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 981ebd57-6588-3305-9e2d-72dec7c33244 | -14.74859 | -46.3062 | 2025-07-24 12:32:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 71dbc22d-9284-3a1d-a8d9-462e55269b6e | -14.74509 | -46.29979 | 2025-07-24 12:32:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 39d3d18c-069a-3833-9ca0-c1a298abe992 | -15.60088 | -44.54971 | 2025-07-24 12:32:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 6aeed795-661f-3e2b-8580-6257f5a25420 | -15.15013 | -46.19628 | 2025-07-24 12:32:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 03c69f87-3ba2-3fd8-9552-cde63ffaaaec | -12.719 | -46.97052 | 2025-07-24 12:32:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6b1ccdbc-9dce-3516-bb8b-c198cafcfd35 | -8.33001 | -44.93475 | 2025-07-24 12:32:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.5 |
| e23ed36d-8b45-302b-b181-429a6b9dd486 | -15.60319 | -44.53015 | 2025-07-24 12:32:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 294.2 |
| fae3bb6f-939c-3465-8387-89d8d2487492 | -9.23372 | -47.55218 | 2025-07-24 12:32:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 2a0fc299-aa73-3c1c-9ee9-0bf1ef5aa835 | -15.60678 | -44.51729 | 2025-07-24 12:32:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| fb3554b1-9335-3388-b507-9f593b44a91c | -9.34147 | -49.90985 | 2025-07-24 12:32:00 | TERRA_M-T | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c7bdb56b-baf6-3660-8b73-84032621b3a9 | -8.82874 | -44.53127 | 2025-07-24 12:32:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4b1f628d-b6d7-3fbe-90ec-c728e1782780 | -13.70213 | -45.67305 | 2025-07-24 12:32:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2cc12dbb-d31d-308e-9d6e-79d6236911bb | -14.37442 | -50.32647 | 2025-07-24 12:32:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8a3622b2-3ea0-3552-97ea-a2bbc8fb4798 | -9.4094 | -47.4784 | 2025-07-24 12:32:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4c9b958f-5d23-34d3-824e-65680b4ed4e3 | -14.33657 | -52.0975 | 2025-07-24 12:32:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a8552405-1c9e-36e0-b737-bac514e541c8 | -13.21214 | -51.0929 | 2025-07-24 12:32:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 18317dc9-3b50-3856-95b1-f0241715a580 | -15.60461 | -44.53687 | 2025-07-24 12:32:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 269.3 |
| 77494bfa-fefa-3a22-a9e3-2b8a327bbf10 | -7.91819 | -48.12396 | 2025-07-24 12:32:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3ef04ead-2a0c-3031-9917-add9af538b71 | -8.32697 | -44.92842 | 2025-07-24 12:32:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 77c3868a-8003-3f96-8231-f86ffe26ea2e | -15.62045 | -41.34015 | 2025-07-24 12:32:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 49.7 |
| 887a9d1d-883f-300c-819b-8851a2c3d039 | -14.61427 | -48.87376 | 2025-07-24 12:32:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 978760c0-00cb-37a3-80e3-625497b354ce | -12.71743 | -46.9823 | 2025-07-24 12:32:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| fbfdb59b-2c3c-3e71-9f07-d254890a818f | -8.32508 | -44.94226 | 2025-07-24 12:32:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| e9032746-5ef0-3fcf-ac20-fd8466c2a628 | -9.40804 | -47.48826 | 2025-07-24 12:32:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 198e1171-47ad-3abc-93e9-1742d7aa7687 | -8.33904 | -44.9499 | 2025-07-24 12:32:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| f7ed85bf-c97d-363b-a409-f2b1a2d1ef67 | -14.17786 | -45.34257 | 2025-07-24 12:32:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 39fe8c5d-f913-3c37-94e1-7b70d58722f5 | -13.17502 | -49.42517 | 2025-07-24 12:32:00 | TERRA_M-T | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 38472e0b-a4bc-3ffb-a0a3-3092c1937aab | -8.50323 | -47.23235 | 2025-07-24 12:32:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 16835374-afbb-30dd-9666-df1333b94027 | -10.62972 | -45.23233 | 2025-07-24 12:32:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d5cacbaa-f6b5-3281-9f36-24529325a0b5 | -15.59206 | -44.53547 | 2025-07-24 12:32:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 2d15514e-a813-37c3-b484-915405ea73a6 | -8.67512 | -46.93206 | 2025-07-24 12:32:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1a17cc0e-2974-37b7-a272-4f6bc4ec7d52 | -11.1378 | -48.63652 | 2025-07-24 12:32:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 0405b24f-cf41-3fe7-a067-4c65bb760030 | -9.23235 | -47.56195 | 2025-07-24 12:32:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d011ef51-6a24-33ca-9141-6a738b7ec2c3 | -11.92646 | -50.2925 | 2025-07-24 12:32:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 134c7a4e-da22-314c-85ba-fd79d7dd61fa | -14.06039 | -44.48057 | 2025-07-24 12:32:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a5605a46-4261-3e55-9419-3c1f3313b388 | -13.54965 | -45.61683 | 2025-07-24 12:32:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| aacfa456-ad24-3d1f-8d7b-e0ee3b238231 | -10.95313 | -45.94787 | 2025-07-24 12:32:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 61405b36-bb4f-3a0a-bfa8-765406329fe6 | -8.83073 | -44.51636 | 2025-07-24 12:32:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 39.0 |
| b8d0af6a-7f8e-3e7f-9f27-b7913f6bcaae | -14.61558 | -48.8641 | 2025-07-24 12:32:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fcb3b2e4-2e0f-3aa8-8ed8-eab1e000e9b0 | -8.86419 | -45.47331 | 2025-07-24 12:32:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 40b00404-e0a4-3b4e-977c-eb2c7129d02a | -8.19992 | -47.22253 | 2025-07-24 12:32:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4cf14c2d-560f-3979-859e-2909eb448c8b | -15.34099 | -49.42001 | 2025-07-24 12:32:00 | TERRA_M-T | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 568708c9-7238-3275-b7dc-f2618101ddcc | -14.17592 | -45.35857 | 2025-07-24 12:32:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 79df66c0-ecbd-3dbc-8cd9-b1585aad0b59 | -9.3503 | -49.91112 | 2025-07-24 12:32:00 | TERRA_M-T | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 08cd7178-c34b-3ad8-88c8-4a86153694c9 | -14.09797 | -46.33953 | 2025-07-24 12:32:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e8df7758-684f-38f5-bcec-780945b71421 | -12.70603 | -46.99203 | 2025-07-24 12:32:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0ca924a5-110a-38ec-9597-7513807de5c7 | -12.7063 | -44.94137 | 2025-07-24 12:32:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f5c2a1fe-2c82-3c4b-9921-3f27466cda39 | -13.54936 | -45.61086 | 2025-07-24 12:32:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4ff2a1f5-8bab-334c-ac7c-5eccbc02f8e0 | -7.87547 | -49.7724 | 2025-07-24 12:32:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8780911a-7deb-3ab8-94ca-f6fed81bf3bb | -8.24362 | -47.51599 | 2025-07-24 12:32:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f49dbaed-db65-3e0f-a3ad-44112fe94f6c | -11.28306 | -42.33588 | 2025-07-24 12:32:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| a95ca646-5ffb-3c1f-94fc-4a8a37173f75 | -8.32822 | -44.9486 | 2025-07-24 12:32:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |


[Clique aqui para ver as próximas entradas](README27.md)
