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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0e8e23f-3f39-3930-a658-ca1d5fbfb647 | -10.7409 | -54.0196 | 2026-08-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 693411ad-1cc3-374c-9af9-fc0bcf2280db | -6.6411 | -58.4793 | 2026-08-26 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| dae6a3ab-e26a-3c1c-b149-f9cb9ff5f5e6 | -8.7582 | -49.978 | 2026-08-26 15:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 308.5 |
| df1dfe6f-327e-338c-8dc2-002ba6d381c2 | -6.235 | -55.4715 | 2026-08-26 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 9adb3b67-9120-3a3e-8ac5-11e980f35a0f | -3.2179 | -61.2174 | 2026-08-26 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c47a069c-b540-3214-ade9-d94a3eb8fc6f | -6.7815 | -59.748 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c8abc00f-865b-3d78-a8f3-a0f8d0c414a8 | -6.3733 | -45.1963 | 2026-08-26 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 5d6ef524-0d51-3fc0-9615-4159d54a377d | -6.3545 | -45.1978 | 2026-08-26 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 8e103aed-092d-3e0a-8d54-1a08ce6b17db | -8.9418 | -45.748 | 2026-08-26 15:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 85c1fb10-3d96-3e6f-a89f-a69263ed2369 | -3.1267 | -61.1811 | 2026-08-26 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 6a65f2af-272b-3c5f-854b-84ed45aa8564 | -6.7295 | -59.153 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 37c77ef8-7d08-3cac-84de-5c623091e748 | -6.2348 | -55.4915 | 2026-08-26 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| a1407d73-e962-3243-9b27-6a2c00445837 | -13.2095 | -51.3356 | 2026-08-26 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 4621ea5a-08d9-3771-bb03-4ab87c187f47 | -9.1899 | -49.9818 | 2026-08-26 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 51c052b5-b5f3-3bb0-a1b1-994c7b013843 | -6.5139 | -55.2187 | 2026-08-26 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| c22fbd32-e3df-3c7d-8925-1f561ee8ff09 | -8.7772 | -49.955 | 2026-08-26 15:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| e8343d70-5ae3-3995-9e4b-3c65f3b944cb | -6.8192 | -59.5927 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| cb93aaa3-6d7b-3346-ae08-56790c3143d1 | -11.7357 | -54.5227 | 2026-08-26 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 5e4f82ef-1d77-349e-ba3d-d65cb80ca323 | -10.7793 | -50.975 | 2026-08-26 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| bf889356-c0ef-3c9c-98c8-bcc1c7e4875a | -8.073 | -47.5287 | 2026-08-26 15:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 97ac80a5-26bb-38ca-a962-86cfc968b377 | -13.2092 | -51.3569 | 2026-08-26 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |


