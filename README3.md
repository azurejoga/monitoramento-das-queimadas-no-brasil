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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a74211c1-31a4-3914-b68c-0b0b6c9e55a5 | -17.43983 | -43.28415 | 2026-04-26 11:23:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 19572396-8575-39bd-a3c6-a061f1666fb2 | -13.38725 | -45.33395 | 2026-04-26 11:23:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 51e699e8-1c7b-3070-ab99-2b4ad98c71b9 | -18.84118 | -39.90884 | 2026-04-26 11:23:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a747b571-3715-39df-a7ce-8e7fc4197e48 | -20.18574 | -46.91499 | 2026-04-26 11:25:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 452aadf8-21ed-3152-af7b-2b0ed2bc4e9b | -20.18291 | -46.90727 | 2026-04-26 11:25:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 21ac4472-f2c4-3300-997b-47f7d4c88431 | -10.15107 | -52.69765 | 2026-04-26 12:59:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| c5593ee2-bac0-393e-a5c6-f42b5003fd29 | -14.7238 | -53.97943 | 2026-04-26 13:01:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| ecabce4e-339c-3a77-a45e-3cc8f55cec51 | -14.72014 | -53.97257 | 2026-04-26 13:01:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| b0577783-277e-32e6-96a4-3cfb745a5afa | -14.72765 | -53.93966 | 2026-04-26 13:01:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 2b7c4462-1031-399a-8c58-5380df36bce9 | -14.72426 | -53.93276 | 2026-04-26 13:01:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a95e637b-faa8-3450-8b07-30c53107ef7c | -14.724 | -53.9737 | 2026-04-26 14:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 3f327c96-d279-3e55-a74e-afa15127a487 | -14.724 | -53.9737 | 2026-04-26 14:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d340d9ab-c13d-37e3-abe7-8453560e7b2c | -14.724 | -53.9737 | 2026-04-26 14:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |


