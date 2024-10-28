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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 194efe76-22c4-3b7d-b130-8957f23dfc88 | -2.2845 | -53.8023 | 2024-10-28 00:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 442fa088-852c-382a-bf5f-de044df6be4b | -2.2846 | -53.7822 | 2024-10-28 00:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 355.4 |
| faaf7a10-e1fd-3dd1-851b-2d1e46437843 | -2.2846 | -53.762 | 2024-10-28 00:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 30691649-79f3-3b07-988c-6091221fd840 | -2.3919 | -48.5484 | 2024-10-28 00:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 883a2793-1a5d-3510-ace2-ca794784550f | -2.4104 | -48.5479 | 2024-10-28 00:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e536c759-26f3-3514-b257-678b380f1753 | -2.5127 | -51.1821 | 2024-10-28 00:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 88429b55-f093-339e-9ecd-11adf16386b1 | -2.5251 | -47.442 | 2024-10-28 00:35:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| a619de79-76fe-3105-8f4c-8456806566a2 | -2.531 | -51.2024 | 2024-10-28 00:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| f4471e39-f141-3b45-88e4-602b890d784d | -2.5311 | -51.1816 | 2024-10-28 00:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 519731ca-c31e-3c8b-aecf-7485f639d582 | -2.8054 | -51.7951 | 2024-10-28 00:35:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 24ca3d9e-ca69-3e26-b000-acf0cfcb736f | -2.8372 | -53.3261 | 2024-10-28 00:35:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| e0c28ab5-cd4c-35b1-a61a-33c0da1bc11f | -2.8555 | -53.3459 | 2024-10-28 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 9bb4b1cb-7b4a-3d90-9245-b60e7f2cc27d | -2.8556 | -53.3256 | 2024-10-28 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a46ac34b-5c8e-3085-96b8-54705b1fa640 | -2.8739 | -53.3252 | 2024-10-28 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 5e91a9e6-b6dc-3395-a726-86e59f393f71 | -3.0317 | -50.4176 | 2024-10-28 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 69c96057-1da8-3ee6-b839-dc1b8109f885 | -3.0353 | -49.4901 | 2024-10-28 00:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| fd89c6e4-ebff-3e9f-a770-99ab3eb361f3 | -3.0537 | -49.5107 | 2024-10-28 00:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| ab3625f8-0676-3994-9884-9b098b755c4d | -3.0538 | -49.4895 | 2024-10-28 00:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| baceaafe-eae8-33dd-8c92-60ec5d43adb5 | -3.2719 | -46.2294 | 2024-10-28 00:35:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 3d4c1352-9919-3fba-a3e7-152aad0f38cb | -3.272 | -46.2072 | 2024-10-28 00:35:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 7f00c510-d66a-3f53-a937-cd5aa42ed37d | -3.3567 | -52.1704 | 2024-10-28 00:35:24 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| f7b5cae2-33ab-3316-ac0c-aade938a46da | -3.4013 | -46.3353 | 2024-10-28 00:35:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1d0be0d2-8c04-3166-9adb-20579a24cd6d | -3.4014 | -46.3131 | 2024-10-28 00:35:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 388c6c4a-ffee-3637-aa01-3a07a5faef01 | -3.6727 | -51.5629 | 2024-10-28 00:35:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 056ffcb1-50b0-3c56-96bf-14341a6b0586 | -3.6911 | -51.5622 | 2024-10-28 00:35:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 42d826de-d3e0-3731-8b92-eb036d939449 | -4.2797 | -45.5362 | 2024-10-28 00:35:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 2c1953b7-22d0-3f48-8a04-e496653d509f | -4.2799 | -45.5138 | 2024-10-28 00:35:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1beb648b-12f4-3e35-9bc8-c7d5048b9e6a | -4.4093 | -45.6641 | 2024-10-28 00:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 30f93dac-b995-3d87-9252-0334269ea2cd | -4.4094 | -45.6416 | 2024-10-28 00:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 181.3 |
| 8e9f129c-9b5c-3eb0-be49-d3be00dd5cd4 | -4.4279 | -45.6631 | 2024-10-28 00:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 7b1989f5-15f8-3d9a-8f6b-d0a1b81e889d | -4.428 | -45.6406 | 2024-10-28 00:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 179.0 |
| e3d4b6dd-7f17-3c02-ac6c-b6affa6533e1 | -4.7768 | -46.3801 | 2024-10-28 00:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 106.4 |
| ccc5b5cb-3564-3936-a00b-e0e085166a8f | -4.7766 | -46.4022 | 2024-10-28 00:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 135.6 |
| d0f63de7-8865-36c7-9c24-e7c46115e9ec | -4.758 | -46.4033 | 2024-10-28 00:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 24492825-6097-3ea7-8fe6-e40322c4aadd | -4.7581 | -46.3811 | 2024-10-28 00:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 858a9b2d-6edc-3eab-8999-c8abc63a2908 | -1.1836 | -53.5158 | 2024-10-28 00:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ef94482a-d26a-39a0-a464-18f292b26fbf | -1.1836 | -53.4956 | 2024-10-28 00:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| b9d6f656-9aee-317e-916b-c9875cd27c73 | -1.5349 | -52.1079 | 2024-10-28 00:45:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 82535032-dede-3bab-a20d-69d1ce7c971b | -1.5349 | -52.0874 | 2024-10-28 00:45:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 4791d572-ac8e-39a9-be09-22d8ef065bf1 | -1.5349 | -52.0668 | 2024-10-28 00:45:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| fa0a0da2-08c0-3959-8c6e-601d4904f389 | -1.5532 | -52.1076 | 2024-10-28 00:45:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| b0b6cf8a-3d83-3907-b816-81ec77181a01 | -1.5533 | -52.0871 | 2024-10-28 00:45:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 49193ad5-c7aa-3b91-9d48-739048610c9c | -1.9763 | -52.0804 | 2024-10-28 00:45:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| a9c56888-1647-382c-a661-e5877d1055d6 | -2.0499 | -52.0791 | 2024-10-28 00:45:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| fb5a66ed-abd3-3921-81fe-72daa6b037c1 | -2.2662 | -53.8027 | 2024-10-28 00:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 3b12dffe-f447-341d-bca3-bae3dff764bb | -2.2662 | -53.7825 | 2024-10-28 00:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 280.3 |
| 76d160c6-1170-32a4-aadc-2f861e189bda | -2.2663 | -53.7624 | 2024-10-28 00:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| fa9c5c16-5f84-3f77-a614-9674b62dd615 | -2.2845 | -53.8023 | 2024-10-28 00:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| e1f6c981-b016-3f85-b674-2abf5f3be754 | -2.2846 | -53.7822 | 2024-10-28 00:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 289.3 |
| 1bd1d260-bacf-340d-969d-9b3456c73d44 | -2.2846 | -53.762 | 2024-10-28 00:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 7b20e7ef-572c-3060-839b-6a28c6b74b25 | -2.3919 | -48.5484 | 2024-10-28 00:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d26210f9-d9c9-301c-8207-c6d7fccbc951 | -2.4104 | -48.5479 | 2024-10-28 00:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| deb39ce4-82a8-3c0f-99ec-e4200e4bf003 | -2.5251 | -47.442 | 2024-10-28 00:45:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 91155a1f-bcc1-3090-a737-eaf6b1fb8b20 | -2.5594 | -54.0181 | 2024-10-28 00:45:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 47c52483-7980-3263-8e51-0d217a8445aa | -2.7033 | -49.33 | 2024-10-28 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 02eff39a-6786-30fa-aaf9-8ce262fc890a | -2.7034 | -49.3088 | 2024-10-28 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 1bb9e8e6-81fe-3663-9b68-821638cb3619 | -2.7218 | -49.3295 | 2024-10-28 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 7d31c920-9892-38fd-842a-796f66efcc47 | -2.7219 | -49.3083 | 2024-10-28 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| a1258255-ca22-348a-94dd-2cb49651b1cd | -2.8054 | -51.7951 | 2024-10-28 00:45:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| bd638b5c-652b-3c67-8ae1-3b099c5421dc | -2.8372 | -53.3261 | 2024-10-28 00:45:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| f9edce85-0184-39fb-b6a4-a6d3db30a9d2 | -2.8555 | -53.3459 | 2024-10-28 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 0767ce27-c69d-38ec-b8a4-4e412ccc9f82 | -2.8556 | -53.3256 | 2024-10-28 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ad023ab6-3c4a-3213-a332-886c286e26d8 | -3.0317 | -50.4176 | 2024-10-28 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| a98eefba-a006-381b-93e7-a74f762065a7 | -3.0353 | -49.4901 | 2024-10-28 00:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| ead54943-105c-3f91-835c-115113fda16d | -3.0538 | -49.4895 | 2024-10-28 00:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 26878c3f-2087-3b9e-abb4-577a2a4e4273 | -3.2719 | -46.2294 | 2024-10-28 00:45:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 523ab587-9c31-3cba-9111-fd45ced35ef9 | -3.272 | -46.2072 | 2024-10-28 00:45:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 88a95cdb-861b-397a-b120-455c20e2c62c | -3.4014 | -46.3131 | 2024-10-28 00:45:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 07f3df3a-4e2b-32a5-be50-95842a014d3d | -3.42 | -46.3123 | 2024-10-28 00:45:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 3f6e09ac-6566-30ae-a3a0-5bd4fff1c0e5 | -3.6911 | -51.5622 | 2024-10-28 00:45:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c6312ab6-7860-3539-93c9-1baa786bad58 | -4.2797 | -45.5362 | 2024-10-28 00:45:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 4d7be12d-b926-3391-8abd-c88032ef8eb3 | -4.4093 | -45.6641 | 2024-10-28 00:45:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 85c498d3-edc9-3a65-a42b-70d2a2152953 | -4.4094 | -45.6416 | 2024-10-28 00:45:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 071facf7-6079-3b96-baa7-2f8861ce3d1f | -4.4279 | -45.6631 | 2024-10-28 00:45:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 0a2c2e22-945b-3fce-9bbb-d01ced4a2b76 | -4.428 | -45.6406 | 2024-10-28 00:45:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 226.5 |
| 60baacda-c21b-3091-a26b-4ef00504f9fd | -4.7768 | -46.3801 | 2024-10-28 00:45:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 3088252d-2302-34a2-9488-bf52e815941a | -4.758 | -46.4033 | 2024-10-28 00:45:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 462711f9-0fa5-37d0-b6c6-35a30d6cd813 | -4.7766 | -46.4022 | 2024-10-28 00:45:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 139.9 |
| c82c8db2-16ce-398e-b2d0-49aeed6c57de | -15.3686 | -40.155499 | 2024-10-28 00:45:38 | METOP-C | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8311efe-88d8-37a0-8c6d-6c57df24c602 | -15.3718 | -40.168098 | 2024-10-28 00:45:38 | METOP-C | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e5aa0305-3a91-3963-bffd-222bad46bbcc | -15.375 | -40.180698 | 2024-10-28 00:45:38 | METOP-C | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b9cc2676-22d1-3faf-96b7-37ac2e39e4ef | -15.3621 | -40.170799 | 2024-10-28 00:45:38 | METOP-C | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 994115e5-c36f-3860-bcb1-cfea2cc88be8 | -15.3653 | -40.183399 | 2024-10-28 00:45:38 | METOP-C | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f4da9252-3d19-3812-9412-657f027c331e | -15.438 | -41.127499 | 2024-10-28 00:45:40 | METOP-C | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| efded6ed-6c49-3dcb-9197-c58978c3bbbd | -15.5118 | -42.263802 | 2024-10-28 00:45:44 | METOP-C | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e6bf697d-5787-3f18-88a8-4054d8e5381e | -14.9711 | -41.875702 | 2024-10-28 00:45:51 | METOP-C | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 864f7005-2c08-3905-a1dd-5528d54656d2 | -14.5538 | -42.965199 | 2024-10-28 00:46:02 | METOP-C | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 877be007-ea1d-36fb-a82e-bcbaa0d5e40d | -14.5559 | -42.974098 | 2024-10-28 00:46:02 | METOP-C | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 672eaf7a-2222-34e9-a48c-2bb944f63e8d | -14.5581 | -42.983002 | 2024-10-28 00:46:02 | METOP-C | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e089ce4-b7fe-3e95-a4d3-d6faffe26bdd | -14.1387 | -42.9179 | 2024-10-28 00:46:08 | METOP-C | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 81aaf811-441c-3bc3-bd65-4896578ec0ab | -13.9031 | -43.442902 | 2024-10-28 00:46:14 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1dfc2708-ce3f-3de3-b875-dcd310b8164b | -13.8934 | -43.4454 | 2024-10-28 00:46:14 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20b7082f-0a2f-32f8-b115-4d817df7ecb9 | -13.5827 | -43.057701 | 2024-10-28 00:46:18 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 66649888-5077-3e50-9592-e32f94370b80 | -13.5537 | -44.320202 | 2024-10-28 00:46:23 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 832165a5-ed57-3f58-b4ed-5c89729ca04f | -13.5555 | -44.328098 | 2024-10-28 00:46:23 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 56238107-4333-373e-b342-bdcf31437d7e | -13.1754 | -42.956699 | 2024-10-28 00:46:24 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 092a6e11-25b6-3391-9cdf-16928f350031 | -13.4605 | -44.275902 | 2024-10-28 00:46:25 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d1949cd-2510-3259-8cf5-e7d5d3d8841e | -13.3316 | -44.605801 | 2024-10-28 00:46:28 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d30f160b-6aa9-3c03-b5da-9e1ffd277d0c | -13.3334 | -44.613499 | 2024-10-28 00:46:28 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d23ae857-bc54-3cc8-b7b4-6878d9016f3c | -13.042 | -43.993599 | 2024-10-28 00:46:30 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
