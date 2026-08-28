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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ee97b06-fffd-3a88-ba7d-254240ab5a1b | -12.4494 | -43.415 | 2026-08-28 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 4d5a60aa-b51a-3782-8feb-519edb898596 | -13.4552 | -54.0174 | 2026-08-28 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 5ad04354-b3a8-3e9e-90a7-3e70591e14e3 | -12.7797 | -44.2576 | 2026-08-28 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 41d37fec-59a5-3928-86e5-03141696bda8 | -6.7513 | -55.6853 | 2026-08-28 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 5bb40741-b29a-3b70-9e08-c72e698144c1 | -7.3324 | -46.6656 | 2026-08-28 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 2a0f5fb4-7fe9-3bf4-a640-02fa8391b7f3 | -11.2693 | -54.0129 | 2026-08-28 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 7a71d590-a345-3939-95f6-203a14285ed1 | -8.87 | -66.8935 | 2026-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f300621c-1a11-3271-9826-b22363d26b50 | -8.87 | -66.9121 | 2026-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| b3dadc83-6f28-371d-ba2e-ffd2c3c2a7b2 | -6.1472 | -57.7995 | 2026-08-28 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 34043e61-79cd-31bb-b389-1669ec0a04cf | -4.8398 | -45.37 | 2026-08-28 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| be484c0b-1f0c-37e8-a796-a7d113ee5600 | -5.5046 | -43.9815 | 2026-08-28 00:00:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| ecb09121-f807-330c-b479-8a2bfb8e69f9 | -10.3895 | -61.231 | 2026-08-28 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e9ac6b65-985a-3030-9ad4-b6a3d8ae1b2c | -2.7304 | -47.0424 | 2026-08-28 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a2043890-b45d-3114-8a4e-f5b3b497f63b | -12.7603 | -44.2608 | 2026-08-28 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 6cc765d3-993f-31c1-b404-584b0c43e8ac | -10.7596 | -54.0384 | 2026-08-28 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 91fe4e80-68bc-3db4-8fea-e5accccd466b | -10.5168 | -64.4997 | 2026-08-28 00:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e75a0c3f-10e2-3669-b65d-8b6be5d5c4bb | -4.8395 | -45.4151 | 2026-08-28 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| bfd24721-6b80-3602-acb3-906093d99edd | -20.3458 | -47.5939 | 2026-08-28 00:00:00 | GOES-19 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 80.6 |
| f798df0c-687a-3e69-8763-d1d639d7817b | -8.9873 | -65.4379 | 2026-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c0c4c71d-9225-31cb-81ef-360a2bce86f4 | -4.8397 | -45.3926 | 2026-08-28 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 265.5 |
| 239db2c4-13b0-3382-a924-3cc550670914 | -10.4981 | -64.5005 | 2026-08-28 00:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| b3da076d-55c7-3503-b296-5f23ec9916ba | -11.7354 | -54.5431 | 2026-08-28 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 2d549eac-b356-36d1-a517-9e82598f3094 | -11.2314 | -54.0164 | 2026-08-28 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 6417d342-d108-3872-98aa-9af1160cb19d | -12.4994 | -43.8095 | 2026-08-28 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 27c33ab0-af99-3e8a-92a4-befe191b8533 | -6.1656 | -57.7988 | 2026-08-28 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 154.9 |
| f72c571c-e48e-3ae0-b5a7-54ab00319518 | -4.8582 | -45.414 | 2026-08-28 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 188.8 |
| ea9aae53-38ea-3b58-b41e-e44b94a9e64b | -12.5187 | -43.8063 | 2026-08-28 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| b1039e96-0353-3abd-8029-3f07e1791381 | -7.4007 | -72.6259 | 2026-08-28 00:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ce91bfd3-f593-393d-8b62-6d48379e4731 | -12.43 | -43.4182 | 2026-08-28 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 135c7ba0-2967-31d7-9341-e538c96d1388 | -15.5403 | -41.9175 | 2026-08-28 00:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.0 |
| 4e014fc4-d149-38f5-bdf2-2b5265bb3629 | -11.7357 | -54.5227 | 2026-08-28 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| e34bf5b9-8949-37a7-94cf-906d8b55e479 | -11.7165 | -54.5449 | 2026-08-28 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 036ccca6-9c8f-3fbd-99e2-c22cf9a19af3 | -7.8828 | -46.1028 | 2026-08-28 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 3314ed11-e9b7-3c7b-a3b2-591b61488507 | -11.2317 | -53.9958 | 2026-08-28 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 020c9139-07eb-3388-95f0-24935177bfc3 | -4.8583 | -45.3915 | 2026-08-28 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 290.2 |
| 1026f61b-88cd-3d8b-8eed-01fe3f73c4af | -13.5991 | -45.772 | 2026-08-28 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| fade8317-24ff-34ed-ac45-f1a5374ffa07 | -12.4305 | -43.3944 | 2026-08-28 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| d12ce0fd-b53a-33f6-973d-421af68ca80b | -4.8585 | -45.3689 | 2026-08-28 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| a623a8f0-8a5e-3c76-9cf4-aed1088add4e | -6.1657 | -57.7793 | 2026-08-28 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| c769d6bb-5c57-3947-91db-818cd698000f | -11.7357 | -54.5227 | 2026-08-28 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| c015839d-827b-3dc3-83a7-9113aa4fe19e | -12.7797 | -44.2576 | 2026-08-28 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| e9ef358f-8552-3cc4-9eff-c2826b130c82 | -4.8398 | -45.37 | 2026-08-28 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| e6e9c75d-d0a9-35fa-97e8-f2aa6c14f91f | -6.7513 | -55.6853 | 2026-08-28 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 9aa21f59-db2e-3e44-a2bb-47ab904ad692 | -12.43 | -43.4182 | 2026-08-28 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 376.6 |
| 84232295-015c-3ffd-a9b5-2e0d9aa20f9e | -10.4981 | -64.5005 | 2026-08-28 00:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 02e8d59c-5508-3c86-9509-0498dd92c116 | -11.6396 | -50.4553 | 2026-08-28 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 0171a010-b678-3c73-b1f7-4fb2e0cc7cbe | -12.5187 | -43.8063 | 2026-08-28 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 936f5272-7ee3-302b-94a5-9838f149ba7a | -11.6392 | -50.4768 | 2026-08-28 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| dc0bca83-dc38-31fc-b680-5a922db7d708 | -12.4494 | -43.415 | 2026-08-28 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3e791058-2043-3c72-aa72-e7b7bbfe29ff | -12.4994 | -43.8095 | 2026-08-28 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 9a4b2e17-2dbe-3e5d-969b-bcd96e4e6ffb | -11.6586 | -50.4532 | 2026-08-28 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 837864d4-e8dd-3e60-b40d-6c54eeb4a985 | -11.7167 | -54.5244 | 2026-08-28 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| cc1e3313-ca3b-3c40-a8c2-7c09c193a3b3 | -11.2314 | -54.0164 | 2026-08-28 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 7fbbaea2-a855-322f-b8e3-7e37a48252cd | -15.5403 | -41.9175 | 2026-08-28 00:10:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.6 |
| 67c231cb-c763-38b8-a7cb-85e2465e454b | -6.1657 | -57.7793 | 2026-08-28 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 307a31c1-ea71-3416-ac8c-ed645b3494ea | -4.8397 | -45.3926 | 2026-08-28 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 179.3 |
| aaa6a035-5bae-3fd6-b423-4c783c172af1 | -11.6583 | -50.4746 | 2026-08-28 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 8c0305cd-b9c7-3f04-86cf-3667948d72cc | -11.7165 | -54.5449 | 2026-08-28 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 7b429e26-cf86-3575-a75f-c6018ceefc14 | -12.7603 | -44.2608 | 2026-08-28 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| a7055000-eb6e-3b3c-9eaa-70d74c7622f2 | -6.1472 | -57.7995 | 2026-08-28 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| e8404327-6f2e-3033-a2c1-6eca3fb296b9 | -7.5846 | -61.3232 | 2026-08-28 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 2a0b508d-b9d1-3622-8224-6ecdb45644c4 | -7.6029 | -61.3606 | 2026-08-28 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ecb35cf9-3220-3ceb-9c89-983c7149f39d | -4.8395 | -45.4151 | 2026-08-28 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1b3a66d2-0fc0-3bdc-bf39-a1168ff0d756 | -11.2317 | -53.9958 | 2026-08-28 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| c975383d-775a-3d8c-9a98-5595c7b3e605 | -20.3458 | -47.5939 | 2026-08-28 00:10:00 | GOES-19 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 52352373-e9ac-3bae-b12b-a2f09766489d | -13.5991 | -45.772 | 2026-08-28 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| cd81e009-11ba-35fa-8e92-8a32f8ddfba3 | -4.8583 | -45.3915 | 2026-08-28 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 24cf1fe2-b21f-30a9-a6ed-25d8825d42e1 | -12.4305 | -43.3944 | 2026-08-28 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 296.2 |
| f4737051-4ae3-3cc7-8318-5f8513571162 | -10.3894 | -61.2502 | 2026-08-28 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| cdd69cb8-dce2-3103-95e8-ae73de9516e3 | -2.7304 | -47.0424 | 2026-08-28 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a2936e41-85aa-3b9c-b350-a27f27cde2ff | -4.8582 | -45.414 | 2026-08-28 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 233c7913-4c6e-39ca-982b-07c4f8d3c090 | -7.6214 | -61.3408 | 2026-08-28 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 3735fae3-facd-3a76-8ce2-177e708747b2 | -11.7354 | -54.5431 | 2026-08-28 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e3a73856-92d2-3842-8fa9-5e0455908ddd | -7.4007 | -72.6259 | 2026-08-28 00:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 611bc897-abcc-320c-97c7-2ff98eb00e7d | -8.87 | -66.9121 | 2026-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f5be25df-0865-3e11-b71a-2d19bbea7bc2 | -8.9873 | -65.4379 | 2026-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 6ba9cac0-3d54-3f60-9164-a57ea9f3c5a2 | -7.603 | -61.3415 | 2026-08-28 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 9e976b63-42d6-3de6-ac1f-a271fd1ae38a | -10.7596 | -54.0384 | 2026-08-28 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| bd747383-a336-3ad0-8751-b2d8687ee2c6 | -10.3895 | -61.231 | 2026-08-28 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 465df494-3972-3d55-b738-40e7097291e5 | -6.1656 | -57.7988 | 2026-08-28 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 3b53a3b9-607e-33dc-99ab-88937ef317f5 | -7.3324 | -46.6656 | 2026-08-28 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 69181af6-d3b4-3bad-a945-c8927a17282f | -12.45 | -43.42 | 2026-08-28 00:15:00 | MSG-03 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 383e41c9-1997-3667-8540-4fc21a3453d1 | -12.77 | -44.29 | 2026-08-28 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85f6191a-9743-35ea-b88d-4bd6e52a9d5b | -7.28 | -45.88 | 2026-08-28 00:15:00 | MSG-03 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8036c85-2190-3a5d-b7cb-1178998e259c | -7.25 | -45.83 | 2026-08-28 00:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6dc8041-6f47-3c21-b129-2cd5caba60b6 | -7.28 | -45.84 | 2026-08-28 00:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bcb34e65-8668-3096-92f6-cb02f20454f1 | -7.25 | -45.93 | 2026-08-28 00:15:00 | MSG-03 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b645262-a99a-3ac4-b450-d42a855fdde2 | -7.25 | -45.88 | 2026-08-28 00:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d67e0c1-9d7e-379f-b668-f29c64cfc495 | -4.84 | -45.4 | 2026-08-28 00:15:00 | MSG-03 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1286a09f-24d2-3e0c-bd01-9c2221a49273 | -4.87 | -45.41 | 2026-08-28 00:15:00 | MSG-03 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c21c7051-a233-37cb-907d-f65883f0a3ba | -20.3458 | -47.5939 | 2026-08-28 00:20:00 | GOES-19 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c99ede99-a8d9-37eb-a68c-5e66924fa659 | -4.8583 | -45.3915 | 2026-08-28 00:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 248.6 |
| 40706bf9-c11f-39b0-9e9b-474f7b6f43bd | -15.5403 | -41.9175 | 2026-08-28 00:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.4 |
| 32381437-6133-3bf8-a848-5db91ae4167f | -11.7357 | -54.5227 | 2026-08-28 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ce330328-1b41-35d4-acaa-0792af16d326 | -12.4494 | -43.415 | 2026-08-28 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 0b85cc76-5da1-3612-9f1c-ad7a3ccad4e8 | -10.3895 | -61.231 | 2026-08-28 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3b8808f9-851e-320b-a678-f12bf6bbfdd6 | -6.1657 | -57.7793 | 2026-08-28 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 91740951-e1a8-3836-ad9f-4e9b9268442b | -10.4981 | -64.5005 | 2026-08-28 00:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 58f09435-aa07-33c8-8645-68d282e0a867 | -12.7603 | -44.2608 | 2026-08-28 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 87d79a32-74d6-364b-8ca8-e79388b575e4 | -10.3894 | -61.2502 | 2026-08-28 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |


[Clique aqui para ver as próximas entradas](README2.md)
