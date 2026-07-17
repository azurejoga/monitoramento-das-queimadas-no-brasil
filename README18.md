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
| c6929bd6-b332-3f8d-af3d-111962289380 | -19.8436 | -57.9917 | 2026-07-17 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 88270e8a-b27a-3d63-9852-e2665c7f719d | -10.8625 | -46.5589 | 2026-07-17 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 4b6a3137-82f9-39e1-a16b-0fd02088adf2 | -18.5675 | -56.8109 | 2026-07-17 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 797d942d-c3f2-3c0a-8e3b-eb3c9d16d8dd | -18.5476 | -56.8135 | 2026-07-17 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.0 |
| 41fc0302-4248-3f33-8d8e-20f0bc3956b7 | -9.5085 | -47.143 | 2026-07-17 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 5ed5b973-cfcb-3f6e-89a8-d5bc965e9f80 | -19.8436 | -57.9917 | 2026-07-17 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.3 |
| ec0c6b2b-62dc-3cae-95fa-5a21a2657e97 | -10.8435 | -46.5613 | 2026-07-17 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 0592b04f-5364-33c9-b8a3-0ca308638152 | -10.8625 | -46.5589 | 2026-07-17 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| a581c0b7-5417-31ee-a528-e3c82596c941 | -9.5277 | -47.1187 | 2026-07-17 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 30ca0922-3ef1-37f6-9f6c-423ba3a5da92 | -10.8625 | -46.5589 | 2026-07-17 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 2bb6b024-b674-39d9-9e5f-042b772ad321 | -19.8444 | -57.9501 | 2026-07-17 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| ca682bce-bc8d-3712-aa81-5f213c34051d | -19.8246 | -57.9319 | 2026-07-17 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 0263ff30-1600-3160-a614-37f02a306681 | -19.8436 | -57.9917 | 2026-07-17 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 1d5c723d-17c1-3efd-b23c-2a9a4fdc2f26 | -9.902 | -53.3736 | 2026-07-17 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 4fef47a6-79ea-3016-aea5-925b31efc013 | -9.5085 | -47.143 | 2026-07-17 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 480ae8b3-8123-304d-a9b3-f1a5f1455bbe | -18.5675 | -56.8109 | 2026-07-17 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.7 |
| 692f448b-8241-32a4-96cc-8c71b8e10fbf | -10.8435 | -46.5613 | 2026-07-17 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 45134c55-54a3-3a10-8ab7-2cf9d93b5dd7 | -19.8447 | -57.9293 | 2026-07-17 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 3185b47b-8f4e-3c72-8e49-ac7b48483555 | -18.5476 | -56.8135 | 2026-07-17 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 1d774f33-3c42-301f-94c4-812ba406a3b4 | -18.5671 | -56.8317 | 2026-07-17 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| e2bc7cd1-92f9-3a2f-a936-92a11fb6bc12 | -9.902 | -53.3736 | 2026-07-17 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 55b6cbf7-d653-39c0-89d8-32c7b30951a3 | -10.8625 | -46.5589 | 2026-07-17 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 7ec74e66-7db0-36bc-9135-f83879a4063d | -19.8447 | -57.9293 | 2026-07-17 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| b5714390-23d9-3d9e-815d-391470e43843 | -19.8436 | -57.9917 | 2026-07-17 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.3 |
| e06ae8ea-5e53-355a-991e-f28c38ffdcd7 | -9.5277 | -47.1187 | 2026-07-17 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 046b7ce5-a65d-34c5-ab5b-e7f799c8a4dc | -18.5675 | -56.8109 | 2026-07-17 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.7 |
| cefaa76e-45ce-3842-9cb7-bc689d1d26d0 | -18.5671 | -56.8317 | 2026-07-17 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 2237e883-c256-33ee-8329-afb47bb88f82 | -19.8246 | -57.9319 | 2026-07-17 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 44435a9e-f4e6-3054-8cc5-0b65abbcff6a | -9.5085 | -47.143 | 2026-07-17 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 5dc587ec-2da5-3612-bb97-c66af49f7406 | -18.5476 | -56.8135 | 2026-07-17 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 9d6a5c5e-fa18-3ca5-a78c-e19a74890b7e | -18.5675 | -56.8109 | 2026-07-17 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.8 |
| c264fb93-5c62-3d0d-b600-8973fd7d5949 | -10.8449 | -46.4711 | 2026-07-17 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 84164a19-e6bd-35e8-b825-7f1a728c1d20 | -19.8436 | -57.9917 | 2026-07-17 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 634a3222-3a00-3e82-9be6-be6a9ba128d5 | -18.5671 | -56.8317 | 2026-07-17 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| f50f9670-b217-3647-a44d-66e3b87a3e39 | -9.902 | -53.3736 | 2026-07-17 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f6ebb3f5-85b2-3305-82cb-f6a93417b504 | -9.5085 | -47.143 | 2026-07-17 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| c8247c48-63d0-3fde-b76b-542764f3e8cc | -18.5476 | -56.8135 | 2026-07-17 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.3 |
| f3d47c48-a903-3add-b1d3-04fbda219ba0 | -19.8444 | -57.9501 | 2026-07-17 14:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.5 |
| dcf86bfd-3131-3fe5-9be6-52b71235002c | -18.5675 | -56.8109 | 2026-07-17 14:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.3 |
| 6b91a302-3fb9-3e4e-b536-7ed2174dcc43 | -19.8447 | -57.9293 | 2026-07-17 14:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 33febca9-f70a-3702-86e3-7b505e9566b3 | -9.5085 | -47.143 | 2026-07-17 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 58f6d02f-4fb2-3011-ae37-5a1c85cc8630 | -3.4066 | -49.1163 | 2026-07-17 14:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| c5d517cb-36ad-3374-8ff7-ab1691bb2ca8 | -18.5671 | -56.8317 | 2026-07-17 14:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| f7df5a8a-b37e-36f8-ba9b-bb392055dbb5 | -18.5476 | -56.8135 | 2026-07-17 14:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 5986ee12-12d8-3e7a-be3c-9f0813d29604 | -9.9213 | -53.3308 | 2026-07-17 15:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 49f520b6-408d-3110-9c79-3290f5ff7c26 | -9.5085 | -47.143 | 2026-07-17 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| fc3b7396-3709-3e3e-967d-ff10c60759d1 | -3.4066 | -49.1163 | 2026-07-17 15:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 3c4e7bb8-2a59-3ce1-bea0-9837f4376cdf | -18.5476 | -56.8135 | 2026-07-17 15:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 199354d9-47d8-36e9-abe1-9e68696bf78d | -18.5671 | -56.8317 | 2026-07-17 15:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 870200c9-c6e9-3de0-9bb2-1847bc215a9b | -18.5675 | -56.8109 | 2026-07-17 15:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 7a0b25fc-6336-36d5-8618-29faf4a1d6a2 | -3.4251 | -49.1157 | 2026-07-17 15:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| e5be1010-8f46-3118-82e2-b7f95bdef109 | -18.5675 | -56.8109 | 2026-07-17 15:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.8 |
| cbbdb97b-9d91-38aa-a697-0b881cf3a8e2 | -9.902 | -53.3736 | 2026-07-17 15:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 1e31917d-0be6-338f-9b3f-b07818dbd44d | -19.8447 | -57.9293 | 2026-07-17 15:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.5 |
| c7f84c40-937a-3894-ac01-73a0a96b4e93 | -18.5476 | -56.8135 | 2026-07-17 15:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| fb3c3042-8a25-365b-9d2c-08997ec62cc9 | -9.9213 | -53.3308 | 2026-07-17 15:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d6bb69e6-052f-36ba-8939-0aa4a146d981 | -3.4066 | -49.1163 | 2026-07-17 15:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9dd011d2-ef4a-3a81-8340-5aca128c9f9f | -9.5085 | -47.143 | 2026-07-17 15:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| fd64b6a0-cca9-315c-a18b-06a500cec219 | -13.11 | -52.48 | 2026-07-17 15:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c64b1da4-71e5-36ea-a6b2-39a66fd92e5a | -13.11 | -52.54 | 2026-07-17 15:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f14b3f1-714b-3c14-9e1a-857293b9bddf | -13.08 | -52.52 | 2026-07-17 15:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc1ba92c-0a1e-371e-9e67-a3ced6235f69 | -17.86 | -50.73 | 2026-07-17 15:15:00 | MSG-03 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c623b4ae-4e76-3fa1-be0f-5bef0f8eb842 | -13.08 | -52.46 | 2026-07-17 15:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe9a1751-0bfc-3c71-b042-fab2a543c5bd | -9.9213 | -53.3308 | 2026-07-17 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| b171424f-9988-3531-b01d-4e4627e553d9 | -9.5085 | -47.143 | 2026-07-17 15:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 806bddc3-2bea-3078-bd37-ec6d1e9eab5c | -18.5476 | -56.8135 | 2026-07-17 15:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.0 |
| c39be2ed-23df-3df7-980e-3ff95e95b8c0 | -9.5085 | -47.143 | 2026-07-17 15:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 178fcb09-ee00-310b-95db-b7080665f082 | -11.5082 | -50.3418 | 2026-07-17 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |


