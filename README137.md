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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 090b801d-2efe-316f-90e3-730df53d9185 | -11.6621 | -50.2169 | 2026-09-20 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 34496b14-c633-33da-bff0-113a2d1e71b8 | -3.6077 | -59.0577 | 2026-09-20 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 06556a69-18f4-3568-83c7-e3992a3ee27a | -8.1686 | -54.7634 | 2026-09-20 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 213.8 |
| 8dbba542-721d-3443-a5cf-18712d8558ce | -6.3471 | -58.2973 | 2026-09-20 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a233bbaf-9492-3160-a9a9-096368bc6e9b | -6.1653 | -47.5052 | 2026-09-20 15:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| d2759091-7c8e-3d1d-b9c9-20c0610dd305 | -3.6076 | -59.0769 | 2026-09-20 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6e92dde8-e52b-3955-8cf6-90c30d69b13f | -10.9692 | -57.208 | 2026-09-20 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d3d784da-ef4d-3356-8147-75386f9233e5 | -10.6143 | -50.5884 | 2026-09-20 15:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| bbf1d6f4-f794-31b5-a2b7-ae795198c189 | -9.0355 | -60.3589 | 2026-09-20 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| cc33f795-8aeb-3b5d-8219-fa5908f6e1aa | -11.3609 | -44.1286 | 2026-09-20 15:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| b0b824bc-1328-3c55-9b93-42f25192dee4 | -10.7612 | -50.9132 | 2026-09-20 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| f0f1e2e6-fe1b-3023-9d1f-0e3fd5aedf0f | -9.2682 | -48.2034 | 2026-09-20 15:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 63a8320a-d8ea-3ad6-a608-b1e9816c6bab | -6.737 | -55.0674 | 2026-09-20 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 3c4e6b81-1114-3d2b-b795-7d1844c9cb3b | -7.0615 | -47.5265 | 2026-09-20 15:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 0ef54c88-eea9-32b6-9fd5-f07ad3d2beca | -2.8974 | -57.7987 | 2026-09-20 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 80314289-6a76-36be-89cd-922a1fc618f4 | -8.0708 | -55.3321 | 2026-09-20 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 3da47daf-576b-33b8-833e-afa9fbf7115a | -6.5829 | -58.9851 | 2026-09-20 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 937f2ea8-cf8e-3679-b88b-cc262068fedd | -8.1684 | -54.7836 | 2026-09-20 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| c6b4764b-6384-3a83-99fa-9fa34a767066 | -9.2603 | -45.939 | 2026-09-20 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 688989a2-de85-36b3-aa16-3e4384db0540 | -11.041 | -54.1567 | 2026-09-20 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 188.0 |
| d59f8600-e8f9-3729-a6da-20e4482e48b1 | -10.8759 | -57.1355 | 2026-09-20 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| eed9a6d9-78af-31a7-b25c-7b91a6ee661b | -10.8757 | -57.1554 | 2026-09-20 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 191.0 |
| bb45ed0e-944f-327a-bcc6-677664513b0e | -10.8553 | -50.9459 | 2026-09-20 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 346.5 |
| f7879f10-f578-3046-9356-6a66992bac98 | -11.9352 | -49.7752 | 2026-09-20 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 200.5 |
| 75920c51-3dd6-3fa2-9487-0d0bb6c66047 | -9.6668 | -54.3129 | 2026-09-20 15:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 2c3ad0fa-fefb-3d2b-aee2-b6c82ae5f71d | -11.9349 | -49.7968 | 2026-09-20 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 179.5 |
| c9a79cef-3ef0-3907-8f93-6b7c42a86078 | -11.9493 | -50.0971 | 2026-09-20 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 2aa4ea0e-e86f-35e6-9f34-1c637753789d | -6.4941 | -58.3884 | 2026-09-20 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 1a9bdebb-a416-3684-a21b-0229e1f49ba3 | -3.3492 | -59.867 | 2026-09-20 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| a40d7f48-323d-3dfe-8c7a-4e0261b6bac5 | -9.0544 | -48.7469 | 2026-09-20 15:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 151.4 |
| d74d6401-d0c9-34bc-bfd3-c09f94fe126a | -2.8791 | -57.799 | 2026-09-20 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 214.8 |
| 9c4cac73-4277-3183-a662-1303073b1d84 | -10.5535 | -57.4567 | 2026-09-20 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 50cee97f-be76-365a-8435-da5cee77804d | -5.9814 | -57.7867 | 2026-09-20 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ba6c448d-8bd2-3ec6-8033-e2a3d4cf5eff | -10.8367 | -50.9266 | 2026-09-20 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 228.0 |
| a47122d6-ac99-39e5-9835-c16a20a45dc5 | -11.0259 | -48.2944 | 2026-09-20 15:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| befc33b2-7550-3493-91db-7c721b8d044d | -9.6665 | -54.3332 | 2026-09-20 15:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 45f1bfec-363e-3452-9a38-baf447fc6f81 | -3.4454 | -58.2327 | 2026-09-20 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e97a05ea-13dd-3894-bd21-1ae0fca44cee | -6.9851 | -45.8235 | 2026-09-20 15:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f58f7c76-6092-3edd-8ac6-84c08fb00a0b | -11.0412 | -54.1362 | 2026-09-20 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a3d73685-5a87-31a6-863b-0cc1ce0c41b2 | -10.7466 | -50.5959 | 2026-09-20 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 9968d51d-4f8a-3a37-8291-63e5fdc139c1 | -7.2519 | -55.5994 | 2026-09-20 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| aef62e66-2fde-3c84-a917-179cb76f2edf | -6.4942 | -58.369 | 2026-09-20 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| cba29e94-db8b-3abd-94dc-766c6b9c4062 | -10.8569 | -57.1568 | 2026-09-20 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 02ca30c5-6820-3d1e-a62a-2de9a83b2686 | -13.3964 | -51.6317 | 2026-09-20 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 131.8 |
| ffc6696d-0ebd-3aaa-a4e6-8f6765fcfa5d | -3.1079 | -61.408 | 2026-09-20 15:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 6a4e7d53-37d7-391b-9e16-d84a8244d6e8 | -11.0407 | -54.1772 | 2026-09-20 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 98cb248d-6fcf-38d7-af22-33e9273b1aef | -9.3575 | -50.1156 | 2026-09-20 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 9f90ee4c-c123-360e-b301-4bfe1a6d1ec2 | -12.026 | -50.0663 | 2026-09-20 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| fa2d53d4-ebba-31d1-8d68-85edca4277f1 | -8.1688 | -54.7432 | 2026-09-20 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 2ff307ad-ded3-3de7-a0c6-c5f9fe22ad6c | -12.0263 | -50.0447 | 2026-09-20 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 354.7 |
| 8557eb14-1f8f-3bd0-90a8-48f343b52557 | -2.8962 | -58.2825 | 2026-09-20 15:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 77e131c4-9e61-3c22-9b9b-0e073859f606 | -6.3656 | -58.2966 | 2026-09-20 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d85d31a4-3f40-3e54-921f-c361d75e9131 | -1.75 | -54.9317 | 2026-09-20 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3594a9ab-cf64-3abb-95de-3690caa1c37a | -10.0956 | -48.4226 | 2026-09-20 15:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| eab4aad1-bb4f-3816-9c92-336fc8e6bf76 | -9.699 | -54.8176 | 2026-09-20 15:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 93e30b8a-36ed-32d5-98a8-e88645ec5141 | -6.1981 | -55.4534 | 2026-09-20 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 68cac578-42fa-3bb6-858c-25f3a1e29d87 | -7.3564 | -44.4726 | 2026-09-20 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 402cc392-8cf2-3df3-a78b-df6f64ba2a0e | -10.41 | -48.933 | 2026-09-20 15:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 0e5bdde9-9b19-38f9-8476-9d43df870356 | -7.0428 | -59.2173 | 2026-09-20 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a5dac402-c4f4-3653-ad8e-f48f7d2edde5 | -3.7347 | -59.4002 | 2026-09-20 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 3d57b33e-a2d5-3ddf-8c4f-81d4aede66ba | -13.3772 | -51.6341 | 2026-09-20 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| f080c348-5b96-3549-964a-7ee7bfd43505 | -10.9665 | -49.7583 | 2026-09-20 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 90707a48-8a22-3b29-b68d-e52e8535c989 | -9.7311 | -46.0886 | 2026-09-20 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 975ca2b3-07ad-3906-8b65-0aa8879fc402 | -3.4003 | -61.2898 | 2026-09-20 15:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| fdf849e1-0fff-312a-a749-3359ccb6cd3d | -10.1145 | -48.4205 | 2026-09-20 15:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| ab1f9488-af33-3fc8-98c4-f89b3941c687 | -9.2606 | -45.9164 | 2026-09-20 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 5fafb57b-4849-3142-8f92-5c081d7365a7 | -9.6853 | -54.3318 | 2026-09-20 15:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 45d23ae8-7542-3c41-ba76-40526bda1605 | -7.3912 | -44.7216 | 2026-09-20 15:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 808266ce-f83d-3486-8e82-6ddc7ec96125 | -6.0925 | -57.6847 | 2026-09-20 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| d3f9361e-af2b-38ce-8c96-7162a31a3ff6 | -3.331 | -59.8292 | 2026-09-20 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 278073a0-de6a-3116-9bb9-ac8b291f2f68 | -11.0223 | -54.1379 | 2026-09-20 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| af710e24-7526-3dae-adb6-fec0d7cc23d5 | -2.8961 | -58.3018 | 2026-09-20 15:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| de928178-1499-351d-ba2b-6c8a4e5800f5 | -10.2787 | -50.2605 | 2026-09-20 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| e30574a1-c7db-36e8-acce-398ef1f659d1 | -3.5356 | -58.6939 | 2026-09-20 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 73ab96d5-1ea1-3536-af90-ee64f87f77ed | -5.8088 | -55.7095 | 2026-09-20 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 105d75b0-34a1-3565-98e7-85f11962db20 | -11.8487 | -46.8781 | 2026-09-20 15:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 928ba3dc-379d-3e8a-98ee-13fee39fd24c | -6.347 | -58.3167 | 2026-09-20 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 7c2f9214-a8d4-3299-8de4-81761e4eb793 | -9.2563 | -46.2323 | 2026-09-20 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 1ca373c1-b477-3980-9293-4b4f1c566888 | -5.9982 | -52.183 | 2026-09-20 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| b709cac9-2410-360f-bb32-96e4f59bb40c | -11.6624 | -50.1954 | 2026-09-20 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 2adb6fe9-b468-3304-8548-ebbcdfe44066 | -1.7499 | -54.9516 | 2026-09-20 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ce766cf6-ecef-3029-b1fd-fc43863391b5 | -11.4545 | -45.3432 | 2026-09-20 15:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| a6e5fc77-3587-3358-9ed1-c1c25a7b04fd | -10.7463 | -50.6172 | 2026-09-20 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 47f914b5-7e06-38e3-9169-463f878eaeeb | -3.3866 | -59.5797 | 2026-09-20 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1f6860f0-a708-395a-ac30-b575e9a40da3 | -3.6946 | -60.5835 | 2026-09-20 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 375.4 |
| de7d719f-0b24-3057-915c-e2db4b000775 | -3.0534 | -61.2767 | 2026-09-20 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 1f752f3a-30c5-3ce5-b5bd-359c530290f8 | -10.8945 | -57.154 | 2026-09-20 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 1d5330d8-9ff3-3d8a-b74f-0a6c4cdc69f5 | 2.7269 | -60.2966 | 2026-09-20 15:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 278129d4-ed7e-32e1-a8b0-cc492389c142 | -7.1203 | -42.083 | 2026-09-20 15:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 128.8 |
| aa23cf69-321d-320c-bb05-1b8cc3e42e3e | -10.8177 | -50.9286 | 2026-09-20 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| fefa4bb9-bded-3953-9a94-65ddc9494562 | -6.1231 | -55.6359 | 2026-09-20 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| abf654ec-0eed-34c0-941a-0bbee5440610 | -11.0506 | -54.9309 | 2026-09-20 15:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 757.0 |
| fd548dfe-22f3-3e58-a507-a5062bb578d5 | -3.7347 | -59.4194 | 2026-09-20 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c5214ef0-bee6-3ed5-9ae6-0283fecdd59a | -9.3572 | -50.137 | 2026-09-20 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 5facfb98-8ff5-363b-9e81-70af3e733b5a | -7.7661 | -44.823 | 2026-09-20 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| b9ebac16-c8d6-37bb-b3c6-5b2bac648f08 | -11.0221 | -54.1584 | 2026-09-20 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 6cdabfe7-0e51-36ae-90ea-9f3671cc3fdf | -1.5858 | -54.4552 | 2026-09-20 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| fa677309-dcdb-300e-b341-ee57b91070a4 | -7.3073 | -55.6163 | 2026-09-20 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 05b50bca-945a-3b18-8c44-db91fd4a75d4 | -8.1871 | -54.7824 | 2026-09-20 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 5723d542-1067-30ea-8258-2770e29fc0d3 | -11.1222 | -49.4818 | 2026-09-20 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |


[Clique aqui para ver as próximas entradas](README138.md)
