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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a76fbd27-f31b-37c9-827a-98613cc05c35 | -10.4285 | -61.22685 | 2026-08-25 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b9dd635-fa6e-3636-9efa-093655c6a749 | -6.8406 | -52.50246 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7af56b49-a546-3c60-a2e3-7ea30f35d920 | -7.00737 | -59.23943 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e89cf1d5-7263-38cc-848d-2f5c97e83ed4 | -12.74929 | -46.46911 | 2026-08-25 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1feb6eb2-96b5-33a0-825f-930ee790a85d | -7.2144 | -60.61913 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8967a0a4-b7ca-38f0-bd6c-9616a4398c0a | -11.20385 | -55.04918 | 2026-08-25 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39695a09-4900-3b64-b1b8-fa3baacb2d7a | -11.16537 | -54.0056 | 2026-08-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c60a114-3f39-3251-86b8-c9d212725e98 | -9.97778 | -48.32027 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3906c661-93e1-345f-9b2e-507b767e634a | -9.67097 | -55.10115 | 2026-08-25 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fcc4d4a-b9be-3e81-a9fb-1703da123523 | -6.84465 | -52.50302 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b6ace6e-f06a-3029-817b-68d8f85090aa | -6.82274 | -58.65139 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c03a0752-8aec-34c8-800c-4d1fd6f1415b | -12.89254 | -48.48494 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c635b248-0577-309c-915b-96461203aca7 | -9.44459 | -51.58563 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a259f1a8-fadc-3ef8-9829-5a7b3d0f1044 | -6.22667 | -55.61855 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c5b28b31-2906-3e97-a700-531608052940 | -7.0062 | -59.24673 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9800e5bc-425d-3e0d-b15d-26c4c8a7fc83 | -8.08654 | -47.52039 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d031557c-a1eb-3d82-9f6c-1dce87b26b96 | -6.6 | -56.37076 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 005cdf5c-bef6-3e4a-b321-864eaf1e5f10 | -6.61605 | -58.38749 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 877f38c0-0163-372a-8f5a-f509e915ff3a | -11.98305 | -45.90723 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d1a4b379-afc8-3c06-83a1-bf516f805b14 | -6.63493 | -58.48401 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dfae7c7-d907-354b-a01c-eb569bd9f91c | -9.19254 | -59.45119 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7566eda4-57a6-3db8-8203-7cff7f64e9fe | -6.81215 | -58.65336 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c758e726-7ac2-3c91-aece-a2944d662c9e | -9.43652 | -51.67516 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbdac307-bd35-3c07-8a1a-bf587dce0368 | -12.86815 | -48.49312 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0355dca0-19e7-38d2-9f3d-35e37f65a1db | -6.13223 | -57.85351 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 861bf1b8-b09a-3b99-90fb-755c39a3c345 | -6.53856 | -56.26306 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 489b940a-e05a-30c7-844b-d9033faf43e3 | -9.201 | -59.57115 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68be1eb9-5db2-372e-b61a-fd64d2221ef3 | -6.43938 | -54.96006 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe39d66d-6dcd-3eb8-82fc-12a1a9b3b960 | -6.99766 | -59.24884 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 68af61c3-163d-3a5f-9440-813ba16cc276 | -6.12742 | -57.83865 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1e178f6-800e-3c6b-9281-54946ddb1950 | -13.3492 | -48.20578 | 2026-08-25 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dde75953-1322-33ee-81ff-fb1b69de6336 | -11.99051 | -45.93162 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 2492c782-5c85-3638-9739-8c61e968ec8b | -7.05521 | -56.61817 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a38e8faa-f408-3a57-aaf9-d15d05438a08 | -8.15988 | -46.69622 | 2026-08-25 05:12:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbf890ac-a673-3f12-9be0-11e1faccb2d9 | -6.15173 | -57.94533 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0b8f35c6-68e3-36fb-807c-a0d5f2edbcac | -8.56652 | -63.02145 | 2026-08-25 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05cefc25-ec36-33ca-9968-6c091c507c52 | -6.62715 | -58.48999 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f4f486a8-6eaf-3fca-83a4-baaf0a4e235f | -6.80344 | -59.58933 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93460483-ae7f-38b6-9881-f5e787f6efd8 | -12.72109 | -48.38595 | 2026-08-25 05:12:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4dc422f9-a4bb-315b-a842-22610383ab72 | -11.99117 | -45.92558 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| e00552da-b4f8-38bc-ae2e-38644f737f45 | -6.50793 | -55.22297 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e83107c4-5378-3750-aaa7-26cd68018e19 | -6.63604 | -58.4986 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 832887a6-32a7-301f-97ae-d58982125f0c | -7.38293 | -55.18405 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fcb28995-b464-338f-9150-f4ce37cecd3e | -12.88458 | -48.50306 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3600310-afbe-3d7f-8a56-a746ea80891c | -6.85632 | -59.41083 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 434b0745-b107-3271-af59-aaa73e67376b | -9.6764 | -55.08934 | 2026-08-25 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7892e09f-6a02-33bd-80b3-0e32f04fdd1d | -6.96829 | -59.08439 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b48a0330-e550-3f98-9fc8-15569c768193 | -8.17275 | -46.70044 | 2026-08-25 05:12:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0968a6c3-0efc-35c3-8b16-68f544689adf | -8.11538 | -47.47957 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdea6f4d-e616-3ee0-b5f0-9412c24bfc90 | -9.41814 | -51.64469 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74a0c80a-3787-354d-bfd2-f5b0ac60f062 | -12.74876 | -46.47378 | 2026-08-25 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab43eac2-d4c0-3ae7-bf7a-d552cc7f7ac6 | -6.99484 | -59.24468 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 2930843a-d57a-35c1-8049-b7128cab957f | -6.63215 | -58.47997 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a82861d6-6968-3c88-96d5-aa1970a33dbc | -8.08449 | -47.5363 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ffb90d5-e6cf-34cf-877d-5ea87db29e6b | -8.07229 | -44.65463 | 2026-08-25 05:12:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 457f3d85-47cc-37e7-a78f-4589a33888c2 | -6.12459 | -57.81337 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c9262016-a1ee-30cd-8d85-e9b28a6a2389 | -7.49427 | -55.35464 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4775daf-dbb1-325a-84dd-4863b5d81f21 | -6.82819 | -52.49784 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7821138-a363-3a5c-a019-3298bd0af81e | -10.48073 | -50.43758 | 2026-08-25 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0011061e-e920-3da1-9c72-78116616b07c | -6.63104 | -58.487 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c90b9f5-065a-3726-a76c-b5f339fd44ee | -7.53945 | -61.35167 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8264c7d9-e7ae-3b5f-81c5-f61d0c5806e7 | -6.14841 | -57.94482 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 43768f8f-6c7a-337f-aae8-03a4d03cfc58 | -7.54187 | -61.29567 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 570c0594-dabc-3dae-820b-c8f96a0e7fd0 | -6.86765 | -59.40856 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 643d5866-047f-351a-b841-6c6b52cb4c52 | -6.80911 | -59.59787 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bde453e2-3a93-3b20-b75a-2b21b9650c55 | -6.82552 | -58.65544 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e45d822a-5282-3274-bc15-c392c6a45453 | -6.95577 | -56.4907 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b8b91fb-b837-316f-8498-232cd6739cd4 | -9.97828 | -48.3164 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f78bc116-df60-32ab-bd68-4f59f6e140b6 | -6.17434 | -57.93106 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad4cc759-92a9-3a13-b475-124178813482 | -12.87933 | -48.49775 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec765f90-dba9-308b-83a6-8e0c4b732842 | -12.59089 | -47.91798 | 2026-08-25 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88f56db3-0d13-3d37-aa31-c93ba7e427d5 | -6.95242 | -56.4902 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff4c9605-d6d1-3f66-a27b-34ac9aea0836 | -6.891 | -55.69897 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85fd5030-0ed0-3df4-9113-980cb3c68a31 | -10.83567 | -57.51316 | 2026-08-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08b7246b-4b08-3e33-ad6b-32743fb98f1e | -7.00398 | -59.23889 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| da6cf587-c46f-3dfe-80b6-778079085365 | -8.15251 | -52.01868 | 2026-08-25 05:12:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5330516e-1335-3b72-8429-e2699d1dedde | -6.98692 | -59.25087 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8a5df8db-644b-37ca-8220-68552b2cca91 | -8.57424 | -55.27668 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 530f35e9-10eb-3dc7-9344-8a205ed53c5a | -6.00762 | -57.67097 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fc980e2-bdf4-30f5-acbc-45c48db89447 | -6.5477 | -58.52071 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01d19c36-e03f-3119-a689-07359f5cd43e | -6.13277 | -57.85005 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ef6b6d2-91c5-3af1-b22b-84c6d047229e | -8.59946 | -50.02107 | 2026-08-25 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b86b008c-7566-3402-a5fc-9beafa0f4b2e | -6.83705 | -52.49834 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b5186c85-cb05-3f81-ae6b-881e50f8edec | -6.77019 | -59.44646 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 236c9fc4-6fa4-3577-9bb0-afa37d7d897e | -7.00561 | -59.25035 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17410513-2939-3cff-a818-780180f25cd9 | -6.12164 | -57.74556 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89a40fdc-2ec2-3577-b298-c15df2d44c84 | -6.13445 | -57.86095 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 166d813c-936b-310b-9b60-11de401f03f0 | -6.95188 | -56.49374 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d89bf36-9eac-33f5-bff1-a5898aa79069 | -7.4955 | -55.35786 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51bb667b-989b-30b8-8958-546816f7c602 | -6.62993 | -58.49403 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f8aa6f76-1cd0-36cd-aa18-000635232b22 | -7.00046 | -59.26075 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4d7b5d22-1d64-3ca7-bedc-bbdec798643e | -6.79658 | -59.58825 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36285e12-bb1f-3836-9023-637b4ef458bb | -7.90096 | -46.38602 | 2026-08-25 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc8ca22e-3467-3ce9-9622-b95025ef59ad | -7.49307 | -55.36247 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ed861bb-0e5e-321e-90b8-39bf9da8e97a | -5.90876 | -57.71515 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4db66d7-e0bd-31f8-b84f-591c987e04fc | -8.5795 | -54.84846 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e292920b-9ecb-3dd1-a3b7-127db660fade | -9.15323 | -59.56717 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cc85c4e-1b1d-32ee-80df-6c933f0f5ed8 | -11.16609 | -54.0006 | 2026-08-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb755ab8-990f-34a6-a27e-126be35b2261 | -6.80971 | -59.59414 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4ab5b3c-b55b-3d49-aa61-aa39977452e5 | -12.89073 | -48.50048 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README53.md)
