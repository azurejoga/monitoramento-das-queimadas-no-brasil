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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38757f41-d101-30e5-a065-8f656fb3df9b | -16.58763 | -57.80262 | 2026-01-30 12:36:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| bec5a4d8-2b53-31e0-b9be-e102fc570123 | -14.53332 | -47.88768 | 2026-01-30 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 29ff0942-2912-368e-8f0b-c2c0d6894b45 | -20.29323 | -57.34758 | 2026-01-30 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dc7b508e-1e43-3256-b5da-c73f1538b0d5 | -20.19988 | -58.03629 | 2026-01-30 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| bf4e1166-d6bf-37fc-a3b9-18d66bc42ebf | -20.3125 | -57.34747 | 2026-01-30 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 006921d0-9b6a-37e6-a4be-ca9e55789c43 | -25.78777 | -53.3061 | 2026-01-30 12:40:00 | TERRA_M-T | SALTO DO LONTRA | PARANÁ | Brasil | 4123006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 424d8a5e-61f9-34c1-ba14-2d09326ca238 | -28.45178 | -52.80609 | 2026-01-30 12:40:00 | TERRA_M-T | NÃO-ME-TOQUE | RIO GRANDE DO SUL | Brasil | 4312658 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| f4e485a8-b88e-3ac1-b96e-ce934ffbef1c | -26.25648 | -53.62683 | 2026-01-30 12:40:00 | TERRA_M-T | BARRACÃO | PARANÁ | Brasil | 4102604 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 1eb9d566-1cfe-32c8-bc2a-f855091421b7 | -28.50978 | -50.94103 | 2026-01-30 12:40:00 | TERRA_M-T | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 6165a7ab-57f8-3275-acab-e279cd2a6ec4 | -25.91967 | -53.46841 | 2026-01-30 12:40:00 | TERRA_M-T | AMPÉRE | PARANÁ | Brasil | 4101002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 42fcb4ea-6e14-38e2-8c5b-ad64a97608bb | -28.21632 | -48.70243 | 2026-01-30 12:40:00 | TERRA_M-T | IMBITUBA | SANTA CATARINA | Brasil | 4207304 | 42 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 88b01cb7-837a-37f9-9cbe-3a0a740b92d6 | -20.4088 | -57.895 | 2026-01-30 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 8bfc89d9-2203-3f4c-9f91-93c818af9bfd | -20.3272 | -57.9478 | 2026-01-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| c84085f8-7ff8-3164-8459-d687226045cd | -20.4088 | -57.895 | 2026-01-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| b608edc3-bf2d-32fd-9a1c-f6954d24ad63 | -20.3294 | -57.8224 | 2026-01-30 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.1 |


