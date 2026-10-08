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

## Dados Diários - Página 291

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4075fde-b4c0-3053-845a-2584ac5575ea | -6.05782 | -42.91863 | 2026-10-08 16:20:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| a61bc28e-680b-3f73-ae80-983f90bc8306 | -6.21592 | -44.85531 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b37a57d0-a361-3b55-8f56-0227b873fc19 | -7.39559 | -45.64289 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e40bbe07-6434-329c-b704-be7cb1cd7ee6 | -6.97761 | -45.13001 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 11ae251e-5063-3aff-acfd-0f8361cd98f2 | -5.73449 | -41.7663 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 38f61f46-e654-3e33-8f73-4b9f9f0012bb | -5.02135 | -42.44372 | 2026-10-08 16:20:00 | NPP-375 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 86975b2b-7dbe-35e4-b778-7de6b07269fb | -6.45481 | -46.01138 | 2026-10-08 16:20:00 | NPP-375 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| af625874-5bac-37c9-ae35-96b87e89f88e | -6.63345 | -44.88596 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f3918ea3-4821-3ad5-9bab-0ea55fe31dc2 | -6.132 | -47.93589 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 0fd4a24d-7c23-3019-82ea-aa7fff88988f | -5.7015 | -41.73595 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d63b4389-40c1-323c-a5d8-0a82e2a28e9a | -6.90017 | -44.92101 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 986262d3-4d52-347f-846d-61bfa1f5ac70 | -5.74672 | -41.70575 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 4709ac5e-c352-3151-af53-06e15513a0f6 | -5.53649 | -44.28799 | 2026-10-08 16:20:00 | NPP-375 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 2af0847b-d40b-36d5-b23b-bfbc3692bbf2 | -4.57612 | -38.94855 | 2026-10-08 16:20:00 | NPP-375 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| bb13fc46-6ccc-3b5f-bd38-1a7b3d7cf99e | -5.93312 | -43.88758 | 2026-10-08 16:20:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cc78d768-a9cf-33da-b759-3edb09560eaf | -5.74561 | -41.62798 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c49013bc-8a0a-3c71-87c2-530676e8d734 | -3.80259 | -40.45438 | 2026-10-08 16:20:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b9e86bee-c64a-3f6e-b92f-381d1e00ffc3 | -6.43401 | -44.81255 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 978e7d92-463a-3a39-8aa7-031fe414066e | -6.36987 | -45.79868 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| baf5bc28-aa17-3d09-8cc8-727549abf079 | -6.13806 | -44.14998 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c2a8aa9e-4008-34d9-a6bc-feac1af6c48d | -7.08153 | -52.67926 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 99bcae8a-f179-3fbe-a171-2dafb268fd99 | -4.63193 | -43.49944 | 2026-10-08 16:20:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| c1a9c447-4cc4-3e0b-9581-d7fa1d6783c8 | -3.90213 | -44.13278 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 08c0919d-1dc5-302b-9e01-f4c360bef42c | -6.79838 | -45.05202 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 0e04ca5a-8e0d-3891-befa-68a72bfdbbeb | -3.28858 | -49.12969 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 41a9fd42-54ca-354a-aa1e-1b035137eca0 | -5.70358 | -53.45145 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| a386f5b7-56fc-3add-b359-6c1263f45fac | -2.99759 | -49.21461 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e53a2d8a-1473-3c1c-ba4b-50cb312a7ba2 | -8.21942 | -46.37496 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7d4a7873-6523-3a81-a432-38dce1974e68 | -6.77069 | -44.12424 | 2026-10-08 16:20:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 37dd6e9d-d495-3f56-bc04-fcc1c79413f4 | -6.31462 | -45.06232 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f274ffb6-3f89-3152-ad46-b2ecb03f3280 | -7.05047 | -44.34211 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e27a102f-b0b8-3edc-8243-c26e6428b11d | -7.086 | -52.68384 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 1e321d43-17a6-3518-9d02-95d293f908b5 | -6.95013 | -45.27903 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| cc13b6e6-891e-3f03-b6c6-431f3ac1524e | -6.59794 | -37.88522 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 17.6 |
| d1f7ba65-e680-3f87-b66e-d2ef244a91a5 | -5.86294 | -47.69556 | 2026-10-08 16:20:00 | NPP-375 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b99c5a8-02e8-3713-b057-852dd69b521d | -3.73133 | -39.5275 | 2026-10-08 16:20:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 24f0886c-f89d-3d58-9d8a-5f69c89dccf1 | -6.41203 | -44.96039 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| c35001f0-6664-3587-a815-727e1dcbc35e | -6.59683 | -37.90015 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 91.5 |
| ee7c63a3-8544-3b2f-8d62-f94a7e5412a5 | -6.84455 | -41.7505 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 5aa78d50-f703-38e1-9c86-0ffd45de1135 | -6.15996 | -47.93339 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 9d45c203-ec26-3266-8bc8-db2492b81f4e | -5.7415 | -41.71827 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 23053cdb-7a93-3954-8ec8-e15e8e4d9912 | -6.57131 | -41.60723 | 2026-10-08 16:20:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| dfbfbb70-0e59-38ed-b215-3855d5b715a1 | -5.37684 | -44.6432 | 2026-10-08 16:20:00 | NPP-375 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f84fe832-bf1d-3d79-9256-8819a43cec3e | -6.67166 | -45.36562 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fe6eb536-e57a-3737-b12f-46c3006ffe2f | -7.31245 | -43.99939 | 2026-10-08 16:20:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e5ec369-5325-3bcd-957c-267f2f161157 | -5.71906 | -41.63979 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 4899ffb8-f1b6-3240-989a-a5b6d36af3bd | -6.86795 | -44.90147 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 888c12f1-0ab4-398c-8831-12d52189e2c5 | -7.10953 | -42.52865 | 2026-10-08 16:20:00 | NPP-375 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| a1309eb0-91ab-39e9-8e49-65b03a045daa | -7.71623 | -44.7369 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 503b70a0-c46e-3daa-ae53-3b844c858184 | -6.94457 | -43.06676 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a8a382c3-0f50-3d27-85e2-986c309bb1ee | -6.33185 | -43.35339 | 2026-10-08 16:20:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 489f7347-dcfc-39e5-858c-8577bf55cd1a | -6.67049 | -45.3574 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fc7e6be5-a3a2-34cf-8726-6216c8098d99 | -5.74643 | -42.06288 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f4b08b7e-819b-3bba-81c7-295ae8a51497 | -4.09721 | -44.1275 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 42787e1c-c89e-3fc6-9301-b24aaac2f8c1 | -6.79413 | -45.05268 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| c328b7a8-ee74-3b11-a517-c5ee6f3c41d9 | -3.46472 | -39.52718 | 2026-10-08 16:20:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 25e6cfc5-a4b0-3183-9cc8-b83230415d5e | -3.88678 | -40.98478 | 2026-10-08 16:20:00 | NPP-375 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 956f7689-1331-3d48-8df9-2a58a5206596 | -3.2609 | -42.53674 | 2026-10-08 16:20:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6eec70b4-a0a5-3dac-af36-5e1ffb2090f9 | -5.99266 | -40.93088 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| dfebca9a-b890-3505-bfaf-d16caae04a97 | -6.7551 | -45.13748 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7d113927-b398-388b-821d-d1ebb0474171 | -7.19054 | -44.33434 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2e5236b1-3c14-37ca-b5ba-61e31b8c44ed | -7.0886 | -52.67844 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6c4923d7-af58-3701-a310-61f2f6756629 | -7.3099 | -44.01026 | 2026-10-08 16:20:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 465ed91e-e9b2-3d55-96f2-ea840c4a4787 | -2.43089 | -49.62963 | 2026-10-08 16:20:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e5359323-ea83-3f0c-a919-45149b33afbe | -2.07175 | -46.57852 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3b9aab05-06e2-37c2-8666-3609df633ebc | -5.38124 | -44.20156 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 29d9800b-68fe-36a6-a7b3-90c878892e8c | -2.0837 | -46.56796 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 37348e72-1c53-3c85-b34e-d5f1443ad0ef | -5.99831 | -37.3841 | 2026-10-08 16:20:00 | NPP-375 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 8.9 |
| c2d21a82-6498-3054-9650-5bd6b757b6d4 | -7.96456 | -47.26894 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| df028520-1bcd-315c-816e-1660f41f7224 | -5.34758 | -45.7142 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f34ee6fc-629a-3693-9aae-2bbc4a6bbdfc | -2.74274 | -54.13129 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 23d8929b-f369-3ecd-aa58-2328403cd19e | -5.75054 | -42.06632 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 4936b849-06c1-38d2-a898-790293e7d3a1 | -3.25285 | -50.40101 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3a09cea4-d5ed-346d-a7f8-47a693425a37 | -5.09432 | -46.2162 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 259.9 |
| ab824861-70d6-3fd8-ae1e-03095be4bedd | -5.84827 | -42.62801 | 2026-10-08 16:20:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ba6c2dfb-8584-3fe6-b5f2-7d9c859f25b6 | -4.34187 | -43.16001 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 46b22eb3-14e1-369f-b8ba-5aab93cc8fb0 | -3.20917 | -42.95838 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 8d0e11aa-4f7b-398c-87f0-20dc7bc713ff | -5.72994 | -45.15146 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0c1d955f-be52-3af6-bd84-9bfdc69c251e | -6.12164 | -44.13329 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0f09417a-e48e-3dc2-a5b4-3320f1534fb7 | -5.1943 | -48.31865 | 2026-10-08 16:20:00 | NPP-375 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ea3e43a-1762-3cb1-890d-22bef53a8872 | -6.64791 | -43.78162 | 2026-10-08 16:20:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f618de66-d249-3651-a909-10a0dbd4bf10 | -5.51256 | -37.48759 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 24.6 |
| f03cfb10-d4f7-3a99-8d3b-5be1f6e11319 | -4.27518 | -38.68927 | 2026-10-08 16:20:00 | NPP-375 | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 139e4b5e-f750-3449-ae71-3bcad6fc17b5 | -6.40616 | -44.94954 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 5f11e121-2f24-32c8-8d98-3baec1141f91 | -3.39106 | -50.21457 | 2026-10-08 16:20:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| ec6ad18b-8724-3afa-8758-b064fac337cc | -4.05266 | -38.93764 | 2026-10-08 16:20:00 | NPP-375 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 06e144e3-aed3-344f-9316-1702d1a6000d | -5.88161 | -52.50996 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fc021416-0827-3a53-93d9-86499a2faed4 | -5.92837 | -44.28238 | 2026-10-08 16:20:00 | NPP-375 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e8637746-9e0a-3966-91d3-2f023a8f8905 | -7.18487 | -52.61678 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 3a8f6ec4-0702-3434-9f2f-860723099e70 | -5.38689 | -44.1855 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c0e7ffb6-c534-3a35-8431-493488b877ac | -4.16853 | -43.34198 | 2026-10-08 16:20:00 | NPP-375 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 18054a38-278e-3a3d-a74f-c1ab5a5520ba | -6.8326 | -39.55339 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| f6f2375a-9991-3311-ab0f-20e610bbf391 | -6.45613 | -46.02061 | 2026-10-08 16:20:00 | NPP-375 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 29ef88c0-5bed-386d-a160-7eac4c979434 | -8.20428 | -46.37092 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 213c71cc-3153-3251-93cb-399cf2331d1e | -6.13817 | -53.0685 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f87516a5-f330-382e-b60d-a0055b11633c | -5.97172 | -41.35231 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e7e5dad8-5b17-332a-86f9-085e1ba9d727 | -6.18852 | -44.02309 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9f1e66b8-4afa-3668-a913-c7706b706d6e | -5.76523 | -42.06813 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 764378be-6e21-3adf-b8fa-797f6785379b | -8.20908 | -46.37049 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 51378b6d-1f80-3279-be65-e32a5ab06dae | -7.2538 | -45.34173 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README292.md)
