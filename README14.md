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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2de90be-b517-3132-9968-c5bc74d49a78 | -13.20802 | -50.7547 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a011d455-a76e-381e-9b5a-c9ba8b87b594 | -14.18107 | -45.33709 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58da006d-a420-33e6-af05-5d82b1b9b274 | -17.32905 | -41.60289 | 2025-08-18 03:55:00 | NOAA-20 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b7153adf-4675-3e0f-8fc2-b21c2b814b8f | -12.53806 | -48.49893 | 2025-08-18 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a236955-4572-3463-9b14-242eda66aa5c | -10.99759 | -45.65673 | 2025-08-18 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cea2feeb-c88b-37e5-bb09-5f3db0357aae | -12.4265 | -43.76468 | 2025-08-18 03:55:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93532f48-63d3-312b-b817-ba5618b7a3be | -15.86678 | -50.21329 | 2025-08-18 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 67e6b29a-df79-3709-b900-c6f64ea41025 | -14.17478 | -45.30256 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20a01001-0253-32b6-9760-5660bfa1dddc | -9.1801 | -49.66932 | 2025-08-18 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cb0635e-5751-335c-80e7-613bf5bd0be2 | -16.22227 | -43.14162 | 2025-08-18 03:55:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f6331aa-2358-32ec-afae-3e7c58b31b60 | -13.96432 | -54.08551 | 2025-08-18 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bede0ab-3047-353b-b63d-5dc2a961c010 | -14.5672 | -44.06372 | 2025-08-18 03:55:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ee227ba3-6e10-3c1d-9213-42421ebec6ac | -13.42191 | -49.13699 | 2025-08-18 03:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b76fa72-7f5b-3b84-98d8-84f7773f1d86 | -11.80875 | -44.9397 | 2025-08-18 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1e06cb4-f0eb-33f6-af0e-a40c3cd1aa27 | -11.85159 | -51.58515 | 2025-08-18 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 22495fe0-f214-307a-8df1-155d777da3c2 | -8.78074 | -50.00236 | 2025-08-18 03:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f2ecef3d-f949-35ae-8707-9068f0d5d7ce | -12.53489 | -48.49821 | 2025-08-18 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98ceaedc-4821-3884-880a-561bb2351e91 | -13.5767 | -46.99603 | 2025-08-18 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e84ae309-aba9-37a9-9c75-1e3c12a7c57e | -11.80404 | -44.94262 | 2025-08-18 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f357ebd-f223-3a38-97fc-ed9fa77b32d2 | -13.22294 | -50.74046 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 823c1cdf-9b2b-3568-adfa-913e607a9a53 | -12.18744 | -47.22964 | 2025-08-18 03:55:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68192499-debb-322a-a973-e0147d2641b1 | -13.87293 | -45.53963 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ea8d262-a7cc-3f4c-b71d-72f36b716dbd | -13.23195 | -50.75552 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7dc0699-8fd6-333e-9075-df314d4c226b | -12.18651 | -47.23465 | 2025-08-18 03:55:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f67abc82-8a7a-3364-a562-1fa6dbfad437 | -13.61872 | -46.89632 | 2025-08-18 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8ea4e18-338a-3cbd-a402-52a90b5a6e77 | -12.5324 | -48.50096 | 2025-08-18 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bc86327-7eed-31f1-a51e-942c8afd1fae | -12.62651 | -46.89515 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f33d5b47-c241-33f0-980f-bbef00c4c950 | -13.97047 | -54.08516 | 2025-08-18 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d679779f-b00c-349e-99ae-fa8dd1ad50ad | -14.62722 | -54.91066 | 2025-08-18 03:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e330281b-c8ea-3102-84f3-2b4bd98ff04e | -13.43312 | -45.89967 | 2025-08-18 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74a5fe40-d9d5-3770-98f2-c147034283b0 | -15.86751 | -50.20964 | 2025-08-18 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 24ebdafe-1602-38b1-8941-20bbd63d0498 | -15.72525 | -48.41783 | 2025-08-18 03:55:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcf7d6b7-466c-310e-acd5-ca43e6e7c59e | -16.97365 | -41.86299 | 2025-08-18 03:55:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5b50e5c7-cdbe-3bd2-9db9-0fb54fff1d43 | -14.62006 | -54.90908 | 2025-08-18 03:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a941b03-ca00-3fd2-af47-47887ce55c99 | -13.58452 | -47.75677 | 2025-08-18 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df5617ed-000e-3dc8-9504-d7c6f9805b58 | -9.86983 | -44.69402 | 2025-08-18 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f852185-2ae0-35c8-b1a8-afc4af9a136b | -12.61573 | -46.90084 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc2914c0-2e68-3a44-8694-0c1ed316eebc | -13.20717 | -50.75887 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 87f32328-93e8-301a-9b89-1f2b52d3fcc2 | -12.63579 | -46.89593 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e4efa8c-4c16-3b33-b64e-61f2da062e2f | -8.77872 | -49.99858 | 2025-08-18 03:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 73cf5d01-007c-38bd-bffd-e0505a75d3cb | -14.18088 | -45.31476 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2469ccea-9b0e-3f55-a164-3dd67dd45d16 | -14.62552 | -54.91823 | 2025-08-18 03:55:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d4cd07f-9bae-3d9f-b515-43a1c80835c1 | -13.42962 | -45.89491 | 2025-08-18 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9119a02-c873-3def-b4a3-709ecaf72821 | -11.85052 | -51.59039 | 2025-08-18 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2890c311-cd04-3050-aea6-957516f13b04 | -17.21832 | -49.58292 | 2025-08-18 03:57:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d8ab798-4920-3e72-bce4-ce1c563c468f | -21.42658 | -43.88316 | 2025-08-18 03:57:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 3ee291b9-fc90-3e21-b3bc-e3a8cc890067 | -15.00611 | -54.79183 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 064abef3-00ef-3e3d-9ef2-5682faeb84bd | -19.99967 | -46.15701 | 2025-08-18 03:57:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc1e5d07-16e2-3efc-a220-d6fd1c0a9385 | -14.95243 | -54.76655 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7c079ab-a367-3e86-892d-32a40d034d35 | -17.09538 | -49.88532 | 2025-08-18 03:57:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6ca4c61b-9c0b-362f-ae57-60997ca69b9d | -19.14884 | -47.03342 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 808bd4c6-2d1d-33ce-af65-08cefad92456 | -18.54438 | -43.99502 | 2025-08-18 03:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36877b67-6d88-34a9-8dc6-2e0979b99d94 | -23.11949 | -45.69226 | 2025-08-18 03:57:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 96b035b5-37e1-357c-9d44-937010376f8e | -17.39116 | -42.62391 | 2025-08-18 03:57:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| acea1d76-c2c4-33e6-a8af-ed749439b07f | -16.83962 | -48.91345 | 2025-08-18 03:57:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3681542f-0671-34f2-b67e-38682c6c139d | -20.21432 | -47.03735 | 2025-08-18 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68de000b-2781-3982-913b-35f403ecff9f | -22.32922 | -47.72664 | 2025-08-18 03:57:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c20b535-304f-3d4f-aacd-dfe301ff21ec | -22.14553 | -44.82771 | 2025-08-18 03:57:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f1285acd-b275-3bcc-85d2-6b2cc9c60785 | -14.99358 | -54.79714 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3432b699-aa04-3305-8c21-c35df4cf9e2d | -22.66959 | -47.65957 | 2025-08-18 03:57:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a8e2136a-3c76-35e7-b1eb-b8e8d653156c | -17.09287 | -49.87146 | 2025-08-18 03:57:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1c7ef598-7367-3ee4-8f70-ef4a1a1b0c65 | -22.20079 | -56.03872 | 2025-08-18 03:57:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c8ed9fe-4ff5-37ea-95fc-4a3595841ad1 | -19.12878 | -47.00503 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de4621bc-36f2-395f-adce-c93fa6a22a01 | -22.20128 | -56.05067 | 2025-08-18 03:57:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a67d9c36-a7e9-38f0-8ad1-34f4c5c59715 | -17.92449 | -44.36844 | 2025-08-18 03:57:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b80444e8-5d34-33dc-9fe2-8b4054d80586 | -17.09351 | -49.86829 | 2025-08-18 03:57:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ac686e6-48cc-3d59-b62a-f78b93cba285 | -22.14202 | -44.82711 | 2025-08-18 03:57:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1967b201-ea3c-3157-a40c-9d663cd9b66c | -21.79191 | -46.58197 | 2025-08-18 03:57:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 67bb168e-f401-3b12-b129-e37a94f8ac29 | -15.00271 | -54.78971 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b915617-ac43-3c5b-88db-e8e0aa701e49 | -17.39135 | -42.62714 | 2025-08-18 03:57:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c6f51477-499f-3db7-a712-f00157937c1b | -19.14397 | -47.03667 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 54949481-a590-3340-8f9e-84e28d07d0cf | -17.39054 | -42.6277 | 2025-08-18 03:57:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ea1bf915-4024-322b-a79a-7bc2155e07a2 | -19.53733 | -45.61439 | 2025-08-18 03:57:00 | NOAA-20 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e84a9d1-1471-3c46-9f3d-1a3f8d3a0699 | -19.15138 | -47.0424 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b96ee00-1734-3282-a009-6aac236d75ea | -23.37944 | -45.4375 | 2025-08-18 03:57:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 756d2d0f-6259-3fb5-a07f-4de98921e808 | -21.11472 | -44.23003 | 2025-08-18 03:57:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6aade7e2-6ff3-35da-9a97-a6d9e9767ad1 | -20.4247 | -43.67916 | 2025-08-18 03:57:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 74f8e3d3-5d70-38ca-be21-0fcaf893e2c2 | -14.95774 | -54.77589 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad17100f-3b61-37fd-b941-e6aa90803d52 | -15.00231 | -54.80893 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 77bf8301-9a4c-33e9-9052-7f248d3fd11d | -14.98634 | -54.7807 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 77d8fa0a-52cc-310e-beaa-97b4ecaeb333 | -20.48252 | -44.14669 | 2025-08-18 03:57:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4cbfba10-a307-3d2f-88f8-195c7931357f | -19.13284 | -47.00594 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be1e8bbe-196a-31d9-bbb2-0b5311fee5b5 | -19.51712 | -40.99069 | 2025-08-18 03:57:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e0333975-49b5-3664-b485-d211a7c54419 | -17.89504 | -44.43065 | 2025-08-18 03:57:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 673a1815-ae7d-39aa-9067-c2d553bfa1d3 | -23.76218 | -47.38213 | 2025-08-18 03:57:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 84d240bb-0d72-3b33-8639-40250bb0e3d7 | -18.78181 | -49.07929 | 2025-08-18 03:57:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4999230-0038-39c8-95a4-2e17876a4505 | -17.39456 | -49.22789 | 2025-08-18 03:57:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29627953-cf4f-3dc3-a0c4-674e37acabcd | -18.54859 | -43.99155 | 2025-08-18 03:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0747243e-b075-378e-9da6-0e5ad1878832 | -14.97357 | -54.77151 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c701ae7a-49fc-3b3d-a35a-f4b8d2a2374b | -20.42537 | -43.67519 | 2025-08-18 03:57:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6f0d8470-303a-3629-8ba1-e3398007d587 | -14.99001 | -54.79749 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b3ddfa87-e85d-32f8-9e75-a4d5bdca1be6 | -20.20699 | -47.03197 | 2025-08-18 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7659999d-b04b-33a4-b123-4b8d58a34bd6 | -14.97028 | -54.78614 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bc6957de-6bc9-3bd6-8462-59bb7d436819 | -20.00532 | -46.14785 | 2025-08-18 03:57:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a012c27d-5539-39d9-905c-40d21c69b1d2 | -23.44737 | -46.96735 | 2025-08-18 03:57:00 | NOAA-20 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0c03c991-c738-3553-839f-eeae35a0a3c3 | -19.43182 | -43.73255 | 2025-08-18 03:57:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e4c638a-255d-3473-8ed6-49fd26f64268 | -22.93747 | -47.0378 | 2025-08-18 03:57:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c396b384-5553-3629-bbc9-0547518019d8 | -17.39261 | -42.61956 | 2025-08-18 03:57:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d4cd0601-fb68-3736-b010-f42357ff2adc | -22.20285 | -56.04424 | 2025-08-18 03:57:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be2448db-02e7-3f55-a909-c6212b73003b | -23.30509 | -46.89157 | 2025-08-18 03:57:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |


[Clique aqui para ver as próximas entradas](README15.md)
