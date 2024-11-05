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
| bb752de8-1beb-370f-8475-07a97fbc15ae | -5.39877 | -42.75082 | 2024-11-05 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e84c6470-3aae-32dc-abf3-932fb5062fbd | -8.49303 | -42.09413 | 2024-11-05 04:08:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 12894289-0688-3651-842d-be49f8a9dea9 | -3.08662 | -54.50284 | 2024-11-05 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2c2dd6af-9b22-3c62-a48c-093919dbe3ca | -4.79622 | -43.7797 | 2024-11-05 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 59a3bcdb-1024-3e60-9526-53ee5a227a88 | -5.37584 | -46.44939 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad1a485e-7d2c-3c3e-9833-893c4ca7b194 | -6.17875 | -43.58921 | 2024-11-05 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3abae60d-e332-33e8-92a7-f49b2e76ee81 | -2.78642 | -48.72458 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8af800e1-5fbf-35b7-bbf2-3728d8878c34 | -2.24306 | -46.4723 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 714252fc-b9b3-3a52-ae40-282e27bf2fd5 | -1.93301 | -46.45785 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07782204-0d40-3054-b906-5d13b4e42e98 | -5.50463 | -47.60143 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03c17fd5-c6c4-31f0-8dc8-45783d1f624d | -6.09928 | -43.95584 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 391c0d8e-ee2f-3942-9480-594d354a19e5 | -4.38685 | -43.10839 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afa45f53-6e43-32a4-962c-02cdf3af4082 | -5.57936 | -42.78975 | 2024-11-05 04:08:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0ed24bd1-66c3-36c6-898d-31c1f2a7c4f6 | -2.71874 | -46.67263 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 524b3503-a98f-3490-8a82-759d54d877e7 | -3.6776 | -43.67462 | 2024-11-05 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 579c8efc-7121-319f-9479-1ac30e335d9d | -3.21297 | -53.10783 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4c5f9488-0b73-3bb9-919f-193eae486646 | -4.38568 | -43.11583 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b50d8c6-37dc-3877-98c3-c8de5aa35218 | -3.43828 | -44.95671 | 2024-11-05 04:08:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25db563b-d0f3-3ba1-a0ff-aeb56af1f804 | -6.17582 | -43.95636 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 26b12225-f0be-3eb0-8d4d-8c47667999d7 | -6.93945 | -40.8386 | 2024-11-05 04:08:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 66f3167c-fede-387a-aa32-384699709ba6 | -4.74531 | -45.81993 | 2024-11-05 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4113a72-c11b-3db6-89c2-07a21607d2dd | -4.79559 | -43.78362 | 2024-11-05 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6d7f4b37-4cb3-3703-b2c7-8dfac3836c1e | -7.20819 | -39.35955 | 2024-11-05 04:08:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 14bb57f9-b918-31e8-93a4-871533b33eea | -8.32761 | -43.59275 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de2ed104-4ba0-33f2-9219-ea138039e55e | -6.84245 | -44.77486 | 2024-11-05 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46a3a7c6-16ab-3c2a-bf66-e6fc420fb705 | -6.10153 | -43.96413 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 86682b4e-c958-3f0a-95ca-97fc18170e1c | -3.04431 | -53.26896 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44550fc5-8545-3130-9275-6f31510c39b7 | -2.71377 | -47.73208 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fddf4f3-ca63-341b-aa6d-6f75780f34f1 | -2.2435 | -46.47309 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 852f8bb1-dbcd-39e3-b738-1c571874a1bf | -6.46755 | -42.23005 | 2024-11-05 04:08:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 897e8725-b8b1-30f8-8a3f-378bc58c5e82 | -3.75067 | -46.14483 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79879604-f629-3922-90aa-14f34b8f4e17 | -2.4643 | -50.22934 | 2024-11-05 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a920c26-8094-3a68-a1cc-21a1a64889f6 | -5.47116 | -42.82822 | 2024-11-05 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 079f798d-3524-35e4-87c5-3a8524ef328c | -2.2123 | -46.39533 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b63de6c-7dca-3d8c-954b-604c99af1058 | -3.55246 | -44.63459 | 2024-11-05 04:08:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bac9d177-22f5-34e9-8b0d-cca5027542f9 | -3.90244 | -46.4422 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7193563-c20c-3cb4-9d73-f5bc18f91e6a | -2.90035 | -48.59864 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cb539e2-292c-3efc-ba11-f9daad343a16 | -6.69704 | -37.47269 | 2024-11-05 04:08:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7e8eb603-e729-3f01-939c-a441ea79b633 | -4.53194 | -46.40067 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b5285cc-9904-3cad-8f5e-a0d644e9ecbc | -2.66427 | -48.56723 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8a034f6a-4844-3d70-a46b-cffd64fc9434 | -3.04337 | -53.27436 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ad4347f-5ca3-360c-bb72-08416ffac71a | -6.46701 | -42.23353 | 2024-11-05 04:08:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 81e88985-effc-3233-be55-0d254fc702ee | -3.08328 | -54.50621 | 2024-11-05 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0b7a1908-1a3c-3dcc-bc6e-ed36f628182a | -3.30519 | -47.01589 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e07ac1f-0c2b-3fad-9064-519528df4ab5 | -3.95908 | -45.83172 | 2024-11-05 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4e5fd0ad-15f2-3306-bc46-11f86aeee177 | -6.10502 | -43.96467 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3cb1df4a-ab34-3a6d-91b4-978eaba1ada7 | -2.8068 | -51.48825 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c0bee49-2a6e-39b5-9057-6edda1ae8d0d | -2.63605 | -48.02834 | 2024-11-05 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94af735c-d945-3439-bf9c-ffa5d83d1f88 | -5.11592 | -43.95731 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa6fdb8d-a99a-3360-82e9-cb8f5cdd0595 | -2.79571 | -51.48184 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce14ba1b-40dc-3d9a-bae3-9b42a1d0e272 | -4.8342 | -44.94578 | 2024-11-05 04:08:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6c550a6-2e63-3adb-8fcc-6efd6e9f014c | -3.11972 | -51.10812 | 2024-11-05 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e283d810-e1b0-311b-80f3-ccb77cb81d03 | -3.54986 | -47.401 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec04f035-094c-31cc-b907-fe17b09f3c7d | -8.49687 | -42.09118 | 2024-11-05 04:08:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f8904db0-6443-384b-8205-8be1461dd3d0 | -2.82427 | -48.46402 | 2024-11-05 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0347796e-ef39-32b7-913b-8e2f2c588b87 | -4.28428 | -48.64612 | 2024-11-05 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c33621da-e1a4-367b-ad1b-d883c158f6ac | -5.85599 | -39.42451 | 2024-11-05 04:08:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 39ad1e4d-f3e8-3630-b103-71736d84edcb | -6.48801 | -39.97138 | 2024-11-05 04:08:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 88883c6d-871a-363e-8804-c9321a11f3fc | -5.43249 | -42.64624 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a20cd195-dd8e-3582-918d-f58f9bc8ce80 | -3.17157 | -46.60726 | 2024-11-05 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d958938-2450-3d31-8c5a-8fc92f7ea000 | -6.32155 | -42.03242 | 2024-11-05 04:08:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f295d726-3bb9-3da3-9496-5b225e2f34c6 | -3.3198 | -40.03416 | 2024-11-05 04:08:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 39b1395c-bd9b-3521-982b-65216dacf9b4 | -5.3032 | -46.25315 | 2024-11-05 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 894f00e1-73aa-3b6a-9f1d-a172f43a12f7 | -3.75472 | -46.14554 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf3a3c3f-4650-394d-aee9-effe8b862341 | -4.05653 | -46.92988 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ddb061b0-4488-35da-a38a-b4d97942a506 | -3.0395 | -53.26625 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9d4e723-92c2-3b10-a72c-bf078ded45a2 | -6.52184 | -45.93731 | 2024-11-05 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec31d2f6-22f5-3889-8c54-71353b86438b | -4.21523 | -44.2883 | 2024-11-05 04:08:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82aea198-15d4-3518-9612-6d3c426c8bf6 | -3.78588 | -41.60688 | 2024-11-05 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 076d44b0-8fa5-34c2-abee-e6b48872acb0 | -3.21387 | -53.10242 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1bbe5c59-0ab1-3273-b376-9080bf744d62 | -8.32527 | -43.6074 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 25f7761a-6500-311e-bb05-10f3ac3cb0f3 | -5.06407 | -44.23693 | 2024-11-05 04:08:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 204222a1-3e53-3614-a97e-ba140b1af75b | -3.7925 | -41.60791 | 2024-11-05 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 45a78acf-16c9-3b77-8e4f-d3bd2b560573 | -7.41142 | -45.56424 | 2024-11-05 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65176ea8-6516-3589-98f8-0642bc53e61b | -4.1835 | -40.67204 | 2024-11-05 04:08:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 700183e6-8a1e-364b-a247-af9b2c81d11c | -4.89343 | -42.99393 | 2024-11-05 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ba8f16d-f8a9-3b4c-b992-967d53e5bdc4 | -4.56308 | -45.80177 | 2024-11-05 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5092737-4e9a-3c92-988a-11824a074cc7 | -2.64522 | -48.57338 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15eb942c-7eda-3e29-aa4d-3e43dbd8dbbb | -6.10913 | -43.96132 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bb385d79-019c-3cce-bf0e-fe2b83d4907c | -3.00919 | -45.85025 | 2024-11-05 04:08:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5f136d71-3719-37e7-a0d1-7b56d094afc8 | -5.9335 | -43.65211 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97c52d72-84d2-3b8d-8dc1-ff566f24cb6f | -4.87663 | -44.56584 | 2024-11-05 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd41357b-d295-3f55-b28f-6886cd3879d9 | -3.36072 | -44.2648 | 2024-11-05 04:08:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d3b7174-792d-37df-b3fb-f7b81f7a73d5 | -5.49637 | -41.67485 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c6a164a8-6d5d-313d-91a5-3d00442d41e7 | -3.84246 | -45.85671 | 2024-11-05 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 231fe103-6626-3734-8d8a-fa44c4760f61 | -5.50899 | -47.60211 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7244854-bb57-3591-bc99-ce687cdf1ebd | -3.56233 | -45.24622 | 2024-11-05 04:08:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05cc89a3-c19f-38d2-b628-087db4a24223 | -6.19371 | -39.23491 | 2024-11-05 04:08:00 | NOAA-21 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c6c6e9b-6300-338f-aa6d-31ba6df8901e | -4.41043 | -43.11539 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b95afb0c-2a20-3f3b-8e0e-3717d87cd3fe | -2.65985 | -48.57579 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5be75d0f-cbf5-383e-8c37-3f426166f644 | -2.09171 | -46.49871 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5d90b1e-3948-3a99-868c-297cef1af070 | -3.21373 | -53.10368 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6d1090b3-dd77-3147-8d7a-f1173c414b8f | -5.44655 | -48.21297 | 2024-11-05 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fae31a81-31dc-332a-9eed-b461b7de573c | -3.54907 | -47.37811 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fdeac52b-3cc9-3edc-9066-2f15d167eaa1 | -5.29182 | -46.24746 | 2024-11-05 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a689a70b-623b-350f-a814-ff95f704e940 | -4.86918 | -45.62318 | 2024-11-05 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27842533-068f-30b1-9fac-3946ede13b2e | -7.26631 | -38.94565 | 2024-11-05 04:08:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22036ff1-d586-3cfa-b789-d05669a31435 | -3.54392 | -47.38176 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f9055f6e-471f-3308-8d31-93fb84e8e9c8 | -4.79272 | -43.77914 | 2024-11-05 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df320930-f82f-3d33-be1f-b1c85e73dc2f | -5.33028 | -47.31573 | 2024-11-05 04:08:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README15.md)
