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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 138019f6-e712-3a1a-93af-8f0d80055c6d | -10.5535 | -57.4567 | 2026-09-16 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| efc50c5a-5fad-3ca4-9886-b2466a450588 | -11.9906 | -52.4695 | 2026-09-16 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| cc205db2-f005-31c5-8c8d-c91aaad9c2be | -6.8412 | -58.9746 | 2026-09-16 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9a4ab674-33d5-32e0-98db-987f94ed0eab | -3.4278 | -58.0009 | 2026-09-16 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| b35b3704-922d-3906-82c2-65a0a84f8ec4 | -9.7608 | -60.4561 | 2026-09-16 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7d276dff-eb84-3b59-9972-a83a8d22a257 | -3.2752 | -54.2622 | 2026-09-16 15:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 60170c3e-9588-3cd2-b53a-6db02d504a52 | -6.1609 | -52.7496 | 2026-09-16 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 0f8d9c24-e8d4-361d-b336-a26df086b684 | -13.5652 | -51.8656 | 2026-09-16 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 00de8d27-b601-3815-ad3f-3ab3cdb47255 | -9.0962 | -65.9384 | 2026-09-16 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b064d85c-1927-35ec-bdc9-a1879a4c7a0a | -8.6311 | -66.5287 | 2026-09-16 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| e4f3a058-b5a8-3977-9892-e43e731ec3de | -9.3569 | -50.1583 | 2026-09-16 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 56aae77a-dab7-37a3-bc9c-0725a580d322 | -8.6181 | -44.528 | 2026-09-16 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 7e3388a5-ef9f-3cfa-8407-554c2ad31f42 | -11.0247 | -49.6656 | 2026-09-16 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 5490fcea-9d85-380f-90b5-22b13ea993a8 | -6.2731 | -55.2904 | 2026-09-16 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 953f400a-f459-3c0e-8b01-eab3cc04f148 | -9.7322 | -64.9067 | 2026-09-16 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 175.5 |
| d47f41a7-3b5a-35a1-9a20-62fe23f48bab | -3.1697 | -58.6437 | 2026-09-16 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| ec207149-8246-367a-975f-eb17b2ea1945 | -10.7015 | -54.1663 | 2026-09-16 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| c2cf4025-60c4-3084-b1dc-fac97c906f68 | -12.2131 | -52.8637 | 2026-09-16 15:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 44188cdd-2caf-3acb-9482-d288a4a4bee0 | -8.0192 | -54.8333 | 2026-09-16 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| baf76204-12d9-3541-9203-6f22c70b2017 | -9.0309 | -61.0314 | 2026-09-16 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 075bfa9a-a4b4-3f23-8212-914e006a3cef | -8.6493 | -66.6025 | 2026-09-16 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| c26e0a34-c612-31db-bc66-17cb4dd846d0 | 0.1747 | -51.4805 | 2026-09-16 15:30:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 87125431-051e-3f80-a23d-adee9db0ffac | -9.031 | -61.0122 | 2026-09-16 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 3647f033-7de4-3ca4-81f7-da1d781974a6 | -3.4462 | -57.9812 | 2026-09-16 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 4d4bc5d9-76cb-3cbd-8728-0ce7347f90d1 | -11.9734 | -49.7705 | 2026-09-16 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 83340739-5012-358a-ab5f-c7ad11d553b2 | -6.8411 | -58.9939 | 2026-09-16 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 38dccd8d-4787-3a46-92cf-19f8f3c86f35 | -14.2796 | -51.7097 | 2026-09-16 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| b27ab660-20c1-3f0c-9c93-2eb741f73884 | -13.2874 | -51.2618 | 2026-09-16 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 24d1e7df-fcaa-3240-b47d-9edf838b749e | -6.8226 | -58.9947 | 2026-09-16 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 5406c00e-e237-3358-8764-708bcdc96169 | -3.3183 | -57.8677 | 2026-09-16 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| c051fcc9-522f-3d67-92dc-c5810464cfd9 | 1.2058 | -50.7894 | 2026-09-16 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b07a1c56-7ef7-39ae-bfb6-8d99b9cd47b8 | -9.1337 | -65.844 | 2026-09-16 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 8b30a4c0-4b68-3b84-a708-e6453ba91190 | -10.8571 | -50.8183 | 2026-09-16 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| c40a2346-71fc-38ff-8d7f-a5982db4899f | -8.5428 | -44.5132 | 2026-09-16 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 446.5 |
| a62d265f-ffd0-3fe7-ae74-8390812fbdeb | -8.5989 | -44.5531 | 2026-09-16 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 407.5 |
| ff0262c1-7943-304d-b461-82d107623edf | -8.6188 | -44.4819 | 2026-09-16 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 762ba007-e54f-321f-b48a-03829386e0ef | -13.5841 | -51.8845 | 2026-09-16 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ef1024a6-d0bc-30f8-aca7-7ae5854bbef0 | -14.2016 | -51.7627 | 2026-09-16 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f16fbb93-c5b8-3427-8d65-bacf0c9d6fd4 | -9.8099 | -45.8759 | 2026-09-16 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 326.8 |
| 5496b354-5cce-31d7-9bec-1fbdbaab32d5 | -11.6972 | -54.5672 | 2026-09-16 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 644a40c9-a7cf-3492-b3a2-e1c84c28c49c | -15.6557 | -52.7366 | 2026-09-16 15:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8bdbbb6e-68b6-3f71-a905-fd0dbdba126f | -3.2568 | -54.2627 | 2026-09-16 15:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 56058063-12b0-399b-a246-bb4906dbb2d5 | -9.7979 | -60.4734 | 2026-09-16 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a64f67c7-2851-350c-967d-a1dfc1549e9a | -14.1822 | -51.7653 | 2026-09-16 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 6f0b11a4-5fca-3dbf-b039-ec5391664baa | -10.0104 | -52.1217 | 2026-09-16 15:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 5cc6aafd-eacc-3895-bac9-1caac30fa6ca | -8.6184 | -44.5049 | 2026-09-16 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 260.7 |
| 04299850-951e-35e1-9dcb-5561c032ceae | -13.4499 | -51.8799 | 2026-09-16 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 6507b332-6b7e-3ae8-ad69-43cf916b23b6 | -12.12 | -57.1967 | 2026-09-16 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 01baee1e-75ee-386f-9dcb-9b147c67d755 | -8.8456 | -45.8939 | 2026-09-16 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 158.9 |
| b060f6f8-e886-3eb9-ba29-5f885965d242 | -9.8552 | -60.2966 | 2026-09-16 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 0ee43d98-3237-3f45-a74f-7d810d04d981 | 1.0767 | -50.9572 | 2026-09-16 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 8918b5ca-435d-30d3-9233-756905598abd | -13.3202 | -51.5986 | 2026-09-16 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 469699b8-741c-39f2-bf99-a8a504450fa3 | -11.2677 | -54.1361 | 2026-09-16 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 1d4e9b6e-509d-3367-9ec6-136f2b6f1128 | -11.2488 | -54.1378 | 2026-09-16 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b22bf0f2-0231-35d8-ba44-9ec5543489a2 | -13.5844 | -51.8632 | 2026-09-16 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 63b9a3c7-f18c-3fd6-bfc1-cda20e6587eb | -10.3766 | -58.3171 | 2026-09-16 15:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| e0e5ef4f-1b0e-3bb5-9ecf-90c6276f1850 | -10.3955 | -58.2962 | 2026-09-16 15:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 5d1296e0-0cd4-3a85-8a56-055252b23eb4 | -6.2732 | -55.2704 | 2026-09-16 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e74a26d5-eabe-3e36-96c6-a84017009b6c | -8.2052 | -54.8416 | 2026-09-16 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 8c4d368c-6834-3471-9e8f-fe450609ee46 | -9.7909 | -45.8782 | 2026-09-16 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 50d6ac46-0986-3bb7-9d96-5fa7cd99be5b | -10.3953 | -58.3159 | 2026-09-16 15:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| e61bac94-28ab-3281-88cb-7e6f513cddca | -3.1514 | -58.644 | 2026-09-16 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 0c40f76d-261c-3a41-a17b-2e83490f1266 | -10.4772 | -50.9634 | 2026-09-16 15:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 3d4acbe6-1b50-3980-8c80-5392cf79eb99 | -8.6178 | -44.5511 | 2026-09-16 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 260.0 |
| cde30baa-f4f5-3e01-970f-82ef0e6c1df4 | -2.6785 | -57.5115 | 2026-09-16 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 76adadaf-f154-3a44-97e9-a030ef3c028c | -6.1362 | -59.8871 | 2026-09-16 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 316e06a2-2513-3d2b-9dd5-ea782cfac6f2 | -3.68 | -54.1706 | 2026-09-16 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 380fefcc-f554-3d0f-ad95-45c2e9124f5a | -11.2302 | -54.119 | 2026-09-16 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8cd4d6a7-8b68-34e6-9224-b35b09ef01b3 | -8.9239 | -63.3371 | 2026-09-16 15:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 422266b9-0fd1-33e0-bc7f-460052b088f2 | -13.395 | -51.7169 | 2026-09-16 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b9d4ad05-bd84-39c9-b58e-e40dddb84044 | -13.3387 | -51.6389 | 2026-09-16 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| cb986eca-80d1-30be-9245-b3b227971e8f | -10.331 | -45.2883 | 2026-09-16 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 58e3b5ad-b31f-3f34-b97d-4a2a76fab7f7 | 4.1316 | -61.2378 | 2026-09-16 15:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| a52cacd2-9f51-32ce-bb5c-eaee4ff39110 | -12.6628 | -50.8264 | 2026-09-16 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| dfe85a1e-47ad-3340-ace9-eaf7d4b9d7ad | -8.9601 | -44.3973 | 2026-09-16 15:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 80e7b474-b8b8-3b50-9071-c8a5a426b8a2 | -2.6968 | -57.5307 | 2026-09-16 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| afef58f3-3b89-3e74-854c-4ded006ac6cf | -9.1725 | -59.4241 | 2026-09-16 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 5ec16382-5e56-3ff3-bf58-d0b086a6b94b | -3.1174 | -57.6779 | 2026-09-16 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| b1b25725-dcdb-307c-9fca-ec2781a77f58 | -8.7949 | -46.9069 | 2026-09-16 15:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| e2975a33-8963-31ab-b3a6-016e79f28e1d | -10.5535 | -57.4567 | 2026-09-16 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 19bf2722-67b5-3295-ae98-df32b733ec43 | -10.0293 | -52.12 | 2026-09-16 15:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 4d25e101-bc48-3654-890a-a10202583303 | -12.1265 | -44.199 | 2026-09-16 15:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 0ece3560-e3fc-3070-8bc9-ff603d6cc63f | -9.7793 | -60.4744 | 2026-09-16 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| a6a62a36-c7f1-3dba-aa6c-912c0220525e | -5.2023 | -49.3348 | 2026-09-16 15:30:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7bacb081-fc5a-3356-8c36-99fc6152d2bf | -13.6337 | -45.9732 | 2026-09-16 15:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 163.0 |
| a02930f2-de81-3b89-a55a-87c9ba7a59a1 | -15.5588 | -53.8266 | 2026-09-16 15:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 57e31a9f-5585-305c-a3b0-952944026fc0 | -8.6493 | -66.5839 | 2026-09-16 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ae74cea6-0b94-3f7f-ab99-3f7b81e9f1dd | -11.2113 | -54.1208 | 2026-09-16 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| b89ba041-9e3c-31d5-b7ff-d9d66e260332 | -7.7992 | -66.9203 | 2026-09-16 15:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 04c70787-a2ad-3d0e-ad96-9a9e2a546168 | -7.0058 | -59.2382 | 2026-09-16 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 05760a1f-04c9-3bb4-b928-5279b023530c | -15.5786 | -53.8031 | 2026-09-16 15:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4efa1555-b7d9-353c-a891-f0cc18797b25 | -9.1337 | -65.8253 | 2026-09-16 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 74708e8f-d346-35c8-9652-b1034da38a5e | -10.876 | -50.8163 | 2026-09-16 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 5d84b067-5bad-3635-8466-8c3290aa388c | -10.7013 | -54.1868 | 2026-09-16 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 13f9b1ca-0127-355b-a256-97fc48cd1f4d | -8.411 | -54.7274 | 2026-09-16 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f89270cb-e62c-3bff-a5af-a0c6b24c0521 | -15.5592 | -53.8056 | 2026-09-16 15:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5dcd3013-2c55-3e23-bce3-508cf0d9b288 | -6.1178 | -59.8877 | 2026-09-16 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 3cf968d6-a7fc-38a7-b574-eb749e979c81 | -8.8585 | -44.9149 | 2026-09-16 15:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 391.1 |
| 3c27d823-ff1b-3160-9d69-2c47ff440a8e | -2.7331 | -57.6271 | 2026-09-16 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d5ebe492-8820-3f22-9695-45b08157fe86 | -13.3391 | -51.6176 | 2026-09-16 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |


[Clique aqui para ver as próximas entradas](README84.md)
