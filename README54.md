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
| 1fda0bbf-5ab5-34ff-a47e-97d2936add54 | -10.53399 | -51.36552 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac8fb6f1-91a8-3de1-8c1e-d2fdd9e551e0 | -10.54762 | -51.32888 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee6d3bf9-89a7-3371-a1df-69d046438126 | -10.57833 | -51.35276 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 016c59a1-d70a-346e-9051-036f3c0fa776 | -9.71148 | -53.96607 | 2026-09-13 05:12:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fe1ecef-67ab-3c6a-b836-6f0b6aebda75 | -9.85384 | -60.31007 | 2026-09-13 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 543622fc-6520-38c1-acef-8817dda00775 | -10.94789 | -48.3545 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 733ed422-4774-3c6a-a437-63ac34d2ec3c | -13.39889 | -57.03081 | 2026-09-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0281f5e-3c13-3d23-a980-7d2c3f93fb38 | -13.33361 | -51.6195 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e90d3590-6bdf-31f1-9764-e86e6cd55276 | -10.57205 | -51.36703 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14464a58-80b2-3bd7-9cfb-8befd188efe6 | -9.71334 | -54.35905 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79803325-60bc-33fa-8f15-aa26abb8ac1e | -10.63 | -46.10197 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40d4b73c-90a6-38ee-a27c-5ce05921da09 | -13.30597 | -51.72747 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4d9b18f-43d2-3491-b10c-74e5ac7b6c99 | -13.45643 | -48.47953 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0400a27a-6a06-3b76-af13-db7e6fb8c83f | -10.54704 | -51.33299 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d93045d7-bafe-3eb2-8df4-0493cbb8d779 | -8.77349 | -61.40083 | 2026-09-13 05:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| eceda22e-c57f-3e50-ba74-9db0467c9cf5 | -13.33305 | -51.6236 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b32d1973-0cd3-3d6f-a596-fefb10d21056 | -10.69124 | -54.15486 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14c6e610-4beb-35a5-aa62-1b4d3a1f33bd | -9.22333 | -59.41124 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a79210f1-f36f-3c1f-9198-26de08afb364 | -9.33568 | -60.28646 | 2026-09-13 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d7af79b-6c7e-3343-96e4-4b8e891e131c | -9.59535 | -55.14937 | 2026-09-13 05:12:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 944fea5a-ca36-316d-9d03-699c6151e286 | -10.62834 | -53.89861 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97380ab9-497b-3745-9dcd-10205307978a | -13.62758 | -47.88114 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7190302c-8471-31e3-9136-1b3aeece83c8 | -10.9346 | -57.11249 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d5342bb-cc62-3812-86a2-0837c672d35f | -10.58254 | -51.35315 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0420f972-b34c-3338-bd1f-5ebdf520d65a | -9.88288 | -47.59181 | 2026-09-13 05:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a05653d0-de7e-337b-af4f-028d8dcfc853 | -9.89444 | -47.58655 | 2026-09-13 05:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e76975df-3821-3f8c-a895-087b9b6764e8 | -13.62736 | -47.88103 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7afa339c-be22-3a7c-a31e-3d1766d43f0c | -13.30653 | -51.72337 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4a26cc2-00f3-35f0-908e-a1ff83ee8ea0 | -10.68769 | -54.15432 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 072197bb-b856-37e3-a24a-23347b372a1b | -10.75766 | -46.25048 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38aca4c8-e284-3ecf-ba68-8973791bf4b7 | -13.45732 | -48.47953 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8941f313-b4c5-33e6-92f3-97bbe8bdd08b | -10.56322 | -51.36934 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2b9508e-ef78-348d-9ce6-eb7bf07baf9a | -10.50501 | -53.57189 | 2026-09-13 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5887b0c-f010-3c20-9f0e-d15e3c34dc2e | -13.61571 | -47.88481 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b35873a5-cc61-3971-9fdb-284f20478212 | -8.86562 | -62.53105 | 2026-09-13 05:12:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf8ad8a8-7e5e-3dd5-bd9b-d541904a8aef | -8.76863 | -61.40534 | 2026-09-13 05:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3fb56ef2-1a3e-387d-a5e4-231bd40c3d58 | -13.34113 | -51.78533 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c1b688f-3e1a-345d-9e4c-e23c5190de04 | -12.16213 | -48.96917 | 2026-09-13 05:12:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7eaee598-b1f8-3ee7-96c0-87a25197f727 | -10.53971 | -51.3854 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d796703-51a9-3d55-b20b-808e3cee1c6a | -9.57334 | -55.15719 | 2026-09-13 05:12:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 993860c9-e148-3cfa-b642-184b8da3cf5c | -11.57484 | -46.99433 | 2026-09-13 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a14aa3e8-adaa-3fbb-b249-52c0f09ed725 | -8.7704 | -61.39492 | 2026-09-13 05:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fdfd789d-443f-3bce-b96e-a2ffaf33aa2d | -13.4565 | -48.48604 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3dc804ef-ee5f-3444-bbcd-146dd7657d76 | -16.26657 | -50.23169 | 2026-09-13 05:14:00 | NOAA-20 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 236a5e8b-86c3-35f3-99de-1d292187c72c | -16.43391 | -51.78122 | 2026-09-13 05:14:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55f53635-cc24-3233-b7da-cfa7c1ab180f | -16.03613 | -52.66227 | 2026-09-13 05:14:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26e9b1b6-d54e-3ffc-8f06-f5ce4bf74dd2 | -15.54932 | -53.80907 | 2026-09-13 05:14:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 231ff7b1-ab5c-3704-bf45-471973cacc36 | -15.56133 | -53.83558 | 2026-09-13 05:14:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4295b11e-04ff-3d40-91e2-e96b5efe4b7a | -15.55198 | -53.78942 | 2026-09-13 05:14:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b67ffa5-d799-32a8-abe6-604fa5ca8917 | -15.56864 | -53.78193 | 2026-09-13 05:14:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52048312-492d-377d-be6c-ef3e64df8201 | -15.40924 | -55.77732 | 2026-09-13 05:14:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3d9ebc19-44cd-3956-855a-71455535bdf3 | -15.5718 | -53.78741 | 2026-09-13 05:14:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7c182c5-72f0-32ed-97a3-41ff76e25524 | -18.60324 | -48.66499 | 2026-09-13 05:14:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c32f3d13-f509-3d93-b9ab-63a0f6a352af | -16.03564 | -52.66602 | 2026-09-13 05:14:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10a354b1-2a67-375a-8187-097544d90755 | -16.26169 | -50.23106 | 2026-09-13 05:14:00 | NOAA-20 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29b14c6c-5383-3aec-864e-1da4c424b630 | -18.60368 | -48.66088 | 2026-09-13 05:14:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8d77d2d5-e10e-362d-a475-f84bdd108c0b | -15.56797 | -53.78682 | 2026-09-13 05:14:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d56593da-6c08-3837-ab29-a6dc6270af28 | -15.54232 | -53.80305 | 2026-09-13 05:14:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 138fd24c-0bf7-3e12-bf14-9d66ba9206ac | -15.55064 | -53.79929 | 2026-09-13 05:14:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f26c09ce-fc02-3e6d-ac9d-940a6b037070 | -15.55392 | -53.78763 | 2026-09-13 05:14:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdf308a2-2e54-3e38-b401-024cba6430f3 | -10.6827 | -54.1679 | 2026-09-13 05:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 79212808-0e75-357a-9417-f6562af3293b | -2.67642 | -57.54361 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a0b15b78-89ed-32e7-9961-9d88a6729cf2 | -2.67931 | -57.52347 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 465eb2f5-f2d6-3713-8e0b-40f7a496c442 | -3.74241 | -61.74855 | 2026-09-13 05:53:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 507d6548-449e-3a78-a156-a871c4e567af | -5.12399 | -55.96521 | 2026-09-13 05:53:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9dac9220-d61a-3235-aeb6-e582bd60143c | -2.67844 | -57.52351 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ae82ed4b-cea2-3b29-8970-7289cd55f0ad | -5.13133 | -55.96069 | 2026-09-13 05:53:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1957d111-b80e-314d-83ee-0cafbcb5295f | -3.73236 | -61.75578 | 2026-09-13 05:53:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ece9cacd-a8f0-32f3-87da-202a096bafa4 | -3.16637 | -58.64839 | 2026-09-13 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 011fd171-2288-3717-a1c3-3ba58b44f4a0 | -2.54118 | -54.65921 | 2026-09-13 05:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa44cc49-205e-3d99-9d95-23a2b9ccca2e | -3.72861 | -61.75082 | 2026-09-13 05:53:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac700b02-a833-3ab5-a781-3dbb0707f21b | -3.59917 | -59.07354 | 2026-09-13 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9be6cb97-9ad1-3d83-8cad-ad47d0093dc8 | -2.6816 | -57.54852 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 6401b769-c3b1-3e42-be24-5493ced153d1 | -2.68217 | -57.5445 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| a7de01c7-bb11-3fe4-9806-e9a9f7b02366 | -2.68333 | -57.53646 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c890a2e6-ce10-33b8-9f9d-b84287f72cfc | -3.64192 | -58.63035 | 2026-09-13 05:53:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98b3c34c-647c-3bbc-b224-f786e7fe469b | -2.67602 | -57.53958 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24689694-0e4b-356a-ad22-0ae4fcc90d84 | -1.7384 | -55.84742 | 2026-09-13 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cdb08ca-0ee9-309a-89ce-40c3db4082fe | -2.67269 | -57.52261 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| acb5e2ea-497a-3680-9b10-4428b534095a | -5.13 | -55.96225 | 2026-09-13 05:53:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b57c6a62-c008-3aa9-9aa1-38b8df69bda4 | -3.40808 | -59.24648 | 2026-09-13 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d2b8246e-865e-3735-97a5-7e871652d8c8 | -2.68692 | -57.54535 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 1fcae25a-a4a3-3c4c-a878-15066f30d269 | -2.67125 | -57.5387 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c8cd575-e031-3b88-baed-364c1011195c | -2.74448 | -57.6398 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c7209fa-d7f0-36c7-823f-a865cf0f696e | -2.68116 | -57.54447 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c74933a5-ef2d-3e92-8bb5-88225ab6aaa3 | -2.68275 | -57.54049 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 866b1569-2110-3a97-929b-4b305af7e875 | -3.7871 | -59.36526 | 2026-09-13 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2e5d7d8-b119-3632-aebf-6b52bf0892d0 | -2.67662 | -57.53557 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1dfe94bb-8e63-36c6-a5b9-509690c841f1 | -2.67815 | -57.53154 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9d20cb05-a3b5-3683-94f2-2b47af403e5f | -3.40632 | -59.2483 | 2026-09-13 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| af9196eb-9e0a-39d3-ac68-2a187b3a56b9 | -3.64243 | -58.62684 | 2026-09-13 05:53:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 120c539f-1a80-3d08-912b-4933b4f6ab94 | -2.66693 | -57.52173 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a5f9dc1-8fd6-3e07-94a7-14da7379fdb5 | -3.59965 | -59.0703 | 2026-09-13 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f8d67e0-e0ef-3987-8065-eb47cd67d778 | -3.16147 | -58.64417 | 2026-09-13 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b333ac70-a067-30c6-b2c5-07c647949d00 | -3.60444 | -59.07432 | 2026-09-13 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96206fe5-c635-3309-bb84-c0e492d3fee4 | -2.67571 | -57.50249 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 383148ca-d397-3935-a072-aa223d34d609 | -3.06489 | -59.26848 | 2026-09-13 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4f5958a-2c5d-32c4-874c-d839db363cb1 | -3.74177 | -61.75282 | 2026-09-13 05:53:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 024d8820-78d5-3671-b63e-73f667fcfefa | -2.67182 | -57.53467 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e46a4493-a185-3a0f-8bf7-874b8c67405e | -1.73208 | -55.84643 | 2026-09-13 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README55.md)
