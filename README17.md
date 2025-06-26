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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d5796ab-a5ec-3612-9eb3-128b33555ee5 | -11.83318 | -51.25644 | 2025-06-26 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 019f9c8f-5119-398d-8c9d-969c17925092 | -13.03782 | -48.83363 | 2025-06-26 05:08:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81b23a73-84da-3f2a-b098-746220bf2c9d | -11.06468 | -55.37617 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4b4e5c49-3671-3277-8fa8-e90ec4be0292 | -10.1046 | -58.22786 | 2025-06-26 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 938c8b1e-c82e-3d5b-820d-0f72ce7b9244 | -11.06129 | -55.37564 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bade9814-6d2d-32c1-acdf-c75aebdc38cf | -14.53 | -49.92867 | 2025-06-26 05:08:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f31813ec-bdd4-3bbd-80ae-6c00e94047b1 | -12.03096 | -47.77308 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1242ceaf-3a3e-3aac-b240-6a8a30f0d057 | -11.86853 | -54.69594 | 2025-06-26 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbc52971-7983-3da4-95d6-df894cb2e93d | -11.13567 | -58.61265 | 2025-06-26 05:08:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d95cf4ea-1641-3205-98af-9897b4eb4ab1 | -11.07664 | -46.63565 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2ca155a-9dfe-3ef8-ae63-0758593af5f4 | -10.82437 | -53.73899 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06c1216d-05d3-3e38-9f20-cf6c6bcfaba1 | -11.82783 | -51.26379 | 2025-06-26 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8bc6a8b-8c2f-3aae-94dd-17e0cc1e942f | -11.4332 | -54.47992 | 2025-06-26 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d4a998f-7e54-3fd7-9699-80fe3a1f29ec | -10.82076 | -53.73844 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88e2c214-9686-3af3-8646-036e4a62220c | -11.13684 | -53.91407 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f437a37a-c84f-3c4c-bc84-8d6b32161b48 | -11.60727 | -55.54252 | 2025-06-26 05:08:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8d168e1-a6a2-37c4-bfa5-992a6250ffb1 | -11.13819 | -53.93801 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19b39e5d-97e9-3ac7-8cf6-c2b91748a440 | -11.8749 | -57.01949 | 2025-06-26 05:08:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13aca251-4c1d-3f4c-ac37-d82089fe3937 | -9.39729 | -63.26604 | 2025-06-26 05:08:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0ed52bf-f20e-34d7-88e2-84d415d6e998 | -12.61565 | -57.87273 | 2025-06-26 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bebc8730-cf1e-39b1-875a-03542f01b0fc | -12.58559 | -57.38054 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 185ffe81-b304-3798-bb4f-03a2072e56a5 | -11.84061 | -51.26036 | 2025-06-26 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2eb51b38-b2d1-3a65-9b4c-4565f87f01d6 | -14.3784 | -50.32815 | 2025-06-26 05:08:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ab6802c-c6ef-345c-b0da-77e888b004c9 | -15.93237 | -57.67345 | 2025-06-26 05:08:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 491a2186-2399-362e-affd-54257d335016 | -11.07091 | -46.63475 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc686d00-9187-3d9e-b051-6c1cd5a3f785 | -11.82415 | -51.25917 | 2025-06-26 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a70a6004-e30d-3914-bf83-70fcba9b1888 | -11.82741 | -57.76947 | 2025-06-26 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f2faa9c-6078-3194-ae91-0a06ff99f723 | -12.79747 | -48.73798 | 2025-06-26 05:08:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad5aacd7-292d-39cd-9f36-b9b9927f1139 | -11.83056 | -62.7725 | 2025-06-26 05:08:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 308022c8-cdc0-3fae-84aa-219fac8cc80a | -11.57632 | -47.43364 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d842dae-d0df-32fa-adf2-5355fc69adf9 | -14.19835 | -57.408 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7fec4ffe-8cb8-3070-be43-94839e0c512a | -11.2354 | -49.48724 | 2025-06-26 05:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 942c11d3-a2df-3a98-acd0-ab7e75635e69 | -13.29287 | -57.0785 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6905b333-2a60-3d80-9de8-5bf351eaa705 | -11.8189 | -47.54831 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab6f6ce4-1abe-3501-bcc7-691dee271f8a | -11.1403 | -53.93995 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cae87cc3-b552-357f-b9ab-8338f43d2cb3 | -11.11 | -46.6489 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7410b72a-b7f3-33dc-86c7-db9abb8648b1 | -13.29397 | -57.09324 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad3c9db6-b1af-3da0-ac5c-77e77d8e7525 | -9.17518 | -61.40425 | 2025-06-26 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b131a785-7e8d-3e1b-bd7a-f778a8bfe3c6 | -11.81763 | -47.5587 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d938fb8-c4e2-3709-b51f-d0fb02abcc2d | -10.87276 | -49.54338 | 2025-06-26 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b8b27ce-138b-3a4e-87d2-03491b00ac9b | -10.87494 | -53.77917 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33d0ebf1-bf7f-37a1-aab9-c848c19e8ee4 | -12.02513 | -47.77592 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1116587a-d9b0-3ff1-a2c1-2266b738f65f | -10.3045 | -57.13259 | 2025-06-26 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 636a1c6f-9565-37f7-a816-068d12307704 | -12.5808 | -56.98502 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 508d8ce8-cac3-338b-86b0-b4f59b3ce084 | -17.59834 | -48.42794 | 2025-06-26 05:08:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4d4a466-4159-3a3a-8994-16508381f57b | -10.86595 | -53.76511 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a555719-7f7d-316d-bcbb-fafca28458d6 | -11.83075 | -57.77001 | 2025-06-26 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b10f628-ade1-364d-8fda-6d8a27ad6833 | -11.07543 | -55.3741 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0bdc15d8-a858-3e92-8352-12da8cf9cd4e | -12.04684 | -48.0766 | 2025-06-26 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95fd242e-f337-3317-8e11-f0d3a2a320d9 | -11.08284 | -46.63261 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 193f724b-cb5e-3b47-b459-32d3124f92ed | -12.03052 | -47.77664 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59a4afcd-3439-38ac-a6ab-63b60c4b54b1 | -10.7051 | -59.12749 | 2025-06-26 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61eb1424-c1ef-3367-8d83-eb1444e887d9 | -11.61027 | -46.50458 | 2025-06-26 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c9cc6d7-d26d-315a-9f9d-cdd1c177eb5e | -13.09981 | -52.2997 | 2025-06-26 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 97f67eda-7a2f-3d19-bb38-4e99488f3dcb | -11.08856 | -46.63353 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c77563b5-ca09-3f80-903d-c6ccabf56fcf | -9.79096 | -57.42229 | 2025-06-26 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 422920bf-6890-3567-8b17-58396a4e62cd | -10.1012 | -58.22731 | 2025-06-26 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33731be1-0f77-3803-8fc3-b3695b089f70 | -11.58713 | -44.64912 | 2025-06-26 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9617714b-f50d-3cb9-a5ff-78457ed5c9e4 | -12.58503 | -57.38408 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fcdd4d7-217c-3779-ac69-213a71f1e475 | -13.10032 | -52.29612 | 2025-06-26 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0a86e0f3-ae63-31b6-8c7d-5775ba908945 | -11.44022 | -54.48102 | 2025-06-26 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 569696d3-9717-3ff2-9891-fa21bba6872e | -10.87454 | -56.45411 | 2025-06-26 05:08:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f19b4b2-8a9e-337b-b4f3-b3eee5093b68 | -10.11196 | -64.91723 | 2025-06-26 05:08:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2fdd72b-5aa1-3b3e-883b-bd7d7343cd49 | -10.87399 | -56.45763 | 2025-06-26 05:08:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b49a1b2e-761c-3ee3-bec0-e46c7478b90d | -10.86895 | -53.7698 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af8c5ad2-e426-3209-83bd-674dafe2b627 | -10.71428 | -59.13695 | 2025-06-26 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48573969-eb22-3bf3-b1f7-10a1e8328cee | -13.04328 | -48.83139 | 2025-06-26 05:08:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b1826b9-34b9-3dda-b7a0-1f63b51df17c | -11.83125 | -62.76859 | 2025-06-26 05:08:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02c905c6-19b3-320b-bfa3-7bef5be81b31 | -10.55982 | -52.01236 | 2025-06-26 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 830f9d49-f78d-39b5-ae02-619b7d3fcec7 | -11.80843 | -47.54039 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 612ceddb-68b1-3884-94c6-691d36adc25b | -10.30117 | -57.13205 | 2025-06-26 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43563bc1-a9bd-3173-a469-82cd353cb249 | -9.17116 | -61.40359 | 2025-06-26 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 35133f67-1285-35d8-9135-68c381818b25 | -13.52082 | -56.57315 | 2025-06-26 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e568415-8c0b-3184-ad77-42b4f32870e0 | -11.06373 | -46.6459 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99fe9a81-72c2-32fd-9d35-ea94e5e90665 | -10.86834 | -53.77396 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93bee7da-f45e-3008-8fa4-cfe72e0bf206 | -14.90618 | -54.3252 | 2025-06-26 05:08:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf5b44f2-190d-32bb-9c98-a5afd17edd98 | -10.30006 | -57.13908 | 2025-06-26 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96ef4a71-dfa9-30df-9846-c67b2bb38b67 | -11.06864 | -55.37302 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17183a1c-b9f4-316b-bd85-8ddbd2e42564 | -10.30394 | -57.1361 | 2025-06-26 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2276ab04-d3f3-3cd1-9586-f8d2b854bed8 | -13.29453 | -57.08969 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75d59f7c-dce1-3001-bda9-bbe59d1c5e03 | -11.57425 | -54.52065 | 2025-06-26 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 842c0fd1-4d37-372a-9d62-21e5fbd07111 | -11.06413 | -55.37985 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f9d1a075-47cc-384c-80f9-d65934ec63a1 | -12.48607 | -45.90287 | 2025-06-26 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fcaca0f-22f9-362b-91c9-04e1264a7ba5 | -12.48664 | -45.89806 | 2025-06-26 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f2c57ca-1e46-3528-a7af-34d199d3f932 | -11.13918 | -53.92293 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3474d622-515e-34b3-8144-1c1a3c742f37 | -11.80456 | -55.07249 | 2025-06-26 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 285d4b56-a8e9-38f7-9511-cfb9875ec54d | -11.83262 | -51.26043 | 2025-06-26 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7077bcc1-42d5-3ccb-9fb3-a26b4c705f79 | -12.79238 | -48.73717 | 2025-06-26 05:08:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 721bdd1e-9cf9-333b-a51c-e4356027ca94 | -13.29508 | -57.08614 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56c0daff-60fb-3ca7-99d8-36d4d1ce745a | -11.14178 | -53.93856 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7b6b49a-48b2-3553-a767-163d99b84fd5 | -13.04401 | -48.82537 | 2025-06-26 05:08:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f1c1fba-ed50-3e88-b8e2-d349eb337ce6 | -9.57725 | -63.20596 | 2025-06-26 05:08:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36b65544-d27c-37d4-900d-958d1177daef | -11.60783 | -55.53885 | 2025-06-26 05:08:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 231b825e-4f9e-3004-bdd8-901089c3f0d3 | -11.06651 | -55.06586 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da751f80-7eec-3619-a444-c7832d335d78 | -10.30062 | -57.13556 | 2025-06-26 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22c923fb-d9fb-33f1-865e-f691f8ce8220 | -13.10083 | -52.29254 | 2025-06-26 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ccaf5012-c0a0-3937-bbcb-5c49d965efd6 | -11.3607 | -48.70623 | 2025-06-26 05:08:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1602ab9e-d048-3f38-be19-8ab04f40a48e | -10.825 | -53.73478 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 150d714a-4ac0-3867-ad1d-356cc0c75221 | -11.60977 | -46.50853 | 2025-06-26 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c92856f-434a-355e-8bef-88f09c353601 | -13.04947 | -48.8231 | 2025-06-26 05:08:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README18.md)
