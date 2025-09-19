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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a388fe6-039a-3c75-8983-d8565030ae8d | -7.61114 | -44.62117 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f6aa80f-2ebf-3776-a98b-22c9037ce849 | -8.54929 | -47.54853 | 2025-09-19 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfc28c03-3de0-3ed8-aa45-349c2aef50f3 | -7.49185 | -44.40192 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1651bdeb-d54f-39d3-9779-937030ababf2 | -7.31747 | -44.05342 | 2025-09-19 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 822dc4bc-048a-3bb2-b040-a61e2b0c5764 | -5.79649 | -45.35495 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55f3833f-d997-3f5f-b086-d2c9e8b45f3a | -7.54116 | -45.50416 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1a119a6-60d1-391f-b3ac-fc701c51d760 | -7.54572 | -45.505 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2584b38e-07c1-3210-8ef7-10de16e6415f | -5.70465 | -49.10157 | 2025-09-19 03:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc7a180b-ca46-34a3-84f3-8783419e7c02 | -9.01452 | -44.9063 | 2025-09-19 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b54019f6-be46-36c3-a763-286f60e8ebb6 | -7.29173 | -44.12798 | 2025-09-19 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 754f4347-4330-3e8e-8df3-66f0f8c3227f | -8.63116 | -45.70875 | 2025-09-19 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b315ace6-d52e-3824-a33b-eeb6a12225b4 | -8.1429 | -43.62597 | 2025-09-19 03:53:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6df4acb3-2615-322e-bb8f-d742d53468be | -7.87065 | -45.64073 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 51fa21be-0220-3ffa-bff2-221cdf7ca803 | -6.95957 | -44.76429 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 49d152e8-8524-317e-97e8-38b86ceebee1 | -5.21076 | -42.31395 | 2025-09-19 03:53:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e1ab9530-2aab-3370-bd62-0fcb05bc9119 | -7.30851 | -44.05573 | 2025-09-19 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 339bebfb-96dc-37f7-8678-12a27706fd78 | -7.45659 | -38.7729 | 2025-09-19 03:53:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 29b31d42-3a52-3a24-a9de-4dcd3600cb4f | -7.70971 | -44.39705 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4a6ef20-9aeb-38f0-80ca-1555df888700 | -6.95202 | -41.30144 | 2025-09-19 03:53:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a056419d-770c-3ec9-b26e-bf551869cbd6 | -5.91943 | -45.0773 | 2025-09-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f575d305-20e2-3505-b504-8c18d2004aa8 | -9.13962 | -44.63757 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a33ea5f8-fb10-37dd-9ad0-3f1c4af2fc58 | -5.13055 | -47.83301 | 2025-09-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c4d2f160-3a5d-3f9e-8622-15825ce96040 | -6.20158 | -43.92566 | 2025-09-19 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c78e6bd1-c1f5-338e-b0db-a12616bdedf9 | -5.80787 | -45.71521 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6563c624-bf3e-3473-b975-f5596f8e0a73 | -8.37753 | -44.6812 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2741f3d4-d759-346b-b703-1074903b84c7 | -9.0375 | -44.87572 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e238bee3-5492-396b-b6f9-e891757090b1 | -5.45527 | -46.69566 | 2025-09-19 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b8bd4a7-7ffc-3b3e-85c9-2bff145c3f54 | -7.2899 | -39.31051 | 2025-09-19 03:53:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9f2dd10f-7085-3af5-a60d-2ea5de216b28 | -7.44878 | -42.64439 | 2025-09-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f3e2dd8a-9389-3493-8eba-4cee06edff13 | -5.47579 | -44.11477 | 2025-09-19 03:53:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 953da212-764f-39bd-9a32-60b2b846d31a | -9.17738 | -45.315 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 648fd160-a060-3d38-9ed6-9cc075c55a04 | -5.76058 | -43.39218 | 2025-09-19 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf7688b0-6b0f-3cc9-8850-2ebc727a438b | -7.31875 | -46.60504 | 2025-09-19 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b4c3c2de-7a40-3216-af88-cd7d2c6f5335 | -5.75998 | -43.39582 | 2025-09-19 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 219b3352-76cb-35e5-9e16-fef760c18e3f | -7.87147 | -45.63598 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 315f3799-a4dc-3aeb-b40b-d9fd93bc3a9c | -8.02911 | -45.70351 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4e12310-a040-3659-9ca4-e3459c7a226e | -7.28621 | -44.13501 | 2025-09-19 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df3ebb5b-5528-3f4b-8211-1a9e14dd8ad8 | -7.58249 | -45.48232 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 24115d2a-a973-3458-847e-cbaa157ef42d | -7.50067 | -45.29902 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 630ac921-d2ba-32b0-af22-ac06e963af3b | -7.23235 | -46.59672 | 2025-09-19 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0028ef9-66ad-3b6d-a362-526f20a7a366 | -8.54871 | -47.55172 | 2025-09-19 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 062a1e24-1b5a-336c-81b7-55fb21e0e839 | -8.06119 | -44.07401 | 2025-09-19 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 068c1c8f-bac7-3c68-9253-afc7ddd42f44 | -9.18176 | -45.3158 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4b3eed5f-eea9-3512-99dd-4173a4ac31e9 | -6.24963 | -46.11932 | 2025-09-19 03:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7c35f3a-66c6-33cc-94b7-e4aab332aec9 | -8.62658 | -45.70817 | 2025-09-19 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5dcad09-9d5f-34c4-9166-76b62b7d09b8 | -7.5097 | -45.30043 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2709e6ad-340d-35f2-8f24-d035ae8cb485 | -6.59167 | -45.58218 | 2025-09-19 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49580e05-435d-3113-bca6-f3bddd049302 | -5.83068 | -46.28027 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c7485fe-89d7-3529-b14e-a48e16a2c759 | -6.20609 | -44.0537 | 2025-09-19 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18a0f82f-0959-3791-871b-a2d086908a08 | -5.08865 | -47.51981 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43ca7b91-6f63-336d-a855-316782cc8c4a | -9.04177 | -44.87645 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ede55b3-41bb-3e19-ba1f-967156875f27 | -7.08752 | -41.40619 | 2025-09-19 03:53:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3069d6cc-577a-301e-ba7a-8e3c3d31505a | -7.99256 | -43.94098 | 2025-09-19 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a47a4a6-4085-393d-b9fa-9772c7c7c9a4 | -6.93372 | -44.75598 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80d4d0f3-eb3e-34b5-b604-830103f31a37 | -5.77784 | -45.97073 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e45e83c5-0c7f-3d63-abec-1722fb4f2b56 | -9.14512 | -44.85667 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3f41644-2f9e-396f-8ecf-9a608ccea539 | -8.74856 | -44.23446 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dceec6b-9488-3755-adc8-397afea3a25f | -7.04235 | -42.00815 | 2025-09-19 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 481edd00-0510-3418-8bd6-887049574f74 | -9.173 | -45.31422 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bfa6ed9-d0af-3551-af0f-e36788252834 | -5.5019 | -37.79379 | 2025-09-19 03:53:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10b18af9-e713-3849-8966-96d4b501f1c6 | -9.18464 | -45.32514 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fd485f9-5243-315c-99d7-559554792314 | -9.02539 | -44.97014 | 2025-09-19 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dccbffa-060b-3acc-8fb6-e012c0defdfa | -4.95846 | -42.81706 | 2025-09-19 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9568ec82-66d2-3747-b901-dd44a7e7b55c | -7.23728 | -46.5977 | 2025-09-19 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b085d9b-3ea9-396f-8f2f-580a1981d0dc | -8.37743 | -44.67471 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32a9ce15-2487-319c-9673-b92e2c2f8610 | -5.12498 | -47.8321 | 2025-09-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bc20ed9e-8cb8-38b4-997d-71bb2ba293b2 | -5.95715 | -47.0954 | 2025-09-19 03:53:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b24f95c-3163-399c-aa0e-39f4854215a2 | -5.24832 | -38.17436 | 2025-09-19 03:53:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 058c638c-cc0f-373a-9e95-146f7d42714c | -6.7599 | -46.00946 | 2025-09-19 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9354d29c-67f5-3da6-be9c-f95a74f65b63 | -5.66278 | -45.03756 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95810c34-9c12-3a75-86b7-ebcef36ed569 | -8.48452 | -44.7335 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9db52296-f43c-32dc-8eaf-071940bfc101 | -9.17224 | -45.3185 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68bcf4f5-178c-316b-876c-584c32fa2dd6 | -7.86847 | -45.626 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72ea4f12-2751-3940-92da-36e229d99e81 | -7.35853 | -38.96363 | 2025-09-19 03:53:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7c1a5263-e1b5-3bf5-b75a-9f2d4fa0de26 | -8.54812 | -47.55491 | 2025-09-19 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f686551-aeda-30d9-a994-b0aa43717997 | -7.5771 | -45.48642 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f05ddc45-6f50-3336-aa85-d07aadc50154 | -5.4682 | -44.69065 | 2025-09-19 03:53:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c153e1e3-3dab-331c-b804-4efa1d779b12 | -9.15434 | -44.8792 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dd72645-4407-3d86-a4d3-7124dfd227ef | -5.50244 | -37.79034 | 2025-09-19 03:53:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a446ed28-7948-3a43-a171-a66673cf3814 | -8.38097 | -44.67949 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a88fa3dc-40af-3144-ad18-cfcfd48ec7bb | -8.33645 | -44.63953 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6554297a-5d53-3458-b5f3-2943487bf59d | -6.75896 | -46.01474 | 2025-09-19 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f41671ce-f1b8-3f8e-94d2-7a21446701ac | -7.29105 | -44.13187 | 2025-09-19 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3a72244-9784-38fb-b2ab-c030164a7cd4 | -7.561 | -45.49817 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ac26a2f-247e-3fb4-9127-3f23fa4082e6 | -5.92615 | -43.93944 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a8799e9-d986-3c4e-aacf-2a7c61ea959f | -5.71923 | -43.64381 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1df4275-d888-39ff-b6cd-0f233fd75652 | -8.14243 | -46.78237 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 278cd968-f994-3656-8c87-8e37f22d9d7e | -7.55642 | -44.78577 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96f58a15-c46f-36cc-9e95-e8602253584b | -6.97884 | -44.48832 | 2025-09-19 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4eb131b-c30d-3c5f-8a76-ddcb320dfed9 | -5.50136 | -37.79725 | 2025-09-19 03:53:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4a410c3d-8bd1-3902-be0e-235d944e920f | -5.9847 | -45.86015 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f0cb455-3347-390c-9951-139d216d44ca | -8.21442 | -45.80114 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7362f02a-c37f-3739-99c9-b9d7fa4bc714 | -6.00504 | -43.70108 | 2025-09-19 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0328425c-fdc7-3d0b-9d04-f0319baa145d | -5.80172 | -43.90554 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41842298-d54a-37e9-86bb-09ce6c70c679 | -5.924 | -45.078 | 2025-09-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8c9a2965-297b-3ac1-9f85-0e731749bd3a | -6.76083 | -46.00417 | 2025-09-19 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 346a6977-d963-3da8-bd44-90ed087325ef | -9.18689 | -45.31231 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7432d6e-b655-3b5a-9305-5e59900506b9 | -6.95535 | -42.4402 | 2025-09-19 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 03e3a718-e16a-304f-bc3b-8a370f1e5fcf | -10.15684 | -39.07315 | 2025-09-19 03:53:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| daf58b1d-9c96-3805-8196-c090b28f2eee | -7.87757 | -45.62798 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README11.md)
