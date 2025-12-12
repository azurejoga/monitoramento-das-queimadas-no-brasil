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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8734b336-4a6b-36cd-ae4a-1b1dac54a441 | -4.65845 | -42.39811 | 2025-12-12 03:57:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ee0f55a1-169f-381f-a9ae-a76733a28f95 | -3.23669 | -42.07579 | 2025-12-12 03:57:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e67b9a01-cb95-3cc4-a33a-2d47a3b19601 | -4.73627 | -43.07303 | 2025-12-12 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d53484e-cfb1-339c-80fb-932a9b2f0dcb | -2.21791 | -45.40561 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 373d4c33-db8c-31ed-84ce-2aad0402c78d | -4.16168 | -39.25087 | 2025-12-12 03:57:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0729da6f-84e8-3397-b9e6-18305c7c3f16 | -4.81016 | -44.48057 | 2025-12-12 03:57:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 70443340-3884-3429-9849-2d9382a85223 | -2.29453 | -45.59071 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c37ed522-62f5-3ce8-b7df-1fe5b538d7dc | -3.49651 | -44.89301 | 2025-12-12 03:57:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cbe3f962-bade-344f-87ee-7cf743497ddd | -4.63499 | -44.40127 | 2025-12-12 03:57:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3cc81864-6946-3536-8ee8-81cc943fed1a | -1.79612 | -45.76399 | 2025-12-12 03:57:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5d4af1c-b42b-355c-ae55-62190f799248 | -3.85991 | -45.30446 | 2025-12-12 03:57:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62e5d401-5b51-3c66-8d99-33af01c84018 | -3.22894 | -42.07446 | 2025-12-12 03:57:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 30cbb62e-cddb-3f55-bbb9-1502e870a182 | -2.22805 | -45.40101 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22725d6f-af8c-37a2-9853-901961510dc5 | -4.77024 | -43.60223 | 2025-12-12 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa8325a8-98a2-3ced-a2e0-45146613a7f0 | -2.29429 | -45.59197 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c18df1c6-197f-388f-a378-ded7f5651e43 | -2.82559 | -45.2593 | 2025-12-12 03:57:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad840fdd-766a-3791-b023-2315933f153b | -5.15888 | -37.70077 | 2025-12-12 03:57:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6db2b894-90c9-31a0-99fa-96a0bb2a4674 | -3.24562 | -43.28868 | 2025-12-12 03:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 368155af-cb97-37ff-a235-bafdf996f202 | -4.99728 | -38.05777 | 2025-12-12 03:57:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b51c8ea4-bf70-337b-b1a9-a8fbad325339 | -4.30657 | -43.21315 | 2025-12-12 03:57:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e13c7c4a-e739-3f59-8815-dd8275d17234 | -3.38319 | -47.19125 | 2025-12-12 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01c3f327-3f2f-3672-86d0-22a03101def8 | -3.23202 | -42.07995 | 2025-12-12 03:57:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d2ffb819-059a-3fe4-80fc-9ad31ce8c068 | -4.10945 | -47.30125 | 2025-12-12 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 87b50eac-9fe9-3296-aaff-6096a1ada5f0 | -2.22869 | -45.40174 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2eae4251-e660-3982-9858-dbfa2b7585af | -3.65521 | -47.15534 | 2025-12-12 03:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7098437-6a66-32dc-a073-7347af5de559 | -2.48326 | -47.77533 | 2025-12-12 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c245db8a-7663-3e3f-a3cb-0292c9a92b03 | -3.96115 | -41.5216 | 2025-12-12 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a161fdb9-b824-3184-aee0-5ae48cbee7ae | -3.24143 | -43.28796 | 2025-12-12 03:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ef012dc-ec29-3d31-96e3-1f50bb196b3e | -2.23298 | -45.40187 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7333914b-efd2-368a-bcf5-5b7fd4def84f | -4.45508 | -43.70563 | 2025-12-12 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d278bcf6-9d99-31dc-be6b-6eab39621880 | -3.23244 | -41.79997 | 2025-12-12 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e933e7d3-b788-3181-8b7c-844aa6badbc8 | -2.53824 | -47.80073 | 2025-12-12 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| d8afa26b-b94f-3880-b4cd-a563d39b2257 | -2.36667 | -47.68692 | 2025-12-12 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aabb9e3b-07a0-3af4-b178-de9c9b462f9a | -4.69181 | -43.24226 | 2025-12-12 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 455fe410-ba95-3bd6-ae65-01a2a62328d7 | -3.23484 | -47.46987 | 2025-12-12 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8df41d62-8889-3a69-a5e1-4ce33bfe9d8b | -4.38855 | -46.67139 | 2025-12-12 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ad4ca11-c762-3813-8f14-32aa49385e28 | -3.77236 | -47.16425 | 2025-12-12 03:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d48edd6-97ac-379f-99e6-0f1234c62c3a | -1.84743 | -46.39731 | 2025-12-12 03:57:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 801bc984-afe5-3fd2-9f1d-ee2f383a6cae | -2.69623 | -45.69877 | 2025-12-12 03:57:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a8ea4e59-4134-3136-bdbd-b3ff568a8e28 | -2.47058 | -48.06285 | 2025-12-12 03:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 661a378c-5f54-3748-aa14-8dc7d8bdcfa8 | -4.38576 | -43.63104 | 2025-12-12 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b2aead7-00ec-34c7-8093-3bdd910f9d68 | -3.24498 | -43.2925 | 2025-12-12 03:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1f1d06a-dc5e-38bb-8c57-664ae5225808 | -3.81377 | -47.05224 | 2025-12-12 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff8fd8f1-5ad6-3911-b878-8f84aebb1027 | -3.6593 | -40.90065 | 2025-12-12 03:57:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4255f1d9-be5c-374c-9518-51da987ea83e | -6.84169 | -35.04517 | 2025-12-12 03:57:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ac6a3c37-6d2d-3a2f-9ed6-6dcf12c8f39f | -2.43585 | -47.19415 | 2025-12-12 03:57:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e131481a-210a-3baa-bfa7-e1fe6963e38e | -2.69631 | -45.69767 | 2025-12-12 03:57:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7cd2ccd-230e-39c8-95b4-dc8206c9a930 | -3.39631 | -42.10372 | 2025-12-12 03:57:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| aa510042-4418-3fac-a2da-044645d0b9fa | -6.25561 | -35.37511 | 2025-12-12 03:57:00 | NPP-375D | PASSAGEM | RIO GRANDE DO NORTE | Brasil | 2409209 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 224a9075-ff9a-3554-a1c9-6eff74037014 | -4.73165 | -43.07588 | 2025-12-12 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a12ac5a4-e61f-3964-afb2-7a40584c98fc | -3.44182 | -41.64904 | 2025-12-12 03:57:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3062e305-e3d1-3467-8998-a93400df86f2 | -3.76695 | -47.16329 | 2025-12-12 03:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf010b88-5b10-373f-a2a2-0d29a4b6c924 | -4.16225 | -39.24728 | 2025-12-12 03:57:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 98dbe984-3c2f-340e-a8b7-c184fc45a3b2 | -3.97549 | -42.50929 | 2025-12-12 03:57:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 61d2f48b-50c0-39c6-91dd-658372193f74 | -3.85716 | -40.66359 | 2025-12-12 03:57:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c5a63a4e-c6e6-3d17-baf5-071cc9ac5101 | -3.96042 | -41.52604 | 2025-12-12 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7190e19d-d95e-39d5-b2aa-0eff6d5225ca | -2.29524 | -45.5863 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2971199-471c-37a0-9036-ffe914a29cac | -6.12243 | -38.34951 | 2025-12-12 03:57:00 | NPP-375D | DOUTOR SEVERIANO | RIO GRANDE DO NORTE | Brasil | 2403202 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 178e730d-e72d-3b0c-bda5-e1f660aef9fc | -2.34028 | -45.7814 | 2025-12-12 03:57:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5148f08-4c0f-308c-b647-95545e0d9736 | -3.65415 | -47.15577 | 2025-12-12 03:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc8351dd-1aac-36c2-9218-3b8872dd30b2 | -3.23281 | -42.07512 | 2025-12-12 03:57:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ba55db2e-d29d-30eb-a2e2-f38898f3c850 | -2.83859 | -46.73566 | 2025-12-12 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1a9155c-b62f-307b-87c4-552d918d75b5 | -3.60447 | -45.52226 | 2025-12-12 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6c0e4b9-dd10-3c2e-9f1b-16e16a48a356 | -3.1429 | -39.57301 | 2025-12-12 03:57:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4d53519a-31d8-37e1-9077-bac98704165d | -3.95297 | -41.52487 | 2025-12-12 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 548799dc-b8b8-3f33-aadd-3e5c4cd04001 | -3.23425 | -47.47342 | 2025-12-12 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 610932cf-efe6-325d-ad73-7f88b2e17ec2 | -1.55318 | -45.80931 | 2025-12-12 03:57:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3ffc66e-f6bb-3e89-ade8-9f3bcdfb1f1c | -5.89216 | -38.17799 | 2025-12-12 03:57:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3374400b-7063-309f-a5e9-ba3225bc96ac | -1.66606 | -46.23174 | 2025-12-12 03:57:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a1525f6-36d1-3b60-993d-6377f36250fd | -4.46232 | -38.2501 | 2025-12-12 03:57:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4eec6a19-0ef1-3d8d-a934-e0654d4b3778 | -4.11004 | -47.29781 | 2025-12-12 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d53cc5f-5178-3a63-a6e0-cc328170c172 | -3.93593 | -40.73272 | 2025-12-12 03:57:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9c91928e-db79-337e-bd77-a20a6ff0c1c5 | -5.92949 | -38.35058 | 2025-12-12 03:57:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47693c03-48c4-38b2-a358-64f4d8c207d6 | -4.30248 | -43.21243 | 2025-12-12 03:57:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7695c771-b67a-3caf-a06e-52b70c25a011 | -3.62942 | -45.39222 | 2025-12-12 03:57:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fba6406-a60b-396f-a47c-f1c2b0b04ae0 | -2.69538 | -45.7034 | 2025-12-12 03:57:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 70faa8f7-c83e-3f7b-a0a2-25b6bcba5181 | -3.2336 | -42.07031 | 2025-12-12 03:57:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 010a46ba-4014-31c4-92f2-f5834674a040 | -2.70121 | -45.69966 | 2025-12-12 03:57:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1ee42bc9-4628-3e35-a1ed-5a5febc74e27 | -4.30438 | -43.21591 | 2025-12-12 03:57:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a02b9551-6f9c-34b3-b232-20eaffd93243 | -4.3891 | -46.6682 | 2025-12-12 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7530f8fd-c8dc-3507-8d27-a6d46222fa6f | -3.30395 | -42.52791 | 2025-12-12 03:57:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c762398-834b-31ee-a11a-3e7b1707c5f6 | -4.93549 | -43.96491 | 2025-12-12 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e00d41e0-71a6-320d-ad3b-58f7f370ba99 | -3.02586 | -49.05325 | 2025-12-12 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3a010df-b556-373e-9bbb-fd5099498c67 | -3.8258 | -42.17513 | 2025-12-12 03:57:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eee4ce94-afb0-3fef-bb1f-cc3b43347fdd | -3.81712 | -45.67455 | 2025-12-12 03:57:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67ae2ecf-7662-3b29-b117-b34e55c7f960 | -4.38511 | -43.63496 | 2025-12-12 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdcfdf78-9060-328a-a6c2-65f6e0fba158 | -3.43805 | -41.64843 | 2025-12-12 03:57:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 35a2c70b-9989-3221-9fca-61b3cdf0ca8c | -3.62461 | -45.39138 | 2025-12-12 03:57:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7433dc51-c5f6-3650-9ab1-a150094f9886 | -1.7966 | -45.76104 | 2025-12-12 03:57:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db2c18b7-e0cb-3761-b2d0-c132e40a75ac | -1.31715 | -46.53207 | 2025-12-12 03:57:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cfd7dec-c497-3155-942f-7b720d0c75ac | -3.27139 | -45.56097 | 2025-12-12 03:57:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6755f48d-65ab-39a1-9518-0bb203cc2c35 | -3.96414 | -41.52663 | 2025-12-12 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ab42f413-051d-3268-a001-a09ba6db2b49 | -2.29928 | -45.59276 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35c27604-2ed3-348f-bf9f-d021273cb69a | -5.67856 | -39.53747 | 2025-12-12 03:57:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bedde41a-8cbd-3f7b-b591-d1284867bf6c | -3.38378 | -47.18777 | 2025-12-12 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b2003bf-1343-3120-afbb-083940c1166c | -2.2321 | -45.40741 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 614abc53-7cfc-3bb8-adc7-61911caf17bb | -4.79826 | -42.14794 | 2025-12-12 03:57:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7836eeea-b178-3ff2-8ae0-c85311721d33 | -3.65579 | -47.15194 | 2025-12-12 03:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f0130ab-90e5-3af0-8709-f2998f69f51b | -2.29953 | -45.59151 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9ecf542-358b-33b7-87b9-e701ed1e452f | -6.46972 | -35.1657 | 2025-12-12 03:57:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README12.md)
