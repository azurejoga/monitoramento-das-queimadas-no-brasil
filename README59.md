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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5f58608-25b7-3259-a066-19c242a33f21 | -1.3932 | -49.0387 | 2025-11-17 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 028b5fee-f627-3326-9504-d2125d563390 | -10.1107 | -44.7883 | 2025-11-17 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 1a9f9ca1-c3fc-3caf-8dc5-01caab0b33d4 | -3.6701 | -44.7303 | 2025-11-17 14:40:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 2bcbec47-d945-3c32-8b36-61808cdbc13f | -10.1718 | -44.5264 | 2025-11-17 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 4e37f670-0ba3-3cbc-905f-4d679ae7351e | -2.4015 | -45.7243 | 2025-11-17 14:40:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| a1565781-97f5-31be-b153-ea912de76b0c | -3.6021 | -43.5868 | 2025-11-17 14:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 627c0314-0db3-33d9-a7bd-c1b6fc8c4034 | -8.5129 | -45.3629 | 2025-11-17 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| c2f76bdc-bbae-36f1-b533-42d7ef3fcdc4 | -3.0895 | -41.6819 | 2025-11-17 14:40:00 | GOES-19 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 11b29a93-9b21-33bf-a3a0-57fc44e51c49 | -10.0649 | -45.299 | 2025-11-17 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| ecaed511-bf99-3153-a271-c9b7e07a1769 | -8.1215 | -43.5148 | 2025-11-17 14:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 6df39232-50e1-3ef1-9e48-26eaaee9cd56 | -3.2533 | -42.5288 | 2025-11-17 14:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e82868b4-0d08-3b85-ba3a-6f5481b03a05 | -3.3841 | -46.0694 | 2025-11-17 14:40:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 48e700f7-5404-392a-a0c8-7618322fd742 | -10.092 | -44.7676 | 2025-11-17 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 42ac6122-4403-3de5-9f8a-af8d3a02a87b | -10.8516 | -44.8748 | 2025-11-17 14:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 6e24f7c0-665e-3e23-a605-052a9459cde2 | -10.5197 | -45.3784 | 2025-11-17 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 09bebbdb-5ffa-3013-bfe8-752f233ab0dc | -3.9554 | -43.7773 | 2025-11-17 14:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| c8299bff-4dbe-35e1-8832-ba0091208cdc | -11.6755 | -44.7342 | 2025-11-17 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 323.9 |
| a175b2c6-b909-3bf6-b81e-65e3bae8ce6e | -3.6451 | -45.9025 | 2025-11-17 14:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 72e3c28d-c324-3528-b0f0-18d8459da7ff | -11.7805 | -45.2963 | 2025-11-17 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |


