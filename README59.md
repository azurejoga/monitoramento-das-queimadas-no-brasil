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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 649227c7-bf2e-3408-aa7a-fde15bab9409 | -3.9317 | -59.33358 | 2026-08-25 05:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3874bad9-196e-34ea-93ea-ae1dc0777829 | -5.95564 | -53.59884 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7795e28a-fb55-3d27-b474-134696904fe1 | -4.1911 | -54.57951 | 2026-08-25 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60739e37-b167-3b6d-95a0-6a3eaf148ce8 | -4.19199 | -54.57624 | 2026-08-25 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c2e96bb-cd29-332a-8601-505b9909cbc6 | -3.55116 | -54.49541 | 2026-08-25 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e95e4cf-87af-32b7-98bd-2b9ca1aac727 | -3.54645 | -54.49138 | 2026-08-25 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6695ea73-7f06-303e-9f39-ea5321635fca | -3.1306 | -61.18759 | 2026-08-25 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b77433ef-828c-351f-a810-359c55bdd0ca | -5.00742 | -56.13634 | 2026-08-25 05:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cb58c95-2bfb-3c31-8c50-c0b56f021d96 | -3.10368 | -61.22506 | 2026-08-25 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd91a7b9-c492-3aaf-8f44-54d1ac0d1f49 | -4.47876 | -54.80716 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28c26230-483b-3017-8461-f94c7df07941 | -3.49083 | -59.29399 | 2026-08-25 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff4b4f61-8be0-3244-bf48-635cf1c0f3a2 | -3.09685 | -61.20129 | 2026-08-25 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6466b2b0-3e3a-3601-95f2-6d4480907806 | -1.42324 | -55.7272 | 2026-08-25 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a23cb0e-ee64-3dda-bd36-a4c404e0f72c | -3.59276 | -54.04223 | 2026-08-25 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75374353-2379-3222-a54f-5842acbc9173 | -3.59553 | -54.84051 | 2026-08-25 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9c6f55a1-c095-37a1-9d4a-9f06633bcb77 | -1.74735 | -55.25052 | 2026-08-25 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b3f01c8-887a-3d93-b908-eda1de3a26d5 | -1.41861 | -55.72651 | 2026-08-25 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85c74c8e-a183-3ad1-9944-413fedd3dbe6 | -3.1334 | -61.21452 | 2026-08-25 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78da291b-fc29-336b-8ad7-e3daf49644be | -5.9515 | -53.58654 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa3efed8-780d-3651-b50e-f8862c8153a8 | -4.13845 | -56.36224 | 2026-08-25 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed41c965-b92a-383f-8019-924a60e9638f | -5.95454 | -53.6067 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 840a8993-6712-3db2-a11f-8ccdded7aa4b | -3.39033 | -59.56803 | 2026-08-25 05:46:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f18dccb-adc5-370d-b2b8-e7fceeaacba2 | -4.4965 | -55.46521 | 2026-08-25 05:46:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7512ec5f-5293-3322-af73-6e3fc16678ee | -6.99587 | -59.24456 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| ed45f704-3673-371e-9f5b-a671b635d51f | -6.71851 | -59.44508 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0881632-0bde-3e3c-8a0c-2ec189ce1b69 | -6.12881 | -57.83219 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 646987c7-0490-30bc-8e40-cb9a99f35e65 | -6.74771 | -59.64743 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 352926ed-3d6f-3749-9948-ff5492ddc8f8 | -8.57234 | -54.84918 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f7ccc7c-0a7c-3f31-a86d-6af5d6ea7e14 | -6.55887 | -56.55571 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b82a536-db17-324c-af2d-f2bfa46d4136 | -6.15384 | -57.94547 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cbaf219-217b-32b0-807b-414a45a2d293 | -7.00225 | -59.25613 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| aff52a76-6ccf-34d1-93b0-9697f949fbdd | -9.02815 | -50.82051 | 2026-08-25 05:48:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9ecfc9f-c67f-33ed-a509-6175344b879d | -9.03181 | -50.81965 | 2026-08-25 05:48:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 276ad4e2-df8f-3597-9a18-5020ad5a0a8f | -6.85879 | -59.41252 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 90cf55b4-1d76-35a6-9c5c-3e3072121a24 | -7.01567 | -59.2477 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7122db67-3722-34d0-ba7c-c20ba33404a0 | -10.42946 | -61.22685 | 2026-08-25 05:48:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bd003bb-fd4a-3883-8f93-989dff161926 | -10.77881 | -50.92241 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 75a9b9d5-5fe7-3db2-afbe-5962017df1ed | -6.26493 | -55.4225 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0e3f57e-3484-35b0-9c73-2e23188d3093 | -6.83493 | -52.50264 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54a10446-8981-3c0f-ada2-b683779d93a0 | -7.49177 | -55.35078 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c595827-bbbb-3815-9326-bf88c950e6d6 | -8.21702 | -54.99672 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d91b177-3106-3ac3-af07-3530cd576ec3 | -7.48994 | -55.36366 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31075359-1d4d-3871-a5b4-c3c90c3b3c15 | -9.23248 | -60.38575 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acf3a24a-396a-3e65-a350-2aff1c9f97ef | -7.20618 | -60.61876 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f4f3770f-365c-35a7-b6e8-e46bf2e7ba5b | -6.32859 | -54.74654 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef9f347a-9bbf-3019-bf0a-34e8d194cba7 | -6.63996 | -58.48211 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e621426-a1c8-32e0-a963-2e1b51f74a1a | -5.90921 | -57.71413 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7216e0a-2663-38a9-a769-fceafb983e57 | -6.81881 | -59.60098 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 610873e9-866f-3924-a785-f437b371a90f | -6.74865 | -59.66716 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dcbfd60e-da3c-3c61-af22-e6f1b9b62cbc | -6.21397 | -55.48957 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 736df544-879e-361b-8bd6-f613bb98ec16 | -7.38889 | -55.17537 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e52454bc-37a7-3a4f-a28e-912a0e5e67c1 | -6.17793 | -53.4851 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5babb4fe-943e-3410-98b1-87d391bb1bb2 | -6.26073 | -55.4155 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f933c824-a489-3305-8b20-de28ff6646a3 | -8.54401 | -55.30059 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af037051-8b32-3613-ba3c-f97e8b6fd492 | -6.79837 | -59.81685 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e2281ff-fee9-3919-8b7b-72b458e18d5c | -10.77964 | -50.91527 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b4fb7852-d94a-3442-a8b9-cc8c1e81f8e3 | -6.34568 | -54.77978 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3705444f-f1c1-310e-abf2-2e8c1457629f | -6.81637 | -59.59076 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7f73357-998c-3230-8441-164679e60746 | -8.22245 | -54.99717 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2e24551-6545-39c1-97ef-31b9c36c69cb | -6.80037 | -59.42898 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a79c3122-eac1-3e8a-af99-e1a83d5a4038 | -7.00546 | -59.26177 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e4b20ce3-439d-3919-9b54-c41c4db3e2df | -6.33926 | -54.74807 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 472a7e23-9166-387c-9a02-f2187c5a007f | -6.61055 | -58.38206 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22161649-f75d-3d1c-945b-c95f0d423b83 | -7.00942 | -59.26235 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b66a57b2-4882-3b38-b1b3-daed4d24e0b9 | -6.34129 | -54.77231 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20b77291-6710-34ad-9db5-5dc14a3eec28 | -6.44106 | -54.97092 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2677cb3-f48f-3a15-9b73-2df7216131c0 | -6.80428 | -59.42956 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dc16763-1b51-35a2-85c2-98cb2a4a0f24 | -9.19302 | -59.45005 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd934895-4770-340c-82a2-bc5218323b04 | -6.80326 | -59.40911 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46c026ee-7a2c-3ea3-9e3a-cb38e135df9e | -6.12261 | -57.81463 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 515d11c4-5386-3e56-a956-dc9a6c43e1bf | -6.82283 | -59.41206 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e52c41a7-9630-3bd6-809f-4f189544b5e1 | -6.23031 | -55.48361 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 090fbdbf-950b-3701-9a92-bf83c5ed8d05 | -6.8009 | -59.58831 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bc41863-f775-370e-91fd-8ae857ba7159 | -6.63058 | -58.48837 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f88058b0-ccc8-30cb-b257-81494950050c | -11.1632 | -53.99911 | 2026-08-25 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28baf4da-fb09-3981-9353-f5381611cb72 | -8.8203 | -62.33977 | 2026-08-25 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a36b8ef-14a0-3678-913f-8352103e1555 | -8.81053 | -62.33439 | 2026-08-25 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b50b9e2-e7de-3a8d-ae49-a378047cae58 | -6.34224 | -54.7656 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fae44548-7012-32fd-9e18-989acd187401 | -7.49655 | -55.35452 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04c96cec-3e05-3e50-8e36-7b586de3a7df | -8.56869 | -63.0218 | 2026-08-25 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e065f7cd-b429-3f42-b156-dd7939ad6730 | -6.80988 | -58.65781 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41a99b4a-5429-36aa-a318-eac60ec15687 | -7.31985 | -64.69704 | 2026-08-25 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1ee1fe5b-acd9-3fc6-8786-73c7c0a9d816 | -9.19962 | -59.57584 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29658052-915d-3d33-a8c3-13b4a0a6e9f0 | -6.33738 | -54.76146 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69b88502-4afe-3f3d-bb7f-f745936f8dcc | -6.35196 | -54.77376 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a017c821-2e17-3303-8667-b03cd404ccce | -6.17406 | -53.47401 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1797f8b1-a8c8-307e-a11f-6435d07d393f | -8.17491 | -54.96521 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e039b585-a338-33ff-80ad-91e738d94ad0 | -6.78607 | -59.63538 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cfb6f083-1e61-302c-b58e-310109281e08 | -7.00698 | -59.25161 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a83499f-39b9-3ebf-a7b6-ecc102512562 | -6.80792 | -59.59438 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caf83129-f328-3f93-8ca1-ac09aff49b8f | -7.54315 | -61.36773 | 2026-08-25 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1d1c77fe-c6d7-3293-a685-86f83a77597c | -6.85487 | -59.41193 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64abf51f-776b-3132-9b1a-ad8e3569c2c4 | -6.95874 | -59.0808 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73107692-67a6-3e45-8aee-5b808b9aa477 | -8.66651 | -62.8399 | 2026-08-25 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f2d1122-53ae-3145-8fe2-0155bbcb48f4 | -6.34177 | -54.76893 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50aa1d9d-3c60-39c9-bbb0-4fe9e522f3b3 | -11.16455 | -54.00285 | 2026-08-25 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 811bd64e-6450-30de-951d-f8ca3e72bf9a | -8.81456 | -62.33115 | 2026-08-25 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4bb8503-506a-3e6e-8607-bddb22b8e280 | -9.17142 | -58.33084 | 2026-08-25 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a151a5b-88d3-35c0-9a7b-01489ee4c7fc | -6.88949 | -59.95623 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a7677cb-0a05-3ef0-bda9-d6e438a6dc5a | -10.78119 | -50.92801 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 32.9 |


[Clique aqui para ver as próximas entradas](README60.md)
