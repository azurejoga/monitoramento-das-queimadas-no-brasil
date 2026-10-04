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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 933772aa-ac00-3acb-8015-d86ef940e89f | -3.1804 | -54.0658 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b672555-ee2a-3aac-87ec-3e7fa51d8060 | -6.896 | -43.683498 | 2026-10-04 00:09:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5cbe69fc-1b87-33ec-820b-a9ad9fe03f77 | -3.045 | -54.196098 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9409c8e-d25e-308d-85d3-0bceb5fb6c87 | -3.0372 | -54.206902 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80d86e70-d6ed-313a-9dc2-ee77f090f8fb | -4.2584 | -50.739899 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b06c7be-5666-31fe-8182-617e2d7e7eb9 | -2.8062 | -54.0933 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30452b4c-5804-349d-af48-fe96e28fb622 | 0.2025 | -51.114799 | 2026-10-04 00:09:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b4210e97-e230-3210-bf06-8006ff6469ba | -3.2924 | -49.113602 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ee43eb7-8d73-3152-a267-ec24f71e04bc | -4.9246 | -45.677601 | 2026-10-04 00:09:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7292e72f-fccb-3132-b32c-87bbcb333ab0 | -4.1159 | -49.062099 | 2026-10-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4da48818-b4df-3b11-ab32-ae5c74c90f00 | -3.1262 | -53.730301 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99516374-22de-3aea-9e3b-faf441581171 | -3.4059 | -50.3419 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7973bf5-02db-303e-a19e-5896c931bfe0 | 1.9203 | -55.757801 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0d87a04-cf43-3e81-8ee5-81e9739baccd | -2.9179 | -54.086899 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1681bd8c-4fee-33e7-9242-e8f1bf9de21a | -6.2057 | -52.783298 | 2026-10-04 00:09:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e21af95-f306-398f-a943-4ee5ac1790cc | -5.6313 | -50.017899 | 2026-10-04 00:09:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99123e9f-73f7-3419-bbd5-9e608d2426d8 | -15.9058 | -56.319698 | 2026-10-04 00:09:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ff6349c-b4e1-3337-a323-8bf573349e4d | -3.3013 | -53.824001 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24d1f65e-e42e-302c-a10c-1f15a0826940 | -2.5803 | -51.845402 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fa6fdcf-b984-3707-bfec-e48677c96179 | -3.8715 | -55.7962 | 2026-10-04 00:09:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87166406-5f15-30a5-9462-04a54dd4b23d | -6.233 | -53.141899 | 2026-10-04 00:09:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcfd7346-91d4-3636-a926-95ad039f0ec1 | -4.2511 | -46.371201 | 2026-10-04 00:09:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce27763d-13ee-3751-8214-e57e0ab6f622 | -4.2587 | -46.360001 | 2026-10-04 00:09:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dfffe76d-b924-3986-ad10-e7016156d659 | -1.4793 | -49.437099 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78aa527c-171e-351f-a5ce-64edf45236e4 | -1.4078 | -49.258499 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 301a51e2-5782-3016-9c01-de9aab681eda | 1.9224 | -55.7486 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72625c85-1458-3049-8384-91aafb4851c2 | -6.7029 | -45.963501 | 2026-10-04 00:09:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 892aad4a-ba44-3fd8-823f-64511c52b317 | -2.9041 | -54.117199 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7452c2e9-0930-3782-9f3d-f6ee31bbf0b0 | -13.3671 | -41.3209 | 2026-10-04 00:09:00 | METOP-B | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0762313e-ce7e-3001-aeed-263e95fb4f06 | -15.2434 | -40.5154 | 2026-10-04 00:09:00 | METOP-B | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6cec1df-d0b3-36e4-93b4-dbd03a7042c7 | -2.7885 | -54.106201 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2123da7a-da79-3430-a697-5e4635da55b3 | -1.6118 | -55.003399 | 2026-10-04 00:09:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d95e62a-781d-3ea1-9575-7a6d7697d22e | -2.7495 | -51.5443 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbc000c6-e079-3a24-9aa2-c0dd643b6c68 | -9.5756 | -48.631599 | 2026-10-04 00:09:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 851e6269-2306-348f-8571-51186b6a37bc | -3.0096 | -50.458599 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 807684e7-e6c3-3b99-ac8e-91b43a89fc7f | -2.0452 | -56.847401 | 2026-10-04 00:09:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f31b6d5-d2f5-321e-a170-21ce86041bbe | -3.0568 | -54.1567 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef17a376-8b3e-3612-a6d7-689211a8d311 | -7.0111 | -47.515999 | 2026-10-04 00:09:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 759c769e-d4f4-30ee-9f78-ee5e5a293081 | -6.0088 | -53.524502 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81df351a-0604-30b8-88f1-895d57bc9cdc | -2.2451 | -51.912102 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2971415a-83fa-347c-98eb-ff4987081b55 | -3.4728 | -50.090801 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e841fe21-2e33-320d-a0f8-5f70a5775f7c | -2.8179 | -54.099701 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd80974-f135-3018-979d-3a87d7e7a09a | -2.8864 | -54.130001 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a7b686c-149c-3b7a-a5c0-ee3331d25f8e | -7.745 | -49.198502 | 2026-10-04 00:09:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 99df119a-6a33-3485-a64e-d4fa15a99d5b | -2.5753 | -51.868599 | 2026-10-04 00:09:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05218c06-d13f-3f4a-a964-5c6112d9260e | -3.1183 | -53.740799 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeb7f79c-5fbc-3b4c-aa4b-a539775b64db | -2.5886 | -51.836201 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b53b3d27-38ab-30fa-b0fd-119c3f0045d9 | -2.748 | -51.537399 | 2026-10-04 00:09:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5129a909-5743-3685-afc7-83b7c4f0002c | -5.547 | -44.205002 | 2026-10-04 00:09:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69f7a7f7-da3f-35e8-97cb-99cf3dc661e2 | -7.4751 | -47.6049 | 2026-10-04 00:09:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2fa2ab4-2b51-3c35-9c55-c4ef2cc09f2e | -3.3585 | -43.386002 | 2026-10-04 00:09:00 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24b96024-6b31-3945-8d3d-3963f1cb4123 | 2.1017 | -50.739101 | 2026-10-04 00:09:00 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 549b0281-1e47-3606-8dfd-28de43daf2d0 | 3.4285 | -51.300701 | 2026-10-04 00:09:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1d553924-22c3-3883-af84-61f67dd5869e | -6.5731 | -44.144299 | 2026-10-04 00:09:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f93e7f82-cf1b-3e91-8026-eb833356136e | -3.0924 | -51.0993 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a262c50a-d6aa-3e54-90d9-2487b7777e63 | -3.8968 | -49.687 | 2026-10-04 00:09:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81b6124b-3114-3a35-aa8d-9c40c24f20b2 | -1.411 | -49.2728 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f526c16f-2dca-36d8-9423-b0ddccb365c2 | -5.6329 | -50.0247 | 2026-10-04 00:09:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9d6ceb6-cd63-3904-b9e5-1412feac3066 | -2.8277 | -54.097599 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bc4be30-e3c2-3b0a-ab3b-97f54b0e2b49 | -4.9784 | -46.041401 | 2026-10-04 00:09:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76530d25-ba03-37f9-8115-324f95cf3240 | -14.5652 | -52.8601 | 2026-10-04 00:09:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d76a20b-b2e3-3949-afe0-462e87eb3a13 | -3.1145 | -53.724201 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab69631-f139-38ff-9344-3571afa0e632 | -4.1955 | -53.453201 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd4e8f90-aa81-33db-938e-6970eacaf516 | -4.5113 | -45.893902 | 2026-10-04 00:09:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 19d603b1-fdfa-3c13-b95e-04bea03d417a | -6.2075 | -52.791401 | 2026-10-04 00:09:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec9d7ade-7471-3983-85e0-04f1aa5fe1c8 | 0.4179 | -51.119801 | 2026-10-04 00:09:00 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| cff70506-2794-30ae-8370-dc686a504893 | -3.0709 | -49.545399 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01f66933-23c1-3dc2-8ba4-79a29ae0122d | -8.5364 | -50.0639 | 2026-10-04 00:09:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23e8160a-65fe-399b-a9ec-40e4e9bb789a | -6.8931 | -43.671398 | 2026-10-04 00:09:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d9666625-bca7-33a9-9ae9-beff832b45bb | -2.9197 | -54.140999 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76c40d84-f002-30ba-bf82-08a5ad28de25 | -3.8886 | -49.695999 | 2026-10-04 00:09:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7a6e884-8fc7-3e5f-9fd3-78d6c48abc1f | -3.047 | -54.2048 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3e09e3f-ea1b-3bd2-bce0-08775c7d2064 | -3.6108 | -55.497002 | 2026-10-04 00:09:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7281b8a-dbee-37b6-9a3b-5448aa50e8ee | -2.5851 | -51.866501 | 2026-10-04 00:09:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 729005de-a859-3cd4-b55c-fe9a7063a6f0 | -3.1324 | -53.711601 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13681003-5b6a-3e19-baeb-c498691d5411 | -2.9855 | -51.036701 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a104add0-1b0a-3017-8a19-de6fcfc073cd | -5.1883 | -45.483101 | 2026-10-04 00:09:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4a27940-d280-36de-804c-f8d024612da9 | -8.5145 | -48.908798 | 2026-10-04 00:09:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 122afa65-9dec-39d1-9343-0a2430782b02 | -7.8912 | -45.311798 | 2026-10-04 00:09:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f12b5b38-6890-309c-bb28-d13ffb096229 | -4.4545 | -50.970798 | 2026-10-04 00:09:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 031b3c51-40c2-3d2b-baaa-2d64314cb1dd | -6.0777 | -53.463699 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5391491c-6857-39a0-9ee2-20ea927b098b | -8.5227 | -48.8997 | 2026-10-04 00:09:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4fe71233-cda2-38c8-baa8-8a9bf0444507 | -7.4734 | -47.5975 | 2026-10-04 00:09:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 290f3f34-51a7-30d6-964d-92f9ede40930 | -3.294 | -49.120602 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 903ee31e-6c7d-34e5-a38e-c4cdb8b51480 | -1.1205 | -54.144699 | 2026-10-04 00:09:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cbf3f00-a59d-3ffb-812e-8047f6ba3a9f | -3.0391 | -54.215698 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf4d7565-c81d-3854-9594-9cc5e76fb0d3 | -3.1127 | -53.7159 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 466a1e36-89c4-31f4-9a92-da2ca85d68b9 | -4.1075 | -53.612598 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88dbcc2d-1088-3a68-a61f-c5bad2721cdc | 1.7651 | -55.626099 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b99077b2-aeef-3a0b-96c3-521e6170fb37 | -3.278 | -53.811401 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 036589af-7afe-3f15-8ff1-608bf12d4ebf | -4.8048 | -49.2808 | 2026-10-04 00:09:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df62e69a-e137-39b4-bcfc-38b54bf72b32 | -2.5768 | -51.875702 | 2026-10-04 00:09:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca61238a-8bf6-3414-8710-9390b1ba8d8a | -2.2486 | -51.881901 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 918f0978-34aa-35b6-b97d-5e4aebe4a7e1 | 2.0951 | -50.723099 | 2026-10-04 00:09:00 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c85448ea-8b08-3393-95ac-975385707773 | -2.2655 | -54.801498 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5b4a058-133e-36a2-86ef-74e09277cc43 | -2.5917 | -51.850201 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31e8fccd-7bbd-3116-bba2-b419117c98a3 | -6.0796 | -53.472401 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 034fa73e-1522-3575-975f-1dd3d4bb8d77 | -6.4611 | -49.9044 | 2026-10-04 00:09:00 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7903a0fa-1aa1-3e17-a9d0-9657e0582261 | 1.9147 | -55.737099 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a62836f-b112-3dde-b7ee-7534d671ca31 | -2.9688 | -54.084801 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
