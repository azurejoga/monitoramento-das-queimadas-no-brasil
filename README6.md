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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37c649cf-bbb0-32a1-94bd-6357f15228f1 | -3.3452 | -50.4917 | 2024-11-18 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| a41bf329-3be7-3099-ac14-3036b5f7afe5 | -1.6962 | -45.8311 | 2024-11-18 00:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 148.1 |
| ee395a8c-7adf-375f-9997-ffc1d30fe0c5 | -2.8608 | -51.7731 | 2024-11-18 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 9ab0e2dc-4e30-333f-a777-60876769edc9 | -14.3052 | -57.6222 | 2024-11-18 00:30:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 7f81beee-6991-3937-ba9c-59ae008ba2aa | -2.7844 | -52.5954 | 2024-11-18 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 5339f5d8-d96c-3889-a2f7-4e11630a2e18 | -4.5771 | -45.6325 | 2024-11-18 00:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 2063cc9b-21fb-38e2-a9e0-d5b122de0dbe | -3.6593 | -50.439 | 2024-11-18 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 8f5a57ec-1b9e-302a-9a65-0d6227007b65 | -1.7148 | -45.8084 | 2024-11-18 00:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 9d19018e-c2a3-3d14-825c-6a11bb2394ae | -13.021 | -56.4544 | 2024-11-18 00:30:00 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| adbe5e39-1b1b-325d-8d4f-1901cc70a895 | -2.5847 | -51.7181 | 2024-11-18 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 24535f0b-7a87-3388-92ad-ff667bcdd0a6 | -2.8791 | -51.7932 | 2024-11-18 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 2193ab8a-5860-33a0-b95c-39abdd109544 | -14.2857 | -57.6442 | 2024-11-18 00:30:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0a16183d-0a26-38fe-b0c8-49097f526ebd | -2.7843 | -52.6158 | 2024-11-18 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 511932e0-2164-32f5-af7e-4ca957dd0020 | -2.7659 | -52.6163 | 2024-11-18 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 293.1 |
| 90d62439-eead-34cd-9403-abee655de690 | -3.1827 | -45.4514 | 2024-11-18 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 127.0 |
| fe14a868-787a-3803-afaa-765f40a88082 | -4.2685 | -50.5832 | 2024-11-18 00:30:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 46ac9ada-3a81-3e3f-8b91-e7ca9cc4d541 | -3.0764 | -53.2796 | 2024-11-18 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 60990f37-4286-3ef6-acfd-22a494e8b776 | -1.2964 | -51.7204 | 2024-11-18 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 9dc268fd-47df-35a7-8669-b70a6a74e77b | -3.6778 | -50.4384 | 2024-11-18 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f1bfb3c2-6a96-3fd9-85b3-f90fc036a664 | -1.7147 | -45.8307 | 2024-11-18 00:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 126.7 |
| b22f7a46-9bed-391d-9b33-80d951682ed5 | -3.7564 | -45.9422 | 2024-11-18 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 147.1 |
| ce9a63b1-404e-34b2-bf78-400a43d8414d | -3.1827 | -45.4514 | 2024-11-18 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.4 |
| f644a8f9-9eec-334b-a3e0-daf8a240c13a | -1.2964 | -51.7616 | 2024-11-18 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| ddd8cb8b-77a9-3fae-ada3-3d2a55a05b21 | -3.5678 | -50.2534 | 2024-11-18 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| dff05ab6-0f15-383f-bbab-8ccafdcbdd56 | -9.9894 | -36.2226 | 2024-11-18 00:40:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 95.2 |
| 1156632e-81e2-3f5a-8c04-765de62df5c0 | -3.775 | -45.9413 | 2024-11-18 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 133.0 |
| d6733a05-dee0-3be2-b32f-6dbc4cadc23c | -2.7843 | -52.6158 | 2024-11-18 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 526d4ed4-d5ac-3d5f-a9a9-cf7f6a72aea1 | -6.5216 | -35.194 | 2024-11-18 00:40:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 108.2 |
| 1076fd25-ba11-39ec-9cfe-3e4f6ebdf41d | -3.3452 | -50.4917 | 2024-11-18 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 28eed69a-ce4b-3c8f-97d7-2a01372da8da | -14.2857 | -57.6442 | 2024-11-18 00:40:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a63d3767-389d-3f19-abcf-f4a994840f24 | -2.8792 | -51.7726 | 2024-11-18 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 3b03cc18-8aae-3914-bb1b-0c737efe96ad | -1.3148 | -51.7408 | 2024-11-18 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 202.9 |
| 0e88ccb5-78dd-3f90-b0ea-9efb02a1b570 | -1.2964 | -51.7204 | 2024-11-18 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 4f949ae5-c78b-3bc0-9bb0-a7e4cf6e39bd | -1.3148 | -51.7202 | 2024-11-18 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 31fdc2d7-cf13-3828-90ab-144e0b96c08e | -3.0764 | -53.2796 | 2024-11-18 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 0ed6ac11-baad-373f-a319-b89e34b9de43 | -5.9556 | -48.0642 | 2024-11-18 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7fc66de8-b574-3fd1-979a-58cfab18e998 | -2.5846 | -51.7387 | 2024-11-18 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 55e8af3d-2248-344b-974f-4efd7c58bb02 | -2.766 | -52.5959 | 2024-11-18 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| f878e224-8567-3ad3-bbc5-1f973787992f | -3.6778 | -50.4384 | 2024-11-18 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| dbd8baab-6e8a-340a-aeaa-2c7d2ad50f4d | -9.9889 | -36.2497 | 2024-11-18 00:40:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 58.8 |
| 0aa053b2-a7c0-35d7-af2a-5ad9d0fe6dba | -6.5407 | -35.1917 | 2024-11-18 00:40:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 128.7 |
| 5b716c43-5ae2-345b-a644-a6fe618d17cc | -2.7475 | -52.6167 | 2024-11-18 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 67c6bbeb-dc2d-32ea-9997-d9c45f55d157 | -3.6593 | -50.439 | 2024-11-18 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ba24bb03-18ca-3a83-ab9a-267160b66558 | -1.2964 | -51.741 | 2024-11-18 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 349.9 |
| dbb405cb-99dc-374d-a057-6eab4300c264 | -2.8607 | -51.7937 | 2024-11-18 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 119d5187-cc2b-3a68-abd2-9b4e119f8f46 | -2.8791 | -51.7932 | 2024-11-18 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| f10a2ce2-7153-365f-96c6-d63905a5cd15 | -1.7138 | -46.1866 | 2024-11-18 00:40:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 037dbae7-6dc2-3c9f-902a-dcf86d47f6f8 | -2.5847 | -51.7181 | 2024-11-18 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 7e70a11d-a4fb-37ad-a2d5-2587565cab6b | -14.286 | -57.624 | 2024-11-18 00:40:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 73cf644b-ffab-3ada-8159-24456a7a079c | -2.8608 | -51.7731 | 2024-11-18 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 93b1c391-b315-34f6-8d26-525ab1d1fbce | -2.7659 | -52.6163 | 2024-11-18 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 243.9 |
| 9e9ceba7-c4f1-3782-8698-c79a188b53f5 | -1.6962 | -45.8311 | 2024-11-18 00:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 49cfd079-d849-3033-b4d2-d9c96ba71b69 | -4.5771 | -45.6325 | 2024-11-18 00:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 8dd22b06-a117-3a0b-b593-212b7b982a6d | -3.0542 | -54.4081 | 2024-11-18 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 40c06240-dd97-3e94-b5aa-532297d3cfcc | -2.6028 | -51.8001 | 2024-11-18 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 824664be-10bc-37bb-8837-0723834794c8 | -1.3148 | -51.7614 | 2024-11-18 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 2fd8f2d6-1725-3c38-b7e4-ba1cec7ac958 | -3.3267 | -50.4923 | 2024-11-18 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 88f7ad53-9a5a-3016-8e29-35fb6474e57a | -2.1766 | -50.333698 | 2024-11-18 00:49:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6f0e884-1ce1-36a5-92bc-47c400bbbbe5 | -2.6772 | -45.707699 | 2024-11-18 00:49:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 382eda5c-598e-3ffe-acfc-746ccfec57b3 | -3.0561 | -53.278702 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd6fb5d6-10e9-3552-877f-e451ae728e60 | -3.3373 | -50.503399 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6e9c31b-c14b-3915-8e43-c82aae3609b4 | -1.2973 | -51.752499 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d5ca89c-c878-3a44-a141-9dcbde364145 | -3.027 | -54.104301 | 2024-11-18 00:49:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 976122b3-207b-3260-b213-72bc80a226c8 | -14.2931 | -57.621201 | 2024-11-18 00:49:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf5542b2-6a32-3cae-8d5e-d302cfcd5fde | -3.1316 | -52.9762 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e0debe2-d69d-3101-b42c-4a3d87d250b3 | -0.3847 | -51.539501 | 2024-11-18 00:49:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 66cb02d0-104b-3285-9bcd-229a9fbace80 | -3.5711 | -53.277401 | 2024-11-18 00:49:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c7ff91f-7da7-3b06-b0ea-3a377a58f3b1 | -1.2014 | -51.783199 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b375ff3d-0ac3-3134-a119-80fd037d2271 | -3.375 | -53.3214 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ecf56ba-27cb-32f1-8271-9580636e4a84 | -2.8238 | -46.674599 | 2024-11-18 00:49:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 698587e6-ebb6-306a-825c-49656026a806 | -2.7588 | -52.606499 | 2024-11-18 00:49:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ae417d8-d94c-350a-8188-52c555bda2a0 | -1.2913 | -51.726101 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0260c338-3cbd-3f37-ac8b-0321ab891cd3 | -3.0812 | -54.663101 | 2024-11-18 00:49:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1adc7e3-8fbd-302b-ad99-9f00c3cc6f41 | -0.9521 | -51.7276 | 2024-11-18 00:49:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 62cdcf4e-2111-3b97-8f77-b6e91db4d2f5 | -1.1303 | -51.697102 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0a9866d-9853-325b-bac2-7d575bad2749 | -1.1974 | -51.765701 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44b3596e-a237-308e-a7d3-72fcf8ff6d5f | -1.2093 | -55.821701 | 2024-11-18 00:49:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10299d75-ac80-387b-852b-339160535ff2 | -5.5202 | -43.2864 | 2024-11-18 00:49:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4b5582c-698e-32a0-9cb5-df262923526c | -2.5938 | -48.317699 | 2024-11-18 00:49:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55b86692-40eb-3025-a973-43959d2098a8 | -5.1325 | -44.362301 | 2024-11-18 00:49:00 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86d4004d-46d5-30dc-9c48-ce27c4e0267a | -2.5479 | -53.991299 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55ce0486-d448-3149-9e08-615ed300479d | -1.7551 | -50.7383 | 2024-11-18 00:49:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 572b45cb-7f44-3902-9427-542afc369805 | -2.5787 | -51.7281 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec30b437-2234-3ffd-ac66-98f44665f2b5 | -5.5539 | -46.4291 | 2024-11-18 00:49:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6949bf6d-da21-3a05-ae71-f192054f5359 | -3.1012 | -53.749699 | 2024-11-18 00:49:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95788135-a45f-346e-ba04-7b6d645a522d | -1.6261 | -53.2896 | 2024-11-18 00:49:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29e7b402-3721-359c-bace-308d860f9a0e | -2.6078 | -54.256001 | 2024-11-18 00:49:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e196a7e0-4842-3b50-b745-34ba32d88747 | -2.1689 | -50.6134 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba08c663-d0fc-3300-9ba4-d1f2d15990d8 | -3.4393 | -50.8116 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8b6e512-c26d-384c-9ef4-c90576c8a4df | -3.3153 | -46.0271 | 2024-11-18 00:49:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a75fcf4-0c35-3780-bc38-385db7fa664e | -2.6378 | -53.9786 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c50dace6-83de-382e-adda-f08d651495b7 | -2.8605 | -51.789101 | 2024-11-18 00:49:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b35a4715-723e-31e1-8854-9ecb45d83806 | -2.6657 | -46.221001 | 2024-11-18 00:49:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7873b7f3-bef8-3059-8458-1eacbf09b199 | -1.9542 | -48.391201 | 2024-11-18 00:49:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bfd3f18-33f6-3e99-a8f1-1086d703c9f1 | -2.5578 | -49.135101 | 2024-11-18 00:49:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fb79b9c-51d0-3241-a819-588eb4e74b2f | 0.9779 | -51.1488 | 2024-11-18 00:49:00 | METOP-B | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 290c23e6-ce39-3189-90ae-b50290e2a5e0 | -13.0223 | -56.448799 | 2024-11-18 00:49:00 | METOP-B | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f90e99c-13aa-309f-8563-b00d1152d3f2 | -4.5474 | -48.544102 | 2024-11-18 00:49:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cf96b36-2002-34aa-8d4d-7516deed622d | -1.6248 | -55.151001 | 2024-11-18 00:49:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf6bc04e-d184-3138-b4d9-5db865fb3fc6 | -2.5962 | -51.804401 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
