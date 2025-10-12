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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d77dee81-d985-367a-9281-31d5c7f140db | -7.65357 | -42.5754 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a72167e0-6b9b-3f1b-ad5d-1e2620dac190 | -3.45369 | -50.09408 | 2025-10-12 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dc9c1ec-d91e-3dce-ad97-9a72c52779cf | -6.84503 | -47.34224 | 2025-10-12 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f64f4b71-409f-307f-8a06-dfc99e4a08de | -8.47921 | -46.23146 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3b23448-a502-3dc7-9378-535fc8cfa214 | -5.7072 | -42.79432 | 2025-10-12 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2bc15a97-16bb-38b4-8eb0-40ea7052e52b | -3.53544 | -48.92535 | 2025-10-12 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9e980bd9-0555-32b4-bbc9-ba0c457b716c | -7.40267 | -46.94585 | 2025-10-12 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d213fd11-be06-3f9d-aa12-84e3d2ce2482 | -7.74561 | -42.40612 | 2025-10-12 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0d0bdf61-4904-3e54-9f67-f1526dc9fa79 | -4.27441 | -46.93652 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 446da373-f121-3011-9630-9d2c0ef7c585 | -6.56566 | -39.56251 | 2025-10-12 04:42:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5987719a-3ce0-39a6-8c9d-4ee69feb7420 | -4.5791 | -45.69436 | 2025-10-12 04:42:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 70ac0992-38b8-3790-bfb0-c4c831b79765 | -7.85501 | -46.89217 | 2025-10-12 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef2a39c2-b7d6-38ff-a716-d77969a51802 | -6.46533 | -44.63649 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c336419-30a4-3e1e-bcbb-0b1b556a092f | -3.97148 | -42.84874 | 2025-10-12 04:42:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 1140d3ea-022c-3fb5-8ed4-690347466de0 | -7.80529 | -42.43046 | 2025-10-12 04:42:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1f9a6978-68dc-3869-a6db-1a8b01d63805 | -4.27845 | -46.93328 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 411d8bf0-0dbf-3f3e-a9ea-11a1a07553f3 | -7.89073 | -47.06802 | 2025-10-12 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40ec6d9c-d40c-37b7-9739-44231b22fdea | -8.8303 | -46.04125 | 2025-10-12 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69f14423-27eb-3296-b4c5-34cdb9db0e07 | -9.40011 | -42.67173 | 2025-10-12 04:42:00 | NPP-375D | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e36b6bf8-b9c6-3e15-bd03-eb70793c7876 | -7.52586 | -44.29077 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df3d6753-445d-30fc-8339-ec1c2d328d16 | -7.67848 | -42.56868 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eb03bfc4-31d3-3439-bea3-13f76da419c4 | -3.53321 | -48.91792 | 2025-10-12 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cafc4ef-4c72-305d-acec-818834eb8770 | -8.33151 | -46.24359 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4db4de03-bbd0-336c-9e6f-b81bdb0e43ee | -4.47223 | -44.92038 | 2025-10-12 04:42:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 859b5d33-6695-3e61-8a14-75a996bf93d5 | -5.05591 | -43.27204 | 2025-10-12 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21a41cd3-4af2-3393-bc7b-93d058d5d3d0 | -5.71168 | -42.79503 | 2025-10-12 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2ed11a1-eace-3708-833d-ed2ac8484746 | -7.659 | -42.57089 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c9a6082-7211-330c-9259-f256b442d0fe | -7.05284 | -46.73095 | 2025-10-12 04:42:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 088187b6-c289-31a1-8141-33195e379d7a | -7.85975 | -44.11792 | 2025-10-12 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c9ada93-d65d-378c-96f0-95b0b6050b5f | -3.68287 | -49.19281 | 2025-10-12 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c10ddffb-3097-3d32-9561-781237714cd6 | -3.60916 | -42.75409 | 2025-10-12 04:42:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da1f7d7b-52bf-3bcb-8e19-98b181576af1 | -6.75763 | -44.64748 | 2025-10-12 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 36261ea6-9148-3ef7-a8ab-8466f1b2e72c | -7.14507 | -42.52343 | 2025-10-12 04:42:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b7924d1e-4caa-39df-a0ce-a30dbbb66b49 | -5.66851 | -42.67953 | 2025-10-12 04:42:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 59114721-d782-3d62-b96b-5887ecd4be73 | -6.28002 | -44.4109 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a94a3db7-5a9a-3a80-a5d7-caa37283b0ae | -6.27872 | -43.90974 | 2025-10-12 04:42:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 86a6dc3b-4471-3862-b80b-f413d11e030d | -4.82342 | -43.1384 | 2025-10-12 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 610e53f8-fd18-3aac-b649-d302b0bd8149 | -3.43509 | -49.83696 | 2025-10-12 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3380c0ac-beb1-3d5e-84ca-015b29edb08e | -3.8784 | -42.51106 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 26f0a6c1-4692-339a-9d16-32902fcfe5e0 | -3.71622 | -52.08601 | 2025-10-12 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 873bf252-21fa-3158-b660-21c369945213 | -5.32317 | -42.87747 | 2025-10-12 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 692bc7e5-af94-3ab0-b585-3a289aeed761 | -5.91587 | -45.42576 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 382b6664-8216-34ad-bcc2-d91c2491cb52 | -5.67304 | -42.68018 | 2025-10-12 04:42:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 074010e9-69ee-3233-8c97-c960f00cc105 | -6.84851 | -47.34279 | 2025-10-12 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2192db3-c100-3579-9fad-42f05af38b8e | -7.51352 | -44.60529 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9984adc1-1569-34f5-8b4f-aef9527a2582 | -6.72762 | -43.59473 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f3cc0db6-a26f-3925-87e6-9244408181e9 | -4.38861 | -47.64529 | 2025-10-12 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db334ef7-7586-3a3e-8921-acb6e5115587 | -5.34125 | -43.43515 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f97e1a3-0d59-391e-b9a2-f6433ce38bde | -5.97389 | -44.38051 | 2025-10-12 04:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 536d3167-075a-35d8-afe1-d7a7dfc371e5 | -6.66444 | -45.93083 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab175085-94aa-3b30-9b05-6152fd0dce64 | -3.86886 | -42.51405 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9ac5bfde-46b5-3358-bb51-8ee2e992b5fd | -4.41661 | -43.46905 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef9558f4-6461-3f59-9175-d525cbd9625f | -8.02347 | -44.47525 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df5209f1-1cdd-3a03-b572-ae178e8d24c7 | -3.60551 | -51.34255 | 2025-10-12 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ea44a6a-95d5-31c7-834a-db272203a553 | -2.44332 | -49.37247 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1c8c6732-ca99-3860-8718-da6bfde38622 | -6.73127 | -42.08028 | 2025-10-12 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f636600d-b29c-34be-8f6a-7a38425b6809 | -6.65746 | -43.73005 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2baf01da-32b8-3d17-8e78-63d0dd4542ea | -4.57543 | -45.69379 | 2025-10-12 04:42:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e444c687-dfe6-349f-905c-790307ecdc14 | -7.18764 | -43.31232 | 2025-10-12 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2b1e7e04-cd13-312c-a63b-c4518e4d2f04 | -3.22349 | -48.92904 | 2025-10-12 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1d0351c-c0f1-3f9a-8905-1f66e5e18d41 | -8.02607 | -44.4571 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 826a1beb-3475-3eae-87f3-b11bc17172de | -7.21353 | -39.90611 | 2025-10-12 04:42:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 06a81f3c-b3d1-37d4-bdec-3a520e147f9f | -3.43844 | -49.83748 | 2025-10-12 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e3605ea-fa1f-3eff-b8a3-2012259f671c | -6.57797 | -45.97583 | 2025-10-12 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5649c0eb-eee3-3855-bc9e-ffab01fdfa22 | -8.48078 | -46.19562 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 551c9837-3ee8-30db-874c-bb261688c46c | -3.40964 | -52.88181 | 2025-10-12 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e66957a-3283-3ddb-9357-a6ba9767d100 | -7.40726 | -42.96854 | 2025-10-12 04:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2832bfbd-0d01-3397-b1b5-cc62bf517f83 | -8.47574 | -46.20369 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b541bec5-bbe0-3595-8e20-ff03551ea432 | -5.91966 | -45.42634 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 32d4cae7-1bb0-3763-a043-ca57b0a31f06 | -7.73299 | -46.66085 | 2025-10-12 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14b1bad7-ebeb-3e60-b8f7-8773f1de5efa | -5.91649 | -45.42837 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0cd9c854-110f-3653-ab98-9278db2c51e6 | -8.47508 | -46.20807 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 55422764-5e64-3d3d-8286-7cc6526d2e16 | -7.48896 | -42.76 | 2025-10-12 04:42:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ffe507fd-745a-3f4c-94f7-cea017bed343 | -4.41015 | -43.11491 | 2025-10-12 04:42:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e1173f2-993a-30ba-b24f-a5dc8ff05017 | -3.58186 | -51.24015 | 2025-10-12 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e677e286-1aa4-3337-b29d-497c68e92412 | -3.87057 | -42.51238 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fb934095-cd17-3eca-b78c-7e89fe8db9b9 | -5.60465 | -42.57303 | 2025-10-12 04:42:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6fe7b4b3-c189-31e2-8004-4f7433107fa0 | -6.73082 | -42.08242 | 2025-10-12 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 38611358-f878-343a-ac6e-844918736067 | -7.85621 | -44.5244 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24f65590-5351-3cd6-b3b2-5c65ab58b5a0 | -7.01577 | -42.09963 | 2025-10-12 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 139aa194-6341-3963-bc35-db8fb53d34d0 | -5.429 | -41.37204 | 2025-10-12 04:42:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8c6f8484-1b37-32fd-b2eb-9d90a20b8bba | -6.04778 | -41.8909 | 2025-10-12 04:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 05029e3a-ba42-31e2-a211-2206db25f1b6 | -4.43553 | -46.3557 | 2025-10-12 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d856633-e328-3de3-ad78-63236b01e1c5 | -7.83631 | -44.8013 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c2388f7-78b4-353d-977a-659a1595ac4c | -8.83475 | -46.0373 | 2025-10-12 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7888b573-2baf-3f70-8c69-cfc922bc496c | -5.0927 | -45.09565 | 2025-10-12 04:42:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7d8624f-dfed-3e27-9c8e-557867b9c694 | -4.40077 | -43.51767 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ec2bd59-1e8b-339d-b787-60f93420ccf7 | -6.76939 | -42.83461 | 2025-10-12 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 61ad1f70-4426-3a57-89d9-0f7c5882896c | -4.42445 | -43.47412 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b473972a-93a0-3794-beeb-4025e0fe62a4 | -5.9134 | -45.42323 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5f80fccc-575a-3ace-8d06-39191ba42c1f | -2.45222 | -49.35954 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 980784fe-8f42-360c-985c-7ecef3e8f1b8 | -7.02057 | -42.10043 | 2025-10-12 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 60d98c97-f187-3c20-86e2-0217905cbf1b | -3.6017 | -43.84721 | 2025-10-12 04:42:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6c8373d-c3ac-3867-a975-724c6d74def4 | -7.80672 | -42.42031 | 2025-10-12 04:42:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 337cceea-9c02-31b2-aadf-e7b3a65f25e7 | -5.48272 | -43.07444 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b228b5c0-e508-389f-9c1b-2eb0bc10c670 | -4.3724 | -44.58312 | 2025-10-12 04:42:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03fada22-542a-3b7a-9d22-debd5cff05ba | -3.8757 | -42.50868 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ba35afe8-184b-3b80-806c-2fb59dd8f23f | -7.14715 | -42.50883 | 2025-10-12 04:42:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 82b94599-18b6-3b97-afc2-6c6548794834 | -3.44413 | -52.64264 | 2025-10-12 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 720f3ece-384b-3f5d-976e-ee579cf0bf2e | -3.50918 | -45.84313 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README28.md)
