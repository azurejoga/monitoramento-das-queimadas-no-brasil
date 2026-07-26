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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 604a3103-910b-3bb3-9fb2-6b965e5c706a | -11.852 | -50.2377 | 2026-07-26 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| c3f1dc04-589d-31b7-85f3-9fa94fe05e8f | -11.4753 | -47.5314 | 2026-07-26 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 4ef08939-19a1-379b-b0cb-e5679905aa2f | -12.6679 | -48.2148 | 2026-07-26 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 86f11611-a144-3d11-bbc6-8abc520178f6 | -11.852 | -50.2377 | 2026-07-26 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b55cba36-b813-3626-a0c2-76103edc07fa | -11.4753 | -47.5314 | 2026-07-26 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| fbba9739-9753-39b8-b623-b5fd3d03355f | -11.4375 | -47.514 | 2026-07-26 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 6531b11b-55b8-36d0-a458-cffd212bd687 | -11.8523 | -50.2161 | 2026-07-26 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 78ed00ab-3a33-3f8b-9097-9fb44dd3cb6f | -11.4375 | -47.514 | 2026-07-26 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a7adaf17-809e-3c1b-9614-a5520e4c34a3 | -11.2213 | -50.5023 | 2026-07-26 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 71a6ecd3-d5b6-3ff5-8167-e8a03f29d98c | -11.852 | -50.2377 | 2026-07-26 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| b7c372fc-1632-3be2-a881-6f753c0cd6be | -12.6679 | -48.2148 | 2026-07-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 4acd1d56-f4a6-34b0-a007-3fcffcc8c889 | -11.4375 | -47.514 | 2026-07-26 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 717bfbad-e946-3acb-9241-f4f22ab6e572 | -11.852 | -50.2377 | 2026-07-26 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b05942b3-0d2c-34b7-a4c6-e615ed251ef5 | -11.8523 | -50.2161 | 2026-07-26 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| ebc7e23a-100c-3443-a43f-d74db0f43da5 | -11.2213 | -50.5023 | 2026-07-26 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| d2c3955f-a70e-3c6b-9b52-1c4e71a4956a | -12.6679 | -48.2148 | 2026-07-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 34aa366c-45fd-31d3-953e-55bd47eef2f5 | -11.2213 | -50.5023 | 2026-07-26 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 53c8442c-484f-3c60-b267-e50c41c5194a | -11.4375 | -47.514 | 2026-07-26 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 6e2e08c5-f928-30ed-a2c2-ae543b5aee8c | -11.8714 | -50.2139 | 2026-07-26 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| c648d331-7343-32c2-aeac-428b34b2fc5b | -11.8523 | -50.2161 | 2026-07-26 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 28998cc4-579f-30c1-9a0d-f32321515f36 | -12.6679 | -48.2148 | 2026-07-26 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 898394b7-88e6-3c70-82d2-f7c822f0e291 | -11.852 | -50.2377 | 2026-07-26 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 58dd0696-bd38-3c85-ad91-f1fdcee61115 | -11.4753 | -47.5314 | 2026-07-26 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |


