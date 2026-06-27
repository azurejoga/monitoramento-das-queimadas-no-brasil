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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e4a66cf-c1f9-3804-88a4-d051bda6ec24 | -12.6236 | -57.8926 | 2026-06-27 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 6478cecb-a811-33ac-bc52-bd1d7da5ef4c | -11.9095 | -57.4134 | 2026-06-27 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 227.6 |
| 31f64328-30e3-3b86-a88c-5603ce99b053 | -10.5374 | -53.7094 | 2026-06-27 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| ee185ea4-e0b5-3d60-b9ba-b8aa469233c5 | -13.2583 | -54.4109 | 2026-06-27 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 161.6 |
| aa8959f7-62d7-3d17-92a6-f6e161f244df | -10.7777 | -54.0983 | 2026-06-27 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 1a43c92e-1cc6-33d3-8d7e-f64463e48109 | -8.3095 | -48.1859 | 2026-06-27 14:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 0212c42c-7fb9-3cca-86fc-43e1561836f9 | -12.6048 | -57.8743 | 2026-06-27 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| dfb857c3-040c-3f86-b7a4-5f5e4cffb3ff | -12.6046 | -57.8942 | 2026-06-27 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9d424b0d-e211-3972-9d94-a0d6147aab06 | -11.9284 | -57.4119 | 2026-06-27 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 415.6 |
| 2d9c3d1b-403d-37bf-a87a-7623e850cce1 | -11.9097 | -57.3935 | 2026-06-27 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| ef2ee57c-b5b4-3d4f-ad92-5daaf6156d1c | -13.2392 | -54.4129 | 2026-06-27 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 237.5 |
| 20b793ab-e09d-3f66-b407-98a44d57a72e | -10.7777 | -54.0983 | 2026-06-27 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| fded03aa-f8ed-33f1-8434-d5b0498f7b47 | -13.2583 | -54.4109 | 2026-06-27 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 3376e808-6ddc-3b27-b060-b6889efcd3bb | -10.5374 | -53.7094 | 2026-06-27 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| fe633d50-ed63-3714-bfa7-4796a8f81269 | -13.2201 | -54.415 | 2026-06-27 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 55bbbbb7-fb03-36dd-9b8b-fa8cee842a9c | -12.6236 | -57.8926 | 2026-06-27 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 27e0dee7-4bbf-39a4-b2a7-8375221fc51f | -11.9095 | -57.4134 | 2026-06-27 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 214.8 |
| 050f0a1a-6c9f-37b5-bb2b-d6b366844444 | -11.9097 | -57.3935 | 2026-06-27 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 74ee7cff-5221-3d8d-a3b1-4b39813a7818 | -13.2583 | -54.4109 | 2026-06-27 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 2319da32-8e62-3a8f-9e21-a18f755e0f64 | -12.4651 | -58.5009 | 2026-06-27 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 680.2 |
| dfe200c3-f9a3-3322-8806-3de3fc427c2f | -11.9095 | -57.4134 | 2026-06-27 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 213.6 |
| 6fce395e-b688-3ec0-9b11-4bca03078792 | -12.6236 | -57.8926 | 2026-06-27 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ba153ff6-d989-3d34-bc78-9c76f8b82432 | -12.6046 | -57.8942 | 2026-06-27 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| e4526e3a-645e-34f1-a2a7-1fca1da97140 | -10.5374 | -53.7094 | 2026-06-27 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| d01ea80d-e88d-3338-905b-fedae7de0eeb | -13.2201 | -54.415 | 2026-06-27 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 070e1136-243f-31bd-8802-6eaf728d1f5c | -12.4654 | -58.481 | 2026-06-27 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 252.7 |
| c5bce97f-1a72-3ac8-99d2-3302e41e601d | -13.2392 | -54.4129 | 2026-06-27 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 185.5 |
| 9808930d-e050-362a-9e4f-b6547be39a1a | -12.4464 | -58.4825 | 2026-06-27 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 0e9cb5e0-ce6c-3e1f-ac02-945cdb730c90 | -12.4462 | -58.5023 | 2026-06-27 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 367.6 |
| d6559b0d-f2a1-3f4f-8580-43b98e0ad54b | -11.9284 | -57.4119 | 2026-06-27 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 412.9 |
| 7add815a-92fe-3025-a8d2-3e8e754614e5 | -12.6048 | -57.8743 | 2026-06-27 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |


