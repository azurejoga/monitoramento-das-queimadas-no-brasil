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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e47d4928-716d-30b2-ad46-888abf82b191 | -8.3299 | -44.9261 | 2025-07-24 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| ad9303c4-c59c-3094-a826-d4dfd502cbfb | -12.6681 | -45.0455 | 2025-07-24 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 7eec87f1-e203-3713-a3ec-74559b0cfa6b | -8.569 | -63.8967 | 2025-07-24 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 7b8213ab-dbf5-338f-b71f-17a7cc0546e0 | -12.6488 | -45.0486 | 2025-07-24 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| efbc8f90-2af2-37c7-869e-224bb3b49a2b | -7.956 | -46.2752 | 2025-07-24 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| d86f043a-ad6f-342c-aaa8-77de41caa30f | -12.6685 | -45.0223 | 2025-07-24 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| c152d7bb-42f9-3e18-af80-37e5f1d64ac4 | -7.9557 | -46.2976 | 2025-07-24 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 7a5d788c-a0e8-3592-9bb8-f42ee4dfd933 | -8.3299 | -44.9261 | 2025-07-24 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 7ebccc15-3038-3dba-9757-33bd8d080da8 | -8.3299 | -44.9261 | 2025-07-24 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 30f0259b-0e24-3ea2-b4a8-52bd7e193964 | -12.6681 | -45.0455 | 2025-07-24 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| f4355212-b945-3eda-b3a2-06e5d957754c | -12.6488 | -45.0486 | 2025-07-24 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 96ac88fe-94c2-3e82-b9ca-aaaae159c983 | -7.9557 | -46.2976 | 2025-07-24 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 6827f92d-9800-3442-a2f9-b153c12d3926 | -8.569 | -63.8967 | 2025-07-24 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 90d7653b-dbd9-32c5-ae47-3b5dabe7f5ef | -12.6685 | -45.0223 | 2025-07-24 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| ef7c3fb7-237c-3026-8c45-aac7175e73a0 | -7.6572 | -44.4897 | 2025-07-24 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 314bcf0a-ebdb-36b8-b354-b6a39bad2da4 | -12.6488 | -45.0486 | 2025-07-24 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 54fed84e-55a0-3b70-b0a6-a1108cb8a322 | -15.6132 | -44.5394 | 2025-07-24 14:40:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 779d7c1a-109a-3bd2-b994-57a1402fb824 | -8.569 | -63.8967 | 2025-07-24 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 9cded9c5-4c04-327f-8c48-c252fbd786d9 | -7.6408 | -44.2841 | 2025-07-24 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3d367b8b-340c-39d8-985c-d3054706e5d4 | -12.6685 | -45.0223 | 2025-07-24 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 669efd4b-3c11-3259-821f-fd3b728c92a8 | -6.8825 | -43.1241 | 2025-07-24 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| d34ced89-2531-39ca-9576-356fbefe4b58 | -12.6681 | -45.0455 | 2025-07-24 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |


