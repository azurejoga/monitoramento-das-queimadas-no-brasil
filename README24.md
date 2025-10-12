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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78c95f4d-af5f-3318-99f9-bba62b21f274 | -14.92146 | -46.7695 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 17a16e16-8cb9-3ba6-9ddd-844cc98ade4b | -15.67801 | -46.63897 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64b83f6b-2d03-3272-931e-50f6695f6c68 | -15.65898 | -44.47622 | 2025-10-12 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4efe7dd-e839-350a-b4cb-cf2f1de90a50 | -19.53416 | -43.05756 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ab159ffa-179e-3df6-992b-a447a51d985a | -19.53276 | -43.06015 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7046a09f-2957-3cd1-95c3-753cbcba87fe | -14.91415 | -48.52937 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8ecd07f9-68af-3917-be3e-77b128980c5f | -11.85261 | -56.86491 | 2025-10-12 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 534f0915-6afa-38ca-aaf4-7c6ee5fc35fd | -15.85706 | -56.7555 | 2025-10-12 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79f9cbe0-2938-32bb-979e-7fc3a1e73c8e | -14.40508 | -48.01747 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 876a9f88-6eb1-3ec2-b7aa-2870ba5a01d8 | -14.96938 | -44.93423 | 2025-10-12 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63e66459-8c94-33d5-9378-8c61566e71ab | -15.53562 | -41.80156 | 2025-10-12 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 227948ef-d05d-3177-bd70-ca89e98821e7 | -14.93651 | -46.74113 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 80d7f3e3-9efb-3a49-9061-58e7c2030bf2 | -14.22609 | -45.73977 | 2025-10-12 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fc42ae4-1dec-3556-8c0c-4d529574d0f9 | -15.67642 | -46.62756 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f9f2607a-bbfa-3e79-b8f4-8426fdd80c5a | -19.52105 | -43.04704 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| db3ca7ee-ced4-3628-a7c1-2e69bc500ba6 | -19.12026 | -44.39042 | 2025-10-12 04:17:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 281e5e50-e06d-3c8b-b378-a51a43dcc251 | -15.6871 | -46.62549 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 750f32bb-5f75-3d52-8215-268c3b6af388 | -18.07591 | -45.02979 | 2025-10-12 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a9faf66-9346-3e98-8b08-2d4e65cb0af0 | -16.34878 | -42.38804 | 2025-10-12 04:17:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 001b07c9-4d4c-3089-a47d-dd41c057e55d | -14.9325 | -46.74441 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f2750024-8de1-38ee-a3eb-2707d349fa4a | -17.255 | -52.2724 | 2025-10-12 04:17:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7eb07a9a-9b36-3799-9c9b-ed8e542613f3 | -18.25465 | -46.39305 | 2025-10-12 04:17:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3f0c8a4-d5e5-3856-9161-3161d473ec9b | -14.96812 | -46.74672 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0efb096c-5b84-37de-a2a0-2048c0492388 | -19.51748 | -43.04648 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 14bef198-f0fb-3a29-b865-d68a9c7793e8 | -15.43605 | -44.17776 | 2025-10-12 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bce4acb0-381c-331e-8bcb-730f7c1b4f80 | -15.23763 | -56.87742 | 2025-10-12 04:17:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 994c12bb-1a27-3585-8ba2-fe34836e194b | -18.58224 | -50.58094 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 242208bb-fafc-3c8f-9e01-117df958e8b6 | -17.89352 | -48.2309 | 2025-10-12 04:17:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b034f3df-9b73-38e7-b3cc-7ac878e2e272 | -18.95967 | -45.71815 | 2025-10-12 04:17:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ff685c9-e34b-3e5a-bbb2-c32e45e3571c | -18.45212 | -47.15504 | 2025-10-12 04:17:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ee458c2-7368-347d-9329-fa1eaa73a98e | -14.41297 | -47.95429 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4dc077d5-2cee-3413-8c9a-1146bca44e16 | -15.43272 | -44.17722 | 2025-10-12 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11e98dcb-0f20-3a44-8025-b1e1a8c0d33e | -14.92452 | -46.75078 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 044ed2ef-66e9-320a-8c0d-dc34bd718f8a | -18.55765 | -46.94464 | 2025-10-12 04:17:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26d55f00-a550-38c1-8dd0-99e2d3764d50 | -15.11276 | -42.01113 | 2025-10-12 04:17:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| db6da912-1842-38ba-8c73-45c7c1fe3bb1 | -18.08366 | -45.02366 | 2025-10-12 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 306b644d-3916-3cb3-b61b-5a067b3dff34 | -14.98203 | -44.93995 | 2025-10-12 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cbd95d15-56bd-39d3-8744-19905cc69313 | -15.29128 | -46.14492 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd29d533-26b3-3e78-8e29-108659bd6d37 | -17.18556 | -46.96384 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38fe47c8-c6f5-3bee-99e9-065cdc204e9b | -15.29636 | -46.13459 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29dae7f2-9cf8-3f70-b43e-cd3a3fa1a92e | -14.96994 | -44.93069 | 2025-10-12 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a85ec761-0a33-36da-9b27-2bad6bd6b72f | -19.7862 | -42.3972 | 2025-10-12 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b1440fc7-0601-3976-8c27-b2912d05bcba | -19.527 | -43.0566 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| d1827fa4-8a37-3f5f-b57f-3be80cacf308 | -15.87477 | -56.76019 | 2025-10-12 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a10383c1-e75d-38e7-9f16-f7f123b0adbc | -14.97332 | -46.73619 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 752afdb7-570e-3d03-9b98-889ac3d57bde | -14.89552 | -48.50727 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34a14db2-f542-3b06-a1be-78d6c437eaea | -18.00509 | -52.39519 | 2025-10-12 04:17:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e5c3cc92-cbed-3d93-bcb1-5578db9033fd | -11.78115 | -46.34325 | 2025-10-12 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52ee9134-cc28-3975-9ddf-a110da45421c | -17.94242 | -42.89351 | 2025-10-12 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1395e4a0-4cd6-3476-ab8e-3a9566acbd85 | -15.67365 | -46.62342 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bb29209c-d430-3e10-a987-361b7c54de69 | -12.13891 | -45.59023 | 2025-10-12 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ab776c5-01cb-35e2-8456-4e7d8c4ce362 | -12.22343 | -43.80012 | 2025-10-12 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fc485e4-97b7-3df5-b8ca-4f0a9ca3ff07 | -19.8463 | -42.44638 | 2025-10-12 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7a26fa90-1543-388d-a85e-bf9df4cad31a | -15.36333 | -44.16224 | 2025-10-12 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ec5d6a50-8143-34fb-883e-e9ea5d6bbbc9 | -15.00416 | -53.88733 | 2025-10-12 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1589a816-0bbf-3181-b6b9-178ad7c3ef19 | -17.19075 | -46.95312 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24a4b2cd-c3bc-3710-912a-dd183135440b | -15.69045 | -46.62608 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 83b119a0-0c79-33c9-8b6c-745d0aa1facb | -17.26083 | -46.89664 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7218ea51-a6f0-3748-9556-c79f86aca993 | -15.6623 | -44.47676 | 2025-10-12 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 961edf68-c668-3b97-aeab-ecb91e52c31b | -13.22134 | -47.80061 | 2025-10-12 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79721a7f-47cd-347a-9d65-4ddb6312ed26 | -18.5473 | -47.24046 | 2025-10-12 04:17:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e717d256-d1b0-321f-971b-d16899430fd0 | -18.55824 | -46.94096 | 2025-10-12 04:17:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04b056dc-f75c-31f7-a83d-5d4f032e9759 | -15.28802 | -57.08892 | 2025-10-12 04:17:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8a511ba2-4d25-3ad5-bb91-5da784ee34c3 | -19.50261 | -43.04848 | 2025-10-12 04:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b1d3bbfb-9a74-32cc-b3f8-008f4fc23782 | -14.96873 | -46.74302 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| feb09204-a6e9-34be-beb1-0bf08c2ff6fe | -17.36675 | -46.66235 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 87792c53-3972-3336-a8e7-c55bba99995f | -16.72635 | -43.99902 | 2025-10-12 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5229dd26-0fc6-317c-a1dc-bcbb2803032f | -16.119 | -44.58033 | 2025-10-12 04:17:00 | NOAA-21 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d2cfd86-fe11-37c7-be24-86ac5a38d180 | -14.02241 | -43.48469 | 2025-10-12 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c7b1598c-8a02-3a05-a3c8-a6e69b6562f7 | -13.49467 | -43.03665 | 2025-10-12 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2aff2e57-37a3-36c7-935e-5154cdd9e4b8 | -15.29461 | -46.14544 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb3edf8a-fd71-39fa-951f-e2ad29c0ecc4 | -17.25414 | -46.89549 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf99cc26-99ea-3b68-93e3-0e410381ab88 | -18.58134 | -50.58589 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 9c3d1c6f-78aa-3e34-be00-ac1f0fdb9efd | -14.02856 | -43.48941 | 2025-10-12 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e238855c-558c-32e7-a221-38fcbc5c17af | -18.55433 | -46.94405 | 2025-10-12 04:17:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81268bd2-739b-3994-acb4-ed6778fdcf53 | -14.9721 | -46.7436 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ccf0c9a-ede3-372d-bb0e-2324721748cb | -22.33208 | -49.86193 | 2025-10-12 04:17:00 | NOAA-21 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 665b1902-7545-38c4-9541-63d7bdbb27e7 | -14.40521 | -48.02276 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e21ddaa2-fbcf-332b-b402-887f22ec59ac | -14.95832 | -46.72195 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 39df1564-e0a3-3ec3-bd63-2e250fbc8cc7 | -18.57177 | -50.59452 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 983d7d20-2346-30ce-863d-6464e5b6705c | -22.29423 | -49.89001 | 2025-10-12 04:17:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b64c8802-c82c-35ad-993f-f62cfa4ad28d | -15.2966 | -46.30249 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 364e486b-f523-3d3b-9561-90f85c60d73f | -14.4179 | -47.94671 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dec73242-4b7c-36d5-abf6-4e9ee0c1bce2 | -15.18902 | -44.50306 | 2025-10-12 04:17:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ca81a70-b580-317d-b384-e699045a9a58 | -18.55492 | -46.94037 | 2025-10-12 04:17:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0df0a0f2-4041-3e2b-bd74-e41fcf59ca8c | -11.7771 | -46.34648 | 2025-10-12 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60308443-fb4a-3cf9-8fb9-e43127857ad8 | -14.84613 | -48.48671 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d799bc1b-7e93-394b-bb8d-759e3a04dd54 | -15.68255 | -46.63227 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6c9c61dc-a375-32ce-9bf2-75fdfac61d65 | -14.75319 | -46.12466 | 2025-10-12 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33a3318b-4fbf-3e60-8efd-9de06a48298c | -15.53261 | -41.79658 | 2025-10-12 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c58f0398-33cf-3780-a33b-49a84b683bf3 | -14.96934 | -46.73931 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 194dca51-62e7-3f18-93e0-86017d579666 | -16.11736 | -53.97482 | 2025-10-12 04:17:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae7de2b7-c520-3da6-b1dd-2b11123683a7 | -16.34819 | -42.3922 | 2025-10-12 04:17:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c457d2b-28e9-3973-85c7-89ad0628cd62 | -14.88685 | -48.51414 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fb5255d-d3d7-37e0-833e-a7ce313925dc | -15.00477 | -53.88428 | 2025-10-12 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55746964-42d0-3a43-8976-5753c89c7da7 | -15.23841 | -56.87558 | 2025-10-12 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe636cd6-a172-36ee-9ed3-986e0a00a9b1 | -14.41014 | -47.97128 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59bef87c-f55d-3f88-9612-d813d575a1c9 | -14.91808 | -46.76893 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e0d237ef-8ae2-3158-9af8-58f226e079a2 | -17.19362 | -47.32695 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc46d3c0-a3a9-3d4b-8aae-b6d66080c5ce | -15.23244 | -56.87185 | 2025-10-12 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README25.md)
