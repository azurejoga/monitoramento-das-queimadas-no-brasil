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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab423863-aed9-380e-b187-e16d09f61849 | -3.85136 | -51.93193 | 2026-10-08 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5a4f7ae-9f10-3601-96c2-61b2f17315ee | -1.8234 | -55.03756 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cf0ddb0-1116-33c7-bf8d-57a4ddd06258 | -3.47945 | -50.08233 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85af170f-7fb2-312b-a784-fd78ef8acfaa | -3.99929 | -56.24984 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8e185d9-21aa-37c5-8791-93211d49a634 | -3.10064 | -53.77502 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f7437d8a-1ce6-3799-87d6-0a8353d98985 | -3.85066 | -58.90137 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c35fa1c6-85cc-31bc-b5a8-af19a01261fb | -4.0925 | -52.06778 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6028aa9e-6ae7-3d76-93ce-966eb55890b8 | -4.98398 | -56.22534 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1327fd5-a559-3260-bf69-40d4480b1cbc | -2.81151 | -56.61261 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2a4a9a3-96e9-328e-89a2-d60c26f6962d | -8.13945 | -49.45459 | 2026-10-08 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b010029a-3176-3e91-b10c-8f3194d01c89 | -3.45194 | -58.04419 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4571ae0b-c60d-3025-aa72-c3696f93f502 | -3.53454 | -59.50038 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd3f12af-7f10-3d2b-a258-a84811b0afa5 | -2.99235 | -51.05558 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a98f63f-ab70-3401-9a02-a71f00f4f903 | -1.53011 | -54.55131 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c52a6cdb-85a8-3857-b1c4-e39d27bbe60a | -4.06334 | -55.33122 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8474d4a8-4fc4-3703-817b-deafaeb4751a | -3.29212 | -54.02528 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbfc0cdb-5759-37b0-bb6f-ca27598551d1 | -3.05736 | -53.95898 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 231e4159-cc70-3554-9633-ddf933a4962f | -3.16899 | -58.6295 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec6f248f-2802-3fd9-a45e-3233310e919f | -3.71014 | -58.9391 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0aaf8dcc-7ef8-3378-a8b8-df5c57c35e0b | -3.60478 | -54.35591 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 686c8826-5220-3b6a-9280-768ca29e58e1 | -2.98801 | -54.12743 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34cb6d48-187d-30e2-be7f-201b34d678ad | -2.47404 | -56.07433 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9029c40f-4a13-3284-b33a-9ecdce5af670 | -1.08385 | -54.10756 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e33ae8b4-9110-3244-b79a-08de8707a582 | -3.08862 | -53.71166 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa0c85cf-3bc7-333f-b6d3-b2f2edf81b66 | -1.43768 | -53.23388 | 2026-10-08 05:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 301d69e6-a1f5-3825-abe6-6075b5dfda00 | -4.33601 | -43.79819 | 2026-10-08 05:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d786d787-fc0d-3044-9863-8298dabb6ec5 | -10.49678 | -51.94157 | 2026-10-08 05:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e8e2a23-56c8-343f-9c36-9cabb020ac8b | -3.54191 | -54.67117 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e53acc86-6e34-3fd2-8fa4-089d24d7d9e6 | -3.26775 | -54.06559 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1bb6ac39-926b-3df1-bd36-322b708ab6d2 | -11.76749 | -58.28246 | 2026-10-08 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffffd568-c296-38fb-badb-8b509a5a641b | -2.46182 | -56.06532 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bbc210d-e159-34af-9b56-0b1b7f6bb039 | -1.12811 | -57.2849 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c96463a5-4a0f-33d7-9484-72a8625f6ddd | -2.50629 | -56.12899 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d76eba0-93de-3555-87e9-b76daee5dd98 | -2.9853 | -54.77702 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ba7d3d5-0e55-347d-8d14-645e06b1a9ec | -7.26059 | -48.06268 | 2026-10-08 05:23:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18f00491-1a98-34b6-a39c-ac5c98f9bf5c | -3.12621 | -53.70516 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca7ddfc6-5054-3c60-a523-43f72c4bb97c | -3.01977 | -53.94505 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9e56043-8b86-376f-97c7-2724454cb1c4 | -6.16615 | -52.66066 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11e5a615-ce44-3c3b-a341-428bf1558ec5 | -2.5807 | -56.14757 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 158fddc2-ff12-34fb-b7f1-d278abe1fa3a | -4.11861 | -59.88488 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a871d27b-d019-3cc3-8b85-13f62c7878d9 | -9.4919 | -64.36402 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edcfbbb3-7598-343c-b5c6-80746c79aa9d | -2.38662 | -56.13503 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9347d461-9664-3fa6-92eb-d3d1e491e4db | -2.39104 | -56.12864 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c541797d-02b6-3fbd-a8ed-2d3d13af7168 | -4.49702 | -55.48627 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bff6bc3-162a-3de6-ab72-8d6db1c83f3b | -3.02058 | -53.89281 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3d1226a-3735-3604-a33a-574dee732c9f | -2.58795 | -56.16642 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6af0bb9-83e9-3244-9b49-d437eb6af5f1 | -3.30921 | -53.87029 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5bab624-8f56-306c-b7f6-533b73296275 | -3.08871 | -58.02076 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3eb08db-66cc-30a0-91ad-56f03e479a8b | -2.75947 | -54.08615 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d55d7c5d-ae08-3290-bf43-16364b91c0e1 | -3.05456 | -54.22835 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c32bbf26-e905-39d4-bf72-973c424bf62a | -5.89667 | -61.27861 | 2026-10-08 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 846f34da-6450-3897-889b-fc6bb91e0d02 | -2.54626 | -57.39142 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 165515fd-626f-3fc0-a9fe-c55edd3a5258 | -3.05119 | -53.90564 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bc7008b-aae3-346b-b651-bbe5de9b6724 | -2.94642 | -54.11324 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f39552e8-e76a-335d-b012-39bc2830e298 | -7.38357 | -55.21847 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8ccd3c9-6092-3646-84ae-fa92e21b16d1 | -3.57982 | -54.677 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 1cdfa3f3-a10b-3247-8ada-ad4d5dbab3c2 | -3.43645 | -59.5387 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 432104f1-72e7-3626-81da-7980262e7827 | -3.84319 | -55.97585 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1679a0cd-54a1-360f-a612-c9fd33c66360 | -3.36523 | -50.47417 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80a0e460-d148-398a-b9a5-ff5b8d46d98a | -2.98689 | -54.11145 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a9c84cfb-14a8-3146-b971-7b9701a37473 | -3.29407 | -54.0816 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de6b6cfc-b3e3-3eab-ac8b-18c0ed65dc0f | -3.64779 | -59.17113 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08f8784b-f00f-38a3-bb25-f7308d7f2d53 | -7.22287 | -55.16005 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da98fd74-2ca4-369a-9978-60c132ad919e | -3.62026 | -55.50471 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d12753c1-2165-38b9-9b33-ddcd971b2e3f | -2.89749 | -56.67215 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fe9d939-b90e-3b16-ae12-41a76e33f91d | -2.99207 | -57.203 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0036884-28c4-383f-9c41-041bcf9ba1fc | -2.49694 | -56.16649 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ef49b71-d389-39a3-a836-898351e04ddc | -3.53139 | -54.65474 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec7bc1d2-496c-388c-9572-5e7a11cc6767 | -3.52197 | -59.34996 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16c18725-39db-348b-b3ad-b051c84bdfdb | -1.40649 | -54.60694 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e57624a3-4f26-316e-8237-625589fef854 | -3.57641 | -54.65353 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16a6cc57-fec4-3dcd-8f55-725c15cf1deb | -4.00486 | -56.25784 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc2bd72c-b693-3e39-9cdc-85e66756d240 | -2.94521 | -54.12094 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0dfe1d84-f4a2-3e42-ad1e-16ec891df473 | -3.54222 | -54.67553 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 159cfca5-ff5e-3216-83f4-be5ca9b0922a | -9.47429 | -64.36079 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 27f15d0b-2d3c-3ad2-aa33-871e7a2a4d69 | -8.62648 | -67.0251 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 10cf47df-de10-345c-a4a9-93202e12ebf5 | -8.62051 | -67.02745 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 141f8dba-cec4-3da3-bdb0-b8f811cd1bea | -3.17682 | -53.83813 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08d59d87-00dc-3d45-805c-e058f1d65557 | -3.43578 | -59.54277 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 422cb617-70e0-3cb6-b1d4-07eb7cbfc0ff | -4.60673 | -55.71861 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb4df764-06f9-3064-ba4f-63bd1f5758d3 | -3.65302 | -55.31977 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7a5231a-dcd0-352a-8008-bbdc85b43106 | -10.64852 | -53.85278 | 2026-10-08 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9735656c-8f77-34f1-8f7e-f0e6c69eae88 | -3.0162 | -54.22235 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4558248d-2ff9-3329-8c26-2f1176cb9125 | -3.17306 | -58.62628 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7d8a094e-0b3d-33d0-9b02-da3bd206b8e0 | -6.62255 | -43.73104 | 2026-10-08 05:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43c37b9c-1a05-3ddc-91b9-8c82a9034a87 | -3.48438 | -50.08981 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12b9f9f1-6aff-3c96-98ff-f019b6701f9b | -3.0976 | -53.93304 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35f65abe-39ef-3f1d-a1f0-b8cb3f4c8e22 | -4.10789 | -54.40734 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d40de95-beb9-3b6c-8a23-5fcbd74974d0 | -7.25513 | -48.06187 | 2026-10-08 05:23:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9e261c6-dd3f-3402-a9a4-e553ac00fce4 | -3.98369 | -56.21892 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55192d29-c9ed-3666-b40c-b8f96691ea46 | -3.72959 | -54.65754 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04ffb371-181b-362e-beee-93354d8f504e | -3.10481 | -53.77164 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6faa62cf-8330-3f6e-b6e1-ef8e92433cbe | -3.08328 | -54.25525 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 123cf967-dccf-36a1-9ee1-e0f07041b8e8 | -9.14143 | -65.29649 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7339a721-297f-3e2a-bcfb-e81b62750935 | -3.09894 | -53.76255 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d6f353e-5700-3a1a-a182-046077087a39 | -2.56767 | -50.68001 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b24ae54e-9e12-3cd9-94ca-f2bcc11791d5 | -3.27188 | -54.06224 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 453e6866-64a1-3fa5-867e-befea76d9bfa | -3.27142 | -54.04216 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bd17d63-7b26-39d1-81ee-ce9f0c054a60 | -5.86425 | -53.46291 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dd13ef90-87a1-36ab-a5fb-a88d799ea507 | -4.32132 | -50.78352 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README147.md)
