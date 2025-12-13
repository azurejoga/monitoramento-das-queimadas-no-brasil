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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9b24c02-b6ce-32da-97ee-d12874cd04eb | -1.90717 | -45.4714 | 2025-12-13 06:14:00 | AQUA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3ed08703-117a-3180-913d-da1df46e1b3d | -2.73494 | -45.07681 | 2025-12-13 06:14:00 | AQUA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7134fb2f-98de-3029-87b1-55c1d55cde3e | -3.47048 | -44.19005 | 2025-12-13 06:14:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4f26a6d0-d5ce-350f-bb93-46783c871fa5 | -3.19397 | -41.84303 | 2025-12-13 06:14:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 3a77e8b8-46cf-32c2-8174-9907d46f73ff | -2.73731 | -45.07245 | 2025-12-13 06:14:00 | AQUA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 00574fd8-a173-3e5c-9fd4-57b5cc7e7c5d | -3.20738 | -41.83788 | 2025-12-13 06:14:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 4e029794-48ad-395d-8a1a-410819f0ffa4 | -3.46858 | -44.203 | 2025-12-13 06:14:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 2ba1da85-9feb-3837-8180-02b941793a57 | -3.19179 | -41.85558 | 2025-12-13 06:14:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 3398ab93-dca4-3b5b-8f74-b0ba9ed294b7 | -1.89772 | -45.47002 | 2025-12-13 06:14:00 | AQUA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 28fe4898-b94b-3fe8-8d41-d9aa431175c0 | -3.2045 | -41.85738 | 2025-12-13 06:14:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ce876ffb-2f2b-3056-81f3-80f144c2e511 | -2.73661 | -45.06573 | 2025-12-13 06:14:00 | AQUA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a764d726-e461-3866-8ba2-1ae2d5591a9b | -2.47741 | -47.7704 | 2025-12-13 06:14:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1b0f955b-dd55-36dd-80a6-6268f0ec3b4d | -3.31828 | -46.34741 | 2025-12-13 06:14:00 | AQUA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c59a048-333e-3b58-b9b1-3bf8f6e0f3c8 | -3.19466 | -41.83601 | 2025-12-13 06:14:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| cc8a3c26-0c7e-349c-88d9-de1af3dcdb55 | -3.23839 | -47.25054 | 2025-12-13 06:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| df9f6b76-bd3a-39fc-8f02-d80fad8b9476 | -3.2067 | -41.84488 | 2025-12-13 06:14:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| d12da8e7-2c6d-3226-a79e-a981fa3a52d3 | -3.19127 | -41.86248 | 2025-12-13 06:14:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4cfc766f-3d0b-30e7-ace3-6b2a61c41b9c | -3.2007 | -41.8678 | 2025-12-13 06:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| d0a271cf-d1f8-34e4-9a37-07df43b752d7 | -3.2009 | -41.844 | 2025-12-13 06:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 43.3 |
| a9ba2221-1de5-322e-bdb7-5cbf0ed49f00 | -3.1838 | -45.2264 | 2025-12-13 07:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c2239184-13ee-3c10-b4b1-882514c2f6a9 | -3.2007 | -41.8678 | 2025-12-13 07:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 4e2b7a9d-2121-3251-9d17-ec26bd41200d | -3.2009 | -41.844 | 2025-12-13 07:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 73811b27-bf51-3440-8a61-1cd030503cf2 | -3.2009 | -41.844 | 2025-12-13 07:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 5a8f9e95-10a2-311d-9e94-c89ca7764d6c | -3.2007 | -41.8678 | 2025-12-13 07:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 3c120dee-99ba-3d80-a4c6-49d8895c2812 | -8.2066 | -37.4086 | 2025-12-13 11:40:00 | GOES-19 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 281.5 |


