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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ce77675-c1b6-38e7-a371-a2ccfc2cb3e0 | 1.95091 | -60.83834 | 2025-03-14 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 172066f0-346e-3fc0-8654-90b2faa3034f | -15.58441 | -56.01472 | 2025-03-14 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f0ccd62-5f2a-3602-8257-7c987aac72f8 | -15.58063 | -56.01546 | 2025-03-14 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46dd78c6-eb1f-3e73-8a56-2d2c40aa46c3 | -12.49477 | -53.33332 | 2025-03-14 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ceb7f27-2df6-3908-91a7-d444a6b042e5 | -15.26222 | -51.47336 | 2025-03-14 05:31:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 638fc7e6-dd58-3ed0-ad74-c4630689c7e2 | -6.22421 | -48.05057 | 2025-03-14 06:01:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 014ca602-b1f6-3cf7-8f1f-4f6009dcd7e8 | -14.4604 | -45.3922 | 2025-03-14 10:10:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 908d9698-1215-355f-9536-41539dcca91e | -14.4604 | -45.3922 | 2025-03-14 10:20:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| ecd62fee-885d-35ef-862c-1c13b3ce7ea5 | -14.4604 | -45.3922 | 2025-03-14 10:30:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| a6bbd27a-2866-3bd6-99a5-8fd44e50e46e | -14.4604 | -45.3922 | 2025-03-14 11:20:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| eef7a7c9-3223-3373-a2e8-c1be0a7b2f9a | -14.4604 | -45.3922 | 2025-03-14 11:40:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| d9781d58-304d-366b-a4ad-6d82a1093fcc | -14.4604 | -45.3922 | 2025-03-14 11:50:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| bb994785-f6eb-36f0-bf5f-8d41ba84f9e0 | -12.8833 | -44.8716 | 2025-03-14 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 243d639b-77cc-3d54-8415-e23c5393246b | -12.547 | -45.342 | 2025-03-14 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 1bfd08de-79c6-3eac-b69e-3c49e1401f9e | -12.547 | -45.342 | 2025-03-14 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 89a69901-2df1-3194-86e5-69957e08029a | -12.8833 | -44.8716 | 2025-03-14 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e2f74c52-d4d1-3f6e-8b78-b4fab0c30f32 | -12.547 | -45.342 | 2025-03-14 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 6e084af2-a459-33d0-9984-d7c1f7e232de | -7.8302 | -44.196 | 2025-03-14 13:50:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 19077209-3099-30ca-aa7d-ddba3b42f7ef | -12.547 | -45.342 | 2025-03-14 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 4f288a1e-7c46-35da-9d0f-ae6172dea4ab | -12.8833 | -44.8716 | 2025-03-14 14:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 8d932775-df00-350f-b4d0-390859a4e0df | -12.547 | -45.342 | 2025-03-14 14:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| a1419fca-4a1e-3a11-8c18-09ddd8291975 | -12.547 | -45.342 | 2025-03-14 14:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 512ff580-eea5-37aa-872b-8bc44ce26ae5 | -12.8833 | -44.8716 | 2025-03-14 14:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 6227590f-e9f2-30c8-906b-e975185fe77c | -7.8302 | -44.196 | 2025-03-14 14:10:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 62d92d43-f1f1-32a1-aa99-c1124f231dfd | -10.6689 | -44.3904 | 2025-03-14 14:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2d56fdcb-b752-3d04-85c1-1771b08ffc3f | -10.6689 | -44.3904 | 2025-03-14 14:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 306fcea7-0d07-305e-a7e2-61e4c03bce4d | -12.8833 | -44.8716 | 2025-03-14 14:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 4a8587f8-7afe-3919-816b-51d496fd504d | -10.6689 | -44.3904 | 2025-03-14 14:30:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |


