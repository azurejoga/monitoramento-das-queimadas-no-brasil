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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e94e48fa-ffc9-39d5-a525-13d8b8eb4a5e | -7.64835 | -46.26271 | 2025-08-21 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a184e87-73ef-364d-b2c2-03ea9bc987ea | -7.65685 | -45.24594 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 927c9b09-4e42-312d-aa92-6c09562cce49 | -13.81142 | -44.19878 | 2025-08-21 03:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68b39423-0495-38cb-9727-e961a9f0e294 | -7.64951 | -46.25619 | 2025-08-21 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ba620bd-577e-3be9-a987-99402efc6a0d | -7.60506 | -44.38496 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d153d259-5315-37b5-89d1-c5b910738297 | -6.17356 | -44.73664 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4339c30-0849-3737-8310-5c9560c54a26 | -8.34425 | -47.50438 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 848ca9e4-cd96-3350-80ae-507851a68d1a | -13.0215 | -45.16754 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 2136cd5a-2632-3b1d-a74f-092b6b46a78d | -9.66646 | -48.3815 | 2025-08-21 03:49:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df1b8d94-4fd7-3b27-bf14-aecf976d4041 | -7.38898 | -45.98703 | 2025-08-21 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bb8b45d-7236-3b4d-817d-03b6e91cf64b | -12.94545 | -46.184 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b35d28f8-eb5f-3832-9d1d-6c063b9bd934 | -6.42909 | -45.48832 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5659ece3-5e91-31af-991c-3f5654c35078 | -9.86434 | -45.97997 | 2025-08-21 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2bd3ba77-d960-3fbc-ac7b-e1d85e144181 | -7.01796 | -44.60973 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| db520aa1-94b8-3aa7-bd2e-fab9a8616741 | -8.16031 | -47.36301 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e36a14b-14a2-3ab7-8217-ad33e47bb5ee | -13.64212 | -43.80428 | 2025-08-21 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1620723-3233-3261-9a3a-bb3f1206c250 | -6.49737 | -43.1072 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35344e0a-a26d-3bd1-8e0c-74751beda981 | -7.72318 | -46.6194 | 2025-08-21 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6e2b22f-f535-32b1-ab0a-6f14cb1c42a9 | -12.08714 | -44.72217 | 2025-08-21 03:49:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2483d2e7-e457-30a7-8916-df1695587b78 | -8.28825 | -47.28599 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9f094a5-55ee-3a65-8dd4-181857d6f4ee | -12.98639 | -45.20774 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a4411fbe-229a-3d42-8d89-1c1ac8d0a634 | -13.0371 | -45.20795 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 58a22856-05f8-308f-a4a2-8768c50470b0 | -7.63123 | -45.24778 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f1a59c41-c1a0-33cb-a7d8-d7b75a2a0e6a | -13.03122 | -45.16474 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 3664e0be-a7e1-3a6e-86e9-e3a10d754504 | -7.63514 | -45.25443 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 70f22822-521a-3215-b69b-89e426b37722 | -12.93898 | -46.19212 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d66fb22-358c-3ea6-b4ff-a77f4cf5f63e | -12.97832 | -45.20154 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95f225be-fdb9-3568-b093-a0fbf90f2913 | -12.88812 | -46.06674 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c99bc0ed-89a7-303f-8969-c2dbcdc326f6 | -12.94435 | -46.24231 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 55a83aca-c7f6-3c65-9a2b-ba741597866d | -13.32886 | -40.34335 | 2025-08-21 03:49:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7e313e53-e306-307a-83a3-1e22ba28c9dc | -7.65837 | -45.24928 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 59c9e81b-3246-3044-a29f-16d35c722497 | -8.09573 | -42.35211 | 2025-08-21 03:49:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b14515d5-7f0c-3feb-9ed3-45e13d27676a | -6.36202 | -43.25927 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dbec956-61f4-3f04-815c-cd6261b44f68 | -13.04203 | -45.18101 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7e4a41eb-5cb6-3961-81b2-6ad6b497b11b | -13.15542 | -46.90264 | 2025-08-21 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c05eef63-0699-3002-8a0f-b343f30dc414 | -12.97927 | -45.20707 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9bd8c4de-da3b-3ae5-8a1f-cde5eeb6bf0f | -12.66924 | -44.96316 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c3efbab-77cb-33af-b513-15d36851ff15 | -12.66483 | -44.96231 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b444652e-ce70-3974-be00-92ee49d29876 | -13.03316 | -45.1792 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| cdef0437-54de-35ba-b49a-8e8d486f3b6f | -11.81325 | -50.64888 | 2025-08-21 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f006629-1505-3ac1-a0ce-edcf686dce6c | -12.95455 | -46.24075 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e0790f4d-5ef9-32d4-88e5-12b767f5c561 | -12.22141 | -45.40031 | 2025-08-21 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf832f82-8010-3160-b154-9fd09a7804f8 | -6.94866 | -42.86127 | 2025-08-21 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e954b0d4-0e38-326c-a21b-ccfbc8423d33 | -10.54051 | -42.55058 | 2025-08-21 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 35723ff9-92e0-3e94-809c-131700eb9daf | -6.13162 | -44.71864 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f95b9c8d-b5bb-352f-97bc-fe52f1fa0ba2 | -7.88956 | -46.72781 | 2025-08-21 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9382e45-5b1f-37a5-97c2-eca4c10dc10c | -7.95093 | -42.64015 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8d489134-1081-347f-9535-39fa884b7231 | -12.64533 | -46.86603 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5522d56d-84c8-385e-aa14-ee5e28bd9190 | -7.01603 | -44.61774 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 96ca3789-369f-3dd6-b9b6-ab81f1d539a2 | -7.02824 | -44.60693 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 812a9531-8538-34a9-9306-f05b35a899fd | -7.88894 | -46.73129 | 2025-08-21 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6768a4f-1796-3de4-8136-2f64b0870237 | -7.86131 | -46.72987 | 2025-08-21 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 14271eb2-37bf-39a1-8194-8db342c50a56 | -7.85303 | -45.1888 | 2025-08-21 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cdd57312-0338-31e6-8393-22ca51da9c72 | -12.98107 | -45.21148 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7a4cbc04-c23b-39af-8cdd-ad4c11b241f3 | -6.49616 | -43.10374 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6282df0-ef1f-3975-97cc-85a54600cb85 | -12.64394 | -46.90114 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adabebc7-995d-3720-9319-95f8490799b7 | -7.86193 | -46.72642 | 2025-08-21 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8479688c-426e-3663-9dbb-7ceaf0b54ee4 | -10.70522 | -48.22373 | 2025-08-21 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 351dd477-3a26-333b-89e3-b36f9237d07b | -6.29589 | -43.88368 | 2025-08-21 03:49:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19d88813-15f6-33b8-99ce-e103e090d77e | -11.81191 | -44.25737 | 2025-08-21 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9de0bc1e-9535-390f-8070-86a61016065b | -6.42609 | -44.67177 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d703fc4a-db3e-3cff-b1e5-cb7f770a6d88 | -6.29024 | -43.69164 | 2025-08-21 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3f51264-f2b5-3239-b410-1f1150ac5f1d | -13.65404 | -42.47973 | 2025-08-21 03:49:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| af75c900-06e2-3dd8-a1b6-03cc4073fe4a | -12.71889 | -44.7873 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| da16fe8f-e7ed-30c6-a335-30b0b17656dc | -13.04009 | -45.16653 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a340fcec-8ac9-38af-9b7a-3a49aec9c27a | -9.33566 | -48.51989 | 2025-08-21 03:49:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15e0eb11-f983-3d29-a0b4-eaf53a71e4fa | -12.98009 | -45.20249 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bacfc759-20c9-3866-9b8d-941146e183ca | -11.17696 | -46.14172 | 2025-08-21 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 113452e3-8322-30e2-ac20-b9169cec358c | -9.87523 | -45.97648 | 2025-08-21 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f7658a5-d033-30e5-8962-f03ee6e17186 | -6.10745 | -45.4124 | 2025-08-21 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65037d2c-313a-3fe4-9b22-794bfee8400a | -8.14299 | -47.34137 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa918294-7033-38d4-8a2b-16cb5883f5c2 | -13.05058 | -46.8288 | 2025-08-21 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f61ac18-c32d-325b-ae29-1b543353febe | -7.66178 | -45.24669 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb87f7c5-4d0c-3009-871a-b452e65c12f1 | -12.08539 | -40.31642 | 2025-08-21 03:49:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fb66fbdf-0594-3b18-8cf0-95bb268a67f0 | -12.89566 | -46.07889 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0bb44779-716a-3848-a35f-184996c2fd37 | -13.03875 | -45.19895 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 907f09bf-4793-3fc9-921b-c4c222036fa3 | -6.56868 | -43.00157 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7b051cc-abaf-3c4f-aca8-8678c1af1ccd | -11.02238 | -44.59803 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8cbb363f-b5ee-3c49-92c0-938a689ebdc4 | -7.20803 | -45.31421 | 2025-08-21 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7a2fef6-713d-3a5e-90fa-aa053a41fd59 | -13.02234 | -45.16303 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2d8436e1-37b0-3705-b2a5-67de7d4794f6 | -7.0218 | -44.61573 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| f43d6fec-bc3e-3b14-97f9-e120b885b7a4 | -7.63864 | -45.24633 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60c00668-f632-37a1-a6a9-586c89b726e2 | -6.28947 | -43.69623 | 2025-08-21 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4c57a60-3bd6-3da6-b7c4-f4ac3f4e2335 | -11.30176 | -44.9496 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a1179de-d4e7-34c0-8ee0-47258b2efc56 | -8.3834 | -44.60454 | 2025-08-21 03:49:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbf517cb-24d2-32d5-a145-d4cc6fc91c68 | -7.6308 | -46.26984 | 2025-08-21 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 758d4c35-161d-366a-9868-c5ec8e7a8221 | -13.03483 | -45.17012 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b78e6973-0cbf-3364-a238-4ad2f6bacee7 | -6.42216 | -44.66574 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fd4eb05-0b6e-358b-b40c-c82fbd937331 | -6.95647 | -42.86657 | 2025-08-21 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 521315d5-1f73-3803-8a3e-2eb2842c6f0b | -13.02317 | -45.15854 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 848dcdfd-e2b5-3934-af93-c664dc00f18c | -13.03347 | -45.20258 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9b32624-adb3-39ed-8d5a-c328b3c35cbe | -13.18488 | -46.91056 | 2025-08-21 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d36e7ee5-952e-3b22-ad75-6fa3d3f3271b | -6.36272 | -43.25504 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d45b9ae5-0a32-32aa-aadb-beca6ee89bcb | -6.51358 | -45.45472 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80414dc7-dc69-3eba-ab07-a9da8de97f4e | -11.02611 | -44.59678 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 341f2dfa-54be-3a1d-9fa3-bf6f624b8127 | -6.61648 | -43.88503 | 2025-08-21 03:49:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 586fdae9-dc1f-3317-9d1a-55341360e3e5 | -13.75564 | -41.79346 | 2025-08-21 03:49:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7fadcb82-5f75-3dea-9065-64d1315d219f | -7.01517 | -44.62286 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| ce804757-8fef-3b98-8d5b-0e18dd753610 | -13.64149 | -43.80786 | 2025-08-21 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a17742d1-4576-3e76-8054-705714870376 | -7.02651 | -44.61681 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |


[Clique aqui para ver as próximas entradas](README17.md)
