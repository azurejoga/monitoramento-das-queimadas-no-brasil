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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e74ebd2-6461-37f0-960d-4e8997c6295e | -8.77317 | -46.91603 | 2026-09-19 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eafd30f-0e83-3a36-be88-cad7fa4f71b4 | -1.49466 | -54.97748 | 2026-09-19 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ac09838-9343-38e0-bfeb-274d50573d68 | -4.3647 | -47.78348 | 2026-09-19 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3724d68d-7eef-353d-8dc0-7292988d3233 | -6.80471 | -43.00855 | 2026-09-19 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aec8d194-d869-3bc7-aac9-6e92cdadbdea | -8.72476 | -44.87354 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57112a0a-a617-39ee-93d1-ceca9af1cb67 | -7.85793 | -45.18012 | 2026-09-19 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8eee061-7f6f-333b-88d7-4848ab8e696f | -4.40685 | -55.50071 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9141a618-3a37-3c81-91e4-0607cb638ac6 | -6.36529 | -58.29178 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32911c71-e924-3e32-a7ef-73e8ab52044a | -7.29006 | -44.52497 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b629ce5-58e1-3f39-8d37-ab9dc8bec4b8 | -7.69576 | -46.12169 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd4b95aa-a970-3eee-8a14-27a1a46b74d3 | -4.14258 | -48.22114 | 2026-09-19 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab3d4610-7925-3a19-b631-be27e50269a5 | -5.85404 | -52.07208 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86bca765-a589-3b79-9a2a-d532dfdf7adb | -6.32702 | -55.28205 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb10daa6-8ca6-3b3b-8100-ec4600a9bebb | -5.86914 | -46.71627 | 2026-09-19 04:38:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68079f2e-7979-35f4-8550-38ae33dda82d | -4.17988 | -49.4054 | 2026-09-19 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00f6ff61-a28c-3432-8521-a93fa72bc6df | -8.12831 | -44.82548 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e646ace-56b3-3dfb-a1a1-0a6318168b0f | -6.98795 | -49.76099 | 2026-09-19 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d36ffff3-6382-3f14-a829-83cadb73f187 | -6.66043 | -50.89841 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f2187ec-af54-34da-a816-42e8acae912c | -7.36119 | -44.46569 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9502ab8-de0a-3552-b754-81eeb978e88e | -6.44804 | -59.98859 | 2026-09-19 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 246b8c63-9a9f-3cfa-92df-fc4ca70fcefc | -7.58266 | -43.44872 | 2026-09-19 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17009861-d01b-3e92-8381-ff46bab7d3a2 | -7.73967 | -47.30622 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c005971-c630-3644-a41e-5b725374276a | -3.23147 | -46.94288 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63737f8f-fc95-325d-96cc-d5309bbf06bc | -8.29352 | -46.84981 | 2026-09-19 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e243f94-b129-3589-ace3-b6c83aa9e61b | -3.45686 | -50.61468 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70d07ad9-6704-3003-912b-4fc90511385d | -2.82908 | -50.46599 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 06d41a6f-0997-3f36-ba34-d8bb9ea940be | -5.83322 | -40.59923 | 2026-09-19 04:38:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 07c93d0e-bb7d-33f4-ba77-f0a065c25d43 | -7.4857 | -46.12453 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d544653-1dc9-339c-9192-b3ace95f1eb7 | -7.64023 | -46.10572 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 986a5867-3def-3746-b690-53c808d235cf | -8.36579 | -47.24854 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f3ad89e-2b12-3fc1-ab2a-08baed3bd2e8 | -6.08907 | -44.30238 | 2026-09-19 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a283680a-a35b-3a88-8ef9-27e7662c4dfe | -6.65231 | -50.92274 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02e34f7a-2f82-3d39-9552-bad5d927ee81 | -3.376 | -52.79586 | 2026-09-19 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff85d338-f084-37e6-8460-0a13b6bcd132 | -7.6902 | -46.11364 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 867a679c-caa9-382f-8c90-04c5c980bddc | -3.36391 | -50.44639 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 077d82e7-b6f2-3fde-9d21-9f1a87d63158 | -3.44466 | -50.66361 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32441e4a-f8ca-3ddc-b828-a5ac4eb4412e | -4.88261 | -56.07221 | 2026-09-19 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a84ec821-6482-3cab-8d35-90a1a08ff4fb | -8.39339 | -45.63875 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdd167ba-34d1-3f85-942c-3efb8655f1a1 | -6.66244 | -50.93466 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60dfa6f5-935e-3d44-a89d-b991ca5d1f5f | -5.1423 | -45.77561 | 2026-09-19 04:38:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a556683-8875-3abf-8b2c-b5e8a6f565bd | -8.82849 | -44.90013 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28d07969-9edf-3428-8789-35eb196cd1b6 | -7.19225 | -50.832 | 2026-09-19 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 804f796e-0f53-3a57-95e9-ad41899b2e0e | -1.9975 | -49.45176 | 2026-09-19 04:38:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53c8c297-5961-377e-945c-26e2a4271a2e | -6.67446 | -50.91108 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38ac4c88-6614-35a3-90dd-d1aeb9f03e0d | -5.14285 | -45.77216 | 2026-09-19 04:38:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abdaafdf-0726-39a6-8b5a-f8477065281e | -8.38694 | -47.20163 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c820f9c-a868-33fc-a765-9a2e88eb25a6 | -2.1451 | -50.89933 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83ae4eaf-1938-3852-b4c1-ffbe87811f28 | -5.87951 | -44.97862 | 2026-09-19 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5154b0e2-5cc2-3ab1-971f-f3b653bb1e17 | -8.37583 | -47.20702 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 741d7d20-cf15-34cf-b73e-bd402bb22ecb | -6.66436 | -50.89901 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63c910b6-84f3-38c1-9b1e-acd6c3441e5a | -8.87988 | -45.94036 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69262b72-be1d-39a4-b087-4e48fa17e729 | -3.51742 | -50.79975 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e83314f9-d62a-3a88-a7b0-1c276d3db57a | -6.44219 | -59.98088 | 2026-09-19 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5dfcf6e6-1e09-3203-9258-a67490e0fc96 | -4.21865 | -56.33344 | 2026-09-19 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a49c5fa-99df-33be-a9f1-a19286f86d24 | -5.94299 | -44.79408 | 2026-09-19 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7639a69-873d-3e01-840a-19b8e8685d14 | -7.48625 | -46.12104 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebce3478-2923-3014-9671-b3d034858fd5 | -6.37068 | -58.29831 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a29f6ba-1177-32e1-98e7-4a588a3a80a3 | -6.90478 | -41.71157 | 2026-09-19 04:38:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bae27c20-92d9-326e-a4e1-8d09bd2b0713 | -3.04276 | -46.92413 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7785477-0d66-31d9-89ac-80c21a0c354a | -4.38208 | -55.25811 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bc1496dd-0d12-3b38-96b2-86a25579cf90 | -4.5042 | -54.9665 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb42e28b-0ed9-36e5-a4d5-6d179df84b5f | -7.36407 | -44.47001 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f200619f-f93a-3cd7-b5ce-0faf1e549c35 | -8.76973 | -44.22515 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fe27d10-7813-3b69-b280-82e300a11b09 | -5.76807 | -57.45492 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 066229a5-9ae2-3f51-970f-1506feaa9b8a | -5.19222 | -49.33336 | 2026-09-19 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 421b80c8-1acd-3d43-8cf8-670f62149016 | -2.82099 | -50.46469 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d7d18b50-8281-3454-a78d-ae6879064de2 | -5.80984 | -49.08924 | 2026-09-19 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bf1eb89-4f6c-3c17-bbe9-5a7fdcac8b79 | -6.02206 | -51.76498 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5312e539-ce9f-3ed7-bd21-01687ebcf479 | -4.56077 | -42.97719 | 2026-09-19 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de0f1f2b-6b5a-3f8e-aace-dfb8c540a2a8 | -5.22265 | -49.3078 | 2026-09-19 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2a99ae9-f471-33b7-9bfd-cf157fc7db71 | -3.73607 | -54.64863 | 2026-09-19 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f1b06f9-a12e-3243-a8fe-ee0ce9db9282 | -5.41175 | -42.94126 | 2026-09-19 04:38:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f722c077-5051-3a49-b282-98f0dba01cf3 | -3.47204 | -54.69744 | 2026-09-19 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8578a254-1815-3546-8709-a3eb3937e5a1 | -4.71459 | -55.68966 | 2026-09-19 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b58ccce-b8e0-3728-b0d8-616284d287f0 | -5.40813 | -42.94071 | 2026-09-19 04:38:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eed4be96-efc8-3dc9-94e9-0846a0546ac6 | -7.57894 | -44.90952 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdecafe6-3863-3ef7-841e-bd9b68458ba5 | -7.09249 | -42.08721 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5a763bb9-3f8e-3263-81ce-b33a441ea6f5 | -6.36551 | -58.28439 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47dbe70f-353f-30cd-b3db-4e7ceec34bc4 | -3.85173 | -50.01252 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0966cdd0-b8a5-361c-bfa9-090a22bb8c43 | -8.39674 | -45.63932 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0fd188a3-6327-3116-bf59-37c792328070 | -4.28404 | -48.59062 | 2026-09-19 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78da93e0-780e-3a5b-9c4d-bac627441363 | -6.23073 | -44.69344 | 2026-09-19 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 438bf626-3972-38ad-aa34-82e54a0e5312 | -5.86265 | -51.9412 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 197bd462-e3e2-301c-9dca-6537e8615503 | -7.76096 | -46.73256 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b8b24cb-de07-3120-b639-ed1f904f04da | -7.57312 | -46.74504 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c7504a0-db91-3c61-a6f5-572834a3c379 | -7.32215 | -45.32933 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acae9c93-f5f0-314d-a305-2ace95df6ab3 | -3.52211 | -50.79679 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e67ba0f6-4098-391a-92f0-846734d2cd2b | -3.03204 | -48.41484 | 2026-09-19 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ea19202b-feaf-39d9-a5dd-4f75e30e9b93 | -8.37133 | -47.25662 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6896af30-b990-390f-8adc-643c83d89f9d | -3.37381 | -50.46128 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca8c0cfc-14eb-3272-975c-9fd0d249d44b | -7.57552 | -44.90902 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f95d3ff4-4f4b-332a-9369-e1616c31fa80 | -2.0332 | -48.77895 | 2026-09-19 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7db2b3c4-e286-3e31-ac8e-2892ec185a2e | -8.4705 | -44.5096 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e0f56c3-5a78-35f2-a32f-9520f91a64c2 | -8.45435 | -47.66086 | 2026-09-19 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4bbe79a-aad9-3ff4-81a7-7d3e74312c94 | -3.22976 | -46.95364 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 450e6676-79b4-38f9-b95f-dbeb41084c54 | -7.78166 | -44.88391 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22e416ef-3258-3b6e-98e5-7f19ce29badf | -7.83624 | -44.9146 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8bc1978e-9ed6-3f3f-84ab-92a9f5a54202 | -7.08473 | -42.08601 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e7acdcb8-8201-3b53-8740-ab3756497a88 | -7.37632 | -44.73163 | 2026-09-19 04:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a3ee924-91cc-3641-923c-38c5810a4801 | -2.90352 | -57.8177 | 2026-09-19 04:38:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README47.md)
