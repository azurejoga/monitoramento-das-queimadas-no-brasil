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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36199410-a3d1-3951-ba0a-37b6a8c294b6 | -3.90162 | -47.00439 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8802c603-18f7-3dff-99bc-be01a3e0a003 | -4.04133 | -49.76926 | 2024-12-23 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1bc14af-d6a4-3a8c-ae35-0f59145d323f | -1.82878 | -45.72671 | 2024-12-23 04:31:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9231f06-965b-3b6b-b2a1-0666b22e0f54 | -3.94966 | -46.76279 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2401a1d6-71cf-37c9-a72a-0748d29b845a | -2.65319 | -51.86841 | 2024-12-23 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 046a14b1-ec42-3e8b-9e15-a9dfdd439924 | -4.01836 | -46.91238 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d1fb9a9-c811-308a-b207-c1db0f5458d7 | -4.77683 | -46.3825 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a238e0c2-3757-3164-8685-55acacfaf4e7 | -3.80109 | -46.72213 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e51e9489-b551-3b8e-b64f-c1440bca6b15 | -3.83714 | -46.68846 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aae7d0e2-767f-3e99-ae4f-62c9e9de0d3b | -4.07937 | -46.80137 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 585d4169-1412-380b-9a81-1bb6672742dd | -3.91399 | -46.67173 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1b9a7aa-927c-3923-aeef-a3e4cf61727c | -3.92215 | -46.35653 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bef24320-2174-3b26-a32f-ae6f5678a29d | -2.62491 | -46.11662 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a62b5153-00f2-3ea2-8120-76fdbbfd777e | -2.63688 | -45.68882 | 2024-12-23 04:31:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5d4ac1e-9f40-38f9-9d15-2c06f6734e8b | -3.50641 | -47.19804 | 2024-12-23 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f3276f4b-c05d-30cd-99d5-2f3580725e95 | -5.9296 | -45.48868 | 2024-12-23 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3e37d30-5be0-320f-a2b7-d3919c9cce01 | -0.21391 | -51.59755 | 2024-12-23 04:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f9f8ea3-b565-3e00-bcb1-0dee1150852a | -3.7324 | -50.25166 | 2024-12-23 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e01a0379-8ef2-3dff-bd3a-b0f008f258ce | -3.90658 | -46.99452 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95e50896-0f25-3bde-b372-928b0766d3e3 | -3.9138 | -46.36604 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bfaf0aa-8b7d-35cf-bee9-3b565f43066d | -3.54042 | -43.59062 | 2024-12-23 04:31:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0fa6ff9-5ac4-3f9d-bc51-f1ea90205a68 | -4.7808 | -46.40135 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df8e4dd7-ccc0-3686-a97c-1c2fee6bdbd4 | -1.63409 | -45.85203 | 2024-12-23 04:31:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4ab9bc5-72a5-339e-b286-2347f85b2001 | 0.15119 | -51.12088 | 2024-12-23 04:31:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 378e4f23-79db-3808-b60b-33f852c0a869 | -3.92015 | -46.90781 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44633d95-9e4c-3e5e-8f30-c88871d4c5a3 | -3.92526 | -46.94055 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c96435c5-bc6d-3ea8-81f7-0fc61565ee78 | -3.9207 | -46.90434 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfbca139-657c-39cd-8176-c67d0cd7528d | -3.91968 | -46.9326 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32b1763e-e9b2-36ba-a1a1-8483aecb52ea | -3.68682 | -52.48525 | 2024-12-23 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a840c7c-33d5-3385-9d4a-8a8b63f5c0af | -2.94009 | -53.05553 | 2024-12-23 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1fe8ebda-33a4-358a-9545-df7f9d44adc4 | -3.97955 | -46.92057 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c84c2e4-e3ae-3765-a207-b42eec196be9 | -4.09999 | -46.82236 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2106e5e2-a597-326d-b939-06d9db26dc40 | -5.81736 | -35.47915 | 2024-12-23 04:31:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 93b4dc29-efd7-3a7a-b7e9-4f449211af80 | -4.08659 | -46.79893 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e99f18e-69b9-39da-b235-e0dd28b0757c | -4.76954 | -46.38499 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6518d902-2f99-3877-8ff6-0ad205fceaec | -4.32847 | -44.1964 | 2024-12-23 04:31:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| df8b4e1a-1a20-3663-98a6-be5645e95fa6 | -4.27848 | -55.73973 | 2024-12-23 04:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0a2a4f3-b927-3814-b923-08b34b6891a4 | -4.04839 | -47.02073 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6572c0a3-689e-379c-a87d-cab9ba01fd0b | -4.15472 | -43.65824 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d808608-08e9-3e3f-ac5d-a9ba23e5f53f | -2.72295 | -46.18274 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c66286f-e518-38d1-bebe-6ea0c65d1709 | -4.48087 | -45.42792 | 2024-12-23 04:31:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c01d7d0e-6f67-3450-bc8f-9369aec7a0b8 | -4.05692 | -47.09658 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72420d99-d447-323d-9ad7-0e5bf09c9054 | -3.17853 | -45.97335 | 2024-12-23 04:31:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25ac9e5e-4c49-3eb1-afd0-48d99b403c9d | -3.98116 | -48.90188 | 2024-12-23 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08734592-57cd-39e5-ab29-a4ef089687f8 | -3.92457 | -46.90138 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5c581b0-c8c3-3123-98a8-e1450d6d01c4 | -2.44174 | -51.78922 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c116c57c-d615-3a10-8fa4-6f08fef773df | -4.77572 | -46.38964 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c68929a7-2e74-37bf-a1f1-6403de8d7b57 | -3.91663 | -47.01735 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd1489b4-9b47-306e-a03f-fa96a1fe1ef7 | -4.45137 | -45.30754 | 2024-12-23 04:31:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc4e2878-d3f8-3a24-b782-cb47cd30ef8d | -3.03997 | -52.71144 | 2024-12-23 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01e22f74-f13d-3420-b3f0-74d32964deb8 | -3.00457 | -48.12572 | 2024-12-23 04:31:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1b023d8-cf09-3306-911c-20b4346434e6 | -5.35286 | -46.22002 | 2024-12-23 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea125e52-ec3b-3244-948e-faf391d4e47f | -2.56236 | -45.56336 | 2024-12-23 04:31:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0db7ee78-3afa-3c27-a8c4-810e0576d8bd | -2.26544 | -46.3944 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61a3e515-1086-3936-bbc9-7e175beb11f5 | -3.91465 | -46.92117 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28ad5528-24c9-314a-8fab-6f3ad1c9f6a9 | -3.8659 | -46.58546 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 597ed372-ecf0-30b3-ad73-74947a270b0e | -4.02422 | -46.91389 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a53238ee-cad1-381e-b1e7-eb05abfb4b1f | -2.98263 | -54.12438 | 2024-12-23 04:31:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de0c4821-1552-36bc-8c62-72454a4238d8 | -5.3557 | -46.22417 | 2024-12-23 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 727f9988-b71a-3d6d-bff8-ca3bbda6dbd0 | -4.05638 | -47.10004 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dd2b399-f54b-34d0-84db-0e614f1bc98d | -3.99456 | -46.93359 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6b74f8b-9e78-3e43-a8f4-40bfd3a8b063 | -3.94836 | -46.88018 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc971153-7ba5-3002-80ec-c8dea8122bd3 | -4.37201 | -46.26947 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 006b7210-b04f-3329-ad86-6e69ca743628 | -3.80475 | -46.85089 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44864907-a598-3dda-9ac0-33a3c2cf6a5e | -4.0591 | -47.08273 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c35b17b-5d22-3e09-a2a7-c4e693a0fb52 | -3.93224 | -46.358 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 629cf5ed-1ab2-32db-a19b-e3bef915f133 | -4.14583 | -43.66609 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 67d6fa48-ec00-3499-ba7d-5e4002ff8d09 | -4.16055 | -43.64528 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b3a6d319-ac0a-3b17-8bfa-ca7cc05f81a1 | -3.91907 | -46.91475 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dd0198c-9083-3fd4-8178-f58d102182c3 | -4.77688 | -46.40435 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41ad2acb-2f2c-371d-866f-ef9ec91b095e | -3.80831 | -46.7197 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c384c662-b773-378a-8e22-d6fdd03ce22e | -3.8388 | -46.67796 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c42499a-fc6a-358d-a4a1-280c55d07562 | -1.98651 | -52.06661 | 2024-12-23 04:31:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e43a2b77-97d7-3d4d-bdb0-6d3d29a6d3e3 | -3.75079 | -47.19361 | 2024-12-23 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c9c5679-302a-32b8-94cc-3cf2395c3ae0 | -2.26878 | -46.39491 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6f588b40-6bf4-36a3-b89f-d2616a1f4dc4 | -3.80251 | -46.84343 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2905bc9d-31b8-3e0f-b3fa-7ec15ccd5bf9 | -3.90719 | -47.01234 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4696c094-8d31-3912-bba4-eb05819498de | -6.90831 | -43.53574 | 2024-12-23 04:31:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4e99b21c-04b4-36dd-bd29-a75690e3530f | -2.73874 | -46.87265 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 547079c0-dda9-3854-82e3-36f84041a1af | -3.98792 | -46.73661 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4940f06-a70e-3234-b463-13ecd41d116d | -7.38435 | -35.2665 | 2024-12-23 04:31:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 09f059fd-e363-3d4d-8560-3835309a55f2 | -4.03569 | -47.03651 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56854839-2d3b-30f2-af96-d81d6249de8d | -2.61935 | -46.96367 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d345931-9e06-30e4-98ca-6edc6a4252a6 | -4.23131 | -43.78633 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05a67f8a-9c0d-3efe-b397-8fcac80f6fea | -2.12994 | -50.69963 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e277001f-4210-3a15-9cdc-6a75677de9f1 | -3.97833 | -46.68867 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7acda577-08ef-31da-b848-33f2be4008d3 | -4.03751 | -46.79074 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d51f434d-26e1-3727-808f-f61483c18c4c | -4.15235 | -43.64861 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2f98d1c0-100a-3e3e-9f96-f335125c8b2b | -4.95391 | -44.00452 | 2024-12-23 04:31:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d240393-cdc5-3086-be44-6c46f8739ac2 | -5.44947 | -44.8114 | 2024-12-23 04:31:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f2a8941-8aa1-3674-bc9e-832b5191003f | -4.10776 | -46.81641 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4f521d0-e8d1-33b9-8489-51db412c92e3 | -3.09554 | -46.56588 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| faa6d450-bbc4-327f-8dad-98cd22512217 | -3.97105 | -46.66963 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98a40550-6a58-36e8-8a38-535d36ad5e14 | -4.04893 | -49.76656 | 2024-12-23 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 224f5630-6080-39d2-890d-c6e1e6f7cacc | -3.09721 | -54.55106 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddf4eecc-a0d1-360c-8714-fcc5d7f330e6 | -3.80995 | -46.70924 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2db93e47-498f-35bb-a74c-b9a8456c4e91 | -2.63766 | -46.97712 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bba35d11-174d-3b01-af75-d20939052e1b | -1.09605 | -53.66786 | 2024-12-23 04:31:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49acc241-5560-3593-943e-3eca5552d194 | -3.92124 | -46.90086 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7cf1714-84e8-3985-84fd-e1e5437dc822 | -3.29455 | -45.61126 | 2024-12-23 04:31:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README14.md)
