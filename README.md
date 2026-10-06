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
| aac26e23-b0ae-3bcd-b29a-314e9ee2a941 | -9.1037 | -64.385 | 2026-10-06 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 517e3759-6169-3eeb-9d9f-ee29c4e2ab13 | -2.7979 | -54.1334 | 2026-10-06 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b8f404cd-e165-395b-b89b-c3a4fc82fd86 | -5.8509 | -45.0318 | 2026-10-06 00:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 8fa56cdc-c710-32f7-9c6a-c5e357a8a5a6 | -3.6915 | -55.942 | 2026-10-06 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 6da7cb5e-c778-3b7c-b944-f9f12a5d1d64 | -9.7313 | -65.0757 | 2026-10-06 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 0a2701d6-c0d2-3e5b-b26c-681edb8dc7c1 | -9.7312 | -65.0944 | 2026-10-06 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 37158306-1317-3e82-bfd1-ad8ae40f7fd6 | -8.7782 | -62.8703 | 2026-10-06 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a4e88a96-9b6e-3a6b-9126-e8383b714589 | 3.5647 | -61.3246 | 2026-10-06 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ab73554b-c417-32e2-8812-bf26e8d48fef | -3.6732 | -55.9425 | 2026-10-06 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 0a3558f1-b8ae-3b22-ac09-8b9675d37e89 | -3.0375 | -53.8865 | 2026-10-06 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| a2b45dc4-f71a-362d-942d-14177d45c809 | 0.4465 | -60.5442 | 2026-10-06 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 6029761c-c3e9-3aad-b898-a7b35a83c502 | -8.7036 | -45.2061 | 2026-10-06 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 7b714463-ce88-3d50-af5f-312da5ff0f6b | -14.9165 | -59.3855 | 2026-10-06 00:00:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 46efa5f0-863e-303d-b0c5-0155708f7930 | -4.8075 | -47.3261 | 2026-10-06 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 8ea26360-58ca-37cd-9490-d175377cd48d | -5.8323 | -45.0105 | 2026-10-06 00:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| b2b8ba4d-f66b-3859-a776-a8486a43c8be | -3.2755 | -54.1819 | 2026-10-06 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 831bba69-9453-38bb-ae44-163742ebdbc7 | -12.1386 | -63.1496 | 2026-10-06 00:00:00 | GOES-19 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 54dcd85d-cb9d-3ed6-a1f2-985e5a67181d | -3.6731 | -55.9622 | 2026-10-06 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 20a84e0d-91be-31fc-ac7e-6627aeeca7b2 | -8.7033 | -45.2289 | 2026-10-06 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 72c24193-ee1c-34bc-8e7c-a9adf4e99cf0 | -3.3906 | -58.1953 | 2026-10-06 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 51d5d571-7e3f-31cc-9a59-efb02d4c1bd7 | -3.5062 | -51.6717 | 2026-10-06 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 0b56d8f3-fd3f-31c0-a5c9-72724ff5ff8e | -4.1085 | -49.3871 | 2026-10-06 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 4bb77fdd-645b-3384-80f4-9c8e5fa24cc0 | -11.657 | -43.6373 | 2026-10-06 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 69a67b5d-c706-31f9-b4dc-0981266ea2da | -2.7796 | -54.1138 | 2026-10-06 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f0f23d9b-7543-3289-b408-e46eaa249a39 | -3.6915 | -55.9618 | 2026-10-06 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 699460f2-60b0-31a8-8b0d-9cb940ee0e93 | -3.0192 | -53.887 | 2026-10-06 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 8c02e510-148b-303a-9748-0c7a48c190fe | -3.3905 | -58.2146 | 2026-10-06 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| e52832a6-f658-3d28-9452-63e883784c3b | -3.1608 | -50.4347 | 2026-10-06 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 2a7a77cc-0e45-3226-8414-c3b906f93bda | -11.2603 | -45.5308 | 2026-10-06 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 7d68bc48-ed2c-31bc-8b70-1159a5910db1 | -9.7127 | -65.0763 | 2026-10-06 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 81914f0d-2fbf-3442-9575-0a63cec3cf1f | -11.6946 | -43.6787 | 2026-10-06 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| c9d9db3b-d9d4-389b-8a5c-a661392b9a80 | -5.8511 | -45.0091 | 2026-10-06 00:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 1d7ac03d-c443-314f-a51d-996b3894afd5 | -3.4955 | -49.8979 | 2026-10-06 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b396adc1-53d1-37d7-a6b7-f6cc1ad99ce3 | -4.3587 | -47.7853 | 2026-10-06 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 34524a04-3dfc-3179-b9b2-4bf16231dc8e | -3.3723 | -58.1957 | 2026-10-06 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 629fc11e-3535-3338-b483-9e44a71a6cac | -9.7126 | -65.0951 | 2026-10-06 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c149ef65-7223-3e4e-b108-068b1efb5c89 | -2.7879 | -57.6843 | 2026-10-06 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| f01c7ff0-093d-3913-bb4b-8e0dd4d25f55 | -2.7879 | -57.6649 | 2026-10-06 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 6b26b420-1f5e-34ca-98ea-b0392bf51c97 | -11.6951 | -43.655 | 2026-10-06 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 426c25d0-a36b-3286-afb1-b551cb7394db | -4.8073 | -47.348 | 2026-10-06 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 109c87a4-2f3d-3cad-8624-50295f2b4473 | -4.1084 | -49.4084 | 2026-10-06 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| e9d158a0-6652-3c75-aade-0e37f3dd9ff2 | -3.0191 | -53.9071 | 2026-10-06 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b4ae0bdf-9915-3c22-b062-e5d70273c115 | -2.7796 | -54.0937 | 2026-10-06 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 5132a2d4-56d2-3559-ba97-dc65667fdc5c | -8.7033 | -45.2289 | 2026-10-06 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| be67562b-b4e8-3cd9-9185-7d549d5f5065 | 3.5829 | -61.3243 | 2026-10-06 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 02e1f38a-ed94-3e66-83c9-bb27f073c4e3 | 0.4465 | -60.5442 | 2026-10-06 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 82.8 |
| e771d3e8-a28f-3110-bde5-0645bcd515cd | -2.9817 | -54.1091 | 2026-10-06 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 51e56fd7-5072-34c4-ad09-aeb98793904e | -2.7796 | -54.0937 | 2026-10-06 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 3f7fbf44-be19-3286-b1f9-599f28ea0c98 | -9.7312 | -65.0944 | 2026-10-06 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.3 |
| ceafef0a-41b5-39c3-98db-b18b6620cacb | 3.5647 | -61.3246 | 2026-10-06 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 93.3 |
| e6b7e2d5-944c-3260-8e24-b1ef32fff9c4 | -3.3722 | -58.215 | 2026-10-06 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 0a87322c-f42e-3ff2-9b78-d16dd1d2ac86 | -2.7979 | -54.1334 | 2026-10-06 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 5a64bf41-9f15-3be3-83ad-822e9ba8c0ed | -2.7696 | -57.6847 | 2026-10-06 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 2749bca7-0888-315e-b365-b0a9060e4bb4 | -3.0001 | -54.1086 | 2026-10-06 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| d5ba3b94-4ccd-352b-a8de-3488d283715a | 3.5646 | -61.3435 | 2026-10-06 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| a9dad6dd-a9e1-30a1-9707-f30bd0738cb6 | -11.3749 | -46.6722 | 2026-10-06 00:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 5326780a-4da7-3bbc-ac33-61006b76ff06 | -16.2039 | -39.2981 | 2026-10-06 00:10:00 | GOES-19 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| 80a0ab78-6016-31f9-9147-c5923afde4a2 | -12.1386 | -63.1496 | 2026-10-06 00:10:00 | GOES-19 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 661e58b4-70a6-307d-a7a2-f7ead53b84a3 | -11.3753 | -46.6497 | 2026-10-06 00:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 51bd5dc5-e561-36a3-8fc5-7b13beb8927e | -2.9816 | -54.1291 | 2026-10-06 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| ecb7d17e-3ff8-3098-96c7-4274e77bdd62 | -11.6946 | -43.6787 | 2026-10-06 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 273d87cb-63f2-3aac-9f94-ce526810832d | -5.8511 | -45.0091 | 2026-10-06 00:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| b428eb8f-9964-35f3-9695-ac78d2baf2ca | -4.8073 | -47.348 | 2026-10-06 00:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ec60bea7-8576-32de-9eb8-042eaaba74b1 | -3.6732 | -55.9425 | 2026-10-06 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 141.5 |
| b9c60bd8-d98a-33ad-a8c1-90f56d93d25c | -3.6915 | -55.942 | 2026-10-06 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| f3cfa828-00bb-3532-8b02-87bbc2520dfd | -11.6951 | -43.655 | 2026-10-06 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ed4673c3-a425-3f55-afbd-30bab0d218df | -3.3723 | -58.1957 | 2026-10-06 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 9e9e4f6f-e5f0-30ef-94a1-819e41ef85e5 | -3.1608 | -50.4347 | 2026-10-06 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 950dbc0d-ef28-33da-8d88-6d412b0794ca | -5.8323 | -45.0105 | 2026-10-06 00:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 23f28335-8f4a-3701-90e3-f57c47999354 | -3.6731 | -55.9622 | 2026-10-06 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 86a50da1-e51e-337b-b73d-3a0e63d606e0 | -4.8075 | -47.3261 | 2026-10-06 00:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| af383c5f-cf29-3515-9e11-9375b5653993 | -5.8509 | -45.0318 | 2026-10-06 00:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 3ce39465-813a-3875-8de8-c3ca16689e4a | -8.5847 | -45.6502 | 2026-10-06 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 4139e077-d65f-3ef6-8854-290d0de8f8cb | -3.4955 | -49.8979 | 2026-10-06 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8aa6dbc9-1ea0-3181-a163-f94d27ade8db | -3.0375 | -53.8865 | 2026-10-06 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 32c19c0e-2689-3f50-80fc-b090288abab2 | -11.657 | -43.6373 | 2026-10-06 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| faaf79c9-155f-312c-9eb1-a5f668ed0cde | -9.7313 | -65.0757 | 2026-10-06 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| f02674a9-80ae-3716-b152-324263093394 | -3.0 | -54.1287 | 2026-10-06 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 8377dcf6-18fe-3ca7-9940-6755066b0ca0 | -3.3905 | -58.2146 | 2026-10-06 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 3bcb7366-abbf-32e1-9d3d-d44517942ad1 | -2.7879 | -57.6843 | 2026-10-06 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 178.8 |
| c6b951da-db96-3b58-8ea6-482d7799ea13 | -8.7036 | -45.2061 | 2026-10-06 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| cff4e45e-76ad-37ee-a8cf-148b9a3f1fe7 | -3.0192 | -53.887 | 2026-10-06 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| f6e1a272-be68-3495-8c53-8be5d970e623 | -3.6915 | -55.9618 | 2026-10-06 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| e98f4e39-0819-32b8-911e-83dd896fdb29 | -3.0191 | -53.9071 | 2026-10-06 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0d043c49-1642-3337-b3b0-dc6034f09d39 | -3.3906 | -58.1953 | 2026-10-06 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 56dcb38a-4dd1-33d3-8139-647163ccaf04 | -2.7879 | -57.6649 | 2026-10-06 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 154.3 |
| a2464f2b-186f-3291-a7f8-7afc45f2bace | -3.2755 | -54.1819 | 2026-10-06 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6ce2261c-422c-3ad9-b1ff-799fa77b6ce2 | -2.7796 | -54.1138 | 2026-10-06 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 6ac9a6a0-79bf-37e0-ab95-06d11c4c153b | -2.7696 | -57.6653 | 2026-10-06 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f69aa4a7-1331-35e1-af9e-c29043d8e7ab | -14.92786 | -59.39138 | 2026-10-06 00:13:00 | TERRA_M-M | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 69b8ba72-2cfa-38aa-8fe8-a11586888a5f | -12.6347 | -42.87322 | 2026-10-06 00:13:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 79.4 |
| f99c4e3e-8ea5-348f-99d8-a6dc33667696 | -13.87911 | -43.78284 | 2026-10-06 00:13:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 7cf9de15-b097-38fe-baa7-0a34148665e5 | -13.0291 | -43.12487 | 2026-10-06 00:13:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 45655c2b-d407-3ff4-92ac-3d7560767e14 | -12.64087 | -42.86736 | 2026-10-06 00:13:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 78.4 |
| b2c50b25-8ca5-31b7-9a8d-722ce6c905e9 | -16.14295 | -46.19484 | 2026-10-06 00:13:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| e6899418-f9f1-347a-a54b-ea6d36e5b4c7 | -13.71274 | -49.39404 | 2026-10-06 00:13:00 | TERRA_M-M | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a6e5ad70-a275-35f0-b9d8-fc1d7ea39efe | -14.76735 | -47.17338 | 2026-10-06 00:13:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 81b138e3-e192-3ac5-b6ec-75f611a72f8f | -13.88291 | -43.80638 | 2026-10-06 00:13:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| a23c4501-fdea-398a-af6a-fc2b519b0bb9 | -16.14878 | -46.18829 | 2026-10-06 00:13:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b67e2d87-8c56-34d3-8cef-5f8b18d846b2 | -14.93587 | -59.38395 | 2026-10-06 00:13:00 | TERRA_M-M | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |


[Clique aqui para ver as próximas entradas](README2.md)
