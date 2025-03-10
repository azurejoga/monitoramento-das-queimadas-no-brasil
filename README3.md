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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5264835e-5c9d-34af-b6ff-46e436f5c20d | -24.67594 | -51.90563 | 2025-03-10 05:10:00 | NOAA-21 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a5d5653d-092e-39a2-9c16-c4d8068e46cd | -23.5422 | -53.36619 | 2025-03-10 05:10:00 | NOAA-21 | IVATÉ | PARANÁ | Brasil | 4111555 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b3d5ee16-8e4b-38b0-b366-8242fc451b0a | -23.5417 | -53.37067 | 2025-03-10 05:10:00 | NOAA-21 | IVATÉ | PARANÁ | Brasil | 4111555 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 79a9eac9-a6d7-30ea-869b-d9316eddea81 | -9.18856 | -61.38289 | 2025-03-10 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f8e18e95-1c22-3572-929e-20700804c144 | -9.12652 | -61.46617 | 2025-03-10 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f813feba-96e9-34b1-b0ff-d15691499b2d | -9.1866 | -61.38564 | 2025-03-10 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 273f173a-1d09-3e68-9ff7-135e8d25d498 | -9.18469 | -61.38512 | 2025-03-10 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 83731bfc-fb37-3cd4-9246-c93f935cefd6 | -21.7218 | -51.8997 | 2025-03-10 07:10:00 | GOES-16 | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.9 |
| 97bca6c1-2922-3f89-84aa-c28d08f5054b | -21.7218 | -51.8997 | 2025-03-10 07:20:00 | GOES-16 | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.1 |
| 59a7bef3-4c9c-3b92-a04d-460acb479046 | -21.7218 | -51.8997 | 2025-03-10 07:40:00 | GOES-16 | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| 47918362-8080-34b5-ae86-486c5414d8d4 | -21.7218 | -51.8997 | 2025-03-10 08:50:00 | GOES-16 | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.2 |


