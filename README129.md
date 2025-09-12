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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d4d20c4-d5c8-3fc6-8901-2fa14a92ceca | -15.1406 | -50.1409 | 2025-09-12 13:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 659b489b-6678-3cfb-ad52-1816a964da29 | -7.5455 | -44.3856 | 2025-09-12 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ca0009ca-d49b-3897-8322-34ffd42253db | -8.4331 | -47.2527 | 2025-09-12 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 93e48f0f-f4cf-3bbf-bae0-c849ee033ea7 | -9.6727 | -47.568 | 2025-09-12 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| be375f49-276f-3968-9098-bae704797130 | -11.429 | -43.5307 | 2025-09-12 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| f3edd00f-a42d-3ba9-bb96-93905d2be173 | -10.8781 | -45.5826 | 2025-09-12 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 273.1 |
| 2f2d17a6-db78-3ac4-a605-7eb79cd9bb26 | -12.9292 | -54.7538 | 2025-09-12 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 6be80336-48c4-3ab6-bf10-f569d78b0c85 | -12.0852 | -47.5842 | 2025-09-12 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| dde33e0b-c3ae-3238-8e0e-fa49b085b36e | -16.9621 | -45.8176 | 2025-09-12 13:10:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 6cee8eeb-1b2d-3236-a6f0-82b8edc45d80 | -7.3212 | -49.6255 | 2025-09-12 13:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6faeb9d4-4ff0-3d20-83f1-4d9f9a390293 | -10.3504 | -50.5516 | 2025-09-12 13:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 9c0d2df4-4578-34ca-9a56-f3bf124e09ea | -16.4123 | -45.6728 | 2025-09-12 13:10:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 278a54d5-0df1-3cf8-b150-e4246b4bda0e | -7.542 | -44.6844 | 2025-09-12 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 11476a14-5eab-3b93-92cd-6bf6ce67e216 | -6.8184 | -45.6349 | 2025-09-12 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| ff1256e7-349a-34a9-b199-bf3414879c2f | -10.8972 | -45.58 | 2025-09-12 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 30db258c-121e-304b-97b3-a74b14c65eaf | -11.1149 | -51.3423 | 2025-09-12 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 16997cc2-3430-3696-93f2-1c692a2a3c95 | -9.0379 | -47.0597 | 2025-09-12 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 29e24c5c-28ee-36de-875f-66080b20f8ac | -10.0943 | -47.1664 | 2025-09-12 13:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 220.7 |
| b1c61d5c-24af-307b-bbb0-0cb23a16a60b | -10.6979 | -48.6612 | 2025-09-12 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| b8e39425-0d5d-3cc6-b0d2-8be7799ac3e4 | -6.1894 | -41.0641 | 2025-09-12 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 643f5b91-14e2-329f-8056-4bf65c741e10 | -9.673 | -47.5459 | 2025-09-12 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 193.9 |
| 67d4ce23-f0a0-3344-b449-a4d4ed7f992e | -8.3689 | -44.8305 | 2025-09-12 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| abb9f1ef-f5e1-3629-b2a1-9fb248e76109 | -8.9374 | -46.0869 | 2025-09-12 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| c069eea5-87d9-30fa-9c13-af5227f4df2f | -7.5643 | -44.3838 | 2025-09-12 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 6995e05c-b8ff-3843-b439-fefbdc72de7d | -12.0657 | -47.6091 | 2025-09-12 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| cec4d6c1-35ad-330c-b499-6b4f0a93e9fb | -15.5236 | -48.5332 | 2025-09-12 13:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| a8cf6aa8-626c-3069-b305-4a0b19bfae64 | -10.679 | -48.6633 | 2025-09-12 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8fee54b7-3e52-39f8-aac1-c63ef15f8edd | -12.6821 | -45.3209 | 2025-09-12 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 89dffeb2-0ff9-3363-a044-166ae13c2c70 | -8.9563 | -46.0849 | 2025-09-12 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 328.4 |
| c2d8ec5a-e160-3d6b-964a-13ff0bfb0943 | -12.9406 | -47.9768 | 2025-09-12 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| ad46270e-d4a8-38d7-8bb7-a3130c0c0de3 | -14.1717 | -46.1815 | 2025-09-12 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5b19f6fd-2803-3622-b628-65f9ce178cf7 | -14.2732 | -45.053 | 2025-09-12 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 44e75a9c-50b8-304f-8c4f-6aa80662c752 | -14.1907 | -46.2012 | 2025-09-12 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 56f14760-e562-3362-8337-278fc6ae761c | -11.4285 | -43.5544 | 2025-09-12 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 0472744d-70e8-3332-b5a6-646067cd2a66 | -9.057 | -47.0355 | 2025-09-12 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4c625310-fa43-347f-8116-60dfbf04e125 | -15.1313 | -56.3414 | 2025-09-12 13:10:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| f460dc6e-5b08-3791-bad6-d3f93eb9ea65 | -8.9371 | -46.1094 | 2025-09-12 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 393ff1e0-40ad-3c13-be64-e414093441e0 | -12.0849 | -47.6065 | 2025-09-12 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 505.3 |
| ebf5a88d-24e6-3480-bbb6-71572a58b00a | -8.1837 | -46.0965 | 2025-09-12 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 7d39ee4f-487d-36f7-b8c9-552ae1777f6e | -14.2727 | -45.0765 | 2025-09-12 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 7d519351-b458-3a66-b9d6-fa7929502047 | -6.1703 | -41.0901 | 2025-09-12 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 795.4 |
| fbb3be37-eb7b-37b0-af66-8e3ea03a7db5 | -8.8901 | -49.9236 | 2025-09-12 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 316bad82-4e64-348f-860b-94f6103bf277 | -11.6806 | -46.6536 | 2025-09-12 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 93a6b2fc-a753-3bfe-b4d8-af59312d604d | -10.3507 | -50.5303 | 2025-09-12 13:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 0bfdd4f9-0e34-34aa-a133-3e884fb3ee6d | -14.4588 | -47.3174 | 2025-09-12 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 2e814325-e149-3674-9025-178604ea64c2 | -6.309 | -42.2311 | 2025-09-12 13:10:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 588defa8-eb8b-3d55-9900-54c2ee778214 | -11.9713 | -51.164 | 2025-09-12 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2cc8cf10-b6fb-3039-b9d7-242a25b445ce | -14.2922 | -45.073 | 2025-09-12 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 301080af-8724-3bf3-9c18-d9fa83e67b62 | -9.77 | -46.0163 | 2025-09-12 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 5d63743e-9d57-3c80-bec0-d1404c9d8b29 | -10.6983 | -48.6393 | 2025-09-12 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 13af3b61-31ae-3295-98f8-e20ac108ee5d | -9.6919 | -47.5438 | 2025-09-12 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| dc026e03-8025-3722-a35a-5aacf644db4c | -10.6979 | -48.6612 | 2025-09-12 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 275.3 |
| 6475028d-0f8c-3d87-902f-54338107846f | -13.1835 | -51.7642 | 2025-09-12 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| bfec9d8e-674b-3f39-bedf-9732a2bff206 | -14.394 | -52.9245 | 2025-09-12 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 9a7e8fc4-1c88-393a-805b-bbbe5c62bea6 | -8.8768 | -51.111 | 2025-09-12 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| fef8fc99-53d4-3f34-a7d5-40ad91d21d7a | -8.4331 | -47.2527 | 2025-09-12 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 1900f1b9-b987-3632-8d8c-3030b1bfa2da | -14.1717 | -46.1815 | 2025-09-12 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 104.7 |
| f405efce-4eea-3e45-8e64-92204262bcd6 | -12.0849 | -47.6065 | 2025-09-12 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 411.8 |
| 85992049-8688-3693-bf91-e13b083a3d63 | -10.1216 | -47.9154 | 2025-09-12 13:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8614a8dd-f5a1-3b68-b67e-9d143735d276 | -10.1405 | -47.9133 | 2025-09-12 13:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 5344f677-36ed-3d59-98dd-ba9b009ed04e | -12.9292 | -54.7538 | 2025-09-12 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 135.6 |
| ac416363-4db8-3124-934c-8eeb8f078617 | -14.1492 | -45.4009 | 2025-09-12 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 65636d99-ef65-3ab5-800b-0137e14e44c7 | -8.8899 | -49.945 | 2025-09-12 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ba383bd9-edc3-3a59-9705-bfe1d339ec25 | -13.2027 | -51.7618 | 2025-09-12 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 6188cef2-f08a-3e64-9e4d-eb6e02c32a60 | -11.4863 | -49.2658 | 2025-09-12 13:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8d6df701-4e55-3afd-93df-9adac755f79a | -11.4398 | -48.5733 | 2025-09-12 13:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 247.3 |
| 1bb5fa1c-9b22-39a0-9102-2e1d70527acd | -13.1838 | -51.7429 | 2025-09-12 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 969ae5db-2e29-30f6-b910-eb45154ffbee | -8.9566 | -46.0623 | 2025-09-12 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 2c5a0231-6faf-39fb-ac07-39354aeaa4dc | -15.1402 | -50.1628 | 2025-09-12 13:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a67f56f1-5a4d-3ea3-8d5c-cb827fb29330 | -10.8781 | -45.5826 | 2025-09-12 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| a1cc055e-e887-3624-9347-1c457e2f4c71 | -6.3226 | -53.4553 | 2025-09-12 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 2e2e1cd6-af5b-30fb-a674-3c40a7c82c85 | -11.429 | -43.5307 | 2025-09-12 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| b8983ad4-2996-3373-b058-db88cc6aaa37 | -6.8184 | -45.6349 | 2025-09-12 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 66a6b352-5d66-3e7d-a846-f9452ee85bca | -11.1949 | -48.4277 | 2025-09-12 13:20:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| f19e7b4d-55ee-3cd7-9ed3-cbb4b1806480 | -8.9374 | -46.0869 | 2025-09-12 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 4adb8659-abcc-35c1-9ddf-7d54a4df9753 | -15.1363 | -52.4679 | 2025-09-12 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 0c10dfdf-ab06-39d0-8f23-09de0939d4f8 | -7.5452 | -44.4086 | 2025-09-12 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 8cd36635-9b02-34dd-bced-f4e77c59e65f | -14.2732 | -45.053 | 2025-09-12 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 1e9733f7-7dac-32c4-8a4a-915f4d17ebd6 | -6.3278 | -42.2294 | 2025-09-12 13:20:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 3e5e5b98-9659-376c-a70f-b3812ebd1a4e | -12.0657 | -47.6091 | 2025-09-12 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e8f5cc14-7ae8-34b7-bc48-41ba52318653 | -11.5422 | -50.6161 | 2025-09-12 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| ee59f8cb-501d-3147-908c-e54577397f5d | -9.057 | -47.0355 | 2025-09-12 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b44e4dc3-9e06-3a88-abaf-69769495c245 | -8.4705 | -47.2712 | 2025-09-12 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 664fc08a-7439-33f2-a162-0adf0b71befc | -14.2927 | -45.0495 | 2025-09-12 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 9ea25398-9fa0-3c8e-a762-9bd81f1d64d1 | -9.0376 | -47.0819 | 2025-09-12 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 9346f787-1d87-32e5-bd13-559aaf9d75c6 | -10.8785 | -45.5597 | 2025-09-12 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| f715e68e-4a73-3199-9b03-8cfb7681f5af | -15.5236 | -48.5332 | 2025-09-12 13:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| e206eba0-ca5a-3539-bb6d-c5b29946c38a | -6.309 | -42.2311 | 2025-09-12 13:20:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 800130c9-7ad6-3b05-8ae5-f1c0a626ab2e | -11.4285 | -43.5544 | 2025-09-12 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| c18f6f8c-fb2e-31f9-8be0-8522fce4b193 | -8.9087 | -49.9433 | 2025-09-12 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 643cc4b1-bbfa-3292-8cb7-fb49d48de8e9 | -9.6733 | -47.5238 | 2025-09-12 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 9d6505dc-c451-3b08-b381-eff6505d79c8 | -8.9563 | -46.0849 | 2025-09-12 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 235.3 |
| 07310381-68de-3ddc-9f11-740e7e85a5bd | -7.5643 | -44.3838 | 2025-09-12 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| f6bbe94e-e3ec-3ddb-a4f6-3f7df923a2fc | -8.8901 | -49.9236 | 2025-09-12 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 26ba8192-dce0-3fbf-9e26-d18306e6d984 | -9.77 | -46.0163 | 2025-09-12 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 194.0 |
| fc8288b9-c8cb-31e1-a045-22fcb1d7d36b | -12.9101 | -54.7558 | 2025-09-12 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 3482cfb7-8798-3be0-9887-aad22fbddb55 | -11.5425 | -50.5947 | 2025-09-12 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| adee5073-6790-3aab-abc4-f1c9429fc621 | -14.1907 | -46.2012 | 2025-09-12 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 143.1 |
| ffbccd31-102b-3e2f-9664-99f7753f3ff7 | -6.1891 | -41.0884 | 2025-09-12 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 212.6 |
| 897a1636-7457-3e8c-a4a1-dbe512378753 | -15.1313 | -56.3414 | 2025-09-12 13:20:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |


[Clique aqui para ver as próximas entradas](README130.md)
