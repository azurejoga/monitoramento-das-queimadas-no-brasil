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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd81918a-02ad-3439-9b6c-da7a99834876 | -2.47382 | -49.03178 | 2024-12-13 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d82a1b3-303b-369a-a7c6-aa4c52970fde | -2.50436 | -46.84978 | 2024-12-13 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 378799d7-055a-3659-869d-08f2a7c03a18 | -3.03781 | -44.47375 | 2024-12-13 04:18:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94255ee9-93b4-39e1-ab0d-0390db17e71e | -2.3054 | -45.11787 | 2024-12-13 04:18:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f3c3bd6-df51-3c7b-a90b-287bf7a1a1f3 | -3.14244 | -40.04983 | 2024-12-13 04:18:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9faa5f4a-d7ee-36c5-9982-da82f8aac8e0 | -2.55995 | -49.09005 | 2024-12-13 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68273b02-e45f-3954-bd41-dd5ce880b226 | -0.94069 | -46.92371 | 2024-12-13 04:18:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f27df3c-9ff6-3f92-9c8a-b65e60c91bb2 | -3.06901 | -40.0503 | 2024-12-13 04:18:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c13c0446-bb3b-3098-b253-78e6be3e4f75 | -2.3709 | -48.28125 | 2024-12-13 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e1dc3f7-ec77-3aaf-8eda-04472841dede | -1.63137 | -54.02269 | 2024-12-13 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e4ff8f3-2c01-3df7-a285-c8e91cbfdfc4 | -1.53606 | -46.29525 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f597653a-aaf0-3a33-9a2c-33a2bd1cd03a | -3.14084 | -45.5947 | 2024-12-13 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1542a504-8e19-3a79-aa79-ea3543519a96 | -2.56347 | -49.09434 | 2024-12-13 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 116823fe-0ec9-3f16-b6bd-dc13b73952d6 | -2.47323 | -49.03541 | 2024-12-13 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15fddbac-80c1-3417-884a-d2e74020683f | -2.79989 | -47.42225 | 2024-12-13 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b800cb61-0f59-3324-909c-bf7c224c811c | -1.90124 | -46.81693 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78985aa6-f156-3662-b517-78cd313a8569 | -1.96567 | -48.39136 | 2024-12-13 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a166dc68-a3c9-390a-8c3b-a2d7c4942e26 | -1.92502 | -52.72967 | 2024-12-13 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 796ab1b8-a4e8-3325-af71-ad311421acb4 | -1.73666 | -52.02247 | 2024-12-13 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4f44194-f1a5-3e6d-b8fa-52ffad143be5 | -1.62384 | -46.66628 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 74ed213d-022f-3581-bd85-948c2717f865 | -2.50861 | -46.84626 | 2024-12-13 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6780891e-37ab-3f55-8ddf-1ac2a26c11f3 | -3.42292 | -43.16366 | 2024-12-13 04:18:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7643098d-143b-3412-9471-9ab927619dd9 | -1.74126 | -52.02625 | 2024-12-13 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8843a7b3-eca1-300a-b9f4-6d5f760fd9f6 | -1.25563 | -52.17048 | 2024-12-13 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17feb95a-c55e-3613-b3f2-535138d656e3 | -2.61051 | -47.94187 | 2024-12-13 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a611d1c3-d71d-3ba6-adef-91de7886a02e | -3.04114 | -44.47428 | 2024-12-13 04:18:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 020e2d01-b993-3283-b0ff-74a9298ad86c | -1.69782 | -45.77417 | 2024-12-13 04:18:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 517955dc-286c-3e6e-8c86-7edd26ff2202 | -1.23234 | -54.14035 | 2024-12-13 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7dd6ab9-2062-369c-8caf-d0f96e0230ab | -1.05359 | -47.66391 | 2024-12-13 04:18:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbfac359-3b03-3c58-97bf-72d6da812a7a | -0.75347 | -47.76002 | 2024-12-13 04:18:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 10d11b7f-0505-3a2c-81ac-bc85a848b374 | -1.62556 | -54.02171 | 2024-12-13 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce294730-990f-3780-a042-ef19f0165d01 | -3.37885 | -42.32993 | 2024-12-13 04:18:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 53e50005-1da2-37f3-b40a-476b5e858333 | -1.19092 | -46.66654 | 2024-12-13 04:18:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d6520c5a-c4c9-3486-8f32-eef4ad3402ee | -1.9743 | -45.39594 | 2024-12-13 04:18:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f2121b5-5f00-3b8a-beb5-8175be80906e | -1.61823 | -46.67012 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa4d361e-62fe-3632-9270-a280770c9de5 | -0.75423 | -47.7552 | 2024-12-13 04:18:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5578c8c9-f2d9-3315-9323-312997e594e1 | -3.70072 | -42.12415 | 2024-12-13 04:18:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ab9587b-84d5-351d-8e5a-ecae6bc00209 | -1.97646 | -48.69329 | 2024-12-13 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e261473b-ce33-3490-bf20-4c7a390c4c13 | -1.53544 | -46.29919 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97625308-6b54-3256-b056-ba476688afad | -3.14424 | -45.59524 | 2024-12-13 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ac7cd20-bf1f-3e27-ac10-85525019326f | -1.24577 | -52.16571 | 2024-12-13 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c158692e-2eab-3978-ab74-9b8ed362da54 | -1.91235 | -52.65011 | 2024-12-13 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10a0e328-2e55-3fe6-8e85-ca7a41c15e5f | -1.99402 | -46.54176 | 2024-12-13 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05a9ad1a-4b07-3958-94e6-d869ee40388c | -1.69904 | -52.78116 | 2024-12-13 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c1190e6-67d2-37f3-99af-01b1ccd6887c | -3.14142 | -45.59108 | 2024-12-13 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1c3cae9-fe2b-34e3-9d72-ca73f1821588 | -3.36242 | -42.2786 | 2024-12-13 04:18:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 871b4f40-ac25-3749-bc28-551743349c14 | -2.60858 | -47.71849 | 2024-12-13 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d1bb76d-e3e5-3593-b91a-4cc29017e607 | -3.30285 | -43.53773 | 2024-12-13 04:18:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5852700-0a71-3d71-b1f5-80d4ff5f8ab6 | -2.83258 | -40.30283 | 2024-12-13 04:18:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| efee5ef2-630d-3f4c-ad8e-589a7eef0d0c | -1.73617 | -52.02542 | 2024-12-13 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 549dc259-7a43-316c-a35a-f9b98cf5864b | -1.46565 | -46.81337 | 2024-12-13 04:18:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfbaf737-74f8-33b1-8a0c-ce5d0b45dd27 | -2.90392 | -46.69848 | 2024-12-13 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adca072d-fa6e-3d3f-9d13-e62f17e9ffac | -3.0406 | -44.47775 | 2024-12-13 04:18:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bd46e11-42b5-3a22-a2a5-71d214ed08ed | -2.55908 | -47.5955 | 2024-12-13 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5771580-df28-3de7-b2ca-16c44cac1265 | -1.25095 | -52.16656 | 2024-12-13 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2c1a409-4331-30bf-acd5-592afd132d79 | -2.83629 | -40.30341 | 2024-12-13 04:18:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b556ff45-f665-316b-ba43-555bddbb1f87 | -1.57257 | -46.04066 | 2024-12-13 04:18:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07c34da3-b316-3fb0-b987-557a625b7468 | -1.7791 | -45.54995 | 2024-12-13 04:18:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2866695c-f9f6-3181-aaff-8383d751aa8e | -3.3584 | -42.30429 | 2024-12-13 04:18:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bfa85009-689c-30af-a558-e4a37e790973 | -3.37544 | -42.32941 | 2024-12-13 04:18:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fe8be173-17d9-39d7-9668-450b6caa18e5 | -1.62024 | -46.66571 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 52e2f511-b8cb-3373-9604-175e687368e8 | -3.14539 | -45.58799 | 2024-12-13 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6e6c756-c54b-3d78-a074-8aebfbdcd8f2 | -1.61958 | -46.6698 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e2df369-a666-3063-bd31-78a8356e97be | -1.70351 | -46.00887 | 2024-12-13 04:18:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ff9ed32-0dbf-39d9-b08e-ba7cd862c66a | -3.25053 | -42.41468 | 2024-12-13 04:18:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e85f7bed-38b0-3bc2-b0de-d6d897edf053 | -1.89763 | -46.81634 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9041e28b-1abb-305e-896e-5cbcfb7b9ea6 | -3.06972 | -40.04574 | 2024-12-13 04:18:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8caa456b-c265-3723-9c7c-83f6ad2b3ecb | -3.66997 | -39.58054 | 2024-12-13 04:18:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9516ea50-ffb4-3d48-b44c-1b822380c828 | -1.25514 | -52.17357 | 2024-12-13 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb6d9648-e000-31df-87f4-176727cf09be | -2.646 | -48.11164 | 2024-12-13 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28659102-fe6b-3a80-9ba3-be54d1baadc5 | -1.25612 | -52.16739 | 2024-12-13 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c14d624-3a11-36b8-8e7d-7e142e8a6114 | -2.30878 | -45.11839 | 2024-12-13 04:18:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dbfac21-e725-3226-9cb9-181e1aee3858 | -3.22227 | -42.07916 | 2024-12-13 04:18:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 037d76c2-02da-3d0d-bd12-1efea1146e03 | -1.74175 | -52.02328 | 2024-12-13 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66745f18-db00-3497-8879-bef11b68a910 | -2.60867 | -47.93948 | 2024-12-13 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55f972e7-45fb-3dee-a375-7feb0f4351a1 | -2.46972 | -49.03113 | 2024-12-13 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b5313fac-60b8-34e4-9ef1-0986dadabc24 | -3.36181 | -42.30482 | 2024-12-13 04:18:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c873a204-58b7-3966-beb4-2cd945c56684 | -1.91818 | -52.64769 | 2024-12-13 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7051cf77-6440-399c-b634-be1a164ddcb4 | -3.36184 | -42.28227 | 2024-12-13 04:18:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20d73133-e168-3990-be37-b16a4ed52e85 | -1.25046 | -52.16964 | 2024-12-13 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a799d84-4aa9-38e6-b03e-f04d5c001d42 | -1.33656 | -52.30037 | 2024-12-13 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd7a4951-d7d7-385b-bfaa-63b210842948 | -2.73162 | -47.88782 | 2024-12-13 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cc5e352d-c841-3f81-a8c0-258404e20fa3 | -3.30111 | -43.53408 | 2024-12-13 04:18:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e88cdd6-1f37-3e7e-879e-2c8ded9e33a0 | -2.61127 | -47.9372 | 2024-12-13 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e611c3f-53cb-35f5-8d4b-cc97679eef9c | -1.61886 | -46.66602 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de236f79-a16e-3127-9502-07a94ed202f8 | -1.62318 | -46.67037 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b3dbce2d-a381-36ef-bc46-7f5c92d9da57 | -2.83451 | -40.30109 | 2024-12-13 04:18:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 811ab470-b36b-3b7b-9f23-639e3ce75f32 | -2.71577 | -47.55433 | 2024-12-13 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90f06945-a913-3175-be49-d17c55549da3 | -1.92559 | -52.7263 | 2024-12-13 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad50c4fb-a2ce-344f-ab19-b2f5c2ebe47e | -3.04393 | -44.47827 | 2024-12-13 04:18:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c49bd03-9b26-3c75-b59c-6f1b7c55d49b | -1.53252 | -46.29468 | 2024-12-13 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c2c02ee-e96d-3be7-9992-f54182fc3f81 | -3.30339 | -43.53426 | 2024-12-13 04:18:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f9cdeeb3-9986-327f-af34-638fe6582140 | -3.14199 | -45.58745 | 2024-12-13 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11d9b586-38db-3a9e-af76-6daefb436a04 | -2.50738 | -44.1029 | 2024-12-13 04:18:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efd5211a-5432-3193-a15b-3b35c77d3f5b | -3.13866 | -40.04925 | 2024-12-13 04:18:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e046c5b9-b7b9-3224-9cf8-26c9dfd7592f | -1.46202 | -46.81279 | 2024-12-13 04:18:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 112fe262-0f01-3a61-a650-88fdd2e7b13d | -2.71807 | -47.56379 | 2024-12-13 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bac0210-7f11-3556-bd2d-7f61bf218d56 | -3.35782 | -42.30796 | 2024-12-13 04:18:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60d25f95-7f6a-395e-9d82-a148cae5e17e | -2.71707 | -45.53656 | 2024-12-13 04:18:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8685403-319d-37a0-9a41-fe99da9f8757 | -2.50501 | -46.8457 | 2024-12-13 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README16.md)
