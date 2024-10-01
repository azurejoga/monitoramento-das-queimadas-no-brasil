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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3df2a7a7-283f-34a5-85cd-963e722808e7 | -11.80452 | -47.59838 | 2024-10-01 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58a372fa-ba86-3e06-8b24-9194380a0c20 | -11.80397 | -47.60127 | 2024-10-01 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 904ccf93-68b2-3142-b07e-556088eed3a1 | -11.80381 | -47.60213 | 2024-10-01 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| adc777da-dc44-336a-8298-dfc5adb67bd6 | -11.76984 | -47.60228 | 2024-10-01 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 955ed219-24c1-3944-a8c0-f8a1cbe8b660 | -11.7637 | -47.60479 | 2024-10-01 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3497f739-682e-34b6-bc23-401f61f42dd0 | -11.44638 | -46.95245 | 2024-10-01 03:49:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91994cdc-16c1-3ecf-83d3-7edebd0bfbd8 | -11.44126 | -46.95072 | 2024-10-01 03:49:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d101d264-bbf4-39fe-a547-2257d3038027 | -11.44065 | -46.95393 | 2024-10-01 03:49:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bc5f938-4f96-3cab-b03d-ebb068663408 | -11.44056 | -47.81772 | 2024-10-01 03:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39912f31-9470-3238-ba0c-ec7a319fafee | -11.43983 | -47.82155 | 2024-10-01 03:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfa702e1-e46b-32c0-bc96-dc65df22626c | -11.43853 | -47.81849 | 2024-10-01 03:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d7d0b96-7fac-3fd2-9256-5be15c880bea | -11.43487 | -46.95561 | 2024-10-01 03:49:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 375b912e-f0e5-3e45-be74-7dacd65e8614 | -11.43425 | -46.95889 | 2024-10-01 03:49:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e02c37b9-e255-30c1-8db9-1aeebb074778 | -11.31007 | -46.84988 | 2024-10-01 03:49:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45acc804-0a8c-3e14-9671-8e83067d1b2a | -11.30908 | -46.84939 | 2024-10-01 03:49:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5aa4b58f-0217-334d-b288-81cb5a791fc8 | -11.30482 | -46.84896 | 2024-10-01 03:49:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9019d90-f0ac-3ae0-9c6e-d92a2c74be5c | -11.30382 | -46.8485 | 2024-10-01 03:49:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17fad3f8-53c4-3f9b-8095-9942f73998bb | -11.10463 | -49.60071 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7579e3cc-31fc-33d7-a003-7fefa95c2071 | -11.10289 | -49.59414 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cedb131a-9ba5-396d-ae3a-a2c7885635cc | -11.10034 | -49.58944 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7902706-83a8-3ba4-b648-4c161a740df6 | -11.09937 | -49.59442 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0f97144-c653-3f03-8b35-0e4cf6613535 | -11.09766 | -49.58791 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b30e36f-1891-3042-a830-7f153424284e | -11.09665 | -49.59287 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4cbaedb-4c58-39cc-bf81-c97b7c89ea00 | -11.00589 | -46.48274 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cfc435a9-163e-3845-90dd-3fdccfccbeb6 | -11.00517 | -46.48668 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9fd6071d-976e-3f48-8237-fae9d8fa0bbc | -11.0014 | -46.47832 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5da98f8e-5689-3c15-95e4-97a9ec3294cb | -11.00068 | -46.48216 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 37b2b480-f84f-3d13-b16b-3460d6f27f4c | -10.99998 | -46.48593 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9f4e8b4-5462-3023-b330-1e25eba47ab7 | -10.99934 | -46.48937 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5c02844-6129-36f9-aabc-2bed4baf67f3 | -10.99875 | -46.49256 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f72c22e-507c-36d9-a949-3a7c2368892c | -10.99816 | -46.49572 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c8adda8-ccea-32c9-8683-a625c355ed05 | -10.99757 | -46.49888 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c4bc03a-3adf-3883-a7f7-da86e3d5daff | -10.99698 | -46.47348 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ae3832d-72a8-3c48-b536-af6f64a0c4c0 | -10.99623 | -46.4775 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bfce311-e028-35ea-8502-752765fb26ee | -10.99552 | -46.48132 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ff0e58f-cc05-3cc2-81ef-0555748b3bd9 | -10.99524 | -46.51138 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb7e3e82-723b-3eb1-a89a-5da88405a393 | -10.99467 | -46.51444 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 494de845-ef16-3293-a522-c567acae943a | -10.9941 | -46.51749 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b9bb3627-8ff0-3dc8-8fe4-66ad246747b4 | -10.99353 | -46.52053 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71e89c9b-a38e-35d8-9964-e9453576f60c | -20.81103 | -53.13018 | 2024-10-01 03:51:00 | NPP-375D | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b4e9ab0-5c89-3948-a818-ed57881b6e9a | -20.80961 | -53.13613 | 2024-10-01 03:51:00 | NPP-375D | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9424af4-0e29-3bf7-97d9-628b54ea6187 | -20.80466 | -53.12844 | 2024-10-01 03:51:00 | NPP-375D | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94e79566-ac4c-3d76-af1a-d137c19def57 | -20.79824 | -53.12694 | 2024-10-01 03:51:00 | NPP-375D | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c94781c9-1b74-3ec2-a160-96aaa47ac74b | -20.79608 | -53.1077 | 2024-10-01 03:51:00 | NPP-375D | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dd65da8-bdc1-3615-a725-2ec929a02ea5 | -20.78964 | -53.1063 | 2024-10-01 03:51:00 | NPP-375D | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6967502-9846-3b7f-9f80-533a301bccec | -20.78937 | -53.10929 | 2024-10-01 03:51:00 | NPP-375D | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b05aeff-1879-393a-b65c-3a76534d4f7c | -20.59883 | -46.24147 | 2024-10-01 03:51:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 64780970-1523-3022-bf33-6db0edc1d606 | -20.59455 | -46.24075 | 2024-10-01 03:51:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f88087d-e948-3a37-8257-77580e3e9947 | -20.53662 | -46.28817 | 2024-10-01 03:51:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83305202-d0be-362f-bf8d-be3b46c1f897 | -20.53575 | -46.29264 | 2024-10-01 03:51:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d0c4e572-5936-3009-9fd0-d045ee6382b7 | -20.53143 | -46.29199 | 2024-10-01 03:51:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f436aa4-927f-3315-994b-a93ec77445ed | -20.5306 | -46.29625 | 2024-10-01 03:51:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8963f28-a235-3dd2-92e7-9f450fcffa37 | -20.52543 | -46.29992 | 2024-10-01 03:51:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 92c9fc9c-5060-3cd9-bdad-4ca09aa07ce8 | -20.52113 | -46.2992 | 2024-10-01 03:51:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60cbf183-7720-3d5f-b2ea-ed44608d5ad1 | -20.51593 | -46.30299 | 2024-10-01 03:51:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 895821fb-ee31-3cf7-b1a0-f89bb817f22d | -20.09429 | -47.34491 | 2024-10-01 03:51:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d2d8b43-c070-3687-98e0-dd1d1d92f3bd | -20.09194 | -47.34262 | 2024-10-01 03:51:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 408240e5-15ab-36d5-94cc-64a6a5d40930 | -20.09094 | -47.34769 | 2024-10-01 03:51:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b9f4612-b669-3523-8c7c-ccd9727070a2 | -20.08972 | -47.34378 | 2024-10-01 03:51:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e06c3dd6-8b82-3d44-b627-420b0af46d88 | -20.08869 | -47.34882 | 2024-10-01 03:51:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4b99a47-ba9a-32de-a3a3-3319c13ea973 | -20.07316 | -51.33609 | 2024-10-01 03:51:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 819f207e-1527-345b-a5c5-baecc1afd7fe | -20.07216 | -51.34058 | 2024-10-01 03:51:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d401e373-27ef-3315-9d5f-f252952d0b35 | -20.06718 | -48.17719 | 2024-10-01 03:51:00 | NPP-375D | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fe0f3d78-40e7-3f54-8273-c3ad472ced82 | -19.78537 | -47.9623 | 2024-10-01 03:51:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06b4d5ef-1798-3aac-ae82-86ffefa8c57f | -19.76195 | -46.63975 | 2024-10-01 03:51:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0848a48-b17a-3db9-a670-8396cfedd0a5 | -19.75934 | -46.6295 | 2024-10-01 03:51:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c31e3132-8eb0-30ef-bc7b-65f2c64c67f7 | -19.75843 | -46.65784 | 2024-10-01 03:51:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ccdca4a-170d-34cd-a68b-1f070c9dc67b | -19.75755 | -46.66236 | 2024-10-01 03:51:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 919b7445-f295-3e59-bbc7-0ee59a6d9001 | -19.75754 | -46.63875 | 2024-10-01 03:51:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b0a1ba9-8988-3f48-9816-2933d53666f3 | -19.75667 | -46.66687 | 2024-10-01 03:51:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53d27c15-5df8-338b-a668-5000be004dc5 | -19.75664 | -46.64336 | 2024-10-01 03:51:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 337bfe59-f621-38fe-8c21-473c473569f5 | -19.69673 | -47.23247 | 2024-10-01 03:51:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 181a80cf-420f-3953-9744-b3246c913ad0 | -19.69567 | -47.23775 | 2024-10-01 03:51:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bc18cac-67cf-36fb-9e96-fbf9d6e4ef42 | -19.69523 | -47.21617 | 2024-10-01 03:51:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00487963-c0b6-30c3-b05d-61e7e5d6daea | -19.68612 | -47.21383 | 2024-10-01 03:51:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a5258e3-c6c3-30b1-bf08-fbcbc851a79e | -19.67711 | -48.79237 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8369d117-6b19-3151-9d8c-b05eace3e1df | -18.64253 | -52.48714 | 2024-10-01 03:51:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4277a268-e230-3f33-bdda-cca7596528b4 | -19.67647 | -48.79548 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1f4e6a9d-d166-3f75-95f6-dafbcd34232c | -19.67584 | -48.79857 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7362f89c-cde2-3eea-8c71-c2cc65611302 | -19.67511 | -48.78917 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1e35d2bc-48f0-3e85-a541-dd33359a31aa | -19.67444 | -48.79227 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 020e6f1a-e4f9-335f-8d8f-d6029ece3256 | -19.67378 | -48.79538 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 5f590347-8117-3c1a-a819-8c02e18307a7 | -19.67312 | -48.79849 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 23d27fc4-883c-39d7-95d8-a243c97f8285 | -19.67275 | -48.78777 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2f2b0dc1-4b31-36b5-bfdd-1090fbae05ea | -19.67211 | -48.7909 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ca8ee5f1-046b-3992-9b41-a895e0b452c4 | -19.67147 | -48.79401 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| f7be2a72-660d-3d55-b4e4-edb22dcaf1df | -19.67082 | -48.79715 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 950d12d5-e91f-30c2-a288-263788f0d7b7 | -19.6701 | -48.78771 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 997cb785-f40f-38da-af67-bed06d7e06f4 | -19.66944 | -48.79084 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 95c97783-02f1-3f83-8b37-b859092e03e2 | -19.66877 | -48.79396 | 2024-10-01 03:51:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 546f6a4f-5f69-311e-9e6f-285280f93540 | -19.30041 | -47.43622 | 2024-10-01 03:51:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e072a1f8-f9ca-34ae-8577-69b61e271788 | -19.29971 | -47.43406 | 2024-10-01 03:51:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13a534c4-4bd9-3298-a54d-47c8b90b60db | -19.29573 | -47.43517 | 2024-10-01 03:51:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c86443fb-0480-3e70-8618-7b7a6390cf8b | -19.29503 | -47.43299 | 2024-10-01 03:51:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdff6bec-5b1a-32ce-b04f-e2e247847421 | -18.99916 | -47.25931 | 2024-10-01 03:51:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93cc2585-7131-3d28-a3d0-515975813002 | -18.95007 | -46.93047 | 2024-10-01 03:51:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c0a05c79-e841-3ab2-a56f-91c3191b4a50 | -18.94914 | -46.93523 | 2024-10-01 03:51:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 171cd34f-abf4-3297-a0be-9520089a60aa | -18.92507 | -47.03382 | 2024-10-01 03:51:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1031b787-6a6d-369a-95b1-73e2240f2c27 | -18.92147 | -47.02771 | 2024-10-01 03:51:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6acdd6b4-be09-30c5-9305-65ff8376cf5c | -18.92049 | -47.03269 | 2024-10-01 03:51:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README54.md)
