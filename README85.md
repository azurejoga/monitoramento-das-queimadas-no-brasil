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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa6ef09e-1df5-33a9-b677-829b420c1778 | -17.73223 | -44.37751 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f95d1dfd-b861-3f81-a493-9df935423071 | -15.7662 | -46.2549 | 2025-10-08 04:40:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ade6fa0-40ca-39e9-9b45-edb8f313d2d3 | -16.88498 | -46.96421 | 2025-10-08 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6080d2d-46cf-3fcc-ad6a-c4e306dd0877 | -15.38004 | -47.31703 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 780dcced-6167-385b-b608-be13349a33c9 | -16.33406 | -47.05175 | 2025-10-08 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cbb3825-f822-3058-ab9b-cebf171e9067 | -11.99413 | -46.77214 | 2025-10-08 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fdcba364-f6e2-36e1-8948-c4670bc52406 | -11.17083 | -54.89452 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 24c60be0-02f7-3bd2-a365-8bcc09e45ce2 | -15.63925 | -52.55017 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd1d71f2-fa79-3f42-8efd-13d5924b6f2d | -11.17257 | -54.88453 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e90a3a3d-7f32-3f20-83a9-c582cc712f74 | -13.2236 | -47.18185 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c5d9400-da85-330e-97ab-c24648d38229 | -17.97711 | -44.97548 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acd1afde-b49a-3cd8-be09-4a3422496ccc | -13.75337 | -45.7536 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 071e79cd-edcc-3de3-b045-0fc3bf342314 | -11.95996 | -51.46665 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9bce189-ea84-36a3-bbf2-adc6efd617c6 | -12.93028 | -46.84594 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b07d9233-f62d-35bf-af6a-9540af52d7fe | -18.07705 | -44.45588 | 2025-10-08 04:40:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d861f179-db6f-3de4-8128-25aeec6ceb8b | -11.74462 | -50.94439 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8c9bae1a-7cb5-3f3d-ae4d-0ecb2418471c | -15.40496 | -47.99758 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5bd20de-4e10-329b-ae66-776e2a16dcdf | -11.13919 | -54.8872 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acf21808-f171-3a37-9d70-14403d3fc6f5 | -15.89005 | -46.25637 | 2025-10-08 04:40:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c669ae1-6992-31c2-9e7a-300cf6c6839a | -13.30548 | -48.03122 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 577a45af-b702-3a2c-a53b-41f938aec0be | -19.15278 | -43.32354 | 2025-10-08 04:40:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 49e4e64b-b056-3f0a-88c2-8eba64a014c2 | -13.33597 | -48.01795 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1a54c74-635c-318e-a28e-324ca836c8a0 | -13.80087 | -45.80035 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae579475-c5d0-3fcb-ae47-7103d84977da | -13.21114 | -51.65215 | 2025-10-08 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bb40f272-362f-3f3f-baeb-8f957a6b5f4e | -12.94465 | -46.85265 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9c2f77b-1dab-3b56-804e-bf69b11d9df2 | -12.0431 | -47.77742 | 2025-10-08 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e7444a1-9db4-3011-a4a5-01c8a04fd744 | -13.22167 | -47.17848 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| decf6529-9c26-34d0-8376-0237a5bc839d | -12.38791 | -51.12905 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daa1e592-42b1-3571-b63d-910f36d99fff | -12.49974 | -54.71638 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 659a5a1d-dc65-3b0c-b63e-b4f9404a0bf4 | -12.38623 | -51.13965 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1628aa89-79d4-33dc-bdae-216887b05af3 | -19.15795 | -43.32395 | 2025-10-08 04:40:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 24b3b543-933e-3d03-a3b9-2c1e0cf97778 | -11.70591 | -50.9525 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| afd82f56-2fdf-3b33-a14f-4b600c4223a4 | -13.0702 | -47.93616 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db4ec4e7-3355-3f26-bdf1-e680f351bd2c | -12.93404 | -46.84647 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a45b9c6-023c-3aaf-9176-57eff60aacec | -15.37565 | -47.32095 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d9f4052-7e5a-399d-953e-c6a14496ead4 | -15.39336 | -46.28019 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11ab0ba3-c614-303c-973d-4453fc903d21 | -13.05832 | -47.94285 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74727bc4-b02e-3857-8dfc-d9f436db1cdc | -13.29776 | -48.03432 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 541182bc-be69-34c2-a542-7921d495957f | -12.23873 | -43.7807 | 2025-10-08 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e18e6f8e-4ecb-3e4a-8dd0-12a6644df302 | -11.13895 | -54.89392 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8386aa1-0724-382d-bde4-198dd4d19ca6 | -18.03882 | -57.52159 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6ed5d3a5-cfdb-3be7-8df6-fbbd12057c1e | -17.9452 | -57.53083 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5b75c7fd-7f3f-3228-afbe-7b094458a536 | -19.42687 | -49.5878 | 2025-10-08 04:42:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08be6554-79c4-3244-a90a-17716b58e07f | -17.96949 | -57.50767 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c2ad9042-def4-3a9b-a3ce-2250c9072cfe | -17.93983 | -57.53696 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f4ad4ec8-281c-3954-bd9d-2fd5c86ac6ff | -17.83057 | -57.63106 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 742778fd-41bc-3f6e-b672-436938308873 | -19.98361 | -45.40331 | 2025-10-08 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 41928e39-a209-315c-a0dd-1d03cf3f2805 | -20.28455 | -48.5155 | 2025-10-08 04:42:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3560bcf1-13af-3702-99dd-85cd0de59948 | -17.97282 | -57.51245 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 30b13501-3563-3bf4-8621-4a6096517989 | -17.9969 | -57.49694 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a9bab863-a095-3fad-a4ad-0db410822621 | -21.04018 | -45.6762 | 2025-10-08 04:42:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c9dcc0c-6e95-3bc5-bb78-0814058c7f38 | -17.95821 | -57.50609 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ecf1678c-4b99-38c1-9f6f-72a54c51a915 | -18.04228 | -57.52573 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0890209c-4a7e-3e19-a692-39c27355d925 | -17.93646 | -57.50932 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a354bb3b-33ae-34fa-8b43-53711778c60e | -18.00161 | -57.49439 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c0d6c77e-8b0c-3bb3-827e-62ee75e5d43f | -19.83098 | -46.16283 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4770027f-7620-3349-b86f-0804363b2873 | -21.53264 | -45.43557 | 2025-10-08 04:42:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6079a642-8b38-3591-b0d7-0eeb2bdab9f2 | -22.39317 | -50.02284 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1bbe3526-8cbb-31e8-a8b1-933b4f42a4ff | -17.94465 | -57.51077 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f22d7d6e-8eca-3284-bec6-555f69c4a246 | -20.09152 | -44.20128 | 2025-10-08 04:42:00 | NOAA-20 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 96a380ad-ee12-33e6-935d-84ba09e216c9 | -22.38077 | -49.98063 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 29cac0ae-9a97-3e50-8c49-425dc993353c | -20.26595 | -43.2592 | 2025-10-08 04:42:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0c239062-ff3e-3241-acc0-e8b68f4e06c2 | -21.29861 | -45.4552 | 2025-10-08 04:42:00 | NOAA-20 | SANTANA DA VARGEM | MINAS GERAIS | Brasil | 3158300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 02c2631c-04c5-3c1f-8e92-2cb095d846e2 | -19.47664 | -55.47997 | 2025-10-08 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 26a40aed-9bf6-3b11-b453-74739d80892e | -17.82864 | -57.64148 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 91090ccc-9de5-3437-b962-01cfb4abdd35 | -17.82431 | -57.61866 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b3e13011-61df-3d78-b408-7401f9b61513 | -20.49874 | -45.9495 | 2025-10-08 04:42:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7863eab6-83a4-3407-9c29-e3cfb8ecae60 | -17.8328 | -57.63106 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| dd13c0e4-d4a6-3d95-b19f-4ebb035298d4 | -20.20406 | -43.95759 | 2025-10-08 04:42:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8ec35b8d-2d54-3e65-bc57-0f6b81078a8a | -20.49937 | -45.94381 | 2025-10-08 04:42:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a641dac-0f5f-3838-a091-1bac10e54954 | -19.82879 | -45.25748 | 2025-10-08 04:42:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d50c0da-54b8-3df0-8ca9-f5d1d07aa965 | -19.82782 | -46.16771 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 61fd5b70-da16-39fc-bfa3-444b9bbd8fa5 | -17.99822 | -57.48989 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 373ea423-0e3b-3e77-9be5-8d7251a3f695 | -20.49922 | -45.94535 | 2025-10-08 04:42:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4b8cbad-15c7-3d84-8e0c-e58e3eff2582 | -17.82707 | -57.62688 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c2e07476-2e4a-38c7-a69b-5cdeae49102e | -17.82733 | -57.63731 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.3 |
| be4a92fa-60d9-30df-b8a0-c65f557e2791 | -17.83002 | -57.62318 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 13f40a26-ed0a-3cf8-9628-648948687b99 | -20.39238 | -43.06923 | 2025-10-08 04:42:00 | NOAA-20 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0d8ed759-13ae-385f-b16f-a8a281ecf28f | -21.55343 | -46.00574 | 2025-10-08 04:42:00 | NOAA-20 | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c64c664d-0006-34dc-a117-390bf93efbf3 | -17.96294 | -57.50338 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5630e4ca-ec66-34aa-bb4b-0f0dfa229146 | -18.05464 | -57.52749 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 61461240-5e0f-35d1-8569-efd842200918 | -17.83899 | -57.64348 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c3e7d916-5bc3-3217-93bf-27b76c901a01 | -20.10014 | -44.21341 | 2025-10-08 04:42:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cf161b77-273a-3015-990f-4c81f8a2ba3b | -22.38434 | -49.98113 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c9b745c6-0788-3474-a8a0-759201311a61 | -17.82929 | -57.63797 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 41cf22e1-7f59-371b-a591-f237f94aab11 | -19.82621 | -46.16624 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 71aa66c8-e64e-3e28-8d57-9df5913b09e2 | -19.78098 | -43.883 | 2025-10-08 04:42:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a648d34b-3be6-33ae-a6c6-eb84c63db710 | -17.86004 | -57.64527 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fd29155d-e48c-35cf-8875-7997b4117271 | -17.97355 | -57.5086 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 50a16dee-4204-3642-aed3-d951a886d598 | -22.3411 | -49.88186 | 2025-10-08 04:42:00 | NOAA-20 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e682ef53-b279-35b1-a0fa-76f2e5991589 | -17.98045 | -57.49446 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d1e9b72a-6676-34ee-9376-428ee4c41932 | -20.49836 | -45.95208 | 2025-10-08 04:42:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 909f6230-8934-315a-920e-10143ea001f5 | -20.58576 | -46.34555 | 2025-10-08 04:42:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fc4d6b2-26a7-3981-89ce-53a7db16e6e6 | -20.2656 | -43.26264 | 2025-10-08 04:42:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 65c9a547-6d74-397a-a675-ca302c1d47af | -20.50359 | -45.94616 | 2025-10-08 04:42:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32fbcf68-89de-3fff-b8f3-0802ea5484bb | -17.9412 | -57.50658 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3fec8e3e-6b35-3d28-9c82-a558f70f0b67 | -17.82361 | -57.62247 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 794e3182-11e7-3d22-a260-389174ed6cec | -18.02129 | -57.52485 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 18fc254f-0c7d-307f-b87c-e2b278c4f07a | -18.01488 | -57.55928 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4b83f4c3-5bfa-3947-8eb0-b51298d74914 | -17.84303 | -57.64474 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README86.md)
