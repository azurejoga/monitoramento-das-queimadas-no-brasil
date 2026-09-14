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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec4633eb-9f9f-3a3a-850d-ee4f4ecd87a0 | -2.89215 | -50.37889 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9393ed17-7fe7-3ee1-8c67-9ccc40dae036 | -6.13345 | -59.88495 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b39729f-f7a2-3a54-991a-1e20a9d7b87a | -3.53991 | -53.98299 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 34044f8e-6bf4-3ee8-a1c3-c159b0625bd6 | -2.91298 | -50.42448 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 1da18ebd-3a06-363e-9837-c921bf31ef19 | -3.33892 | -54.19078 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e1a5bfd-8ece-380b-9958-bd5c0e302a77 | -2.9096 | -50.44786 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c3a55bd9-f6fd-3f29-983c-bab28d8d83c4 | -2.89972 | -50.37386 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21ed1689-7d03-3284-941b-14956abdad63 | -2.91626 | -50.44903 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6189f512-4450-3669-937d-87f031fcb5dd | -6.58685 | -58.86794 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f803a334-9e33-36da-8e96-e748ff8a3c7d | -6.10983 | -55.66486 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8a5db6d-89a8-3bbc-920f-514ac35fa87a | -6.64868 | -59.96056 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83cfdb88-0bf1-3277-8336-138543bead97 | -5.96504 | -57.77376 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14b11b38-fc30-38bb-b7b8-157c6b181e89 | -3.22826 | -50.58785 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a16637d1-2e34-30b3-910c-c2f5b2b5e175 | -2.9962 | -60.80773 | 2026-09-14 05:36:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32473ba1-ca69-35a0-af36-a5b941322c46 | -2.66796 | -57.53932 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3299d2cb-3c63-3cf7-a5ff-998f256df02e | -4.38924 | -55.20128 | 2026-09-14 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 32d038ba-e0c5-3d53-8244-ba522a872637 | -6.10944 | -55.66768 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4eb6f26-bfaf-3b68-b9ef-55a5bfd1bcf8 | -6.32281 | -59.98611 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0c8f597f-d5e0-3add-8af1-9bb4bed32df9 | -2.9373 | -50.39834 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 63d1e416-f5a2-3006-8973-0a1080180526 | -3.74274 | -61.74483 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34ec1ab2-b739-3e34-b4dc-4fa4c773377c | -6.08789 | -57.90453 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e5f94e0-e7de-339d-9821-23bbae06b131 | -6.32786 | -60.01196 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3954a8be-d230-3ef9-bd60-6ac714df2feb | -3.53942 | -53.98639 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1121e821-d6a8-361c-b140-a6fe4904c0f4 | -2.70364 | -57.53994 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6aa494e0-33a7-3cb3-a469-6175ba1db49d | -5.12568 | -55.95849 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eff23287-200b-309c-8833-44acb91db2a8 | -3.54171 | -53.98813 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 330e0e3f-8322-3238-b00d-34831d676584 | -5.12491 | -55.96387 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b48ab46f-409b-3bb5-8d5e-f3fc8cb28fc5 | -6.37291 | -58.30305 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84eb8a5a-68fb-3e3b-9792-91118fc36cd0 | -6.87253 | -55.29753 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3b76477-282b-3ccd-9ac8-cada4dfc15bf | -3.04832 | -60.79225 | 2026-09-14 05:36:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ca23c83-8d0b-3d02-9d83-325f427afd91 | -2.88987 | -50.37326 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f238bcc3-ab29-3ffc-9dd8-028d5155a97f | -3.36533 | -61.2812 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9995e643-4246-3539-8aa4-20d3458d9dc9 | -3.16045 | -58.64451 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c5cb5b4b-2a17-3c76-9199-cd0e81658ecc | -2.6781 | -57.5563 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f5bc53f-9f8c-3321-81b6-b6db8d17ba09 | -2.90471 | -50.38685 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 587e86a6-17d4-3f4b-9c99-d50a5f7db628 | -6.31192 | -59.95652 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90301f4b-df6f-3863-84d0-31e12a03647b | -2.74269 | -57.61908 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c86ded2-9faa-3c74-92af-627f6e3ec75b | -3.37443 | -61.33547 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e247df10-18d5-300d-8445-6dd714366b05 | -6.1389 | -57.69858 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea21bc8d-5098-381e-a711-0c790334ad86 | -2.90556 | -50.38092 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4962aeba-0373-3e6a-a41a-bacae25727ca | -2.89214 | -50.40386 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11252c65-9ea6-3c76-80a0-19defb9733b7 | -3.36078 | -61.28804 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27cfba48-c9c2-3bde-baed-4151a9e7a8b2 | -2.89877 | -50.42823 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5afdcd41-ada5-3652-9d74-eb357bb5196d | -5.07905 | -56.2496 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d97aa86a-7857-3173-aa7f-5167bdf56c3e | -2.90545 | -50.42931 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 96a56a53-3898-335a-b169-d6eda82241e8 | -3.72095 | -58.87152 | 2026-09-14 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f3c5c5b6-cf76-3166-a997-ec652f991e78 | -6.02826 | -59.94128 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3070d523-40e9-3cb1-97d2-26759653f632 | -3.72812 | -61.74997 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8a73b9c0-bb8e-3f9c-8aeb-f2a19a28ec97 | -4.34275 | -54.78218 | 2026-09-14 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fc97571-1674-3f7a-a6f1-32102e287bc2 | -6.59642 | -58.86517 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a0ef78f-95a3-3340-b424-29a87ff56d38 | -6.32043 | -59.97651 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c0f832b8-23a1-3e2d-8bcc-6d9d1d439791 | -6.37763 | -58.29987 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67b28ae7-37ec-3ae1-a239-2dbb31959061 | -6.59544 | -58.8656 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f15cf6f-035d-33b1-9db2-f7e2c447fc44 | -6.38042 | -55.25838 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4369f486-bf13-31d6-9610-5c143a478448 | -3.60131 | -59.0754 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 001eb74f-1f10-3e49-b952-d65f8e412993 | -3.37785 | -61.31335 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 486b6622-00c6-3ff1-91fc-2fa275f7f086 | -6.32299 | -59.99274 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 114d063e-7924-30bf-b53a-783a52dec4fe | -3.73039 | -61.7577 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 254dbcd4-d0ce-3fbd-b5d2-31767f799200 | -8.12102 | -54.80111 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed79bd19-88a7-3640-8ed0-ace65a0e2ead | -6.28217 | -59.92409 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa9587c0-e102-342f-9d6f-7dca5da51662 | -3.36875 | -61.28172 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63a73ecc-0a01-303d-a749-bff0df61648a | -6.3659 | -57.86791 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2027739b-0130-3405-8c3a-8443f7ea01da | -6.07763 | -57.86322 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 10e6ad64-cf7d-33a6-aeca-0e6cdcb90287 | -4.38883 | -55.2041 | 2026-09-14 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae801939-704a-3c81-ac45-b07cb1042cc2 | -6.93142 | -62.93337 | 2026-09-14 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8917cd87-516c-32a3-b6d2-6752e16264c3 | -2.89844 | -50.45288 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fadb1148-418c-34be-85ff-d70c4f43851e | -3.38858 | -50.7609 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a798ee2f-cca2-3dc1-bb1f-e955cae53339 | -6.8552 | -55.56821 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77bd162c-cb4f-3537-b6b7-8245f75326c9 | -2.90818 | -50.3883 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a8ecc5b0-fe55-342a-a687-6d98feff4600 | -3.54477 | -53.98742 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccac03c3-fb66-3a7b-a46f-a814a143906f | -6.07725 | -59.92107 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b37583b-c380-3a18-8136-21a4e354d912 | -7.10085 | -55.63303 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e7cf044-d6ca-3921-bdf5-167893db0026 | -4.3432 | -54.77902 | 2026-09-14 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f651d72-b2f6-354f-9d6f-f8f44645b227 | -3.09254 | -61.18386 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22683a63-00b5-3bfd-87e1-e9983ee0b8ed | -6.32185 | -59.97407 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68ed8055-b2c4-3c66-a46f-d8bd36a681ff | -6.58491 | -58.85321 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcf29f6d-2533-3cc1-8946-ee3c74156391 | -2.90378 | -50.44088 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| c18b9d56-211c-30b7-a4c7-3ff756f680e4 | -5.13124 | -55.95398 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11faf601-3a50-3c3f-9caa-798b9b5159b4 | -3.59439 | -59.06955 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84f60b82-5a90-368e-9f73-9935a3eee911 | -3.39437 | -50.76749 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2416bc2-62ab-388a-b4c0-c2dd29061a2b | -2.89961 | -50.42239 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f2e5f261-0079-3bbd-875f-8b45861ffb32 | -2.67751 | -57.56006 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d17a70c-b4d6-32d3-bc0d-a77c9ef9b568 | -2.91723 | -50.39506 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b60c48dd-314f-3a22-a370-c5a0e3ce7349 | -4.5539 | -50.46122 | 2026-09-14 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e7a8ec44-1ef3-31b3-8721-8baf6ac4f265 | -2.88879 | -50.40245 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94ab879f-3b2a-3979-a42a-35f445488cc7 | -4.12733 | -60.68322 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b34fc22d-3b3d-33ef-990a-3ebffce54784 | -3.54039 | -53.9796 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38a1a623-5e54-341a-9569-502e12501753 | -6.66399 | -58.88255 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ad7eede-b0a1-32ee-8bb3-b907b11df4e9 | -5.28232 | -55.96098 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47c1eeaa-1fd0-3fd7-833e-d853f8da8584 | -6.28832 | -59.93443 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c8668b8e-41cf-3848-86c1-95a280d0120a | -2.88461 | -50.38375 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8297b516-58a3-335d-9a89-9d9c4302d33c | -6.37345 | -58.29922 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9248dc32-c28a-3a45-aafd-7452082dd8d7 | -6.62572 | -58.37419 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 278720d1-cd76-3eb1-aec7-46b972b703b6 | -2.89302 | -50.37281 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39179185-b970-385e-9a6f-d3e7dc08247e | -6.1152 | -57.6781 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2645992-3ced-35ec-88b0-900836c12a3a | -3.35243 | -59.38533 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68742f54-76c3-3ed0-9285-128dcb74057e | -2.67423 | -57.56632 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 795d4cd2-1776-3143-90c3-5cf89189f0e1 | -6.08876 | -57.90623 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4c5b024-7f54-3985-a899-7396c703e63d | -6.11343 | -57.67984 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d7898562-a869-36fd-8913-1a66728e08d3 | -2.91311 | -50.37608 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README54.md)
