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

## Dados Diários - Página 254

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b22c81b-2a3e-3386-a25c-0291165ac99e | -11.2661 | -45.1859 | 2026-10-08 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 0b038dd8-ea85-3af2-8ac8-43269a6ff8a8 | -9.4819 | -66.7836 | 2026-10-08 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 10b92423-3153-3eb5-a66b-c1d134a48b78 | -3.0002 | -54.0483 | 2026-10-08 16:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 241.1 |
| 4a22673a-bc77-3017-adbe-792d83be0def | -3.1697 | -58.6244 | 2026-10-08 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 200.1 |
| 937f7fe4-8927-3174-8aba-cbe3461d293e | -1.2086 | -49.0412 | 2026-10-08 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 7882139b-eaf7-34d8-9e8f-d43b0fde3ab2 | -2.8713 | -54.1518 | 2026-10-08 16:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 23e2ece6-e392-374d-b16d-35fc09b24523 | -3.3912 | -58.0017 | 2026-10-08 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 7948fddb-b10d-3e80-83ec-a178019e1389 | -9.4819 | -66.765 | 2026-10-08 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 5e9078ae-cf74-3cc6-bc0f-c571c05bdf50 | -3.0447 | -57.4851 | 2026-10-08 16:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 9682c8dc-57be-3625-8add-6a741eae7b99 | 1.5649 | -56.0026 | 2026-10-08 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 2840a245-6784-3129-9ca0-529c99759f0a | -3.0631 | -57.4847 | 2026-10-08 16:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 799036b3-47ea-3967-aa4c-332cfc4e5c3d | -12.1733 | -44.775 | 2026-10-08 16:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 33697d8e-7ca6-37d8-8316-1cb3979e7ea1 | -2.9082 | -54.1108 | 2026-10-08 16:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| eb17a873-de52-3cb3-8ac2-3c1a700c2cea | -8.9501 | -45.1334 | 2026-10-08 16:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 249.0 |
| 9ab8264e-e26e-309f-9813-463f776154c7 | -1.4118 | -48.9318 | 2026-10-08 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 70236ef9-6f49-3290-af17-73222a3bfc1a | -8.5367 | -67.032 | 2026-10-08 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 590a59f8-96a6-3a54-aebc-f59586401386 | -2.572 | -56.1646 | 2026-10-08 16:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 150.1 |
| e478bf7f-d166-396b-afe6-953f277208ca | -2.7332 | -57.6077 | 2026-10-08 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| a2964dab-c2b3-3be1-8f82-25cb0effcb1d | -3.8786 | -44.1265 | 2026-10-08 16:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| aa055ebc-efda-3278-91f0-d56776fc0718 | -12.1545 | -44.7547 | 2026-10-08 16:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 272.0 |
| 17a7a8e3-0ef2-3a08-855b-f219279f4133 | 1.1691 | -50.7481 | 2026-10-08 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 86b9513d-71c4-3da9-8d44-6d05486bd764 | -12.232 | -44.7194 | 2026-10-08 16:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| cfff6543-6d7b-34cf-86e3-cf5f43200c70 | 2.0895 | -50.9628 | 2026-10-08 16:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 1e4629f3-63e2-3596-8f1a-d9849489f098 | -6.6899 | -45.3746 | 2026-10-08 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 454ffc2a-8fb5-3089-a7d3-03118b93ff17 | -3.4095 | -58.0013 | 2026-10-08 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 4c9ed624-e59a-36db-af41-dfcaabccffc1 | -1.2082 | -49.2539 | 2026-10-08 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 359d80cc-8d83-3c6a-bc13-d061e3574567 | -2.7332 | -57.6077 | 2026-10-08 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 620527bf-4575-3473-b02b-b30ccc72b1e6 | -1.1161 | -49.1913 | 2026-10-08 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 6fbcf4bb-e93e-3a84-8d47-cb11ece97fd7 | -12.1545 | -44.7547 | 2026-10-08 16:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| b3d8c831-f0c8-3d7e-856d-1cfa0507bf10 | 3.5448 | -51.2772 | 2026-10-08 16:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 102.3 |
| cf3fcd92-0c6c-3d77-b50c-d3adc5310b02 | -2.8164 | -54.0929 | 2026-10-08 16:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b512568e-64a6-35e0-b0fc-183426a52366 | 1.6385 | -55.785 | 2026-10-08 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| eac10400-e9c0-3fba-acf8-0d90dfe40e6c | -5.8597 | -53.479 | 2026-10-08 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a49e5f42-c342-3bfd-8927-c3c0eb14d2bc | -9.8618 | -65.0146 | 2026-10-08 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| afa5db9e-15ef-3815-a491-412393fed29c | -3.095 | -59.1832 | 2026-10-08 16:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 9ce43403-9e30-320e-b1b5-97991211b834 | -9.0401 | -66.052 | 2026-10-08 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a1464367-db31-3bb3-95c9-7907d1f336f1 | -8.5733 | -67.1422 | 2026-10-08 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 74e02393-6357-3e9a-9768-7545935155fc | -8.9501 | -45.1334 | 2026-10-08 16:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 396.6 |
| ddee9eac-6511-3068-9732-2ae1badf65e9 | -6.6901 | -45.3519 | 2026-10-08 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 6f8df3fb-80d0-3d5a-bb73-00ce69c392a5 | -2.788 | -57.6261 | 2026-10-08 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e3cbf8ad-2937-3e22-b201-9d12e594fd20 | -2.8897 | -54.1514 | 2026-10-08 16:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 66b1dac4-cf59-35b5-984b-1fc69d4eaf33 | -12.232 | -44.7194 | 2026-10-08 16:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 53a09238-5b2a-3ddb-bcc9-349954e07147 | -1.3264 | -56.4176 | 2026-10-08 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 25518a1b-5cd2-35db-a1fc-7a0bf71d2fb1 | -9.4819 | -66.7836 | 2026-10-08 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 1b504bfa-53ac-38ef-b92f-5a8c834f2d15 | 3.2311 | -51.3079 | 2026-10-08 16:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 21332639-3619-3d02-b9b4-5dc985f5cdea | -9.7686 | -65.0556 | 2026-10-08 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.1 |
| a9f2707e-2927-3f6d-a615-44c01811a439 | -9.5003 | -66.8017 | 2026-10-08 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 204.8 |
| 65fb8620-dc55-3363-8774-f77f551f0a2f | -3.2085 | -57.87 | 2026-10-08 16:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 309a04dc-0438-3b5a-bbeb-11afd88a2177 | 3.5264 | -51.257 | 2026-10-08 16:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 80a67ffb-e36e-3968-b111-7f6060daefc7 | -2.6052 | -57.5711 | 2026-10-08 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| ee5069f8-1f57-36dd-ac9a-58e13ce9b6ba | -6.6899 | -45.3746 | 2026-10-08 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 150.3 |
| a5b31a5b-da4c-3c64-b90f-315d3b341390 | -2.998 | -54.7492 | 2026-10-08 16:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 887d4dbf-63c7-3f80-bfe9-cd8d383b51b3 | -9.0585 | -66.0887 | 2026-10-08 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 5d53e234-b6a3-3745-a94f-91d5d43dc0c9 | -2.4942 | -58.0768 | 2026-10-08 16:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 134.3 |
| b69701fd-3c91-35f7-a8f8-77be98223aa1 | -9.479 | -67.4897 | 2026-10-08 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6e9e5103-5d20-31a0-8519-44294b486ab0 | -9.8061 | -64.9979 | 2026-10-08 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| baca699b-2992-3675-85e0-22175b9ac0cb | -9.4818 | -66.8022 | 2026-10-08 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 9bc15fe9-0b8b-3156-9391-10fc86ccaf68 | -3.0447 | -57.4851 | 2026-10-08 16:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 7f965d28-12df-3bf5-bfc6-bce3879e8317 | -8.6105 | -67.0672 | 2026-10-08 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 9266318a-900b-3c3b-b9b4-6ecd36362293 | 3.508 | -51.2576 | 2026-10-08 16:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 312c3e20-fef4-3bcf-b80a-3c3d0a1efce5 | -7.2 | -55.1026 | 2026-10-08 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 7eba2d8e-db31-3919-8324-ae7beb250ec9 | -5.7312 | -41.7309 | 2026-10-08 16:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 3753b00d-0030-3923-9ecd-6ee6a56319e4 | -9.4819 | -66.765 | 2026-10-08 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 3b08357c-5e38-3e92-86c5-4f73f6511c2d | -2.572 | -56.1646 | 2026-10-08 16:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 610b7cfa-7e91-3c0d-b526-90ca6104cf55 | 1.9424 | -50.8824 | 2026-10-08 16:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 013682d2-adda-37c3-8089-9a292d5b3bed | -9.1326 | -66.0864 | 2026-10-08 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| bfbf1849-a976-3c38-aebf-da965830d148 | -3.0799 | -58.0083 | 2026-10-08 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b0cac9d3-c14d-3b2d-a171-c480f818341f | -22.23597 | -45.89772 | 2026-10-08 16:13:00 | NPP-375 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b2d20a52-35fa-3b77-94fb-b8b201745aab | -4.07 | -44.09 | 2026-10-08 16:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f0f58f0-0430-3c85-b822-99c9033ddae8 | -5.11 | -46.19 | 2026-10-08 16:15:00 | MSG-03 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cf441629-1842-3f46-9377-2903322c9c5e | -4.08 | -44.13 | 2026-10-08 16:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f73df936-b7ee-3694-91b2-7a460b4be50c | -2.73 | -54.08 | 2026-10-08 16:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baa5a519-873b-3bcb-955f-191123b4c52a | -5.97 | -40.93 | 2026-10-08 16:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9ed6ca3a-a6a9-3825-8d3a-576b3228bfc3 | -6.52 | -45.38 | 2026-10-08 16:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0cdd81a8-9c75-3aa2-af25-d593c8b06850 | -8.2 | -46.34 | 2026-10-08 16:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ef73feb-d9ca-3ae1-b074-9b5f78f757d1 | -3.0 | -54.04 | 2026-10-08 16:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16f8dc39-7c4b-3a9d-b59c-58701524dcd8 | -5.37 | -44.17 | 2026-10-08 16:15:00 | MSG-03 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f82a300-5cb7-3e65-bde1-ef7f1a316d04 | -8.2 | -46.43 | 2026-10-08 16:15:00 | MSG-03 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca4bd4cc-d3e6-3dd3-aa92-17892107e841 | -10.76 | -46.61 | 2026-10-08 16:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a509b3ea-eea9-3c5f-9dca-1bba47c41ca8 | -5.7 | -53.44 | 2026-10-08 16:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69d1c4ed-5f04-301e-93df-3faf3f0b5743 | -6.32 | -35.09 | 2026-10-08 16:15:00 | MSG-03 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0003e35-a281-3726-b366-2fca60c8705c | -2.76 | -54.08 | 2026-10-08 16:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 400ed553-86fd-31b0-99a3-737bb8276f14 | -4.1 | -44.09 | 2026-10-08 16:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2696e8e-22f1-3111-85c9-3225c1d32fd1 | -2.73 | -54.14 | 2026-10-08 16:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3924e31-097c-3eed-b1c8-7d2cc97fb3c3 | -5.37 | -44.22 | 2026-10-08 16:15:00 | MSG-03 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bedbf394-32a1-3d4e-99aa-d7139fb60c28 | -6.15 | -47.91 | 2026-10-08 16:15:00 | MSG-03 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8812dadc-8943-3b29-8d7c-b0959f904392 | -6.32 | -35.13 | 2026-10-08 16:15:00 | MSG-03 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 29f0c353-a7c3-30d8-90c0-7db47c2c90e0 | -16.93444 | -40.29473 | 2026-10-08 16:16:00 | NPP-375 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a9ef3de-c01a-30f3-9777-4c9f03cea162 | -15.56882 | -42.89359 | 2026-10-08 16:16:00 | NPP-375 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3484021b-ee8b-3ff9-95ff-8a6318e3b21d | -15.83143 | -45.39935 | 2026-10-08 16:16:00 | NPP-375 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 490e4ed4-5674-3fdb-9a66-596b44cc14ee | -17.96203 | -42.77275 | 2026-10-08 16:16:00 | NPP-375 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| de53cc42-51ed-3db1-bad3-2977e63191a9 | -17.9603 | -42.77238 | 2026-10-08 16:16:00 | NPP-375 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 41.0 |
| d20c3845-f726-32d2-adcd-4d377536f2c8 | -15.10337 | -49.6616 | 2026-10-08 16:16:00 | NPP-375 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c9a21fb2-93ef-304e-a778-4807881a025a | -14.60135 | -40.01652 | 2026-10-08 16:16:00 | NPP-375 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 6cb891eb-9baa-3831-8a72-4bd1da3b8741 | -14.20166 | -41.84067 | 2026-10-08 16:16:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 5cfe62cc-e9f3-32d2-ba72-f16f11ba3aa5 | -18.06064 | -41.5013 | 2026-10-08 16:16:00 | NPP-375 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 26e29770-e17c-3c59-b1cc-bb91f12cbb77 | -14.02544 | -39.03304 | 2026-10-08 16:16:00 | NPP-375 | CAMAMU | BAHIA | Brasil | 2905800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| cad17d09-aac8-3514-a2a7-0dabb3fbbfc4 | -15.38831 | -44.3469 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| a2057a02-1ee0-392a-9031-9eade0b8eb1e | -14.46245 | -40.56473 | 2026-10-08 16:16:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 190f2a94-1a79-313f-a950-0526708d46b6 | -16.05197 | -40.64902 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |


[Clique aqui para ver as próximas entradas](README255.md)
