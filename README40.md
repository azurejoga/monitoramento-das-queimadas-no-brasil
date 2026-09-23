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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4289b273-6d31-36a5-8cc8-171dcf2f11d5 | -8.935 | -61.495 | 2026-09-23 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 621b65d1-aa05-335f-9a54-7062787ee8ed | -9.1211 | -61.4291 | 2026-09-23 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 514e0138-9e33-3fb6-81f9-e3dcf7fe77c2 | -12.7952 | -50.9171 | 2026-09-23 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| da4005b2-83bb-3a90-a96c-fe73723948b5 | -6.6146 | -59.9272 | 2026-09-23 03:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 91d2997c-b4ad-3896-9367-d6a1c10974b6 | -8.9164 | -61.4958 | 2026-09-23 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| e319a268-71b3-39a3-8b93-fe6889011348 | -9.1024 | -61.4491 | 2026-09-23 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 24e91de3-4abe-34fb-b7f2-3ef028baa5d7 | -14.6106 | -45.6438 | 2026-09-23 03:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 1295de06-e842-3476-88d3-9c53ba8f6fe0 | -12.0595 | -50.3634 | 2026-09-23 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| bbcbeacc-eb54-3795-93df-fb6d0cf39224 | -6.633 | -59.9457 | 2026-09-23 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| ef956d5d-089c-36cc-9149-239586e58673 | -8.9351 | -61.4759 | 2026-09-23 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1db4378e-be2d-3707-85cd-f0fcc24eca3f | -12.7958 | -50.8742 | 2026-09-23 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| c589d7a0-4389-33e6-b0ce-89118f930b0e | -3.2313 | -46.9596 | 2026-09-23 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| aacab302-2c49-38d8-927c-ed613e63ed8e | -3.6947 | -60.5645 | 2026-09-23 03:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 895c3e45-c48d-3b37-8e99-ad05b0df9fd2 | -11.2853 | -51.3454 | 2026-09-23 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 86a3812e-41f6-3f52-8d75-fdc4b21b03ed | -3.6946 | -60.5835 | 2026-09-23 03:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3aa552ce-855e-300c-a98a-04cabfcf0f97 | -11.304 | -51.3646 | 2026-09-23 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 46c44598-4db0-36dd-9ac9-c5c3c8cc7f67 | -12.0786 | -50.3611 | 2026-09-23 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 949a6a54-06fd-3207-815f-095c57b0922b | -6.6145 | -59.9464 | 2026-09-23 03:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 5cd95653-3aa2-3f90-9f76-9d93183fa35d | -8.4538 | -48.6944 | 2026-09-23 03:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 9a895038-8876-3044-8a90-42728fb32654 | -12.7763 | -50.898 | 2026-09-23 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b68df072-baef-3794-b096-36a44d285212 | -12.8143 | -50.9147 | 2026-09-23 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f28421bf-10c8-3261-9a39-1c5ee77a1174 | -14.6507 | -45.5902 | 2026-09-23 03:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| b609c418-d5f4-3dd3-8eed-ac8bb7587e00 | -6.6148 | -59.908 | 2026-09-23 03:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| a017e8c9-ab59-3c05-b36a-dfefe362b7e9 | -11.8871 | -45.7623 | 2026-09-23 03:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 20220d5a-753e-32e5-8121-4a69e245511e | -14.6297 | -45.6635 | 2026-09-23 03:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| bb27d2f6-2536-30b0-89db-e6db5e43d559 | -5.7567 | -45.1067 | 2026-09-23 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 9f3d3df0-dced-35bd-b3ac-2e1daa2a0e9d | -5.7754 | -45.1053 | 2026-09-23 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 957e6af2-a858-37eb-ade2-a2483a63787e | -9.0839 | -61.4308 | 2026-09-23 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 154c1804-4c97-3ab9-805b-2eb7ee1a1036 | -6.6331 | -59.9265 | 2026-09-23 03:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 242e54e3-b9e5-3126-9514-783338ad6a33 | -3.2314 | -46.9376 | 2026-09-23 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 4601f3a8-0e6f-377f-b1f1-66bcbdeff779 | -3.6763 | -60.5839 | 2026-09-23 03:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 295e7bdf-df55-35ab-b868-70ffaf9f9f52 | -11.3043 | -51.3434 | 2026-09-23 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| dede39be-4b72-3f32-8125-cf9db19297b3 | -8.8105 | -44.2757 | 2026-09-23 03:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 335e321d-b52e-3a84-8488-22fb4da34118 | -8.4726 | -48.6927 | 2026-09-23 03:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 630bb23b-a9b5-308d-ad60-83770f8c2727 | -9.1025 | -61.4299 | 2026-09-23 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| bfa92ddc-8917-31da-9a92-b30780af74b9 | -12.3679 | -50.1539 | 2026-09-23 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0ab813ce-ac4b-3903-b2ee-7d787953f5c2 | -12.4212 | -46.9777 | 2026-09-23 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 406f3af4-d682-3d3b-b7e3-a8dcadfc26f8 | -6.6145 | -59.9464 | 2026-09-23 03:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d4375136-cc37-34a8-938a-40b67b173ef7 | -6.6146 | -59.9272 | 2026-09-23 03:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 05d06f4c-41e9-37aa-ba2a-0508b7d8777f | -8.4538 | -48.6944 | 2026-09-23 03:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ebc212f5-4fbd-3fe8-a666-ce05a176c8a0 | -6.6331 | -59.9265 | 2026-09-23 03:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 305c3807-58d5-3862-8a59-8efd3d48cc2d | -11.8867 | -45.7852 | 2026-09-23 03:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 1dd8b5be-a808-3912-a9bd-61ec1fcf0f6a | -12.3679 | -50.1539 | 2026-09-23 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 806213de-512b-310e-b091-da5475942c22 | -12.1192 | -45.6368 | 2026-09-23 03:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| e03ecd58-38c9-3a3a-8fca-1baabba1faa9 | -6.5941 | -43.7333 | 2026-09-23 03:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| e3f248f6-9cd5-38c5-be95-9e5939ea925b | -11.8679 | -45.7651 | 2026-09-23 03:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| e62b7b80-f071-3bff-b2a3-8342e4d60738 | -6.6129 | -43.7317 | 2026-09-23 03:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 700.6 |
| 31feee6f-814a-369e-ab71-fc93c555bdef | -12.0599 | -50.3419 | 2026-09-23 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| dc969f91-c7e1-36a0-8e64-20967997c9c7 | -5.4069 | -49.281 | 2026-09-23 03:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d4ef76f8-2b91-398f-ba1e-dad0f5df1e2b | -9.1024 | -61.4491 | 2026-09-23 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 119d82f7-5fe4-32b2-a14e-0e196288c6dc | -8.9165 | -61.4767 | 2026-09-23 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ab394791-cf7d-3b1d-b9a9-b7df4b20e5b4 | -11.3043 | -51.3434 | 2026-09-23 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 5217feff-fa04-35b4-8497-273457842b78 | -8.9164 | -61.4958 | 2026-09-23 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 19276f1e-f216-301d-97e1-93378ff778a4 | -12.815 | -50.8718 | 2026-09-23 03:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3c1f72d2-3cd1-368e-9931-ae815bf54422 | -11.8871 | -45.7623 | 2026-09-23 03:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 28871914-6d21-3855-a041-00e53f62ff82 | -8.8105 | -44.2757 | 2026-09-23 03:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 76fc5e9b-76fa-3d20-8a65-6cd6c70826d9 | -9.121 | -61.4482 | 2026-09-23 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c4946f2a-37f6-3321-9a99-666afc5adea0 | -14.6507 | -45.5902 | 2026-09-23 03:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 31a1e2f0-11d2-35d9-ab21-b9997a3911cb | -12.0595 | -50.3634 | 2026-09-23 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| c74c74b8-423f-3118-8954-fc59920aeaf7 | -6.6315 | -43.7533 | 2026-09-23 03:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| be918e16-7c34-3f0e-bd4d-2c28408df4bd | -5.7565 | -45.1293 | 2026-09-23 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e4548588-a565-38c5-bae1-e17ea5e279da | -6.6317 | -43.73 | 2026-09-23 03:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| fd666511-6b89-3db5-8012-d05fe9928b61 | -8.935 | -61.495 | 2026-09-23 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 44109451-9784-311f-9cb6-6b19fd69574a | -12.387 | -50.1515 | 2026-09-23 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5f901765-5c66-397c-8dfb-479af0169867 | -3.6946 | -60.5835 | 2026-09-23 03:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 2875775e-26e5-33e1-ae6f-3aaf02477c96 | -12.3488 | -50.1563 | 2026-09-23 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| aec9cfeb-e0f4-342e-b91f-06528b92446c | -6.6127 | -43.7549 | 2026-09-23 03:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 619.3 |
| 15d2a931-0d0b-39f5-b0d9-140fe848a796 | -11.304 | -51.3646 | 2026-09-23 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| d82ef65f-74ed-3a2f-93bc-a010cbbd50ed | -6.5939 | -43.7565 | 2026-09-23 03:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 4f019096-b644-3f82-9e65-5a4e8f75a724 | -9.1211 | -61.4291 | 2026-09-23 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 1ea7fd9d-c0a9-3116-a43a-8beff6710a49 | -5.7567 | -45.1067 | 2026-09-23 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 2e654ca1-c9a6-3fd7-a745-e0dd14400284 | -12.4216 | -46.9551 | 2026-09-23 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| d390943a-303c-3de0-92c1-43ac2bef0f92 | -9.1025 | -61.4299 | 2026-09-23 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| cd53e27a-4b5e-38e0-8b12-ea7075148b26 | -11.2853 | -51.3454 | 2026-09-23 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4e34aac2-0e7b-39c9-87e3-2a5eeadb6b79 | -11.8675 | -45.788 | 2026-09-23 03:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| e1e84101-54ac-3299-9576-2ca0c9f94fe9 | -6.633 | -59.9457 | 2026-09-23 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 59d069fc-8793-3b15-aeb0-57029d910dc8 | -10.716 | -48.7246 | 2026-09-23 03:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 1be50300-2cd7-3ee6-a51c-8ed10f0ce6b0 | -3.6763 | -60.5839 | 2026-09-23 03:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 781fc23c-6491-3173-858f-f0f9090add67 | -6.6148 | -59.908 | 2026-09-23 03:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 5a61c075-f6a2-37a1-82dd-cc7d27e8abb2 | -3.22937 | -46.95006 | 2026-09-23 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b7e20511-6d4d-3178-9066-ba1eaefe8007 | -3.22526 | -46.9572 | 2026-09-23 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 107ec104-ca09-359c-b32c-403e2281479e | -5.18096 | -35.94882 | 2026-09-23 03:42:00 | NOAA-20 | SÃO BENTO DO NORTE | RIO GRANDE DO NORTE | Brasil | 2411601 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| acbef0c1-b154-37c6-95f1-716238727050 | -3.23061 | -46.94313 | 2026-09-23 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| dadb9b0e-0b58-3cd8-af1a-8fdd1db24a28 | -3.21942 | -46.94833 | 2026-09-23 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7c24dae9-5afe-3609-8e34-485df8fce516 | -3.22232 | -46.9483 | 2026-09-23 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 818f1a46-868c-37e4-a16a-4f4053e463fd | -3.22356 | -46.94137 | 2026-09-23 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| aff28381-a122-373b-a079-b62cd35c8ede | -3.22107 | -46.95529 | 2026-09-23 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| cfd24ddd-331e-3581-9fb7-bb6d53e15efe | -3.22644 | -46.95034 | 2026-09-23 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a3b54b74-ff72-306a-829f-52727963093d | -3.22763 | -46.94342 | 2026-09-23 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 5396cf28-856b-3883-ae17-9f1dd09c7646 | -3.2206 | -46.94152 | 2026-09-23 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3204802d-0215-3923-97d9-ce55cc80d886 | -6.57179 | -44.15664 | 2026-09-23 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 17ca452a-ce42-3b34-a814-e8f93f9f0d7d | -5.93508 | -35.61936 | 2026-09-23 03:42:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 30991d41-c823-34f5-9a67-d61192abe849 | -6.93016 | -46.55841 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ce0138a8-7fcb-3bc7-89de-1b4bf0467c75 | -6.19028 | -45.31803 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55bb7410-83ad-3231-b0f2-4f463439b47c | -6.60601 | -43.74137 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| d40b0012-c84a-37e8-ada8-9224897d6c5d | -7.13273 | -43.07523 | 2026-09-23 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 996df26f-7455-3a8f-b8ec-37609436af95 | -5.28125 | -47.2576 | 2026-09-23 03:42:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 468618de-4118-341d-9220-0bd5648af7f6 | -5.34771 | -45.16397 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 33061734-983b-308f-945c-7ba7401907c3 | -7.49729 | -44.33009 | 2026-09-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4e39e64-873e-3d8a-bb5b-a882f6f9e3c4 | -6.92584 | -46.56738 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README41.md)
