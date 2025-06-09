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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74c3be6a-8e68-3d4f-86d1-7351288b4928 | -11.5775 | -44.8645 | 2025-06-09 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 4630d328-74ef-3b3a-9a45-27f5baa44867 | -14.2442 | -45.5002 | 2025-06-09 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 6320e7d2-db49-3a67-959a-6449bde80e08 | -14.2057 | -45.4838 | 2025-06-09 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 70565f5c-12c5-3fee-a1b3-dcd89edb3662 | -14.2252 | -45.4804 | 2025-06-09 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 244.5 |
| eed1f7c2-7a08-3317-b052-a641a1114ddc | -11.5771 | -44.8877 | 2025-06-09 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 6334d875-06bd-3d3b-b4e1-a01b62e84110 | -11.5775 | -44.8645 | 2025-06-09 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| e62c6ad6-103d-3f95-9057-b99df0d17469 | -14.2447 | -45.4769 | 2025-06-09 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| cbdaf54f-867c-35f6-bd04-47816ba027c6 | -14.2052 | -45.507 | 2025-06-09 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 32a7cb71-46d2-3df4-a148-8275743e6a4a | -14.2247 | -45.5036 | 2025-06-09 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 08f55ddf-4755-3396-9ab0-9ebbf0a407f4 | -14.2057 | -45.4838 | 2025-06-09 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 32c163d8-fba2-3325-9518-e8e0ad865d5d | -14.2252 | -45.4804 | 2025-06-09 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 2faa45f0-11e3-3e2d-8aed-f51f43d33ec4 | -11.5775 | -44.8645 | 2025-06-09 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 3343182b-21ab-38a9-b3d0-e48137e8a34b | -14.2247 | -45.5036 | 2025-06-09 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| fd81e9d9-bd0e-38c8-849e-0c649477955b | -14.2442 | -45.5002 | 2025-06-09 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3bf105ed-4e83-36b8-9620-5efab3657fd8 | -14.2447 | -45.4769 | 2025-06-09 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| a9b1b1c2-e779-391a-b4b0-0d6898c445e3 | -11.5771 | -44.8877 | 2025-06-09 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 673f9e97-11d7-36e5-8601-92b6dd2215a8 | -14.2052 | -45.507 | 2025-06-09 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 7d2fe0c1-85f3-38c4-86b2-c12527b0e671 | -13.726 | -45.2421 | 2025-06-09 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 48f7147c-a24b-3716-a6af-89615cdf7f88 | -14.2052 | -45.507 | 2025-06-09 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 404a3c26-782f-3ca1-a580-d7d395d4bd67 | -14.2252 | -45.4804 | 2025-06-09 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 234.6 |
| 1e1b205d-3841-3a0a-bb60-6eaeb3c6cfb9 | -14.2247 | -45.5036 | 2025-06-09 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 4e29f78d-9001-3918-a88c-324713f6ca7a | -11.5775 | -44.8645 | 2025-06-09 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 7073642d-b2f7-3333-aba7-ac0658d7f62f | -11.5771 | -44.8877 | 2025-06-09 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 5891a13e-bc7d-34ce-8b90-678b497c7ba2 | -14.2447 | -45.4769 | 2025-06-09 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 3ef5f50c-c763-3ae6-bd60-4f6bcc27d086 | -14.2057 | -45.4838 | 2025-06-09 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 5cf85504-0a1e-357c-aa7a-1eeb4562072b | -11.5719 | -47.4521 | 2025-06-09 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 8170d81c-55cc-30c8-9e87-1fc9783a8d30 | -14.2447 | -45.4769 | 2025-06-09 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 1baddcef-63dc-359d-882a-8d2dce4635af | -8.2841 | -47.1342 | 2025-06-09 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 1f950137-5575-31fd-8f60-f8d2efe7662b | -13.726 | -45.2421 | 2025-06-09 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 084ff999-d7b6-35b1-8162-6964bf3b24d4 | -14.2052 | -45.507 | 2025-06-09 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 6a596884-143f-3610-81d9-4b3c02882b43 | -11.5771 | -44.8877 | 2025-06-09 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 3df2509a-b03e-3785-bea8-2c5e802af28f | -13.7255 | -45.2654 | 2025-06-09 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 7f4f7c8a-e850-3036-96b6-6f92a9216a91 | -14.2252 | -45.4804 | 2025-06-09 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 213.0 |
| a008d637-72d4-3bb5-aeac-54de8f2f9a90 | -6.6306 | -49.717 | 2025-06-09 13:40:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| f7e34703-2214-3d4c-b0a7-e1190e2c6a0b | -11.5775 | -44.8645 | 2025-06-09 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 837f9dcc-3eb3-33f6-b17c-5f5c115db74d | -11.5719 | -47.4521 | 2025-06-09 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 63529617-bd41-3d66-8c81-2fa4bd2dae97 | -14.2247 | -45.5036 | 2025-06-09 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 4163b7ac-81a9-3d01-bcac-1d8da62a565d | -14.2057 | -45.4838 | 2025-06-09 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 214.4 |
| 39439e16-b9f8-35e3-896e-69f9d05b0911 | -10.8568 | -53.7836 | 2025-06-09 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| b352fd5b-0c20-3d27-ad48-379c32797ad4 | -6.6306 | -49.717 | 2025-06-09 13:50:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| fa0f52fc-d5b7-3ec9-9c4d-efd0202e94ac | -14.2247 | -45.5036 | 2025-06-09 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 5ab1b495-d168-3b01-bdb7-df0cf2b4f35b | -14.2057 | -45.4838 | 2025-06-09 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 51fad313-0ce8-353e-8a0b-d67f5e96c198 | -6.2228 | -43.3226 | 2025-06-09 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 1d06170c-1625-332c-a25b-828b49d57c68 | -11.5719 | -47.4521 | 2025-06-09 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 5a1ffb59-fc01-3849-b1c8-85d67d07da06 | -14.2252 | -45.4804 | 2025-06-09 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 496e0ddc-c7c7-33c0-8a26-44877f15ab1d | -14.2447 | -45.4769 | 2025-06-09 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 920eecb3-10a8-3792-9ce3-1f791316ee72 | -11.5771 | -44.8877 | 2025-06-09 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| bb65a3f6-ebf9-3f76-839b-77a74617d026 | -11.5775 | -44.8645 | 2025-06-09 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 5db7e0ee-8df5-370f-acf9-e768b3c93752 | -14.2052 | -45.507 | 2025-06-09 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 9e61913b-7ac2-3b47-af87-d281465721e2 | -14.2057 | -45.4838 | 2025-06-09 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 241.1 |
| 90014e69-51d2-3da0-8553-b079fce6c53d | -11.5775 | -44.8645 | 2025-06-09 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 7e09354c-67e3-38ca-b7c8-2ee5dc5642e1 | -14.2247 | -45.5036 | 2025-06-09 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| da8e1760-2f99-3760-a7c0-aa5f502d5cca | -6.2228 | -43.3226 | 2025-06-09 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 3286e1d9-4b9f-36d3-95da-49d896194a3f | -14.2252 | -45.4804 | 2025-06-09 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 09b8e570-8948-3a23-8e85-545798c27df9 | -11.5723 | -47.4298 | 2025-06-09 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 606ce0bd-c32c-3340-a767-bd930afa0cfb | -6.6306 | -49.717 | 2025-06-09 14:00:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 6d412d9c-6dfa-3aed-b342-05e882a48c33 | -14.2052 | -45.507 | 2025-06-09 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e5c03946-6a09-35a1-a4b8-6f9fd13eaad4 | -14.2447 | -45.4769 | 2025-06-09 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 1f807cc5-6560-36c3-be42-493b3f48782e | -11.5719 | -47.4521 | 2025-06-09 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 249e2c45-2cc3-3805-9b04-67efab1a50cb | -10.8696 | -54.2947 | 2025-06-09 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 97a79315-1ca4-39a5-a3ba-ba01c5e2bfb4 | -11.5771 | -44.8877 | 2025-06-09 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| d0127be2-fb07-3d7a-bcbc-d40a80cff67b | -14.2447 | -45.4769 | 2025-06-09 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| ef1dfd78-81f0-3cbd-b85e-adec8509bf5e | -14.2252 | -45.4804 | 2025-06-09 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 4ea6f65b-453d-36cb-b603-6856b5b529bd | -14.2247 | -45.5036 | 2025-06-09 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| a2d97f19-b279-303e-8bc2-caac88714a28 | -14.2052 | -45.507 | 2025-06-09 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 52d4cc1d-c83f-3d89-aef1-a922cbdfb343 | -11.8963 | -47.4537 | 2025-06-09 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 7ff6fc71-462a-331d-88f8-ecb710a1bff5 | -11.5719 | -47.4521 | 2025-06-09 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 45ccb9e3-2d4e-3ea5-90d8-0f5923158067 | -11.5723 | -47.4298 | 2025-06-09 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 11b2b60a-558d-3a75-bbd4-7e85db6eb3da | -10.8568 | -53.7836 | 2025-06-09 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b1c90da2-2122-328d-b143-8317b58308d3 | -11.5775 | -44.8645 | 2025-06-09 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 53d5ddf8-6a90-37c3-bdc4-09106e3e1af1 | -14.2057 | -45.4838 | 2025-06-09 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 221.6 |
| 5cdca77a-8a00-354c-ba8b-1cd8a44e4af5 | -11.5771 | -44.8877 | 2025-06-09 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| ebc84bc3-e96f-38f4-9f1a-73f4e8e24322 | -14.2447 | -45.4769 | 2025-06-09 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 19095ae0-6a49-33ca-8925-22d40c740e64 | -14.2052 | -45.507 | 2025-06-09 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 7d8dfc81-0ac7-3e07-b587-d7a73eaebc89 | -10.8696 | -54.2947 | 2025-06-09 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 8c550b6d-826a-3bc8-8562-145c03715828 | -11.5771 | -44.8877 | 2025-06-09 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 7580c2d8-0b07-31b0-a11c-e5ed5c31cb40 | -11.5775 | -44.8645 | 2025-06-09 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| c3068793-697f-32d6-9e7f-a475d407dbcc | -11.5719 | -47.4521 | 2025-06-09 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 16c2e4ff-4817-3545-8462-c218e39fa14d | -11.8963 | -47.4537 | 2025-06-09 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| f10dca2d-0114-37ed-a025-931708d753ab | -11.5723 | -47.4298 | 2025-06-09 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9054ca20-2d3c-3579-91bf-24fad84391ff | -14.2057 | -45.4838 | 2025-06-09 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 253.4 |
| 47bc49d6-2089-3e1f-9b52-7951e792f17d | -14.2247 | -45.5036 | 2025-06-09 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 8e5220bc-1f81-342b-94bc-e48365b785fe | -6.6306 | -49.717 | 2025-06-09 14:20:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 267b485c-f361-329c-8056-fd832e091abe | -14.2252 | -45.4804 | 2025-06-09 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 14a36222-e67b-3c4f-aa5a-16e150ba5570 | -10.8568 | -53.7836 | 2025-06-09 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 5dfcaeb4-88ad-3e33-8cc4-7e350b6b1d00 | -10.8694 | -54.3151 | 2025-06-09 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 642fc363-0d24-391f-8c16-ebcaab1d7538 | -14.2247 | -45.5036 | 2025-06-09 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| fe46329a-0f65-31e4-92fc-5a6cdd7256dd | -11.5723 | -47.4298 | 2025-06-09 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| fb83c2c0-8e27-382e-9c64-a6b625253d77 | -7.1407 | -43.5908 | 2025-06-09 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 70fa7e3b-8f1e-3be7-b875-c2f0b62a8f0e | -10.8882 | -54.3135 | 2025-06-09 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a0ad286e-d1e1-3987-9b01-b35313168ecb | -10.8885 | -54.293 | 2025-06-09 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 340a72d4-8c77-3390-bd1d-4fa2dc4b73e7 | -14.2252 | -45.4804 | 2025-06-09 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 5bd074b0-451d-325d-b264-d7e7e142832f | -11.5719 | -47.4521 | 2025-06-09 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f52d18b3-6c0c-348c-9fba-20a36e800170 | -11.8963 | -47.4537 | 2025-06-09 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b219eaa5-392b-33f9-8521-3ef1838c5027 | -14.2052 | -45.507 | 2025-06-09 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 1354b356-ee92-3097-95b9-e3d865b138ad | -6.2228 | -43.3226 | 2025-06-09 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |


