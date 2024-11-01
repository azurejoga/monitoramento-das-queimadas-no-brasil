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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eca5b6f1-78fb-343f-8bc6-1835a9be86dd | -17.6664 | -57.5028 | 2024-11-01 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.5 |
| 0a0bd15e-f62a-3d32-b3fe-25e28cfb0a2e | -17.6667 | -57.4822 | 2024-11-01 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 051fdc18-d59d-37ce-a97f-1050e40bc7d5 | -19.4878 | -56.6227 | 2024-11-01 01:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 181d4b01-4858-33e0-bf0d-fcdb308b0794 | -19.4882 | -56.6017 | 2024-11-01 01:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 0968e251-2144-356a-a050-82383a4a34ff | -19.5083 | -56.5989 | 2024-11-01 01:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.8 |
| bb2943cd-c10d-328e-8ff5-e1bd055f51b7 | -19.5087 | -56.5779 | 2024-11-01 01:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| a2e3f2f7-4a5e-3eb9-99b2-8b11ee0d39c7 | -19.4886 | -56.5807 | 2024-11-01 01:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 2f4186a9-cba9-3a44-b546-3c4ffa1447b0 | -19.5079 | -56.6199 | 2024-11-01 01:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| daebb517-af20-3cd6-913a-8b1e185b2961 | -1.8654 | -52.3282 | 2024-11-01 01:35:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b16cc94a-f3e1-3dcb-ba09-4bc7804fb4b7 | -1.8654 | -52.3077 | 2024-11-01 01:35:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| d1493f74-f51c-3634-8894-bde3b5ecc64f | -2.1695 | -48.7252 | 2024-11-01 01:35:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| bc107e0f-6b07-3ad8-8d67-e1bc23610a44 | -2.188 | -48.7248 | 2024-11-01 01:35:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| c4cd3926-ab8d-3bac-b061-ea8f324a6cb5 | -3.0354 | -49.4688 | 2024-11-01 01:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 49efedc0-3bdd-3723-adb1-803caf5061d1 | -3.0538 | -49.4895 | 2024-11-01 01:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 251.4 |
| eeb7d7cb-1a0e-3711-b0c4-8b97a42be502 | -3.0539 | -49.4683 | 2024-11-01 01:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 211.9 |
| 1e379ba6-0427-325d-8595-d91663b3c1ef | -3.0723 | -49.4889 | 2024-11-01 01:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c00e1293-d23a-30ea-bb48-7247e960fd64 | -3.0353 | -49.4901 | 2024-11-01 01:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 206.0 |
| 826f2b20-0367-3103-aba1-83a018817abd | -3.5446 | -47.3855 | 2024-11-01 01:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| eb431d86-859b-3475-b532-b75e76a94d48 | -3.563 | -47.4066 | 2024-11-01 01:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 9077c827-1a25-38a3-962c-4eac6234d4d7 | -3.5631 | -47.3847 | 2024-11-01 01:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 342.6 |
| 00f29446-8d9a-3b21-90b3-a8f3f02732e4 | -3.5632 | -47.3629 | 2024-11-01 01:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 09f6ff60-25d8-3363-a013-d0bc84ea82c9 | -4.3867 | -43.4757 | 2024-11-01 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 220.5 |
| e7fc10d6-cb6d-3d9c-b566-a366ce5bc64c | -4.3869 | -43.4525 | 2024-11-01 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 3d7aeaf6-ad9b-3b5e-9865-838973b918de | -4.4054 | -43.4746 | 2024-11-01 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 5b57c10b-785f-39dd-8abd-317e503ad755 | -4.4056 | -43.4514 | 2024-11-01 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c29c9cf4-3deb-3a9c-8d47-cc59d32fef01 | -4.5394 | -45.7019 | 2024-11-01 01:35:32 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c5c28a7f-3ce3-388a-9ca8-3ac89378bcd8 | -4.8067 | -44.8061 | 2024-11-01 01:35:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 8c519f93-48fc-3973-91d0-950f787ba00a | -6.1039 | -43.9824 | 2024-11-01 01:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 721bb8b0-f789-3334-bade-4d6b3c5d2a87 | -6.1041 | -43.9593 | 2024-11-01 01:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 156.6 |
| f9509b2f-b165-329d-b40e-a8ab57d9f3c2 | -6.1043 | -43.9362 | 2024-11-01 01:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 8c9dc492-d7d3-3f12-a012-468e3c76300d | -6.1226 | -43.9809 | 2024-11-01 01:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 06febe48-77d3-3880-b89a-d7a85bd06a2d | -6.1229 | -43.9578 | 2024-11-01 01:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 232.5 |
| bb69ec9e-f5ab-335d-a9e8-d1445954f986 | -6.1231 | -43.9347 | 2024-11-01 01:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| a616da63-e805-34eb-a28f-8d94ef720ad7 | -9.4391 | -40.3171 | 2024-11-01 01:35:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 866ee705-f789-3f09-b39e-93e3719faaba | -10.2762 | -36.3327 | 2024-11-01 01:36:03 | GOES-16 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 111.9 |
| dd708df6-eb82-3380-9471-be7f3640e851 | -10.2768 | -36.3057 | 2024-11-01 01:36:03 | GOES-16 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 125.9 |
| f05d3c46-8aad-36a9-9130-1c5cce9cf8bf | -10.1071 | -68.3823 | 2024-11-01 01:36:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 2f9e27a3-ec74-3114-8380-56d6928d805d | -10.682 | -64.9831 | 2024-11-01 01:36:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 95d58258-d8df-3c0f-9f12-345822803d0f | -17.6467 | -57.5051 | 2024-11-01 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 1338c7f6-1654-3080-895f-715ca0ed769b | -17.6661 | -57.5233 | 2024-11-01 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 581735e9-294a-3558-9c64-3c5b7ba98a33 | -17.6664 | -57.5028 | 2024-11-01 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.6 |
| 5934bea4-f25b-3937-9868-7374690cb25d | -17.6667 | -57.4822 | 2024-11-01 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 5ce8205e-53d6-3a59-a8f5-6090ad7b6703 | -19.4878 | -56.6227 | 2024-11-01 01:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 9670a29d-c9af-3504-854b-5a07c4d26240 | -19.4882 | -56.6017 | 2024-11-01 01:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.9 |
| 98f8f47c-1581-35d3-acf9-e630523d301a | -19.5079 | -56.6199 | 2024-11-01 01:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 20a1ecc2-4bfc-38dd-a26f-1488d69af129 | -19.5083 | -56.5989 | 2024-11-01 01:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.6 |
| cb027f59-6f98-3860-81ff-512e30a92c88 | -2.1695 | -48.7252 | 2024-11-01 01:45:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| b34a211a-00e5-31d8-82df-dc7099ce3194 | -2.188 | -48.7248 | 2024-11-01 01:45:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| c03fd941-1322-3570-8a94-2f9872f7d331 | -3.0539 | -49.4683 | 2024-11-01 01:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 5724d7f5-a265-3f56-8981-8f16c3fcba5d | -3.0538 | -49.4895 | 2024-11-01 01:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 085797f5-5220-38fc-a233-e704a49f9f27 | -3.0353 | -49.4901 | 2024-11-01 01:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| dfd8b5fe-4323-3138-8c01-d372adfefce1 | -3.0354 | -49.4688 | 2024-11-01 01:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| a974e806-0f64-3c1b-ac18-acb78821f5bf | -3.5817 | -47.384 | 2024-11-01 01:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 977b3312-505b-38c8-8fac-c7a0221beaa0 | -3.5632 | -47.3629 | 2024-11-01 01:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 0664d5bd-1ed5-3b45-a84b-66188ff6c1a7 | -3.5631 | -47.3847 | 2024-11-01 01:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 294.7 |
| 631912c4-1cd9-3336-babb-1766d9a62d18 | -3.563 | -47.4066 | 2024-11-01 01:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 9f2d7143-3d98-36b0-bd45-abe844b17aad | -3.5446 | -47.3855 | 2024-11-01 01:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| e80f5bff-d9e3-367c-92d8-e2147f2c88fb | -4.3867 | -43.4757 | 2024-11-01 01:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 229.1 |
| 05c87546-e3dd-3285-a1f4-a5cb8c11c1c8 | -4.3869 | -43.4525 | 2024-11-01 01:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| e0f7b1e3-6c43-3b00-95b9-e4f311d6b222 | -4.4054 | -43.4746 | 2024-11-01 01:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 4ec22a65-6b34-39a0-86f7-fbd7e0f7a6a9 | -4.4056 | -43.4514 | 2024-11-01 01:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 22cbce69-29c5-3e42-837e-1c873b7d04b2 | -4.5394 | -45.7019 | 2024-11-01 01:45:32 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4d7c5dae-a0f7-3c85-a5b6-6834b517d65a | -6.1039 | -43.9824 | 2024-11-01 01:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c5d3c71e-9132-30de-bf02-7d66df665538 | -6.1041 | -43.9593 | 2024-11-01 01:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 43f6939b-8784-3a04-9b90-93f7ba456792 | -6.1226 | -43.9809 | 2024-11-01 01:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 840223dc-2d6f-34dc-a3ca-4c0f6c459b33 | -6.1229 | -43.9578 | 2024-11-01 01:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 224.3 |
| d40721fd-bfcb-31c6-af6c-41e8ea4cdb9f | -19.4878 | -56.6227 | 2024-11-01 01:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 2fcc6193-3152-3ca3-b6db-cc9a5d2df99b | -19.4882 | -56.6017 | 2024-11-01 01:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 46829234-9aa0-3aa8-95d7-ce5a32754d37 | -19.5079 | -56.6199 | 2024-11-01 01:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 6e95da95-ceb3-3a89-b01e-1ff7e3a2eddc | -19.5083 | -56.5989 | 2024-11-01 01:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 9c7e1edb-b444-30df-ab47-3046de3a7721 | -19.5087 | -56.5779 | 2024-11-01 01:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| a0ccfc8f-dabb-303d-a882-b92fec7aa212 | -2.1695 | -48.7252 | 2024-11-01 01:55:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c669319c-ba9c-379b-b7c6-38a5ceea9b54 | -2.3545 | -48.678 | 2024-11-01 01:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 92306a48-935c-351c-80e8-9e1a3e42408e | -3.0353 | -49.4901 | 2024-11-01 01:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 7408da14-f47d-3c6d-83b7-ead2ba6a625f | -3.0354 | -49.4688 | 2024-11-01 01:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 47b69ab4-fdcd-3104-8f97-252abd5f9cda | -3.0538 | -49.4895 | 2024-11-01 01:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 172.1 |
| 3faa63e2-107d-3519-af6a-220a8ef5605b | -3.0539 | -49.4683 | 2024-11-01 01:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 50f4f1a4-cf7f-3d29-ab14-4bc8a4f84a48 | -3.5446 | -47.3855 | 2024-11-01 01:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| e289a4d0-a2fc-3255-a65c-70491e0c976d | -3.563 | -47.4066 | 2024-11-01 01:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 1b0bd761-8dbc-35bb-8280-5b1664a6dc89 | -3.5631 | -47.3847 | 2024-11-01 01:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 259.2 |
| 07207d4b-4554-3f25-a671-b03b2f06b587 | -3.5632 | -47.3629 | 2024-11-01 01:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| c7849765-760a-35ff-854b-08827a48cd15 | -4.3867 | -43.4757 | 2024-11-01 01:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 7c30f34d-44d8-39bc-a9d4-b340575e5ab8 | -4.3869 | -43.4525 | 2024-11-01 01:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| d10d6eb9-a067-33e6-a3b3-6739b3c12f7b | -4.4054 | -43.4746 | 2024-11-01 01:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 250.4 |
| 6586cc5c-0746-30c1-8b1f-2eb5d85c27fd | -4.4056 | -43.4514 | 2024-11-01 01:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| e1594a6d-b636-3070-b44c-531afe72d349 | -6.1041 | -43.9593 | 2024-11-01 01:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| dfe73651-9052-3b13-be54-09772f214f85 | -6.1226 | -43.9809 | 2024-11-01 01:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 492a9954-ecfc-3243-a4f7-ac7335ddbe9b | -6.1229 | -43.9578 | 2024-11-01 01:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 92ffcda4-bf73-3542-ba8d-016a0b0f0fcd | -6.1039 | -43.9824 | 2024-11-01 01:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 16b7c355-b734-36d7-bf2b-a7d99c3e0ca9 | -9.8923 | -36.2668 | 2024-11-01 01:56:01 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| 397f8cc8-cdf2-3ad0-93f7-4aef993c9276 | -9.9116 | -36.2634 | 2024-11-01 01:56:01 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 100.1 |
| dbf45124-044f-33ed-acb5-c52b317ab765 | -16.9008 | -57.5313 | 2024-11-01 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 7e4af10d-9ff8-3021-9267-a346310f77a5 | -16.9012 | -57.5108 | 2024-11-01 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| c1143d3d-6fcd-33a9-a8f4-74ff937f56c9 | -17.6467 | -57.5051 | 2024-11-01 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.0 |
| 84a91d7c-b702-3dfd-a327-e8a3fff4f34d | -17.6664 | -57.5028 | 2024-11-01 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| b79f728c-7e6a-39a9-adc7-9109a87767e2 | -17.6667 | -57.4822 | 2024-11-01 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.3 |
| d84b836f-8b7b-3e4d-a165-31e443f235b8 | -19.4878 | -56.6227 | 2024-11-01 01:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 58693b36-a5ba-3899-949c-2bf3efda4c43 | -19.4882 | -56.6017 | 2024-11-01 01:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 54d4fd43-8ae0-32c9-a439-00b4dbf05805 | -19.5079 | -56.6199 | 2024-11-01 01:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 398bc69c-7257-3eca-8c88-8c252715e874 | -19.5083 | -56.5989 | 2024-11-01 01:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.6 |


[Clique aqui para ver as próximas entradas](README8.md)
