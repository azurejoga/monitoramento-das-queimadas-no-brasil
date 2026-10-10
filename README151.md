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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d5bf1c0-ddf0-37c9-8749-955739d4a9e9 | -12.1627 | -45.3547 | 2026-10-10 11:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f1e92e48-3792-3691-85b9-a5e2b5ac99db | -10.9174 | -45.5088 | 2026-10-10 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 91e836a0-ff76-3278-a9a1-117703f09af1 | 1.40925 | -50.6755 | 2026-10-10 11:57:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d0e3093d-75d4-325c-842e-b7d5fa7460eb | 0.99847 | -51.09247 | 2026-10-10 11:57:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8f68953f-ba5f-3a19-8593-2f05c238fb8c | -1.41008 | -47.60907 | 2026-10-10 11:57:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0c3169b3-3e10-3cbc-aa40-0d2c56baa0f7 | -1.73117 | -47.66661 | 2026-10-10 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9b012de8-19d5-3263-ac5b-ad0925420a80 | 3.23397 | -51.2996 | 2026-10-10 11:57:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1094e0cb-b78e-3a2b-aa07-970f3399d012 | -0.88223 | -48.71427 | 2026-10-10 11:57:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 60ef69ae-0a2f-3fd1-afc1-03e2d8188ebd | 3.73898 | -51.60836 | 2026-10-10 11:57:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b8ed32bd-2466-36a9-a693-8738ea57c5eb | -1.42426 | -47.22754 | 2026-10-10 11:57:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3e409b09-69c7-3b59-86cf-65b82535b92a | 0.29457 | -51.39707 | 2026-10-10 11:57:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 196c3953-3175-3de3-a0f0-af37416f14c2 | 0.6966 | -51.43203 | 2026-10-10 11:57:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9ee6dadd-f9df-3737-96da-1eec06f8469f | 3.23533 | -51.30917 | 2026-10-10 11:57:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 28b9a7b2-293c-3623-831c-878ec89f7ba8 | -0.88089 | -48.72364 | 2026-10-10 11:57:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 64592cf8-1c8b-3bb4-b54d-82f880ed0de0 | 3.99912 | -51.62634 | 2026-10-10 11:57:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 53e73207-70a4-30ed-a2c1-fd868a85669c | -1.48683 | -47.95428 | 2026-10-10 11:57:00 | TERRA_M-M | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| efde1d6f-8cec-3031-8f50-42147d7c95ab | -1.40854 | -47.61985 | 2026-10-10 11:57:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| d5aee923-d9a9-372d-813b-a7f82cba17cd | 0.99977 | -51.10152 | 2026-10-10 11:57:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 5cc8adb2-474c-3383-8374-310f981e4271 | -1.73333 | -48.82586 | 2026-10-10 11:57:00 | TERRA_M-M | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a7488c9a-d0a1-39ba-bd0a-c0ce9838691d | -1.11039 | -54.1694 | 2026-10-10 11:57:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| a3188fe9-3999-3240-b1fb-2a05c1bd4f48 | -11.8978 | -47.3642 | 2026-10-10 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 163.8 |
| d04dcc8f-b220-333e-8a61-73e8abcc608e | -11.1873 | -45.3347 | 2026-10-10 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| a138e9fd-447d-3201-8024-2e38339c3bd6 | -11.7772 | -45.4806 | 2026-10-10 12:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 155.2 |
| e7f4a502-ba9a-3e9e-890c-a809aeaa66e7 | -15.043 | -41.3576 | 2026-10-10 12:00:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 107.2 |
| 4d617e1a-2b9b-31df-89b9-1159f474e136 | -10.917 | -45.5317 | 2026-10-10 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 2e159e2c-9aed-31c4-9921-2817e2727b19 | -10.9361 | -45.5292 | 2026-10-10 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| baad7b18-e4e1-3d79-87ed-97862ec02375 | -12.1627 | -45.3547 | 2026-10-10 12:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| d704b290-7ccc-3e0f-8d31-c3df7b9e4203 | -7.2372 | -55.0805 | 2026-10-10 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| f10ed395-0b4f-34cf-a29a-714a70013277 | -10.9174 | -45.5088 | 2026-10-10 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 4ea09af8-08e2-397a-a2a4-d8ad9055f1ef | -15.0233 | -41.362 | 2026-10-10 12:00:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 102.1 |
| cee94002-e7e0-3daf-b906-e9e071f539c3 | -11.0745 | -44.1003 | 2026-10-10 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| f23ffdcc-2a14-352e-81a3-19617adced54 | -11.0933 | -44.1209 | 2026-10-10 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 8c1e010b-74fe-3546-a029-3e77d8c7f4bd | -11.7768 | -45.5035 | 2026-10-10 12:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 1ac0f1e1-313a-31de-a3ce-e472232cef45 | -11.0937 | -44.0975 | 2026-10-10 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 2656466b-4e35-3046-9a9c-222662966a73 | -4.11437 | -54.01143 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 98c9c59d-1da0-3e4e-883e-b3e0d8ec0be5 | -3.01146 | -51.00115 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 768e9f1d-d9df-3b99-b2c1-5eff9a26abb6 | -11.77505 | -45.52367 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| c35cb9e6-040a-39d5-8c43-86ef6f8ebb61 | -9.08748 | -44.29216 | 2026-10-10 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 273.0 |
| 0706b677-4e6d-3254-809e-149ed1e0620b | -6.41852 | -51.9543 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| eb50f6a0-b027-3e9e-a637-837f2a027216 | -6.78121 | -49.98696 | 2026-10-10 12:00:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| ca89f1b7-3a56-33e7-9500-2850b372f0da | -9.27386 | -47.40694 | 2026-10-10 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 94e1744b-3a3a-326d-8b4d-261c6bce6504 | -9.21592 | -45.64737 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 51b2449e-c413-30a2-839d-f16bf50f536d | -11.90241 | -47.36611 | 2026-10-10 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| fd7cad7e-ad6f-3a05-b51e-870525f78e90 | -11.56852 | -43.6769 | 2026-10-10 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 6a2f499b-5cdb-3bb6-ba4d-5d5a22525638 | -11.78037 | -45.47933 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 467.0 |
| be289db4-609e-36ac-91e2-abf4e3d45dbf | -3.5973 | -54.59641 | 2026-10-10 12:00:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 150019b3-1c7a-35c8-846e-6139afcaf479 | -2.30069 | -48.54163 | 2026-10-10 12:00:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b330fb0f-38a7-3e2f-9e71-b566700c7c93 | -2.46025 | -47.58051 | 2026-10-10 12:00:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5a56cc55-6701-309c-8c39-e53de92dd8cc | -7.42724 | -55.30013 | 2026-10-10 12:00:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c8d893b4-5b51-3f20-a379-2d262179fe71 | -8.70473 | -44.92366 | 2026-10-10 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| b1e72e76-a61e-30a2-81b7-03b7b4cbeee7 | -12.17576 | -45.33889 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 12cdb97f-0f1f-3c8e-bafa-c7a206ee991e | -4.74012 | -55.6681 | 2026-10-10 12:00:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 901321b2-9800-3e47-82f0-4c201861f7f8 | -4.05383 | -49.05379 | 2026-10-10 12:00:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 6b8069da-0fab-3fda-9c33-5e9473e81bec | -4.89457 | -49.04408 | 2026-10-10 12:00:00 | TERRA_M-T | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 5e2290a3-11d1-3f0b-9685-2710d4facc71 | -5.93343 | -52.18101 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7da93321-3495-3d06-a457-405f5d5366f3 | -4.1222 | -50.98 | 2026-10-10 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8c75f7ec-e7a1-380d-a4e8-b2d4dbbeab98 | -8.91968 | -45.40217 | 2026-10-10 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.8 |
| ba54b00e-56b6-3706-966f-956844e088dd | -3.79487 | -50.74933 | 2026-10-10 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 255227bb-30e8-36f3-9b29-7883e4960c73 | -3.523 | -50.39849 | 2026-10-10 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e32ae91c-44d0-33ec-97fd-337f1ca7a4d9 | -11.02538 | -49.11042 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8bf62a84-e2e5-3f2f-8a79-df7d5920b633 | -3.48502 | -50.33298 | 2026-10-10 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5c19207a-1e19-30c9-954a-62af4ba3e17d | -9.21354 | -45.66179 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0f3e9d86-3494-30ef-a51a-f64cda463b4d | -7.21709 | -55.06669 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 22857e6d-2a2c-3a4b-92a7-8074c659636a | -7.28721 | -47.24641 | 2026-10-10 12:00:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e5c34018-6f14-34e0-b1e5-c918b22e5560 | -9.09043 | -44.26658 | 2026-10-10 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 322.7 |
| 0bcd0d07-08e7-39ef-8a93-96cf3a81dcc3 | -3.30071 | -50.331 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 19d1015a-8a8e-390a-bf34-4aedb49b9211 | -2.58043 | -48.25102 | 2026-10-10 12:00:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cefdaadc-e60c-31e1-8ba3-f0863b0ce6f1 | -7.19268 | -55.15989 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 18ad885f-d811-3f63-8cc5-a8922eeb2d60 | -12.16575 | -44.7785 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| a5645f49-ce4c-3f1f-a2ab-17ae552358a5 | -2.93602 | -54.07481 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b8a77d23-e4fa-3d7a-9635-4e0beaa7a65d | -3.26552 | -50.38889 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 932797e5-4cc2-31cf-be10-fd936959b675 | -9.08499 | -44.28523 | 2026-10-10 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 407.9 |
| 683f87e1-3abf-3fa9-9064-0b0595bbbf39 | -3.89252 | -52.19004 | 2026-10-10 12:00:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e282c890-1c07-3d15-bec9-0a496b4bf856 | -3.7503 | -42.51288 | 2026-10-10 12:00:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 64116a6a-926a-3277-b9c5-74c474b43323 | -10.21825 | -52.11201 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c4ef241f-ed03-3d51-98a0-4673bb38e77c | -7.53276 | -45.3159 | 2026-10-10 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 5219f632-517b-304d-b666-419619b032f3 | -9.0993 | -44.28661 | 2026-10-10 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| bab5eb35-7a8c-37b2-8f0f-da5d1c0850ae | -3.17334 | -50.45076 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c92f3f53-ce57-31bf-9fcc-7b77b7df9f8b | -11.78367 | -45.53071 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 3eaf6a67-c9d5-3876-8a56-ca9bc5c22d26 | -5.79638 | -53.81023 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7637b6bf-c985-37a2-a18c-481d9ae368b2 | -11.78617 | -45.50862 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 0ab00806-5c51-3cbd-88e1-9317c8ae6a4f | -3.24931 | -54.03259 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| e1892332-4fde-3103-b309-b17f5887d515 | -8.70767 | -44.89977 | 2026-10-10 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 1503c0d8-4edb-3cc3-b91d-40557707b015 | -3.01021 | -51.0099 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 9dc2e0c2-218d-30a2-853b-8da8eebfbadf | -3.56837 | -54.37675 | 2026-10-10 12:00:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6158a9fe-2b6f-30a1-bd2a-e093b6dec625 | -8.52546 | -46.89084 | 2026-10-10 12:00:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2834a87e-31a3-3b43-8fe2-25fe0fba900b | -4.40498 | -49.76601 | 2026-10-10 12:00:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 4e43112e-ea5d-3594-a14a-a1eeb8d1048f | -2.89501 | -54.07478 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e42ae0ba-92e8-38db-a23b-c28aba049f9d | -3.98704 | -54.45462 | 2026-10-10 12:00:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 803a2b47-96de-361d-b45e-ee5a9934c13b | -12.16268 | -44.80433 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| be917bf9-f31b-32a0-9fa5-ced3e096b6c4 | -2.29564 | -50.25865 | 2026-10-10 12:00:00 | TERRA_M-T | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1fce5e39-2a9a-3dc2-a3d8-cb51e31ee2f0 | -3.54403 | -54.7414 | 2026-10-10 12:00:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 13ba7a71-ab41-3f2b-86d3-598017dcc60c | -7.1326 | -44.88168 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 4632b00f-5d71-3cd4-b755-b498ae308073 | -2.24207 | -51.92249 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3f325598-8156-3057-be64-24852c74be26 | -3.28348 | -53.86498 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 1e895d9d-f918-3cb8-a6a2-7cf27a159f61 | -3.50371 | -49.94652 | 2026-10-10 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2e5ed9da-dec2-38ed-8976-612b516b5303 | -12.17295 | -45.36246 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 4740c2de-9537-3d1b-8295-ae5608b1c32d | -6.77188 | -48.65951 | 2026-10-10 12:00:00 | TERRA_M-T | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a21c86f3-5312-3132-88b9-93ef71403444 | -7.09018 | -52.6803 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ec5993a2-0c7b-38a7-8666-3c443ddfb738 | -2.89592 | -54.06918 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |


[Clique aqui para ver as próximas entradas](README152.md)
