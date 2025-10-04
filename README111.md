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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85d3af19-b495-3065-9882-79f7e6892cf8 | -11.92747 | -46.38944 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3aa22bf5-eb65-3400-a617-cdfe049a46db | -13.73895 | -48.08797 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5c778f77-1edc-387b-bbc0-0bc02c83ed61 | -13.32607 | -47.57597 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21f2ec88-6c49-354d-baee-3b2f1dab398c | -13.88396 | -46.51546 | 2025-10-04 05:06:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 95c6b193-2517-343d-ae25-962b71fd2272 | -13.68129 | -48.04365 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d28627bd-d5ad-3403-a3a2-2fd930670565 | -15.23343 | -56.82995 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 092a6f08-c73f-3a3e-af5a-af1d6842d7fc | -13.69957 | -47.35405 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c5447e6-3d3f-34e8-ba21-9c4f81d8f48d | -15.62171 | -46.94265 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5298a231-1ab1-3541-83bd-31f08f4df8d4 | -14.04223 | -53.92673 | 2025-10-04 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 62beeff2-186a-372e-af88-f03cf40bfa47 | -11.91971 | -46.40526 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 83f396a2-4732-3dc6-a03b-8174f48b2dcb | -12.93226 | -45.0653 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72564ab3-34f9-30c0-8266-2cde1ced6837 | -10.12882 | -52.34366 | 2025-10-04 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7d4f1cc8-e4b5-3659-a22c-49cc95173251 | -12.70192 | -48.54676 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6c7db4c6-ed76-310a-b9f1-a999faf54da5 | -13.29522 | -47.83879 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d58acbf6-4531-3316-86dc-a41f1b26a6e4 | -15.22619 | -56.81014 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 41b119fc-bc45-3b7a-9d1b-86e724a0c799 | -12.72368 | -48.56077 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad14ac3c-ac19-37d7-9213-744a55d3bc08 | -12.64395 | -46.98363 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5c2bf828-9f86-3a18-b419-79e64cb48a9b | -13.22832 | -47.82771 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 137768bb-b489-33ab-a269-6ce898680952 | -13.73931 | -48.08482 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e41ed227-2d36-342e-bc18-18acb0d469d5 | -13.10315 | -47.89001 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf2217cb-c0c1-3890-9914-9a169a0dcaa6 | -11.55084 | -47.64409 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f01a02fe-b1f2-39a1-9117-7cfcb05498a7 | -10.59918 | -54.35165 | 2025-10-04 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ec42229-ab6a-3b43-af45-8fe7f18c423e | -9.76966 | -62.32958 | 2025-10-04 05:06:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9254ba46-ec7e-3a0b-b8c9-62b06bd6d134 | -15.32066 | -47.33101 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8843063a-3a39-32e8-aa26-c701ca4f5e72 | -14.46208 | -48.39943 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3dad0ad2-d0d3-3766-98a4-1f58e67a7cc4 | -13.32213 | -48.11439 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d762f6c7-c752-346f-b97b-1a95679b8ef8 | -13.28979 | -47.83811 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 01ff4b9e-f3cd-38ba-a3ae-8098ae9a968a | -12.03857 | -45.19917 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 59c468df-3ea1-3342-a2e0-40d2e3adc387 | -11.91188 | -46.36943 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| db6fc3cb-5387-360c-89f1-3fe74d5b18f3 | -15.61573 | -46.94244 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cb13ce4-efb6-3aed-aa4d-31f213d61052 | -14.92829 | -46.88071 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77fdf99e-8d9c-3941-b46c-94cd245e018e | -9.44873 | -56.65321 | 2025-10-04 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11435b2d-57a2-3b41-a1e0-258969ad255e | -11.12853 | -55.4671 | 2025-10-04 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed9e5dd2-6a81-37e4-a786-cea995861b48 | -11.91474 | -46.3967 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8cda97c9-2e8f-3fd7-a2d1-e2ab1d6df4a1 | -13.32086 | -47.24582 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54f8b2c0-eec9-388c-a6c8-78f8f84839e6 | -13.35232 | -48.07243 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7543160-9d35-3115-aa34-cd8c72b323b6 | -11.91821 | -46.36616 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39e46032-6fe1-3ef6-b53a-8a0432854f0a | -15.59867 | -52.46066 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b18a2f7d-7861-3bf9-b6c1-61f52d51cba2 | -15.22914 | -50.12293 | 2025-10-04 05:06:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d890c74-c793-3aea-b5dd-b0fd725aaf7f | -13.13447 | -47.81308 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 10bf9505-64f8-3717-bc2f-66b0d82e20d0 | -11.70139 | -47.50671 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 562c3306-9bd0-3f20-aad8-2f24397ee886 | -13.70595 | -47.34846 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8e2913a-fb41-3e27-b647-70afae1bc2ab | -11.86695 | -44.96425 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcbf6581-4d23-3d1f-b2f5-25f277abf43f | -12.81329 | -46.85458 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 24c697f6-8030-3f14-b1d1-17d7934363dd | -13.25564 | -47.26448 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e90c0f0-4155-343f-891e-f5dc81999267 | -12.38502 | -54.46441 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eec8d6d9-9779-372d-b011-2c8f2338aa17 | -14.79737 | -48.2987 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fcf9576-64b4-34be-a6ff-72bd36a5e37c | -14.94544 | -49.97133 | 2025-10-04 05:06:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51b0d00b-9889-3a0c-8636-fed72f3ae522 | -12.88662 | -47.1707 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0815e2d4-48a2-3a95-8cdc-927f164e41bf | -11.91811 | -46.3751 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48db1fdf-c463-3c79-a6b8-f9a4bcdbc417 | -11.74221 | -54.72396 | 2025-10-04 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71f2cc74-b233-3cda-99c1-2811c40b898a | -12.71036 | -48.56293 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61367efa-8101-3632-a255-11fc6a0cd522 | -10.64578 | -55.0903 | 2025-10-04 05:06:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cd8dddf-1657-3628-82ec-0eb302465658 | -14.46249 | -48.39602 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 699cfc10-9c0e-33e0-a486-152ed9825663 | -11.91556 | -46.39616 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a21a34d3-ece9-32c1-b521-dee17d418a05 | -11.92517 | -46.35745 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eefb9cd4-9592-3d54-8363-23cf2d1ec847 | -11.91767 | -46.37093 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6b8fec49-0dab-36c7-8318-30f629f84311 | -14.89425 | -48.38675 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6de904c-dff6-386d-9376-e3667bc37d2d | -15.31401 | -46.37414 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac849609-217e-3465-bc0b-3eedd50cb8f8 | -14.66184 | -48.28672 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e673d97a-279c-3c27-9ef4-c597b41d7514 | -10.83626 | -57.17698 | 2025-10-04 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9aca125c-f177-3a96-8e6b-e42b673f4162 | -12.59678 | -49.88159 | 2025-10-04 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f99a1a9-2431-3786-b111-c9926a336b9f | -14.66224 | -48.28326 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03327c23-874d-3537-9743-85154101698e | -11.24883 | -47.80513 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1f979c44-86c3-3d25-b958-882eaf893d6e | -15.24335 | -49.30253 | 2025-10-04 05:06:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e1efc77-aa5c-36b3-81f3-7d409c8e40fb | -10.93098 | -48.82965 | 2025-10-04 05:06:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 758989bc-5be6-3929-aede-76265b2b9866 | -13.54818 | -47.24686 | 2025-10-04 05:06:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e879da46-2405-3a05-8a55-2c2f343c28aa | -13.24847 | -48.49588 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56ea8b85-0f45-388b-be24-12510b2c3fe8 | -14.72668 | -48.07677 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8543084-66db-34f1-ad80-558ae3b0f1d8 | -15.31353 | -46.37895 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e58ab0aa-bc25-3a4a-9666-1368e4f74b5f | -14.57795 | -52.49211 | 2025-10-04 05:06:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da2cbe5c-79f8-3980-938c-5d02116ad218 | -14.94287 | -46.85723 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d4d5d752-f3db-36d6-8352-b8f620a07698 | -13.39081 | -47.55134 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 053d225e-64e6-3db4-aec6-9b35b162002f | -11.92291 | -46.38465 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ec922861-bd06-3a33-bc5e-f53399ab4abf | -11.13507 | -47.86146 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b76dcb1-a410-31c7-a9f6-aa0809c5f24d | -14.92064 | -46.89582 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07f5f3bf-84c6-3d09-ace5-e1f6359d0708 | -15.53254 | -46.84204 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 78a5feed-8d8e-3c10-a18f-a09e4814ba32 | -15.66539 | -48.14341 | 2025-10-04 05:06:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebba9377-9c63-3d2c-b3cf-a055319ac7c5 | -11.49455 | -44.99436 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2a70e4d3-e443-3920-9be7-635ab5a0697a | -13.39049 | -47.54921 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 65e77102-839f-3c1a-9df4-48b160674e0d | -13.08553 | -48.12431 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22fd1ac9-f854-3c98-ab4d-33d7c444921b | -16.04115 | -50.93763 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 698c6f3c-24d4-3218-90e7-f6854612a21d | -16.36736 | -49.40329 | 2025-10-04 05:06:00 | NOAA-21 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbcef47c-9d35-3cfa-bc2b-9657e309a1f4 | -15.32725 | -47.33307 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da314140-49a7-3dc5-bac2-d9a542c4df10 | -12.27489 | -55.12373 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7895538-0fc1-3394-9b94-4d57dd2d96c6 | -9.44819 | -56.65668 | 2025-10-04 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 709b7889-a2e2-3f45-a909-d183087e4a61 | -13.33395 | -50.95001 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 91655c8a-2d1b-3fe2-839b-55be1b2951ac | -15.03556 | -56.04711 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 02201416-def3-3ebe-be49-4381f813969b | -11.79737 | -48.92136 | 2025-10-04 05:06:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20c985b1-a9d0-3eb7-a6be-53c14b9b9663 | -11.11493 | -47.89454 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 791615e3-94a6-3cf4-acdb-163d400c83db | -11.49515 | -46.74889 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fb979a9-6cfc-3655-8811-dc36ae232b7d | -11.91395 | -46.36008 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82fcefbc-f8e3-3f61-9f80-c59f633d7724 | -12.91713 | -54.73339 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 395a2381-f94e-3edf-8ab7-56282ad1f38d | -13.88992 | -46.51621 | 2025-10-04 05:06:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 313d6d99-cf64-3ff1-872c-aea2edecc99f | -11.91974 | -46.35275 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59276a79-7f0e-3da7-b647-5e1082941ed7 | -13.31202 | -48.13923 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba514418-3c7f-388d-94fc-c2ef72a796d7 | -10.33665 | -51.21386 | 2025-10-04 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| acf798ba-1248-3924-851c-1934f3c16c8b | -13.5746 | -48.18138 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0b6591e-a902-367a-a330-437248486ed3 | -10.42012 | -50.66887 | 2025-10-04 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 67835f22-1651-3d1d-af56-bd00234b546d | -15.22788 | -56.8215 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README112.md)
