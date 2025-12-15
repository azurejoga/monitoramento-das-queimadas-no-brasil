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
| e2ecf2f0-7be4-341e-96e8-dcee75a27959 | -6.25535 | -39.90939 | 2025-12-15 11:57:00 | TERRA_M-M | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| a7c00e73-ad49-331a-b072-93fcda23776a | -6.66871 | -39.41009 | 2025-12-15 11:57:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 33df831e-d630-3228-b41b-836cf1a3fef1 | -9.67207 | -43.89149 | 2025-12-15 11:57:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2249b354-9734-37c8-aa4c-d2ee35ab59a9 | -8.46207 | -40.28979 | 2025-12-15 11:57:00 | TERRA_M-M | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 25.4 |
| cd5ad3cd-dd51-3806-8a8c-6914aa46d6d7 | -6.55657 | -41.73564 | 2025-12-15 11:57:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| e87ce3c9-9ab3-3ebe-b9f6-3525c7d6400e | -5.98515 | -38.16148 | 2025-12-15 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO OESTE | RIO GRANDE DO NORTE | Brasil | 2411908 | 24 | 33 | nan | nan | nan | Caatinga | 18.4 |
| bab6e00d-1eff-3b4a-a5e0-3ec09ee9a3af | -8.10507 | -38.8568 | 2025-12-15 11:57:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 04c52389-df3c-34e7-94af-81bd2a567d07 | -8.43906 | -38.93292 | 2025-12-15 11:57:00 | TERRA_M-M | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 9fecaccd-c35c-39c4-8b6a-06441e75a7ec | -15.218 | -43.4358 | 2025-12-15 11:59:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 49.9 |
| 210211df-e617-3296-9062-0a984cb42614 | -15.22593 | -43.4332 | 2025-12-15 11:59:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4080962e-9520-30ae-9755-c5947bb5d66b | -22.87008 | -43.77926 | 2025-12-15 11:59:00 | TERRA_M-M | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 90862832-06d5-3262-8f43-7e6e92221bfd | -5.8781 | -38.3544 | 2025-12-15 12:40:00 | GOES-19 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 9b10c947-3ae6-37e4-bad1-c25fb141d256 | -1.2503 | -46.3055 | 2025-12-15 13:50:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 721b8eb4-980a-31bf-a0de-69723f0d93e5 | -5.0028 | -41.2821 | 2025-12-15 14:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| bbcd6ac9-f84e-3bd1-97b0-34c3be9cdab5 | -5.0028 | -41.2821 | 2025-12-15 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| 6a916606-71ba-3a52-9c76-305723776621 | -5.0028 | -41.2821 | 2025-12-15 14:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |


