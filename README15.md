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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa9130d8-18ff-3ce7-bba6-341db4b1e822 | -14.59386 | -48.8584 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f3f3a09-19d1-332c-8f3a-23d7db66a961 | -16.51118 | -41.62584 | 2026-09-11 04:10:00 | NOAA-20 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 960a0d75-456a-3c30-8279-6724152c56ce | -14.0606 | -44.03109 | 2026-09-11 04:10:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 06988a5f-1dee-36cf-b058-6067c925775c | -18.63631 | -43.22809 | 2026-09-11 04:10:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ec5117f1-9d33-31a7-9596-021e6e459650 | -14.95274 | -47.52276 | 2026-09-11 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14327d4c-1ac3-3980-8015-419a44551fe2 | -14.59901 | -48.86756 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a011b53c-beab-3132-b3b2-840423242244 | -13.4367 | -43.81503 | 2026-09-11 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f09dda1c-ee9e-38a9-a9d0-718a13d5b1e4 | -14.61596 | -48.85157 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49db745f-af31-3415-a6d2-a9581580d88b | -14.66045 | -44.12166 | 2026-09-11 04:10:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 46e19090-625b-341c-b934-843471ea1f69 | -14.0419 | -43.85113 | 2026-09-11 04:10:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d21cf9e-39cd-3175-ba86-c142b334ac50 | -16.31262 | -48.84983 | 2026-09-11 04:10:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e552d267-47f8-3189-b711-08033eb236d5 | -14.67291 | -44.13181 | 2026-09-11 04:10:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6443c074-ae33-398b-b9db-757734665d22 | -14.91031 | -44.6715 | 2026-09-11 04:10:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 062e063c-723d-3120-aa0e-438cad964faa | -19.49664 | -45.22463 | 2026-09-11 04:10:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a00e2e6-2a1a-3b5d-a039-0786dabf3533 | -14.90937 | -44.67205 | 2026-09-11 04:10:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9d11c54-18f5-3143-9cea-0a630dd9e56d | -17.02032 | -41.38171 | 2026-09-11 04:10:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d85d9cbb-f08a-3480-b107-c8a09d7bc290 | -14.60348 | -48.86843 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9152db44-f6d4-36d1-b5f1-3f01c29c4ea0 | -18.08276 | -46.84653 | 2026-09-11 04:10:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7186eb3-a91b-311f-92e0-aacc21b8abaa | -14.67216 | -44.13088 | 2026-09-11 04:10:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4927cb86-3923-350a-8f93-78c17c273493 | -16.75737 | -51.87043 | 2026-09-11 04:10:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43937392-8cb1-3a50-8ea2-84c75ca93677 | -19.67755 | -44.16389 | 2026-09-11 04:10:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2dec01c4-986e-39f3-afe0-7ace58ce1545 | -13.55032 | -44.16913 | 2026-09-11 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dee780d-ce9a-3e0f-86fd-c20ed6dfb429 | -20.48701 | -57.46537 | 2026-09-11 04:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8de81cde-044c-3623-a759-ae6385267408 | -20.48546 | -57.47184 | 2026-09-11 04:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f78bd89e-c88b-3499-b784-9e9cc85e851d | -22.26801 | -55.84093 | 2026-09-11 04:12:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5428ff4-bc7b-3222-9e96-36b48636dd6c | -22.27733 | -55.84506 | 2026-09-11 04:12:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 617c9003-327b-3441-9582-69eeeb822169 | -22.27393 | -55.8425 | 2026-09-11 04:12:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 099b9dbb-0786-3cde-aa5c-086b8b294811 | -22.25845 | -55.84512 | 2026-09-11 04:12:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab3210cc-11e9-346b-9b83-0afa6d24eb8b | -22.26548 | -55.84193 | 2026-09-11 04:12:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1e2d083-89f7-3a99-b1a5-314bcd5a64c3 | -22.26571 | -55.8505 | 2026-09-11 04:12:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7910ec55-f02d-3c65-96c3-9ff4eb1a5114 | -22.26094 | -55.84415 | 2026-09-11 04:12:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0fba09d-d176-3b99-9c53-fd6b9fdd122f | -22.25978 | -55.84896 | 2026-09-11 04:12:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85b93f19-2230-3ee2-9ca3-a9b7ede77ccd | -22.26913 | -55.83626 | 2026-09-11 04:12:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cddb2271-d40e-3d9f-8413-ee39d1e84e9f | -22.26658 | -55.83723 | 2026-09-11 04:12:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55dcb893-ae0f-3bf6-8082-a9d39c58f236 | 2.50887 | -50.85363 | 2026-09-11 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 81a94b16-b7b4-3f3a-8f29-3a4ca6613294 | 4.75473 | -60.43953 | 2026-09-11 04:49:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c53825d-b349-3772-be7b-3d478b998ded | -2.26829 | -47.48627 | 2026-09-11 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa959810-61e5-353b-9239-c08b7b39b72f | 1.28418 | -50.67979 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c76d7be-defe-3c3e-9611-c4f70572dce6 | 1.28695 | -50.67584 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ca554f9-db5b-3381-8994-782d712f6632 | 4.7611 | -60.44344 | 2026-09-11 04:49:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf8f38f8-fe55-3cd4-bedd-47dc0b9128a1 | 1.38554 | -50.63229 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31b5eb20-a1dc-3eb1-bea0-693eb5d500d3 | 1.26204 | -50.71134 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5eeb6e96-1b15-3add-adb8-511a00500bf8 | 2.51547 | -50.85262 | 2026-09-11 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 225ec01b-75b2-316b-ba75-15cf2653c1a9 | 0.97957 | -51.12426 | 2026-09-11 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3f350db-8589-356e-9c6e-5826508c8343 | -1.79132 | -47.83862 | 2026-09-11 04:49:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab47c70b-d55a-353a-bed7-eea58e558a17 | -2.88384 | -40.02562 | 2026-09-11 04:49:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| dcd1b796-7776-3f19-a8ea-65f922bd2ad7 | 0.98564 | -51.11982 | 2026-09-11 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce4141c6-4c4e-33f4-b040-203f92f7a5bc | 0.97576 | -51.12561 | 2026-09-11 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56f6cd14-b87e-3a26-9e94-998b330475c7 | 1.29963 | -50.67037 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30b9a86b-8d71-35c4-b345-df1d9c1c388e | 2.51217 | -50.85313 | 2026-09-11 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ec4a996-0795-3140-8139-7e8addc52582 | 1.24883 | -50.71338 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cd1e32d-fd65-3c37-b01d-d9d66932ff8c | 2.49288 | -50.98956 | 2026-09-11 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9add4cf3-27cc-30d9-b30b-3a1db22bf58c | 1.38662 | -50.63917 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49b376d2-7846-3595-aef9-f1d39fdc8154 | -3.32312 | -42.30025 | 2026-09-11 04:49:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6376156d-bea6-3314-8347-372a31ad6cf2 | 2.5111 | -50.84627 | 2026-09-11 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1a40eaf7-c609-3e5f-b96f-e70dc7e62e16 | -1.03302 | -53.73785 | 2026-09-11 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dc3044f-9ff6-31ef-a581-13c92320638d | 1.28472 | -50.68322 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20b89f6c-8f4e-390e-ae1c-caa7aacdc2f7 | 2.51494 | -50.84919 | 2026-09-11 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0f45852-5802-3d2c-91cf-46912aac1d65 | -1.46023 | -49.35954 | 2026-09-11 04:49:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba91c691-cd08-349d-bd65-3bd48458a90d | 4.75926 | -60.44293 | 2026-09-11 04:49:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed8025c6-bcba-3959-b319-1f86bc964e73 | 2.51271 | -50.85655 | 2026-09-11 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7613b322-f820-3912-8653-29b1de315f83 | 1.28195 | -50.68717 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fd33d12d-c703-3523-a062-3e1a66815aac | 0.97629 | -51.12904 | 2026-09-11 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c065fd9-0ec2-326c-b09f-38833645ef41 | -0.67145 | -50.76965 | 2026-09-11 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb41c168-24fb-3442-b28a-54038505179e | 2.51164 | -50.8497 | 2026-09-11 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fbb1047c-6f2d-3f66-8dac-ac223d87f56b | 4.75864 | -60.43868 | 2026-09-11 04:49:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd19de13-9433-3c3f-8ad6-ec82a6a8f1e2 | -1.32311 | -49.01124 | 2026-09-11 04:49:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc912331-eefe-3c08-af8e-beaab9af0f64 | 0.97299 | -51.12955 | 2026-09-11 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46217475-0c63-3fed-9aea-3ba49b7b89af | 1.25213 | -50.71287 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c800cc02-6baa-32f5-9edc-bc5feb7309a8 | 0.98234 | -51.12033 | 2026-09-11 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb9cf00c-b1e7-36f2-b68a-d71c4d22e573 | -0.93118 | -47.1889 | 2026-09-11 04:49:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb8113b3-98de-38bf-bece-d79d2d8fe754 | 1.28141 | -50.68373 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fd679d70-4a46-39cc-be8c-962cfcc494d1 | -2.30163 | -48.5835 | 2026-09-11 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 671314c3-602a-329a-8a8f-c6f98518bac2 | -3.32364 | -42.29664 | 2026-09-11 04:49:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ab29e864-2297-3f68-b30c-ba41b7169f49 | 1.29025 | -50.67533 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11f9076b-b60b-3849-884c-e2cb1c65e3bb | -2.25389 | -47.98679 | 2026-09-11 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2f707679-2068-382d-a2b6-d3fe7210c67b | -0.93042 | -47.19367 | 2026-09-11 04:49:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a672535f-cd67-3d50-acff-c75fec9892c8 | 1.28748 | -50.67928 | 2026-09-11 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 391c3b19-f2a9-3db1-997d-cea3ff9bb546 | 2.66339 | -50.86432 | 2026-09-11 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4d5f5030-f986-32f2-9e8d-6c7a4e97d1bb | -1.02957 | -53.73734 | 2026-09-11 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a5a0861-8043-39e9-8a8a-be3b16f0d518 | -6.19372 | -55.26823 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1619d2c-6af0-3968-bc50-39c3f227938b | -6.50582 | -58.37831 | 2026-09-11 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2da8e04c-6564-397a-aa6b-7f8e8f776572 | -4.35789 | -54.77458 | 2026-09-11 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4d2eed75-c677-3541-ab0c-b6682ee5f3f0 | -2.93278 | -50.46908 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f5b312b-14a7-3b4c-ae4d-3087a1dad73d | -5.00147 | -57.01192 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 539ed9e3-12c0-3f2b-8bcb-ec8bc5241469 | -6.84149 | -59.36094 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb5caa8b-c511-348f-b454-bc9f73f55fcc | -9.90663 | -45.90214 | 2026-09-11 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5574d98-caa3-3c09-93da-f5502cdb29a7 | -2.94017 | -50.47715 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dd65aab-96af-38e5-b9c0-c968c5125ce9 | -6.7993 | -58.9003 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 523f114e-bd64-3a6e-a2c5-f6482a7bc1d2 | -6.3249 | -55.85649 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a460b9a-f836-3b9e-9ccf-c62ba56d4308 | -9.6378 | -47.68384 | 2026-09-11 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b83432c-351c-3ff4-8130-1093e3fc87ac | -8.39073 | -46.29756 | 2026-09-11 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7387c939-d62d-3b45-9aca-de574498b90c | -2.72104 | -57.63077 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f85a167-af78-386c-bc7b-cff2d80794cf | -2.939 | -50.46225 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30e64bd1-28e4-3546-9599-dc28dfc7fcc0 | -9.70157 | -43.40495 | 2026-09-11 04:51:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c86e4c6f-99e5-3d8a-8bc3-ec26f59c138f | -8.77566 | -44.17862 | 2026-09-11 04:51:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cdee85db-bc4e-3ba4-9a14-ef0c665a4023 | -4.07684 | -48.25502 | 2026-09-11 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 48c578e2-9bdd-3e70-8b20-9d09f74ca5e3 | -2.94637 | -50.48178 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7de4a338-4bd3-3279-a2a8-b1188611a9a2 | -6.19084 | -55.26379 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7783a60b-fe68-3ee8-8d99-44bf020da9ff | -6.76731 | -59.42693 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README16.md)
