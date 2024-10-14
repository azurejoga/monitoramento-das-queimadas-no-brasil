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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe59782e-99a2-35cf-8e9c-ba6057d3986d | -7.61765 | -44.06883 | 2024-10-14 04:44:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0479e8c-bc9a-3504-b0ba-8f1cb3e53d87 | -7.60242 | -44.6358 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46302422-8e69-30af-be61-5acdede726ab | -7.6018 | -44.64019 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e221c71-7721-3c64-ab36-85c1ea94926e | -7.59733 | -44.63949 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 825201a9-82ae-39e6-bfd1-fdbe3e20f25d | -7.34607 | -44.33926 | 2024-10-14 04:44:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24d1553b-1fbd-35de-93d3-8c3c4deed804 | -7.34543 | -44.34373 | 2024-10-14 04:44:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cadef136-e157-3904-ab20-31af1a642943 | -7.34346 | -44.32489 | 2024-10-14 04:44:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 291bf44f-8fdb-3f1c-ab15-5f531894fd39 | -7.33959 | -44.31934 | 2024-10-14 04:44:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a2858ad-523c-3dbb-9d96-6caf0cd14d67 | -7.33891 | -44.32418 | 2024-10-14 04:44:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51b4a904-1a95-3da0-8e5f-d9a186b3e9f3 | -7.3124 | -44.9786 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22570a0c-8b6d-3f5b-9037-ea17855ed9ad | -7.31239 | -44.98109 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd34271e-3656-3e67-a30e-9f903884c0ce | -7.30803 | -44.97805 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c8105c8-5be1-31f0-aa24-49b194e3b484 | -7.30802 | -44.98053 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46e35833-6422-3f3d-996d-7cc53bcd640b | -7.27066 | -44.95977 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 516fa95e-a782-3a5e-b6cf-a478c2257953 | -7.26945 | -44.96815 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9496693-fcd8-35be-b7cb-a97f900d3af4 | -7.26568 | -44.96346 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62b9bb57-a18d-3b42-8a05-3ae605c8a1b5 | -7.2651 | -44.96746 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7236b1f0-3133-3a3d-8bf0-2a247a115b95 | -7.26195 | -44.95846 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e7dd893-d838-3fab-ad83-64fbdda7928a | -7.26132 | -44.96283 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b60d756-83c0-3011-8d02-bd92e8f9a21c | -7.26075 | -44.9668 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f44757d8-b43b-32de-b196-4df1ebecf31a | -7.25759 | -44.95784 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bcc30ee-d1af-3a40-b3af-9fe2e5a7c27d | -7.25697 | -44.96219 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71f6a496-33f4-349b-8e58-0ce852ef4601 | -7.2564 | -44.96615 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a3f6a04-4e7f-3c08-bbc0-6fb449a299ad | -7.25435 | -44.91835 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 95cd8ba7-1908-377e-ae89-211bce962484 | -7.25324 | -44.9572 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64fafdf7-b1a5-3bb8-88b0-879bf24dbe16 | -7.25262 | -44.96152 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2b774ce-bdf8-3db5-a296-fe9eb37c689f | -7.2489 | -44.95643 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c9d11c2-3b64-36d2-b7dd-8fe7064bf6d7 | -7.24828 | -44.96075 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea028074-9c43-31a7-a0cb-3ad715b9def5 | -6.98367 | -44.71521 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a3dfa00-05c6-325b-92e8-db719b5d1814 | -6.98309 | -44.71919 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61383926-5a86-3ecc-8c7d-beb48e755d9b | -6.84449 | -44.38496 | 2024-10-14 04:44:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd4c86ea-51b8-333a-b537-d20ba78b41c1 | -6.83998 | -44.38438 | 2024-10-14 04:44:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5eab91b-12f5-3036-84db-302f6f9dd342 | -6.83455 | -44.85141 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ab7129a-8c07-3eb8-a453-ba85f62bf446 | -6.72008 | -44.68024 | 2024-10-14 04:44:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca906a78-e7af-31a6-9f42-aaa8e52ae23a | -6.62529 | -44.68925 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07624bff-46de-3410-884b-cbe6ee3e098f | -6.62467 | -44.69362 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f032222-94f9-30ae-9b59-6d3d59933ab0 | -6.50768 | -44.69635 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 049356be-f970-37d8-b67e-07f825d0ec93 | -6.50327 | -44.69587 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 514f01e0-dd1f-357d-bbc1-f6edf404513e | -8.04209 | -44.81772 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 20b3a5df-56df-310d-ac5d-763d7cfcf2d8 | -8.0414 | -44.82257 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f28a1589-04de-390f-9efb-02ced4a75f2f | -8.04075 | -44.82712 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a6e120c-9df2-343d-9d8a-290b7f997782 | -7.96509 | -45.13886 | 2024-10-14 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f221fa1-683f-33f7-9f12-6b584c00da04 | -9.26684 | -45.22747 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b63ab476-6543-3848-b29f-b5f712f70b17 | -9.26244 | -45.22682 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c336472-eae9-363c-ab99-a71e4f60db95 | -9.83166 | -45.055 | 2024-10-14 04:44:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fe2afb1-f008-392e-a66f-203e863970fb | -9.82779 | -45.04983 | 2024-10-14 04:44:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d6d729e-4322-3efc-8879-aa1f9d21baba | -9.82269 | -45.05357 | 2024-10-14 04:44:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9e45a18-8ecd-30c9-bff1-8ab8c2c73eb5 | -9.66572 | -45.21544 | 2024-10-14 04:44:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a3b9303-1bf4-374a-bc13-dd143e3d4250 | -9.66129 | -45.21476 | 2024-10-14 04:44:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fc03363-41a2-3988-b596-9b74d226a118 | -9.65687 | -45.21405 | 2024-10-14 04:44:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ff0856b-9f94-31f7-bcef-1c32931ad756 | -3.05499 | -44.47211 | 2024-10-14 04:44:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea5bb546-14d0-39ac-b74d-a4796dab6023 | -4.91823 | -45.83287 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 476c1f8d-4e5c-3ceb-9cff-0d3ee6d32b7c | -4.90246 | -46.01094 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f8080a0-1cb5-3b06-b56f-ec0f59efa71e | -4.84299 | -45.84741 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 641ce0b9-5868-3822-b631-53baa99a7fad | -4.83753 | -45.85686 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 82b71c83-19d2-31aa-afea-b6dd7be6cae1 | -4.83542 | -45.78885 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a603773e-ba76-374d-b7c0-daa24ae04664 | -4.83466 | -45.794 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9af2de5-e3fb-3192-9006-7076419252a3 | -4.82918 | -45.79185 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14809a83-1e37-3aed-8ded-021af9de2b0c | -4.72415 | -46.13683 | 2024-10-14 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5084c95e-7e6d-3e89-af02-eeef6fa737a3 | -4.71809 | -46.15064 | 2024-10-14 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87301cbf-60cd-3733-950e-47f59512e61e | -4.71734 | -46.15554 | 2024-10-14 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d7c2f4c-75a6-3b39-a177-d5b2f05443a0 | -4.71345 | -46.15506 | 2024-10-14 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b748f4e1-9cac-3f36-8748-516e42a10af1 | -5.05418 | -45.14843 | 2024-10-14 04:44:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 299b19e5-59f3-3c3e-8430-c3648f6e073f | -4.63199 | -44.86115 | 2024-10-14 04:44:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2839389-f1dc-35bd-a224-263b9b082e94 | -4.63179 | -44.86211 | 2024-10-14 04:44:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3993202-edf7-3c2a-bc8e-5705cb5a7610 | -4.62758 | -44.86148 | 2024-10-14 04:44:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f908a93-7c61-312c-a874-857a76d26273 | -4.62699 | -44.86533 | 2024-10-14 04:44:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c99659d7-a73e-37cb-9ce5-6d928b47d4aa | -4.62337 | -44.8608 | 2024-10-14 04:44:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50e0085d-07f3-3275-b78e-750dbf3b27fd | -4.62278 | -44.86468 | 2024-10-14 04:44:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 871a6bf7-04b0-311f-b6f3-3c0e3ee6c942 | -3.7814 | -45.24623 | 2024-10-14 04:44:00 | NPP-375D | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39f0f679-c724-3773-987b-fef26a47a313 | -3.77788 | -45.24207 | 2024-10-14 04:44:00 | NPP-375D | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 181f1850-2797-38cb-97cc-b445c24f7fde | -4.21211 | -45.77089 | 2024-10-14 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d25d92cc-0880-3fd6-959b-73f2a9101829 | -4.20815 | -45.77034 | 2024-10-14 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f209a14-5ac7-3ff2-a999-348b13f038b9 | -4.2074 | -45.77535 | 2024-10-14 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5a64bc5-2855-34c0-b510-af8f50fd46a9 | -4.2042 | -45.7698 | 2024-10-14 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f9ea176-bf54-362f-bbe9-23086672752b | -3.89947 | -45.70177 | 2024-10-14 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a0f318a6-a684-3d1d-98aa-0a788e8dfad7 | -3.87028 | -45.97455 | 2024-10-14 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76cf0cc7-5920-3d84-a7a5-933bda728667 | -3.86713 | -45.96914 | 2024-10-14 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25fb3874-2d6d-33f1-9f2c-b3496835bdcb | -3.8664 | -45.97396 | 2024-10-14 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1742c46e-bf2f-31c0-a883-0985ee15d539 | -3.73511 | -45.7349 | 2024-10-14 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 40.1 |
| bae9f027-04cd-34f5-9962-b5c68361019b | -3.73194 | -45.72934 | 2024-10-14 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4d34f0bd-3e7e-37fd-b7a3-6a00ee892433 | -3.73117 | -45.73434 | 2024-10-14 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 3fb5324f-eb7c-3e68-9e56-1a0c5fe8a986 | -3.63465 | -45.50036 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa70546c-083f-3a72-b8a1-35fa46d94e63 | -4.99837 | -45.47054 | 2024-10-14 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7c7e4c1-d3eb-3766-841b-a769a92ba1bc | -4.9943 | -45.46989 | 2024-10-14 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 934cf330-c41d-3b0e-a5b6-e8d4087bbf26 | -4.96787 | -45.6216 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7df8120-7ae9-3fbf-983b-b7a706e11f43 | -4.96736 | -45.62504 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad257417-2d24-3924-aace-3c4f565b7ed6 | -4.9548 | -45.76596 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6424b8d7-a2a2-3d5e-a873-fd5fd48bb0b0 | -4.9508 | -45.76537 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86ca3221-c384-322e-9817-1ac0c9fe9cc7 | -4.90709 | -46.00678 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09105dc2-a20e-3235-b816-ef06f06731e5 | -4.90398 | -46.00428 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eefe27ec-7399-3f03-960a-21986d25fab9 | -4.90323 | -46.00914 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b846d927-47e7-3199-bb43-971da492f407 | -4.90317 | -46.00606 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ff8a2b7-a228-313b-a6b2-48b00ef77f9f | -4.83141 | -45.78844 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 51e664a2-6116-3452-b053-634117e46e8c | -4.83066 | -45.79358 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15d04a2c-10a5-3c63-9ba3-0cd07c0671a2 | -4.82998 | -45.7867 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97b0c968-20c9-3f3d-bb1e-2805c2eef3fe | -4.8068 | -45.75188 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68a9494c-c22f-3dd6-9e87-b8f1c9a8cda9 | -4.80602 | -45.757 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e6acfe8-6676-311a-89b5-c6267491ec7c | -4.78 | -45.79437 | 2024-10-14 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0ef6926-bf6f-3718-9e66-0d8ca5845318 | -4.71419 | -46.15012 | 2024-10-14 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README75.md)
