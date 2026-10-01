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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a929de8b-e1b7-380b-8d49-1cb05daee6de | -10.7667 | -50.5086 | 2026-10-01 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 35b60f37-1128-3c4e-a72b-6bbaa38e1bf6 | -3.1839 | -54.0839 | 2026-10-01 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 77355697-1a6d-3548-9a8e-8e99258c995b | -8.5554 | -66.9945 | 2026-10-01 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 182.5 |
| c0a38880-de20-3bd7-9aaa-640d600ba204 | -6.0179 | -49.5648 | 2026-10-01 02:40:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 5697e7a1-1c97-3bf4-b47e-e1bf745e0fb6 | -3.295 | -53.8597 | 2026-10-01 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 89748f8b-70b3-3f8d-88fc-81bf86eb3d74 | -8.5738 | -67.0125 | 2026-10-01 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| d7377ecf-5ae6-3dbe-9b4d-babb363073aa | -3.1655 | -54.0844 | 2026-10-01 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 163.3 |
| cab06c9e-651f-37e6-b3b2-eaa93fa93a9d | -3.1245 | -50.289 | 2026-10-01 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 931732a8-0647-34bb-be50-8628d16345c0 | -9.1221 | -64.4031 | 2026-10-01 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0943435c-caf8-34f3-98c3-49ff5240aae9 | -3.1061 | -50.2686 | 2026-10-01 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 6289e5bc-6fb4-3366-be33-7512f78006fa | -20.1886 | -47.397 | 2026-10-01 02:40:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a77dbe5d-49f6-32b6-98a1-6b9624335411 | -8.5554 | -66.9759 | 2026-10-01 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| d947e41c-777e-3997-ab26-ae113ed2f198 | -3.1471 | -54.0849 | 2026-10-01 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| d01e2444-2858-3655-bccf-619b847104b4 | -8.5738 | -66.994 | 2026-10-01 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| e6757169-9f55-3871-aff6-653e83a9527f | -8.5369 | -66.9949 | 2026-10-01 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| da260566-76b2-3faa-b60c-e66c665f16b3 | -1.9003 | -45.8043 | 2026-10-01 02:40:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c0192e32-cd8b-313f-b97c-2e2cf92d7d77 | -3.1839 | -54.0839 | 2026-10-01 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| a5681899-e0c6-329f-92c3-0ce17b5f4966 | -11.4037 | -51.0148 | 2026-10-01 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 0aa353c1-596f-3037-bb7b-26a7c17859e0 | -9.1222 | -64.3843 | 2026-10-01 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 92e8b802-41ba-3beb-b356-ba25fb2aff16 | -2.908 | -54.151 | 2026-10-01 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3679f99a-d092-3dd4-b899-f50219141d2c | -11.4034 | -51.0361 | 2026-10-01 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 8ff06b25-f26a-3f2c-a737-241e6e3d4fa2 | 3.2742 | -60.6105 | 2026-10-01 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0d596f3e-d3c6-33cc-9317-4f8d4aab65e0 | -3.106 | -50.2896 | 2026-10-01 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 8259c926-92fb-3898-91da-e25a757675b3 | -12.1857 | -48.4345 | 2026-10-01 02:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 34c26fe5-f3fc-3695-8f0d-013795fe65ee | -9.1408 | -64.3836 | 2026-10-01 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f9f3a6e1-c6c7-3ed2-abd7-e106ee31b5ce | -11.8287 | -50.5192 | 2026-10-01 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 35e008ad-8345-38eb-bd79-f3dde51bfa5d | -5.7563 | -45.152 | 2026-10-01 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| bfb9fef1-3e7d-3de4-b7f0-034e164a76fb | -3.1838 | -54.104 | 2026-10-01 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| f76981e8-28b7-324e-a199-bb58e15e03f2 | 3.2924 | -60.6101 | 2026-10-01 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 81ce6fef-09ca-318f-860c-4482a6b5ccc0 | -3.5808 | -51.4832 | 2026-10-01 02:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| d5c9343d-80de-37bb-b6e2-79e43c85b647 | -3.1655 | -54.1045 | 2026-10-01 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 170.6 |
| 4e9efee9-13a2-3ea7-8ad3-480bc56c6473 | -3.1655 | -54.1045 | 2026-10-01 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 165.0 |
| e8fc7322-e7c2-3706-a559-b40b14e241d0 | -8.5738 | -66.994 | 2026-10-01 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 6eed7048-b1b3-3132-9ad4-c56798bb313b | -12.1857 | -48.4345 | 2026-10-01 02:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 191cc3f4-b51b-3aca-af8f-9eafcae77e4b | -3.106 | -50.2896 | 2026-10-01 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 0c55faf1-81dc-30bc-bb69-def6e07bc64f | -3.1655 | -54.0844 | 2026-10-01 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 680d8c50-e1e6-3113-a535-0e24d0ae6520 | -3.1839 | -54.0839 | 2026-10-01 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 806d945f-0c4f-304d-88c7-ce32240aa4c3 | 3.2742 | -60.6105 | 2026-10-01 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| a47b761b-7f5f-341d-8981-5ae3d81d79c4 | -11.8284 | -50.5406 | 2026-10-01 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 005b9877-8b2c-399c-a196-72d7f273f39e | -11.8287 | -50.5192 | 2026-10-01 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| ee082550-9a18-326e-850c-d6787c0d0857 | -8.5738 | -67.0125 | 2026-10-01 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 136ee108-9e84-304d-b158-32744f1fe5f5 | -3.1471 | -54.0849 | 2026-10-01 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 26a3c533-b738-3028-97e8-6c03922f1cd6 | -3.1838 | -54.104 | 2026-10-01 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 29e8f374-f9b1-33c4-b4cb-b129988b8b46 | -6.0179 | -49.5648 | 2026-10-01 02:50:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3654cd29-2d42-35a2-b76b-069e64d432f5 | -13.6479 | -53.9336 | 2026-10-01 02:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b3de7ce9-3727-3b3e-bd37-21363a8aba3b | -3.1245 | -50.289 | 2026-10-01 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 036bd3c7-520e-394e-a5b1-54d54e87b30d | -2.908 | -54.151 | 2026-10-01 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d2bbc011-2efe-314d-9b77-3a5e2ce68548 | -5.7355 | -43.2916 | 2026-10-01 02:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 40ba7aa1-6612-3abf-8c3e-8f9145183b50 | -3.295 | -53.8597 | 2026-10-01 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| ab1fa069-d6f0-3ef2-9c53-bfd1306e4d5f | -13.6671 | -53.9314 | 2026-10-01 02:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 4ee1fb9b-7a7d-38d4-8db8-daf8ed3bcdca | -11.8478 | -50.517 | 2026-10-01 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| a0c53673-71b1-321f-bcab-19d55d0d267c | -3.5808 | -51.4832 | 2026-10-01 02:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| a5712fd6-7494-32ca-b34e-436e241d633d | -9.1222 | -64.3843 | 2026-10-01 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.2 |
| c23bd3c1-88c9-3b4b-a513-4d5c177c1d6b | -1.9003 | -45.8043 | 2026-10-01 02:50:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 7e74dbc3-e01e-356c-a253-fff3a618b7b2 | -5.7563 | -45.152 | 2026-10-01 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| a881afc9-bf74-3b5d-be1e-f67bc79a5d2d | -3.1061 | -50.2686 | 2026-10-01 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 57e4364b-1778-3913-a944-01a08ea3b259 | -13.6671 | -53.9314 | 2026-10-01 03:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 1fb70411-fa25-3b4d-a09a-d0a145d0bcce | -9.1408 | -64.3836 | 2026-10-01 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 659ea803-a26a-3cd7-b005-7468c0419033 | -6.0179 | -49.5648 | 2026-10-01 03:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 18d137d7-db79-35bb-b8da-39a0b9325b12 | -3.295 | -53.8597 | 2026-10-01 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c9e7c543-4c86-3d65-bcef-26806cbd0485 | -14.4225 | -51.2624 | 2026-10-01 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 9dd54541-f4db-367b-8f5f-6b3a34f7f990 | -9.0046 | -65.6988 | 2026-10-01 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b7a0c924-dfa7-3119-9d0f-9f6139d281fb | -5.7357 | -43.2682 | 2026-10-01 03:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 50692ed5-5a92-3ecf-b050-ca7ef25d972f | -9.1221 | -64.4031 | 2026-10-01 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 106.8 |
| c0e7b35d-ee49-3208-a2a6-ec9a4a3eecf8 | -9.1222 | -64.3843 | 2026-10-01 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 171.9 |
| c5a571f5-a438-36bb-b3b8-5fa511b19c87 | -8.5369 | -66.9949 | 2026-10-01 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 81e98783-0382-3bdd-84aa-e8a446af0937 | -3.106 | -50.2896 | 2026-10-01 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 74322275-d356-363a-a804-7cf7cf0ec94c | -11.4503 | -43.4091 | 2026-10-01 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 7e9adc8b-fb4a-3130-aba4-1a8d4bedc30d | -1.9003 | -45.8043 | 2026-10-01 03:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c743a995-6269-3a6e-b851-ad5387802871 | -14.4031 | -51.265 | 2026-10-01 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 27da71dd-4848-3f2b-8caa-038c76b3959b | -8.5738 | -66.994 | 2026-10-01 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 72025b6d-28bb-3512-8a84-8d1ba67288f7 | -3.1838 | -54.104 | 2026-10-01 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 170.1 |
| be7a8bbc-2794-3367-93df-47eabc766305 | -8.5554 | -66.9759 | 2026-10-01 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 2385e10e-874d-3403-af89-e77f86d2c616 | -11.4687 | -43.4537 | 2026-10-01 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 74e5a283-a265-305d-9005-0b6241f4f4bf | -11.4311 | -43.4121 | 2026-10-01 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| cdda7e6f-0546-3763-bf73-92806bcb7c88 | -2.908 | -54.151 | 2026-10-01 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 15a48607-2350-3c75-83d9-d83b241730c5 | -11.4495 | -43.4566 | 2026-10-01 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| be45e9ce-e645-3438-a3d0-0768ca588842 | -9.1223 | -64.3655 | 2026-10-01 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 8d278df8-b035-3e62-af8c-40307f8b75b1 | -11.4037 | -51.0148 | 2026-10-01 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| d86396e4-7a85-359d-97f1-913d0442512a | -3.1061 | -50.2686 | 2026-10-01 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 701b05c7-80d1-32d4-a7ba-d5d3beadce63 | 3.2742 | -60.6105 | 2026-10-01 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 753a818a-ba8c-3e6d-85e1-fe71fab05a9e | -5.7355 | -43.2916 | 2026-10-01 03:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| ddfce0c2-a116-35e0-b74f-fd43bffc2fd3 | -3.1245 | -50.289 | 2026-10-01 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8dcac8b2-bcee-3a86-b480-60bc17e8a879 | -13.6479 | -53.9336 | 2026-10-01 03:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| bff8f4e5-ba9f-37c8-b317-f169cf3f630b | -12.1857 | -48.4345 | 2026-10-01 03:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| ffb692f9-44bf-3161-8742-ed853e4f7188 | -5.7563 | -45.152 | 2026-10-01 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b060ddf2-d759-30fc-8b1e-6c237e8c9f94 | -3.1655 | -54.0844 | 2026-10-01 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.9 |
| 234ee947-333e-3fe4-a38f-bb1e3d5e4d36 | -11.2903 | -50.9846 | 2026-10-01 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 7b1fa467-078e-3efd-837d-8f843c099cb1 | -11.4691 | -43.4299 | 2026-10-01 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 4d5f6db5-649e-3d5d-bb8a-4ba04c7c01aa | -15.4978 | -46.1294 | 2026-10-01 03:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f1a1b39b-3d90-33f9-bca2-d93ebe5af4a0 | -3.1655 | -54.1045 | 2026-10-01 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 0a2bb8f9-49d5-3b34-87fc-3fb36ad35624 | -8.5554 | -66.9945 | 2026-10-01 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 5f0f18fb-1b67-31c3-81d5-003efe4ffe48 | -11.4499 | -43.4329 | 2026-10-01 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.6 |
| a3158341-630e-3294-9552-8e877a766a40 | -3.1839 | -54.0839 | 2026-10-01 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 2074a5d2-36fd-38cd-abea-7805b7f8c558 | -3.1245 | -50.289 | 2026-10-01 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6eda3616-7ba3-3026-9508-64108fa03b91 | -11.4311 | -43.4121 | 2026-10-01 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| a7ddfac7-eaaa-3b35-9be0-32a000e58a01 | -3.1839 | -54.0839 | 2026-10-01 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 2d366fbb-1939-3cb6-ae6c-bfd2d75d7695 | -5.7355 | -43.2916 | 2026-10-01 03:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 3bae4241-4591-3952-a9d3-a64587d151e1 | -3.295 | -53.8597 | 2026-10-01 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 00e87d80-1ac8-334b-af62-2c9efea3688f | -13.6671 | -53.9314 | 2026-10-01 03:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |


[Clique aqui para ver as próximas entradas](README18.md)
