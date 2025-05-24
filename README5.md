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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00c34a0e-eeab-314b-b565-da8c372b85d3 | -20.9398 | -56.5998 | 2025-05-24 02:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 93c91f6d-52da-326c-9a7c-59369fe6dcee | -8.07 | -43.1216 | 2025-05-24 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| ea969ed9-5f55-3c44-8b2e-5ca23bae08c6 | -4.2816 | -48.2655 | 2025-05-24 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3d299667-23b8-3878-baf9-58dd2cd03ee1 | -8.0703 | -43.0981 | 2025-05-24 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.8 |
| a9e6aafa-ad70-33ee-81da-eb7ce3052600 | -13.1498 | -56.8054 | 2025-05-24 02:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 06f4a686-1392-36d7-9878-fba46f5d8186 | -4.3001 | -48.2647 | 2025-05-24 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7f6ec7f1-4965-3c7f-abd2-c162c0f4f78c | -20.9402 | -56.5786 | 2025-05-24 02:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 47.0 |
| f7c1f32d-1dea-3f28-933f-ab994c71ebb1 | -8.07 | -43.1216 | 2025-05-24 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 15b21bb4-16b8-30c6-b331-e8917ff3c1a3 | -8.0889 | -43.1196 | 2025-05-24 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| cb70d4e6-db7a-3202-b594-5cb09b14f5a7 | -4.3001 | -48.2647 | 2025-05-24 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c98fb287-6eeb-3684-a198-8aeccd94f1d2 | -20.9398 | -56.5998 | 2025-05-24 02:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 58c01bc0-e82d-3449-a191-1514fda247b4 | -8.07 | -43.1216 | 2025-05-24 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 4d3e940f-2db3-36e0-b66e-25cf46618b37 | -8.0889 | -43.1196 | 2025-05-24 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 4e5d4f89-dbc1-3148-b7da-f05f545ffa03 | -4.3001 | -48.2647 | 2025-05-24 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 86f89537-0b64-32c5-af95-1242b89f47fd | -6.2226 | -43.3459 | 2025-05-24 02:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| b7577428-7067-3806-a0cd-2f9511d5e20d | -20.9398 | -56.5998 | 2025-05-24 02:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 3022205b-deb1-30b8-80a6-d1d6f51e6e39 | -13.1498 | -56.8054 | 2025-05-24 03:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 6b3b7cc9-3767-3c46-baf9-53f23ae0d8c3 | -8.07 | -43.1216 | 2025-05-24 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| de58f6d0-093c-3545-bf19-38283201345c | -8.0889 | -43.1196 | 2025-05-24 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| 215cb9fc-440c-30f6-940a-7c6170e22b28 | -8.07 | -43.1216 | 2025-05-24 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| e30e83e2-d72e-3a6f-89be-6360bbf09e59 | -20.9398 | -56.5998 | 2025-05-24 03:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 874a40aa-7b8e-3f21-8cc5-f52f55a75106 | -8.07511 | -34.97659 | 2025-05-24 03:15:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8e5c77ad-3ee5-320e-ab34-4e64b262d46e | -8.07871 | -43.12452 | 2025-05-24 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c8e8820d-76d4-39d5-8d4f-a2cdf23770df | -8.08007 | -43.11763 | 2025-05-24 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 12b68110-df56-3d72-98d3-36287998e2fb | -10.49269 | -42.42626 | 2025-05-24 03:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0199b7c4-7f6d-3552-aafa-5e361d4cd7a8 | -8.07303 | -43.11624 | 2025-05-24 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 90bb35e8-f106-364d-bfaf-be05ba922b58 | -10.55226 | -42.4302 | 2025-05-24 03:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 615261f6-6c0c-3733-b756-4a2b2ffa2497 | -10.4938 | -42.42071 | 2025-05-24 03:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| edfc0e0b-8538-30f0-bbca-1bd5e6e66d9b | -8.07166 | -43.12315 | 2025-05-24 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| e11a8994-053f-3f9d-a5fa-63896ea07ab9 | -8.06707 | -43.12301 | 2025-05-24 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b6691941-6559-34ee-bfcb-8852135f1cab | -8.07412 | -43.1244 | 2025-05-24 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.4 |
| 5b8f722d-1f45-3428-8e8d-d2d4b12286f2 | -8.0684 | -43.11607 | 2025-05-24 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fea2b81d-5c0a-3887-acea-233f4a8c8245 | -8.07544 | -43.11747 | 2025-05-24 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.4 |
| ad527509-0d83-3713-ad32-b56ee70c7319 | -6.95354 | -42.80215 | 2025-05-24 03:17:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| bbd7360f-cf5d-3a3d-af94-122632e7d74f | -6.95005 | -42.80547 | 2025-05-24 03:17:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4bc12113-83f2-3f3e-a629-53f826763b2a | -6.95137 | -42.79866 | 2025-05-24 03:17:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e2768438-b0b9-3c52-9ca5-c0e5fd59a493 | -10.55112 | -42.43574 | 2025-05-24 03:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5cc505dc-2280-32de-8b5b-0d6920485e6d | -20.34734 | -40.361 | 2025-05-24 03:19:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a7db14b2-aca7-3dc4-9de3-1f8a0c3cfa63 | -16.30174 | -42.77613 | 2025-05-24 03:19:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95474b4b-4484-39e9-b5ce-da3e2b63019c | -16.30275 | -42.7714 | 2025-05-24 03:19:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1c37c68-c59d-3fd3-9b09-4121a675aa92 | -14.22769 | -44.63176 | 2025-05-24 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e72e970-a7c9-3406-8c80-699aef139ed9 | -19.76117 | -40.87475 | 2025-05-24 03:19:00 | NOAA-21 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5ac719f0-0053-30cb-9733-701aa4cadc76 | -8.07 | -43.1216 | 2025-05-24 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 8914d975-64af-391a-8f0c-1cc3aa406130 | -8.0889 | -43.1196 | 2025-05-24 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 74f2928b-c1fd-3055-bf35-feb1acb43b99 | -20.44739 | -46.37765 | 2025-05-24 03:21:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bc675ce0-cbbf-3f47-a33c-f86cc3416e3a | -29.61225 | -49.94213 | 2025-05-24 03:23:00 | NOAA-21 | TERRA DE AREIA | RIO GRANDE DO SUL | Brasil | 4321436 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| d234b1a6-5b4f-3290-8a9f-481f727d19df | -29.61029 | -49.94907 | 2025-05-24 03:23:00 | NOAA-21 | TERRA DE AREIA | RIO GRANDE DO SUL | Brasil | 4321436 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| 3e77fbe8-9c73-327e-9f3c-b24cf0bd1e48 | -8.0889 | -43.1196 | 2025-05-24 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.3 |
| 69619eb5-f5f4-3d2a-bdd5-518de3b883b8 | -8.07 | -43.1216 | 2025-05-24 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| ab6e126d-fcfd-3320-9337-56f899fa9660 | -8.0889 | -43.1196 | 2025-05-24 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.9 |
| 79ab7c25-a9cc-3db5-8b88-c1ab7d492ae1 | -8.07 | -43.1216 | 2025-05-24 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| 53b4983b-ef71-3971-ab00-261167a2fd2e | -4.17735 | -42.03336 | 2025-05-24 03:42:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 34f143ec-a5e9-3daf-b0c0-fbc18d9ae044 | -8.07833 | -43.12124 | 2025-05-24 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.8 |
| 4c385ede-c9f4-30ae-a24f-42c34096e595 | -9.48817 | -40.34497 | 2025-05-24 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5c44ce43-8102-318f-8cb5-ed77defa77f5 | -7.22091 | -43.11619 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| eb3bc9ca-36bd-3b14-b25d-d2273c1a7bac | -7.54123 | -45.8344 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f9747b40-a10c-3aaa-9e24-bfe8d31789d2 | -7.2055 | -43.12823 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5271ebd0-c6e2-31f0-9f63-8be9ceb9bd89 | -10.54915 | -42.43348 | 2025-05-24 03:45:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a055dd42-d5cf-308e-8c6e-cb79dcbc35e0 | -6.94791 | -42.80358 | 2025-05-24 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 44e57101-e11a-3c34-8d93-03eca13019f2 | -7.65908 | -46.1081 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74a85386-f4a8-3246-92af-1db5a94eef8f | -10.72498 | -45.04405 | 2025-05-24 03:45:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a1cac8f-8deb-39a2-9020-152da2b0a0c3 | -7.54197 | -45.83032 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd5dc14f-8c51-3bcd-bab3-cacc12763143 | -7.79717 | -46.22596 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5145df30-7906-3b65-8d57-b672ac7ca301 | -7.22965 | -43.1231 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 248cbacb-a700-3734-9f8e-bf1128fa1dd8 | -8.07527 | -34.97765 | 2025-05-24 03:45:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c828a84e-299c-351b-9f9a-6184a2ce819a | -7.07203 | -44.93302 | 2025-05-24 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f11f5125-8e1e-37ee-9e58-777137c08bc1 | -7.80305 | -46.22707 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee784c10-d318-3593-ae15-e986ac98c5fb | -10.36689 | -47.98551 | 2025-05-24 03:45:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9e1a9744-4982-35a4-a928-5ac3e456906c | -10.55425 | -42.43007 | 2025-05-24 03:45:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bac43f1d-55c8-38f7-a39f-d911e8882fff | -10.36585 | -47.99079 | 2025-05-24 03:45:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f21fe0e2-2657-3ec3-8112-42e22cce065a | -7.23154 | -43.12178 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| caac82ae-fd36-3dc2-8dfc-cf7a4ef578a6 | -6.22844 | -43.36179 | 2025-05-24 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c31d04b-b8e2-3c35-901d-8b50b951aa66 | -4.29389 | -48.27381 | 2025-05-24 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 54e9e780-fb6d-33e5-97bf-1d862333d61e | -7.2267 | -43.12096 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| a84b5e5e-2abd-33e6-b246-8be8c3edeb70 | -10.7305 | -45.15985 | 2025-05-24 03:45:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93eeee60-5355-3995-b3a6-2dc3787c7dab | -7.06716 | -44.92863 | 2025-05-24 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6888fec-9637-3ac0-b9ac-6494a2df1c76 | -8.06847 | -43.12141 | 2025-05-24 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 33cf55b0-e9e1-32ec-a902-c7afde4e619c | -7.95604 | -46.8285 | 2025-05-24 03:45:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ceccfbd3-893e-30b9-b76a-5908b54c64fd | -8.07413 | -43.11714 | 2025-05-24 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 43.6 |
| b972ce6c-8c21-337f-8b47-6f398249c339 | -10.36795 | -47.9801 | 2025-05-24 03:45:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b23e5b9-e6af-32ff-b941-4a0c301c90a1 | -4.29116 | -48.27189 | 2025-05-24 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| bbd3a515-6b16-3cb4-91d1-80affef371b3 | -8.74917 | -44.92308 | 2025-05-24 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be6fa0f9-4b27-305c-a918-7331334732fe | -7.22575 | -43.11698 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 777ba52e-7ea3-3550-b844-9b28630c769a | -10.02618 | -48.69928 | 2025-05-24 03:45:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b9d158e-bbbe-3fbb-97e2-6f7e1b944292 | -7.65323 | -46.107 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c30c165-22cc-3b14-8f76-9a0a4ac87996 | -7.79128 | -46.22491 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 982ef4f2-50d5-35a1-8453-cc81d561ec31 | -8.06937 | -43.11627 | 2025-05-24 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 36759bbe-5dab-3bfc-9de1-ae2d1beedd83 | -10.0327 | -48.70086 | 2025-05-24 03:45:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd929d8b-3686-3231-b736-a76dbcd9fbda | -7.06579 | -44.9363 | 2025-05-24 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdbe4748-e04a-3efb-acee-c263a60aabb3 | -7.2248 | -43.12229 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 0a444f65-a8f0-3fda-969a-e6c86b4e01b6 | -10.73091 | -45.15718 | 2025-05-24 03:45:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0468778a-655e-356b-abe0-b894586d1b01 | -4.81928 | -44.35559 | 2025-05-24 03:45:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4723294-0b9d-30d5-97c7-cc1e0d739f26 | -9.49502 | -47.47956 | 2025-05-24 03:45:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9c53636-ae10-383a-a929-da8c09d408c5 | -8.75338 | -48.03635 | 2025-05-24 03:45:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3eac1ec7-adbe-3817-a024-86427e6f98f4 | -7.07268 | -44.92938 | 2025-05-24 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9571c62-9312-3fad-9ef1-0374aeeeb1bf | -7.2276 | -43.11564 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b18f0231-e8d5-380b-98ae-7d3f358e8a87 | -6.94855 | -42.80239 | 2025-05-24 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 266a4b9a-bcf8-306b-a73b-88eaccff592d | -10.54989 | -42.42927 | 2025-05-24 03:45:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b023e724-18be-3c77-9516-e0f9ac95e3e2 | -5.3472 | -43.74829 | 2025-05-24 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f52cc84-abda-3bd3-8c2d-b0be3e08836f | -6.95329 | -42.80331 | 2025-05-24 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README6.md)
