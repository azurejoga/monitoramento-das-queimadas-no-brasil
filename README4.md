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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d023bb54-120f-3bc9-af6a-6659658f1441 | -9.07609 | -49.66665 | 2025-05-24 00:56:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| ddfc78fa-0a6a-3836-8231-de18b0a7ed5b | -10.72464 | -52.47268 | 2025-05-24 00:56:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 32481654-9b23-3f97-af75-43ed0f8afc22 | -10.36765 | -57.51158 | 2025-05-24 00:56:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 660c7e24-b05a-3272-b519-cf578098be03 | -7.65378 | -46.11065 | 2025-05-24 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f1da681c-86c2-381c-85ea-325a7cd688d2 | -7.79262 | -46.22754 | 2025-05-24 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 71f5f4e6-2f26-3964-9162-a9e346d0e048 | -7.07929 | -46.04602 | 2025-05-24 00:56:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6b5e8b2e-fc10-3734-b600-1d3b8404c9b5 | -20.9402 | -56.5786 | 2025-05-24 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 7d52d780-c026-3063-aacd-4433fbcb9f14 | -11.7583 | -54.2337 | 2025-05-24 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 9a2baf85-59a8-328d-8141-b969b5bce955 | -13.1498 | -56.8054 | 2025-05-24 01:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 582f7f86-173b-34c4-8456-e3b3a91eff30 | -6.2226 | -43.3459 | 2025-05-24 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 465be744-35d5-397e-9c6d-5bcff6b4c852 | -8.0889 | -43.1196 | 2025-05-24 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.1 |
| 3db9a2cc-ad3b-3f32-a1d4-a2824ab971e5 | -20.9398 | -56.5998 | 2025-05-24 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ec6892cb-3882-3810-9f91-60a4bdc3e37d | -8.07 | -43.1216 | 2025-05-24 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 135.8 |
| 3277c5ac-3ea5-3468-a1db-afb6ad596363 | -13.1496 | -56.8255 | 2025-05-24 01:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a79ce208-03ff-3ac9-8240-2e47c99c3201 | -20.9601 | -56.5967 | 2025-05-24 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 50a61efb-3a97-3957-809c-05ca74582cf3 | -13.1496 | -56.8255 | 2025-05-24 01:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 4bc7c8fa-589e-398e-b476-c0839dc52113 | -20.9398 | -56.5998 | 2025-05-24 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 86.4 |
| d28b5737-4c73-3d62-ac75-04c8708baccd | -13.1498 | -56.8054 | 2025-05-24 01:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 79e91079-163c-3a18-8334-e45caca80c85 | -8.07 | -43.1216 | 2025-05-24 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.4 |
| cb00fa01-2c9c-3c5c-a5e4-6b92de5d582d | -20.9601 | -56.5967 | 2025-05-24 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 12ed0b74-d3e4-32e8-bd67-e488f6933354 | -11.7583 | -54.2337 | 2025-05-24 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2daf095c-dbe7-3faa-86fd-b7dbdaaf5b56 | -7.2214 | -43.1153 | 2025-05-24 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| f1e715be-3e96-301b-af89-7733d5703745 | -20.9402 | -56.5786 | 2025-05-24 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 565db5c8-df11-3416-95cb-dd2eeb8cddcf | -8.0889 | -43.1196 | 2025-05-24 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| fab32268-3afd-3016-b7d2-df250ad187b8 | -7.2214 | -43.1153 | 2025-05-24 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| fe22f1ef-3e0d-37b8-b19f-7e636adefc4a | -8.07 | -43.1216 | 2025-05-24 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| d4c1c046-b933-3b7a-b278-710ab7b179e8 | -20.9398 | -56.5998 | 2025-05-24 01:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 876f6c36-71a7-34e3-8f7d-d22992c08504 | -20.9601 | -56.5967 | 2025-05-24 01:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 58.7 |
| cf4f5ffe-5326-3521-9b0e-da157fc08663 | -8.0889 | -43.1196 | 2025-05-24 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 768d9d2e-4131-3ee6-9ea0-894dcfa1ad4d | -20.9402 | -56.5786 | 2025-05-24 01:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 1f583ebc-1257-31b7-a067-b6ef6919317b | -13.1496 | -56.8255 | 2025-05-24 01:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 1580b512-d8e9-32bb-bf6a-9c434e6fd850 | -11.7583 | -54.2337 | 2025-05-24 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| a0dedb87-8bf9-30ac-859d-4b2a7515333f | -13.1498 | -56.8054 | 2025-05-24 01:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 9eedb402-9cc7-3a9e-aca2-80db757ebbdd | -13.1416 | -56.8036 | 2025-05-24 01:25:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea5fcfba-fd82-3a1d-90c2-15716486af38 | -11.9925 | -57.2038 | 2025-05-24 01:25:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00b4d036-8c7a-321b-941c-8eff7f0d9475 | -13.1455 | -56.819 | 2025-05-24 01:25:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81f84056-3020-3a8c-9783-d5096bad8b33 | -13.8646 | -59.726799 | 2025-05-24 01:25:00 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da788c74-3977-3bee-bd20-99d150796e4e | -13.1551 | -56.816502 | 2025-05-24 01:25:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3bbfda-0600-3a80-ba35-7020b339419f | -21.603701 | -56.0326 | 2025-05-24 01:25:00 | METOP-B | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 626552f6-0544-3186-a177-9b0ada6ff397 | -13.1512 | -56.801102 | 2025-05-24 01:25:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a8d715c-23bf-351f-8dcf-bcebd391ab59 | -20.9342 | -56.587101 | 2025-05-24 01:25:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b5383cf0-6da4-329b-bc4f-d1806ef373be | -13.8525 | -59.719398 | 2025-05-24 01:25:00 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58d56d05-fdbd-338c-ba38-e45e14ad1fff | -15.6269 | -57.3013 | 2025-05-24 01:25:00 | METOP-B | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 300fbaf1-2224-3457-854c-60413411ceb9 | -13.3639 | -54.241798 | 2025-05-24 01:25:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d6ff3d69-e47f-3859-90fe-758c1b52ca84 | -13.3699 | -54.264301 | 2025-05-24 01:25:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71c053be-c02b-3197-b8e2-edc4f17ba77e | -13.8622 | -59.7169 | 2025-05-24 01:25:00 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8719175-97a1-3157-a58b-80672ae95df3 | -13.9826 | -56.009701 | 2025-05-24 01:25:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f65519c-ed9c-3d82-8b56-0215c81a1621 | -13.3602 | -54.266998 | 2025-05-24 01:25:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81bab28c-0e6d-3721-a656-93d16dd36bdb | -20.9468 | -56.596298 | 2025-05-24 01:25:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a34490fd-0d02-3b0c-89b8-1d9ea3e83733 | -11.7476 | -54.213402 | 2025-05-24 01:25:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60986d72-f6cd-3f61-9b97-32503df10c64 | -20.940701 | -56.572201 | 2025-05-24 01:25:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 40e4d85c-cb50-3282-bbc8-5f99bb386205 | -10.3624 | -57.494701 | 2025-05-24 01:25:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e24418c4-c392-3404-acfd-1b3cf427a1c0 | -20.9402 | -56.5786 | 2025-05-24 01:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 71.7 |
| d4482663-59d3-33d2-bde6-c4156f088c44 | -8.07 | -43.1216 | 2025-05-24 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.2 |
| e306ac58-663e-3155-8ba2-d0a783a4d13b | -9.4956 | -40.3586 | 2025-05-24 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 80c48ac8-e8a1-381c-a6e4-bbcb6bd09008 | -8.0703 | -43.0981 | 2025-05-24 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| a8933759-ad7a-3583-ad8d-428fef2c6695 | -13.1496 | -56.8255 | 2025-05-24 01:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 031a4cdc-40c4-3037-b56f-ba089c30f27b | -20.9398 | -56.5998 | 2025-05-24 01:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 5dae9d45-6c40-3260-867f-75cbe13592a6 | -7.2214 | -43.1153 | 2025-05-24 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 197b371f-958f-3b43-9998-48be7bd68e2b | -13.1498 | -56.8054 | 2025-05-24 01:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ed8bbc40-0784-3046-a994-edfc4e006951 | -20.9402 | -56.5786 | 2025-05-24 01:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 9d851c08-b9f1-36d4-908b-7d4f6f9e6b6c | -20.9398 | -56.5998 | 2025-05-24 01:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 80.2 |
| f2c19771-3ef1-368a-9c17-edb6869e4258 | -8.0889 | -43.1196 | 2025-05-24 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |
| 6b46831a-2c15-3500-8c7b-b256fad28993 | -9.4956 | -40.3586 | 2025-05-24 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.0 |
| a7d4139f-9342-3ecf-a0aa-438899aa3645 | -13.1496 | -56.8255 | 2025-05-24 01:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| e3d48573-e26d-3a72-b4d4-5772d3781daa | -8.07 | -43.1216 | 2025-05-24 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 5ea6fb47-7e49-31d7-a250-caec824f92db | -7.2214 | -43.1153 | 2025-05-24 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 50.3 |
| 32c5ea37-ed73-3ec4-8de4-1a3dc35420a3 | -13.1498 | -56.8054 | 2025-05-24 01:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| ca86ecea-3578-325e-b5b3-74df5b27d253 | -10.3654 | -57.5095 | 2025-05-24 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| ba17bc40-6a63-38dc-bf01-25eea294a877 | -13.1496 | -56.8255 | 2025-05-24 01:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a694ffde-ce12-3ab6-9c69-e054d8de7900 | -20.9601 | -56.5967 | 2025-05-24 01:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 56.4 |
| acb9bad8-a948-3a89-82d3-df3f671f7d42 | -13.1498 | -56.8054 | 2025-05-24 01:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 37352296-07f2-372a-ad51-ed3df029a876 | -8.07 | -43.1216 | 2025-05-24 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.2 |
| ebddb226-5c73-3ed2-ad87-485577a73ece | -20.9398 | -56.5998 | 2025-05-24 01:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 26706111-e1bf-3835-86a1-49e6e87ea872 | -9.4956 | -40.3586 | 2025-05-24 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 166.8 |
| dd310ee4-15e9-3acb-91f1-fc103993560f | -9.496 | -40.3337 | 2025-05-24 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.9 |
| b8bcb7f6-4a62-3062-b860-061406a8125e | -7.2214 | -43.1153 | 2025-05-24 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| a1f5e6f1-ad32-3291-8218-61d4d7c2b94a | -9.4956 | -40.3586 | 2025-05-24 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 78edcbd6-41b6-365b-b33a-fda300e56b9c | -20.9398 | -56.5998 | 2025-05-24 02:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 498aff33-ea19-3922-8c76-36c117f949d2 | -4.2814 | -48.2871 | 2025-05-24 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 8a4f5cef-a3bf-30fd-8ade-67ac76beb595 | -13.1498 | -56.8054 | 2025-05-24 02:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fccb4f7b-5c4b-3ab1-a7f8-5d393861e9d5 | -20.9402 | -56.5786 | 2025-05-24 02:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 5d8522ab-2207-3022-9906-c0e7b7ea17eb | -8.07 | -43.1216 | 2025-05-24 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| 9f524c52-380a-35f6-9076-a5cfebf60768 | -4.2816 | -48.2655 | 2025-05-24 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8616cafc-eb06-3484-be71-4a9f27184691 | -13.1496 | -56.8255 | 2025-05-24 02:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 0d61f973-eff4-304f-8077-cb3c300b2aaf | -20.9402 | -56.5786 | 2025-05-24 02:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 52.5 |
| e9d8cb50-7c0f-382c-90e2-49fab808e9ee | -8.07 | -43.1216 | 2025-05-24 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| 135480ed-2536-30f0-b8c6-1b1a22b98ca0 | -13.1498 | -56.8054 | 2025-05-24 02:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| beb26aa5-1d24-3f9b-8a83-623df05bfd5e | -9.4956 | -40.3586 | 2025-05-24 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 121.8 |
| aafa4c02-b224-38ed-8a5d-65e7953600f3 | -9.496 | -40.3337 | 2025-05-24 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.8 |
| f2bc78c2-0255-398f-91d1-7fd82ab12066 | -20.9398 | -56.5998 | 2025-05-24 02:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 3619d1ac-11b7-3d82-a469-93709a5f20ad | -4.2816 | -48.2655 | 2025-05-24 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 8da0fd25-bbef-39bd-b481-89bc2d5f56dc | -20.9226 | -56.592098 | 2025-05-24 02:17:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 40c963cc-9d01-36c6-8652-cd52784a7f4a | -20.932699 | -56.625099 | 2025-05-24 02:17:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c4ea547b-be78-3735-b4d9-829654e2897e | -20.941999 | -56.621899 | 2025-05-24 02:18:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 801c14db-0452-3f16-bf5e-4acb287c83f9 | -8.07 | -43.1216 | 2025-05-24 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| 66b7395a-0afc-34ec-9f53-05e6305c3721 | -13.1498 | -56.8054 | 2025-05-24 02:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 7215b29d-bb72-310f-8ab4-6ca9198c8b0a | -20.9402 | -56.5786 | 2025-05-24 02:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 5e4d4d8f-aa15-3568-a648-a1329cca2760 | -20.9398 | -56.5998 | 2025-05-24 02:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 44c329f4-2b7c-3179-b96a-dd34d912f8b4 | -4.3001 | -48.2647 | 2025-05-24 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |


[Clique aqui para ver as próximas entradas](README5.md)
