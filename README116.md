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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fa29949-99cf-379b-b5cd-d026240bdd2e | -17.6073 | -57.5099 | 2024-11-10 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 308.0 |
| 35843d80-1e12-3ecc-89bd-e7b02d047b5a | -3.2169 | -50.2651 | 2024-11-10 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1dbc136d-2074-31fd-9612-3af2fa58e524 | -3.1423 | -50.4352 | 2024-11-10 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 274.3 |
| f3442d1b-7f9c-3519-a241-9a73e813add1 | -17.313 | -57.4834 | 2024-11-10 04:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| f078b924-df73-3a1b-b15d-70dc3a4b6e81 | -2.7587 | -49.3497 | 2024-11-10 04:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 6697841b-7771-3398-85f8-e7fd7350e929 | -8.3967 | -44.1365 | 2024-11-10 04:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 9537dbeb-c4ff-3515-a97a-ce9fd39a2ab2 | -2.8802 | -51.4835 | 2024-11-10 04:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 39600c16-d216-3b1e-8583-3006ba4d07f9 | -8.397 | -44.1133 | 2024-11-10 04:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 6a1c4be4-c665-34d1-b69d-3e5d0f50fdbf | -3.2352 | -50.2855 | 2024-11-10 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| ba1e03d8-0259-3130-82c1-ead37198c998 | -12.433 | -64.1272 | 2024-11-10 04:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a17e2797-fad9-3b36-8d6d-92da152f28ae | -2.4365 | -46.3019 | 2024-11-10 04:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 0d005f41-48ac-32e8-9c05-cef988f9f7f2 | -3.9485 | -48.1508 | 2024-11-10 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| db65a182-9185-3b93-9854-8a80226f3847 | -2.8803 | -51.4628 | 2024-11-10 04:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a4c51dc3-3a4d-3da5-b322-4f1bd43448be | -3.2168 | -50.2861 | 2024-11-10 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| eec9f7d1-35e5-35b1-82ed-59fd7a4d6839 | -3.1239 | -50.4358 | 2024-11-10 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 669b3c89-6188-3201-a92c-996d32b1ee66 | -3.5064 | -44.0294 | 2024-11-10 04:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 5c83b496-2d2c-3caa-8127-80377366d841 | -2.9494 | -52.7748 | 2024-11-10 04:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| df40a994-cc65-3338-8b56-7993d571c135 | -3.1424 | -50.4143 | 2024-11-10 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 94d40c3f-1558-3a18-b5bd-5793c1a2317e | -2.9355 | -51.482 | 2024-11-10 04:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| dc83d51f-48e7-3e3d-8675-9601a76dc934 | -3.9668 | -48.1932 | 2024-11-10 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 8b609935-13ab-381a-b70b-d155a839fac5 | -3.2244 | -53.0524 | 2024-11-10 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| a5649576-babd-320c-bb05-70b985546d88 | -3.1238 | -50.4568 | 2024-11-10 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| b9928436-76a5-3720-a606-a6c990030c71 | -2.7772 | -49.3492 | 2024-11-10 04:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 3e4ea3c7-aad7-3678-9e79-173813e8efa9 | -3.9483 | -48.1724 | 2024-11-10 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| cdb8ee9d-6dbe-3df9-9885-b792c25a6728 | -12.4329 | -64.1462 | 2024-11-10 04:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b8fda883-8f6c-3eee-aefd-3d917cb654e0 | -11.03194 | -48.80133 | 2024-11-10 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe2d0ac0-e73b-3483-8d31-750371f0c38b | -11.87049 | -58.82016 | 2024-11-10 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d24f7fb-2a35-3bc5-a5d4-74aeb0ee6cd2 | -12.41712 | -64.13213 | 2024-11-10 04:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9916b021-ba0e-34e6-a422-8b829e0ffc02 | -11.70464 | -48.98627 | 2024-11-10 04:40:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a90e88fd-eb90-37a1-9ad8-062bb01f9e7c | -12.41524 | -64.13793 | 2024-11-10 04:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4cd05e0f-50ff-30fe-bf4b-7e49d9200fba | -12.42203 | -64.13953 | 2024-11-10 04:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e6c4e53b-98ec-3c6a-8292-cfb823b7967b | -10.42733 | -49.24331 | 2024-11-10 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04348b48-2d4b-3d8e-81ca-8958ff004fbb | -10.99886 | -49.35405 | 2024-11-10 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8be73e2-c851-3c3f-85d7-3b078eb416b6 | -13.21446 | -50.47477 | 2024-11-10 04:40:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e403f33-6c75-3b87-8169-4d305877124f | -10.39451 | -49.30032 | 2024-11-10 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 337be43f-3464-3ca9-a8ba-805e1fec3ed2 | -10.2438 | -54.96811 | 2024-11-10 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1984c910-3ba4-3533-af7a-938738f8a8b5 | -15.27022 | -57.68281 | 2024-11-10 04:40:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dfc3951f-78e4-34e8-9032-c5cf02d3d84e | -15.97902 | -56.82961 | 2024-11-10 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b72c751-d9a6-3763-9120-bf758f84a8e7 | -10.43573 | -49.2556 | 2024-11-10 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4091b075-4d65-3837-9f06-b11e2aabc66d | -12.42333 | -64.13329 | 2024-11-10 04:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9b294851-c0c8-319b-9457-f70a1bba625f | -16.06375 | -56.86911 | 2024-11-10 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b03574b3-5bdc-3431-b6eb-d5793ff14b86 | -16.02353 | -59.85265 | 2024-11-10 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7776be45-ec78-3097-a1e5-c4b94a93096d | -10.99614 | -49.01342 | 2024-11-10 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec5b71bf-5882-35c1-9ca6-6b801534dd32 | -10.13801 | -49.14687 | 2024-11-10 04:40:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78eb85bb-fb1d-3b75-bb81-fe0a7b09eade | -15.2659 | -57.68192 | 2024-11-10 04:40:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3da6e61-72e9-3136-8c1c-41f5f2201da0 | -10.9983 | -49.35764 | 2024-11-10 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3ba8917-d12b-34f7-8903-e85d75dd9e94 | -12.15631 | -48.95216 | 2024-11-10 04:40:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83cbabbf-7fc5-3cc2-9cf6-dd0c615de7c5 | -15.88691 | -56.67196 | 2024-11-10 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 351e69eb-25ab-320a-a7bb-43526cc4f993 | -14.71622 | -60.02469 | 2024-11-10 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ad622cd-324e-3fcb-88e3-3e11fd7159cf | -14.71683 | -60.0216 | 2024-11-10 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cf03f0a-ca24-3118-a2f0-9228568672f7 | -12.1529 | -48.95162 | 2024-11-10 04:40:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86fdccd2-48e1-3eb5-bb43-2ff5f6fa77cc | -16.27814 | -55.32921 | 2024-11-10 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38214986-836a-349d-8507-dcb6ebcabfd3 | -11.81693 | -49.28043 | 2024-11-10 04:40:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e104612-e83d-397d-ab77-f6625eac78ae | -12.42391 | -64.13368 | 2024-11-10 04:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 511707c6-aae0-3c35-a603-3d72890a52dc | -11.66027 | -54.04423 | 2024-11-10 04:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f7344303-3598-36af-b958-638cb8762e4f | -12.42257 | -64.1399 | 2024-11-10 04:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 8ad76bda-a889-3fb1-b99d-712a4f6d13c8 | -15.2667 | -57.67764 | 2024-11-10 04:40:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d172832a-77e9-39e4-bec6-e707978906dd | -14.72323 | -59.88256 | 2024-11-10 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 20c8520e-7a9a-3c76-9e11-f48971d382de | -11.6698 | -54.05491 | 2024-11-10 04:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0de0e380-776a-32ce-bd55-92ab0a0ac6c3 | -12.41579 | -64.13832 | 2024-11-10 04:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f8de781-815f-3511-80c7-45c48a51ebcb | -12.62237 | -48.52078 | 2024-11-10 04:40:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e5bfae5-9056-3af2-a436-e53e38961da3 | -15.56847 | -47.85569 | 2024-11-10 04:40:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18c3b4f0-d80b-3ff0-8d86-a72e50fc8f66 | -11.0291 | -48.79712 | 2024-11-10 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e370f1e-bcc4-31b0-b1f2-65b8023205e9 | -10.9955 | -49.35352 | 2024-11-10 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1fa2f7a-00c7-3a20-bd24-8ec04f2ad06e | -11.0257 | -48.79659 | 2024-11-10 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2eb93131-0541-33c4-8dbb-2bab68c00186 | -11.02626 | -48.7929 | 2024-11-10 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2356571-22ac-3926-bbec-06ed13e45746 | -11.70521 | -48.98584 | 2024-11-10 04:40:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80f42eaf-1a7a-3d56-8161-262426c192dd | -14.7213 | -60.02577 | 2024-11-10 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 791b3d4b-c169-3d71-a075-9a2c3303b03d | -12.41654 | -64.13171 | 2024-11-10 04:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6b82378c-23f6-353b-92f7-17a9c1db2c47 | -12.45743 | -46.81934 | 2024-11-10 04:40:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36f72f9e-4bb9-3b6e-a6fb-a3ea442f7e59 | -15.88289 | -56.67119 | 2024-11-10 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3bd2f90a-d685-3954-b2df-f1d2c1122545 | -14.72383 | -59.87953 | 2024-11-10 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ea66af48-7ec0-370f-a4d8-f4e11b4fa2e3 | -11.70521 | -48.98257 | 2024-11-10 04:40:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 254b60ea-9313-3e22-8c08-3d1be359da0c | -17.2801 | -57.49484 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9c3da7ca-15a4-3c47-b69f-04385cca9ed6 | -17.62339 | -57.48967 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 89802f69-0c2e-37f1-a1ef-21963a825078 | -17.29534 | -57.48187 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ab551b8f-a3e1-345b-92ef-e3ccee136784 | -17.60178 | -57.44559 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1fa1f415-930c-3fdb-8f59-107e9e043686 | -17.23663 | -57.49808 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8323ef7f-7cea-3421-8fa5-01c3dab3cbf4 | -17.2932 | -57.49348 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 4e0b4896-5b69-3743-ba61-7e8dd1d45d06 | -22.78789 | -43.75698 | 2024-11-10 04:42:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e36711c6-d681-3b64-a1bb-2dc7da808cbd | -17.30287 | -57.48742 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f27d4f63-1597-3bbb-b8fb-bdd663b11835 | -17.60233 | -57.4655 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c8b5246e-40ae-352c-9f40-e8609b9ad8df | -17.30145 | -57.49517 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 76d3bc7c-39d3-32ac-b925-7ff6fc97b330 | -16.09222 | -60.10603 | 2024-11-10 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96c91e16-0775-3ae1-92ef-f190d69463db | -17.77242 | -54.92761 | 2024-11-10 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfda0acf-2d1c-382e-a286-a39b7bca80b0 | -17.23736 | -57.4942 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e87aa4bd-c214-3d9e-a6df-9c3d71e28a2b | -17.62254 | -57.51739 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 304a5fb4-d4e4-305b-a4a1-368a5ec935ce | -17.61076 | -57.53497 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 41826a4e-a9d9-3ed9-93b8-43602befd571 | -17.61574 | -57.50801 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 65cc4c38-50b1-3263-9812-1a28dc61e9cd | -17.29804 | -57.49045 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| aef40c1f-1e66-31f9-bf18-4ff31b5efe67 | -17.25533 | -57.4898 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a3f9cbdd-ed29-32f0-9cae-e5774a53f826 | -17.29875 | -57.48658 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 33831fc2-e935-3289-a5e9-acf983015b95 | -17.61843 | -57.51654 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 2da4ff03-84ac-3d7d-9a4e-98b7c07bd1a9 | -17.61234 | -57.50333 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 884ceee4-f638-30d4-a03b-463f7a9f8864 | -17.63217 | -57.51138 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 0160de00-f2cc-3a1e-bf86-131451dbc3cf | -17.60665 | -57.53412 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 8587fa40-2e40-37db-859c-018e305e0126 | -17.61163 | -57.50718 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 12bd6377-f97a-3c69-aa91-520db8cbdd89 | -17.60162 | -57.46931 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f2ef2ab0-9ed7-3e6e-8373-49e2b308cc01 | -20.47843 | -53.67641 | 2024-11-10 04:42:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0ac5364-bcd5-34ac-8680-8c4e1ffc48e5 | -17.61886 | -57.44511 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |


[Clique aqui para ver as próximas entradas](README117.md)
