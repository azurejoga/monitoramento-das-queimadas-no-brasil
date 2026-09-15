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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecaf49cf-f53a-3ef4-bbca-4e046d55d5d6 | -7.5609 | -62.3111 | 2026-09-15 15:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 2a92835a-a185-3253-91a1-9b576c1ab4e7 | -3.5727 | -58.5389 | 2026-09-15 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 404.9 |
| 1688f925-8872-35fc-9984-adb1459ddceb | -1.3558 | -49.2732 | 2026-09-15 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 7f0836c8-1851-3455-a321-6df8fc837ea8 | -10.6112 | -57.3138 | 2026-09-15 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 0866d9fb-25d3-3b36-89a5-b0686a95788b | -9.1337 | -65.8253 | 2026-09-15 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 72d53992-b283-39e4-b5ae-6185f2c1bbce | -6.277 | -41.6841 | 2026-09-15 15:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 68cdc4ec-a873-3a10-9d7d-45239ff1a59f | -2.4815 | -49.3996 | 2026-09-15 15:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4b32a22c-a42d-34f3-9478-b70f10313793 | -8.7889 | -45.8999 | 2026-09-15 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 6b1342a6-3ea7-3652-9928-30099b4a8168 | -8.114 | -45.6301 | 2026-09-15 15:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 054ba703-f44b-3d93-98e8-135fa5339c5d | -10.3113 | -45.3366 | 2026-09-15 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 70906364-149b-3c8f-822f-f4615310924c | -11.2677 | -54.1361 | 2026-09-15 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 375ecf6d-22dd-3685-9aa1-4eed63948b49 | -6.6952 | -58.7097 | 2026-09-15 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d5c1aece-7ba4-3cf3-98d9-a082e0d877a4 | -11.1017 | -50.9199 | 2026-09-15 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 5c29addf-90f9-3585-acc3-d5bf5a17f210 | -3.8378 | -51.7637 | 2026-09-15 15:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d7143f1a-e658-3f50-b593-81b4f6ad65d9 | 1.2244 | -50.7266 | 2026-09-15 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a0166b62-60af-3e91-b5da-34ffce827f9d | -8.8078 | -45.8979 | 2026-09-15 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 4df06dbf-91b7-3dd8-b5e3-b42cc9ef90f0 | -12.4707 | -41.4047 | 2026-09-15 15:20:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 1daf1b2c-79db-3b93-abd9-3cc2b2608b64 | -9.376 | -50.1352 | 2026-09-15 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 39e120bc-e544-3fcd-b00e-cbece27e332b | -9.7687 | -46.1067 | 2026-09-15 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 9f52c878-7066-300a-b967-05310e6f0356 | -13.4468 | -54.5968 | 2026-09-15 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| b2d8db8e-0fa1-39c0-aa09-0099ab141248 | -10.2922 | -45.339 | 2026-09-15 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b45c0ff3-80fd-388d-a9cc-90f4f68126c4 | -8.8361 | -62.489 | 2026-09-15 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| eca2d963-bd21-34c0-b1d1-43b462da423f | -8.638 | -44.4567 | 2026-09-15 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 422.8 |
| 9e00661b-9495-398b-9642-9a2bfc6ad34e | -10.5924 | -57.3151 | 2026-09-15 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| dccb0f85-c652-312d-94f4-b18363ba0284 | -2.7768 | -49.4553 | 2026-09-15 15:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| e86f5187-cb7b-307e-a07b-5fc53e271e1c | -14.0133 | -53.8709 | 2026-09-15 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 85f68468-531b-3e12-a225-e6c2ca00ebcc | -15.5974 | -53.8426 | 2026-09-15 15:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| a11b7f14-2b17-3e86-804f-2950c8bb3f1d | -8.827 | -45.8733 | 2026-09-15 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| c777b14e-086d-3e9f-88c9-882f4929b0db | -15.3797 | -52.9652 | 2026-09-15 15:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 76196776-a145-3991-9881-5c7b8cc103e4 | -15.5981 | -53.8005 | 2026-09-15 15:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| b932ae3c-bdbe-302e-afec-b22087031bce | -6.3574 | -44.9023 | 2026-09-15 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| e9578e2a-b13d-314a-b9cc-6c744a4d2cf0 | -12.6826 | -54.6763 | 2026-09-15 15:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| f611b01b-d0dc-365b-afcf-1d6fbf7acfab | -15.3598 | -52.989 | 2026-09-15 15:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 0902eefb-d560-332f-891d-4e09affd9d1f | -12.126 | -44.2225 | 2026-09-15 15:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 846d7150-6b5d-3966-8476-14b0365517b5 | -6.0169 | -52.1614 | 2026-09-15 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7b587243-ceb4-3e9c-bd61-974ce364149d | -8.8361 | -62.489 | 2026-09-15 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 43508f9a-1603-3db1-88ec-e92009374b2a | -13.7006 | -51.8061 | 2026-09-15 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| aa2b2dbc-d2a9-3428-a9c8-d838e89ff275 | -3.1816 | -61.1045 | 2026-09-15 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 56a7f003-167e-386e-94dc-bd5193cd1b01 | -1.861 | -54.4315 | 2026-09-15 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 2c680fdb-e595-3b5e-8b93-802d26f24746 | -8.6293 | -63.0085 | 2026-09-15 15:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e75ff28f-d224-3e06-b7ed-43eb7ae7d991 | -7.5582 | -44.9116 | 2026-09-15 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| f93f279b-5eed-35ff-8839-5d97cc16c9db | -10.2926 | -45.3161 | 2026-09-15 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 115fe903-cb2c-362f-b93c-98143a0c48f5 | -14.1822 | -51.7653 | 2026-09-15 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 03e32d3a-7393-3d30-86bf-2d33c75fdcaf | -7.5397 | -44.8905 | 2026-09-15 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| ff644b9b-f428-31a1-8aa0-3b5d1a1adb99 | -10.6112 | -57.3138 | 2026-09-15 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| cf0d2ac0-c6f2-36bb-b461-819e286a1da5 | -10.7084 | -50.6212 | 2026-09-15 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 91c04857-fa15-3872-b803-5229b9bd48a5 | -9.4931 | -56.7564 | 2026-09-15 15:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| cb69134b-f141-3763-95b0-6e8aaecf5fcc | -12.6824 | -54.6968 | 2026-09-15 15:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| e6d84e72-bfed-383b-9f2d-0355495f3421 | -12.6821 | -54.7174 | 2026-09-15 15:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e60ef78e-4c70-3c48-80d1-dca1d9893afc | -9.7358 | -47.0958 | 2026-09-15 15:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 41d75ee1-d7d8-320c-b9e5-1d4961c8668a | -3.8096 | -58.8994 | 2026-09-15 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 29e1adc5-067d-399c-a3f6-b15ad5d8272a | -15.2821 | -42.8075 | 2026-09-15 15:30:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 90.2 |
| bbef8964-994a-3d46-844a-d54eea4fb118 | -15.5779 | -53.8451 | 2026-09-15 15:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 485574f3-df76-3aa2-960d-e425ecbfe3dc | -13.6526 | -45.993 | 2026-09-15 15:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 74fb563a-8a37-3e23-b551-73bdcb5db92e | -9.1337 | -65.844 | 2026-09-15 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 4f78ca67-16eb-3a20-bec0-80d4ecfd845e | -6.2832 | -59.9202 | 2026-09-15 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a2e3b5b6-51d2-3666-b4bd-7b1065c99b48 | -2.9815 | -54.1492 | 2026-09-15 15:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 693a04c3-1879-3275-81f8-38023ecf43f1 | -9.3954 | -50.0908 | 2026-09-15 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c74495f3-72a5-34b2-aa92-445e582b6f87 | -9.3575 | -50.1156 | 2026-09-15 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 425e9f89-23bf-3af6-8edd-1e68fafef3dd | -8.7892 | -45.8773 | 2026-09-15 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 8d6dd008-5573-3999-813a-733ea0903e48 | -9.1337 | -65.8253 | 2026-09-15 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 118c1d56-f750-3b6e-9f94-95c994403828 | -15.5977 | -53.8216 | 2026-09-15 15:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| c2a7e8d3-3cbb-341a-b15f-ea9cb536057c | -5.8136 | -52.0897 | 2026-09-15 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 93b7e7b7-bf1f-33dc-b5ba-10029b395b64 | -5.8321 | -52.0887 | 2026-09-15 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 03007255-e763-3e71-8549-191bbb6af7fc | -15.5195 | -53.8527 | 2026-09-15 15:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 16a63935-6bdc-3715-8152-0d42aa4de29e | 1.0767 | -50.9572 | 2026-09-15 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 087eca69-9e19-3e64-b2d2-e064bfb93718 | -15.3797 | -52.9652 | 2026-09-15 15:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 521d3564-958c-33ca-b26b-6666c05ab04e | -6.0169 | -52.1614 | 2026-09-15 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 525af3ed-a452-37a2-96ca-2b489cbfe8ab | -6.6767 | -58.7105 | 2026-09-15 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 5082db4b-8e65-355f-82d4-f74c41025eae | -1.2268 | -49.1899 | 2026-09-15 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 3cb250ca-281d-37eb-b1a9-5b80cfca9da9 | -12.6826 | -54.6763 | 2026-09-15 15:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 68cd154e-be52-372e-8f74-0c15c08b9c82 | -13.4468 | -54.5968 | 2026-09-15 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 24df6e5d-0469-3c22-a2af-45a4904efe49 | -15.3598 | -52.989 | 2026-09-15 15:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 5645d5b1-be2b-319d-ab2c-d5302ba235d4 | -6.6021 | -58.849 | 2026-09-15 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 9a8fed73-3721-3607-862b-1e242126f709 | 1.0951 | -50.957 | 2026-09-15 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 90521849-c99b-3368-96c9-6cc6943aa207 | -15.2859 | -53.9037 | 2026-09-15 15:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 017804fe-f5d2-374f-aa3e-5b58f9366311 | -13.7002 | -51.8274 | 2026-09-15 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 2c486fea-7ced-38d8-bf39-e0a5a7a53447 | -14.2985 | -51.7286 | 2026-09-15 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| b962259a-f7d9-3996-bbf2-742b9690ff6a | -15.5786 | -53.8031 | 2026-09-15 15:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| f60879be-3aab-3780-9511-8f948210571d | -12.6636 | -54.6782 | 2026-09-15 15:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 79600abe-13a0-36da-bdff-657c417a818a | -10.312 | -45.2907 | 2026-09-15 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 69d4f981-9e06-342c-aa99-2e89c6fde258 | -5.6225 | -45.5002 | 2026-09-15 15:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| c5286dda-ec41-37e4-8c55-571c66c1001a | -6.6512 | -43.6587 | 2026-09-15 15:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 87cf9a5b-e512-3150-8ad5-898477362024 | -9.3569 | -50.1583 | 2026-09-15 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 6de7bc8a-083b-3d8f-b5ea-d1628f098c3c | -15.5588 | -53.8266 | 2026-09-15 15:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 5bc12746-9bf3-33fa-9b38-e7f01042c448 | -12.6633 | -54.6988 | 2026-09-15 15:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 18053e43-78c6-3a51-994e-5c6cb5b3b49f | -6.3574 | -44.9023 | 2026-09-15 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 20932200-2117-3aab-8fcb-5a8800ce45c8 | -2.8839 | -50.4428 | 2026-09-15 15:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 36c2e055-fe22-3ce9-9aec-ccb0f8b7166a | -9.7687 | -46.1067 | 2026-09-15 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 7249cb8e-de38-3970-97d0-84f8b4763ec8 | -8.5417 | -54.6985 | 2026-09-15 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| f2a3d588-f8c7-3e68-a67b-33bbee905e28 | -12.1265 | -44.199 | 2026-09-15 15:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e7b919c1-614c-3fb9-a89a-3540bff13770 | -5.8135 | -52.1103 | 2026-09-15 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b0dbc90f-fe73-3e20-ac65-28c59bbc8f94 | -9.6104 | -46.5967 | 2026-09-15 15:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 8963f8a3-021f-3380-a9df-49aee768f159 | -11.5041 | -45.7939 | 2026-09-15 15:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 7486ffa7-4e28-360c-94be-30604e055cee | -8.8459 | -45.8713 | 2026-09-15 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 16532a19-a5b7-3a5c-9fbc-cc95ea1fbdfc | -10.5924 | -57.3151 | 2026-09-15 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6ac0f3f3-1225-3f09-bfd8-a6e62740a6ba | -8.7889 | -45.8999 | 2026-09-15 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d5466438-aa03-32fc-b39a-0fba1556a589 | -15.2475 | -53.8876 | 2026-09-15 15:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 36.7 |
| d7161bfc-1932-34c9-a123-f8337b178e83 | -9.3954 | -50.0908 | 2026-09-15 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4dda6ee6-28a0-39d6-91f7-821f1351365e | -10.0293 | -52.12 | 2026-09-15 15:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |


[Clique aqui para ver as próximas entradas](README87.md)
