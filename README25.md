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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb87305d-c8b9-3ea8-8871-bd80df0d3e43 | -7.3394 | -46.89628 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 428857f0-806a-3755-b51e-8ec7c9091806 | -4.8306 | -42.73774 | 2025-10-30 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a5e2f993-3b38-392c-90c9-ca91a450253e | -7.08529 | -44.94099 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73ee9813-fa28-392a-91a9-5d06932da6f2 | -6.15115 | -41.60016 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a1be4465-5110-318e-9052-30be7dda231b | -6.85605 | -42.14266 | 2025-10-30 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e693fe46-7fa9-345d-b4ea-7b410ceaa6dc | -6.15854 | -41.59771 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 53b417e9-22a0-349f-af59-0b4048e1ade3 | -7.34433 | -47.63863 | 2025-10-30 04:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8bbba58-62e4-32d2-aecf-fff104675be2 | -6.13864 | -41.7001 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d3a9c11d-8ba8-3343-a4af-00b3cc07886e | -3.52873 | -47.5525 | 2025-10-30 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3746db73-5902-3e76-bc28-053be1d1a890 | -5.70299 | -43.15229 | 2025-10-30 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ea5d88bc-51ab-37ff-8e09-75de9f1720c2 | -7.86594 | -44.22865 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f92dbb64-9279-3722-acf2-9e99ea0e8168 | -3.63111 | -43.92135 | 2025-10-30 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac53b80f-f500-37f8-8333-6f43451418ae | -7.92617 | -45.5019 | 2025-10-30 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c10090bf-f85f-304b-baf4-7844286e6111 | -5.6099 | -47.12818 | 2025-10-30 04:04:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72032e37-9b2d-3461-84ea-7b1210a72144 | -7.52619 | -42.85452 | 2025-10-30 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4dc221b3-74a4-348b-bf74-2025773d0764 | -7.16704 | -39.46042 | 2025-10-30 04:04:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6e8a8309-9a11-32fa-8b0a-bbd850982350 | -7.40001 | -43.93837 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99ef0e5f-6a56-37fb-a289-66c6208998d8 | -7.47315 | -38.5593 | 2025-10-30 04:04:00 | NPP-375D | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ac6f4577-ffb6-351c-a992-944dc67ced2e | -7.9215 | -39.71821 | 2025-10-30 04:04:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f1ded07-da94-38f2-8bcb-7a5de0d4dace | -4.31196 | -48.22654 | 2025-10-30 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48204efc-9464-3ec5-9f25-a426bf780da8 | -7.65419 | -42.2463 | 2025-10-30 04:04:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 550b49a7-768c-3383-b6a8-5d5e0949ffbf | -7.60543 | -46.79603 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ad3d0e0-69d7-3e40-aefb-edff9de8c57e | -5.01666 | -43.77058 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca0a1e72-69d8-3b66-a065-672ce92e7ce2 | -5.64336 | -41.08883 | 2025-10-30 04:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b18fe70c-aaec-3eb8-910f-53e6e1c5dc92 | -6.17158 | -41.60362 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 051268dd-f892-3360-b2d9-ed270204c1d2 | -7.30071 | -44.97137 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 263ac54a-6779-39be-beed-465aca36e9a7 | -5.80937 | -40.83435 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97b50416-e158-34e6-9cd9-870653be8761 | -7.64729 | -42.24521 | 2025-10-30 04:04:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9f6f48fe-c965-3e36-8ee1-a6778851953a | -6.55526 | -42.34576 | 2025-10-30 04:04:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ce9f0c70-582b-379c-9d12-971880876e2a | -6.70756 | -43.44804 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5577d35-c97d-371c-a949-198c16bdbef1 | -5.38089 | -47.20524 | 2025-10-30 04:04:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5659a946-65e5-327b-affe-d66811806bca | -7.96999 | -45.44175 | 2025-10-30 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 048d2bec-4904-3827-9338-0b8d0a9b73dd | -6.01925 | -41.98034 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ac7cbfa7-ef8b-3b94-9d10-d2cc316f7126 | -5.0583 | -45.32314 | 2025-10-30 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ce0059f-61da-3be6-889e-37f849623a8d | -7.93406 | -45.4805 | 2025-10-30 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37ba9376-d8f6-3822-9c07-44bfb155d7c1 | -5.57574 | -42.17412 | 2025-10-30 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a994ecd0-9cc4-377c-aadd-fa98afa8f33e | -7.14457 | -40.4622 | 2025-10-30 04:04:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a51c7774-7686-34c0-8546-df315411c8bf | -7.33842 | -46.89778 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c5fae17-99c2-33a3-9d27-e0e807f2cb12 | -6.48543 | -42.21658 | 2025-10-30 04:04:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 87f4bd0a-417e-3ae8-8a01-c4fa07c9619d | -4.47078 | -43.44524 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 8e0f1bac-198d-3f83-ab43-946308203f5a | -6.47132 | -42.23777 | 2025-10-30 04:04:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 35242672-6010-379b-ac4c-569e3082492d | -6.18415 | -41.69971 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 93d994e7-5d0f-3ece-87c4-a738b9aacaf8 | -7.61356 | -43.56688 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 259e875b-53b3-3c76-ada5-67fa5b5c8484 | -5.50737 | -41.73467 | 2025-10-30 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3cca89cf-b6ea-3e19-9635-f184e8ff305b | -4.86688 | -45.54588 | 2025-10-30 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d432c77-001b-34c7-951e-9cfe305bbfb4 | -4.59689 | -46.06114 | 2025-10-30 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f4b7160-a709-320e-85fc-b8637e5c3669 | -5.43494 | -45.3457 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2dd23d56-2efc-32e5-840c-d9e63bb8eb0c | -5.75823 | -42.85725 | 2025-10-30 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9b37e56e-696a-3d8c-81d9-60eb9c28dbb4 | -5.79821 | -40.81818 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c2510e64-10e5-3cd5-aa56-46852405669f | -6.85644 | -46.28893 | 2025-10-30 04:04:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72abc414-0c97-358c-a3b6-7ed3b00223a6 | -4.433 | -43.37156 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfd175b3-7b2c-3eb8-a435-ee6419c57c61 | -3.00875 | -51.38743 | 2025-10-30 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e226e65c-b15b-317f-8542-15b0a66e6b57 | -7.92336 | -45.4939 | 2025-10-30 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 604fbd01-236d-31be-bc8a-fd647b3ddda3 | -6.14265 | -41.69703 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6a68857c-9ca9-3aa3-ad87-aca9ce80307b | -4.55869 | -46.34116 | 2025-10-30 04:04:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26cc4ee0-2589-3ecb-9ea1-5c06f8e75fe6 | -6.21772 | -41.53571 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1fc609e6-8b01-3937-b594-10e90a64a0a3 | -5.64473 | -45.98024 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 033bea30-a0bb-3d94-b4f0-261de310a43f | -4.90892 | -45.67702 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34e79bff-2cef-38e4-bc84-8bf98a957527 | -6.30963 | -42.10733 | 2025-10-30 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea938617-7c0f-3e0b-a414-5c9ec46aaaea | -7.1231 | -47.0033 | 2025-10-30 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf7ceff7-8920-3434-bf03-cf1f36b16876 | -7.25534 | -45.5779 | 2025-10-30 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f2f239d-3352-31da-971d-0fa1b2fdb7e8 | -6.14309 | -41.71623 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2138eb01-ba01-3915-bd5a-db8923cc3836 | -4.26127 | -43.71236 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 5d42fe7c-e574-3d62-b62c-34343fc5e1e4 | -7.61579 | -43.576 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 199df3c2-667d-3cab-89b3-102ca6094c7a | -6.01233 | -41.97923 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 5c50b5cc-7ed9-36af-aee2-ae9a9aecf562 | -5.43744 | -45.09839 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f493553-8168-3249-9b64-e457992e0e1a | -5.94937 | -46.65585 | 2025-10-30 04:04:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91963fa4-28d2-3124-a95d-e687ab028f88 | -5.23034 | -46.14257 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f9cff2c-049f-3e7c-9b16-b0af1b3efd1a | -2.57277 | -45.79823 | 2025-10-30 04:04:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 81d04b4e-7c6b-37db-9de5-0cb6487c97d0 | -7.79678 | -46.42352 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ec2a5bfa-0ae7-304d-9e18-a9066cf04128 | -5.5926 | -42.78008 | 2025-10-30 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c50b80f0-3d3a-3db3-a2f6-5ed9bbf5da17 | -5.2981 | -35.97914 | 2025-10-30 04:04:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5e0c7878-000e-3a57-80f9-8e0cebf332b7 | -8.92617 | -37.28193 | 2025-10-30 04:04:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f4fb5566-c1c6-3558-9a9f-9967b6b7e11a | -6.13528 | -41.5901 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4494ac23-970b-3534-af47-3c701ae3d3d0 | -7.80828 | -46.40872 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06636d36-e1dd-319a-8bac-babf1a36ea45 | -4.98963 | -45.52233 | 2025-10-30 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65d6b702-10c0-3f62-b397-f3e71923ced4 | -6.1494 | -41.6111 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ecacad91-0cac-3424-820d-76807e4a1d25 | -7.45266 | -47.18734 | 2025-10-30 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44b8fe32-fb2a-3496-8d1e-2be8203b0c7e | -6.78945 | -39.14896 | 2025-10-30 04:04:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a5e6c51b-15f6-3ee7-ae3a-0de0329fe2fc | -4.75925 | -46.85616 | 2025-10-30 04:04:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a23610da-8373-3dc9-89c4-c07743b3e7b8 | -6.14998 | -41.60744 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 58b71b7e-3398-3f2b-bec1-33e95918d567 | -7.97407 | -45.4423 | 2025-10-30 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abaabe7f-86b1-347e-ae97-5fe9cf1c2b26 | -7.65074 | -42.24575 | 2025-10-30 04:04:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 06db2796-7864-3f40-97a3-f2dfee10c160 | -5.92714 | -44.73113 | 2025-10-30 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| adba9503-b717-30a7-a331-f0a2ffba5860 | -7.50811 | -44.07895 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 308e4d9d-b9bd-3737-9238-c0229593d3ee | -6.30641 | -42.32305 | 2025-10-30 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1709a5d7-a628-3c70-8b76-374b2bde52a4 | -6.53438 | -43.56783 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8d13fa30-c652-33c4-8940-1d0eac92a4a7 | -6.95106 | -40.91187 | 2025-10-30 04:04:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 036e0b0a-ce1e-308c-85c2-18cd84e0e254 | -5.51492 | -41.23487 | 2025-10-30 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 65f94296-5b98-3130-8b91-3600d6294c62 | -6.88644 | -45.5546 | 2025-10-30 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac78ba08-a9ac-3140-90cf-7f9207360046 | -7.3392 | -46.8932 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad43a25d-62bc-397f-93ea-844808941ac0 | -6.16543 | -42.38876 | 2025-10-30 04:04:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 720b2d60-d896-3d98-ae1c-ac08e13afd2e | -7.29997 | -45.66637 | 2025-10-30 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb3b2bbc-564d-344f-a73b-aad4e31b408e | -7.78074 | -46.49013 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c07a7f1a-a672-3494-bcfd-c9ea1115229d | -5.95014 | -46.6513 | 2025-10-30 04:04:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca8f504a-6b02-3677-9ffa-9ecd3f290257 | -5.47862 | -40.89489 | 2025-10-30 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ad92696a-edd9-3129-9d3f-1efc9c26b38c | -6.85207 | -46.28819 | 2025-10-30 04:04:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15d84667-4c1b-35fa-9113-957aca61e907 | -7.79819 | -46.41539 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 95ec2283-b16b-311e-a3d1-4f9f73020e1a | -7.34152 | -38.48687 | 2025-10-30 04:04:00 | NPP-375D | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b3db68ce-85b3-3a94-8f9b-6d8510864c3c | -4.26205 | -43.70762 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |


[Clique aqui para ver as próximas entradas](README26.md)
