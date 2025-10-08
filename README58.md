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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17a016b1-f4b1-3273-a3af-20abd2882588 | -19.46532 | -45.95842 | 2025-10-08 04:19:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 294042f1-3aae-33c1-857e-96f77c370602 | -18.40898 | -45.21214 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2efae8d7-02a0-3ee0-9524-48bec1c60ae8 | -8.94729 | -44.60752 | 2025-10-08 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8691e851-b228-305d-82b9-c6af498270ce | -13.75213 | -45.74395 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b78cc30-be91-3fbe-b9fd-5696e2ad1f8b | -15.76661 | -46.25433 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7245037d-31a6-36c9-8311-cfccf0c2c09d | -13.72506 | -45.69861 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e1626af-349b-3b5b-b2ec-35b6b1395426 | -15.24249 | -46.36086 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9a54100a-aca0-334f-b734-6f28727c4015 | -18.0597 | -44.44334 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3eccc83e-11ba-352e-b2a7-9355adbb683c | -17.84824 | -57.60143 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ef4341ab-ceba-3713-ad1b-436f8d2333ee | -15.17211 | -56.82824 | 2025-10-08 04:19:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a47cd4b-c39c-3987-938b-6c91e2dc998e | -15.36755 | -47.32001 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 054e06b1-9632-3664-a8b4-a4f00c8814c0 | -8.61635 | -45.1029 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf3db1c2-c036-3051-9cb4-6effe9584883 | -17.93937 | -57.50681 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fb07e33f-29d4-3ade-ae01-ba237a17adef | -18.04785 | -44.4529 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 187c08ff-b407-3cdd-b679-56537939db56 | -18.05498 | -57.52683 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4f994d9f-f42a-3662-bbb8-e992db8a45ec | -17.13785 | -45.78732 | 2025-10-08 04:19:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba67d5d5-3d51-3e34-9ed0-3f5219d808eb | -8.60363 | -48.25226 | 2025-10-08 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 924dd23d-8808-3512-aa9c-de3736337102 | -15.60114 | -47.25086 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 084e547e-cb82-354d-bee1-2ff95884b5e9 | -17.84942 | -57.59616 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7b466343-5db9-30cf-9eb5-e3504285de36 | -7.81448 | -44.17974 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| adb79730-14ce-3396-bbee-11ee52f3df1a | -17.94626 | -57.53233 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 923821e0-c789-3acd-8f27-a18f4655f54d | -15.64796 | -44.4884 | 2025-10-08 04:19:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b794c784-9141-385a-8134-70e2e86614f2 | -8.25343 | -50.09383 | 2025-10-08 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06afbf03-3c3c-3653-a884-ee750d42d173 | -17.13351 | -43.46244 | 2025-10-08 04:19:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5f82222-fb8a-397d-a6ae-3a80c3e061e2 | -8.61628 | -44.90664 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5f42c24-963f-30bd-9c75-ce10b3f353c5 | -14.7108 | -46.08686 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f9c5bc3b-e41c-37f6-ab25-63c938724f9b | -7.81674 | -44.14417 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43c2a77a-cb6b-3959-be5b-e9f061031ada | -8.17592 | -50.15931 | 2025-10-08 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40d14629-4f4e-34a5-9db3-640fd24b44d6 | -15.9888 | -50.84068 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0877a63a-ad6a-3d2c-97be-461c27dad43e | -7.46874 | -46.85196 | 2025-10-08 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5679e96-ec1d-3206-84e2-facf7714284c | -15.35589 | -47.32603 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5e60372-4c2b-3ce8-b89a-af423742c190 | -15.29805 | -56.9257 | 2025-10-08 04:19:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2c04fdb-9dbb-311f-879b-6fbec90660ea | -15.29727 | -56.92332 | 2025-10-08 04:19:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f226bddc-609e-33ad-bc96-289ab219b01f | -17.98204 | -44.97599 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 726afb5d-1af6-334a-87c0-22b6d887cbe2 | -17.28953 | -42.65411 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 741c3f39-9e8d-35e1-b0dd-33ff502f5106 | -18.02694 | -44.31407 | 2025-10-08 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f449ca98-920e-335f-8880-ef7a06f2ea03 | -15.19496 | -43.73586 | 2025-10-08 04:19:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 50be89e0-9f92-3465-84e6-72f011a1df52 | -13.74704 | -45.75418 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96dda7c4-4efe-3856-9301-6512d84155f6 | -19.51342 | -44.07965 | 2025-10-08 04:19:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2e00f41-4fc1-37b5-9232-98cf280eceae | -18.29745 | -45.44529 | 2025-10-08 04:19:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2bfa1faa-f13a-3621-900b-c8dc9100d371 | -14.70805 | -46.08262 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 746b14df-a924-3178-8bb0-aeb121985e1b | -15.3878 | -47.31449 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a298e6b2-da2e-3367-b8f3-6cc345a96a59 | -7.80883 | -44.23655 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e1b90d7-0b68-33eb-a93e-ea6646055250 | -17.43647 | -45.80856 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f1fbaa9-effe-3f76-91d1-3a752dd26e3d | -15.19553 | -43.73213 | 2025-10-08 04:19:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 86017776-a865-3c60-940c-59c060998cda | -17.65556 | -42.34852 | 2025-10-08 04:19:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7372ce57-d42d-3087-92af-a45741b1cff8 | -15.27835 | -46.31066 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 760afcd4-86bc-318d-a8ac-5d53ca8493d8 | -14.43346 | -46.15631 | 2025-10-08 04:19:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29c0ee02-3e9a-3ed8-8df5-41b6ea4346d0 | -20.1888 | -43.93234 | 2025-10-08 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8788f3dd-3a21-3d54-99b0-4d83ab02dab6 | -13.31495 | -48.02142 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f398cce4-0e56-3096-b62d-bdc71fb9b4f0 | -14.92644 | -46.79281 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1036f42a-2884-3f8a-acbd-76532542d12f | -7.78882 | -44.21169 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96fd0dd7-294a-3fec-8bf3-c6ec1d97c546 | -20.20041 | -43.95098 | 2025-10-08 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 0409870e-08a7-3e80-a799-63641b327eef | -15.25925 | -46.36416 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d24b3fcb-97c7-355d-b1a3-cad7aaee03c2 | -17.1566 | -56.59758 | 2025-10-08 04:19:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| c7f354d5-fdbd-32d3-bde2-304498aa5a5a | -18.04898 | -44.46837 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37e91e6f-62c5-3771-bdb8-182fbf075cd1 | -17.15966 | -56.61171 | 2025-10-08 04:19:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| da1d9867-a60d-3489-9ff4-846f0a4198af | -8.92734 | -46.59403 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43ee1430-7d06-3f51-90af-15bc8e35dc82 | -18.06991 | -44.46769 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de7513ca-46e9-3294-bb54-7f4674ff8b40 | -17.8482 | -57.60001 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d0aa8dee-8917-3b74-bb10-17b1a8d46cde | -15.28094 | -45.34327 | 2025-10-08 04:19:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 890658e1-9605-3c2c-b910-a7a580763baa | -17.82797 | -57.63484 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 4a132567-29ad-3fe1-a6c4-65dacdf14046 | -9.29807 | -46.42576 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa6fae42-6ccd-3827-86d2-764e2274ba39 | -17.96448 | -57.50763 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2cba87b8-fc22-3ffe-9809-160929ff3bed | -14.25438 | -45.86113 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdf6ecdd-e8c0-3366-80fd-d33bad013bc0 | -17.57215 | -46.05825 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| c5de05af-98fa-37e4-a08d-31270103d063 | -14.72188 | -46.04013 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d5b7523-edc2-381b-b0bf-5a49eeb0d567 | -14.89614 | -46.85045 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af998167-5043-3c6d-9153-c3493322eacd | -8.55436 | -46.23007 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71d80a9a-3884-3404-aa83-f67224041cb3 | -15.66338 | -43.65517 | 2025-10-08 04:19:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d01e6bb4-b408-329b-9a00-38f148c60222 | -15.16743 | -45.74082 | 2025-10-08 04:19:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba02e83f-9d51-3e5c-bd3b-1afd4e5dfee8 | -7.61577 | -44.13374 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7536183a-1be0-3889-bf16-900d98c18f79 | -7.81058 | -44.18271 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6aa8a18f-2fb5-3ea1-8b50-f354c377eda0 | -15.66394 | -43.65139 | 2025-10-08 04:19:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b7290b9-586f-3bb4-b717-ad03f860a473 | -13.2948 | -48.03282 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9557c79b-6040-33f4-a047-5acbe8c8510b | -13.30184 | -48.0322 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ed138a0b-ef51-35c8-b6ea-5ccf25bb67e0 | -17.83145 | -57.64765 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 9b8cdf6b-79ce-3a63-889d-c2ac81e8419f | -19.46769 | -43.89694 | 2025-10-08 04:19:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8a15096-a696-362b-9fed-600f1f67c3c3 | -14.36268 | -47.73392 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 81df5faf-4d98-38a6-9345-4a34d064eb58 | -7.81726 | -44.18379 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7dc459b-da8d-375e-8820-a619635c9153 | -17.93477 | -57.5271 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ee1ecd9a-b22e-3284-9a70-4fbc4a972154 | -14.894 | -42.10587 | 2025-10-08 04:19:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 329aa409-8f0c-3a2e-8c8a-1731117145ae | -15.08123 | -46.61839 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69e897f5-9898-3fb6-ac1d-6b962a6586a2 | -14.45381 | -48.79576 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a611881-f6ac-34f9-9c51-e75195d863e5 | -7.82619 | -44.1493 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0eda6dd3-9a71-3106-beeb-07ffce165400 | -14.71972 | -46.03228 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93238af7-b443-3e39-aecf-7c49480ee112 | -8.93736 | -46.6 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c90e8e1b-9491-3274-aa33-39bf4f59b7bb | -17.13578 | -45.78751 | 2025-10-08 04:19:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f665a2c0-aa88-3091-9190-22ee6d043934 | -15.49278 | -47.92818 | 2025-10-08 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23e43534-31f3-3053-870e-9234870de791 | -17.95154 | -57.50891 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a30d9f0e-9547-3ac0-9eaf-22b72fbacbf1 | -14.94573 | -46.80339 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2eacc14b-27c1-3404-ae15-6ed081857a1b | -5.0401 | -43.5973 | 2025-10-08 04:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 704d1259-6aa2-3b28-a019-19ee413bfb53 | -17.8417 | -57.6254 | 2025-10-08 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.3 |
| b4698841-e1b4-376a-b444-0f64b2bff2d9 | -7.3447 | -43.8503 | 2025-10-08 04:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 42.6 |
| fcbde34a-b600-387e-9bc9-275439d88cd6 | -6.9491 | -63.086 | 2025-10-08 04:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| d26e8f04-235b-3fe5-9501-9fa220be0965 | -8.2263 | -44.178 | 2025-10-08 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 19947600-ff49-362e-8afa-883dfc0f7957 | -5.1416 | -44.9443 | 2025-10-08 04:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a57df55e-f9e0-3715-a364-2ec3f6c13f3b | -17.8219 | -57.6277 | 2025-10-08 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 22dba9ea-3430-342a-8080-2037f4fc1457 | -22.3966 | -49.97664 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3cf2243c-20a0-38da-8a21-8c31b6b7c1fc | -21.95626 | -44.66368 | 2025-10-08 04:21:00 | NPP-375D | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README59.md)
