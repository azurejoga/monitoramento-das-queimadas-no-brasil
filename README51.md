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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f3472d5-014a-3b20-aa54-6ee65ab543a3 | -6.25088 | -45.44159 | 2024-10-25 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50a2ef9b-ff95-3ccb-a930-301fe70d6645 | -6.00863 | -45.95026 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 039525ce-3e8a-3dba-85d7-8b808180b3ed | -6.00563 | -45.94542 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7d991c0-abb4-3fd6-b44a-bdb18d65405a | -6.00498 | -45.94973 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf6864f7-be87-3708-b303-88932c6bb6f3 | -6.00433 | -45.95404 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 713745b8-bdb9-3020-b7c2-85762827620b | -6.00003 | -45.95778 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 414a4045-5f3b-3154-a717-407c97c0cc60 | -5.9844 | -46.2327 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27c94f05-70c7-374d-9c0f-52ab2f2624f8 | -5.98132 | -45.36332 | 2024-10-25 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f6103801-4cab-34f5-802f-1718d4cdb79d | -5.98064 | -45.36788 | 2024-10-25 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 76107992-b0f4-3c63-a30a-7d5232adf8f4 | -5.97996 | -45.37243 | 2024-10-25 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| b565b427-32e7-36c0-b5da-23a4d2e1d8b8 | -5.97687 | -45.36727 | 2024-10-25 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 107a5857-354e-3113-96c5-4e3767b3097b | -5.9762 | -45.37182 | 2024-10-25 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 655dd4a9-3ba3-35b5-b989-29570a96ee20 | -5.90476 | -45.56067 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bd3a84df-2527-35e2-b972-76d06793039a | -5.70689 | -45.00677 | 2024-10-25 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 73cd4f8d-cef7-3f69-97ee-7d3cf33d4c69 | -5.70671 | -45.16482 | 2024-10-25 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98074a19-8741-3e12-a329-a9ff058adbfe | -5.70618 | -45.01157 | 2024-10-25 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 18dd3ae4-b619-3f6a-98c0-259e163d2deb | -6.08107 | -46.30893 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9782193b-9bee-3d28-8cc1-b1b9ba599ec8 | -5.84563 | -46.3878 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e72414a3-a9c6-3732-80a7-d8984dec8c6a | -5.84502 | -46.39183 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36b745f3-76fd-3a7b-bf77-463b6c89c48a | -5.84146 | -46.39125 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56afe3ab-c065-3716-8c4d-3ab1c7ac1346 | -5.66883 | -46.34657 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45ba2cc6-4ea0-3525-8a25-b70a3f131b51 | -5.64529 | -46.40483 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e46f9821-917d-3fae-8e1e-595c3c208364 | -5.46232 | -46.35455 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09a534ba-b1e9-3f5a-ae85-5fa76791a122 | -5.45877 | -46.35399 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0853b3f2-e528-3988-b413-7d5471e96532 | -5.38451 | -46.15747 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f56240c-7127-396a-b754-a32556ae4c56 | -5.34538 | -45.44109 | 2024-10-25 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f858685d-9e3e-3b06-8282-c3d1f74b871a | -5.33239 | -45.55171 | 2024-10-25 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61568f41-33ed-3d05-937d-8ebaba290afa | -5.33172 | -45.55609 | 2024-10-25 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67845ba3-4de2-388b-9c6c-188347d56436 | -5.2852 | -45.7387 | 2024-10-25 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cc925ac-d28a-3bc8-9893-207a2a9e7c6f | -5.28456 | -45.74295 | 2024-10-25 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 268d5644-c633-3613-aa3c-7459910595dd | -5.27542 | -45.51374 | 2024-10-25 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4047e7e1-37b3-36cb-b756-03f8f2ae868b | -5.18229 | -46.22415 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5002c7f-e8cd-3fac-b518-a2d3604749d4 | -5.17407 | -46.19101 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3eea5f7-0be3-35bc-8547-2ca9e160cb71 | -5.17288 | -46.18959 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11ab6c52-5278-3922-b1ca-4926ccb1b3c5 | -5.17045 | -46.11992 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f8e5339-bea7-3cee-a321-b2ac9e23b728 | -5.1058 | -46.13494 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6375d041-df00-3c6b-b217-36e19ae57c19 | -5.09937 | -46.10477 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c44e283a-9e9a-3c4b-9332-545cff248261 | -5.09333 | -45.82504 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcde6ce9-a8b5-32a4-b301-6b5a5afb2b20 | -5.09267 | -45.82928 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 86d356a1-c6ff-3f15-8e66-1f10ad6ebab4 | -5.07258 | -46.05536 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 409004e6-4717-342c-b072-2c31ab6adeb1 | -5.06724 | -45.8253 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9960a95f-09ab-3fc7-9e30-c283667f689a | -6.44239 | -46.06096 | 2024-10-25 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18478226-b839-309c-a11a-1930e5b1d87b | -7.88183 | -45.43316 | 2024-10-25 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ccc9c3e-fa1c-3ba1-9559-c24f73df9a50 | -7.88529 | -45.60973 | 2024-10-25 04:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64108324-b096-3381-b437-73df7ef9cbfa | -7.81245 | -45.58267 | 2024-10-25 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c4435d5-230b-36d0-af93-b70a3de1cc63 | -7.21578 | -45.58147 | 2024-10-25 04:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 60a3c456-f3f5-3b91-8f7c-aa8c2b4f319a | -7.21511 | -45.58604 | 2024-10-25 04:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 76c8d7eb-91ce-34b1-a9e8-e022d3358336 | -7.21444 | -45.59063 | 2024-10-25 04:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 427f9368-c03f-3f61-94ef-6ecd596abeb9 | -7.21187 | -45.58329 | 2024-10-25 04:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1024017f-f93c-33ff-a7f6-5ad9a0836dfe | -7.21133 | -45.58543 | 2024-10-25 04:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 834733c6-e9f1-35cc-b2fd-a932d925c6e8 | -7.18477 | -45.48003 | 2024-10-25 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ab15317-3435-3222-9a99-8819b4bd67cc | -7.81799 | -46.51883 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 100d94b5-9672-34b2-b343-853e8596bf8a | -7.70631 | -46.59641 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13495d32-8bcd-31b0-ae1d-cc2fdd2a546f | -7.56313 | -46.79497 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18fa69b2-2a4e-3cc0-bc43-4de6df778859 | -7.56176 | -46.79331 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a3a2599-cd63-374a-9e8b-f422c5a89434 | -7.56116 | -46.79736 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22eb2d41-6dbf-34cc-b84e-dd60e1d42291 | -7.53954 | -46.75834 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 851e24bb-afa3-31a7-bc7e-72de91e2a293 | -7.53892 | -46.76238 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cb0dd3d-b199-3b50-b1a9-f0e8152b250a | -7.53849 | -45.84608 | 2024-10-25 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c3b20e2f-d086-34ad-9374-9c4a5e298f25 | -7.53783 | -45.85057 | 2024-10-25 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de881959-5d80-3973-b542-45b44492dfa0 | -7.53608 | -45.83654 | 2024-10-25 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c5f9a0c1-2370-350f-9357-ae508aec2737 | -7.45082 | -46.86428 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d28e3d1-8fa0-3c5a-aa74-3b3a07e9e69b | -7.42559 | -46.6512 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea5844c0-dd14-385b-b8a0-8c62d64374e5 | -7.42497 | -46.6553 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a00bf012-6bfb-39a9-b5ab-edfd2ac23166 | -7.38345 | -46.53975 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c88860f5-67c4-3afb-9ccd-5af3021d0e8e | -7.38239 | -46.5405 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56788846-2c9d-33f5-8a2e-39ae070cae06 | -7.32646 | -46.29684 | 2024-10-25 04:38:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47c3aaff-e750-3977-954f-c14fd6e50098 | -7.26196 | -46.05212 | 2024-10-25 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04cc8b70-2c58-3460-b331-09f89be63fc3 | -7.26131 | -46.05647 | 2024-10-25 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00a232fb-b3c0-32e9-a6a4-503e7495e1c9 | -7.25763 | -46.05591 | 2024-10-25 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07eec279-d478-304a-addd-86ad69afe910 | -7.04722 | -46.32066 | 2024-10-25 04:38:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24f882b4-4124-392c-8c63-3fbb90f744f3 | -7.02399 | -46.12663 | 2024-10-25 04:38:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ca56da8-a868-3574-a50d-8cd949e9c60e | -7.01582 | -46.43105 | 2024-10-25 04:38:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72bb05c4-634c-388c-9aa8-0dff12282971 | -7.01222 | -46.4305 | 2024-10-25 04:38:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41de5969-5eec-334e-8980-381968dd633c | -6.99711 | -45.98817 | 2024-10-25 04:38:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cff1ad51-2592-3a22-ae13-9a56dac1a1d4 | -6.96021 | -46.33077 | 2024-10-25 04:38:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f936963-9451-314d-aa82-d50668d8e957 | -6.8498 | -45.89614 | 2024-10-25 04:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 460b0b60-2295-312f-9df0-40d2d09bf101 | -6.84918 | -45.90029 | 2024-10-25 04:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ea825e0-b0ad-3c0b-91c4-bc3f3fadc116 | -6.77511 | -46.24967 | 2024-10-25 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1de468d4-500f-3c76-b84b-d2ac777f1f4b | -6.49793 | -46.16362 | 2024-10-25 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98f8619f-b56b-3d9c-9a0d-e649e205972d | -9.30382 | -46.17522 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0c0a5f8-2fc0-3af6-aa00-5573483f0916 | -9.30007 | -46.17465 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcb85bb2-405c-3450-af7d-91d73855e886 | -9.27415 | -46.2215 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6461035f-ac25-3643-b7bd-8f22845b48a8 | -9.27369 | -46.21839 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ab9e203-a9f7-36fe-b618-7ecd6b2b347f | -9.26993 | -46.21791 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44b1c2b4-c24a-38f6-9f8c-26b07fc4194e | -9.26926 | -46.22237 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6af1b86-7644-33c3-9974-2f78149fc3aa | -9.26665 | -46.22048 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ab48f27-25fc-3a28-be72-0ec3836948fa | -9.26552 | -46.22179 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c0913ae-a986-3a5a-b7ae-e003bed862c2 | -9.20987 | -46.31387 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8232a72b-a47a-30d1-b7c6-4e8f5332b72a | -9.14537 | -47.10689 | 2024-10-25 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b88440cb-d7ba-38f0-b480-9c61823dacdc | -8.76749 | -46.58894 | 2024-10-25 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dea5dbf4-bc46-3117-80bb-ff5dcbd12b55 | -8.51197 | -45.87862 | 2024-10-25 04:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4ea15828-2776-3211-a29c-cd827e68c37b | -8.1791 | -45.55675 | 2024-10-25 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de258317-42c1-3e70-81fc-31eefa4af211 | -9.27792 | -46.22191 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b7bdda4-3410-3152-bbdb-cc77f74e7fce | -9.27302 | -46.22284 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b82fecce-1fa7-3f81-97b1-778f3af0e914 | -9.27104 | -46.21657 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 608c7bf9-3ceb-3922-9947-440927176bed | -9.2704 | -46.22105 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a50c459-6153-35a4-9939-3bf46e8c7746 | -9.14894 | -47.10744 | 2024-10-25 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9865d06e-ad0c-3c5f-aed4-0d37d8274279 | -9.14597 | -47.10283 | 2024-10-25 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2b91cf2-05b7-3c95-9354-e67124b84e48 | -9.14239 | -47.10229 | 2024-10-25 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README52.md)
