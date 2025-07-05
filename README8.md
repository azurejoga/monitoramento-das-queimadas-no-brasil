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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccaf236d-5fba-30aa-adac-f1509be2ffbd | -7.20762 | -48.18472 | 2025-07-05 04:19:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a4f982a-ddc9-343b-9075-0354c929924d | -7.23343 | -43.08956 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 45298019-d693-36e5-93c8-fc61e60fe1d4 | -5.99734 | -43.73769 | 2025-07-05 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c28f627f-3b0a-32e6-9d0f-68d094c51c86 | -5.5679 | -46.6721 | 2025-07-05 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b50acd14-67de-3f4d-b17f-f53a53d250c7 | -8.75717 | -43.95598 | 2025-07-05 04:19:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41465d1b-d7c0-3f1b-8c6a-55c5c5db0144 | -13.02343 | -46.30304 | 2025-07-05 04:19:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b90a947-f053-34da-8231-69c45f1a9fcf | -10.61163 | -46.4288 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fa0fec2b-1974-3dad-b09b-ce1e52eb43c1 | -11.87401 | -44.87282 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79c7f084-8dd5-3cd8-854c-63af5aa73321 | -9.51894 | -43.01318 | 2025-07-05 04:19:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 43010571-2520-3aea-81e9-01fdaaff4669 | -9.00036 | -47.44331 | 2025-07-05 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8d43f90-4413-3036-a5c1-39e84223b0a9 | -9.94783 | -55.20391 | 2025-07-05 04:19:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a87f5d9d-b8fa-3803-b70a-2d598370e6c1 | -6.87731 | -43.22077 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 44e9bae6-664e-398b-aff8-9878917ec541 | -11.72805 | -48.8718 | 2025-07-05 04:19:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb21dac5-3f99-3876-914c-344b9cceb10b | -7.61352 | -45.75077 | 2025-07-05 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87b1d334-1f96-3040-8ad5-4a66a295a277 | -6.60853 | -43.89025 | 2025-07-05 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2315a45f-d4d0-37ac-be24-fc57f27b5a5e | -7.23286 | -43.09328 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 67df7529-279f-3834-bc67-5fa06f86d0f5 | -10.56751 | -49.13216 | 2025-07-05 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3567fd8-1989-3fae-b97f-911e489f1799 | -6.01618 | -44.52761 | 2025-07-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68975b44-5e56-3bc2-acec-507058f31070 | -8.09182 | -45.39221 | 2025-07-05 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2f2f04ff-e907-3d5a-be9e-ea3762114974 | -7.30762 | -44.11105 | 2025-07-05 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 17af9477-463f-3e05-8e24-b14125d44157 | -10.32374 | -49.93431 | 2025-07-05 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94a4d37b-7371-3163-ac70-9a6737185374 | -11.88182 | -44.86656 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9546dc68-d36e-3ae7-ba22-2f094afb4430 | -11.8729 | -44.88005 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5f17b52-5b8d-3c19-8244-d63fb488bcb0 | -6.67517 | -43.87561 | 2025-07-05 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bac74ff2-9d69-3513-844f-b68393d23478 | -5.42737 | -47.1483 | 2025-07-05 04:19:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6d1eeae-4616-3e58-85af-ab51f0374418 | -10.61055 | -46.41415 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8f7af39-1849-3ca2-aed7-a0d5619f5018 | -7.30443 | -45.36594 | 2025-07-05 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67cd30b6-4bbf-3a48-a0e4-61d32b984eea | -5.72522 | -49.11176 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0059d394-86d3-3814-b8d1-4067d476caac | -10.5566 | -49.13023 | 2025-07-05 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a09c9647-b1c7-3ac6-a14f-e6ae8131d724 | -7.70301 | -47.28674 | 2025-07-05 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad2bd171-ee2b-3dcf-a260-f0d889398527 | -9.75733 | -48.26851 | 2025-07-05 04:19:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05ff80ac-cf5a-3081-ae52-f23753f10f7a | -8.37873 | -51.07195 | 2025-07-05 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f3cc3935-3d08-37e9-8da6-d948834a2156 | -10.36494 | -46.99137 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53e31c08-fd77-3392-8f21-c50ff4615c84 | -9.61148 | -49.01866 | 2025-07-05 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30b284ea-fea8-378d-b9a2-ab4a8c37b970 | -11.33441 | -51.44265 | 2025-07-05 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51d8588d-493c-3ee4-94a8-d973eebdd1b5 | -9.94909 | -55.2048 | 2025-07-05 04:19:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 909edae4-0551-3dc4-b1dd-01a9469df893 | -11.94448 | -48.42395 | 2025-07-05 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 881b3d68-3cf5-3854-ae4f-0c4abc3cf41b | -11.87847 | -44.86605 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30f88b4a-1552-399b-9fdc-8bd6e4adbea1 | -7.6562 | -44.35891 | 2025-07-05 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba37385f-f8ab-31f1-8814-208801db7b18 | -12.76057 | -44.40424 | 2025-07-05 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfabb3f5-f005-3083-88e4-44e526adfed0 | -6.79956 | -44.75383 | 2025-07-05 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0da488e2-dc0b-3286-93e2-e0228f52fc1f | -10.37165 | -46.99247 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09746cf1-6b7f-3003-b53d-816022a1ad8b | -7.23001 | -43.08904 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9992170f-274c-388d-af84-d2d6a03afd13 | -10.55258 | -49.43902 | 2025-07-05 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a5f4938-1366-358b-afdd-61f206c2aae9 | -9.95326 | -55.20493 | 2025-07-05 04:19:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85456ee4-a5ab-3a56-8a85-a3c24384fc85 | -7.2883 | -45.7021 | 2025-07-05 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8beadeb-0901-39af-8d7f-b02c0780c099 | -7.22289 | -43.08809 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d600e3a-1512-3d98-a122-ea4135854e5b | -10.888 | -56.45715 | 2025-07-05 04:19:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6a90223-b5be-3f00-bccb-69631bc784a6 | -10.56388 | -49.1315 | 2025-07-05 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7f525f5-af1b-3fa3-9d20-a2587fb9bdee | -10.6216 | -46.38736 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3cf93fb1-e9ce-3e78-b0c3-983802607e6b | -9.58381 | -44.6062 | 2025-07-05 04:19:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0270412d-b31d-3167-ade6-6897b41a2783 | -11.02215 | -56.25772 | 2025-07-05 04:19:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f60bb5c2-adc7-332a-8608-7d42dc141a69 | -6.773 | -44.14217 | 2025-07-05 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2709cfeb-0ed5-38c4-978a-224a7798d1f9 | -8.09732 | -45.37889 | 2025-07-05 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9b1da8d-4f37-366f-bb0a-b2a26dba03ec | -8.09677 | -45.38234 | 2025-07-05 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 768617f4-1012-3d0e-a846-e3343b94f18d | -8.00908 | -49.71952 | 2025-07-05 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 986f91c6-8562-3691-b7dc-fcf1c2ead408 | -10.66414 | -46.39787 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45567c37-118d-360e-b495-1deef85a2e15 | -6.60908 | -43.88673 | 2025-07-05 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e52790aa-4872-3dd2-b5a5-878c6fb514be | -7.19146 | -45.32688 | 2025-07-05 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8a634ba-fdf0-3106-86f6-a03dfcc86607 | -10.60887 | -46.42473 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e5fdaf02-f5c0-306c-b7c8-c08c14159f06 | -10.81971 | -54.02083 | 2025-07-05 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2965e8b-2cc4-36b9-8729-5e9afc95b020 | -12.01405 | -47.76909 | 2025-07-05 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0387c31-7993-3f14-8daa-254c725a108f | -10.61652 | -46.41901 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2db5609d-d676-3013-b978-8d95f0a75316 | -8.9957 | -47.45026 | 2025-07-05 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8f5d25c-1913-3ed7-ba83-a3e316383cef | -10.61596 | -46.42254 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c5dad54-03b8-38f3-bb59-27d5f0c44916 | -6.54853 | -46.4406 | 2025-07-05 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8707a1e6-b225-3abf-97aa-f74c41bc9db7 | -5.57133 | -46.67265 | 2025-07-05 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e0b3b2d-b494-3d2f-a2f1-aa4cf8cbf9a8 | -9.00318 | -47.44764 | 2025-07-05 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f736b38-6520-3a6a-bb25-fe7820aa9cee | -6.71766 | -43.11767 | 2025-07-05 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 959d2000-7454-304f-bfd8-ac7bac3f9eb9 | -12.05093 | -48.54586 | 2025-07-05 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 482efe3d-83ec-3c36-b968-c909f79b9128 | -12.94921 | -47.13299 | 2025-07-05 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c6cb641-a5d0-3f6d-bd77-12b4c7cf8c7c | -8.00993 | -49.71651 | 2025-07-05 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 921ff0be-1bd0-382e-8aaa-84441448996f | -8.08521 | -45.39117 | 2025-07-05 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ec8d160-e9e4-3964-a418-6ed1aeed71c6 | -11.1052 | -48.90575 | 2025-07-05 04:19:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8533b7fa-8cb4-3ca4-ab50-90711aada974 | -11.43744 | -45.10868 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0de819a9-ea68-304a-bcbf-022e2198d0c7 | -12.05181 | -48.0752 | 2025-07-05 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a928f28-92d1-36a2-9163-2c024211a7ed | -12.68875 | -44.60285 | 2025-07-05 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f083b502-38e6-3588-a541-e1aa222cbec0 | -5.87307 | -50.15022 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 330bc0b6-2704-3531-8529-373bf8ce8e82 | -6.75585 | -44.61974 | 2025-07-05 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 94cc7f48-4082-340a-8d27-bf06fe73fb35 | -5.99401 | -43.73717 | 2025-07-05 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6a04aa9-ac88-344a-b0b0-9475a8ff261c | -13.11977 | -46.91677 | 2025-07-05 04:19:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5b1ef4e-3120-396f-b51d-2598be832cac | -6.01287 | -44.52709 | 2025-07-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3339d74c-7bff-3531-a723-483a58d26582 | -7.22005 | -43.08384 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 088a7267-c26c-3f20-aece-0cc9cc6b7878 | -7.29756 | -45.36451 | 2025-07-05 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5739e9c1-8644-355b-a4ab-0b69d9f3328c | -6.8001 | -44.75037 | 2025-07-05 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a743809-00cd-33f4-bbf8-0780f8b0fa74 | -10.55454 | -49.4364 | 2025-07-05 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92d60b94-b68b-3e54-99a4-c47beb17e640 | -7.00602 | -43.5405 | 2025-07-05 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 90c7bab9-f2f1-3e4d-9f18-8f2368bdfada | -5.87537 | -50.14946 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e29ecc8-0023-3b12-8e2c-956e40e358a6 | -8.99975 | -47.44707 | 2025-07-05 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2e1dfbc-708c-3f0b-9d8c-cd890c44e18a | -7.70017 | -47.28242 | 2025-07-05 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22f7f929-1e44-3166-856f-b2a210751034 | -11.45074 | -45.11079 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39a1b62e-f77a-32bc-93e0-891e3adc6648 | -10.5646 | -49.12717 | 2025-07-05 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e22e608-b388-3133-a2a1-bd717b200497 | -10.57115 | -49.1328 | 2025-07-05 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 712647c1-4f42-3bf1-b771-5ec347d7cfe3 | -12.01465 | -47.76539 | 2025-07-05 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 32b1e6bd-d013-3e63-98da-9eec0acbc021 | -9.78914 | -48.2521 | 2025-07-05 04:19:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10b82af0-6ab0-38e5-80d6-3245afe80da1 | -7.24195 | -43.07948 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 888ad1b9-f4d4-3be3-8b3c-0c5b77962d74 | -11.8701 | -44.87592 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 164b3162-4d88-3490-a4f7-015ef0fd8d02 | -6.65804 | -44.31337 | 2025-07-05 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ee566ec-db54-3d47-8894-385be8889cfe | -12.01345 | -47.77279 | 2025-07-05 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2abf5f07-653a-3147-8435-6b69b89251d9 | -9.78497 | -48.25545 | 2025-07-05 04:19:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README9.md)
