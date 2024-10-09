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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f85cc6d8-356e-3290-bdc1-0e513cca4b60 | -22.16968 | -48.09754 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7004e308-4e6c-3871-a55f-25663bc6113c | -22.16816 | -48.10354 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d28d1114-ec75-3a78-9598-37023ef96b91 | -22.16726 | -48.09676 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ea5f4d2-6c7f-32ee-8646-4884c945e961 | -22.16463 | -48.08956 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 700d2af7-b8f3-308c-9363-a9c5d40200d4 | -22.16313 | -48.09544 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16fc05e8-0bc3-34e7-85c8-3dd93ddcd33c | -22.16215 | -48.08883 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| fbe61f77-f6c3-389a-87a2-aaf773dca469 | -22.16069 | -48.0947 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ad99f7fc-8807-306a-b907-90b4b0629281 | -22.15922 | -48.10065 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5435b6d2-481f-3045-9a63-02ca90528e49 | -22.1567 | -48.1207 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 483d3612-7e3f-3026-95bb-559385209390 | -22.15561 | -48.08664 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d5291bb9-6be8-35ba-8e27-4e455b5fe77d | -22.15505 | -48.12719 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39ecfdcc-31b3-3884-b0f8-52439418306f | -22.15443 | -48.11996 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f21a3ae9-e0d4-3f80-9489-fd67e81c9ae9 | -22.15413 | -48.09262 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b3164851-122d-3cc3-8b1b-b502b79c5692 | -22.15331 | -48.13401 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bfabd6b-bbea-36ea-aab6-c5d6ad3c79bd | -22.15279 | -48.12659 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 929b9ff8-98ee-39a3-b092-175a1293f554 | -22.15261 | -48.09873 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 60278e9f-9441-339a-8566-85bc77b7076c | -22.1511 | -48.1334 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 84eecbc6-5179-397d-943b-83d91a6ff66c | -22.1494 | -48.14022 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffcc8b5c-96b6-36e3-82a3-c4dde6e46a45 | -22.14605 | -48.12514 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 20b9931b-2c25-38b2-a4a6-e75278dc1291 | -22.14438 | -48.13186 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 014e7cc6-efb5-3523-9654-23d7e03438ff | -22.14273 | -48.10996 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2554adc7-8ae3-3d7c-834d-f566df403254 | -22.14271 | -48.13859 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f750eece-90cc-392a-b1c8-2f04c3cf1b97 | -22.13932 | -48.12368 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4652ac92-e0fa-38f9-a1ac-6ccf08225a68 | -22.13622 | -48.10764 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f84f2d7-c767-30d1-bb4b-ae38b3d6fdba | -22.13274 | -48.1216 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c4a17be-75b6-3eba-bd05-fd5d70ae0ad0 | -22.131 | -48.12857 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cd5026d-3788-30c2-857c-247e417a69b9 | -22.12937 | -48.13512 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13eede5e-39b7-398b-8fc8-122aaf679aa6 | -22.12619 | -48.11942 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5c47f83-2899-3fad-9721-bfe7feb21c77 | -22.12451 | -48.12617 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea859c08-17ad-3b73-a358-5753bf282c6a | -21.65509 | -47.70953 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 058ee441-8faf-3f08-9371-c6e4a60f9faa | -21.65359 | -47.71556 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2c9f7bf1-511d-3573-b6b8-3c6af9a2f452 | -21.65156 | -47.70845 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a92d5d9d-9b6e-334e-a634-535532b67f15 | -21.65009 | -47.71454 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e6fba406-b9ed-3201-9473-74c571f075a7 | -21.64859 | -47.7075 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2db37fe5-3757-3c9a-bc1f-49386fec5213 | -21.64708 | -47.71359 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 61b49bae-832b-3560-b574-d1603c185db7 | -21.63903 | -47.71777 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 387fc6a6-c864-3def-ae56-3d151116b651 | -21.63704 | -47.71066 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 211abff4-d3d0-3007-866f-b6dd91ffed69 | -21.63552 | -47.71695 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b97c7a4-1665-3fdd-b54c-8584906a5036 | -21.63403 | -47.70973 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7104a2e1-0375-31b0-a1b8-5b8d4f1f8a82 | -21.63242 | -47.7162 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ad9eb63-928d-39fc-a047-66560a702625 | -21.63055 | -47.70859 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48e05687-fe22-3760-987a-26290b9bfbee | -21.62913 | -47.70127 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdced50d-1f67-3c97-9f16-b2f895d32eb8 | -21.62893 | -47.71527 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba40807e-898d-3a17-912b-b1d5f128069a | -21.62754 | -47.70766 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24f5eede-9f08-30d3-a729-76bbb6cead9b | -21.62587 | -47.71436 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b744ebb3-6225-3c15-808e-e571c3482a2e | -21.62407 | -47.70646 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8f0d6d3-0cdb-3bfe-b2af-139acdc2356c | -21.62243 | -47.7132 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25893528-2d2a-325c-8713-e0b2cfab80b3 | -21.62104 | -47.70564 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4b0b6c3-eb4f-3140-a5f2-1f36cea2dbf0 | -21.61938 | -47.71228 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43570960-dd9b-3439-9059-637083d8ae3a | -21.61765 | -47.71918 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 847417b1-f5e4-3a34-9347-d3d8e9045119 | -21.61603 | -47.7257 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3d5ce020-e7b5-3565-af85-2e6fdfd04c29 | -21.61592 | -47.71117 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 25d70ef7-bbc2-3bb7-aadc-b44467a71ea0 | -21.61426 | -47.71803 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f9a0dc77-3667-3571-980e-8cdba9be008d | -21.61267 | -47.72458 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2c27feee-d225-3b86-8db5-cce99958b8ae | -21.61248 | -47.69658 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcf43116-9421-3c5f-b7d0-42f62f46b133 | -21.61117 | -47.7307 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c6b02f30-7e76-3905-9d64-5892619422a2 | -21.61115 | -47.71714 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.4 |
| dba4dc27-315f-31be-ba08-80ebfa792391 | -21.61022 | -47.67718 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 99b531f6-00a8-3da5-98df-72e710fd30e0 | -21.60954 | -47.72358 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e1bd8184-2424-3c8f-91a7-5e8636c0f11a | -21.60881 | -47.68296 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77b1abac-0f81-3f70-a8e4-e931e36f0eba | -21.60804 | -47.72955 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 910688d5-45b2-30c9-86bc-13c023f3f852 | -21.60741 | -47.68869 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd87c924-3d7c-3194-b67d-62ddea6bea2e | -21.6062 | -47.72237 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ce453999-20c2-3d10-ae1f-64fbbd8320e5 | -21.60599 | -47.69449 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d55beeb2-8ebe-3c31-baec-d720a39ab70a | -21.60448 | -47.70067 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7811104e-2137-34ac-b8b0-785b9f0452b0 | -21.6029 | -47.70716 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05f0adf6-e623-3186-9e2e-0c43940a8799 | -21.60229 | -47.68101 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 723cd29a-26a0-3ead-b5aa-3d12847039a5 | -21.60134 | -47.71353 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6614a3fe-b796-3d1a-8e10-ab3ec36762d4 | -21.60085 | -47.68691 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64d3a150-3dac-344a-9b5c-43b9afa0fdf2 | -21.59939 | -47.69287 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdddf002-7863-3ea1-9dbc-d054c3778499 | -21.59793 | -47.69887 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d564d597-a0ba-34c5-afee-cc0d239f5029 | -21.59649 | -47.70473 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d812009d-d244-37c5-af0e-0a3d6a910271 | -21.5951 | -47.71041 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1546ae6-c4ca-30ec-ad24-bf1b0e5d91ef | -21.59373 | -47.71601 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20477ea1-926d-3eed-83c6-ff231f5e882e | -21.59226 | -47.722 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcf5371c-2690-3300-977b-a5ab5fd6b9e5 | -21.5887 | -47.70793 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0df85b8-ebaa-3d29-a75c-e212a1023845 | -21.58741 | -47.71317 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 017d4043-16d5-3613-a9e0-187935bcfca0 | -21.58069 | -47.8846 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4ab0833-57ef-3bd2-88e5-81d2a5080d07 | -21.58064 | -46.98672 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 509d680d-9be5-3cbd-a6fe-56aa7ca4ce39 | -21.57981 | -46.98518 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1d7ec54-b7c6-3349-97ad-97cc0c0d63a4 | -21.57915 | -47.89093 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 089ef353-26a8-3460-be74-24e6b3b30f4b | -21.5783 | -46.99156 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13bde2de-4e84-33c6-9cb4-9ddeee4c9537 | -21.57685 | -47.91032 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99335b14-0f88-3457-91ec-51732c823a61 | -21.57659 | -47.88312 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a05abd6b-cab7-3871-966b-62c06bd51e8d | -21.57501 | -47.88941 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3a40fde3-2579-36d7-932b-2ce89e92a11d | -21.57454 | -47.90979 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7cf95077-0dc3-341a-89be-da2a345735b8 | -21.57445 | -46.98451 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b9031e4d-54a3-3c30-9ca0-8651b4b161a6 | -21.57413 | -47.88249 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0e3e35a7-3694-3f28-804e-6e46cbde7709 | -21.57361 | -46.98302 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 172883ca-e9bf-3af5-8f52-2f2489735e82 | -21.57297 | -46.99056 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8fd73af5-1327-3c3b-af13-e99aa32114d8 | -21.57258 | -47.88883 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5f2ddfe3-9867-3a12-88a4-a2ff3eb455dd | -21.57212 | -46.98926 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6eca86f-9914-32cd-8380-616fc19e8d24 | -21.5703 | -47.90813 | 2024-10-09 03:25:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48be6404-18e7-37e9-bcdd-8caf192063be | -21.5682 | -46.98253 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1ee2c185-c314-3b91-8074-ee68440852a6 | -21.56733 | -46.98114 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db6a5e6d-9019-3149-9629-5c21e20da989 | -21.56102 | -46.97941 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edd95371-6b4b-38c6-902b-17d156bbbac3 | -21.5597 | -46.98494 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a30dc586-59ac-3519-b0c3-cc9ed76ba9e1 | -21.55833 | -46.99067 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4faa3079-37f0-3a06-a1f0-f676c21e7f96 | -21.55484 | -46.97713 | 2024-10-09 03:25:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 865919f0-92df-38c7-b009-35e890eb9273 | -21.54342 | -44.15462 | 2024-10-09 03:25:00 | NOAA-20 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README65.md)
