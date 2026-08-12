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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5d64914-183b-3bc6-a11d-669dbc20ce8b | -11.4873 | -44.553 | 2026-08-12 03:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d9bd2272-2480-3fae-8b11-48ff3bc201fd | -11.4677 | -44.5791 | 2026-08-12 03:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| ac7e6d01-c713-3b95-9151-5d18aff2edf1 | -6.54287 | -43.11297 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c63561be-d735-32b6-8b85-97f7c8138aec | -6.54562 | -43.12784 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dac618d8-bed7-337d-82e9-b6486a5d6779 | -6.88693 | -41.94438 | 2026-08-12 03:28:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e362a5b-dd2c-3714-8a7d-20daa1f48119 | -6.77017 | -38.76359 | 2026-08-12 03:28:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1a66da3-2a09-3fa8-b9fc-214547d903b7 | -6.54879 | -43.11098 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fd8bc12-4c3f-3155-8243-ad51947994a8 | -6.34032 | -44.06046 | 2026-08-12 03:28:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e327c2d5-8bb9-3e28-a4c1-4e7c17504574 | -7.18475 | -44.37242 | 2026-08-12 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3a0815ba-9961-3c2a-837d-b8730bdecfd5 | -6.99348 | -42.62989 | 2026-08-12 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0e4bfdfe-c0f7-3dbf-88e0-7f4e54be954d | -6.88561 | -35.01287 | 2026-08-12 03:28:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0761c944-158d-3f37-bd14-dd1461efc0b2 | -6.53356 | -43.11988 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 783f69c1-e264-34de-a70b-b74b59d3e79b | -6.5401 | -43.12115 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb8f0b55-356c-3ea9-b374-2d5a09faef59 | -6.53902 | -43.12686 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1320a150-b4f9-35bf-8989-81e995719967 | -6.34037 | -44.06499 | 2026-08-12 03:28:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 9e0a949f-1d67-3ec6-87f0-4ecb3ef534ab | -6.04248 | -43.86988 | 2026-08-12 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 00aa8646-08c1-3beb-8f29-0d840c3e5b0e | -6.54774 | -43.11657 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f83e5bdb-2eb1-360b-ad0c-42114b74b716 | -6.53974 | -43.13021 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 84a2b5a3-8409-35b2-a4cb-1d84177c176c | -7.19302 | -44.36698 | 2026-08-12 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e410b69-901b-3b12-a4c4-1136e25e97c7 | -7.00722 | -44.62505 | 2026-08-12 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa3ad057-1c4b-3340-87c8-3ae92f51585d | -6.54837 | -43.11995 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65799c12-0fa9-37c5-9cb7-f24a646892ab | -6.33914 | -44.06662 | 2026-08-12 03:28:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 766a804a-219f-3124-bf69-a1b726d9af68 | -6.54078 | -43.1245 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b64716ba-6b40-3c74-a569-bb2de70b917f | -6.04934 | -43.87135 | 2026-08-12 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3ff65c12-faa1-3e5f-a5be-2e6d5af6b430 | -6.5412 | -43.11535 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4140bbd6-e1fc-3158-b72e-81762ad6b059 | -7.38579 | -42.86076 | 2026-08-12 03:28:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6b7b0182-029a-3558-809b-e158b02eede8 | -6.89273 | -41.94696 | 2026-08-12 03:28:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd19da2a-0bd9-3d04-be7a-91bd8a5068dd | -6.53528 | -43.11751 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5df10634-f10c-3515-930c-1bffc73eb4ee | -7.18605 | -44.36566 | 2026-08-12 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b4d6066-a8b2-31be-afcf-27a4d66f24e5 | -4.97762 | -37.23978 | 2026-08-12 03:28:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 75feda11-73bf-3cfb-a828-2f118eccca96 | -7.18656 | -44.37092 | 2026-08-12 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2dc45db5-62f2-3951-b5df-c4baaca1277a | -6.99879 | -42.63647 | 2026-08-12 03:28:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9738e8f8-951d-3798-b55e-23bd11d02449 | -7.01012 | -44.62945 | 2026-08-12 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 735f0a54-15fb-3cb1-81bc-b323c08b97d3 | -7.01302 | -44.63303 | 2026-08-12 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c12af0a1-95b2-3c0a-8b24-ab96e1e0eb0c | -6.54182 | -43.11876 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a0985823-f553-3c08-9b0b-57f2cc39395c | -6.33922 | -44.07119 | 2026-08-12 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b6e8ca5c-4a45-3f22-8463-7714ec5b9c55 | -6.53422 | -43.12329 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d907c19-e82a-33d2-8809-a5f4e61f0282 | -6.39349 | -38.91198 | 2026-08-12 03:28:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50d4f5db-36f9-32c9-8388-5f2bae181d21 | -6.89454 | -41.93715 | 2026-08-12 03:28:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3b64bb89-074d-3729-9f53-d8d90dee4c01 | -6.99677 | -44.83173 | 2026-08-12 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 490199a9-6abf-3281-9d88-a5a13a7a516b | -7.39118 | -42.86714 | 2026-08-12 03:28:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40c28be8-8294-3663-9bc3-15860188e6e6 | -7.01443 | -44.62575 | 2026-08-12 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a78e5ba3-fb85-3a1d-9ef0-21919e717c7a | -7.00391 | -44.83326 | 2026-08-12 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eeac562-bd22-3b67-a9e0-829cbb642e63 | -6.54667 | -43.12225 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 086c14c3-b3ce-38c0-b101-1bb47252c4e6 | -7.01145 | -44.62234 | 2026-08-12 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 56589d9e-20b8-37b3-be60-f393dcb214c7 | -6.54735 | -43.12561 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 76fdab8b-64c4-347d-a6a6-eab432bbcff1 | -6.5494 | -43.11431 | 2026-08-12 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c351a28c-c988-3681-9028-e6463b3798f4 | -6.39398 | -38.90916 | 2026-08-12 03:28:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca296bde-108a-3cd5-9ce2-02fc4f57c9e5 | -11.4681 | -44.5558 | 2026-08-12 03:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| b945448d-5dda-3caa-9e24-26126d399616 | -11.4677 | -44.5791 | 2026-08-12 03:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| a714e4e0-02c3-33e7-bb2a-543be1c62054 | -11.9535 | -46.3444 | 2026-08-12 03:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| e54740c6-42e8-36cc-adca-6ec5bf0cb361 | -11.4869 | -44.5763 | 2026-08-12 03:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| aa04c2f9-b6b8-3e0a-9af4-8959a86d5907 | -8.96 | -60.5358 | 2026-08-12 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 5cb14f5e-5bc4-3cb6-a698-b65814f0cd71 | -10.2261 | -45.9389 | 2026-08-12 03:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| e46302b7-9d33-335f-99fa-1e0c2ccbd64b | -8.9601 | -60.5165 | 2026-08-12 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| cfc53ea7-661e-3eee-94f5-0617f41cee4a | -11.9719 | -46.3871 | 2026-08-12 03:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4ccfac59-9a3f-3d50-b518-71dfd1569620 | -11.4873 | -44.553 | 2026-08-12 03:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| a0d4bbe1-ed02-3088-8782-4aef901fe8f1 | -9.52591 | -40.34096 | 2026-08-12 03:30:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a3f90b16-2892-3592-a6d2-186e2c9464f2 | -11.46803 | -44.55511 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9b9a7e5b-20aa-30a4-a5d4-2fc557a924cd | -9.52562 | -40.34108 | 2026-08-12 03:30:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b4b2ed26-1182-30e3-a0f1-2a7081602d7d | -11.46567 | -44.56664 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 142a2602-3750-3fe2-8ed2-2e76658ae37a | -11.48305 | -44.57135 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 3f41e726-68f6-3ced-a0f7-4bfae13ab378 | -11.48417 | -44.5767 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0027c8af-733e-3c5b-945a-321b23620b17 | -11.47341 | -44.56229 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 57f99ae9-e79f-3f34-8be5-d4360ac65241 | -9.52624 | -40.33784 | 2026-08-12 03:30:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5dd73e92-7dcc-330b-acca-6056b285b7cb | -11.45912 | -44.5652 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 38da080b-7d8e-3500-9e87-f5282c0f0044 | -11.47223 | -44.56806 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 27218ff4-5b91-3624-aa9b-6df07c101b90 | -11.46148 | -44.55367 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f5e09688-b509-3ded-8fbf-131740739043 | -11.48534 | -44.57096 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| ca239c13-0ffc-350a-bd41-ec1ca65f0169 | -11.47761 | -44.57526 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 35b57a0a-6583-35f3-af4d-51211422edc7 | -11.48184 | -44.5771 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 934f5e8c-ce6f-37dc-8a79-a7334756679b | -11.47105 | -44.57381 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| a3791436-aa91-37d5-92e8-6ebeba4147d1 | -11.48425 | -44.56561 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0011c8d4-1026-3d27-8aec-2d907ab75bc5 | -11.4603 | -44.55943 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3659978-8a38-3e43-b603-1b3ed2883dcf | -11.46685 | -44.56086 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 83f261ec-b9e9-3b70-8ab6-c352b96e67eb | -11.47879 | -44.56949 | 2026-08-12 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 985653b9-a361-31f1-a989-405bdf0c10ed | -17.81409 | -44.38022 | 2026-08-12 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d0ba524-3326-3eeb-aad2-64da476182b7 | -15.05478 | -45.32784 | 2026-08-12 03:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f13c50c3-aa29-37be-b34c-ec045b618bd7 | -15.52291 | -45.86102 | 2026-08-12 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66a6a8a9-9e36-3fca-b08b-0e718b1dea22 | -15.06119 | -45.32942 | 2026-08-12 03:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2597b1f3-15bd-324e-a2f8-225796e8e8a0 | -14.98111 | -46.59862 | 2026-08-12 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d7d1d72-0a43-3679-9ea8-eb0a1f3734f2 | -14.28254 | -45.28503 | 2026-08-12 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb0b44cb-a81e-36e0-b435-adca5b1e31a0 | -14.27606 | -45.28339 | 2026-08-12 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ce1b62a-cfda-3f5e-935d-a284e38642de | -13.54039 | -46.28087 | 2026-08-12 03:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10d0bbf7-1e9c-31c9-aff8-027706521a8d | -13.54191 | -46.27377 | 2026-08-12 03:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f4c9f40-d09b-30ee-8c9b-2074f192f7cf | -14.27724 | -45.27783 | 2026-08-12 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e29a9e7f-bb62-355b-86ca-852cc8d0fc17 | -15.51643 | -45.85907 | 2026-08-12 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7343d83e-646f-3989-a7fb-94786c342b7f | -14.98814 | -46.59967 | 2026-08-12 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32daa156-3c89-3c6c-95ff-16f226ab1c73 | -14.97986 | -46.60413 | 2026-08-12 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0f5dec3f-c4f4-386f-8223-d737d1727820 | -17.81458 | -44.38244 | 2026-08-12 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 872cdcb4-b4e5-3549-890a-873eca1c8a7f | -18.32091 | -44.30107 | 2026-08-12 03:32:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc2c6015-6c92-3d95-9412-978d5a5b864c | -14.27619 | -45.27702 | 2026-08-12 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc560632-56dd-371d-8a33-9632429fea52 | -14.28146 | -45.28415 | 2026-08-12 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 91c8d5d5-c10b-3e35-90db-1eb72effa71e | -13.53192 | -46.28629 | 2026-08-12 03:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61fdc448-cbd7-3ac8-8177-39563eb3b25e | -17.80886 | -44.38074 | 2026-08-12 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c35ac1a6-d8ee-36ae-b508-aa840f92aef8 | -13.53906 | -46.27605 | 2026-08-12 03:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03738ae6-9788-3fdd-bf5c-0f9a3f20eac7 | -13.546 | -46.27775 | 2026-08-12 03:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca15ef11-979e-3732-9de2-09f6862b2d0e | -21.49371 | -48.63879 | 2026-08-12 03:34:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94d5fea8-5a55-37bc-988b-208bfe7a20e4 | -21.49372 | -48.63728 | 2026-08-12 03:34:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3313b188-51e2-3bad-aab7-c5059d7e5f6b | -20.94119 | -48.90374 | 2026-08-12 03:34:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |


[Clique aqui para ver as próximas entradas](README7.md)
