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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b4d6bc6-7b15-3a5e-9cf9-994eb55e8540 | 1.79231 | -60.51865 | 2026-03-24 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99955185-3a13-3bef-8ee6-7cdf9eda360b | 0.98863 | -59.38207 | 2026-03-24 12:44:00 | TERRA_M-T | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 583b22d8-c8aa-37d7-9a5b-328441f7c361 | 0.76997 | -59.86536 | 2026-03-24 12:44:00 | TERRA_M-T | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d5e70957-0299-335d-b462-2b619d4b3e22 | 0.77159 | -59.87696 | 2026-03-24 12:44:00 | TERRA_M-T | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8ee003a1-6e8c-3726-aaea-d2c029b1f6af | 2.78488 | -60.30242 | 2026-03-24 12:44:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 34445ce0-a80f-3c05-ba4c-bc8f36f07022 | 3.58383 | -61.01053 | 2026-03-24 12:44:00 | TERRA_M-T | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 629c7c1b-16a9-33a7-8ba8-a2236fa40f6d | -18.78584 | -53.47854 | 2026-03-24 12:49:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c72c8a7f-f3fe-3cdf-9ac3-ed346d9f873d | 3.913 | -60.9584 | 2026-03-24 13:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| b7a3d87a-5751-329f-9bb5-6e1ec2a4f71a | 3.913 | -60.9395 | 2026-03-24 13:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0cb1a1ac-4c28-368a-859f-02c78c8e50c0 | 3.8947 | -60.9399 | 2026-03-24 13:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 53e164aa-518a-32a0-8b47-8469eed4383d | 4.0597 | -60.8037 | 2026-03-24 13:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d593ce76-0c6c-3b01-9cb6-b2357d25f94f | 3.913 | -60.9584 | 2026-03-24 13:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 67.5 |
| b5c96b81-634a-3329-a46d-a0e2f6cfcbc1 | 3.913 | -60.9395 | 2026-03-24 13:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| d59ad409-1777-3fd8-b3c8-67342d1ae0c6 | 4.0597 | -60.8037 | 2026-03-24 14:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 52992e08-bb1d-3094-aefa-416d5554d8e3 | 3.2361 | -61.2359 | 2026-03-24 14:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 592d3617-bab3-382a-8579-44c15e43fff5 | 3.2361 | -61.2359 | 2026-03-24 14:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 87.9 |
| e4826312-af61-3b44-ba7e-242b0dd23b3c | 3.6021 | -60.9835 | 2026-03-24 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |


