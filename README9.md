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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76a6bf7b-574d-30bf-ad5e-87596c134c87 | -10.12087 | -47.37728 | 2025-12-31 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5083452f-1c3c-3da8-bc45-e8c7167520d8 | -12.54236 | -57.34055 | 2025-12-31 12:38:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5404a5b1-eb51-3a7d-8ade-5c2a6a1d6ac1 | -15.32757 | -57.80841 | 2025-12-31 12:38:00 | TERRA_M-T | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 74617897-4362-3cd0-8a9a-faa2c4699b46 | -11.74213 | -49.08131 | 2025-12-31 12:38:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1bf895b4-4ae3-3920-97cb-848a8013f167 | -10.10766 | -47.37554 | 2025-12-31 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6d68f604-a911-31f0-84bb-f3cd7d8b46f2 | -11.73562 | -49.07468 | 2025-12-31 12:38:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9fb3f398-5887-34d9-afb6-e52fdd0a1f2c | -14.26427 | -57.0775 | 2025-12-31 12:38:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 67fecfd9-a34e-39b0-b85e-4099ed2575cc | -18.78639 | -54.14148 | 2025-12-31 12:40:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8807ac7e-f826-3464-91db-a48aea3fcac7 | -22.39347 | -53.85941 | 2025-12-31 12:40:00 | TERRA_M-T | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 2f18b30e-20c8-3938-b61b-4680c545475c | -19.21721 | -53.43622 | 2025-12-31 12:40:00 | TERRA_M-T | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 60aa1d70-6b95-3166-990e-ee6d1a256252 | -31.29044 | -54.07648 | 2025-12-31 12:42:00 | TERRA_M-T | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 8.6 |
| 9f1a0604-fbfe-3920-b36c-1f78d1bb7574 | -1.0809 | -47.9916 | 2025-12-31 12:50:00 | GOES-19 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 567416f6-453e-3db9-8b41-a500f3210b34 | -7.2646 | -38.0763 | 2025-12-31 13:00:00 | GOES-19 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 97.9 |
| c213c20c-d3b5-3b94-8826-9e53d70c424d | -1.0809 | -47.9916 | 2025-12-31 13:00:00 | GOES-19 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 8dc467a7-284a-320e-8e31-2c049899d20f | -1.0809 | -47.9916 | 2025-12-31 13:10:00 | GOES-19 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| e78c11eb-b9e1-376d-9860-037f62d399b5 | -1.0809 | -48.0132 | 2025-12-31 13:10:00 | GOES-19 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b2763351-50c9-32bb-82de-b6c6188e75f6 | -7.2646 | -38.0763 | 2025-12-31 13:10:00 | GOES-19 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 93.5 |


