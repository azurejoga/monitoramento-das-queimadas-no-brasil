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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81c7fd0b-9b08-3a3a-bc35-123209084b7e | -16.9717 | -56.7646 | 2024-10-06 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.5 |
| 971ae4a4-3b68-3715-9335-03e0abde6000 | -17.1375 | -57.4221 | 2024-10-06 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 6f5c0089-5a11-3868-b882-138cb4e9ee79 | -17.8323 | -53.7616 | 2024-10-06 04:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 7710e04f-8f83-3364-88e6-8864e5792340 | -17.8319 | -53.7829 | 2024-10-06 04:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 90fe02b3-c762-3abf-a142-d4aa50caf7ea | -17.8125 | -53.7645 | 2024-10-06 04:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 985ad16f-0e7d-348a-938e-7f6123e4d7b6 | -17.812 | -53.7859 | 2024-10-06 04:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 162.5 |
| dcd32a17-58cb-32e2-8429-cddca8b57214 | -18.659 | -57.2552 | 2024-10-06 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 4005eda1-a50e-3a0c-b873-f1df889e39f1 | -18.6586 | -57.2759 | 2024-10-06 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.2 |
| 74c8fb08-a61d-374e-95fb-969bb286ec57 | -18.6391 | -57.2578 | 2024-10-06 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 652d18a4-0553-33e4-a69b-2c92584e55e0 | -18.6387 | -57.2785 | 2024-10-06 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 196.1 |
| 36515701-59e6-3e70-86cf-627d29d3de43 | -20.5118 | -47.485 | 2024-10-06 04:06:59 | GOES-16 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 64.9 |
| be8efc00-7998-3aa0-a8ba-6dd768933a9d | -2.7981 | -48.6873 | 2024-10-06 04:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| b772d45b-fe49-3a93-9b33-4df54b3685e2 | -2.8166 | -48.6867 | 2024-10-06 04:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| a2667ed3-be3e-3111-a12f-b5cf2d4014aa | -2.847 | -50.4648 | 2024-10-06 04:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| aff9535a-e923-3aa8-8d7e-50fbd67ec54e | -3.1129 | -48.6131 | 2024-10-06 04:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| f7c6842c-40ee-3847-bef6-d2c23439e4b6 | -3.1314 | -48.6125 | 2024-10-06 04:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| bb235432-f892-3abc-b1ea-582360643b8d | -3.1315 | -48.591 | 2024-10-06 04:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| e469cbef-750a-34b0-85c9-8a79ce6d8a0a | -3.3084 | -50.451 | 2024-10-06 04:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 9379fd81-bed1-3d24-9716-1697bf7e3ce2 | -3.4195 | -50.3844 | 2024-10-06 04:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4bb40589-e7ce-38de-857e-6bf9b2dc9fa9 | -5.0139 | -49.7696 | 2024-10-06 04:15:34 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 8f87c604-1443-381f-9c5d-d40afa0197b9 | -6.9514 | -59.0666 | 2024-10-06 04:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| af67f7bb-710d-36c0-808f-29c8d0689643 | -8.3882 | -46.3006 | 2024-10-06 04:15:53 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 1a94b0ce-69de-3948-800d-2a548fdd2c31 | -8.3885 | -46.2782 | 2024-10-06 04:15:53 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 2be18bcc-c127-3feb-b2a6-7f880aad6eb3 | -8.4073 | -46.2763 | 2024-10-06 04:15:53 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 94f3c063-107c-33c9-9050-afcc27bf9d32 | -9.3278 | -46.5385 | 2024-10-06 04:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 83db5a9f-c5af-375b-b7ff-6832edbe0696 | -9.3464 | -46.5589 | 2024-10-06 04:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| d333da38-8328-3adc-a92e-d250fb14fd80 | -9.3467 | -46.5365 | 2024-10-06 04:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 202.9 |
| d2bcea75-3f28-370a-9634-ed1ed131592a | -9.6778 | -64.6457 | 2024-10-06 04:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 844c32d9-89d9-3909-9174-2b5d07f460e0 | -9.6779 | -64.6269 | 2024-10-06 04:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 16195fd1-2089-306a-b0c6-137e21da07be | -9.6965 | -64.6262 | 2024-10-06 04:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 508e4c83-bfad-3792-a6e4-68543991509e | -12.6089 | -53.1338 | 2024-10-06 04:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| de3791bb-4931-30ad-bd6d-bb2ab9718242 | -12.6092 | -53.1129 | 2024-10-06 04:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 46f1e490-5ad9-3a3b-bb1b-3640d8c044a7 | -12.628 | -53.1317 | 2024-10-06 04:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 5680e5e0-18ca-363e-88a4-e06a0d7ee93f | -12.6283 | -53.1108 | 2024-10-06 04:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 1744fe16-5271-3cd6-9b50-a82264cee79a | -12.763 | -50.5352 | 2024-10-06 04:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 72032984-259d-3b2f-88b9-ce1e56f166ea | -12.7634 | -50.5136 | 2024-10-06 04:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 50535b1c-1527-3947-99dc-a9a4b4018362 | -12.7822 | -50.5328 | 2024-10-06 04:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9bb08c77-abd4-3797-a148-c32d7c57af4c | -13.3786 | -61.9582 | 2024-10-06 04:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 9bf2adb8-8ab3-36b6-b118-5a9dcde8319f | -13.3976 | -61.957 | 2024-10-06 04:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| e0dce5f4-1639-3066-b6fe-eab12659c821 | -13.6724 | -51.1911 | 2024-10-06 04:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 655f6dda-a006-3023-859d-3c4818b6980e | -16.3764 | -57.3663 | 2024-10-06 04:16:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 2f2b3456-7fca-30c8-a977-583e4b4cad93 | -16.5544 | -57.2032 | 2024-10-06 04:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.5 |
| 25eee518-b3a7-31a8-aa20-cce40147f9e8 | -16.554 | -57.2237 | 2024-10-06 04:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 3becc462-65d2-34cf-a88c-8755c6c4c514 | -16.8238 | -57.4584 | 2024-10-06 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.7 |
| 048815e0-10a1-3382-8d2a-332965f29aca | -16.9717 | -56.7646 | 2024-10-06 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.1 |
| 842d406d-3699-3911-b7e3-1ce95a84d5a9 | -17.0003 | -55.0817 | 2024-10-06 04:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 205f7744-f11d-33a4-93a0-3850b9ac2788 | -17.0007 | -55.0607 | 2024-10-06 04:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 48ef1e6f-0c51-3b7a-b6a1-45a5462414b8 | -17.001 | -55.0398 | 2024-10-06 04:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 72c1737c-c91e-323b-a968-82cd0b002a80 | -16.9907 | -56.8034 | 2024-10-06 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 32fc7ccd-8668-3a1d-b446-2ee8d561c47a | -17.02 | -55.0791 | 2024-10-06 04:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 46d86fd8-0f40-385c-98b2-860f351cc930 | -17.0203 | -55.0581 | 2024-10-06 04:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 242.2 |
| eb214d8f-f5af-3a3d-92aa-df79ddab4c56 | -17.0207 | -55.0371 | 2024-10-06 04:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 128.1 |
| f6aff046-ce8f-350d-925e-784f9fcc7688 | -17.01 | -56.8217 | 2024-10-06 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| b12db80f-afe7-331c-add8-960310ea1f98 | -17.0885 | -56.8122 | 2024-10-06 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| a751c2c1-ad7f-3f3d-95c9-ed4d718733b7 | -17.1182 | -57.4039 | 2024-10-06 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| e8e2da36-dc83-34be-ad0f-8613ccde6a4d | -17.1185 | -57.3834 | 2024-10-06 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 16960f15-a9b3-35d8-a738-ee2a7bf56cc7 | -17.1571 | -57.4198 | 2024-10-06 04:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| aa7b3464-64cf-3c92-97a3-647e9861f6a8 | -17.1375 | -57.4221 | 2024-10-06 04:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.2 |
| ee54562a-acfb-38d8-8e97-dee2df05eaa7 | -17.812 | -53.7859 | 2024-10-06 04:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 12e9e0c6-e913-312b-a2c4-8e89fe968a84 | -17.8319 | -53.7829 | 2024-10-06 04:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| b8f582a4-755e-3500-9f6d-2920172b726d | -18.6387 | -57.2785 | 2024-10-06 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.1 |
| 57847fce-35f3-3de0-a817-cc4600dc29f1 | -18.6586 | -57.2759 | 2024-10-06 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 18135cd0-1ff3-3a89-a336-1cdbdf96f696 | -18.659 | -57.2552 | 2024-10-06 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 48c4342c-8c78-3c5e-8827-d4518fe170b2 | -20.5603 | -49.4139 | 2024-10-06 04:17:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ccf7f4df-8967-3672-8c62-c089cc140536 | -20.5609 | -49.3909 | 2024-10-06 04:17:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 111.2 |
| a8baf74e-da3a-311e-adce-98398ffd2b54 | -20.5807 | -49.4095 | 2024-10-06 04:17:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 262.3 |
| 07ce13ea-31b5-3498-97ef-d867dae96eff | -20.5813 | -49.3865 | 2024-10-06 04:17:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 477.4 |
| c86ff24d-267a-3961-a6b7-6317b57e4ea2 | -20.582 | -49.3635 | 2024-10-06 04:17:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 02edc710-64f1-34e5-ab68-4098ca243fdf | -20.6018 | -49.3821 | 2024-10-06 04:17:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 30cb266f-95cf-37a6-8b49-add2d1cf2111 | -5.11197 | -56.26298 | 2024-10-06 04:17:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2827086-8ecf-3564-993e-a83f6a25320b | -5.11103 | -56.26815 | 2024-10-06 04:17:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a595aa97-7cb2-3e5d-86b2-3f1a63a73c36 | -9.88037 | -36.38863 | 2024-10-06 04:17:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 134cb2b0-8b15-30e1-b653-48501c6ae110 | -9.87565 | -36.38683 | 2024-10-06 04:17:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b9af6025-1d28-3922-93db-38b53c4db9f4 | -9.87521 | -36.39013 | 2024-10-06 04:17:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3bf0f929-76c2-3dbb-ae2c-4c1e92a02fa3 | -9.87509 | -36.38793 | 2024-10-06 04:17:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 59f745f4-940a-3c63-b90e-001bc3aec2f3 | -7.73836 | -37.97195 | 2024-10-06 04:17:00 | NOAA-20 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4d3277fa-f43b-3617-b1ea-832b682388f6 | -7.73796 | -37.97386 | 2024-10-06 04:17:00 | NOAA-20 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc5944cd-25ad-3adb-ab78-34208d9fab82 | -7.24234 | -38.54435 | 2024-10-06 04:17:00 | NOAA-20 | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cc00c7d2-ec77-370a-8a5a-3e0bb9d091e1 | -7.23859 | -38.53926 | 2024-10-06 04:17:00 | NOAA-20 | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1307109c-3993-3dd5-84b8-5cf54ed1ec7d | -7.23798 | -38.54363 | 2024-10-06 04:17:00 | NOAA-20 | MONTE HOREBE | PARAÍBA | Brasil | 2509602 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 771322f6-50ea-3125-8187-69f5f6a3a8bd | -7.36833 | -39.17949 | 2024-10-06 04:17:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fd615fe8-5828-39ea-81c7-57f0d445b458 | -7.3451 | -39.15656 | 2024-10-06 04:17:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 08ec78aa-4ba2-3dc7-aeb5-825307be49bb | -7.34451 | -39.16054 | 2024-10-06 04:17:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 76172586-26e9-3536-8177-c9ee869686f1 | -7.34394 | -39.16441 | 2024-10-06 04:17:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6752b9f5-ad8d-3ea8-8034-fe0bf76097f1 | -6.87218 | -39.20355 | 2024-10-06 04:17:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ff40c5eb-ef3c-3e3a-8e1b-060f2c44b68e | -9.32497 | -40.69112 | 2024-10-06 04:17:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 20d81ad8-40aa-3f58-be5e-cc8c93c5f650 | -8.76419 | -40.58187 | 2024-10-06 04:17:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b2b9f84-a93d-301b-ab07-57e93198d3cd | -8.7641 | -40.58376 | 2024-10-06 04:17:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ee4bbd16-146a-34ba-b38d-e68ef24e7cd8 | -8.49941 | -40.55934 | 2024-10-06 04:17:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b0f439fc-c153-353a-ab24-a42db82f88da | -8.49265 | -40.57848 | 2024-10-06 04:17:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51cbea41-2523-3e57-ac8b-fc1a2ba0542d | -8.48333 | -40.69718 | 2024-10-06 04:17:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d84eaa4b-178b-3ee4-a1d4-7c1a67260bf7 | -8.33758 | -40.62864 | 2024-10-06 04:17:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9e9018c8-5ccf-3fa1-a6d6-e57d77e730c2 | -8.33662 | -40.62719 | 2024-10-06 04:17:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 15ce83dd-98a1-3e58-8276-a1a128b523fe | -8.20386 | -40.72633 | 2024-10-06 04:17:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 26a0cbdd-062e-32f0-8b87-2aaefadb136f | -8.20207 | -40.72338 | 2024-10-06 04:17:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 30f5a095-9edb-3fa5-b8a4-5e2c6c8d6a5c | -8.00318 | -40.5902 | 2024-10-06 04:17:00 | NOAA-20 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 765b1268-b86e-3008-9da8-0da459a80e9f | -8.00121 | -40.59233 | 2024-10-06 04:17:00 | NOAA-20 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 043b9db7-1a97-36b8-9ac6-0dd136a2d1e8 | -3.32006 | -40.007 | 2024-10-06 04:17:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b3b4c22-f98f-3d55-8116-b25f5c249764 | -6.27371 | -41.86014 | 2024-10-06 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0af486b9-b819-302a-b567-d3b8350d5a59 | -6.2731 | -41.86411 | 2024-10-06 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README63.md)
