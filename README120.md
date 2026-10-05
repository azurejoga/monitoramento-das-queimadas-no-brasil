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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acbe71b2-716f-3807-8cb5-6db91d6c43b6 | -6.7084 | -45.22412 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1f7bec21-e9f4-3463-a95c-40cbf0482a1b | -5.80389 | -53.42222 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1607e23-b701-3eb7-a111-715073644dbd | -8.59737 | -66.81483 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| d3921932-43c3-3c0d-b13f-4fc5f9afa0ef | -9.46533 | -64.32709 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 267ad4b4-18ee-30b4-ba53-b72c720f1c5e | -6.72539 | -44.27396 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 7abd3ed4-3fc5-39f1-85a0-9fd06d449080 | -8.53237 | -50.43896 | 2026-10-05 17:15:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2b37b590-7fd7-3043-9960-bef443999f68 | -3.78913 | -59.37602 | 2026-10-05 17:15:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d918a42a-7d30-3d92-a540-bdd45c2978ec | -9.45972 | -64.33272 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bc2be9c9-63c6-343e-a179-5a38200ba421 | -4.46745 | -54.96322 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8e0d9f3b-441c-34e4-809c-b7a29e8938e4 | -5.95104 | -41.3574 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 175.7 |
| e9baed22-3458-3a2d-b852-b015a1dbebab | -6.6837 | -55.10375 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 16e1ce86-c7ae-39d1-aaa2-0bdebcb49b3f | -9.40927 | -47.31069 | 2026-10-05 17:15:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e975e5ff-0191-3410-93b1-663a8ce7d721 | -3.07656 | -54.15926 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 08d8677f-1623-34e1-982e-217133480c04 | -3.21391 | -42.44514 | 2026-10-05 17:15:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 92bd3b49-66c0-3447-90a9-f5688bbbde3c | -3.58344 | -55.40357 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a707bbf6-6ba0-3e3d-aee9-cac299dccd24 | -3.26993 | -54.00888 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a4659c20-10fa-3bdc-ad32-a78327504012 | -4.32674 | -43.82243 | 2026-10-05 17:15:00 | NPP-375 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c22ad8cf-b2e5-3607-8983-2bc204ae55b9 | -6.25204 | -52.84327 | 2026-10-05 17:15:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5da2c03f-3074-3b06-a436-f7a474b663ff | -4.16135 | -60.78621 | 2026-10-05 17:15:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fbf9bde5-c501-31bd-ae0d-52cc8135009f | -3.79544 | -41.76594 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 39af7789-82e7-3f72-a7b0-086f9b03ba7b | -3.57037 | -55.41708 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 20fea43c-9a67-3916-a725-225a302be511 | -6.24148 | -55.6455 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9ecc72fc-e8d7-3fae-b5df-364232c6dd04 | -5.47456 | -41.23106 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4403e283-292f-36f0-a907-91b0d9623ffc | -10.87762 | -61.40676 | 2026-10-05 17:15:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1dd9cb16-0b14-3eb2-b428-21fcf23bf875 | -3.65352 | -55.48008 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87b1eacd-530c-3f70-8cf6-94e9f256d381 | -4.81579 | -45.92744 | 2026-10-05 17:15:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 07c5198f-8242-34f8-9528-53017d3a3147 | -3.52567 | -54.33204 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 27f25a5f-fe1b-3606-b998-627bc6890e6a | -9.12113 | -64.36301 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 599ef8a4-b199-3ce3-96b9-671a4d77e081 | -6.00343 | -43.78853 | 2026-10-05 17:15:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 10c0893b-c321-36d6-9547-285157e48b80 | -7.73181 | -45.47016 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4f9a187e-8c95-3d3e-be96-5c996fda4925 | -4.4326 | -43.43002 | 2026-10-05 17:15:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e549e97e-680a-3314-a9f0-1fdab5bc9531 | -3.50742 | -54.61104 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d2705ac7-9a90-3a17-b72c-7d3c468f4527 | -7.23044 | -55.19658 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 379ad5d6-2919-3a27-ae5a-3e3b92609fe0 | -3.3588 | -43.01969 | 2026-10-05 17:15:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 79b9ca76-bbc8-358c-abc0-583f2721118e | -3.95341 | -56.05356 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 8b7138e0-6635-3722-849b-6eb0d040c191 | -7.90494 | -44.20223 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc979729-eef2-323a-87a8-d5a23a4265b6 | -6.42543 | -43.71532 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5ce0eb1f-2a23-38f4-85bf-2637025cec4c | -6.10615 | -55.67339 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| fbecedd0-0408-36e9-8ba8-878ece3e9478 | -5.55143 | -44.08482 | 2026-10-05 17:15:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b1091b46-b31f-3e17-a5fc-6e6805598bc7 | -8.00476 | -42.9132 | 2026-10-05 17:15:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 440190c6-1915-3d92-99a7-68e57e274e50 | -5.98709 | -55.36575 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d6d1e0ed-2c15-318c-80ac-b51260af527a | -6.20873 | -44.8019 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 064b878c-c621-3763-9af3-d25e29a8b0e5 | -7.84719 | -54.84421 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 73a25347-4ce2-379b-a1d6-0621a2347c15 | -4.13621 | -54.01326 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a099b5c3-f4a7-3855-a5dc-f021761e1900 | -3.88695 | -58.95183 | 2026-10-05 17:15:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e9650967-1e28-3b69-b31a-c3043bafa4f0 | -3.06487 | -54.17162 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 54cba4e1-a1c1-3cb2-9f36-81734b7fefb9 | -4.55713 | -43.71089 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ce68f01b-49d1-34b2-b1d0-36fd4f7d1af8 | -8.8164 | -49.30746 | 2026-10-05 17:15:00 | NPP-375 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2ad8bcf2-d279-3adf-b414-986c8bf8b38f | -7.38608 | -55.00042 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b714348-1ad8-38d3-b6c6-63acd59a2050 | -8.00514 | -42.91431 | 2026-10-05 17:15:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 46.1 |
| 58b50f7d-f375-3ac4-bc5f-94843dbd8a6c | -4.06668 | -54.04523 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 7a48f783-51f8-330a-9db6-d0b487839b70 | -8.52939 | -54.57617 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 23fe9062-e753-376f-90cd-936c8f7eb66f | -3.69522 | -55.96112 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 9ffdac09-67f2-32fc-9e25-9fb5ed68d03e | -4.86663 | -43.46753 | 2026-10-05 17:15:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bbfff5ea-e85e-373b-93a8-9fd5ed08da81 | -3.03704 | -54.25418 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dc15ce07-eecb-3515-aa15-f000cf2555f2 | -3.71651 | -54.23149 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 63aab0cd-734f-3bf7-86cc-97b2af895a99 | -3.79905 | -58.34916 | 2026-10-05 17:15:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| cf6f683b-fcc6-33f9-8a61-30ab4f318c80 | -5.39974 | -54.45192 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 77413954-53ec-31b3-9a76-c778e6098c5b | -3.93947 | -52.02824 | 2026-10-05 17:15:00 | NPP-375 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f7c52fd2-1ba7-39c2-8a0b-3a26021455c1 | -7.73273 | -45.47541 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7c5acac4-5054-34fe-b14b-2544558443e9 | -3.67531 | -54.53807 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| e6cc92c6-b5b0-39bc-b689-e4e4f2f88d1c | -3.89757 | -58.73705 | 2026-10-05 17:15:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| bb51b8e0-7d5a-3d18-883d-0a2d2fe836bd | -3.05725 | -54.20877 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a95cf7bb-8e69-37ab-b579-98ccee5e591e | -4.15682 | -60.78681 | 2026-10-05 17:15:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8a5a150a-5885-3b65-9357-58c71bdfd1eb | -8.54455 | -54.58501 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e303a4bb-423f-3ed4-9db9-8132644a6e1a | -3.69069 | -55.95427 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 5aa477d5-d8a1-385d-90c8-ff8bf9224840 | -6.71369 | -45.54806 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5931db4d-78b0-3b66-b981-27592faa64f9 | -4.42422 | -55.63763 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| af2b1eac-d963-3723-949d-05a2f25a6bb1 | -3.28762 | -53.83629 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d1431a72-5ad8-3da8-9622-2d976c982c6f | -5.20743 | -60.24816 | 2026-10-05 17:15:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b0631e20-e24d-3209-835e-b35406175040 | -9.07643 | -66.08981 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 76b61a4e-ab80-3c33-b236-2bd71b033e3a | -3.49904 | -54.62292 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 1edf0157-355f-337b-81e8-05d14b925860 | -8.53369 | -54.60526 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4194f1ea-c99f-31e8-b122-9df0f1f3cdcc | -4.35762 | -43.82972 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7bbd7346-790c-396d-a7fb-9442304bb0d9 | -9.03506 | -45.17094 | 2026-10-05 17:15:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4e53f474-dfce-30f6-a7bc-bd90e686dc95 | -3.05926 | -43.39559 | 2026-10-05 17:15:00 | NPP-375 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8c9e94dd-f276-3c9d-9cec-1b13175c4cf4 | -6.70974 | -45.55463 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6946cb12-7bca-3951-81b0-270c72b626be | -6.726 | -44.2775 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 8b00b2bf-552d-3132-96f9-f42d31ac79bd | -9.13777 | -65.90668 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 34c80e20-befb-3f68-aec3-273ece1acf7f | -3.73127 | -55.48256 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 724e16b8-990a-3526-ada8-444cf3c63c1c | -7.22866 | -55.20821 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e827ebc5-0b60-367d-9630-554789100c2e | -5.51711 | -44.11684 | 2026-10-05 17:15:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7b0d3b57-8b80-321d-8c6b-7a038325855f | -3.23644 | -53.87951 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee50794b-6144-3b2f-a0f5-a26b130e192b | -3.21441 | -42.44279 | 2026-10-05 17:15:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2881c648-7158-3bf7-9286-ad7c902789a7 | -7.22127 | -55.20547 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e09a3352-0a5d-348b-9228-b98b8ddfbb51 | -8.6613 | -66.59073 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b7539fec-3853-3454-a508-79ff3fb9358a | -8.0108 | -46.44843 | 2026-10-05 17:15:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e7cd35d5-23b4-3335-9358-4ab80654bd1f | -5.14721 | -42.68821 | 2026-10-05 17:15:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 902a64f1-4cc0-36e9-8470-8dea6e116cfd | -4.44511 | -54.97377 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| e6da1f30-c43e-3e08-a1cf-608b88fa5170 | -4.06615 | -54.04178 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 330e3d25-1376-354e-9eaa-20bc0c419f67 | -8.42461 | -54.99792 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| cbbaae7d-5aeb-328b-8cc6-0766fe62137f | -6.00274 | -43.78455 | 2026-10-05 17:15:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a1ee4270-90a1-3cc5-bb01-6748f7ffac4f | -3.09865 | -53.74881 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 2170e001-16f1-3a8d-80d8-04d3c48685a5 | -4.06468 | -47.06228 | 2026-10-05 17:15:00 | NPP-375 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ac1181fb-2d43-3b54-b12d-022ad14cd2b3 | -6.32991 | -42.54849 | 2026-10-05 17:15:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| a0926892-11d3-3fab-8f5e-ec6c921ba7e4 | -2.47784 | -49.37854 | 2026-10-05 17:15:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a8c8de8-c5e1-3f38-8d46-745ade2c1e5a | -6.87475 | -43.68137 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d3560fdc-cc62-3431-aa83-c06255bd84a5 | -3.32073 | -53.85254 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ba46f67a-9fd4-3923-8933-dea5ecd72262 | -5.89488 | -53.63879 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4a7edb4b-3c4e-387b-9d32-56b7c0624746 | -8.52708 | -54.58395 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |


[Clique aqui para ver as próximas entradas](README121.md)
