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
| a504a6b9-5436-3e03-a4e6-2e05f018c0e5 | -5.2883 | -45.2744 | 2026-09-14 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 7c9a402c-d291-3804-9c14-7e0c9fd7d521 | -6.3015 | -59.9387 | 2026-09-14 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| cc030caa-0cbc-3df5-8f36-5cac8e283db5 | -6.3197 | -59.9764 | 2026-09-14 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| c939864f-64e5-39a1-97fa-d2118e0bd9e5 | -10.0716 | -48.7957 | 2026-09-14 00:00:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 533daac1-4316-3777-bdd9-1ca70d73a64c | -5.8021 | -53.8061 | 2026-09-14 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| d9b863b4-1e0b-373c-85a1-e7927b4ec5cd | -2.6784 | -57.5504 | 2026-09-14 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 63007df2-804d-3bef-a888-02bb81912b08 | -10.433 | -48.6474 | 2026-09-14 00:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 78e98c45-3f20-387f-9519-741cd465d8b1 | -6.2917 | -55.2695 | 2026-09-14 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| cf392b73-8ebd-3790-af2f-f5b5cd8e27e7 | -5.0872 | -56.2526 | 2026-09-14 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| b9c4fac4-c9c4-32e5-93c5-bfb682f41789 | -5.8206 | -53.8052 | 2026-09-14 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9e885c94-2ba1-3dcd-845c-4e608e5163f1 | -3.728 | -61.7555 | 2026-09-14 00:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 4203ebf1-fd1f-3613-b262-25d638a1b2ca | -4.1334 | -60.6692 | 2026-09-14 00:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 710fde83-194e-3de4-a1fe-c4d2a3aa8c88 | -4.1333 | -60.6882 | 2026-09-14 00:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| e4ed1394-89af-3583-b6fe-06e4e9f512c6 | -12.1589 | -45.5621 | 2026-09-14 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| ef549003-789c-3e6f-96e6-c4e26d4585fe | -6.5837 | -58.8498 | 2026-09-14 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 23ace887-e68b-3ee3-a819-28fc24707f23 | -6.5836 | -58.8691 | 2026-09-14 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 9cd02539-6a57-3f14-9661-96db9eee13e4 | -5.2885 | -45.2518 | 2026-09-14 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 680629fa-5c48-3786-a53d-9c34b65fcc94 | -9.4325 | -50.1299 | 2026-09-14 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| db184cf4-6ce2-37c9-bd75-6e2565942a25 | -6.2831 | -59.9394 | 2026-09-14 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 6b7cc2ff-2861-31e5-a870-a8b563088cb3 | -6.2832 | -59.9202 | 2026-09-14 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1934a582-14e3-31f9-b646-4037df61ac41 | -5.1255 | -55.955 | 2026-09-14 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| c97c5c4f-29af-3e75-a32a-97f170a71774 | -4.115 | -60.6886 | 2026-09-14 00:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 6fa20690-3730-3a19-9580-4fd43017b6d6 | -6.6021 | -58.849 | 2026-09-14 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 014b4227-0ff5-3116-bbf8-a7a545239275 | -6.2916 | -55.2895 | 2026-09-14 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ec9c8b5f-2455-3872-89ee-26c416d4e208 | -10.0719 | -48.7739 | 2026-09-14 00:00:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 891fa62d-f539-3965-9b7c-9cdc0af1ad6d | -6.3014 | -59.9579 | 2026-09-14 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 43121b6f-6b7e-304e-8bef-66b873a4f6ac | -4.8562 | -48.3667 | 2026-09-14 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 409a6611-d6ae-3e3b-ae8f-fb3fe7689c5b | -6.5838 | -58.8304 | 2026-09-14 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2e239256-8e31-36ee-9196-074337f0e6a9 | -5.2885 | -45.2518 | 2026-09-14 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| a445b693-926b-3083-867b-16fd6caf48b7 | -5.1255 | -55.955 | 2026-09-14 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 45f04910-69a1-3823-ba0c-ead405719ad7 | -9.4129 | -50.1957 | 2026-09-14 00:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 601331f6-f6d8-3cdc-8ee2-e9b95a5d13a7 | -6.3197 | -59.9764 | 2026-09-14 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| f19bdb6c-6530-301d-9950-3e97bf09efbf | -12.1589 | -45.5621 | 2026-09-14 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 0b46e5af-e2b3-3a31-ac9a-27ca620e3f05 | -3.1816 | -61.1235 | 2026-09-14 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 3dd0cfc9-e489-3b10-9466-4b31bca26326 | -5.8021 | -53.8061 | 2026-09-14 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f6f8f16a-4e86-3675-8f3f-122b555df28d | -6.2916 | -55.2895 | 2026-09-14 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 284ae6dd-d228-3270-aba8-9c14c51d9f5b | -6.3014 | -59.9579 | 2026-09-14 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 09f3a337-3b3f-301d-af3a-983e8f52aca7 | -3.4089 | -58.2142 | 2026-09-14 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| c0db4f31-2a07-331c-a176-02392daca5bf | -5.8206 | -53.8052 | 2026-09-14 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| b0095862-093e-3ddc-9c76-aedc2e1f6055 | -6.2917 | -55.2695 | 2026-09-14 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| e86deb8b-c27f-3e85-84c2-6308d67c8252 | -6.3015 | -59.9387 | 2026-09-14 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 345173ea-b9c1-343b-abd0-78d0868d739f | -4.1333 | -60.6882 | 2026-09-14 00:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 95fd3fe0-d191-318f-9ff6-816a06216785 | -6.5838 | -58.8304 | 2026-09-14 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 12efcd58-815a-3596-a150-651d7e68c73d | -6.6021 | -58.849 | 2026-09-14 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 095c2680-ef0c-3a85-a7bb-bd7908fc8235 | -5.2883 | -45.2744 | 2026-09-14 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 5f2509b2-f918-3110-b56f-4d2e2751c045 | -9.4325 | -50.1299 | 2026-09-14 00:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 8fcf2d5c-3687-3c26-9fc2-db45cd48f35d | -6.2831 | -59.9394 | 2026-09-14 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| cb182d7d-5b30-34fb-b136-e02e88756b5f | -6.5837 | -58.8498 | 2026-09-14 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 3eaa2da7-12c5-33e7-91b1-aa39b37a64c5 | -4.115 | -60.6886 | 2026-09-14 00:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| c181fd04-d660-36da-ab7f-ac5fd50dcd41 | -9.4132 | -50.1744 | 2026-09-14 00:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| e0e3d3b5-4544-37c5-8581-546e42ca417b | -3.728 | -61.7555 | 2026-09-14 00:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 12c28445-e440-3506-bb60-a528266b7b45 | -2.6784 | -57.5504 | 2026-09-14 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| af9a8ef5-d48e-3d76-88e0-fee057f66210 | -12.4901 | -41.4012 | 2026-09-14 00:10:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 1723a7ee-3732-3352-8afa-438442247a49 | -10.66 | -54.19 | 2026-09-14 00:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8e5db7d-e855-314a-bd80-f8ec1224d363 | -10.66 | -54.12 | 2026-09-14 00:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6296c343-46c6-3788-bd35-3c14e2c63481 | -2.88 | -50.4 | 2026-09-14 00:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2189380-8854-3bde-b4c6-43a22eb4bbf4 | -10.69 | -54.2 | 2026-09-14 00:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 632ff6bf-8906-3d37-b9c7-ef937eb68b46 | -10.69 | -54.13 | 2026-09-14 00:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c47719f-17f6-3d99-aca4-cd0108d6f114 | -2.94 | -50.4 | 2026-09-14 00:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5a6c81c-9d3a-3804-a808-80c89bf4d60b | -2.91 | -50.45 | 2026-09-14 00:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83833355-54c3-3cbb-b855-2701fe11de14 | -2.91 | -50.4 | 2026-09-14 00:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffc8ff73-ccad-32f4-8582-f98d30a42efb | -2.91 | -50.35 | 2026-09-14 00:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c1467f5-0fc8-3a8a-a5ae-8a04c616a6ac | -2.88 | -50.45 | 2026-09-14 00:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51102f85-b9e6-3356-91fa-e0c1ea47f882 | -6.3014 | -59.9579 | 2026-09-14 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f286fd76-c73e-3d70-ba28-ba8b079df7fc | -4.115 | -60.6886 | 2026-09-14 00:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 5b82f837-d19f-38b1-9c10-8a924bdc0e69 | -3.1816 | -61.1235 | 2026-09-14 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| f72625f0-1437-3065-8754-d6fb4d2addda | -9.4325 | -50.1299 | 2026-09-14 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 773a9a83-1d46-37a0-9c34-87c59eeaf2b3 | -11.2265 | -46.4215 | 2026-09-14 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 8fcc0709-0eff-3f85-9dc3-6285f2277545 | -6.5838 | -58.8304 | 2026-09-14 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ce08ca1c-debd-3fc2-9de9-6bd6c6ac9ed1 | -6.1111 | -57.6645 | 2026-09-14 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 6ad3ff0e-da47-39a9-a1b3-d073304f54b8 | -9.4132 | -50.1744 | 2026-09-14 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 00d420e8-e41b-31fe-b46b-37f5c5f97417 | -9.4129 | -50.1957 | 2026-09-14 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| b533e4a7-37ea-377d-8fa6-ac4641e7739d | -6.6021 | -58.849 | 2026-09-14 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 9972677f-80d5-3c33-9325-b3200b243bfd | -11.2074 | -46.424 | 2026-09-14 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| bf5b7559-2eca-3780-9ef5-2a831a3242c1 | -5.2885 | -45.2518 | 2026-09-14 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 948406df-69da-373c-8242-ead2ef1b5083 | -6.3197 | -59.9764 | 2026-09-14 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| da1182cf-fb3c-325a-91f6-2dd9bfddf366 | -3.4089 | -58.2142 | 2026-09-14 00:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| eca509ec-7a90-309a-bbe8-1991f9bf32ba | -5.8206 | -53.8052 | 2026-09-14 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 79558ef3-15bb-387a-8a6e-fd753d96e5e0 | -12.4901 | -41.4012 | 2026-09-14 00:20:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 9ae8b726-4824-38f3-8f07-0b0d669a8fab | -4.1333 | -60.6882 | 2026-09-14 00:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 4ef779b9-5730-3642-94d6-c29ac78ff59e | -5.1255 | -55.955 | 2026-09-14 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 60ef7716-3d25-30f7-adc4-4d3721e3b5e9 | -6.5837 | -58.8498 | 2026-09-14 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 28e31ade-8e62-3b77-bbc3-d8387b06967f | -3.728 | -61.7555 | 2026-09-14 00:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 76b1f989-11db-3b1d-b61e-8fc136b040df | -6.2917 | -55.2695 | 2026-09-14 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e61c8447-aa7a-369c-8037-fc0556febb7f | -5.8021 | -53.8061 | 2026-09-14 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 1d962b72-8c64-36c8-a0f1-093b09654802 | -6.2831 | -59.9394 | 2026-09-14 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| aa715128-482c-3ec9-b941-3c072f7fd188 | -6.1109 | -57.684 | 2026-09-14 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| ab7a7b4a-37ed-3ddc-a394-ad5703fd6fa0 | -6.3015 | -59.9387 | 2026-09-14 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 59c6d4fb-1d94-3093-b85d-56045fcc5ef0 | -5.2883 | -45.2744 | 2026-09-14 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f9639290-f360-3835-b3d7-3d1a266e25ed | -6.8446 | -55.5611 | 2026-09-14 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 09ab332f-7d4c-34ba-b759-d12c5b99bf3b | -6.2916 | -55.2895 | 2026-09-14 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4b96c05c-a433-3066-b6f8-09da32364331 | -6.6021 | -58.849 | 2026-09-14 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 83758150-036c-37df-a6cf-a0e0cc32dd4b | -6.2917 | -55.2695 | 2026-09-14 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9f098b92-7a9c-3907-a97d-0f87243c8f5e | -12.4901 | -41.4012 | 2026-09-14 00:30:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 56.6 |
| 119e9165-2ebc-3d9c-92b3-ee1759db3134 | -5.1255 | -55.955 | 2026-09-14 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| b5e3c5d6-9cb5-3b47-b7ce-4f627306f1b6 | -6.2831 | -59.9394 | 2026-09-14 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| cddce6c0-4f0b-3aef-8c56-53ada792dcb5 | -2.6784 | -57.5504 | 2026-09-14 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 113f4f51-5780-3ccb-bb77-a6c81b5ba1c2 | -4.115 | -60.6886 | 2026-09-14 00:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 9225972e-204d-37cf-b6a3-8e920b90ad7c | -5.2883 | -45.2744 | 2026-09-14 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 0fb4e291-3675-390f-97c3-d6f23e828f37 | -5.8206 | -53.8052 | 2026-09-14 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |


[Clique aqui para ver as próximas entradas](README2.md)
