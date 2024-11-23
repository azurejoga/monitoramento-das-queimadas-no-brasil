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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39130c45-de29-38af-bacf-c1a2a82b1f26 | -2.9619 | -44.9639 | 2024-11-23 14:20:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 3859e4d1-b5b5-30ec-bf46-241dfe7623c7 | -7.3727 | -39.986 | 2024-11-23 14:20:00 | GOES-16 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 142.7 |
| 7499f97b-ae64-3dc3-9e3f-2307baff38e9 | -5.2464 | -43.5369 | 2024-11-23 14:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 6af7222a-b039-3a4f-84f0-e69cb7ecd81a | -4.2606 | -48.6755 | 2024-11-23 14:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 3d3a8126-7663-3a6b-b3ca-6c0e640e6227 | -1.8985 | -46.4263 | 2024-11-23 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| e06a3292-0be9-3e4e-a986-b86e283d6737 | -3.5144 | -42.5873 | 2024-11-23 14:20:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 0f90bf5d-fd7b-3739-a706-2291a8a8b54f | -2.694 | -52.0653 | 2024-11-23 14:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| dfb490d1-6e88-33ec-9fbc-e4e653efedf5 | -1.1103 | -53.3953 | 2024-11-23 14:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b4e0877a-3e35-3eac-93ca-40702ed58e12 | -1.5493 | -54.3357 | 2024-11-23 14:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| b2e7143c-0a58-3b0e-a4e3-46dcfe967114 | -2.4456 | -49.0816 | 2024-11-23 14:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 04b81b42-8710-3b06-9adf-51f46b5dc719 | -1.7892 | -53.6293 | 2024-11-23 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 55335495-1532-3df4-8129-2587522a65c7 | -1.8576 | -47.8926 | 2024-11-23 14:30:00 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| af6e3b54-4a4b-3ab8-816a-9f01ad54c7e0 | -1.4408 | -53.3715 | 2024-11-23 14:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 535caa76-342e-3ada-b3cd-bc872d13a3be | -2.962 | -44.9412 | 2024-11-23 14:30:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 92.8 |
| ae04c8e1-a2ec-349a-b2f2-bac1dc9e8a80 | -2.1302 | -49.5563 | 2024-11-23 14:30:00 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 5efa308e-ef1c-3d20-8175-16b70d576f1f | -1.7892 | -53.6091 | 2024-11-23 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4b70e4d1-dad9-3230-9bd3-d65e69feb199 | -1.5493 | -54.3357 | 2024-11-23 14:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 3d1a47c6-1cad-3d4f-b763-667dabc401c0 | -1.5351 | -51.9847 | 2024-11-23 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 48e127bc-678b-3753-932f-558000244d0f | -2.7615 | -48.5812 | 2024-11-23 14:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 492c9bc2-9ada-38e4-ab31-cb96679633cc | -2.9619 | -44.9639 | 2024-11-23 14:30:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1f08c897-659f-3064-9eb1-5ecf4a8a88d7 | -3.4195 | -42.8736 | 2024-11-23 14:30:00 | GOES-16 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 901f6535-4273-3cd1-b449-553c055fb902 | -5.0996 | -43.1744 | 2024-11-23 14:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b81ed859-e948-3340-8e9b-3b4ec884da29 | -1.4224 | -53.3919 | 2024-11-23 14:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| cc2592ac-d2d9-3900-a89e-6b446b11fe05 | -5.4736 | -43.2412 | 2024-11-23 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 8e261fec-6a2e-3b4e-9017-b3bfe507f3b1 | -1.1103 | -53.3953 | 2024-11-23 14:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 554e06a8-d3fc-3195-b1a6-eba06f869017 | -1.4408 | -53.3917 | 2024-11-23 14:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 8b583525-3135-3bef-8b9d-5330d3d7d503 | -1.5352 | -51.9436 | 2024-11-23 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 8feedeae-a214-3ac0-9902-3adc6241bb5f | -1.5351 | -51.9642 | 2024-11-23 14:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7002fa89-3289-398a-b960-cfaa542061ee | -1.7892 | -53.6293 | 2024-11-23 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |


