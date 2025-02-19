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
| 92c05b91-ae50-3ade-b825-9a5f3bfb8aa1 | -15.81463 | -42.11409 | 2025-02-19 04:48:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c6a5842-5eee-3d4e-b505-9803fcc1c1d5 | -15.81416 | -42.11871 | 2025-02-19 04:48:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 499e51a5-d80a-3378-a6ff-302eec962fbc | -18.33256 | -54.4308 | 2025-02-19 04:50:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ab7be1c-c5c8-3b0d-a4f9-581f26da44a0 | -20.21909 | -46.48591 | 2025-02-19 04:50:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0a7d4ad6-9240-312a-9935-aeca49811eb8 | -20.22332 | -46.48746 | 2025-02-19 04:50:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 140f659d-cd5f-32e6-af2c-716c8ab09e4f | -20.29788 | -46.51681 | 2025-02-19 04:50:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92884dc8-007f-3203-8205-cdbbb0c4e3e9 | -18.3259 | -54.42963 | 2025-02-19 04:50:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bd8aec8a-ec21-361e-b892-656399aa95cd | -18.32531 | -54.43328 | 2025-02-19 04:50:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee590d32-1887-3c0a-8eb9-61c55ff6c490 | -19.53661 | -45.90545 | 2025-02-19 04:50:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d93b4ac9-0a90-3b49-b0a6-a884c27fd52a | -18.32923 | -54.43021 | 2025-02-19 04:50:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f38b609c-4826-3b54-a417-c8277ced89d3 | -17.74286 | -56.31031 | 2025-02-19 04:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 11a14fe0-d443-3d02-bafb-0a5c33205e0a | -20.22276 | -46.49268 | 2025-02-19 04:50:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3a37b57-c18c-33ff-b310-8e3c4e73d125 | -19.53723 | -45.90591 | 2025-02-19 04:50:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72d5bc6c-bc3b-3e49-9b8a-4f64813e5d4c | -20.2233 | -46.49163 | 2025-02-19 04:50:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 225fe390-398d-35b2-b838-8175b172af9c | -18.32688 | -54.44483 | 2025-02-19 04:50:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 669923e1-6278-3e63-9c85-2b7a6974079d | -18.33139 | -54.43811 | 2025-02-19 04:50:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 42995cdc-7afe-3d4d-a01e-f375b2574807 | -20.08048 | -54.75336 | 2025-02-19 04:50:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 53ea8e41-6e69-3006-b48f-88d1449b0018 | -18.32472 | -54.43694 | 2025-02-19 04:50:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53689979-d0a8-3f16-b800-7382161136fc | -18.56092 | -57.38541 | 2025-02-19 04:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 034ea490-7b61-3398-b0f8-888f321495d3 | -20.29846 | -46.5117 | 2025-02-19 04:50:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c74cfc0c-22da-3db5-b090-f26c7a19589e | -18.32864 | -54.43386 | 2025-02-19 04:50:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 74e7b182-cebc-36c5-8cbf-9c2ac54a2124 | -17.33385 | -53.73099 | 2025-02-19 04:50:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dde8578-67b1-37be-bb82-15610bfcead5 | -20.76232 | -46.76932 | 2025-02-19 04:50:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0b8deebf-169c-3eaf-8b12-2af6a1faeabc | -18.72019 | -49.16199 | 2025-02-19 04:50:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bff11a55-44ac-3cbd-8eef-d1b3520fcec1 | -20.3285 | -55.00655 | 2025-02-19 04:50:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64fa3dec-7a71-3fb7-9397-4bcce8ce2dcf | -20.2185 | -46.49108 | 2025-02-19 04:50:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 64704cad-549f-3ad5-8c64-8839ee1461b3 | -17.73308 | -54.85197 | 2025-02-19 04:50:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fcc4ee0c-9db2-3701-bb89-5ea3fd054e1a | -20.33184 | -55.00716 | 2025-02-19 04:50:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c14f8c52-ee61-3c87-8116-8e3d9881c552 | -22.46121 | -49.28763 | 2025-02-19 04:50:00 | NPP-375D | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1991abfd-f066-3a6c-b3c5-d1c5e0434d34 | -18.33197 | -54.43446 | 2025-02-19 04:50:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c3b46395-9758-34e3-baf2-e5bdf9f9d89d | -20.30325 | -46.5123 | 2025-02-19 04:50:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 26112483-81e7-365b-852e-c8f06ace83ee | -20.21851 | -46.48695 | 2025-02-19 04:50:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 78f475ca-67a2-3323-a41e-4021e85de50a | -17.32996 | -53.73404 | 2025-02-19 04:50:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 182b530f-5513-3e28-82e9-558645293251 | -18.32806 | -54.43752 | 2025-02-19 04:50:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d2f5040-d89f-35c2-8412-4e7b1bcd62ce | -17.33053 | -53.73042 | 2025-02-19 04:50:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4984567-f771-3488-8056-2d6e72a59a0a | -20.72767 | -54.41159 | 2025-02-19 04:50:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6034674-ff71-395d-90ce-5e4ad38a6063 | -20.30273 | -46.51691 | 2025-02-19 04:50:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 529f56a2-8042-3224-9bee-9811fce3ff94 | -18.32355 | -54.44424 | 2025-02-19 04:50:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c82cb9f9-ab41-3138-a844-093d29ffa4af | -17.73248 | -54.85566 | 2025-02-19 04:50:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 862e8473-b4a0-3c0b-b577-e9cf4bdf35cd | -25.32398 | -53.53519 | 2025-02-19 04:53:00 | NPP-375D | LINDOESTE | PARANÁ | Brasil | 4113452 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 858d3f42-3c4c-3416-8de3-79f00538a0d3 | -25.32802 | -53.53172 | 2025-02-19 04:53:00 | NPP-375D | LINDOESTE | PARANÁ | Brasil | 4113452 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 2dfb564f-3c98-38a2-a144-c70838ad1f56 | 2.25313 | -60.29215 | 2025-02-19 05:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e424398b-ed1b-3fd7-8b90-85d079dcd099 | -2.79771 | -54.14573 | 2025-02-19 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3442ef11-878a-392f-a7ea-b4776037fa1e | -6.21603 | -48.06371 | 2025-02-19 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81d7f6f4-2fe2-37f3-ae57-3a7a23895bc7 | -6.21558 | -48.06703 | 2025-02-19 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8ffe13a-4050-30d3-b192-ed54b1ad9cb1 | -4.6662 | -55.96701 | 2025-02-19 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f68a9a0b-84ba-3b94-b3b6-de2965a4d072 | -2.49794 | -56.08207 | 2025-02-19 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ca2a4b9-d217-35e6-a048-fdebc7b9a864 | -6.21338 | -48.06444 | 2025-02-19 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35aedfc7-6e87-363e-a312-418b5ecc03d6 | -6.21291 | -48.06773 | 2025-02-19 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e5f8768-2106-3ffe-9c4b-9a1167a822fb | -1.66792 | -54.57875 | 2025-02-19 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1175cc2-f95f-3736-bbef-45cde4d63945 | -4.13074 | -54.90046 | 2025-02-19 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dedfc822-97e3-3a0a-b524-8d3ed08a0c49 | -2.49078 | -56.08449 | 2025-02-19 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66c3ef26-77a6-3332-8bee-ca53152abe24 | -14.68535 | -53.38762 | 2025-02-19 05:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1815793-aabb-383b-864b-e225eaf25213 | -14.68166 | -53.38284 | 2025-02-19 05:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc9a99d7-e683-31dc-a1e1-3b5993f30035 | -20.21813 | -46.49396 | 2025-02-19 05:12:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b3901d7-a7bb-32d5-ac4d-ffb55bd5b52f | -17.73401 | -54.85445 | 2025-02-19 05:12:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c8bd744-f416-3ab7-b891-2514875ed29e | -18.32707 | -54.43081 | 2025-02-19 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec1ad84b-5baf-36fa-bf18-abb0dbcfffce | -19.05811 | -56.06947 | 2025-02-19 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d0e2f1e3-bfe7-3f32-b8c4-a21d328e21ae | -18.32607 | -54.43866 | 2025-02-19 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3ba7378-bb08-334f-883a-ecdc45a1e35d | -19.11902 | -56.21973 | 2025-02-19 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e4fbfe57-f1eb-3f8e-866d-4099b1c34516 | -20.29914 | -46.51693 | 2025-02-19 05:12:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ad0b0c3f-dccd-3d4e-9583-8c57ef98f9b5 | -18.33074 | -54.43528 | 2025-02-19 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95d20bd4-9354-36a8-80b5-1a4e753c892b | -15.69971 | -50.51723 | 2025-02-19 05:12:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ca3372b-2ea1-37c4-9671-b964ac43d6f0 | -18.56065 | -57.38479 | 2025-02-19 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7aa6260a-4e86-3954-8b83-0a88718f19ca | -16.2011 | -56.75832 | 2025-02-19 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03eaa1d8-0222-3337-8c7b-71be613829b9 | -18.33023 | -54.43922 | 2025-02-19 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd03b090-f20b-3cad-9224-876f628011df | -20.21657 | -46.48674 | 2025-02-19 05:12:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0c136117-2aae-3642-a640-1c1e4c796c38 | -20.22515 | -46.49459 | 2025-02-19 05:12:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ad94e38-fac1-3b15-96cc-5d9ed71ba1bb | -18.33124 | -54.43135 | 2025-02-19 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72e0e421-6577-3508-a357-c80d73af810b | -20.21863 | -46.48769 | 2025-02-19 05:12:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29a3d03c-18a7-3c98-9cf2-dc0fa4a8e7bc | -18.32657 | -54.43473 | 2025-02-19 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9433798-1738-32aa-892a-9dbaf73b8551 | -18.56419 | -57.38535 | 2025-02-19 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1a7234a9-87a5-3ed8-ac52-4bfa805e2e08 | -20.22314 | -46.49355 | 2025-02-19 05:12:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 564c7946-34c1-34c0-8c92-525f88fee0fd | -18.3229 | -54.4302 | 2025-02-19 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a5b112d-2cf6-3a55-91f0-c5681d04b573 | -18.32505 | -54.44657 | 2025-02-19 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 506f814b-82a0-346f-80a8-1e62eaead18f | -20.22074 | -46.49374 | 2025-02-19 05:44:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9dd408d5-092b-388b-830f-79a40d782ac5 | -20.21113 | -46.48747 | 2025-02-19 05:44:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 584a1899-b531-3f1d-a848-4e469a29c91f | -20.22259 | -46.47783 | 2025-02-19 05:44:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b870314e-6fd9-39bf-9979-6edf4d0c2413 | -14.4709 | -45.8074 | 2025-02-19 11:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| afc82efd-4235-3ff3-8a54-cfc8d6ecd47a | -14.4709 | -45.8074 | 2025-02-19 11:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| ea402964-8f7d-3326-b1c6-b5c14a0cfa18 | -14.4704 | -45.8306 | 2025-02-19 11:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b8065f0e-dfe1-3d99-b1ef-6c83c1ee9729 | -14.4709 | -45.8074 | 2025-02-19 11:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 06bdea17-ab81-3f29-b1ca-4033456a745a | -6.83246 | -37.9999 | 2025-02-19 11:55:00 | TERRA_M-M | SÃO DOMINGOS | PARAÍBA | Brasil | 2513968 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6029d0f8-236c-3a35-9e24-887cbde79f49 | -8.7422 | -36.57712 | 2025-02-19 11:57:00 | TERRA_M-M | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4dbb664f-61fb-337c-88db-f8ccebd400e3 | -8.55161 | -36.95097 | 2025-02-19 11:57:00 | TERRA_M-M | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 00172813-4a24-3100-9c70-dceb5aa66844 | -8.38021 | -36.59486 | 2025-02-19 11:57:00 | TERRA_M-M | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 16552649-6d3b-340b-89d0-28179c4238cc | -9.36531 | -38.02039 | 2025-02-19 11:57:00 | TERRA_M-M | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 3cea78ff-959d-348a-82b0-f5f62fdc1315 | -9.28053 | -36.67978 | 2025-02-19 11:57:00 | TERRA_M-M | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 10.1 |
| d21ad5ba-8a5f-3910-80d9-3565de83cbca | -10.66938 | -39.94084 | 2025-02-19 11:57:00 | TERRA_M-M | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| d10960bd-af19-321e-88d5-28e78780ddfd | -10.01014 | -36.20855 | 2025-02-19 11:57:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 8d9b3c92-fc7f-3f29-b18a-83abd8d2b8ae | -9.9229 | -37.41173 | 2025-02-19 11:57:00 | TERRA_M-M | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 593dbb23-9527-3f32-b9e5-af4d79a5831b | -7.79343 | -37.79856 | 2025-02-19 11:57:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 11.5 |
| bbed114c-b9cb-32f2-a75e-9f0455aa984f | -12.29118 | -38.64175 | 2025-02-19 11:57:00 | TERRA_M-M | TEODORO SAMPAIO | BAHIA | Brasil | 2931400 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 16f1cfdf-07a4-3c5e-9307-60d98fbb79fe | -14.4709 | -45.8074 | 2025-02-19 12:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 186.3 |
| ec2db405-8113-3689-bf23-c0c651917cb0 | -14.4704 | -45.8306 | 2025-02-19 12:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| fdc47760-5b57-36a1-a311-32f3599868d9 | -14.4709 | -45.8074 | 2025-02-19 12:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 1e12972a-53f0-31c6-904c-3f9cadce38ac | -14.4704 | -45.8306 | 2025-02-19 12:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| a4a41305-100e-32fa-b870-941151aaf343 | -14.4709 | -45.8074 | 2025-02-19 12:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 212.9 |
| 45696f80-4654-3800-8c5c-c99b96792ff6 | -14.4704 | -45.8306 | 2025-02-19 12:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| e931ca58-9564-3e38-a26f-4cf162cdc6f8 | -14.4904 | -45.804 | 2025-02-19 12:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |


[Clique aqui para ver as próximas entradas](README5.md)
