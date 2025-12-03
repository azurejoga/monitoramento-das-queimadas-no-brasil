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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 727a510c-1bf9-31ee-8740-e9dcd21e9638 | -2.21009 | -47.99896 | 2025-12-03 06:24:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| f8485b5a-1aa8-3d88-915a-da0b316dd3e3 | -2.60266 | -49.25298 | 2025-12-03 06:24:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 581db381-a172-3fc3-a02b-f242fa0e6a18 | -2.20056 | -47.99756 | 2025-12-03 06:24:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 96201f05-d3e5-36f4-9ce0-0c475ca8d4b5 | -4.39054 | -43.14223 | 2025-12-03 06:24:00 | AQUA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 44234a36-da24-34e7-a514-ac79518e60f4 | -2.3541 | -50.1007 | 2025-12-03 06:24:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 23f47ef6-55d5-3fc3-9407-843a774409e8 | -2.35278 | -50.10947 | 2025-12-03 06:24:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 123838af-d08f-3728-a49e-ab047ffa5c15 | -14.68098 | -53.39677 | 2025-12-03 06:26:00 | AQUA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0ff5c030-38ed-3abe-875e-7e5956dfe3a5 | -15.11845 | -52.94407 | 2025-12-03 06:26:00 | AQUA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 122a90a9-6873-38d8-9b66-a6a7a24f2469 | -12.79676 | -50.88383 | 2025-12-03 06:26:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68175538-0c12-30c9-93b5-b9808553fa19 | -15.1171 | -52.95315 | 2025-12-03 06:26:00 | AQUA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8ffb0897-408f-3fa3-bb21-6de9582f6447 | -14.67962 | -53.40578 | 2025-12-03 06:26:00 | AQUA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8b22d9c7-f11e-3575-94b7-16c7d45b48d0 | -21.62086 | -56.1289 | 2025-12-03 06:29:00 | AQUA_M-M | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 27d232ec-92c1-3684-a917-dbf0f173c1b0 | 1.9867 | -55.7211 | 2025-12-03 06:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 27f55eef-2905-3417-96dd-b69784b04150 | -3.6748 | -43.9066 | 2025-12-03 07:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| a2b8af89-bf99-3e05-8f53-d9526699edce | -3.6935 | -43.9057 | 2025-12-03 07:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |


