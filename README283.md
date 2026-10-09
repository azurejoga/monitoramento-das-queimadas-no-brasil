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

## Dados Diários - Página 283

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f3dd664-37df-377d-8a53-4faf35bd6ff9 | -3.19806 | -42.96209 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ea292166-0e84-3aae-bb68-6f3aad8cf0ab | -4.15815 | -44.33046 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 3f61be88-ddcd-3295-b14a-cd6249d8b3e5 | -3.89248 | -42.11435 | 2026-10-09 16:03:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 6b7ec3a2-0ff0-3cf6-a33e-423f792c7a91 | -4.24233 | -44.25262 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d24c070d-871d-36ec-b1ce-b6967b89899d | -4.32741 | -40.17455 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| cfa64672-ade8-399a-862b-046bf012ef74 | -4.35864 | -44.35841 | 2026-10-09 16:03:00 | NPP-375 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 56c1c1d1-8938-391e-b32d-15da3d6c16f5 | -3.18349 | -42.96426 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 831a71c8-ec74-356a-b566-5823e829eb6f | -3.15234 | -42.84083 | 2026-10-09 16:03:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 86a43c35-2f1b-33fc-bbfb-f31831016856 | -4.32667 | -41.24169 | 2026-10-09 16:03:00 | NPP-375 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d82c5ebf-76c1-3b66-8aff-9ac36c076d1a | -4.73424 | -45.27394 | 2026-10-09 16:03:00 | NPP-375 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| addc2cfa-3d57-397f-89fb-6badf3f037e6 | -4.24654 | -44.25537 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 544c369e-424c-3c4e-b631-1015a9f1395f | -4.50145 | -42.54293 | 2026-10-09 16:03:00 | NPP-375 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 4270c929-57f1-33bf-b72d-2aab15d71dbd | -3.97999 | -41.75492 | 2026-10-09 16:03:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| a8cf44aa-8ecc-3d98-8343-95012710745a | -3.52233 | -43.0314 | 2026-10-09 16:03:00 | NPP-375 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 272f7d67-ccf4-3c46-b4b5-84e87ff9ebee | -4.64796 | -44.84671 | 2026-10-09 16:03:00 | NPP-375 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d2f9c32d-be53-3666-adad-fba57b589bd3 | -3.83142 | -40.28968 | 2026-10-09 16:03:00 | NPP-375 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 4978c259-c267-3f27-a2bb-32a2859f56d3 | -4.19105 | -40.39594 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d999c222-aaf6-31cd-8296-5a829dbcf19f | -3.89082 | -41.59745 | 2026-10-09 16:03:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 864ca954-094e-3394-a17e-ba3a651d564d | -4.43469 | -45.24628 | 2026-10-09 16:03:00 | NPP-375 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 30.5 |
| a9495904-a08a-3cc2-a5a5-072d9ea85510 | -4.1537 | -44.33812 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 771005ea-2817-3e6d-8746-a9231e18d70f | -4.43526 | -45.25029 | 2026-10-09 16:03:00 | NPP-375 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 27.2 |
| e64bcdb2-9375-3f84-a6e7-c38f5a3a9635 | -3.8559 | -40.09289 | 2026-10-09 16:03:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 74bf1aac-3d14-3ccf-afef-d29f821b5b04 | -4.10592 | -42.50189 | 2026-10-09 16:03:00 | NPP-375 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| fad93cae-2188-3557-9633-02df3408a10d | -4.07555 | -44.15685 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| ea5214cf-bf13-3435-98cd-2940df35c779 | -4.06971 | -44.15421 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 3574ca55-b819-3354-a532-7ba3f9f72d75 | -4.07068 | -44.16092 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 19774f9e-8189-3ab3-a89c-6df7babc5b17 | -4.8309 | -45.83253 | 2026-10-09 16:03:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 13f12a50-af7d-3252-b1c3-edeb02c16d63 | -3.85655 | -44.15655 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1f10869e-7a1a-3f12-abe0-096ad3a27b98 | -4.03092 | -40.64909 | 2026-10-09 16:03:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 464c3b86-6276-3499-8734-06dd3d30e0b8 | -4.64479 | -44.84293 | 2026-10-09 16:03:00 | NPP-375 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 167bf5ff-872e-3704-bf10-1ed073ca55ab | -3.421 | -44.43697 | 2026-10-09 16:03:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a7102c8e-1eeb-3119-9149-ad3f27c91b5f | -4.31539 | -40.35137 | 2026-10-09 16:03:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bb21bddb-0a87-329d-b5b6-59416729d9d0 | -4.10115 | -42.50259 | 2026-10-09 16:03:00 | NPP-375 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 08defc24-c304-3e5a-b83a-5a7eebb63598 | -3.4616 | -43.09569 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ece6668f-0e29-35b1-af25-4812b1d3de41 | -3.48108 | -40.57294 | 2026-10-09 16:03:00 | NPP-375 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 24.1 |
| a7fa28e5-60c2-3fa2-a2c0-0b1bcdb94717 | -4.71832 | -45.74594 | 2026-10-09 16:03:00 | NPP-375 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 95c1c257-e55d-3397-b07a-9d2037955b36 | -4.24184 | -44.24919 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b26f71e5-72d8-3afb-969c-5b725da781a2 | -4.84897 | -46.09464 | 2026-10-09 16:03:00 | NPP-375 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b5dd5577-8baa-361f-a57b-29636d6bf411 | -4.14779 | -44.33543 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e1a1bec6-7695-3cdf-96f4-96f90f409977 | -4.24603 | -44.25196 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4049b417-c406-3e3e-b5c3-b58884a8d2d4 | -3.17072 | -39.58529 | 2026-10-09 16:03:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 560e2bca-6f79-3192-ad10-4bc52e503ece | -4.51215 | -43.63033 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e449689a-7bfa-3eca-8858-9838f27268ba | -4.49835 | -43.64503 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c7775bea-937b-3ec7-9a46-7ab55e33d6da | -3.5899 | -41.70889 | 2026-10-09 16:03:00 | NPP-375 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f1ab587c-fc2a-3668-8f68-78b52825d6aa | -4.02263 | -41.7623 | 2026-10-09 16:03:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 0960c923-a1d3-364e-8dfe-0b971f72c23e | -4.73484 | -45.27825 | 2026-10-09 16:03:00 | NPP-375 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a4ec99e-3eb5-309f-99ab-f454ffe3de73 | -4.0275 | -40.64973 | 2026-10-09 16:03:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2afd11de-18c5-30d2-968f-2fad2559aa5b | -3.82067 | -44.6008 | 2026-10-09 16:03:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b3cbd0fd-c51a-32de-99c5-ae7d6072a15f | -4.40317 | -43.12119 | 2026-10-09 16:03:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| d994f291-7e3d-3474-8da5-4cad538965d9 | -3.80026 | -44.61458 | 2026-10-09 16:03:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4eddf5c1-6cfb-380c-b977-999a438ab310 | -1.75092 | -48.70467 | 2026-10-09 16:03:00 | NPP-375 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ebe359da-6882-3132-80f1-f7c84c9cfa68 | -4.23669 | -40.55773 | 2026-10-09 16:03:00 | NPP-375 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a82521d3-733c-3216-bd80-3a6b1d5756fe | -4.15394 | -44.353 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3b145e96-f8ee-3abc-84c4-497acebeedec | -4.1642 | -42.95669 | 2026-10-09 16:03:00 | NPP-375 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| af64757e-26f2-3105-874d-04a511382ebf | -4.24063 | -44.25266 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fdea81c8-5cfd-3e16-8f00-230418499064 | -1.59359 | -48.35962 | 2026-10-09 16:03:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ed2f46cc-7310-376b-8c16-229656f73379 | -4.50695 | -43.63104 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6f2fca4c-6963-3776-be10-ef340576277c | -4.07604 | -44.16021 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 221e76e5-d075-38f6-ba3d-ab1556fae296 | -0.26097 | -49.78972 | 2026-10-09 16:03:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c236411d-583a-3bcd-812e-cf6d90ebdbc8 | -3.97895 | -41.7581 | 2026-10-09 16:03:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9a030591-d4cc-35ab-8a8f-f0fac7d81385 | -4.2374 | -44.25671 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 71a5daa5-ebf2-3666-a843-f14e6ee09a5a | -4.44106 | -45.2496 | 2026-10-09 16:03:00 | NPP-375 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 27.2 |
| d3327826-9b7e-3d64-b12b-2767c80c91e4 | -1.45744 | -48.99414 | 2026-10-09 16:03:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c16fcd54-c67f-3601-ac50-09fd81a2d5c0 | -1.72121 | -48.23579 | 2026-10-09 16:03:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c1bd82fb-2026-3e31-b2cc-288a97efba1c | -3.69246 | -39.12989 | 2026-10-09 16:03:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 45cf6821-1d22-3f46-a21d-83deb4267af9 | -3.18592 | -42.96504 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 88428bc3-bd15-3826-b30a-feb04176b692 | -3.82223 | -44.61145 | 2026-10-09 16:03:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 98749d6b-5b7e-33ff-b53d-a851ab0da6f1 | -4.35816 | -44.35495 | 2026-10-09 16:03:00 | NPP-375 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f79fef32-09ab-30ac-a281-62c57251a100 | -4.03996 | -43.2152 | 2026-10-09 16:03:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fdd3f185-dce8-3145-9c45-04c4c027b7c3 | -1.76866 | -47.80898 | 2026-10-09 16:03:00 | NPP-375 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 632fc4f6-e55d-370f-bf62-f776990794f6 | -4.32333 | -40.17517 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 1fd3431f-27ff-384b-83d8-1e505e3190c8 | -4.57535 | -44.98553 | 2026-10-09 16:03:00 | NPP-375 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 44b87c4e-f3db-3464-8d90-d5c7508eb6c4 | -0.64125 | -49.62178 | 2026-10-09 16:03:00 | NPP-375 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 01c9f81f-4256-34c4-8178-e98252d9ca59 | -4.57589 | -44.98942 | 2026-10-09 16:03:00 | NPP-375 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cbd92101-6bd3-3eb4-acbd-115598978f88 | -4.06331 | -44.92083 | 2026-10-09 16:03:00 | NPP-375 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e7ea0f72-48c5-3fc6-912d-0e77115f40e0 | -4.08723 | -44.16208 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 28021b08-0fa1-3bf8-a3e0-f42385609822 | -4.15189 | -44.33919 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 44d75604-859a-380f-b9f1-e6d893ba23eb | -4.40259 | -43.1176 | 2026-10-09 16:03:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| bc80cf35-4797-3f60-8372-7bbaa3245bf8 | -4.49611 | -43.62933 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ced4e640-5a09-3724-8bb6-ff1b2d1bd7b1 | -3.85074 | -44.154 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bb76c91a-e3aa-3d4d-907c-43f4a1c4125f | -3.45406 | -42.61202 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0994a3df-412c-3c35-8310-35ed46fe5d14 | -3.48264 | -40.57235 | 2026-10-09 16:03:00 | NPP-375 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 45.8 |
| cbf830ec-e9be-3e3d-8fe1-f9c40559fcd4 | -4.24013 | -44.24928 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dc83981b-62b2-3f54-a25f-2debef628590 | -3.51105 | -44.78924 | 2026-10-09 16:03:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 00aa2e35-3dd7-371c-a689-6c4347420a87 | -4.40237 | -43.1155 | 2026-10-09 16:03:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 093f1cc6-6585-37af-b061-a9a12d71b56a | -4.8249 | -45.83362 | 2026-10-09 16:03:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 435763a6-f57c-3c8c-ab7c-48cf3a85ec74 | -3.82171 | -44.6079 | 2026-10-09 16:03:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 45825019-7493-35bc-baf3-b12941094bd9 | -3.50849 | -42.58141 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1e2b3ec0-9b9e-3997-b2e2-d3f493413804 | -1.72213 | -48.24176 | 2026-10-09 16:03:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c9af0bb0-e4e7-36a1-b44e-2623a6e04afc | -3.90248 | -42.11798 | 2026-10-09 16:03:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 647618a5-1057-3315-84ce-b6218c2897d5 | -3.87103 | -44.10723 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff2ed442-a680-3cce-a74b-c26c1c9d3c1d | -3.56697 | -38.96662 | 2026-10-09 16:03:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8d7efc2a-6433-3626-baa0-88f92cf2c06a | -4.50874 | -43.64354 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c5a4b826-0335-3025-b1ea-39524e1fdd34 | -4.07019 | -44.15755 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| d234f3cf-006e-3978-87f6-eb28399b9a4b | -0.82855 | -49.24107 | 2026-10-09 16:03:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1542edd7-329e-35ef-97fb-2213d9cac99c | -4.02618 | -40.64605 | 2026-10-09 16:03:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| b60a5031-cd4d-3d39-959d-6a081ceb696b | -4.02676 | -40.64988 | 2026-10-09 16:03:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d5e56855-7b06-39ed-b4f9-90dacf59ec12 | -0.25684 | -49.27801 | 2026-10-09 16:03:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9d00cc81-65ab-33d0-9bfa-ef20e80ea076 | -8.8899 | -45.3907 | 2026-10-09 16:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| c9f3e517-6001-322d-a76d-680a2b9b0e04 | -3.6435 | -59.3064 | 2026-10-09 16:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |


[Clique aqui para ver as próximas entradas](README284.md)
