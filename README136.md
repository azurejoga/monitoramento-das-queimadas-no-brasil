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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d69d3c9-b4ed-3ad8-8411-914cccef1c1a | -9.20069 | -36.50583 | 2024-11-30 12:16:00 | TERRA_M-T | LAGOA DO OURO | PERNAMBUCO | Brasil | 2608602 | 26 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 84e72e6e-bc2e-38d5-b859-2c1aa93b15e6 | -8.44372 | -45.1157 | 2024-11-30 12:16:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| d4347343-9a56-390d-8e97-d9c7eb36022e | -8.27247 | -36.93018 | 2024-11-30 12:16:00 | TERRA_M-T | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 18.6 |
| d9fa3138-fc33-38d5-b22b-bde75f19ac30 | -6.91225 | -43.54392 | 2024-11-30 12:16:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 433afe1f-25f6-3d3e-9730-f684267ea73a | -17.03423 | -40.62031 | 2024-11-30 12:18:00 | TERRA_M-T | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 034125d9-e0cb-3a3f-94af-06bd7889ae87 | -15.08567 | -43.85037 | 2024-11-30 12:18:00 | TERRA_M-T | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6389b7b3-0a9d-37ab-9fc8-b61080c8d5db | -17.77794 | -42.53261 | 2024-11-30 12:18:00 | TERRA_M-T | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 4f2eaa69-cf85-303c-8a73-5edf46eb8ecb | -18.69951 | -42.46389 | 2024-11-30 12:18:00 | TERRA_M-T | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 9659c7c1-ea37-3e82-b9a2-d1e321cb0e5e | -20.27157 | -41.78944 | 2024-11-30 12:18:00 | TERRA_M-T | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 697c0284-b2a0-3dd0-9731-8c21f79f791e | -18.90369 | -41.15348 | 2024-11-30 12:18:00 | TERRA_M-T | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 989d4e26-cf19-3ecf-a2fe-f8841e1ec9d0 | -18.05477 | -39.81587 | 2024-11-30 12:18:00 | TERRA_M-T | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 752639fe-196a-30c0-8a98-7da6878f3f85 | -16.99978 | -40.69502 | 2024-11-30 12:18:00 | TERRA_M-T | MACHACALIS | MINAS GERAIS | Brasil | 3138906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 447f549b-df21-3f44-bb49-62ffcb6c9f21 | -18.70082 | -42.4544 | 2024-11-30 12:18:00 | TERRA_M-T | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 907d5055-d284-3481-ad29-0d6eb89bd5cb | -16.23995 | -42.83505 | 2024-11-30 12:18:00 | TERRA_M-T | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| befff66d-924c-3d03-b4df-6287e93772eb | -3.92 | -42.39 | 2024-11-30 13:00:00 | MSG-03 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 35da727d-a03b-30c6-ad65-72fbe3bb0bd8 | -3.92 | -42.44 | 2024-11-30 13:00:00 | MSG-03 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5ff16dbd-8e85-3a12-8409-bc8ed644897e | -4.88 | -41.28 | 2024-11-30 14:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08a31cea-ccc3-32f2-a8f4-26e697ae6b20 | -4.88 | -41.32 | 2024-11-30 14:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |


