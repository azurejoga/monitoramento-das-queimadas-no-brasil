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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0982e92f-2af6-3ac7-8a8f-34c13f2187a2 | -5.93845 | -43.64629 | 2026-10-03 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cbd9e7e1-4340-35e5-8290-d0a5ed8bd3e9 | -6.45543 | -55.47929 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db91cb61-1021-3114-9516-81070845b8e9 | -5.88657 | -57.67306 | 2026-10-03 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e301a323-cbc6-3f26-9d1a-b24ee88a2b48 | -4.29958 | -50.77622 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1994e5c-fec5-31e8-bd30-41e986463b06 | -3.57535 | -54.35255 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| add4d083-c460-3b18-8e47-28e667167c42 | -2.8935 | -54.10978 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abb7e1d7-e26f-3e65-a30c-a843ba0eec34 | -2.95371 | -54.09765 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c97b583-3e15-3cdd-a17f-911b4866bb83 | -2.89243 | -54.13829 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2663050c-2c7e-345f-b462-bf5b9274d340 | -3.50384 | -53.20447 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 572f3910-f8a2-3457-8675-b048d48c5b04 | -5.62001 | -44.37753 | 2026-10-03 05:16:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb071371-5e39-314e-9e5d-3269ff131121 | -2.73979 | -49.46195 | 2026-10-03 05:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18ce674c-0f57-372c-a425-3787e3c9fd8b | -5.9492 | -43.6637 | 2026-10-03 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| debc7d11-74ad-300f-9dad-d64465d47635 | -3.05364 | -54.16323 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a46c925-3261-3677-8720-de76834c943e | -6.21215 | -53.26617 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8adb80b-c15a-3e8b-a5d2-67a83c2ea1d6 | -3.09683 | -51.10122 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc7a066d-1292-354b-841b-7d1945aeffd5 | -3.01303 | -53.88697 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ceabeed-9d32-3cda-825b-0e11b856a7bd | -4.30034 | -50.77127 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6b0add1-7233-338b-a08a-6ffd632aac30 | -2.89801 | -54.14632 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32411bca-f3a6-35a9-ac61-1eb331345ce1 | -3.70726 | -50.65573 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ab6ee87-da3c-3723-9be0-10f0eb719c66 | -6.9262 | -49.62273 | 2026-10-03 05:16:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a00816c9-d972-3a6c-a6f9-c73eb2b76946 | -6.0265 | -57.69545 | 2026-10-03 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7136250-44b6-314d-8f05-8fcde3717135 | -3.29094 | -53.84699 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90d45773-dda1-3d24-a48e-cfaca794a583 | -6.84189 | -59.26224 | 2026-10-03 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ed4045f-0561-3cac-9b96-f8f6eac91236 | -3.17874 | -54.10067 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24b93644-5eea-3e4d-b40f-3a334083d8dc | -4.45399 | -47.92872 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 45215aaa-583e-3da9-9659-5066339a79e0 | -3.71509 | -50.6569 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9da565e9-390c-3e71-929e-c11e6b70e977 | -4.26026 | -50.74493 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2c8aa0a-7533-3ab1-95ab-62ddb43c988e | -2.93368 | -54.15906 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2dfa11c5-8931-3a7d-9d54-cf6b0b1ef2a9 | -5.61454 | -44.37766 | 2026-10-03 05:16:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aefd7ce2-2365-369e-abf8-59452ca7e088 | -2.9281 | -54.15102 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afeb0483-2782-31b3-8ee9-508cf1ed9240 | -3.85015 | -55.96447 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8652af02-654c-3105-a9e8-28a460471b1a | -2.49284 | -48.52633 | 2026-10-03 05:16:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb5abc51-970d-3bd4-ba1d-4e82e646035f | -4.7897 | -55.72024 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 516da97d-8c80-334a-b883-3a9442f53fe1 | -5.61386 | -44.38231 | 2026-10-03 05:16:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8c56b556-5c4d-3ac4-be80-057331aac40e | -3.84794 | -55.96737 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7e53774-5330-3408-ad0f-7cffd6b3c968 | -6.3464 | -51.70032 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe9ba002-6b15-391d-be31-35e01f5dc9e9 | -2.15004 | -59.23118 | 2026-10-03 05:16:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c671987b-4e1c-344d-8d3f-c82edde72ee5 | -3.169 | -54.08427 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4932924-1bb0-37f8-a05e-6d0871b1232b | -5.89467 | -55.49376 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52d1e777-d8a1-3936-9f37-40af0d21f970 | -3.2943 | -53.84752 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce617cc2-ee4c-3857-93e8-dcb4c739ac3d | -4.79081 | -55.71329 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e638a089-71fa-3c26-a8e8-7c749c9a0742 | -2.9169 | -54.0919 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59a38099-f952-3e04-8585-00c6ddf19df7 | -4.30344 | -54.79828 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa09530e-1bc2-3cb6-98db-92d59adc505c | -2.97715 | -53.2672 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5aed3c5-763c-3eaf-8e03-292d7a798b5a | -3.02012 | -54.23342 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a8498ab-f431-3f7b-b644-887e89f41113 | -2.88908 | -54.13777 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab3daee8-e344-3e31-9178-ac95aadfe0a4 | -2.60572 | -48.25516 | 2026-10-03 05:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d95ad76-85d2-3333-b2a4-167a0e3eb5bf | -2.17882 | -49.77212 | 2026-10-03 05:16:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c202055-70a7-3631-8aa9-827fc1ee7be2 | -3.17402 | -54.07424 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a46f948-74d8-3e85-81e7-dbdf8ffb7026 | -3.13291 | -53.74538 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d08350e9-196a-3973-be1a-375282f6bdcc | -3.85572 | -55.97254 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9431c3a3-7ba4-3a90-980b-4d5351f8cdb3 | -4.455 | -47.92245 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 49e10c21-288c-3a6b-9f49-2a95ec963b5f | -3.094 | -51.09792 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c34ed661-c06d-3853-bf36-d3c31567ca90 | -3.11789 | -53.74706 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2a963d6-6fb6-3e21-a9e4-d95e3b7bfbaf | -2.04924 | -54.48636 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d32d3bf5-0082-3243-9701-794dee9f4b54 | -4.11373 | -54.41162 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dffe023-1e52-3c48-a45a-711791bfaeb6 | -4.99265 | -56.14865 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1ecd716-32e4-3c44-a663-fa680d7045b7 | -4.42339 | -55.75116 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e03cc03a-3aed-3968-a7e2-d81cec907520 | -3.53239 | -55.5211 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5a825e4-aec1-3a27-a80c-0757a6056014 | -2.86819 | -50.32163 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86a20f9f-9836-387e-a42b-357cd013ddfd | -3.35252 | -43.3866 | 2026-10-03 05:16:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 511f9e7f-7345-3dfb-83f5-c0d8fbc9f5e0 | -4.42982 | -55.74863 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b2c3f1c-6aae-3e99-9b10-96697868ed75 | -2.97464 | -53.26379 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c0b56b1-a0ab-3099-8279-270b40aca943 | -2.94981 | -54.10063 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3030bfcc-7b84-3d3c-b581-c97a936b3fb1 | -2.44166 | -54.82768 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31603d3e-0257-34fa-baf8-0348010cfc23 | -3.09706 | -51.10303 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdc07599-2905-3d96-a94c-4a96da1ecc0f | -3.18489 | -54.1052 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2182a6ab-1fee-3046-a0ce-f83d9ae73f5a | -4.42649 | -55.7481 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4edeef8b-af25-330f-8749-7b75f7d5fb10 | -3.9154 | -54.42672 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88a3bd2b-7f24-3c63-ba11-2f855f665e25 | -2.1568 | -55.21526 | 2026-10-03 05:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19a6dccd-c728-35f8-a7b9-4b338b3fcd7b | -2.98057 | -53.26772 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc0309d6-1089-3f08-88eb-06164479d17a | -5.88802 | -55.4927 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baf15146-7929-35e4-a94f-e8787ed17824 | -2.95585 | -54.09797 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3391c8ce-eb94-35d6-b10f-ababb471f2b3 | -3.10389 | -51.28175 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cc619b6-3089-3846-872c-f29139565ebd | -5.94346 | -43.65767 | 2026-10-03 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 6d7ae681-6a52-3189-9781-568ec9246324 | -4.78859 | -55.70583 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9a76dcb-4ba0-39e7-bbf8-3833d17aa858 | -3.18599 | -54.09817 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98eaec3d-2a48-3b75-bb7f-881c89e8e59d | -3.07629 | -54.36691 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f6c0804-782d-3a87-b971-0be11434e79c | -2.96477 | -50.31777 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dac2ae3-56d0-3d00-935b-18dc105dbfe9 | -6.07534 | -57.79994 | 2026-10-03 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79781e50-1c02-3405-98ac-1f4a11787724 | -4.56863 | -46.58314 | 2026-10-03 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ceff890d-f498-3935-92e3-b0b0e3f35397 | -5.85248 | -53.4678 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a08e6be-6aba-3bf5-99f4-87dc2e59b517 | -3.28364 | -53.82763 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 205f453a-7e0a-3348-a4d0-dfbc8c6f0160 | -2.8924 | -54.11678 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77b0e10e-87b9-3a43-9168-9854d0148fc8 | -6.01582 | -53.53426 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e69859f6-fc73-36c4-b80a-bce04e89b228 | -3.28645 | -53.83173 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3a2996fb-74fe-3df9-9acd-56d084559f2b | -3.41937 | -48.33523 | 2026-10-03 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a38e5f7a-af4c-3258-9149-c153fa148a42 | -5.8969 | -55.50122 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25e44124-3775-3c97-a0fe-778010740fe0 | -3.21159 | -50.91138 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37eaaa5e-ef7b-38bd-a360-bc7ac2cd6452 | -2.89019 | -54.13077 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b839a63e-8d40-3848-b12f-3c44cf8e1cce | -4.40741 | -49.96194 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d3506f6-c053-3753-954e-26f7dc99cfa5 | -2.02352 | -54.30865 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e293d20-1c7c-3aaf-b342-f24c0d1f5887 | -3.58792 | -54.53307 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b4889305-55f3-3163-bfd8-9db1d68e8fa5 | -2.64627 | -54.2394 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 249b8895-74ac-3bad-a062-d99cc86c873f | -1.22005 | -54.53304 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9eccd63-56b2-359b-a4a7-c7a6c9f9baa5 | -5.71767 | -46.19984 | 2026-10-03 05:16:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77e46e54-0613-3303-8936-0e05fe4874d5 | -3.00461 | -53.87478 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17a28d33-44d9-32d6-806c-da1ca33b9c65 | -1.64018 | -55.1445 | 2026-10-03 05:16:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc63a4cd-682f-360c-8af3-eadac5654a4b | -6.01752 | -53.54619 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 212549a0-3f3a-3c85-9317-c539f58dc823 | -6.21839 | -60.02791 | 2026-10-03 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README37.md)
