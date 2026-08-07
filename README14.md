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
| f8469d4d-f7fb-3125-9143-e3722f1bd587 | -6.94713 | -59.52067 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a232c46-8931-383b-8610-fff8360eeeec | -6.93689 | -52.78231 | 2026-08-07 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf58496f-3b6f-3b50-90dd-926be2bbb1d4 | -6.91485 | -42.42223 | 2026-08-07 04:44:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 189185b5-7b3f-3278-b8c4-e0354d322161 | -6.72273 | -58.9338 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f027521-4ca1-39ae-916e-4d7b9244d85c | -6.91543 | -42.41835 | 2026-08-07 04:44:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 955e0ffe-d3b0-32d2-91e4-650dd39fef63 | -10.48787 | -46.69238 | 2026-08-07 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0ef57a17-2216-3e68-bcca-74ce3535c092 | -6.9533 | -59.52168 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44d2485b-0125-36f2-a2db-e1f42772657c | -6.61063 | -56.3452 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9d9036c-2914-3529-8d48-f01f0449f050 | -6.27524 | -44.56393 | 2026-08-07 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b3ec6c9-c3cb-3bf9-a53e-52deeb66325a | -6.10156 | -55.8152 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e48cc78-4e70-352a-bc70-5fc925ed4b62 | -6.86376 | -46.00901 | 2026-08-07 04:44:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 611deb55-8b6f-3be5-9cb6-9e6ab2f43af8 | -6.13461 | -47.18001 | 2026-08-07 04:44:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1136b9dc-677d-3a5e-82b9-33a4ef70b388 | -4.99109 | -37.09826 | 2026-08-07 04:44:00 | NPP-375D | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8758378a-0cf8-34c9-b12d-64c222d16425 | -6.53366 | -56.54581 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76dff092-a5bd-3496-b1f1-435270474c46 | -8.55499 | -45.37202 | 2026-08-07 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25b54755-5f8e-3dc4-957e-9241ec939323 | -6.54868 | -56.2585 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f584dce-7832-34c7-96ff-718ca5063a4e | -4.93569 | -41.98292 | 2026-08-07 04:44:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e674902-9678-3fdb-96c3-0cf9bf583d99 | -9.64232 | -47.8085 | 2026-08-07 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a1cd480-7db3-3926-aa81-3a4dfb1bbda1 | -6.64208 | -56.42285 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a35abb6-6006-3c66-8805-2365d9e26fed | -4.26842 | -48.19308 | 2026-08-07 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1fc75514-9642-3064-a248-324f0325bb84 | -6.62104 | -56.37493 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b32840e6-8a0c-3b62-99c3-2f222a107e72 | -4.27508 | -48.19414 | 2026-08-07 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54cdb82a-acf1-33a4-b4e3-173962a01583 | -6.55366 | -55.17636 | 2026-08-07 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21bca608-5839-3566-839b-9688633d8e63 | -3.59301 | -49.07307 | 2026-08-07 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62c8ff6c-25a6-3b47-9363-f5a239545635 | -4.84753 | -45.21923 | 2026-08-07 04:44:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4a304199-15cd-3c73-b8ed-a5321acb71cb | -6.07047 | -49.48937 | 2026-08-07 04:44:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9f8d32d7-a209-30f1-aa4d-0ac63f89ec5c | -2.69235 | -48.20926 | 2026-08-07 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f62892c-b904-3b9f-aa90-3981b0caef33 | -6.35974 | -45.46337 | 2026-08-07 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b51a1db2-44c0-3f86-8a83-3dc32e4bf1ef | -6.87779 | -56.51348 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd96db59-2282-321c-9b1a-ca89148ab949 | -6.47713 | -42.23839 | 2026-08-07 04:44:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 7773ef47-5be1-3bf7-b2f9-e661c6b908e7 | -6.8603 | -46.00849 | 2026-08-07 04:44:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d7c3912e-fb7f-36bd-852f-0669b34c3da9 | -6.52856 | -56.54488 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7128c931-f7cb-36f3-b4a9-80076fbb604c | -10.49435 | -46.64989 | 2026-08-07 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6935ae0-1490-3e83-a4e4-c4c432fa1d71 | -6.89931 | -42.43963 | 2026-08-07 04:44:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4884c209-8fed-331b-b19a-05aef5b1d01b | -6.35912 | -45.46735 | 2026-08-07 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03d7c449-8488-3564-8f51-1cb28051ce32 | -6.69869 | -40.46838 | 2026-08-07 04:44:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 82d756fd-d598-3c0f-8db6-85640b310a5e | -6.64712 | -56.42379 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f51f132-86a5-3c11-8040-13083909098d | -7.03278 | -56.51247 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f608ce4-2605-3cd2-a6f5-0814c71406bb | -7.08848 | -46.54512 | 2026-08-07 04:44:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e14ccfe-2579-39e8-820a-920ab0faf4c5 | -4.84403 | -45.21869 | 2026-08-07 04:44:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7dc33af5-00c7-334b-8e10-0bd32e87e443 | -6.53311 | -56.54887 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6a0a59c-c469-3dc4-b037-da633374e65e | -6.71999 | -58.93316 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e7ad645-e5dd-3188-9f20-937de24c7935 | -5.02853 | -56.19341 | 2026-08-07 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09847385-24a1-3eb3-bf75-facba70b3edf | -6.60399 | -56.35358 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| deef4c40-9415-39b4-9c79-aa1c2d382a87 | -5.37341 | -49.17511 | 2026-08-07 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4252cdf1-fe6c-38f3-93a8-59b93a09e9fc | -6.6101 | -56.34824 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72c934bc-b23f-3bfe-8e8e-8bfc875f9be5 | -7.0333 | -56.50943 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3cbd958-fd1b-312f-802c-5964a32ec2e2 | -6.53605 | -54.92642 | 2026-08-07 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93af7366-764f-30cc-85a0-e9f0eb71264c | -6.89508 | -42.439 | 2026-08-07 04:44:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 211157ae-bb69-3975-a1e6-08ae17c63e88 | -6.916 | -42.41448 | 2026-08-07 04:44:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 05a15462-db5b-3e23-8c26-00b21d63d14e | -6.53874 | -56.54681 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 726487d2-d3e1-3e57-b48e-79ad09655662 | -8.07881 | -45.57893 | 2026-08-07 04:44:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23e88807-c844-3ebe-9102-a3c8d85d4949 | -6.91658 | -42.41058 | 2026-08-07 04:44:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 26bf6e81-b47c-3426-a990-f5bcae4c3e51 | -6.64157 | -56.42566 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89362e64-df53-3152-92ae-8da8dda7298e | -6.63924 | -56.40956 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 721b35c6-fe86-39d9-98d5-ee803fdbee85 | -7.09188 | -46.54566 | 2026-08-07 04:44:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03fda5a3-cddc-307a-9822-786a79f7b3df | -3.0584 | -48.7481 | 2026-08-07 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fc4577d-18a9-38d1-b209-741cad6ced22 | -6.06649 | -49.49245 | 2026-08-07 04:44:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab308e5d-be53-3a0a-be06-50ccc218ece4 | -6.98611 | -42.91127 | 2026-08-07 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 44ff4a29-1dfb-3023-abbc-06cd830674a7 | -4.45785 | -47.91721 | 2026-08-07 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9d779b8d-2abd-34c9-94a7-d8e74adc17cc | -6.41792 | -55.79238 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36b3fb49-b393-3f9d-a63f-726e2fef41bb | -6.13182 | -47.17599 | 2026-08-07 04:44:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93d3f6a9-db87-37f8-a3a5-4403f83c7cf1 | -8.65915 | -45.85836 | 2026-08-07 04:44:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36826e66-99a7-3a6a-a8d9-d61adbfb0aab | -6.48372 | -42.22318 | 2026-08-07 04:44:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| da02554a-ee12-3981-8ea2-c789520272d1 | -8.33899 | -46.39894 | 2026-08-07 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb86bff5-9714-3752-aa0c-012cc67e55ea | -6.13849 | -47.17703 | 2026-08-07 04:44:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 20c8d7e7-e72e-3d72-9e0a-cba30be8b446 | -6.86147 | -46.00086 | 2026-08-07 04:44:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b7cc74e-9c78-3539-a666-00e6cee4f753 | -6.13794 | -47.18053 | 2026-08-07 04:44:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f00ad93b-3a4a-3398-b72f-51da90a51507 | -7.75702 | -45.03048 | 2026-08-07 04:44:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8af01207-6893-3ff3-aeaa-5b2329fd4d97 | -4.84463 | -45.21481 | 2026-08-07 04:44:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c89ca831-765f-3670-a28a-069e4b63ab3e | -3.12256 | -48.58547 | 2026-08-07 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77d77b24-f937-3053-a99a-5846e4e0e8e4 | -8.66624 | -45.85936 | 2026-08-07 04:44:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4097cae1-f2cf-3708-adfd-46ab175da4c2 | -8.5367 | -49.55676 | 2026-08-07 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ff2a509-b9b0-3a6b-9dff-6b0b302128ac | -6.62204 | -56.36916 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f53e526-baf6-3862-b21a-f9d7ac310b03 | -6.72355 | -58.92937 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c4bcf03-8816-3f23-be8b-4db99a4c8518 | -6.7086 | -58.96253 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5c5e6539-ff54-3a26-b645-fb780e32113c | -6.62613 | -56.37551 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fbadf8e-c664-3565-b0f0-ae0bc2983e7b | -6.91392 | -41.94556 | 2026-08-07 04:44:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e6fa20cc-f72b-36c3-b22a-ca3fc023e00a | -6.86435 | -46.00517 | 2026-08-07 04:44:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46e8650b-9192-3ed5-bf58-007d15148500 | -8.08238 | -45.57947 | 2026-08-07 04:44:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef3f2ab6-7217-3114-9bdd-beae5b8522ca | -2.88575 | -48.07463 | 2026-08-07 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32d55be4-abea-33b3-9018-f1c156183e37 | -6.91062 | -42.42159 | 2026-08-07 04:44:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3a27b19b-2e41-3fce-98b4-b675f8f7e730 | -6.10298 | -55.81625 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9bc77d5e-b094-35e9-9e56-214c782a65c9 | -4.27231 | -48.19014 | 2026-08-07 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad850666-cc12-3a14-a20f-8d6510f689f3 | -3.06179 | -48.74864 | 2026-08-07 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31019d99-06e6-38d1-b149-c91751c3ddca | -6.53821 | -56.54983 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a4a4c3e-9eed-3c9b-873c-cb5c6425d77e | -4.26898 | -48.18961 | 2026-08-07 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52bf72b5-3384-3bbc-ad7f-8b819dc2e17b | -6.53256 | -56.55198 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc0f5703-99bc-354c-a30f-cec30aa47012 | -4.26454 | -48.19603 | 2026-08-07 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5b4bd16c-fcf4-3594-940b-49aca87d2694 | -3.82002 | -50.63288 | 2026-08-07 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| badac621-46ff-3dfb-93a1-a90cd842ff5e | -6.70938 | -58.95816 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 73f6e2af-d1e0-329b-955f-41cc39909779 | -4.46172 | -47.91428 | 2026-08-07 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0af604e8-3cf3-3347-97f2-acf966018162 | -7.03654 | -56.51053 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d84c714e-4b2e-31a5-ba2d-82e8b9807816 | -6.6553 | -56.40707 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fd73b75b-2f5c-36d7-8078-133013d6ee2e | -4.36934 | -47.77234 | 2026-08-07 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c02843a4-8ceb-3567-b877-bb5e20b08f36 | -6.60451 | -56.35059 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83a0fd63-a70f-37a7-b79e-bc4820c11842 | -8.55561 | -45.36784 | 2026-08-07 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4c5b52b-1bf0-36f1-b9ab-9e61a29bb1c4 | -6.86232 | -56.57138 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c8f8bc2-6073-3356-ae33-49b6501c343f | -4.48675 | -49.82352 | 2026-08-07 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 832d6e2b-870d-3cd0-a7fd-f58d1f6057a1 | -7.71727 | -46.22115 | 2026-08-07 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README15.md)
