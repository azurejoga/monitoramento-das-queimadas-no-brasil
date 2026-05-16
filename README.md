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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 048724fb-dd9b-3784-8b46-9b754835f812 | -14.1831 | -52.8667 | 2026-05-16 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 6ebcf8c6-1196-3bfc-870f-b224b7efddf9 | -14.1828 | -52.8878 | 2026-05-16 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| d0547285-58bc-30ec-93b2-b1cd7dc18ea7 | -14.1828 | -52.8878 | 2026-05-16 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 316d6061-493f-33f3-ab67-505ba66ed6d9 | -14.1831 | -52.8667 | 2026-05-16 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d911c013-892e-3310-9053-86e3ab0765ac | -14.1831 | -52.8667 | 2026-05-16 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 0abeb585-7504-3638-bb17-b51f9a5045a4 | -14.1828 | -52.8878 | 2026-05-16 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 6864d715-0221-3c0f-a015-d81574a5cdc8 | -14.3488 | -54.5584 | 2026-05-16 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 42855345-36e9-32e7-8872-c044db1cc0b8 | -8.0761 | -44.1244 | 2026-05-16 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 06503b56-2070-323b-b62a-7804494ecc5c | -12.0445 | -45.285801 | 2026-05-16 00:20:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80b97bd0-d8d2-3823-b650-caa7c5aa4ddc | -11.0422 | -48.9161 | 2026-05-16 00:20:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49faf268-a0a7-3de7-bfe7-2aa4e9c8a7f0 | -9.456 | -47.8162 | 2026-05-16 00:20:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d1b0d5c-ecf2-34de-9aa8-23564f6778f2 | -11.0439 | -48.923401 | 2026-05-16 00:20:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebacf02b-05ff-377d-be51-30315c41c3bf | -11.5996 | -48.023201 | 2026-05-16 00:20:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c22ea5f3-2fc2-3df5-875f-9b02f5f963f2 | -14.3562 | -54.545399 | 2026-05-16 00:20:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4da8ee8b-9f27-3431-9aeb-6244762182ad | -11.7434 | -44.5191 | 2026-05-16 00:20:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c82bc6b4-fa90-38c3-94df-f2014736e493 | -11.7405 | -44.507301 | 2026-05-16 00:20:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c13518b9-1ea2-318f-beaf-cc233703fca5 | -13.034 | -49.926399 | 2026-05-16 00:20:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 607a5bb3-167d-3853-979e-5ddca35cebd0 | -12.8451 | -43.750702 | 2026-05-16 00:20:00 | METOP-B | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2bec020-ba2a-3e6f-8b53-491bacd0c7f8 | -14.1836 | -52.8629 | 2026-05-16 00:20:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 322a565e-0c17-3a70-9042-0969a6626a0f | -11.4877 | -52.911301 | 2026-05-16 00:20:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 128e7bd7-3544-3598-a670-08440662d4b4 | -14.1738 | -52.865002 | 2026-05-16 00:20:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d0f2bdf0-e7a5-3f36-b95f-1ee642dcaeae | -14.1756 | -52.873299 | 2026-05-16 00:20:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 952aec2b-1dcc-39cc-ba3b-4940f7512e75 | -11.4403 | -54.082802 | 2026-05-16 00:20:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c4f1161-49ca-3125-bb84-d745cc76cadd | -8.0806 | -44.1408 | 2026-05-16 00:20:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8bd8d51f-9376-3071-b3f3-58412241c429 | -11.8711 | -43.8652 | 2026-05-16 00:20:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76022196-a6a0-3a2d-86a7-a60d089e0166 | -16.4289 | -52.787498 | 2026-05-16 00:20:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f9f4c6d8-98aa-3b9e-acfe-50a71b0c9676 | -11.5978 | -48.0154 | 2026-05-16 00:20:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f992a9b-a9c5-303f-b94d-35bff4f600e0 | -14.1819 | -52.8545 | 2026-05-16 00:20:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 72c91e31-16a8-342a-ba05-1b5c689fa4cd | -14.1854 | -52.871201 | 2026-05-16 00:20:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c2379ab9-925a-3b2b-a1e7-a51bbc37226f | -13.0356 | -49.933399 | 2026-05-16 00:20:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae131a5c-1dc7-3636-a1d0-c67826920495 | -11.486 | -52.9034 | 2026-05-16 00:20:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac07fdd3-90f4-3ef4-a8ad-0feb9aeb868c | -8.0771 | -44.126499 | 2026-05-16 00:20:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4ad2dd52-b080-3d1c-837c-fa5c7b26b71e | -14.1871 | -52.879601 | 2026-05-16 00:20:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4f65c1e-02a0-35be-a0a6-edff6b5d0a64 | -14.1773 | -52.881699 | 2026-05-16 00:20:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9808d118-71aa-3224-890c-e14ba69eabfe | -11.8679 | -43.8522 | 2026-05-16 00:20:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f0699756-109a-3edc-bf6e-c84635c983f9 | -8.0736 | -44.112202 | 2026-05-16 00:20:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 46408b5e-9105-334a-8928-2b2f0820753e | -9.794 | -48.070202 | 2026-05-16 00:20:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5914e17d-14b6-36b7-8f92-849632080840 | -14.1831 | -52.8667 | 2026-05-16 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 2c033b46-943b-35a3-b700-9581bf608094 | -14.1828 | -52.8878 | 2026-05-16 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| dabda341-02fb-33b3-8510-72afcd2cfe38 | -8.0761 | -44.1244 | 2026-05-16 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 9757960a-afe6-3298-b793-8c6416fdd4ea | -16.42355 | -52.80466 | 2026-05-16 00:30:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 53efc3ff-214f-39e4-947c-e0539831e2bd | -16.16529 | -58.48338 | 2026-05-16 00:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 3bb27900-d391-3eac-9eb1-f1534d364ccb | -16.42231 | -52.79544 | 2026-05-16 00:30:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 962acc6a-4631-347d-82bf-74888b08d532 | -16.16739 | -58.47666 | 2026-05-16 00:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| a76ffc65-8290-372b-9573-9e0507335a46 | -16.16943 | -58.49592 | 2026-05-16 00:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 84b18b76-0382-31d2-9a58-0c8659116743 | -8.85762 | -50.21344 | 2026-05-16 00:33:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7a696d64-a8df-39ff-924c-cd79534ff5b1 | -14.16616 | -52.8724 | 2026-05-16 00:33:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6b012aa4-4038-3b71-8e5b-2298f18009ab | -11.87606 | -43.87672 | 2026-05-16 00:33:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6c769c95-c35c-337b-8fa6-0c3f9bcc19d0 | -13.03836 | -49.9374 | 2026-05-16 00:33:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f4e1c70e-ba7f-3488-ad8a-10cceecdca57 | -14.17744 | -52.88917 | 2026-05-16 00:33:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 6e4c6f0b-6d37-3bd3-8430-1f0d2baaa8cd | -14.17497 | -52.8711 | 2026-05-16 00:33:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1face52c-3d6b-3b22-8e08-f21afc65b23d | -11.86689 | -43.88525 | 2026-05-16 00:33:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 736262af-0723-335b-a87f-a66e44c6fbc1 | -11.48109 | -52.91221 | 2026-05-16 00:33:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 20947250-a377-3e24-b4f9-2791c2147408 | -11.48234 | -52.92117 | 2026-05-16 00:33:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| a323a3f4-31ee-395e-9098-7fe2204b3c33 | -13.02861 | -49.93901 | 2026-05-16 00:33:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| dd216eb5-2545-3664-bc20-4ece998f6d8c | -14.35499 | -54.56323 | 2026-05-16 00:33:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4448a072-3c04-3dfc-b6ba-f91447caf5a4 | -11.4403 | -54.09174 | 2026-05-16 00:33:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| c45f4df5-9a5f-3c36-8fbf-e5c6ecaef806 | -11.03748 | -48.92817 | 2026-05-16 00:33:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5d9ed0cd-b52f-3e42-b667-883b582bba0c | -8.08103 | -44.14051 | 2026-05-16 00:33:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 74cad107-451a-32b9-8796-7065b5ec05a0 | -14.21261 | -54.66597 | 2026-05-16 00:33:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 19b1e727-03f1-37e1-8118-c2655a9f0840 | -14.35371 | -54.55329 | 2026-05-16 00:33:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6436fdcd-bb71-3a75-a86e-1d61da1632d8 | -11.44152 | -54.10084 | 2026-05-16 00:33:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c463f815-92c3-379b-8305-4f6cd816580a | -11.59962 | -48.03389 | 2026-05-16 00:33:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| c30d4323-9742-39d5-b18b-e9002db8f9d3 | -8.08575 | -44.1326 | 2026-05-16 00:33:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 65f22e00-7a1f-3b81-8709-55a0752c1381 | -14.17621 | -52.88014 | 2026-05-16 00:33:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 43e009c3-9018-3f26-9b57-4ee560a3c22c | -12.0241 | -47.80126 | 2026-05-16 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1511cabf-d0dc-3892-8bc0-908194a88663 | -11.74636 | -44.53033 | 2026-05-16 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 3680a930-7eeb-336f-9a41-66a120ea7ee9 | -10.91847 | -54.11921 | 2026-05-16 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 89fd4d7f-1fab-36fc-aa3b-ded11a8d747e | -14.19669 | -54.68854 | 2026-05-16 00:33:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bb633f95-0774-3934-88dd-03f3e152e3c3 | -8.0761 | -44.1244 | 2026-05-16 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| a6846bd5-ef63-3eac-bc75-b2d368d6250f | -14.1831 | -52.8667 | 2026-05-16 00:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| b85a2ede-f970-389f-badd-e12406cefac0 | -11.5971 | -48.031601 | 2026-05-16 00:47:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63821793-6946-390e-b737-a64e2bc53c80 | -17.353001 | -42.621201 | 2026-05-16 00:47:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d11df0ed-818a-3ac7-9029-735cb5e348bf | -14.1841 | -52.8801 | 2026-05-16 00:47:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e9b401ff-6940-3fe3-88dd-1f04fd69b99f | -12.0291 | -47.802799 | 2026-05-16 00:47:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a25921e-9606-3164-b939-ef1097f85d3e | -13.0325 | -49.936199 | 2026-05-16 00:47:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7bc73d69-3e2d-3991-9cbe-4f80ff4f0733 | -14.1804 | -52.862499 | 2026-05-16 00:47:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97577045-58d8-3890-aa38-93cd7cd8af07 | -14.1725 | -52.873402 | 2026-05-16 00:47:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dcf4fc2b-c28f-37db-bc2b-2a578d2a91b8 | -13.0309 | -49.929199 | 2026-05-16 00:47:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3fdafd09-ccf3-3955-9aad-a1e92e977ce6 | -11.8755 | -43.863602 | 2026-05-16 00:47:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b855e89-4634-37db-85fa-28638e896058 | -8.7044 | -47.980301 | 2026-05-16 00:47:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 850d60de-2cd4-3397-9bb2-04cef0a94d2a | -12.8515 | -43.7537 | 2026-05-16 00:47:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1728f146-192f-3900-b91d-4c1e8ab346c8 | -9.4616 | -47.819099 | 2026-05-16 00:47:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98414560-62be-3397-9d69-c77cffd73902 | -8.0919 | -44.1395 | 2026-05-16 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c26af8bb-3dbb-3adb-bd81-45ed6ce834b6 | -11.8785 | -43.875599 | 2026-05-16 00:47:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 663d5474-7589-3607-8a6e-2ee0f8c43150 | -13.0341 | -49.943199 | 2026-05-16 00:47:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 406ef999-d5b3-34b8-bb27-a5d7b65a9151 | -14.1823 | -52.8713 | 2026-05-16 00:47:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a24e79a0-8c7b-3f52-a888-4f95b3020030 | -11.5953 | -48.0242 | 2026-05-16 00:47:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c02a9af-d2b6-3bd4-b578-467c04460c21 | -10.9148 | -54.119701 | 2026-05-16 00:47:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4fa3abad-63b0-36cd-9f40-71572491d18e | -8.0854 | -44.1129 | 2026-05-16 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3eb3314d-5f27-3b8a-8b8e-1b40b8b1a1eb | -17.35 | -42.6092 | 2026-05-16 00:47:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bcad4256-8e7f-37d7-b669-d24d06774cd3 | -11.7488 | -44.5215 | 2026-05-16 00:47:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5454dfc9-e932-3eff-9bb8-5101d1b1d19f | -14.1743 | -52.882198 | 2026-05-16 00:47:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ab89813-f55f-3d7c-b70c-1ce0d11cbd62 | -8.7026 | -47.972401 | 2026-05-16 00:47:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04d24152-b972-3026-ae40-5749e2c972b2 | -14.1761 | -52.890999 | 2026-05-16 00:47:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cfbb985c-40da-3a38-bd10-6d188fab305d | -12.0273 | -47.7952 | 2026-05-16 00:47:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41b3c3d5-87d0-3933-9fb2-2fe2fa105c6d | -11.8725 | -43.851501 | 2026-05-16 00:47:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9dbdfd3b-50f1-3c35-b6c7-baa63cbe83c1 | -8.0887 | -44.126202 | 2026-05-16 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 121ae27d-3cab-3eba-9d3a-26b0457292b4 | -11.7461 | -44.510399 | 2026-05-16 00:47:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b83cb00-5235-37a2-8cf8-f2e8ec73cf79 | -9.7903 | -48.076199 | 2026-05-16 00:47:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
