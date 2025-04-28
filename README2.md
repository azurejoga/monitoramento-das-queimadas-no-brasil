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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46fcb974-7756-36a7-9bd9-0d7109fde0dc | -11.3955 | -52.94377 | 2025-04-28 05:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd4865cc-191b-32ca-a3b4-0b6c1a0c011f | -10.66141 | -51.03316 | 2025-04-28 05:12:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2da5e88a-8017-3166-9d77-92fa98a95e42 | -11.39185 | -52.93928 | 2025-04-28 05:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d1f93c9a-a3d7-357c-8a84-85f948c2ae1d | -10.82141 | -68.96642 | 2025-04-28 05:14:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6c6e058-e561-35e8-b3e6-933478a6688f | -27.68545 | -52.83697 | 2025-04-28 05:18:00 | NPP-375D | RONDA ALTA | RIO GRANDE DO SUL | Brasil | 4316105 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 212a4841-0ef1-3115-b336-f1c733197972 | -27.68022 | -52.83639 | 2025-04-28 05:18:00 | NPP-375D | RONDA ALTA | RIO GRANDE DO SUL | Brasil | 4316105 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f25b2ba2-eb30-3336-9031-f0a502baa2e6 | 4.97441 | -60.53304 | 2025-04-28 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 449ab9bf-62cd-3997-9952-715ecbe00d98 | 2.818 | -61.36006 | 2025-04-28 05:31:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da0fcd8e-5845-3705-b7d3-a381cea66c0d | -6.23352 | -43.37912 | 2025-04-28 05:53:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 29218c0d-121b-3365-963f-e85f8c3553e2 | -6.23165 | -43.37179 | 2025-04-28 05:53:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| db463cc1-c89d-30b8-b664-b284d88c7b97 | -11.39134 | -52.93772 | 2025-04-28 05:55:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |


