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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72bc5ec4-c466-320f-8b1e-9200cfb1fa5b | -5.43981 | -42.85869 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c539d64e-4ee1-342d-a9c4-462e92d284b5 | -6.21079 | -43.5589 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07cac04f-149d-3896-9070-c5ec65902158 | -5.17306 | -45.45513 | 2025-09-05 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd3d7adc-5ff6-3ebc-8b5a-0231d571ae5c | -6.23615 | -46.2565 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc1313e4-23a9-36d8-87ea-3229d465960e | -5.80273 | -45.62151 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb1c9651-4605-3a45-909f-509a8bc1b983 | -5.43661 | -42.85307 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 00ee2ce9-3f5c-3621-9863-6b3bc855adf8 | -2.34792 | -47.58545 | 2025-09-05 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ee435703-f538-38f5-bbd1-e6c91448f8f4 | -6.07608 | -43.34558 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba369bf1-dda0-35c7-96e3-70a51ae153fc | -2.55544 | -47.72852 | 2025-09-05 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84efd17e-aeb0-3694-9f0d-5b1a67d0e0ac | -2.34458 | -47.58492 | 2025-09-05 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8005d7f-3202-3b1f-a45c-53e8ee523c69 | -7.61027 | -46.21223 | 2025-09-05 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7dba540-8183-3a5f-8a1c-a937e77084db | -2.43224 | -49.30904 | 2025-09-05 04:34:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 655c179c-cbb4-3112-8db1-ea463b6808b8 | -6.37231 | -43.02617 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecf7e55c-20ad-36fa-9cf6-ee2cf785de00 | -6.02026 | -46.69707 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7305400a-0b4b-333e-89bf-1ef77d7a9a8a | -7.15938 | -43.89794 | 2025-09-05 04:34:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 675a23a5-b351-3b88-babb-ed2dc1e51fa1 | -6.26442 | -53.44689 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4cce785-0d0a-356b-9a3b-55cd5db2e351 | -5.00062 | -56.25941 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5208ef45-73c5-3f68-b0ee-922b0033a209 | -6.16312 | -44.20457 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e84bc3ad-1dde-39fe-b903-3ae0fc7a7a2e | -3.56432 | -52.70482 | 2025-09-05 04:34:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9946c55-3323-31cd-b8f9-051d2f2ae5eb | -2.51006 | -51.81949 | 2025-09-05 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab77c033-67a5-38ca-a350-8a07991a2b1d | -6.58999 | -44.55552 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 5a622716-710d-3c54-a5fb-13528b24d431 | -5.63304 | -45.73107 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4137ae0-5fa8-39a8-9450-36e09a760837 | -4.89667 | -41.75697 | 2025-09-05 04:34:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ba89b89c-2ba9-34c5-a066-0bb543f4f369 | -6.21341 | -43.55682 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36ff0620-320c-3fb4-b8b4-8d1e6a5f110b | -6.51322 | -43.57211 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a5b698c-e375-35e9-8d23-28cef4386fa1 | -5.88403 | -45.57626 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40a82e74-3fc3-30c0-a60a-b2e7a1188da0 | -5.9589 | -45.72602 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9263de2-8f1a-3432-b6cc-58c25a2c99b1 | -6.2523 | -45.15667 | 2025-09-05 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| da3bcff9-7c7d-3b7e-9907-c14acfa624ef | -2.34069 | -47.58789 | 2025-09-05 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24c4e375-5505-3bec-a744-aa0ebf987c2c | -3.85463 | -48.97514 | 2025-09-05 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03710a02-2a1b-3ff0-8299-02cfb949da88 | -4.16426 | -46.82031 | 2025-09-05 04:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35ad6f82-1b53-3a86-9c96-230be3c94598 | -5.56744 | -45.57258 | 2025-09-05 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2ad7a52-a3a1-3bfc-bf5e-91c59b6538f5 | -5.00116 | -56.25623 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebcbaef8-62b1-38ed-85c9-fd9f8be08078 | -7.98321 | -44.52574 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4547dbf3-fb07-364c-a98e-4c94abf3fb1c | -6.26666 | -42.64843 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 35054ed7-500b-3417-adb3-9739cda5c388 | -5.7835 | -44.91834 | 2025-09-05 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc860c2d-fb48-34a5-bddf-df2de611b793 | -3.32925 | -54.90894 | 2025-09-05 04:34:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 293f6e03-9856-33b5-8d9a-9fa1d69cfb76 | -6.4114 | -43.26619 | 2025-09-05 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14f29333-7a26-360e-9c8f-ffb870e07736 | -6.11529 | -44.15437 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4539bfcb-135e-37c6-b30b-16fdd37a897d | -5.04204 | -56.11412 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f24b726-726a-30b6-ab96-c3807d707df7 | -6.51469 | -42.19138 | 2025-09-05 04:34:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f70e859e-9a40-3e22-b228-63127cb761d5 | -5.45575 | -42.82187 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 7d0836e1-16f0-310f-b3ff-09fe9257b06e | -2.47138 | -47.76929 | 2025-09-05 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34ac0491-6254-319f-86fb-d7307b363b4a | -5.21182 | -43.69122 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bf166a5-b883-39e1-8fde-fe674a729e9d | -3.25706 | -46.92996 | 2025-09-05 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ceef211-d943-3913-aecc-15907beff1e5 | -5.0951 | -56.14574 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e802c432-e228-3a11-a380-b3117b15f17f | -5.43584 | -42.85809 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 63b81658-021b-345d-a68a-b5bae6e32d50 | -5.44625 | -42.89607 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 44563c71-3759-32fa-b363-36666a8ec72d | -4.8905 | -41.74007 | 2025-09-05 04:34:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20e0e072-cec6-3743-903f-50db40eb22c7 | -6.05584 | -45.99817 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b2bc667-6024-3926-987e-9785899e338d | -5.54994 | -43.77351 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30a28b14-5123-3680-9596-528b328cd98a | -6.00511 | -46.66201 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6925b8a0-f337-3609-93eb-c8473cd21f0c | -5.73207 | -49.28828 | 2025-09-05 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e8031736-b344-3484-a743-f2808905db5b | -4.16481 | -46.81683 | 2025-09-05 04:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b92ffc1d-4b3c-30b8-b08b-1db559f81d25 | -6.81926 | -45.66359 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7860f0cd-e854-3d05-968f-243cff42d1c0 | -5.81034 | -47.77174 | 2025-09-05 04:34:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8ba30e0-c3bc-37dc-8056-7a1a58eefb47 | -5.23549 | -44.60126 | 2025-09-05 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d80ec6ae-e5ef-37c9-b29b-8ac0cc49378c | -6.26498 | -43.50113 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7cf69b6-d8a3-353b-abae-f0fd90c03d35 | -5.0611 | -43.86926 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33adceb2-4c30-3d84-a771-8b0f376848e3 | -5.51685 | -42.65726 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e26d0c46-d0a1-3002-bbd7-7c2f6d993478 | -6.21586 | -43.56693 | 2025-09-05 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d152ed3b-4e87-35ee-9aa2-875fecc6a14b | -6.2406 | -42.43796 | 2025-09-05 04:34:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0a138194-3108-3d63-aa64-e052c1ea28f7 | -6.66895 | -48.40794 | 2025-09-05 04:34:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca73b5e7-f3b4-36de-8928-ea646aaf527c | -6.37973 | -43.81166 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 137d95b9-bfd5-3488-a307-3b8205bd4e4c | -5.50776 | -42.66301 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2065a442-e82c-34ad-8c4f-37378a0f003d | -4.93734 | -55.8138 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56ebddd1-86e1-326c-aeee-79ced402458d | -7.98524 | -44.51234 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9c1dc2cd-be58-36d8-8608-871ffecbee04 | -6.2285 | -45.64235 | 2025-09-05 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cf7df2e-ea63-3c48-a4d7-7acaf5c4c061 | -7.60969 | -46.21595 | 2025-09-05 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a687d01-00c2-3b25-99f2-ca50ef6f9082 | -5.66336 | -43.6128 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdc395a6-8610-3f24-ba84-8a163781a1d3 | -4.0707 | -48.03448 | 2025-09-05 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7975587b-def8-3c12-accb-ad16bd3e81c2 | -6.27484 | -53.43673 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbd58e76-dc01-38ba-89a6-cde924f29866 | -2.80046 | -48.64348 | 2025-09-05 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9eca7189-3cfa-3e52-bdb8-b90017b0f566 | -5.74889 | -45.54509 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2282130b-cf19-33a6-a848-c468acd5bd0b | -5.54615 | -43.07401 | 2025-09-05 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fa7d8fe-ba62-3dcf-acdf-07be538f76d4 | -6.30037 | -44.74707 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29d11ef8-b5fd-317e-88cc-25ed1d231747 | -5.82648 | -45.37233 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a039947d-fa46-3bdb-a729-5aa0fc0c2fca | -6.73948 | -45.92989 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b0af5f5-ada2-3e16-b924-eaf0509431cb | -5.44679 | -42.81303 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bcbe31a0-94f3-3d24-8a92-7098c5ed9f89 | -6.25316 | -43.28542 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2da4aa2f-7582-3737-8c02-386458796cf9 | -5.88332 | -45.96466 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c30abb1-dd93-3ad8-af3c-c395304a9d18 | -5.48151 | -47.45392 | 2025-09-05 04:34:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d148f60b-bbfb-3ee3-9ba2-59bf69752129 | -5.03572 | -56.11477 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac75a8a2-b151-3bfc-9ab4-8f61adad5d34 | -7.59218 | -44.66655 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9504e7a3-bd99-3051-9d79-0603a3b0effb | -6.12956 | -44.15042 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fd32198-68cd-3271-a950-62d60634bf64 | -6.59753 | -44.55785 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| a0afc30f-1707-32ae-abeb-7b015dc54acc | -6.39218 | -43.83246 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42fd75d8-a572-3fa8-95ad-9e5d760e41ce | -6.13781 | -43.30638 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5f6683bc-ca6b-3fa2-bdeb-f9b22fbc3b94 | -2.89558 | -51.47999 | 2025-09-05 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53dafd1e-946d-3080-bc09-752069f02495 | -5.98503 | -44.71113 | 2025-09-05 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d39f0725-b73f-3879-8435-a08b0e33b14e | -5.8765 | -46.03133 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1606991-09b2-30dc-b458-468e30644990 | -3.226 | -47.12672 | 2025-09-05 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e24bf94-e7ca-3d59-acde-fc542fbe928d | -5.44863 | -44.59388 | 2025-09-05 04:34:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa69dd1e-ce0b-3044-8cb1-087ba0e3bbb6 | -5.20052 | -43.69178 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93b353dd-2524-3dee-98fa-d447a68193f4 | -6.21298 | -43.54468 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b027c11d-ce02-3d30-b14d-c6f1449e54a4 | -7.9839 | -44.52121 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0a92fd3a-cd5a-3e0b-aa89-1c5b97db719a | -6.59795 | -44.55217 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dea2d0e9-b55c-3890-9713-e79657d2ae00 | -6.15978 | -43.18341 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 40c88058-098e-3b88-91c6-71f751f85d95 | -6.51433 | -42.19037 | 2025-09-05 04:34:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 61ddf2cd-ed20-3798-8f62-f707022dcf31 | -5.17364 | -45.45133 | 2025-09-05 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README19.md)
