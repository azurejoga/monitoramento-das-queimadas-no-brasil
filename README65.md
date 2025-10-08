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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3ba3911-1bac-3efa-a419-63dc81efae1b | -8.15245 | -54.84388 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 904cee35-5e02-33a8-a242-d6a33ecb9ae4 | -11.81484 | -45.137 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de75e9a2-2c4b-3b9c-a366-2bc4b174d4c3 | -8.46192 | -47.20578 | 2025-10-08 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 927f0504-53c7-3cc5-af6a-d5a6ac8a0cd0 | -5.11385 | -49.95227 | 2025-10-08 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3af231b-b8c4-3748-ae81-cf2a777fac12 | -10.50255 | -51.84003 | 2025-10-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d39fc76-3059-30bb-9e42-3d1aacedb847 | -4.47927 | -49.71602 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5c6b6e8-e431-3c64-a005-250c2ff3193d | -10.2317 | -52.69608 | 2025-10-08 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa05e9d6-2020-3d01-b22e-08371935df65 | -9.20097 | -46.90054 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fd30d4f-00e6-3dae-bfec-acb4084f05bb | -7.82042 | -44.1427 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 759c5d04-75ca-381c-8cf4-59751e382527 | -5.40389 | -46.22561 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbc32c25-082a-3589-9954-d4bceacc8688 | -8.44497 | -54.71607 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41f95bde-fa4b-3eb3-962a-4a274eb03fa2 | -11.76132 | -45.13763 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64c3ef32-83ee-3267-a593-a2b91cf437dc | -11.86396 | -44.93235 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1abbfd57-7cf4-3565-b2cf-829cdb6dee5d | -4.69153 | -45.84616 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 017e6402-46d6-3bfb-a46d-4ec3c55bdc5b | -9.61932 | -54.31648 | 2025-10-08 04:38:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33fed439-1206-37a4-889c-8ec563bb944c | -10.37349 | -50.27174 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0da7e1a2-c783-3bcc-bd68-a4ad048043d6 | -7.43716 | -43.14231 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5d5bb081-834f-3447-abbc-bda8b84779f9 | -5.71621 | -44.82347 | 2025-10-08 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e8ebb23-556d-3f72-a287-17590e979bea | -7.80036 | -46.0196 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2b48b83-9ddd-331c-b2ea-f4e684050e1c | -9.1764 | -46.91809 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 948f952d-db06-30b1-8519-82355779b614 | -10.5823 | -51.47583 | 2025-10-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc699dd7-5a4a-3b54-8603-b61752e38304 | -6.44928 | -44.58311 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c89d5d8c-e600-30cf-822f-bb481f0bfab7 | -8.11414 | -47.25222 | 2025-10-08 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b60cc7c3-3a83-3cf2-94ab-6847ae7344ca | -6.16407 | -51.16301 | 2025-10-08 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00af8a96-6bd4-36af-bc27-53efb941546e | -4.95012 | -45.596 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29b23161-a2ef-38f4-838d-ba18e6ad99ac | -8.61876 | -45.10466 | 2025-10-08 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5390fc43-fc00-37c5-a87d-f80050323c28 | -4.22102 | -46.83706 | 2025-10-08 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3af4cf9-1f6c-33dc-b2a2-d63c18781833 | -6.36832 | -41.618 | 2025-10-08 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c0c2be99-24cc-32ae-acf5-ff0ad7dc220d | -8.86484 | -46.77701 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9fdd5e9e-a0df-34af-a50e-05edc0e7cdfb | -9.97676 | -48.78531 | 2025-10-08 04:38:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 078126f4-8158-3252-b1c5-4099acfc7fd8 | -8.19726 | -44.19993 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad903e47-9dd3-3125-b666-6a3fc2018853 | -11.06176 | -47.93434 | 2025-10-08 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c28a54b-8cf1-3408-b83e-dd0798dad1af | -8.44649 | -54.71621 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe13c03d-28ff-366c-b9e2-d82d2f96fc27 | -8.11418 | -44.77489 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c4f57ff-4cba-368b-9952-48c8f564a278 | -7.91097 | -47.13874 | 2025-10-08 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9897d2ef-0409-3efc-a593-52679b6e8fdb | -10.23104 | -52.70003 | 2025-10-08 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fd95e28-9dc4-3ad6-9169-47724739f9df | -9.2058 | -46.89274 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24a97bd4-fd62-35b6-a8df-e8e200b6b00c | -3.49906 | -51.11211 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23c7f35b-ec62-3e9e-870e-815c819b3bda | -4.68496 | -45.84109 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 226c51e8-b8ba-36c3-bfe9-ae2cef7a538a | -4.08431 | -48.04206 | 2025-10-08 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32c8e2e0-4043-3985-a257-a20171e1dccb | -7.7905 | -44.23121 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8efd852f-0c1d-337d-9d0f-74cc914b9310 | -10.6823 | -47.55254 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a832ed9d-01a4-3f52-a3b9-db0d6a465e48 | -5.82447 | -35.47974 | 2025-10-08 04:38:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ea583503-34d5-31cf-aa16-802085334d94 | -10.91717 | -51.01884 | 2025-10-08 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38918fef-4423-36d1-b385-13cf73bc89ac | -6.28393 | -45.31964 | 2025-10-08 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ead620e-3df6-3864-90ea-5f686311f393 | -10.81547 | -48.81059 | 2025-10-08 04:38:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3928d5ca-c9f2-3495-89f6-bbd3f0cb0899 | -11.77365 | -45.13936 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbdd3fde-fbcd-3cd7-acd4-20656bfd3e2d | -8.479 | -46.28043 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e38d7f6-9372-38ec-a308-3b5e89435fc9 | -5.19049 | -45.96186 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c3f4c84-d529-3989-b3a5-9c16c98c0a81 | -10.39956 | -50.23684 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8672827a-749d-3df7-9d29-99b6c936b6ab | -4.91937 | -48.54183 | 2025-10-08 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2c086b3-888f-3327-9e7c-b3876c5f21fc | -9.29947 | -45.65188 | 2025-10-08 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8f6f9488-8a04-3056-94c5-eddcb8287c0e | -9.76183 | -47.68924 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa4304b4-a1e3-36ae-a7f2-938c27c2a0eb | -4.91225 | -48.02426 | 2025-10-08 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce91a0d1-62f8-3acb-b73f-5605819987c2 | -9.32702 | -60.59931 | 2025-10-08 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48086f1e-6972-3fdb-9ca0-adc34ce29b60 | -8.33326 | -46.22884 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d988baa-dc4e-32d1-95db-e4493c075bb2 | -11.46526 | -43.48615 | 2025-10-08 04:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 109df4ad-c25c-3de2-b270-fe75afae2407 | -11.79518 | -45.04654 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7d4ddc7-fd49-379c-841a-8dbb5f30c7a0 | -9.90382 | -54.86272 | 2025-10-08 04:38:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23faff4e-355d-3a3c-9ae9-6a7be36e4a5f | -11.13236 | -47.94814 | 2025-10-08 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4057cf42-4a7c-3bd3-b01c-2a904ea310de | -10.46623 | -52.16988 | 2025-10-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c727fd1e-3de0-3fe4-876f-b6b452fd8ac7 | -6.09406 | -44.81215 | 2025-10-08 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31825107-64d2-31d8-9f7b-a156a04976a0 | -7.41474 | -45.17554 | 2025-10-08 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c90ea429-1a9a-3d67-9927-c0c4253cff3a | -7.77902 | -44.19445 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f67826a8-af04-3d42-86c6-d12c70b0cd7c | -5.70195 | -44.21983 | 2025-10-08 04:38:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b46988fd-8377-3518-8933-f2c270ea5ceb | -8.62017 | -54.99071 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 299eeba5-fb78-3c42-b7b0-2e72a8bc7d6a | -8.60152 | -48.2484 | 2025-10-08 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4d7f04d-1877-3d27-a278-6c4d44c9b069 | -10.47246 | -52.17482 | 2025-10-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15f10191-8a40-3509-80fe-176963ef0367 | -10.04961 | -48.28287 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77ec998f-aa1e-3687-ac5e-8d3f0de9213a | -11.50143 | -44.97144 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0becbec5-7fee-3d8e-b4ca-b90b28788604 | -9.54413 | -47.76431 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 612351ba-0f9a-3586-a6c2-f73747c09057 | -9.62234 | -54.32184 | 2025-10-08 04:38:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e073892-be61-329a-87ca-7301fb6453e7 | -6.42369 | -47.24502 | 2025-10-08 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffad2f69-9a3e-3163-a4c8-19668a76b53a | -7.40705 | -45.17426 | 2025-10-08 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 670f0607-0f60-343d-adf3-bed0073293cf | -6.34695 | -46.32109 | 2025-10-08 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f729d137-2a0a-3289-9912-fed6dd024724 | -8.51712 | -46.29766 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3b581256-6eec-3a51-a05d-9657d2ef320f | -6.40463 | -44.72012 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8322323-eceb-3811-abcf-1a50967fa904 | -4.29502 | -44.70898 | 2025-10-08 04:38:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fc8432c-9e93-31d8-803c-bf839e746056 | -11.33613 | -44.88283 | 2025-10-08 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bebc09f3-12d0-3da8-a52f-74cac39b432e | -6.71164 | -42.15126 | 2025-10-08 04:38:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0d4f9bec-23b4-3c4f-ac2e-b3688b402377 | -10.401 | -45.36775 | 2025-10-08 04:38:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4c2dd9b-e561-3a5b-9ba9-9b406f5df33c | -10.89644 | -51.02243 | 2025-10-08 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c0531db2-890a-33b0-8c68-9e08b49aaaa0 | -11.1881 | -49.7776 | 2025-10-08 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc9af493-eadf-315f-8f23-a9ae85451e4c | -5.8469 | -43.41265 | 2025-10-08 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 33f74628-b0e4-341a-8ea1-5e5fc1b07c19 | -5.25748 | -44.13552 | 2025-10-08 04:38:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fed3efd6-aa28-35a2-9c4c-b8d7b8740868 | -8.57951 | -44.33809 | 2025-10-08 04:38:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f9d97f4-756c-3289-9b81-942e6aa9a04e | -11.81071 | -45.13652 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49701bd6-1324-3e02-a817-26ea99a72dea | -8.51776 | -46.2933 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32918210-c068-3078-8972-43ce34efab71 | -5.48588 | -44.61863 | 2025-10-08 04:38:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fc79820-47c5-3bc4-abb3-4f7ec6be5688 | -8.11355 | -47.25608 | 2025-10-08 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3986bbef-c9b3-34c0-afc1-d189429e4993 | -7.02724 | -49.5229 | 2025-10-08 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36053c64-5eca-3b4b-8c06-211b0d8c1643 | -7.35625 | -43.86738 | 2025-10-08 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2ccd68a3-b4fa-3455-8e78-c40299030c1d | -6.4615 | -44.57704 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e538674-b725-3cca-af35-acf3feccff59 | -5.15304 | -46.09529 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| af4ba4c0-91f4-3b6f-a455-1b9eca25a793 | -4.85586 | -45.79475 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f12e9065-fadd-3db9-9e2a-46f189baa0a8 | -5.30077 | -45.85017 | 2025-10-08 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 522dd255-a82a-360c-86f6-654c8edb629c | -10.89255 | -51.02542 | 2025-10-08 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b49de790-dfce-3c72-9e4d-0508944ca606 | -3.41351 | -51.23516 | 2025-10-08 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e12b957-08d8-3a0a-baef-f4aa5d5086b9 | -5.02253 | -50.99986 | 2025-10-08 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82a52aa7-9252-30fd-814f-ce3f792821e6 | -6.00359 | -43.75487 | 2025-10-08 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README66.md)
