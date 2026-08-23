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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f830d7d2-e6c9-3f57-87b8-9100f09fdaa7 | -8.98422 | -50.77231 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c65f3b7f-f4ce-3a33-a103-86dfa6119a26 | -8.90465 | -60.54166 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 891296fe-b1df-36cc-beda-df34ff2c90fe | -15.75912 | -49.97185 | 2026-08-23 04:46:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e90c600b-7560-3749-b4da-4c2bac203230 | -16.67378 | -49.32736 | 2026-08-23 04:46:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5df729d-d796-3b41-a613-6e0f920192e5 | -10.43938 | -50.46529 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f52134a-2ce0-3d43-ab12-1883ccb24912 | -9.24448 | -60.79239 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46dc4da4-6d8e-3826-9a55-568808ca3bc9 | -14.30778 | -53.23499 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79cef301-4e1a-3149-a345-475aca763fd9 | -8.53419 | -54.85213 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 069750dc-fb57-37fe-b03a-1eac88653e7d | -9.10995 | -61.58953 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c310c11-8956-3e43-9336-b64504d87350 | -8.52985 | -54.82465 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58cb882a-5c11-32b1-944e-d0118b3ec0d0 | -15.72764 | -56.04087 | 2026-08-23 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 592a23e6-0e53-3fa3-89bc-dfc94160f357 | -8.40129 | -62.68995 | 2026-08-23 04:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 978721cb-b381-3d72-a3f1-75395d00cf62 | -16.40377 | -51.84937 | 2026-08-23 04:46:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d85838fe-98a4-3bc4-8e7e-49a10152fbf0 | -12.21873 | -43.15669 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 698499a9-8dc4-3600-8934-0cd5d0e696cb | -9.67653 | -53.59976 | 2026-08-23 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 846e0de1-e9f7-3ddc-8916-3d059b812158 | -8.52545 | -54.82386 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc8697e4-cefa-3f06-8397-50efa0851b59 | -9.03729 | -60.44199 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 377235fd-4df5-36dc-8a8d-957846cbeff3 | -11.61376 | -50.55355 | 2026-08-23 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ba5e836d-085a-3e9e-b7bf-f71944da0aca | -12.73113 | -48.40138 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba1d0c45-580c-3c66-9f08-0f87d6749a3e | -8.99177 | -50.76969 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a9af449f-a42f-3865-bc5e-d49744e31acf | -12.02005 | -55.34303 | 2026-08-23 04:46:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08dce0e6-efa4-3c6a-8054-238093d2e1a0 | -9.01532 | -50.73443 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a85a116-7192-3a94-aa05-48448fa1e671 | -12.77722 | -48.47086 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6387dd23-41a7-30cb-b300-069925bac5f7 | -9.79467 | -46.60965 | 2026-08-23 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec16fbad-7cde-3987-be4e-ec0d9b0d6cb5 | -12.81238 | -48.39888 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 269075ce-cbdf-3dac-911b-4c58d2d3cae1 | -14.50733 | -59.81861 | 2026-08-23 04:46:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 263f5fa7-d29f-35f9-ae7b-60afe01494a8 | -12.23164 | -43.1689 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fcdcc997-f58e-3b30-a852-a755933fdf02 | -8.51955 | -55.34264 | 2026-08-23 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4cf301d4-74f0-378a-a66c-846bf459f69c | -8.52768 | -54.81098 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d726562-8cbc-3ba2-a7cf-d66649372ecb | -12.82748 | -48.47894 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c4373b4-ad58-35eb-a9e9-18bfe8206205 | -12.07155 | -50.59568 | 2026-08-23 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a52ce244-7200-3924-a698-138cac6b4061 | -10.80162 | -50.96503 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fab8a510-6476-3cba-9dcc-c3a2d82ceaae | -8.53128 | -54.84268 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e0e1742e-7245-32cb-a6ab-7400bcdd09cc | -12.55981 | -47.9298 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93020b52-1531-3e8f-a6a7-7dda757e64d5 | -13.16613 | -51.42276 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 85f296bc-9835-3383-8c2d-253d47eae2a5 | -14.36449 | -51.83246 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faf0669a-cff9-30a2-b2b7-b8cd22e48d10 | -9.79 | -46.61691 | 2026-08-23 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 75d4390d-0093-3197-9f05-fcca8c3baefe | -7.61767 | -60.97726 | 2026-08-23 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1fcef8a-29f3-351c-aa16-aa983c575ed7 | -11.20512 | -55.08232 | 2026-08-23 04:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abd33de1-237a-3a22-9245-4bd53ab5867a | -12.73283 | -48.41258 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3264503b-79ef-357a-9531-cc5aebf5bf73 | -12.73734 | -46.45068 | 2026-08-23 04:46:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e48d4fc-c7ee-3322-b487-993cbffbc950 | -12.85367 | -48.46505 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92bd9263-62d7-33a5-8f9a-2c855bdd48ec | -9.02569 | -50.73626 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35f5bda5-ad12-3e3e-9821-534c4b937b77 | -8.22317 | -55.02837 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f89aa1d4-9e0b-321a-b720-c30c6017fb04 | -13.19354 | -51.42751 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 209cbcec-d7d2-3988-93fe-30b220e81fe7 | -12.75204 | -47.1145 | 2026-08-23 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 224aa315-bec0-3444-b1eb-5e58c09e7071 | -8.97979 | -50.75592 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14f7825b-f927-315c-b656-1382de4b5954 | -13.88757 | -53.98465 | 2026-08-23 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e43aa8a2-361e-3ddb-b283-d319068c7449 | -12.8492 | -48.47169 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a59963c8-fb5a-3698-b78f-1ab1cc567d8f | -16.05582 | -50.44476 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 703f9ddb-65fe-3781-b71e-0169ef7c81f1 | -9.20982 | -59.79398 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffe8ccbf-e65d-32c5-9509-c075c28c4179 | -13.19382 | -51.44704 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63d6ecd8-0a43-388f-ae41-3bd42094a507 | -14.359 | -51.78023 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76bf3bc1-b9fd-39eb-a6a4-0f824a3a800d | -14.39599 | -51.78595 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d1863f7-8e61-3101-a24f-3f0f7afc23ff | -11.43437 | -44.53291 | 2026-08-23 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9d7dd65-8e0d-358a-9b54-b7b0b9fd5644 | -7.54899 | -61.17668 | 2026-08-23 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08bdf4e2-fbda-3d3a-9e87-3e755fe3ca1a | -12.29097 | -43.15558 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9e3bd7b2-0fee-396f-aa33-ded0ac672655 | -16.71715 | -49.13405 | 2026-08-23 04:46:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d61ea2b-f220-35a5-9462-fee139d834dd | -15.31376 | -53.79749 | 2026-08-23 04:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ef389846-4b9b-3a2f-ab19-02a23963f410 | -9.04668 | -50.8764 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7272c03-18dc-33da-926a-6b6b08cfaa6c | -12.65175 | -47.64766 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea29994f-04a1-31f6-b44d-5b95ded85e89 | -12.74682 | -48.41107 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0557db65-97f2-38b8-8fed-9c102e6f10b2 | -13.09609 | -43.34578 | 2026-08-23 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 879d85c9-d9d5-3383-a500-6cd53076f31c | -11.27954 | -50.73606 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 048f9758-b444-385c-a84c-7184cff003d3 | -13.18731 | -51.42254 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93671e17-4879-37c6-96d5-916a0012d60b | -12.40035 | -42.90369 | 2026-08-23 04:46:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f480683e-8bca-3c2c-bedf-d5b14e0c62a9 | -12.36752 | -46.4547 | 2026-08-23 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c38a152e-f627-32b7-b014-6dc542c4dc72 | -11.42973 | -44.53736 | 2026-08-23 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1f11b70-b669-3bc5-ad06-b78ccedfa6dd | -10.46188 | -49.96631 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 017c0c34-5c7a-3771-9d32-e19ba6c9f0a1 | -13.68645 | -51.84895 | 2026-08-23 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 813dd4b9-62d9-3e39-8ba5-530704678eed | -17.16109 | -46.4077 | 2026-08-23 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 654d09f4-0968-3f79-ae14-bf237e365aab | -13.1764 | -51.42454 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| eb1c773d-a88a-3ae3-ac71-e526e6d65c4a | -8.89992 | -60.54208 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fdf52792-14a8-33f4-bd78-4998fa5ad395 | -9.04269 | -60.44797 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 565749e9-3c67-37f4-b1d5-3b9806ad480c | -8.5306 | -54.82035 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e46c60e-5da1-3c3c-8242-435ab4077e6e | -12.25114 | -43.18838 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a04d9849-8bcb-3cfe-9d90-d5377f360b97 | -12.59484 | -47.88247 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c4413c8-e6b1-39a4-8858-ac39e9464256 | -9.44874 | -48.23706 | 2026-08-23 04:46:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d9f8dc1-5b62-30a1-9f27-9b935cd328e1 | -9.154 | -59.55821 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23385d0a-d491-3d89-ab9e-f3181128d50b | -9.15541 | -59.48606 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63eefecc-fa2b-3388-8134-5f94c6a9b8bd | -9.12418 | -61.59932 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93a39755-a657-37e1-a181-e3bc1d049154 | -12.56264 | -47.93401 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ac587f6-742c-3212-9b0d-a9c24c51c2f2 | -11.20163 | -55.05196 | 2026-08-23 04:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f07da843-46d7-3866-9afa-6f54f458792f | -10.82005 | -50.96037 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7597b214-5809-3592-82e9-eb672dcc6d13 | -13.88426 | -54.00372 | 2026-08-23 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01be6c66-aa5e-39b4-8c50-5c545730053c | -12.75802 | -48.38322 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d20f7731-fcda-3b20-b89f-3817959ea159 | -8.98325 | -50.75651 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 67b9fa5d-6ecd-33ae-b7e4-fb55b9fef692 | -10.3418 | -48.23833 | 2026-08-23 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1088f49a-de39-31f1-8a5a-c5b1c41fb274 | -10.83569 | -50.96692 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aab73896-350e-3a61-b5f2-cf5c57cfae39 | -12.36812 | -46.45064 | 2026-08-23 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b4bf7963-8fd7-3cf6-804e-8dfd824034f5 | -15.96435 | -47.50089 | 2026-08-23 04:46:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5a0e89dc-6ede-3f8f-94c7-cfabaa93a445 | -13.18353 | -51.44526 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c68b03b5-de86-3de4-9d18-2781d8b5ac5e | -10.83878 | -50.99077 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8588e932-214f-34f5-9c20-698bae69ca69 | -9.12223 | -61.59821 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d11289ee-4dc4-355b-92b6-0f7c93c90969 | -10.29764 | -50.39335 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b29129c3-cace-3acf-9a1b-ed7f4ed3d2a2 | -11.84773 | -51.67543 | 2026-08-23 04:46:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6787d70a-c7f7-31ce-bcf5-ad393b491b50 | -11.43044 | -44.53233 | 2026-08-23 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc494acf-99cc-39dd-898d-dad9e2968ec5 | -9.42192 | -51.66968 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19ed6ecd-b637-3915-b8aa-3bc990c3eb08 | -12.56207 | -47.93768 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfbfbb2b-611d-3a8f-bb43-0e400904dd7e | -11.10181 | -49.89232 | 2026-08-23 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README36.md)
