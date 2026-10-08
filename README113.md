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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2195e73-8068-392e-88bd-5ab7d19f60cb | -5.88055 | -45.96276 | 2026-10-08 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 757f1196-7b3a-3d15-a67c-5c754c6be512 | -4.37559 | -55.45035 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42307078-756f-3cb6-a55a-3d30fd68ff0a | -4.6019 | -56.07879 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d257d045-0348-31ab-9564-cf714de62e72 | -3.00255 | -54.1214 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29565e1e-5cb6-30c6-a573-eca82907d060 | -3.00164 | -54.10333 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 32ab4271-7010-3064-a37a-23b8255b30d5 | -7.38072 | -47.61122 | 2026-10-08 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ae80a358-b05d-3b55-bb2d-00ef04cbd5a2 | -3.03557 | -54.10413 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d8959de1-e55a-3a2f-94d4-9fa59522eaaa | -7.4223 | -48.36156 | 2026-10-08 04:46:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1345037a-3f31-3e15-bb7e-ea6981e301fc | -3.18092 | -54.10642 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75d24b3c-559b-3a60-9b17-d598b56a8947 | -8.52803 | -46.92043 | 2026-10-08 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dcde8ef-cdc7-363c-ab1a-503045c2edbe | -8.74094 | -45.15738 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f1072daf-82a6-37ff-9df6-0c99200fa962 | -2.82553 | -54.10549 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3021d39d-021e-3f41-8d5b-20344b7862fe | -10.98077 | -45.4024 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cedcd39d-f06b-34b1-85ac-e85a6de715bc | -4.08435 | -55.33587 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d120738-56c8-3fe1-be9c-44bb0c324365 | -6.1642 | -52.66003 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83970817-99d4-3adf-bfb9-95f9ee2515df | -3.27824 | -54.06358 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c791ccc-5599-3989-8db2-80c7779e7c59 | -3.30722 | -54.04454 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dc46d243-5af6-36ed-b834-c8823151d6cc | -3.30792 | -54.04024 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 229139c0-45f8-33ff-bd2f-8e3f58921725 | -10.48025 | -47.22788 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 225b006e-da34-3562-b20a-5a89e9a22de2 | -8.28607 | -45.71162 | 2026-10-08 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60ee8170-c286-3042-bccf-63027f1fe510 | -3.55962 | -59.46714 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ff8d08e-3d55-3a2a-815a-da3af03ff4a7 | -7.19318 | -46.53058 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb5bcdc0-c66e-3d04-a16a-6a8a5a1f09cf | -5.6755 | -46.34906 | 2026-10-08 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7ebf9ef-fb07-31a3-89e3-640ae6abde3b | -3.09237 | -53.93413 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f958707f-c4c5-304e-be04-582f434339d7 | -8.21983 | -46.33253 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 05808aa3-da20-3358-b54f-421c6ea24f00 | -3.03265 | -53.90868 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cb86be2-2f70-339a-a73c-2d01319225c5 | -4.14023 | -54.25365 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfff8fb2-d862-3862-8a94-b8cdc7d893a0 | -3.95318 | -56.10988 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 05846516-bbe3-38c6-9680-aad30ae8b993 | -3.04482 | -53.95006 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1ec9b1da-c690-3517-a925-ce0de264a7d2 | -4.14248 | -54.90784 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4cb7554a-9f95-3bab-ac0b-8d96cc4b34cb | -2.77972 | -56.50942 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c69536e-2183-33ff-86bd-2683e597d5ab | -3.00064 | -57.75999 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2d7778f-276a-3037-a6d4-2c14a4d980de | -3.27592 | -54.05433 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9a6347c-feee-393a-a862-c59ccbe72284 | -4.05857 | -55.3216 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42faf65c-7891-38e0-a880-ffd302d01b25 | -3.96142 | -56.11126 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85e5d5e1-bb70-37d6-955d-2c49823146ae | -3.27699 | -54.02358 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eafb158f-7426-3777-94be-270c67172646 | -3.10236 | -53.75042 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc361724-581c-39b5-bbc6-117f6421a220 | -3.28397 | -53.83703 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c03b82d0-4211-3277-925e-3ebecd77fa38 | -7.07122 | -40.93991 | 2026-10-08 04:46:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 052a8884-4c12-38e4-8d74-6523ceb46448 | -5.28395 | -60.09112 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3aa82c4-4911-323b-82eb-422b59bc376b | -3.96876 | -51.90832 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 960aee3a-eaee-3300-9958-e64fc8648a57 | -3.64929 | -54.27714 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8329d990-06f1-3122-8875-c75d06022ab0 | -3.29075 | -51.56794 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1fad70e-b93e-328f-a74d-4ffb64b3d3c2 | -3.04712 | -53.95926 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 280.2 |
| 10cbfdfb-0c37-3bfd-b3ed-2667061e96db | -3.27662 | -54.07079 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09a2c3a6-0a0c-368b-bacb-35288c43c353 | -3.8472 | -55.9907 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db2f6a48-a545-3b72-9eaf-97641de30672 | -11.26868 | -45.19928 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 127ab249-f180-30e7-b483-b8967b490bdf | -2.71971 | -57.46726 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 78ba5142-7536-3ddc-a397-9f14411a11fc | -4.00044 | -51.01579 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5f07e3d-1168-349f-a658-4e6c5f65f669 | -3.0208 | -54.17385 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d62c6603-6419-34a2-ac77-cc7587bfca9b | -8.20702 | -46.3345 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c25df0c3-aab5-35af-bc3a-bc68ce23af55 | -3.29447 | -54.00728 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| adcca559-9603-3c62-9a64-801adb7e90d1 | -2.48977 | -56.10715 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22370a00-3b6a-3a15-ae44-ddad080dfe4a | -5.22549 | -60.23983 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec340a8b-ee83-37e0-a152-47358d219575 | -3.30077 | -54.06121 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8743b0b6-0fc1-3873-ab2c-10e73680fabd | -3.5822 | -54.31646 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30293fd7-39c8-382e-9af7-1cbab0f18b0a | -11.21421 | -44.865 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 117dad0a-2792-3411-a94b-b6c9b5fc9310 | -3.00925 | -54.12694 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c11e71fa-0a23-3308-861d-a0bcd24c91b7 | -5.96471 | -40.91829 | 2026-10-08 04:46:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d30df296-2d34-354b-aa87-9e4c7336cb4f | -2.93634 | -54.17885 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4cc5a90c-b8c5-3c14-872d-a2cfb35f9ae2 | -7.26249 | -45.34361 | 2026-10-08 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aec0b0da-c404-37ee-987b-61501d1841bf | -3.00555 | -54.12636 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c8fd3e7-9e49-3b82-97fb-af5fdf6b262c | -3.10631 | -53.77259 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f26e3d7f-fab4-3198-ab2b-b800aea6ad78 | -6.01152 | -53.52542 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2de12512-4cc8-3954-938d-14117e1cc350 | -6.48987 | -62.85783 | 2026-10-08 04:46:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c06c510-15d9-384b-b456-ec33f4aa5de9 | -4.92826 | -55.86825 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9fb273c-0504-38fc-84a9-a274f204a4c4 | -3.00791 | -54.06397 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 49fbfbef-19f2-3000-9b2e-07a5f78b9d7e | -11.00886 | -47.9697 | 2026-10-08 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bb92918-d7ff-33bc-a8d6-8a2099b772a6 | -6.68379 | -55.09553 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 43a0e31b-efde-34ad-beb2-45306028ee56 | -3.30295 | -54.67139 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bce82c4-f453-319e-b6ee-5c357262b32d | -2.98808 | -54.06985 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65ac9c66-aff9-3a6f-af06-40442f0d5de4 | -5.72865 | -41.76811 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fc71e0c1-9304-394b-b0d5-242d23b7c2f9 | -3.47257 | -59.50492 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 512d6d1b-a960-3936-abac-57a22b820fa9 | -11.71553 | -43.66209 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a80d3323-0b49-3190-8e86-801e452444bb | -7.44281 | -63.55054 | 2026-10-08 04:46:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 56b8a99b-b3e5-321f-8b6e-1fc57cc773d6 | -9.41043 | -49.0046 | 2026-10-08 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 848e5cdd-983b-39a9-91bd-c1ab7dc1a81d | -5.95547 | -46.3847 | 2026-10-08 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6db00dba-8b75-37f4-86fd-924a5df394fd | -2.86958 | -54.88056 | 2026-10-08 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 33b375fb-e3fb-3a8d-9226-1161b2233788 | -3.10459 | -53.76677 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60744493-52a4-3379-9b59-51ef3278634d | -2.80309 | -54.07947 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d46b4b0-8d10-3910-82e1-0e671f1ee145 | -5.72914 | -41.76463 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0e696bc7-bc34-3ea5-bb9b-2b94585d87cc | -3.38738 | -59.43099 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9f23ef8-94f4-324a-8032-b686d70aa87a | -3.69957 | -50.67251 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b52a845a-8b6e-3553-9b2a-96512a96e25f | -2.99616 | -54.06662 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3e532628-5fdb-30b5-9992-e90df1a539c2 | -9.95033 | -45.97166 | 2026-10-08 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 761bbfda-69f9-3f3f-a9e1-8f3a8ed67567 | -5.67403 | -46.35923 | 2026-10-08 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16d49310-da4b-3fb5-b7a2-96b74967a4ed | -5.91349 | -53.88376 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29234bfb-6d5a-378b-9bd7-16336343c9ec | -2.94433 | -54.06478 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e69a743-9c00-3e90-afbb-020bec7cbfa7 | -6.13564 | -47.93307 | 2026-10-08 04:46:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d26b1522-3ca7-3395-a446-334a8f34266d | -7.23305 | -55.17041 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1f763095-eb5b-3f8d-aadb-c9e9728d0aed | -3.01595 | -54.13249 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab20bfc7-f508-369a-95cc-d116f1130dfd | -6.31765 | -43.34359 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ba233cd7-f55e-347c-a57a-97d1b59165ab | -2.79129 | -54.08214 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae4cabfb-29fb-3f62-b212-43289c6003dd | -2.7809 | -54.076 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 163d3891-99b9-3f75-b0a9-5e046b445bcc | -3.02496 | -54.07556 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 54429d66-4b81-3ced-86aa-33aac2537182 | -6.16997 | -51.93641 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54c7bafe-53b0-3b4d-81b3-48493cce652c | -3.43742 | -56.93231 | 2026-10-08 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdc8b0e2-cce7-3617-ac84-8f250983c4a9 | -2.99158 | -54.04807 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1cf2804-4c0e-3969-a74d-900b61327fc6 | -3.02427 | -54.07993 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fec7f59f-09b5-3c3d-b398-11688805b16b | -6.11342 | -55.70883 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README114.md)
