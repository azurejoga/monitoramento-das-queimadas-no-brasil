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
| d6dcf20f-79cd-32e8-9c5a-6b7efd0a6f70 | -10.99796 | -46.50911 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8dea111e-f0ab-3e71-8489-acd37011bd9e | -11.52334 | -47.67038 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| df2daa3a-254a-3013-b474-2125842c4390 | -15.74423 | -46.26254 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b9e7eef-cb6a-3b1d-8f39-e1f77598a87a | -13.73493 | -47.96655 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d628900b-127c-3836-88bc-deb3037b1b2f | -12.93868 | -51.01118 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98692361-a9cf-349f-b73c-5daf6ae613cd | -14.68867 | -48.33881 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 730ff154-4a05-36d7-bcd5-040916a05507 | -16.35433 | -51.48258 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e1b40e8-0dae-3b6d-bc39-96bc34947345 | -14.69351 | -48.34001 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 434f4cf4-ce7c-31bc-9b79-bab78b9271c2 | -16.009 | -50.85385 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8e47b8c0-90d5-3f95-a90b-d9b0a8d3c3bc | -11.68757 | -47.48848 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cecad179-7f06-3bc2-bf32-4ab1c3b6e647 | -11.91735 | -46.25299 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c47c367f-dcd0-3e3a-b7d4-b439a378492e | -15.34677 | -47.33622 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d66f2852-9e3f-3556-bc5a-263f6716ef66 | -14.93733 | -46.84089 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abff6f3e-b5c9-35ca-8ee6-6a5e0df76187 | -13.25368 | -47.81639 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9393976c-6a3b-3cce-aa6e-83b88c780971 | -12.92579 | -42.38357 | 2025-10-05 03:55:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6bb25cf5-0278-33e4-8825-53e47c35ae9b | -13.52115 | -47.24068 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 440efa09-b8d1-3cc9-ba29-97bfa31e6a69 | -11.45611 | -51.5235 | 2025-10-05 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b45c9fe3-32dc-3540-b8e7-580230a4e164 | -11.78332 | -47.55627 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84e05f02-4db0-34bf-a931-0f0873d2e233 | -13.09314 | -47.83691 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 901f52a3-4227-37b8-92e7-cfa96673d6a6 | -10.94475 | -47.06137 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7a147d94-7ec2-31f3-992a-c01d31aa6d61 | -18.33331 | -45.88633 | 2025-10-05 03:55:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 495d4f2c-09e9-3f8d-9f87-d332481023e6 | -12.10467 | -43.44773 | 2025-10-05 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaa11aaa-c2b1-3aa7-a662-47687077c32a | -11.80161 | -46.82063 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30005730-7bd4-3f79-a2d1-9ef705e88aef | -11.01833 | -46.71304 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 450e5ce3-6fc5-327a-8271-a64ed058ed7d | -11.09518 | -47.75642 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c9dab39-f8a8-3fc3-9896-9dc007fb900b | -13.28346 | -47.58498 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 14f42210-538f-3602-9532-b8c387cbda8c | -14.9869 | -49.98164 | 2025-10-05 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff33c760-cee9-3a66-a4de-983dcadf50f9 | -12.104 | -45.14246 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c6e5face-1b1b-3fe2-8c8f-364e1e050d99 | -14.32825 | -47.69904 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d81e856e-1d92-32fe-be57-b90435a502d0 | -12.23081 | -47.83552 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9ebbdba-719e-39e4-9c6a-f06f6326af19 | -11.83086 | -45.09405 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7747f25d-86fe-3a57-a980-296b33bdca76 | -15.36226 | -47.9761 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e185e32e-d49a-3e36-9435-17e97b6c5fb7 | -14.92216 | -46.84873 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 91f7e5c8-42cf-39d4-9a05-a8fde15c41b4 | -14.68033 | -48.35532 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f7d258fb-ba3e-3432-b05f-ef4ee85ef873 | -14.88841 | -48.25989 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17dc5a0d-b4a8-392f-a979-5221c32c718f | -14.94902 | -46.84686 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec1c96b2-6511-3f56-a4e2-b04e801d09c5 | -12.1193 | -50.90984 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2967d4b0-4a54-3937-90a8-994da713542f | -18.20269 | -53.37904 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e6daddf-ac0b-3116-9b50-b3de85fde23a | -21.69029 | -48.42197 | 2025-10-05 03:57:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 39c6ae50-7456-3a15-b1ba-ace51e599152 | -19.78244 | -43.66705 | 2025-10-05 03:57:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4143734e-faf1-39d3-a935-c10fc97a994b | -22.64575 | -42.80915 | 2025-10-05 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 47c00e0e-da59-36fb-acec-39e9f1db5b75 | -22.48499 | -46.81385 | 2025-10-05 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a87266a-debe-3e7a-9c38-cdb495a64316 | -20.7316 | -44.33006 | 2025-10-05 03:57:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 813c3202-4ecc-3f04-bc12-ba513d39fd80 | -22.48018 | -46.81807 | 2025-10-05 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc94e09f-5807-363c-87ed-a2d30522192f | -22.96037 | -45.45595 | 2025-10-05 03:57:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 826ad8a4-da3e-37dd-a480-db334efe5f99 | -19.94436 | -44.38719 | 2025-10-05 03:57:00 | NOAA-20 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5247a7cb-4297-3b8a-a315-c3c2e089244c | -22.15456 | -50.02493 | 2025-10-05 03:57:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8c867981-7cff-3241-928b-c99ede3d420c | -18.17379 | -53.36168 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7295990a-be39-3f07-be0f-7df8ddd955de | -22.48132 | -46.8146 | 2025-10-05 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43e5982b-55be-360e-9bfe-1a474adffbc5 | -20.77619 | -49.38702 | 2025-10-05 03:57:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6dfd244a-4413-3067-b8bc-52b07cd16958 | -20.73376 | -49.62374 | 2025-10-05 03:57:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 39ac35fd-fd13-3108-bdb8-4b5e1ebc1121 | -18.31215 | -47.44084 | 2025-10-05 03:57:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96b9a415-bde4-3d42-aa72-5eb6f519d2cd | -19.50947 | -50.37677 | 2025-10-05 03:57:00 | NOAA-20 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 334e55af-7d1f-3936-9ae7-7a4ac7e7e02d | -19.94907 | -44.64529 | 2025-10-05 03:57:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 809a4a19-c860-39e6-ae11-44b84f9a8ec9 | -19.51016 | -50.37351 | 2025-10-05 03:57:00 | NOAA-20 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bc502f7-9fb6-3c4b-88ea-ece7a8678742 | -19.06705 | -46.90229 | 2025-10-05 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa5b818a-3a0f-33ec-8b8a-0234d0b14580 | -21.59299 | -45.27469 | 2025-10-05 03:57:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a54f37b3-d469-3d60-97d5-ddef8df8210f | -19.24128 | -47.85489 | 2025-10-05 03:57:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4883585-71b6-30cf-8722-d6158c05ec92 | -18.18414 | -53.35836 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b3f3268b-3648-3de4-85d3-29a593be9100 | -23.39059 | -46.79884 | 2025-10-05 03:57:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d94606cd-d775-3d37-b026-f204a4f2538f | -22.69746 | -44.45914 | 2025-10-05 03:57:00 | NOAA-20 | ARAPEÍ | SÃO PAULO | Brasil | 3503158 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ac46c371-3ef7-3096-8f52-8ff4e18b09c3 | -19.95066 | -44.63634 | 2025-10-05 03:57:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 094d7551-3d6a-3a68-a4ba-741b6abd0a8e | -19.01529 | -50.59961 | 2025-10-05 03:57:00 | NOAA-20 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| ceca45b5-4987-3a93-809f-a321c818ed1e | -18.23805 | -53.36789 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5bf690aa-2b6f-3cb3-b97c-3d13efa617b0 | -19.49448 | -43.62791 | 2025-10-05 03:57:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f4d0f7e-e5fb-3674-b99a-4ae5c4a56083 | -20.32251 | -47.73628 | 2025-10-05 03:57:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 275dbd5d-60bb-3a97-b226-d8cb5342ca3e | -20.32758 | -47.73286 | 2025-10-05 03:57:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66ad419a-0077-3ebb-85a6-f5e0b3174b3d | -20.74213 | -44.33204 | 2025-10-05 03:57:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0b28d523-c003-3319-b106-05f9eb79fad1 | -20.73368 | -49.62295 | 2025-10-05 03:57:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 79d876d2-d976-30e9-a6bc-1b35e79fc1aa | -21.68943 | -48.42628 | 2025-10-05 03:57:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 25d9a300-5250-3cc6-8d15-dc9fb8fb2e71 | -20.56342 | -44.04041 | 2025-10-05 03:57:00 | NOAA-20 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1909edb6-6f91-3bd4-833d-373fa1aab6dd | -21.58938 | -45.2739 | 2025-10-05 03:57:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5bd4d664-8eab-3c7a-91c9-c15828eccc2e | -20.73008 | -49.61629 | 2025-10-05 03:57:00 | NOAA-20 | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f4e7ee54-fd2d-325f-b473-02c8e6e305a1 | -20.91517 | -45.15193 | 2025-10-05 03:57:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c6601d98-2df7-36bb-b977-296a09b96ecd | -18.18793 | -53.35738 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9780510a-1bc8-3bb9-ae31-311a1922c4d7 | -19.8636 | -45.69674 | 2025-10-05 03:57:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1180738e-c225-32d0-b513-ff779e5987aa | -22.93806 | -45.40731 | 2025-10-05 03:57:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3102a984-fa7d-31e4-acb7-5a368dec10e3 | -19.58915 | -44.63536 | 2025-10-05 03:57:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18286104-78d9-3a50-b8c5-03771c19cb4f | -20.73863 | -44.33134 | 2025-10-05 03:57:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8f58f00f-681b-3229-8f04-d9fa5f9f5cfa | -20.06876 | -44.21464 | 2025-10-05 03:57:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8d9b0012-15a4-3339-b308-997892bfbac3 | -21.58496 | -45.27763 | 2025-10-05 03:57:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fff179d9-794a-37ad-b2fe-5f8eab857100 | -19.63048 | -45.97087 | 2025-10-05 03:57:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f73e93ad-3477-338d-b787-3c21a2173132 | -21.55943 | -43.98962 | 2025-10-05 03:57:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 156199cf-7dfc-3105-908c-a685bf1e4adb | -23.20221 | -45.10381 | 2025-10-05 03:57:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fbc3de39-c443-3398-b9bc-f826ffb9fd0f | -22.75598 | -42.01658 | 2025-10-05 03:57:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8d847697-85e9-3a52-a971-b151effa61e5 | -19.83891 | -46.52217 | 2025-10-05 03:57:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e44b0529-4649-3b64-8f38-b1b5f6f8cf45 | -17.9691 | -51.14915 | 2025-10-05 03:57:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53c46ac9-43cd-3e51-a27d-8ea69612f320 | -21.82554 | -47.40144 | 2025-10-05 03:57:00 | NOAA-20 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 02466163-2698-3a36-96f5-dfff8c23bf8d | -22.20578 | -42.98458 | 2025-10-05 03:57:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1e1ab096-1b2d-376d-b277-9305852457a5 | -22.96118 | -45.4515 | 2025-10-05 03:57:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a5e7a966-f699-3b4f-a8e4-57be75e25961 | -19.5051 | -50.37225 | 2025-10-05 03:57:00 | NOAA-20 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b42f581-2c72-3502-9162-982dab4a21eb | -19.12572 | -44.6435 | 2025-10-05 03:57:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3b13c62-f3d4-305e-b08f-4c3244adfddc | -19.63437 | -45.97151 | 2025-10-05 03:57:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 379fed39-9a53-3fa2-9717-8c72d2acae14 | -19.01454 | -50.6031 | 2025-10-05 03:57:00 | NOAA-20 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 0be38592-9f88-3096-aa28-30578825f8e6 | -21.16972 | -44.27479 | 2025-10-05 03:57:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f2036d77-57bf-3821-b50f-800def775205 | -18.24603 | -53.33257 | 2025-10-05 03:57:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eb853abf-e4e7-3287-80dc-e07f5372da42 | -22.36826 | -50.02408 | 2025-10-05 03:57:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fac443a2-33c0-3083-8c22-a94f6a311c17 | -23.01704 | -46.24769 | 2025-10-05 03:57:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 84753787-be1c-3967-b2bd-18c92aa8f85d | -18.14181 | -53.34218 | 2025-10-05 03:57:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b4a3eea1-496e-3707-8733-259b7dfc664a | -20.06122 | -44.60662 | 2025-10-05 03:57:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README70.md)
