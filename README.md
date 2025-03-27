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
| 2d8fe195-da9d-39a1-bfe3-47234043da48 | 3.9845 | -61.5054 | 2025-03-27 00:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 08de19e7-0675-3864-b0dc-f776c2598386 | 3.9662 | -61.5058 | 2025-03-27 00:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| cd06efe4-4743-3925-8870-b2a89f6fafa8 | 2.032 | -61.1013 | 2025-03-27 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 3ec3a266-2a80-37bd-867d-3c6ccb73096c | 1.8317 | -60.8765 | 2025-03-27 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 8205163b-db11-3ab5-a84a-bd00147c11fd | 3.9662 | -61.5246 | 2025-03-27 00:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 955b1413-d23c-33e5-8fc4-9b4597fdace4 | 1.8317 | -60.8765 | 2025-03-27 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.9 |
| cf5041ac-ed01-3043-84d4-189c07d79204 | 3.9662 | -61.5058 | 2025-03-27 00:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 92.8 |
| f0d3aa9a-6f98-3f24-b015-400ed5d24922 | 3.9662 | -61.5246 | 2025-03-27 00:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 8b52e4c6-bc77-3dc0-9ce9-db9211f83df9 | 2.032 | -61.1013 | 2025-03-27 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9ab4a02c-4ee8-393e-b8a6-4d190f975f7a | 3.9845 | -61.5054 | 2025-03-27 00:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2d45e796-5e8a-3bcf-b397-a2520a1a339e | -21.7007 | -50.3721 | 2025-03-27 00:20:00 | GOES-16 | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| 2d6c124f-d7b6-3c2c-9f5c-ce6b4ff8356c | 3.9662 | -61.5058 | 2025-03-27 00:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e5ddaba8-e955-32c5-8a2b-44de0ab8dcda | 3.9662 | -61.5246 | 2025-03-27 00:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 4b28b6bc-0c82-3125-b116-4aba5c3cb814 | 2.032 | -61.1013 | 2025-03-27 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ca7c8df2-374f-3c94-a18b-e16fa660be75 | 3.9845 | -61.5054 | 2025-03-27 00:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 44f69e71-d2f5-3e06-82f2-6124cceb3776 | -21.69953 | -50.38732 | 2025-03-27 00:20:00 | TERRA_M-M | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.2 |
| c2b2e5d6-780f-3e00-909b-6020f12a325f | -21.69254 | -50.35225 | 2025-03-27 00:20:00 | TERRA_M-M | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.6 |
| 8e34b8ab-cd7a-3023-86d1-1e9c2401a070 | -21.69636 | -50.34674 | 2025-03-27 00:20:00 | TERRA_M-M | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| a87646d3-9b05-31d3-b9e9-949bd6e01a92 | -21.69596 | -50.39284 | 2025-03-27 00:20:00 | TERRA_M-M | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 41.8 |
| e60367d1-ca41-35b7-a7a6-aa0e4d81b067 | -13.26481 | -43.02351 | 2025-03-27 00:22:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 8e61e51e-50dc-3d10-bc9c-ae9235d2826f | -10.69282 | -40.42907 | 2025-03-27 00:22:00 | TERRA_M-M | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d5d7ddcf-014c-3057-94f2-bf558285987d | -13.25575 | -43.02481 | 2025-03-27 00:22:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 2b88fc12-138a-35de-ae48-8dbaa2971431 | -12.2654 | -42.09634 | 2025-03-27 00:22:00 | TERRA_M-M | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2bd41c79-df6e-3991-ad7a-1c7bc54cef28 | -8.10782 | -43.12898 | 2025-03-27 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| bc048fc7-29ab-3b58-be92-0e97f3af7093 | -7.3783 | -41.41283 | 2025-03-27 00:24:00 | TERRA_M-M | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 00b82ac6-3fc6-3362-9646-fe1d894b86c2 | -7.90271 | -43.9184 | 2025-03-27 00:24:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c3bfd92e-fc72-3b45-9861-627190b7089b | -7.07325 | -44.38149 | 2025-03-27 00:24:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 97a5e576-9cb4-38d6-bd96-89dd49847851 | -9.15593 | -43.12232 | 2025-03-27 00:24:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b835a44e-fa11-350c-9a78-c201ddad09b0 | -7.37694 | -41.40338 | 2025-03-27 00:24:00 | TERRA_M-M | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 2cfb782a-7762-3232-902f-4f5d5fe6ca8f | -8.3786 | -43.96526 | 2025-03-27 00:24:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 13c1040e-603b-3253-814a-7d5de49c56f9 | -8.09896 | -43.13025 | 2025-03-27 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 697772fa-f989-381b-97a6-7870e190222e | -8.37736 | -43.956 | 2025-03-27 00:24:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2b438ce-2359-3dcf-abf5-e96b1354c67e | -7.23757 | -44.77919 | 2025-03-27 00:24:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c9451c64-e519-3f06-bb12-29718fc78957 | -8.11914 | -43.14555 | 2025-03-27 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b1a91b57-f033-323f-9505-caebcb402122 | -9.15717 | -43.13129 | 2025-03-27 00:24:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 45730e1b-b788-3072-bb2e-aa02f50a518e | -8.37933 | -44.03723 | 2025-03-27 00:24:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c690a883-8efd-3c3a-896d-06392f0f5bc5 | -7.06417 | -44.38275 | 2025-03-27 00:24:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a6d5c908-23e0-31ba-a373-f0c97f37f1e8 | 3.9845 | -61.5243 | 2025-03-27 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 45.3 |
| b6981bc1-9244-3446-85a5-d2f675632f0a | 2.032 | -61.1013 | 2025-03-27 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a094d7d7-bd08-361a-98d0-8a3ab7c77a94 | 3.9662 | -61.5058 | 2025-03-27 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 49869a58-a35e-3e7a-809a-d3d1325d9650 | 3.9662 | -61.5246 | 2025-03-27 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 261eabac-751b-3a42-870d-742c4563ead0 | 4.0575 | -61.5605 | 2025-03-27 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 36.9 |
| c0d72374-ceb3-3bc9-9ec0-553ae7041f00 | 3.9845 | -61.5054 | 2025-03-27 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5d79767e-f526-338d-b8be-e6e137eeacc1 | 3.9662 | -61.5058 | 2025-03-27 00:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 4207bef8-3f01-343a-930e-ab68d047bd37 | 2.032 | -61.1013 | 2025-03-27 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d27d0b52-e105-3d97-b0f5-9cd14f284278 | 2.032 | -61.1013 | 2025-03-27 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| d064b37a-cc5c-3aef-89f4-350e085e45c7 | 2.032 | -61.1013 | 2025-03-27 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f7750cbe-5351-355f-81bb-dd934e8fa597 | -4.6126 | -43.2528 | 2025-03-27 01:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 672b5b79-262a-3968-9a0d-df8454403837 | 2.032 | -61.1013 | 2025-03-27 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ec9f0765-0ac6-30af-a50f-c50934038826 | 3.9662 | -61.5058 | 2025-03-27 02:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 36.9 |
| c690adcb-32df-3715-b44c-2dd0a5fdd4a2 | -7.22281 | -35.79177 | 2025-03-27 03:04:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| da9df09c-b2d0-364d-a588-7f3bcb1a1b2f | -8.38995 | -35.02799 | 2025-03-27 03:04:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6f21c3dd-a667-3dd0-9216-1f84d1600fbe | -7.37681 | -34.88725 | 2025-03-27 03:04:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e34d701b-b4b9-393e-8473-2eca1d2d55b2 | -10.50213 | -36.79612 | 2025-03-27 03:06:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 76fb9765-006a-3fe8-bbcc-f815df788f75 | -14.05486 | -41.64297 | 2025-03-27 03:06:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 88153660-375e-3ed7-a21c-786e60428cea | -9.28522 | -40.40495 | 2025-03-27 03:06:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9472ebfa-b80e-39d3-aef3-40559d34b75e | -10.28618 | -38.11715 | 2025-03-27 03:06:00 | NOAA-21 | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 84582002-9a33-3194-8f1a-f8402f0e7da4 | -11.29065 | -38.49099 | 2025-03-27 03:06:00 | NOAA-21 | NOVA SOURE | BAHIA | Brasil | 2922904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1fcdc0f2-5c6f-3f10-b92b-2153d725a8fb | -12.3991 | -40.93742 | 2025-03-27 03:06:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 6519a170-b8b3-33e5-a0df-36fb037ab11c | -10.43056 | -40.50612 | 2025-03-27 03:06:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8cc8be3d-daa9-36be-b1ef-8eaff9fc88a6 | -10.82563 | -37.16641 | 2025-03-27 03:06:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 51950cac-9881-339f-b99e-82266f8ad163 | -17.76858 | -42.79544 | 2025-03-27 03:08:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0f831f3d-f088-3517-b043-86b630682fcd | -3.93671 | -41.4877 | 2025-03-27 03:28:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 96a8158c-49d2-3a5c-bb51-b5611c25f4bc | -3.93705 | -41.488 | 2025-03-27 03:28:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2f821254-3ab5-3a77-a26a-8331c6b55438 | -3.93604 | -41.49168 | 2025-03-27 03:28:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f496c478-d206-301c-9e9f-ff03770ee3c3 | -3.93636 | -41.49197 | 2025-03-27 03:28:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| edfac3a1-ae22-384f-84fd-863ef53c98f8 | -10.43296 | -43.33926 | 2025-03-27 03:30:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4348fc39-e421-3dca-97db-25937a1a8712 | -10.52228 | -37.73888 | 2025-03-27 03:30:00 | NPP-375D | PINHÃO | SERGIPE | Brasil | 2805208 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 916999ef-6e02-37c9-94f6-5bcdf1b43a2a | -11.25363 | -41.90558 | 2025-03-27 03:30:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| db713803-0b72-3e4f-a4ad-b214c65f317c | -10.43876 | -43.34032 | 2025-03-27 03:30:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ea9b44f8-cc37-3ca8-8cf7-64ab92089d29 | -9.49675 | -36.89954 | 2025-03-27 03:30:00 | NPP-375D | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a914901b-f451-3209-85c1-cf3021998e56 | -11.28171 | -37.27817 | 2025-03-27 03:30:00 | NPP-375D | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 61a2a5dc-90b4-38de-ab96-8072ead68e7c | -10.43801 | -43.34427 | 2025-03-27 03:30:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 35da99a0-f389-3116-a87f-989a35dfef43 | -10.52096 | -37.73896 | 2025-03-27 03:30:00 | NPP-375D | PINHÃO | SERGIPE | Brasil | 2805208 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 33199bfd-699f-3d89-a4ee-a49274e61933 | -10.69229 | -40.42625 | 2025-03-27 03:30:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4949686f-1e7c-3d92-b8d7-9b89c0a34e58 | -10.34777 | -38.47341 | 2025-03-27 03:30:00 | NPP-375D | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b5f13abd-19f0-3a00-a45e-3322d33c4e44 | -8.39107 | -35.02373 | 2025-03-27 03:30:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2f9724a3-3ae6-3a7d-aa7b-857035f0e5b4 | -7.07017 | -44.38331 | 2025-03-27 03:30:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7edfe187-4c73-3320-9545-2415d537cb13 | -7.22065 | -35.79253 | 2025-03-27 03:30:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0f5fab6b-c288-3450-aa17-67ddda58eb95 | -7.23552 | -44.78046 | 2025-03-27 03:30:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 590df226-d7fe-368d-b87f-d8e8bf8a95fe | -7.2366 | -44.77474 | 2025-03-27 03:30:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd5bf826-b119-3c46-b163-57226019b4ca | -7.07116 | -44.37807 | 2025-03-27 03:30:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88e58d3e-324c-3caa-b45c-8a79a2bd4baa | -7.06362 | -44.3822 | 2025-03-27 03:30:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14ed18d9-e271-326a-b79d-96b7ac68ae3b | -13.20607 | -40.49692 | 2025-03-27 03:32:00 | NPP-375D | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dabb285e-b722-3fc3-b15d-6e9340250941 | -21.69925 | -50.36895 | 2025-03-27 03:34:00 | NPP-375D | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2cc18d06-18fc-3060-a4ac-f59629135047 | -21.83108 | -47.0339 | 2025-03-27 03:34:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cadd04f5-35d1-3cec-86e3-353345c8865b | -25.1912 | -49.32896 | 2025-03-27 03:34:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| aa216c81-4260-300b-9ee6-2130802a6d0c | -21.83002 | -47.03848 | 2025-03-27 03:34:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48047d56-f6a0-36c8-8430-cf7e11d98b93 | -25.19866 | -49.32566 | 2025-03-27 03:34:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cf8a584f-5689-36f1-bc19-ff2815b91b4e | -21.69234 | -50.36669 | 2025-03-27 03:34:00 | NPP-375D | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 322b20bf-7c18-3cad-9793-fd02cd4777b5 | -7.31241 | -39.27491 | 2025-03-27 03:51:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2fac2741-7458-349b-bb77-5bbbb47b2893 | -5.57371 | -39.53868 | 2025-03-27 03:51:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ceb08e1c-0523-3a01-bb63-e1324f79d2fa | -7.23427 | -44.7789 | 2025-03-27 03:51:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7db225a-a62b-32bd-861b-f6d19f96d1e8 | -7.47359 | -37.32031 | 2025-03-27 03:51:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 53582b57-c1e1-3d46-b75b-5f185cd7d8e8 | -8.75716 | -35.23694 | 2025-03-27 03:51:00 | NOAA-20 | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2f81e70e-31e6-3e97-8961-9444a4ede4e6 | -7.06792 | -44.38149 | 2025-03-27 03:51:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65c276c5-4837-391d-86d7-bd8d86aad564 | -4.61122 | -43.14714 | 2025-03-27 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa11c169-d7c9-3ede-8775-bb572234e1b8 | -6.53797 | -39.4237 | 2025-03-27 03:51:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0e77df3e-f544-3fc1-93dc-67e74a9dcc51 | -5.63171 | -44.32258 | 2025-03-27 03:51:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0d21c25-15e9-35a7-8da2-c418612fbaa4 | -7.06293 | -44.3848 | 2025-03-27 03:51:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README2.md)
