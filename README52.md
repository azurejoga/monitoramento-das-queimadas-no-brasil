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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5df7b8f-99e4-3537-b73c-ae46a6ab6d80 | -19.08002 | -44.40346 | 2025-09-04 04:29:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e777c501-b53b-37b5-aea1-08baf3ad0a17 | -15.17343 | -52.35435 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 31f7c980-b7fe-3e3c-846e-6468330e8244 | -17.172 | -46.2488 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf2d900d-f26a-3805-b1ed-eceea719244a | -15.53631 | -48.3397 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 941ebf14-2c7f-3825-bfd4-64c3f3598cd2 | -19.51238 | -46.14462 | 2025-09-04 04:29:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e0fc745-af02-3825-9913-c3e7b97f3d8e | -15.30338 | -52.75297 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a63f7f6-5e9b-3407-a12e-e8f149cd184c | -15.17073 | -52.35656 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7736df9e-3b4d-3eaf-8638-c65a44e34d2d | -17.17551 | -46.24935 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcb9a4f1-95be-399f-a408-593ddba8f78f | -15.19618 | -52.34284 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67aee2a6-71dc-3a12-8a7f-cca38e1d58be | -15.17718 | -52.35489 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 50cdaf23-e8e2-3e43-944b-c5d670c1e496 | -15.74492 | -53.63607 | 2025-09-04 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 90c9fb4b-3bdf-3b05-8d2d-2e113c3bacb0 | -15.54671 | -48.40353 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1bbc08b2-7bbd-33b8-ad30-723ecafa6baf | -16.55069 | -55.10554 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b21c1e45-59e0-3307-94e2-ba125d5112bb | -17.61154 | -46.64241 | 2025-09-04 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25dfa4a8-2f1e-39ad-9d10-ea71f5b5d87b | -16.55494 | -55.10661 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3aff63d4-e227-3f49-98ed-c4b6a1a7570b | -19.72249 | -49.09894 | 2025-09-04 04:29:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d20fede0-5080-3df4-912e-abd25fa47bd8 | -16.6599 | -44.08506 | 2025-09-04 04:29:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb0ca676-297f-34e1-9a95-321e0608a7e3 | -14.583 | -53.019 | 2025-09-04 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f0159ed-cb22-3fce-9b67-62e172fe3dc0 | -15.98334 | -55.9607 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c7ed0110-3efc-33f3-b55b-ba22db6c44e5 | -15.24585 | -53.7947 | 2025-09-04 04:29:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4660bb8b-8332-3739-8a29-d33f58b6876d | -16.077 | -43.62018 | 2025-09-04 04:29:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9cdde8e-76a8-3b67-a151-34caace32f3e | -15.98522 | -55.95091 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1a00b170-9bf4-348f-bbd9-170a0e12c8c8 | -14.57786 | -54.57362 | 2025-09-04 04:29:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30eaab5c-7084-37d2-ab31-ebffe94dcfa3 | -16.30669 | -45.70427 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc6568e5-291e-390d-9770-767e2b894199 | -20.37163 | -43.62771 | 2025-09-04 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 706feda1-5aa8-352d-b5a9-29f678456209 | -18.14012 | -51.79245 | 2025-09-04 04:29:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 60bddb85-fafd-376f-b583-d510b53712b1 | -17.05414 | -46.43852 | 2025-09-04 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b49cc007-5b24-33c7-82bc-c89c0ac5e6dd | -15.55279 | -48.38628 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 344700a4-2de4-3960-a54d-c4336f5c66a9 | -15.30582 | -52.73894 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6a5d06d-6cd8-36da-b579-62740600b029 | -16.07897 | -43.62112 | 2025-09-04 04:29:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ef0166b-d15c-39fe-842f-d85f538573f3 | -17.14392 | -46.24441 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bb62df6-4777-3c0f-ab40-0aabbfeee805 | -16.30432 | -45.69532 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9df21a6b-28a3-3af8-ae13-97e8abbac269 | -17.17493 | -46.25343 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d03d7a66-fdd0-30bc-93d4-f48a96acfbd4 | -19.71903 | -49.14338 | 2025-09-04 04:29:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 59a1d2fa-15f8-3148-92ca-1479c8dead53 | -15.41376 | -55.9383 | 2025-09-04 04:29:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18cfbc67-9f38-3dcf-b370-3a970056a260 | -18.07036 | -45.97135 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4eba0cdc-58fa-3858-a566-2154da6cd678 | -17.17842 | -46.22892 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7795379b-965c-3645-917d-fed4f50cc00a | -15.54129 | -48.30765 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4719bdc2-c82b-3e85-a425-d74d9427b612 | -15.30379 | -52.77325 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb6b6d20-1831-3561-896e-2f650f03409d | -20.10067 | -50.00887 | 2025-09-04 04:29:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 6354b969-9ffe-359a-a968-92f33639b12d | -19.22061 | -44.4856 | 2025-09-04 04:29:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a55d56dc-79d9-3823-882d-809402f16059 | -15.57226 | -49.5514 | 2025-09-04 04:29:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75744a8b-e9bd-32e7-8e9c-74805030343b | -15.19751 | -56.36424 | 2025-09-04 04:29:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce721f06-7241-3997-9560-559b7516fc4c | -17.1644 | -46.25178 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f491f372-23b5-3067-8d7c-3697df4acc01 | -15.98428 | -55.95581 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2ee353c1-6942-3fd0-8468-6fa6d0d4b353 | -16.30849 | -45.6917 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| efd316d6-607f-3a5f-b63e-88eb73874712 | -17.15734 | -46.22563 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c269c4a-090c-3a45-b909-014df0b27952 | -17.17142 | -46.25288 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 176f8986-0de8-31b1-895b-965e888c4a50 | -15.59536 | -52.88657 | 2025-09-04 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61cd050c-53e4-378d-9300-557a7ba6e5ab | -14.57243 | -54.55507 | 2025-09-04 04:29:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e302d0fa-3b87-36b4-8cab-ebf85068688a | -15.15611 | -52.36584 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 745bcfba-a71f-326d-9582-0a1804f56b19 | -17.15036 | -46.24958 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66d11274-4b51-3a8c-869c-5c6efc441e69 | -6.7503 | -58.7462 | 2025-09-04 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 63c42a9e-fa86-32ab-88f7-df1bca12efae | -4.9951 | -56.256 | 2025-09-04 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| e6ace605-ffed-3d79-822b-bec43178db6e | -6.7649 | -63.1292 | 2025-09-04 04:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 68272633-bb11-3858-be7c-79b75708b199 | -6.7319 | -58.7276 | 2025-09-04 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| d47f993a-80ba-38df-aaa4-7fb0495ee8d7 | -6.7504 | -58.7268 | 2025-09-04 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 613c574a-c782-3550-938a-bb275e6cde0a | -23.23795 | -49.41698 | 2025-09-04 04:32:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1c272a9e-3c20-3dde-9bd1-b91a256f5c4f | -22.76364 | -50.35878 | 2025-09-04 04:32:00 | NOAA-21 | CÂNDIDO MOTA | SÃO PAULO | Brasil | 3510005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9403c959-6739-3a12-a8ad-2655ef9d0b22 | -22.27952 | -52.04037 | 2025-09-04 04:32:00 | NOAA-21 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9f58f189-48ff-3653-b68c-3b4d9eebb550 | -23.17817 | -49.85622 | 2025-09-04 04:32:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6383be27-d1cd-38c0-a6e3-382a04acf6bb | -22.65683 | -43.68832 | 2025-09-04 04:32:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| b3f14175-4d58-3403-99c6-fa47910bcdd6 | -22.33747 | -49.88556 | 2025-09-04 04:32:00 | NOAA-21 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7ce9c642-d307-3062-9475-37126d7f7b42 | -22.26794 | -49.56396 | 2025-09-04 04:32:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9a3dd689-5b5e-3b6b-a433-e5b78d490c8b | -22.67389 | -47.4642 | 2025-09-04 04:32:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aa45897c-e230-3c14-a530-72f41c5d344e | -22.26188 | -49.55907 | 2025-09-04 04:32:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7d281f7f-a28f-3a0d-8710-b55ebff8dee2 | -22.62203 | -54.98265 | 2025-09-04 04:32:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 67994742-c021-36cc-9f96-4077d236f6fd | -22.61532 | -54.97576 | 2025-09-04 04:32:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ecbb8afe-e20c-3534-87d0-a8e5d6410301 | -21.94899 | -50.51886 | 2025-09-04 04:32:00 | NOAA-21 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b919048f-cda8-3bb7-95b6-16ecf264bba1 | -22.46308 | -47.55009 | 2025-09-04 04:32:00 | NOAA-21 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 43a0bda5-cb5d-37ca-8306-22f5258abd37 | -22.65252 | -43.68735 | 2025-09-04 04:32:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| ba811392-70f2-3f87-9d49-91b2800bb9ed | -23.31412 | -48.80918 | 2025-09-04 04:32:00 | NOAA-21 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d1b8a2e-beb2-3fd8-afb9-ec19de1ed4dd | -22.65303 | -43.68277 | 2025-09-04 04:32:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d866553d-fc42-3b61-97e1-fc88940f3f3d | -22.58302 | -50.79058 | 2025-09-04 04:32:00 | NOAA-21 | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94fe3e90-0428-319a-af6d-085b3139a4a0 | -22.38553 | -48.38222 | 2025-09-04 04:32:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0efdd438-7a23-3880-8204-8dc246dd9bb6 | -22.66115 | -43.68918 | 2025-09-04 04:32:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 1f69f378-30f9-379c-917b-89b17183c22d | -23.29803 | -46.16285 | 2025-09-04 04:32:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f626f8c9-bba7-3b6a-a47c-5861c9afaca4 | -22.74697 | -43.63568 | 2025-09-04 04:32:00 | NOAA-21 | QUEIMADOS | RIO DE JANEIRO | Brasil | 3304144 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c75666e1-9774-3603-a0ff-ca13ff1956c7 | -23.51468 | -47.16766 | 2025-09-04 04:32:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c3aade3a-1b29-340e-9ddf-30f83aaa3bf5 | -22.67742 | -47.46473 | 2025-09-04 04:32:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c39c3b65-4a53-3237-83fa-40be07e2e0dd | -22.46357 | -47.55274 | 2025-09-04 04:32:00 | NOAA-21 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 325d7c50-3dfb-33d6-812e-9b6bfa7a1996 | -22.89147 | -45.31639 | 2025-09-04 04:32:00 | NOAA-21 | ROSEIRA | SÃO PAULO | Brasil | 3544301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| fadf81ee-555e-33b8-9016-04d531b176ca | -22.27481 | -47.6355 | 2025-09-04 04:32:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9397b5d-ce39-3011-a5fc-9519d6315223 | -22.34067 | -49.88628 | 2025-09-04 04:32:00 | NOAA-21 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 29ef8ace-90ed-3e77-94f8-09b1a41b0177 | -23.47239 | -47.24939 | 2025-09-04 04:32:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 78c2f07e-1876-3502-ab23-b7fb5f6be643 | -23.36062 | -47.16921 | 2025-09-04 04:32:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 872c61fb-614f-3bfa-a779-b80f3ffb350b | -22.27828 | -47.63611 | 2025-09-04 04:32:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d553e26-3f8f-31cb-adb1-5df37277d0ca | -22.81823 | -45.16603 | 2025-09-04 04:32:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1ec081ec-ecec-3326-aceb-fe949a9000ef | -22.53544 | -52.02406 | 2025-09-04 04:32:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8cde3fd1-cdb1-35c0-bc67-627a0d9e8303 | -21.45857 | -54.55584 | 2025-09-04 04:32:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 407d2284-9bbb-3fa1-86a2-4b5b925ff13c | -23.88851 | -50.7773 | 2025-09-04 04:32:00 | NOAA-21 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 947c111b-0fef-3f5e-800d-ce229af39a89 | -22.54539 | -43.56693 | 2025-09-04 04:32:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 047367b1-bbea-3b77-b840-a68abdb1e2f3 | -22.53479 | -52.02798 | 2025-09-04 04:32:00 | NOAA-21 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 706aed29-e33d-3ec7-b569-2ee104a1d9ad | -22.28235 | -47.63251 | 2025-09-04 04:32:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c413d2e-8f8e-3a8b-b383-be90bb8de3a6 | -22.61819 | -54.98178 | 2025-09-04 04:32:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cdef4d7c-69e0-3904-83f6-dc46d1a01070 | -22.22768 | -55.97607 | 2025-09-04 04:32:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1d7140e-4436-3309-821c-6055fbb26d1d | -22.91506 | -42.41923 | 2025-09-04 04:32:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 7b1e72b3-5956-305d-8951-6158905aa517 | -23.42522 | -47.0546 | 2025-09-04 04:32:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 63e865ac-7701-31e1-8838-0920a59242ee | -22.26737 | -49.56768 | 2025-09-04 04:32:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2d6c3901-51ef-3619-ad3e-19a773505339 | -22.98763 | -47.0929 | 2025-09-04 04:32:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README53.md)
