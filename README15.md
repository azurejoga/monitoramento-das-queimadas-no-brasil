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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04c9849a-e95f-3f79-b688-2c7e26219de9 | -11.7513 | -54.7868 | 2026-06-06 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 37a55044-d306-35df-9ce6-93f97a65ca3d | -8.9241 | -45.6594 | 2026-06-06 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 09b29b9f-6b03-37ff-9ae4-69573062f9da | -11.7323 | -54.7885 | 2026-06-06 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| dcf16ceb-9857-3ff6-b5f3-92cdd09e0094 | -8.9427 | -45.68 | 2026-06-06 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.8 |
| be70f6cd-1b98-396f-a276-38af5a9488e2 | -14.2118 | -57.4299 | 2026-06-06 14:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 83d96654-5c44-32a1-b7e6-fb98a5cbf0a8 | -14.6368 | -58.6933 | 2026-06-06 14:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 4e9f6a53-5436-3277-9d79-953ea0291e06 | -11.7513 | -54.7868 | 2026-06-06 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ed94953f-58d9-39fc-bd73-016fe80b1a39 | -14.1926 | -57.4318 | 2026-06-06 14:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| bfc9b6a6-698c-3fb7-ba7e-e82bd4c49e07 | -10.8573 | -53.7425 | 2026-06-06 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| b4192937-ed59-3e3f-857b-738713308423 | -8.9241 | -45.6594 | 2026-06-06 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 1ef999af-6bd4-3bed-9df0-629fa8b52f3c | -8.9433 | -45.6346 | 2026-06-06 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| a215211e-2804-3b5d-b200-9e00f70bb010 | -10.8573 | -53.7425 | 2026-06-06 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| ddfa65c7-a828-3e2b-aab0-057c2ba2cfab | -14.459 | -54.8972 | 2026-06-06 14:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 75914bae-1731-3d58-865a-3604a10c1d7a | -8.9433 | -45.6346 | 2026-06-06 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 8a989b32-7215-33a6-b6ab-88414539e00b | -14.2118 | -57.4299 | 2026-06-06 14:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 6516eb3a-b022-3ea0-a81b-af10d9a63a6e | -11.7513 | -54.7868 | 2026-06-06 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 477947c6-13fd-39a0-8e6f-03232aeec8a8 | -8.9241 | -45.6594 | 2026-06-06 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 39147161-b26e-339b-b245-7c41ba54508d | -11.7323 | -54.7885 | 2026-06-06 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |


