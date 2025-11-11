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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 052aab88-3a13-3260-bf35-290701a0578d | -19.79044 | -58.02723 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 237e7f18-cd0c-331e-8090-49013f2b166b | -26.61268 | -53.16274 | 2025-11-11 04:55:00 | NOAA-21 | SANTA TEREZINHA DO PROGRESSO | SANTA CATARINA | Brasil | 4215687 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d8b88729-408a-3ea4-8ade-d096f549c838 | -19.76063 | -58.01326 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4f4fc882-9cc4-3d5d-91d8-4208a4666549 | -19.79737 | -58.02854 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 6dac5998-d5e7-363c-8d67-35218855a33f | -16.68183 | -51.83376 | 2025-11-11 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dab131af-a276-379d-b94f-e872ff12337b | -19.7551 | -58.02471 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cc89c59f-255d-3ac4-814b-ce68fe0f8857 | -21.77049 | -55.94545 | 2025-11-11 04:55:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9345a9e9-55b3-36c0-adc5-b231866a3f98 | -15.55746 | -55.24383 | 2025-11-11 04:55:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15c5f2c9-091a-3ba5-95e7-329fb5093a9e | -19.81122 | -58.03117 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 62091ee7-9ddd-32ea-9d5b-66ff6aa930d7 | -21.42432 | -47.67545 | 2025-11-11 04:55:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 42151e1c-c9e6-37b7-bf8b-a42dfc01124b | -23.59882 | -49.00929 | 2025-11-11 04:55:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f466876d-8fc2-3304-81c7-45ac7364976a | -19.79112 | -58.02319 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 94eb5688-b918-38a4-80de-efb7c61cbc92 | -21.28073 | -54.15382 | 2025-11-11 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8c51ae0e-4d02-3783-b1a0-77747ed3568a | -19.81669 | -58.03112 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 3fadd67b-6a8c-3340-bc39-e21eeba601fd | -15.58132 | -56.01924 | 2025-11-11 04:55:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9610a0c-e5bd-30e1-9a9c-38c5707ef6fb | -19.80083 | -58.0292 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 3aa3c2e0-1f79-3498-997d-9623c66ca452 | -22.68009 | -50.44466 | 2025-11-11 04:55:00 | NOAA-21 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 21ffc1da-5396-3463-9778-87039e9ca735 | -19.80776 | -58.03051 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 47f9695e-9f3f-3917-8555-0782f27ef879 | -22.98142 | -47.24125 | 2025-11-11 04:55:00 | NOAA-21 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b46d3ffd-453b-39e3-ad26-8455d9ca66ea | -19.75579 | -58.02068 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 532ac4b2-c771-3700-b9a1-f1c71cbcb806 | -19.75926 | -58.02133 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e0475a50-6917-3409-9e23-0655d7d6ef95 | -16.53314 | -52.77289 | 2025-11-11 04:55:00 | NOAA-21 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33aaaaec-370e-3831-97ca-9befcc0e83c0 | -22.03798 | -56.06097 | 2025-11-11 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f902f6eb-9a72-3928-8c3b-560530a12d8d | -19.72668 | -58.0444 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3c94df91-71dc-3eae-b733-897fde0d16b3 | -19.75995 | -58.01729 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| de2aa40c-2f03-33de-bd36-8f14b72767a2 | -19.80429 | -58.02985 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 7532a451-2e9a-3bfa-8ec7-5eaddde31e37 | -19.81323 | -58.03047 | 2025-11-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 3a11b745-e4ee-3307-ad6f-dbfcebbf3b96 | -21.12583 | -56.89497 | 2025-11-11 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62ce7232-ccc5-3f1c-8798-f98122a89bc5 | -22.03856 | -56.05726 | 2025-11-11 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34935ea2-0322-3ef5-b5a7-3a58214e72a0 | -4.7204 | -46.4497 | 2025-11-11 05:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e9d7dc77-821b-3fb1-b3d2-4f5acd2ae129 | -4.7204 | -46.4497 | 2025-11-11 05:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2ab8d0fd-a247-37f1-8d0b-0d995eb96158 | 0.72639 | -50.72632 | 2025-11-11 05:18:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9f6fa69-d6d5-3493-938d-a1a30c9821d8 | 0.27556 | -50.31417 | 2025-11-11 05:18:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e841655e-a5d1-35a5-81e6-3cd1ab20c9dd | 3.53333 | -51.77579 | 2025-11-11 05:18:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 092cda76-2b6d-3281-a066-a77d03fea3b5 | 2.96068 | -51.42535 | 2025-11-11 05:18:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9048b011-e430-3dd5-ab67-00a554bdc2f5 | 0.28025 | -50.31347 | 2025-11-11 05:18:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e02e798-7ca4-32ed-b5da-6a9b495f3c94 | 2.96421 | -51.42093 | 2025-11-11 05:18:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ce07349-b572-3388-8b34-62deabc0b055 | 0.27877 | -50.31525 | 2025-11-11 05:18:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10b0bcb7-3ab8-360f-b78f-a41d353f9bdc | 3.53735 | -51.77512 | 2025-11-11 05:18:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47bea338-b7b8-3938-ad8a-3455b14237e1 | 2.96483 | -51.42468 | 2025-11-11 05:18:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9a50da5-53e1-349e-8cae-ae3c94cf30db | -2.15456 | -50.70107 | 2025-11-11 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a0710377-b47b-3127-8ec7-256dd6a7f006 | -4.72087 | -46.45119 | 2025-11-11 05:20:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b48b4eeb-eb2c-35fe-a0c5-c1ce988a1520 | -1.64225 | -52.04785 | 2025-11-11 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0f7901f5-1270-32ae-afba-febf40fb6f0b | -4.74096 | -49.52933 | 2025-11-11 05:20:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbf9685b-af52-3f8c-930f-f58e37cac1d1 | -4.20674 | -50.63233 | 2025-11-11 05:20:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33d98f76-247e-3fec-8150-80171fad22ea | -4.87254 | -46.6899 | 2025-11-11 05:20:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0601180-f5b4-36dc-8b44-b1d0a9b6d8f2 | -3.46946 | -59.28586 | 2025-11-11 05:20:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a4d97f8-7076-32c8-9aad-ba9645335722 | -4.20486 | -50.63517 | 2025-11-11 05:20:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faa903e2-bd83-3c3e-bf61-799969c2c42d | -3.809 | -46.00503 | 2025-11-11 05:20:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3374ffab-00c4-3c01-8ee6-34612216e4bb | -2.90209 | -54.181 | 2025-11-11 05:20:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44017669-363f-304a-bf4d-7acca5f57124 | -2.15477 | -50.70773 | 2025-11-11 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5412842-adc2-3000-967b-812770bf4b5c | -4.86513 | -46.68803 | 2025-11-11 05:20:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 440b8348-8524-3f8b-9aaf-c8751f922df3 | -2.606 | -49.2268 | 2025-11-11 05:20:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c21609e2-8632-3a09-a9b6-2af5ce3c3a6b | -3.63922 | -44.62468 | 2025-11-11 05:20:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c2e2267-2058-3768-8eda-d7ca42e0e2b2 | -3.55611 | -55.47841 | 2025-11-11 05:20:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97c1c88f-7058-3da9-951d-7f073e6af5ae | -4.25662 | -48.5838 | 2025-11-11 05:20:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87589034-4452-31d3-9c25-ba952bb9434c | -2.10003 | -56.6352 | 2025-11-11 05:20:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9562160e-6126-3403-9f88-c4020f5de527 | -4.72013 | -46.45646 | 2025-11-11 05:20:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 29e5dd2a-66a9-3ecb-a96b-3b1b227b167f | -2.49231 | -50.25452 | 2025-11-11 05:20:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ceee4ed8-1341-31ef-920e-c526dbc87217 | -1.42178 | -55.40959 | 2025-11-11 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d6ccefaf-6c84-3fc8-b633-940d2b5cba23 | -3.76103 | -60.30724 | 2025-11-11 05:20:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| abfc5e36-9db3-3f31-8310-89c298c41405 | -3.81282 | -46.00586 | 2025-11-11 05:20:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c889f83-3cd6-3943-a5ad-3e0f74fe8f83 | -2.92277 | -54.19831 | 2025-11-11 05:20:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86247d13-2590-3450-85fb-1a348cbdcfd1 | -1.41828 | -55.40902 | 2025-11-11 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ff724bd-0922-3430-b06b-f95d6b28b110 | -2.90241 | -54.18316 | 2025-11-11 05:20:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df1c5e06-5b23-36cf-a610-7d5c14ff7b2e | -4.25155 | -48.57903 | 2025-11-11 05:20:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb3dda8d-96cf-3026-810e-dc041b26d022 | -4.25098 | -48.58288 | 2025-11-11 05:20:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9d8fed2-6b4c-3ebf-94d9-cba05c7a5595 | -3.59322 | -55.46637 | 2025-11-11 05:20:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2eb23fe-5c25-3025-b3e0-f35d2f9ee9ca | -2.8683 | -45.42998 | 2025-11-11 05:20:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 521ab52a-f196-3401-8434-47d0cd8ec60f | -4.13783 | -50.64722 | 2025-11-11 05:20:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 253faf20-e232-3eb3-8fc3-c5e049216dbc | -1.48934 | -60.23037 | 2025-11-11 05:20:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf1e1140-21a9-3094-9a24-c6bdd6011bc4 | -2.09891 | -56.64236 | 2025-11-11 05:20:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c15c1d9-ac67-340a-a072-9d1607b85837 | -2.71932 | -48.349 | 2025-11-11 05:20:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c531d610-11a9-3894-b649-60f02a6968cf | -3.5926 | -55.47042 | 2025-11-11 05:20:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9493c7f8-1f6b-34d7-b8ea-4a038c301c9f | -4.86614 | -46.68876 | 2025-11-11 05:20:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3898281-19df-3c05-9ccc-73d2f171fd67 | -3.2149 | -45.27645 | 2025-11-11 05:20:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 01b76852-1ca0-3308-a87f-4a880399ab01 | -2.60551 | -49.23003 | 2025-11-11 05:20:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9745ee0a-e701-3cf1-aca1-01c96aca4d91 | -2.72197 | -48.34534 | 2025-11-11 05:20:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 905f48c3-553f-3e71-be52-2600b727e612 | -2.49148 | -50.25996 | 2025-11-11 05:20:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 666a23c7-7305-3ca4-a812-5afeebef0f0a | -1.64164 | -52.05185 | 2025-11-11 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f8da8f0d-5ab8-3d11-8145-033c2872fe9d | -3.55968 | -55.47896 | 2025-11-11 05:20:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6771b536-b844-389b-a405-aae7beb5c95c | -2.15553 | -50.70272 | 2025-11-11 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5fddced2-8af2-3106-b22f-e9f018faf705 | -2.65504 | -52.07973 | 2025-11-11 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7a36b1d-e5b2-3c3e-a1fb-6ceda025b485 | -4.73565 | -49.52831 | 2025-11-11 05:20:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f18971f-8a9e-359a-9075-beeb27698db2 | -4.87151 | -46.68931 | 2025-11-11 05:20:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5db7d95-113f-32e0-b12d-b89bb08917e9 | -3.80623 | -46.0047 | 2025-11-11 05:20:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe5abebe-add8-33a2-a164-48c3b76d25c7 | -2.87506 | -45.43102 | 2025-11-11 05:20:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4562df17-a911-3ceb-9bd0-974340bd3add | -2.86918 | -45.42402 | 2025-11-11 05:20:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d235129a-bd44-3fd7-9f52-68021b51a9ba | -2.10229 | -56.64288 | 2025-11-11 05:20:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2b48e7f-59ee-3ff3-b349-27ff5b359eb2 | -2.09947 | -56.63878 | 2025-11-11 05:20:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba1b2d07-09f4-3947-a82d-7e534c64477d | -2.83652 | -59.24391 | 2025-11-11 05:20:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 569ae486-5fed-308b-a848-8fbd030674cd | -3.59384 | -55.46232 | 2025-11-11 05:20:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f87662e5-1fce-3937-baef-2babd066c317 | -2.69225 | -59.425 | 2025-11-11 05:20:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7317af8-b037-3c8a-9c48-b7a45875c4b2 | -3.22546 | -61.24017 | 2025-11-11 05:20:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73638dbd-e67d-3507-9a1c-b7332806347b | -4.71448 | -46.44985 | 2025-11-11 05:20:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6c81b93-6886-30a1-938d-aab6f29d15bc | -1.94299 | -52.00872 | 2025-11-11 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cee0d398-c8f7-3e23-9d62-ed5d79133e85 | -2.72138 | -48.34913 | 2025-11-11 05:20:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1aebd2b9-800c-3dab-90ce-475e3d2a6ae5 | -2.30789 | -56.99794 | 2025-11-11 05:20:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4fe7736d-d131-38bb-af4e-4448640ae2df | -4.20185 | -50.63149 | 2025-11-11 05:20:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2af6c84a-76f8-34c5-9277-9e50fb9ac9e0 | -3.63822 | -44.63153 | 2025-11-11 05:20:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README19.md)
