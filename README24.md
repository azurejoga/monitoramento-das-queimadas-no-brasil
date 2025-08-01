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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5aaeb66d-e3be-396a-a749-d28dc46b966c | -6.82285 | -59.25979 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 179.0 |
| be0a2bbf-d255-3177-86d1-e2c45b1445fa | -7.07699 | -60.05382 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3cf3388-748b-329a-929c-ab4f59423b4b | -7.33035 | -59.61882 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1941d708-390d-36fc-b847-210c45cee6d5 | -6.73804 | -59.18127 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 56f70f02-9846-312b-82b4-5589f1effea7 | -9.01629 | -59.53408 | 2025-08-01 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d76dc84f-7c69-3303-aa6a-11735aaf793e | -6.73337 | -59.1638 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 3ebe9149-db62-39c7-bcee-c0d53aad0108 | -6.64263 | -59.09686 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 386de80f-e879-38a1-8707-1735c24329c3 | -6.62585 | -59.98026 | 2025-08-01 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d45396ac-51c0-3994-8dee-db698ebab21f | -6.83063 | -59.25677 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ba00c412-98da-3fa7-bd23-49be05146f3d | -6.64199 | -59.10101 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9672049-4f3a-375c-bb1a-78580eba8da4 | -6.95974 | -56.37676 | 2025-08-01 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 896dc593-875a-3925-8415-461a8e8aebca | -10.11246 | -58.22688 | 2025-08-01 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67307329-3192-3bc5-a402-79e584b01b54 | -7.32975 | -59.62279 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bd0c299-e39f-3654-a189-82798ba93017 | -6.74413 | -59.16548 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 443d5bfe-3fcd-3173-9153-b5f843638ba7 | -9.31886 | -62.05745 | 2025-08-01 05:31:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d93d92c2-f1ba-3af2-89b8-ac9d978cf7cd | -6.81927 | -59.25925 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.0 |
| c7ca2259-6fb0-3fa4-ab04-f0d7830fda22 | -6.73867 | -59.17718 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| fa3e5985-d35b-3a50-b188-fdad7dbd1dba | -9.46128 | -57.84056 | 2025-08-01 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 28b35902-0526-33b2-8f03-2350b676b994 | -6.73696 | -59.16432 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f9420c53-9911-3edb-a79a-31073db08ac8 | -8.12376 | -65.43826 | 2025-08-01 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31ea656a-090a-3ffb-aaaa-68708639d358 | -9.53394 | -62.06627 | 2025-08-01 05:31:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5b8b745-009a-3e87-b3f4-8d01ba078c6c | -10.32725 | -58.72679 | 2025-08-01 05:31:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09f345a5-ec85-300d-ad71-bef5b62ac5f0 | -6.82347 | -59.25571 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 330560a5-b513-36bb-b966-2e7785ea3160 | -7.90095 | -61.52163 | 2025-08-01 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65c8e1c6-adf9-3795-921d-8520c22491e2 | -6.73759 | -59.16024 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1332af5d-2b2a-36f1-94ae-787fb858fd1b | -6.7393 | -59.17308 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| b77ecb62-2e73-3861-936c-803b83bfe52f | -9.62019 | -63.42633 | 2025-08-01 05:31:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12eaea10-fca3-31ca-bc4e-d923ed6d7251 | -6.8258 | -59.26442 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 179.0 |
| 3fa0f13f-54e8-3079-97e5-8ce30c6db101 | -6.8157 | -59.25869 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.0 |
| cf943a70-6d84-3f96-8328-4fa7f527ce1e | -6.83295 | -59.2655 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| c900e6d7-f022-3d67-a1cc-77d8714fadab | -7.07469 | -60.04561 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f930f854-7fec-343a-9c04-91233176b2e7 | -6.73947 | -59.14793 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73f10e99-ac74-38b1-9751-3680e16bfc22 | -6.81865 | -59.26331 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.0 |
| af7a2f0f-5fc4-39d0-a8fc-c94c397386ca | -6.62468 | -59.98781 | 2025-08-01 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e48157b8-4cb2-3bd3-ac37-7b99a5908bea | -6.82875 | -59.26904 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a4c53b59-5897-3dee-9895-72a33a805ae7 | -9.31552 | -62.05692 | 2025-08-01 05:31:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 490c644f-c496-3be2-9245-98c5e4f82729 | -6.83 | -59.26088 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| f5713cc0-4f32-3e6d-ba8f-6b13638a95f7 | -6.734 | -59.1597 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c811a0f-ad42-3a40-8aed-1473dce244ec | -6.6218 | -59.98354 | 2025-08-01 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f813ceed-f68d-339c-b5b8-fef444935e35 | -6.74602 | -59.15317 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94d42eb4-453f-3748-9bcc-98c1f60ef13f | -9.62352 | -63.42686 | 2025-08-01 05:31:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 496de8f3-d09a-3fd1-a991-cb7df9bc94d8 | -7.07122 | -60.04509 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf627df0-609e-33c1-8a5d-1a50e287001d | -9.45678 | -57.84341 | 2025-08-01 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5cc15c07-6951-342f-9007-b7b4d201dd78 | -6.7496 | -59.15376 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1c2c4f8-d5a8-37fd-b191-c65ae8bbbb85 | -9.45326 | -57.8393 | 2025-08-01 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19b5c0af-ab14-3f22-a8c4-0b486680224d | -7.32267 | -59.62172 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 758c99ae-fde5-38c4-9bfd-d55e3861ca2a | -6.81151 | -59.26217 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0103c41-4aad-3a9a-b1cf-edb129bcbe09 | -6.62355 | -59.97219 | 2025-08-01 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 90c78649-f765-3f9e-a50e-b72b1060f73b | -6.74225 | -59.17775 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44bdcdea-a774-3b9f-b31a-dafbdeea4e4c | -6.83233 | -59.26957 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 2e1747c0-642d-3edb-9e0a-ecf4a3fce819 | -6.73275 | -59.16788 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 733ba5c4-5c9d-39d6-b20e-e922ab676050 | -6.72916 | -59.16736 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 3283dfd5-ca30-3c1d-b0e1-62e19bdeeb75 | -6.64757 | -58.81998 | 2025-08-01 05:31:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f963165e-ffd3-3962-a5a3-c4e47cc1d415 | -6.95918 | -56.38076 | 2025-08-01 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 474c0566-870a-38d9-b7c1-30d2bad67ef3 | -7.08162 | -60.04666 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4d7607a-8575-3429-8a18-af1070730acd | -6.68189 | -58.86415 | 2025-08-01 05:31:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d292dce3-9033-3059-a0b9-be0b6d805914 | -6.6439 | -59.08854 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a03c64b9-6658-39d4-9a53-d5f343d5648f | -6.73446 | -59.18071 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 65f8fcb1-5dab-3d6e-bfee-415f65deb283 | -9.45776 | -57.83644 | 2025-08-01 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 59f2e207-f7cb-3fd0-977d-141d4763cda3 | -6.73821 | -59.15614 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 23730d0c-256d-3ffe-aa1e-4f53ec175885 | -6.62238 | -59.97976 | 2025-08-01 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| dde26c77-b047-363d-973f-b02ffda7a75e | -6.64982 | -59.09795 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 776de9ad-87bf-3a74-a070-8c2fb9796364 | -6.81447 | -59.26679 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 7a2f1d62-0021-3371-a254-5ea4c5622336 | -11.90675 | -55.88694 | 2025-08-01 05:31:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d75527ab-7f96-34f8-9348-551c8046f650 | -18.95144 | -54.3232 | 2025-08-01 05:33:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67086ef1-6559-3645-b09b-0ea006469da8 | -15.08653 | -55.20543 | 2025-08-01 05:33:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e0146d0-8738-3f4a-aabe-3946fe4d9bab | -19.01563 | -54.65761 | 2025-08-01 05:33:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 995bc63e-e76d-3fc3-920e-741b1154445a | -15.08068 | -55.21029 | 2025-08-01 05:33:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77a5cad4-9f15-3da6-b931-4a423ba3d34d | -15.08103 | -55.20739 | 2025-08-01 05:33:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdb86a27-158c-3934-9f1f-57bbd5a5ea37 | -15.40792 | -55.77608 | 2025-08-01 05:33:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 67ed4639-6b18-31f0-91c3-d4aec584ac0b | -15.40722 | -55.7821 | 2025-08-01 05:33:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f48e350-d166-3520-81a8-289ab24643df | -19.02125 | -54.65854 | 2025-08-01 05:33:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c90c1f8-7b6f-3c83-bc56-3e8a70a5a24b | -15.08002 | -55.21587 | 2025-08-01 05:33:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9c5b77b-a50b-3b58-ac04-d841fb10ea51 | -12.27465 | -63.80427 | 2025-08-01 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cd6b98b-517a-347f-9681-bcf8d169d053 | -15.07553 | -55.20928 | 2025-08-01 05:33:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd96b197-ff0b-3f26-b126-4ca57e5c5229 | -15.08035 | -55.21314 | 2025-08-01 05:33:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0075cfa7-d69c-3f95-9104-3d83c6763949 | -12.27577 | -63.7972 | 2025-08-01 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff36dd3a-40ed-387e-aa14-e997d53951df | -15.07519 | -55.21219 | 2025-08-01 05:33:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55ca855e-007f-3986-88f7-354bc01ecb62 | -22.27372 | -55.9636 | 2025-08-01 05:36:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b8365d7-bbb2-3a74-b431-da0ed48d3e13 | -21.45039 | -57.14548 | 2025-08-01 05:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1d63e1a-e771-325d-b5e2-403f876f79c3 | -22.27916 | -55.96393 | 2025-08-01 05:36:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 485426d1-be28-3a3e-b8e8-2e4706636051 | -21.44542 | -57.14491 | 2025-08-01 05:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3317c900-f76d-3893-bb8f-1b655082b487 | -6.7294 | -59.1723 | 2025-08-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 224.3 |
| fae74e8e-a953-3efd-92f4-42b76ca8cf4f | -6.7295 | -59.153 | 2025-08-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| be0359f9-3f35-35be-9d18-47695923d8aa | -8.0321 | -43.1257 | 2025-08-01 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 313cca47-10ef-3802-a765-dff3c79287a5 | -6.7478 | -59.1716 | 2025-08-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 6b3e8de2-3220-3ff8-8661-b89732aac806 | -6.656 | -59.0981 | 2025-08-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 856e7c2a-f398-3653-a1ec-684c5caeff53 | -8.0513 | -43.1001 | 2025-08-01 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 196874c8-fd52-3244-a491-b92925a5c992 | -6.6376 | -59.0988 | 2025-08-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 11fad70a-04d6-3a35-b9cb-ab8ffa7f0703 | -6.748 | -59.1523 | 2025-08-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| eeaa8bf8-14eb-3b1b-b36a-01f8d8f4bb59 | -6.7293 | -59.1916 | 2025-08-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 1a9131c3-d325-351e-9c02-3d7291854c3d | -6.7477 | -59.1909 | 2025-08-01 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 280fab43-d79f-3472-b8df-2f28f8ecac4e | -8.051 | -43.1237 | 2025-08-01 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| cabd0e23-3d5e-3496-b9bf-bc67c3048388 | -8.0324 | -43.1022 | 2025-08-01 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 16d19038-1935-3878-9d4e-31c2336210cc | -6.7295 | -59.153 | 2025-08-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| bdcb9f13-4e11-3835-b884-6ce1f65f6d02 | -8.051 | -43.1237 | 2025-08-01 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| cdc04756-dcbe-3414-9343-b76e08ad597f | -8.0324 | -43.1022 | 2025-08-01 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| d8b9dc16-7999-31a9-8ae8-ec7a4381b6ae | -6.656 | -59.0981 | 2025-08-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| aba932d6-c17f-33cc-bec0-015272b07876 | -6.748 | -59.1523 | 2025-08-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 53d4b431-dce9-3444-a8bd-c0195c1ec999 | -6.7477 | -59.1909 | 2025-08-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |


[Clique aqui para ver as próximas entradas](README25.md)
