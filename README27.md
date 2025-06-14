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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9e3e04d-88fe-3e9e-b7d3-ee7f43962626 | -13.9663 | -54.4364 | 2025-06-14 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 49616e32-9838-32a1-a4e1-fb1dd0d25b4d | -12.6236 | -57.8926 | 2025-06-14 13:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 022c572b-0657-3f80-9ed1-2e967c60bb7c | -10.8696 | -54.2947 | 2025-06-14 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 011b22f0-920f-3a0d-86fa-b655807a0f11 | -8.6097 | -51.5731 | 2025-06-14 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| aeaeabb4-5373-38f4-9a42-ddf152fe9d6a | -10.8696 | -54.2947 | 2025-06-14 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 42afa5d2-550e-33a8-9033-670530ce866f | -13.9056 | -54.6498 | 2025-06-14 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| d748b15a-eac5-315c-97ed-3b1892f167dd | -12.5177 | -57.2031 | 2025-06-14 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 733236e6-4f02-36c3-8563-a05b364d1572 | -12.6236 | -57.8926 | 2025-06-14 13:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 0030abea-d801-302a-bbb3-ce71715e0d3c | -13.9663 | -54.4364 | 2025-06-14 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| aa866546-2751-39e2-b0db-3b467822ea0d | -13.726 | -45.2421 | 2025-06-14 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| d71cc235-1cf0-32d9-8d23-b971ba2baf82 | -13.9056 | -54.6498 | 2025-06-14 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 5f5d9d35-878c-32e2-9c7c-c46a137fc8a4 | -12.5367 | -57.2014 | 2025-06-14 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7f631da7-0277-3edc-b679-15043e79fb5e | -10.2677 | -46.968 | 2025-06-14 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| fecdbf9c-9ca8-3ea2-b60e-465f5f1401c0 | -13.9663 | -54.4364 | 2025-06-14 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 9a62a0d5-d91e-3a24-9815-bac8bf7051ac | -12.6236 | -57.8926 | 2025-06-14 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2349fa9d-3e7e-3235-8bb6-5ab44d8375ee | -12.5177 | -57.2031 | 2025-06-14 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 17f8c830-e459-3c8c-89f8-6c6cf76e4804 | -12.4645 | -58.5603 | 2025-06-14 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 422eab16-4549-36c8-878d-51771fe2bf4d | -10.8696 | -54.2947 | 2025-06-14 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| a1483655-5739-326e-8213-5cb77229eeae | -13.9663 | -54.4364 | 2025-06-14 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 91500ac7-bcb8-393c-8835-a69792588b0e | -12.6236 | -57.8926 | 2025-06-14 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 629f132e-7709-30af-94a7-834dc6160da0 | -10.8694 | -54.3151 | 2025-06-14 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 0d6af70e-1f59-3326-81a2-7ab12259cde7 | -13.726 | -45.2421 | 2025-06-14 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 7f1b6725-1564-3021-8edf-3a77f9e1d12a | -10.9355 | -56.8322 | 2025-06-14 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| a8b754c2-5bcd-3273-b53b-162a25013377 | -12.4647 | -58.5405 | 2025-06-14 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 64b6288a-c792-38ee-aa0c-d0ca219b2f42 | -12.2664 | -54.5331 | 2025-06-14 13:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a2eb370a-b955-3de3-baf1-483dba8e11f1 | -13.9056 | -54.6498 | 2025-06-14 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| f8dacafc-d187-3541-8926-699f2ad3db12 | -12.4645 | -58.5603 | 2025-06-14 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 2abc5ee2-05bd-3676-a3d9-f0f15c0f83e4 | -10.8696 | -54.2947 | 2025-06-14 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 81529e18-8224-3dcb-9ef9-0b12a8b46338 | -12.5177 | -57.2031 | 2025-06-14 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 01a78603-98f2-3b71-9453-5b88a8dd6f1b | -10.2677 | -46.968 | 2025-06-14 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 71094223-111f-3b7a-a6db-5d8023fc3b9a | -12.5367 | -57.2014 | 2025-06-14 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 3237450a-1b35-3ac9-aff3-917e60f81c81 | -12.5367 | -57.2014 | 2025-06-14 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| e41f5f6e-4e1b-3e39-81d3-a1a3820a0bf3 | -12.2426 | -44.1572 | 2025-06-14 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 4f477354-584d-3d59-a5fe-3ad082e52a1b | -13.9056 | -54.6498 | 2025-06-14 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 018c5a83-4f55-300e-99f4-1d83b2c08223 | -13.9663 | -54.4364 | 2025-06-14 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4985e7f8-6c58-3ca4-aa90-da803cd4464f | -12.2664 | -54.5331 | 2025-06-14 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 137f3291-9253-358b-af26-df65633103c2 | -12.5177 | -57.2031 | 2025-06-14 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ee3ff438-66d1-38de-96fb-b0e0a71d11ce | -10.8696 | -54.2947 | 2025-06-14 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 5ff1dc3f-80bb-3ddc-bfff-21dfaf8c80fb | -12.6236 | -57.8926 | 2025-06-14 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 268f54fd-e70a-32cd-96e6-1a16dd738afa | -12.2233 | -44.1602 | 2025-06-14 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c303fcb7-e7ef-3fe1-8bf7-b961b5c976f3 | -12.4645 | -58.5603 | 2025-06-14 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 03171267-2624-34db-8090-82cc4a808f01 | -10.9355 | -56.8322 | 2025-06-14 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| bf1afbc1-83b7-32a1-9d06-58831534262a | -10.9167 | -56.8336 | 2025-06-14 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| af0077a3-a8cd-3ad0-8eac-03e49d9ff16a | -10.9355 | -56.8322 | 2025-06-14 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 179.5 |
| efc8e744-28ce-371a-99b3-a9d21845aa79 | -12.2233 | -44.1602 | 2025-06-14 14:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| b55e1a31-f4b6-3352-b60e-8506316d2253 | -10.8696 | -54.2947 | 2025-06-14 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 26aa8d56-26f0-3a0b-971e-9ad2d6707be2 | -10.9167 | -56.8336 | 2025-06-14 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| f2b49c60-d1a1-34e5-8e9c-551b1668aeb7 | -13.726 | -45.2421 | 2025-06-14 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3f0c5bc9-8838-3afd-920d-ed4056640718 | -13.9056 | -54.6498 | 2025-06-14 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 538f5e15-1cd4-3856-ba72-72d14e3f0699 | -10.8694 | -54.3151 | 2025-06-14 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 27ec6698-3cd7-3be5-a2f5-5716340ae809 | -12.4654 | -58.481 | 2025-06-14 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ac9d096b-b146-324a-9830-f0c80e5ce133 | -12.6236 | -57.8926 | 2025-06-14 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 990c4332-eb04-3919-b6ff-2857018d0a17 | -12.4645 | -58.5603 | 2025-06-14 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 018424b7-435f-3ffd-b940-3ed7b1f2c671 | -12.4647 | -58.5405 | 2025-06-14 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 069dcdc7-cb61-3f8b-a423-e1ae310d619f | -12.5367 | -57.2014 | 2025-06-14 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e2af2564-4c51-35be-bbbc-58120c319900 | -12.5177 | -57.2031 | 2025-06-14 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 193996f8-5243-3378-8748-ab04da6df9f9 | -12.2664 | -54.5331 | 2025-06-14 14:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| b95aa046-c538-38a5-b4bc-353b7455e212 | -10.2677 | -46.968 | 2025-06-14 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 9038d827-c941-3ba0-b830-7e05a775487d | -12.4654 | -58.481 | 2025-06-14 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| f87a0b76-e418-37b3-a7cb-45231bb9933b | -12.4647 | -58.5405 | 2025-06-14 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ae164ed0-ed3c-395f-8022-e8f2b13105e1 | -10.8694 | -54.3151 | 2025-06-14 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a3ce8f2e-93f5-3699-b11f-dbfe9177fa68 | -10.9357 | -56.8122 | 2025-06-14 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 5608c2ed-bc46-34e1-98dc-4e5dabeecf8d | -10.8696 | -54.2947 | 2025-06-14 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 143.6 |
| d84ac43c-db28-3994-8e8d-528c381f78c7 | -12.4645 | -58.5603 | 2025-06-14 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 0096f212-b861-38be-a1cf-9a72f15b5d34 | -12.6236 | -57.8926 | 2025-06-14 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| b9fc2acb-f2c5-3e3a-b147-7bfc803a1112 | -13.9056 | -54.6498 | 2025-06-14 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| a40d87ea-72b2-377a-b241-3328058e4d98 | -12.5177 | -57.2031 | 2025-06-14 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 87932ef2-c943-3b49-b478-ab1a2aad4fe0 | -10.9167 | -56.8336 | 2025-06-14 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| e471c3a2-3095-35d2-b725-c5022d96d692 | -12.2664 | -54.5331 | 2025-06-14 14:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1e9d5d2c-6a86-3364-94dd-e7786407c833 | -12.5367 | -57.2014 | 2025-06-14 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 3e833a45-103e-3c0a-8547-38d9729634ce | -10.2487 | -46.9702 | 2025-06-14 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 309.7 |
| 14061651-7d77-3e84-b041-37c60a5adb6a | -10.9355 | -56.8322 | 2025-06-14 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 188.4 |
| 3aee1b5c-6faf-3679-8e77-97cdc8452c66 | -12.2664 | -54.5331 | 2025-06-14 14:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 6a7f21c9-f13c-3c28-863f-828121a14c47 | -10.9167 | -56.8336 | 2025-06-14 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 5c45684a-c5c0-36a6-90ef-b03131726770 | -10.9355 | -56.8322 | 2025-06-14 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 207.4 |
| 79ac4e25-ce5c-3039-bbee-19356f2cae80 | -12.4645 | -58.5603 | 2025-06-14 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| b1c0d34e-da54-3ca8-bade-442da5603d50 | -10.9357 | -56.8122 | 2025-06-14 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5ea6db35-7f44-3154-bcb0-44db5e6f5048 | -11.0113 | -55.0764 | 2025-06-14 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| a24392b7-13c7-3c2b-8eb3-a7f7f532245d | -13.9059 | -54.6291 | 2025-06-14 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 78d82da3-cbb0-3bd2-a707-b607e116757d | -10.8694 | -54.3151 | 2025-06-14 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 6197ac9b-3883-38f6-acf1-827d20753ad7 | -13.9056 | -54.6498 | 2025-06-14 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 91e8d9d7-e81c-35a5-a6d3-cb7a51a43edd | -12.4647 | -58.5405 | 2025-06-14 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 01820acb-bb50-328a-b03b-bdc1f694cb00 | -12.6236 | -57.8926 | 2025-06-14 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 449c4b88-07e7-318c-8f8e-886c03a00da7 | -10.8696 | -54.2947 | 2025-06-14 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 2c8bf086-18d6-3ae4-b218-396afab2b13b | -10.9355 | -56.8322 | 2025-06-14 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 250.7 |
| 5841926f-fb08-3944-8161-2cc721e643d4 | -10.9167 | -56.8336 | 2025-06-14 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 155.4 |
| 6f2b11a2-b902-37fc-8629-1c7ca97d59ed | -12.4645 | -58.5603 | 2025-06-14 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d4e521b9-d4b2-37a6-8814-8759273b262d | -13.9056 | -54.6498 | 2025-06-14 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 142.0 |
| c309d8a8-0582-324d-a5fb-dca5bafddf62 | -12.4647 | -58.5405 | 2025-06-14 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 15028890-3d97-34a3-b686-37291286386f | -13.9059 | -54.6291 | 2025-06-14 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| bf8bedf3-5a5f-3f48-ae92-c7b82f994929 | -10.2677 | -46.968 | 2025-06-14 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 354.1 |
| 3ff730dd-f051-38b2-a786-c7408c98a824 | -10.9357 | -56.8122 | 2025-06-14 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 2e8bc502-d1ee-3178-b1d8-479dd5b89bad | -10.9169 | -56.8137 | 2025-06-14 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e6df4eb4-6a0b-3be6-92d8-31aedb85a007 | -12.2664 | -54.5331 | 2025-06-14 14:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| f23691e1-50fc-35ae-ade8-a3a98198baa4 | -11.011 | -55.0967 | 2025-06-14 14:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| bd0d87b1-42eb-3e38-b085-bd71097ea0bf | -10.8694 | -54.3151 | 2025-06-14 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| f59e7c28-2bb2-32e7-8e2f-b1fa23d3f9df | -10.8696 | -54.2947 | 2025-06-14 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.9 |
| a2c5e5f0-cfc2-30b7-a4a1-e37aa4411959 | -12.6046 | -57.8942 | 2025-06-14 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| c2cf5f2d-e986-3f9a-95d6-9eb4b8840ab0 | -10.2487 | -46.9702 | 2025-06-14 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.2 |
| f71b93ab-33ec-3937-8a27-3ffc1b343b3b | -10.2674 | -46.9903 | 2025-06-14 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |


[Clique aqui para ver as próximas entradas](README28.md)
