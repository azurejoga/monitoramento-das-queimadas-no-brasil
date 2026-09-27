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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87681d96-83d4-313b-8937-5e64b171c75d | -6.28253 | -53.38266 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c7703a1-2dc0-33f9-bf5c-870638bdba52 | -3.91643 | -43.01853 | 2026-09-27 04:51:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 67d0bd9c-e576-339f-8119-0955a9db8413 | -2.79289 | -57.69759 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d683791d-39f2-3369-8c52-2d672d8dde52 | -4.67544 | -45.98915 | 2026-09-27 04:51:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c00bc719-8565-37f1-9cd5-e920803b9e14 | -4.9826 | -56.14944 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 250ee896-0780-32a2-984d-7e61fa341793 | -4.49913 | -47.50759 | 2026-09-27 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b14e0c7a-8747-3c5c-a827-662143ba66c4 | -4.36154 | -55.27721 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80034f27-bc6e-3a0c-bc62-1061faf63d26 | -6.35052 | -46.44612 | 2026-09-27 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32de7c4c-1b4b-32eb-bb96-a353e40853b8 | -2.92835 | -45.50528 | 2026-09-27 04:51:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e232231-efd5-37bb-8349-9c28169463bc | -2.36457 | -50.34486 | 2026-09-27 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 301ba24f-3c56-36b1-ade2-132271327cae | -4.46168 | -55.03469 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a88573dc-fea3-3c71-8b4b-5460d093fcc0 | -3.07473 | -54.38327 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16932ed6-06af-3879-8ed8-b2ceebcb30e7 | -3.20153 | -51.04012 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4fa650f4-1bd4-37af-932d-762567eb4f52 | -5.16403 | -56.00299 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a3f9774b-4487-35da-9798-d01e0be6ef0c | -6.09409 | -57.63128 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72ac84ee-3cbf-3cb1-860c-e68470a3a58c | -5.17844 | -46.08657 | 2026-09-27 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 967f7aad-bdce-3d11-90af-c882aa094945 | -3.76532 | -51.81014 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4697954-dae8-339a-88c7-3eb6ddf44aed | -4.28759 | -48.60713 | 2026-09-27 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69423e77-9d42-3834-ae79-962edab39270 | -3.0155 | -52.498 | 2026-09-27 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c1843c0-6b59-3836-ba1a-b81b4e7886c0 | -7.50001 | -55.02414 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d80dbee8-d4bf-3c58-81d2-f927c73573a3 | -8.35222 | -44.18989 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f03625bc-a1b6-3967-9b71-06d5285d1ebc | -3.62193 | -51.85837 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0670c04f-5952-3f58-962e-51d3e51ea599 | -8.35836 | -44.18409 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f3405766-3047-3ea8-9ddc-6bbd2e9c3ba8 | -3.39631 | -54.08267 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7427511-df43-39c8-a914-ad8c12f57ef1 | -4.54888 | -55.535 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfc3227d-7c28-3e17-9784-1929b63974f8 | -8.25112 | -43.78692 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d34f2015-290c-390c-8a36-a8bfab1f0dd0 | -3.01604 | -52.49457 | 2026-09-27 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8af15266-8a5b-34e0-9f7e-ea69659bf1df | -8.59358 | -54.64767 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b3d7e90c-f995-3c30-bc18-4142232f33e7 | -7.68547 | -54.747 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea67885c-4ae4-354f-b995-555f9b7d71cb | -3.86939 | -51.79796 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 741eb285-bd5a-33ca-a744-5689bb80639b | -4.28922 | -55.25375 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ccd7a23-1867-32cb-b264-cc133d390e6b | -2.67267 | -56.46241 | 2026-09-27 04:51:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a26fb0d7-7d5e-33a6-881f-3666dec93610 | -4.50919 | -54.94477 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3274b78e-1e83-3c58-ac2e-28eb3c8c574b | -3.10604 | -50.32002 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a92b3b25-499e-3b3e-ad37-dcf74ad54ae7 | -3.27021 | -50.14544 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7966bd75-0e28-3f11-a300-8a6073ab1b60 | -2.41791 | -50.30105 | 2026-09-27 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 741e1e8b-8b77-3e0c-aaf8-f9c855d9a8cf | -8.34024 | -44.16373 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a29cec3-2e3f-3179-ab97-4027a683b048 | -2.97245 | -51.04762 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87a840c5-f65a-30cf-98a5-a6e77150305d | -3.87323 | -51.79502 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eef62fb0-0174-3441-9661-d1c021acf024 | -2.36679 | -50.34119 | 2026-09-27 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6914944-90b0-3c8e-bcda-f4372a52022d | -3.84638 | -45.13712 | 2026-09-27 04:51:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1bddeda-97ff-3b06-a4de-1914df9ab48b | -8.36799 | -44.15147 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c88aea81-b250-35ca-8dd1-4462e8046577 | -3.4211 | -50.43839 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af874770-b6fd-3ffd-9256-e5b6aa6fdb3c | -8.35879 | -44.18077 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3e5450e-b63f-33c4-b7f0-b85d8e313c6b | -4.56341 | -44.08192 | 2026-09-27 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11c9088a-91fc-37a8-b12c-bb064934a5a6 | -3.94913 | -56.09768 | 2026-09-27 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87d056f3-9dbc-35d8-98e8-2053abdab43a | -3.10327 | -51.27875 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4be3c233-826e-3034-a193-867daa5b4823 | -2.72874 | -54.1989 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2d08772e-2135-3615-928b-7d2731da87c6 | -8.34418 | -44.17447 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 315c8858-ffb9-3f7b-93be-4f82bcf7be21 | -8.35608 | -44.15998 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 951f0357-32d0-3afd-acfc-c088ad365b63 | -3.42449 | -50.41658 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1436218-470a-3491-8825-fc0b1ab9ba0a | -6.05932 | -53.61115 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44f79e9f-b904-3e94-a752-fad291721f44 | -6.88182 | -55.55564 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e566bcda-a91a-3876-8820-80ba2ba7a379 | -8.34737 | -44.18567 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2951a734-63b6-365e-ab24-15fdbb34a86a | -6.04659 | -53.60552 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccd83796-6997-3761-b288-f88d61cd0dc1 | -3.81928 | -50.63255 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6857bec5-3adc-3b6f-afdc-f71c0e207d79 | -6.09636 | -57.68093 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d16d3acb-0dcf-385a-8d44-8147f372401c | -8.08996 | -54.73708 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae2014eb-ce05-3116-b64d-52ebfc44a7fe | -3.00476 | -54.20577 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e93b01f-d73e-3782-965d-cf9352c86738 | -2.96653 | -49.56345 | 2026-09-27 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d0c55ee-5965-3d52-96cb-9da112ea1c6e | -4.25838 | -51.04374 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18131588-87fd-36b4-b675-6d2be3507336 | -1.61989 | -55.10752 | 2026-09-27 04:51:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba441474-6642-3fc9-9b2e-bda7f57d61b3 | -11.72294 | -50.61424 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5777962c-16df-3fcd-aad2-9a7d6e52d27c | -15.42299 | -47.90933 | 2026-09-27 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3bcb0587-710f-384c-a7e0-a7386b5b06f9 | -12.66418 | -47.29588 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 94d6a3f1-8315-300e-8c97-2f13689a68e2 | -11.27526 | -54.43521 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f831dac4-45d0-3ae0-a1d8-700713693c1d | -11.27856 | -54.43574 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f967f9ae-3aed-35d9-80e0-3734b6bb45ee | -12.13843 | -50.32734 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fc9a066a-f083-3082-b502-e1352908a01d | -9.57162 | -62.70479 | 2026-09-27 04:53:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15b45715-0094-3a5f-a3c1-f3b443bdf32b | -12.67166 | -54.64196 | 2026-09-27 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da3fdc5e-750e-3169-8312-753b2389187c | -14.11966 | -46.3291 | 2026-09-27 04:53:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab891ef3-0bda-3168-855c-44c266bb2611 | -13.0979 | -47.4198 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e1f3402-c604-3207-8338-5d0c12e284d5 | -9.61632 | -55.10557 | 2026-09-27 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5bd27e1-65cd-3509-8dc1-ea161bab99a4 | -11.61237 | -49.87023 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4266bcb-1176-3cb6-b291-17e9db7883c2 | -12.90035 | -61.71726 | 2026-09-27 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 751ace72-c1f2-3bee-9763-55b70f1e7ff5 | -10.61461 | -54.00861 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b87018b-f62f-3b4d-be1a-35e3271c8db7 | -10.81041 | -60.72855 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 319f9328-a07e-37ac-8657-664cb3ae02f0 | -11.775 | -51.00498 | 2026-09-27 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b8d521c-7bfa-3294-9cc0-379a11ebb1d7 | -12.57966 | -55.68825 | 2026-09-27 04:53:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be00d71a-76b8-34fe-80bf-83aeb01285d6 | -11.0488 | -51.32354 | 2026-09-27 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f721b541-accb-35bf-91ba-c0e69398de5e | -11.98896 | -57.60213 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d6b9432-40df-315d-a9f7-00630506734b | -10.42343 | -53.79182 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 245d0919-f77a-3e4c-b788-025b6b5755ae | -9.39513 | -60.34195 | 2026-09-27 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73f5a692-56e6-3935-b585-fda9f0d4a892 | -12.23225 | -50.7121 | 2026-09-27 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef3b2a3e-4a8c-3aaa-8104-f1ea5be3dbfb | -11.42607 | -47.42629 | 2026-09-27 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 33ae64eb-1403-304a-99fb-9f78af762a31 | -10.03881 | -62.45835 | 2026-09-27 04:53:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa233774-def1-330f-8742-31a103c8ac16 | -14.22142 | -48.50574 | 2026-09-27 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba516b4d-61ba-30a0-8f51-723915a5a215 | -11.88922 | -50.49889 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c855d3e6-5214-3733-9982-6fefc5cee4b5 | -12.25172 | -50.70616 | 2026-09-27 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6ade4c4-fa16-3898-88cb-1c7444d97612 | -13.33675 | -51.32621 | 2026-09-27 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98b814a5-5031-360d-a2f1-1bd578505a07 | -12.29015 | -50.27518 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c412fc4-bf21-34c7-a256-0e1af64645de | -10.2974 | -59.46125 | 2026-09-27 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aa68719-4822-39d5-8621-5a88970407d7 | -9.7745 | -54.285 | 2026-09-27 04:53:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fb0795b-490c-34a4-b4a1-f0caecbebb3d | -11.88667 | -50.51646 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| edb0d0f2-b694-383f-8e7c-d5f0be4bb248 | -11.27912 | -54.43222 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1623e2da-a008-3df7-adbd-0b9bfdad75d8 | -11.57859 | -50.50082 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fa95e3e-2107-3b32-a0fe-7f58744f7a51 | -11.24016 | -49.85151 | 2026-09-27 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6b764a6f-f512-3408-815c-17e23a12424e | -14.69 | -59.6095 | 2026-09-27 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 18f48f49-3ffb-39e6-ab25-edb59626dcab | -12.46057 | -54.44833 | 2026-09-27 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e088966-29b6-37b3-a483-0878358babc2 | -12.65963 | -47.29523 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |


[Clique aqui para ver as próximas entradas](README33.md)
