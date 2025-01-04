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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09e96c6a-6ea8-3425-a1ab-9b58e38186ad | -12.16867 | -44.60447 | 2025-01-04 12:38:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d8474a5a-0c9d-3204-a7f4-8862a122d69b | -17.56182 | -49.9622 | 2025-01-04 12:38:00 | TERRA_M-T | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bf778d35-bd42-37fc-81ae-a3129e4aa224 | -15.79387 | -49.01523 | 2025-01-04 12:38:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8733f14e-9381-3c17-b11d-efef25e0acf3 | -12.16722 | -44.61531 | 2025-01-04 12:38:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 6822cb84-0c2f-3a8e-88f5-dd27b0f4731a | -12.83568 | -39.80038 | 2025-01-04 12:38:00 | TERRA_M-T | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 40.1 |
| 6de79e22-cb93-3551-8c82-7a9a7e262b2f | -27.62896 | -50.21054 | 2025-01-04 12:40:00 | TERRA_M-T | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| c1d5129a-924a-3926-b607-e96c40f13dde | -26.9007 | -49.00263 | 2025-01-04 12:40:00 | TERRA_M-T | GASPAR | SANTA CATARINA | Brasil | 4205902 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 9dc793f3-3d2b-3a82-893b-87c730f4c89f | -21.13022 | -42.38908 | 2025-01-04 12:40:00 | TERRA_M-T | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 1dfa3465-4b2e-3480-ae97-1a1888630919 | -27.37459 | -51.65097 | 2025-01-04 12:40:00 | TERRA_M-T | CAPINZAL | SANTA CATARINA | Brasil | 4203907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| b49617e0-aaa2-3164-9f4c-a9e560524c1b | -21.13043 | -42.87289 | 2025-01-04 12:40:00 | TERRA_M-T | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| eb446e14-954f-3a32-9ca1-d9c9dd8d3e6c | -25.92519 | -50.79284 | 2025-01-04 12:40:00 | TERRA_M-T | MALLET | PARANÁ | Brasil | 4113908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 9db73417-dea8-34c0-8e98-597b6d86d047 | -21.13246 | -42.36736 | 2025-01-04 12:40:00 | TERRA_M-T | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 2784ef56-42ee-3d8c-8e01-1b21a8aaa0a5 | -27.67934 | -50.04932 | 2025-01-04 12:40:00 | TERRA_M-T | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 442e6cdb-57c5-3168-8a92-914149765e58 | -27.67794 | -50.05945 | 2025-01-04 12:40:00 | TERRA_M-T | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 28c3a68e-3979-368d-acc6-6806e76e5260 | -26.47269 | -48.97855 | 2025-01-04 12:40:00 | TERRA_M-T | GUARAMIRIM | SANTA CATARINA | Brasil | 4206504 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 2b67fa96-6d5b-350b-a061-852a5cb64de5 | -28.97242 | -51.06295 | 2025-01-04 12:42:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 0a79c13a-7021-3001-a2f2-c569afafaadd | -4.9103 | -41.1196 | 2025-01-04 14:00:00 | GOES-16 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 80.8 |


