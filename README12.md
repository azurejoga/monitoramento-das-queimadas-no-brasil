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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b17287a-9fa7-3c0e-8fc9-d69467c8053f | -19.06314 | -52.85878 | 2024-12-18 04:06:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87c5be9d-ef32-3b47-9851-9d4758e3caeb | -21.58975 | -49.23437 | 2024-12-18 04:06:00 | NOAA-21 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f218ba0a-66f7-3e7b-852d-cc86a59354cf | -21.19131 | -49.86182 | 2024-12-18 04:06:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 75d98a88-a5d5-3c27-9a1d-f75dc779d298 | -19.06843 | -52.86005 | 2024-12-18 04:06:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f57606fe-f422-3d26-876c-e8350cd1b8f1 | -19.05716 | -52.86081 | 2024-12-18 04:06:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f529328f-5f12-3cfa-9e49-964d6dadc198 | -20.78198 | -49.8541 | 2024-12-18 04:06:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| eea4380c-ac70-3b1b-a8ab-1aeedcc47188 | -23.70979 | -46.89404 | 2024-12-18 04:08:00 | NOAA-21 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d674288f-8a93-32b8-a50f-615c38e71d2c | -23.40492 | -46.55625 | 2024-12-18 04:08:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f1fb2d29-032e-3dbd-b78e-235fd5358552 | -23.59596 | -47.43754 | 2024-12-18 04:08:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 21a77188-7be6-3878-8480-e601a3e2388e | -23.57818 | -54.74559 | 2024-12-18 04:08:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eb50da56-b34d-3ee1-9036-2b53fddf3462 | -23.34107 | -46.77143 | 2024-12-18 04:08:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f0b84495-38ca-33cd-9ad2-4d20997758f8 | -22.15493 | -55.28374 | 2024-12-18 04:08:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b610f97-4526-3162-8632-51a36fcc88c4 | -22.5418 | -48.81203 | 2024-12-18 04:08:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bbe0d08-8392-3ecd-8016-eb61abaab7af | -22.29773 | -49.70836 | 2024-12-18 04:08:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 92723383-846d-3717-b2a9-875c59cf71cd | -22.15392 | -55.28817 | 2024-12-18 04:08:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0400c0b-4df4-3699-88f0-71276ad9860c | -23.52061 | -46.97577 | 2024-12-18 04:08:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dfd17240-f8cb-36f2-b724-16c20ea6277a | -22.07012 | -56.20303 | 2024-12-18 04:08:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7851448b-19c9-3b89-9837-b274f5fcdbd2 | -23.63466 | -46.28587 | 2024-12-18 04:08:00 | NOAA-21 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c163e92e-43c9-37c7-8d00-916a4deddf45 | -22.29364 | -49.70742 | 2024-12-18 04:08:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f09e09b0-2516-3dac-b5cf-cb7a30b492cc | -22.20368 | -53.16004 | 2024-12-18 04:08:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4e608674-227f-3528-a3d0-a6ef8a83b643 | -23.78164 | -46.70605 | 2024-12-18 04:08:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| b6d00000-a34f-3df8-9cd4-f9c743bb57c2 | -23.63161 | -46.42597 | 2024-12-18 04:08:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 38646264-9904-3475-8909-a227b4bf34de | -22.92122 | -45.41332 | 2024-12-18 04:08:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 871d577b-ef17-34b9-97d7-ed13fcede4ef | -23.46856 | -46.47607 | 2024-12-18 04:08:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| be3d1d56-1ae3-3a53-9f74-266f637c2133 | -23.70419 | -46.47855 | 2024-12-18 04:08:00 | NOAA-21 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8ea76fa3-00df-33d7-a962-d96611c1b0b4 | -24.24467 | -50.74217 | 2024-12-18 04:08:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f126ce5f-e6b5-336c-b7e4-62835d28a4f1 | -24.24422 | -50.74192 | 2024-12-18 04:08:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| de49daf1-6edb-37f5-a62e-789460036257 | -22.0703 | -56.20364 | 2024-12-18 04:08:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67d09d0c-c169-348d-9202-649720ae5744 | -3.2317 | -46.8716 | 2024-12-18 04:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d0e8e69c-fc52-303d-9887-241e27aa07e1 | -3.2503 | -46.8709 | 2024-12-18 04:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ac742c2f-34e8-3c24-8a60-99229e637768 | -5.9369 | -48.0654 | 2024-12-18 04:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 3e13b042-a71a-34d2-a77f-523ae2c9310f | -3.2503 | -46.8709 | 2024-12-18 04:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 86605ef8-e551-37e0-9486-85e886a0c065 | -1.24985 | -46.39246 | 2024-12-18 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dced38d7-3900-3f5f-a301-5aa14e8c8e29 | -1.403 | -46.67987 | 2024-12-18 04:23:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57cd91c9-5a37-3946-8f84-b90930c5d2a5 | -1.54326 | -45.74243 | 2024-12-18 04:23:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e78abd5b-2f22-3b09-a48d-a249f7726279 | -1.47173 | -45.74193 | 2024-12-18 04:23:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bba73650-9791-33a5-a421-b2f033e17dfe | -1.37961 | -45.9625 | 2024-12-18 04:23:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61d53e6c-1e3d-3afe-8d7e-6c59a49923c0 | -0.75517 | -47.75602 | 2024-12-18 04:23:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8216e66-b085-340f-b83d-2529f9d28a7f | -1.04167 | -46.60173 | 2024-12-18 04:23:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f35e03b8-3fcf-3f24-ba50-ad49ec15557e | -0.75163 | -47.75546 | 2024-12-18 04:23:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 760330e7-da0c-314d-ba9b-b83c3f92f875 | -1.44788 | -45.74176 | 2024-12-18 04:23:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c69c4c7e-55c7-393a-a9e6-cb926e13152f | -1.40347 | -46.67943 | 2024-12-18 04:23:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dcffa82-0a77-31c0-924d-7c46521e0591 | -1.47118 | -45.74539 | 2024-12-18 04:23:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbfe2183-ed01-3467-b9ed-46440916ea6d | -1.38016 | -45.95901 | 2024-12-18 04:23:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54f3f409-98c5-3f17-b3b5-446ad4eead8d | -4.11922 | -43.56637 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b20dfc5-8908-3ff4-9611-1d234bf9f229 | -5.93479 | -48.07191 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96b0f487-c02b-3f7d-ace8-9f208451f0ba | -4.04061 | -47.02381 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a01ed8a-233e-3e6b-9270-7f0c9149838a | -4.44491 | -38.0618 | 2024-12-18 04:25:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f5bd84d9-bae4-329a-bc32-2b57f1faeecb | -2.70668 | -47.73079 | 2024-12-18 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7c91a17-8e4e-36f1-9c2c-f71c0a9b255b | -5.04471 | -43.21909 | 2024-12-18 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1fc014e-b55d-36f0-9368-c51a2ec9fdad | -3.95909 | -47.05856 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23550c50-04ba-3f90-8772-eef10b5a4160 | -2.36531 | -48.49314 | 2024-12-18 04:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dbe6bb5-73a2-366e-9250-c71426556c92 | -4.04117 | -47.02026 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bf084ee-4593-34f8-81c0-a28db69d3e85 | -3.93072 | -47.01369 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24ecab77-379d-37ac-9b97-194e95e665a9 | -4.01541 | -46.96515 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef1b1306-5dd6-3ef5-8305-0437afc3000d | -4.01701 | -47.04198 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bb036d2-8a33-398a-adb6-92e7197b430c | -4.97123 | -43.71864 | 2024-12-18 04:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 177d1b83-b708-376a-9ab0-90a7e71465b4 | -4.30285 | -43.89069 | 2024-12-18 04:25:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8817f664-07fb-362c-85d5-3ddbbdf40f99 | -4.98229 | -43.71638 | 2024-12-18 04:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 94376598-6883-3f0c-aac4-2a4ae7ee5a84 | -5.98808 | -43.48051 | 2024-12-18 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11c599e7-157a-3e0c-a113-edddb059ca39 | -3.9902 | -44.17229 | 2024-12-18 04:25:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 528af5e9-bfc0-3ebd-b097-a6afa96effc4 | -6.98195 | -43.56545 | 2024-12-18 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf73940b-a194-329d-8e1f-fac1ab0580d0 | -1.79267 | -47.06317 | 2024-12-18 04:25:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bcdce26-de8e-3d07-bd09-64bfdef51e97 | -4.12211 | -43.57075 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01a90818-ce2d-342f-b956-b54d6456ba2b | -5.87872 | -44.88483 | 2024-12-18 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aacce4f8-76a1-36c4-aad0-c84912d453fb | -6.98851 | -43.57065 | 2024-12-18 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c69d0ab1-b795-3e1d-9298-c0d3e4a4f7ad | -5.94343 | -48.06182 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37858a96-8059-39bc-ba4c-31a1b9b8f4fa | -3.65266 | -53.46169 | 2024-12-18 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13e8f68b-fede-32f8-b75a-22fcc8a04dec | -5.93598 | -48.06445 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7760ca6-4be5-3c2d-838d-55367594f7f4 | -4.16792 | -43.97355 | 2024-12-18 04:25:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71d8c413-9389-3433-89e1-63fc86bacbd9 | -4.01375 | -46.93217 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f5c33b3-a012-393b-b02a-5d9d11cca48c | -3.16327 | -45.97886 | 2024-12-18 04:25:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffa869fc-1399-303b-8443-ffa2271b2f9a | -4.00865 | -43.16496 | 2024-12-18 04:25:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a03cd6e6-9e35-3360-b866-1a60a6b4f176 | -4.01768 | -46.92915 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe8d9af0-15a2-3611-ae8c-fa9dd79639b0 | -7.15642 | -46.70062 | 2024-12-18 04:25:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d15204b3-72c8-34c0-bb34-76914b2d83d5 | -4.00971 | -47.04446 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4901f43b-8ac5-31eb-abfe-9e0d1bf95d96 | -6.63094 | -47.3451 | 2024-12-18 04:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc00743e-f5fe-3788-9965-c8020d0a2123 | -7.19877 | -44.92182 | 2024-12-18 04:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a41498e-214d-359b-9656-ff78068828b0 | -3.02747 | -45.23185 | 2024-12-18 04:25:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1b57c5bf-b48c-32a8-a97f-157988ee7bd0 | -3.16218 | -45.98578 | 2024-12-18 04:25:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4cf323d-6e64-3f5c-86a4-ecd303e15c9f | -4.44678 | -38.05739 | 2024-12-18 04:25:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 44415157-483d-3b48-a042-4da5fc5a4752 | -4.37617 | -42.94538 | 2024-12-18 04:25:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 668b6cc0-9655-3970-9b55-55c4de9a051f | -4.87853 | -41.40166 | 2024-12-18 04:25:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e9c4c72e-843e-3098-bf27-e83f6f90acef | -4.55385 | -45.72202 | 2024-12-18 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94fab9b3-b98f-3d06-b453-40d6e6d824fc | -4.03612 | -47.03039 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73c6962f-46d5-3e66-a037-bca48beddc02 | -6.14137 | -43.91284 | 2024-12-18 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fad5789c-1223-3857-9f49-2a93ec1709e5 | -5.21574 | -44.90754 | 2024-12-18 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ebb4def-f577-30a4-8840-fa66f223eaef | -5.81158 | -43.05354 | 2024-12-18 04:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 82b98993-b298-3043-8c4c-cb7b7e717185 | -5.94669 | -48.05788 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bcd487d8-3f76-3baa-a9bc-9daf6cd38f40 | -6.7565 | -40.12888 | 2024-12-18 04:25:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 247f0e90-8ef2-3536-b0f5-2dba4b2d5ae4 | -7.19537 | -44.92126 | 2024-12-18 04:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4983357f-0fa2-327f-9bbf-9025ed006df1 | -4.0588 | -44.91424 | 2024-12-18 04:25:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 0228b2e8-151e-356b-a242-75360f6fb7a9 | -7.15419 | -46.69315 | 2024-12-18 04:25:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea9fd5cc-6b92-3764-85dd-50c29295902d | -5.93822 | -48.07245 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b648141d-8221-3fe5-aa52-63997a2cad1e | -2.13948 | -46.4619 | 2024-12-18 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6bb9a0c7-3d1d-3360-b0e7-4f5cc5e39d6a | -3.92292 | -46.93222 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41e2d975-e684-31d0-80f1-7a519f7ab2cd | -3.0236 | -45.23479 | 2024-12-18 04:25:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 93c0d541-842f-3053-a042-fc3d9d184d59 | -4.54013 | -43.28922 | 2024-12-18 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be1909f6-3e76-347a-9304-c1ba3a839bc7 | -4.93604 | -45.09307 | 2024-12-18 04:25:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61e5d31d-8330-3ad3-b3ca-87ac39649783 | -2.28479 | -47.91151 | 2024-12-18 04:25:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
