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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bf426e8-a492-3eb0-ae6b-8fb88c912565 | -11.50423 | -50.46759 | 2025-08-23 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ef2ca2e-355d-3726-81d0-a2f3806f5822 | -9.51004 | -60.55668 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29855e7d-c906-3a2e-899f-28e1d9a171f4 | -9.51679 | -60.51861 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2770e5c6-c670-3943-a0dc-c5b9afe5cd4c | -9.52548 | -60.54955 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e7ab77c-ea7f-3506-9d03-4984e66d9b53 | -14.9525 | -48.01398 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0f75243-8b26-32b2-b05a-c5195fd57580 | -9.9521 | -60.17818 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3135a950-b434-313c-9871-40e74f695fcb | -9.52342 | -60.53449 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e903b09-3329-332b-bd06-ec3e286c061c | -9.528 | -60.53526 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f1452c6-6e59-36e6-8fec-7a376b116f25 | -13.14961 | -46.88046 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9203af6f-b81f-346c-a087-69ec09c8ea04 | -11.11177 | -62.66375 | 2025-08-23 04:53:00 | NOAA-21 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81be1df1-f2cd-3beb-a4ea-8ce362925061 | -15.00643 | -54.8848 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70207424-85a7-3d6e-85a8-0382bbf324b1 | -14.28329 | -58.53063 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2407ca4-066a-3b8b-9253-be4459ea8814 | -13.4619 | -47.03216 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d7da788f-f7d5-34e8-8a99-235b64b31555 | -11.31097 | -55.14391 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2628eb8f-c4c1-3ffe-96f4-cf4e897f0fd2 | -17.26765 | -46.7676 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3db608a0-d750-3158-973f-a91417a0ab39 | -13.48782 | -47.03467 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c83365d-ed58-35bd-8c86-4de9aaaee0be | -12.95584 | -46.30222 | 2025-08-23 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 779e6a41-f4a5-3036-8e52-6ac4a0db4d10 | -14.29235 | -58.52286 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf6580ce-288b-3c68-b7fa-b910662b6235 | -14.78908 | -45.50279 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4e706fc2-a7c3-3973-85de-0fd1b7707d7e | -12.78042 | -48.71127 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4de89309-e5f6-31d5-b6b4-9ab81562c39b | -12.50318 | -53.8191 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0bc8617-243f-3f33-ad36-874e44355aad | -15.06056 | -56.39982 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1ef2bb78-005b-3d14-ae0a-b4d7b3df1386 | -10.60835 | -55.40658 | 2025-08-23 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da097af3-d41e-304b-a8d7-5ca4c8d300d9 | -12.51311 | -53.82069 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2d58e6b-94bf-30fa-b249-35360bd39878 | -14.57508 | -54.51101 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 705f87d0-baae-37b6-a89d-fa147cac3c85 | -14.28409 | -58.52606 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0583add1-de62-3ae4-941d-47b4db38205e | -14.78492 | -45.49223 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 13b7a382-5b2d-32b3-a080-b13e92e5ace8 | -14.77229 | -59.66365 | 2025-08-23 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44f1b181-7cb5-3dde-8efd-4a224df5c951 | -15.02791 | -54.89926 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6ae335e-093e-3377-b05d-70f72eb164b9 | -14.41903 | -53.33486 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 611c73b4-7f35-3d6e-9747-e3a540ef0c68 | -13.4831 | -47.03439 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab93afa8-db21-3fc2-a994-546e0027a46e | -9.96097 | -60.17973 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 77723e0f-915b-393e-bebf-d98bcbc95bbb | -15.00149 | -54.87303 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c048a662-4e32-32a4-a7ea-ebf6179fdf5b | -14.68142 | -56.61385 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f758a128-b16c-385e-9c19-ec4851cd6615 | -9.24496 | -60.48122 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c0c9c05-34bc-31f2-82b7-16df4bc70cbf | -14.69971 | -54.91038 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc5c16eb-2db3-3531-a5c9-69b1b5a6af88 | -13.50129 | -47.04138 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4852bdf5-b0ac-3a94-92f6-0c76c04d1583 | -14.82437 | -47.96206 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c64b81ac-fc74-3270-86d6-c5ceaa679d78 | -13.36806 | -54.40058 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65be36b3-502f-33c8-a84f-327653b3ebcd | -12.98527 | -56.90115 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d8b4e60-f85e-3269-a94b-eda716086df5 | -14.66033 | -54.85672 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85d255d5-6b19-38a9-9ad4-a52c9f911b6b | -15.01854 | -54.89408 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72f26c3e-0eb1-3045-ba53-85be8b3a369c | -8.87616 | -62.42616 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7693c20b-5fd3-3de7-b2fe-2c8ed4a0466a | -9.95416 | -60.19211 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 222.7 |
| 89f31a5e-b2a0-3264-bfed-2da6e8391329 | -14.33325 | -53.09159 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 848b3cdd-5312-3bb3-a2d4-3377871e1f26 | -8.89192 | -62.42899 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9e2aeea-e177-3f5e-a229-e8d02131bbac | -13.03531 | -46.3243 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8e646d42-5eec-37c7-a5ac-530cfc997445 | -9.24037 | -60.48045 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 17c42dac-6b47-32e5-857f-865b2c26b25c | -15.55359 | -51.6933 | 2025-08-23 04:53:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6378a1d3-ed03-3391-be76-6a1bef198c0f | -14.61902 | -54.83895 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77063176-7848-30dc-90ac-c23c6ee617a6 | -15.02241 | -54.89107 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8dec28f7-1b46-3d12-be2b-464e6321df22 | -17.27254 | -46.76786 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ff2bbb57-ea35-3311-9180-9430543badd9 | -14.75854 | -55.99114 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d621fa59-ee59-38d3-a67a-d7022a850561 | -9.95069 | -60.1931 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4cd14521-6485-380a-9b9f-37fe50ce2958 | -14.31739 | -58.55583 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09ae97c2-c35a-3cc3-ad08-947ab470ad66 | -9.95221 | -60.18433 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 77f3ebe9-6529-3d4e-ac9b-51759b8fe2de | -15.02516 | -54.89516 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3b0044f5-575f-3e9e-a828-ea53e5cad3bc | -15.07137 | -48.48747 | 2025-08-23 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b4bed27-4d79-39d1-becc-ad08db0afeb9 | -15.56046 | -42.68733 | 2025-08-23 04:53:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 571285c3-312b-3fe5-95a3-f79cbd386020 | -12.94299 | -46.30775 | 2025-08-23 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 33c5034d-f502-3718-886c-c36485df9d0d | -12.30346 | -49.99641 | 2025-08-23 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01031086-ed0d-3ef8-b818-b9e21aac52e6 | -14.99818 | -54.87249 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c3276d1-a487-3221-94f0-4228a72062b8 | -17.27704 | -46.77451 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cef728db-6744-31c1-a9fc-21611806e65a | -12.51366 | -53.81716 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d170bca7-d05d-3d93-8f9f-70b5d2cbb515 | -9.5251 | -60.52496 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 32c82179-600e-3a4e-be4f-d3c47bc837d5 | -10.46518 | -59.1379 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee4fe4d8-4613-37ff-ab9a-4b665526146f | -14.63429 | -59.5523 | 2025-08-23 04:53:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da989e39-4456-3461-b64e-e350ba3af46b | -12.99777 | -45.2193 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f3f2a41-61d1-3b6d-bac2-e17496dfda48 | -13.42001 | -46.27645 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 528feea2-7cf8-303a-b75c-a62908080ab3 | -11.3223 | -55.2236 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ad7fd1e-9153-30aa-8bb8-0ca571deabee | -9.94625 | -60.19231 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d3f0f248-eb6b-3c52-bd92-a7afac944e6e | -13.04327 | -46.79788 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1abddee3-6538-3060-afc1-9c00320edd2e | -14.61571 | -54.83841 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8803c08-fca0-3586-bb60-d75989477028 | -13.03482 | -56.82708 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14511151-ad83-3546-852f-42fa61b9a51b | -11.51092 | -50.47305 | 2025-08-23 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 060a32be-fbb9-38df-b4ca-ccabfb09f234 | -13.72082 | -44.40013 | 2025-08-23 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c70db947-7401-3ba8-b874-8b8049bb57c3 | -9.50309 | -60.51611 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c36d9bd1-a793-3ded-a185-796eb71acb29 | -14.47003 | -55.94596 | 2025-08-23 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de150b27-b3e6-32e2-ba5e-7f169862cba7 | -14.94341 | -48.01386 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07bb009c-d313-3e6e-a745-8a08633ff5d6 | -14.69366 | -54.90573 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a689019-8908-341e-b657-692fef7eda20 | -12.51035 | -53.81663 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e00fa6dc-3a50-3354-a3bd-7816e55aff43 | -16.23744 | -48.76146 | 2025-08-23 04:53:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 131cf1af-68f4-32f8-b26b-e4c0e4f7c5ea | -13.51005 | -47.04765 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e4d1c66-56bb-3109-b849-1073a5d02316 | -13.35814 | -54.39897 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53cc918c-29b9-3fd9-8173-d5d0fdda4ea8 | -14.47129 | -56.48082 | 2025-08-23 04:53:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3581338-b57e-3452-9d5f-a1ca18d4367b | -14.68545 | -56.61066 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b2fccb8-05bf-32fb-ba6b-52e83bff31d8 | -13.4862 | -47.02847 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02de77ca-4566-3a47-9311-9f8c4f88f387 | -14.67801 | -56.61325 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9a9bac37-d82d-3594-9fb3-aad767e27f71 | -14.27428 | -58.53036 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d44c69e-8971-35b6-9412-444a0b8d21c1 | -14.60586 | -54.79309 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5ba4534-7a32-3f1e-abc9-dcf4a857786d | -11.29516 | -53.95498 | 2025-08-23 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca04c9e8-8a16-3b5f-89f9-0141374a0bfe | -14.59174 | -53.16238 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f126be7f-cc59-36de-9d5f-970634e04550 | -17.27341 | -46.76196 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8721a927-1e6a-3327-a806-89e13d59913e | -9.51968 | -60.52895 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e5558a2-c579-3d12-a82a-9f8bd942dff3 | -13.38185 | -46.20765 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d553772b-f372-33b3-8cd6-214d33f7cdf9 | -11.18872 | -55.03477 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d992ceb-a14d-357b-ad5f-10e9f520f65f | -8.69784 | -62.87695 | 2025-08-23 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7029802-b256-348c-8f55-7268247dbf9a | -9.96184 | -60.18151 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 434cc2f2-facf-3360-b3f0-cb40c7b54265 | -14.32932 | -53.09474 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2aa42ae5-c8c5-365f-993a-5ddb837f5ac2 | -10.40803 | -57.68272 | 2025-08-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README55.md)
