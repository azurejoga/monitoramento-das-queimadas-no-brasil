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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbb7d827-da09-38fd-bdf9-a647b08cff3e | -2.33602 | -50.98867 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3a641ce-6ab4-384d-841b-aae113e0398f | -1.87842 | -50.96686 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f657762-1d6a-3f58-a8d9-a1f13d67db79 | -4.49658 | -48.49385 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2a7aa91-bd00-3971-b0bb-7ad6d97c205c | -3.54339 | -43.56115 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 93542748-980a-320d-9f6e-21ac8ed0822f | -3.59377 | -47.35454 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| ad8efd1b-b2a3-3408-8ba9-5c27243dddef | -3.23563 | -50.1556 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7483f686-1913-32d7-a654-1a700ef4cb5a | -3.7291 | -50.43684 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d8e1654-6969-3f47-af6d-2d4b805ce5f6 | -4.40462 | -48.60775 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11dedcd7-2745-308d-a241-76de28084af2 | -3.82589 | -46.50349 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccbb431b-bfb4-3c31-81c0-d6c65b780835 | -3.01627 | -53.43223 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97f00d40-b810-3ae3-b3ff-eb11195b9348 | -2.86437 | -54.09619 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 588c974e-d3b0-3403-91dc-efbfb9354e07 | -0.18765 | -60.76403 | 2024-11-09 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21f20569-51b0-36ae-9239-12890d976c01 | -2.48475 | -49.07542 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c40fa00-5e9c-311c-9bca-061871622fef | -2.6019 | -48.19687 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ebb665b-2929-3e40-aca8-d151c5eed5cd | -2.22306 | -46.5421 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dd52ba86-436d-30a0-8ab8-b449fff380c4 | -2.58517 | -54.00299 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f890013c-7b45-3dcd-bedd-02fcccda18bd | -2.97136 | -53.86756 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc96acca-e696-3c9f-80ec-1ebeb54d9bc3 | -1.52065 | -52.1855 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 198c22f8-25fd-3447-99aa-4bf76fffeb6e | -3.02699 | -51.52753 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 828f8553-2f7f-38ac-9a9e-01b6c82442cb | -2.00104 | -49.00636 | 2024-11-09 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aabaa1a5-d435-3761-be59-070ec65f0645 | -2.14719 | -49.13514 | 2024-11-09 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 470e3b13-8099-3d31-8514-049be688213f | -3.34924 | -50.26553 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 05b91e5b-eb29-34ce-9504-ef9f893ee373 | -3.79474 | -50.03237 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dea60eb-e18b-3355-b9bd-b19519124d08 | -3.17774 | -50.57877 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b565c1e1-ecda-3d32-a38f-df56e6c98941 | -3.06707 | -48.05963 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c5b01a3-76ca-3cc2-bbcd-88744df0d7aa | -1.40246 | -52.16004 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6001d5a-7a01-3c97-b0c5-39f1e3c7c9bc | -3.27588 | -51.06471 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b2bfad1-d2f8-3a4f-8450-0b09689de011 | -2.86865 | -50.41109 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9a98d984-910f-31db-b153-84428fcc6e10 | -3.21492 | -50.24208 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d53b529-1def-3718-9b8c-d0ae89eca429 | -3.05014 | -53.69202 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cfadc52-a837-3834-9e22-6a62140e522b | -3.12876 | -45.95504 | 2024-11-09 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c089ae9-e499-3006-be99-55c451623ce0 | -2.68163 | -51.81741 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59dcd3f8-6563-3efa-9199-18d7c485d87d | -3.55035 | -43.56895 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 55380658-64c9-3e55-b587-b0be93645a66 | -5.73314 | -43.50593 | 2024-11-09 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ddca20af-83d8-31c7-9389-ef31a3b624c6 | -2.82907 | -49.10813 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1569172-a81c-30a2-aa65-4ce4cd8d4373 | -2.14882 | -51.4285 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e4f7865-2a32-350d-9efb-c091325bc2a1 | -3.75626 | -54.64294 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37c27075-e5bb-3c37-9082-9ad93c8573bc | -2.91677 | -51.676 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c05c61f-f4b8-36fa-9833-69b829e7e941 | -2.66155 | -49.8686 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 534a3499-9520-3379-8c02-f7f0c810c002 | -2.26361 | -48.9835 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bcb9bf0-6c15-3c69-94b8-b02f4bf9960d | -5.04155 | -46.79735 | 2024-11-09 04:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7144665-3ead-31de-9c6f-d883dee2aa17 | -4.95088 | -48.45137 | 2024-11-09 04:55:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddaec192-ff85-3b44-a273-803a9aeb41de | -5.28759 | -50.57058 | 2024-11-09 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 312d5181-1663-3d41-a35f-eb57543dc0f6 | -3.16166 | -50.58859 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cefd3e82-fb0d-374d-b558-3577fdd28a00 | -3.76161 | -51.02148 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7b3474e1-a54f-3ec1-8215-8a7d5cd2e117 | -3.34396 | -45.16317 | 2024-11-09 04:55:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d65e1f24-0be3-3900-8d7c-6133c86e381a | -4.75385 | -48.42679 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 025b00a5-12d9-3355-9dae-1640fd89dbb0 | -2.79656 | -48.27959 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a13f4650-b685-3561-9508-ed9566c684b8 | -0.64632 | -52.38714 | 2024-11-09 04:55:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 909bf9ad-d4e4-3313-b8ae-8210cafa8659 | -3.03073 | -53.2756 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25e68fd5-2fbf-3d4c-bab0-4a1c390cfb4a | -1.82772 | -53.71659 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b7e20cd-acc3-3173-9483-ac737ec700cc | -3.17657 | -46.62578 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58d06b1b-48cf-3d90-b51a-b5d7b4bb01f0 | -2.94373 | -54.4549 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa846c56-3b2d-3de7-9e2b-3769db1ef80e | -3.96855 | -48.17268 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 32af2b5a-ab20-3ffd-943a-9b298b3242c9 | -4.78204 | -49.74868 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| faf44fb2-b471-3c3f-aeec-f9c8a3e818e6 | -3.65213 | -50.13512 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7feeef0-74b6-3043-9ba3-1647829ff270 | -5.20638 | -46.11118 | 2024-11-09 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 603f1f34-b110-36fe-893e-ab4000679aee | -2.58656 | -48.16177 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 908f567b-3e18-3cf3-b74a-354a311b90af | -2.81393 | -52.95512 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f1b4953-14c7-3661-9276-b61b29b17003 | -2.14433 | -50.27089 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40e30882-fd3a-3c1d-991a-a579cf898612 | -3.24065 | -50.26733 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| acc00d54-dac7-3ba3-bfa1-3fc866be914a | -2.19829 | -49.52288 | 2024-11-09 04:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48249219-3836-33bc-a2d8-3cf8d14e75a3 | -3.91226 | -46.45536 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7ed3ae12-499f-31f3-8906-a37a3567b9e8 | -3.07447 | -50.5725 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fbd5be81-677e-3373-ba63-e61a788a8eca | -2.17396 | -53.23662 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1abd303-6dec-3baa-9522-d86eb824e49d | -2.40957 | -48.53018 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0e471621-99a2-3a36-b0f2-27baf7ad1ec0 | -2.58386 | -49.13079 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 794a2966-2f28-3a94-80d2-efe00d44f360 | -3.8431 | -51.19525 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0dd5f46-4253-3bf3-bb1e-b77bb73682f8 | -1.63897 | -50.43717 | 2024-11-09 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12d2eefc-088d-3622-9fa6-5680d0e11133 | -2.24483 | -53.77487 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 23fa1579-3316-3ec8-943c-bdee284df48b | -1.4979 | -54.3905 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c55bf41-ccca-3d6f-a498-3ee9f32c7731 | -3.1813 | -50.57931 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 517f1816-2920-34cf-9a7c-866a56ab5265 | -3.95422 | -48.15515 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c3b0741-af47-32af-97e3-da672d705379 | -2.6065 | -48.19396 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fffde938-7bdd-3aa8-8805-ab32dc33189c | -3.15565 | -54.48409 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a6738494-b703-3233-aedf-d07037ea1086 | -2.22018 | -50.61853 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adf631ec-1dfe-303b-85ee-6858b82559e7 | -2.83295 | -49.46281 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3331aa2-f7d2-3345-9596-4c58ce83fdfb | -1.51797 | -52.22436 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25b3023e-c668-3ecb-8ede-317f2e547866 | -3.07748 | -53.88034 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1373c7af-5031-33f8-a8f9-744fd04e75ff | -3.61815 | -51.54445 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc426684-5536-32a0-82df-7e59fecc43a3 | -3.2464 | -46.47389 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ca5ad3c-c3ac-33cd-82a0-9439c2c991a6 | -3.78855 | -46.13945 | 2024-11-09 04:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82823a32-451a-3c3c-9b3c-8059ad949d3e | -1.21568 | -52.94155 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9293302d-c297-3b1c-8424-1689b2df2393 | -3.03013 | -53.25785 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87e53574-5ceb-3c0b-a767-19ee706089ed | -2.10798 | -50.66589 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0a2c3ba-6eb8-392d-ad81-1dbf497e9132 | -4.34398 | -48.62422 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aac6369b-4b32-3952-be1f-a7211c886edf | -3.32954 | -49.91278 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dbb11b06-074c-3ae6-8f59-37d0c2bce200 | -2.10508 | -50.66147 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 617557bb-5a73-3b20-91a7-f689e28232fe | -1.38464 | -51.97784 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d8c0326-8fa8-335e-81d8-41ab90649688 | -2.80173 | -52.94615 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41d43ce7-19ea-3dd8-8312-0dfedee43f01 | 0.04974 | -49.5442 | 2024-11-09 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 751351bf-647d-35ff-abdc-96ec7b9056eb | -2.87285 | -50.4076 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdcc63fb-d42e-396a-8b8f-b78211d0a830 | -2.86927 | -50.40705 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e3f16d0d-ed0f-3153-be2f-9d3fb74550d4 | -2.69633 | -51.70154 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 572cf3b3-2ab7-3d4f-a884-60b57a7ab1d3 | -2.62988 | -48.47348 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e582458a-4c34-3ced-aefd-267954b08333 | -3.33571 | -50.0872 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 435c2a40-159a-3b5a-a67f-adcd2eb576cf | -3.07128 | -51.35604 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3d30c3c-87b5-3fce-a958-9ba4d03e0c60 | -1.56192 | -52.28442 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f281178b-c6bc-3ec4-bba5-d5cdcc447b92 | -3.03514 | -53.26923 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1920a703-498a-3807-af47-a988818bfc44 | -3.03149 | -51.01046 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README93.md)
