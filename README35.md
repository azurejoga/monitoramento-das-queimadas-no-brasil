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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87a58836-f484-3f7d-901a-05848e618c62 | -6.70626 | -56.88277 | 2026-09-10 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3dcfb85-2b63-3a43-b841-c51336519486 | -6.46017 | -60.02937 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d314b216-91ed-355f-a013-b653ed9e3f3b | -8.09142 | -54.84591 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f3c26e86-6aff-3cd3-9465-cf2ddeb79e93 | -6.68032 | -59.92425 | 2026-09-10 05:12:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f2838bd-7a01-3367-9070-837133feb733 | -6.7867 | -58.88639 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faa7879c-ade8-33e8-a73c-0fe1beec99cd | -6.77549 | -58.89195 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dce0e57-00fd-30eb-ab19-281f40f0fc65 | -6.46781 | -62.86242 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39a4ce1b-7416-39b5-b40c-6e2aec57637a | -6.13901 | -57.68727 | 2026-09-10 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72b2397a-e93a-382e-a415-b20bee2ca99e | -8.94724 | -44.40557 | 2026-09-10 05:12:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0782848-bd6e-39e4-b083-2e194bb7eecf | -6.76839 | -58.61821 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f9e6b3d-e347-3777-8a17-33236af93f45 | -6.95386 | -59.74849 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e22a28e8-a816-3a5b-aaf1-aed93da2922d | -6.39593 | -55.24499 | 2026-09-10 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94ec6d6b-a5a4-3479-b108-5c323fe3f533 | -6.76562 | -58.61414 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f972184f-ef33-3f12-ba3d-33a7bf4f4b78 | -6.77663 | -58.88482 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c48d159-f20c-30d6-94b9-7a836d526e66 | -6.95178 | -59.78299 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b2fc125-72f5-3342-a858-fedcb44d9848 | -6.78727 | -58.88283 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5addb9de-dd81-384c-b2af-d37448da0ca3 | -6.77828 | -58.89605 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cae3b527-cd18-3275-94e0-bd35f44f4b84 | -6.78106 | -58.90015 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 260b9c14-92cb-35a0-9350-6b494db96683 | -6.87616 | -56.50943 | 2026-09-10 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b9314c9-1d44-3d9c-b656-666865dffada | -7.24705 | -59.52042 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa806574-2156-3d64-ba42-c95f523beb25 | -6.76407 | -58.96342 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbf3bef9-50af-3e3b-85ef-04e3fda69f4e | -6.78835 | -58.89763 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e58d8dae-9904-3805-949f-4f62f639200b | -6.76954 | -59.42965 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38b10f3d-d93a-3195-9e9a-bf49092c8bba | -5.88619 | -57.76022 | 2026-09-10 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd167c30-56a4-301f-a58f-fa368d8035a4 | -6.55568 | -62.88547 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 031db0dc-fbc2-3c24-8697-9756051f310b | -6.78948 | -58.89049 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca9ba778-8e97-315c-9bac-7e4fb2b4d82e | -6.86634 | -56.5732 | 2026-09-10 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db8f4984-cfb5-3c03-a4fb-c751e71bef10 | -6.45606 | -60.0327 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6530fc2-b2bd-3c4d-94c4-bedf4eb0305a | -7.12416 | -56.51167 | 2026-09-10 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 544c9b9a-2cce-3bc6-acb1-3cbf6b43310a | -6.06086 | -57.79456 | 2026-09-10 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81bd3743-e0c5-3d83-ad10-3af781056862 | -6.76129 | -58.95931 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29e2733a-f3ac-31b6-98b1-2bd1027556b8 | -6.75831 | -59.7416 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea4d7142-0667-33eb-b224-d4b33ab846ee | -6.50234 | -58.38504 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94103b7b-e2b5-38fc-a790-0d60eb0ecb45 | -6.50344 | -58.37805 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0ac74db-7b9f-30aa-9c41-bf8cd56e5484 | -6.54489 | -62.90532 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e09a6573-297b-3ec3-9f58-7562b7f61b51 | -6.8795 | -56.50995 | 2026-09-10 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91fa4142-d237-3f88-afc4-e092efab2714 | -6.81463 | -60.13169 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 023fca66-d744-3ae5-b480-111aae160fd8 | -6.8245 | -58.99508 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4abccc1-09b0-3748-be26-69599a980719 | -6.81176 | -60.12724 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 271951dc-5050-3bae-aba1-05c7e11d172a | -6.90067 | -52.19342 | 2026-09-10 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80596444-8812-35fb-a30e-5a5715da2cec | -7.75329 | -49.19891 | 2026-09-10 05:12:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2a9cfad2-954d-3e19-ab13-55fb34ace501 | -6.76895 | -58.61467 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 981e01b2-9cc3-3917-a36c-61fd4d0d6dcf | -7.97789 | -43.99413 | 2026-09-10 05:12:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1b13860f-2e43-3a43-8eeb-dbcecbb78bb3 | -8.97697 | -44.97561 | 2026-09-10 05:12:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 739a0bb7-0df2-39df-a21d-0c3345f671fe | -8.09021 | -54.85412 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e267712c-94bb-3b2e-806a-5dcacf1e2f9e | -6.55034 | -62.8921 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 118bf438-420c-3309-a158-2cb156cb3633 | -6.82114 | -58.99456 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e167594f-e622-33f2-bc43-d1d4a6af2ec1 | -6.51052 | -58.28959 | 2026-09-10 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae4fc56a-e791-3445-b997-13548ec65076 | -6.77606 | -58.88838 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9079cd9f-c067-32c4-b3e3-0039636c4890 | -6.50289 | -58.38155 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e27a2671-0e57-318d-9b1e-7c93a1a1e1fd | -6.09621 | -59.97269 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beea1986-5d9d-341f-9226-9a2bf2c61a6e | -6.55506 | -62.88912 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 25394581-414c-3de8-8880-802d4caa285b | -7.56095 | -61.37766 | 2026-09-10 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68318533-b3ce-3245-92b8-bfef6f9021dd | -6.5072 | -58.28907 | 2026-09-10 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19c9b673-5387-3cb7-ace2-1ab38fcbca5b | -6.77999 | -58.88534 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bb1a674-bfc5-38bb-aa75-92752d93f227 | -6.80051 | -58.95089 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1adbbc3d-64c9-3d9c-9f64-82d851b129be | -6.82507 | -58.99149 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1994d88e-81a2-3492-8a21-ebe49ecae3f3 | -6.6581 | -58.82241 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbe93485-f9cc-35a9-8626-bc2a36b6d2d5 | -6.43619 | -58.15664 | 2026-09-10 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d65e6a4-be4d-310c-a1b4-50490c9248a4 | -6.78334 | -58.88586 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 680fb79f-fc63-30d7-8737-45419a28ef1e | -7.98137 | -44.00026 | 2026-09-10 05:12:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 64667b99-dcb5-355f-a6cc-f0409d4646a7 | -6.78891 | -58.89406 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed4a8506-237e-318b-ba00-26b32af0d29b | -6.63482 | -59.43884 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b0398eb-e67f-3983-9172-7037e757dd66 | -6.78778 | -58.9012 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a52a046a-53cf-35cc-8b61-7dcd69abae70 | -8.09204 | -54.84171 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 93bb5b07-45d5-3fb3-8ec3-87c2c1f4e84f | -6.50677 | -58.37857 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60cab5f8-5ab7-3cf4-b9b4-48e726644de8 | -6.76896 | -59.43333 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 557de212-264c-3b01-be7a-d2c2fe0cf856 | -6.65419 | -58.82545 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28f8d340-f534-3963-a765-bcac39dbebe4 | -8.98376 | -44.97709 | 2026-09-10 05:12:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b197aab-2837-38ff-8933-0168d1adf8e9 | -8.08602 | -54.85764 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c29e832-d191-3a3f-8914-176c8e1bc784 | -6.56263 | -62.89412 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14d22615-37f1-36a2-ba06-8df46017a220 | -7.01959 | -59.77835 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 954f608d-305f-306b-85d7-2ac5094017f9 | -6.95546 | -59.76031 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4efaca25-4ef5-3783-ad7c-20900d1b1b4f | -6.75893 | -59.73781 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 197abddb-06ab-3d9a-93e7-2a9bad653a00 | -6.39017 | -55.21257 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaea0c0e-e8b2-3a09-8d4b-4076d4b1bd7c | -6.15829 | -59.94278 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 003b9090-e444-3433-9b73-92573f6dce9e | -6.50512 | -58.38907 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ccdc64e-403c-39f7-9e5e-79070f1634ab | -6.50899 | -58.38608 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be2d7db1-5d93-3ea0-bf2b-c8cb08b5df3c | -6.39997 | -55.24169 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b82555c-62a7-3230-93b0-1393ae926b2b | -9.3387 | -45.64405 | 2026-09-10 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e28f5648-3f96-306a-b7fe-8a8c6d9f247d | -6.79005 | -58.88692 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11a899fe-9099-397b-92ce-88cc2b7ea044 | -6.38785 | -55.20442 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f0b5e9d-cb11-3907-9a79-ae0d9906cdc9 | -6.79841 | -58.89923 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1fe877a5-383a-3a68-99f6-f4a51a086aaa | -8.94022 | -44.40421 | 2026-09-10 05:12:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06de7aac-3086-3de7-a0b5-7c3df90647b6 | -8.12003 | -55.06661 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d70f7654-26b5-310b-8e43-acf9a7bb3c51 | -6.80108 | -58.94731 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0c37b7bf-41ef-396a-a199-7092351e2182 | -6.78278 | -58.88943 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d361a40d-b3fa-320e-b6db-122aa88dd47a | -6.79421 | -58.79624 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e871f4d-36c6-3654-a452-e6a13287bfed | -6.80444 | -58.94785 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4e3fb458-7660-3b9c-8a40-e24f63acc417 | -6.78556 | -58.89352 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efe99648-d46f-37ab-88b9-0f22054269c1 | -6.76951 | -58.61114 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 353b8b7f-21de-3045-bfdf-bb8d3cb332e4 | -7.24084 | -59.51563 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d62f6db4-a678-30f8-bd73-e02da3dd24e6 | -7.24424 | -59.51619 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 942ab2df-610d-39ba-9af5-76942d2abe4b | -6.77885 | -58.89247 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d613b54c-c2ee-36e0-a64d-7e1173ed1c8b | -6.45544 | -60.03659 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa7cff63-91f1-3e8d-bae2-3ae421bd3d14 | -6.78613 | -58.88996 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69e01695-4c6b-3334-87f3-93783474f5c1 | -6.54374 | -62.90611 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 293adf5f-2646-3d8c-a2e5-f0008e0d6421 | -7.75595 | -49.20287 | 2026-09-10 05:12:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c9e0350-fa42-3f4f-aad7-972a8994bf33 | -6.76464 | -58.95985 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e2d6c426-b33e-3352-85f2-8bbe3b60e87c | -8.82486 | -46.92601 | 2026-09-10 05:12:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README36.md)
