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
| f5889735-aeb2-3a24-86cf-d24bdae5aa25 | -1.7875 | -52.74181 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aa84a5f3-e903-358f-ade9-1098f5a54979 | -2.86688 | -54.01169 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| eb4c47c7-0a84-3f41-9fc9-9de38292df6f | -2.54616 | -53.42118 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| beb8747c-610f-3f72-8acf-ebcb87e6e024 | -1.90685 | -52.86894 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a6a36e26-1a76-3e4b-9a34-cacda38c4862 | -1.38559 | -53.55612 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b5099be2-41bf-3d64-932a-dffa9c9118ec | -0.96429 | -51.71967 | 2024-12-02 01:13:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f6b2e24-5687-3b9b-8512-2ff933e5db23 | -3.33706 | -53.54908 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 79dfe2fa-2057-38b6-97c8-010d85d757ef | -1.44362 | -55.42902 | 2024-12-02 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 58a82648-604e-3aac-a22b-6660f389c573 | -2.87789 | -54.01323 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8834da53-2726-38d1-a542-495860cbbf9f | -3.14055 | -53.84978 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 166b91a7-7113-3825-bf41-7eb6d70c1ba0 | -3.34223 | -53.38018 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7f6f1557-c349-308f-8baf-568a3c725d19 | -0.3355 | -51.5963 | 2024-12-02 01:13:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 441decd3-decf-3e56-8d04-0c93b677754d | -2.61139 | -54.29124 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dbd02ebe-ae0c-3a33-886f-212f15efd8f9 | -3.04007 | -49.37658 | 2024-12-02 01:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2c60f76e-81ce-3fd2-9983-d8019814f9a1 | -3.38824 | -51.14288 | 2024-12-02 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 09d306a2-e382-331d-9bc9-3a68c4e9e6b7 | -1.72644 | -52.4986 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46c3f230-f7f7-31f2-8f84-261bdf57e091 | -1.8795 | -56.3074 | 2024-12-02 01:13:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c5a76487-9849-3ef8-8bfb-566996d97fd5 | -0.59206 | -51.68953 | 2024-12-02 01:13:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| aa7019d3-170a-335f-b27e-0022389ae556 | -2.41819 | -54.01858 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b523d290-ec5e-30dd-9542-93ec210d9a46 | -1.00871 | -51.72824 | 2024-12-02 01:13:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e94a3874-f038-3284-a00d-8f513b11d88d | -2.70468 | -52.91151 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e4e9d905-f9c8-3bf9-973b-d46cf11eed74 | -1.72513 | -52.48913 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7985d77f-b84c-358d-bef4-5584a35aa385 | -2.04716 | -51.19171 | 2024-12-02 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5bf332c9-4ad4-371d-bed1-b740031e55c6 | -2.7249 | -54.17292 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| dde81c8e-2b8e-39e3-bcd3-ae2db4cecd3e | -1.72521 | -52.62358 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3fb635fc-1747-3968-817e-fffc0898303f | -1.67154 | -52.1032 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e4de0e31-ec35-33cb-8430-170897b14cc8 | -3.25387 | -53.87287 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a7712cf-1447-39c9-bd57-74e3281af9d1 | -2.43625 | -53.62957 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7277cded-ca7c-3b20-b9db-257ee5b2a95b | -3.13932 | -53.84097 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 59827960-3d75-3e2c-8bee-cc6717bbe9f3 | -3.09789 | -54.141 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8abba86e-7256-395c-bc64-92709c360451 | -2.57158 | -53.40851 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 53c18eef-66e0-3b03-bfc9-4fef444a56b2 | -2.54492 | -53.4123 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 70063c15-92e3-3b13-8ebc-9d29643c8d61 | -3.34099 | -53.37132 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05305c26-91ed-3504-b0d1-e320afe97332 | -1.07813 | -53.46305 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 78c5b3e1-3113-3917-996c-448c969df9e8 | -1.23636 | -51.61951 | 2024-12-02 01:13:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ab2274ac-6694-3bb2-97ef-7e0135baf092 | -2.52632 | -54.06934 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 89809c58-7445-3f7c-990d-66f6dabbd502 | -2.41667 | -54.15088 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1f290fd-15dd-358b-9266-ef7d44b9f5ba | -2.25873 | -53.61266 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 46e21256-0e1e-3bb6-9793-d77d8a19dab4 | -3.21251 | -54.17256 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb520256-dc20-3f86-9285-4681f798918f | -3.53376 | -53.50903 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 49ab838d-1766-35fd-9099-730d697474a1 | -3.37442 | -53.22187 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b0e1eaf-d264-3c84-82df-d8890f15567d | -2.8956 | -54.01073 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a533fa83-dbf9-3d5e-aede-66315eec825b | -1.68035 | -53.94699 | 2024-12-02 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9521e50-3ad6-398f-92e1-51da44144800 | -3.07075 | -53.68625 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| b9ac0ff0-2d91-34c4-a070-50e0d76567f2 | -2.25996 | -53.62151 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 493f7d90-7be3-3196-91a4-96b250e397d6 | -2.79293 | -51.9039 | 2024-12-02 01:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| b63d2102-545e-369c-9b36-dacfb9ddffb8 | -3.07061 | -50.98863 | 2024-12-02 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7bd7b14c-87df-345d-b7de-f8909002aff5 | -3.46804 | -53.49131 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7a2fffe5-1e4e-3e3b-a6cc-2b5e9aa53e3a | -3.53499 | -53.51787 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0475b219-9ab3-3614-a80d-b27870fe39d9 | -1.67591 | -52.79815 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e504ff24-6917-37ab-b5f7-07c1d0d321a1 | -3.64075 | -54.67099 | 2024-12-02 01:13:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c91620e1-cc14-3c64-93d9-cfb05a4bb3dd | -2.89682 | -54.01955 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 610898f9-ae6d-34e7-ad0b-ca525c2dc426 | -3.1743 | -53.63829 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4dfe2702-eedb-344c-ac0a-f8873cfa52a2 | -1.72651 | -52.63294 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 79e8d798-5193-3e4b-9fd6-6fa3420938d1 | -2.27084 | -53.62312 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 77b312a0-a668-3101-bdda-4dfa92e460bd | -2.74233 | -51.74993 | 2024-12-02 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 825e058f-d5d9-38be-a683-248867aca851 | -2.86294 | -53.322 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f85bbc6c-1d7d-333e-a9b3-bae25ee50c1b | -1.48021 | -52.64811 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81424a78-c3c8-386c-a926-42150d90418c | -2.98839 | -53.35539 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3999e058-6788-3953-8c04-cbc9320f3a0e | -2.63544 | -54.19142 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f7cc044b-cb42-3878-b5ed-6fb1f5d19036 | -3.75709 | -54.64861 | 2024-12-02 01:13:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 30793b4f-4d5c-3b80-acef-8501d3ea0502 | -1.174 | -53.4253 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 648987b9-41f3-36fd-a85c-7cd957caaba7 | -2.59145 | -54.21297 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6c221513-dc09-350e-b78a-ba6cd5d25dbc | -2.6797 | -46.61492 | 2024-12-02 01:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 3ae4943b-2f9b-351d-a146-6ce5ae88a48d | -2.856 | -54.19312 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 751b1f02-5dd0-3d2a-bf61-67413f264c3a | -2.98732 | -53.28303 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8a8ce3c3-f99f-3682-81b6-084c282235de | -1.70415 | -52.47277 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 84584f4d-3d56-355a-b501-5c1222d0d612 | -3.25491 | -53.62106 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e4bbade0-56a0-3cc8-99c6-5f976dd5696c | -2.41696 | -54.00977 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 539dbc60-1f31-3835-a0a2-77ffddef77b7 | -3.49848 | -54.17749 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 15dd7895-3432-3066-8331-e98be930765d | -1.28351 | -51.64985 | 2024-12-02 01:13:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f42183e8-0ce6-3b61-bb7f-13e362ad8987 | -2.02661 | -54.32012 | 2024-12-02 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cfb50905-b792-3af4-be8d-119309b96635 | -3.02675 | -51.53643 | 2024-12-02 01:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 773723f5-6103-375b-a8f6-27080164daab | -0.26009 | -51.50177 | 2024-12-02 01:13:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c15ee3f1-ee15-33a9-910f-7ca103daa7d2 | -3.28891 | -50.43859 | 2024-12-02 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 7d9ab2fe-d1e4-3f10-947e-63559953cfb9 | -2.04871 | -51.20258 | 2024-12-02 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6323bd28-6003-3562-bea9-e9a369366a5c | -1.20056 | -53.87459 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22410d89-adc3-3fec-ab93-09c80f3bf86e | -2.55257 | -53.40216 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7abdef24-19e3-35f9-841d-1ed4e81e8492 | -2.89832 | -53.96542 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 965a89e4-33f1-3b18-a7ab-d9a27aac7f2f | -2.96279 | -53.89613 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3abe7d2f-acf5-30fa-966b-1abf156fc93a | -2.99073 | -52.5196 | 2024-12-02 01:13:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 566a4d14-dbfb-3f6e-838e-4d3add287bb0 | -3.26622 | -53.63745 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 28e0a7a5-48bd-333a-a9bd-ef7ec903df68 | -2.02538 | -54.3113 | 2024-12-02 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c47882e3-87af-381b-95b1-a160c6b65db0 | -3.52768 | -52.8043 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c7c81799-6779-3445-8473-ead0951c2963 | -3.09459 | -53.72784 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 97a849bb-e044-33f1-b51b-002ade73b2c0 | -1.56934 | -55.3396 | 2024-12-02 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f265017a-ce34-3118-bb91-b0289cfca2fa | -2.81103 | -54.0645 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 46bc108e-0674-3a28-8e15-097988b44e2d | -2.79971 | -48.67946 | 2024-12-02 01:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c2e01312-c0e6-3eea-aace-2db076e9f669 | -1.29733 | -52.8574 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2ac00459-2f69-372a-be05-f55c247b84a9 | -3.09666 | -54.13215 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 32113ac8-e5aa-3922-a22e-51cde9029481 | -2.81225 | -54.07332 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 896de1ce-d570-3c49-960e-5f7e40123ee2 | -1.37134 | -53.64881 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4a2072e-4c05-3fe6-9f41-c43ec2dbfde6 | -1.2349 | -51.60897 | 2024-12-02 01:13:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 4d326087-0790-3a30-9032-1bd76ff9466b | -2.8078 | -53.05655 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 242ba25f-b953-3069-9b6f-6eb42d49f9fa | -3.17822 | -54.32837 | 2024-12-02 01:13:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1e0478a3-5212-3b9a-af95-acd33e5cdfd9 | -2.63063 | -53.36709 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| cf963b96-588c-3ebf-a3d3-5c3632146e9e | -2.90107 | -53.06448 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 45c09685-e12a-3039-8667-0ea23ca15397 | -1.27531 | -52.69943 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d1d5e0d1-bd92-3a98-819a-bd8d0d9e23dc | -2.76307 | -54.12252 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e7c17cfd-cea9-3300-ab3f-20a13c202ea0 | -1.45587 | -53.5942 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README16.md)
