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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90522dc8-0785-344f-aa4b-0a1fb789d30e | -16.08308 | -43.63411 | 2025-08-10 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44c5f054-ed9a-31a7-a497-671cdd1e2288 | -20.1721 | -43.7189 | 2025-08-10 03:57:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 7dc08e6b-fb2a-3dcf-b757-2d6a5216a7cf | -19.57681 | -47.22755 | 2025-08-10 03:57:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c1c6144-36ae-394d-beca-e0ec0a0e4000 | -19.5761 | -47.2314 | 2025-08-10 03:57:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e9b8bce-3876-3636-8599-0f156ec46564 | -12.55543 | -47.08146 | 2025-08-10 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 67b89046-bade-3a2c-b37a-bda0268be1c4 | -16.36942 | -42.54382 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6cc96599-7c51-3991-bda7-b80f491a0234 | -14.59589 | -47.16187 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f4f78fe-edc6-3868-a702-e4a84571d5bd | -16.37465 | -42.53319 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9770ea88-7868-3f36-82b4-b54e4fae95bf | -14.29672 | -51.9699 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6313b519-d409-34ed-ac2f-82b130b40e90 | -12.7149 | -46.36739 | 2025-08-10 03:57:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eae8e45e-3866-3498-947c-f0de1ac79e4c | -14.30164 | -51.97335 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bcc56b83-2603-3323-84bc-fb365182cd3c | -16.37404 | -42.53691 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d09b55f4-e6cc-3dc2-a9fc-1d058852af86 | -13.64167 | -48.98508 | 2025-08-10 03:57:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a1b191b-e7b1-3206-af68-ecf7a0c56507 | -19.58285 | -47.24072 | 2025-08-10 03:57:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6afae58f-505b-39cf-a4be-09b4e1e3cf16 | -14.58786 | -47.15569 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe3e8a0a-38bc-375c-9237-88bf1f828b52 | -16.37865 | -42.53001 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ced6a3a5-3f1e-3f49-961a-864771226870 | -14.3008 | -51.98053 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ff6e569-bbcf-36c1-9a38-562f90d54593 | -14.28942 | -51.9712 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2e135bc9-ebec-3a16-8995-dba550542c73 | -16.31023 | -52.9241 | 2025-08-10 03:57:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44fd88d1-5571-3e98-8b21-baf643aadf42 | -14.30184 | -51.97564 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ed82911-a0a7-3137-84ce-61d1ec1eacdb | -16.37744 | -42.53746 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 9ce6405c-9435-3a12-a7cf-0720615af7a7 | -19.07954 | -43.54288 | 2025-08-10 03:57:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2fb2d16f-544a-3a09-8555-b202d9c0efee | -18.55592 | -43.43632 | 2025-08-10 03:57:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 41b6f161-9071-3195-a1d7-4a745956947a | -12.58124 | -47.14712 | 2025-08-10 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f8049502-a44f-3d5b-a26d-46b58597be31 | -14.46424 | -47.84878 | 2025-08-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 136a4ebf-a637-353d-9019-b46a52daaa2c | -12.16874 | -50.22189 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89cc7c13-1847-3420-99c0-7435ee5ec690 | -18.17285 | -46.98769 | 2025-08-10 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 64ca96d7-7eee-31bb-a9d9-dfb6a26be17e | -19.08364 | -43.53951 | 2025-08-10 03:57:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89a13fbb-2f91-3ec1-9f6b-c33351599cf3 | -14.09212 | -46.57758 | 2025-08-10 03:57:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a956e91b-eb74-37e1-a186-fb48370e4714 | -18.98346 | -48.41084 | 2025-08-10 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a953b020-9d7b-378b-8ddd-42abc07a6f3b | -19.48833 | -41.7481 | 2025-08-10 03:57:00 | NOAA-21 | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a1e0aede-f134-3082-94df-690bbe328d32 | -16.37526 | -42.52947 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a6cd630-d1ba-36de-a377-10f0800017b1 | -17.51393 | -41.73586 | 2025-08-10 03:57:00 | NOAA-21 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 119a7b69-1535-347b-9500-2c13e085891c | -16.0767 | -43.62871 | 2025-08-10 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 794ef3a7-2a2e-35f4-ae58-f80c92277bb1 | -18.17968 | -46.99691 | 2025-08-10 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a47db86-086b-3590-ae80-c32c19ab5c00 | -16.37159 | -42.55187 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fb109a7-fae4-3341-bead-848425d5968d | -18.17474 | -47.00047 | 2025-08-10 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea01eeb3-0f13-34e8-b5d6-b2a2df8604a5 | -14.09444 | -46.56495 | 2025-08-10 03:57:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2100d560-911d-316c-b0fe-0b085792ed0e | -20.54243 | -42.37333 | 2025-08-10 03:57:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f81c9252-e112-3484-8e19-174ba2518b06 | -14.70137 | -48.56616 | 2025-08-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 510c28bb-e42c-3579-9003-87c2da02ba8b | -14.39763 | -43.78167 | 2025-08-10 03:57:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e93926cc-36e5-39e2-b6b1-77429cc82837 | -18.2184 | -43.51822 | 2025-08-10 03:57:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac346505-47dd-3e56-995b-ba639b76fb26 | -13.63667 | -48.98358 | 2025-08-10 03:57:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 280000ee-03ad-379f-8abc-6775e0e3590a | -12.60321 | -47.13114 | 2025-08-10 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee5d7c8b-6a2d-3e68-9dff-3a8c3d42b035 | -14.59251 | -47.16331 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24ca4cda-06a7-3062-a773-2c515af2b4b6 | -19.7718 | -43.01442 | 2025-08-10 03:57:00 | NOAA-21 | NOVA ERA | MINAS GERAIS | Brasil | 3144706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 38c836cb-e22f-385a-b4e9-b6d4f8c9c316 | -18.1789 | -47.00109 | 2025-08-10 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| caf87b43-96f1-3f12-9c8a-961138b62714 | -13.63571 | -48.98854 | 2025-08-10 03:57:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f7d54a75-d0c5-3cf0-9abb-1976fea228ac | -19.96273 | -44.68802 | 2025-08-10 03:57:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc34e36b-90cc-3fb7-a7f1-41b56bddbc43 | -14.29977 | -51.9854 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8967017-a196-3262-b116-68654a8836a9 | -14.03939 | -46.34276 | 2025-08-10 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 480508d6-c4c0-3246-a872-01545a9c414e | -14.29647 | -51.96767 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d3e9909-f203-39f3-a1c2-341c6ba9cc9c | -14.29039 | -51.96646 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 775042b4-eac8-3629-97a1-e42c0c65dfe9 | -13.59836 | -46.94232 | 2025-08-10 03:57:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 37de3b94-b3eb-38d7-8f3e-148a577bd5e4 | -18.1721 | -46.99165 | 2025-08-10 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c9e780ac-acf8-3634-8b8c-3ca3ffcbea2f | -13.11096 | -46.89768 | 2025-08-10 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b82cc903-6bed-3ea4-a27f-b0c0af7d4d7e | -14.28354 | -51.97224 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54226225-5a2e-3eda-8f1e-e07edeec1b67 | -16.38483 | -42.53488 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eae47fa7-d937-3c88-81ca-18e2c0360fef | -19.08299 | -43.5434 | 2025-08-10 03:57:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5696ca32-b792-347e-85fe-2c7d8bf483ab | -14.71667 | -47.51888 | 2025-08-10 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bf7f62e-df8b-3b2e-8225-f83c959a56d5 | -14.4667 | -47.84717 | 2025-08-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3b1b1d41-0560-3641-a0f7-a5c22f61a470 | -15.09673 | -46.54243 | 2025-08-10 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5756327f-9091-34f0-b68a-2bdfcf61df55 | -14.2955 | -51.97242 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ee5a627-d750-39d1-a133-7d6cedd78b34 | -14.10664 | -45.41034 | 2025-08-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad408811-f745-360b-9d50-b995028f5d7c | -14.45312 | -47.85631 | 2025-08-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f28d44da-6ef2-377d-98ad-3034e261d6a2 | -19.57538 | -47.23524 | 2025-08-10 03:57:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 857d3e60-1c31-3e51-8ba9-ee37093a9102 | -15.68927 | -43.21074 | 2025-08-10 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 48c66a67-b26e-3631-84db-c10fd9f014fe | -17.56921 | -47.50924 | 2025-08-10 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fbb80c7-db4e-3d89-bc4e-817604169675 | -13.63854 | -49.00121 | 2025-08-10 03:57:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a206651-0de1-37e6-82a4-0b1a40c63d6e | -14.29468 | -51.97948 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24f3b5cb-e32e-365e-b246-69db8f466c63 | -18.53544 | -45.01102 | 2025-08-10 03:57:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db0828dd-3004-36a8-b005-a90fb75218e8 | -19.88479 | -44.76189 | 2025-08-10 03:57:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75d8a791-5a93-32a7-aa53-d6dbd1886dcc | -17.95683 | -43.25494 | 2025-08-10 03:57:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 265fd24f-a924-33b3-a277-38d3fe00a3eb | -19.78082 | -43.72503 | 2025-08-10 03:57:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bc5c19e3-d2cd-35f5-b455-1ba4841428d1 | -13.6329 | -49.00297 | 2025-08-10 03:57:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc439e8b-c97f-3d45-8e13-0947074c9532 | -16.304 | -52.92292 | 2025-08-10 03:57:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b38b2af9-7ec8-3110-9857-98b3b215e374 | -12.71413 | -46.37164 | 2025-08-10 03:57:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aae9a763-6df6-3e50-9978-ed75db1d0277 | -12.58034 | -47.15201 | 2025-08-10 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e8336e4c-74c7-31f7-80b9-852a54e08002 | -12.70898 | -46.37518 | 2025-08-10 03:57:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7cbb7ff-6ab9-3f18-9b54-620592b4c244 | -14.29063 | -51.96875 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a0d141f6-05f2-3a59-99f5-a8b3895a2bff | -18.75632 | -40.59402 | 2025-08-10 03:57:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8accffff-9bbf-387f-b9ca-1c14a339e91d | -14.60034 | -47.16271 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7d17f9c-5fc7-36fc-b50e-48dc340d1d03 | -14.58527 | -47.15257 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64f8f3ab-ea5f-3bd7-8e37-c47b36751a24 | -18.26635 | -43.27562 | 2025-08-10 03:57:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5b0c3882-c636-3d3f-8553-d34baa0b5c3e | -14.29353 | -51.98201 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36b7fdb8-94f0-3434-bbf5-8f6f41d7589f | -13.62773 | -49.00235 | 2025-08-10 03:57:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdb41fbc-3e50-3bda-9597-92ad92cb79eb | -14.2957 | -51.9747 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1cac37af-cdbf-3c0c-a466-b1a6ff23a5b9 | -19.40249 | -43.35663 | 2025-08-10 03:57:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 41bb5f3c-f892-3c1c-b668-65a375895995 | -19.57947 | -47.23606 | 2025-08-10 03:57:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16424644-255e-37aa-9151-9a89f901b2d3 | -8.9401 | -60.7288 | 2025-08-10 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| effec780-4926-35e9-a70c-ebb6d2e89474 | -9.3808 | -61.5124 | 2025-08-10 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| f333175d-30ff-319d-a3d6-c860a2a3ab54 | -9.3806 | -61.5315 | 2025-08-10 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 5167a0b1-0c0f-3835-8cf3-0723d6209345 | -8.9215 | -60.7297 | 2025-08-10 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 35caa905-11a8-38c2-9834-c1d07b7d59a7 | -16.3731 | -42.5425 | 2025-08-10 04:00:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d442c606-ea4d-3ef5-a54b-def778401335 | -8.9399 | -60.7481 | 2025-08-10 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 2ecca200-6ecc-37a8-a839-a2a5f72c7865 | -16.3737 | -42.5178 | 2025-08-10 04:00:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 52.3 |
| e8e82512-a1e6-34c7-968e-a64471d8db88 | -7.0614 | -59.1972 | 2025-08-10 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 35835802-c0ca-3432-84e9-8a3489c4168f | -7.08 | -59.1771 | 2025-08-10 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 45755803-ee18-3998-a2ca-88800e9fbb4e | -7.0799 | -59.1964 | 2025-08-10 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 6c3b5721-bf03-3431-8cce-442c8fe3d22b | -7.0615 | -59.1779 | 2025-08-10 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |


[Clique aqui para ver as próximas entradas](README12.md)
