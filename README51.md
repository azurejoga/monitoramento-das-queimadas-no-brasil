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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46f72589-ba28-3e25-b136-fece0c14ce1a | -12.99406 | -47.95589 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44cf7bbd-4f15-3bea-b798-5f772eea28e7 | -16.655 | -49.76069 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6be96917-6a53-320a-a4d3-50eb3be1ab3d | -15.90491 | -49.97005 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef4870ff-7da6-341d-99de-a405290aec84 | -11.34093 | -43.49238 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67f8b1d9-7aa9-3318-a802-e64ae5118845 | -13.75175 | -48.7692 | 2025-09-15 04:51:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2eeb932-33a0-39a1-88ea-724c21c2c20f | -16.28695 | -45.68222 | 2025-09-15 04:51:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e69f09b-ca34-30cc-a048-d734c566ee69 | -13.19345 | -47.28581 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3c33a440-013b-3c09-980c-19a94e19f19a | -14.50543 | -47.35068 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ebdfd84-13af-3cfb-84e2-10514966de43 | -15.77763 | -52.21651 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7919d5fc-1798-3130-a6bd-cf0656e636e7 | -13.21383 | -44.07575 | 2025-09-15 04:51:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77851205-b1d7-35a8-8718-ea0ca754ec86 | -14.14755 | -46.26174 | 2025-09-15 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e85e85d6-3170-3099-bc71-5a3f94e3c12c | -12.11723 | -44.84152 | 2025-09-15 04:51:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b34610c3-53f2-32dc-a202-3a85fb2df3d2 | -10.76472 | -50.63673 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbc5811f-6ef8-3c4b-9d55-d7bf57fc1ee9 | -17.18209 | -48.5895 | 2025-09-15 04:51:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4e9ad79-c74c-3227-ad80-d3af7d3489c6 | -17.17172 | -49.38346 | 2025-09-15 04:51:00 | NPP-375D | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6192795-1608-3d7f-9d90-42dc655b6346 | -15.32002 | -52.84285 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46ee759f-b9dd-3bcd-99f3-62b21f8db291 | -14.79955 | -51.60975 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 46a79ea0-8d52-372c-96c9-0bcb77e1b97a | -11.77226 | -46.66283 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fc93d5c9-f2da-31ea-b232-1d930727869e | -13.18621 | -47.27757 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09f6c0e4-73d9-3c20-a1ba-46eb39b92375 | -12.00739 | -46.66854 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d7491127-79c4-32d8-9905-1b242bbbabb4 | -15.7787 | -53.47102 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35a73961-32dd-396e-bcdc-3ff923950d50 | -12.083 | -44.87605 | 2025-09-15 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e224381a-9233-31e4-80aa-cf60c4b2b387 | -17.16792 | -49.38289 | 2025-09-15 04:51:00 | NPP-375D | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96cb65be-1406-3f6d-9c4f-a240638b4d4f | -15.68527 | -54.33898 | 2025-09-15 04:51:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 886b081f-5db9-32df-8344-698f2049318f | -15.77927 | -53.46741 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e78501a6-53ac-3bb0-a1aa-cc83bb40222c | -11.79848 | -50.46515 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c80a567a-460b-3eaa-91ab-c26dee095919 | -11.07768 | -49.73612 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6db6120-79f3-3fb6-af36-2613caec03be | -15.76937 | -52.21507 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6baa418c-26aa-307c-b9d9-79c33c12f95e | -15.10507 | -52.48315 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 45720397-b590-32dc-bbe5-12489273bea9 | -12.24659 | -51.06699 | 2025-09-15 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e2cd9c8-bf83-3378-90d1-cd4b0cbb37ca | -11.85827 | -50.50443 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fa631aed-5b1e-3577-94f6-6dec35418096 | -13.18839 | -47.29226 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6d588e8e-be12-3fc6-9823-53fe4745f1e7 | -11.76384 | -50.80534 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8731550-bebd-3d5c-a395-68ff60da7462 | -15.78317 | -53.46437 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 452b87a4-7aee-31a2-a7d2-c836ac98a067 | -11.7779 | -50.43889 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 755870d1-6062-3fd3-8c91-0491875af811 | -10.90546 | -48.18675 | 2025-09-15 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d89be065-f2e5-3156-8874-f2be8d89a889 | -14.1457 | -46.26019 | 2025-09-15 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a28b02d-7a65-343c-a009-c2cb259087b3 | -14.51367 | -47.35243 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| beaaa0bd-ecd8-3253-bed7-f9820bd7acb6 | -16.48265 | -55.11978 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6023206c-3476-3c83-9be4-eedcc43aabe1 | -13.90329 | -48.31326 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee16f315-1f30-3b4e-886d-01f91cde5a75 | -12.97879 | -47.97954 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6f8c624c-1e42-38c6-bc2f-8f5b9c7a3108 | -13.75485 | -48.77449 | 2025-09-15 04:51:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe27f1a8-7ca3-3e19-bd4f-2a61875f8162 | -12.42925 | -63.88884 | 2025-09-15 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 839b5a79-25d2-36d4-9411-aa8416103572 | -11.1264 | -45.30824 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 516e7a26-07a8-3b61-921e-f93660a6557b | -11.77119 | -50.80273 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b198cd1f-7bfc-3bfd-9c23-8410f931b769 | -15.0984 | -52.48205 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6204a7c0-7bb6-321e-a770-d129ee3b9e4a | -11.31521 | -51.14041 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21b32d17-f93f-318c-9d69-a3a4b035f19b | -15.79098 | -53.45831 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b5ff9344-850d-3612-ba29-76461d6a0c20 | -12.00478 | -46.65643 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65590fa9-0939-34de-ab6b-b204e555e898 | -16.66412 | -49.77629 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 087f0253-fb52-32fe-8984-c78f5e6d1dab | -15.78374 | -53.46077 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 87d06759-c2be-3c41-b358-1c6c1399ded3 | -15.90006 | -49.97816 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| decc715e-a4bd-3204-a0fd-e955380c8c03 | -15.75705 | -52.22803 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b4fb83a-3951-3005-81ab-80439eebf3e9 | -11.08815 | -49.71371 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 713c65c9-b08f-3696-acaf-1f9d79acafb5 | -11.80933 | -50.43995 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 6267d314-b81a-3389-b75b-31ad2219cbe9 | -13.86577 | -48.12785 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25897685-4cbe-3b03-9675-28bc0dc0bb7e | -14.43177 | -53.36349 | 2025-09-15 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 850601a5-6501-35ec-9d3b-7dfdf44c0d72 | -12.00111 | -46.65193 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1023b5fc-5aa3-306f-9a2f-c5e1185b71c6 | -17.06661 | -49.6778 | 2025-09-15 04:51:00 | NPP-375D | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1438d5fe-6a9d-3db4-9298-41c15c7f2385 | -14.4627 | -55.95906 | 2025-09-15 04:51:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41f0315d-8d8f-3bac-b5e6-cd57d84db022 | -15.11063 | -52.49149 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19a22940-918b-39c0-9a44-f79fe5b081f2 | -14.80688 | -51.60714 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7af70d3b-8ef2-3626-8bbd-b84c4bfedfde | -12.17172 | -44.09484 | 2025-09-15 04:51:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40129dff-5f7c-3433-89b5-3ff727a7b674 | -10.91236 | -45.56186 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3f1d004-a06f-38e6-9f33-b5a7c3aeedd3 | -10.92205 | -45.60036 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 769eb858-3a7e-3bba-aeec-e9704d2256e5 | -12.96375 | -48.00169 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c1ea4988-18fe-350a-a97f-fc20057b7222 | -11.77591 | -46.66734 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 28f1b389-caeb-3c85-921e-352947e400f9 | -11.76327 | -50.78643 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6539844a-bc40-3c29-85e3-7025311abfac | -10.66754 | -48.67658 | 2025-09-15 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b230b192-f6e2-394c-85e7-547ba5af7528 | -12.95656 | -47.99606 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7994256a-4203-344a-8429-8004b516cd34 | -13.88458 | -48.30531 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c1201e1-d764-39fc-8aff-3b617e088cf5 | -10.76416 | -50.64038 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d3908ec-a6ba-31a0-8698-cb9b979be5a3 | -11.32904 | -50.86565 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea8fd364-9387-3bd6-98be-f1ecae564824 | -9.69006 | -61.99942 | 2025-09-15 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7ab9b59-c9ef-3346-a160-114f15b25c98 | -9.14555 | -61.16306 | 2025-09-15 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b165c8c1-5e94-31ad-8404-fd6edb230d42 | -11.61481 | -46.59025 | 2025-09-15 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17b8de90-cf85-3fb9-9769-97c4b86ae44d | -13.00047 | -47.96728 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5f52c96-a1fd-3365-9b9a-4186f627307d | -11.74024 | -50.45605 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 071d81aa-30cc-3f2b-8e22-ab6fa5e11847 | -11.65279 | -46.5983 | 2025-09-15 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c85ac113-b628-33fb-aac2-d48097ad29f9 | -11.0806 | -49.74057 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d0e6d97-4cbe-3ee7-8dad-7e1a7bc8cdcf | -11.80248 | -50.43888 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bc6ecb57-7a80-33bc-9e4f-bbb4e2c54867 | -11.78533 | -50.4362 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d28ad83-b22c-325e-99c0-8f0a3fe78554 | -12.97951 | -47.97437 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| a6f2c239-4b17-3cc6-9bf4-a872baa3fd56 | -11.26536 | -50.82957 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 945b14a2-a426-30da-b050-84bf00c1250e | -17.73995 | -49.08698 | 2025-09-15 04:51:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e86ccf09-92be-350a-a5a2-1bf090390463 | -13.75927 | -48.77052 | 2025-09-15 04:51:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ef8958d-2013-3ac2-8558-3d581e2aadaf | -12.96313 | -48.00622 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 05508268-6643-353d-a528-e48a4f43b763 | -11.76444 | -46.65754 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6b23b3d7-4134-3fb9-9db1-af5bb8dd974b | -11.06548 | -49.71938 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d785fcaa-86de-3d3a-b6f6-9c8df5caa376 | -15.79775 | -52.19749 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9bfce1c-8a49-3c34-92f7-36044e8f09ff | -13.00829 | -47.96852 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83318056-0cd1-3990-b817-a0d4eb31d1d8 | -14.49305 | -47.34822 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e40f552-bbb4-3e51-8fb6-ecfc36b02ef5 | -15.7943 | -53.45888 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39e50e4a-5beb-321b-8635-fcd8b112ecb7 | -11.73681 | -50.45552 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd2a4fac-24a2-3064-8a0b-5393c924278a | -12.09451 | -44.86239 | 2025-09-15 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54d7c2fc-9884-3e7d-b4b2-c32cd457e672 | -15.66533 | -52.24282 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae395c6d-65c9-3eee-8db4-21caf6c09866 | -15.76825 | -52.2224 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d30102f3-5052-368f-9e52-dcc6b8fb6554 | -11.71995 | -46.4845 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 448e6572-360b-34b0-9727-b63c61fbd9df | -18.71295 | -44.27522 | 2025-09-15 04:51:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c68e368b-8bc1-3857-a818-865634d1b680 | -11.76271 | -50.79011 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README52.md)
