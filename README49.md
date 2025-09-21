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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e1d40af-ef97-3d4a-8326-d50831627ad5 | -12.43652 | -45.11137 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 7f6c1b40-eebd-3b73-9a48-7f9134de07ef | -10.26259 | -46.06397 | 2025-09-21 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 684376c6-6102-3508-b749-1c9e7dfc2442 | -17.39997 | -45.53789 | 2025-09-21 12:00:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8c2b76fb-6391-3aab-bd96-6c40249fbb2e | -10.00123 | -46.23366 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 49f65f07-9746-3255-aa2c-3fa6f0b07525 | -18.28193 | -44.31885 | 2025-09-21 12:00:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0435d240-2310-36ef-8ade-6ecc3f7d041e | -12.43345 | -45.13187 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a5a5c3ec-d537-3d3f-aca4-a57e5c761a9e | -11.49192 | -40.05561 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO JOSÉ DO JACUÍPE | BAHIA | Brasil | 2929370 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 6a90a047-ce0c-35b1-9e93-b5f1222afd32 | -14.47067 | -46.50536 | 2025-09-21 12:00:00 | TERRA_M-T | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 3fed402c-f180-3e34-aad0-0c093dd38650 | -14.79573 | -42.84614 | 2025-09-21 12:00:00 | TERRA_M-T | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 4.7 |
| dc749f0a-9139-3a70-9278-fc2e1b582837 | -12.70397 | -46.8523 | 2025-09-21 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 101f43f9-56a4-35a9-9465-66d366dc9605 | -9.84102 | -46.14556 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 52ade044-ca1f-342d-8597-340c558eac64 | -10.03886 | -46.26564 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| c44b0e20-8339-34ea-af78-9ce2535204d9 | -11.62051 | -42.88405 | 2025-09-21 12:00:00 | TERRA_M-T | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 5ba0a969-3065-3ba3-8b91-4385853b35da | -13.03467 | -42.20575 | 2025-09-21 12:00:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 35.8 |
| 929b4b80-8948-334c-ba6d-42500f591d6c | -11.23155 | -46.16799 | 2025-09-21 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b58e11e4-b9d1-3ad0-a305-4cdf1dc47d05 | -14.63516 | -48.26953 | 2025-09-21 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 31b41b3d-7fd1-36b7-89fb-763838dbf2fd | -14.4688 | -46.51717 | 2025-09-21 12:00:00 | TERRA_M-T | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 63625b34-35dd-3c17-9252-9f7bd855400c | -12.44316 | -45.10818 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 178.6 |
| f7c381f3-abce-3618-b0e0-683f40587ccc | -12.11987 | -47.92008 | 2025-09-21 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8ce8b98b-c1b6-37d6-a959-649333dd82bb | -15.8857 | -47.28968 | 2025-09-21 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 9e613d35-97e1-3f64-9872-60b5bb4326b1 | -14.86043 | -45.49358 | 2025-09-21 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 05e95f2f-8642-316c-8e3b-77d96b47cb7d | -12.45252 | -45.1096 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 1a6f70d1-126a-3bf6-9054-e41087bb458d | -14.62198 | -48.27699 | 2025-09-21 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| da0ba605-68b4-3d92-bf5d-381ba56285e2 | -11.61922 | -42.89303 | 2025-09-21 12:00:00 | TERRA_M-T | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 4495bd66-29b7-3cec-86f0-68a1e07bfcf1 | -12.44469 | -45.09827 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dfbabb94-fed5-3170-b67f-43f8bcb66b65 | -10.87442 | -46.6176 | 2025-09-21 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 09b5c668-4032-3a24-9835-5c9ad331b298 | -12.88998 | -46.84246 | 2025-09-21 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0b7ea388-d254-350f-8d94-42d572c8b705 | -19.22684 | -43.75782 | 2025-09-21 12:00:00 | TERRA_M-T | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ec75c4f7-31e9-3ac3-b60c-bd3593935c77 | -15.69736 | -46.98639 | 2025-09-21 12:00:00 | TERRA_M-T | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b145f8f3-dd84-3df1-848e-6b2be6b3806a | -12.70589 | -46.84001 | 2025-09-21 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 828fb39d-4748-35e8-8c7d-4166d2238abd | -10.04086 | -46.25245 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d1bf36d7-a9ca-3550-85e8-97e1ca5d20f9 | -12.29139 | -45.27125 | 2025-09-21 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 1aef9768-dd58-3644-8a43-16fbb3a6e1dd | -16.60725 | -41.66069 | 2025-09-21 12:00:00 | TERRA_M-T | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| f477b496-d5e5-3dd1-a181-521aba6f6994 | -10.02849 | -46.26379 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| fba1560b-78c6-3cd8-924d-1440c97aebed | -15.87364 | -47.30003 | 2025-09-21 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 9bc1f7e5-b60e-3e78-bce7-04a080711ae3 | -14.44646 | -47.57155 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 9a24bbc0-fa20-3b47-b80d-ec167b820998 | -17.1164 | -45.93758 | 2025-09-21 12:00:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 583ed530-f591-3096-ba8f-d8c543427c1b | -16.40037 | -43.4911 | 2025-09-21 12:00:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cad513c3-369e-35c7-a360-cedc9ee9bcbb | -12.43499 | -45.12158 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| a9108109-9f50-3c67-9a6a-7597e78689bd | -15.87171 | -47.31225 | 2025-09-21 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 30a6fbb8-6b55-342d-89c2-ae67f58a2b11 | -13.25049 | -47.20903 | 2025-09-21 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 17b9978a-84ca-3eb3-8fc4-3866a495b528 | -23.38683 | -46.09899 | 2025-09-21 12:02:00 | TERRA_M-T | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f55b5c5b-d9ae-38db-adde-8d6f78e516f1 | -23.48542 | -45.4245 | 2025-09-21 12:02:00 | TERRA_M-T | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| b8f90071-1730-3fce-99b2-954f57c63696 | -21.88568 | -41.28748 | 2025-09-21 12:02:00 | TERRA_M-T | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 5c52773e-b7aa-3896-b5b3-602c302b5f1c | -22.63819 | -48.2511 | 2025-09-21 12:02:00 | TERRA_M-T | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e4735a3a-e549-363d-8201-fde20257c5eb | -23.33603 | -46.9804 | 2025-09-21 12:02:00 | TERRA_M-T | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| e13933f7-4d90-3bf7-b9c7-2e137974801a | -22.38641 | -49.03225 | 2025-09-21 12:02:00 | TERRA_M-T | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 11762abe-2bfd-3fb7-92d4-a7c44a0d60a5 | -21.96523 | -44.32311 | 2025-09-21 12:02:00 | TERRA_M-T | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| df73a3af-993b-3b4a-9dae-b20db2610466 | -21.27382 | -43.79532 | 2025-09-21 12:02:00 | TERRA_M-T | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 39fe1928-87ca-31a4-ba9b-61684ff96383 | -21.30441 | -44.6338 | 2025-09-21 12:02:00 | TERRA_M-T | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 866c49c0-2422-3141-b7e5-1a933aaf56f2 | -23.32849 | -46.96875 | 2025-09-21 12:02:00 | TERRA_M-T | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 79a4f67e-4d65-34aa-9cec-fe387df7401a | -21.28965 | -43.883 | 2025-09-21 12:02:00 | TERRA_M-T | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| d74d2531-463d-35b2-8f08-1cc57c3d046b | -23.33763 | -46.97011 | 2025-09-21 12:02:00 | TERRA_M-T | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.4 |
| c1a87260-abf9-3d81-9756-bf1929d11c34 | -23.16227 | -47.61949 | 2025-09-21 12:02:00 | TERRA_M-T | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.9 |
| 54d15187-689c-35b1-8316-3691c26fc189 | -23.21848 | -47.03085 | 2025-09-21 12:02:00 | TERRA_M-T | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 89a6a348-f400-3c56-9d8a-2e8c3aadf395 | -22.30056 | -48.49869 | 2025-09-21 12:02:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| a4987b19-13d4-341b-8fed-e2edded5bea7 | -23.14356 | -47.61609 | 2025-09-21 12:02:00 | TERRA_M-T | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| af3f0292-52db-3507-9391-c15d0acfa1d3 | -23.77573 | -47.36476 | 2025-09-21 12:02:00 | TERRA_M-T | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| d60dea7d-7a94-31d1-8eb5-433357475b60 | -23.16057 | -47.63013 | 2025-09-21 12:02:00 | TERRA_M-T | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 7b824a95-7116-3a59-bf85-1381b58559b1 | -20.62285 | -46.43906 | 2025-09-21 12:02:00 | TERRA_M-T | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 010ff0d2-bf6f-3ce9-a4f0-450f9c5d38d4 | -23.24814 | -50.8618 | 2025-09-21 12:02:00 | TERRA_M-T | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 08c5a6c9-74d4-3fb9-88e7-e7639fac482e | -23.22005 | -47.02065 | 2025-09-21 12:02:00 | TERRA_M-T | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 3a927f14-29b2-3f1e-913b-f0f5ad1d61d2 | -20.62132 | -46.44912 | 2025-09-21 12:02:00 | TERRA_M-T | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d20c1970-c1ac-38f2-aea3-09517a3b2fc4 | -23.39896 | -49.12476 | 2025-09-21 12:02:00 | TERRA_M-T | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 30ef8044-5326-3188-af68-f5539baf118b | -21.88727 | -41.27457 | 2025-09-21 12:02:00 | TERRA_M-T | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| f4ace350-42c0-3118-9bc2-18119e5f1401 | -23.39682 | -49.13755 | 2025-09-21 12:02:00 | TERRA_M-T | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 2f21161b-0f82-3636-9ee1-1e744db0c564 | -23.25044 | -45.83556 | 2025-09-21 12:02:00 | TERRA_M-T | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| a8d4b892-33bb-3b1f-a66d-f44b8028d8eb | -21.27516 | -43.78559 | 2025-09-21 12:02:00 | TERRA_M-T | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 48dd33aa-97a5-341d-8af6-04207389a395 | -23.38539 | -46.10868 | 2025-09-21 12:02:00 | TERRA_M-T | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9957d9b6-9207-3d18-b52c-4f3b93cb4bc6 | -23.33918 | -46.96008 | 2025-09-21 12:02:00 | TERRA_M-T | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 6a906f0a-6aa3-3aa3-8fba-28973f39aab1 | -23.15121 | -47.62844 | 2025-09-21 12:02:00 | TERRA_M-T | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.6 |
| 10e80163-b6a6-32b3-9ef6-6586aa4533cd | -23.1866 | -49.47751 | 2025-09-21 12:02:00 | TERRA_M-T | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| a480545b-fbfe-3f09-b770-59ad81f41104 | -23.48404 | -45.4341 | 2025-09-21 12:02:00 | TERRA_M-T | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| f486f101-a3ef-3deb-9f08-ac718430ad98 | -23.2401 | -50.85334 | 2025-09-21 12:02:00 | TERRA_M-T | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 38.8 |
| 20ae247f-8de0-3b24-ac7a-0bd5ff6eab9f | -23.15463 | -47.60704 | 2025-09-21 12:02:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.7 |
| d49ec811-0684-336e-87b1-47d897c3d028 | -23.15292 | -47.61777 | 2025-09-21 12:02:00 | TERRA_M-T | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 476.9 |
| a58f8d60-7c71-3816-9a25-676a9fdcd691 | -23.1523 | -47.6245 | 2025-09-21 12:10:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 234.1 |
| bcd37126-26bd-31ee-ab03-35124b2bcd79 | -12.7114 | -46.8454 | 2025-09-21 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 1e709084-fbe5-3a19-b0a1-b815d88fcde8 | -5.5771 | -42.1493 | 2025-09-21 12:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| b282a685-3a10-3583-9011-ddf7bc138d5c | -14.8479 | -45.4846 | 2025-09-21 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 82ad2d2f-9368-3e02-ab40-968e55890d8f | -12.6088 | -45.1244 | 2025-09-21 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 69fd09c4-49a0-3512-ba82-58a05dad3234 | -12.4361 | -45.1052 | 2025-09-21 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 304.0 |
| c4770c4a-6da8-38cf-bbcd-9020c1f68d58 | -12.4357 | -45.1284 | 2025-09-21 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 203.6 |
| b67ec32d-b973-3bac-b12d-7224673cbe08 | -7.714 | -44.4612 | 2025-09-21 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 61e5e5f0-499d-38e4-bcfa-66de9a09dfa8 | -10.0314 | -46.2786 | 2025-09-21 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 8754e5c4-83b6-38fe-9509-9a0797d53043 | -5.5771 | -42.1493 | 2025-09-21 12:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 409b98cb-2346-3cfa-97a9-b7b171b48dd1 | -7.5566 | -46.735 | 2025-09-21 12:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 4e025fe2-a811-3e59-81f8-fd994e15280c | -12.4357 | -45.1284 | 2025-09-21 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 590aedcb-c7c0-3bf6-97b6-71a03739ddc6 | -5.5583 | -42.1507 | 2025-09-21 12:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 56fdea62-b23d-3427-8cf6-2784d16e6bd5 | -17.1173 | -45.9491 | 2025-09-21 12:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 7a86e651-4304-3b5b-8539-4b07f2cf32dc | -14.8479 | -45.4846 | 2025-09-21 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 332.9 |
| c438c554-7d22-32c6-80f9-9cbd9c3742e3 | -12.4361 | -45.1052 | 2025-09-21 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 9c12122d-8396-3bdf-b1b4-88aae93475e4 | -15.8829 | -47.2973 | 2025-09-21 12:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| b6c78e18-a04a-3b48-a28d-8adc8734c471 | -11.4857 | -43.5692 | 2025-09-21 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| fab501f2-1c94-368a-8868-b3f7c48e02e1 | -12.7114 | -46.8454 | 2025-09-21 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 68087a94-7937-32ab-86f6-4737f6e87687 | -12.6088 | -45.1244 | 2025-09-21 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 73700670-f403-37c0-b535-7e1a2a02349b | -23.1523 | -47.6245 | 2025-09-21 12:20:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 184.4 |
| 41634cf3-234d-3b0a-bff0-525b793ff423 | -10.0317 | -46.2561 | 2025-09-21 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 09d547d5-f512-3d62-bfdd-8b0a2b721bb2 | -7.714 | -44.4612 | 2025-09-21 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c6006909-e0ff-336f-965e-5ae7cdffaa32 | -7.714 | -44.4612 | 2025-09-21 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |


[Clique aqui para ver as próximas entradas](README50.md)
