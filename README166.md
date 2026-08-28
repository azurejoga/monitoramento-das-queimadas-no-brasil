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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 090b0cbf-3fb7-3bd3-8b09-04c1bac4af99 | -3.68157 | -50.93628 | 2026-08-28 18:49:00 | AQUA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 17e2c4b0-7f2a-37cb-bda2-7071b44d6021 | -7.34764 | -55.16855 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 557dae24-9005-3711-9556-aa2fd68c95fb | -4.7954 | -43.14295 | 2026-08-28 18:49:00 | AQUA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 821e6866-f0ff-3e16-b8ef-bee7df9f6d3b | -7.50133 | -55.28942 | 2026-08-28 18:49:00 | AQUA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 42cda619-4fc3-3767-8f90-2fea26ae1ede | -3.71261 | -45.26155 | 2026-08-28 18:49:00 | AQUA_M-T | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 400c16e4-da04-385c-8812-d33b75a58c86 | -3.22277 | -48.81223 | 2026-08-28 18:49:00 | AQUA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 9e701c6f-a538-3a8d-aa75-13ed8529d726 | -5.37269 | -45.66033 | 2026-08-28 18:49:00 | AQUA_M-T | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1b73359b-11fa-3e8f-a5f0-161cd023b75f | -5.2145 | -49.18098 | 2026-08-28 18:49:00 | AQUA_M-T | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3139d328-46f5-3b3c-b782-6480f30b3336 | -3.35175 | -44.23298 | 2026-08-28 18:49:00 | AQUA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 659c6ac5-e838-320f-9037-c9294b7ff6ea | -5.02487 | -47.05345 | 2026-08-28 18:49:00 | AQUA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fe3f1ac0-97e4-3f22-b3b3-11804a84b2a6 | -5.95511 | -44.80692 | 2026-08-28 18:49:00 | AQUA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 0c345f5b-dffa-3129-b328-7daab93f68a0 | -4.93473 | -47.45393 | 2026-08-28 18:49:00 | AQUA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f873f0f2-acd4-3992-9d3e-c9a0f45e222d | -14.6024 | -53.1508 | 2026-08-28 18:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 82e6ffa2-dfa8-3ca4-a6fe-b91e003be3f3 | -9.2099 | -59.4027 | 2026-08-28 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e9b43341-e952-31ca-bc7f-14e84b73bfcd | -11.2314 | -54.0164 | 2026-08-28 18:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e00db4cf-40b5-3510-b26b-74e5b86af992 | -11.2493 | -45.0501 | 2026-08-28 18:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 4184cd48-12e4-32ba-9ba2-43af6f45ec7a | -10.3391 | -49.9762 | 2026-08-28 18:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 5ad35943-240f-3efe-9957-86975546b9a5 | -8.6673 | -62.8369 | 2026-08-28 18:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 1f0d0366-8dba-3e4e-a7d2-09e4f17de486 | -8.5975 | -54.715 | 2026-08-28 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 884850bc-0341-3998-8abf-adb8945de69b | -7.4734 | -61.4037 | 2026-08-28 18:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 68d7a89b-f29f-3c3c-b967-e41fff81d574 | -7.5478 | -61.3056 | 2026-08-28 18:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 133.1 |
| aa1321e7-eba6-371b-a720-d1062b2574e7 | -4.3021 | -59.4826 | 2026-08-28 18:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| f768a1c2-2dc1-3786-ac3b-283f7f9535ac | -13.5991 | -45.772 | 2026-08-28 18:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 0c143443-5c48-384d-a0a5-c5a3b5457ea3 | -11.2128 | -53.9976 | 2026-08-28 18:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 28732bc2-c325-3306-b843-052a67a7c4ba | -6.8957 | -43.6368 | 2026-08-28 18:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 6a262e87-95b9-357f-b7c6-86f7e26e551f | -6.7513 | -55.6853 | 2026-08-28 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 03125da5-639c-3bdf-ab20-de822ece48dc | -8.6694 | -49.5369 | 2026-08-28 18:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 009db80f-68c5-3287-bf34-e80924091dd6 | -11.1995 | -55.1008 | 2026-08-28 18:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 02571bde-543f-3265-bba9-7e5220141517 | -9.1711 | -49.9835 | 2026-08-28 18:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c914fb26-cea6-3b77-808d-acaa8530cab7 | -6.8384 | -59.4571 | 2026-08-28 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| aabe8cf9-1005-31ad-9858-64f6046a6451 | -8.6487 | -62.8376 | 2026-08-28 18:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 89029a11-01b4-3bfe-8a15-9d687d631378 | -3.2361 | -61.2359 | 2026-08-28 18:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 69fd1123-b66a-3bc0-8fe2-2c28ae4b5cef | -8.631 | -66.5473 | 2026-08-28 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 9e1a88da-f675-391e-b326-028d19abdf6f | -8.3785 | -70.8456 | 2026-08-28 18:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 0f566158-20b6-3d6d-bfe5-0ff784a37170 | -6.1657 | -57.7793 | 2026-08-28 18:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 169.2 |
| 2a6fa255-4b01-35ea-bc8d-0ddae1c231da | -10.3897 | -61.2118 | 2026-08-28 18:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| a214db76-473b-3b4f-a7e1-764a927a2744 | -4.3205 | -59.4821 | 2026-08-28 18:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b13d237f-1b67-35d3-b3bb-52bf84d4519d | -12.0538 | -47.1865 | 2026-08-28 18:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| af9c1a6d-b50d-3fff-81d6-2fff7647e12c | -7.4735 | -61.3846 | 2026-08-28 18:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| e7abb09e-81cd-3858-aabb-7d78d97ea765 | -8.8184 | -49.6308 | 2026-08-28 18:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 7f220a56-d783-3246-a96b-943f1a9d9272 | -9.9708 | -53.9419 | 2026-08-28 18:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 6019cd99-feee-372f-86cf-0ed2b011c2b4 | -11.006 | -49.6461 | 2026-08-28 18:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c9427a2d-7846-37a4-a8e8-515d837ad774 | -8.0739 | -45.8372 | 2026-08-28 18:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| a134ad67-d68b-33b7-afd3-fa5d70bbd3f6 | -6.7279 | -59.4423 | 2026-08-28 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 3a26db2c-0ab4-3c04-9fa6-1d6e1085df7e | -7.529 | -61.3635 | 2026-08-28 18:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| d43841f1-15ae-3b64-8d4b-95861d694332 | -8.9553 | -50.7882 | 2026-08-28 18:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 05adf714-d30f-36c2-b048-e8a168b212fb | -14.1784 | -48.7703 | 2026-08-28 18:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 109.4 |
| dd743388-b7b1-3f1d-a6b6-700e344ca539 | -6.1841 | -57.7786 | 2026-08-28 18:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 24b89523-5ac2-3b45-96fe-8a22077bf24e | -6.8569 | -59.4564 | 2026-08-28 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 122f768e-15af-3324-8fe4-8bd68537a1de | -9.1895 | -59.6364 | 2026-08-28 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| a4dace11-f305-3128-9695-4e3bc402c656 | -6.8358 | -59.9379 | 2026-08-28 18:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 24f54356-a93f-3595-a221-055553dfca2e | -4.1696 | -42.4346 | 2026-08-28 18:50:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| ef62726f-144a-3770-a7d2-4295411157ab | -14.1835 | -52.8456 | 2026-08-28 18:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 146.1 |
| d4442ea4-1257-37d5-a9a1-7a0f0685ca27 | -14.419 | -52.5837 | 2026-08-28 18:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| da6194f9-ea50-377f-aa19-13ca97f6aa34 | -9.1525 | -49.9639 | 2026-08-28 18:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 5d87eb77-4033-3138-92a6-2f04708785cc | -6.8571 | -59.4179 | 2026-08-28 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 6a4cb420-55cf-3600-8d2f-3ab52a9386f3 | -4.3022 | -59.4634 | 2026-08-28 18:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 9ea68515-c176-3999-8179-8cba5695807c | -6.5323 | -55.2378 | 2026-08-28 18:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 4fa7af0b-9fc8-37f5-9e57-2f1e3266e062 | -9.4825 | -66.6347 | 2026-08-28 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 23d3140a-38f0-3d54-8f17-467bcb21bf2c | -9.4331 | -51.6716 | 2026-08-28 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| ec29234d-ab07-3094-aa14-89a97cab6b47 | -7.6031 | -61.3225 | 2026-08-28 18:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ee398650-70c2-3473-abb4-a5763756fd3d | -6.8955 | -43.6601 | 2026-08-28 18:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 8367b796-828c-3ee7-95c1-194670214483 | -6.8007 | -59.6127 | 2026-08-28 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 92ff57e0-1368-3309-ba6c-29c8caceda15 | -3.6664 | -48.9573 | 2026-08-28 18:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 72a6d28f-0eb8-35f9-99c7-c2c94deaece8 | -6.5865 | -55.4346 | 2026-08-28 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| a1315635-ae5c-3b85-80a9-bb24b71d2d48 | -10.3202 | -49.9782 | 2026-08-28 18:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 58eac33c-2515-3da8-8d9e-cbe334a009d6 | -8.0928 | -45.8354 | 2026-08-28 18:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| cb65593b-a87f-3954-b038-a5059482d448 | -12.9052 | -59.9053 | 2026-08-28 18:50:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| b93713c6-44a1-3e7f-aee7-9548bc6d46a2 | -8.6486 | -62.8565 | 2026-08-28 18:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 70a1ae9f-9e52-36c2-beee-2a033d1c6303 | -8.6672 | -62.8558 | 2026-08-28 18:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 59956a2f-9989-30d1-abe0-6330a0c08104 | -7.0039 | -59.566 | 2026-08-28 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b6d99bb9-568e-3aae-8484-f4261f49ee77 | -6.912 | -45.6496 | 2026-08-28 18:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 2aefd2a6-b791-328a-a844-c56c1ee50b0c | -14.5827 | -53.1744 | 2026-08-28 18:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 7daccfd7-b837-345f-ae87-59bbd34dc3ec | -7.5662 | -61.3049 | 2026-08-28 18:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 185.5 |
| 1344b7e5-8bc7-3496-98ff-1340e18cbe6d | -11.6212 | -54.5947 | 2026-08-28 18:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 143.3 |
| b08a3037-8ae1-305a-a2fe-3f401cd88e89 | -10.9589 | -50.2958 | 2026-08-28 18:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| d4e3068c-4a49-3360-bc1f-0f547258cbd0 | -6.7698 | -55.6844 | 2026-08-28 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 252ab515-209e-36a9-ab65-6b949ad842b7 | -6.1744 | -53.4631 | 2026-08-28 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 7eb04ca2-991a-3017-b344-a20bac1b14d3 | -6.857 | -59.4371 | 2026-08-28 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| c11294d9-f285-34db-9c39-b668c73c90d2 | -14.3997 | -52.5862 | 2026-08-28 18:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 33db06c5-654b-3829-8eaf-319a9c7ef496 | -14.1645 | -52.8269 | 2026-08-28 18:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 87e09cf6-31d7-36dc-8853-1821ebb1a95c | -5.9996 | -57.8249 | 2026-08-28 18:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 5c2453e2-eca2-3b1b-88ac-811e390dc597 | -6.9521 | -58.9506 | 2026-08-28 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 44c2df72-5e93-31f1-a7d9-14ddd24f7247 | -6.9336 | -58.9514 | 2026-08-28 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 182.8 |
| 0e2f573d-1b0e-373d-8f2e-644437da2eb5 | -9.2477 | -57.0697 | 2026-08-28 18:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| a129d7b4-98c8-3791-bd7d-459e647244ed | -6.1473 | -57.78 | 2026-08-28 18:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| b1a0c0da-8524-3983-835a-67a91b481b23 | -9.7874 | -43.5742 | 2026-08-28 18:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| eaa3cb85-94ed-3d46-8d58-33657bf7a3e8 | -8.87 | -66.8935 | 2026-08-28 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 6e781775-c3b5-3e40-a6b8-dee0fd05c5f2 | -6.8357 | -59.9571 | 2026-08-28 18:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 3f1c9e5f-8fe0-3219-9021-007d3f24c920 | -6.8542 | -59.9372 | 2026-08-28 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 8c72ba47-e17b-326b-aaf8-4459639d940d | -10.3898 | -61.1925 | 2026-08-28 18:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 49004856-ecf6-3158-9b67-da4bd2a54d50 | -5.9995 | -57.8444 | 2026-08-28 18:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| e320d1d0-5490-3b49-b789-3a94d30ebae0 | -9.7878 | -43.5506 | 2026-08-28 18:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| dae1b9f0-9966-3340-9685-a4a18764068b | -9.4329 | -51.6926 | 2026-08-28 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 382506c0-a634-34bb-87ee-20fff457e8b7 | -1.31877 | -47.86456 | 2026-08-28 18:51:00 | AQUA_M-T | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d40adc1f-b725-38ea-9513-71b2a0170fd5 | -1.89919 | -47.04299 | 2026-08-28 18:51:00 | AQUA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 813965e4-3663-3159-8104-0406d931a515 | -1.12453 | -54.10243 | 2026-08-28 18:51:00 | AQUA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 83002045-4940-3640-b7ee-7f5fd2f4a97c | -1.36601 | -49.07693 | 2026-08-28 18:51:00 | AQUA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 541e70e6-2973-3b0c-9c1b-f563a5fbda8f | -2.02502 | -48.77658 | 2026-08-28 18:51:00 | AQUA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| e52276ff-33d3-3e40-9eef-6c964d12b1ba | -1.40173 | -50.6999 | 2026-08-28 18:51:00 | AQUA_M-T | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |


[Clique aqui para ver as próximas entradas](README167.md)
