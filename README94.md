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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1786f145-b5ad-3056-9bcd-da8ef1dacc90 | -9.6865 | -47.9409 | 2025-08-31 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| d1203a93-bc33-39d0-901c-63fac8d34eb8 | -7.4178 | -47.4537 | 2025-08-31 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 7e8de518-222d-3a9a-8927-79bbd9135800 | -11.8334 | -51.4975 | 2025-08-31 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| dd158422-e91a-3045-8434-3e1cb8e3c1dc | -6.5021 | -43.5553 | 2025-08-31 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 9b4e2b4f-12a3-3ed7-b1f8-0baa77bee8d5 | -13.3812 | -47.0377 | 2025-08-31 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 3a288cbc-7bc1-3110-b5bc-548dbabab1f2 | -14.5448 | -51.9943 | 2025-08-31 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 8d58f182-f7e0-3a08-a5d7-86ef1f883baf | -9.2639 | -47.0804 | 2025-08-31 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 6d435410-07f7-30ec-ba62-784269100ebb | -13.4006 | -47.0347 | 2025-08-31 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 110.5 |
| e0a1a4d7-d061-35d5-aa21-243615e75e0d | -6.2959 | -43.5263 | 2025-08-31 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 6de56fcc-6279-3498-b112-8e349f75add3 | -14.5646 | -51.9703 | 2025-08-31 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 777f97df-f5bf-35a5-8d2c-7b94958441c5 | -6.949 | -45.6916 | 2025-08-31 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 7442c6d4-aca7-3c12-871e-8b990a1d0fd5 | -8.8939 | -45.094 | 2025-08-31 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 63828678-0d53-3a85-9d8f-2c758e595467 | -6.9678 | -45.69 | 2025-08-31 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |


