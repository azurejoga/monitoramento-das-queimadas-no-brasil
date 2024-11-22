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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b20f7c37-7fd6-3e69-b9e7-ed23ffae111c | -1.9458 | -49.5177 | 2024-11-22 14:30:00 | GOES-16 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 575c1fe6-3214-3a5b-b141-cb7cb8f73818 | -3.9646 | -45.3272 | 2024-11-22 14:30:00 | GOES-16 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| e0168666-d09a-3dba-9433-2ac327e3f163 | -5.529 | -43.3304 | 2024-11-22 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| cd409d43-459c-3fe5-92ff-03b5d0a9cc29 | -4.1782 | -43.9499 | 2024-11-22 14:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 02244a6a-acbc-30f5-a8d6-b8e851df2ee0 | -4.1783 | -43.9268 | 2024-11-22 14:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 3c0bc63d-454b-3c96-8a59-d4a00e9ff324 | -3.7457 | -44.5447 | 2024-11-22 14:30:00 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 98cca8ab-0545-3a99-9b94-62f08d7dfe39 | -3.446 | -41.4735 | 2024-11-22 14:30:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| b049c80a-c0ab-3429-b428-c8afa5d46734 | 1.4002 | -55.9453 | 2024-11-22 14:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| fed23132-e31d-3605-a1fb-537d4edb59de | -5.4363 | -43.2206 | 2024-11-22 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 7b50ab13-7a01-387c-9f31-fd27121b28cd | 1.4185 | -55.9648 | 2024-11-22 14:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 06845ee0-660b-37dc-8f42-f74c79af6258 | -0.8182 | -51.7868 | 2024-11-22 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 61.9 |
| c0a62b9c-1e64-340e-bfe5-a4bbda54c9c3 | -3.7719 | -43.2534 | 2024-11-22 14:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| acdef53d-1811-35d6-b4e0-71e475253a51 | -5.4546 | -43.2659 | 2024-11-22 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| d8837fc3-e2a7-362b-9638-8a5e632d10fe | -5.5325 | -42.9325 | 2024-11-22 14:30:00 | GOES-16 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 997c8d2c-733f-30b0-b6f6-91068a932f9e | -5.4734 | -43.2646 | 2024-11-22 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |


