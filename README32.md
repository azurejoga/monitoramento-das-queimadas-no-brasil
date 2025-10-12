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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3811fe84-ec9c-3e35-bb76-0105699be293 | -3.50495 | -45.84668 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68103d29-1062-34e8-851a-48363c854e68 | -5.58039 | -42.9906 | 2025-10-12 04:42:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c7453913-41a7-3214-8fee-f8dd385dfe32 | -2.45166 | -49.36303 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e23b3e91-0524-3e7d-a1cd-c76f247fb97e | -7.50872 | -44.63773 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 870c87da-a76a-3e79-811d-d9ed0304ba64 | -5.48775 | -43.07082 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5d7d246-369e-3f16-aea6-a7d7463d0b1c | -3.44901 | -45.6062 | 2025-10-12 04:42:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e044780-4abb-3834-a13b-fe3a6a43b779 | -4.42502 | -43.47029 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd55ecb6-f289-3c78-99d1-faa21603ba3e | -4.61641 | -49.53917 | 2025-10-12 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b51a6ab-ee8d-3926-b744-6655be593085 | -7.65625 | -42.5905 | 2025-10-12 04:42:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 10605103-1fa6-305f-83a6-5de6d1e3472a | -7.03359 | -45.49703 | 2025-10-12 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6173b9b1-644d-3606-8b9c-8f76d9ffad5b | -5.67213 | -42.68146 | 2025-10-12 04:42:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb939866-466a-32cb-b125-1437693a0632 | -5.80232 | -51.50032 | 2025-10-12 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d06e0af0-d173-30c4-ae4b-a5c99d38558b | -7.49169 | -42.76692 | 2025-10-12 04:42:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 015c0b0a-daba-3bf0-9ca2-fc68beb64eb6 | -8.47853 | -46.23595 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 109b8dfa-6052-38c1-a078-be60274b4b37 | -6.78874 | -44.52274 | 2025-10-12 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3a2b4d5-59ae-3924-9673-0d36437ac990 | -4.4044 | -43.52204 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b85077a-d2cf-3631-b8cd-07b7813b29a4 | -4.81848 | -43.14185 | 2025-10-12 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e667e73a-f9af-3eb1-bcaa-66404d744b2c | -8.3291 | -46.2341 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fda6feb-2439-3f88-914d-8e83d082b3bf | -5.93819 | -43.94365 | 2025-10-12 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18ee3cec-7623-3598-8706-56b7617c4ea6 | -6.74047 | -42.15293 | 2025-10-12 04:42:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a6c9c42e-772b-3d74-b9fd-f6bc1da61e03 | -7.05549 | -45.21575 | 2025-10-12 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3fddc6b1-2151-32c1-a1e4-8b863ae4ecaa | -7.52023 | -46.5422 | 2025-10-12 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 077a48d3-3ef4-3cc5-b44f-12ca4fd9996d | -7.79509 | -42.434 | 2025-10-12 04:42:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ca8d3436-35bb-3e6b-94b8-f92a6b514c91 | -8.47706 | -46.1949 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 773d9d82-4a99-33a9-a178-e14d4772e172 | -6.80619 | -47.05167 | 2025-10-12 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a8427f1-bc38-36ab-a7fd-48d514d6d3ba | -7.73836 | -42.41949 | 2025-10-12 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d660c12f-2152-352d-b6a4-cfc2dab2d638 | -7.89368 | -47.07254 | 2025-10-12 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce654451-68e4-39ba-a36d-ce0b2bf909fc | -3.25769 | -50.05273 | 2025-10-12 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af977a31-f877-3321-b816-904d641cd798 | -5.86462 | -42.84084 | 2025-10-12 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8a0d9738-8b8d-380c-9809-65aa5f540f4d | -2.87999 | -50.73498 | 2025-10-12 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1eeaab3b-da2f-3039-b828-f39d5d68d9b0 | -3.61045 | -42.74575 | 2025-10-12 04:42:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1467d4ef-f767-3668-9091-1cffb9f888eb | -4.27634 | -46.93353 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dc50913f-2a71-38b9-a9eb-52ac6a9d9bfa | -7.64821 | -42.57947 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 110905d4-2b01-3a54-a9b1-785c6448cb34 | -8.33217 | -46.23913 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2adb1cc-7ab0-3cd7-8da8-305c4fc242e9 | -3.53044 | -48.91744 | 2025-10-12 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f92b4d03-8d93-308d-93eb-bec2fb32f893 | -5.17911 | -45.43682 | 2025-10-12 04:42:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0de36dda-d9c3-3f40-ba04-d27e3fab02d2 | -4.27228 | -46.93677 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39e9adfa-ce5e-3690-8cf4-e51a0333316a | -6.57132 | -39.56344 | 2025-10-12 04:42:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 916d177c-ace9-3d94-8398-53290efbf914 | -7.43389 | -42.97725 | 2025-10-12 04:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 758529d1-2208-33b3-a68a-fe177eec2c52 | -5.47701 | -43.39251 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd695892-28c9-313d-acb4-dafb3507bfd4 | -3.87395 | -42.51037 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 74c2080c-ba0d-3db2-b29d-4bad7c614ada | -3.27715 | -52.95932 | 2025-10-12 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f7414de-7715-36da-a1fa-85052386a0f2 | -6.71029 | -42.88812 | 2025-10-12 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a6223ba7-17cb-302d-9ab8-f27d1b8ab13b | -3.53266 | -48.92137 | 2025-10-12 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 55bec592-7bdd-3f8d-b7e6-31071cb7eab0 | -7.85363 | -44.51326 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 479b592c-255b-3f6a-b109-cdd43415b796 | -6.57944 | -45.97754 | 2025-10-12 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42e847ed-9340-3cbf-b71f-5801e2f216e1 | -4.61782 | -45.77653 | 2025-10-12 04:42:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2f97f5d-c877-3fdb-97ea-7d83ba862aec | -5.91208 | -45.42518 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 110ded00-7fdd-380f-89d6-e64830125d0e | -7.14854 | -42.4991 | 2025-10-12 04:42:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 670ee339-ae6a-3393-b49a-c0d7b48e0b96 | -7.50297 | -45.12797 | 2025-10-12 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a939f397-6451-3aa9-bc87-c86b6d4a73aa | -8.82964 | -46.04588 | 2025-10-12 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a79149c6-5eb1-3733-9be4-ab7dba1b8004 | -3.94763 | -52.17692 | 2025-10-12 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f45d66e-5def-32ba-bfa2-65f8982c572c | -8.70813 | -46.83435 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 360d31e0-b8af-33c3-b57e-5739b0ed7c6f | -5.37317 | -45.04304 | 2025-10-12 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39c03ec0-1f12-304f-9bfc-0bd2bd0046ce | -4.27499 | -46.93275 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b559d287-2c32-3c99-afe9-9bd5793c0818 | -6.28055 | -44.40741 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03d97f24-4368-3c85-b299-328bb0843ea7 | -7.20328 | -45.48845 | 2025-10-12 04:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dcc73eb7-1b43-3092-a5a8-739622366501 | -6.58461 | -44.6192 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 5fac6495-59b0-3308-ba32-432f3ff415dc | -4.82403 | -43.13432 | 2025-10-12 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3daf3b2-b774-3ddf-9ed4-732fdbec3ec4 | -6.49572 | -42.43647 | 2025-10-12 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 085cd2fd-3af4-3b63-866d-3d26d4047172 | -5.33545 | -43.42783 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2d9c953-bdd2-35c5-8984-9ee728d2b2d5 | -4.45886 | -50.09922 | 2025-10-12 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3143572b-1048-3ef4-883d-94c5abc7b750 | -4.94344 | -44.76768 | 2025-10-12 04:42:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df8b3bca-38a6-39e2-816d-a9c6ab901f8c | -7.86034 | -44.52494 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7eecfe3-575a-30cd-9d09-1190aab125db | -4.2796 | -46.92575 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4826cb88-4eb8-39ec-829d-f5fe6bb78187 | -6.25722 | -46.01846 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76a58967-52f2-37c5-877b-4ae0e5a6c733 | -6.78927 | -44.51925 | 2025-10-12 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce05af48-0851-347c-b454-13e78f114a51 | -7.8526 | -44.52033 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1f5177a-9edb-3e9f-b657-b50bdc31f601 | -7.64889 | -42.57461 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e58a8561-c02a-32a7-aae7-97470cd20cfa | -6.88769 | -44.69591 | 2025-10-12 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e5ccd21-55ee-3ee0-8ae0-372b0b52c212 | -3.92415 | -44.32446 | 2025-10-12 04:42:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f182942-eff5-3816-aedd-66f77a7846a2 | -7.88467 | -44.46024 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d48775bc-483e-3bc6-be28-8b190db09e34 | -6.4659 | -44.638 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74c5479d-4468-3a6a-a308-2ef0378c2e10 | -4.54159 | -49.68785 | 2025-10-12 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a029a027-ea52-3d6e-b171-738b740f8e36 | -3.50527 | -49.05515 | 2025-10-12 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e96b9835-373e-3c43-88f9-5be8058ed9df | -7.18823 | -43.31466 | 2025-10-12 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a81b29be-b1fc-3554-a7d1-7d8b90ab6207 | -5.25639 | -46.15326 | 2025-10-12 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27f74a73-8116-3539-afd5-c6e4e330600b | -2.4383 | -49.36094 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d751816-d7b6-3264-bf7e-ffd81a67439e | -7.42999 | -42.97208 | 2025-10-12 04:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9f18dcd2-6844-33eb-b619-f301b43772f3 | -7.67776 | -42.57378 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7be9cdca-6a9e-3dc2-94d0-7892a0758d03 | -6.77065 | -42.82582 | 2025-10-12 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4306b8dd-ba81-30d6-98d7-818fc3c031f3 | -7.69114 | -42.37596 | 2025-10-12 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7738da4c-b390-3312-89ce-fed61532a866 | -7.68245 | -42.57449 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e2d16475-5dff-3d91-b0c5-c218121c4ca9 | -6.16697 | -44.67154 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d45a7d6-0fe6-3b42-ad7c-5ac42956fb7a | -5.36245 | -46.29295 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7464ace6-a281-3231-ba79-359bb897cdaf | -7.40206 | -42.97242 | 2025-10-12 04:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| de7a7898-a6a2-351e-ac79-a47e77456a63 | -4.81725 | -43.14999 | 2025-10-12 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc63f281-8f58-3d47-8428-cd6481a09c14 | -6.9903 | -42.03699 | 2025-10-12 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8a22f62d-6bff-3158-82a8-9047e811e52c | -4.78748 | -43.0823 | 2025-10-12 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62e2876d-12ec-3aa2-94e5-f370a38e4fdd | -6.75707 | -44.65123 | 2025-10-12 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64c42bcb-07d8-305b-b3fc-2031bdd3c990 | -3.87435 | -42.51738 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b27b647e-d2eb-35e6-953d-2914aa981563 | -6.73977 | -42.15786 | 2025-10-12 04:42:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| fa7e2d95-c549-3915-a565-f273ca2fc1aa | -3.53931 | -48.92242 | 2025-10-12 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45ffab40-df17-3825-8837-b41d8e32f64d | -4.66334 | -49.387 | 2025-10-12 04:42:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cf30e0b-3627-3dd1-9198-549f4bc48a28 | -7.51813 | -44.60228 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 906a7c97-17e4-3348-9de1-fd2539eb8b35 | -7.26226 | -44.14898 | 2025-10-12 04:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aadf3cf7-f403-3513-a521-43a5bffcc5f1 | -5.33852 | -43.43639 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1627a5e-abb4-343c-95da-2f56fbf289ec | -7.40141 | -42.97701 | 2025-10-12 04:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0a7323f7-d581-35a2-9d40-6ed11ae64e30 | -11.67615 | -43.77839 | 2025-10-12 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| db288537-1a26-362b-936c-ff4ec76e4ee7 | -8.95336 | -48.66449 | 2025-10-12 04:44:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README33.md)
