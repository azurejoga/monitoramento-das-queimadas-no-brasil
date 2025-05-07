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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1e87f67-9e4f-3f92-b316-56f8a4645046 | -11.3668 | -49.6265 | 2025-05-07 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 8c8b23c8-c965-323a-b10f-b425ce14771c | -18.4279 | -54.7129 | 2025-05-07 14:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 117.7 |
| f2388a78-c732-3538-a960-a290b9800ade | -10.6479 | -46.9221 | 2025-05-07 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 3e9361f1-8585-38f1-88b3-c157ca0c0729 | -10.5144 | -46.9608 | 2025-05-07 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| bfdda581-65ac-355e-9fe9-260979bd929a | -11.3668 | -49.6265 | 2025-05-07 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7af4fd50-535b-33fd-9a4e-12a3b6d60028 | -10.6479 | -46.9221 | 2025-05-07 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e5c75469-b054-3af6-af47-d92c19900b88 | -18.4283 | -54.6916 | 2025-05-07 14:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 58336c5f-fdf5-33aa-8dec-d23377ec4cb0 | -10.9733 | -44.441 | 2025-05-07 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 147.0 |
| ffd72998-224f-3178-9123-cf9587d1ef2c | -18.408 | -54.7158 | 2025-05-07 14:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 121.0 |
| bbd43472-d8f8-3e5d-b1ab-3ab409a17bde | -10.8126 | -49.9258 | 2025-05-07 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 2b4dc728-8c8d-3f6e-8094-1e8596a5936d | -10.6479 | -46.9221 | 2025-05-07 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| bcaf12bb-9f6e-3e1a-8c37-b0a3ee0bb3d8 | -10.9736 | -44.4177 | 2025-05-07 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 866f22b8-5ef1-3c3f-ad19-b08e09bd1764 | -18.408 | -54.7158 | 2025-05-07 14:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 1eba8eab-9a22-31c6-9a91-4d20c2ce08cc | -10.5904 | -46.9515 | 2025-05-07 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 5825321d-9c9c-3fdf-b512-5ca41c3d6e47 | -10.8566 | -49.4902 | 2025-05-07 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 3e569552-642c-3a0d-b392-ef8220d85c63 | -10.6479 | -46.9221 | 2025-05-07 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c305caba-7648-3026-9f66-007908a200ac | -10.9541 | -44.4437 | 2025-05-07 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| aa04bdbf-8e4e-3ff3-b091-3bbd0c525250 | -9.6634 | -49.7228 | 2025-05-07 14:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 6a9245c1-d299-354f-bc1c-4ed19e9edc8d | -18.408 | -54.7158 | 2025-05-07 14:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 363fea96-2aba-318d-817b-4a21446ccdad | -13.4905 | -52.9505 | 2025-05-07 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |


