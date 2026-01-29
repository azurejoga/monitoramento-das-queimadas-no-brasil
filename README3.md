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
| 6b88b779-06e2-3312-b1ea-067787c83ebf | -1.19879 | -53.65805 | 2026-01-29 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cd3ba1f-8059-3713-9362-dd1a8ca136a6 | -1.19816 | -53.66206 | 2026-01-29 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2bf441d-390e-3ec1-a56c-b2195bf74117 | 1.49042 | -55.90809 | 2026-01-29 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcf6f63e-47f0-3c9a-a96e-f1c730c491bd | -1.80762 | -54.4962 | 2026-01-29 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 181b8ccf-399d-34da-b4bd-565a9c697c7c | -1.80704 | -54.4999 | 2026-01-29 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eee57c4d-2f49-3a7a-9368-5e830b35868a | -1.8042 | -54.49567 | 2026-01-29 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e88efca3-d76d-37db-befb-d2e2d3cfc43b | -1.81046 | -54.50043 | 2026-01-29 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6dc57dd-1bc3-3068-bda5-f089f41029b5 | -6.21388 | -55.6657 | 2026-01-29 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de0e6878-de47-3590-8052-a7dca132395f | -5.28503 | -56.01843 | 2026-01-29 05:12:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b898740-e7ec-33b5-b4ca-ad91286b1208 | -6.10161 | -45.85316 | 2026-01-29 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86b70a6b-cb34-3610-aa6f-b1e35ec827bd | -16.44127 | -57.26949 | 2026-01-29 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| afa68348-af9b-3d25-90d2-b534d41be53b | -15.63873 | -58.08308 | 2026-01-29 05:14:00 | NOAA-21 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0918890f-7ee3-3460-b380-52d55d648368 | -21.81347 | -52.73838 | 2026-01-29 05:16:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1adc968-321b-3d2e-a7eb-63339c6ee66c | -21.78193 | -52.73445 | 2026-01-29 05:16:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56836ffe-fd24-33c5-a304-3c959fff2729 | 4.12228 | -60.98704 | 2026-01-29 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab80f7e5-3aa1-3092-bab2-221262967eaa | 4.12338 | -60.99397 | 2026-01-29 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 869a3dd9-f0d2-3765-a713-f96c044312d7 | 4.12393 | -60.99744 | 2026-01-29 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65762123-a4b1-3724-af85-7263cd9e696b | 4.12006 | -60.9945 | 2026-01-29 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34672b50-4369-3061-9589-3cad8f6409c2 | 4.26489 | -60.28675 | 2026-01-29 05:37:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da71360e-4664-3406-9ceb-2a6590407a97 | -1.31099 | -53.20495 | 2026-01-29 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f7356364-712f-3b4c-b015-a135e5915932 | -1.31154 | -53.20143 | 2026-01-29 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b12bdb9-c9f6-34e6-b17b-b7e5859fda9d | -1.20161 | -53.65841 | 2026-01-29 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6153ab17-0353-3211-b96b-52c077907f5d | -1.80645 | -54.49329 | 2026-01-29 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c986c98-c247-31a7-80c1-fd9e7a49125b | -1.19572 | -53.66127 | 2026-01-29 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01e23366-ce1e-322c-9ecd-1cd06bcb98a9 | -1.19626 | -53.65773 | 2026-01-29 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eaca8c3d-7fbf-3c23-8caf-8cba6ad6b47e | -1.20106 | -53.66196 | 2026-01-29 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a1249eb-9e63-3d63-a568-cba190b9aa26 | -1.3121 | -53.19788 | 2026-01-29 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 30e02640-5a79-3b1c-9f60-d5c6f1a79f71 | -1.81064 | -54.49991 | 2026-01-29 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a2a3f34-1a77-3a21-9962-72e441f0cfb6 | -1.80601 | -54.49619 | 2026-01-29 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e6b2f2e-3e0c-3d84-b90c-6dac4b0d0622 | -1.80556 | -54.49912 | 2026-01-29 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e9254b4-a94a-30ee-a503-25eff3afcb6a | 3.4765 | -60.16401 | 2026-01-29 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92534aea-88bc-3289-b036-6248c37c5b10 | -1.30604 | -53.20054 | 2026-01-29 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af0851f3-d643-32cd-9133-1e4acdadab5c | -11.9516 | -63.84424 | 2026-01-29 05:44:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f463c1ae-bb7d-39b7-beef-f5b4d865716d | 3.53412 | -60.70025 | 2026-01-29 06:01:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 612ba45d-0f35-30d7-aaa9-65ba0f6a402e | 3.53245 | -60.70415 | 2026-01-29 06:01:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e131ab81-efef-3695-9abc-e7087a816a13 | 4.16743 | -61.06522 | 2026-01-29 06:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33f6d669-a48e-3f22-9121-db5400a327c1 | 3.53161 | -60.69923 | 2026-01-29 06:01:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7905945d-02aa-3287-a91f-0e8c3d1ef6e5 | -1.31113 | -53.19061 | 2026-01-29 06:48:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 64d41d52-7a91-333e-b91f-db34df43f72d | -1.30054 | -53.19878 | 2026-01-29 06:48:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3e6f86e9-03e9-3c63-a638-3772fc3aed4c | -1.79988 | -54.49439 | 2026-01-29 06:48:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 62e0bafd-b3df-3193-9a55-0cca035a2a73 | -1.80119 | -54.48559 | 2026-01-29 06:48:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1731d94f-55d6-3751-bb82-7333e97f1ecf | -1.3097 | -53.20014 | 2026-01-29 06:48:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e0e24ac8-d484-3743-859e-cce85888e028 | -20.28881 | -57.33527 | 2026-01-29 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e21c95e2-5700-32c8-898a-82f8852092e4 | -4.63991 | -39.37915 | 2026-01-29 11:51:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2a800e1a-2752-342e-82e4-50135b191a87 | -6.08018 | -35.39886 | 2026-01-29 11:53:00 | TERRA_M-M | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 26.1 |
| fc7eae3d-f242-3251-a041-9fcbdf4b8086 | -6.08074 | -35.39225 | 2026-01-29 11:53:00 | TERRA_M-M | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 25.6 |
| be59e75a-d195-3098-b149-7073452e9c9c | -20.73589 | -42.02373 | 2026-01-29 11:57:00 | TERRA_M-M | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 38a19bdc-77ba-3214-99fa-bfdfa34f6b66 | -20.73882 | -42.01482 | 2026-01-29 11:57:00 | TERRA_M-M | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 6e0ffddb-fdcb-345a-a80b-5cdc4003046c | -20.73713 | -42.02991 | 2026-01-29 11:57:00 | TERRA_M-M | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| ae481007-4501-3835-8326-2c2bd3136d36 | 4.1323 | -60.9917 | 2026-01-29 13:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 79.7 |


