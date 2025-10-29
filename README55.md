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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe54fa6a-bab2-3211-ad81-c3d9f53b4bd1 | -20.53518 | -45.76737 | 2025-10-29 04:27:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d8087a1-0da1-3724-91e7-517b6f279863 | -20.16608 | -42.15628 | 2025-10-29 04:27:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8c6f336f-0e24-3445-81a5-956c5809778b | -20.16554 | -42.16045 | 2025-10-29 04:27:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2cbe9c59-93cd-3417-9f85-0fbe19b4a0ee | -19.81546 | -44.06956 | 2025-10-29 04:27:00 | NPP-375D | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2dc1d74-b409-37da-b758-b78cb20b9bf8 | -19.80395 | -43.24907 | 2025-10-29 04:27:00 | NPP-375D | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0d0854e7-377a-37d9-945c-19bc8ae93d09 | -19.4289 | -48.06614 | 2025-10-29 04:27:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0db3fbca-41a0-3b61-8c09-a906f818cf05 | -19.68975 | -43.09367 | 2025-10-29 04:27:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| f7af9d6d-1f12-391d-86af-e4ab08891e0c | -19.45218 | -43.59988 | 2025-10-29 04:27:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 20.9 |
| bf951825-302b-359f-bf46-afa2c919532f | -19.46229 | -43.5821 | 2025-10-29 04:27:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36095c69-f80d-3e40-af98-81ecb46cba86 | -20.80149 | -42.7561 | 2025-10-29 04:27:00 | NPP-375D | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9d08857f-e0cc-3c5e-ba29-2b69d97d422e | -19.45281 | -43.59507 | 2025-10-29 04:27:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e5c66e05-d922-3df9-a0a0-6e706fd8f06f | -19.48357 | -49.28074 | 2025-10-29 04:27:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0001e9b5-6307-31a0-854b-9af76387397d | -20.99777 | -42.79967 | 2025-10-29 04:27:00 | NPP-375D | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 569c704e-7455-370c-b8f6-d520ddb245d1 | -19.45723 | -43.59098 | 2025-10-29 04:27:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e6b879f-1122-3dda-af3f-ebc8b6608642 | -19.45663 | -43.59554 | 2025-10-29 04:27:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cbd855b2-cb10-33a6-9063-46e18fcc9a50 | -19.42557 | -48.06555 | 2025-10-29 04:27:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e900f734-38ef-3613-bfc0-498188c4a416 | -19.90175 | -45.84585 | 2025-10-29 04:27:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3267c085-55eb-36d5-a4c3-6c788744fc68 | -20.16704 | -42.1549 | 2025-10-29 04:27:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ea5c4e61-48f6-3815-8fb8-5bc67de8464a | -19.42166 | -48.06863 | 2025-10-29 04:27:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27f706a1-4c6a-32e1-8ccf-83eada6f528c | -19.804 | -43.25058 | 2025-10-29 04:27:00 | NPP-375D | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ea91101c-f496-3764-ac78-f0bb01a2dbaa | -20.8572 | -42.86621 | 2025-10-29 04:27:00 | NPP-375D | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8cbe357d-3568-3d21-9216-4ff0ee61881e | -19.81918 | -44.07016 | 2025-10-29 04:27:00 | NPP-375D | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15efcb73-8a49-3072-af84-6ba6ed57e333 | -19.57447 | -43.18113 | 2025-10-29 04:27:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 080a2090-42fb-3423-8e9e-ec04e6bb46e0 | -20.16651 | -42.15923 | 2025-10-29 04:27:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 080a3452-5f70-363e-82c2-7fdca45a168a | -20.9231 | -45.58751 | 2025-10-29 04:27:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c35f87c-c221-3e04-b948-a2fec5108d39 | -20.92369 | -45.5834 | 2025-10-29 04:27:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfad9597-f9fc-32de-a653-8d422471875d | -20.99824 | -42.79594 | 2025-10-29 04:27:00 | NPP-375D | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 31ca25c2-f4b5-3212-8975-c98acfe40f76 | -18.9197 | -45.0478 | 2025-10-29 04:30:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 90.4 |
| c23197ec-7b01-348e-b976-17c5cefe225f | -4.2342 | -50.0804 | 2025-10-29 04:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| d39c348a-2774-3fc3-961c-2d89e720efb2 | -4.2159 | -50.0601 | 2025-10-29 04:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 2246b0ae-c11c-3ddf-89e0-61f9b0b50833 | -12.1958 | -46.717 | 2025-10-29 04:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 34ed0ba4-d6da-3909-a87d-05595ba49dd6 | -10.8671 | -50.0916 | 2025-10-29 04:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 69848313-1457-36e9-9d15-5c4de769deab | -4.1972 | -50.0819 | 2025-10-29 04:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 9024ce97-0a32-3064-911e-d3f14d49803b | -4.1974 | -50.0608 | 2025-10-29 04:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| f2f5c1ee-bae6-3501-be6a-bc8ae3456b25 | -4.2157 | -50.0812 | 2025-10-29 04:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 263.5 |
| e96cc9a2-6d7d-3009-aeb8-95e0e05a4646 | -4.2156 | -50.1022 | 2025-10-29 04:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| ce4c1277-dfff-3048-8006-d99ee1c7f313 | -19.4214 | -48.0566 | 2025-10-29 04:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 59.2 |
| fb25d5ea-5b05-39e1-b507-de0904a7e133 | -7.8037 | -46.4458 | 2025-10-29 04:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| bc13e20c-7bdc-33eb-9619-470513c85f24 | -4.2157 | -50.0812 | 2025-10-29 04:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 281.7 |
| de3f7acb-06d9-39bb-83ae-4ee7a0825efe | -4.1971 | -50.103 | 2025-10-29 04:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 0add1840-6b2e-39e3-bbef-0b3f59dbde07 | -4.2156 | -50.1022 | 2025-10-29 04:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| f2342b14-2afe-38b2-8d0b-0fe9f8fec98a | -10.8671 | -50.0916 | 2025-10-29 04:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| d2f5355c-e1bb-3109-b9d7-ab12ca90bc85 | -4.1972 | -50.0819 | 2025-10-29 04:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| f2a99e80-cebc-37df-b125-552751ac01b4 | -9.4361 | -46.9063 | 2025-10-29 04:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| e4a6a660-7bbf-328c-a9fd-835da9acd994 | -10.8481 | -50.0937 | 2025-10-29 04:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 46328755-2d8e-3ae6-b591-20ed846c0223 | -12.0032 | -46.7892 | 2025-10-29 04:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ad161e0d-9a82-3133-a706-65fd94d53c13 | -4.2159 | -50.0601 | 2025-10-29 04:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 8d2f6e5d-25f9-3c88-8b64-0f4c18761456 | -7.8037 | -46.4458 | 2025-10-29 04:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| fcec7535-b556-389a-b016-fb5eec0830a8 | 1.96269 | -50.95676 | 2025-10-29 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 682f645d-5946-3a63-a21e-1aa404f93483 | 1.60793 | -55.69732 | 2025-10-29 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77e15cbf-3031-3438-87ce-80f859eeafd0 | 1.88636 | -50.82578 | 2025-10-29 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ccd4a11-1265-36d4-b3ce-495fefcfb02d | 1.60036 | -55.70765 | 2025-10-29 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eea5a7ad-9d91-3422-8b49-e21349422dbb | 1.83628 | -50.50419 | 2025-10-29 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 61e5e340-7d5f-31ce-a692-4c2ab92da32c | -0.86569 | -47.3124 | 2025-10-29 04:42:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d88369b-0486-3ccf-a992-848fdec86cf6 | -0.42336 | -52.03873 | 2025-10-29 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb64ea63-cb2d-35c5-b551-32cea9c9e9fc | 0.69215 | -51.46154 | 2025-10-29 04:42:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fce6505f-6616-3e4d-8ca6-c0ad4211ed21 | 1.80162 | -55.67181 | 2025-10-29 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3165e2ce-86e9-365f-b3a0-e4c563d3e646 | 1.60863 | -55.70178 | 2025-10-29 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ad79b46-c108-3b00-896a-0af5189f1bba | 2.34787 | -51.54002 | 2025-10-29 04:42:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6746081-bfc9-39a9-b10b-588c27155949 | 0.1509 | -51.09891 | 2025-10-29 04:42:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba4e9d9b-a2e7-3445-b161-de458fd17aee | 1.83291 | -50.50471 | 2025-10-29 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5b762af3-027b-3f37-b3cc-e196ee110fe7 | 1.04059 | -51.31329 | 2025-10-29 04:42:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 762b59e9-c3b1-377c-88a6-2c0fd221e036 | 0.60878 | -51.57846 | 2025-10-29 04:42:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 843056a1-c2c8-3089-a085-7aeef026e115 | -0.42684 | -52.0393 | 2025-10-29 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47ade41a-9b85-3852-ad75-fb1c5def98b8 | 1.03567 | -51.37146 | 2025-10-29 04:42:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6104a57-eaf5-35bc-9362-8ad66f25e9bc | 0.07584 | -51.1292 | 2025-10-29 04:42:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79c6c829-1088-3f59-b1a5-519483e59c00 | 0.15429 | -51.09838 | 2025-10-29 04:42:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2a096c9-73fc-3370-b6c5-c7f2a2b6ecd1 | 1.60484 | -55.70696 | 2025-10-29 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f893789-220a-3f9e-9d5a-783529c37d80 | 0.57743 | -50.33757 | 2025-10-29 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e382d68-bdf5-3249-add5-6a20be75d603 | -0.43033 | -52.03986 | 2025-10-29 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f94a956-6613-352b-88c2-0d8efc5a7b28 | -1.14256 | -48.09641 | 2025-10-29 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9897e5bf-f014-3c85-91cb-b054df89155b | 1.60415 | -55.70245 | 2025-10-29 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3b0b67c-1e01-3e10-b520-08e2f5c51398 | -3.22527 | -49.36793 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 685e37a0-9f06-39eb-9178-6dd69b3ae86d | 0.4555 | -60.48589 | 2025-10-29 04:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23a383f2-242a-3026-acbe-b1c070cf39f9 | -4.3605 | -50.66002 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d216a00-3fc4-3817-ac32-dce5bd64c160 | -3.2402 | -48.77826 | 2025-10-29 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3068e24a-7b2a-39ac-bcec-e77e57d8e25e | -7.81341 | -46.41525 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9820b93e-9d10-3d20-becd-cc17c73eb363 | -6.09053 | -41.7795 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d37b1932-ea4a-31e3-8aa4-b358a6c0683c | -3.3223 | -52.6295 | 2025-10-29 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| effbbac0-61ee-34f6-af37-73d2e552d91e | -8.29049 | -49.31504 | 2025-10-29 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 689fefa3-b4b3-3ddd-a44b-154882d4b0c8 | -3.37967 | -48.94532 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 344700a8-4fe9-393a-9191-f3874a4002e0 | -2.9429 | -55.79206 | 2025-10-29 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c007742-49b9-3f23-b1f5-a1cf3524de79 | -8.52025 | -44.09306 | 2025-10-29 04:44:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fabbaacc-39bc-39c6-b25b-ac72e6e9f2d9 | -7.80257 | -46.46087 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c841ae7-0298-3e97-abed-946e6c5ffa71 | -7.80183 | -46.4659 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18a9f494-2716-373a-b408-868415e9c3dd | -7.45115 | -47.15686 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29f3c104-ed70-394b-aa93-fda9ca21ab80 | -8.01074 | -46.20871 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1411c94-5bef-3ce5-9e36-7e1c60cdf1c4 | -3.37806 | -50.14571 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc24e1a8-35cc-3be6-a9d7-95f3ea7d9ba5 | -4.25047 | -48.57514 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b4fe489-7194-352c-a5cf-acf63e6e4d5b | -6.12602 | -41.70646 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 201baa5b-e066-32e6-a1b7-fc4969ccd8bc | -7.74805 | -44.71848 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74e586e4-a005-30b8-be3f-4526e52cefa2 | -4.35669 | -47.23616 | 2025-10-29 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56328892-ab60-32bc-a3a2-2df42c0b73b4 | -5.61044 | -49.11703 | 2025-10-29 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77f654cd-c39e-3e8f-9ef2-a1b3a9ad5352 | -3.71511 | -41.56524 | 2025-10-29 04:44:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ac2b6022-9711-3194-9ad7-33ca0aeee239 | -7.2687 | -46.90133 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5599f4d6-fa04-3854-9444-d35b585164bc | -4.74449 | -46.45687 | 2025-10-29 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b48e256-056b-35a6-8dc7-af2f9f5f17ca | -5.33167 | -45.43389 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05717eea-bd3e-365d-b7bc-4382b69b2fd3 | -1.37625 | -52.98956 | 2025-10-29 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77768c13-4de3-37d9-a6d5-4f3e891f4500 | -7.45635 | -45.47197 | 2025-10-29 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0038ea2-b416-3653-8a8c-67b9da40b0e8 | -5.60914 | -47.10943 | 2025-10-29 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README56.md)
