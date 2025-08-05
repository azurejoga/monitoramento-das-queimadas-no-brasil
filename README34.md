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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00f28b6b-747e-3472-9839-7da49a443812 | -2.9371 | -42.2827 | 2025-08-05 14:20:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 3d8bdaf8-776d-30a1-90c6-4a3d628ad687 | -13.0723 | -56.9131 | 2025-08-05 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 865b88cf-316f-3432-9450-c1a3b86f26ae | -5.9249 | -45.1171 | 2025-08-05 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 1a38b25c-06ec-3835-947d-6b02baa82ddb | -10.7842 | -45.5037 | 2025-08-05 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| d4688967-4736-3d1b-9b5b-45389d45a2ea | -7.9934 | -43.2005 | 2025-08-05 14:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 57b09881-9900-3c70-b618-c4628d2e62e1 | -8.8426 | -47.6098 | 2025-08-05 14:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 0180eeb5-b6d4-3c9f-95f7-5f05bd8551d7 | -6.433 | -44.8279 | 2025-08-05 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 4bc112eb-7ddd-3e0f-a40d-035f8cc34777 | -7.838 | -45.1127 | 2025-08-05 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 74b3a69e-6f6a-3cf4-a2f6-9f326d79f77c | -12.4243 | -44.7125 | 2025-08-05 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 2135ccfc-a8f1-3e3a-a580-eaa3d451d5f1 | -13.0538 | -56.8746 | 2025-08-05 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 78a841e9-43b6-3f3a-9012-cdbf17490a9a | -7.7616 | -45.2111 | 2025-08-05 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| c4aff8f4-1bf5-3964-bc29-07ac61d7f7f1 | -7.9931 | -43.224 | 2025-08-05 14:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 143.4 |
| 5d956eaa-83b9-35c3-a4e2-a87eae2ea895 | -13.0914 | -56.9114 | 2025-08-05 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 059cdb37-9de1-3be5-ab40-060e6e65feb2 | -6.236 | -45.8607 | 2025-08-05 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 318ed856-6df4-3704-b0e6-2e7bcded0c65 | -8.012 | -43.2219 | 2025-08-05 14:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 246.2 |
| 0f95ce79-ab19-316f-9809-245af535e45d | -6.2932 | -45.7441 | 2025-08-05 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| e096c1e0-ab6b-31a7-b744-d32f90998661 | -7.9943 | -43.1298 | 2025-08-05 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| bd1d6d83-7ad8-3ce1-9f79-831b616eb5de | -10.5776 | -50.507 | 2025-08-05 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 82a7372b-af38-3c69-9170-d963508d17c4 | -7.994 | -43.1534 | 2025-08-05 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 6c719bcf-4c44-3353-af1b-f14e989bd30d | -8.0123 | -43.1984 | 2025-08-05 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| c0d8b9ad-d286-3fe4-832c-7dd82fd24405 | -13.0916 | -56.8913 | 2025-08-05 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| bf6ec62f-8329-336f-9a19-ecc338585cbd | -8.0117 | -43.2455 | 2025-08-05 14:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| aed86b82-d014-306a-a7fe-1e3abea1a7a0 | -5.9249 | -45.1171 | 2025-08-05 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 7fdbd2dc-e87b-347a-9529-137cf2c893fe | -6.2173 | -45.8621 | 2025-08-05 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| ce3a4ea6-f3b0-39a1-9739-8fe0b65f49d6 | -10.7838 | -45.5266 | 2025-08-05 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 9917d47b-8ae8-36e9-8397-cb81cef81b10 | -6.9793 | -42.8798 | 2025-08-05 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| d3b642df-8dc9-3895-a4d0-9a64514255ff | -7.0946 | -44.3589 | 2025-08-05 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 122bf76f-c7a4-3d43-a98a-91cf2b1b64be | -7.7613 | -45.2338 | 2025-08-05 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 79cc3501-e793-3598-bbee-b7c53444d61b | -7.7425 | -45.2356 | 2025-08-05 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 70643fee-12ae-3f87-89dd-90849972f174 | -5.7887 | -43.6134 | 2025-08-05 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| b449c30d-8d05-3e7a-81b4-5737c7b5cf6a | -7.8383 | -45.0899 | 2025-08-05 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| b2b582cc-114f-3c3e-a231-50b2c8769bec | -10.7842 | -45.5037 | 2025-08-05 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| e98d5284-c43f-3413-97a5-66a519086fa7 | -6.9736 | -43.3965 | 2025-08-05 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 82a04ef5-9372-3804-95ca-a54570632fbf | -7.0757 | -44.3606 | 2025-08-05 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 21f70809-3d0f-3b06-b883-b53e948c3018 | -6.9736 | -43.3965 | 2025-08-05 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 57e11071-d2b7-3be9-a0d5-384e6a8e5061 | -6.452 | -44.8035 | 2025-08-05 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| df9c9886-6c0d-3dc6-ae0a-55f9c96ceb9f | -11.7474 | -45.0014 | 2025-08-05 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d730af08-0aca-340b-89dc-ae44c05a6039 | -6.2932 | -45.7441 | 2025-08-05 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 7d400a5b-bf36-34cc-8ff4-78ed92483ca2 | -13.0916 | -56.8913 | 2025-08-05 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 86a2b570-8327-3ed9-8cb8-921d5cd47bfe | -10.9298 | -48.3717 | 2025-08-05 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| b595bef7-8100-304d-a4cd-b47af9dc7b3a | -5.8154 | -46.9798 | 2025-08-05 14:40:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 266e191f-3228-3cac-afcd-ec1d9559ba1e | -13.0538 | -56.8746 | 2025-08-05 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 1670b65d-e19b-3e24-94f1-196e0b89588b | -8.0123 | -43.1984 | 2025-08-05 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 98fe78e9-60f9-3c94-984f-7a4422083787 | -8.0117 | -43.2455 | 2025-08-05 14:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| f6d7bffd-0d35-360b-bd07-0398898961e9 | -7.61 | -45.3163 | 2025-08-05 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| c7e33b95-a7c8-33ad-82f4-d0c08c612c00 | -6.9924 | -43.3948 | 2025-08-05 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 7f9d84aa-4ae4-307c-bc33-7917329d6114 | -7.7613 | -45.2338 | 2025-08-05 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 19bc6594-f1d0-34d7-b889-cda907affe34 | -7.838 | -45.1127 | 2025-08-05 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 2469c714-6526-33e8-b2f3-32a61e1a2354 | -13.0726 | -56.893 | 2025-08-05 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 095f3a48-91d3-35ca-88ae-f1657df29670 | -9.6752 | -46.0273 | 2025-08-05 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| e2d7fe96-926e-3212-b371-84c554d988c6 | -13.0535 | -56.8947 | 2025-08-05 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f3cc3a60-422e-30ef-b68b-bb29d72306c2 | -8.012 | -43.2219 | 2025-08-05 14:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 326.8 |
| ce4ed929-0e88-3f16-b4e2-f3b68c4cd360 | -6.433 | -44.8279 | 2025-08-05 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 107c8f65-28de-3ac4-97ba-a86a3409eb4f | -7.9931 | -43.224 | 2025-08-05 14:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 264.3 |
| c1769614-a679-30b3-a2ad-e71ab435deb3 | -13.0914 | -56.9114 | 2025-08-05 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| ff0debae-ab77-3946-a3cc-d79ff2cf0d6f | -13.0728 | -56.8729 | 2025-08-05 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 19a3a2c7-97ee-324d-b2f9-84b8603e7224 | -5.7887 | -43.6134 | 2025-08-05 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| dd5c755d-f660-30db-8dbf-83d04a206711 | -7.9943 | -43.1298 | 2025-08-05 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 06e461c5-1262-33be-b8b4-785ef6f49110 | -7.994 | -43.1534 | 2025-08-05 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.9 |
| 235c37c0-e884-3ddd-8cb2-1714460f9a9a | -6.5009 | -45.5479 | 2025-08-05 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c2965a6b-97b1-341c-b26f-a96b93cc31f3 | -9.1849 | -48.8427 | 2025-08-05 14:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 35c6e43a-b0c7-31b8-b863-260dd4c34333 | -11.9203 | -44.9757 | 2025-08-05 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 59150634-bc29-3a01-8441-3acdd237c576 | -6.2173 | -45.8621 | 2025-08-05 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 411a5c9a-3361-32d0-a026-effbb33876bd | -6.7871 | -43.25 | 2025-08-05 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| daccbc7f-d73f-372f-80fc-d7b6708981d9 | -6.9793 | -42.8798 | 2025-08-05 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| d0d32c9c-e9f5-3aef-93d3-0f2a3f29dd38 | -7.0946 | -44.3589 | 2025-08-05 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 7f12e019-1fc0-34fb-8ed9-8f05d0fba5ac | -6.4332 | -44.805 | 2025-08-05 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |


