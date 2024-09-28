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
| 9e9173a1-2409-359f-b403-79474b125ba3 | -5.54365 | -44.67313 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4bd3e56-eb29-34c4-8c5b-e3b5805ddfe3 | -5.54248 | -44.67937 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab77a9b4-4b38-3f2d-b956-2f0e8f1ab5ea | -5.54105 | -44.6767 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5a15f8af-58f8-306b-ad3b-ccfa28a073a2 | -5.39073 | -44.64812 | 2024-09-28 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 668ebfc8-13fe-37de-b521-a91c7fe50d8c | -5.25505 | -44.72961 | 2024-09-28 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 17b4745a-d680-3986-a49a-c9dce291c867 | -5.25426 | -44.72958 | 2024-09-28 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 55afa1f8-b09a-3559-89a5-3949dc9cb3a0 | -5.2046 | -44.53675 | 2024-09-28 03:28:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c1f5588-77a4-3fa3-a2c0-0e7377a1a6a2 | -6.88864 | -43.87004 | 2024-09-28 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a34bf171-f3d6-3f8e-9f90-60db9a57c3ad | -6.88136 | -43.87416 | 2024-09-28 03:28:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14d7c003-a6a6-30d0-954d-49005bf0484d | -6.63076 | -43.85855 | 2024-09-28 03:28:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a81287c-e3d3-3aea-b828-6d127d22c2ba | -6.64636 | -44.71334 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6009cc45-447a-36b5-bde1-8a27722f33cb | -6.64521 | -44.71945 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5674b64f-66e8-3026-a0d3-0ace53c5a5e1 | -6.64232 | -44.71635 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cdce949c-f111-3eab-bbfe-74f2e91481cf | -6.63858 | -44.71802 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23c1ab94-bc5c-31e0-a358-9c154276b28e | -6.58511 | -44.18148 | 2024-09-28 03:28:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ff2eebec-b428-3e2c-9642-a5d88f1682cc | -6.58412 | -44.18694 | 2024-09-28 03:28:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 14b11328-bc79-32dd-8aed-7d8e7aa1266e | -6.57879 | -44.1795 | 2024-09-28 03:28:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2fc80f66-e3bc-389c-961f-57b569511347 | -6.57769 | -44.18548 | 2024-09-28 03:28:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8199d818-1702-3a3a-b149-9ed1ebb205d3 | -6.5724 | -44.17786 | 2024-09-28 03:28:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ba170df-f8e3-312c-b987-cfb2d73faa87 | -6.57134 | -44.18363 | 2024-09-28 03:28:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 95b281cb-382f-3847-bf08-9586af13006d | -6.56106 | -44.94403 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c696f9af-3d7b-38d0-9f48-67e00156044a | -6.55992 | -44.95003 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01588e5b-37a0-3013-9c9e-a60051047081 | -7.89155 | -44.60426 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 0263a477-62eb-33b3-aaec-72a4f7af5c3a | -7.89055 | -44.60955 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 2c43eb76-e34f-3513-8cac-6043d550bd65 | -7.88954 | -44.61495 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| c6e0d45e-edf2-30af-9635-68928bc8c205 | -7.88851 | -44.6204 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8c7ba369-4c89-3dc1-9de7-ed3c665e61ab | -7.88748 | -44.62589 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 49f0e248-bbea-32df-97b8-0f5c96753c4c | -7.88506 | -44.60298 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| e57f4f35-a70f-3f9f-8f64-b0f87a469099 | -7.88407 | -44.60823 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 07574cc2-aae3-3cbe-8ac1-dd1884e40a54 | -7.88305 | -44.61366 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| a1b9882a-71e5-30a9-8744-d190ccd5f5b4 | -7.88201 | -44.61914 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| ab28ca43-9228-33a7-ba52-1e7ff64514a9 | -7.88098 | -44.62465 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a4d2a35a-d40e-3701-9b85-f5b55142ebe3 | -7.87855 | -44.6018 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 11402ba7-1660-3056-aeaa-e9dea0d632d5 | -7.87784 | -44.64126 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e37c996b-175c-3a74-a9ae-c942b92645d0 | -7.87758 | -44.60696 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 33650464-c1d7-32f6-9f5f-0a34c243e4f4 | -7.8768 | -44.64682 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d671ddcc-5495-3eb3-9432-a0d003256dbc | -7.87655 | -44.61238 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| b01b44a2-fa2b-3fc1-8ae0-d352be0ad856 | -7.87552 | -44.61788 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 01a7711d-cda8-3261-8e23-19616199d9ed | -7.87028 | -44.64557 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b758732-e9db-34de-9ae6-8de2d11a03f5 | -7.87005 | -44.61115 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8ece8dde-d67d-38f0-b5d1-21bbff589e39 | -7.86902 | -44.61663 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d8e23f6a-d802-3a49-8c12-93882c0c9918 | -7.86459 | -44.60446 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ca435864-05c3-3e6c-8ff2-e46c96a1b2ff | -7.86377 | -44.64432 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5944ef3-102e-336d-b3f3-c03b86e73974 | -7.86355 | -44.60994 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c54dc4fe-c156-393c-aecc-1f0cde0be5ed | -7.86272 | -44.64989 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25b8f7c0-afb9-33b0-8aab-5293644dc110 | -7.86251 | -44.61543 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2c5b38ed-30f9-3fd1-ad7c-ead7b9035f46 | -7.78995 | -44.67683 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f6461de1-1492-3db7-bd04-9124b0859556 | -7.78887 | -44.68242 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 64f96e71-279d-39eb-bc7b-8ddb952f4bc8 | -7.78328 | -44.68319 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8ee041af-4ffc-3642-a47b-a2aeb52896e0 | -7.78231 | -44.6813 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aecca951-cc9d-3182-b953-b00a0a3a559d | -7.77777 | -44.67649 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 573930aa-0f1e-3f26-9485-5ab4c050759c | -7.77123 | -44.67529 | 2024-09-28 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f7eecb2c-1f55-3c0d-a823-97b98a8fd70d | -7.38713 | -44.10907 | 2024-09-28 03:28:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eadf277d-7038-39b4-93ce-22da97b4db9e | -10.85922 | -44.80043 | 2024-09-28 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21cc2f3c-e7e0-35fc-bf65-f73a1d99f341 | -10.85822 | -44.80549 | 2024-09-28 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d565e72-7b62-335a-808a-e5c284f10a52 | -10.85296 | -44.79922 | 2024-09-28 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79e198d5-d01e-3198-a252-ff3fb649029a | -10.6951 | -45.8697 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6624ac51-3bf2-37d5-9ec1-9bca76380804 | -10.69164 | -45.86803 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c4cca978-b61e-35c0-9477-170f6240fb69 | -10.68848 | -45.86802 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aab8dc7-b8a9-3140-a5a5-bbc96b829731 | -10.68302 | -45.86057 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95d89f75-c8b2-357b-88de-bd53917fd6f4 | -10.67464 | -45.95092 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a82bb0d2-9380-3aa7-8cb2-ef49ad91fc1e | -10.67373 | -45.88744 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7e98eeb-d079-38bc-b4bd-7d3b482f0a30 | -10.67333 | -45.95729 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 10007b89-cd24-3ed6-9884-3dcac645fc44 | -10.6725 | -45.89342 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81c750c9-4146-3ffa-a5ea-805d9f15a2f6 | -10.67197 | -45.95124 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 09e75bf6-b7f7-37bc-be04-b55ddc0b95aa | -10.67072 | -45.88744 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ada5ff00-4bf3-34bf-b8ed-afd77c515a01 | -10.67071 | -45.95761 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b88195bb-bb73-3918-aed8-52c9fec8bc8d | -10.66831 | -45.87997 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75d85781-f87c-3bf3-80dd-2a9b1896f952 | -10.66797 | -45.94935 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0540d69b-88dd-3730-8755-865f60d4d5d5 | -10.6671 | -45.88585 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d6b8958-b092-39bf-b622-fdd2157e29c7 | -10.66657 | -45.94328 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88d03d63-5be7-351b-89f1-4ce36aab2ba0 | -10.66531 | -45.94963 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 383b3830-1802-370e-abd0-d096f04b76b9 | -10.66525 | -45.87997 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8855e3a-dd3b-3214-be1c-94c023072f7f | -10.66261 | -45.94146 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 115af81d-8e02-340f-96b5-6685694e56cb | -11.11134 | -45.59134 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4703b2e2-6f71-36cb-b0ae-da1fcc2a91c9 | -11.10498 | -45.58921 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84794bb3-3c2b-3af7-a41f-55d5b401c128 | -11.04348 | -45.73536 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bd43057-2b07-3d9a-8e97-dc2e569395a0 | -11.04107 | -45.73507 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf52f210-bfde-3642-bcb3-c7a5736b8ec0 | -11.03696 | -45.73368 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48c5399f-5403-32f4-a98e-999af74c504c | -11.03582 | -45.73939 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0da346e9-8443-30c4-8d3a-498ecab7ad71 | -11.03454 | -45.73347 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4f8ef85-a8da-3a26-bbfe-cf9a8e89363c | -11.03336 | -45.73919 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 087ae103-84ce-3078-b398-333162e67c5f | -11.0273 | -45.71335 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0d97ea68-994f-34bc-886e-8f059f46576a | -11.02617 | -45.70754 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 527c36f1-1960-35a3-b96a-afbeafb6ff17 | -11.02615 | -45.71912 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a4b22798-7073-3fa9-bcc1-3e1341625c05 | -11.02499 | -45.71327 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b8ba5954-9ebe-321d-9c4b-7cf22d43cc1a | -11.0238 | -45.71902 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 489881ce-3e2f-39ec-87a4-13ec6c03d545 | -11.02074 | -45.71192 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1cdfd51e-b245-3fcd-b20c-bd8325c99e11 | -11.01958 | -45.71769 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bb7c3044-5356-3d6f-b20d-b43e81406530 | -11.01842 | -45.71186 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3960e86e-ffb2-3f3d-8b46-855142771086 | -10.87111 | -45.5218 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 53a6c5e3-8da5-3354-94ba-56b9bc29a46c | -10.86968 | -45.5291 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5c055c1c-f2a6-337a-97a9-1abce552788b | -10.84418 | -45.55497 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 35b40777-7d82-34d8-b120-2abe1cbbcf9e | -10.84246 | -45.55543 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 265f6962-dae8-3f9e-9636-4b97c2081fd7 | -4.9849 | -45.40425 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b8a61794-11cf-355b-9258-696a38e85793 | -4.98369 | -45.41101 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc2043ca-9299-38a2-b739-f794ccc3a9aa | -4.98155 | -45.402 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0f6fe31-47a6-34e5-9685-1723260e124e | -4.98033 | -45.40855 | 2024-09-28 03:28:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af8337ea-c2ab-3a92-90ba-be48a58e04e5 | -6.17833 | -45.43501 | 2024-09-28 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2db707de-c785-3016-982b-22212a3e6226 | -6.17711 | -45.44176 | 2024-09-28 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README28.md)
