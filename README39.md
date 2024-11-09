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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 899f6946-295a-3566-8e0a-46b647d6fb0a | -2.2875 | -50.68076 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ac13acf-cdc4-3d46-8145-cb263ec1b783 | -2.22679 | -46.43287 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32f06848-7ac4-3921-aa69-c17bd6092d76 | -1.54346 | -51.85315 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6c45d69-7e67-3c84-ba59-9220abb4f03e | 3.74435 | -51.60929 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a5f6bc0-f23e-3320-b99c-8c9d5d10ede6 | -2.78848 | -45.96611 | 2024-11-09 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fc6a4ef-2ca4-3131-8f41-0f1f6d6e29cc | -2.58918 | -48.16375 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bdfdc10-5ce9-32b7-8294-4d1bb1e4c89c | -3.55115 | -43.57574 | 2024-11-09 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 885d39bb-9ac2-33a2-ba6d-9147dfa2f822 | -2.37379 | -46.73483 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbc3bd90-39c2-33ad-b8c8-1a3b206d920b | -1.51559 | -52.18126 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9d4c2dd2-a246-35c6-9509-a94471393695 | -2.04135 | -46.59843 | 2024-11-09 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 609167c5-4e83-3e84-8282-e2a578518ba0 | -2.34381 | -50.51667 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47881f09-f79c-3dd4-9d4d-e6612f57d1bb | -3.15133 | -46.50223 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9cba671-d92f-3974-a8a6-a9a9f798ce2f | -1.59623 | -52.48792 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f0f640a5-ab80-31b8-8dfd-a9dc5b3e14b8 | -2.31151 | -46.47845 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfb564e7-9d54-306a-a8bd-05b113afe4f0 | -2.69982 | -46.69419 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c41203d-399f-3e41-a87e-b0a358adce40 | -2.62232 | -46.16341 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2bbd0ded-ceff-3dcf-82ac-f0e72a26c39d | -2.38826 | -46.77224 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5e2f337c-fedc-3f38-be4a-5f558f9b8746 | -2.37972 | -46.58774 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a3e595d-7a02-3011-8ef7-b2103d091471 | -2.19658 | -48.95925 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6eb5229b-b8cc-354f-9f62-614052ae9d42 | -1.54804 | -51.85025 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 424598f5-0309-39d5-9810-e91e0e7d82c6 | -2.17604 | -46.43215 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69279ba7-46b8-3a87-ac48-17d9dc49c27f | -3.50408 | -43.98166 | 2024-11-09 04:31:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5f3c920-65a5-3a70-9b45-b74943d0bc70 | -2.5692 | -48.18222 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c77d01bd-d977-38f5-bb32-727caff1c75e | -2.55366 | -46.18861 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1635fd43-8415-362b-a40e-ab71b687c30a | -2.1876 | -48.55161 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b7ae0b5-4e8e-3d99-aae5-e0780d7cba37 | -2.34335 | -46.57869 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a2d659e-c61f-35dc-b6bd-39bfef0a6c4e | -2.44584 | -49.18377 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8803f299-efc7-30fd-96c6-6a1f8f32952a | -2.20795 | -50.33625 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac22de21-6b81-349c-a3b0-9b610d74ff45 | -2.07187 | -48.50818 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 457ba1f9-aedb-3957-8eec-f52207b044dc | -1.9146 | -51.49892 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e5980fa-3eb8-3234-b8eb-443ba092d0f0 | -2.42752 | -46.30123 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c6ff3a60-4b0b-3631-9e05-d5b50b71ba0d | -2.21656 | -50.72978 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6311ea7-8c48-3597-a3ac-2532bf3829d7 | -2.69768 | -46.70797 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a225032-0f15-36dd-87db-810f071c7bac | -2.38389 | -46.7786 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 157dfa0d-11cd-3c2e-9cb4-1d050a3a6f2a | -1.73029 | -52.46161 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7e59667-f6df-34fa-9dbe-a4ab127e3b3f | -1.83348 | -52.01675 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9a87e16-fa92-30da-952e-52195232ea24 | -2.20463 | -46.79243 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4b658c8-347f-3bdf-84e3-61bcac2cf7c8 | 0.84561 | -50.21034 | 2024-11-09 04:31:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b16e59f-3463-399c-868a-48657a02c404 | -3.54574 | -43.5612 | 2024-11-09 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 53286c03-f19f-3b94-b13e-a6dcb930ba1c | -2.8406 | -48.46669 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c568a747-a178-3851-b8a4-e1263b157f21 | -2.71477 | -47.7309 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54cb0508-c9c6-3b6c-a00f-26d48c93393b | -2.46668 | -50.40456 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e9b9ab7-32e4-390c-9aa4-bbb03d870fb9 | -2.51348 | -46.36057 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 580fd3cc-2d2a-3109-8d32-0e894bbddfc8 | -2.14688 | -48.83111 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b492dbc1-149e-3efd-b2b8-e4cae34edab8 | -2.10077 | -46.2149 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39f1ce6a-25fb-3b03-9186-d533f67b06e2 | -2.5952 | -47.01504 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc9e5646-e277-3fb1-a955-2074d7394f1c | -2.26124 | -48.84102 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dd25f86-7f79-3023-9532-f4ce1f1688ee | -2.74993 | -45.9995 | 2024-11-09 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a61959a-bdf1-3a04-bf43-1a4470d86a50 | -2.52924 | -46.30257 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b2dfddc-b931-3005-9dcc-de0fa8f1d494 | -2.12741 | -46.3716 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0866c3b-b3cb-3568-9062-d37bb4cedc16 | -2.21631 | -48.47898 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0e66c86-c543-33b5-9316-dfffb650f9c7 | -2.89121 | -45.3855 | 2024-11-09 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e634716-a2e4-31f4-9259-bfca79b01da1 | -2.50827 | -46.30654 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fdb6d13-71c8-392c-9d8a-c28f37b76899 | -2.79651 | -46.64195 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54079312-5756-3fe0-8de8-b51d31867126 | -2.13255 | -48.73947 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48755a85-2618-379e-94ac-1aff58893c79 | -2.58924 | -48.20688 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da9f28f5-04ce-3947-abef-398412e1035b | -1.99345 | -52.08986 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 527497e2-a497-34ff-b9c5-36cce2d39d07 | -2.70036 | -46.69074 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8425b43c-110d-30a8-be1f-b79e7749f156 | -2.89065 | -45.38917 | 2024-11-09 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcf8bd22-10b3-35de-ba7f-bdb66e36aee1 | -2.65543 | -48.6313 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cba06577-afd8-3daa-9763-7c477c7de115 | -2.18349 | -46.86295 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90ee1633-7756-3f63-a7f6-0b2dc5b39dd3 | -1.94122 | -51.39982 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4451a3ed-57c7-32c1-8a63-53940c09240b | -1.88376 | -52.17569 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 266be4f6-7c7e-385d-8e81-39831026aade | -2.79517 | -45.96713 | 2024-11-09 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d095bd54-f46c-386e-8ced-034c4c9926ef | -2.40985 | -50.31048 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b21fa7fb-e429-3680-b24b-247c7bb669f6 | -2.08646 | -48.29155 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0bfc0d2-226a-3074-9a0f-74fe09b4e1ee | 3.36666 | -51.27481 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a283f50c-7b81-3b65-8ce2-3289e9eff305 | -1.9606 | -48.69837 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54554ba2-7508-3dd8-8641-2211847152c7 | -2.1364 | -46.66588 | 2024-11-09 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 169725bf-4aa4-3b07-9dde-1ca0a0e6bc63 | -2.53921 | -46.30408 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb420800-4820-3405-ba3a-7755f7e9a5ce | -2.63714 | -46.78948 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90e3cefe-adcd-3bfb-915d-1a2ab54c6c20 | -2.08983 | -46.48253 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 289e3a6f-fc55-3b68-816e-00f11e6875fa | -0.91226 | -52.56242 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b5d695c-0e4d-3621-87ce-18c0e5f2e946 | -3.55251 | -43.56684 | 2024-11-09 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e50f95f-ae6e-30ba-8651-5f58688b72e9 | -2.10678 | -46.19803 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2fd9d714-af28-3d28-af3d-4594ac770543 | -3.15079 | -46.5057 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d297a58-d404-382d-b1e0-53a88e82398e | -2.44357 | -50.2603 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98e1b092-c1ed-3a19-968c-6b5a0de0c3bb | -2.13537 | -48.74363 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ead1103-8558-3d15-8253-1b2efa146130 | -2.16533 | -50.13073 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc352ede-5a8c-3390-83f8-bd819d625523 | -2.3596 | -46.7608 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b591087-29a7-329a-a457-44f436baabb1 | -2.12133 | -48.28227 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03b7f006-6f35-37db-ade1-2f2d28dd30cc | -2.61953 | -46.1594 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19b0390a-2ff2-3ddf-8e50-d6dfbc8ce8de | -2.62008 | -46.1559 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 480f7d3b-ff66-34b6-bffe-c118cc432d61 | -1.77753 | -52.34984 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13162560-395b-3dfb-a558-d8fa76ca8e37 | -3.55624 | -43.5674 | 2024-11-09 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f9662f6-464f-30eb-8655-683bb83a365d | -2.31031 | -48.55203 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d250a09d-f952-3b78-a5a6-72415717343d | -2.66769 | -46.72377 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87a7ea74-a95f-3077-b32c-cc8aea079c08 | -2.67878 | -46.78607 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8de8a66-adae-313c-bcfb-629b048d06cd | -2.39295 | -46.58978 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc1b01ad-98fa-3d3f-941c-5592ee9a7cb9 | -2.90013 | -46.80614 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62f86d6a-6877-3e9a-a6cb-b7be57af6d71 | -3.54947 | -43.56178 | 2024-11-09 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ecb95792-782d-38b8-8ddf-140cff38488b | -2.63597 | -46.77523 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5f02866-4870-33e6-a595-a2604c76567b | -2.28923 | -48.72973 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb605c11-67e0-36e6-ac14-4a34f6df27d0 | -2.57308 | -48.17923 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 370d4700-c700-3bc0-adfe-d6c688d4cea5 | -3.13008 | -45.9567 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c14041eb-cf7e-31e2-a1f6-3da9214b7c13 | -2.63383 | -46.78897 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42415c19-5d2d-31c7-bce5-80172dac497d | -2.30247 | -48.53614 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec484ceb-b5dd-314b-9a2d-0d63caa5574f | -3.52523 | -40.91083 | 2024-11-09 04:31:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 72e51332-93f3-3a72-a236-17704db780f7 | -1.78165 | -52.35049 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 201d2af2-9a8b-3485-a2f3-a8247070e40e | -2.06593 | -53.27879 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README40.md)
