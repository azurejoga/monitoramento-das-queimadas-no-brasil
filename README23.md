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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63d87d17-6fe3-33d5-bffa-f3d43d36fc26 | -3.1282 | -54.2459 | 2024-10-16 02:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| db4f6015-5bf5-338d-951b-b9ca543eef93 | -3.1283 | -54.2259 | 2024-10-16 02:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| cd0d2662-397d-31e1-9ef7-539df26737bb | -3.2862 | -47.133 | 2024-10-16 02:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 329e38b5-ac71-3eb4-87e8-ab34d279b8b3 | -3.958 | -46.4442 | 2024-10-16 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 127.1 |
| cc198c8a-64db-36e0-8a97-5e734b0bd98a | -3.9581 | -46.422 | 2024-10-16 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 3cd394a3-7877-309c-9655-5ed6c2a7190e | -9.1728 | -65.3945 | 2024-10-16 02:45:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 1e6ff16f-82b6-3679-b8c8-b320b433ffa3 | -10.2628 | -47.3024 | 2024-10-16 02:46:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| f323393f-480d-350c-8de5-f3b5cfc58cba | -10.2439 | -47.3046 | 2024-10-16 02:46:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| bb2c2558-ff14-3967-9b23-0e41c5de1677 | -10.822 | -49.256 | 2024-10-16 02:46:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| a8c5a723-a101-30b8-8622-9d537f6b21ea | -11.6917 | -65.2243 | 2024-10-16 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 5692ee94-a3a2-3f28-8a4f-c3606db230c5 | -11.7106 | -65.2046 | 2024-10-16 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 3e3a9cb8-ae2b-3c5c-9a95-a7b1642f6886 | -11.7104 | -65.2235 | 2024-10-16 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 33954ee7-a0c5-38aa-8ea6-9bccc3f3c88d | -11.7103 | -65.2424 | 2024-10-16 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 0c9ac2c4-bf7a-3585-b95f-7db1963e9821 | -11.6918 | -65.2054 | 2024-10-16 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.0 |
| ef2b01ed-f7c6-3987-b91d-3758e9898497 | -11.6915 | -65.2432 | 2024-10-16 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.1 |
| dd07f59d-dcb3-313e-89d6-45ba96bc1c89 | -11.9381 | -64.8729 | 2024-10-16 02:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 8589db97-6227-3666-9c6d-a23d54752242 | -11.938 | -64.8919 | 2024-10-16 02:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 773119c2-092b-3d29-bf8e-2d8494c55a06 | -12.3983 | -63.7093 | 2024-10-16 02:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 83e7fa5d-6931-388b-9393-d497b284407c | -12.3982 | -63.7284 | 2024-10-16 02:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 92b8691e-3f4c-31a1-985c-126462ef5820 | -12.3795 | -63.7103 | 2024-10-16 02:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f5d442d9-25e6-397e-a61d-1c917d8eec42 | -12.3793 | -63.7294 | 2024-10-16 02:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9d7258a1-9cc9-3f60-92c9-9ad524570953 | -17.2081 | -56.6946 | 2024-10-16 02:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 9577f42d-8a3c-336f-8a62-5e582fcfdc62 | -17.1954 | -57.4767 | 2024-10-16 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| f1be11d4-a3b5-36d3-bf19-8f218f90e02f | -17.1951 | -57.4972 | 2024-10-16 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 634c1d79-ba6b-323d-bc2e-9da9f88a57bd | -17.1758 | -57.479 | 2024-10-16 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| d0c35638-3c48-331a-ad42-1a92db2d862e | -17.1754 | -57.4995 | 2024-10-16 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 9be2ee5d-95f9-3af5-a6e0-76bf189aff35 | -7.39828 | -35.24345 | 2024-10-16 02:49:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 55859ffa-b833-3b9b-a6b3-9978eb407446 | -7.39711 | -35.24956 | 2024-10-16 02:49:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cdc6a0fd-6795-3a12-85f6-49ff60256f4e | 1.0016 | -52.2164 | 2024-10-16 02:55:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 795d9e77-bfb4-3078-aebe-b93d4748a228 | -2.5259 | -47.2237 | 2024-10-16 02:55:20 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| e1ccae84-578f-39b3-a585-f5001ae5f845 | -2.6118 | -49.0985 | 2024-10-16 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 1ed653d9-4a9d-326b-bcdd-6a0e00573a25 | -3.1098 | -54.2464 | 2024-10-16 02:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8928c225-0bbd-3748-89ca-941c78081727 | -3.1099 | -54.2263 | 2024-10-16 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 6e62da5b-89a4-3370-8341-2dee6e2b1b02 | -3.1282 | -54.2459 | 2024-10-16 02:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 1d5aa628-fbed-335b-8329-e47438dd333f | -3.1283 | -54.2259 | 2024-10-16 02:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 6ed7396a-dac1-3e0d-96be-ce16f96109ce | -3.958 | -46.4442 | 2024-10-16 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 8759a4e2-9f47-3327-9df7-02e344244a7e | -3.9581 | -46.422 | 2024-10-16 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.0 |
| d4147cee-f00d-3ab7-a6a5-8ae2abc07b2d | -9.114 | -47.0074 | 2024-10-16 02:55:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d56ab09a-115c-3f4b-9dc4-3eb97078e037 | -9.1142 | -46.9851 | 2024-10-16 02:55:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| b49dfcc4-d286-3b2c-a982-2602f0cc862f | -9.1517 | -47.0034 | 2024-10-16 02:55:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 6ed37ebd-0aac-3a14-9f65-a87a28beaed4 | -9.152 | -46.9812 | 2024-10-16 02:55:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 569a69dc-08d0-3dd7-a56b-21dc294254b3 | -9.1706 | -47.0014 | 2024-10-16 02:55:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 352259b7-e953-36f5-910d-92d00ecad185 | -9.1709 | -46.9792 | 2024-10-16 02:55:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 6a907ba1-a578-363e-9291-8f40a5727160 | -9.1728 | -65.3945 | 2024-10-16 02:55:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 18ae403c-0ba4-39c3-8dbe-0a01d4d26b02 | -10.2439 | -47.3046 | 2024-10-16 02:56:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 2a01d8f4-96a0-3577-b87c-b0e7a9ed2dc1 | -10.2442 | -47.2824 | 2024-10-16 02:56:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| a37f9189-4340-3b54-98b5-ac23f406a0ea | -10.2628 | -47.3024 | 2024-10-16 02:56:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 30611a2d-a3c4-3131-9c64-3e0f1647831d | -11.6915 | -65.2432 | 2024-10-16 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 6ba5c8ff-c08e-38be-8eae-ab4ef0bb1875 | -11.6917 | -65.2243 | 2024-10-16 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0da6b55a-c2d1-3625-8f74-d9e19c841be2 | -11.7103 | -65.2424 | 2024-10-16 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 600f48ae-983c-3518-9f05-dd18292dd147 | -11.7104 | -65.2235 | 2024-10-16 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 8ded528a-9d9c-372b-aed5-fc4d611cc778 | -11.7292 | -65.2227 | 2024-10-16 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 47004c8f-917f-3f67-9142-c0d00ca7769a | -12.3795 | -63.7103 | 2024-10-16 02:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 5ef1230f-b965-3bf4-a070-6543f0d9f0d0 | -12.3982 | -63.7284 | 2024-10-16 02:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 149eb18d-a5c2-3dd7-9539-a9277b912eb0 | -12.3983 | -63.7093 | 2024-10-16 02:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8c798f4d-c022-3477-8533-150d96cf8b81 | -17.2439 | -42.6575 | 2024-10-16 02:56:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 300e6f00-67e4-3611-b6e8-2eb14798097e | -17.1664 | -56.8439 | 2024-10-16 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| b6fab8f9-895b-3224-a900-ec915812b3f4 | -17.2081 | -56.6946 | 2024-10-16 02:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 07535366-2a1a-37e1-a929-093a5289df26 | -17.2177 | -57.3102 | 2024-10-16 02:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 0fb9abce-8b8b-38b5-8794-2061f0de0a31 | -17.8249 | -57.4425 | 2024-10-16 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.3 |
| 9e5e7be9-cfb2-3425-9bd8-cdb4b8a4f3c6 | -17.8253 | -57.4219 | 2024-10-16 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 597c7dd6-7851-36a5-a01f-c71227d983bc | -18.2742 | -56.5795 | 2024-10-16 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 18ae4761-97ee-3bb3-97eb-d45ebf75f7e0 | 1.0016 | -52.2164 | 2024-10-16 03:05:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 30.7 |
| b2cd55b6-7db0-3e64-b9bc-e6222b7b877c | -2.5444 | -47.2231 | 2024-10-16 03:05:20 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 028f4de3-fc6a-3669-96d1-82e38ff01f6f | -3.1098 | -54.2464 | 2024-10-16 03:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| a2ed915b-9907-3f07-8800-98c9c95b3825 | -3.1099 | -54.2263 | 2024-10-16 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 1829abe8-e50e-33f5-bc1c-009a0ffd5c76 | -3.11 | -54.2063 | 2024-10-16 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 42cf8b0f-cc18-3883-8ae4-234300a9e59b | -3.1282 | -54.2459 | 2024-10-16 03:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 000fe770-d824-3d03-9e49-67ad90d6e17c | -3.1283 | -54.2259 | 2024-10-16 03:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 7d6f811c-a5e0-3d60-bc9e-1a81072b429e | -3.958 | -46.4442 | 2024-10-16 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 2fadaa66-f7f6-3d9b-89d9-3b86541b2fc5 | -3.9581 | -46.422 | 2024-10-16 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.6 |
| c83618ba-a059-3bc3-8f8d-686396c0680c | -9.1509 | -47.0701 | 2024-10-16 03:05:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| a40bbfc0-818a-330a-8658-60549173aebe | -9.1728 | -65.3945 | 2024-10-16 03:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 39ddd19b-2941-3fda-b294-90d5c9a1fef7 | -12.0427 | -46.7161 | 2024-10-16 03:06:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 536d7b58-2e4d-3fd3-a3be-59dd3d6f32fb | -12.0619 | -46.7134 | 2024-10-16 03:06:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| feeb0cea-c245-3348-8520-5cb6107ebe35 | -12.3795 | -63.7103 | 2024-10-16 03:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2ddf618c-ee6c-3c61-a826-ad37d5884c22 | -12.3982 | -63.7284 | 2024-10-16 03:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 15fa6de8-fc49-3118-b908-5a852bdbf4c4 | -12.3983 | -63.7093 | 2024-10-16 03:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a8e6965b-ffdb-3f03-9790-f1c70a916ca9 | -17.2439 | -42.6575 | 2024-10-16 03:06:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 980cf29c-c35c-3174-a3f1-8c2537daa15f | -17.2177 | -57.3102 | 2024-10-16 03:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| dec8c7df-1c4f-34a1-99b1-36697b81625b | 1.0016 | -52.2164 | 2024-10-16 03:15:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 29.2 |
| d214cd10-840a-3e79-acaa-e268103ff270 | 1.0199 | -52.2162 | 2024-10-16 03:15:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 30.7 |
| bc03af28-eba7-34db-adcd-755c2686850d | -2.6118 | -49.0985 | 2024-10-16 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6e5d9f68-0fed-30a9-8ae8-c0e651a9bd9b | -3.1282 | -54.2459 | 2024-10-16 03:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a5d10ebc-cc5f-3675-8b80-77a040f8894b | -3.1099 | -54.2263 | 2024-10-16 03:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 77efebbc-d81b-3622-97f9-4a289093d6ce | -3.1098 | -54.2464 | 2024-10-16 03:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f9dbef3e-fdb0-386f-8719-82ac79af74d7 | -3.288 | -50.9321 | 2024-10-16 03:15:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ed379808-7c7a-31cd-9f6e-14a7cbe0a05c | -3.1283 | -54.2259 | 2024-10-16 03:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| fa62b985-f068-3734-b102-6a51919b0fba | -3.9581 | -46.422 | 2024-10-16 03:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 111bf83a-10f2-3153-a04c-61486564bb04 | -3.958 | -46.4442 | 2024-10-16 03:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 111.7 |
| e1a06dfb-d4c6-3856-a1e8-0a877a3c9253 | -9.1712 | -46.9569 | 2024-10-16 03:15:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 9839552a-0c8e-3192-bf0e-44c6e662054f | -9.1709 | -46.9792 | 2024-10-16 03:15:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 236f95cc-5e63-397a-b22e-1911ab05b534 | -9.1706 | -47.0014 | 2024-10-16 03:15:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| b49d8d8c-b4eb-36df-b616-6e14fe8bc19e | -9.1523 | -46.9589 | 2024-10-16 03:15:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| c0d604fd-ad9c-3c03-b9fe-129c19e43b83 | -9.152 | -46.9812 | 2024-10-16 03:15:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 295.4 |
| 99981d33-cd9f-3d64-9a48-6ca5781e83b6 | -9.1517 | -47.0034 | 2024-10-16 03:15:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 148.1 |
| f6dc673d-fb77-3d2d-9be7-26a33dad2931 | -10.8224 | -49.2343 | 2024-10-16 03:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| fa4d30e8-b6f6-3855-8f57-dae6b7ebb833 | -10.822 | -49.256 | 2024-10-16 03:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f3ce0cc2-17c3-3a45-82f6-76bf7894ce32 | -11.7106 | -65.2046 | 2024-10-16 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 0375cf44-11aa-3718-a150-188d4cdbf096 | -11.7104 | -65.2235 | 2024-10-16 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |


[Clique aqui para ver as próximas entradas](README24.md)
