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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29971495-652c-352d-88a2-40faa088f21f | -11.7172 | -54.4835 | 2026-06-15 16:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a7797f1b-a5f6-3b01-a7be-6f627c9354f3 | -9.2631 | -50.1457 | 2026-06-15 16:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ed6363c2-0472-3a77-9c56-03cb133ce18c | -9.2634 | -50.1243 | 2026-06-15 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 15d8c3d2-fa51-353b-b978-edea3ffec2d3 | -9.2631 | -50.1457 | 2026-06-15 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| f9bc27f3-6b62-3df2-a37a-2dea70712a73 | -8.9641 | -46.934 | 2026-06-15 16:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 7f472651-f279-3937-932f-d04041d6422e | -10.1495 | -56.5915 | 2026-06-15 16:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| c3be2712-e626-3a01-ab28-170c028016c8 | -6.194 | -48.5033 | 2026-06-15 16:40:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b7b19992-4a95-3806-8463-dd4cbe5601c9 | -11.7172 | -54.4835 | 2026-06-15 16:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| e65dbb80-f3ce-32f7-9e4d-c4b29857b76b | -11.717 | -54.5039 | 2026-06-15 16:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 76134127-f079-36bf-86b7-c27628c09dcb | -5.7941 | -45.104 | 2026-06-15 16:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| d1bd97f6-e00c-3d8e-8a82-320e2d450298 | -11.717 | -54.5039 | 2026-06-15 16:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| cb8381e9-a544-3303-96d6-4924512cc5cc | -5.8128 | -45.1026 | 2026-06-15 16:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 68075429-d1f5-36d3-9d49-a6257e6b1c99 | -9.2631 | -50.1457 | 2026-06-15 16:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 5493f509-a1cc-3a28-a093-e94c65fe8e6d | -9.2258 | -48.5782 | 2026-06-15 16:50:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| fee650f9-ea29-3bdf-956f-25c3cbb41783 | -8.9641 | -46.934 | 2026-06-15 16:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| c471de4d-d569-3b3f-ad48-e70abb5ecfc0 | -11.7172 | -54.4835 | 2026-06-15 16:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| b695cae2-a538-3e41-a6a9-fbdba7310ddc | -9.2631 | -50.1457 | 2026-06-15 17:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c4b67f52-647a-3d30-9900-04749a1457a3 | -10.085 | -52.1775 | 2026-06-15 17:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 156c2bac-643e-3a83-9cde-8d9ffa64d93d | -11.717 | -54.5039 | 2026-06-15 17:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 9f96732a-1c35-3b60-a372-4d764cd50fb2 | -11.7172 | -54.4835 | 2026-06-15 17:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 46a75312-d6a1-3556-b075-6448d63804a6 | -8.9641 | -46.934 | 2026-06-15 17:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| bab03089-9024-3e6c-b8a7-853951c2b74e | -11.717 | -54.5039 | 2026-06-15 17:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| ed0eb1df-fb3c-36a8-a408-78a77c31393b | -11.7172 | -54.4835 | 2026-06-15 17:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 0d0239e8-de0d-3881-8ee2-ce6f345d531c | -8.9641 | -46.934 | 2026-06-15 17:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 2dd83e97-8d1e-3064-80f1-3abd83b2b202 | -6.1568 | -48.5057 | 2026-06-15 17:20:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| fb324499-7d17-31ef-8629-d6704e2352dc | -12.0668 | -47.5421 | 2026-06-15 17:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| edf4e6f8-3469-3a0b-9cc6-68ab25bd0215 | -6.1569 | -48.4841 | 2026-06-15 17:20:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| ff1fc758-f565-3a48-a42e-78601c50e9d0 | -5.8128 | -45.1026 | 2026-06-15 17:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| a86da622-6351-3c63-8d24-7122df2dea03 | -11.7172 | -54.4835 | 2026-06-15 17:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 946bf7e7-87ab-3169-9505-95c0985002d4 | -8.9641 | -46.934 | 2026-06-15 17:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 31612069-8f63-3252-904f-d1c5e4ee190e | -12.0668 | -47.5421 | 2026-06-15 17:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 4c61d4c3-7959-380d-a94b-6f89c9bd46f9 | -12.0668 | -47.5421 | 2026-06-15 17:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 03f99ba6-fba6-32fa-b7a0-e3dca4302859 | -11.717 | -54.5039 | 2026-06-15 17:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 2c4a8422-7279-33ef-acd7-1af26b415a3b | -11.7172 | -54.4835 | 2026-06-15 17:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 841b6e36-b69b-3adc-82d1-5ed782252365 | -11.195 | -49.6895 | 2026-06-15 17:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 79acc1c8-dab6-3e1c-9309-4974aa594d46 | -5.813 | -45.0799 | 2026-06-15 17:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 194.9 |


