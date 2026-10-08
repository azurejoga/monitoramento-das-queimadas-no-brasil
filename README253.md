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

## Dados Diários - Página 253

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8b17957-024e-3d69-902b-a2ee103ff726 | -3.8567 | -55.9769 | 2026-10-08 15:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| cf0ea9e9-9597-3ece-b5e0-961a85a3a4cd | -2.7613 | -54.0941 | 2026-10-08 15:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 177.9 |
| b4ee10d0-91fe-377e-bff6-8f5f901b3ee2 | -3.354 | -58.1961 | 2026-10-08 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 6d39808c-d4c0-34f3-ac50-96013cd77961 | -11.2661 | -45.1859 | 2026-10-08 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| a399e67c-f0ae-33a7-9b00-cbb7a228ef51 | -2.7515 | -57.6074 | 2026-10-08 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 4de93acb-115c-399d-88b7-f127acc75215 | -3.2268 | -57.8696 | 2026-10-08 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 4ed04100-19d7-303c-9f8a-3bd79cf6f569 | -2.4942 | -58.0768 | 2026-10-08 15:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 18775cbe-7631-3a0a-a970-8458676d964f | -2.7979 | -54.1134 | 2026-10-08 15:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 796a60b3-a5d1-3d5c-bcc2-170eedae7b82 | -1.3264 | -56.398 | 2026-10-08 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e114d9f7-4fc8-363f-b95e-f10aef54c0f3 | -8.6106 | -67.0486 | 2026-10-08 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 344.0 |
| 2828e609-e2ea-3139-99db-c2fa50fae034 | 1.6568 | -55.8045 | 2026-10-08 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 35db89b7-97cf-3245-8684-cbaf3094818e | -2.4428 | -56.5399 | 2026-10-08 15:50:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 7f3e44d2-2536-3929-b25e-62e02a812924 | -2.572 | -56.1646 | 2026-10-08 15:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 92e1a8cb-edcf-3ea4-befd-3412dc5575de | -3.0447 | -57.4851 | 2026-10-08 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| f8a703ab-faf4-33cb-b483-9611708bce14 | -3.3172 | -58.2355 | 2026-10-08 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5c35f262-3bf2-33dc-b34d-2f61fdbbc3d5 | -2.9449 | -54.1099 | 2026-10-08 15:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e9cf70bd-c82f-335d-ac9d-8f431433b886 | -12.232 | -44.7194 | 2026-10-08 15:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 321.4 |
| 0a6e34ee-b31b-37fb-9525-e0ce5f42d210 | -11.2295 | -46.2403 | 2026-10-08 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 88327d9f-9240-3e84-af48-944ef5d66d2d | -2.7332 | -57.6077 | 2026-10-08 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| cb8cb5c4-0151-338e-891f-099a9deb47b6 | -3.0631 | -57.4847 | 2026-10-08 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 9ca9f15a-66af-3288-a4f8-542a6fb4e8b6 | -2.572 | -56.1842 | 2026-10-08 15:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 8439675f-3f5a-3432-ba30-9ce08682cc36 | -9.5003 | -66.8017 | 2026-10-08 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 178.9 |
| 598a8405-8b04-38b1-b845-eea93556ee83 | -8.9501 | -45.1334 | 2026-10-08 15:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 417.9 |
| 578f6b69-aa19-3236-a157-edf8f6a043f9 | -7.1998 | -55.1226 | 2026-10-08 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 1d386660-bc12-3bc1-a797-463ed681bace | -1.6213 | -55.1321 | 2026-10-08 15:50:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 1a7c604e-cc30-3876-9678-9a1efa47d71a | -5.75 | -41.7294 | 2026-10-08 15:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 285.3 |
| c8ad2154-9a86-3ca2-acb2-b9a08d079572 | -2.6052 | -57.5711 | 2026-10-08 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 351a4faa-804d-307c-8d72-6d95d5253d75 | -3.0074 | -57.7384 | 2026-10-08 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 744a9092-ef7a-3678-b4d8-a2dec2c8b515 | 1.7672 | -55.5463 | 2026-10-08 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 83c6e425-1d7b-3297-ad73-5f666761ec7c | -1.3277 | -55.4327 | 2026-10-08 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| de49526f-ac72-3ac8-b242-02f3fa91b0f9 | 1.5466 | -56.0028 | 2026-10-08 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 647d3ca2-7999-3bc0-b668-d827b0028778 | -3.0192 | -53.887 | 2026-10-08 15:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 227afd74-382d-32d3-9eb7-2e47a5af51dc | -2.788 | -57.6261 | 2026-10-08 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 63f4f679-ff59-364d-99c6-47dc69500564 | -9.4819 | -66.7836 | 2026-10-08 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 4d41def4-e3d0-3f8a-8a84-9a8857b53b24 | 3.5448 | -51.2772 | 2026-10-08 15:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 2527bb75-ed5f-3b4c-8612-825cd1c3f833 | -1.4118 | -48.9318 | 2026-10-08 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6c8b9079-5063-32c1-b38a-c6482eeebec4 | -3.6446 | -58.9416 | 2026-10-08 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 3ea4ed7e-0ff1-3e44-8b0b-843773e927c4 | -12.4825 | -62.6124 | 2026-10-08 15:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ab038c7c-3b46-3823-a331-b9edcd23846b | -9.479 | -67.4897 | 2026-10-08 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 7076d6d3-e84e-36d9-aef5-628bfffb0d8f | -2.3115 | -57.9829 | 2026-10-08 15:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 187.4 |
| 50238c7d-d50f-3fbf-b1a3-05e2bfd5801a | -12.1948 | -44.6554 | 2026-10-08 15:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| fb8f80ca-bb1d-3491-9a7c-15f8084e91aa | -2.9819 | -54.0287 | 2026-10-08 15:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| fb399f18-b466-3bf6-8d47-5582aac6f2e9 | 1.5649 | -56.0026 | 2026-10-08 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 7d2d75f3-168e-32b8-81df-d83fc39af226 | -2.4805 | -56.1269 | 2026-10-08 15:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 69390f54-1a52-32a1-b585-f3003cd5f805 | -3.2451 | -57.8693 | 2026-10-08 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 789c3133-a420-3208-95e7-daa517e98cf7 | -2.0447 | -54.3085 | 2026-10-08 15:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 7ac69deb-4785-33df-9404-d658beaf0de8 | -2.2222 | -56.9348 | 2026-10-08 15:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 152fa707-b081-3689-ac56-34cdd89a0c91 | -0.3952 | -51.9947 | 2026-10-08 15:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 63d8410c-7588-3e0e-ba25-79067bd54a4c | -2.8713 | -54.1518 | 2026-10-08 15:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 049ad905-0906-3924-a7c7-a86562db1ed0 | 1.5283 | -56.003 | 2026-10-08 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 314a739d-64b5-3ece-bfbf-1a56e4bc54e4 | -2.8897 | -54.1514 | 2026-10-08 15:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bfd36e1c-086a-3f81-8395-464742558d4a | -3.332 | -59.466 | 2026-10-08 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 63ddea8a-c5d3-3158-9bae-36b24655819f | -3.8383 | -55.9774 | 2026-10-08 15:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| a23ec0e1-68a1-33ba-ba2c-04f77e335314 | -12.1922 | -44.7953 | 2026-10-08 15:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| e094a09f-2398-344f-a2c0-17a7a72e616a | -8.5921 | -67.0491 | 2026-10-08 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 39f7d304-6d01-33b7-81aa-20522b1c6ace | -2.4989 | -56.1069 | 2026-10-08 15:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| becf8bce-a13e-3bc9-a40f-2eabbe0fd938 | -2.8938 | -59.2251 | 2026-10-08 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 90001d83-c83e-3716-bac1-226642277060 | -2.8434 | -57.4696 | 2026-10-08 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 137.0 |
| b16d62b3-871e-38b5-9f88-5dd7d3be6747 | -10.9575 | -45.389 | 2026-10-08 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| b75aecc9-2bd2-3ae7-a568-4723d81896c1 | -2.8247 | -57.606 | 2026-10-08 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 84e6d126-e659-3129-b97c-7428d894496b | -2.4623 | -56.0879 | 2026-10-08 15:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7d01cfc6-18bc-3393-a9c2-dd0134788762 | -2.9082 | -54.1108 | 2026-10-08 15:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| c0dbf083-1391-39b4-a9b2-f9a88faa1781 | -2.853 | -54.1322 | 2026-10-08 15:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 457c7428-80ce-37f8-84ac-71a825d55297 | -6.6901 | -45.3519 | 2026-10-08 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 146.0 |
| b83eb372-1892-30d3-8230-02518387320f | -0.4136 | -51.9946 | 2026-10-08 15:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 56.2 |
| e865247a-0abf-37da-bf72-09d73e997350 | -9.519 | -66.7639 | 2026-10-08 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ee50a539-202c-381e-84f0-319fa3903e7d | 2.1511 | -55.9552 | 2026-10-08 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| df33aa31-a3b8-32af-a891-a732b32454c5 | -3.2085 | -57.87 | 2026-10-08 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 116.7 |
| a094aaff-eb94-302a-b6f8-695d018fabf2 | -3.6439 | -59.1721 | 2026-10-08 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1ab701e0-4256-3b18-b27b-b1c53f092391 | -2.4804 | -56.1466 | 2026-10-08 15:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| db18d108-b731-3077-919f-d8323c7d4771 | -3.188 | -58.6241 | 2026-10-08 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 357a5064-8f41-30dd-a00e-b2f6d27c5849 | -3.1697 | -58.6244 | 2026-10-08 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 203.2 |
| 2e27ac03-0e12-39e4-a756-9a4893f704ad | -2.8164 | -54.0929 | 2026-10-08 16:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 469cb0a1-24b8-3fc1-9c6c-d143e674d0a8 | -2.8938 | -59.2251 | 2026-10-08 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 29bfe58d-38ff-3e59-b731-d93d1355e4df | 3.5448 | -51.2772 | 2026-10-08 16:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 21f45c58-7b6b-3b2c-919c-af34f85a6d6e | 1.6385 | -55.8047 | 2026-10-08 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d0a77eed-032a-3379-8b32-dbc89f841b48 | -9.4818 | -66.8022 | 2026-10-08 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2ea3347f-0e7e-3ee1-b0bf-57b616228226 | -2.9264 | -54.1706 | 2026-10-08 16:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| dde70e2d-f804-389e-a26f-db91529a86dd | -5.8597 | -53.479 | 2026-10-08 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| def69712-7fbd-3d9a-a26d-34b5a149007b | -12.1738 | -44.7517 | 2026-10-08 16:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 7ad4cc09-5022-32b6-94ac-405397efd634 | -2.788 | -57.6261 | 2026-10-08 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| e2b8320f-26b4-389f-92a6-7ff8c5727a88 | 1.6568 | -55.8045 | 2026-10-08 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4b017592-6cc1-35b0-a40e-60026e218db7 | -9.7689 | -64.9992 | 2026-10-08 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 602c7c32-7bd2-3f9e-ac5d-855668e95325 | -8.6106 | -67.0486 | 2026-10-08 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 428.1 |
| e308d2db-f8ce-3baa-8795-d0fc6bc3de50 | -5.7319 | -41.6589 | 2026-10-08 16:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 174.7 |
| f4aed808-3689-3a90-99e1-6df9dd11facf | -2.8247 | -57.606 | 2026-10-08 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 7fb8da39-2017-3d1e-a006-c14bd622a82c | -9.8061 | -64.9979 | 2026-10-08 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 4f24c13a-5a4d-3f00-a7a2-e3b3b42d3702 | -8.5733 | -67.1422 | 2026-10-08 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 27dddfd5-7359-3988-bd59-7cfd7ceab73e | -1.2082 | -49.2539 | 2026-10-08 16:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 8196e032-622b-35b6-9a65-4af620c3c690 | -1.6213 | -55.1321 | 2026-10-08 16:00:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 147beaca-239d-37ed-afc0-ba02d5f250c7 | -3.2085 | -57.87 | 2026-10-08 16:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 131.8 |
| f39482de-7fbe-3f09-a3c7-97e379490ca8 | -9.479 | -67.4897 | 2026-10-08 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ec4a12be-e689-31ab-b2d0-09b882b53d12 | -2.8897 | -54.1514 | 2026-10-08 16:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 3d37b361-15b5-3ecd-ab9f-7ab2d379dd00 | -2.6052 | -57.5711 | 2026-10-08 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 49f5f5bd-923e-3a12-b8c5-323ab6c1e774 | -2.998 | -54.7492 | 2026-10-08 16:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7a864db1-bdb3-35c6-b431-030ad198368c | -9.8434 | -64.9777 | 2026-10-08 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 63aaa851-892d-38ce-a565-76b8b2f54ad8 | -3.0799 | -58.0083 | 2026-10-08 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 75cdccd3-1e95-39ab-83d0-ffda57e27881 | -5.7321 | -41.6349 | 2026-10-08 16:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 198.6 |
| 1fbb0edc-c8f5-3428-8f60-1b116d1c4f06 | 1.7672 | -55.5463 | 2026-10-08 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| b29bc2fc-bae0-31a1-9a9f-8e46eff1bafe | -2.0447 | -54.3085 | 2026-10-08 16:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |


[Clique aqui para ver as próximas entradas](README254.md)
