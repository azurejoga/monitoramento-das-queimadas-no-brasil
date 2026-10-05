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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a483774-ce92-349b-9ec8-f54fd0a68862 | -5.19887 | -37.37 | 2026-10-05 16:39:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 9.0 |
| fb3e30cf-c5b5-3aa0-98c8-974aef4e1ec4 | -5.98199 | -53.56527 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e8c5b00e-61bb-3431-8252-caad545b5f5f | -4.84395 | -40.40792 | 2026-10-05 16:39:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |
| f5baac3c-2be0-3f7b-b066-bf19f8f36e4a | -1.4739 | -56.74885 | 2026-10-05 16:39:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 74926092-6517-3bf3-adb1-72abe58059cd | -1.51785 | -54.81058 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 53900faa-b9cf-3f73-9c25-9f603fdfbe0a | -2.99368 | -54.03505 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 454ca555-711c-30ef-9ddf-db97afdafec9 | -3.37535 | -58.19712 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 178.6 |
| 80c3f8f6-3586-306d-86a1-785ed2362c66 | -2.57412 | -57.44964 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b21ee53-d0be-336c-b953-489f2634c945 | -1.30743 | -54.22264 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d7f60a8a-7dcf-38d1-a124-f723f504b7d5 | -3.18197 | -57.23965 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d74ca5bc-7517-3b7f-a456-d87804b26e98 | -5.95627 | -41.35889 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 204.7 |
| 4eaad714-e46e-314c-b011-5ce9162c6f3f | -2.95046 | -54.15266 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2be51e79-ff3b-36a6-ae62-f2518b22d42e | -6.20785 | -44.80061 | 2026-10-05 16:39:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 2b51665b-4a20-3e2a-9c02-0792914ec3ce | -3.20818 | -42.49022 | 2026-10-05 16:39:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a1a51503-f8e3-3777-b2db-24a71ff0775f | -2.98622 | -57.89726 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b81662a9-a8a9-300a-907a-95f26fd847b8 | -3.91561 | -44.14066 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ce6cf4d-2a6f-3a52-b496-e66db5431121 | -3.16237 | -40.85513 | 2026-10-05 16:39:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| b8e8dab9-c003-35c1-9985-916e66326356 | -5.99552 | -53.62886 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| b56800f9-ee85-3129-9322-3506cbb8f7a9 | -5.44424 | -42.64431 | 2026-10-05 16:39:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 125bc2b0-bf83-36b8-b2bb-a8d4de79c255 | -3.21978 | -42.77735 | 2026-10-05 16:39:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b444d90f-c096-3a31-8dca-f749de9629cf | -2.88661 | -42.37501 | 2026-10-05 16:39:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4c28a7a1-1c77-330a-ba59-03c540dbeaaa | -0.72297 | -48.09388 | 2026-10-05 16:39:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 366d9b2e-5c8b-3dfd-9089-737a32615fe7 | -3.49365 | -43.34728 | 2026-10-05 16:39:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| aa39c9b0-2ffe-3975-a031-48e05559db2f | -2.99224 | -57.90011 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c65d6a92-90cb-3c0b-a461-57e1e800d7b1 | -3.79054 | -41.75939 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 0b223db9-59d0-3531-965c-4c524b8cc9c8 | -4.9119 | -39.90586 | 2026-10-05 16:39:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 953f482e-2426-304a-bcac-e1cecd34b35c | -6.18151 | -43.38243 | 2026-10-05 16:39:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| a7a132b6-fdde-3c69-bd33-8a6609c94118 | -7.22726 | -55.20761 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68b68808-7369-3ce8-8e7b-b3875b9df8d4 | -3.51739 | -54.62804 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 208.3 |
| b94aafab-0f19-3dd9-9246-9453e82f3a99 | -3.49066 | -54.65817 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4b74f150-fa8b-3c07-abaf-c9d846c8add8 | -5.26206 | -47.92512 | 2026-10-05 16:39:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 99e505cf-882e-3168-968a-cb0828730209 | -3.51792 | -59.56322 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| e425e944-4c0b-38a0-b235-b6fe2d2e2067 | -3.72493 | -45.40254 | 2026-10-05 16:39:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 601aa94b-46a5-33cb-8d3b-ffa35058495c | -3.27985 | -54.18382 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 31c17afa-a5be-3977-a766-223dade7949a | -3.40259 | -58.57341 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 262ddc39-572f-33ab-992a-a1580babac68 | -1.4495 | -47.75274 | 2026-10-05 16:39:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| c0870bcc-9a44-3ed3-a652-2373ba86fc0e | -3.1093 | -57.65955 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f41b1b67-f64b-36a1-a872-071f6db4c110 | -1.1881 | -49.25002 | 2026-10-05 16:39:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 637a5c89-a12e-3873-a756-4b410491f562 | -3.79643 | -41.765 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 8af4ef17-7bb8-3a03-a30b-9a8ad72776aa | -3.29903 | -44.70382 | 2026-10-05 16:39:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9a1f6eb2-7cd6-3b4c-8272-a6c33bf8bd03 | -5.44018 | -42.64492 | 2026-10-05 16:39:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 0639db55-cc90-372c-938d-4a4d4ee80eff | -5.19239 | -37.36699 | 2026-10-05 16:39:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 7306571f-6c5d-3246-9a78-ed9a6220ee88 | -4.17726 | -44.30162 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cf447e1b-fc90-3f0b-86c3-e6b2640f64bc | -3.13909 | -53.72541 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 86e05075-ab7f-3f8b-b63d-3771e7a525f8 | -1.48866 | -55.6693 | 2026-10-05 16:39:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 97a33966-29d4-3ac8-98ed-eea76431912e | -4.06306 | -54.04536 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 3ab97fb2-d57d-3475-98e8-0ed3c424e3f0 | -0.3872 | -52.0765 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 022d388e-7548-312c-9b7f-4dd772d6b49e | -2.60222 | -57.564 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f45f79b6-da07-33ee-bc08-9bcf0515c809 | -2.77642 | -57.66003 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| bb7b56e1-d15c-3dc7-81a4-f8b7d51834db | -3.38474 | -42.59415 | 2026-10-05 16:39:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0ae81c1-febe-321c-9fcf-0cda72037ddb | -3.65445 | -39.43572 | 2026-10-05 16:39:00 | NOAA-21 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5c628dc0-24df-3993-95d0-86a9f9938cf4 | -3.91704 | -44.14978 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7a5badbb-7db1-39a5-bb3c-f1085af54d5c | -1.4271 | -55.34776 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 59f8a0bb-d082-3f2c-a5f1-9e774de54693 | -3.51037 | -59.55461 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| a5679851-63e5-3dd4-a459-bd2df03af9b2 | -5.37658 | -45.90614 | 2026-10-05 16:39:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3bc0a6fc-60a2-3a6d-9b1f-88e38eaaa574 | -2.56909 | -57.98041 | 2026-10-05 16:39:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b2d0c5a-fad8-3228-b9de-0a69b8b2f803 | -4.20145 | -41.75891 | 2026-10-05 16:39:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| acbb3192-cb00-3129-97c0-82ee87a85c12 | -3.64206 | -58.62426 | 2026-10-05 16:39:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| f8396382-4e92-3290-a137-c4b34a3bb80c | -2.11857 | -51.11648 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 41a9fdf0-c3b9-386e-9919-f778e56d9a33 | -1.21637 | -54.53722 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 625c7d69-1df2-352c-9522-7742347fa65d | -3.33043 | -59.47942 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5a71271f-ed8b-33d2-81af-14e406fb0b8b | -3.47604 | -55.43031 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 6dc26265-0710-3cf3-aa7d-d77ddd49feca | -2.53753 | -58.03209 | 2026-10-05 16:39:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| df303ae3-f087-30a8-96c8-32863f15c4b3 | -4.33168 | -43.82458 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9bad3db7-306d-34f2-b0a8-197aba690232 | -5.36395 | -38.27544 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f0f597ab-7742-39c6-8454-e4749c803d65 | -7.33404 | -55.73825 | 2026-10-05 16:39:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c6e9f8de-8fa1-3b18-a47b-d247b3cb1962 | -4.7818 | -39.96791 | 2026-10-05 16:39:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 45.1 |
| fed618ee-a8aa-3f03-ac6e-37a0b2fb44c8 | -3.32309 | -59.47583 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d9745b0b-5d14-3b73-aadc-e037d97a5283 | -4.85862 | -39.59249 | 2026-10-05 16:39:00 | NOAA-21 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 1ac06c6b-21c5-3699-bee4-05db84c1fb75 | -2.81132 | -49.87195 | 2026-10-05 16:39:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b0527aee-991c-328c-8dfd-f8b364d32d8a | -5.20022 | -42.73533 | 2026-10-05 16:39:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| a4adc945-1f4c-3c02-a9ab-6da1dc1c2505 | -3.23986 | -58.7574 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e1217c8c-3e4b-3b48-9e53-a31c5b3a0f9e | -4.29593 | -42.18637 | 2026-10-05 16:39:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 6f0f5f02-4264-378a-ab2f-9be45d67b72e | -3.99736 | -56.27517 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 04182223-d378-3f6e-a044-638b462abf6e | -3.51044 | -54.61135 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 18e6c4fe-1fd1-3762-bd3a-942918bde2d7 | -3.40325 | -58.57229 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 116ff2eb-d293-369b-99f6-f332be1ebf6a | -4.38024 | -43.91489 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6e065535-5494-3a26-b1f3-96204329c7c5 | -3.28414 | -54.18328 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 2c451864-655e-3b48-aac6-f59c4b0ab0d7 | -4.38099 | -43.91956 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cb4f534b-54c7-378e-b22f-3d275ecae551 | -6.09739 | -47.6524 | 2026-10-05 16:39:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c90f632-d0b8-3dbb-9099-0af56fac6932 | -2.95165 | -54.16054 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 06ec8eae-9078-3933-bc38-5a5cb4411ba7 | -4.30642 | -54.79594 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| aa19adf8-908f-3da7-8c58-362e93105974 | -4.3157 | -38.4803 | 2026-10-05 16:39:00 | NOAA-21 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 14ce8d6e-af35-3bef-8a14-650652db88ac | -3.92622 | -49.71338 | 2026-10-05 16:39:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ca91ea56-fe41-324a-bc6b-7b57049c084e | -6.06636 | -53.84296 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ed5fee74-518b-3f2d-a5a6-a2f2b7e528d3 | -5.8356 | -45.01691 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7bb8f9f8-43a2-34db-bdda-aec7b1f3ef6f | -2.63076 | -49.30661 | 2026-10-05 16:39:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 95b42838-9528-37b3-9cac-c72dace51c38 | -4.08491 | -40.85437 | 2026-10-05 16:39:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f156222c-bcac-38f6-b126-e5c909f1c628 | -5.12617 | -42.76972 | 2026-10-05 16:39:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2342e205-7593-312c-946c-b8bcf4832da1 | -2.94571 | -54.12112 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5395cacd-ab35-3dd8-b0b3-de8367b2016b | -3.19769 | -57.08786 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9c84175a-cb19-3ea6-a406-a5d01b9ef237 | -5.99123 | -53.62946 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| ffaaa5bf-43cb-37ff-b42d-8bda68fda370 | -3.50223 | -54.61697 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 07a1ae34-bcd7-3adb-a2a3-8e6968fa0170 | -3.4094 | -42.66074 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c4412002-05a4-3300-9887-64da8fb0bd52 | -4.34573 | -44.37815 | 2026-10-05 16:39:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ae41f28f-6d04-3094-be4b-c0ab453303e2 | -3.07723 | -54.15968 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 0affe227-5cde-346a-9037-2bf88e0bcec3 | -4.81021 | -42.14978 | 2026-10-05 16:39:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| f8a540fd-2f08-34b5-accf-35057e8e9783 | -2.95472 | -54.15211 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 78c09e33-18ac-3705-9d79-002d84af1f6c | -1.46136 | -55.2697 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 64d04478-8127-371a-959c-fb46cce6472c | -6.07132 | -53.83826 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README91.md)
