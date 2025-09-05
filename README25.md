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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f281e84a-599d-3de6-a648-3be76dbf5861 | -9.07269 | -47.01635 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 846a8d3f-83c6-3c92-a9fa-3725076348b7 | -10.98118 | -45.94055 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a67e046-9b56-3df8-9d59-8e9b8bd07cb9 | -11.00413 | -47.15601 | 2025-09-05 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dfbaa4e-d7ac-3567-acb7-3077d58f0dd1 | -13.44501 | -46.93359 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43379edb-de0b-30be-8cdb-d300f2b87595 | -11.60267 | -47.75069 | 2025-09-05 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77ae5337-acee-3a18-b378-fc7d36ee8c98 | -6.49696 | -55.89094 | 2025-09-05 04:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f8021bd-6a21-3c9e-a4f5-b23a61a6c02f | -8.48337 | -45.08104 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ba7e4345-a130-315f-8538-f8de34db33a4 | -12.50715 | -53.8392 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 858d33b0-4670-3895-a714-8bd95958d1e3 | -8.87249 | -52.02407 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb7e1c41-bbff-327c-80eb-281f32ef5d3a | -9.70158 | -51.07516 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ab3f9bc-ce94-3df4-b4fe-a02b973216d9 | -8.87176 | -52.02852 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68e20da4-0290-3fa6-b8be-58d822f033e4 | -9.69787 | -51.05408 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 085d0a3b-9d42-32e9-91f0-e3e4f3beea46 | -9.76173 | -46.91083 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 49e40076-8ef2-3ed0-9c7a-5dc7b0f01d05 | -12.97235 | -48.05278 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c9470a9-254f-39c9-8698-0559482c793a | -9.44166 | -46.81719 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 977f5c48-1157-3092-851e-d75db45ed315 | -12.5308 | -49.10362 | 2025-09-05 04:36:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6918986-07a6-36b3-9b09-41e89e86a2e7 | -7.05701 | -50.85752 | 2025-09-05 04:36:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1587e9b1-b959-36d0-aacb-87e848cc60ba | -12.97597 | -48.05654 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53309999-249a-3473-a61a-ed65c9f6d771 | -5.50207 | -60.1291 | 2025-09-05 04:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a82df410-ff21-3f7a-b978-9ab23bbb7ba4 | -8.09179 | -45.33096 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 570f734d-1081-33a8-835c-d8b12ed3ea00 | -12.48271 | -53.84003 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fb7f92b-506a-34c0-bbb0-50a018f95c87 | -13.74184 | -46.9227 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da6527aa-d9cd-300b-8eab-7c8455925003 | -8.81434 | -47.51073 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c231a14-883d-35e6-9348-fd0cdbf90216 | -12.44187 | -48.08485 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c3a5130e-b34b-3cf0-8f9e-f546e93dfe1f | -9.69715 | -48.98877 | 2025-09-05 04:36:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cd2882a-a6a9-3437-b007-e1005616b8ff | -11.81021 | -44.26086 | 2025-09-05 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d48ee9e-78e0-3e22-ba63-8f26faac3ffb | -7.75135 | -48.78671 | 2025-09-05 04:36:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f66bce75-c50c-39bf-b05d-ae2f4736f876 | -10.96855 | -45.9764 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4df34459-de8f-3937-b75d-36b80201e8d8 | -12.99002 | -48.05503 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f83c80b3-f45b-32df-b3c1-48a7cae44fc3 | -11.65129 | -54.51452 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f98bbd81-2e5c-3d24-aeb9-22b53b1e2677 | -11.96476 | -46.77372 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 733af9c9-9988-3918-a3e9-56937e88838e | -12.18067 | -53.89479 | 2025-09-05 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f037297d-cb3e-3aa6-be7e-f5aedbedcb62 | -11.62726 | -52.20392 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 730bfc2a-0dd4-31c4-9742-2e4676ae2ef9 | -11.99453 | -46.74996 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bb4a138-90be-3b39-b9f7-c29e3751fc24 | -9.96604 | -51.65813 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bc30303-9c53-3a0a-82aa-f484ddf42546 | -11.32238 | -55.22538 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae767400-e489-32ed-ac06-f4e8777bc893 | -13.51186 | -46.92177 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b4657db-3ded-3f38-8007-1e73412630bc | -12.9729 | -48.0716 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3f0817c-58ef-3331-99f4-d2dd5f24f18d | -8.02363 | -45.41971 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a4beacbd-1de8-3ad4-97d8-118633e0f669 | -12.49663 | -53.85299 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53dcbb8e-8cec-381d-aedb-fa48ce700c4b | -11.60329 | -52.16913 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c002d1d-79ab-3962-aa66-4af5b9b6a2d9 | -10.53033 | -57.78051 | 2025-09-05 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b33628bf-61fe-3930-9d98-98156f90ed9f | -7.99278 | -45.45583 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74e204ec-f112-3cc1-a94b-ea2139f32db0 | -12.96898 | -48.05224 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7b274ca-3d77-3f07-9eea-d895bcab1811 | -9.97036 | -51.6544 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc531b6b-ef7b-3f6d-ae63-5ad5e0c74e50 | -10.96945 | -49.7589 | 2025-09-05 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9732622-dfc7-3123-a17c-5eaf83fc9205 | -10.07991 | -48.06433 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aef375d7-c41f-374c-9c5e-74bc24d0fa54 | -12.29288 | -50.02315 | 2025-09-05 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93a38798-c84b-303a-acd9-27bc853ddd3c | -8.97983 | -44.45371 | 2025-09-05 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 312d123f-f5a0-35ee-a442-e02c43856de1 | -12.48664 | -53.84074 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a01b2beb-ce6e-3a45-9ad2-ed7634b5dccc | -7.7282 | -50.32301 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e6361ed-881f-39c6-9659-389f26817204 | -11.61781 | -52.19355 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f96669de-8668-3966-9b07-6b813f9f9ddb | -8.64284 | -45.74832 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2172302-c7c5-334b-96c4-45c0d7b9442d | -8.86784 | -47.92661 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3ea36ff-72ba-3fcb-98c3-0c0e3ffebf15 | -10.77022 | -48.28214 | 2025-09-05 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2646f50d-8f86-369c-b6a6-e686574b7365 | -9.81098 | -45.99786 | 2025-09-05 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6362a32b-1c14-3d0e-9257-cd2df3e0315e | -8.99645 | -45.52911 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d507da2-7bb0-39cb-9cf5-9e456f9ef74e | -8.02546 | -45.40757 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6270c4ff-7d37-3014-a831-9fe2c02a8c52 | -12.11961 | -43.34197 | 2025-09-05 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c7f8da8-846f-3815-b63b-71151121e0d9 | -12.02022 | -43.78506 | 2025-09-05 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3477d80d-3889-3728-9226-9dab3647d6c7 | -12.52261 | -48.0754 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a308af5-6082-3cca-af5d-6d827471b0b3 | -12.27478 | -50.15676 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dc3470f2-447b-3f07-bf0a-278d660ca9e8 | -10.16196 | -46.2496 | 2025-09-05 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c3dd349-da62-3208-b44c-6313faefa7be | -7.75803 | -48.78777 | 2025-09-05 04:36:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c3821b0e-5115-3fc6-9483-ded7c61881b4 | -12.11901 | -43.34626 | 2025-09-05 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00c7d0a7-ccaa-3436-921a-4d07d6d459d1 | -9.50621 | -57.78531 | 2025-09-05 04:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b4bfb9d-6fca-3d4f-8a87-0be64b187eca | -7.77697 | -51.08294 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b56e4d2b-f316-3b81-a3aa-29ff2241ca53 | -9.42683 | -46.77702 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bde9927-1c0e-3141-8bdd-273dec13dfc7 | -7.69848 | -50.28639 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7312c96-9580-369b-813e-ebadb08dcf6d | -12.49359 | -53.84722 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76bfcf81-1d1c-3fcc-ab8b-eb79cd01ddf8 | -8.90237 | -45.79379 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e892255-ef85-3704-9fcb-c668b8f1cd22 | -10.14176 | -46.00013 | 2025-09-05 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ed9c5fb-3a22-325b-a3af-c6f40171d21e | -11.39015 | -55.37439 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63dca018-fa34-345b-91fa-a5045e41d180 | -7.71654 | -50.32892 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 982d95a3-6b25-3dc0-a81f-544d35918454 | -13.55364 | -48.13113 | 2025-09-05 04:36:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c60f342-ce34-309a-a011-38f9a7ae88c3 | -11.58301 | -52.17878 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dbf7e0e-ad83-339d-a4e5-355f32c5a608 | -7.68542 | -50.25723 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fcec6631-8039-3118-9178-fdb4444d58f5 | -9.82167 | -46.65722 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0a6002b-4e53-3c58-8440-014281120915 | -11.62364 | -52.2033 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6790c951-fbd0-367d-983e-430aa99b8998 | -11.91996 | -46.64303 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e82c779-3769-3e05-9fa3-402b11fcc11a | -11.85131 | -47.54147 | 2025-09-05 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3867b69-d5c9-383d-b733-d3cdf25a918b | -12.99677 | -48.05611 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6d121b6-7043-3820-ba7b-5c0b6dbabfc5 | -10.76578 | -48.28867 | 2025-09-05 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06e41702-c25e-3418-8d72-189b4969e0b0 | -12.08461 | -45.69452 | 2025-09-05 04:36:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 510babfd-2c0e-3946-8f09-4a285064bb01 | -7.05637 | -50.86144 | 2025-09-05 04:36:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c186c45-7197-3c1d-86e5-7570b045b057 | -11.63892 | -52.2235 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a5e4bac-89d2-335d-a0bd-97e4bfb88d7e | -11.6493 | -54.52582 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce90cdb5-c87e-3e94-a644-af6302f9cce9 | -10.54381 | -47.01297 | 2025-09-05 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42fbe7d8-65e1-363c-b058-4e436e4d814c | -8.0177 | -45.43497 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 025975df-a78f-3fe9-a34d-4bb4262682ce | -12.44132 | -48.08847 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bb8c7bb-97dc-3ef0-863a-aabb8920c6ae | -10.23763 | -50.54255 | 2025-09-05 04:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb8436d7-f82e-3854-8d9d-fdfd30b24643 | -12.44243 | -48.08121 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a08f0d7-2680-394a-b6c0-f92442884787 | -11.02112 | -45.06704 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd157d00-fa8d-321b-b829-82bbcd4b5da3 | -11.63529 | -52.22286 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bbb2c1c7-71aa-30ed-870b-dada80c6e044 | -12.32019 | -47.0469 | 2025-09-05 04:36:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a8f2557-2a50-3f36-aa26-e137ca334fe0 | -8.86505 | -47.9226 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cd46735-737d-3d72-bb68-b55b6b6b4600 | -8.80595 | -47.49855 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12a65ce3-5fb8-3c8a-abcd-130cce1cca17 | -13.32241 | -48.5642 | 2025-09-05 04:36:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfe6c0e5-4584-31dc-a998-4edc41998a1e | -11.87715 | -51.54866 | 2025-09-05 04:36:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1877eeaa-9bc7-35a7-a4aa-5b1b3d008bb1 | -9.08059 | -47.01004 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README26.md)
