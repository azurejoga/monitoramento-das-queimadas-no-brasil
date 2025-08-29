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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 707a69a4-8b2d-35fd-bffc-a9fe8003c212 | -6.73003 | -43.5753 | 2025-08-29 05:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d88ccff5-33e0-3d9b-965d-039c1b3a5a49 | -7.04424 | -44.37307 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e431809-5261-3a79-aef6-11832a01d6ca | -9.69318 | -47.06506 | 2025-08-29 05:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd8090b4-c8aa-369b-8608-b3a3d4bc38d0 | -6.43749 | -44.57301 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6daeebb-b227-3a73-94d2-caaf426e3f2f | -3.75772 | -54.81679 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91e9a846-8326-3de4-9b84-5d727a7ecf9f | -5.86857 | -42.95895 | 2025-08-29 05:06:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e603c693-e9fb-35cb-ae0a-2a3df7cde0a8 | -3.52831 | -52.86665 | 2025-08-29 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fc7506b-8b35-3028-ae04-fc787569bbaf | -7.05321 | -44.35383 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5668fc0-7d3b-39ab-98d2-7399261c4ae6 | -9.04452 | -47.0118 | 2025-08-29 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8bf0d64-89f6-3a7f-84d2-95f2464af3d6 | -7.56381 | -47.50391 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93ee4152-d2bb-3a9b-a85b-3a692f160080 | -7.39191 | -45.93621 | 2025-08-29 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 418cd388-723e-3c05-a51e-c44633e87c95 | -7.39528 | -45.93439 | 2025-08-29 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a511cb4b-3abf-35b3-a242-96191ea014c1 | -7.04919 | -44.38338 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64f70950-524f-3dc7-b656-bc910483473a | -7.05278 | -44.38409 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85dac2a3-6312-3c61-9b4a-21654c042839 | -8.05368 | -49.97195 | 2025-08-29 05:06:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d8db6f7-b492-3eba-af89-a7b3e2365ea1 | -7.74031 | -50.27463 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ddae2c9f-4756-3ce4-a66e-989d1945012b | -4.10253 | -48.19885 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66cdd3ad-5c2f-3914-a5dd-5e7fd98245e0 | -8.70098 | -50.37864 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a537655-bc30-3019-92f4-59a6e080abe0 | -9.42706 | -47.64522 | 2025-08-29 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a26773f1-9c97-3a29-9886-6323bb482648 | -6.98185 | -59.33224 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0f004f5-ce01-31e4-bbf8-3511a02b7d2c | -8.56093 | -51.31243 | 2025-08-29 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| caae06b3-5c55-33c4-aff6-779a7a702ace | -5.33106 | -51.32803 | 2025-08-29 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4fff4d72-910d-3595-ad04-8e3a9121de6b | -3.92327 | -47.69188 | 2025-08-29 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f96484dd-5dcd-3ba8-9469-de47ed6149ee | -6.97816 | -59.33163 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86442a40-1ea9-3c36-8014-a186cf567a64 | -6.43142 | -44.57187 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37a87efa-9cfa-3f5b-9c7a-957d37c03cd8 | -6.70743 | -49.47486 | 2025-08-29 05:06:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd164d38-2d71-3e61-ac8c-68520692ccc3 | -7.16013 | -44.1515 | 2025-08-29 05:06:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1db1acf1-b8d6-3a68-8e5c-818713aa9ae8 | -6.70424 | -49.46565 | 2025-08-29 05:06:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b33e8564-3472-3423-b6d8-854dc1d17ffb | -6.55129 | -43.91905 | 2025-08-29 05:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e76ff38f-a41c-3b68-ad88-14aa88992a88 | -6.80243 | -58.98963 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc10b7b8-f1ec-3622-aa71-ad20761194ca | -3.38654 | -59.45627 | 2025-08-29 05:06:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efd3904b-5211-3fde-92ce-931cdf602dec | -8.45027 | -43.7202 | 2025-08-29 05:06:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87cd5b9d-db22-32d1-8de6-7f7134cdb943 | -9.43746 | -47.64671 | 2025-08-29 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c8636b7-88db-3585-aa1a-2ac83d664a1a | -5.62534 | -45.00107 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| aedf8d94-cf6c-3507-a659-78790ca16e87 | -7.81049 | -55.2225 | 2025-08-29 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f5abdd9-30de-3c5a-88c4-2118c0d1616d | -3.41767 | -49.04642 | 2025-08-29 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| afffedc0-f0ea-33c7-946e-f515f405d1ff | -7.16644 | -44.1526 | 2025-08-29 05:06:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37f53311-c686-39f6-a57c-912d0b65f327 | -5.86935 | -42.95305 | 2025-08-29 05:06:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1d5648df-e5aa-30a0-bd15-fff29d17c68a | -5.69378 | -45.96295 | 2025-08-29 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e0418494-b245-3281-aca0-c09a7589b33b | -7.2211 | -45.44714 | 2025-08-29 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9781147b-0315-3d1e-9292-051f1cd72616 | -6.87648 | -43.61268 | 2025-08-29 05:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61145aba-1f07-35b2-a1ee-0bbc0cd0cadd | -3.76715 | -54.8218 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2502aaa5-1cf9-32d3-8854-31c55a0be24f | -3.79198 | -49.42912 | 2025-08-29 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5e9e2797-8252-3129-9472-553eb3468c33 | -7.04222 | -44.38791 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c853d29d-aa8a-3791-92d2-2873a5f9f6b0 | -7.5689 | -47.50478 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2167f95e-6055-3e2e-8d87-b53b41e303ef | -8.707 | -50.36731 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 783838e6-2c28-3981-b89f-af501343f875 | -7.3929 | -45.92868 | 2025-08-29 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a895b27-bd61-3333-bfb9-738d672e5bcb | -7.04621 | -44.35851 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c4c6e3c-98b8-38cb-ac62-2f1675b65a59 | -7.40494 | -43.38285 | 2025-08-29 05:06:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a9a3e53-688e-33b2-8090-0ea80a9bd55b | -5.6938 | -45.96215 | 2025-08-29 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f093968c-2b80-3b4c-bbfa-555d7c9a43df | -6.49125 | -43.53609 | 2025-08-29 05:06:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccbb7472-aec6-31fc-8e2e-381a632c41ab | -6.98782 | -59.34221 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f7f52bf-064c-3338-a1d1-7433d06eec66 | -6.70485 | -49.46138 | 2025-08-29 05:06:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 23211744-1708-351b-af18-adc5bf2682a0 | -6.1403 | -44.42616 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efe85a77-ef39-3cef-b3c2-789f5e6c851b | -6.81578 | -44.99939 | 2025-08-29 05:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87a1669b-dbb5-3893-99db-bbee1b14d968 | -6.26894 | -43.8122 | 2025-08-29 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 543f2b9b-bb17-3e12-9644-861cdb18f415 | -7.39807 | -45.93323 | 2025-08-29 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57847b80-f97c-3889-9458-a54fe472e373 | -8.55565 | -51.31 | 2025-08-29 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aaddb352-ef36-3455-abd0-e2687f48498d | -3.75827 | -54.81333 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3f1be32e-48e1-3cd0-af48-0ea6587cd601 | -7.10735 | -44.5917 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d5da7b3-0bf8-3b68-b444-d5cf156255cc | -6.00868 | -57.85254 | 2025-08-29 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7743ee0-a8d0-34e4-9b98-e5a579a5c2fc | -7.72698 | -50.27703 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 84e95001-233e-39af-9ae9-f53fba72bfe7 | -5.61908 | -45.01096 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 51f19e3f-9014-379a-908c-f8846d017c8c | -6.97745 | -59.336 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6508fee3-b750-382e-9516-8d0f15a4cfa0 | -6.70926 | -49.462 | 2025-08-29 05:06:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 94e3942f-5688-3408-9129-99bed79144d8 | -6.8818 | -43.61974 | 2025-08-29 05:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78299a65-5b37-3b1c-a0f4-6876c5eda9a2 | -5.597 | -45.20636 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 546fdd95-2d25-3e9c-806f-96b8db2f085b | -4.58786 | -43.31324 | 2025-08-29 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffa493fc-dd0c-32ea-be8f-140d4537013d | -5.36958 | -50.89504 | 2025-08-29 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a8bfe1c-2275-3faf-99dc-9217d3e1f978 | -6.5392 | -44.10307 | 2025-08-29 05:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be1c846c-454c-371a-829b-5c82addd5a5b | -6.20311 | -43.3246 | 2025-08-29 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37aaed6e-4ebc-3d9e-b971-24245ead5e32 | -6.98624 | -59.33984 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2796d8d5-bee4-375e-b10e-392843c20146 | -8.44231 | -43.65408 | 2025-08-29 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9b729cb-eefe-35a5-917f-fc9cd2067d61 | -6.70302 | -49.47421 | 2025-08-29 05:06:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a155e1fb-0c3b-3da8-8107-c410bde1ad90 | -4.07977 | -48.04379 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4876e21-d2e4-3d09-ad40-a58682e1cc92 | -9.43226 | -47.64598 | 2025-08-29 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47f11472-2da9-3bb4-9130-b19bcd8aea33 | -7.03728 | -44.37756 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 41212e15-4e03-3b06-8cac-c085bfbe7004 | -6.34088 | -58.18597 | 2025-08-29 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbaafc34-82d5-30ee-8499-900d8e841c1a | -4.22622 | -56.00566 | 2025-08-29 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f3d860e-f1e4-3935-9914-fd81bbf99f23 | -3.73309 | -48.93995 | 2025-08-29 05:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39f5baba-7693-3e78-81ef-e8982eafd71c | -6.16644 | -47.27682 | 2025-08-29 05:06:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f77af6e0-7db3-377e-9dd4-16f141b82168 | -3.66219 | -50.95219 | 2025-08-29 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 173d155b-2d4d-35bb-8315-ac8508afbb77 | -9.51579 | -46.54129 | 2025-08-29 05:06:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fd612d8-dd74-36fe-9b27-4962c7a426da | -5.99823 | -57.85087 | 2025-08-29 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8314a448-59d3-3e98-b11d-f286560d4fb5 | -6.81637 | -44.99501 | 2025-08-29 05:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25751d8f-bc20-3fdf-98a8-15b4c2218729 | -8.29676 | -45.14651 | 2025-08-29 05:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75cea8b5-f5ed-3404-b054-0831ffbc99ef | -6.70804 | -49.47057 | 2025-08-29 05:06:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e56bf5ba-af6b-3c23-8f53-b538f473284d | -4.11067 | -48.0127 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54466566-17d0-3056-a37b-78b648d76a0a | -3.74503 | -53.80402 | 2025-08-29 05:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbe18a21-777f-3a4c-9caf-d4340888a4c6 | -4.11465 | -48.01828 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc95bbed-23a0-3c3d-8195-7e0bc690b475 | -3.7605 | -54.82076 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| a5606dd8-1c14-3ac1-afff-4e9ba0bfba95 | -8.69439 | -50.39402 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97b32147-2d45-3178-a53c-b44d320bdb3a | -7.5693 | -47.50193 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5c7bc84-0859-340f-8215-d5db0ee71893 | -7.7235 | -50.3008 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6446f507-b670-3c5e-b99a-90fd933e697a | -8.56289 | -51.31636 | 2025-08-29 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 426e1e05-222e-39a8-abad-f20e76a11089 | -9.49744 | -45.38626 | 2025-08-29 05:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e3b10da-1982-3415-bd6d-125d54b8348c | -8.70212 | -50.37085 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eb1d729e-5287-318f-9e02-99b3290cb1db | -5.70533 | -45.96019 | 2025-08-29 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8f4de7b-70cc-3683-9343-f76b4389c649 | -6.55058 | -43.92432 | 2025-08-29 05:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c4bb5b4a-c705-3923-8f30-214cf9261012 | -6.9075 | -59.41442 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README61.md)
