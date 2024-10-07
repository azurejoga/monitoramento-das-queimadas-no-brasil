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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1889c95a-2b6a-3618-938c-b59da56bcde7 | -11.92572 | -50.09017 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| be179b0e-9ef2-3659-b644-00571382096e | -11.92452 | -50.09656 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c29d978-0c74-3a30-9457-70d005d5e60b | -11.92056 | -50.08911 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9d907728-a36d-348e-ab57-0554a4cc8e41 | -11.92029 | -50.11897 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6b2ece2-0036-3a2f-80b4-17affdb6bcaa | -11.91995 | -50.09231 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8adc9f69-2d08-32de-87ed-dec3e78fc5c1 | -11.91572 | -50.11472 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2687e600-644b-35ab-8e0c-56b7ba91df41 | -16.3159 | -51.27748 | 2024-10-07 04:02:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3e6aaf6-dac9-3f30-bad5-618d237b80fc | -16.31467 | -51.28352 | 2024-10-07 04:02:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2cc9f3e-8bab-3618-b526-664024608b5c | -16.31407 | -51.28648 | 2024-10-07 04:02:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b1fe0e6-2cf9-3199-89c7-9921a34b8f9d | -16.31133 | -51.27354 | 2024-10-07 04:02:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e86221ae-3cdd-3af8-84f3-8b8909c4adb8 | -16.31067 | -51.27676 | 2024-10-07 04:02:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3392d88-0534-3b58-ad56-79bbcef2461f | -16.31003 | -51.2799 | 2024-10-07 04:02:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15c5141b-19f9-3c9a-8830-3024ea26df2f | -16.30943 | -51.28289 | 2024-10-07 04:02:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8794e964-0e05-3088-8e3a-0059a466eab0 | -16.30881 | -51.28588 | 2024-10-07 04:02:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5ec0deb-fea8-3503-97c7-bf799b841da3 | -16.20119 | -50.92599 | 2024-10-07 04:02:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8ea13d8-063a-3bbf-8ca2-755f2f60bec0 | -16.20058 | -50.92902 | 2024-10-07 04:02:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25ceb730-b802-397f-84f5-a5a5554f29e6 | -16.18922 | -50.93315 | 2024-10-07 04:02:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6f905a3-87e1-3abf-a3fb-638cb32a1608 | -16.18414 | -50.93219 | 2024-10-07 04:02:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce4c0a38-0bf3-3cd3-af50-3fc673303235 | -16.18291 | -50.93832 | 2024-10-07 04:02:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c39fcd0-5b08-351c-b897-ae3c7cbdaf01 | -16.18167 | -50.94454 | 2024-10-07 04:02:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd7a1e68-f039-3f73-8ace-5b7dbe08ab06 | -16.17784 | -50.93736 | 2024-10-07 04:02:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dba1f9de-a816-3a46-a757-559c5f6991c0 | -16.17722 | -50.94044 | 2024-10-07 04:02:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 763512d8-6f44-3e35-9f91-e3c00ea205b4 | -16.17278 | -50.93631 | 2024-10-07 04:02:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35cfed0d-bdf5-3551-a0d1-75a31f48035d | -16.0633 | -50.44662 | 2024-10-07 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df068711-f55b-30a5-8b80-78ed356d491d | -16.05837 | -50.44564 | 2024-10-07 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9d7ad28-e75a-316b-a375-b12d7dffd81f | -16.05233 | -50.45035 | 2024-10-07 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d31a453-8793-30eb-9663-8071cebf74ae | -17.24236 | -50.715 | 2024-10-07 04:02:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f664f5a-561f-309a-847e-d7e1ccc8b147 | -17.24121 | -50.72085 | 2024-10-07 04:02:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6923373b-a24d-3e3c-818a-7bfba666ecde | -17.13999 | -51.71491 | 2024-10-07 04:02:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7a357417-bbac-3d18-8af8-8f0b67a41b08 | -17.1393 | -51.71832 | 2024-10-07 04:02:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| cc37d571-127e-3ed9-84f6-78abc8a6ec34 | -17.13409 | -51.71712 | 2024-10-07 04:02:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| dab624d1-b991-31b6-9091-7281b3d700bb | -17.13025 | -51.70927 | 2024-10-07 04:02:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f5ea7fb-7c46-3d93-a841-ae4d056341ca | -17.12955 | -51.71268 | 2024-10-07 04:02:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f72ce63-639d-3f04-b2bd-d2755421b9b5 | -17.12888 | -51.71595 | 2024-10-07 04:02:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a633cfed-2b96-3f1a-9534-37e823aebff9 | -17.11254 | -51.71586 | 2024-10-07 04:02:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc1978f9-685c-3b7e-a0d4-d5b39d539f93 | -17.11184 | -51.71928 | 2024-10-07 04:02:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6badf5c6-3813-3d3e-925a-b8bdfdee2bdb | -17.11114 | -51.72267 | 2024-10-07 04:02:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 39a9b450-001f-3acb-b009-ec8978613156 | -17.10662 | -51.71812 | 2024-10-07 04:02:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ce86faf-7e7e-3047-85a4-dc5b8cb99dcb | -17.10593 | -51.7215 | 2024-10-07 04:02:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c316403-d682-32dd-8ac9-1ebae43b6a7b | -11.29041 | -51.37217 | 2024-10-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f6f9953-c832-377f-9764-d7a8730bd839 | -11.29022 | -51.38247 | 2024-10-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 93c91867-0de6-35f6-8171-ff6bebdfa917 | -11.28965 | -51.37617 | 2024-10-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b953ecc0-ab4b-31cd-b737-4b706bbc82ca | -11.28611 | -51.37335 | 2024-10-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4a9f33b3-073f-3da8-a000-70b1e6cd2a99 | -11.28532 | -51.37734 | 2024-10-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| df75ad86-869b-3a21-a89c-0b72ad54d75a | -11.28397 | -51.375 | 2024-10-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c7a70d65-0e1c-34b7-951c-a379fe0986cd | -11.25556 | -51.36917 | 2024-10-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1149a55e-5491-3843-a75f-3110660dc8a8 | -17.67099 | -53.08763 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ffc2727-282e-319c-b00d-bdda4a564872 | -17.66624 | -53.08232 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efbe19c8-0727-3ce1-92d1-74bbc361a71c | -17.66535 | -53.08644 | 2024-10-07 04:02:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3254a18-cdc6-37c3-b91f-3edde661b555 | -17.66447 | -53.0905 | 2024-10-07 04:02:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 59344d54-41f8-320c-b173-3f4632adb240 | -17.66391 | -53.05236 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b6e8234-9579-316f-ab30-37794bf8bbdb | -17.66359 | -53.09458 | 2024-10-07 04:02:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 48894e53-4b94-35a3-9f30-40b8e1ac9b3d | -17.66274 | -53.08614 | 2024-10-07 04:02:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed757756-6327-3c2b-80eb-e33e48dbbf38 | -17.66271 | -53.09866 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30d32f89-c28a-37fc-a180-61dff1d7c33d | -17.66189 | -53.09022 | 2024-10-07 04:02:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7091199-0459-3208-9408-4026d728eeef | -17.66112 | -53.05152 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65bdde7a-9a09-3b62-8938-3fda400c3edb | -17.66104 | -53.09429 | 2024-10-07 04:02:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4141b15c-7721-3028-bb1d-8eb8fb505209 | -17.66029 | -53.05537 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0179396-632b-3dab-a71f-035c0b926d88 | -17.6602 | -53.09833 | 2024-10-07 04:02:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f2663ee-8605-3897-a084-c40db3418e8e | -17.65976 | -53.08504 | 2024-10-07 04:02:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1717884e-48fe-3abd-bdc2-a295538d97aa | -17.65831 | -53.05107 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c8b769ef-db63-3776-97aa-753653bff50c | -17.6575 | -53.05492 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ebc0766-2a3e-3449-a386-91662eee3f17 | -17.65552 | -53.05022 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e8c979c-aada-3e29-bee6-a22ac6c4a16d | -17.65469 | -53.05405 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56aa9731-ad98-31d7-a3e1-3ec671cc88d8 | -17.65191 | -53.05355 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 134a2954-c18a-3eb5-9a41-e67f4315dbd3 | -17.65109 | -53.05744 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45ced62f-8af7-38d6-92d9-73d50877a365 | -17.64743 | -53.06038 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b70e7352-195d-3539-b875-5d64206159d3 | -17.64469 | -53.0599 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4b418b6-868f-3873-81c3-f8aaaf8030b8 | -17.64182 | -53.0591 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52415c48-b1bd-3b0e-9213-8e0ecad7d3eb | -17.63907 | -53.05867 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c79e47e4-3a58-3e1e-b93f-37c4510facaa | -17.63146 | -53.09479 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07a8e588-92f4-368e-8754-5c4b21d43f9d | -17.63124 | -53.1076 | 2024-10-07 04:02:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb399236-c977-3dd2-9d08-d55a7a0a1048 | -17.63057 | -53.09899 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc435b2d-ba45-3105-9dcf-cea464e09365 | -17.62882 | -53.1073 | 2024-10-07 04:02:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b81ecc93-f2c7-39a7-b7d8-937a47849277 | -17.62798 | -53.11131 | 2024-10-07 04:02:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 651a6ad2-73f7-38bc-ae8b-9592a6d7acf2 | -17.62714 | -53.11526 | 2024-10-07 04:02:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c2509e0-261f-3c40-88c4-22c88f8769e9 | -17.6232 | -53.10595 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f14d7e16-7323-3454-934b-06e2bacd70e4 | -17.62237 | -53.10988 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20ef7501-63f2-3d33-a967-3f5663cc9333 | -17.7714 | -53.09843 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d8528d2-5c8a-3c89-9d17-027632848f0b | -17.77055 | -53.10237 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29c68b09-5e6e-3290-be8b-24dbccf16c12 | -17.76969 | -53.10633 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d580758-775d-3e52-a245-4ec23f11b4fe | -17.76784 | -53.10312 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40569108-c825-3ac0-8e09-3b02f214aad3 | -17.76701 | -53.10708 | 2024-10-07 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbe985bb-fe83-341b-be20-6351f384e31f | -17.84114 | -53.7841 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b1b00786-961a-3dc9-955d-3d1a213c2181 | -17.83978 | -53.7813 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 77454007-5eff-3770-84b3-fb4a9b80d532 | -17.83897 | -53.78497 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e541c370-106d-31a9-974c-283ca599a5ad | -17.83557 | -53.78145 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 688c1568-0465-3fed-b033-1041db14449a | -17.83474 | -53.78533 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bd8e2bc3-2766-3bae-9cef-625520d9cda3 | -17.83419 | -53.7788 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bbc61a13-574c-3159-b052-a384a1a59ce7 | -17.83336 | -53.78255 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6e4c3c6e-004a-3b3e-9945-411127ba9c89 | -17.83068 | -53.77565 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b071b36-379a-36e8-b807-51add480980f | -17.82997 | -53.77892 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7774562-deaf-336c-ab54-870b9c835041 | -17.8292 | -53.77364 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2ac5ae0-6328-3f2a-b85c-e1a6ef1030a6 | -17.82852 | -53.7767 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29f87b5d-38da-393d-99e0-620c83a28bcb | -17.8256 | -53.77076 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bac93627-7de5-3ec1-8375-b4975a3edac1 | -17.82488 | -53.77409 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d2d555a-b59a-38b0-aba3-c9c974574bfe | -17.82424 | -53.76828 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 82c813c9-ad08-3ac4-b427-1afef5154374 | -17.82344 | -53.77193 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5595191-4eac-348c-a9f8-dafc51e12ddc | -17.8085 | -53.76474 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d0696313-91fc-3f01-a8f8-1aacff754bac | -17.8077 | -53.76843 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README60.md)
