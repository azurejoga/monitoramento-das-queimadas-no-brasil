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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73c55fb8-1f95-39de-837f-69c9c7e17f06 | -12.7671 | -48.0236 | 2025-09-14 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f877f325-a843-3026-8d6b-2cbb8d3cec10 | -9.72 | -46.8749 | 2025-09-14 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| c8e76895-d16d-3986-8418-9838848a0288 | -10.9452 | -47.3538 | 2025-09-14 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 311.2 |
| 2c347eec-3aa5-3e59-8b24-5e80a7ca853c | -12.9485 | -54.7313 | 2025-09-14 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 9139c194-0937-302a-8539-2bf99dd61aeb | -8.979 | -45.7892 | 2025-09-14 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| db3b4254-840d-3f04-83c1-48d6be424471 | -8.4331 | -47.2527 | 2025-09-14 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 0eb9a682-4261-38b7-ae92-f1aa25a2f23d | -12.9103 | -54.7352 | 2025-09-14 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| cbd027cc-f531-3677-bdbe-7dbdf64a40da | -8.9365 | -46.1545 | 2025-09-14 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 5e927b4e-8ba6-305e-993b-3a453e17f0b2 | -11.4824 | -50.8147 | 2025-09-14 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 591c258d-e033-3c4f-86db-9681f5d556ef | -12.9482 | -54.7519 | 2025-09-14 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 7272c304-a1fe-3c88-b532-c6ae7f758735 | -11.5017 | -50.7912 | 2025-09-14 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 1a7810d8-f67f-39be-9ef7-ade51786a51d | -9.7386 | -46.8951 | 2025-09-14 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 127fd231-3aad-3b5d-a31e-c5ae8613a046 | -8.9371 | -46.1094 | 2025-09-14 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 896b1817-3b75-3680-8135-d646d66056ff | -8.8987 | -46.1585 | 2025-09-14 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| de54f466-1f94-3feb-b710-bd98a54f0e93 | -14.4779 | -47.3368 | 2025-09-14 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 3c1831c4-1e09-3b36-8dc3-fce3a441ca87 | -8.7683 | -46.0373 | 2025-09-14 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| e24e5b73-2e9a-30d0-ad86-4ec32c9c531a | -8.9362 | -46.177 | 2025-09-14 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 4152f19f-0e1d-3a6b-b863-5de9754bc67b | -10.9262 | -47.3561 | 2025-09-14 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| e10f25ec-4b9c-31e6-8e63-5cc1eb645571 | -14.2917 | -45.0964 | 2025-09-14 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| d9dbeb29-a9a3-3564-a915-86284795c7eb | -8.9176 | -46.1565 | 2025-09-14 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 848a847e-e893-34f3-9ca8-8450d7b5c1a7 | -14.1722 | -46.1585 | 2025-09-14 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 304ebe8b-577c-3f40-8fd8-e05011c6da47 | -6.9798 | -44.5529 | 2025-09-14 13:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 134.2 |
| af136078-19ba-36a3-9baa-522363563e84 | -11.4827 | -50.7934 | 2025-09-14 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 98a00e6e-9372-3356-8394-19bafc866665 | -12.9292 | -54.7538 | 2025-09-14 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| ec4bfcdf-1e7a-3f90-9d4d-3e9de9b3a79d | -14.2912 | -45.1198 | 2025-09-14 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f883ef27-5f01-38d2-945e-3b03778e8fbd | -8.9173 | -46.179 | 2025-09-14 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 2fb2fe7a-d58d-39d3-b8a3-6e6ee8879edc | -8.4519 | -47.2509 | 2025-09-14 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 3b0d4c52-7550-36a9-b3b7-340b04548e15 | -9.7389 | -46.8728 | 2025-09-14 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 251.7 |
| 0606633c-0c29-3d4b-b596-f581db30dc9b | -11.2927 | -50.8143 | 2025-09-14 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 4fef68fe-8854-39a8-8a5b-ddaa2e172da8 | -8.6436 | -44.0396 | 2025-09-14 13:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| d78be5b1-1563-3975-9f3a-175799325778 | -11.483 | -50.772 | 2025-09-14 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 32381785-abf7-3aa6-acd2-c6466a6e7c88 | -10.9096 | -47.2023 | 2025-09-14 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| d3dcfb56-3d54-3e65-8312-039ccae6ed36 | -13.5876 | -51.6715 | 2025-09-14 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 32ff4aba-169c-3f19-accb-60207d3f0a94 | -9.7579 | -46.8706 | 2025-09-14 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 7f87033b-ff79-379f-9d86-464b83086963 | -14.1492 | -45.4009 | 2025-09-14 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 0d1fec47-ad5d-3f54-bdfb-96559d3fe967 | -8.1386 | -43.653 | 2025-09-14 13:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 6fa3f87c-5b9b-31de-97f8-583bbe22551d | -15.7786 | -53.482 | 2025-09-14 13:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 248.9 |
| 77cba0b7-0aea-3036-9ee2-661c65015975 | -8.4145 | -47.2324 | 2025-09-14 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 07684653-f93b-3378-a763-612179785e90 | -14.394 | -52.9245 | 2025-09-14 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| e354e13c-0271-3d5c-9ed9-76835314fff9 | -10.929 | -47.1776 | 2025-09-14 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 923af31f-1711-3e95-b6b8-fcccd0a82d25 | -15.7782 | -53.5031 | 2025-09-14 13:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0e1cd4ed-e024-3f0d-abec-bc9fbeeecf8b | -10.8994 | -45.4426 | 2025-09-14 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 8ff6dae6-dc23-3b0b-a846-fa8dd1aee54f | -15.9233 | -47.2443 | 2025-09-14 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 73277c75-7457-3773-ba7f-215141ff95cc | -8.1383 | -43.6764 | 2025-09-14 13:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 1f4b6f92-646f-335f-99f4-08b403292264 | -8.4334 | -47.2306 | 2025-09-14 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| b33897e6-82d0-38e5-ad8a-c4fc55144813 | -14.4783 | -47.3141 | 2025-09-14 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 96bbbc88-30d0-3f76-a586-2bb5f8317b8a | -8.4143 | -47.2545 | 2025-09-14 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 4fe5f7ef-2795-3cbc-a890-78811b9cb91a | -12.9294 | -54.7333 | 2025-09-14 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 279.9 |
| b323aecc-5bf8-35ea-91a9-f7802a9775cc | -14.4973 | -47.3336 | 2025-09-14 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 35e467ee-3a5c-349a-aa22-8c5f43813ceb | -14.3747 | -52.927 | 2025-09-14 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| c935a55d-9cb6-3071-9fe9-41612a12ae65 | -14.4312 | -43.1986 | 2025-09-14 13:20:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 979d093a-3780-37dd-8f36-ca2281ee8c1c | -8.9368 | -46.132 | 2025-09-14 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 252.2 |
| f96e9633-5425-3baf-a840-1a7a8e75df32 | -12.9482 | -54.7519 | 2025-09-14 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 724c3cdf-e924-3fe2-a7c3-f62adf7e46fd | -10.9286 | -47.2 | 2025-09-14 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 07fc2760-801f-3b36-91a0-b26ae2202099 | -11.8484 | -50.474 | 2025-09-14 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 14c23fc4-f2bb-3ba2-81c2-85375feee43c | -8.4334 | -47.2306 | 2025-09-14 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| f1d975c7-7e31-3dc8-872b-0e5f8c116c7f | -6.9986 | -44.5512 | 2025-09-14 13:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 622a4bd2-7001-3ae0-a9f4-c34fc600904e | -8.9976 | -45.8098 | 2025-09-14 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 9eb35a1f-0715-3f57-85a5-77164b2eb9ed | -14.3285 | -46.1088 | 2025-09-14 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 0f068b95-77ad-3df7-b28b-c053cc7a32f8 | -18.5999 | -47.1944 | 2025-09-14 13:30:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 64.1 |
| a7867a9e-9e0e-3c55-9696-d3fd689d557d | -11.293 | -50.793 | 2025-09-14 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 90f04b81-cd92-342e-8a29-4c3c34d78c13 | -8.979 | -45.7892 | 2025-09-14 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 9d0a265f-b602-3e8d-89a7-2a5810a9713e | -14.4973 | -47.3336 | 2025-09-14 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 9f2fd28f-086b-3fa7-bfcd-4e99408312c9 | -8.4145 | -47.2324 | 2025-09-14 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 84438fec-fc98-37ad-a0e1-e6098622b872 | -12.9103 | -54.7352 | 2025-09-14 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 4dfba704-d05b-3f57-a5bb-5e189c724570 | -12.5795 | -45.6591 | 2025-09-14 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 15b923ca-4bbe-3525-a11b-4a9c886465b9 | -14.4312 | -43.1986 | 2025-09-14 13:30:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 7fbfbc3b-e64e-3670-97dd-fdf786ddebf8 | -14.1492 | -45.4009 | 2025-09-14 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 3018991c-4a61-3a06-bf28-e4402894301d | -12.9485 | -54.7313 | 2025-09-14 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 32c004e6-65e8-35c9-a234-692493e08465 | -8.6436 | -44.0396 | 2025-09-14 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 70a3411c-46c4-3e99-92bb-9dac0f101aa5 | -12.8212 | -47.1445 | 2025-09-14 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| daaffe7a-40ca-35a9-a048-da95bde3d080 | -10.8991 | -45.4656 | 2025-09-14 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 928758b8-5d99-30d4-8ddc-c29ba20a502c | -11.3831 | -47.3429 | 2025-09-14 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| bce50553-5ac4-3cb1-9754-8c5e665903c4 | -11.2927 | -50.8143 | 2025-09-14 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 51d7d8f6-7881-35a2-bc63-93e4f2a766e6 | -10.5586 | -51.9661 | 2025-09-14 13:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| ed261a10-2d9e-3947-ac95-80138c8aa96c | -12.7831 | -47.1276 | 2025-09-14 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b4970ae6-c21d-335f-9dcd-a3a7fa26e108 | -10.9096 | -47.2023 | 2025-09-14 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| e5e8efed-892d-35a5-9216-163c373c96cf | -8.9979 | -45.7871 | 2025-09-14 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| af1fb138-413b-3e8f-b7a9-c95700b922f3 | -10.9452 | -47.3538 | 2025-09-14 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 658d06b8-6da1-343e-aae3-c142d615fa7e | -10.3512 | -50.4876 | 2025-09-14 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| bbaeafb7-467f-3628-88b8-fd7b9f36e896 | -10.8994 | -45.4426 | 2025-09-14 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| c1f2712a-d6b6-3f54-81c5-e14366cd0fd3 | -14.3965 | -41.3479 | 2025-09-14 13:30:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 119.9 |
| e3a52918-5a71-3a97-aca2-f9a46df423eb | -10.3696 | -50.5283 | 2025-09-14 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| aaa9688c-5a0f-3fb5-b664-7c09325547e4 | -14.4783 | -47.3141 | 2025-09-14 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 5102fb83-fd4a-3c4f-b18c-7d17a98b49f7 | -8.9371 | -46.1094 | 2025-09-14 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 5f058854-55bf-385d-9a51-934ad6ac4eec | -8.7683 | -46.0373 | 2025-09-14 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 5e679f7a-a341-313f-9e70-58c2a05803ac | -8.956 | -46.1074 | 2025-09-14 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 3849af60-5bbc-30f5-9fcb-f9935382e264 | -12.8019 | -47.1474 | 2025-09-14 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 08874c2f-f801-3023-bcd6-24e398785d75 | -14.6393 | -41.0217 | 2025-09-14 13:30:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 8cf98299-1c15-3cf6-b743-efcfa3f62693 | -10.3699 | -50.507 | 2025-09-14 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 267c7757-2762-3dd4-ad31-34aca48c8ed7 | -8.9079 | -45.457 | 2025-09-14 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.2 |
| fa533bff-c038-3e40-afbf-cfa3f546b3c1 | -12.1427 | -47.5763 | 2025-09-14 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 17638bcd-2fe5-3c14-8170-ea6a1cb48dcc | -12.9292 | -54.7538 | 2025-09-14 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 3980439f-fe94-389e-a946-a2ff0f14464c | -9.7386 | -46.8951 | 2025-09-14 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 6c94474c-956e-3f6e-85e1-a08d9b41c4e4 | -8.9595 | -44.4436 | 2025-09-14 13:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 7f78a559-8067-3480-b235-6bc6b619542a | -14.4307 | -43.2228 | 2025-09-14 13:30:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 0d8596de-3851-3cbe-9345-d57bbd6ada52 | -16.4128 | -49.0732 | 2025-09-14 13:30:00 | GOES-19 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 92.6 |
| bb3e8417-1e2c-30f6-881d-7340094679b1 | -3.6924 | -47.4886 | 2025-09-14 13:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| f0f12652-aa55-341b-84cf-ce344a9ba07c | -12.8208 | -47.1671 | 2025-09-14 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| d8322f9f-4fbd-32c6-8ad1-d53c99b9a192 | -14.2912 | -45.1198 | 2025-09-14 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |


[Clique aqui para ver as próximas entradas](README85.md)
