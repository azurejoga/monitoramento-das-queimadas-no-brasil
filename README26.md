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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecf11760-2cfa-30c8-8518-563e2d869096 | -3.33134 | -42.78236 | 2025-08-16 04:08:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4f9eea1-efd0-3023-b375-473b5a5dfa3b | -6.58659 | -42.23269 | 2025-08-16 04:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2f1d5e3f-4b4b-350b-8c82-8dd76842cb79 | -2.51173 | -51.82106 | 2025-08-16 04:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edbef311-3e5c-3bd6-bfb6-682ffb3c401a | -3.98367 | -43.24199 | 2025-08-16 04:08:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6959e7a2-4931-3f36-81b0-f22871ed5ba9 | -3.82135 | -47.73747 | 2025-08-16 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84aea870-31bb-3a0c-b8d2-4bc87b2ffba8 | -4.9195 | -43.25967 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 161d17e2-cdfb-3120-ab95-d7e6a051fb4c | -3.37896 | -52.71926 | 2025-08-16 04:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7c64d1b2-f25b-3a32-bc46-f634a7a0ef5c | -5.19973 | -46.09258 | 2025-08-16 04:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88fec9dc-5014-355e-b845-ffe6b54b1dbf | -2.49053 | -47.56871 | 2025-08-16 04:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d2a0aea-0942-3136-9350-b0c12cbf180c | -2.50989 | -51.82507 | 2025-08-16 04:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1cdd6bb-8475-35b7-94a1-34c5d782b8a1 | -4.91826 | -43.26731 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0317b54-cee5-3c74-9735-b072f82e1278 | -3.82597 | -47.73814 | 2025-08-16 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2ed5eec7-a34f-3cb6-87c8-3d3b3451511d | -2.91103 | -48.30446 | 2025-08-16 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af76e237-3e95-3bc4-afff-067d944c20a7 | -3.43094 | -49.0478 | 2025-08-16 04:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 779f8b8d-af87-3fe0-9a54-90570517a93f | -5.1951 | -46.09186 | 2025-08-16 04:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6515adfd-3b6f-389f-a90f-96ec61955630 | -2.48782 | -47.57149 | 2025-08-16 04:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71c9d0e7-bdb6-355d-89fe-a22989790a48 | -2.04665 | -50.79306 | 2025-08-16 04:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0aad43d4-5dcb-3790-b2a1-f04f7f401153 | -3.32848 | -42.77805 | 2025-08-16 04:08:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23a0d4ae-208f-33e6-a048-f88bbca5a50c | -2.5422 | -47.72247 | 2025-08-16 04:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 40be24e7-a263-380f-9c41-af82a87b30bc | -3.82519 | -47.74292 | 2025-08-16 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| af2af89f-640b-3b26-996d-50be5b7f5a67 | -4.19137 | -48.22371 | 2025-08-16 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90e861bf-f91b-3521-b19e-5244c200ea0b | -3.32728 | -42.78557 | 2025-08-16 04:08:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3770b70-c64f-3714-9d7e-285a9c347116 | -2.82472 | -49.00633 | 2025-08-16 04:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 546d3c49-41be-3798-a2f1-9a15f0cf3742 | -3.32788 | -42.78181 | 2025-08-16 04:08:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8993a42b-2747-3be1-94ec-76eb0bfdb3ee | -3.82675 | -47.73335 | 2025-08-16 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f9c1951b-b46a-36ad-a507-4ba670d17dfa | -4.92297 | -43.26023 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0720908-3a80-3716-8811-087b48d81ccc | -4.14771 | -46.45508 | 2025-08-16 04:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8ef430a-3e5a-3d0f-8c4c-a789aeed4e43 | -3.98832 | -47.88727 | 2025-08-16 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38c05faa-8231-33a1-9743-b81343128480 | -5.6127 | -44.79969 | 2025-08-16 04:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 492aa770-2554-3dc3-803e-0f10da2d5363 | -6.69133 | -41.73749 | 2025-08-16 04:08:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 391b4e3a-df9a-31f3-9f1d-4b4d39ff2584 | -5.06098 | -43.12267 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94922922-b488-376f-827b-9d313f7f541f | -3.43601 | -49.04866 | 2025-08-16 04:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fdb7080-6010-3b08-8079-0eb556474c8a | -3.98717 | -43.24254 | 2025-08-16 04:08:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 36a9fd00-3a36-3001-8eba-b3de91248bc9 | -2.51071 | -51.82032 | 2025-08-16 04:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55d19917-fd88-3c50-8348-e8ea59f97ade | -2.38172 | -47.66412 | 2025-08-16 04:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2c227be8-f4e8-34a2-9ba1-9e9cfa452e23 | -4.9211 | -43.27171 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f8ed2e2-ab79-390d-97c7-408027ce0787 | -7.9148 | -61.7478 | 2025-08-16 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| bf5628f6-be54-3a1a-b96f-621bfc08c647 | -7.9149 | -61.7288 | 2025-08-16 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b6020246-352d-355e-95bb-32313611deec | -7.0796 | -59.2351 | 2025-08-16 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 2c9f9b05-49b9-319a-96f1-0e7e8a83b436 | -9.1709 | -59.6374 | 2025-08-16 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 1684a70e-228c-3975-8faf-4fb5468d91a5 | -8.9893 | -61.7024 | 2025-08-16 04:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5db6ecf5-334a-35c4-9a89-b5199894ff8d | -8.9892 | -61.7215 | 2025-08-16 04:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| e07f1285-4577-3b31-8273-bf5ba8ac47d2 | -6.9486 | -59.549 | 2025-08-16 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 600dbe73-5fc7-34d0-ad61-79f41455edea | -8.9706 | -61.7224 | 2025-08-16 04:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 96fae265-4d8c-3ba8-87bc-0c7b681dd185 | -14.9438 | -54.7166 | 2025-08-16 04:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d122d3b5-833c-3c83-9f7d-f27c4ddcab2d | -6.9487 | -59.5297 | 2025-08-16 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b38bc6c6-2022-3968-8848-8d12047c7981 | -14.9628 | -54.7351 | 2025-08-16 04:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 7c6ae1cc-25d5-3e6c-9666-6d36db32255e | -9.4994 | -60.5278 | 2025-08-16 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 15046e25-4e5b-380b-b498-b454820ec072 | -9.1708 | -59.6568 | 2025-08-16 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 83bf0f14-74d4-3ea8-9ac3-f85f9ee230cf | -6.0807 | -59.9465 | 2025-08-16 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 6e3e3575-4ef2-37e3-9d95-87b2e6d70a01 | -9.4992 | -60.547 | 2025-08-16 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 485b9ae4-c7e5-3767-be76-3818b1829a21 | -14.9435 | -54.7374 | 2025-08-16 04:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5f9c50dd-b69b-3597-a5b6-356d9996e94c | -6.6327 | -60.0033 | 2025-08-16 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| e6271d0d-5fe9-364c-8174-b65eb8494b25 | -14.9441 | -54.6959 | 2025-08-16 04:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 5152d1ea-2846-319a-915c-60221b459991 | -8.9708 | -61.7033 | 2025-08-16 04:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 974a3d92-a831-3320-b863-861412972d69 | -8.9709 | -61.6842 | 2025-08-16 04:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 92.3 |
| a7941a76-ef1d-3821-bf5c-3bdb34423f3c | -8.19432 | -45.03227 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bfd2ff7-9795-30de-a22b-4d205ad3bd2b | -12.53154 | -46.95782 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b73fb3a7-d933-3932-80cb-9cc9266e21ea | -8.1888 | -42.26219 | 2025-08-16 04:10:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e791a52e-18d3-3965-922a-00385207de48 | -12.55535 | -46.95652 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 35eb8082-3e96-377e-b6b1-df89f398e94c | -6.55493 | -43.04564 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d2e5304-1692-388d-ba64-0480289ca20f | -12.04675 | -45.7634 | 2025-08-16 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1caf6222-0b64-37b7-ad0e-38d1d923cd59 | -5.62756 | -51.29491 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 490712e7-cbeb-3dca-9d93-4711f033a4a5 | -12.23235 | -41.38667 | 2025-08-16 04:10:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3344ea3f-0832-31f7-b452-e4d105be9b77 | -6.21129 | -45.92316 | 2025-08-16 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c26d49cf-ae9a-3fe5-a2cb-93bce261db88 | -12.60559 | -46.9611 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7b675f98-9399-3795-beaa-b44b6b3946fd | -7.40019 | -44.88921 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25ba64a5-e445-3946-8066-ee8fb4fa62d3 | -12.80507 | -45.98933 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 859587ff-59e1-31eb-aa01-13db3d131c92 | -7.39515 | -44.89706 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c40f44c-fc7b-3cf3-b8dc-e7d73a0c5941 | -11.91416 | -43.43436 | 2025-08-16 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82d2d24e-8c64-32d0-90b5-90549f1fd494 | -12.53452 | -46.96324 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0458f680-85a8-3a61-8e7a-898828e8cecd | -9.16281 | -45.31568 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65ac51ea-8857-3944-876b-456a47a31e41 | -12.59455 | -46.9341 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| be7f5c62-620b-3c6b-be70-e0715408e6ce | -6.67128 | -43.76757 | 2025-08-16 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a29d833-78ba-3fa5-99a4-702c2615e955 | -7.55522 | -45.42297 | 2025-08-16 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0160756e-2635-30de-bb93-07cd22bfd91a | -7.4241 | -44.88036 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51101295-9bed-35eb-bb8a-6b0adc1a2951 | -6.86297 | -42.80494 | 2025-08-16 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 09dcbbba-6ec9-3e7e-898a-94b29b0cd543 | -12.53536 | -46.95848 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c08f33ba-f911-3653-96ba-5d4362dd31df | -12.56843 | -46.94906 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fd7b1d10-b5f9-33ca-8cd0-03e5bd97dd84 | -8.19137 | -45.02742 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b084622-292a-3ada-b28a-f916fc2cea78 | -13.57413 | -46.97873 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7995f874-76c1-30ac-901c-ffbe524a18dc | -12.923 | -46.9613 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| afbd9390-8f01-3be5-9ec5-3d856af5560e | -13.15883 | -46.87265 | 2025-08-16 04:10:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02a311a4-06b8-3aaa-a273-a08d2a0ea6ed | -8.18705 | -45.03107 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddf57e39-589d-3aee-96c1-5142532005f0 | -8.18047 | -45.0256 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdfa5dab-6d46-3834-b457-89654ee6e797 | -8.19501 | -45.02802 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f90d46a7-0db5-3d3d-8890-26c35472dd52 | -13.58624 | -46.97584 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af9b16b8-e260-3e12-b4e2-f1fbfb838266 | -7.01099 | -44.31199 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6b462d1-16bb-38e1-ae09-23b5b2948c20 | -7.53226 | -50.53042 | 2025-08-16 04:10:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b623122-9ee2-30ba-86c6-d7903d1924ee | -7.01032 | -44.31601 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a750305-c938-3c53-9f8c-1cc24e0953fd | -8.29502 | -44.96546 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fd38640f-5003-3fa3-8e6f-2b46edb64313 | -8.18891 | -45.02113 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00e52ed8-201b-30e2-b10c-b2cb3678bcc5 | -7.39654 | -44.88868 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d206e3a-c228-3ead-bbc5-1ee2fbe014cf | -7.40454 | -44.88554 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7dac90e-dffd-39cd-a2df-c23b788e2579 | -9.26953 | -44.54385 | 2025-08-16 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29577078-0da9-3ff4-bf81-ffb5ca2f2544 | -12.29653 | -50.01311 | 2025-08-16 04:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3581826-9a54-37cf-a717-5b6d848b7e3d | -8.19183 | -45.02597 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b9020f7-f7c0-3395-b6a9-37ad9d768f76 | -13.47049 | -43.75428 | 2025-08-16 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39305eb5-00e2-36c0-a7d2-7283021a3f98 | -9.33053 | -37.98108 | 2025-08-16 04:10:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4ca5400c-7490-34d8-80c9-12242f89a5e7 | -12.4905 | -47.51043 | 2025-08-16 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README27.md)
