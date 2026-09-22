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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6224233-e4ac-36f6-9d14-6aa74c16ef31 | -3.5844 | -59.068001 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cff21582-a964-38ba-b1b9-715697d04d2f | -3.7261 | -60.585098 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c70071fa-9246-3695-8c8f-3cf2d65c68f1 | -11.3258 | -54.035702 | 2026-09-22 01:19:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a69a2f5b-78d3-3626-8111-84132099831d | -6.706 | -59.9576 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38c2d788-a820-310a-9fdc-75e61693589f | -7.581 | -57.697201 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00393d3a-7da5-315b-80d7-f6ec51ba1188 | -5.9809 | -55.3591 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0cddb1b-9130-3ea1-9977-f18b7624ccce | -4.4156 | -55.239799 | 2026-09-22 01:19:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6477e347-48b7-31bd-a6e5-490e6a7d348e | -3.4304 | -61.322102 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 200b89fe-0115-3681-8b75-6cde61fdb241 | -8.2708 | -55.306099 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 472037aa-8033-385c-9e74-d37e1c811c72 | -6.4234 | -59.9837 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c010c3f-0963-32bb-817a-b717e1252466 | -3.4019 | -59.575199 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1f6e9c6-b629-3bd2-8064-a2c67233e676 | -6.4512 | -59.9702 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 949cadf5-aae3-3ef1-bf64-606a28c8793b | -3.8203 | -59.330898 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0394320-690c-3fdc-b8cd-809ad0b983c7 | -6.6277 | -59.930801 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 178915f4-bccc-31c2-a88f-a8cf71dd54d6 | -11.4229 | -47.342999 | 2026-09-22 01:19:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ec9eaf7-c76c-3a0a-ba16-384406ed015b | -5.2102 | -56.073101 | 2026-09-22 01:19:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff7dbb82-3136-34be-8f49-20e29a222b1c | -6.3559 | -58.290501 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7b1e553d-3d55-3836-b32f-4c5a112bd201 | -8.2551 | -55.283401 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f3b89a5-d228-3957-9f33-b878282db373 | -6.6344 | -59.914501 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17414950-afe8-32ab-ba99-88eb204eb6c3 | -6.4558 | -60.035599 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0da9c495-0c80-3a8e-88d3-b6b7db847ac5 | -3.285 | -57.861198 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2bdc75df-64f4-354d-9577-6474e8c15c68 | -6.4478 | -60.000401 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5bfb50e6-76f6-3fb3-a5e8-c10bb3e1538d | -10.6119 | -53.9907 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fefb5cf4-6dec-3082-af45-099e40992cd4 | -7.4185 | -49.844002 | 2026-09-22 01:19:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61d6547f-732b-37ea-9728-56549feea158 | -6.0784 | -57.625801 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30c1f92b-9fac-3641-8c6f-fe2a8568bebd | -3.9413 | -59.6334 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb4384c6-41b0-3cdc-a15c-90cbfabb5ea2 | 2.0961 | -60.203602 | 2026-09-22 01:19:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e2b2b623-a0ee-35bf-a3a6-c44afcc3fa2e | -6.0621 | -57.867199 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdc60e2c-b072-36a2-a685-b0fb55239912 | -6.7392 | -59.423801 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5c68f59-ccff-333f-8359-6a71e5d00080 | -10.4362 | -50.362099 | 2026-09-22 01:19:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13d2bf52-84b9-3565-aeac-67ea6e7d04c0 | -7.083 | -61.082901 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| acdd7bd4-c663-3b74-a587-9b6943ae1643 | -15.3658 | -57.3326 | 2026-09-22 01:19:00 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bdac7e6a-1143-3de5-8462-3cc36d90ce5e | -3.3785 | -56.9314 | 2026-09-22 01:19:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f869522-ec51-3bc8-95ef-4070ea32584f | -2.5725 | -57.501999 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a1ddc95-a711-3d37-af2a-f427e4d1846e | -6.8679 | -59.8993 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e435667-65a1-327f-8dad-811fb782b46a | -3.2833 | -57.854 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6feae914-a7f3-3a45-8672-3d5d233c2d18 | -6.3452 | -59.9571 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 398b417b-cc6b-36dd-8a83-4557619aea21 | -11.316 | -54.038101 | 2026-09-22 01:19:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06f81c19-e11f-35ca-b41c-6040e6dbe435 | -10.9333 | -58.3307 | 2026-09-22 01:19:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db4266d6-9cad-3876-acc3-53b9f0c8b35b | -8.6246 | -54.623199 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da729dda-7a32-3d2a-8316-1bddcd82fbb0 | -11.1032 | -48.3134 | 2026-09-22 01:19:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be99bbe9-4604-3904-b398-ab32f11176e5 | -5.8172 | -57.745098 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af4ac28b-6c3f-36d7-99a1-a9f538bf3d65 | -6.0932 | -57.689602 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f82f2647-4da5-33b2-8bb8-aa23bb48414e | -3.9815 | -60.034 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8827060c-18eb-3152-af9e-c343e09b29de | -6.1618 | -57.718601 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70453ccb-b436-3109-b0ab-b9421187e237 | -6.1046 | -57.6945 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e4e622f-05c9-388f-88d3-da3a7c1ed455 | -6.098 | -57.621399 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c445ade-1c07-331c-9470-3420309533a3 | -3.3928 | -61.2925 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4de4e24e-feeb-3c64-9a4b-07bd43ce6cc0 | -3.3894 | -59.520699 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fdd6d573-331f-3298-a536-1a6a577f5e51 | -2.8575 | -57.797001 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6a5b7c1-8061-340a-9208-51436011a156 | -3.1117 | -61.415798 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d52c2d1-9e9c-3e7c-a164-fda21401d461 | -3.4141 | -61.295399 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dae558b2-b77c-3259-8e5b-d5eec8c81b7d | -11.0414 | -54.142899 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23fa1a3d-4050-37fb-8c71-36526cee7d94 | -6.3338 | -59.952202 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3d2770a-b79d-36a6-b755-832f06f2d4d0 | -6.0066 | -57.761398 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a37c722-0af1-32b8-b2eb-db56fc8c1120 | -3.1785 | -61.211601 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c879c85-d18f-3206-91e0-691199b2c945 | -3.0692 | -54.425301 | 2026-09-22 01:19:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 748dfbf2-534c-3aa5-8b00-2fc2656ba925 | -6.1063 | -57.7015 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeb7805f-2b8d-3ea4-bc1c-9c30e52188f4 | -6.3126 | -59.9496 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93e6b460-b59f-3c0c-9de6-da042643b3b1 | -9.3043 | -58.919399 | 2026-09-22 01:19:00 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15b0a3f6-1ae3-311e-ad33-cc225b779a46 | -6.6946 | -59.952702 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b32afac0-8105-3f74-aa6c-049dc76bc7e9 | -3.0445 | -61.256401 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6af99312-8a76-368e-a749-b29d5eb469b7 | -3.8208 | -58.885101 | 2026-09-22 01:19:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba90bb1a-aac0-3a01-9f9b-093dc4257ece | -12.1485 | -47.393902 | 2026-09-22 01:19:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da35ac0d-6a03-35a1-9a20-20ae77a43efc | -5.8074 | -57.747398 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5589184-bc1e-31f0-bfeb-7598ab458cb2 | -6.6214 | -59.902699 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43cdb34d-4d55-3080-a238-6c23ed1223ab | -5.7569 | -45.084 | 2026-09-22 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 298.2 |
| d830a325-3220-3e3f-96a1-4c7bbae1e344 | -9.2762 | -46.1627 | 2026-09-22 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 4bf35a3d-16ea-3fd1-bf03-eb7e13942055 | -11.4209 | -47.3603 | 2026-09-22 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 140.7 |
| e42fc689-776d-3c5e-8c20-52ca3e1b4b8f | -9.2383 | -46.1668 | 2026-09-22 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 356.2 |
| d0b323d1-853d-3c58-9481-75fb9c79ec63 | -2.8608 | -57.7994 | 2026-09-22 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 75f04420-94aa-34ec-8beb-a62966b4560d | -5.7571 | -45.0613 | 2026-09-22 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 736ced25-eea1-3de9-96e0-e1071035d7e8 | -6.0365 | -57.8235 | 2026-09-22 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 4193e5c1-6506-37d2-a623-62738214a746 | -11.6793 | -43.4684 | 2026-09-22 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| cab4f4c9-32f8-3924-ae7f-2d518c2e1e94 | -7.5704 | -57.6766 | 2026-09-22 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 2097c652-5082-3ffb-85bc-82508bb3688f | -3.2212 | -53.9422 | 2026-09-22 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 21d390e6-01be-3a05-ba29-10fe01f897e7 | -9.257 | -46.1873 | 2026-09-22 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 1547f09f-e971-3b74-a6f6-71b15a7e95b5 | -3.3867 | -59.5223 | 2026-09-22 01:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| ba0192d0-05b6-3e6e-aa50-43509349e8ca | -7.5888 | -57.6953 | 2026-09-22 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 7776426c-d7a0-385f-9beb-049a80d44756 | -11.4404 | -47.3355 | 2026-09-22 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 3ef89cb1-437c-3168-bce8-f8249caeed87 | -11.44 | -47.3579 | 2026-09-22 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 6e3c9d58-3597-3d21-9ca4-b42263204d0f | -11.4022 | -47.3405 | 2026-09-22 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| f986a8c2-a7a8-329f-8088-0eb2551b0517 | -7.7144 | -61.2419 | 2026-09-22 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| eab23689-a067-3043-82ad-12f175cb2b79 | -11.4113 | -46.7798 | 2026-09-22 01:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| c17200fc-e5e1-382c-a93c-1d921136f0ba | -17.6155 | -46.6607 | 2026-09-22 01:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 114.2 |
| d341a171-3e8e-367a-8b89-ee9826c728c5 | -3.2211 | -53.9623 | 2026-09-22 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 694bcdb5-a17b-3c8f-b7cf-c6dea028036b | -6.1109 | -57.684 | 2026-09-22 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a0804bf7-78c7-31be-ae44-c027c849eb0b | -2.4206 | -58.2712 | 2026-09-22 01:20:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| dca426e5-469c-3497-b121-586179465858 | -8.0298 | -44.8197 | 2026-09-22 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| cd101871-cb53-3a38-b2fe-d7cb6b5ec05f | -11.3257 | -54.0282 | 2026-09-22 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 42de5967-e9bd-3e26-9237-83887016b07f | -6.4485 | -59.9909 | 2026-09-22 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 38ae3c8a-d170-31fc-b4d4-5cf58dfff0aa | -12.7868 | -54.0275 | 2026-09-22 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7c8ca099-fccd-3a47-91cb-a63ab32328f5 | -6.467 | -59.9902 | 2026-09-22 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 0335d37a-43a6-39df-94ce-ad978ef9da9b | -9.2573 | -46.1647 | 2026-09-22 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 341.0 |
| 0ea7bd86-682e-364e-a607-5113889a1e42 | -3.0542 | -54.4081 | 2026-09-22 01:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 6f9ac032-7134-3a4d-bdcf-fc6c97975f72 | -5.7382 | -45.0853 | 2026-09-22 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 151.9 |
| db830e1c-0ab9-35c7-81aa-8a7484c39917 | -12.165 | -47.3948 | 2026-09-22 01:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| de0f0164-832e-36ff-b13b-f1e83dff0859 | -9.2386 | -46.1443 | 2026-09-22 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 253.2 |
| 19c33db9-4cd6-36b7-bf5f-96561459aeb8 | -12.7865 | -54.0482 | 2026-09-22 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| a244684a-a5ef-373a-a925-143424480b75 | -9.2576 | -46.1422 | 2026-09-22 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |


[Clique aqui para ver as próximas entradas](README22.md)
