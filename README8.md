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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71d2e7b9-f0e1-334b-81b7-dbdaf4cb39fd | -8.50775 | -48.06036 | 2026-07-10 04:34:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b5a4a1c6-a2fa-3229-92ab-19d762ab6c7a | -9.35659 | -48.22329 | 2026-07-10 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e642f2ee-2c99-3c32-b65f-c00050f324b9 | -8.82934 | -48.33164 | 2026-07-10 04:34:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbecdc7a-1b76-3173-9784-7b34c3d8773b | -13.75865 | -46.26707 | 2026-07-10 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2568b66-a478-336c-8d84-ff67f69b76bd | -13.36758 | -54.36833 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 059ae5ef-ccd9-34f3-8f5a-40b42a301111 | -8.11518 | -47.10046 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07750393-0ece-32b2-a1bd-86eece998fdf | -12.49577 | -43.77117 | 2026-07-10 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88469542-b92d-3f32-b4e5-344afe2923ed | -8.11131 | -47.10347 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b65e77dc-25e8-3107-913f-633f8ddbdca1 | -12.84932 | -44.3509 | 2026-07-10 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9be5a838-591a-37d6-960e-c614fe3e5687 | -13.36423 | -54.36408 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fa22f2e-e20d-32f3-8cd4-d9094dd5c0e7 | -14.12524 | -46.31253 | 2026-07-10 04:34:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3435cf80-239b-34df-9992-327f9e5071f4 | -8.0433 | -46.92595 | 2026-07-10 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a25f0e1a-2cd2-3de3-b0d8-fe55f344aed6 | -9.01662 | -44.85329 | 2026-07-10 04:34:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba59e55d-cfe9-3090-a5c7-a5376247156c | -12.44481 | -49.44727 | 2026-07-10 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e26bd319-093f-3338-860e-b01554017712 | -11.47619 | -52.92304 | 2026-07-10 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e6cf092-4789-376b-992b-55616fa93028 | -12.28806 | -51.59805 | 2026-07-10 04:34:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d21d8215-83cb-3b3d-9b46-00601c1f00d1 | -8.83264 | -48.33216 | 2026-07-10 04:34:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7927a61d-1d63-342c-8643-639865708dc1 | -12.50089 | -43.76424 | 2026-07-10 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 420182b4-da7d-30a5-ab50-d4c8145c29a4 | -10.26682 | -46.38698 | 2026-07-10 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd30393d-e761-37c2-b086-9489eccbb3d8 | -8.03511 | -47.42289 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3310b8c0-2633-325d-8f14-940aada69142 | -13.31178 | -54.34584 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5651cc82-139a-330e-bcef-98399137cfd5 | -8.72211 | -47.84147 | 2026-07-10 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd658f4c-db8b-3844-bcf8-b83ca753e0a5 | -11.8815 | -47.67776 | 2026-07-10 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b18a364f-7d59-36ab-9f19-d00c9d96964e | -8.11185 | -47.09994 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2e0edca-11e3-357b-9226-621fd0a3dc58 | -10.85118 | -45.04234 | 2026-07-10 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 245ff23c-84d0-3d74-b130-5dfec423aa73 | -12.45685 | -49.58634 | 2026-07-10 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4672929-1225-3431-841b-0aa7d9d98a06 | -11.84307 | -48.24039 | 2026-07-10 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ad05d9a-b360-3f40-af09-a5fe7c92447f | -13.35964 | -54.36689 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb9ac9a4-4291-3152-ae38-a27dc1e4d21e | -8.1115 | -47.58908 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2538dd01-5711-38e4-8af2-946d956278ff | -9.55736 | -48.6791 | 2026-07-10 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54b2bf61-fea7-360a-9513-657515f1036f | -6.55504 | -55.15623 | 2026-07-10 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9db99c67-b12e-38fc-b325-2c12863b96fe | -13.27293 | -45.14651 | 2026-07-10 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c21bd767-e3fe-3cc9-885b-6b9536ac8530 | -17.53812 | -54.00313 | 2026-07-10 04:36:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d877e458-fae0-3c1f-8989-4282da5d7cd3 | -18.52586 | -47.23588 | 2026-07-10 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a5aa4eb-c63f-3c26-9dcf-6ee2f35f98b4 | -19.60131 | -47.60587 | 2026-07-10 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a60c017-0499-3d37-8c13-b0a53c1825fd | -17.54096 | -54.00841 | 2026-07-10 04:36:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0026290-b467-3252-a4ce-122709c097c1 | -14.73126 | -48.19611 | 2026-07-10 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 929a1b6f-1fe4-305d-a652-e5d04c59358a | -12.85565 | -58.31153 | 2026-07-10 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6ae4345-08f2-39c7-a9d6-1725d9ed96c1 | -14.73462 | -48.19671 | 2026-07-10 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b563c5aa-584d-3be7-8d0c-46792b923052 | -18.10296 | -54.00242 | 2026-07-10 04:36:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c564499d-cc95-36ad-91bd-586a9e98882e | -16.5296 | -47.73692 | 2026-07-10 04:36:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30cb5e38-02c2-3df1-838e-97b968247801 | -18.024 | -41.8318 | 2026-07-10 04:36:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ea3a2590-1901-37dc-8396-ac3bac5eec82 | -18.02898 | -54.35725 | 2026-07-10 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5b1c9f53-4a16-31a7-a7f7-388582505655 | -18.17875 | -42.69752 | 2026-07-10 04:36:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4caec7d7-50b1-3c56-aced-312afec8a601 | -20.45879 | -47.6138 | 2026-07-10 04:36:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a62436fa-9f4a-3cf3-a569-c8fd142be70b | -17.53892 | -53.99857 | 2026-07-10 04:36:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d2a2610-4c20-36c0-9994-7708320aa197 | -19.66551 | -47.60496 | 2026-07-10 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2d677e45-3929-3504-bba0-c0392a3a4ee1 | -17.99805 | -51.14777 | 2026-07-10 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5f0e261-3fe9-3cf6-9a0a-249542c75b07 | -19.95009 | -44.08961 | 2026-07-10 04:36:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aa0067b7-a464-3b25-933f-52aa90f7b870 | -18.02816 | -54.36187 | 2026-07-10 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8f5b02ed-60b8-3743-a39a-9563c7e2b781 | -17.53447 | -54.00242 | 2026-07-10 04:36:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2bdcc6c0-3894-3143-9217-9365e834f77a | -16.52902 | -47.74089 | 2026-07-10 04:36:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b877671-d5c3-3cec-a581-1c7547ccf82c | -18.50053 | -47.60127 | 2026-07-10 04:36:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa20ece1-fab6-33bb-b617-3decd1d71a03 | -12.85047 | -58.31049 | 2026-07-10 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9917824-4135-3a42-a3fc-a065396bcb1e | -16.83179 | -46.31644 | 2026-07-10 04:36:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b084deaf-78ba-306d-8642-07c327f67d64 | -19.6649 | -47.60936 | 2026-07-10 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a3d74377-b269-31f1-aca7-0498d08f2af5 | -20.66812 | -48.67842 | 2026-07-10 04:36:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4209743-a817-3f94-81e6-c038302bdb28 | -18.02159 | -54.35584 | 2026-07-10 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1088dfb2-1361-3cfe-b514-868a16cf225b | -17.54177 | -54.00383 | 2026-07-10 04:36:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9a0a5f6-0acd-3784-b231-323d1d6eeb2c | -16.79783 | -49.42192 | 2026-07-10 04:36:00 | NOAA-21 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88e38d8f-2791-350f-a266-dc1a76e98234 | -14.73406 | -48.2004 | 2026-07-10 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bad171db-ee9c-3a87-b656-2829bb483d1e | -18.02734 | -54.36651 | 2026-07-10 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e113672d-6651-30bb-82fb-e175e2df8353 | -19.6625 | -47.60006 | 2026-07-10 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b9375c0-3575-30f5-b63e-384fec5cf3d0 | -19.59771 | -47.60536 | 2026-07-10 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17fd4214-09dd-3fb7-8777-95e37b83439b | -13.95368 | -53.90786 | 2026-07-10 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17bd7e5e-6e8f-3fbb-ad5b-a4b07b8ade0a | -13.95191 | -53.96277 | 2026-07-10 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a09a2744-4f75-38b8-9067-b4255c582176 | -18.10218 | -54.00687 | 2026-07-10 04:36:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9726474a-48b6-3c3f-aae8-92e11f1b7229 | -19.5929 | -47.61345 | 2026-07-10 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6fb26abc-73e7-3fe3-894f-ae2dbd43ee07 | -18.03104 | -54.36722 | 2026-07-10 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 232ed120-cd16-3666-ab21-42ea7d76c6c7 | -19.60315 | -47.6041 | 2026-07-10 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f21d83c-14b0-32b5-a586-18fe17ff7b67 | -13.94893 | -53.95721 | 2026-07-10 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87871381-ecdb-3901-92f1-042bd030cb80 | -15.54353 | -47.38584 | 2026-07-10 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e804e2d9-9fb8-331d-a6b7-dba23baada09 | -13.60465 | -56.59791 | 2026-07-10 04:36:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69af3afe-d314-3cb0-9fbc-0cc46727475d | -18.17834 | -42.69714 | 2026-07-10 04:36:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 5f170bcf-070e-39f2-83e8-12f0514923cb | -14.73182 | -48.19235 | 2026-07-10 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8673827a-1c33-31b6-9eac-19e6c36008b6 | -13.95276 | -53.95793 | 2026-07-10 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dce1f2c9-f2ed-3e1a-af23-4f74164494fa | -19.85286 | -49.07433 | 2026-07-10 04:36:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13d07487-a5ce-3298-97b7-7b380f11d635 | -20.96745 | -43.81445 | 2026-07-10 04:36:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 61be0a47-b6d2-3c30-be0c-9e9023a19f89 | -19.5965 | -47.614 | 2026-07-10 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fdf01b74-f5a9-320a-a744-04f91917bc4d | -17.40134 | -47.32687 | 2026-07-10 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d9ad979-37ed-39f2-86b6-4227234bbd03 | -15.66851 | -56.0704 | 2026-07-10 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3d45fc07-b1fa-3351-a896-7efb8e0aed90 | -19.66611 | -47.60061 | 2026-07-10 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 001a581e-383b-3750-9c9b-4918dee0d074 | -17.53527 | -53.99785 | 2026-07-10 04:36:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b2fe599-d2ea-3505-b9ea-a0c816a12e6c | -14.72902 | -48.18803 | 2026-07-10 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| afb12337-367d-3176-8ab7-e0ecea444d16 | -21.74262 | -47.71796 | 2026-07-10 04:38:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46f3dc72-60f4-3252-b020-778b0dd6c113 | -20.15189 | -54.40252 | 2026-07-10 04:38:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8cb324f-4585-3a9a-a86f-9d682c1b974c | -21.76559 | -56.30151 | 2026-07-10 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ff459808-6fc7-3f80-afa0-a9bda39b6082 | -21.76947 | -56.30234 | 2026-07-10 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee72ea8b-d895-3d0d-8be8-dbc2058633f6 | -21.12463 | -54.37358 | 2026-07-10 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 798e36ee-525d-3f1f-a3c2-607562e7568e | -20.1555 | -54.40319 | 2026-07-10 04:38:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b17728c-a88d-3999-8ad2-5443670d6e14 | -21.77045 | -56.29706 | 2026-07-10 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a5fe9c0-b168-30e1-a863-6f40d8190991 | -20.18284 | -55.39562 | 2026-07-10 04:38:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e834e91f-48b9-3193-bd6d-be0724b76b72 | -21.76269 | -56.29537 | 2026-07-10 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e26cb955-b69e-3220-9fce-c4533d087217 | -21.08668 | -55.76816 | 2026-07-10 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d49987a4-9eb4-3442-9031-9db9213caf00 | -21.44484 | -54.56375 | 2026-07-10 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35957b08-1190-30f6-aed9-ff6d0dfc886e | -21.45443 | -48.68159 | 2026-07-10 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9520ed49-d9c1-32b1-864a-f5e57bc06cdd | -22.2343 | -56.69832 | 2026-07-10 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51a8c02f-d455-3c05-b435-447908f2820d | -23.74659 | -54.55267 | 2026-07-10 04:38:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d36d6ed9-8e28-3521-a484-12b668a8e644 | -21.76657 | -56.29621 | 2026-07-10 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1b7c4c6c-9615-32b2-9656-83c25f7a2ace | -22.79407 | -49.34988 | 2026-07-10 04:38:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
