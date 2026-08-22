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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 059cf1c6-d841-3114-9d50-843e27da6fb5 | -4.44817 | -55.3917 | 2026-08-22 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8df41307-a890-3c4c-bc9b-fb88281ff80a | -6.37679 | -54.9526 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5089214e-7412-3e79-8fe2-635e19d990dc | -7.59703 | -61.2303 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8aa2985-78ff-323a-a8fc-8ba63011aee8 | -6.69749 | -58.95607 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9652b848-69e1-3907-9d91-9a9ab658944d | -8.19088 | -54.9764 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3e7e79c-8e92-3fcc-b237-8d2e742b2afa | -6.6756 | -58.75018 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd0e28d8-5a35-39bb-ab82-9250bb77d30d | -6.93761 | -59.30655 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee1401e8-8863-3489-b79c-c4660045fad6 | -6.77604 | -58.69476 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa37eac6-e305-350a-bb9e-012f852b696e | -6.99847 | -59.05014 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 646a72c4-3105-392e-a772-c91bb9fa4ca9 | -13.40183 | -54.36374 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a35abe0-dbcd-345e-a014-db4edef40e42 | -6.22628 | -55.62011 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 5bd54ddb-6c5f-3767-90c4-36a3e9301873 | -6.10933 | -59.94339 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d5ab7d7-ae24-334b-9376-901d7e40f6b8 | -2.50249 | -48.13898 | 2026-08-22 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 020fc982-e47a-3087-8918-75a7e525bc24 | -13.98673 | -53.67134 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d14f290-d9a6-3ab8-bdd9-1637b378129b | -6.78767 | -59.43875 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6a9623c-1126-3613-b029-af799826e2c6 | -6.11269 | -59.92237 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f158462d-af0e-3cc3-aa6e-dfd77981532b | -6.7716 | -58.6798 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7357c4e6-0308-31fb-a0c3-bb2fc6d02657 | -8.53002 | -54.84913 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 19b552fe-c917-3f26-9223-a9799e34c686 | -1.98861 | -56.46365 | 2026-08-22 05:23:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25fbcf69-722e-3b04-bdb6-94f0db56b3c2 | -6.765 | -58.70015 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b38e998e-3089-3361-89b4-56d5bea9c35f | -6.2624 | -62.52453 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1acfda13-8b20-38c5-a484-9374f3c0b50a | -6.85381 | -59.40668 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32974a3b-5737-3d95-99a2-e4500758fb75 | -6.76384 | -58.66432 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 64e6a16c-aaeb-39e7-9288-c6b6a5844cf4 | -6.1756 | -55.44049 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1729a648-6bba-3525-b508-4aac6fdc7f73 | -8.57701 | -54.79509 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 083d9127-e4f1-36fe-b4f8-7a5a167b5ca3 | -6.93816 | -59.30309 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6010ac0-103b-3eca-9cb1-b4b1acd85b47 | -7.34802 | -55.66796 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80330a39-3967-34f1-bbad-cdeeda1992cd | -12.76453 | -48.4046 | 2026-08-22 05:23:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5fe7296e-7496-37b7-8d44-2616cbc74181 | -6.00551 | -57.80449 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7485b4c-b36b-3f5c-a1e3-3d93f61ff133 | -6.36187 | -62.89685 | 2026-08-22 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7543126f-64f5-3395-aaee-c2e01d906213 | -2.49679 | -48.13803 | 2026-08-22 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a85dcbe0-c9f9-3d10-b70f-79985f67171f | -14.12567 | -48.06745 | 2026-08-22 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31c85b04-4913-3c36-92a5-04bbbd28ff01 | -6.8937 | -56.437 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c551501a-4e35-3d83-b1ca-0dc7e73030a1 | -6.93582 | -60.08677 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4961c96c-4e04-3dc7-8720-10a3eeb5b0d0 | -8.54903 | -54.85752 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d88f167-4009-3c4e-af90-93c450d00264 | -7.39058 | -60.00531 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efe23251-3278-37d2-8938-f9d0044cbd05 | -6.90514 | -58.99632 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7c082b8-4edf-32b4-bd25-36ad3f26ba64 | -5.74669 | -53.57467 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f8771c3-357e-39e5-bc4b-c4ff21c4ba9f | -6.81192 | -59.41421 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d2d4f17-1964-3e14-bad9-4368c411745b | -14.42286 | -51.80104 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d39909ad-262a-3a29-a340-4579497232f8 | -12.82928 | -48.46523 | 2026-08-22 05:23:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f42c7c17-1e72-3b41-9e04-55074de2797a | -6.11713 | -59.91589 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e46d471-c28d-34d7-b99a-7b31cd65b50c | -8.59629 | -54.74581 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1197e17c-5135-36eb-9308-2a17c8235258 | -6.77665 | -59.44409 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b3be19e-18d1-3bee-ae3c-3579c1c1aac8 | -6.77714 | -58.6878 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 91d9c655-a875-3f7f-abb4-d381dc520a93 | -6.99131 | -59.05256 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c260c097-10e1-3e1e-8e92-6b31d101fbd9 | -7.37571 | -59.9493 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22b2127d-f2c5-3230-bc99-f14fac071cb8 | -12.82446 | -48.46337 | 2026-08-22 05:23:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9860bc39-04bf-3ce5-92ec-139eff74eea3 | -6.20682 | -53.09171 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc6714a3-c71a-32c9-a7ea-b13995e0cb3c | -6.78846 | -58.63607 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4473e20-b862-3a79-ad13-3583e3135fd0 | -6.81687 | -59.40435 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0685d43c-e377-33cd-be40-b6febecaa27a | -6.77988 | -58.6704 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ecfdb78-074e-3147-a17a-802a4080965c | -6.81963 | -59.40834 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38eb407d-c6c9-360b-800f-df59e87f5855 | -8.63031 | -54.73643 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46f14bc3-7269-3652-bef5-9ad55ccb49b5 | -6.76881 | -58.65438 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4649bc26-96f2-39ed-83c9-49ae21e6e235 | -7.3443 | -55.66742 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dea38217-aa86-3702-963e-3929cf821750 | -6.95193 | -59.30173 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f52b2c1-5de5-3122-b56c-270e6c659b2c | -6.53354 | -55.17422 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 458c0fba-6f39-305f-9ab6-3c742d660b3d | -6.85436 | -58.9741 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45f0f163-f2c4-3229-99af-ec835365a136 | -6.15581 | -53.70148 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28d21a0d-dcd0-3e8c-8aa0-3c27e814c4e7 | -6.11601 | -59.9229 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea7fa909-c2cd-37ee-b582-f43edc9fd040 | -6.77821 | -58.65943 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6c579a7-680e-3424-ae9b-6c7f57258cbd | -6.79539 | -59.43288 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 085a65e9-f7c7-327a-8867-100189f13db0 | -8.02906 | -54.00557 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2556bede-e5a6-3fb6-9ca1-df11ad3a462a | -7.1356 | -59.64299 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83514fc9-dcb5-3c3f-8d92-569fbceeb449 | -6.01224 | -57.82737 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 785444c5-69c8-3a92-b2c7-8a96507d1233 | -11.16248 | -54.02452 | 2026-08-22 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c43bfb7-e5b4-3e2d-86fa-7b860ec31e7b | -6.55474 | -56.54699 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75cbb82e-49a8-36f7-bb43-073c428412f2 | -5.9988 | -57.80342 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48936a86-947b-31bb-b120-ecd889c58adc | -6.85271 | -59.4136 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6664f1ca-1016-3a76-a9ad-1a91cf740c77 | -6.65221 | -56.3362 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4724ce5f-92c8-30dc-979e-df53492f8ac5 | -5.7859 | -57.18912 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2518c367-0dc1-3c64-bd39-07c9fa3717aa | -7.35022 | -55.66666 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21a754a5-8f2b-3b20-a6cb-a90d01492b2f | -6.82031 | -59.66055 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8caf9298-f94c-3ad5-9d73-e508883f223d | -7.3504 | -55.67725 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27f5e0a3-2ee0-331f-8c9f-cf9eb7f6b9e5 | -6.85165 | -59.46311 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11d05a49-a475-386e-896e-be84b7ccf0d6 | -6.55317 | -58.51374 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd974da7-24c7-36b1-842a-4387e9e2711f | -8.5251 | -54.82744 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9c832e22-d7d4-32de-85cf-1b2ff2331161 | -6.79728 | -58.62316 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7a58775-6b56-3ddb-a38f-8f6b677400e8 | -6.69692 | -58.93824 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd86c1dd-c4a7-3ab0-8851-596b6a34e6e8 | -6.79208 | -59.43235 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 11053770-9cb4-3a5a-b536-5a18a143e6a0 | -6.6903 | -58.93719 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71bf8b3a-336b-3728-8b7b-10643dbb5623 | -6.37992 | -54.95789 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36fa261e-1193-3d68-8308-b018d503d585 | -8.53566 | -55.3292 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d757d426-aaa9-3a1c-9f7a-6eb72e58c43e | -6.96847 | -59.30436 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d0a45e4-14e3-33ee-9bca-76c46997836b | -8.10631 | -50.05078 | 2026-08-22 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| befffbcc-8b4d-3a3a-a18a-7790aba4b7a6 | -7.39114 | -60.00182 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9003958-587a-3a5f-b55f-ccdc6bb72cef | -5.6872 | -60.24195 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8cff5c9-e96c-308e-8574-69c5d5385bbb | -12.83784 | -48.46022 | 2026-08-22 05:23:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5866bcb4-cbfb-3751-820d-2a41ce991141 | -6.22448 | -55.48214 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a3a6e9a-676e-3e1a-b044-4033f00c82b9 | -6.89291 | -55.71043 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de81e0ed-6b27-3c77-8e1e-8898b4687300 | -6.78711 | -59.42092 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 193a38de-b10a-39a4-8345-040165a46e15 | -6.55108 | -56.26353 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13f89b3d-bc80-3c4c-961b-67e98e42ea95 | -8.58174 | -54.79048 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7bc12c75-b85b-3a26-beb6-2778c6065843 | -6.74893 | -58.67267 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e33801cb-e679-3feb-b9a7-99b4c7dfe1b5 | -5.91664 | -61.29922 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32ce2232-c559-3a00-bb17-9bacc968572f | -6.78629 | -58.64997 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d28bb755-b029-368c-8e95-4c56948ace04 | -6.80972 | -59.42805 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0023d366-c4ca-3a28-9c33-b368effec7c5 | -6.75721 | -58.66328 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c6906d3a-a6a4-3de3-a1bf-06e801358d85 | -6.76828 | -58.67928 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README67.md)
