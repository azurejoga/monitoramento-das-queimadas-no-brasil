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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 888bd474-9df8-36be-83b7-691928328d07 | -3.4249 | -49.1796 | 2025-11-04 14:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| e6bfffca-ad22-3c79-af34-f74c8fd653ca | -1.1899 | -49.1904 | 2025-11-04 14:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 6137c131-ef6f-3032-ac98-b0c947f60226 | -4.0989 | -44.6866 | 2025-11-04 14:40:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0e146521-6eab-3f8b-bb7b-93238864f4d3 | -4.0196 | -45.4595 | 2025-11-04 14:40:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 99864778-92bc-3654-87f4-4b590df65de6 | -1.1899 | -49.1691 | 2025-11-04 14:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 7c49500e-5a83-368a-83b9-cbd5ff7f7ce1 | -1.2268 | -49.1899 | 2025-11-04 14:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| fff310db-1535-3e0d-99e1-441b36c2e340 | -2.482 | -49.2297 | 2025-11-04 14:40:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 62e9d07e-2292-35c6-880c-4decbaf0c9ae | 1.5099 | -56.0426 | 2025-11-04 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |


