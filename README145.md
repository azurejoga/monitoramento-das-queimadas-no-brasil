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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 831052a7-1634-36d5-8c26-4924ecc649fd | -9.48471 | -60.39339 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab961dd2-18d0-34f8-b6ed-fe0fee0bd760 | -9.48408 | -60.34939 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c30a70f-b3ac-3752-afc3-d068469c6958 | -9.48059 | -60.34887 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf0ff647-e7df-3511-9bee-0e989ff4a2af | -10.39532 | -60.70875 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77315b47-9533-345c-b82a-d28f108b170d | -11.22314 | -61.28622 | 2024-10-05 05:31:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f205d33c-ef99-3f8d-8450-e40b8562bc5f | -11.21559 | -61.21959 | 2024-10-05 05:31:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8e76123-8994-3a06-acb9-850cd3824392 | -11.20763 | -61.22606 | 2024-10-05 05:31:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7afc6175-0961-39b6-a57b-895de9d77beb | -11.2042 | -61.22553 | 2024-10-05 05:31:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26aa4170-3867-39d6-9cea-b20e3201bcda | -11.18843 | -61.28467 | 2024-10-05 05:31:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e498a372-efa9-355f-836d-223ea8a6cdcf | -11.18787 | -61.28843 | 2024-10-05 05:31:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f2c1c361-fbd2-3970-a22e-e915f7281d83 | -11.01992 | -61.42346 | 2024-10-05 05:31:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9339b13d-0518-3e43-a3fb-3eb6fbbfecd5 | -11.00296 | -61.42078 | 2024-10-05 05:31:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93c79427-39da-3b05-8a5b-933401e70574 | -10.99956 | -61.42027 | 2024-10-05 05:31:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8437dbe0-0499-3e05-9bf7-64cbcf81a3be | -10.999 | -61.42399 | 2024-10-05 05:31:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 805b5aba-bbf7-3bc5-a5d0-93b0b95e18db | -10.90837 | -61.35 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e982aed4-72e6-3817-8f0f-187c4eb37fa6 | -10.90497 | -61.34948 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c88bfbf-e7cc-36f3-b8c8-f7ee6bafa10f | -10.9044 | -61.35322 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7b414f6-98ac-3c13-bbc8-2b8ddea7c764 | -10.89249 | -61.33992 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cd1a740-a73b-3154-b348-51ee37acf58d | -10.87894 | -61.36066 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37cd9f37-9bf6-30eb-9e93-236d3e3478f8 | -10.87554 | -61.3601 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff8dbf67-797f-3070-984b-60fbf51900a9 | -10.85122 | -61.36003 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c35a358d-2957-3eac-b32b-3bf06976046a | -10.82375 | -61.39796 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07a60a76-76a2-3595-9b33-ae030cbd50af | -11.92887 | -60.40302 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d802da8e-0022-3f41-86f5-030831082bfc | -11.80249 | -60.6953 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf4e4c86-6eb1-3a50-8ed6-8b413ea78b3b | -11.79898 | -60.69476 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6290ecfa-d2b7-3e71-b016-6c3ab2446f34 | -11.68308 | -60.22431 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df5e4ccc-c4b8-3ee4-b482-e07708108099 | -11.6813 | -60.21119 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee814057-a111-3c91-a8c9-923e46d73ebe | -11.67831 | -60.20642 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abe45d70-1e49-3df9-9e63-a354956f3bef | -11.66592 | -60.20203 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eec0988f-2233-3a7a-8442-ddbe8e46e1e2 | -11.51595 | -60.15905 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 317a6193-7cc4-3f4e-b7aa-8e78a3d86652 | -11.24579 | -60.37396 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f87996ec-8eeb-3b93-aca7-f41faca0f399 | -11.3251 | -60.54946 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 673c0f3c-ef17-3f0e-929f-88aab3ec340c | -11.321 | -60.55291 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c037577b-458d-328d-a38b-37e375409618 | -11.29699 | -60.56968 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7704d7f-511b-3cf9-a847-01fe3b40d335 | -11.27829 | -60.61709 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40212af3-9f20-3bbe-b469-e63f995734d9 | -11.2725 | -60.58387 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10b4b319-4840-3b1d-a572-1d5b1602de0d | -11.26897 | -60.5834 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca8dabfc-db5d-311e-8d56-1604c87d8f87 | -11.26837 | -60.58743 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a248671-93d9-36d0-a97c-7ec5aa478b04 | -11.26606 | -60.57886 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a8aed08d-f380-3abc-b386-9a9e7eff859a | -11.26546 | -60.5829 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a372705-a8b5-3820-b3b6-434812d8e369 | -11.26486 | -60.58693 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 75cd9998-5ccd-3527-af30-fec3d4a0b663 | -11.26255 | -60.57833 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4223445c-dc85-392e-9a3c-f275121b744a | -11.26195 | -60.58235 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4703b359-82de-3349-8a71-2feea9437cd5 | -11.26135 | -60.58638 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04dbc8cc-b832-37c3-b339-36dd080d2a65 | -11.25845 | -60.58176 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3329a6c3-e6c4-3d49-aef7-c6910551959a | -11.25786 | -60.58574 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb89f68a-c25f-3a39-a046-30ec6279fef6 | -11.25227 | -60.37923 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ee192b7-5336-3ec0-85a0-833295119b5d | -11.25045 | -60.46548 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00221abb-3285-37f6-9877-3cbc26e3028e | -11.24932 | -60.37459 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0447dbd-a5a6-3779-bc64-19dbc0ee5543 | -11.24874 | -60.37859 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35fe9e1b-0ff2-3366-8dd2-89c611c31282 | -11.24817 | -60.38251 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44d387be-a15e-3af9-9b48-929208f09bb1 | -11.24745 | -60.48594 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3533082f-4f5f-3758-bb20-0fa282537be4 | -11.24735 | -60.58397 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9363d687-d230-3a7c-931e-8f91c8d32033 | -11.24692 | -60.46495 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7219612-2c7b-3cd3-9840-057dbb701175 | -11.24685 | -60.49001 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 782dd744-decb-307d-a1cd-9b93c0b4e0fb | -11.24676 | -60.58792 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c1f7476-32a4-3341-b2ea-fdc06514a922 | -11.24638 | -60.36994 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a76ef97e-05ae-3634-9405-0af4aad46b2e | -11.24632 | -60.46907 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c3beca8-45dd-38d9-a5bc-c4b187696059 | -11.24385 | -60.58336 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 879ce054-6a73-3edc-acd1-1a9e72e8ebd5 | -11.24334 | -60.48934 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 489ad89e-789b-3907-971d-1c99bab18973 | -11.24285 | -60.36932 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fba615c7-9481-3d57-9871-4cbc3d7e0a64 | -11.24035 | -60.58273 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 759a9b33-238b-368f-803f-2e6d89c33b7b | -11.23335 | -60.60581 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 266141a0-4eee-3ec6-a4c0-428d46f033fc | -11.20875 | -60.5041 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5389ad11-7df0-3a90-ac62-d3729f044e29 | -11.20522 | -60.50359 | 2024-10-05 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 444a7d31-8cf0-3b3b-b862-43d47bd66cf3 | -11.17557 | -60.65786 | 2024-10-05 05:31:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 094dd72f-f193-3107-90a8-1bb1e791e79c | -10.91286 | -60.92653 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b31be05-d646-3c59-8efe-61146f60429c | -10.91211 | -60.92561 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f734e9a-71f0-3f88-b71e-1ee0f3a355c5 | -10.91154 | -60.92946 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ad717e3-8bea-3401-92b7-bdd1b85d7850 | -12.56376 | -60.91028 | 2024-10-05 05:31:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0928800-6c92-3579-8602-be2ff76bf5d5 | -12.56208 | -60.67243 | 2024-10-05 05:31:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f88f4abb-2be0-35e5-b038-74a35005ac91 | -13.42641 | -61.92586 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 726471f1-3c02-3e8f-9cb6-57eb081c8cdb | -13.42301 | -61.92533 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0b7db129-3d3d-3f52-bb87-aadc237d049a | -13.41285 | -61.94675 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5427c0d-716d-3c68-b8af-f0f303191c12 | -13.41229 | -61.9505 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87269c59-301b-3cf0-82b3-084ecce43473 | -13.41225 | -61.92749 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a9edfa46-5c93-38c7-a3c2-1a944f242db9 | -13.41169 | -61.93123 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87708918-09e1-3374-ae77-78ce5137d834 | -13.41113 | -61.93497 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91b56a73-b2fc-3bc0-ae43-051392945be0 | -13.41002 | -61.94247 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1494f779-24a2-3cde-bab4-ad38c6e29d05 | -13.40946 | -61.94622 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9a70720-9ba3-379c-b7b0-1dc9569730ff | -13.4089 | -61.94997 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33f1397d-9001-30e9-a3bd-6191f2f67a78 | -13.40834 | -61.95372 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d24b4e0-a451-363e-9992-177fe10afae3 | -13.40662 | -61.94194 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f895585a-de68-38cc-86ef-8ecf9d965384 | -13.40606 | -61.94569 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5db2c46-d009-35d8-9197-f28e387a4358 | -13.4055 | -61.94944 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8501d991-ab12-3664-a4fd-4b42009175a2 | -13.40494 | -61.95318 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d57bb623-e153-360f-a15b-ee0915735fbd | -13.40326 | -61.96441 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3182829b-15db-3fa7-a326-0c7b22ce7ce0 | -13.40322 | -61.94141 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3f88c78-8b10-359d-9a29-d9b84d124dba | -13.39759 | -61.95585 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d3d73b07-f367-3384-9d13-8f5347212efa | -13.39703 | -61.95959 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8301be48-855d-350e-a1b3-1a800f1b62a3 | -13.39363 | -61.95906 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f4d9c4f-de82-31ed-ae66-288dc82e2631 | -13.39135 | -61.95105 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7ed185c5-bca9-30d6-ba81-e15c7bc23386 | -13.39079 | -61.95479 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d97822f3-e7ae-37c8-a865-83e56c241a4b | -13.38851 | -61.94677 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 446599ac-e535-3806-8933-8864692e43b3 | -13.38567 | -61.94249 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ece6d98-fed6-3139-912d-ff9eb202f568 | -13.38511 | -61.94624 | 2024-10-05 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3066320c-ce16-37c8-be6f-b7288fd620ee | -9.17882 | -62.29681 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 048bff7b-9dc1-305a-aef0-a585b994a03b | -9.17855 | -61.57604 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bdef91fa-4e1d-3a9b-b07f-d97371a52a48 | -9.17828 | -62.30029 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31852cb1-d801-3cbb-971d-603c277080c1 | -9.17606 | -62.2928 | 2024-10-05 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README146.md)
