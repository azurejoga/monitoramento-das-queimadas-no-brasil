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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05887cd8-cbdf-3402-9da0-82de07151c97 | -8.9787 | -60.5156 | 2026-08-16 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 503304b1-8055-3b08-86e1-66260a7f0a1b | -12.0095 | -46.4271 | 2026-08-16 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| c1d7a72f-2a52-31ae-ba2d-e3cb4f5cb371 | -6.85465 | -58.96962 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 4b4eb20f-9a52-3e05-955c-4c5049ffc274 | -12.00906 | -46.46849 | 2026-08-16 07:09:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 746b38e7-5f61-335d-b2bb-d6c1150ef5a4 | -8.6524 | -54.72385 | 2026-08-16 07:09:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 18860b56-9168-396e-93d3-fd9d0427adc2 | -6.71207 | -58.92639 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| e8bfb62b-ba01-3c14-99b3-f2b7591ccbc0 | -11.99924 | -46.45926 | 2026-08-16 07:09:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 68ab8e8b-2113-3756-91f8-69dabb018558 | -11.32911 | -46.2122 | 2026-08-16 07:09:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| f7be0c4b-5001-38e4-bc43-e5b6d20fc8dd | -6.6226 | -59.05313 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| b6039f0a-3ba7-342a-ab80-6079676ce775 | -6.69648 | -58.9528 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 49e6953c-b3f0-3be3-83ea-5fe1fd78e980 | -6.10608 | -57.72294 | 2026-08-16 07:09:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 277ee6f3-ea66-366f-a672-fb49560c69fb | -12.01269 | -46.43765 | 2026-08-16 07:09:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 392.6 |
| 1be153cf-65e5-38c8-9d83-b0cdd74a4a33 | -10.27689 | -48.28215 | 2026-08-16 07:09:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| d550b960-2dea-33b1-ac36-469b59dd3711 | -6.86556 | -56.41525 | 2026-08-16 07:09:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a439c6e7-76a3-32f5-9168-03b8db1f315c | -6.63135 | -59.06958 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 5ab8493e-97d5-38ff-9396-486c6cede8fa | -8.9827 | -60.50716 | 2026-08-16 07:09:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 47b20c35-12b2-3737-a898-08d428b54e73 | -8.95593 | -60.52043 | 2026-08-16 07:09:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 798f1ef8-89d8-3416-b577-e68abfc05116 | -6.97561 | -59.01626 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 317c3510-2cb4-30ca-9880-6535c4ea7332 | -6.10796 | -57.71102 | 2026-08-16 07:09:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e70b1a97-bab2-34ac-9b88-56ee9a049190 | -2.96159 | -49.25394 | 2026-08-16 07:09:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8bde5378-334f-34c4-9e2d-1e52ccbd6c1c | -10.27318 | -48.28922 | 2026-08-16 07:09:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 8f746965-c01c-3abc-aabd-8e9dfec6fedf | -8.64231 | -54.71567 | 2026-08-16 07:09:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4ec97400-54f1-37f0-93ab-6ab9d10c047e | -6.61225 | -58.97698 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ebe2416d-f3b5-376d-8740-3e507b392831 | -11.06493 | -47.27227 | 2026-08-16 07:09:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 8d7ababb-d3a3-3bb2-846b-da91be952b7c | -8.89611 | -60.54089 | 2026-08-16 07:09:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b6acbc0b-bb42-3bd7-901e-408d96d57d47 | -6.10422 | -57.73477 | 2026-08-16 07:09:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 45199990-d137-31b8-89d5-619c1f29b077 | -8.64364 | -54.70688 | 2026-08-16 07:09:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8c9d35fc-4966-38c1-8c6b-c3dae3b38430 | -11.21606 | -54.81507 | 2026-08-16 07:09:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0de65a99-c72f-3cd2-b4b5-ad90297606b6 | -6.70744 | -58.95477 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9d2983bc-2d62-3cfb-94a8-6140c894d59e | -6.83323 | -56.44046 | 2026-08-16 07:09:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ff9ea1b8-f707-3539-a93f-2ec6be2ea2d4 | -10.27407 | -48.30354 | 2026-08-16 07:09:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| e1e8c097-0fdb-3090-bbe1-3021667e2dc8 | -6.84403 | -56.432 | 2026-08-16 07:09:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 56cfa157-c5ce-34c4-8f9c-5b3728ed2c72 | -11.57842 | -54.68348 | 2026-08-16 07:09:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 295b33e3-76c2-38da-b693-b496ac6bc598 | -6.59717 | -58.98384 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a2121278-ddc8-341d-891b-92d374bdf5d4 | -6.82244 | -56.44887 | 2026-08-16 07:09:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 4200d099-6251-3164-9123-4e85df52b125 | -11.07658 | -47.26868 | 2026-08-16 07:09:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 6f3e5ca1-409b-3de1-83b1-f342eddcd924 | -6.82088 | -56.45873 | 2026-08-16 07:09:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f4ab53a7-92bb-3f48-b70e-f2081704262f | -6.09596 | -57.72137 | 2026-08-16 07:09:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bb32235e-21aa-397e-bdaf-162262872b26 | -6.72304 | -58.9281 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9f0cf0a0-0887-345f-ac2e-8d0ef7dfda44 | -8.97076 | -60.50524 | 2026-08-16 07:09:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 44de7ce2-3726-3d76-a8b1-c3db158d5d8b | -6.84367 | -58.96787 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0bb98946-9f9a-31b4-99d7-a1780b471587 | -6.9639 | -59.29921 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4a62af4c-53cb-3472-8bca-436245b7ed81 | -8.89949 | -60.59523 | 2026-08-16 07:09:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| cd42f1ff-87ae-3397-8c1c-19c0eddf10db | -6.62023 | -59.06782 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 486e054a-c56b-326c-9c29-898220c8a149 | -8.97984 | -60.52437 | 2026-08-16 07:09:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 1cb036ac-5c9a-3ff2-b2b7-f0a9d67f49c9 | -8.96788 | -60.52241 | 2026-08-16 07:09:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fd6cd281-bb80-3a67-aa2d-59d47a5a74be | -8.59987 | -54.70031 | 2026-08-16 07:09:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 49602404-b1e4-310a-9a1b-553d652d2f9b | -11.20727 | -54.81374 | 2026-08-16 07:09:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2baa2f5b-d0b0-3bd0-bc16-b1f543a2f9a5 | -2.95961 | -49.26738 | 2026-08-16 07:09:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 0f7323a7-0667-30af-8057-cc1b6cddf53e | -6.70975 | -58.94059 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 301f0738-3db7-310b-8290-e34925525903 | -12.00309 | -46.42818 | 2026-08-16 07:09:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| e6228312-9c15-3727-907c-49167a862db8 | -9.30092 | -56.81208 | 2026-08-16 07:09:00 | AQUA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e40d9524-9e5b-320f-b7ac-c4cbf588a92f | -8.89321 | -60.55839 | 2026-08-16 07:09:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 6370e31f-84b7-3377-8d36-4192a7afbbb4 | -6.69398 | -58.96049 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9c297628-d99c-301a-a73a-97109bfe73e3 | -7.3415 | -59.59657 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| c2d2f0d6-7b39-333e-a60b-99d915c9a078 | -6.86404 | -56.42507 | 2026-08-16 07:09:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f450a887-6409-3c5f-9d9a-1539f6e9d9b1 | -6.69625 | -58.94597 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 32b5cec7-dbb4-3c8e-be40-701c237ad4b5 | -6.69882 | -58.93852 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 487f8da5-2961-3445-adbc-23d3b77a1bcf | -8.43259 | -62.67194 | 2026-08-16 07:09:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| b9ecc2e1-9caf-37e7-aff2-8444a6eb1bc0 | -6.59884 | -58.98972 | 2026-08-16 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 19b2c00e-ce35-3494-8df4-79e9e9e6e041 | -8.90235 | -60.57784 | 2026-08-16 07:09:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d2504b98-98fe-34ee-9a72-2d536ab1a5af | -6.1108 | -57.7035 | 2026-08-16 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 9eba5b23-a5b5-303b-b50a-e80d4b9ac715 | -6.3137 | -43.6178 | 2026-08-16 07:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d20f8cd7-b70b-3a7f-9a35-5d63405afcfa | -8.96 | -60.5358 | 2026-08-16 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 17fccf2a-81d3-3ca6-b106-4fafaf5e8fdb | -12.0091 | -46.4498 | 2026-08-16 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 05aa71ab-6d8a-352b-876a-7a8f39444777 | -12.0095 | -46.4271 | 2026-08-16 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| bd3360c1-418d-3ca1-9492-1cda70054e85 | -8.9787 | -60.5156 | 2026-08-16 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c07ed2ea-c6fa-31ee-86a1-064035c243ec | -8.9601 | -60.5165 | 2026-08-16 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 347a7882-c015-3d80-a0c2-fd525ad462bb | -6.1107 | -57.723 | 2026-08-16 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| c5ecd0c6-5991-3742-96da-c16e460f9149 | -6.7123 | -58.9412 | 2026-08-16 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 42dce7e2-cc4a-398e-a350-de326886148d | -14.901 | -46.6283 | 2026-08-16 07:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 4173acdb-e6ea-3062-9b27-e04f804ea028 | -12.0286 | -46.4244 | 2026-08-16 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 566e37fd-c6d6-31aa-866d-a52a40d36ff0 | -12.0282 | -46.4471 | 2026-08-16 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 2fff918e-b29a-3b74-9302-fd679f6f71c2 | -14.9005 | -46.6512 | 2026-08-16 07:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| bbe465f2-83e1-3982-9b5b-d8623500ebd6 | -12.7017 | -48.4753 | 2026-08-16 07:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 40bc34ca-748b-3c6a-ad4d-03ca832948d7 | -12.66926 | -48.43891 | 2026-08-16 07:12:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 3c407729-fb8b-373b-a667-9da3144b5bd6 | -15.02887 | -52.69384 | 2026-08-16 07:12:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ca8690b7-0766-310b-a73a-ca4a8ef39f4b | -15.07598 | -47.00406 | 2026-08-16 07:12:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 46.6 |
| b3b6c20d-d60e-380b-ae52-9f79c1be2da5 | -15.06497 | -46.9977 | 2026-08-16 07:12:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 32cc2c7a-7624-3ecc-aa48-2aa55abb50f9 | -16.33427 | -55.37792 | 2026-08-16 07:12:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6c26f155-77a0-3546-a56c-f7d9d33af544 | -14.88091 | -46.65326 | 2026-08-16 07:12:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 114b4007-b14c-33b9-a7ab-9f76d636b2f6 | -13.79858 | -53.82543 | 2026-08-16 07:12:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 78d4b505-3f60-311a-b986-27801d108c61 | -15.02892 | -52.69924 | 2026-08-16 07:12:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 88ea69a3-1c48-37b3-85d6-2bb4ac181213 | -14.89245 | -46.62671 | 2026-08-16 07:12:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 133.4 |
| bd1937b7-6c4a-3b70-b1cd-88412c159a63 | -15.03053 | -52.68752 | 2026-08-16 07:12:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e6317f08-7144-37e3-b63f-8a8c9d84e8c7 | -12.71561 | -48.47454 | 2026-08-16 07:12:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 7ef9ef45-909b-3a15-8fb4-96189561d555 | -12.70684 | -48.46806 | 2026-08-16 07:12:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 39c2dacf-d528-3109-8101-85b1c8351ed1 | -20.33578 | -46.72368 | 2026-08-16 07:12:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 7b19fa09-322a-3408-acb6-140757c3f652 | -13.79499 | -53.78399 | 2026-08-16 07:12:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 942b6259-3f94-3a42-bf0d-63ce205681a3 | -17.77039 | -49.48088 | 2026-08-16 07:12:00 | AQUA_M-M | JOVIÂNIA | GOIÁS | Brasil | 5212105 | 52 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 497f566e-6811-33a9-bcb2-7c33e8470188 | -20.33231 | -46.71843 | 2026-08-16 07:12:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 122101a0-d9af-33e4-ac39-2d96439bf3bf | -15.13578 | -50.04549 | 2026-08-16 07:12:00 | AQUA_M-M | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| d991c7bc-2615-377a-8be2-17b10e7648b0 | -12.70413 | -48.48977 | 2026-08-16 07:12:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| c09b568c-0b57-3648-9671-ed03959bf05f | -14.88883 | -46.66005 | 2026-08-16 07:12:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| ebd430e8-1545-3aea-b606-61bd11697990 | -12.0 | -46.46 | 2026-08-16 07:15:00 | MSG-03 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 099502e2-407c-37b9-bcf6-28bde35388b0 | -6.3137 | -43.6178 | 2026-08-16 07:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 58c7f526-6cec-3d8c-af48-ea62c974aa81 | -12.0282 | -46.4471 | 2026-08-16 07:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 229.6 |
| dc8d9083-b01a-324a-84bb-ea010b7110d0 | -6.1107 | -57.723 | 2026-08-16 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c43b8992-dc93-3cea-8012-5b72826308ce | -8.9601 | -60.5165 | 2026-08-16 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 64c7f73f-3d6c-39e7-a2ee-7fd32e5dc333 | -12.0286 | -46.4244 | 2026-08-16 07:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |


[Clique aqui para ver as próximas entradas](README58.md)
