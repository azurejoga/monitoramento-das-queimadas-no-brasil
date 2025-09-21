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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2960508a-cac0-3c09-8af8-5d54f61bbf69 | -20.51044 | -42.3789 | 2025-09-21 04:12:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e07b06bb-1bbd-339b-8dcd-5bd6cf1f369e | -22.78205 | -55.368 | 2025-09-21 04:12:00 | NOAA-21 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 72d84875-ce0c-3bee-b9f8-03c82648ea59 | -22.17588 | -46.7414 | 2025-09-21 04:12:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 20506cc5-8a71-3253-954e-a43b1e0b30c2 | -23.41969 | -47.61219 | 2025-09-21 04:12:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5c5c5383-1d2f-3a9d-bf81-0a0266f81f42 | -19.83896 | -57.29682 | 2025-09-21 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 930713da-2670-3911-9412-72e69ec43ffe | -23.14693 | -47.62243 | 2025-09-21 04:12:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 647b3bbe-ffea-3703-ad45-62d0b2f676bb | -23.23102 | -47.62548 | 2025-09-21 04:12:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 46afd415-e3b1-33d8-aec7-aa0e9a942524 | -20.54521 | -56.15174 | 2025-09-21 04:12:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 357abb34-9019-3e3f-897f-530021b94780 | -23.40625 | -47.07952 | 2025-09-21 04:12:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 040eac48-d3bd-317e-a3e5-e4d40f9474e4 | -22.47016 | -48.21271 | 2025-09-21 04:12:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0e4b582e-63a1-3bd3-ba0a-33122ad18e11 | -23.38018 | -46.35932 | 2025-09-21 04:12:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 8fef5d51-559a-3a67-aeb3-3d2fd26fc472 | -20.45741 | -43.25655 | 2025-09-21 04:12:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 41505bc6-b00a-3b75-859c-090e45e90cb0 | -18.74882 | -53.32663 | 2025-09-21 04:12:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25fc80aa-ba9a-395d-a224-35f978302162 | -19.90654 | -44.71997 | 2025-09-21 04:12:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed5a1f40-4855-3779-aa3b-7235b38e0592 | -19.84285 | -57.29708 | 2025-09-21 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 910cbfb4-5924-3866-b359-de8b48bf6614 | -21.62729 | -51.99026 | 2025-09-21 04:12:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f8cd39e5-868a-31cb-b14c-be8a807a17c7 | -21.69509 | -44.27154 | 2025-09-21 04:12:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1b13e65e-9546-330a-a03c-c2bf8d04fd4f | -19.84904 | -57.29866 | 2025-09-21 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b3530277-123b-3b5f-858d-bda07647f0b8 | -23.157 | -46.64523 | 2025-09-21 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f168ee31-2062-3798-8601-99105abe2a6b | -20.27498 | -42.70463 | 2025-09-21 04:12:00 | NOAA-21 | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e1397b08-cf20-35f5-98f9-ed8141a569b1 | -20.53904 | -56.15344 | 2025-09-21 04:12:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c90c3999-4556-3ca8-933b-c96c2902c15f | -22.22487 | -56.01115 | 2025-09-21 04:12:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 757adb6d-4d4c-33ba-8866-733608f28e85 | -22.22541 | -56.01259 | 2025-09-21 04:12:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9abfc503-30e0-3b06-80e0-e3175f51c4c2 | -20.54614 | -56.14758 | 2025-09-21 04:12:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f68dd11d-fafe-33b9-8536-1b9a5d547ed1 | -20.68998 | -43.19819 | 2025-09-21 04:12:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9be96065-e443-3375-85fe-2a47012ce3e5 | -19.9071 | -44.71632 | 2025-09-21 04:12:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7e6fae9-0d86-38b3-a70d-5e76c9b244b8 | -23.48346 | -45.4258 | 2025-09-21 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0e0cc6b2-0e72-3906-a938-cd577636e938 | -20.54576 | -56.1505 | 2025-09-21 04:12:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8cba5da-b25b-3d3f-873f-a12c39c152c2 | -23.5083 | -46.97482 | 2025-09-21 04:12:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e9ad2a37-97f3-3ac1-bdce-1361b52282e0 | -23.444 | -47.61601 | 2025-09-21 04:12:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c06c5884-00a8-319d-95ab-ceff147f0804 | -21.11641 | -42.98334 | 2025-09-21 04:12:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b4403eae-c1cb-3767-a657-c804f56f3f60 | -20.45797 | -43.25271 | 2025-09-21 04:12:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 61162d8d-7194-32b7-9777-a163ef036b07 | -20.12473 | -42.48014 | 2025-09-21 04:12:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c498308e-ee12-397e-98ea-d6649f57da2b | -19.80631 | -44.11383 | 2025-09-21 04:12:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cec17ad-9e1d-36f7-be5d-578dba7a4ec3 | -18.73789 | -53.3325 | 2025-09-21 04:12:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e105126-f388-320d-a621-8ae90bdcb555 | -20.47839 | -44.23084 | 2025-09-21 04:12:00 | NOAA-21 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f7edc0e4-3b04-30bc-8440-b05f98e37ec5 | -22.47366 | -48.21341 | 2025-09-21 04:12:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| acb7ac09-310f-3a16-b863-5c34fc5810d5 | -20.53852 | -56.15468 | 2025-09-21 04:12:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed6e387e-27bd-3634-87e6-86bb6239aae4 | -24.68496 | -48.33124 | 2025-09-21 04:12:00 | NOAA-21 | ELDORADO | SÃO PAULO | Brasil | 3514809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f32fed8c-f052-3787-be82-39f2deae247c | -24.75342 | -48.81957 | 2025-09-21 04:12:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| f667a302-6482-3c75-b90f-0aad9b4e2b4b | -23.37811 | -45.42578 | 2025-09-21 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 092120ad-de17-3a09-95a2-b9180aa40528 | -20.68658 | -43.19764 | 2025-09-21 04:12:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6d393799-3e86-3df2-afb1-27197ec66017 | -23.47635 | -47.2729 | 2025-09-21 04:12:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| db434131-d235-318d-ac94-bb46080d03ea | -23.24652 | -50.85872 | 2025-09-21 04:12:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ba3d8980-931e-3d96-8f41-39459ff9e5bd | -22.71311 | -52.87126 | 2025-09-21 04:12:00 | NOAA-21 | ITAÚNA DO SUL | PARANÁ | Brasil | 4111308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd742958-22de-3718-9907-57feda064793 | -24.75599 | -48.82181 | 2025-09-21 04:12:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| cb9b2a92-c432-3e7e-8e6c-d7ed4311660d | -21.66963 | -44.08179 | 2025-09-21 04:12:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1ecc8ff2-5b82-3bec-97fc-ea20f42d007a | -24.6877 | -48.33598 | 2025-09-21 04:12:00 | NOAA-21 | ELDORADO | SÃO PAULO | Brasil | 3514809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 89967a07-b629-3ea1-aeb6-8b60e8ffa138 | -23.53489 | -47.618 | 2025-09-21 04:12:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4e03453b-9273-37bb-9365-15f81a78d1f1 | -23.22316 | -47.02477 | 2025-09-21 04:12:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a95bc293-ae33-398a-96d0-5a45592daba6 | -22.73979 | -47.283 | 2025-09-21 04:12:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 356dae96-e9ad-3ffc-bcbe-13ebea94283d | -21.29471 | -43.88845 | 2025-09-21 04:12:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 30ec26b3-a56d-34f7-a380-ea4e9ba25868 | -18.74474 | -53.32446 | 2025-09-21 04:12:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ef436d3-ff3a-3104-8156-386520a85dbc | -22.27025 | -56.01586 | 2025-09-21 04:12:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e7c941a-e26d-3b82-a3e8-8f2ec17cd439 | -20.94435 | -41.54394 | 2025-09-21 04:12:00 | NOAA-21 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6714e3f3-7152-3d4a-bd9d-32af99b6d42b | -20.41354 | -42.93118 | 2025-09-21 04:12:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| be81385c-ba65-3b35-b11d-6bf9dd291ada | -23.21679 | -46.42153 | 2025-09-21 04:12:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 12a13b6c-1f29-3a48-8086-ac5f342f72b1 | -20.53429 | -56.14777 | 2025-09-21 04:12:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38270a0a-850c-3a18-ac5a-56ce54ef8d0d | -23.68009 | -46.25161 | 2025-09-21 04:12:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 19531dd9-b2c5-3620-a3f1-7c0cfed0bc8c | -19.89373 | -42.67763 | 2025-09-21 04:12:00 | NOAA-21 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 578d2150-afc4-3e54-bb2e-94cb5359e7ab | -20.12531 | -42.47606 | 2025-09-21 04:12:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3b535c25-7648-3293-8a2a-a5499f8bacea | -23.3272 | -46.91757 | 2025-09-21 04:12:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 231c5c67-d303-39fd-ae77-ab718972a051 | -23.48016 | -45.4252 | 2025-09-21 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 57a91ae9-5dcd-3c96-8bc5-c34e0dc07f13 | -23.36324 | -47.15115 | 2025-09-21 04:12:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d2c85552-424a-36ce-9a37-efece49c4edb | -19.68238 | -43.94587 | 2025-09-21 04:12:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60561aac-4579-31b1-8695-d565a4406b85 | -21.29137 | -43.88785 | 2025-09-21 04:12:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 490ffad9-22c7-30b3-8299-00f8865d4bd1 | -23.47234 | -47.27612 | 2025-09-21 04:12:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 121f470a-d6aa-372d-ba18-58a0c2b0b552 | -20.54314 | -42.27446 | 2025-09-21 04:12:00 | NOAA-21 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| edf1f5c5-7c8d-3f39-b449-c3bb6be6d103 | -22.22634 | -56.00837 | 2025-09-21 04:12:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de7b9985-a846-3b59-8098-c9a27b074b53 | -24.96476 | -48.58736 | 2025-09-21 04:12:00 | NOAA-21 | BOCAIÚVA DO SUL | PARANÁ | Brasil | 4103107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7808d7f2-e83c-32b9-965e-e34efcf2dfdc | -23.22523 | -47.03313 | 2025-09-21 04:12:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| e71a72f6-e646-3d24-9833-ac9b5c104212 | -19.71657 | -44.01208 | 2025-09-21 04:12:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e37d588e-2f27-3297-9ddf-7250baef49c6 | -23.16246 | -46.64941 | 2025-09-21 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cdf3115e-0140-3b9f-bcee-ba591da239a0 | -21.28803 | -43.88726 | 2025-09-21 04:12:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4819086e-91ed-3682-9e10-a41e054c5255 | -23.15034 | -47.62308 | 2025-09-21 04:12:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 455020d1-5662-38c1-bc60-dcabfcd87d11 | -21.33694 | -46.72567 | 2025-09-21 04:12:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 7fda83fa-4085-371e-a0fb-ba348cc7515a | -22.63734 | -48.25388 | 2025-09-21 04:12:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2072aa6a-2d08-3c29-ad90-6482f4a92018 | -23.15913 | -46.64879 | 2025-09-21 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 34c21cf2-445f-3fe2-9d56-e25f32caa7c4 | -26.71187 | -51.68131 | 2025-09-21 04:14:00 | NOAA-21 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1545acbb-abc8-3669-aed6-0a067001d45a | -28.28971 | -50.3554 | 2025-09-21 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 9e9762a2-1a12-3eec-a249-1f3fd78a4530 | -25.21195 | -52.66323 | 2025-09-21 04:14:00 | NOAA-21 | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a71e2097-60a4-3db3-801a-f48af0829a85 | -26.18075 | -51.73447 | 2025-09-21 04:14:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 745ce5f9-f82d-3f0f-a9ee-50f2298ff2c1 | -26.18134 | -51.73911 | 2025-09-21 04:14:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3ade109e-cfe2-30f0-a00b-dd405045d188 | -26.17742 | -51.73812 | 2025-09-21 04:14:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| c9d556a1-633e-3de2-93ad-7a5f038a5b1a | -25.24293 | -49.65416 | 2025-09-21 04:14:00 | NOAA-21 | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 866c55c0-dc57-35c7-af84-e953b217ef1a | -28.28531 | -50.35923 | 2025-09-21 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9431585d-f93d-36c1-b2ad-626adb5889f4 | -28.28718 | -50.36937 | 2025-09-21 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| db88d825-158c-3121-8f87-4f478debb689 | -25.05612 | -52.19171 | 2025-09-21 04:14:00 | NOAA-21 | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c38927fa-6c28-3775-a8c7-72482b225fd6 | -26.17852 | -51.73238 | 2025-09-21 04:14:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 6d003ce3-f6f6-38aa-a8a5-1f01b84eb02c | -28.28425 | -50.34458 | 2025-09-21 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 45c3e9e6-8103-32c2-a4d7-d1ddc88e001e | -28.28257 | -50.35381 | 2025-09-21 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b16862ba-da79-36e2-a289-262b360883d9 | -26.17682 | -51.73351 | 2025-09-21 04:14:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 88d76bde-b0fc-33d4-b557-b34940ed9070 | -28.28698 | -50.34998 | 2025-09-21 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 5688e0bc-1451-3235-9796-d3297c974617 | -28.28341 | -50.3492 | 2025-09-21 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f3041500-a84e-3cf7-9671-023b54d176eb | -28.28781 | -50.34536 | 2025-09-21 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 66750649-27c7-3ecc-8412-288e15361c40 | -26.17961 | -51.74024 | 2025-09-21 04:14:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| c368e413-68c0-3daa-a190-7f21dfc9f4cb | -25.15435 | -51.97012 | 2025-09-21 04:14:00 | NOAA-21 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c21f9159-d2d7-365a-8acf-715beef5b58e | -25.15108 | -51.96997 | 2025-09-21 04:14:00 | NOAA-21 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0917ff5a-cde7-31cf-99c2-63908b4f787c | -28.29159 | -50.36552 | 2025-09-21 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 208d3834-1130-331b-81b3-630809a02229 | -25.1551 | -51.97116 | 2025-09-21 04:14:00 | NOAA-21 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README20.md)
