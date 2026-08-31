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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91a87133-888b-39ad-a5a9-cf1d7e77b768 | -16.56762 | -52.50442 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d4c85d34-fa7d-396c-8416-2c64c21987d2 | -15.41942 | -52.67394 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ee7d086d-f277-3511-9242-9100362c883b | -18.20756 | -43.98164 | 2026-08-31 16:48:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4f3cfa0b-6147-32aa-9d9f-c03519920991 | -19.28611 | -47.1895 | 2026-08-31 16:48:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 77465ae5-a5f7-35b8-a720-46343eb08312 | -15.18991 | -46.23952 | 2026-08-31 16:48:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2601dfb6-1b69-3877-973c-e9984e24934e | -14.39703 | -53.02113 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 425d5713-9b08-3730-ad43-42ab60617823 | -17.22804 | -53.27341 | 2026-08-31 16:48:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 99e42010-f0d5-3168-acab-0ffa1f2054e7 | -18.26575 | -40.55079 | 2026-08-31 16:48:00 | NOAA-20 | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 0863e405-2a92-3fd1-9606-dd25a75627ae | -17.50459 | -44.22888 | 2026-08-31 16:48:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 8a0d2717-7dda-3f20-a151-4277ebbf0d91 | -18.66236 | -46.84741 | 2026-08-31 16:48:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 703fecb9-5f42-3566-bd33-c2281bc70616 | -16.14725 | -49.00859 | 2026-08-31 16:48:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 294884a8-1ab5-33d2-bf4d-75935a5b5db2 | -14.70158 | -53.59003 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 0ce1483f-9990-3011-a268-d8f4b3a93dcf | -17.20932 | -44.82796 | 2026-08-31 16:48:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 35ba9aeb-3981-39d8-a373-1d2eb4251fa9 | -15.54669 | -56.2803 | 2026-08-31 16:48:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4681ca44-11d9-32c5-9a6b-dc7f0132951e | -17.82561 | -44.45544 | 2026-08-31 16:48:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2eb11a90-b1a1-3118-ac9e-e758a0d6f5c9 | -16.71488 | -49.29726 | 2026-08-31 16:48:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9e8d78a7-064d-3699-ae48-078988e20037 | -17.56372 | -44.72199 | 2026-08-31 16:48:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cdbdc569-8d42-3ccd-a2ea-0e0c49787371 | -15.68434 | -48.22423 | 2026-08-31 16:48:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5115724a-184e-35f9-984f-c7663115be40 | -15.08941 | -48.36811 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 43a02252-3786-352f-86ae-be7595f1d657 | -13.06727 | -45.17549 | 2026-08-31 16:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 690c35bd-b2e3-31d2-8eed-7759964aed2a | -15.67652 | -45.94384 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8fb44784-f985-3439-894a-20da45059789 | -17.53163 | -52.55347 | 2026-08-31 16:48:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 937d12f5-6754-331f-8532-54c59c6258c0 | -19.2138 | -57.35741 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| b7ea684c-8f9c-3148-a971-a2a0eeaac807 | -18.27065 | -52.6981 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 32f449c8-d8f9-34d1-a422-5091a2c777e5 | -16.58113 | -52.51066 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |
| af7b5a71-ef33-3113-9248-fb5804007c09 | -18.98348 | -46.81951 | 2026-08-31 16:48:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 24b6de03-1f3d-3003-a1f1-49db5446081d | -16.9926 | -51.83957 | 2026-08-31 16:48:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 33.0 |
| ea309009-9aec-3474-a678-1cbc9cd1d739 | -16.27562 | -42.5826 | 2026-08-31 16:48:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d6911af2-419f-3896-8054-6a5ebb88ce7b | -15.11507 | -48.15487 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5463ae31-5aff-3f9b-b875-2859d286882a | -15.23445 | -56.39221 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 727e9c27-c3fa-31b6-8b76-28ec4ddf5729 | -14.39829 | -53.26918 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 614acb30-d75d-343a-bb4e-ab146f656da8 | -17.35171 | -44.9282 | 2026-08-31 16:48:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc140a9c-18a3-3eb6-868d-fd4c183cbc81 | -18.27118 | -52.70239 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 34.7 |
| b9bb0acc-8680-38cc-8c60-b123060783da | -15.99926 | -43.54112 | 2026-08-31 16:48:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 315025be-594d-3fb1-9f9c-b20eb156fb90 | -19.21293 | -57.34838 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.1 |
| e2e6a7e3-a6e3-3adf-978e-1120b79eec71 | -14.46104 | -53.3528 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5e19cdf3-5133-32ab-89b6-a108c659c8b9 | -14.79895 | -48.26361 | 2026-08-31 16:48:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 315246b7-82d8-3cae-bbfb-528e5a15da64 | -17.54232 | -44.61168 | 2026-08-31 16:48:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1ecc9ba3-f4c5-3037-9398-97f8f7672be1 | -19.17727 | -57.352 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.5 |
| c374ee8d-ba64-3a4a-895a-1dcf5b6c8844 | -19.12975 | -57.39164 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 0dafd660-4aee-3fce-9977-cda157afbe7a | -14.47075 | -53.32661 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4a4b2f43-0fed-3f9e-b172-60f5a01ae9ff | -14.59527 | -53.09184 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 77c5705a-1656-3f1e-b557-928f90765392 | -15.60799 | -39.96664 | 2026-08-31 16:48:00 | NOAA-20 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| e7f26c3f-ed03-3fd7-9e66-f9b671c673d6 | -18.12234 | -51.61241 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 1696c5b8-015c-3c25-8450-e4a27daed9f9 | -15.98355 | -55.95419 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 25.0 |
| 3b2337fd-87b2-3149-b40a-e3cf90202d54 | -18.26647 | -40.55473 | 2026-08-31 16:48:00 | NOAA-20 | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| ffad8854-284f-3b69-8f2b-3ed4df5726e5 | -15.50096 | -56.01431 | 2026-08-31 16:48:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 60d8a76b-5f73-3d30-83b8-e17bbe3093aa | -17.46202 | -52.4099 | 2026-08-31 16:48:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| a7dbec18-6090-3bda-811d-0e1b45388165 | -14.44541 | -49.00714 | 2026-08-31 16:48:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c6307be8-f1ca-3013-ad50-8a1b6f2a14fa | -14.57743 | -53.59674 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| fa02d595-c32f-325f-8e59-66ebf2439a43 | -15.05368 | -41.22164 | 2026-08-31 16:48:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 20177aca-26cb-3b83-993a-5d031d18ed99 | -19.16453 | -57.40827 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 62ccfb04-192b-3710-9ada-63b32e7fc3e8 | -19.20698 | -57.34898 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| af4d29ce-4a74-38d2-b35f-36628b418d5c | -18.41427 | -47.96542 | 2026-08-31 16:48:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e8603e4-1989-30e1-aeeb-2e45826b0388 | -15.73433 | -56.10275 | 2026-08-31 16:48:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 28f7489b-2f1d-3e3e-a206-c891d1b79482 | -18.89078 | -48.2413 | 2026-08-31 16:48:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ae382986-ad21-308f-8b88-6ad43b60d044 | -16.86618 | -48.27349 | 2026-08-31 16:48:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ddc2a7e-33bb-3be5-97ee-716f4ff2d12e | -19.47652 | -57.55787 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.8 |
| f59e0e8b-c791-3286-9888-5c14bc77b2bb | -17.3755 | -44.88122 | 2026-08-31 16:48:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| dcd68279-3bd9-3f35-ba17-9fa31653d491 | -20.26678 | -58.14386 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 7084b659-1acd-3269-8be7-3dbdaed4dc17 | -14.40274 | -40.66661 | 2026-08-31 16:48:00 | NOAA-20 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 781f52fe-94a7-3d8b-9fc6-80349f95415c | -14.51979 | -52.18228 | 2026-08-31 16:48:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 88fb8e3e-cff3-32e2-971b-acd937131aac | -17.79288 | -44.44921 | 2026-08-31 16:48:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 27b096b2-70d2-3fd9-8824-2fb308f68dc3 | -15.40302 | -52.71193 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fbbffad0-2f15-38c4-ae83-25ff1fe93de3 | -19.22525 | -57.3517 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.0 |
| ef6a16ed-71e9-3e43-afb1-e0ead403297c | -15.87634 | -56.47665 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4d3bec1e-58bb-3e80-9905-164208505e0a | -19.15261 | -57.4095 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.4 |
| a37e359d-8565-33bd-9d94-a6a4a98784bd | -19.16964 | -57.39857 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| cad6feef-1e29-32b8-a948-c240b3768be8 | -14.40306 | -53.27266 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e5278d24-b076-3a5e-9838-49e8c8b3321c | -14.48192 | -49.03993 | 2026-08-31 16:48:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a21f9783-4024-3a0b-8686-54474dac0fe5 | -13.6156 | -40.6448 | 2026-08-31 16:48:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 390bea68-8f8d-3553-b5f3-0855a7433124 | -14.47389 | -52.14071 | 2026-08-31 16:48:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1a7cbf42-5bf2-3baf-a91a-3d5895f70109 | -18.37991 | -44.45565 | 2026-08-31 16:48:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30d39cc5-9ae5-3b64-ae82-1a7a8309f6fc | -15.98318 | -55.95095 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 25.0 |
| b5f23a16-11f6-3cf9-98cb-94ef1cd4fe04 | -19.13818 | -57.38348 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.9 |
| f6d47382-f4b3-36fa-a8d6-658b46823fc2 | -15.50803 | -55.14049 | 2026-08-31 16:48:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c8560536-4027-3dd7-be13-09dac3fc0333 | -13.77194 | -42.72148 | 2026-08-31 16:48:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 54eac814-dc6f-307e-8aa0-52ccf633e53e | -13.09289 | -45.17921 | 2026-08-31 16:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 4f1d7654-4e1a-333a-8375-433f7e2b5e6a | -15.55655 | -56.27237 | 2026-08-31 16:48:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a49d69f-718c-3cb7-8ac9-dee6992d47d7 | -15.21328 | -41.75014 | 2026-08-31 16:48:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 72ac3bf2-c241-3962-a571-8dc1a401de37 | -19.09491 | -57.40437 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| dd2cc3fa-3d3e-3e50-9b89-b10c2bb3faee | -18.42105 | -47.96432 | 2026-08-31 16:48:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ae760b9f-7a6e-3b1a-83f5-956b74749b0f | -14.95463 | -54.57458 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6b54231f-f0a5-3be0-b1e5-bcf3435b87e2 | -15.55277 | -56.28659 | 2026-08-31 16:48:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 11d75468-3484-3a7d-9a11-b8bf90503627 | -18.41766 | -47.96487 | 2026-08-31 16:48:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9b90a780-17b1-374c-9338-9e3e6ec0e3e8 | -19.08852 | -57.40045 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| c9aa4bac-d4b5-3a1c-a4d7-ad24e1f2f3b1 | -18.26738 | -52.70728 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 42319dd8-e8ed-3b69-b41f-e985ad89b1a7 | -16.55932 | -52.51665 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 72bf721c-932b-3340-ab38-5bd03b8188ff | -19.10965 | -57.40018 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.4 |
| 8cdcf5e5-d8cd-3de9-aeb1-85dce3be6413 | -14.45871 | -53.1668 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| f8a6f151-3f99-3e7a-882e-6b685236d907 | -19.10374 | -57.3714 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.5 |
| 6912c9b1-049c-3333-ad67-715dd8b798b3 | -15.36889 | -41.18516 | 2026-08-31 16:48:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 1035a40a-f65d-3773-8240-2ccef608b575 | -16.86279 | -48.27399 | 2026-08-31 16:48:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be603f66-effe-300b-b562-1e69e3615994 | -18.8308 | -44.25101 | 2026-08-31 16:48:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cdbb819b-31a7-3fde-a8cc-7061e816817a | -15.50024 | -56.00788 | 2026-08-31 16:48:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9444de07-75b5-3dea-acb6-497fd2f344b7 | -17.85383 | -52.1058 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 3a6b974b-3eba-3ec5-b4e4-2725e24e2bf9 | -16.55414 | -52.5095 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 6258a7c3-1f4e-3096-ab56-53680f647180 | -17.86636 | -50.50203 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 255.2 |
| c350a0cc-b27d-388d-99ec-1d9cf411ec38 | -19.16029 | -57.3629 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 979b50b5-2f2a-323e-a55b-9e5b6bcdcbab | -17.88752 | -52.10559 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README143.md)
