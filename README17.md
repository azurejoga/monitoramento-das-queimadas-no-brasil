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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a856c371-2bcd-389a-9431-2f7aff0a4fcd | -10.7101 | -46.5782 | 2026-07-18 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 42967d83-249b-365a-9abc-59caa1cc1f3a | -10.4718 | -42.4839 | 2026-07-18 13:20:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 117.3 |
| b1a8bdb7-26ef-3cc9-8e0d-d5d6ee8e3c04 | -10.7101 | -46.5782 | 2026-07-18 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 638a604c-9051-38f8-b56d-0229b22be1de | -9.883 | -53.3958 | 2026-07-18 13:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 35d949ee-4d87-3afc-b282-376744c4044c | -10.4718 | -42.4839 | 2026-07-18 13:30:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 138.1 |
| c8a836d6-3b65-3f52-9cad-b456859ce6af | -9.9018 | -53.3942 | 2026-07-18 13:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 08c83479-cf59-3bf3-a4ee-4a4c3dc46062 | -10.7101 | -46.5782 | 2026-07-18 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ece92204-8bea-3d83-93c7-d727ca37af33 | -9.9018 | -53.3942 | 2026-07-18 13:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 9b4070e8-d974-3577-b1a2-1dd5c28b1069 | -10.7101 | -46.5782 | 2026-07-18 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 51bad659-d4f5-349b-91bf-7d0409110dee | -9.9018 | -53.3942 | 2026-07-18 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 5920d85d-893c-3642-95bf-81183c30586a | -9.883 | -53.3958 | 2026-07-18 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| fb8b60a7-9f01-3b56-a639-7c91d7dd303e | -9.9018 | -53.3942 | 2026-07-18 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 165.4 |
| 9a15ed75-b318-3910-9eeb-db9568980626 | -10.7101 | -46.5782 | 2026-07-18 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 5fee2a87-746e-359b-91f3-92e082a41bfc | -9.9018 | -53.3942 | 2026-07-18 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 3232e685-0f10-3355-82ec-92f8ca3c274b | -10.7101 | -46.5782 | 2026-07-18 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 3997b979-863d-32d0-8773-286aa4465ae8 | -14.3103 | -53.3342 | 2026-07-18 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 5476b097-787a-353e-b667-00bc93907050 | -10.7101 | -46.5782 | 2026-07-18 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 255ec858-3975-32dc-9614-b9d0fd75c619 | -11.8076 | -45.9334 | 2026-07-18 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| f7b9f9d4-2867-3a51-8d0a-75e09e17553a | -9.883 | -53.3958 | 2026-07-18 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 66fa65e6-7bcb-390a-8772-2729827aeb4d | -9.9018 | -53.3942 | 2026-07-18 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| d7413fc7-7728-32c3-a402-7bda9f96f3cc | -4.6689 | -43.226 | 2026-07-18 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 15af7ac1-741a-3da7-a75d-7da6146471b4 | -4.6689 | -43.226 | 2026-07-18 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ac5eafc5-ee00-31f1-a025-68e6e3c14820 | -10.7101 | -46.5782 | 2026-07-18 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |


