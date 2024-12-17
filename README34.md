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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c376b52-e1cd-36b4-9515-68f2f75bc5d6 | -3.6296 | -42.0613 | 2024-12-17 14:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 12c686df-fed9-36b2-b937-bbfc5668d149 | -6.0836 | -44.1454 | 2024-12-17 14:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 6c9a4f69-9a2a-3bbe-8d5d-3fff748212f0 | -3.4915 | -43.3368 | 2024-12-17 14:30:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 4e4b68ca-6d31-3366-8881-b1c6c9caf1ce | -4.9643 | -43.7182 | 2024-12-17 14:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 206.9 |
| e6b94bbd-d0ea-301d-84b3-0971238599dd | -6.9158 | -43.5185 | 2024-12-17 14:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| fdecf181-66af-3d88-b635-ed418cf8873f | -4.8707 | -41.3639 | 2024-12-17 14:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 106.2 |
| 9f67ddfb-d770-35ca-bfdf-ab1b1215afd8 | -10.2638 | -42.3701 | 2024-12-17 14:30:00 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 81.6 |
| e04ce3e2-bedc-3f4c-aca7-84c6ea21d39c | -5.9597 | -43.3673 | 2024-12-17 14:30:00 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 97873358-abf5-35be-b964-ba62dcc16efb | -3.4102 | -44.6055 | 2024-12-17 14:30:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| bc615ba3-fc49-3d31-9ec8-123637b327e6 | -4.3092 | -43.8966 | 2024-12-17 14:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 821fbf29-62f5-3118-a5ab-6e71a9ec3406 | -6.961 | -42.8344 | 2024-12-17 14:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 167.4 |
| 2389f506-43f9-30dd-bf65-40471e293abf | -5.0807 | -38.8064 | 2024-12-17 14:30:00 | GOES-16 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 83.0 |
| ff0ceff8-41f7-307d-b29d-c87f8a7ad73e | -6.0335 | -37.98 | 2024-12-17 14:30:00 | GOES-16 | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 97.0 |


