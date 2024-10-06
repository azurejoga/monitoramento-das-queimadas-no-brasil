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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 092eedbd-cd0e-3ed6-9985-463f5ef8548f | -7.97272 | -54.76661 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18501aa1-440a-3f24-ba7a-33ea4a253918 | -7.97216 | -54.74564 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b17b77a4-5134-3725-8073-aea865bfce83 | -7.97156 | -54.74973 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56d45a4e-8a0a-3015-a58c-4a2b7fb1dd63 | -7.9686 | -54.74509 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14cc17a5-ddec-3b0a-996c-325fda711f72 | -7.96795 | -54.77425 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0e1cd2a-1792-3966-a153-c456adeba174 | -7.96619 | -54.76142 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b7712f7-53a4-38e0-b5ef-beee40de6178 | -7.96323 | -54.75679 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de387534-ac74-357f-a5a4-7ec8a67f0174 | -7.94956 | -54.75558 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6235fd6c-6c6b-32ca-a227-1d1420db938f | -7.94537 | -54.75912 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea6aa8cc-8be1-36ce-a947-17eeadb95dd5 | -7.90556 | -54.7573 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac13e6d0-44f7-39db-b063-8a257b340999 | -7.88031 | -54.87755 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dc4570f-a571-31ce-9042-b5a4786604a7 | -7.87971 | -54.88158 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86b1fd7d-6fc7-3558-98a2-5f7f0f16e26b | -7.87557 | -54.88508 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d4a3f05-79c4-36f0-ab6e-b20b12a04bf6 | -7.87143 | -54.88857 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f31c002-1ced-371c-b7d4-b34c3f25d29a | -7.87083 | -54.89256 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9580f01c-47bf-33aa-bfbd-c3fc46fdb78f | -8.06475 | -54.78479 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0f9c782-2433-321a-8a2a-b11968215304 | -8.1753 | -55.15576 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 105a77a4-a00c-3fdb-bf47-c3fb142d90a5 | -8.11343 | -55.30632 | 2024-10-06 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69303b96-2ef5-3304-a28b-e7d8265075b0 | -8.11285 | -55.31021 | 2024-10-06 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dc67967-14d7-3033-8c91-77c0430c2738 | -8.10995 | -55.30577 | 2024-10-06 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cc935da-3db0-3b7d-8eef-723a5629d280 | -8.10961 | -54.86924 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65aed561-b9eb-303d-bc94-47ae0ea02eb7 | -8.10937 | -55.30966 | 2024-10-06 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f70a7fc6-906d-317a-b383-9acc9f1a4c71 | -8.109 | -54.87331 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f05088fd-2c5f-393a-b6fc-c90a83c385bf | -10.63931 | -55.92002 | 2024-10-06 05:12:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09cc2370-9414-3b1f-bc2a-e464fe2a704e | -10.63526 | -55.92338 | 2024-10-06 05:12:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37a41a72-9459-3c6f-98ba-1d96e45a2757 | -10.63178 | -55.92285 | 2024-10-06 05:12:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8906fb81-22be-3e36-8740-0fc8016442df | -11.56303 | -55.66587 | 2024-10-06 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b0676e3d-6fae-30be-a04b-056b24cda669 | -11.55948 | -55.66534 | 2024-10-06 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3933baf-d792-3244-a7e7-d7a195cd58f4 | -12.14975 | -56.69581 | 2024-10-06 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46ee7a92-33ca-3b8b-9efc-db3d44a6a9db | -12.14919 | -56.6996 | 2024-10-06 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebcf82d5-6090-3488-ab51-c7303fe7f3e3 | -12.14633 | -56.69527 | 2024-10-06 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6320cd7-73cc-3871-bb32-a0b7a2c451bb | -12.14577 | -56.69906 | 2024-10-06 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76b39e92-294d-37c2-89fa-ed988d4a1bd6 | -12.14521 | -56.70284 | 2024-10-06 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7a6cf76-8475-310a-aad1-0c97fcef4aca | -11.93089 | -56.96152 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71cb7e48-028a-38f9-9b41-4fc78b06f4b8 | -11.93033 | -56.96521 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac3b530a-ecf1-32e6-9ba9-571c4fd3952b | -11.92978 | -56.9689 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6880724-fd00-3ddb-aaaf-a2cbee25fc1d | -11.92691 | -56.94196 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc905e05-2991-3be6-b24f-e0bbebfed083 | -11.92639 | -56.96838 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41d1e740-78f0-3e50-91ab-95f93ba9d284 | -11.92408 | -56.93774 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6ca4816-b5f6-3322-9421-0556564e6d2d | -11.92352 | -56.94144 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3b2e9e8-8b4e-3c9e-9a4a-a1cb0bc3097d | -11.92297 | -56.94513 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eac18079-e6e3-3764-945a-4c4b82a06f99 | -11.92181 | -56.92979 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e620118-f2e1-39cd-93df-d44011fe7f4e | -11.91898 | -56.92555 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61b01604-d8f1-3053-a4ff-e26ab237660d | -11.91842 | -56.92927 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23a30728-42d0-3a2b-95cc-eccd5e95e856 | -11.91786 | -56.93298 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98e3d987-1f20-310c-9ed4-9f2cc099b5e8 | -11.91559 | -56.92503 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa4fff7e-19e2-3c80-a588-9fbd19335ae3 | -11.91503 | -56.92874 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd7abbec-afd6-331d-9bcc-0eca908b58ad | -11.91447 | -56.93245 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cb6663e-a6a8-3016-8a39-25ea3f7f3b27 | -11.91392 | -56.93616 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a5bb208-2696-3ca5-b0fb-abc9789bc06f | -11.9128 | -56.94358 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 335170da-30fa-324f-9146-c9e6c8a63f3f | -11.9122 | -56.9245 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5b97fd1-3a95-314a-9e0b-21c3015f4c8c | -11.91164 | -56.92821 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebaf16c5-c105-3b2c-a493-b186f28f4031 | -11.91109 | -56.93192 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2029ebf-091a-3d58-b2be-048e4b8c26be | -11.91053 | -56.93563 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 321dbd25-8fb6-3062-bb83-f7c06c674b2c | -11.90997 | -56.93934 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0aec37f6-2826-3b3b-8361-7c9afb4244bd | -11.90881 | -56.92395 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cc79b20-eeb3-3b8f-b52e-d1adbcd3e62e | -11.90826 | -56.92767 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41cba021-2510-3eb9-8994-b202768715db | -11.9077 | -56.93138 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a636d059-00c7-3267-ab2e-28c24c28a452 | -11.90714 | -56.93509 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 603f4e12-2ab9-3ecf-a69d-e11e364fea06 | -11.90658 | -56.9388 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bc475b8-200d-3a5d-82e2-4ee12803b9e1 | -11.90543 | -56.92342 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e89a0e8-686e-37bc-85c2-27fc7556ca17 | -11.90487 | -56.92713 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7513c08d-2913-3485-921e-27409ac05fe5 | -11.90431 | -56.93084 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa7fafbf-0d5c-3936-9840-7654a9a9d61e | -11.90376 | -56.93456 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed94527e-e2b5-3b89-898d-1d4572875ecb | -11.9032 | -56.93827 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a684eb54-442a-37f2-b1d8-dea4fd37dc95 | -11.90148 | -56.9266 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b8d2f024-a117-3cb2-a7f0-db86b4461b90 | -11.90092 | -56.93032 | 2024-10-06 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 123296fb-622b-37cc-8123-3d78edd412a8 | -11.49165 | -56.7843 | 2024-10-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c2c45ee-0b8b-3971-ba0a-ebe2603b5dc1 | -11.48998 | -56.79543 | 2024-10-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3f48aed-3924-399e-a80c-85bc98045e85 | -11.48826 | -56.78378 | 2024-10-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24571a82-53ed-3cc6-9460-31b8d74ca758 | -11.4877 | -56.78749 | 2024-10-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72c34203-656c-3a98-b073-e5e52c3eb6b1 | -11.48715 | -56.79119 | 2024-10-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39dceafc-2128-3722-9cbe-f5dca8e34205 | -11.45753 | -56.28525 | 2024-10-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3c92a3e-e86f-3190-8842-0c198bc64bcc | -11.45407 | -56.28472 | 2024-10-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 777d9db7-54f8-3955-95a3-877022e3a563 | -11.33154 | -56.23526 | 2024-10-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9479e9d-72a2-3fc7-bbf0-07b1493ac7b3 | -11.33041 | -56.24295 | 2024-10-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b836b17-7a20-393d-b82b-8e2684e04c64 | -11.32809 | -56.23473 | 2024-10-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5902b068-7fe9-3379-90a4-ea3d437c2857 | -11.32696 | -56.24242 | 2024-10-06 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed21c4bc-0cb5-3740-9147-df7c0ce957c1 | -9.41836 | -57.05711 | 2024-10-06 05:12:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12122cd9-fb6b-3f7e-a2d5-5e8417af6301 | -9.30368 | -57.29213 | 2024-10-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a29aa2e5-93b4-3f9d-80d4-a14bdbba2b33 | -8.97863 | -57.6549 | 2024-10-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b762a31-e7be-389a-9600-7e763570e482 | -8.97808 | -57.65837 | 2024-10-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2589ec88-eef9-353d-bc42-a96d5efcc75f | -9.9665 | -57.75529 | 2024-10-06 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1bb0e87-ca3c-32d2-98e1-6d1a53ec7b7d | -9.96319 | -57.75477 | 2024-10-06 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63a8716d-9fa0-3fd3-81e5-a87c64b91b09 | -9.93806 | -57.85082 | 2024-10-06 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0545426-761b-3e16-940c-352f15531d47 | -9.93476 | -57.8503 | 2024-10-06 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ccb6c52-3261-3d84-b081-a2bd8562b11a | -9.93422 | -57.85379 | 2024-10-06 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eff34c95-717c-3fa9-a2a6-6d95c593b4cb | -9.92082 | -57.47948 | 2024-10-06 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 172e4f55-5c12-3e60-bf77-887694735d00 | -9.91805 | -57.47544 | 2024-10-06 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93a129a6-3bf0-39a9-b055-a4efeac9a902 | -9.9175 | -57.47895 | 2024-10-06 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29b5f8d2-24af-37ac-8be2-514330fd99b4 | -9.91473 | -57.47492 | 2024-10-06 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e4a28bb-3ecd-3217-81cd-2238c739b2b0 | -9.91419 | -57.47843 | 2024-10-06 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a2dfa30c-b36c-34bf-b1d6-ed8034ca7404 | -9.91088 | -57.47791 | 2024-10-06 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3c07eea3-1cae-37f7-85bd-52baef88f7ea | -9.76726 | -56.70836 | 2024-10-06 05:12:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 546d60cc-e009-3b28-ac51-fdb13b1f2cdc | -9.72558 | -56.98132 | 2024-10-06 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 861b558b-d547-31f2-9a46-bc5692050512 | -9.6963 | -56.66424 | 2024-10-06 05:12:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb1b20b2-7e06-3c3c-b92b-1916abce022c | -9.64824 | -56.70858 | 2024-10-06 05:12:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e8d0a0a-1dd1-3683-a814-f160be24b499 | -9.44065 | -57.83167 | 2024-10-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16339cbf-a074-3dee-90ac-2da23671cd3e | -10.45134 | -56.81739 | 2024-10-06 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eee4a6d3-10b0-3e6a-ba62-a838c1efa213 | -12.34779 | -57.36654 | 2024-10-06 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README108.md)
