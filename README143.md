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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 615f23cc-a9c4-3175-a9f1-56b512c875a7 | -3.6076 | -59.0769 | 2026-09-20 16:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| f079f218-f028-31bf-9f65-e8a337e1df53 | -10.2787 | -50.2605 | 2026-09-20 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| a6b40486-60b1-3adc-90cc-c6786f5c840a | -10.279 | -50.2391 | 2026-09-20 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 6800994f-285e-3048-852d-d4efdcd1e9f5 | -2.9143 | -58.3401 | 2026-09-20 16:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 166.4 |
| eb284257-969b-38ba-a71a-e8c298a8efe4 | -5.3331 | -49.221 | 2026-09-20 16:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 34ee03bc-64ba-3ed6-9315-e6429639452f | -6.6194 | -59.0609 | 2026-09-20 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 5ac0ee23-410c-3f65-a929-f4a8362e226e | -10.6516 | -50.6271 | 2026-09-20 16:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 0921f802-df68-3a08-b772-66b9223c6e96 | -10.3357 | -50.2333 | 2026-09-20 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 01b98a5c-8fba-380c-b54d-567ebef70125 | -1.3741 | -49.3579 | 2026-09-20 16:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 6e91eddb-07dd-344a-bf94-093757df57b6 | -10.8093 | -50.1621 | 2026-09-20 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 3a1416bf-1ad1-3287-9897-326edb6cd59c | -10.3171 | -50.2138 | 2026-09-20 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 156.7 |
| d5a2b2bb-f465-3566-8f72-f656082712d8 | -10.2793 | -50.2177 | 2026-09-20 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ab8e477f-2198-3f97-809f-e758f58e33d5 | -6.0927 | -57.6457 | 2026-09-20 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 22a84e06-b5f1-376c-aafe-54cffd0a0c68 | -6.1112 | -57.645 | 2026-09-20 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| f093ae15-7fba-346b-b63d-76ba3719a97d | -3.0352 | -61.277 | 2026-09-20 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d4f468ce-f71f-3036-9bc4-4a2fafcacbec | -3.1079 | -61.408 | 2026-09-20 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b336d19a-ba40-37fb-94eb-cdbc6ae18ed2 | -10.809 | -50.1836 | 2026-09-20 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |


