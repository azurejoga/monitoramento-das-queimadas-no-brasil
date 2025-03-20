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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2acebcf8-f161-319d-977d-bc8bb22c9702 | -12.91183 | -45.04741 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3fe8192-e366-3547-8b82-c2b85c2fb9d7 | -12.91006 | -45.05939 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57a41df3-615f-3e02-9829-ff2cff405039 | -13.25595 | -54.37597 | 2025-03-20 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b8c3eec-47e1-35f6-a01c-80009c05e1e1 | -12.91065 | -45.0554 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8c7becd-9fd3-3e93-bc0e-a2bd62e29380 | -12.90832 | -45.04688 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13f3c5a8-0b34-322d-b890-e9984fcbdff2 | -15.34706 | -46.96022 | 2025-03-20 04:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a69389a5-f001-3a38-98cc-f84a6a83b422 | -12.89077 | -44.87114 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7d7dc54-c584-321b-a2e2-e3c9e5db10ba | -12.0971 | -45.63066 | 2025-03-20 04:25:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8bea1df-612a-366c-bdea-cad8074bda36 | -13.26037 | -54.37683 | 2025-03-20 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d90277cc-556e-3af9-bc5f-0da5891f17ac | -13.25714 | -54.38859 | 2025-03-20 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab3a204f-e5de-33c6-a041-34e2c47a93c1 | -12.90714 | -45.05486 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2825ea14-fd36-39cc-83cf-5ba7539733dd | -12.09142 | -45.6221 | 2025-03-20 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3343dec9-5cf5-3d12-8c1a-45c5c5e029fc | -12.91298 | -45.06392 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1bfbea2-1899-319f-a9b3-fd8a950d23ec | -12.88665 | -44.87466 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7ca36b0-7155-3a11-8b66-075fabc6cc26 | -12.88311 | -44.87411 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e48a6e8c-0d72-3aa4-ad1d-863bf9c528c1 | -14.729 | -46.83287 | 2025-03-20 04:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d94c9b2-1d45-3858-8755-90eebe198e04 | -12.14741 | -40.29902 | 2025-03-20 04:25:00 | NOAA-20 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b88fbbc1-87e4-3219-b671-3de5921d4c80 | -12.30095 | -43.50303 | 2025-03-20 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 916ee838-1bc4-3913-bb05-d6318cd690c7 | -12.91708 | -45.06045 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aa75b3f4-5080-3407-8924-054d14fbd81c | -12.09426 | -45.62638 | 2025-03-20 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48d05fc6-27bc-3738-b8e4-247ce4e1bb7f | -12.91124 | -45.05141 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f713ca80-be56-3650-9d0d-c98a311cb907 | -12.09653 | -45.6344 | 2025-03-20 04:25:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1088270d-affa-3d5c-a3eb-06ff7fb78b2a | -15.07704 | -48.94575 | 2025-03-20 04:25:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3febb496-1b71-33ad-b1e5-a681c1e10723 | -12.89896 | -45.03727 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4333cbf-24a7-3f50-ae98-f35a2ff486ac | -13.25875 | -54.38581 | 2025-03-20 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c600fadf-f166-300c-9ab2-1a8e5a96cc10 | -12.09596 | -45.63815 | 2025-03-20 04:25:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76186ef2-0db6-3062-888b-33f06917c845 | -12.29341 | -43.50192 | 2025-03-20 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cc5dec1-4284-3629-a6b1-a609615418c4 | -12.17572 | -44.05516 | 2025-03-20 04:25:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ed42e49-f764-3d0e-84ae-89bd09e60a28 | -15.34761 | -46.95655 | 2025-03-20 04:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da8cf820-5d53-39b4-b6c1-e75cbd230b21 | -13.25153 | -54.37513 | 2025-03-20 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 583f0776-4c66-355f-9f7a-5db04deda6bd | -11.57353 | -47.6264 | 2025-03-20 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d59f4d6-8244-3927-9745-245e71ccaca1 | -12.90596 | -45.06285 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a79fc9bf-1a3d-3836-8d29-fbbbcb34264a | -12.90773 | -45.05087 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ae52d34-3b98-3f3b-b0cb-3a877c8a9fc4 | -12.91475 | -45.05194 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2067a7f8-aece-3047-b03c-2a3c1b1360d7 | -12.09312 | -45.63387 | 2025-03-20 04:25:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74c9e105-5f7a-38b5-9043-eb5f4df48240 | -13.25966 | -54.37517 | 2025-03-20 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b216deeb-a462-3d48-85c0-d34d9052e1cc | -12.33197 | -48.00705 | 2025-03-20 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e4e8a7e-4700-3b2f-9c2e-693efddb5302 | -14.84856 | -46.80635 | 2025-03-20 04:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51b62a62-cca8-3a34-b881-ca1b413f8920 | -12.91416 | -45.05594 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d2df7719-5392-32a8-ad54-b03714352ceb | -12.90655 | -45.05886 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ba43cde-590c-3ba4-9935-e23161fbd625 | -13.25794 | -54.3903 | 2025-03-20 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f94d6819-dcca-3d92-96dc-a956f4c358a8 | -15.3437 | -46.95968 | 2025-03-20 04:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d50b237a-ab3a-3237-8030-dcc7bd938db7 | -18.00049 | -54.0141 | 2025-03-20 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31da1bdf-c3f2-3c7a-9b0a-f99ac7955a2f | -22.54016 | -48.8117 | 2025-03-20 04:27:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 488dd44d-66ab-3a6c-a2a2-4c6c6246d211 | -16.46195 | -55.07571 | 2025-03-20 04:27:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 82ebd098-584f-3cb5-b750-a57c09899024 | -18.53694 | -56.18259 | 2025-03-20 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 166416d1-aee1-35d9-856b-3fce52f701bc | -19.42536 | -54.78725 | 2025-03-20 04:27:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60dee7f0-59ef-3979-86f9-23a90275159e | -22.61293 | -46.98265 | 2025-03-20 04:27:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20f02310-7bcf-37f1-a273-8aff9c2e8019 | -19.43089 | -54.78042 | 2025-03-20 04:27:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 875cdb20-3860-3232-a4e5-124c6743b50d | -23.43897 | -51.42696 | 2025-03-20 04:27:00 | NOAA-20 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d3254bc7-fd8e-33a5-82e7-f3c2397220f3 | -21.50097 | -53.06609 | 2025-03-20 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| beda169d-791d-37c6-bec6-28968e75ea9a | -21.24059 | -56.46651 | 2025-03-20 04:27:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf11b51a-11b7-36f1-8c60-853a24ddb240 | -19.439 | -54.78228 | 2025-03-20 04:27:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cf5cf26-0626-381d-a839-9cd280f50019 | -23.57513 | -47.21529 | 2025-03-20 04:27:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed8e65b7-43b4-3799-8961-e007c030e1ca | -21.11756 | -55.66084 | 2025-03-20 04:27:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9475136c-b5bf-3159-863a-7f63b22c066a | -20.99589 | -51.79142 | 2025-03-20 04:27:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 17171598-1741-3f71-af88-f8fb7a99c1ce | -21.12171 | -55.66182 | 2025-03-20 04:27:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5171499c-57a5-31d4-9ce8-bc205cea4ff8 | -20.98352 | -48.63709 | 2025-03-20 04:27:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ac9e1eca-b76f-31ac-8846-8894298482fe | -19.43015 | -54.78431 | 2025-03-20 04:27:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e798bcba-8832-325e-b4cb-ece8778b5ac6 | -18.00514 | -54.01123 | 2025-03-20 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed79fc73-8c20-3d16-9fe1-42b666e806cd | -21.00543 | -48.64442 | 2025-03-20 04:27:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1e93f2cb-9c05-3e89-b21d-3a9f7938f6fc | -21.24614 | -54.0428 | 2025-03-20 04:27:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a773038-cbb1-3bf0-af8f-014cfbc4de53 | -23.63603 | -46.41473 | 2025-03-20 04:27:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c620829b-89ac-3ac9-9783-0d377c226886 | -21.23622 | -56.46552 | 2025-03-20 04:27:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d747c09-8d1c-3e8a-95e3-9153dbba5548 | -21.11674 | -55.665 | 2025-03-20 04:27:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8bd61e5-fe6b-34f8-b2e3-e2006ba491b9 | -16.46278 | -55.0713 | 2025-03-20 04:27:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 350a35fe-4e0e-32eb-aea9-4cfc0db8d526 | -20.50144 | -55.92596 | 2025-03-20 04:27:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a72cb19-4f70-3c38-ac7a-08b788d01bea | -16.30185 | -53.84089 | 2025-03-20 04:27:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 351502b3-1d77-304f-afe7-28f0226debed | -18.536 | -56.18741 | 2025-03-20 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5abb8dcc-162b-3634-8b99-56a4b5a4ea9b | -19.42203 | -54.78248 | 2025-03-20 04:27:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 707d356f-4b0f-3366-bf53-77b4eb4c4a98 | -21.04396 | -49.90493 | 2025-03-20 04:27:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1167b43c-958b-37ff-b808-06b795984e59 | -17.14746 | -54.00534 | 2025-03-20 04:27:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03cf7116-d9a8-395a-9e9b-61846d46afb6 | -21.1209 | -55.66601 | 2025-03-20 04:27:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0eb44af9-c31b-3185-a45e-4e551e2573d1 | -22.07037 | -56.19792 | 2025-03-20 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e592de0-5d6a-3e15-af06-c037e9f432e0 | -17.77983 | -42.80831 | 2025-03-20 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a2af616-69c9-31e5-90e4-ab8c8f64bf63 | -19.42609 | -54.78338 | 2025-03-20 04:27:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24d831bd-3870-3043-8f25-ce1dea014cc6 | -20.25504 | -49.67522 | 2025-03-20 04:27:00 | NOAA-20 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f295c10-f2e6-3028-8b37-99652070efd4 | -21.22728 | -56.25823 | 2025-03-20 04:27:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e57b0a01-6512-3a8f-9625-a632d7d33bde | -20.98685 | -48.63766 | 2025-03-20 04:27:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9e53bdbc-75d1-3e3b-8a1c-8e6848c5e4bb | -17.14724 | -54.00594 | 2025-03-20 04:27:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6304f75-c43a-3567-a616-be5095070fff | -16.30188 | -53.83926 | 2025-03-20 04:27:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43237f07-c5d9-3628-a3d1-66b9d2c9597f | -25.19168 | -49.32646 | 2025-03-20 04:29:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8ba9c409-b4da-3acc-b955-0af7fd4faef6 | -26.62316 | -52.76627 | 2025-03-20 04:29:00 | NOAA-20 | FORMOSA DO SUL | SANTA CATARINA | Brasil | 4205431 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bf420e0b-6505-3842-af33-f9ac09923c4b | -28.99332 | -52.30656 | 2025-03-20 04:29:00 | NOAA-20 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f85657a7-6fbf-36d8-9dfe-bf0654414715 | -28.99664 | -52.30727 | 2025-03-20 04:29:00 | NOAA-20 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 4a05eed9-0856-3a0d-a9e2-5e35047ee884 | -25.56764 | -49.36638 | 2025-03-20 04:29:00 | NOAA-20 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 86a17acd-b365-39e5-8604-86316f71354e | -28.58567 | -49.43983 | 2025-03-20 04:29:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 450ca891-69a7-3efc-8bef-6adbb80af3c2 | -30.50465 | -50.40962 | 2025-03-20 04:29:00 | NOAA-20 | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| b00ff1d2-e5f9-3f3e-a5ce-f4cc41a0d962 | -28.99034 | -55.48023 | 2025-03-20 04:29:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| f35c644e-4bd5-363b-aa50-4a26c3857cb1 | -27.36212 | -48.64222 | 2025-03-20 04:29:00 | NOAA-20 | BIGUAÇU | SANTA CATARINA | Brasil | 4202305 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dc852bcc-1c74-3585-a634-913997f27f20 | -26.31451 | -52.63758 | 2025-03-20 04:29:00 | NOAA-20 | MARIÓPOLIS | PARANÁ | Brasil | 4115309 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6188dea5-243d-3d5e-95e9-0283fcd79699 | -28.98952 | -55.48265 | 2025-03-20 04:29:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 953e2120-45dd-386c-857f-99a5d59a9c79 | -27.68555 | -48.75083 | 2025-03-20 04:29:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 91c4d9dc-03fe-3041-ba1b-89d61ac4a61d | -27.00836 | -53.16768 | 2025-03-20 04:29:00 | NOAA-20 | PALMITOS | SANTA CATARINA | Brasil | 4212106 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 67727b2b-6379-3968-9fd9-69c3edee8eeb | -27.3359 | -50.57395 | 2025-03-20 04:29:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 96fb1eb2-5b05-3405-a7bc-665938c4ce8d | -29.66945 | -51.29219 | 2025-03-20 04:29:00 | NOAA-20 | CAPELA DE SANTANA | RIO GRANDE DO SUL | Brasil | 4304689 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 6e9bf113-7085-3c1e-9b6f-8211499ca4eb | -31.59662 | -52.73705 | 2025-03-20 04:32:00 | NOAA-20 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| ccea99b2-ba7a-3294-97cb-44ae8f762441 | -30.74491 | -52.66185 | 2025-03-20 04:32:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| ba9be34b-fc2c-37b1-b59a-2c138bfc0aa6 | -31.26861 | -52.87463 | 2025-03-20 04:32:00 | NOAA-20 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 3b8c36e1-2ad8-3c2a-8fd3-029079acb45f | -7.05154 | -44.37315 | 2025-03-20 05:01:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |


[Clique aqui para ver as próximas entradas](README4.md)
