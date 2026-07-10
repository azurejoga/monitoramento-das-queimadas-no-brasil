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
| 47186514-2f28-3e1c-9d39-cfb604cacd7d | -12.49144 | -43.76881 | 2026-07-10 03:30:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09dfa5b1-9b1a-3ede-93d7-cee346b39c40 | -13.27238 | -45.15176 | 2026-07-10 03:30:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6606b895-bff4-3c09-8934-986d522213a2 | -12.49674 | -43.77445 | 2026-07-10 03:30:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 66a9fcf7-bac1-3280-bc64-950d5c22b768 | -12.49804 | -43.76822 | 2026-07-10 03:30:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 24cba693-5f5f-397c-862a-e3f4053a641b | -12.49818 | -43.7704 | 2026-07-10 03:30:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 93b98c6d-0492-386b-b467-2aaeef213b20 | -12.49684 | -43.77661 | 2026-07-10 03:30:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 68e127ee-c24b-3a41-babb-7f165a7dbb7a | -13.30836 | -43.72343 | 2026-07-10 03:30:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| beca610e-1d67-31d2-addc-a0cd46ec421f | -12.49544 | -43.78068 | 2026-07-10 03:30:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2012a64e-0ce3-3dba-8c54-152ceedd2bce | -14.84022 | -42.77193 | 2026-07-10 03:30:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc61c13a-ef04-3fa5-9ea0-80aa33c3d933 | -19.36439 | -40.86372 | 2026-07-10 03:32:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 35ab88f0-c181-3617-a996-ec96f4a52668 | -19.36504 | -40.86058 | 2026-07-10 03:32:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6934da95-14a2-3e41-8ed6-5c9600ad7253 | -18.02211 | -41.83314 | 2026-07-10 03:32:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 35176ff4-4975-37e8-9544-321ac87e4254 | -10.1286 | -50.1902 | 2026-07-10 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 8b989b0f-67d4-323c-889d-48c01d9a3834 | -4.15624 | -43.09488 | 2026-07-10 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10d3f2d4-9beb-367e-aeaf-f2f03d0dee8d | -11.99998 | -38.74126 | 2026-07-10 03:47:00 | NOAA-20 | IRARÁ | BAHIA | Brasil | 2914505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 937759b7-6a9b-39a3-b78e-2e90e394066b | -13.41853 | -40.26491 | 2026-07-10 03:47:00 | NOAA-20 | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 67edd041-d632-3822-9a67-14e403977a33 | -12.12224 | -38.91679 | 2026-07-10 03:47:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 09fcce5c-672f-3cd3-9799-0719fe2153e7 | -12.45278 | -49.58106 | 2026-07-10 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4a62aeca-a7a1-3cd1-967c-3bdf37c98290 | -11.44764 | -47.57646 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25bb0794-a0fc-3978-8dfe-4dfc9f939e97 | -12.49733 | -43.76247 | 2026-07-10 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 67b141a5-8225-3a24-954b-40e965aaa960 | -6.93921 | -43.71809 | 2026-07-10 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00d7882c-2dbe-3b6a-a577-3c17add682dd | -2.90181 | -40.39552 | 2026-07-10 03:47:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 87106fff-8393-33bf-88a0-d2df128dd964 | -10.26493 | -46.38913 | 2026-07-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 001299b2-b2e2-3d78-8681-d8e7c216fdf3 | -11.43746 | -41.43394 | 2026-07-10 03:47:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1b1137f7-5bd8-3979-a958-461c617e566d | -11.41947 | -41.41958 | 2026-07-10 03:47:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 54ff69f5-101e-3f47-9c23-e689dfdda6d0 | -11.44694 | -47.5799 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 736fc424-2243-307b-9cf7-64bffac88761 | -12.4462 | -49.5797 | 2026-07-10 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aeaa11b2-e1ed-33ad-b86c-f8b69a430559 | -13.25774 | -45.12727 | 2026-07-10 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| feefe544-e699-3e6f-ab28-2d1da575a090 | -12.49646 | -43.76724 | 2026-07-10 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ff0e1b81-6b52-30a9-baef-3526dc343059 | -6.50019 | -42.21397 | 2026-07-10 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 686cfaab-6b07-358a-a9cc-cb772b07d8e3 | -3.95156 | -41.53178 | 2026-07-10 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f824b23f-34c2-306d-90e1-f08b57ed9b05 | -11.45969 | -47.59603 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06f7f802-08c3-3b28-84f8-7e3aea06c2f6 | -12.4476 | -49.5835 | 2026-07-10 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4185f33d-a279-30a2-8d3b-454534e441c3 | -11.46483 | -47.60139 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f87d04c-9e52-319a-9b29-ccb5f474d9e4 | -10.86128 | -44.44225 | 2026-07-10 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98a9c03d-0d75-3ede-a521-5528e82c77d4 | -6.41968 | -43.71692 | 2026-07-10 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 367cd55d-a781-31fd-afdb-0ae0a0221200 | -12.49191 | -43.76632 | 2026-07-10 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ff946ea-f01d-3f77-8034-66fc20ac55e0 | -11.46906 | -47.61147 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07c960a8-625b-3d1e-bc85-599c371f95d2 | -12.45419 | -49.58487 | 2026-07-10 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6e20a5fd-997a-35a0-a5eb-dbc3bd20f6cf | -4.34145 | -47.77302 | 2026-07-10 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1cc7c097-d887-3b42-8660-6a55469a679e | -13.32986 | -40.89054 | 2026-07-10 03:47:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 168896f8-95ff-3a3b-ac6c-d4750de35367 | -11.8519 | -48.24346 | 2026-07-10 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bcf70a7-287d-3580-a709-4950e06b93fa | -4.97978 | -37.47467 | 2026-07-10 03:47:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 6360404a-9690-3f24-909d-1b83a44c5267 | -11.87488 | -47.67852 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b65a68e-2dd2-3795-92f6-a48645017691 | -11.8396 | -48.24096 | 2026-07-10 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 75ec1e24-33c5-3ef5-a593-909d3d7e4001 | -12.84428 | -44.35059 | 2026-07-10 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 850a6ee5-2c09-3d1c-9358-5ec4fd2bbf31 | -11.83343 | -48.23981 | 2026-07-10 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8bc7ad75-c48a-30fa-9919-43bd527b8a60 | -5.71232 | -43.22876 | 2026-07-10 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20d4d8bc-24b5-336e-961b-307b30683ced | -5.75199 | -43.26492 | 2026-07-10 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74264211-fbb0-3324-b897-1683b7a76bc0 | -11.87893 | -47.67225 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 47359e42-5a7e-3af9-bf6d-008eccb593b4 | -10.85501 | -44.43905 | 2026-07-10 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8489793a-0a9e-3191-b6f4-beb432978dd9 | -6.50105 | -42.21217 | 2026-07-10 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 8f696c6c-dd51-386d-b30b-d80958d4943a | -3.32109 | -40.00594 | 2026-07-10 03:47:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9873c236-8b29-35d4-9a6e-0f7584b1998f | -5.12491 | -37.50058 | 2026-07-10 03:47:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0e47015d-26c0-373d-90f6-f1a828b53502 | -7.72884 | -44.5615 | 2026-07-10 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59534a71-a012-370b-895b-d125511c40b1 | -6.93972 | -43.71522 | 2026-07-10 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92a52061-bd7d-3ce3-a06a-afa7d38432cd | -11.45686 | -47.59203 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6990c22e-f067-31a2-ad6c-48807c55928e | -12.84899 | -44.35152 | 2026-07-10 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc2946d0-c68c-3f47-9cd3-411b1c832081 | -6.50098 | -42.20929 | 2026-07-10 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 809f992a-b745-3f0d-b76c-351c5cf74414 | -11.85091 | -48.24843 | 2026-07-10 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cba94b9c-9687-38c8-89cd-40989d5d8de2 | -5.03779 | -37.41161 | 2026-07-10 03:47:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| faf282a9-a2ee-3d42-b3e4-33d776e7ff25 | -11.45267 | -47.58217 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f90d6312-094f-3ca9-9ee1-d2fbe6a87138 | -12.4488 | -49.57769 | 2026-07-10 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 30fb6dae-f514-3cc1-b455-34e8faabc1ce | -7.72943 | -44.55826 | 2026-07-10 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38ad962a-d7c6-3ff5-88c2-d2e3104ff776 | -5.80199 | -43.63309 | 2026-07-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0db5ab68-acb4-39a4-9423-0a0e9ff168a3 | -4.94384 | -48.2505 | 2026-07-10 03:47:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a464c08-94ee-3440-abc3-6d64f9dd5465 | -6.94573 | -43.71042 | 2026-07-10 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20e85de4-8ccf-38e4-b01d-8c3633cf6951 | -11.4617 | -47.59874 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bddfff6-d4b8-3a04-af18-00b0d231302d | -13.26917 | -45.14744 | 2026-07-10 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce5b6d81-2c67-37c5-af95-7ae6fe57e50a | -13.27029 | -45.14162 | 2026-07-10 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d10d408-a024-3a6b-bf70-5908b8698dea | -4.34645 | -47.77338 | 2026-07-10 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 21bf9ac6-ea49-3240-a90d-1afd3de26cf7 | -13.273 | -45.15406 | 2026-07-10 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 289ae4d0-b5cf-3940-b96d-57753c0a82a5 | -4.77369 | -41.79262 | 2026-07-10 03:47:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 93ddcdf2-b91d-3d14-abe5-7648265564a3 | -12.45155 | -49.58685 | 2026-07-10 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fd0939d4-beb5-349c-b83c-0b559c33a92d | -12.84721 | -44.35398 | 2026-07-10 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d561ef66-001c-31a6-9d18-cef4833b1c0e | -11.46405 | -47.60538 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf5d8461-bac5-3256-95fb-db6f334189ff | -12.50015 | -43.77292 | 2026-07-10 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 939e54d5-34fb-3e68-b4cf-1b10dc67f6b9 | -11.45889 | -47.60009 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d6c83b8-34ec-32ca-9932-2d1b42e857af | -11.46289 | -47.61138 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d33591b2-ef7f-368b-926e-271f6cf14b66 | -11.41756 | -41.41879 | 2026-07-10 03:47:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1dac7a43-b622-3711-b360-90245141afa3 | -10.85993 | -44.43992 | 2026-07-10 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bd9589d0-4aae-3de7-bfce-6d63044ffe3d | -10.13021 | -50.17751 | 2026-07-10 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 52759833-0665-3adf-bab4-167546cdf6e1 | -12.49472 | -43.77677 | 2026-07-10 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15dc052f-e2d9-39fa-8f9e-9c254226d1cd | -6.00416 | -39.1962 | 2026-07-10 03:47:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4fb951ef-6867-3eb2-9dff-34da2bd4c407 | -11.85038 | -48.24653 | 2026-07-10 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 12984a77-8a49-3ff4-b27d-b504cc57da34 | -13.26806 | -45.15319 | 2026-07-10 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab0afc8d-b8a3-34fd-b171-4fbab1a1cc22 | -6.94023 | -43.71235 | 2026-07-10 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5588c56-6050-3712-87c9-61f46899b9af | -11.87802 | -47.67675 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9fe87b7f-0a48-351d-9749-aacddbe752f7 | -12.50102 | -43.76815 | 2026-07-10 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| db68e944-347b-3a48-abde-f1767be1332e | -12.84816 | -44.34882 | 2026-07-10 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a8df0e6-8bd7-31e7-a57e-d60311674213 | -10.12734 | -50.19148 | 2026-07-10 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a666b078-43ec-3467-a00f-36c438ff3e1a | -11.46595 | -47.60836 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 60f88e2e-7396-3d37-bc9b-bde9209fb728 | -4.34072 | -47.76628 | 2026-07-10 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d77d7a5d-a360-384f-8cd2-33af09631852 | -12.49559 | -43.772 | 2026-07-10 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 95bee68e-d2e5-3d74-aedf-3de21800c9f9 | -6.93523 | -43.7114 | 2026-07-10 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 173dc60a-cbbd-30f5-ac4e-8e03e46921a6 | -10.25858 | -46.3918 | 2026-07-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3ec65cce-d169-3451-a24a-569e5ee2bf35 | -11.456 | -47.59628 | 2026-07-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d43d78ff-a708-3d8c-81c5-84cca4ca3557 | -10.25934 | -46.3878 | 2026-07-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a1064313-060a-3b49-abf3-1264675b7571 | -13.30955 | -43.71829 | 2026-07-10 03:47:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 25e5523a-b94a-3c91-b38c-5af498ee6db6 | -3.31696 | -40.00525 | 2026-07-10 03:47:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README5.md)
