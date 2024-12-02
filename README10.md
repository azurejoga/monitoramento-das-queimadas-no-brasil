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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ab67e03-9924-39ee-9f50-fd0e16c638d4 | -1.5661 | -55.338902 | 2024-12-02 00:57:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcebdf30-84cb-3d5c-8c1e-66e90f02b7f2 | -1.3381 | -54.969799 | 2024-12-02 00:57:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1293edf0-1133-3946-a264-37da0f824441 | -2.9843 | -53.341499 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf5c2bdc-7efe-317c-86ec-b038e2aaa791 | -2.8021 | -53.041901 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 031a65a0-7c1b-3b3c-baee-5e1d5d0252f0 | -2.9858 | -52.500401 | 2024-12-02 00:57:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25b3df1f-3f96-3f5a-833d-0e5232195955 | 3.3826 | -60.527302 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 536d7207-eaf8-3fda-bda9-91ef17775c2e | -1.2744 | -54.553299 | 2024-12-02 00:57:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 521fe73f-9cf1-373c-8058-2b99b40a87ad | -2.8163 | -53.0592 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bf69a94-4992-3477-9c5a-282c5ea290c3 | -20.7217 | -54.4341 | 2024-12-02 01:00:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c0c44c6d-d818-33e8-8726-c1f6f28d10c0 | -12.2493 | -63.4688 | 2024-12-02 01:00:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7ceba956-806b-3993-b021-6f105bebb826 | -2.6348 | -53.3712 | 2024-12-02 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 51782e74-06a9-3785-b190-a6eece7fa4a3 | -2.5612 | -53.4133 | 2024-12-02 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| c83df510-c5f2-32d7-8411-20430e8ba27e | -2.2666 | -53.6212 | 2024-12-02 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 42c37278-b5eb-3d7c-b633-a0c6644e7cff | -3.4017 | -50.2381 | 2024-12-02 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| fa9e175d-0a19-30f0-9d4c-d6251376c62f | -6.0862 | -48.0339 | 2024-12-02 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 0bfaef55-c816-3b84-b29e-0643c3222775 | -4.267 | -50.8551 | 2024-12-02 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| fff1d480-f18f-3a3d-99c7-c41e9ec5a110 | -2.5428 | -53.3935 | 2024-12-02 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 24923a44-425a-3afe-ad7c-5e9b9b0d03c6 | -3.259 | -53.6388 | 2024-12-02 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 35c1cb5e-d4be-3a45-ba22-94c409c1706e | -3.2774 | -53.6383 | 2024-12-02 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ed5bc21f-f6c0-3b14-8ccb-51a8f7f353bf | -2.5428 | -53.4137 | 2024-12-02 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 0c1a4204-0762-3254-8ff5-cc12d59a4222 | -2.6076 | -45.2469 | 2024-12-02 01:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| c56e6879-fa70-3bbd-906d-e02aa125c9c3 | -2.2667 | -53.6011 | 2024-12-02 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| fc6296cd-b491-3a3c-9c61-6ed0e4a5df0e | -12.4171 | -63.7274 | 2024-12-02 01:00:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 790ce7e5-3b69-3032-9b03-ed0734ffdcd1 | -2.0263 | -54.3088 | 2024-12-02 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 9bbe12d1-68cd-3e32-bd63-f4123e3f8e6f | -3.4017 | -50.2171 | 2024-12-02 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 9fab8237-6fc5-3ca4-b944-7cec8ac6bc54 | -3.6562 | -51.128 | 2024-12-02 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 277dcf34-ff28-3f2c-93c8-54f3f81053a2 | -2.6349 | -53.351 | 2024-12-02 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 83716298-7e31-374e-b0f0-6620e07733ba | -2.5612 | -53.3931 | 2024-12-02 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 0bae20a8-a84d-399a-ba88-5c0dce1bbefb | 3.3842 | -60.4756 | 2024-12-02 01:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.9 |
| e3f12314-a241-340f-a677-2c5e72caeeb3 | -6.086 | -48.0557 | 2024-12-02 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 238.1 |
| a613d827-2551-3572-8ebc-e2f211efcbba | -4.5932 | -43.3471 | 2024-12-02 01:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 0b261137-e812-396c-8e30-525395aba9c2 | -2.9871 | -52.5086 | 2024-12-02 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| c07e17e3-67bd-39fa-8ba1-69a9cd88d88e | -3.3848 | -49.8596 | 2024-12-02 01:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 31cdb288-1e60-3d7a-81e6-3a8b77f28914 | -2.9208 | -45.8417 | 2024-12-02 01:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 60a3ed16-c97d-3049-9193-8ae99aa8898b | -2.8012 | -53.0633 | 2024-12-02 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 111b2d4d-43f1-38a1-a1be-0451fcfc8ac5 | -4.9085 | -41.3371 | 2024-12-02 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 148.6 |
| 66c5aeba-93cf-386d-892f-7748239a5d29 | -2.8197 | -53.0425 | 2024-12-02 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 8ddee670-fd66-3091-98c2-e0eb0950d6f4 | -4.91 | -41.32 | 2024-12-02 01:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f1956286-396c-3fce-9967-0c5e9ec43a4e | -12.4169 | -63.7465 | 2024-12-02 01:00:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 64a6b841-8fbf-31f2-919b-55d46ce174da | -2.8196 | -53.0629 | 2024-12-02 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4484eace-4cc9-38a8-b4d9-6402cfd5e3bc | -4.9272 | -41.3358 | 2024-12-02 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| 9e2fedca-f9ba-3a7c-9767-d9f53e7d6a86 | -3.2591 | -53.6186 | 2024-12-02 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 9cf2f619-2fe9-3ced-97b9-fe008a554c9d | -4.5745 | -43.3483 | 2024-12-02 01:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 6e855d24-b0e7-33c4-b2ed-d822c0f40ede | -12.4359 | -63.7264 | 2024-12-02 01:00:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 127.6 |
| a9beeeee-7f4d-3967-9e44-b36edb405baa | -3.2775 | -53.6181 | 2024-12-02 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 146d8678-1c55-31de-a669-1e4ff0632df2 | 3.3841 | -60.4946 | 2024-12-02 01:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 7577af5e-632b-3e74-8cb8-04ff69888d76 | -2.5796 | -53.3927 | 2024-12-02 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6babaf10-e989-3952-9d78-951c4b60fd3c | -12.4358 | -63.7455 | 2024-12-02 01:00:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 51b142d0-c466-3ee3-8919-8ff12ecfd1c1 | 3.3841 | -60.5135 | 2024-12-02 01:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| cdf7b1f7-799c-3cec-b9c2-c86a49fec6ed | -6.0674 | -48.0569 | 2024-12-02 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 346b5e18-4c90-37e4-b1e4-7cd2e1291e43 | 3.384 | -60.5325 | 2024-12-02 01:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 04610794-02ed-3bbb-a1d3-7d793095e442 | -2.8013 | -53.043 | 2024-12-02 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 8f642df9-65a9-3233-ba47-f9c62b6ff4da | -4.9087 | -41.313 | 2024-12-02 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| f7eb9bb2-ced4-3abf-b7bb-dfa6d674a28d | -6.0858 | -48.0774 | 2024-12-02 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 20780030-16b8-34c2-b1e6-8ce842bc4805 | -3.4201 | -50.2375 | 2024-12-02 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| df06beed-3ea8-3795-90f1-af3028b43d23 | -2.0263 | -54.3289 | 2024-12-02 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8f90cb25-def1-39c3-8855-5821562de55c | -20.7421 | -54.4306 | 2024-12-02 01:00:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a847be9d-a23e-3cde-b21c-9d00285e4002 | -4.91 | -41.36 | 2024-12-02 01:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0d99f74a-9090-3b16-808f-7273fd7282db | -6.06 | -48.05 | 2024-12-02 01:00:00 | MSG-03 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87ef0fcb-c6be-33ca-946f-a599032b10f7 | -20.73179 | -54.43433 | 2024-12-02 01:09:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 65b08877-61e8-30e8-8093-b00858a37341 | -20.33247 | -48.82285 | 2024-12-02 01:09:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ea64bcf1-824b-3da9-b51c-1ad9d0913d44 | -11.05854 | -45.37346 | 2024-12-02 01:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2c24e5ea-3f46-3c1c-b78f-53309c5db72f | -20.721 | -54.43565 | 2024-12-02 01:09:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 38.9 |
| a320a468-23b8-36b6-a331-cc00c30403cc | -11.06141 | -45.37941 | 2024-12-02 01:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 33632ebe-17d7-3391-9294-0a9190e94e6c | -20.71935 | -54.42155 | 2024-12-02 01:09:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7e22f789-22c4-3335-9829-db8399baefa2 | -20.32344 | -48.82441 | 2024-12-02 01:09:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fa917f1b-73b2-34ed-846e-53ed97316c61 | -20.73014 | -54.42025 | 2024-12-02 01:09:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 39.1 |
| b6d49010-3d07-3078-8cf0-fa4e26c91f88 | -6.086 | -48.0557 | 2024-12-02 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 244.2 |
| 3d9609f1-5cee-3aeb-9a85-4f607cc9b02b | -2.6076 | -45.2469 | 2024-12-02 01:10:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| d4ec4988-5f47-315e-abe5-c5c3d66526f3 | 3.3841 | -60.5135 | 2024-12-02 01:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 92f2aee0-e1d8-3010-a5ea-979dcdb64517 | -2.9871 | -52.5086 | 2024-12-02 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 72998690-aa62-3dba-b081-e79981b27950 | -12.4358 | -63.7455 | 2024-12-02 01:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 59d57ed1-7e35-3f96-a79c-60dc345937d2 | -2.8197 | -53.0425 | 2024-12-02 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3dca3cb5-ec4d-31d5-a6fe-9337f07f1c10 | -6.0862 | -48.0339 | 2024-12-02 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 7a03e003-bd6f-3856-8ee0-0e9840aa776a | -4.9272 | -41.3358 | 2024-12-02 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 40279659-00c6-31c8-81b9-cefac1943d2d | -4.9085 | -41.3371 | 2024-12-02 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 157.8 |
| 4809a084-4f02-3bfc-9527-73697bbba5d7 | -12.2493 | -63.4688 | 2024-12-02 01:10:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d4d5aa7f-ee33-367e-88af-27983b136d5b | -2.8012 | -53.0633 | 2024-12-02 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f479107b-741f-36d5-8fb3-d48dc87d1152 | -1.0735 | -53.4562 | 2024-12-02 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 14c8f1b5-b66a-34c8-a122-775a43e10662 | -5.5882 | -45.1412 | 2024-12-02 01:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 62f874d5-b25e-31b1-96fa-bdc98ffb368c | -2.6348 | -53.3712 | 2024-12-02 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 99f03f0a-cc8c-399f-aa33-032ef2c9fe7a | -4.267 | -50.8551 | 2024-12-02 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 27a96510-823a-337f-bcf3-02d50bc591ae | -6.0674 | -48.0569 | 2024-12-02 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| bae25e27-f4fe-3249-8e21-102c9cf216d3 | -2.8013 | -53.043 | 2024-12-02 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3d1581a6-a771-389e-aa9e-abd2f877605d | -3.4017 | -50.2171 | 2024-12-02 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 40d86735-bd28-3d7e-a686-daf7d2119e5e | -12.4169 | -63.7465 | 2024-12-02 01:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 7ccfae76-b997-3d1b-9b8e-0a2fedbe6365 | -2.6164 | -53.3716 | 2024-12-02 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| fe2fa7ea-5bd0-37f4-ac97-0f0baf3a28c9 | -3.2774 | -53.6383 | 2024-12-02 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 09669c4c-0316-32b3-8ff7-8a0ccc2fffb0 | -2.2667 | -53.6011 | 2024-12-02 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 49139cb9-a018-3637-8784-64d6bf3fbc44 | -12.4359 | -63.7264 | 2024-12-02 01:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 957bf1b4-925a-3d2e-8390-b15ede42b80d | 3.3841 | -60.4946 | 2024-12-02 01:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 170554b1-e166-37c2-90be-89ccf47de201 | -2.5612 | -53.4133 | 2024-12-02 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 3da5384e-174a-3251-a71c-668689c1d80d | -3.2775 | -53.6181 | 2024-12-02 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 2c490bb2-7d66-32ff-a0bb-0c4caf0de4aa | -12.4171 | -63.7274 | 2024-12-02 01:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| c69355d6-bca4-3884-afd2-580cd68b450b | -2.8196 | -53.0629 | 2024-12-02 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| d0704032-935f-390c-88e1-033f4b761ab2 | -4.5745 | -43.3483 | 2024-12-02 01:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| fb3a2337-a9ed-39e7-af07-227f5c5de73d | -20.7217 | -54.4341 | 2024-12-02 01:10:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3393859f-9af0-31bf-a8d8-4f743c6980b5 | -2.6349 | -53.351 | 2024-12-02 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 989bb3a5-d5fa-37a1-82ca-519900db1907 | -6.0858 | -48.0774 | 2024-12-02 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 4fb56b7e-6473-3d9a-9765-82c556b8f7df | -3.4017 | -50.2381 | 2024-12-02 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |


[Clique aqui para ver as próximas entradas](README11.md)
