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
| 8bf4dc19-f087-3797-9195-17fbfacf9095 | -6.67603 | -43.772 | 2025-10-22 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b60c887-cb3b-3b05-8ae6-960bde7a9918 | -9.43668 | -49.19713 | 2025-10-22 04:25:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f7296bc-a481-382d-bf90-18f987e3f0a6 | -9.19897 | -49.69217 | 2025-10-22 04:25:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 405b9342-e9c9-3533-81b0-1835f72b565a | -2.94905 | -49.34178 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d28965ea-8d67-3f02-bd3b-f9b12ecb95e8 | -3.32956 | -50.22354 | 2025-10-22 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 397817be-9efc-3042-b23a-b6de0f21732c | -4.45354 | -43.23497 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 045e15b5-3d28-3594-a9e0-c506b5dda858 | -3.8173 | -47.41162 | 2025-10-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce96ec32-03dc-381e-9a50-e0acfb3e533e | -2.77199 | -48.58715 | 2025-10-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25203ec3-1526-354e-8ba2-44454bb9cedc | -4.45005 | -43.23444 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3de26f51-75af-3711-985c-eac2f66fcd78 | -5.15601 | -37.64765 | 2025-10-22 04:25:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c09191a2-3347-39c7-b49a-02e34e12fb67 | -2.94958 | -49.34451 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5deb3a42-1995-3f36-b741-a9f9059f0ac1 | -3.33738 | -50.75185 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 673c51ae-1f32-3f25-ad38-855c351cad56 | -4.91104 | -37.2021 | 2025-10-22 04:25:00 | NOAA-21 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 27b7f5ab-2207-33e1-9915-eb4a332f8890 | -3.14608 | -50.16352 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9942f835-98c1-308e-aedb-423fb5aa221f | -8.22774 | -45.74984 | 2025-10-22 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38e50d47-2663-35a4-b531-2f10f6d836e4 | -10.25389 | -48.46737 | 2025-10-22 04:25:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb1ff8c3-2841-3d78-8ba6-a0bd5cb08314 | -3.02835 | -49.45498 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17832a97-7410-3fbf-82df-0a2fc8017631 | -7.9485 | -44.84279 | 2025-10-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9158a7e2-d8f7-357b-bc57-4e143af10adb | -3.52015 | -43.90373 | 2025-10-22 04:25:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b74a6e82-e2c4-3f29-9aaf-d389a1230ce6 | -3.00394 | -46.91727 | 2025-10-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28d069fa-b42a-3958-8fa3-3cc71fee5aed | -5.51848 | -47.42301 | 2025-10-22 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbcbc689-2c86-3306-a5c9-bbe0a7c7438a | -7.50728 | -46.63821 | 2025-10-22 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 117c8b32-cd81-3977-ad90-3a44f1d2da74 | -3.24741 | -50.13337 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f087567-15d5-361a-ab26-1710b6956f4e | -6.53463 | -44.3588 | 2025-10-22 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d0f26f5-e5e8-32c0-b67c-4e78ed0b2193 | -9.11465 | -48.82165 | 2025-10-22 04:25:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb7e6266-a295-373c-a378-effd2a2be49a | -8.97053 | -48.64901 | 2025-10-22 04:25:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee368185-79e9-390f-add9-6fd2b2c3daea | -9.22436 | -48.59952 | 2025-10-22 04:25:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 640b774a-874f-3c13-a043-c25dbc70f03d | -2.90687 | -48.98504 | 2025-10-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34bbebab-4357-32d7-9022-06aaabf3bb5f | -3.0404 | -49.52637 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a16bd019-9ea2-393f-9d07-df3539563c12 | -4.30335 | -48.06452 | 2025-10-22 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 702e1ee0-18be-345b-ac8a-59a3db2fc18b | -7.31486 | -46.30375 | 2025-10-22 04:25:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0867ecca-fcc6-3365-a688-fc65ccad4475 | -6.3416 | -43.51196 | 2025-10-22 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e819b4ca-86bb-3cbe-a861-22d34f91d51d | -3.25607 | -50.12962 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4e95bf6-0aaa-3547-8405-ade644825ca1 | -7.94602 | -45.2567 | 2025-10-22 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e47467b-eab6-3379-9c43-d90c55b16784 | -3.94101 | -48.08751 | 2025-10-22 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9acb3a48-907b-3e7f-b5a7-6f29920042a6 | -4.83547 | -42.11462 | 2025-10-22 04:25:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 11bca841-fdba-3e71-8940-1b27ae6dcb80 | -4.22718 | -47.21553 | 2025-10-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 406afc5e-b167-30e3-8332-b3578de6e632 | -7.6575 | -44.58786 | 2025-10-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c36ed78-7fc9-3405-89d9-b1ea434b742a | -7.93778 | -44.84494 | 2025-10-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b10b668-ad13-3d8a-af68-7a49641d93fc | -6.64595 | -43.60782 | 2025-10-22 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 66783646-084f-3bae-a9b2-7d2faa0e6585 | -7.1511 | -44.96621 | 2025-10-22 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da1965c3-5585-3631-910b-276a941e5e22 | -7.74484 | -46.55957 | 2025-10-22 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c7d58fb-e0d1-3b01-85fe-157a564edbf2 | -7.51058 | -46.63873 | 2025-10-22 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75781011-050f-361e-822e-51ac4c06a449 | -2.93022 | -48.30157 | 2025-10-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4971395f-3f93-318a-89c4-27d32af5ce27 | -4.73858 | -43.26094 | 2025-10-22 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b41522b3-1d8f-37e1-913b-2e903febe101 | -9.23706 | -48.5639 | 2025-10-22 04:25:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33941bd5-7604-333f-821c-08827b81db17 | -6.35358 | -47.50023 | 2025-10-22 04:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 259f88d9-142f-3589-b3d5-0953a97c5d22 | -3.24994 | -48.76842 | 2025-10-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ecbb132-5923-37b4-9713-8ab2384e6b5b | -2.90884 | -48.73688 | 2025-10-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53b26cd1-9439-302a-8cbb-273eb5c612ad | -4.28376 | -48.25497 | 2025-10-22 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1c25340-a45f-3ee9-a869-b2c9b7e85541 | -7.65688 | -46.8787 | 2025-10-22 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e84f7677-ef61-3a52-9402-567d72595c15 | -4.45704 | -43.23552 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 7b72de68-a654-3638-8ac9-2197a9d0ca84 | -3.94039 | -48.09134 | 2025-10-22 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31950fc9-5575-307b-905c-51a5cbd20761 | -7.94511 | -44.8423 | 2025-10-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1365301a-f3dd-3b83-9531-0d8223a0c6aa | -3.14862 | -50.17118 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50e110ef-394f-3f67-ac35-d9baae67a4dd | -3.02458 | -49.45438 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c6d026fd-1ff6-3f45-9d50-eb14b576ca2b | -4.22381 | -47.215 | 2025-10-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56b6a613-3c4e-3876-9f80-85c023c57bbe | -7.66035 | -44.59206 | 2025-10-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d084fff9-d7b7-3883-aef2-9f7f59373502 | -8.81232 | -48.66912 | 2025-10-22 04:25:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14e4ffa2-92b1-309a-8cf4-26bf39a56978 | -6.32083 | -47.42582 | 2025-10-22 04:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29f32e06-ba0d-3ea9-8280-2bd76d159c9c | -4.11278 | -48.02749 | 2025-10-22 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0faa919e-00fe-3106-bd02-09f97a79c849 | -4.12116 | -42.17852 | 2025-10-22 04:25:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 31bb0adb-1c79-37c3-aa19-bd3eaa27352b | -3.41471 | -48.88356 | 2025-10-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cff58f5-dc73-3123-94c5-858834d36536 | -7.13625 | -45.21942 | 2025-10-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f91e2ec2-9f87-309f-9912-056950399798 | -4.44491 | -43.23478 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cac8171d-0ae3-3368-9511-f9a554951681 | -4.83794 | -42.11329 | 2025-10-22 04:25:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d61a41c-866f-30eb-8609-b72a44eacaf7 | -7.84206 | -45.24812 | 2025-10-22 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0597e5a1-bd0a-36d9-bdad-e460c4e26ae9 | -4.73918 | -43.25703 | 2025-10-22 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 1bfc36c7-ece5-3676-8467-5967b3a28ebd | -6.53406 | -44.36251 | 2025-10-22 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 63c24f7b-d1d7-37b3-bfac-365be4c6f6c6 | -2.92957 | -48.3056 | 2025-10-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75a31864-1216-33f6-97a5-2eb75190146c | -2.02993 | -56.88202 | 2025-10-22 04:25:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40c9c84a-fadb-37c7-b712-8c054cc39c9d | -2.69265 | -48.70495 | 2025-10-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06f6aa8b-025c-3e34-b49a-fa6165579eb7 | -7.88991 | -44.53512 | 2025-10-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d020ab6-c5af-392a-96f0-4fc67bc9b4a3 | -3.24571 | -48.76469 | 2025-10-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb2856b4-df07-3322-b2fe-fd4fa65b16f1 | -6.63887 | -43.79461 | 2025-10-22 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c8b6f8c-19d6-31b8-99eb-af0d4c5bf2f6 | -3.51972 | -49.44431 | 2025-10-22 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 43519cc2-2ed1-31bd-a374-0d8fe21fc218 | -7.94116 | -44.84546 | 2025-10-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4ef9f36-4f3d-380d-bf94-472d1f0165d2 | -5.93378 | -47.31343 | 2025-10-22 04:25:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9448156-17f0-35b0-a987-97dd60392782 | -5.92098 | -42.6825 | 2025-10-22 04:25:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a7c11bca-8176-35a0-8dc1-468a379eedff | -7.9352 | -46.01153 | 2025-10-22 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 861c95d8-08fb-326c-a47b-83caeae13ca5 | -6.81723 | -45.304 | 2025-10-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 421cc6fc-5852-301d-88eb-4f19bfff4947 | -7.63684 | -42.17342 | 2025-10-22 04:25:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7a65eafb-2a31-3ee0-ae79-4a4427757271 | -5.41393 | -45.29205 | 2025-10-22 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 63488192-aa14-37b1-acb0-2589c10fb740 | -5.97397 | -46.60668 | 2025-10-22 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 081924ad-c31c-33b6-a92e-85f420995872 | -3.25051 | -50.13899 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eb4b1324-46f8-3f65-b4db-6b82e8eb0300 | -3.99339 | -48.32682 | 2025-10-22 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cca5311-59e3-337c-8a37-a02678fd31cb | -7.51004 | -46.64219 | 2025-10-22 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e30f89c-5a0c-3252-9b05-73fb90ca5670 | -4.08528 | -39.96793 | 2025-10-22 04:25:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8ed80f69-6ab7-3dac-9ce8-75aadc540272 | -8.22572 | -45.80703 | 2025-10-22 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d2616e22-3642-3021-8561-f4c5e9635d2f | -6.6801 | -43.76863 | 2025-10-22 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d404a8d9-2bea-33e2-8e5a-c0f250a2bbad | -7.74538 | -46.55612 | 2025-10-22 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 706ec5ee-1601-37d9-8dd8-dda67b5c7729 | -3.56843 | -49.48254 | 2025-10-22 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 820b3633-5ab3-37a4-b272-f66ec565610d | -2.80991 | -54.37802 | 2025-10-22 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 603f9a68-8c9b-3d5c-8e6d-9a95be889965 | -5.73537 | -46.45885 | 2025-10-22 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72b29679-f950-3fbd-84f5-7b1d222b95b6 | -5.44717 | -48.09441 | 2025-10-22 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4942df75-ef97-3645-9de0-098ba0718d58 | -6.13575 | -47.00609 | 2025-10-22 04:25:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f85ca4b3-e0b9-3ffe-9842-b32cf1716589 | -3.02824 | -49.45837 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41803fa0-30c6-3ace-ae8f-841d76662997 | -8.2316 | -45.74685 | 2025-10-22 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d70360c1-cae6-3929-9a1f-87eb33d9e997 | -7.29688 | -45.10576 | 2025-10-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c90c2d8-2968-39ca-833d-4fe19dad761c | -3.15028 | -50.16109 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README9.md)
