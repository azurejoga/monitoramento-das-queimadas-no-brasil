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
| 1b33d056-166b-3303-867e-4361c5c6ac23 | -8.0321 | -43.1257 | 2025-11-27 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 172.8 |
| bad7f97e-4b01-3714-a809-a03263bc0559 | -20.408 | -57.9368 | 2025-11-27 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.9 |
| 2f349d00-b661-3a43-aeb1-e6351403071b | -3.8269 | -50.1809 | 2025-11-27 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 8ba78a45-1818-3881-9e63-0a6dcfcd7135 | -8.0507 | -43.1472 | 2025-11-27 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 168.4 |
| a6e231f9-640e-341b-84cb-19723e0070fc | -20.4076 | -57.9577 | 2025-11-27 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.7 |
| aae67429-1521-3003-a08d-47c51db9300f | -1.3494 | -53.0891 | 2025-11-27 02:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d149a5af-9135-38ad-9acc-5bc498895a22 | -2.7588 | -49.3285 | 2025-11-27 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 2107114b-b3f1-3f45-b5ae-4bf8b1ff798d | -8.0321 | -43.1257 | 2025-11-27 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| ecb31ef3-a6ad-3619-9042-245954a0777a | -8.051 | -43.1237 | 2025-11-27 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| d6790383-0c72-3375-b037-552d42662486 | -8.0318 | -43.1493 | 2025-11-27 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 51f428aa-015a-38f4-93eb-cddc6646a519 | -8.0507 | -43.1472 | 2025-11-27 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.7 |
| bd995030-f4c7-325e-a0d3-56018befa963 | -13.4841 | -46.7048 | 2025-11-27 02:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 49079afe-c2fc-3657-a3c4-62ebbb56b65d | -3.5269 | -43.6828 | 2025-11-27 02:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 9fbed88b-1185-3c86-861d-217689fb7656 | -1.3494 | -53.0891 | 2025-11-27 02:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 53cf420d-6ef6-3cea-9c56-e9dc7a540db8 | -3.8269 | -50.1809 | 2025-11-27 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 2259ba31-21d4-372b-a849-51136af463d2 | -3.5083 | -43.6837 | 2025-11-27 02:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 50433e6e-8a62-3cad-bb48-935b9224945b | -4.7203 | -46.4719 | 2025-11-27 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| f1fd0438-227d-3a35-853a-75715956bb2a | -4.7204 | -46.4497 | 2025-11-27 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 3c2b2e73-18a3-38ba-95e6-f0311f04f117 | -3.5269 | -43.6828 | 2025-11-27 02:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 0a4bedbd-88bb-38d3-8756-26b43ea08598 | -4.7018 | -46.4508 | 2025-11-27 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7e54a289-6343-3c3f-bfc7-7b464490bdea | -3.2195 | -45.5398 | 2025-11-27 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 93db4966-015d-3457-a57b-284ef205808c | -13.4841 | -46.7048 | 2025-11-27 02:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 37b0c56b-9996-3059-80c2-25c9dd1bcc78 | -4.7204 | -46.4497 | 2025-11-27 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 3cd7cd53-64d4-3187-8cbe-0571af2376f4 | -4.7018 | -46.4508 | 2025-11-27 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 86.0 |
| cb83e652-a7a0-37a4-a7b9-a59d95a9b89c | -4.7203 | -46.4719 | 2025-11-27 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 74108f89-ec8f-3f76-8835-52bb59d0df5f | -3.5269 | -43.6828 | 2025-11-27 02:30:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 0bd37c01-4b8d-3069-aadd-b006310982a6 | -2.7104 | -47.4147 | 2025-11-27 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| cf15db37-57aa-34ad-8569-39b2345585f3 | -2.7105 | -47.3929 | 2025-11-27 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 0db82f46-73cf-368b-9054-5eed603d17fe | -4.7204 | -46.4497 | 2025-11-27 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 23878f8f-0ed7-3040-aa22-810e3bb1f83d | -4.7203 | -46.4719 | 2025-11-27 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| caa83949-c937-32bd-a820-14098db07b31 | -3.5269 | -43.6828 | 2025-11-27 02:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 06f5b882-a7a9-3859-ae60-4cdbb41ecdaa | -4.7018 | -46.4508 | 2025-11-27 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| ab6c2c4d-3907-3f2d-ac43-09c6fd65029a | -3.5083 | -43.6837 | 2025-11-27 02:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| f69d5849-f775-3b8a-840f-69bf80e5d7d7 | -2.7105 | -47.3929 | 2025-11-27 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| fc96f393-786e-33ce-aa5b-62d5b48ddf04 | -2.6919 | -47.4153 | 2025-11-27 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| e9976575-ff4a-38f9-b5ef-4676980edac7 | -2.7104 | -47.4147 | 2025-11-27 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| d4887271-96ba-3537-bc93-b61bf13e0362 | -2.692 | -47.3935 | 2025-11-27 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e34574f5-660e-3a6d-b23b-8de855cbc3b1 | -4.7018 | -46.4508 | 2025-11-27 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| d8905841-878b-398d-8db2-430f56fffcd1 | -4.7204 | -46.4497 | 2025-11-27 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 177.9 |
| c00b8965-7ccd-387a-a77b-a8dfba7e39ed | -3.5269 | -43.6828 | 2025-11-27 02:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 407c1a45-a757-3647-b3e7-fba50d31df78 | -3.5083 | -43.6837 | 2025-11-27 02:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| d9e31b83-654d-3430-a749-c892b155b424 | -4.7203 | -46.4719 | 2025-11-27 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 7f732d8d-4b69-32c0-ba70-eb308f0e9fdd | -3.5083 | -43.6837 | 2025-11-27 03:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 56f08729-59f5-331e-8285-6a0e40c3bbd6 | -2.7105 | -47.3929 | 2025-11-27 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 296a6900-d5c1-355a-bcd7-24768fb85f16 | -4.7204 | -46.4497 | 2025-11-27 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 162.2 |
| f865cb3a-8ece-3251-95ff-f8022efb71f5 | -3.5269 | -43.6828 | 2025-11-27 03:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| fe106c15-c921-35b2-8872-d468fb2a9f07 | -2.7104 | -47.4147 | 2025-11-27 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d0529487-9a62-3329-b579-717a49bd1ae6 | -4.7203 | -46.4719 | 2025-11-27 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 5bf2ac28-fde9-386d-a9c3-329c32f15dcf | -4.7204 | -46.4497 | 2025-11-27 03:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 97d6bf71-80ce-3667-99fb-2f3ac9e19908 | -3.5083 | -43.6837 | 2025-11-27 03:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 813c68d3-1719-3310-ad81-7c7416f888b8 | -3.5269 | -43.6828 | 2025-11-27 03:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 39ba522c-929e-3335-966e-0a7e29e7d0a9 | -4.7203 | -46.4719 | 2025-11-27 03:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 03570faf-6469-358c-a73d-ce9969342390 | -2.7104 | -47.4147 | 2025-11-27 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 39947ad0-1226-3494-acb9-6835beea9737 | -2.7105 | -47.3929 | 2025-11-27 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 8b85d201-b677-31bb-8820-f7ef4057c40f | -3.5083 | -43.6837 | 2025-11-27 03:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| f83dabd5-df6e-31e0-ade8-be663cbc1753 | -2.7105 | -47.3929 | 2025-11-27 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6ef01842-af1d-3066-a5cc-087f0d9b40fa | -4.7203 | -46.4719 | 2025-11-27 03:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 92.2 |
| da382665-e3c0-3704-a17b-69cd511367a4 | -20.408 | -57.9368 | 2025-11-27 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| afe9b4cd-5b49-35fe-9185-b799befb0ae8 | -4.7204 | -46.4497 | 2025-11-27 03:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 147.5 |
| e2139c44-5caa-3bd7-9cad-bd4658ab76d1 | -3.5269 | -43.6828 | 2025-11-27 03:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| d32647cc-7786-3e08-8a68-b4907952748c | -2.7104 | -47.4147 | 2025-11-27 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 35bc2272-2329-3412-b853-60f3a8a93b55 | -20.4076 | -57.9577 | 2025-11-27 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 8e7c4694-3ca7-3205-ba14-7dcc182565d7 | -20.408 | -57.9368 | 2025-11-27 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 172.4 |
| 51eebc83-0a51-3b47-b8a1-825323788c03 | -20.4076 | -57.9577 | 2025-11-27 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.9 |
| 7c42edda-47d3-339d-a43e-900083d8c4f9 | -20.3878 | -57.9396 | 2025-11-27 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| a8fe368f-3ece-353a-869e-ab3a13deb3ec | -4.7204 | -46.4497 | 2025-11-27 03:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 838c43ae-c739-3cf7-87de-52596ce984de | -4.7203 | -46.4719 | 2025-11-27 03:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| c9ab8db3-c8a4-30a1-8a68-d084b26c56ae | -2.7104 | -47.4147 | 2025-11-27 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b12ceb84-a751-311e-8a81-f8113fbcc0ee | -8.1633 | -43.2055 | 2025-11-27 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| 13adf5cb-3d80-3ccd-949b-821ed7567392 | -2.7105 | -47.3929 | 2025-11-27 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 4c2ca91b-da15-3dab-8325-d51ac56e9cd6 | -8.1636 | -43.1819 | 2025-11-27 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 8eb9e412-adb0-3507-af31-42f7bd5f19c8 | -3.5269 | -43.6828 | 2025-11-27 03:30:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| bce67204-4849-3292-b370-ae08e6516b6c | -28.3197 | -52.5112 | 2025-11-27 03:30:00 | GOES-19 | PASSO FUNDO | RIO GRANDE DO SUL | Brasil | 4314100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 63.6 |
| 6a1f046f-b13a-3f68-87e2-13d8b9328cc3 | -20.3874 | -57.9605 | 2025-11-27 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 22b5b10d-979d-33d1-bb9c-e275aeb8e63f | -3.5083 | -43.6837 | 2025-11-27 03:30:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 44f6e60c-2d66-3d81-baeb-82afd84dbc0a | -2.7105 | -47.3929 | 2025-11-27 03:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 380c7e94-218c-35f1-b31f-185e2aa2c630 | -2.3463 | -45.5917 | 2025-11-27 03:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| aa4a897b-a1e1-32cf-b3fa-bc85d0320148 | -3.5083 | -43.6837 | 2025-11-27 03:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 5717b415-bea6-3a39-8f82-3997bb1789ad | -4.7204 | -46.4497 | 2025-11-27 03:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 0dfdfd6e-9e68-3e7e-a775-961c1eca5c6f | -4.7203 | -46.4719 | 2025-11-27 03:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 016e00f7-c4b0-3cfb-9007-dc7a8bf9ee46 | -2.7104 | -47.4147 | 2025-11-27 03:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 0656adf0-8b9c-3667-bfd8-b2eb8171bf2d | -3.5269 | -43.6828 | 2025-11-27 03:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| e304db75-2dbe-320b-8513-9ee944ee836f | -2.7105 | -47.3929 | 2025-11-27 03:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a370b746-4cf9-3bd6-aa6f-526b98e2aa5b | -5.703 | -47.0532 | 2025-11-27 03:50:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 59f6d020-cd9b-386a-ba3c-9b094fc7731f | -2.7104 | -47.4147 | 2025-11-27 03:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 075592e9-6cf1-341f-adfb-5f6e1886f262 | -3.5268 | -43.7059 | 2025-11-27 03:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 67939759-fe73-3106-93f9-8ac4c5e3af45 | -4.7203 | -46.4719 | 2025-11-27 03:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 165fab8e-0803-30a6-8940-fc32ff116af9 | -3.5269 | -43.6828 | 2025-11-27 03:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| b7007e54-95bd-3d0b-93ab-cdcd2e2a1e39 | -2.3277 | -45.5922 | 2025-11-27 03:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 28a41b89-8c77-3c63-a87c-722c9acb861a | -4.7204 | -46.4497 | 2025-11-27 03:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 114.4 |
| a2ec8895-f2e3-3719-9311-36f4d1b0f0a9 | -2.3463 | -45.5917 | 2025-11-27 03:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2f8b81c1-d6df-360a-887b-e718dfaf6605 | -3.5083 | -43.6837 | 2025-11-27 03:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 0feece46-3737-3b1e-a400-6f9992afc59d | -2.7105 | -47.3929 | 2025-11-27 04:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 30e57c40-55d9-3860-bbce-081ea21a18e8 | -4.7203 | -46.4719 | 2025-11-27 04:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| c646d36f-e3aa-316a-998c-353b3f5d045d | -2.3277 | -45.5922 | 2025-11-27 04:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 54bd883b-17a3-3c69-ab13-9e69d2e49bcb | -3.5269 | -43.6828 | 2025-11-27 04:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 5792edb9-7a78-3676-9d96-2c01b9458ded | -3.5083 | -43.6837 | 2025-11-27 04:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 7830fea0-b9f3-3679-92a7-dfeff08f0305 | -2.7104 | -47.4147 | 2025-11-27 04:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d23bfe27-be99-38b2-a3ba-17cb36b0df97 | -4.7204 | -46.4497 | 2025-11-27 04:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 8a79dbf9-e087-31ce-a72f-e1e45fb5d1a7 | -2.3278 | -45.5698 | 2025-11-27 04:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |


[Clique aqui para ver as próximas entradas](README5.md)
