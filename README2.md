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
| 93a22eef-b75c-3fa0-adc3-c9ab9739d64b | -6.65168 | -41.99661 | 2025-05-18 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| b9404de5-0479-3533-864a-995268ca960d | -6.64545 | -41.99933 | 2025-05-18 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a073f993-3cde-351c-a8ad-b965ebafe307 | -6.65025 | -41.99606 | 2025-05-18 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 9c6a76d6-d81f-3e79-a4c1-808f0a54ed4d | -8.07383 | -34.97776 | 2025-05-18 03:30:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a6c70d46-51d2-3091-a447-fff816751925 | -7.0752 | -44.38555 | 2025-05-18 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04d3ae34-fb50-3f48-90b0-6288ac8a070a | -7.23483 | -44.71718 | 2025-05-18 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2a39c95-aee9-3291-ac8f-e99b0338a916 | -10.34835 | -46.72047 | 2025-05-18 03:30:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 187c50b7-6b8d-3d68-a717-0d50a7e91493 | -7.07726 | -44.91766 | 2025-05-18 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6c15062d-34c1-3ad8-aadc-23808ca7a129 | -6.64957 | -41.9998 | 2025-05-18 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 33fdac49-4948-3f58-96dc-8654aff4dfd3 | -6.64611 | -41.99557 | 2025-05-18 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 21543fe9-bf3f-3031-bad7-a90d39ce57f3 | -7.23335 | -44.71881 | 2025-05-18 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57e6c779-a399-3b70-a715-2a8f51b50626 | -6.64467 | -41.99504 | 2025-05-18 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 41b57545-7734-3a40-a667-8186966a0649 | -7.08119 | -44.91912 | 2025-05-18 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7738e26b-2b4d-3b20-ba18-ac361ff88eff | -6.64399 | -41.99879 | 2025-05-18 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3c8667d8-c2da-3e43-b49a-b8e3ea3c014e | -6.64676 | -41.99183 | 2025-05-18 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 373550dd-0142-373f-ac29-74e0e693cfde | -6.65092 | -41.99233 | 2025-05-18 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 0a9a0e40-fc51-375a-bc66-eb0a77483a4e | -10.34972 | -46.71391 | 2025-05-18 03:30:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff4874e8-42f0-3134-815b-7dfb2200ec68 | -6.65233 | -41.99289 | 2025-05-18 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7ea2d483-17d0-3ab6-8768-3e010700a9c2 | -9.08738 | -40.53452 | 2025-05-18 03:30:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b2694374-b78b-3db0-af49-fc4127bcb055 | -10.34422 | -46.71256 | 2025-05-18 03:30:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 80bd9949-602c-342b-a189-53ccd1326727 | -7.07388 | -44.38843 | 2025-05-18 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 772a70d7-e1ec-3f61-98cb-a2e5da97ead6 | -10.34983 | -46.72071 | 2025-05-18 03:30:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 044c774f-dd43-3c40-8b0c-71a17639bef9 | -17.39102 | -46.64447 | 2025-05-18 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5a5f4fb-c1fa-3431-90a3-6fe6e6cd0c24 | -17.14843 | -44.81104 | 2025-05-18 03:32:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 519d9042-c2de-3a75-add8-d314a9576f1e | -17.14786 | -44.80851 | 2025-05-18 03:32:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2674a33-2c27-3cad-b666-0575a16b0a97 | -11.48324 | -43.80886 | 2025-05-18 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bba19753-2d0d-33e0-a8eb-7c6fee30d103 | -11.48411 | -43.80454 | 2025-05-18 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc17c920-e8ae-39bb-b4b1-aec4f59998f0 | -17.14925 | -44.80709 | 2025-05-18 03:32:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53ac7e84-00da-38cf-884d-66949ef904b6 | -17.7796 | -42.8098 | 2025-05-18 03:32:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad0f15c3-62b1-3f93-b076-10d02243418c | -17.14209 | -44.81374 | 2025-05-18 03:32:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf938bdd-4dfb-3bf6-ab7a-0cd6104e5c47 | -17.14702 | -44.81244 | 2025-05-18 03:32:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c517b0a4-716a-3d64-b55e-bfad30024bad | -12.09962 | -44.75601 | 2025-05-18 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6813394e-1ca4-37cc-9a16-f0a6ada992bf | -13.29558 | -45.37761 | 2025-05-18 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc7310d5-7906-33e3-8fbe-1072e5379a2c | -17.77907 | -42.80556 | 2025-05-18 03:32:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d959282f-b53a-3fb6-9905-1412a8881329 | -16.02946 | -43.67921 | 2025-05-18 03:32:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1811b027-5806-3801-a296-0208a469885d | -17.14762 | -44.81496 | 2025-05-18 03:32:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1871433a-e019-3364-a2f3-af56f5ca9592 | -17.39201 | -46.64494 | 2025-05-18 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d1bb21f-c525-37d5-8543-5485f9a50048 | -12.10664 | -44.75235 | 2025-05-18 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80164a20-df24-3cf6-bf33-78dd11de1e9c | -13.29663 | -45.37252 | 2025-05-18 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08df4c96-5927-3f30-8bcb-bbefba427e91 | -12.10057 | -44.75128 | 2025-05-18 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df14706b-6e25-380d-a237-0e5848ece6ee | -17.14149 | -44.81123 | 2025-05-18 03:32:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a42c115-78f5-38ac-8b7d-3ae25679ac81 | -12.10569 | -44.75706 | 2025-05-18 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62667235-a34e-3892-83e0-7604e8ce0617 | -13.56367 | -43.51123 | 2025-05-18 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34e453d7-8796-31a1-ab7a-413de9b8546a | -19.68017 | -43.92595 | 2025-05-18 03:34:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c00827a-ad9e-313d-9aeb-22bc31f92d8d | -22.78756 | -43.75827 | 2025-05-18 03:34:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0eeb7396-782b-376c-bdb6-3e5cf0e666b8 | -22.9025 | -43.75506 | 2025-05-18 03:34:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0254e581-e358-323c-aaa0-9155e5146bc9 | -22.78211 | -43.04499 | 2025-05-18 03:34:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ed2b3aaf-827e-3fa6-a642-fef480f880ca | -23.09905 | -45.7332 | 2025-05-18 03:34:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f0843709-0bb8-3101-a811-094d530dbd33 | -22.77291 | -47.63062 | 2025-05-18 03:34:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 1c71c47b-d8ff-3e57-a593-ef532a388903 | -22.67503 | -42.85693 | 2025-05-18 03:34:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7684a2b3-22d3-3b28-948a-fbc9fd2e960c | -21.17829 | -43.98268 | 2025-05-18 03:34:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0f03b2c9-2387-3d11-8c3e-4e2a9a748ea5 | -22.67916 | -42.85551 | 2025-05-18 03:34:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9374b6a5-057f-3475-b569-c678650e916c | -22.77397 | -47.62615 | 2025-05-18 03:34:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 11c155e3-9502-36b8-a189-3ddada899aac | -7.07767 | -44.92082 | 2025-05-18 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b44c0479-1516-32f7-9a68-07da9efa283c | -6.64486 | -41.99449 | 2025-05-18 03:55:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e4d4dc19-03ad-3319-9726-1dc2f9151ebb | -7.2089 | -43.09849 | 2025-05-18 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| daeb52d4-da24-340d-acf6-71e2642056af | -6.64929 | -41.99076 | 2025-05-18 03:55:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9b8ad063-ded8-3553-a392-26d96c911faa | -7.07422 | -44.38441 | 2025-05-18 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29d227a5-a758-35a3-99d3-8fad9518e856 | -5.07113 | -37.71598 | 2025-05-18 03:55:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c37dd5e3-2b2b-3e9c-a186-c29581061cad | -8.43123 | -49.10402 | 2025-05-18 03:55:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8ce406b-c768-37f0-aa62-6a1b15d18444 | -7.07398 | -44.91581 | 2025-05-18 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24a45dbb-7cd2-3475-bd0d-b3604eb16916 | -8.11701 | -46.45003 | 2025-05-18 03:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f80f01a4-b773-3029-80f8-077cb909c9f0 | -6.64856 | -41.99511 | 2025-05-18 03:55:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6093a118-fbda-35f1-92b5-724efe7910bd | -8.43698 | -49.1049 | 2025-05-18 03:55:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8563e973-46bc-3e00-859d-7558780d37b6 | -9.31731 | -44.83236 | 2025-05-18 03:55:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa95f25f-f234-3fa3-b21d-f85ba416a6f1 | -7.23421 | -44.71545 | 2025-05-18 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7ef113a-ad89-3e67-a471-978a495faac5 | -8.11794 | -46.44474 | 2025-05-18 03:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 308a3407-3b76-3fc8-8534-03df6eeed818 | -6.65226 | -41.99574 | 2025-05-18 03:55:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 78e873df-f97a-3356-9717-42f15f1d9181 | -7.08207 | -44.92169 | 2025-05-18 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 427cebfd-7d9d-3bc9-baa5-becaf98054ec | -7.07848 | -44.3852 | 2025-05-18 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81eaa780-6278-3a9d-a99a-13a145529093 | -8.00868 | -46.80602 | 2025-05-18 03:55:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2b2f033-b6fe-3e74-9479-8c5a137fe4a5 | -6.64783 | -41.99948 | 2025-05-18 03:55:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c43611ba-f251-3a98-bf32-349b3d17b338 | -7.04595 | -43.48653 | 2025-05-18 03:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59b11c82-c25e-3ae7-aecc-f09f7f05d8f6 | -7.0784 | -44.91652 | 2025-05-18 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d24f3da0-d3e7-3a6a-8fb9-b736fdeefd68 | -9.32154 | -44.83311 | 2025-05-18 03:55:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b0b6eb6-296a-3331-aac4-de679d4e16e1 | -6.65298 | -41.99139 | 2025-05-18 03:55:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 98ee1a80-801c-32b0-832c-0480f7c3b341 | -7.95373 | -49.75671 | 2025-05-18 03:55:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88ab0932-44f9-3ed8-9e05-8d45a3f3a1d7 | -6.64413 | -41.99886 | 2025-05-18 03:55:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bb28fbed-2f1d-34de-b8f6-4b480382c7f2 | -7.20972 | -43.09353 | 2025-05-18 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 817beb57-89c2-37ef-ab21-322df8d31959 | -7.24777 | -43.29823 | 2025-05-18 03:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4eeee7bc-a4fc-37cb-ae46-f3a4f1caa788 | -7.20912 | -43.09555 | 2025-05-18 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4bea5ac4-e519-3eac-8163-506156a7976c | -17.39028 | -46.64344 | 2025-05-18 03:57:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ee170dc-7a46-3c08-9a91-ff800ce4513c | -11.58355 | -47.61659 | 2025-05-18 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 632e6b8e-4b41-3571-9847-c382789bfb25 | -13.30674 | -45.39881 | 2025-05-18 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18ff67aa-6234-3d17-ba33-b12d2a70f761 | -11.79294 | -49.3214 | 2025-05-18 03:57:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3d76924-dd30-382d-b26a-26eb7687f765 | -12.3014 | -52.47337 | 2025-05-18 03:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fdab945-ff1d-3a9b-ac40-78b992dc8263 | -13.04446 | -53.71995 | 2025-05-18 03:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df3986de-4d84-3467-9b88-78c0ff920b65 | -10.34963 | -46.71486 | 2025-05-18 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e8049ae-0eec-3e9d-9be4-106169cc70e6 | -10.34019 | -46.71315 | 2025-05-18 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ef37306-1809-398c-b13b-19a822f61f7a | -17.1477 | -44.80769 | 2025-05-18 03:57:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ceb326f-f284-3b7e-b215-e7bc7ae5be81 | -12.0998 | -44.75171 | 2025-05-18 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b606a10-6e4c-3750-b4e8-cbb464943f65 | -12.29485 | -52.47197 | 2025-05-18 03:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01ca2796-3462-397d-b589-bcb9950ae341 | -13.04152 | -53.72399 | 2025-05-18 03:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3ca990b-9083-3d0b-9a7c-d933cf57ac3a | -17.77829 | -42.80899 | 2025-05-18 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffc22215-0174-3eae-a437-e754c14eac3f | -13.03758 | -53.71819 | 2025-05-18 03:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0e50b7d-6635-329b-a1ca-62f35d733103 | -16.0327 | -43.67952 | 2025-05-18 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d8299f5-839e-364e-969b-920025db3380 | -11.48179 | -43.80481 | 2025-05-18 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00ae0302-2b7e-37c7-84a4-ad9fe4188cb7 | -17.80795 | -41.49852 | 2025-05-18 03:57:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8ab26a61-e8b3-3668-b4c3-6e760a8be781 | -15.28687 | -53.19999 | 2025-05-18 03:57:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 495ef73a-90d6-3db3-8b73-53eef332f5b0 | -17.14687 | -44.8124 | 2025-05-18 03:57:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README3.md)
