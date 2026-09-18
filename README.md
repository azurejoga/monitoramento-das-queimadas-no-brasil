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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05638ef9-3686-3fb7-bc4c-2394ae9fbc14 | -12.2633 | -50.7463 | 2026-09-18 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| d80dcda1-1f53-3b34-b5ef-cb0a05e1c9e6 | -5.7614 | -57.6002 | 2026-09-18 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| bcad7714-8cad-3abf-8e2f-cb3ea855b38e | -13.2683 | -46.8969 | 2026-09-18 00:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| c41a65ce-0552-316d-8f14-c3cf44387eaa | -12.4708 | -50.8924 | 2026-09-18 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5f247aa5-0065-3ddd-8a27-237691ef2ba2 | -9.7177 | -54.8162 | 2026-09-18 00:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 3f858340-e7e0-3e38-9552-d82e15640975 | -6.5174 | -49.8944 | 2026-09-18 00:00:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 6c0a1026-6190-3c04-842e-7abbaca1d7ad | -12.2821 | -50.7654 | 2026-09-18 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 78a23e28-0e3a-3686-a54e-75596b90a600 | -4.5961 | -42.95 | 2026-09-18 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2cd813ae-088b-389c-b8a9-dea29f5c11b0 | -4.5587 | -42.9523 | 2026-09-18 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 677.5 |
| 7ac4540c-ef66-35a1-84d6-b514386de068 | -10.6153 | -46.5675 | 2026-09-18 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| bd2003f4-c7ce-3587-aa84-165cc0d79d8a | -12.3585 | -50.7563 | 2026-09-18 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| fdd0caeb-0eca-3432-a954-abc104dc31d9 | -12.263 | -50.7677 | 2026-09-18 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 279.6 |
| f1f8e607-b9c8-33d9-bdf7-eb1baea99eb3 | -6.1358 | -59.9638 | 2026-09-18 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 3fd83fa2-75ea-3f9d-8cdf-466d06169803 | -9.0931 | -45.7314 | 2026-09-18 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| d2c517fd-ec28-37a2-91bf-fb19f5d6a73c | -6.1359 | -59.9446 | 2026-09-18 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 248f4f15-062e-3142-83e5-550c406b6580 | -4.5772 | -42.9746 | 2026-09-18 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 473.3 |
| 3790b136-618d-3d87-bdc5-1636a136e8dd | -6.1175 | -59.9452 | 2026-09-18 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 39858c3a-8daa-3a9c-8ebd-480e436cf908 | -2.0497 | -52.1611 | 2026-09-18 00:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| bd95e003-d1a6-34e4-91e1-95bc20edacad | -5.7569 | -45.084 | 2026-09-18 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 62d19964-d903-3ab2-8195-a0fdc71fb3d5 | -5.7567 | -45.1067 | 2026-09-18 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 96878912-acd3-33a1-8d11-8c45d3ccb592 | -13.249 | -46.8999 | 2026-09-18 00:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 79c86205-f092-3daf-9198-d8365898904d | -4.5589 | -42.9289 | 2026-09-18 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| e103cf2d-a956-3c33-8855-9ab4c431989c | -5.7385 | -52.2379 | 2026-09-18 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 4f0fe578-5f50-3c20-8cd7-0b1c3f24d016 | -5.7431 | -57.5814 | 2026-09-18 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| d4105176-c2ea-3c97-a718-7a408d8642fe | -3.3638 | -50.4492 | 2026-09-18 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| a5dd956c-d520-3d4e-8b10-6bc69839e61e | -19.1812 | -48.7717 | 2026-09-18 00:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 50d42bc4-a18e-3efe-986d-3092aee8d318 | -3.3637 | -50.4701 | 2026-09-18 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 4ee6cc5f-ee81-3083-a8af-f7f697bce5b8 | -12.2817 | -50.7868 | 2026-09-18 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 6190e485-4ea3-3804-958b-f7923eaafb2b | -9.0934 | -45.7088 | 2026-09-18 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| d8939e0b-fda6-36b1-a9c3-7e0f2ea798db | -5.7615 | -57.5807 | 2026-09-18 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 122db73d-deb4-38b0-85ac-c0c3dc084882 | -5.7429 | -57.6009 | 2026-09-18 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2b662753-e954-3a73-9514-d60aad671a32 | -4.5177 | -56.0751 | 2026-09-18 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| e135308f-7c4d-3ffa-b5be-1e4ff4695a3d | -12.3397 | -50.7371 | 2026-09-18 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| b122e0d4-209e-34b6-8266-7b375916d414 | -4.5585 | -42.9758 | 2026-09-18 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 332.3 |
| 1a5fadcf-7eef-354e-aaa2-842f5ed88a2f | -12.3394 | -50.7586 | 2026-09-18 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| b85e5e17-07f3-3d66-b3b0-5c6e9c7e1208 | -12.339 | -50.78 | 2026-09-18 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 91ec2057-af47-3d31-95f9-8f5f484b3c97 | -3.3823 | -50.4486 | 2026-09-18 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 6aa2fee7-f12e-37c0-b075-e2eb7fb9f27d | -12.6427 | -50.893 | 2026-09-18 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 5d7e05b7-e540-3e9a-ab67-1ee5dba0a59b | -3.0465 | -51.3755 | 2026-09-18 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| ea571bec-c1db-3710-ba95-11f7a3c47b22 | -4.5776 | -42.9277 | 2026-09-18 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 164.6 |
| c76d73af-cfa4-3ff4-9b08-295c70f2087c | -12.2626 | -50.7891 | 2026-09-18 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 131.3 |
| ca984e68-15da-3ba1-9d87-79c08109bc63 | -4.5774 | -42.9512 | 2026-09-18 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 929.6 |
| 2b608abe-2283-34a6-ad9f-0fcfde21e54a | -12.4712 | -50.871 | 2026-09-18 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 9a53101a-2317-36dc-9106-b8a51c745ee9 | -8.9479 | -51.4618 | 2026-09-18 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a4cc0c59-ea24-3838-b0cb-d529351ac48f | -9.77354 | -45.03088 | 2026-09-18 00:01:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5b352444-75b1-38fb-b6a7-e860e132ca7b | -10.82564 | -50.1868 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a63402ed-1646-3a22-916c-6dc520837829 | -9.15945 | -49.99024 | 2026-09-18 00:01:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4dfa781b-9127-3e3a-a762-6c8434265c8d | -6.11488 | -44.04449 | 2026-09-18 00:01:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 72e161be-ef0c-37a9-af34-01aa98437782 | -10.78765 | -46.17733 | 2026-09-18 00:01:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 806ed8e6-cb3f-3c1a-adbb-9c5b683b8e00 | -11.67542 | -54.46852 | 2026-09-18 00:01:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bebcb3b3-31c4-3fc8-8a8e-165030bcf49a | -8.45868 | -44.50313 | 2026-09-18 00:01:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 377649fb-d59b-3b29-88d9-125d9757d342 | -5.82801 | -49.95585 | 2026-09-18 00:01:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a26d22aa-9443-3167-8426-ce1c43d81c44 | -8.55207 | -44.9035 | 2026-09-18 00:01:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 62cc0d14-2760-36f1-bba7-9e446f19594a | -7.00419 | -43.65179 | 2026-09-18 00:01:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 30abf4f6-b384-305e-bf43-5e73de107847 | -8.95141 | -51.46154 | 2026-09-18 00:01:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a2e21b5f-8463-306f-b274-c77603db6d1a | -10.12323 | -45.57541 | 2026-09-18 00:01:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ead226a4-6750-3a26-820a-a0cd694ddfce | -6.11227 | -44.02665 | 2026-09-18 00:01:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| c89b4b1f-8e22-3b36-a898-86b809697832 | -8.99097 | -50.17286 | 2026-09-18 00:01:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a1ca91f9-f7c1-3701-9110-fd223096a90a | -7.79406 | -44.90989 | 2026-09-18 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 5aaec2fa-79e8-32ad-9cf0-c549e393bed3 | -4.56861 | -42.98114 | 2026-09-18 00:01:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 7e3dbb5a-8496-3d97-a1fa-bef96182e952 | -6.4111 | -43.46881 | 2026-09-18 00:01:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 4ef8e7d1-e669-3e99-966b-596fe162c6eb | -5.91218 | -49.76787 | 2026-09-18 00:01:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5e4c93f7-4f6a-3d75-99cb-eef20708f57c | -9.10023 | -45.71923 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| dacf6fc3-eee1-3ca3-b2db-09b63f528f54 | -7.45467 | -46.16479 | 2026-09-18 00:01:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0fcd2e6f-d64a-3eaf-87b6-666b3561dff6 | -9.71192 | -54.81588 | 2026-09-18 00:01:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| d198edf0-a7ae-3a65-95a8-d86c81dba775 | -5.1892 | -49.33527 | 2026-09-18 00:01:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2ff0f597-d559-36dd-9f65-13ae1bf4d232 | -6.77225 | -47.87173 | 2026-09-18 00:01:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9db87372-93d3-3d38-a45b-75af76bf4483 | -10.49115 | -45.29295 | 2026-09-18 00:01:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 9bb40468-e129-32bd-87a7-ae4958dd92e1 | -10.65022 | -50.25199 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 15db20ec-6340-3d7a-ae66-37d6216ce24c | -4.08643 | -49.49165 | 2026-09-18 00:01:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bd196fac-9e81-38f2-a955-ca9a505ea53b | -6.58389 | -46.72873 | 2026-09-18 00:01:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 884da5b0-dc33-367a-b5e7-41215a2acd02 | -6.11836 | -44.0386 | 2026-09-18 00:01:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 9903b4f7-d5e2-33df-aad9-952d2998dde3 | -7.05907 | -47.47868 | 2026-09-18 00:01:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 88d83984-2b48-3495-859f-21ca57781682 | -10.94377 | -53.05693 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 47fc3f64-80fc-369c-a5b4-981708f49f7e | -9.54891 | -45.49455 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 89de7d55-62b4-3e49-83fb-6290678c1141 | -11.52213 | -49.20661 | 2026-09-18 00:01:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7d357b94-a964-3a40-8a7a-48ed7b664216 | -10.99305 | -48.30423 | 2026-09-18 00:01:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 61f7bb18-e2dc-392f-9d30-76f7d269416f | -7.01376 | -43.63132 | 2026-09-18 00:01:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| dd2e028b-2c10-3e6a-884f-729f682065ff | -10.11648 | -46.29591 | 2026-09-18 00:01:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0f3f29b6-2715-3e88-be3f-d78e02982d3b | -9.93663 | -46.59608 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| db490d1a-d070-3dcd-8860-b9775afbc77c | -6.51176 | -49.89146 | 2026-09-18 00:01:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 116e7506-ba47-31e6-bef7-7df2d4c4ed7c | -10.11497 | -45.65458 | 2026-09-18 00:01:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 69207cf2-9234-3438-8784-3b941ed2dc2e | -10.61505 | -46.5564 | 2026-09-18 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 672e8911-5cbd-30f4-8df6-f9fbabc6676e | -9.61143 | -45.36427 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0bee295b-1a49-3467-a64c-33057fb5363a | -4.56176 | -42.93466 | 2026-09-18 00:01:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| d4a2dabe-65fe-39b0-8a87-47a2ee528f45 | -9.94766 | -45.28764 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ea16c098-a044-3905-a4fa-a5ed388df379 | -10.37435 | -50.46164 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d628f0d8-20ef-38e7-871d-b53d36096125 | -10.53755 | -44.84716 | 2026-09-18 00:01:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 9c217ec3-7dd9-3e20-8050-1678dc25ac9c | -11.31186 | -46.78098 | 2026-09-18 00:01:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 91cdcdd6-3e8d-328a-aba7-f581ecd8a10a | -7.85234 | -50.19506 | 2026-09-18 00:01:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 668c19ea-9f0f-3c86-a613-28d6e49a15bf | -10.98295 | -48.2965 | 2026-09-18 00:01:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 35e95626-a90c-3e1c-8dbc-5d53ec273253 | -5.74866 | -45.08521 | 2026-09-18 00:01:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| f38edf93-33eb-3bfd-b21f-3b1cca373062 | -10.66172 | -50.2694 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| ba8c5e12-b26e-331b-bdd1-09f8270be2cf | -6.1896 | -47.53628 | 2026-09-18 00:01:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7c5d3553-d504-3f8a-8d99-56cf4daa7241 | -9.91304 | -46.56785 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 73d34a3f-6dd2-39b5-bad2-0870e2cfa94b | -6.01634 | -51.33376 | 2026-09-18 00:01:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 10952163-f5eb-327a-bb6d-19b8862344ea | -5.73393 | -52.25227 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 92a30236-6fe8-39d3-bd81-95868e16b5a9 | -4.55773 | -42.95269 | 2026-09-18 00:01:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 248.0 |
| 88e80c34-a24c-35a8-9cbf-a889ac802a64 | -7.11512 | -55.12849 | 2026-09-18 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f7b99e6c-3ac3-3d3d-b126-ea8cc08ec013 | -10.63097 | -50.24518 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README2.md)
