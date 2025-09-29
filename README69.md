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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a1a13b7-7703-39c8-bb10-8bc5eae47ce9 | -16.40949 | -47.02807 | 2025-09-29 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89c5ac04-381f-3307-8327-19f2afc90210 | -15.6135 | -46.25076 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f4f7a65-af23-3b07-aed5-49b7cfadfd18 | -15.41642 | -48.22442 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da74628c-3456-30a4-b85f-56b6244b3694 | -11.81262 | -51.79604 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e2b0040-2686-37d5-b3eb-7d8a88333241 | -14.52051 | -48.39243 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab72ebab-4e32-39e5-ae32-37cb34900049 | -10.38194 | -58.5153 | 2025-09-29 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73ae696b-d28a-33d1-b069-0db13a8eb1d5 | -14.71547 | -45.20927 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87665fe3-0b63-3da1-a400-68d34ea0148d | -13.16976 | -47.44538 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32b1c5ee-68ca-3433-81e4-e83c62c8694b | -12.21245 | -43.74221 | 2025-09-29 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c1edf06c-0e15-3aea-ba26-7fd4aeb74841 | -15.2791 | -47.87112 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 214c3213-3be3-33d3-9c75-bf903ca4e92d | -11.83792 | -51.80428 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe854ffe-8391-3f09-961e-ea1d883818a6 | -13.79392 | -47.88486 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7b023acd-331c-3282-9d31-09bf1e9ff4f2 | -12.21534 | -43.75008 | 2025-09-29 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afe53342-643d-3d35-897c-4274793e4fe5 | -15.52929 | -48.51021 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f301981f-c0c7-3649-ae47-acc4fd3005e7 | -16.84977 | -45.79982 | 2025-09-29 04:59:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90640b3b-49ed-3f56-b98b-317c030faab2 | -14.56696 | -48.24901 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e5279bf-926b-3882-a90f-d8e0eb3f6b64 | -12.35688 | -54.15083 | 2025-09-29 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc1c55a7-7ae9-3f64-ab1c-eac5445187a2 | -12.80071 | -47.75513 | 2025-09-29 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e7f51525-f82c-3a78-a87c-aefb5d1951a2 | -12.00639 | -46.63188 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37acdce3-23a7-3c74-b13d-e84bf117a5ab | -15.47045 | -47.93286 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6bab209-440f-3e4d-8576-2e94072ba564 | -16.52953 | -46.95353 | 2025-09-29 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89f977ff-e560-3e62-aacc-78d9ee5cdbb1 | -17.09278 | -48.57217 | 2025-09-29 04:59:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 52c46d0f-2a64-36ba-8215-0eaf89ab5907 | -15.86968 | -46.21453 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c182b3b0-0f57-391e-b994-0450acc5edac | -15.32533 | -47.91307 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ea763dd-321b-3999-a7ea-eb10a7120fb3 | -15.28276 | -49.49608 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 056433b1-d9cd-3ebe-b475-3d5598e40d93 | -13.5959 | -48.06211 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c58f3234-f47e-325f-bbf4-835b4fc83f79 | -15.47579 | -47.93067 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3fd1225-008a-362a-9652-1f6272c422ac | -14.44326 | -46.36185 | 2025-09-29 04:59:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2002fb5c-b4bc-3d25-aed2-69600520fc78 | -13.79309 | -47.9318 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 197f654c-75d6-3f3a-b6c0-af06469b0635 | -12.69586 | -46.89957 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d623a738-1ef7-36fa-b6cd-bc4aa7a57fbc | -14.44367 | -46.35814 | 2025-09-29 04:59:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71b616e2-8bc0-30c6-abb8-8cf466ee6954 | -11.76738 | -47.56447 | 2025-09-29 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a12a99d1-77b5-3fb3-af61-6190c682f053 | -12.45866 | -54.19633 | 2025-09-29 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58b78cb3-2408-390c-baf8-52dc0c09029b | -13.63729 | -47.33157 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74c3479a-2a19-34e1-944a-a0b91aac1600 | -11.91532 | -47.9739 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccb8eaaa-25e4-3ec8-b3c4-70def5cbc38c | -15.65187 | -46.26408 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e64fc07-fcce-3e1c-95c4-e9d5471f3383 | -13.26102 | -48.44558 | 2025-09-29 04:59:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c53927c1-e763-3cf3-a9d4-0380bf86e05a | -13.55849 | -47.27109 | 2025-09-29 04:59:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 124906ad-ab60-3781-8d1a-09817bbe4928 | -13.77505 | -47.91669 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 00d0dc93-a87a-35b6-92cf-0983bc5e0544 | -13.76596 | -47.90957 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e071246b-194f-356c-9a4d-edda608caab2 | -15.60661 | -53.15245 | 2025-09-29 04:59:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7937cb90-62f3-33f8-bfba-87bfd009c91c | -16.50278 | -46.02931 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bc5fc1a-4a0d-3e57-ab2f-99b68a59cb3e | -13.76399 | -48.31968 | 2025-09-29 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dc11b15a-c678-3d18-94b4-8bc4b3b66088 | -14.59081 | -45.01848 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 952f6dbb-425e-37b5-8f56-090af4886ec5 | -13.41844 | -48.19926 | 2025-09-29 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 56b18184-b333-351b-b56f-a49810e021a5 | -14.56628 | -48.25473 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f1721790-5b88-39c5-a0a1-57d4aabfe3cf | -11.70084 | -44.44143 | 2025-09-29 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29df1119-cb9b-3fc8-9a94-7ddc2fac0e68 | -15.05266 | -46.96924 | 2025-09-29 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a463115-3906-3e0a-87e3-34d8c564150c | -12.95856 | -47.20912 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44f119a7-eede-3d0f-8ddd-c8bf0e055d6e | -15.28845 | -46.41531 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 150ba8df-620e-3055-97ee-372dd7fb4ad9 | -14.6204 | -48.2944 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69df6159-cbc4-3670-911f-22514b362d45 | -13.00811 | -49.44841 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 349ce04a-3b90-3034-86c2-2f68252532a4 | -15.27924 | -48.04039 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 854517ad-8dcc-3534-b3b1-7336ac92f2a6 | -15.42067 | -48.23075 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54a4eb77-ef22-3589-98dc-9d480d437848 | -12.4528 | -54.30381 | 2025-09-29 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d3a2ac8-00b8-3ad4-88e7-6c5642d90d69 | -12.01219 | -47.78899 | 2025-09-29 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a73a1932-db43-396a-889b-43f29f2e6e72 | -14.53812 | -48.4484 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| cd1717a6-d368-3194-8059-88d0012879ba | -14.57248 | -48.24403 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c0cfd6b-54ee-30bb-98c8-861fe1a3160f | -14.70951 | -45.2088 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1527b0e6-d755-36a7-87e5-1b0a54561cc9 | -11.00029 | -57.06176 | 2025-09-29 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17bebc1b-261d-3da7-af08-0c87a06bf46a | -11.83919 | -51.79532 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be7d3f0b-0007-3cee-ab03-6b8c49728496 | -11.92227 | -48.03316 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f5fff092-eae5-311c-aec3-92c63f8728a0 | -15.28552 | -49.5107 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7ed40810-d37a-311b-b796-b18931569366 | -13.97871 | -49.67482 | 2025-09-29 04:59:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9960dcd-3aa3-3c66-9e06-224be64c80a9 | -15.52187 | -47.92829 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a62de4d-85e6-3653-85c3-44004dc2d099 | -15.29505 | -49.50747 | 2025-09-29 04:59:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0dc50a80-c914-3055-9b9b-8feba534d254 | -15.07816 | -48.33915 | 2025-09-29 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63e23549-0b7c-3223-b025-c72bea61179e | -13.03008 | -49.4504 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7efaca3b-3862-365e-b791-d184be5722cb | -12.8014 | -47.74955 | 2025-09-29 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12705ac6-0437-33b4-83d9-15e1336fcdcd | -14.42026 | -52.2463 | 2025-09-29 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5a66a1b-842e-38bc-8912-d6773b6b4436 | -13.01636 | -49.45334 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3847bc6c-c5aa-3a48-bdf5-e2e32b41a455 | -15.50357 | -45.88238 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c61bded-f9db-3a77-89ce-67a46e399937 | -12.65389 | -46.92495 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c201485c-83f2-3d02-ab02-9e7c7268f71e | -11.80911 | -51.80251 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b97c022-bc51-350d-ba45-a2868692635e | -11.99724 | -47.11161 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 182883bf-62c4-3132-ac95-e14f45bc6cec | -15.19743 | -48.47467 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 92f0d853-ae36-3750-b4bc-21d957ce6630 | -15.62069 | -46.25403 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 110cab93-8b80-3ae2-9534-2a33e2cc6473 | -13.76052 | -47.91332 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4a22176d-b419-3ef5-a438-7f24b00dccb5 | -13.19671 | -47.39192 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2875d287-7842-32de-abc3-ad080404cb84 | -15.42838 | -48.24996 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0f9dd3b2-ca13-3371-ae87-53136b884967 | -13.03066 | -49.44592 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a98db84-ba81-30d0-8ec8-e3d717e7885d | -13.74829 | -47.891 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe0f58ec-dfc4-3ce1-8862-45687dd2bbad | -14.54866 | -48.40136 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8085e30-23fe-31c0-b0e4-05d476b39fb2 | -12.70002 | -46.90859 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a6563c8-ab15-38bb-9add-1b8ad53e35d4 | -14.49135 | -48.54689 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ffcc82b2-375e-3bd1-bf2a-bb6a22b590db | -11.98086 | -47.12481 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dee736ef-9d42-383c-8db4-ac71fa5c72f9 | -15.04687 | -46.9728 | 2025-09-29 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5eeafd92-9c10-352e-be9d-7318f3e9edf4 | -13.80155 | -47.94381 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8a020730-cd41-3471-8ba3-3fd79fd37337 | -12.01511 | -47.95163 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d8e76a7-f246-3440-9f28-a011c389c559 | -15.53874 | -47.87262 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87f36b14-31c0-3285-84dc-460d7d1f569d | -11.92765 | -48.02878 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 3d73daea-49aa-34ec-82a5-1130946d1c2d | -14.58427 | -48.22785 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c805e298-88bb-3207-b452-4e67d3210117 | -12.93594 | -46.7688 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52d94cd3-f2a5-3d85-aae6-758b2ed88a54 | -13.60186 | -48.05348 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5f66b9ad-34b7-3031-ab45-698baaee79a2 | -13.83471 | -47.93892 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cc8d0e0-a7f3-3901-98b2-7c83c96f8af3 | -15.54186 | -55.75719 | 2025-09-29 04:59:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d39ee3d9-199c-3017-b36a-6fc55b337189 | -13.23059 | -50.95331 | 2025-09-29 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 674317ce-749d-32f4-aafb-29c5116f21ba | -12.92077 | -47.15196 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 770c0c44-3ff0-3eee-b6bf-7813365192e0 | -14.44255 | -46.36014 | 2025-09-29 04:59:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d77f8aa1-c6ad-3bdf-a08e-7b6b4c6709cb | -11.94215 | -43.91504 | 2025-09-29 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README70.md)
