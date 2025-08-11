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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b7315b1-088c-32eb-9eae-c14f4a67c814 | -8.9953 | -47.4403 | 2025-08-11 14:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 69fcfa72-db07-3afb-ad23-22826c4255a9 | -7.4561 | -43.9786 | 2025-08-11 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e33fe2ca-a53f-31b0-b0c1-be6f5634685c | -11.7558 | -51.6118 | 2025-08-11 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 197.8 |
| a854409d-5a12-3bfe-a071-ce48ba00eb3f | -7.0614 | -59.1972 | 2025-08-11 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 72cde6dc-d193-3142-9427-5fcc98c29669 | -3.1861 | -48.8035 | 2025-08-11 14:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 5f4ec6ec-70c1-3d3e-932e-06eccc1a3c47 | -7.0797 | -59.2157 | 2025-08-11 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 22b1bcde-2f32-369b-8745-3cf6ad9864b5 | -15.4216 | -53.9073 | 2025-08-11 14:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| b66d68d3-6a8c-3f0e-b7ee-dd4fd4bc7827 | -7.0615 | -59.1779 | 2025-08-11 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| c6925974-bd13-3847-9856-9c0a05cb7e20 | -8.5788 | -54.7162 | 2025-08-11 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 0a5e2974-7121-3beb-b25a-a6b43fcb3d55 | -9.2042 | -44.5305 | 2025-08-11 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| f9d01ec0-7c49-33e0-b0ac-311c50297a97 | -8.5604 | -54.6973 | 2025-08-11 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 8f19b3f4-4277-3ee0-9d0c-f19e4119cefd | -7.2245 | -46.2291 | 2025-08-11 14:40:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| e6ed4597-862b-3f06-99ec-f8deac9358bf | -7.0613 | -59.2165 | 2025-08-11 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 24540c22-e5cf-3aff-b71a-9c9834186b52 | -15.4407 | -53.9258 | 2025-08-11 14:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 544f9dde-2537-3e3c-99a9-ad8995eb4224 | -15.441 | -53.9048 | 2025-08-11 14:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 782ff5d3-ece5-3147-af1c-7f5542fa9e05 | -7.08 | -59.1771 | 2025-08-11 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 0ed323b7-6ddb-3fab-bac5-074f76898853 | -8.5605 | -54.6771 | 2025-08-11 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a0dd91e8-0978-32d8-8744-6e66b5ad43a6 | -9.2232 | -44.5283 | 2025-08-11 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 22ac4185-1559-3233-a952-3411624752fc | -8.579 | -54.696 | 2025-08-11 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 27daffd1-bfd4-3ca9-b7c7-157db12f39e4 | -8.5792 | -54.6758 | 2025-08-11 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f494020c-20ba-3987-afa2-afc348d88e80 | -7.0799 | -59.1964 | 2025-08-11 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 7dc7e0fb-2775-31d6-90bc-2af350b3e807 | -8.995 | -47.4624 | 2025-08-11 14:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |


