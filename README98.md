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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88d573d0-862b-30a6-8127-713105d7805a | -9.0951 | -47.0093 | 2025-09-06 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 187.0 |
| fd2cea7d-8c38-3dde-a8ea-ba6778fbe29e | -12.9668 | -54.791 | 2025-09-06 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 268f0e03-2d63-3be9-9549-d4d1eb112b3d | -15.3064 | -52.7208 | 2025-09-06 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 191.6 |
| acea9684-2b5c-3cfa-b1b7-6082dd55cf58 | -13.0041 | -54.8487 | 2025-09-06 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 131.1 |
| ce715aa7-d449-368e-81b9-d6c6fbf85fd2 | -5.8485 | -45.3038 | 2025-09-06 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 7d62bd8d-a409-3706-94c4-af6750d90138 | -13.0044 | -54.8282 | 2025-09-06 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 5b8ad74f-a8cb-3788-8c29-c310b024d353 | -6.8281 | -52.8143 | 2025-09-06 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4e28f166-12cf-39a9-bf19-7fdb3c23582a | -12.948 | -54.7724 | 2025-09-06 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| c32f6738-dfee-3835-8dcb-6894c463e60a | -15.719 | -53.5532 | 2025-09-06 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7717db7c-3ed2-32d5-a2e4-40eb6f694131 | -8.0223 | -45.4354 | 2025-09-06 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 161.8 |
| ba4e7cd9-4eb6-3593-a65e-3eef5c871f04 | -5.5695 | -45.1425 | 2025-09-06 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 245.4 |
| 8d162ac0-3ff6-3963-aaae-651038f2c74b | -13.0157 | -48.0771 | 2025-09-06 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 3f73f7a7-f028-3265-8aa0-ccb8e6ca73ca | -6.2672 | -53.4379 | 2025-09-06 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f8714359-9b49-3f9d-8db7-5a3a9c614dbb | -11.338 | -50.2968 | 2025-09-06 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 562d2fc5-670a-326e-8c69-b35ae8c743f0 | -16.3345 | -52.9387 | 2025-09-06 14:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 94ee1eb2-f567-3d84-b0c5-8413cc2185e8 | -13.3195 | -51.6413 | 2025-09-06 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.1 |
| ecd6b524-1657-38b3-804c-d6599b3b6791 | -6.2857 | -53.4369 | 2025-09-06 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 7aaaf653-b8f7-3cc8-a1f6-b73f55056f82 | -6.0043 | -46.7018 | 2025-09-06 14:40:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 9e1bdf30-852e-3161-9b62-8336e6e713ea | -8.4831 | -62.6549 | 2025-09-06 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| c6f66b9d-0392-30f9-86cc-62c077820134 | -10.7682 | -47.7523 | 2025-09-06 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| c8d063c8-80e5-389d-b164-cf84b593d9b7 | -9.4623 | -60.5104 | 2025-09-06 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| e29ab0cd-986f-3318-a192-d6988be6c4cc | -6.267 | -53.4582 | 2025-09-06 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c9f92f52-284e-38fa-9735-881cfeb21ece | -11.0242 | -45.9729 | 2025-09-06 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 282.0 |
| 29262d39-0545-3a95-b6e5-00bea7fb0918 | -6.7233 | -51.9762 | 2025-09-06 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f66b9631-83bc-3a06-97c6-e9adf3650f30 | -6.1679 | -43.1869 | 2025-09-06 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 7644dd91-5c48-30d0-8140-2f37b6476f0a | -6.1944 | -53.2585 | 2025-09-06 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 180.1 |
| 19bc7e53-8f5a-346f-ab54-d1a360186277 | -7.0132 | -44.9385 | 2025-09-06 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| dd6cc75b-c1ed-35ea-9d0c-570e7e0da8dc | -10.913 | -50.8762 | 2025-09-06 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9dbe4d42-e2f8-3594-a78a-1a3d28cfdcd8 | -12.8636 | -47.9877 | 2025-09-06 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| bcf4efac-01d4-3a13-86b5-ebd89bf853a5 | -13.8602 | -46.2566 | 2025-09-06 14:40:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| fed5287d-6176-3a92-a38f-f8a4b935817b | -13.0161 | -48.0549 | 2025-09-06 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 437cef23-152b-3700-a603-f913b775b96d | -9.4495 | -62.3675 | 2025-09-06 14:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| c8f7528b-472d-3837-b88e-564242148252 | -5.7298 | -43.9189 | 2025-09-06 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 254.8 |
| 5bd6678e-e9b4-39db-b3df-056a0ceb18a0 | -9.0948 | -47.0316 | 2025-09-06 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 678e1ff5-72cd-340e-a73f-87b9d25fd915 | -5.9699 | -53.5953 | 2025-09-06 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 39b8abe9-8059-33da-b132-3254d67c2588 | -6.8841 | -44.7215 | 2025-09-06 14:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 337.0 |
| b0e29621-f40a-3b19-98ca-3fc184010406 | -10.7372 | -48.5693 | 2025-09-06 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 6f3061b8-a222-3718-8476-c8c22f88827b | -11.0249 | -45.9274 | 2025-09-06 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |


