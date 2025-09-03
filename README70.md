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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71d04383-7b30-37fb-818d-ec7e11116f28 | -14.56013 | -53.04929 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41c9a81b-4586-3fcf-af06-9022afcb5913 | -14.56952 | -53.03263 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b49fcfe-92d9-3977-ba04-2082d38b6302 | -15.59985 | -52.67887 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43b55dbf-eed2-353e-81be-9de3b1b482f6 | -13.49498 | -46.81829 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f757fd55-edf2-33ed-b6ad-2055a30ef941 | -12.90312 | -48.09588 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6e04283-f7a4-3030-aae5-d860445079b7 | -15.01558 | -50.07158 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7410a78-273d-3729-aba0-4e311d4ac3b1 | -14.06027 | -44.56627 | 2025-09-03 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e985cbf-efb2-3d70-8b79-6547e89dfcb2 | -13.90536 | -48.1155 | 2025-09-03 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c69737c-d200-3cd2-8d7b-9672e076438c | -14.97237 | -50.20233 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 013346c8-7ad1-352a-92f8-f8bf559e8eaf | -15.74141 | -53.69082 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 308d9473-3ef0-3122-b3c0-16dce57c6423 | -13.01569 | -56.8738 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2ff7102-74b8-39c1-bc52-1eeb1dda9e77 | -12.80989 | -48.0512 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f99bfd27-cf1c-3c6d-bf73-501622a3dfdd | -12.79718 | -47.64809 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99875fde-12eb-3ddd-b790-54be8ac3f21a | -15.11856 | -48.16736 | 2025-09-03 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20c9c524-5c05-3515-909b-67b1e542ac49 | -12.52803 | -53.8241 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccbfff77-2a1f-344a-9a36-f5c26c552582 | -15.55374 | -48.40389 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59a9ae5a-8d67-3064-815c-2d1888e54bf1 | -13.90401 | -48.1255 | 2025-09-03 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dba47c3e-b393-3e4d-82d7-0e6429165f09 | -15.01318 | -50.06256 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dff8789d-0b31-32e2-a55c-329e05028298 | -13.70755 | -46.9411 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73042c08-bcfd-31e9-b80f-331825a389fc | -12.94016 | -56.99287 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 693bb634-1289-3101-b581-e56d37750b09 | -13.30647 | -46.84562 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65f99b24-411c-3d68-82a8-df8c7bc7a324 | -14.58188 | -48.05289 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71ee1189-3ab9-398e-b545-75b1e29701b6 | -14.9857 | -50.05975 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32ec5401-af49-3181-9ecc-4d5c6ac1ef25 | -16.53679 | -55.06919 | 2025-09-03 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| feb4f3b5-b703-367b-adc5-1faee10cdf91 | -14.59497 | -54.57932 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9248faa0-660b-3724-b00f-922de90ced6c | -13.49978 | -46.81476 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 028542e9-b89a-3c2c-86da-3de10d88f441 | -12.18145 | -53.88221 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fb5e12b-b42c-3f10-b735-fd42f469b7d5 | -13.70669 | -46.88023 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38a9084e-b383-315e-ab78-6b5f8c9bc5b5 | -13.51035 | -46.93423 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e2992dc-7e66-389f-b293-d12aa3da3d16 | -11.86277 | -51.53957 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61d13b1d-36d6-3b65-9d30-ee5a0ece9d16 | -13.32035 | -51.7655 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62692ac5-b7cf-3ce4-aaee-bb4a2f02e204 | -14.05337 | -44.62303 | 2025-09-03 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4844e87-89b7-331b-a8bb-35d8d323df68 | -16.30768 | -52.96033 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e146c11d-657b-356b-8501-41319c41afde | -12.94395 | -56.94888 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1cd8907f-b91f-3107-aba2-7bdf4ba355ef | -12.92021 | -56.99439 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b66fe935-a1da-3813-aed4-3ae398ef8ad8 | -14.31166 | -53.09193 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4df24163-331f-39d4-aece-6e9389ccab48 | -11.87209 | -52.42532 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b91e785-4cce-373f-b40d-c61f8d47c042 | -15.72171 | -53.64355 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9361ee8a-1474-3166-8308-c45324a86e85 | -13.08993 | -57.12178 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 438fa02f-e2f3-3a8d-8fb0-b4effc905a9d | -15.00659 | -50.05736 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 13e99870-0289-3160-85c9-e876637f5435 | -13.90679 | -48.10491 | 2025-09-03 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e4f7ac92-b8d5-31f2-89a3-ff40ef83ade9 | -14.56511 | -48.05649 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bcff44fc-d46b-3feb-846c-94e584bada16 | -18.1309 | -48.57264 | 2025-09-03 04:49:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aea0bc3a-5908-322a-b64b-d5e305b828de | -12.49904 | -55.73833 | 2025-09-03 04:49:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b200b7b8-f98e-3219-be12-b74baf9ec344 | -17.53005 | -47.58522 | 2025-09-03 04:49:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c5b31409-d97a-3d5f-960a-e9173ef0a76d | -14.57346 | -54.54138 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8140621d-56bb-3055-ad7d-75e84d413d1b | -13.49987 | -46.82025 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a36f8f5f-dcb7-3528-8a21-22aadfeaeb5f | -12.79077 | -47.66511 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 250610df-ab6e-3ec2-b3ff-28fc6bf347bc | -12.96567 | -48.08133 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97ca2e97-8b0a-3eda-9b0e-46f5a832a962 | -11.95781 | -51.3419 | 2025-09-03 04:49:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c8f42ea5-da46-3005-9cad-aa02eb66362b | -11.66924 | -57.35421 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cd8d2874-62c8-31f7-b448-8cd24f3d5994 | -13.01115 | -48.09759 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8396e172-9651-31b6-92f4-b9109905a637 | -15.9981 | -54.13226 | 2025-09-03 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35013618-f046-3b4d-98b3-a92b2cdfd927 | -12.84973 | -48.02219 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 00f5a9d6-ca1d-3f16-a205-799015d4d333 | -15.56824 | -48.41632 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3d67cac8-31f7-36d0-8ef6-696277d6285c | -13.5113 | -47.02541 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 236ed3f3-047f-3303-8ecd-7afc821ea738 | -12.49891 | -53.83408 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2825d1a2-f1ec-3140-8511-760a32eecfbd | -13.73483 | -46.93078 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2da74bcf-8a29-3b29-b130-1251d63b5837 | -14.35316 | -52.80449 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de6d40bc-41db-3d12-8747-d4a995a1f376 | -15.01974 | -50.06802 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 735f664a-7ffc-3bf2-a7dc-d7c5b17155a3 | -15.56086 | -48.41853 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 68cabd97-03f1-3fa2-83dc-194f4b29472c | -15.72502 | -53.64411 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 886a40e8-90e0-357c-8939-4e08af932a23 | -14.61106 | -48.018 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f078993a-885e-3449-a36c-00e3a0cb4c65 | -13.99004 | -49.55621 | 2025-09-03 04:49:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ad2cae2-27f3-30e5-a56e-36c59cce5125 | -13.70809 | -51.94059 | 2025-09-03 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28c9a7e8-6265-37f3-8ee5-d838d51c0406 | -13.2868 | -46.83293 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9c46fa1f-48ef-393c-a224-c1f2cf6a6dff | -15.60372 | -52.6758 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62cd5365-c1ef-3cb9-9fb3-d6bab197e291 | -14.56907 | -48.05733 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50f37f54-5817-3df7-bd7d-565d68d76ca5 | -15.59267 | -52.68139 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1eead496-d783-33aa-a9e3-5ec35660bdf8 | -12.94439 | -56.96874 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d866e36-e217-38ad-80ee-585f98c35e23 | -13.99064 | -49.55188 | 2025-09-03 04:49:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f57ecde7-8ec7-35f0-a231-3d74cc964311 | -12.93705 | -56.94917 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2afdf938-ad02-3940-bced-a64d35148093 | -12.51757 | -49.58125 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af1028ff-7f75-3bfd-8357-3edc372d485d | -11.66589 | -57.34999 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7528407-f75f-3504-bd3f-b758cd6374f3 | -14.80843 | -48.21424 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2357c9ff-fd3f-30e4-8fa8-0a834cb2400c | -13.73861 | -46.93493 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| faef8869-f57a-3818-8148-8bd5576ee8df | -15.24527 | -53.79484 | 2025-09-03 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23689ab1-eb53-39a0-aa89-a3c3b35e6cf6 | -12.63719 | -56.99084 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c035ed4-f03c-3135-8a6e-a828f831f8c9 | -15.0096 | -50.06203 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e45267ef-f5b2-3a8b-999d-564657e688b6 | -13.29936 | -46.93299 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3870b6e5-4555-32be-bcc8-3ee770e2a07f | -15.02274 | -50.07271 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 96151c55-6186-379b-a065-b618e09241a4 | -15.55829 | -48.40786 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf985650-a79e-30f0-906c-3d19fd5ff7e7 | -12.97348 | -54.75864 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a9b92a1-c181-31cf-9382-2c4c69429947 | -12.49231 | -47.47772 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8e821c6-db01-320e-825a-bdd4c77b2b0e | -14.55036 | -51.94102 | 2025-09-03 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c47417d1-4100-371b-9fb9-de5fbdaaeff1 | -14.34325 | -52.80287 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75aa10ac-71bc-3af5-8bb6-7e86dabd8434 | -14.58338 | -48.04174 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0231c844-bd2a-317a-bec5-f2f63d8333e3 | -15.11953 | -48.16014 | 2025-09-03 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d535633-ef4d-3ed8-9447-1a09407d6ea7 | -17.36559 | -49.18177 | 2025-09-03 04:49:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a10c904-2428-3fde-93d7-02c21c4407e0 | -15.72228 | -53.63999 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63f17ca3-5472-3959-ba34-f2243616160f | -12.94311 | -56.99845 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 425f9b1f-1f52-38b3-a300-f73c73a28bfa | -14.57838 | -54.55367 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97f434b2-d91f-3794-bb6b-d22cb6e78ca2 | -12.48685 | -48.04364 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99243fbf-cbcc-3c7b-a958-19dd1431959a | -14.58822 | -54.57821 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ab41577-7149-3096-8b6d-d645f1201dc8 | -13.50411 | -46.82103 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b01bf23-8673-37e8-aaa5-ecac2ff303bd | -15.54966 | -48.35274 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fd53e8a7-22de-38bd-a728-ea6d8db4be71 | -12.89347 | -48.08567 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63c5560b-c0ac-3d6e-b832-0ff29039a7b4 | -11.85203 | -51.5234 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c94d8a63-08e0-326b-9164-8b4d43f06623 | -14.56305 | -49.14705 | 2025-09-03 04:49:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca97cab6-a23b-3932-bfb4-2ec9cd3b10d1 | -11.85999 | -51.53548 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README71.md)
