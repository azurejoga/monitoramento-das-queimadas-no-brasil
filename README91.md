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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ba5c60d-e335-3fc7-8fa9-4229fc6d6707 | -9.95617 | -66.87207 | 2025-09-01 05:53:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1893479c-34fa-3a41-82af-f2f2bc380d2d | -8.73327 | -62.41299 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e30ae85-4174-3b04-960e-c92ca39e1686 | -8.41783 | -70.73055 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19767a14-1f5d-352f-862b-9c47eeebf325 | -6.97058 | -71.74596 | 2025-09-01 05:53:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74b375af-313e-37b5-8e03-3cee595aceba | -9.13291 | -65.84982 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d0ac7d0-0c7e-3aea-a0f0-fe7b8a61f80a | -8.62878 | -62.58512 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 813f7031-b202-3de9-8afd-9a184f9c9cff | -9.11604 | -61.20524 | 2025-09-01 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56d3a958-7fec-32ce-b1c5-a9ed1ec13f5f | -10.88126 | -55.7551 | 2025-09-01 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c33c811-19a7-3574-abdf-2917e0fd1a1d | -9.34698 | -65.42834 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4514c279-d5b7-3b64-885d-4159458df96a | -8.65059 | -62.92688 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52e3cb17-cd0e-3f47-9aef-c8bc35ac7ccc | -9.07469 | -65.43437 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 177d98b7-4ca2-38ac-9203-987e2c24538b | -8.65408 | -67.24487 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d69496e1-8ab6-3477-8e53-6dfc7fc9776c | -8.46286 | -71.18076 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d8b77ef-a100-3599-8da7-915850f2a74d | -9.88364 | -65.01939 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc8781f3-8af9-393c-9e00-27c25b18fb18 | -8.04282 | -70.08942 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9588bd7-078a-34c7-b858-ca2816a6bfab | -8.42771 | -62.29354 | 2025-09-01 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24e01fc4-75b4-30cf-b534-330a9fa3f3c4 | -9.68574 | -65.01915 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a59aa210-9172-35d0-9608-ef77fd10ab8f | -9.82834 | -65.05144 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c42108ab-4448-369c-9a48-9c674f29bf38 | -9.64434 | -63.11446 | 2025-09-01 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cea73b1-30a1-3a35-809b-041fe1281461 | -10.26544 | -68.79099 | 2025-09-01 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c0e9ed7-3eba-3cdf-ad6d-9538ed2378d9 | -8.38327 | -70.7561 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0b57878-a873-3eab-ba4f-bca29cc5ce61 | -8.6502 | -67.24783 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79a32fe3-0244-31cd-8eaa-761736dc1e2c | -9.44185 | -60.57215 | 2025-09-01 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41a377c3-4326-362c-a88a-ba878ad50eb0 | -12.44497 | -63.92326 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6725af69-ec6c-3f8b-a952-4d0f5dbbaa1f | -8.96883 | -65.9631 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84135b4c-8ec8-3b7b-90b3-4791b3e47050 | -9.95952 | -66.8726 | 2025-09-01 05:53:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29b8da7f-35d7-396f-a5f7-e0482d03f25c | -10.84123 | -55.75348 | 2025-09-01 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f51041ee-854c-3a67-ab7a-a1aff17f4921 | -9.82716 | -65.05935 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67633c26-0a9d-3296-a641-680cb1e9db45 | -9.07069 | -65.41445 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d55dd90e-1937-3627-947f-d1090e03e443 | -8.84603 | -64.14777 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc793671-a1e4-3d3b-b816-93c59a6c0e22 | -8.24736 | -72.82078 | 2025-09-01 05:53:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a34127ec-6632-31d8-9a9a-a9c69b7d1d11 | -8.55424 | -63.00941 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 408bf09e-23d2-37b2-a5b8-703479a3d04b | -9.34813 | -65.42077 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdc855cc-c67a-3ec4-9fe5-0cf375af7d06 | -9.07813 | -65.43491 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37b8a74a-53cb-3c1b-b072-107f40876a8b | -9.08488 | -69.9045 | 2025-09-01 05:53:00 | NPP-375D | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 01db8b2d-fadb-33a8-9309-8f1105103d91 | -9.02479 | -65.69031 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad0858df-22d7-309c-9fe0-6381c018e63c | -9.88131 | -65.0109 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0e1f9ee-52b5-3f35-9e0b-fb12e0ccade4 | -8.71169 | -62.42038 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| edf74a2a-f8cf-3437-aa37-29e3e66b879c | -9.17463 | -67.73614 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a23c9e11-3acc-3b2f-a84c-3209efcd27b9 | -9.7035 | -64.53785 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bed44d18-e19c-3cce-9080-6f8f10dd7f8d | -9.13688 | -65.8467 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff4fc673-5c02-327f-9f60-b3a8ee3bab7d | -9.08216 | -65.43167 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d3e2998-98b4-3a02-8c0f-1a4280a78257 | -9.3441 | -65.42403 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 090c7ab4-5e5b-39bc-ac4c-9ddb1788ddfc | -10.08687 | -68.46866 | 2025-09-01 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3839394-5ae6-3a61-bec5-07a9e9a13f0a | -7.46228 | -70.13979 | 2025-09-01 05:53:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87deeb7f-3edd-391c-ad87-beae55b4c91c | -9.07526 | -65.4306 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 862854fa-bb3a-39d0-aa7a-4b50e69d87dd | -10.27381 | -64.29997 | 2025-09-01 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3719f26-7a9d-3b3b-a802-b7ca74cdc3ca | -9.12778 | -65.54181 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 020000a5-4a6e-3f2b-98ba-d5008e867e38 | -8.96093 | -65.96931 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bfcb0a0-b488-3908-891d-8f2565935794 | -9.12215 | -65.76147 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8b83411-6ee2-360b-b248-fb87bf5593fe | -12.44812 | -63.92866 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f6b0967-9f02-39fa-b161-fc21691a58b2 | -8.84176 | -64.15146 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3869ce4a-e6c1-365f-b67b-082286310368 | -8.9756 | -65.96416 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f097aa10-366b-3a0b-8322-82592e501497 | -9.39167 | -68.2692 | 2025-09-01 05:53:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c7fbe539-9c35-3901-9563-7b8b5671dc8b | -8.96375 | -65.97348 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a3390ab-ea0e-316f-9b37-6177dc3282e2 | -8.76169 | -61.43248 | 2025-09-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 128712d7-8c36-3a46-be69-46861007f1d1 | -9.7071 | -64.53841 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e62b301c-03f1-3678-b34d-091638b78eb9 | -9.8395 | -65.0491 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 570fe0f8-c167-3400-bce7-2d6641737d1f | -9.13904 | -65.85464 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15fb63d9-151d-3888-a51e-6ba1d9193dd3 | -8.62728 | -62.59532 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 508abda5-1161-395f-8d25-219b8855453c | -9.68986 | -65.01574 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d68c4c1a-90ab-3d16-bcbf-4566bc0d4b83 | -9.11485 | -61.21371 | 2025-09-01 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fe222dd-677f-3d70-ac89-a8023b0aa772 | -9.87838 | -65.00638 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc23a80f-e75d-36c7-88db-3e91133ae339 | -9.17518 | -67.73264 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65e99d7e-2a87-331c-b7b2-771dae3b0957 | -9.12835 | -65.53806 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab970a75-ff9f-3b28-8be9-28637bb0d8d5 | -8.76597 | -61.43311 | 2025-09-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5227211d-a983-3e4b-9642-439d82602e09 | -9.13351 | -65.55035 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 750b4891-d9e3-3565-bf65-f3e62263ec26 | -9.30382 | -64.54564 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8842df5e-42a3-311b-b38b-95f1b42a0548 | -9.13065 | -65.54608 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9ccd1c1-905a-3ec4-b681-b5f997b1fbd5 | -8.72424 | -62.41871 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 463c90ae-a19d-30b3-a1a3-1f5007980b6a | -9.11545 | -61.20948 | 2025-09-01 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb90ea59-030e-3cea-b863-e1f25a97783d | -8.84539 | -64.15202 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7df9247d-5a93-3e0e-9da7-502c7c54e912 | -8.72373 | -62.42219 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc407343-a23c-31c4-b963-27e4ba172feb | -9.84243 | -65.0536 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e8ccc78-ed12-37f7-a763-380e6a91c96d | -10.36426 | -68.59412 | 2025-09-01 05:53:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 646e3a7f-8fc0-32bd-ad24-dd46a3ba050f | -11.65033 | -57.35733 | 2025-09-01 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 98ac5272-affe-3d32-a9b8-9b54e0702191 | -9.88716 | -65.01994 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80adc102-dc92-3b48-994f-0919acca25f5 | -9.4504 | -60.57804 | 2025-09-01 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 674d84bc-78d5-3116-a6b7-b2528aa24ec9 | -8.0913 | -70.22009 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a6a716c-5a46-36a2-9cb6-9bf06cb8d1d2 | -9.45441 | -62.34254 | 2025-09-01 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47540a11-e0f3-335d-b237-7183d0ece72b | -9.13745 | -65.84303 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 079e67c0-6563-3273-8200-b3bc974eaf12 | -8.44477 | -70.13584 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80b043d1-480a-380b-aa09-d547df09a921 | -10.69396 | -69.7202 | 2025-09-01 05:53:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b031a5e-ed93-3116-9100-be39a7705b69 | -9.07584 | -65.42683 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4abad25b-0279-3bf8-99bc-59a71c7af329 | -9.34756 | -65.42456 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b79f5fe-ee2c-3c33-a317-e4d53145a814 | -10.57847 | -67.75678 | 2025-09-01 05:53:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8823eb1-0134-35ad-9df9-a8628e88f721 | -9.12724 | -65.84142 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e015b0c9-f4ec-3738-ac1d-3e9fc60f8447 | -9.80517 | -67.89899 | 2025-09-01 05:53:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b82dd924-a38b-3386-8149-4e0cd7cf3183 | -10.27014 | -64.29944 | 2025-09-01 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0eaa9576-9d26-3a97-951f-bee14a57f39f | -7.93106 | -63.01114 | 2025-09-01 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3acd273b-2bb7-3374-afb4-b33bab3d5ed4 | -8.0877 | -70.21948 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74c64e94-9441-3e87-b28e-6c7dfed92d7c | -16.21082 | -55.95253 | 2025-09-01 05:53:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f9cb43c2-4523-36ee-a76a-11507c8a5f95 | -12.44525 | -63.93 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1b38fa6-aaa6-3c58-be79-22648f33c61a | -9.13675 | -65.84677 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35257ce8-e4a9-3917-b257-5a859a9c3cb3 | -9.12951 | -65.8493 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c94c7af-f4df-32b1-ab81-0a98d9e09dbe | -8.67911 | -66.93381 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3515444-f0ad-3cae-b88e-72d763d56d4d | -11.51703 | -54.47651 | 2025-09-01 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a26df9f-526b-3634-ac64-dcdc63a685b9 | -8.67702 | -62.40462 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ee52dca-fb77-326e-9d08-789f116565a8 | -8.64743 | -67.2438 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c9cf3d8e-c220-31b7-96e5-0de071e383e3 | -9.70772 | -64.53427 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README92.md)
