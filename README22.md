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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4703bf2-572a-34a7-8b00-1adbf15d6778 | -23.73502 | -54.94567 | 2025-09-01 03:47:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| dfb1b1c3-220a-3760-837f-8019bcfafd1a | -14.78648 | -46.72106 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f23bbb33-f233-3f50-b0b8-8f556c0c6da1 | -14.8258 | -46.73718 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74e61694-69fc-3778-bd89-3a81794a8bda | -14.8493 | -47.09155 | 2025-09-01 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a94e305c-83a7-3a16-9f1b-645b45e2a180 | -14.74496 | -46.76319 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b7e911d-34f1-3dde-8db2-23b6161d50c2 | -15.69686 | -48.89212 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1107994-eae3-37de-82cc-69f7c9ba2684 | -14.8273 | -46.73748 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14d027a3-295c-39a7-b48d-d5b473f641f7 | -15.70134 | -48.90025 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6c6b780a-d081-340d-88b8-4c35253599b7 | -15.59878 | -48.33382 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 59e48ca5-f02f-343a-ad3d-fbb8a8306551 | -21.09246 | -48.23891 | 2025-09-01 03:47:00 | NOAA-21 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e66e9370-ce43-30b1-91d9-3b8023f7c6b5 | -19.78125 | -44.34174 | 2025-09-01 03:47:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16a5d9e6-d3ce-341b-b4c8-be10cd182acf | -15.73266 | -48.95797 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ba0a2aa-f6ac-35ba-aa3b-f8ea12af2df6 | -15.72736 | -48.89497 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aecc41fb-0642-3e11-91af-59fc119aec7d | -15.71557 | -49.00898 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1b796f52-729d-31d2-9df7-2cfd1b1165a7 | -18.66469 | -52.59694 | 2025-09-01 03:47:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ec937093-08f4-3a0d-8b80-db8739c87cde | -15.69736 | -48.90747 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4385eca8-635c-3a42-97b9-fdf049a2dd11 | -16.08221 | -43.61961 | 2025-09-01 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50781815-681f-30e3-8cbf-60706474fadb | -15.72071 | -48.897 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 047166ff-5466-3534-9024-855abbfdfae4 | -18.91368 | -47.20358 | 2025-09-01 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fee51353-280f-328b-90dd-c2d1450a5864 | -14.78702 | -46.71835 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 97b58329-278b-3fa2-9267-5e0b904d9e28 | -15.69509 | -48.95842 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4133b870-a26f-32d1-a3a0-1e1d1dbee27c | -14.74654 | -46.75534 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9163219b-585c-3b30-9b23-bd1a5fa71a60 | -15.69634 | -48.9124 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e715f98b-7448-3b10-9ad9-3606593e633c | -19.83974 | -44.99453 | 2025-09-01 03:47:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 82d5d88a-2169-3481-9109-a7743bec74f0 | -15.588 | -48.32839 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a8784e12-1539-326c-a6a9-50ff1eada819 | -20.81005 | -45.62572 | 2025-09-01 03:47:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a0bc1c5-e211-3dab-801b-e324f0e1b028 | -15.32572 | -46.11288 | 2025-09-01 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8f79185-8e40-3ca7-a40c-aa997b664e36 | -15.69005 | -48.9528 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2e119fc6-1895-3ca0-b42a-bb54981f7ac3 | -14.74445 | -46.73825 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a91445c-02ae-3976-bcca-75b13662e0c6 | -14.85048 | -47.09359 | 2025-09-01 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 07f1408e-0f64-3e00-81af-382e824352f2 | -15.66359 | -47.67357 | 2025-09-01 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ddfa798-e661-312f-920c-e3e1adae232b | -14.74181 | -46.75136 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b423db63-730d-3638-8151-6d59c19e7d34 | -15.70232 | -48.89568 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5064dbc8-c82c-3b18-bbf7-2ddae60e2d50 | -14.74248 | -46.74804 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82e201d4-84a3-3b78-a27a-8193a40644e8 | -15.59012 | -48.31846 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 529cead0-680d-3796-a939-cd2bfcd5c4d0 | -15.70337 | -48.91981 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e27eb175-887b-35b3-88bb-f05994091d82 | -14.74874 | -46.77188 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2a338ba-6865-3e38-aed0-85f75df2f8f0 | -19.97232 | -50.22096 | 2025-09-01 03:47:00 | NOAA-21 | INDIAPORÃ | SÃO PAULO | Brasil | 3520707 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8473e4c2-9d53-3ab0-b2ef-1994197bbf1b | -18.66429 | -52.59284 | 2025-09-01 03:47:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 75680d93-7366-3313-8fdd-e5dc9318bf21 | -15.70112 | -48.95945 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 2187d469-57ee-3d61-bb7b-428ba770a567 | -18.91433 | -47.20045 | 2025-09-01 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fc9f65df-cd03-3c32-9ee6-1705378b6d3a | -15.69589 | -48.89663 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78fef29c-63d3-32c6-9d90-7933424d00c7 | -21.81735 | -46.489 | 2025-09-01 03:47:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d5b8354e-ff72-3077-a688-66a6c077cca9 | -21.87335 | -46.75117 | 2025-09-01 03:47:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 470277d3-9a03-31e4-a5ae-b58072e1c4cc | -15.71785 | -48.99825 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5cfe8d2c-64eb-3679-a07b-a163372e4f99 | -13.68731 | -50.76493 | 2025-09-01 03:47:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ce8aca9e-979e-32fa-9d3f-f5a9708650cd | -15.59567 | -48.34904 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 94c4e3f4-e2b7-3c6e-9bde-966ec93906df | -20.40759 | -46.40807 | 2025-09-01 03:47:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc5fb029-b1ba-3453-8c2c-59f29068832d | -14.74508 | -46.73512 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02c06a28-aa10-3ad2-a8f5-a59b1f094b80 | -14.84974 | -47.09717 | 2025-09-01 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fc7e3b6e-3446-3b0a-86fb-12c4aaa925d8 | -19.48309 | -46.58378 | 2025-09-01 03:47:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7567198-be7c-361d-92d4-3ae0ebfa5c00 | -15.69813 | -48.91518 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ea65837a-3a5d-3c50-a566-91c8fa923f87 | -15.08245 | -48.12166 | 2025-09-01 03:47:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2690be72-b0b9-37e2-a8f9-2843965d4782 | -20.40657 | -46.41316 | 2025-09-01 03:47:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3ec72afe-14e7-3463-9ff9-17c24c9c8e28 | -15.32689 | -46.10694 | 2025-09-01 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 791b4394-5b69-3edd-9821-41e5b9997a39 | -21.08358 | -48.22993 | 2025-09-01 03:47:00 | NOAA-21 | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0f96c9a-f43c-361b-b7b6-237e80b4433a | -26.32549 | -52.7067 | 2025-09-01 03:47:00 | NOAA-21 | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 2f79e8f1-4c00-3e69-ae19-47234165b86a | -15.59017 | -48.34646 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 215263fc-3f5c-3beb-a714-28c8885f4f15 | -20.40852 | -46.40349 | 2025-09-01 03:47:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e26949f7-f9c1-36a7-9679-3fc81b9e47fd | -15.59356 | -48.35895 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f560be1f-45d0-3376-87f0-37d444b7450d | -18.50374 | -46.99936 | 2025-09-01 03:47:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8405f8a-31a1-3f00-a945-2b6bed19fc00 | -14.76763 | -46.76033 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6350538b-93a9-3c8e-9138-3015b651846f | -19.48182 | -46.58997 | 2025-09-01 03:47:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1027da46-a35a-317b-b28b-5257e3b91329 | -18.12212 | -48.53723 | 2025-09-01 03:47:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 619d87fc-59cb-3bab-8fc2-55c351b2be42 | -16.08246 | -43.62064 | 2025-09-01 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06c9fd2e-7310-3d5f-92c9-d186dbf1f48c | -14.7557 | -46.76476 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b932539c-f1f8-3ab1-b4b0-d44a70db3118 | -16.07721 | -43.62286 | 2025-09-01 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0c4d9a2-c257-3475-b669-1c63b35cf71a | -21.08944 | -48.22787 | 2025-09-01 03:47:00 | NOAA-21 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 10805b0d-3acc-392c-a124-f4d695db612b | -26.32691 | -52.70107 | 2025-09-01 03:47:00 | NOAA-21 | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 13be09b3-f3bf-3d17-a1ca-4c5cd8fc1190 | -16.15611 | -49.6333 | 2025-09-01 03:47:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 787e641a-9ade-391c-adb3-8850c1f99617 | -14.84716 | -47.10234 | 2025-09-01 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c3a5bd9d-8dc1-3c09-971e-87f7fa7517fd | -15.6888 | -48.95861 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c6c6c2b-b3e9-30d6-ab16-9992e0d583c2 | -15.32747 | -46.104 | 2025-09-01 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb875f8c-040e-3e55-a1c9-54d63aeab680 | -15.69172 | -48.93464 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9d5cdc82-6922-3115-bc44-c1a81878c19c | -15.59774 | -48.33923 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a404a48d-b55b-3bbb-93d8-7e6d26f80860 | -19.34666 | -44.00042 | 2025-09-01 03:47:00 | NOAA-21 | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04a9abec-7e55-36a0-9d4f-845fc8a908a4 | -16.00187 | -43.42094 | 2025-09-01 03:47:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 801cadd7-1824-3412-9a85-38eed1bade88 | -14.84317 | -47.09402 | 2025-09-01 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ebf94bbb-786a-3437-8b84-904cd7dd0557 | -16.15964 | -40.34405 | 2025-09-01 03:47:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b046edfb-f285-3b34-bad4-885601f2099c | -18.66316 | -52.60342 | 2025-09-01 03:47:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9a0d88c8-179c-35ed-976b-3a4a680dc58d | -16.00081 | -43.42157 | 2025-09-01 03:47:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 228929e6-264c-30ed-b0a2-5e33f7f41d48 | -14.82254 | -46.72613 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6db0376f-edfb-34b4-a4a7-0a8a3ff0544f | -20.41135 | -46.41359 | 2025-09-01 03:47:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f47097b6-855b-3c3d-b4e1-662f2f408816 | -14.85329 | -47.09986 | 2025-09-01 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 116ee231-bfaa-3123-a735-5843c1b108c1 | -14.79363 | -46.74059 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c01d618-9b4d-3bf1-a43c-2b3c9d04f7fc | -15.72684 | -48.95598 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27b7f3a0-934c-3092-a950-477514f3fd69 | -18.11567 | -48.54018 | 2025-09-01 03:47:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 047ab5df-e408-3ac7-b0e5-b1d39d037972 | -14.81875 | -46.72492 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9da09415-1a6f-3acb-aa37-a0d826859db6 | -14.77371 | -46.75757 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e770665-6b36-34ba-ba1c-34c9f8fed328 | -19.85868 | -45.01284 | 2025-09-01 03:47:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f841fc7-d1bf-3cc3-a9c0-588b38c21c4e | -14.78285 | -46.71162 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 318ac807-0399-3317-a6cc-59e6b00f34ae | -16.1146 | -46.82273 | 2025-09-01 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dd0b42b-d7fc-3d43-b6bb-e31f4a7994db | -17.72747 | -42.89378 | 2025-09-01 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8725f435-310b-388c-8ad0-0d086c233234 | -14.79303 | -46.7436 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a378bdff-b1ce-3531-be85-457404ef9e88 | -17.72365 | -44.38352 | 2025-09-01 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1396f430-60c2-3cb8-9946-3d94a17e35c8 | -14.75515 | -46.73997 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05e28d8a-b885-3667-90b3-4ceeb879e338 | -15.69836 | -48.90266 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0c18f8e2-bd40-31c7-9589-401b33450c2c | -15.70118 | -48.88908 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b266b3f-1b79-3455-a2eb-01e5fa647eaa | -15.60246 | -48.34542 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 776c1198-d3f6-316e-9fc5-7880bd46162e | -14.80009 | -46.73577 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README23.md)
