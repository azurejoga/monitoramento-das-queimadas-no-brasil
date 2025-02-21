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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 078cfc71-572c-36b0-9eb0-5ec602005ef5 | -11.97428 | -45.15631 | 2025-02-21 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94ee4644-8c2c-3abc-8afc-2aebc38875d4 | -18.69771 | -40.01187 | 2025-02-21 04:10:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1954699a-08c6-31f6-825c-01dec21cc9a0 | -17.46056 | -47.00966 | 2025-02-21 04:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e2d192d8-f2c5-3331-9043-4e49b63a9137 | -11.85809 | -46.93735 | 2025-02-21 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aab2e83f-816e-304a-a21e-53ae75c34da9 | -12.32301 | -46.66546 | 2025-02-21 04:10:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f192b5cb-26e7-3ffb-8b30-22d3331adc0d | -14.42853 | -45.63549 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c38c4e30-17ba-336b-81a2-531cfae723c8 | -17.46265 | -47.01863 | 2025-02-21 04:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba8cf198-690b-3cc1-b769-4f6b045eece9 | -14.42917 | -45.63161 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd73a6bc-9a67-326d-af6e-74ae65856710 | -14.10942 | -45.66601 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1311d845-7f79-3204-8011-eb1cc26f481c | -17.05357 | -45.04474 | 2025-02-21 04:10:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dacdc120-d6df-304f-b37f-fc6d17f9331d | -14.43135 | -45.63999 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8b5a059-0947-375b-b83c-88970c1d650b | -17.05417 | -45.04108 | 2025-02-21 04:10:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf8ecb09-da87-366e-a448-5783d16716b0 | -12.35562 | -47.98839 | 2025-02-21 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 114553f0-a969-3802-8519-98b4ba74ebd1 | -12.80161 | -45.0081 | 2025-02-21 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78f71264-ba60-3273-9761-c68177513b58 | -14.4549 | -45.65934 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b7ff35b-dcc1-3be7-822f-b3bd595c5614 | -14.43762 | -45.6451 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89606e3e-ddbe-3394-a42d-c9748638b22a | -11.03126 | -45.05878 | 2025-02-21 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b84cc85e-4983-3f01-b52a-349951902491 | -12.75592 | -48.34214 | 2025-02-21 04:10:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2c42ebb-4b9b-3e0a-81cd-77d6f60c5e56 | -14.42636 | -45.62712 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4023566-f3b7-39d3-a709-1a6eb66d1126 | -16.34922 | -43.69611 | 2025-02-21 04:10:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0a26ca4-7095-35ed-8525-2ba9abb7da44 | -11.86188 | -46.93801 | 2025-02-21 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f281aa3-3850-3ada-bced-3dad5989c404 | -14.43545 | -45.63671 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f119769-f2fa-33b1-ae71-7d30dcf351ca | -14.4568 | -47.90987 | 2025-02-21 04:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de567f93-6110-3ab4-ad30-a02c8ab4be04 | -15.74317 | -49.54841 | 2025-02-21 04:10:00 | NPP-375D | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12d6435d-4ead-3208-bb70-aebf7b3c1c11 | -10.54291 | -45.21889 | 2025-02-21 04:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a6376c7e-5cdb-3e04-b918-8e48689f8066 | -20.30026 | -46.49629 | 2025-02-21 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4dfb1e4-5576-3f6f-972c-e1a95e49dacd | -20.45543 | -43.27425 | 2025-02-21 04:12:00 | NPP-375D | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5be2a2d8-157d-3cdc-8b14-0a81e83832b1 | -19.85071 | -43.84435 | 2025-02-21 04:12:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b7eff004-7e91-3459-8e84-83f88214ffad | -19.20733 | -46.10769 | 2025-02-21 04:12:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f03fbfb-8440-3aba-a49a-dd3fd039d3d1 | -19.77694 | -47.9282 | 2025-02-21 04:12:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c997cb7-2c68-301c-b8fb-b7f822836f13 | -23.33901 | -46.77406 | 2025-02-21 04:12:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 47137217-86ee-3733-9858-26a285172c5d | -19.08528 | -46.50182 | 2025-02-21 04:12:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 919ae496-d040-34f8-bfc2-a1645e5586ac | -21.26161 | -49.00949 | 2025-02-21 04:12:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8e3c7fce-eca8-3a25-9d84-dc18a16f7239 | -22.73516 | -47.02065 | 2025-02-21 04:12:00 | NPP-375D | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6ce53f1e-332c-3dcb-9517-607cd3f02ef5 | -18.63844 | -43.17188 | 2025-02-21 04:12:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3ff6323c-be76-3fee-b952-627c69ed8f7e | -19.71782 | -40.35534 | 2025-02-21 04:12:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 30b8cecb-981b-3831-a058-8dc4a6da04c2 | -20.29687 | -46.49566 | 2025-02-21 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de4272b8-6676-3721-a6a7-dcb10605821f | -20.33556 | -45.4346 | 2025-02-21 04:12:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f6275636-8d90-310b-901b-69d1ec23a3ce | -19.4531 | -45.3065 | 2025-02-21 04:12:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f96fb771-d63f-3696-b5c1-689853bda31f | -20.16714 | -47.28005 | 2025-02-21 04:12:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4ac811c-31d7-34e6-93e1-3b2ef5ea657d | -20.16644 | -47.2841 | 2025-02-21 04:12:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d30c46cb-3d1a-345c-94ea-4970eae5da99 | -20.30091 | -46.49243 | 2025-02-21 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4a93867-b50b-3ef2-8f7a-51b7a55c01fe | -19.57844 | -49.40363 | 2025-02-21 04:12:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e1ff015-9efb-302b-bebc-3fbbc69bb180 | -21.98689 | -44.52099 | 2025-02-21 04:12:00 | NPP-375D | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8baa541c-24ea-3049-b8d4-31a40f24d233 | -21.26247 | -49.00478 | 2025-02-21 04:12:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 79ef3865-ac03-3c57-8a69-aa75d45ed070 | -20.41574 | -41.36339 | 2025-02-21 04:12:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 98db0f18-a17d-3822-b6c2-78302377fbfa | -21.9848 | -44.52134 | 2025-02-21 04:12:00 | NPP-375D | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9fe2d586-5f4f-3a95-ad51-b0ef8ba9f8f2 | -20.30365 | -46.49692 | 2025-02-21 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de753481-4e44-31a7-9d62-b93a59846dcb | -18.61159 | -44.25619 | 2025-02-21 04:12:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 303067f7-c34f-3a9c-a114-327d18d8afee | -22.69907 | -43.3465 | 2025-02-21 04:12:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1e4f9c4b-4d59-3957-a006-79b663f0f219 | -21.62481 | -43.46452 | 2025-02-21 04:12:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5f83be55-bb9b-3b84-a9fb-4661b972ece0 | -23.4039 | -46.55669 | 2025-02-21 04:12:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 49160ebf-b8c9-39a9-b2da-70bccc27ab14 | -20.99512 | -44.16078 | 2025-02-21 04:12:00 | NPP-375D | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f712c859-1802-3eb3-9e8c-81c80f9e2f96 | -20.41635 | -41.35891 | 2025-02-21 04:12:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 74bfd269-283b-3831-a6a4-2f97a0d69b3c | -22.23114 | -42.19575 | 2025-02-21 04:12:00 | NPP-375D | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| da3f5368-33d0-3118-a05c-782f224179ad | -20.19878 | -43.28915 | 2025-02-21 04:12:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 429dd5cf-a72c-3cb9-9be9-a454dc27ce6d | -20.19935 | -43.2853 | 2025-02-21 04:12:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c5590c6f-52d6-3e44-a280-90bc2d90aa5a | -22.69748 | -43.34768 | 2025-02-21 04:12:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 37165f64-5c22-3a29-9cfa-7b7ce305f268 | -19.78126 | -45.39411 | 2025-02-21 04:12:00 | NPP-375D | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3373e4f9-07da-33ae-b245-0e838412c89e | -20.31041 | -46.49833 | 2025-02-21 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41e0e01c-424c-3650-998c-14d9ab70b340 | -20.45883 | -43.27483 | 2025-02-21 04:12:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 24a9cbf7-5f6b-30ce-ba27-0c27b099fc72 | -19.4391 | -49.30745 | 2025-02-21 04:12:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 097df772-dc53-3dfd-b094-a071b4722f01 | -20.99847 | -44.16135 | 2025-02-21 04:12:00 | NPP-375D | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6a38208d-d51f-3f0f-b5b4-45769e2c3bf5 | -21.19579 | -44.93948 | 2025-02-21 04:12:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7b17c33f-cba5-3ea8-ae30-56d33d760595 | -22.78658 | -43.75721 | 2025-02-21 04:12:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 69d57d2e-df2e-31d7-892d-3b77579c27b1 | -20.94749 | -43.00336 | 2025-02-21 04:12:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8eb03748-9c22-3e99-8962-f817d8094538 | -20.94405 | -43.00277 | 2025-02-21 04:12:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1c8b973b-fd2b-335c-a6b4-d7e11f26f406 | -20.19975 | -46.53392 | 2025-02-21 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 051a77e4-65a3-3e61-a1a5-8d7ea64bd2dc | -20.2004 | -46.53004 | 2025-02-21 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0986f24f-3e30-3992-b22c-6956b7596fe3 | -20.30703 | -46.4976 | 2025-02-21 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5132a252-f3c4-37e2-b2cd-808b2864282a | -18.63507 | -43.17133 | 2025-02-21 04:12:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| ebebba4e-efa3-308a-8868-e8109f7ecbba | -22.85568 | -43.49973 | 2025-02-21 04:12:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1f18bb5d-1670-3c09-a283-c0c739e3678b | -20.19766 | -46.52544 | 2025-02-21 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 047db5e2-72e8-3067-9ce9-ae4d4830f81d | -20.20105 | -46.52613 | 2025-02-21 04:12:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42a2b6ab-4eaa-3742-badc-f22f0c32cad5 | -21.19637 | -44.93577 | 2025-02-21 04:12:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2e298838-4e43-38dd-b1ee-43e39b985237 | -28.58582 | -49.44345 | 2025-02-21 04:14:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 780f833f-628a-3294-b7ec-6f901c5694dc | -23.98555 | -48.91613 | 2025-02-21 04:14:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 723857cf-ab14-301a-9ee7-9911fcf2becf | -29.77943 | -51.17558 | 2025-02-21 04:14:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| 2fcb8e1e-9a95-318d-b4d2-2aebc6e2a6e2 | 0.69113 | -51.46078 | 2025-02-21 04:27:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9750f820-daaa-37d6-a11f-bb1e87232ccf | -5.8779 | -48.10724 | 2025-02-21 04:29:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc84559f-8c4b-3c87-81f1-17a176d6e3b5 | -6.97505 | -43.01681 | 2025-02-21 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 45a07f2a-1730-3b9d-be51-1f6fae60edf3 | -6.21038 | -48.06784 | 2025-02-21 04:29:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa690228-50c3-3063-ab6a-a4abe3bb4277 | -6.97557 | -43.01331 | 2025-02-21 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7ad6385a-e4d4-3792-8ee7-3aa128de8cbe | -5.67504 | -45.23197 | 2025-02-21 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86bcefc9-1c60-3018-ac51-4b74f86751b4 | -5.25689 | -45.24257 | 2025-02-21 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b9b6912-8093-3d8e-ac61-206f87fe2969 | -6.21093 | -48.06438 | 2025-02-21 04:29:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01403720-95bd-3c2a-9d18-2fb3a438be5b | -5.47565 | -46.16049 | 2025-02-21 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63b8fbb6-e7ce-35ef-87a1-fe222a347813 | -11.86472 | -46.94238 | 2025-02-21 04:31:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73e97079-0993-34d2-94f5-df5ef925707c | -14.43274 | -45.63608 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bb90bef-7af9-30e7-857b-030d76e03a07 | -10.35316 | -44.842 | 2025-02-21 04:31:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 549317a8-93ad-335c-ad14-e7f363749760 | -14.439 | -45.64666 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 972760bb-441d-3cd1-b039-74b0f0fdd61b | -12.15832 | -44.18467 | 2025-02-21 04:31:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdf3ccd5-cc10-3851-8e71-94b7a765a94a | -11.85782 | -46.94128 | 2025-02-21 04:31:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da6f39d6-aee0-3bf7-986d-bc63eed314e4 | -11.80292 | -46.65229 | 2025-02-21 04:31:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52d2d823-6c07-3f45-85de-e70b736bcf18 | -12.35074 | -47.99362 | 2025-02-21 04:31:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 476f5dfa-b185-32fc-9cd7-65f4dd143498 | -11.57463 | -47.61374 | 2025-02-21 04:31:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e6e0376-8465-39e0-9fb6-95b4c5050c5f | -14.43026 | -45.62607 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79d286ea-e46c-398c-973b-42d155763766 | -12.80414 | -45.00486 | 2025-02-21 04:31:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71b30ba3-1741-3da2-8107-189ac6f2332a | -13.53188 | -46.50403 | 2025-02-21 04:31:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46f9a9bf-ff91-3c63-9cba-d6ba96d59168 | -14.43587 | -45.64137 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README5.md)
