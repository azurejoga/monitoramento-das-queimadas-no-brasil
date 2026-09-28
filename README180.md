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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca32dabc-e914-3430-b488-311a91cec84c | -12.8061 | -54.0048 | 2026-09-28 19:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 16663bb8-e772-3ced-a2fb-4a0302ebbc46 | -7.4369 | -55.649 | 2026-09-28 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 29cc3ce7-5f56-3dab-9bf6-8aef65c29244 | -9.1335 | -49.987 | 2026-09-28 19:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 180.3 |
| c76bdeec-c0db-3c43-94a6-d665edd9fe2f | -10.6505 | -50.7123 | 2026-09-28 19:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 4db83162-10f3-3f92-b7c4-0fcf59e2922b | -9.5192 | -46.3604 | 2026-09-28 19:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 34753839-99b7-34ac-929d-90a779209327 | -10.2653 | -44.6298 | 2026-09-28 19:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| cd197489-4beb-36ec-b16e-da5e9d6e1e65 | -6.1251 | -43.7262 | 2026-09-28 19:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 508be30d-9684-32ac-9270-48d7f2f77fdb | -0.5073 | -49.1326 | 2026-09-28 19:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 3e051780-70d9-3e2b-956c-c0376096620a | -12.4351 | -44.1497 | 2026-09-28 19:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| ad1be156-24af-324c-ac6e-bad480992707 | 1.8587 | -55.5846 | 2026-09-28 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 1b09fbf7-8355-3496-a717-26c3564c3e3d | -11.8641 | -47.1004 | 2026-09-28 19:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ab6b1659-3e6c-3db0-848b-e4f9e5e34cb1 | -8.2482 | -45.4356 | 2026-09-28 19:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| a4c19d0f-8f02-3577-aa01-2b08e87f4910 | -9.9781 | -50.1626 | 2026-09-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 0bddb2b6-be14-3b8a-b882-bdf56e709495 | -13.3943 | -57.0645 | 2026-09-28 19:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 0a195cb5-0ad0-3fea-8df0-4f2f917b6749 | -11.1771 | -44.8064 | 2026-09-28 19:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 3f2c0c38-5b7e-3815-bbbc-f1fe1b6fa4b9 | -15.081 | -54.5964 | 2026-09-28 19:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 460.4 |
| 9a7154a4-5647-31fb-86c0-900ae12f3b22 | -10.2254 | -50.0093 | 2026-09-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 520b7125-11ea-3549-b1d3-6737fb8d3803 | -10.824 | -60.7246 | 2026-09-28 19:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 184.9 |
| 1d95b929-9826-3ce4-bb8a-3034becf78f8 | -9.9787 | -50.1198 | 2026-09-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| ba07a32b-d352-3c77-b614-469824cbcc7b | -11.4601 | -49.7452 | 2026-09-28 19:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e713bdff-e64b-30ba-bbb5-aee76e134cb4 | -10.2067 | -49.9898 | 2026-09-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| d16fe502-6d5b-31e0-8641-014eeb84e8a7 | -12.7871 | -54.0069 | 2026-09-28 19:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 66513ce7-a93a-3afb-843a-f12b01998f5f | -12.6267 | -47.2851 | 2026-09-28 19:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 0d06ec13-7c36-3758-920f-91baf3bb56f2 | -11.0982 | -51.1748 | 2026-09-28 19:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| e5ddb8eb-2825-3cd3-bb8c-b4dde42967d5 | -8.2806 | -54.736 | 2026-09-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 41ea05b0-77aa-3c1d-a1bc-88bb07959de4 | -11.5904 | -44.1411 | 2026-09-28 19:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 8c01422d-323e-3f67-b8e4-e467668d19d6 | -12.1202 | -57.1767 | 2026-09-28 19:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 99d6c709-9684-30f0-aa74-caf35e4943e5 | -10.9346 | -50.6825 | 2026-09-28 19:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| ba42b2d1-c0b4-31aa-ac3f-61bad4556315 | -13.9012 | -53.6757 | 2026-09-28 19:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 8f444cde-401b-3bdf-a484-b7987553d379 | -9.9593 | -50.1644 | 2026-09-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 599bcca7-225d-3ea7-b21b-a22ada1f57e0 | -10.8184 | -61.4191 | 2026-09-28 19:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 64674a8d-3571-3bc8-a095-660ea46f9384 | -12.6463 | -47.2598 | 2026-09-28 19:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6471a5aa-1c28-3b68-a176-98be08faa01a | -9.1525 | -49.9639 | 2026-09-28 19:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 45a9295b-b2a7-35eb-a81b-5690049d298a | -8.2479 | -45.4583 | 2026-09-28 19:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ccfbdf66-af04-3bf2-886f-e62732242166 | -11.0223 | -54.1379 | 2026-09-28 19:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 67c85b5c-533e-339a-9d58-fe7e69ad9ecf | -13.6866 | -56.6131 | 2026-09-28 19:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 156.8 |
| d2d09eb1-1aea-3260-ab56-b681210aab1f | -10.8371 | -61.418 | 2026-09-28 19:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 129.7 |
| bec3cd4b-9433-39ee-88b0-594c23de7a7f | -6.8245 | -45.0458 | 2026-09-28 19:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4b825cdf-53b4-3f07-b08f-ec4b664319a7 | -11.4973 | -47.3504 | 2026-09-28 19:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 22a856c5-f93e-335b-a8fd-48832c9f9ea8 | -8.9823 | -44.1633 | 2026-09-28 19:20:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3fa6acb5-6204-311e-b005-2b9fd77f4ada | -10.8426 | -60.7429 | 2026-09-28 19:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 391.9 |
| 590713f0-f763-37f8-9134-0d424a823b36 | -10.0148 | -50.2443 | 2026-09-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| f46fee53-55a1-33c7-96e8-9b876bccf0ae | -10.9536 | -50.6805 | 2026-09-28 19:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 5507c9aa-dcdc-386c-a166-9dcebd93bfd1 | -14.4151 | -52.8165 | 2026-09-28 19:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 61d06b9a-b781-309c-b6b5-598143e94418 | 1.8771 | -55.5646 | 2026-09-28 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 71854537-e3e5-3a7b-a0bb-ac64101eb66a | -6.6627 | -55.1112 | 2026-09-28 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 374.3 |
| 84a6fb02-d96e-3a85-8386-8c5c8a90b133 | -10.2257 | -49.9879 | 2026-09-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| f1419735-f351-302d-bb64-312434631ea4 | -11.1324 | -50.0839 | 2026-09-28 19:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 83e97371-8a52-3487-a227-02f03222f944 | -9.9266 | -60.7171 | 2026-09-28 19:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 230.6 |
| 43ee0226-ee80-3a51-b00b-af6aa9948698 | -15.0616 | -54.5988 | 2026-09-28 19:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 925af7e5-e24b-3606-ae68-8317fc05d203 | -7.437 | -55.6291 | 2026-09-28 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 86515c4c-816f-3247-a343-d2281cf82f2d | -9.1682 | -45.7684 | 2026-09-28 19:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 564c4b4d-faf5-3801-bf5e-67658ce43dfe | -5.4949 | -45.1249 | 2026-09-28 19:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 4c9fb071-6f7e-3643-afe5-3cdd2d6487d9 | -11.1962 | -44.8037 | 2026-09-28 19:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| da86ddf9-f945-3b91-a07f-8666dd96b5d1 | -10.9912 | -50.6978 | 2026-09-28 19:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3e233aca-d9b6-3448-85b4-019e5c3915d9 | -9.1523 | -49.9853 | 2026-09-28 19:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 512f8d2c-f402-397b-80b4-21ca297b8708 | 1.877 | -55.5844 | 2026-09-28 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 3be50abe-e356-3372-80a1-6b663d122cc4 | -7.4185 | -55.6301 | 2026-09-28 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 38c2a1a0-8080-3d5a-9288-58668b8453e3 | -11.1514 | -50.0818 | 2026-09-28 19:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| c2de6abb-c56b-34e3-b585-29966b01ccda | -10.2065 | -50.0113 | 2026-09-28 19:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 181.8 |
| ac472469-9df5-3502-bb99-b00602200065 | -10.9445 | -43.8849 | 2026-09-28 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| aec91f9c-6664-3a00-baa4-440458632aa8 | -10.9536 | -50.6805 | 2026-09-28 19:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 82ed6885-b5b1-3442-b2fc-6e031976d6c4 | -10.8238 | -60.744 | 2026-09-28 19:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 228.6 |
| 5c32196e-856b-3ba2-acd8-92aeb40130d8 | -11.983 | -57.6066 | 2026-09-28 19:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 82d29dca-1802-30da-ae62-19f69a014392 | -14.4151 | -52.8165 | 2026-09-28 19:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| b5c0e016-3aad-3e0d-a9c6-8a5e59480871 | -5.4949 | -45.1249 | 2026-09-28 19:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 9e0259ba-81cb-3e5c-9b3e-42ddcb3b0def | -10.8184 | -61.4191 | 2026-09-28 19:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 8230fe43-ee20-30ba-bcec-6a3d48019e2d | -13.9012 | -53.6757 | 2026-09-28 19:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 07efa9e2-7287-3665-a79b-179697ab68d8 | -7.6851 | -54.7734 | 2026-09-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 27cbeb7b-4c7b-3e39-8eef-7a825b42daaf | -18.6834 | -48.6234 | 2026-09-28 19:30:00 | GOES-19 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 5a943a02-8233-36e0-9b7d-b3dd6690719c | -9.9595 | -50.1431 | 2026-09-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 87c037a0-d8ee-379a-8e85-9e7ff6accd45 | -9.325 | -45.3647 | 2026-09-28 19:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| d43758b7-d2a6-3ece-ac32-c78704528d72 | -11.1775 | -44.7832 | 2026-09-28 19:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| dbedbf24-b84b-340c-84cc-0d36089054a0 | -7.5159 | -55.0245 | 2026-09-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 1ba39c49-c6f7-39a1-bc7a-fdbb304396ad | -13.3267 | -43.9523 | 2026-09-28 19:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 8498ebe3-e071-32ec-a370-84f7b435c607 | -10.2443 | -50.0074 | 2026-09-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| d7c52ea7-3e48-3ee6-908e-89423acb8d5b | -7.6714 | -44.8779 | 2026-09-28 19:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b83ec715-9925-3765-959b-948286db01db | -9.0437 | -49.6317 | 2026-09-28 19:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| c26cd289-cd16-3bc0-8eb8-21aca31e967a | -7.7037 | -54.7722 | 2026-09-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 9ba2bcbe-a634-3c02-a6bb-ee5439ea36ab | -11.4791 | -49.743 | 2026-09-28 19:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 312c793f-a217-3bcf-9bee-00dab0b39278 | -12.702 | -47.3638 | 2026-09-28 19:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 9060728d-680a-3740-b968-56a4f861d733 | -15.1177 | -54.7166 | 2026-09-28 19:30:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ba033cc4-ed5f-37cf-af79-ef69335a18f8 | -10.2065 | -50.0113 | 2026-09-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| b0f22164-d49d-3f5d-b873-3a6c1620fd29 | -10.6505 | -50.7123 | 2026-09-28 19:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 8cb6484a-f9e2-3d48-a8d1-1f52aae52cd6 | -7.6852 | -54.7532 | 2026-09-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 7aaef33c-f73e-3efc-8e9a-01809475706d | -8.2809 | -54.6957 | 2026-09-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 843c1336-f5a1-387b-8281-c011d82078ab | -8.664 | -45.3469 | 2026-09-28 19:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 59209f49-5105-3684-a721-0e1b26ebaeb6 | -10.8191 | -57.1795 | 2026-09-28 19:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 5b2aff64-1115-3801-86c2-3a778d71c164 | -9.9266 | -60.7171 | 2026-09-28 19:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 176.9 |
| 3d5f1c73-f2e7-3395-bb5a-122fc6430524 | -8.2479 | -45.4583 | 2026-09-28 19:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 56c467c8-96aa-3d6a-b7ca-b3cc8a10eaa2 | -7.6903 | -44.8761 | 2026-09-28 19:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 23512455-33e6-31ad-9568-c15099d4161e | -9.1337 | -49.9656 | 2026-09-28 19:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 6a062718-a7d5-39d9-9a5f-182c57992a81 | -11.3436 | -54.1086 | 2026-09-28 19:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 268.1 |
| c4f9c223-bc74-377a-9c4b-4b242bfe0c19 | -12.1204 | -57.1567 | 2026-09-28 19:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 744812f2-79be-309a-8612-6b3f2bf51a09 | -10.9254 | -43.8876 | 2026-09-28 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 3b789f37-b52b-37e4-beeb-d8c3e99bd0b9 | -9.9787 | -50.1198 | 2026-09-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 3b56abbe-1fe4-3b39-a7df-65268296bab4 | -12.1391 | -57.1751 | 2026-09-28 19:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| debe9011-4988-38ea-a6e4-2bf7d752fdd3 | -5.7384 | -45.0626 | 2026-09-28 19:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 7083890d-2712-399e-a58a-1c3ba9b96149 | -12.6828 | -47.3666 | 2026-09-28 19:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 6014e7bd-1a10-3d41-a420-83f56c0fb96c | -5.7386 | -45.0399 | 2026-09-28 19:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |


[Clique aqui para ver as próximas entradas](README181.md)
