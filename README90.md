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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4250b7b6-517e-36cc-8f9a-ffe5599259f5 | -5.9997 | -57.8054 | 2026-08-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| e8fc2c26-0f45-38c2-8eb6-23d6c69296c5 | -6.0806 | -59.9657 | 2026-08-22 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| a26f5e60-7ae4-30f0-84b3-51519f3fbe4a | -6.5302 | -58.5227 | 2026-08-22 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 2b5423da-ac69-3781-8874-c2489156b4c8 | -8.5218 | -54.8411 | 2026-08-22 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| ab5885db-3483-3ada-82d7-395a6f184293 | -6.9499 | -59.3177 | 2026-08-22 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 21977cf5-0760-3955-ae6d-cd695514fad1 | -6.0992 | -59.9267 | 2026-08-22 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 870990ce-d9ae-360f-be97-a3569e66f813 | -8.5408 | -54.7995 | 2026-08-22 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 724d690c-e862-355d-8d00-a2cb66eb2e55 | -9.1909 | -59.4619 | 2026-08-22 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| c8476bbd-0345-3b46-9c31-e9a2d58200ad | -9.6653 | -48.1187 | 2026-08-22 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| ecdb64a4-c29a-3812-80ae-32101094d8ff | -9.035 | -60.4359 | 2026-08-22 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| cf10076b-0fa7-3f7b-ac3a-7d718f2c39fa | -6.0991 | -59.9459 | 2026-08-22 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 59e6c843-aae0-3534-a811-077249b6f259 | -6.8571 | -59.4179 | 2026-08-22 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 32a13fec-eccd-3c3a-9cc5-1a562d34de8b | -6.8992 | -55.6977 | 2026-08-22 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 125a18ed-5181-3a36-a67e-d8a8cf78ae42 | -8.522 | -54.8209 | 2026-08-22 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 170.0 |
| 61aee928-b6f3-389d-b6d1-abc6b2925b7f | -8.1853 | -54.9838 | 2026-08-22 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 162.7 |
| e2391971-f8ea-3ee3-a4e1-79b4f8f5f132 | -14.0688 | -54.01 | 2026-08-22 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 147fef2b-f8f6-32f6-a08f-81dbe2bb9fca | -6.018 | -57.8242 | 2026-08-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 082f0150-a662-391a-b8ee-4541dce1d2ea | -8.5221 | -54.8007 | 2026-08-22 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 107d08c4-87f3-3109-815c-48c7444b9ea0 | -6.8042 | -58.9954 | 2026-08-22 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| cec4f4a2-5e2a-3985-930c-8ad60e10fbf2 | -14.316 | -51.8329 | 2026-08-22 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 53cbf759-804b-34e0-8ba7-3bea2fc10df5 | -12.2806 | -43.1813 | 2026-08-22 14:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 1a9d879c-c674-3d18-a599-6aa6f2f6bd3c | -11.3475 | -46.0203 | 2026-08-22 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| be48269c-9171-3570-b937-9f8cb7ec9d1d | -5.9996 | -57.8249 | 2026-08-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 1910be68-99e3-398c-907e-da68a249bea5 | -11.153 | -49.9742 | 2026-08-22 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| c2ea65ce-9294-30aa-8c0a-f404a90b2718 | -11.3472 | -46.0431 | 2026-08-22 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 434d3f27-f726-382e-8e67-a6cd5032bca2 | -9.6951 | -45.9572 | 2026-08-22 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 225.7 |
| cec4fad5-cb43-3bc5-9ee8-d630f3eea310 | -11.3663 | -46.0405 | 2026-08-22 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| c92fe17f-f166-3adb-a96d-b23475f07402 | -8.1667 | -54.985 | 2026-08-22 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 232.4 |
| 90128202-8b49-3f96-b084-8c6eefe10288 | -8.4089 | -62.6767 | 2026-08-22 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.0 |
| c7c0f13b-6bc7-3665-9676-6f889f895994 | -8.5406 | -54.8197 | 2026-08-22 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 252.2 |
| bbe79162-8b65-3c06-b9bb-62f150e9cc1a | -6.1285 | -57.8393 | 2026-08-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| c144e100-364b-3d4f-9efe-673d557b7548 | -6.8755 | -59.4364 | 2026-08-22 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| f15dcb31-4e08-3ba8-8dda-3f53454b1553 | -9.106 | -60.9127 | 2026-08-22 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9bb3009c-6a68-3565-933f-ae4fed571c00 | -6.8568 | -59.4757 | 2026-08-22 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 503c03cf-326c-35eb-910e-21e1a2342e0b | -11.6446 | -46.5232 | 2026-08-22 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 18c98124-a8fa-3ec9-bf9d-83440f46efdb | -6.1176 | -59.9261 | 2026-08-22 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 819e0b5a-96ea-33d9-ad12-4d87d96942a6 | -6.78 | -59.63 | 2026-08-22 14:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 272a077a-3ed8-3085-8ece-088ddacefb2c | -14.04 | -53.97 | 2026-08-22 14:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 132aad9a-c3dc-300e-984f-65fc0916fc71 | -6.81 | -59.63 | 2026-08-22 14:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 199208fa-d4e9-3095-b65e-6faf9fe00498 | -16.14 | -43.66 | 2026-08-22 14:15:00 | MSG-03 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 898d2f85-b5e4-3d20-997b-484f4e24142c | -8.9042 | -60.5385 | 2026-08-22 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 18ebaca3-d597-3a2a-9e03-97487d40efaa | -15.3427 | -46.0658 | 2026-08-22 14:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 79.6 |
| c3ff0923-de11-3f99-a2ae-241cf3a07538 | -8.3904 | -62.6774 | 2026-08-22 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 114.8 |
| d6775e76-c768-3ae0-ad3b-8cea8fb641b0 | -6.8568 | -59.4757 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| a119d93c-bf2b-3493-80dc-47b9a62b5086 | -16.1279 | -43.6194 | 2026-08-22 14:20:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 319.8 |
| f2c0383e-a619-35cf-8f47-f917107868fb | -16.1273 | -43.6437 | 2026-08-22 14:20:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 276.7 |
| 15bf716f-b980-3745-a0b0-bb3157231b6a | -10.7847 | -50.5706 | 2026-08-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 0efe8f6b-e892-3730-a488-9d132e32760c | -7.344 | -55.6741 | 2026-08-22 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5d880991-b7ca-39a4-8cb3-47cd638181b4 | -6.97 | -59.0465 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| b03423f7-5fd2-31a8-b352-7785b901db12 | -9.035 | -60.4359 | 2026-08-22 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 5a82ee63-7d10-3856-a404-5a5497cfb6f4 | -6.9499 | -59.3177 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| fece6cc3-47c8-3ba8-9fbe-23c50baca89f | -13.9778 | -53.6876 | 2026-08-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f14e4908-4c2a-3ead-9183-51f9aa6e2dd7 | -15.361 | -52.9253 | 2026-08-22 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| e9db169b-6284-3e7c-a131-2013f2e717a3 | -6.2355 | -55.3918 | 2026-08-22 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c9b3491c-b953-304b-9a6c-7a8f35b67d16 | -6.6382 | -53.377 | 2026-08-22 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 8c617587-be7a-32b9-b26b-19bc7b13eec7 | -15.3415 | -52.928 | 2026-08-22 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e4ba75a6-ce14-3584-9cde-3ea5660b6e72 | -7.3625 | -55.673 | 2026-08-22 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 246111b6-f5b2-3d3b-aa57-8402070c84cf | -6.8042 | -58.9954 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| a5109bf1-47b6-33b8-9088-7d48ee00a348 | -6.8571 | -59.4179 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 8f0dd9af-cf52-3191-95a1-dc1b2be4b3e0 | -6.0992 | -59.9267 | 2026-08-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 7daf69d9-28be-3876-96c0-8a6aa6c0b2e6 | -6.8043 | -58.9761 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 603f9fe0-0698-30ff-96e5-a3ac71ae1348 | -9.0534 | -60.4542 | 2026-08-22 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 2f32e894-646d-3b89-b30f-7c2fccc0285d | -8.4089 | -62.6767 | 2026-08-22 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 38f26589-2b6e-3c14-aecb-651d02f85aa6 | -6.1285 | -57.8393 | 2026-08-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 01d3bf76-fbe6-3211-9c23-09689bff75e2 | -6.099 | -59.965 | 2026-08-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.3 |
| cf64f012-536e-3b53-bffe-2a123f8b92e8 | -6.8756 | -59.4171 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| ad1cab46-0621-3d12-8079-d953fb02b83b | -9.4744 | -48.2917 | 2026-08-22 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 0c3640c5-e678-3636-b41b-4f5d0d217518 | -9.0536 | -60.435 | 2026-08-22 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e02a85ff-538b-315a-a528-6073c92c3697 | -5.9997 | -57.8054 | 2026-08-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 7e55b6ee-c4c5-3711-9ad5-247be41b8da1 | -6.5302 | -58.5227 | 2026-08-22 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 0ee45b4e-3202-3fa1-9437-e6d1da33a5cf | -11.6446 | -46.5232 | 2026-08-22 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 59ee9c07-4fe8-3e68-89ec-26e5d00c2f2f | -11.3667 | -46.0177 | 2026-08-22 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 8fdfb4f0-e9c1-3b9e-b35a-51737ba3cde8 | -6.254 | -55.391 | 2026-08-22 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 183.1 |
| c0ac9e62-e159-3d4c-ac59-42c4bc7cb69f | -6.0806 | -59.9657 | 2026-08-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 0d51e071-161c-3837-9b83-cef2175e8fb5 | -11.3472 | -46.0431 | 2026-08-22 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 88723e4f-3973-3bde-b0f9-26a0df1b6f9a | -6.9515 | -59.0473 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0b1eb4b4-7ae3-3a33-81f6-f8a799909ff4 | -8.3481 | -46.5058 | 2026-08-22 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 29c660ae-d69b-31b1-a241-7795966e6544 | -9.106 | -60.9127 | 2026-08-22 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 33b171d7-1de1-3702-b67b-abb89f4aeb76 | -9.1909 | -59.4619 | 2026-08-22 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| aefb541d-3040-3ad7-9dfd-d6c0945559fd | -6.0991 | -59.9459 | 2026-08-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 8b42716a-76b8-3804-92ab-654b44c598de | -9.0348 | -60.4551 | 2026-08-22 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| e8d594ac-261c-302d-bf56-2087e7f22044 | -11.3663 | -46.0405 | 2026-08-22 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 260.6 |
| b5a813d3-b0e8-334f-a843-123525458ce5 | -6.3654 | -58.3354 | 2026-08-22 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e9c94c0d-60b5-3cc9-a450-ac11da2311cb | -8.3903 | -62.6963 | 2026-08-22 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| d6c3ed30-5cc4-310a-b9da-895b96597779 | -14.0688 | -54.01 | 2026-08-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 8ea88300-6590-3b81-bacc-8fba1ef2fd2f | -13.997 | -53.6853 | 2026-08-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e3e7a9b4-7f99-30dd-813d-c554ab5467d3 | -13.9364 | -53.8798 | 2026-08-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 4e03944d-f37b-370a-8923-94660588dfa0 | -6.5487 | -58.522 | 2026-08-22 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 556a6e75-611b-3b4e-aad8-3c1e95416998 | -8.9938 | -50.7004 | 2026-08-22 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f810608c-029f-34e5-a4c6-72f574ebfc0e | -6.1176 | -59.9261 | 2026-08-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 342c3f15-6aaf-3c6f-87be-ccfdd200adbc | -6.0181 | -57.8047 | 2026-08-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| eb9ed4d7-998a-39d6-bd77-9168be09a268 | -9.1724 | -59.4436 | 2026-08-22 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 35c3d883-cd83-3073-b2b6-eebd3ed71ac5 | -9.191 | -59.4425 | 2026-08-22 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| f255bc7b-4ae8-30f5-a978-a35f153bf26f | -9.1201 | -61.582 | 2026-08-22 14:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 782a1d12-ba4d-31ac-86d8-7b42fd77a84c | -6.857 | -59.4371 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.4 |
| b9b22673-cedd-39ae-8a87-c9fe043ce5f6 | -10.9624 | -51.4214 | 2026-08-22 14:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 0af95732-d9ea-3d35-99c9-987a37144e55 | -9.6653 | -48.1187 | 2026-08-22 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 92959a08-0dd9-3e91-aa26-f3db174d7dda | -6.8755 | -59.4364 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 2088278a-7435-3eca-958f-e940a632a913 | -17.5891 | -44.6164 | 2026-08-22 14:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 7000f7ee-3506-3d00-81a5-7326465da3f9 | -6.9315 | -59.3184 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.8 |


[Clique aqui para ver as próximas entradas](README91.md)
