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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88b97028-ecd5-3c17-8938-fe9dcffc47d4 | -10.80388 | -44.5976 | 2024-12-08 12:42:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d69e9d95-d427-3ebe-8c56-0a882fd84b2c | -18.54519 | -49.26618 | 2024-12-08 12:44:00 | TERRA_M-T | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| bc3551ac-0f18-3697-825c-27d396bdccb2 | -7.983 | -50.699 | 2024-12-08 13:30:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 2b99b864-b738-3f9b-9452-2749d6577856 | -7.983 | -50.699 | 2024-12-08 13:40:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| c6cbe20f-92b5-3303-9b5e-3294d506e51c | -10.6398 | -47.4577 | 2024-12-08 13:50:00 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| b88c62bb-0df2-3abc-9651-f5c97b6dc9c8 | -10.0626 | -44.2158 | 2024-12-08 13:50:00 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| d7edb6d7-8ab9-3c48-9295-2f967bf19da4 | -12.6938 | -46.7576 | 2024-12-08 14:00:00 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| c503ce6d-8c7f-302d-b6b8-1534f112616c | -15.774 | -41.2669 | 2024-12-08 14:00:00 | GOES-16 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.7 |
| 06e47926-464e-3ae9-b9f0-bef3613922f8 | -10.6398 | -47.4577 | 2024-12-08 14:00:00 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 75b396e8-c3cd-33f1-9146-6c4eeeb2c58a | -7.5953 | -46.6205 | 2024-12-08 14:00:00 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 6fb38b92-e097-36d7-af7d-068188151c9c | -12.6938 | -46.7576 | 2024-12-08 14:10:00 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 394438a9-e3dd-3195-83d4-8f824879c226 | -15.774 | -41.2669 | 2024-12-08 14:10:00 | GOES-16 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.1 |
| f486b682-c2d4-32ca-92ec-4839e61f69f5 | -7.5953 | -46.6205 | 2024-12-08 14:10:00 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| e723616b-db28-3b49-bf30-81f4d4faaf66 | -12.6938 | -46.7576 | 2024-12-08 14:20:00 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7e7505c8-c0f5-380c-8d46-218197597845 | -15.774 | -41.2669 | 2024-12-08 14:20:00 | GOES-16 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| b6a466ad-1733-3c59-a403-10131d543a04 | 3.6575 | -60.774 | 2024-12-08 14:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 980d7bb6-fa27-3337-be76-fd71bee09872 | -12.6938 | -46.7576 | 2024-12-08 14:30:00 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| a4001018-573d-321f-8559-4770046e0d9a | -15.774 | -41.2669 | 2024-12-08 14:30:00 | GOES-16 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.0 |
| c1fe2b03-0408-31ed-a0aa-7ab072377b1c | -15.774 | -41.2669 | 2024-12-08 14:40:00 | GOES-16 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.3 |
| 6fa56022-9229-3124-8439-878255c85cf3 | -12.6938 | -46.7576 | 2024-12-08 14:40:00 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |


