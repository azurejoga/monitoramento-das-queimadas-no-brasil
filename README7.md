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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f6ce844-3eac-3ae2-8e70-3e3cfedce5b1 | -13.981 | -46.0301 | 2026-05-12 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 89a78701-c576-390c-aecb-4ad0aa7374ae | -13.9615 | -46.0334 | 2026-05-12 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 5fa405bd-dc27-34a0-a709-30dfd201ca0e | -11.9498 | -43.3781 | 2026-05-12 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| f20da94c-e7a4-3412-b227-d08ede18ebd9 | -14.1317 | -45.3111 | 2026-05-12 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 42c59f80-013b-3ad9-bc11-352b8163fe00 | -13.9615 | -46.0334 | 2026-05-12 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| a0b42097-1b1e-3539-8564-2f41b8ee6106 | -11.9498 | -43.3781 | 2026-05-12 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 09ce4eeb-a053-3faf-8cab-247025934580 | -14.1312 | -45.3344 | 2026-05-12 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 2ce665b5-48fc-3c74-818e-1267edcc44df | -11.9305 | -43.3812 | 2026-05-12 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| e67dd04b-5897-3e06-ab2a-1ee57d7aa8d7 | -14.4001 | -44.5846 | 2026-05-12 14:20:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 883f3468-5310-3b8a-b4dd-d369b033868d | -13.981 | -46.0301 | 2026-05-12 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 6775edde-5f5d-3b8c-94ef-7088b77f21f9 | -14.1317 | -45.3111 | 2026-05-12 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 748c71b1-8b45-3e48-aec9-a243036513d7 | -11.9305 | -43.3812 | 2026-05-12 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 60d14573-8ca8-3975-b5b3-2cd16fcc3c99 | -13.9615 | -46.0334 | 2026-05-12 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 4bdbeee8-859d-3bf4-94ac-5641126c5385 | -14.1312 | -45.3344 | 2026-05-12 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| a5447aa4-d3f4-3d17-b027-67bbdb58b0c8 | -11.9498 | -43.3781 | 2026-05-12 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 9360b26b-196b-32d0-a1b6-6b283e8c7996 | -13.9615 | -46.0334 | 2026-05-12 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 59be24f6-78f4-3719-975e-79f65bc6a30e | -12.4875 | -45.4434 | 2026-05-12 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 6fc3f5d1-3b3e-36f1-8a1c-0d60b536e16f | -11.9498 | -43.3781 | 2026-05-12 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 89f669e4-b3e0-3872-afb3-b95e9593a473 | -14.1317 | -45.3111 | 2026-05-12 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 2254b78d-1403-3d0a-82ac-4aec1be34aa9 | -14.1312 | -45.3344 | 2026-05-12 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 34ca4493-dc12-3708-b341-3806b7c317ee | -11.9305 | -43.3812 | 2026-05-12 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| e56f443c-4e3b-319f-a40e-5b41ffdf8c77 | -11.9305 | -43.3812 | 2026-05-12 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 4f6a5a33-4fa5-3f27-a3bc-68de81ffe674 | -14.1317 | -45.3111 | 2026-05-12 14:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| b320530c-2a9c-369a-a2d6-c82f87ea6a2f | -11.9498 | -43.3781 | 2026-05-12 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 7c639297-45eb-3437-83b6-c4218e7fbc11 | -14.1317 | -45.3111 | 2026-05-12 15:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |


