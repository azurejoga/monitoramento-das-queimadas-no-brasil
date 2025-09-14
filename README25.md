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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 982ab194-0d8d-3498-b6f8-893b16e2ff3f | -23.16164 | -47.57823 | 2025-09-14 03:51:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e0f4033c-75f9-3c2f-ba79-0c87b5c8801a | -19.09195 | -44.49388 | 2025-09-14 03:51:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 60e7053e-cb85-30e2-95ad-10b511d80476 | -22.17603 | -49.61872 | 2025-09-14 03:51:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d3b99563-846d-30b6-a366-29287ef6afa7 | -19.64236 | -45.377 | 2025-09-14 03:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ff8fe39-9c15-3001-a98b-92580de98895 | -21.07489 | -47.11265 | 2025-09-14 03:51:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 75169eef-0677-3821-9a85-230dbdb10947 | -19.71994 | -45.43222 | 2025-09-14 03:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36751634-b431-3461-a366-94efb810b74b | -21.62537 | -46.81645 | 2025-09-14 03:51:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8dd98ef9-60a7-3d89-9203-5bb99026c906 | -18.15867 | -49.20214 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2f6e03d1-00fc-38e8-9527-8578e565ad26 | -18.58678 | -47.19774 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 134cec69-026a-335c-93a0-0d69a0066e12 | -18.58948 | -47.19668 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02864baf-1511-3a10-acb0-9554b963afc6 | -22.9936 | -46.46588 | 2025-09-14 03:51:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e510e78d-38ec-3b98-937e-c99cd0b4b3cf | -22.98949 | -46.46507 | 2025-09-14 03:51:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4cfdaa1a-2f09-399d-add9-2b56b6d13699 | -20.2528 | -47.80544 | 2025-09-14 03:51:00 | NOAA-20 | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0aa5cf67-b153-31ac-8d43-9ee2e1c6035e | -19.16983 | -42.66975 | 2025-09-14 03:51:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ab807c39-9452-32be-8334-abd856a59673 | -17.35991 | -52.90664 | 2025-09-14 03:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13898531-b721-3dcc-9626-06cec627ef8b | -20.79603 | -49.36084 | 2025-09-14 03:51:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f417e7e3-c7dc-3d13-97b4-40853879fcdc | -19.17129 | -42.6613 | 2025-09-14 03:51:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b61fa0e8-1110-3b9d-9198-ab8e594871c8 | -20.25031 | -47.79365 | 2025-09-14 03:51:00 | NOAA-20 | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c5b04996-efc5-3279-888a-d9ee92a9289f | -23.1464 | -50.40512 | 2025-09-14 03:51:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bb591da7-7880-3148-8dcb-24eb3a87d9e5 | -22.22539 | -48.61248 | 2025-09-14 03:51:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| fa3c0b1f-91f8-336d-acd6-a42202807176 | -22.72495 | -49.89004 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e22bc92-1f71-3899-80a1-e74016a927e2 | -22.22512 | -48.61376 | 2025-09-14 03:51:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5973ac92-47de-3701-aa0f-8f261cd7ea69 | -19.1497 | -44.84328 | 2025-09-14 03:51:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dd22b7ca-2e33-34c4-ad80-dba6d7746a51 | -22.08244 | -44.95467 | 2025-09-14 03:51:00 | NOAA-20 | POUSO ALTO | MINAS GERAIS | Brasil | 3152600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 949e3563-76d2-3aa6-908d-baf7d4689c40 | -17.36614 | -52.90107 | 2025-09-14 03:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d2fdd5bc-56a1-3198-8fad-b5260d5bfdde | -18.15781 | -49.20616 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f1f1c840-fde5-3492-a18c-770dc3cc0bd0 | -21.0979 | -47.17535 | 2025-09-14 03:51:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83018928-0dab-3f99-933b-0dfdca026667 | -22.00818 | -47.26896 | 2025-09-14 03:51:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c02878d9-a694-3b84-85f1-4d946ec3ce9d | -19.1741 | -42.66623 | 2025-09-14 03:51:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 56a42cc6-70de-3e28-bf0e-fd0e8c015e69 | -19.70621 | -45.4376 | 2025-09-14 03:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d83d08bd-24db-3850-b488-6157317d85d1 | -18.14209 | -49.18736 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f3485b81-aae6-3f77-b0d7-0ecdf93813cc | -19.63332 | -43.73201 | 2025-09-14 03:51:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b6fc9ac2-f9c2-3769-a873-b18738ae29d6 | -19.67177 | -43.10762 | 2025-09-14 03:51:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2ee02d20-ec4c-30a2-92e7-1ab6e7ec30c2 | -22.28435 | -45.96444 | 2025-09-14 03:51:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 76ca18eb-15da-3355-ae34-52f580a5c47c | -22.72998 | -49.89146 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4069b1cb-bcb8-32a2-92e7-15f651c0763e | -23.72118 | -50.8412 | 2025-09-14 03:51:00 | NOAA-20 | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 17ee1c58-d771-390c-8a1c-398bea6b27f9 | -19.17056 | -42.66553 | 2025-09-14 03:51:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fe974bbe-7240-3e42-8c55-9ffb6f361b4d | -18.91692 | -48.01432 | 2025-09-14 03:51:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d279ca34-fa0a-307f-8ce0-339c3989e441 | -22.05138 | -45.6609 | 2025-09-14 03:51:00 | NOAA-20 | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a0764e3a-4a5e-3e80-9158-24531e1925df | -22.19405 | -49.60872 | 2025-09-14 03:51:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0524b220-1f1f-33a1-944b-52942cbbe904 | -18.06549 | -50.74231 | 2025-09-14 03:51:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d40adb5-53e5-3a24-b58c-3e85aec33cea | -17.83048 | -50.4309 | 2025-09-14 03:51:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a32b2653-8211-38f6-871a-039119ceba46 | -20.47987 | -47.45663 | 2025-09-14 03:51:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97a08081-42ea-3e30-b8ca-604726951109 | -25.08439 | -50.91539 | 2025-09-14 03:51:00 | NOAA-20 | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4eaac4d1-f2ba-306a-a335-ad133ca96209 | -20.13011 | -46.87793 | 2025-09-14 03:51:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae032246-818d-3f0e-b65b-ca9b2ea334a0 | -17.83139 | -50.4267 | 2025-09-14 03:51:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb635742-11db-3fdc-aa5a-9e2adc30f3b8 | -22.72778 | -49.90143 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d25d013-b4f0-3a49-ada7-ab7f1cd42899 | -18.26452 | -46.94105 | 2025-09-14 03:51:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddb36289-a78e-3223-99c7-3b7a2374e497 | -23.48027 | -50.84974 | 2025-09-14 03:51:00 | NOAA-20 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 203b5cb6-c4d5-322e-bbea-1ef613789444 | -22.78709 | -46.8007 | 2025-09-14 03:51:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ff89877c-c601-3899-a563-467012fb57b6 | -23.14713 | -50.40189 | 2025-09-14 03:51:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9f3e6f8e-f2df-3515-8daf-b7a9d899d8ff | -22.6635 | -53.12183 | 2025-09-14 03:51:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ad0bc0c-ae58-33b7-b2a8-4f2c4a017db2 | -18.9745 | -48.59142 | 2025-09-14 03:51:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 791cc5ad-0d28-3f8d-8bfd-e7afa4043d35 | -19.70547 | -45.44148 | 2025-09-14 03:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f1dce6a-f686-3a99-b23c-1a8bae12fee1 | -21.30402 | -48.55532 | 2025-09-14 03:51:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef604183-1e01-330e-a4de-a9e70b5da197 | -22.72351 | -49.8966 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea640cf6-151c-3cc8-8a3c-bee90aa318cd | -22.99284 | -46.46972 | 2025-09-14 03:51:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d218d3ab-37e8-3378-807e-c6f82c716943 | -19.17764 | -42.66694 | 2025-09-14 03:51:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3c9255e4-7952-35a7-9d05-25b3867da465 | -17.36299 | -52.915 | 2025-09-14 03:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ff5cf6a-063e-344a-8897-d961253fbdba | -22.17102 | -49.61738 | 2025-09-14 03:51:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0805b2f5-9522-3085-a4c7-b50ecfa65007 | -21.91804 | -46.55309 | 2025-09-14 03:51:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ecd72cd5-6791-3fa3-bf7d-fb54740f0479 | -20.24924 | -47.79895 | 2025-09-14 03:51:00 | NOAA-20 | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1e6d999-76bf-3548-bcf0-8aafb1dce6a1 | -23.79197 | -49.94599 | 2025-09-14 03:51:00 | NOAA-20 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 309ff8bc-1f92-3218-a3aa-89d5aa387ca1 | -21.76938 | -45.45383 | 2025-09-14 03:51:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1bc6592d-699c-338b-a635-b8467479e18b | -22.72705 | -49.90475 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c32039e-90c2-3639-8c45-b886fe88b3cd | -21.62628 | -46.81188 | 2025-09-14 03:51:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| e90dc172-d0e1-35dd-ab29-058a7761fd47 | -23.16876 | -47.56545 | 2025-09-14 03:51:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dc31374f-a156-3755-8ace-8df71899de19 | -18.60636 | -47.19673 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa9b9902-0607-3aa5-a114-4287a746a1e4 | -22.29291 | -47.95193 | 2025-09-14 03:51:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d76a36a-4cdc-35d3-865a-8ded14645d36 | -23.86625 | -47.58883 | 2025-09-14 03:51:00 | NOAA-20 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 30956e55-5dbe-39d6-9678-8859efac36c4 | -17.60667 | -51.83625 | 2025-09-14 03:51:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24c5312b-7a99-36d2-bb28-8c71e29bd0b2 | -18.1557 | -49.2022 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 71cddb6b-97ab-36b4-a806-3e1ce1d61310 | -18.46714 | -49.5769 | 2025-09-14 03:51:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a91d94c6-0ac1-3310-96bc-7253f1cef445 | -21.9214 | -46.55824 | 2025-09-14 03:51:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4fc01c3a-1afb-3e95-844e-51f86df468aa | -22.61208 | -47.66385 | 2025-09-14 03:51:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e25d90f2-297f-35ca-94bd-d5e3c41553b7 | -18.58571 | -47.20304 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5eb6c9ad-721d-35aa-bd4b-3d477e1c11a6 | -19.35906 | -44.80019 | 2025-09-14 03:51:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d74c001-ae40-3af3-b465-d7d3d014eea8 | -23.75457 | -51.77282 | 2025-09-14 03:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 18ebec2d-0ec2-3aae-b870-66472f291460 | -19.72381 | -45.86735 | 2025-09-14 03:51:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af91a5b5-aad6-341b-9860-329794274697 | -22.18174 | -49.61681 | 2025-09-14 03:51:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e5ef57cf-457e-3b55-8e59-3b486a10ae58 | -19.17837 | -42.66267 | 2025-09-14 03:51:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1062d187-2f36-3eab-b389-b0a1d3fc72c1 | -23.7564 | -51.76495 | 2025-09-14 03:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 4dee995a-97ee-39ac-8086-45380b7a60ff | -23.75547 | -51.76894 | 2025-09-14 03:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 22e32081-3086-3f1b-8e5a-e9a099e12890 | -17.39014 | -52.92859 | 2025-09-14 03:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00ba8d5b-8bfe-33ca-9c72-093f796bc73b | -22.72925 | -49.89474 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d512eca-1357-3953-b8aa-09eb2ef2f0aa | -19.17483 | -42.66197 | 2025-09-14 03:51:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1aa457a7-9027-378b-9783-0cfe615a92da | -18.58846 | -47.20194 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ccd0c942-c6fa-33ea-9639-5571c65e7ea7 | -22.73284 | -49.9027 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3f5cedc1-0148-396b-97ba-d8c5fc346996 | -19.71363 | -45.44313 | 2025-09-14 03:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2729442e-0afc-3b64-b0a1-eeb594d9c07c | -20.78546 | -44.90488 | 2025-09-14 03:51:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 27356ef4-152a-3af9-98e9-8c72a83f7e44 | -20.91092 | -46.45859 | 2025-09-14 03:51:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3d267569-fe7e-31a2-917d-c61295439a8a | -23.14717 | -50.40169 | 2025-09-14 03:51:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0d58be9f-9b18-3e19-8b11-52ac75cf4c53 | -22.9977 | -46.46671 | 2025-09-14 03:51:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 65f5a645-d2a0-39c0-9f50-3258b4b8bef4 | -22.73504 | -49.89271 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4874a603-07d5-3d09-b51e-b663a691eace | -20.57249 | -47.6778 | 2025-09-14 03:51:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09c2730a-b541-31a0-a689-355c63b8aca2 | -18.46175 | -49.57558 | 2025-09-14 03:51:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 507d19c7-0d8a-371f-920b-b0c10b8c3237 | -23.30725 | -47.35241 | 2025-09-14 03:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b0b247f6-a04c-3d6f-9cf2-a165ee5fb3e4 | -20.08457 | -46.89824 | 2025-09-14 03:51:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bb7b2a7-ee39-321b-b276-6511f73b3bef | -18.59033 | -47.20415 | 2025-09-14 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7307e4b8-2142-3871-bdbc-be2f942db294 | -19.09584 | -44.49467 | 2025-09-14 03:51:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README26.md)
