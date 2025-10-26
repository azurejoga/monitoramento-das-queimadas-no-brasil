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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e843722a-6e77-3043-a79f-4c93877274c8 | -14.89096 | -52.4783 | 2025-10-26 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 047cb01f-84c8-395a-a6f4-0c011e2ce134 | -19.32689 | -49.80871 | 2025-10-26 04:53:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf9ab1db-43d1-32aa-8b8f-41cbf72a3197 | -16.40691 | -54.04907 | 2025-10-26 04:53:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d23e3b8e-b30a-3e6a-8298-851d37135c60 | -14.76504 | -46.61553 | 2025-10-26 04:53:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0e249c2-9e57-387a-a596-8bb693fd95dc | -17.43389 | -46.88263 | 2025-10-26 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae98a132-0829-3a01-9205-08eb418672ec | -17.32638 | -43.65679 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 18bff768-98e5-35e4-96fd-c98dbd13295e | -15.27108 | -43.18418 | 2025-10-26 04:53:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 90c91f6a-e74c-3ae9-9c66-c18ac43e0c82 | -17.32784 | -43.64167 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cabfa4d9-df2e-3edd-a0f5-63f83db957d8 | -15.9364 | -51.06327 | 2025-10-26 04:53:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 40be49ef-5109-30bb-bd16-6d5c966c405f | -14.83787 | -52.43471 | 2025-10-26 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bdd24ba-5040-32b8-9c56-49de0fca150e | -14.8373 | -52.43858 | 2025-10-26 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd832742-98a8-3ef0-9f99-1b2aaa26b5c2 | -17.13826 | -55.74381 | 2025-10-26 04:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 219ae219-0ffd-3727-b86b-dd48b9005017 | -16.6157 | -44.57468 | 2025-10-26 04:53:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9496ac9a-e94f-3c86-a729-2e088b29ac0a | -14.89039 | -52.48217 | 2025-10-26 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70db26e4-713e-3a9f-9af8-d99a9bc95c6d | -14.9206 | -52.46727 | 2025-10-26 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c3f379f-e674-3049-8a03-97edeb511766 | -17.31455 | -43.63481 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58478c11-77a8-38cd-9488-834881decb01 | -17.31532 | -43.64486 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da6bdd4f-787b-3015-a46c-3fd03ce92b0e | -15.85199 | -53.58403 | 2025-10-26 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d2a0572-4c0a-334a-a656-213e35d5655f | -17.37644 | -52.01672 | 2025-10-26 04:53:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba8114d6-c537-3c45-a412-b187f7bf38ea | -14.76989 | -46.61589 | 2025-10-26 04:53:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b8dba59-983d-3bd0-bb81-38da5070d872 | -17.31663 | -43.63121 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b965e287-9d2b-3930-8fe4-93faac4e43c0 | -17.33388 | -43.6424 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31edbfaf-dd82-33a9-831e-557e18f0e9c1 | -17.32565 | -43.64571 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cf4cface-23db-39a3-acf4-acb631f3887a | -14.65508 | -50.18445 | 2025-10-26 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 707879d8-9594-37a9-9e16-f2f633f5e2ce | -17.32616 | -43.64076 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6a2f4771-4ade-3e10-a373-4b337b458a66 | -19.62864 | -50.62312 | 2025-10-26 04:53:00 | NOAA-21 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28068fb7-f4a7-3fb0-8d29-2f7cfea47d24 | -14.89719 | -57.55423 | 2025-10-26 04:53:00 | NOAA-21 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9706cc16-6be7-3885-8bfc-6023a17910b4 | -15.33417 | -42.81567 | 2025-10-26 04:53:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7c3037a-0dc9-3973-9438-4af55b73748c | -15.46059 | -50.47816 | 2025-10-26 04:53:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 903f35bd-c573-3cf3-8dd7-74f3b5cded1b | -15.4682 | -50.47894 | 2025-10-26 04:53:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28f1bb74-77f8-3410-8630-da0394193058 | -17.3283 | -43.63692 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0b45f2d3-3d75-3b1e-94ea-8417bc7ec904 | -17.01657 | -55.90588 | 2025-10-26 04:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 87e5f39a-70b1-3eec-8184-ac88e5ce5c5e | -14.92119 | -52.46337 | 2025-10-26 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa95d3e8-1122-3146-84d6-3ee3a9e3a64f | -15.60588 | -46.79062 | 2025-10-26 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ab9a0b2-1fd5-347c-9e2d-de355a5b572e | -19.3232 | -49.80443 | 2025-10-26 04:53:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42745d9e-e32a-3b1b-a537-e1d9ccc8821d | -15.94438 | -51.05996 | 2025-10-26 04:53:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd48d8ff-9f1f-3da7-b7a3-76e4a9b90b07 | -17.34139 | -55.01933 | 2025-10-26 04:53:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| db230363-b7ab-30d1-a1b7-5fc4d7adc171 | -16.09351 | -57.27499 | 2025-10-26 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6c2d041-d12f-35d8-b516-569fd3df6d57 | -17.53417 | -51.04757 | 2025-10-26 04:53:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33c026b8-1770-3968-a502-52913a2ffe31 | -15.45997 | -50.48271 | 2025-10-26 04:53:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b49f9d2-717e-3dfa-abaf-c33642e6fc95 | -15.33468 | -42.81072 | 2025-10-26 04:53:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3240d3f-6196-339a-8ea0-dbc2760f488e | -14.80306 | -54.69615 | 2025-10-26 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71e81ef7-1ded-3fc6-a76c-0007d691f653 | -15.36607 | -42.92659 | 2025-10-26 04:53:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 985101d0-850c-37f7-935f-2c1d8638d7a8 | -16.74787 | -52.32375 | 2025-10-26 04:53:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 543512ca-912c-31e7-b9db-6a247b00ee67 | -17.31313 | -43.64864 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1df90a1f-3231-366f-9fe9-d5018715e9e2 | -16.62556 | -46.29271 | 2025-10-26 04:53:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ecb3319d-f012-353d-8b5d-4c382bbca2d9 | -15.35943 | -42.93054 | 2025-10-26 04:53:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 37a5f6f2-8bff-30b9-9a9e-e050110a5b6e | -17.37723 | -52.01854 | 2025-10-26 04:53:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe533e56-90ae-394c-b70d-419294a63de8 | -17.4241 | -46.88119 | 2025-10-26 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6c26a588-9074-31fe-96df-2fdde6fc8881 | -14.39565 | -51.53909 | 2025-10-26 04:53:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a99e61c9-0122-3f3f-b340-f81ac8780c20 | -14.89438 | -52.47883 | 2025-10-26 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 258ff7a8-f684-3ae5-b670-f3a22701bb73 | -16.9257 | -55.53984 | 2025-10-26 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c2d197aa-fb3d-3f8e-8ddb-f8e52c9a9a71 | -15.62003 | -48.90519 | 2025-10-26 04:53:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42efe3f7-2ee4-3c0d-a04d-d2cbab053742 | -17.32012 | -43.64002 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4b69f087-65c9-3350-985c-81eebe45acd3 | -15.25062 | -50.76349 | 2025-10-26 04:53:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c5ddefd-b435-3fda-a009-186f7f622f9c | -14.89362 | -57.55358 | 2025-10-26 04:53:00 | NOAA-21 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3067114-db17-31ca-bf73-7cc97cc355e8 | -15.36224 | -49.50711 | 2025-10-26 04:53:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 245b5ed6-b1b0-37bf-8dc8-855d7b55c8f2 | -17.42054 | -46.86868 | 2025-10-26 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8de000f-53cc-3610-b28d-854c09ce89e4 | -17.05244 | -51.52022 | 2025-10-26 04:53:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19054edb-674f-3d2b-8b37-bf4c4d9f3894 | -17.32736 | -43.64663 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d38c50b-8899-3dae-954f-85ddf19c681b | -15.3627 | -49.50364 | 2025-10-26 04:53:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7685b1bc-b6a4-3fa8-bb37-adbeddc9abb6 | -17.34195 | -55.01574 | 2025-10-26 04:53:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f8c5095c-5218-3214-bdce-2a5e7b1975c0 | -15.25431 | -50.76415 | 2025-10-26 04:53:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54980a7b-f25f-3946-8cbe-a0a3802d918d | -15.84865 | -53.58349 | 2025-10-26 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f295c25-e4aa-3d5f-bef2-ec5f43279b1b | -14.44204 | -49.96076 | 2025-10-26 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 72906d45-04f6-3d24-8af3-40fd44537149 | -14.43819 | -49.96021 | 2025-10-26 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c8548f21-ae4e-362c-9129-254452b1c775 | -17.13494 | -55.74324 | 2025-10-26 04:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 80ce2dcf-ce2e-3acb-87f1-3c6b25458edc | -14.50095 | -57.34156 | 2025-10-26 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 629cf00b-4e62-38d6-9b17-72f7222e13b1 | -17.31962 | -43.64494 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1015564e-62a9-37d6-a97a-3707453d29fd | -14.74232 | -49.69168 | 2025-10-26 04:53:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc324120-49ab-3658-b07c-4b0d70594506 | -14.54973 | -50.99265 | 2025-10-26 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc5fed6f-bda0-37cf-92da-477231ebfc11 | -15.26976 | -50.76209 | 2025-10-26 04:53:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 728871a8-343c-39d6-99c0-bc9d0f8dd167 | -19.40726 | -45.87452 | 2025-10-26 04:53:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40166a7a-8912-3d96-aede-9bcbce43592f | -14.83843 | -52.43081 | 2025-10-26 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c3570f1-1888-3d61-a8bb-1abe3aecb93c | -15.25126 | -50.75894 | 2025-10-26 04:53:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce35144a-a1ef-3a0f-a33f-0e75169d946e | -20.3198 | -46.5394 | 2025-10-26 04:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da98a061-5ab6-39da-9e20-3a6c965467e4 | -15.29897 | -50.75854 | 2025-10-26 04:53:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 81702176-7f0c-3c37-9c3e-816ceb5518e2 | -17.31409 | -43.63929 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 801eed6c-991e-3c0c-a0bf-7d9b2cb68dd2 | -14.8727 | -52.45977 | 2025-10-26 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7fc115f-8edf-3107-862f-b8e5ed8a9115 | -14.92002 | -52.47116 | 2025-10-26 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0f03f13-45bf-3ec4-af2d-1e48454cc80b | -15.68598 | -49.41147 | 2025-10-26 04:53:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 992fa7b6-d065-3e76-a454-fc866671670e | -20.45714 | -49.8839 | 2025-10-26 04:53:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b7a269b-b167-3e23-a231-57f007b87a51 | -17.42477 | -46.8753 | 2025-10-26 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ccd06ff-e8aa-3d41-b0e4-68e2b97c8a09 | -16.61529 | -44.57849 | 2025-10-26 04:53:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3bd948ea-f6bd-3762-a90c-dd86f1417a89 | -14.59468 | -53.11992 | 2025-10-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b1e2978-7262-3e2b-9d01-5764a0f632bb | -15.29678 | -42.9352 | 2025-10-26 04:53:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e9992ecd-23a5-32e0-81ee-f6c906a8493c | -13.77002 | -56.12303 | 2025-10-26 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 829a16c4-07b0-3dd9-94bd-234f6494d7b5 | -14.9797 | -54.82808 | 2025-10-26 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eed4b14d-f004-3f0b-aae6-ed9dc96651f0 | -15.94008 | -51.06382 | 2025-10-26 04:53:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81883276-a794-3c88-9e10-c1028d58fe28 | -14.83674 | -52.44241 | 2025-10-26 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 037643d3-2c73-36e3-8061-3929dbf6977d | -14.65442 | -50.18924 | 2025-10-26 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68d3a095-2810-36d4-9ca0-88cacd17323d | -15.59171 | -43.21322 | 2025-10-26 04:53:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cb26841c-2af8-3ffe-bdc9-0baa48e0a847 | -15.83235 | -49.07493 | 2025-10-26 04:53:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99439e1c-a3a3-315c-b227-d0a839f672b4 | -16.31455 | -50.04787 | 2025-10-26 04:53:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e179849-8519-3749-835c-2cfa28f3e8c1 | -15.36625 | -49.50765 | 2025-10-26 04:53:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6586591c-c267-3d77-ad09-eb933fda480c | -14.55034 | -50.9883 | 2025-10-26 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0cbb885-092a-320d-9705-8d2fc8e4dc9d | -16.46294 | -52.69476 | 2025-10-26 04:53:00 | NOAA-21 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd14ef9b-33bd-3b20-ab69-65bab7a88737 | -16.22536 | -48.65256 | 2025-10-26 04:53:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3d80693-8b91-3059-991c-aee94631da46 | -14.5583 | -49.60338 | 2025-10-26 04:53:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a02e59c1-c5e5-3de7-ba42-68812f2719cd | -14.91886 | -52.47894 | 2025-10-26 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README46.md)
