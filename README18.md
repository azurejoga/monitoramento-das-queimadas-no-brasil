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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7bdbbb3-a40d-3e5b-98fc-04c46312b8eb | -11.0115 | -55.0561 | 2025-06-15 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 291.2 |
| d257a421-031d-3bce-864f-9d9cadd84bc9 | -9.3972 | -48.4305 | 2025-06-15 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e8bc6448-07fc-300a-8d42-aacc2865e270 | -13.9254 | -54.6063 | 2025-06-15 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 859fdc39-2c8a-3009-98a3-09b24de5591f | -13.9062 | -54.6084 | 2025-06-15 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 240.9 |
| 712d6a6e-305d-3dfb-b6b6-f22d885c07cc | -10.9926 | -55.0577 | 2025-06-15 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 81e39a56-b452-3b15-bb3b-f7472c7ad790 | -11.0113 | -55.0764 | 2025-06-15 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 430.8 |
| 705c4633-7f7f-35b1-ab0b-45c87c95c11f | -13.9251 | -54.627 | 2025-06-15 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 315.3 |
| 3658f8be-5c82-341a-a45e-060bd50cc144 | -10.9924 | -55.078 | 2025-06-15 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 8bcabcc7-2388-3853-bd93-6ba00978c835 | -13.9056 | -54.6498 | 2025-06-15 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 480634a1-df3e-3b0e-8fe4-fc12dba643a5 | -9.4161 | -48.4286 | 2025-06-15 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 0c8f4155-d4a1-3599-aa41-43de04447c8e | -10.9926 | -55.0577 | 2025-06-15 14:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 48fdca84-4f79-3dac-9a04-f8b19f34818f | -10.9924 | -55.078 | 2025-06-15 14:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 2808d5ae-524d-31e7-90f2-46a90f4b1b1a | -11.0115 | -55.0561 | 2025-06-15 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 263.5 |
| 48608e72-65f5-3069-b0d7-cd07bc427115 | -7.2158 | -43.6069 | 2025-06-15 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 82ab39b3-624f-3b24-b751-a5c98e9fc72f | -11.0113 | -55.0764 | 2025-06-15 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 431.3 |
| 04f3749d-9901-3c78-90cb-3a4a1fcbed7d | -11.8079 | -43.779 | 2025-06-15 14:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 7304249e-cf0b-3133-a34f-933b9419d524 | -13.9248 | -54.6477 | 2025-06-15 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 441a93bc-1d2a-3724-97ca-0e44f3519f30 | -11.0115 | -55.0561 | 2025-06-15 14:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 378.2 |
| c8fc9080-5e2b-3056-8962-0d1b067712f9 | -10.8568 | -53.7836 | 2025-06-15 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 24cf0ae3-cfb5-3921-8b6f-497c765fd87e | -9.4161 | -48.4286 | 2025-06-15 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9dcc7771-d4f0-3e48-9879-3aeca2c3c3ac | -9.3972 | -48.4305 | 2025-06-15 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 70414865-de4e-3e8c-b9ec-c0a355bf6be4 | -10.9926 | -55.0577 | 2025-06-15 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 30fd04e2-12fb-3bfe-a8f8-b2a9a1ea3a29 | -10.9924 | -55.078 | 2025-06-15 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 22b6cf9a-c9eb-3c08-a835-3d995481ae1d | -7.216 | -43.5836 | 2025-06-15 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3fa6f3b3-b13e-3b0b-8a9b-f0778487173c | -7.2158 | -43.6069 | 2025-06-15 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 175.2 |


