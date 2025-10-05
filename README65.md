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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b362a5c0-d33a-3cfc-a0f9-52845f788ce2 | -12.5996 | -48.12509 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d847bcd5-2ba6-3f84-926d-d9dc57841ed5 | -13.59409 | -48.1636 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b103b128-e2e4-3caa-8c9e-a7c93b0abca9 | -11.09146 | -47.88178 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d88b16c-a77f-3a01-bc2f-0bc7c0b1012d | -13.07699 | -47.92228 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f4e2de6f-f847-3b33-bd4e-fe982fa68adb | -12.42016 | -45.14913 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2a9c05f-98ee-3c6f-b5ca-603d656ee77e | -14.93206 | -46.84467 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e070e3e-0741-3e18-9736-d5173931efd7 | -15.12818 | -45.74698 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be9a85f4-dad2-334e-b03a-7eced0a47980 | -12.5957 | -48.1456 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 619ea0ce-c5cb-377f-984d-dffc0da53adf | -15.50588 | -46.85376 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63791789-fc53-317d-a91b-d107c42c36a0 | -15.5903 | -52.51735 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78cc735b-b25d-390b-9d26-91256bba525c | -15.58633 | -52.50557 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 55b577d0-64cc-39e6-aa79-689ac455afa5 | -13.35015 | -47.19956 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e75210d6-c080-366f-8630-76c5cc3d19f6 | -14.3342 | -47.69345 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7484b873-6d59-3320-871b-00b515de9703 | -13.33314 | -47.1874 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4aaf3785-41d5-39bd-9590-51cd508f0e11 | -14.65395 | -48.33431 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18d2b740-7ed2-343a-a89e-ac3fb6303229 | -15.54143 | -46.83352 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22ad0a3a-7db7-39c9-81cf-72e09cd37b0e | -15.5458 | -46.83437 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd6d4157-9e81-35c3-8fa8-d20ef53c650a | -12.93774 | -51.01574 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cc20b8d-80e3-32bc-8273-cda7fb17b0f1 | -13.07818 | -47.91595 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f687997e-6595-3d10-9ad5-ffca1b571a62 | -16.00648 | -50.85229 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92526a84-4fdf-37c1-9096-2db1a2523953 | -13.30551 | -47.62507 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fbd5d65-9d9c-3113-b9f4-ca8b05b38ef3 | -11.07516 | -47.91229 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82aaa077-2587-326d-8c46-219b5800aca3 | -11.83425 | -45.07508 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f13c3877-0dc5-30d6-8c1c-9ad716611162 | -15.74845 | -46.26318 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d9e8692-30f9-3419-b731-e09773fa8cdc | -12.13509 | -50.92968 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f2a1ebfd-b2f7-3620-a70e-35edab2eca6d | -11.8206 | -45.07948 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec54aec5-66d4-3150-8916-5a358cc14183 | -14.41903 | -46.18027 | 2025-10-05 03:55:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60eda72c-d574-3058-bb11-a2da82f7fdde | -13.33236 | -47.19157 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c292827-93c7-304f-9da8-dc92e7a924f2 | -13.49413 | -47.28159 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94f4b435-bd4b-3f19-9311-052249de7c42 | -14.91664 | -46.85386 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 689140b0-30ad-3f9e-8f5e-bc1dab529571 | -11.45554 | -51.51487 | 2025-10-05 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b557190-3960-3873-959e-be9051f73968 | -12.29687 | -45.35767 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4e0bb08-001e-3e98-9bc9-e3ed7e102830 | -15.29573 | -46.30781 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d798dae-481f-3ef8-b4e5-5ea8081631bd | -13.83816 | -47.91459 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72091da3-0e90-3bd7-bf10-fe10bc9d0fce | -13.30447 | -47.63052 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1110d5a0-4b75-3f02-8a17-a9991e95be59 | -11.07175 | -47.87495 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd7dac80-b629-325a-9013-c0928e7dcb43 | -12.55614 | -48.1617 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae0554a1-94d4-3ced-b851-83dc31a92b72 | -11.85342 | -44.94378 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a169715-b72c-321f-8ba6-38578194cf15 | -13.74957 | -47.96909 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9ab01ad-8e64-358e-9f42-0247f527f3cc | -15.96232 | -43.32721 | 2025-10-05 03:55:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a89ea36-cdea-30da-9b88-e6919c5cf79e | -15.39177 | -47.94961 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b0d7430c-51ce-3c96-881a-550785a33887 | -11.8254 | -45.07663 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fa576e9b-c203-3321-baf6-a91b6346d69a | -15.22661 | -49.29037 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a382a6a2-d8b5-3b5d-9942-b91d78741e07 | -12.12021 | -50.9052 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 80730e9c-6641-3dec-9cdc-a60696d73b9f | -11.48429 | -45.03928 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4eb905e5-66e6-3e05-a30f-c3d42760ce81 | -13.31504 | -48.08138 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 393999f1-d0bb-39c0-b3d4-96c075c3d50d | -13.47553 | -47.22705 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2802268e-c33c-3954-90cb-1b2559b96fc4 | -15.73928 | -46.26578 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92d802ec-6b41-3309-9537-33a64f2567e2 | -16.3444 | -51.47238 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d9e8bcf-dc5a-333c-8129-87f4165fb0ec | -13.26717 | -43.60431 | 2025-10-05 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83c85e40-a147-3771-9094-95417b928f43 | -15.37862 | -47.94164 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 283a4444-bac5-3205-802d-415c79fcaf23 | -12.45392 | -45.52513 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 644fa44c-668e-3418-9d32-fa0f7b13d6a3 | -13.55831 | -44.09694 | 2025-10-05 03:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71f25d4c-7983-3f58-bae5-13ff41d613d8 | -13.30541 | -47.78251 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b789e2d-8081-3ef1-a5f3-15d8ca9c1171 | -11.8678 | -44.95852 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| beb7490b-b643-304e-87ff-9fbc140e7d85 | -15.29558 | -47.32948 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40c900e5-ff34-395e-aefc-ffc20e59f433 | -13.15045 | -47.97233 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91510466-a7fb-369e-bf98-715e32a0c736 | -15.93096 | -48.99403 | 2025-10-05 03:55:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7378c167-100d-3a1c-b0c3-09764279194b | -12.77996 | -48.82449 | 2025-10-05 03:55:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95309237-e3c3-3f3c-b5ae-2ac2da1d65e7 | -11.11765 | -49.86524 | 2025-10-05 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e2c12b8-57db-367d-84e2-3dd3bc97af8d | -13.57805 | -48.16717 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 508eb14f-4c30-3df3-a38a-cae4c3f3532a | -11.90653 | -46.23576 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dd12512-a649-3b9e-97cf-3a3ba02fa132 | -13.03622 | -44.8816 | 2025-10-05 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc94c117-aefb-377d-befd-d6a65e7fb196 | -14.64732 | -48.3321 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 817d0c02-03d7-3a10-a821-a38531ee9fcc | -12.1151 | -50.89926 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41e8103c-7912-3ed8-835a-6e353c4953c9 | -13.3005 | -47.78197 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad206bde-7e3f-3a4b-99b3-a4ec0901cff0 | -15.58222 | -52.49447 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 194f6c44-81e7-3265-bd79-7341568b2d70 | -15.91184 | -48.82937 | 2025-10-05 03:55:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a832a083-280d-3760-9dcc-00e281371a20 | -11.45138 | -49.71867 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d830b129-7610-349c-a1a6-464e8cd7ecde | -16.06873 | -51.0904 | 2025-10-05 03:55:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ab08f3e-991d-3d48-b8d7-3aa6c3c5253b | -11.79223 | -45.01199 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 766a1243-f922-37e5-9f79-006c678f5159 | -12.88707 | -47.3037 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab2a66ba-fc36-3e9a-9b7e-eafc53e71d56 | -12.91439 | -47.31476 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0c2ae8d-7668-3da2-9b61-70aff6d602f7 | -13.95672 | -43.06699 | 2025-10-05 03:55:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9e92427f-015c-374a-96e4-a2187e6f6f92 | -11.79218 | -47.91854 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dad2469-54aa-3c2e-83c9-af4c36707815 | -15.20294 | -47.20073 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6852dca-6a1b-3a83-ac3c-e2c78899967a | -16.34706 | -51.45992 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 255f7fe8-8da0-3b17-b174-9d752dcb3960 | -14.66127 | -48.33881 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 93dca287-3c2b-3739-9c80-f5500d6ba10f | -15.56862 | -52.47889 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c8cb143-fd35-3499-8d1a-3baad9ff641e | -14.93144 | -46.92277 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03a89d6b-bc4f-3a9f-97b8-4f82e3003ee4 | -11.81782 | -45.07106 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2184ac82-702f-3c15-9a7f-5de21c69dee5 | -12.08122 | -45.15017 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81f43a5b-9546-3fd4-b4ab-ab208884797c | -15.29008 | -47.33379 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 391a56ec-c7c7-3a18-a431-7d3908b157e9 | -15.54665 | -46.85395 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 225f7ee4-300d-35d9-8d31-80417fdf2470 | -13.12291 | -47.98288 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 88de76d8-ea6b-35e6-8bc8-db191aed2991 | -11.67185 | -43.89701 | 2025-10-05 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5faaa207-89b9-3114-b8d1-fcb1e433a7a8 | -16.38828 | -52.15308 | 2025-10-05 03:55:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 620c7a25-d12c-3eec-ba25-c686183611f6 | -15.76424 | -46.27174 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9183db8d-9673-3d05-90f1-14b5079d51cf | -11.93216 | -46.43674 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca9ec43c-158e-3883-ba59-12730fe34c1c | -11.09828 | -49.87026 | 2025-10-05 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b42b483b-d694-307d-b61c-3f20664215ef | -13.28393 | -47.60818 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f3b20bae-ebe6-3ecb-9a9a-8490914fe068 | -13.35579 | -48.06038 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 524edceb-e9ae-3c93-9a30-95a19dc539ab | -13.27152 | -47.59733 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4ad6415f-9040-3299-9c5d-f17cc84626fc | -11.88913 | -44.98224 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a0392bf-4ea9-37e8-9882-f05bbf66e45c | -10.45516 | -47.80889 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3896a4ca-356f-301d-afd2-fa0114255faa | -13.29695 | -48.09595 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c92bbf5b-7610-3e58-987a-e9446cde6737 | -15.54451 | -46.81724 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5504f5cd-06f2-32ab-9d95-b1f1b97d9bab | -11.24468 | -47.78156 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c123f1e-9b5e-3baf-b292-ea0ae924e193 | -11.80638 | -46.84777 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3323dc89-0812-3d85-9620-8c8df83121ab | -14.67986 | -48.29437 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README66.md)
