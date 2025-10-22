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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 357edaa4-641c-3fe6-8b19-fe11290d5479 | -17.335 | -55.0366 | 2025-10-22 14:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 116.4 |
| 4c1ecbf3-3d37-3ae2-899e-7e3392bc45d7 | -17.335 | -55.0366 | 2025-10-22 14:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 18d43983-5ad2-3611-8bed-0f9f3d681875 | -17.3547 | -55.0339 | 2025-10-22 14:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 138.9 |
| e7167a44-4741-3690-bc36-51abe9202a12 | -22.3753 | -54.6198 | 2025-10-22 14:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 91.1 |
| 7756873a-edd1-3b41-b896-5fb6cf967722 | -17.6367 | -46.6098 | 2025-10-22 14:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 166.0 |
| f90964d5-8bea-355a-b58c-d1c37cd5f0f9 | -12.0786 | -50.3611 | 2025-10-22 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| a4cde144-bb62-3eac-8a39-a1022a1e45e2 | 1.712 | -55.6854 | 2025-10-22 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| f79d4c20-02d5-3bfa-ad6e-66217855b824 | -10.0161 | -67.8652 | 2025-10-22 14:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 8a992739-5767-3a6b-8e0e-6837e6e91487 | -17.335 | -55.0366 | 2025-10-22 14:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 122.0 |
| 89835dd2-7af5-3f44-ac41-110556492cc7 | 1.712 | -55.6854 | 2025-10-22 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| d084b5b4-3d6b-3488-b29d-6947347d697c | -11.9731 | -49.7922 | 2025-10-22 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 1e18ec91-4663-3783-97e5-af119149332b | 0.9108 | -51.1457 | 2025-10-22 14:40:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 03347eb9-da05-3567-9550-c22e066244d0 | -18.1455 | -52.9639 | 2025-10-22 14:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 9eacd89c-a84f-34be-a688-d1adf27825f9 | -17.3547 | -55.0339 | 2025-10-22 14:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 201.2 |
| 9c06b434-e8c1-3ba1-912f-7a6b44886137 | -17.335 | -55.0366 | 2025-10-22 14:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 111.4 |


