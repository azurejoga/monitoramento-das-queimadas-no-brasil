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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45921324-6347-3047-9be6-f7007a2db3a1 | -15.47152 | -59.42812 | 2025-01-16 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33216388-c5ed-33e1-8e1f-973003c194df | -16.11041 | -58.18226 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2f57df62-9283-3e42-8b1e-f7ba8f717010 | -15.5461 | -59.41393 | 2025-01-16 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ac4ddea-54c7-3a6d-8d31-b963159331dd | -21.58597 | -57.19449 | 2025-01-16 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09e3a4ab-910c-3608-ae8f-2d8416cca4eb | -17.33394 | -53.77149 | 2025-01-16 05:01:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76d25e70-b349-3a35-83e3-1f0fdde4d5d1 | -16.11318 | -58.18661 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| edbe9800-6dec-3d5d-8ac6-4b882e1284a5 | -19.51116 | -55.31641 | 2025-01-16 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1306c9eb-5e45-3980-992a-2830879148c5 | -16.11626 | -58.16775 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4b8f1d9e-1e6e-30a0-8c34-21e8b1fc59f7 | -17.34021 | -53.77478 | 2025-01-16 05:01:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a648f67e-34e9-3250-969c-cb7ca9197378 | -16.11534 | -58.19476 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fd1a68ad-4624-3289-8828-fbe689701eb8 | -16.11442 | -58.17907 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7e7b17cf-6ff0-394f-9ed2-f98c63b239de | -16.11965 | -58.16833 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ad88ebb0-e682-323d-a706-bdb4aa5ef948 | -17.90465 | -54.53878 | 2025-01-16 05:01:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bfd4ac3-cab5-3a48-8cca-5f9ebdcaca4f | -16.11873 | -58.19534 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 4479be80-2fd5-3467-bfb7-5dfdc27cdb9a | -19.50831 | -55.31195 | 2025-01-16 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 9cbb7070-ed84-3615-9af1-943df3b0dba2 | -16.06582 | -58.47599 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 79c81780-3819-3c44-ae97-977726415960 | -16.10713 | -60.04748 | 2025-01-16 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 989d1629-8a89-3cf9-89f0-ce1bdf70e1a0 | -16.11903 | -58.17211 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9c9694b2-7452-3e6f-9406-7af444183503 | -17.3375 | -53.772 | 2025-01-16 05:01:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ccf8e38-eabe-3b04-904f-c3d5b1176505 | -15.38749 | -57.42695 | 2025-01-16 05:01:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26b95f6e-3448-3259-be0f-8abea75cd8ff | -28.50376 | -50.93346 | 2025-01-16 05:03:00 | NOAA-21 | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 994cd2f5-a1b7-3876-a2ae-262aaacc4017 | -25.60629 | -51.5676 | 2025-01-16 05:03:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5658dfc4-15e4-3797-8764-dcfdc0830950 | -30.11198 | -57.35061 | 2025-01-16 05:03:00 | NOAA-21 | BARRA DO QUARAÍ | RIO GRANDE DO SUL | Brasil | 4301875 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 870bb9dd-135b-3474-8289-55d5614f9c1b | 2.1767 | -61.8534 | 2025-01-16 05:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 36.4 |
| b88384fb-c2d1-3c34-a296-7a9dc6155e2b | -16.1115 | -58.1868 | 2025-01-16 05:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 6cac448f-10cd-3a23-9680-13bbeafe03d9 | 4.28828 | -60.11917 | 2025-01-16 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87a92520-1363-3878-867d-be35c1a42167 | 4.14586 | -60.03575 | 2025-01-16 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 386d9d7d-012c-3427-a985-f93ab167ce39 | 4.2661 | -60.29302 | 2025-01-16 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 67fca6c7-f549-3a2c-9ed3-ecdbc3fee4fe | 4.28886 | -60.12285 | 2025-01-16 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 776b53d8-2ddd-378e-a264-05e9fe7f523d | 4.39845 | -60.52077 | 2025-01-16 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c16a325c-0d17-3b17-9be8-18342c42ae4a | 4.41656 | -60.59232 | 2025-01-16 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd7d7784-f5e1-31ea-87d5-294e2fd5f98c | 4.2701 | -60.29609 | 2025-01-16 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dacec7a2-9afc-31c6-8d3b-09bfbda49113 | 4.26953 | -60.2924 | 2025-01-16 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 07a59f80-37e0-3e75-b240-eb283f5a4986 | 4.4125 | -60.58912 | 2025-01-16 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36caf420-4bce-30e1-856d-b228a3ff1828 | 4.29343 | -60.12966 | 2025-01-16 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be7d9974-8d27-3d60-9cf8-41f5e4e6e1f2 | 2.15894 | -61.85744 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4de49088-8927-3005-a629-a5816bf0681f | 1.32543 | -60.03804 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ba12fe5-f36e-31c4-a2fd-147a47ebcf07 | 0.84542 | -59.5444 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ccecba96-ae3e-32a3-89fa-dc9279efada8 | 2.53672 | -60.59158 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8079e081-af79-374e-a2e6-a0a8576bfed5 | 0.70837 | -60.00446 | 2025-01-16 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04310a78-b9d9-3ad7-a231-30bb4c49639c | 2.53963 | -60.59158 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0f16ea42-0b95-31cb-9ce6-900f24155b1b | 2.14155 | -61.86446 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f00a3894-f4b7-31c2-8988-f33d76e31898 | 1.17348 | -60.4924 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8746bf1-7549-3f87-b2fa-6568cd3e1c62 | -1.42313 | -55.31188 | 2025-01-16 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d91eac78-c0fb-3d70-8d98-d05510a83e40 | 0.84815 | -60.55291 | 2025-01-16 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77d3ed09-7d2f-3e4e-a12a-499b45ad752c | 3.14275 | -60.70014 | 2025-01-16 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b002472-74a3-3199-9d21-4042e6558d05 | 0.99662 | -59.60617 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5a14395-7a76-3150-96d5-ba1087d0e7ad | 0.84487 | -59.54094 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dab243ae-9891-31bc-b2d5-86c4f7cfa6c2 | 1.03631 | -59.49001 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 812f7c64-7e98-3399-ba6f-53c3abc04a39 | 0.96597 | -59.47614 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2128e4f3-9e21-3a43-a507-acf47b631769 | 3.13929 | -60.70069 | 2025-01-16 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebf5ebfd-ff15-36ae-9dbc-53328568ef47 | 0.63689 | -59.81177 | 2025-01-16 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4819b8bf-1e14-3378-a961-2896605710c3 | 1.1797 | -60.48775 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8291e79-0e2b-3857-9d21-c21a1642fa37 | 2.14876 | -61.8633 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8ff1bbd-b116-3362-8528-000a4f67c9b6 | 0.92282 | -59.80264 | 2025-01-16 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 351dee4d-e54b-3619-884f-48b09753392d | 1.63669 | -60.28179 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c46bfd2-3f7a-3a90-bfb7-9d73b121430d | 0.84209 | -59.54491 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8a3824cc-c114-3efe-a20b-8830fb9c1c6f | 2.10928 | -61.82301 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1081d28-2622-3186-a570-93cc57f760fe | 2.54016 | -60.59105 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6b725592-4704-3227-9d31-091f019a60db | 0.72334 | -60.12076 | 2025-01-16 05:22:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5db2d468-7371-35c5-8f83-1b34d86c4e58 | -0.84695 | -53.08031 | 2025-01-16 05:22:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb129ba5-785f-385c-aff5-6be51babe5b6 | 2.16255 | -61.85686 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a4f9991-284b-3054-8fe8-835b2b7b03d6 | 2.53957 | -60.58735 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1c3bf158-eb34-3ce9-b702-56c60eccdb77 | 2.18126 | -61.8582 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a0f87e4c-656c-355d-8018-dcf4aa6727eb | 0.85098 | -59.53645 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7269f50-0a4a-300b-8707-3927381bdd13 | 2.1409 | -61.86033 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c449ab3-1579-38ce-92a1-b166a93fdc07 | 2.20045 | -61.81055 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 772987e2-4969-3915-896e-c85a51b5ced1 | 2.54249 | -60.58735 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2d114cb0-0669-3e67-837d-bd234819d096 | 2.16616 | -61.85629 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a9dcb3b6-24e3-3953-bb7c-668caacbe834 | 2.53899 | -60.58365 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 98b13991-819f-311f-addb-998f44f986e1 | 2.53613 | -60.58786 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4b11a32e-6eb7-3007-bfec-bed125958045 | 1.32097 | -60.0315 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f741072-af86-3ba9-a494-404b199cafa3 | 1.93609 | -60.41252 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efcfdea3-df95-3b30-834e-017c96a43071 | 1.01448 | -59.56787 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6037942d-434c-3a78-8d96-96cd7253a738 | 0.99549 | -60.55999 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a17fa56a-d644-37c4-841a-ddfcb89dca54 | -1.68603 | -54.45397 | 2025-01-16 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6b6cb07-4ef3-35c0-9def-8f8a7ec5ef1c | 0.55665 | -59.68533 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 20ec1c5f-1f03-31bc-9456-cad3b5efde26 | 2.17338 | -61.85518 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 251e3b2c-3b81-39a8-9b5d-e69a6096226d | 0.67774 | -59.98411 | 2025-01-16 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ab2a24f-9edf-3a1a-859f-e5080dd7f050 | 1.17574 | -60.48466 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74832ec4-8d07-3367-8bc2-cd73ae2666ee | 3.21151 | -60.58172 | 2025-01-16 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db2af59f-53f9-3067-a4aa-3fbbb7eac2d0 | 1.17066 | -60.49653 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3a3802f-d268-387f-be53-6892aa529067 | 1.32208 | -60.03857 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f910564d-890a-3a3b-8296-92b338d9e952 | 0.83805 | -60.26893 | 2025-01-16 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39eb37c6-83f7-3c8c-90fa-a6f35b431afe | 1.12458 | -59.4267 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d11a2025-4009-39dc-9f23-96184faf0eda | 3.92723 | -59.68145 | 2025-01-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9af030a-cf0a-3419-a99e-c33c557f1938 | 1.93834 | -60.40472 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07aa7205-e122-373a-a4bc-3957055b89f1 | 2.2017 | -61.81871 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62ee09f9-bbdd-3e04-b33f-c3022ce3bcde | 2.15958 | -61.86153 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b0738df-39ce-3b40-9e0a-ee52fc0ba925 | 3.54329 | -60.04227 | 2025-01-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b3af191-f64f-39ba-bed8-e628514ba7ea | 2.22061 | -55.83318 | 2025-01-16 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf997685-af69-35a2-97d3-a47b94fdd654 | 2.08944 | -61.84589 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad2325d9-8d18-3509-a3c0-cbcfc257855b | 2.17042 | -61.85984 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 89d9934c-c177-37a0-9380-1838d2472545 | 3.73429 | -59.72168 | 2025-01-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcf93356-2497-3116-8bd4-2ecb9750617a | 2.20107 | -61.81465 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 985d6b7f-61a7-3cac-af06-e5267b445f74 | 2.53555 | -60.58415 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fd3d092e-f4d2-320f-98c5-645dcedf0bee | 2.53906 | -60.58787 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| be5adc04-e64c-3870-9135-c8ffb3eead64 | 2.5402 | -60.59529 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 61511ec7-0905-3378-8e4f-e6fdd152c4ec | 2.15598 | -61.86213 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 989e0464-1050-3fba-91a7-673f1003bf50 | 3.82746 | -59.71497 | 2025-01-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README5.md)
