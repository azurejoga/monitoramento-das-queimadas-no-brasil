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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d87b55c-2f1b-3404-9429-230cae809490 | -5.97644 | -45.36722 | 2024-10-28 03:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7dd72289-c2d3-3eeb-a9b4-9ae4857abb2d | -5.9757 | -45.37129 | 2024-10-28 03:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 45594d68-cd41-388b-8a27-8eacb72f0cb2 | -5.58259 | -46.34336 | 2024-10-28 03:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bae3de8-8e8d-39d0-bd30-f7b7371de20a | -5.57643 | -46.34206 | 2024-10-28 03:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a641cba5-89e5-38c8-a8b3-6bb28ccf41c7 | -5.44781 | -45.8927 | 2024-10-28 03:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d25ac01-76e0-3fb6-a461-2c75c137d1a8 | -5.44666 | -45.89564 | 2024-10-28 03:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca000bc6-6fde-3c2b-8f69-c952b7bff181 | -5.4418 | -45.89151 | 2024-10-28 03:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a917b8f-e9b6-3c17-ad9a-ac11e6ab29bd | -5.44142 | -45.88995 | 2024-10-28 03:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ff44cb1-2ca1-3860-96f4-598cbd4bdbd6 | -7.51461 | -46.63505 | 2024-10-28 03:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74e539b5-cb24-3ad8-8f02-84375ea3ba16 | -7.46833 | -46.71423 | 2024-10-28 03:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6bd297f-c49b-370f-8a68-b099e6679e30 | -8.99879 | -46.75665 | 2024-10-28 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df1d87b4-9b83-3917-866e-ddf34c28a2e5 | -8.99794 | -46.76101 | 2024-10-28 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 187d8eff-d299-3e80-a14e-ac26650f1235 | -8.99771 | -46.75386 | 2024-10-28 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f366821-34fa-3118-b1b4-ac80eee522c8 | -8.99689 | -46.75823 | 2024-10-28 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9855974-c693-3539-9973-c6fb138af28d | -8.99089 | -46.75704 | 2024-10-28 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eda989cb-30ef-3803-95ca-a0ac3b479d82 | -9.74261 | -46.27697 | 2024-10-28 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16da06d2-2041-3c6b-8430-063088a78725 | -9.73608 | -46.27987 | 2024-10-28 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7901a46-9db5-3cb5-912f-7878e0ba56a2 | -9.6753 | -46.25308 | 2024-10-28 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac00fb3f-98b5-3cdf-a05a-441e3ac7a055 | -9.67455 | -46.25699 | 2024-10-28 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d1424aff-8498-381d-ba27-4327904bdfcf | -9.2669 | -47.91384 | 2024-10-28 03:42:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf305474-16a3-34db-aba2-0c46bf5cb148 | -9.26052 | -47.91241 | 2024-10-28 03:42:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2780fd16-fc59-3780-ab8d-eada38da547c | -10.0534 | -48.06446 | 2024-10-28 03:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39a3e743-ded8-3dae-aaa6-f3caae86ee37 | -10.05214 | -48.06525 | 2024-10-28 03:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8ebc28c-050f-3eb0-b385-4af1d6ab3ab7 | -4.89293 | -48.64859 | 2024-10-28 03:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86642264-ed0f-3f0f-b39b-d1f37b6d36cf | -4.89166 | -48.65561 | 2024-10-28 03:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db8ba6d6-3597-36e1-bc5d-9fc0e425bb59 | -8.13906 | -49.48149 | 2024-10-28 03:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8cf16997-3e0e-3966-a82a-1c58bc19f250 | -15.36755 | -40.18538 | 2024-10-28 03:45:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 388fa20c-ab2e-3eba-b401-c231df83a980 | -15.36685 | -40.18954 | 2024-10-28 03:45:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 832868f7-adca-3606-a528-5811c42956bc | -15.36614 | -40.1937 | 2024-10-28 03:45:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0490d9b4-130e-36cc-b60a-31ebe0560182 | -15.36468 | -40.18055 | 2024-10-28 03:45:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 26a225f4-2360-3505-95f2-ad2959326715 | -15.36397 | -40.1847 | 2024-10-28 03:45:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 74b84f39-b6ce-32ef-8334-d37d4bf761d0 | -15.36327 | -40.18885 | 2024-10-28 03:45:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 74a4c05f-4732-30e2-a7e7-1fcdbe3783ed | -15.36256 | -40.19302 | 2024-10-28 03:45:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8f378772-d080-3507-a779-468042a481be | -15.3611 | -40.1799 | 2024-10-28 03:45:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 30b5440d-f5b3-3f75-89df-95d43ef8749b | -15.36039 | -40.18404 | 2024-10-28 03:45:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7f7015d5-3896-37e4-9d8e-642e3542fdb7 | -15.35895 | -40.17085 | 2024-10-28 03:45:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b1cd8e3a-0caa-3e72-9fe3-954191461468 | -15.35823 | -40.17504 | 2024-10-28 03:45:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8a6230cb-0b06-3461-8d39-3186b27a86e4 | -15.35752 | -40.17924 | 2024-10-28 03:45:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 212320f9-f217-3560-84cc-60b62dabe758 | -16.62743 | -40.40662 | 2024-10-28 03:45:00 | NPP-375D | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 137cd8f4-6295-34fa-81b7-34db29c633a0 | -16.63101 | -40.40718 | 2024-10-28 03:45:00 | NPP-375D | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d4de6f0c-250c-3f2e-8b2e-87e4384f0f3e | -16.63031 | -40.41127 | 2024-10-28 03:45:00 | NPP-375D | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 62ba88c0-6fde-3298-a0a0-303ffeb4dbe2 | -16.62673 | -40.41071 | 2024-10-28 03:45:00 | NPP-375D | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 40e7f005-662b-338c-aa00-b960befc8f84 | -14.18459 | -42.04909 | 2024-10-28 03:45:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| acdce141-8eff-30af-b2ef-11692475db51 | -14.12172 | -41.67643 | 2024-10-28 03:45:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f843b0f-2df9-3071-86b6-3e5767c34641 | -15.50844 | -42.27182 | 2024-10-28 03:45:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fc262b1-717f-3445-b1c9-ac28aa52797a | -15.61247 | -41.85206 | 2024-10-28 03:45:00 | NPP-375D | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d1b4f434-9460-3e74-b17c-e08c99166a98 | -15.3217 | -41.74713 | 2024-10-28 03:45:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a848717b-3ab5-37fe-86d4-96c9ace8acef | -15.31781 | -41.74636 | 2024-10-28 03:45:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cf5598d9-e163-3e1d-ba81-e931972077ed | -15.28031 | -42.09717 | 2024-10-28 03:45:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 62238043-177d-321d-9940-1275172ff319 | -13.70173 | -42.88486 | 2024-10-28 03:45:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cf6075b9-382d-3932-a29b-b0f36499eee9 | -13.57769 | -43.06998 | 2024-10-28 03:45:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 74bc9699-56d9-32e9-8367-f1e31da98e56 | -13.57334 | -43.0691 | 2024-10-28 03:45:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45ce76e8-c555-30c5-809c-29cd076f55d6 | -14.33052 | -42.30416 | 2024-10-28 03:45:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7541862c-88e3-3995-ba60-daf5c4bf797a | -14.5513 | -42.97739 | 2024-10-28 03:45:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c65014a0-3327-301b-9181-a2160d016d84 | -13.89623 | -43.44822 | 2024-10-28 03:45:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38dc4435-f720-3044-973c-99af366328e3 | -13.89179 | -43.44736 | 2024-10-28 03:45:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60a5043c-4ebb-3b0e-a3fe-f4f5a0030662 | -15.24311 | -43.65797 | 2024-10-28 03:45:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 55f26358-fdf9-3d32-815b-ade339a0fb4f | -13.54878 | -44.33292 | 2024-10-28 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 725c9680-fb10-34f8-8926-6c463d8a34f0 | -13.08248 | -44.63398 | 2024-10-28 03:45:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e4d151b-ad64-319f-84e6-03a8db1ea6f1 | -12.97532 | -43.46505 | 2024-10-28 03:45:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 522fb89c-0491-335c-a179-4da8ac527488 | -12.90108 | -44.61009 | 2024-10-28 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8a8a961a-70d7-3493-8255-627a8ef9c43e | -12.89728 | -44.6035 | 2024-10-28 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 61be633e-ea0e-350a-a80f-c9f9431ea899 | -12.8962 | -44.60914 | 2024-10-28 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 96334996-57f4-3844-930b-699c44e33af0 | -12.89512 | -44.61481 | 2024-10-28 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85c83298-f302-337f-b734-c8db235fb072 | -12.89132 | -44.60821 | 2024-10-28 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9de10bc9-2451-3caf-9ccb-dfc3626ad57f | -12.89023 | -44.61386 | 2024-10-28 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad764962-3848-3acf-876a-d9e5d196c0bd | -12.88643 | -44.60728 | 2024-10-28 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94106257-cd0c-3e12-97e8-f358dd43741e | -12.88535 | -44.61292 | 2024-10-28 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd4f6603-69fd-336d-8acb-a336b05e5d94 | -12.88371 | -44.61103 | 2024-10-28 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e47c619e-bc14-39bd-8c83-5685a0cd951f | -12.6857 | -43.89619 | 2024-10-28 03:45:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55b6b4ec-0f6e-3ba5-bb58-6ede796d1bff | -14.06785 | -43.99025 | 2024-10-28 03:45:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 429165b4-c174-3368-89da-d2b8864fc174 | -14.19829 | -43.72236 | 2024-10-28 03:45:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e09cb52-dc1c-36dc-b1df-61f0a9572b82 | -11.95634 | -45.4861 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b4f8730-4853-3b74-a3d1-bb5733f34850 | -11.95455 | -45.48701 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c64a9437-4eb7-3153-a363-b62a852d0ca5 | -11.9511 | -45.48494 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d37b6c6-80df-3307-ad23-4821c89b3ee7 | -11.95049 | -45.48818 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0843b653-40a2-3c34-8c26-b1f53e533374 | -11.94933 | -45.48582 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1da7f2af-a1e1-3897-87e9-67130a8a509b | -11.94694 | -45.52618 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c6cfa44-fa39-394c-a823-00548ee9fee5 | -11.94375 | -45.52424 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3999172-aedb-331a-a149-91b1fe850f91 | -11.94313 | -45.52757 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfd6f8c9-b344-3b17-82f4-75d2582ec879 | -11.94167 | -45.52514 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90a8e3a2-75d9-341d-92ce-dee20ce04a4f | -11.94102 | -45.52845 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c280971-8d4c-3cd5-82dd-bbde5305629c | -11.9391 | -45.51986 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09650c66-5beb-3f56-96b7-8ea7ff2dd824 | -11.93848 | -45.52318 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59ba7d22-206e-3803-9320-83e2d8909f9c | -11.93785 | -45.5265 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 83e5e8fb-4384-3dd1-802c-875815ab4372 | -11.93769 | -45.51747 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70efe8d1-1f8a-33a8-8a4e-988fb820dd90 | -11.93723 | -45.52983 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b134ea23-cf86-3486-b00c-1ed0cfa39262 | -11.93704 | -45.52077 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3cf8984f-f04a-3769-a6b9-c3c65541bca0 | -11.93639 | -45.52409 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7429e4b9-5561-374a-9a17-16cef6b2c59a | -11.93575 | -45.5274 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e52e41ca-538f-3b11-a29e-26bf3350d9ff | -11.93383 | -45.51881 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04081488-86ba-302a-bcbd-986870e40d72 | -11.9332 | -45.52213 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25a14910-ec82-38b4-910e-9e7bf12cd28d | -11.92793 | -45.52106 | 2024-10-28 03:45:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36653024-85f6-36ac-85d0-3565ac19ad83 | -15.15826 | -46.12076 | 2024-10-28 03:45:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| feec8fc3-0b45-3df3-aa60-943a814a0b6e | -15.15242 | -46.1231 | 2024-10-28 03:45:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2dd12d4-f9aa-31de-bbf4-f7cd7ead614f | -16.12895 | -45.92261 | 2024-10-28 03:45:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0d0d461-115e-383b-9b61-4d9d41d8e9f8 | -16.12393 | -45.92161 | 2024-10-28 03:45:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 062157c8-c4c4-3f67-b363-299bc4b57def | -12.67127 | -46.5831 | 2024-10-28 03:45:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ca52a5c-1485-348f-8e99-e3268570833e | -12.66645 | -46.57814 | 2024-10-28 03:45:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53983fe3-ced4-387d-9e1a-ddb2e299f1ac | -12.6657 | -46.58196 | 2024-10-28 03:45:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
