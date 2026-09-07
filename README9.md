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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ad34b98-75ce-3404-af1f-510fe08aea00 | -13.3004 | -45.2442 | 2026-09-07 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 981d74c5-9a4f-31c5-bc96-b9ed2ee4c04e | -11.5001 | -49.6109 | 2026-09-07 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| e2717a19-e1c2-3565-90e2-881c1ef47be7 | -8.27502 | -38.18177 | 2026-09-07 03:21:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 86c45ed9-e2a6-31cb-895b-43fc1f4d77df | -8.27581 | -38.1775 | 2026-09-07 03:21:00 | NPP-375D | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 574f6d58-6477-3e0b-8df8-f8983e9df57c | -13.85181 | -43.64579 | 2026-09-07 03:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 729e11b9-115f-3999-930d-9cacd9c12360 | -9.48966 | -40.28122 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3289e342-afb7-3c06-98aa-cca31002eb9e | -9.56812 | -40.35883 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 23.6 |
| b88472f1-dda1-3232-a590-3c20684ea725 | -9.49 | -40.28085 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3a60657c-d3d2-3ada-b2e1-d1256c5a5607 | -9.49072 | -40.27595 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5b60eb56-9558-311e-95e1-cda07c086ff0 | -9.56919 | -40.35336 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 352d73f3-0bd2-3241-98d1-51a3a73cc6a9 | -9.57457 | -40.36014 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 4ce4c151-bd91-37d2-bda0-39f6247eae6b | -9.49608 | -40.28256 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 602fe2e3-15a0-3b09-b4f3-18681b6e9066 | -9.49715 | -40.27725 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bd190319-d4ac-34b6-a97f-66877bd4addb | -9.49746 | -40.27688 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d1fff35b-c4cb-3bb4-9eed-6dd9e68c4302 | -9.49643 | -40.2822 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f17b0fa0-251d-33eb-9a18-d3393b515e13 | -13.85017 | -43.65327 | 2026-09-07 03:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d96c03a-87e7-358f-88e3-129e3c8ea879 | -9.70149 | -40.62962 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ee098dc5-be3c-329c-bc63-ef547bb92295 | -9.57564 | -40.35469 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 2c746e01-2716-3e6e-9105-bb86d1de8b00 | -9.49103 | -40.27556 | 2026-09-07 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 07cd96fb-3399-3af4-b282-b26c305143ff | -15.93723 | -41.98039 | 2026-09-07 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| da2b15c3-692b-32ac-9403-e4e0359a75c8 | -15.93172 | -41.98098 | 2026-09-07 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 339ba788-d29a-3b26-9c75-9576a935f760 | -15.92963 | -41.98475 | 2026-09-07 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 039a6cf5-09c9-336c-8da2-ae847b7da7af | -15.93812 | -41.9822 | 2026-09-07 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| afe29d47-d7c0-3bac-a348-af45e46c4105 | -15.93603 | -41.98595 | 2026-09-07 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 37.5 |
| d949cfb0-4eda-3730-9d8e-1af1b1b9dd2a | -15.93047 | -41.98658 | 2026-09-07 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 757728b9-fd54-3236-ac61-38eaf8a21cef | -15.93689 | -41.98769 | 2026-09-07 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0399a342-6d10-30e7-878f-a1921bae2310 | -15.9393 | -41.97686 | 2026-09-07 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 10536d7f-6b70-3ba5-9da4-4e8b580d0549 | -15.93084 | -41.97914 | 2026-09-07 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25421271-ef4b-332c-b08d-d0ee2944754b | -15.93838 | -41.97507 | 2026-09-07 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a721a1cf-fd97-3448-b663-c54743d4e4cc | -6.6513 | -59.9642 | 2026-09-07 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| b818a218-ef35-33f8-8531-b35a0ef398e8 | -11.5191 | -49.6087 | 2026-09-07 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 00a090f9-903c-39bd-b9d5-0a8f37ede005 | -13.3009 | -45.2209 | 2026-09-07 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 46aa5fcc-60a8-3ee2-bff4-24bd185ce47f | -11.5188 | -49.6304 | 2026-09-07 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 60bd643d-7662-3f26-ae00-03a8c3f2f109 | -13.2287 | -61.7355 | 2026-09-07 03:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 693579aa-e79f-3f0c-bf8b-dfe1ed475585 | -13.3004 | -45.2442 | 2026-09-07 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 09952ed6-acf7-394f-ac73-d1926cb841a0 | -3.1462 | -60.6506 | 2026-09-07 03:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| d9ee1bbd-bd14-39d4-b6ec-786c9041534f | -3.1461 | -60.6696 | 2026-09-07 03:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 43515d20-511d-3b1e-ab3f-69604f5bae98 | -15.9331 | -41.9772 | 2026-09-07 03:30:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 9bdbe39c-d279-34f1-8b0d-3c6909abf162 | -2.8839 | -50.4428 | 2026-09-07 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 9a0a1d68-7182-3963-844a-a2ce2d2d5405 | -13.3203 | -45.2177 | 2026-09-07 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 238.3 |
| bc51acc8-1903-3bfa-8433-9a3a41d0b18d | -13.2477 | -61.7342 | 2026-09-07 03:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 9278dea1-7491-3d13-87b2-9520ec65b3a5 | -13.3198 | -45.2409 | 2026-09-07 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 190.1 |
| 3c04107d-636b-3585-a575-61116eae0950 | -2.6387 | -46.7817 | 2026-09-07 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 75e18704-abbb-3123-8157-47a1e9fb3e80 | -2.6202 | -46.7822 | 2026-09-07 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 210f3af1-0834-382d-bc00-f24f0af22d0e | -2.8839 | -50.4428 | 2026-09-07 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 14048be7-8f3d-3004-8052-3a83647683f1 | -2.6202 | -46.7822 | 2026-09-07 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 445fbdad-9b14-324f-aed6-225ac1d28bcf | -11.5191 | -49.6087 | 2026-09-07 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 9adcedb8-8ce9-373e-adbf-616d1a0915c6 | -11.5188 | -49.6304 | 2026-09-07 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 483faafe-24cf-3ea0-9a81-353a67aaac57 | -3.1461 | -60.6696 | 2026-09-07 03:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 46e9926e-1371-3670-ab36-3b4b16fb5dfb | -13.2287 | -61.7355 | 2026-09-07 03:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 61cc96fb-cdb4-3875-9a66-b6ee8746e917 | -2.6387 | -46.7817 | 2026-09-07 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 112d0c26-303d-323a-93c0-4cd4ec00aa78 | -13.2477 | -61.7342 | 2026-09-07 03:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 6289f93c-1170-3151-b95b-0810c51cf36b | -3.1462 | -60.6506 | 2026-09-07 03:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 9f0f438c-ea49-3748-b5b1-bbbf0200bae4 | -8.27597 | -38.17773 | 2026-09-07 03:42:00 | NOAA-20 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cb0313d4-5f5d-3131-98f3-d67feafd68bf | -2.62674 | -46.77493 | 2026-09-07 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a73ea0a0-1571-319f-9165-b6b1c50bff6b | -2.62551 | -46.78209 | 2026-09-07 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| daef7b75-5cdb-36af-92bb-a6e4c3977a5d | -8.42353 | -41.43888 | 2026-09-07 03:42:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9e1eaa69-4623-32cb-9adb-d87ed24478f6 | -4.37555 | -44.39487 | 2026-09-07 03:42:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f49d7be-5e18-301c-9a73-d2d11131a00b | -6.77446 | -41.16609 | 2026-09-07 03:42:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0ba8a7fb-de8d-337f-a67c-838e1de6cc18 | -8.56819 | -45.98375 | 2026-09-07 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85d71580-4e8a-38d1-b266-43d7adccbb75 | -6.79294 | -37.97055 | 2026-09-07 03:42:00 | NOAA-20 | SÃO DOMINGOS | PARAÍBA | Brasil | 2513968 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 52121b17-045c-3b51-abff-34f3b7154356 | -9.51704 | -41.9925 | 2026-09-07 03:42:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f939caad-2039-3477-9ce8-9f8598912234 | -4.37632 | -44.39037 | 2026-09-07 03:42:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d443c2d0-6a5e-30e7-b537-609c19f40fa0 | -3.20784 | -42.98016 | 2026-09-07 03:42:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42ca9836-a6cb-3f39-9537-6eee09e71db4 | -9.52176 | -41.99338 | 2026-09-07 03:42:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0605d018-9117-379a-99fa-4b84f741ac5b | -7.0885 | -39.67258 | 2026-09-07 03:42:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 083566f1-abb4-3491-a2f2-5065ffb3d776 | -9.49029 | -40.27115 | 2026-09-07 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97c1f858-eeae-3081-ab2d-48fad2b99f7f | -6.62456 | -38.34687 | 2026-09-07 03:42:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 65914bbb-78f4-37d7-9edc-f5499965b54a | -9.49382 | -40.27582 | 2026-09-07 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0f477028-2f62-332a-961e-f04f7be4a783 | -2.628 | -46.76763 | 2026-09-07 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 714eb066-c0e9-3513-9732-56cbbadd369c | -6.77911 | -41.16705 | 2026-09-07 03:42:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f892d2d7-cc21-3fcc-9cf5-e04f3169c1c6 | -9.57063 | -40.35767 | 2026-09-07 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 61b6ffb1-e1fa-39bb-8f86-e3f52af92b2c | -3.2072 | -42.98405 | 2026-09-07 03:42:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68b93351-d8b2-378c-a015-9324968e4ab5 | -6.56597 | -44.78052 | 2026-09-07 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 946f41f5-23d0-35e4-8a61-759919a58aaf | -4.38155 | -44.39614 | 2026-09-07 03:42:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2092a359-e965-337e-9fe9-6064e467996c | -9.57133 | -40.35369 | 2026-09-07 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 238c0f97-5d67-3d6e-abbb-aa8a620865b6 | -8.27221 | -38.17713 | 2026-09-07 03:42:00 | NOAA-20 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 562ccf60-b94a-30c4-9e58-74ab41e03303 | -7.08917 | -39.66864 | 2026-09-07 03:42:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 899bcfda-5850-3a1e-a4b3-bd6d216be2c3 | -9.51794 | -41.98741 | 2026-09-07 03:42:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 743c1ed3-a4ac-3a5c-a060-2a46b6787c16 | -6.77825 | -41.17192 | 2026-09-07 03:42:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8033a3d8-16c6-3d78-aae9-9a4bfa19117e | -6.77663 | -41.16977 | 2026-09-07 03:42:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 034dd1d5-7dd6-3d80-b479-248a8ad1bbe2 | -4.38331 | -44.39527 | 2026-09-07 03:42:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad08f1a6-6dd2-3047-977f-6003fe84e16a | -8.73126 | -36.89515 | 2026-09-07 03:42:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c732b2af-21fd-3d77-a4b0-1f0ec88696c1 | -4.37729 | -44.39415 | 2026-09-07 03:42:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f11c2b41-a3e3-3803-860c-f8a795999a7b | -8.8501 | -36.87723 | 2026-09-07 03:42:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 16b98cec-db09-3eb3-8734-6468137454a1 | -9.51232 | -41.9916 | 2026-09-07 03:42:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e3a17229-6d3d-3c5c-bd7b-11de22fb7f1e | -2.6351 | -46.76903 | 2026-09-07 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 835472d9-095c-32dc-aeeb-27ee2d3405dd | -2.63386 | -46.77628 | 2026-09-07 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 257e1c9f-29fe-3176-a6ab-b706c3466534 | -7.01904 | -37.27066 | 2026-09-07 03:42:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5fd0274a-2dcd-3b11-960b-8154ab590537 | -2.63264 | -46.78336 | 2026-09-07 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 8e5839e4-5204-3d03-8cd6-a08b898edcd4 | -6.56509 | -44.78551 | 2026-09-07 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16c57699-5c7c-307c-9642-87827f05fea6 | -6.62844 | -38.3476 | 2026-09-07 03:42:00 | NOAA-20 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1aabda70-a882-3e29-90ff-8323b71d184a | -6.57194 | -44.78161 | 2026-09-07 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e43709ce-7153-3dd6-920b-c30dc8dc471c | -9.49314 | -40.27973 | 2026-09-07 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 86b25bdf-db7f-34d6-825a-8f25686d2375 | -9.48961 | -40.27506 | 2026-09-07 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 409a7cfc-e4dc-3efd-8d46-cefa8d68e423 | -11.32387 | -45.08791 | 2026-09-07 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b1a69bd-571e-3bb5-ba4f-b8dafc051770 | -15.93713 | -41.97531 | 2026-09-07 03:45:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 47414e83-6ff6-3476-ae0e-34dbf10cff9e | -9.72539 | -43.41833 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 9db827b4-94e4-3681-9e21-005580951374 | -9.72944 | -43.41935 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0adaa618-6f60-32e7-aab2-803c47fe7277 | -9.72934 | -43.42583 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |


[Clique aqui para ver as próximas entradas](README10.md)
