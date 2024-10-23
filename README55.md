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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9677a296-c58c-3f73-b625-c8796d53ea2d | -5.57699 | -44.87924 | 2024-10-23 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 53b9862f-76be-39ff-89b4-4c27c377fc9f | -7.17255 | -45.14337 | 2024-10-23 05:16:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c19e6652-7241-3bc7-bdf0-eb0878148c8b | -7.16804 | -45.133 | 2024-10-23 05:16:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25d6381c-97c5-3c7c-8b42-e3fa0f874ad1 | -7.16711 | -45.14037 | 2024-10-23 05:16:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f6d856b-875f-36fb-9b78-a070dccf8888 | -7.16633 | -45.13498 | 2024-10-23 05:16:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6fcf37c7-a61e-35a3-909a-4636750f0564 | -7.16541 | -45.14186 | 2024-10-23 05:16:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| afc80f1c-40ba-3451-ab3a-5d298a6af0a7 | -4.75978 | -45.76735 | 2024-10-23 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34829182-c1ae-36b7-99be-71ed8711f40d | -4.75483 | -45.7659 | 2024-10-23 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06e2e9a1-72d5-3b31-8e80-f992fffbb156 | -4.75449 | -46.11353 | 2024-10-23 05:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 30ffb916-8b51-3548-8834-d8875073c78c | -4.75402 | -45.7719 | 2024-10-23 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eee0d451-e5c6-377c-a877-f6c0c9c1a08e | -4.75311 | -45.7659 | 2024-10-23 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6b71c27-8a24-333a-b035-7415ea575aaa | -4.72565 | -45.71659 | 2024-10-23 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d5a028b-fa7a-3fea-84ff-6d0dea1270f1 | -4.72477 | -45.72286 | 2024-10-23 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b8ab2439-800c-3d00-8043-a0812d83624b | -4.72388 | -45.72918 | 2024-10-23 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e043584e-7d62-345e-b063-f243447f2275 | -4.72308 | -45.73488 | 2024-10-23 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| aed9a0a8-7e59-3ec0-8910-ebaeba25c0af | -4.7181 | -45.72126 | 2024-10-23 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3cc45e6-d438-3a95-9fb5-154cee65048b | -4.71722 | -45.72752 | 2024-10-23 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 196b2170-d8aa-36c5-a527-968b54eeec3d | -4.71637 | -45.73357 | 2024-10-23 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 60fe1cb6-96b0-3918-809a-9fb263bb90b5 | -4.71555 | -45.73938 | 2024-10-23 05:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e45e022c-066c-33e5-bf36-218bdd5de574 | -4.65774 | -46.19728 | 2024-10-23 05:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9c10444-554b-3989-8973-65e450aab55e | -5.70538 | -44.99622 | 2024-10-23 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 183a66fa-f88b-3417-b52a-d297329dce69 | -5.36555 | -45.08172 | 2024-10-23 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31937637-020d-3daf-8bf0-cb1c48876611 | -5.22797 | -46.16334 | 2024-10-23 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ef1b0ea-9407-3d3b-af12-f5690329e5ba | -5.22439 | -46.15683 | 2024-10-23 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a55f981-4140-3586-a7d1-7258f1505a61 | -5.22359 | -46.1625 | 2024-10-23 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e78db25a-0e37-3dd4-974a-12f12540921a | -5.22216 | -46.1563 | 2024-10-23 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5ac3f9c-fbaf-3699-b870-fe201ce834b2 | -5.22138 | -46.16214 | 2024-10-23 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a33140c1-77f4-37d0-9de5-4f58e6bab60a | -7.4262 | -46.618 | 2024-10-23 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d879954-68f1-3049-b0ab-68457151202a | -7.41955 | -46.61723 | 2024-10-23 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fb995af-efd6-3c45-847e-38de91fe7eaa | -11.88138 | -47.70704 | 2024-10-23 05:16:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3902e4db-40db-35d6-8e22-6919641a9294 | -11.88074 | -47.71253 | 2024-10-23 05:16:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c770bf0a-f48e-3683-805b-8dcadb1f11f1 | -11.82209 | -47.07552 | 2024-10-23 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 56f7b333-5c4f-3a0e-a0f2-2042a107f30e | -11.82139 | -47.08167 | 2024-10-23 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ef814dd4-0695-33b7-a26c-981b91029875 | -11.81527 | -47.07485 | 2024-10-23 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cb624562-37ff-31bb-ae7d-fe9dc88cef10 | -11.81458 | -47.08094 | 2024-10-23 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c4229db6-d620-366b-b646-18db7cea9656 | -11.62663 | -47.57513 | 2024-10-23 05:16:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 166261aa-adc7-3322-afd9-151f8b93f846 | -11.62597 | -47.58097 | 2024-10-23 05:16:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e1cacc86-87ba-3923-9658-843dee444355 | -11.61938 | -47.58016 | 2024-10-23 05:16:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6e0a7a7-cb5a-3532-af9b-2d8d34c43201 | -4.76872 | -46.61786 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76a511fe-5596-37e0-bdae-566acfec4c4d | -4.76798 | -46.62295 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30ab0d4d-bb5f-3a49-82a7-31531466b0fb | -4.76368 | -46.61846 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cab26f8a-b5e6-3610-8d36-7361d9aaf239 | -4.76298 | -46.62349 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28965d51-cca1-34b9-80d5-534903364102 | -4.76229 | -46.62849 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4be32f8c-eab3-3af6-b205-c0fee9685437 | -4.76227 | -46.61723 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 324dc517-4275-3505-b60b-f4075718ce20 | -4.76154 | -46.62226 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 28896df1-21c0-3e23-9815-09fbe05f5bfe | -4.76081 | -46.62724 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| df981eb0-8a6e-38ec-8a44-5bcedda9e27a | -4.75725 | -46.61771 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bb42275-b5fa-390f-a30d-43e1dc9acc72 | -4.75655 | -46.62273 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fba9797-d162-3908-b5c0-1c3d9f457780 | -4.75584 | -46.6165 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25f854ed-4d6d-38f3-be0f-840d6cfc9081 | -4.75511 | -46.62149 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f6c65752-1c2f-3141-880b-3c31d44d2ec0 | -4.7508 | -46.61705 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a3c9a61f-bf27-3d15-b8ac-bc292aca5a23 | -4.75011 | -46.6221 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cf960eb3-2bfb-3bee-a9e1-6719b01d570b | -4.74938 | -46.61593 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6a27f17-0956-31a8-991c-57d4d911fd16 | -4.74866 | -46.62091 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| adf6c445-e56d-3b8a-aa79-a660a27c0541 | -4.74184 | -46.66803 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96b69a11-6e51-3b2f-9357-a41f44dd2699 | -4.73786 | -46.66371 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55328b87-078d-3670-978f-3ee311b4a45b | -4.73715 | -46.66887 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e75af223-bb0b-3af8-961a-490816011a2f | -4.73648 | -46.67379 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06aa8e0e-b3c9-3a82-a3a6-8e488013fd0f | -4.73539 | -46.66759 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 654b695a-c104-3ea1-8e3b-df1ae9e36c6c | -4.73466 | -46.67261 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 906c0d1c-7cf8-33a0-9eac-17effe26adfc | -4.73395 | -46.67754 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ac7fb22-d5d7-33e5-a267-8b5dbcae9498 | -4.73006 | -46.67313 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63a70e12-d46d-3245-b784-2d79054c0dae | -4.72936 | -46.67825 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 260159ad-ea5d-32dc-99cd-18cf9405ad67 | -4.72752 | -46.67698 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6341cfc6-0cb0-32e9-89f9-babca1d07e5b | -4.5536 | -46.6557 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 840863ea-579c-3e48-b4d9-087ed2e4fd9b | -4.55292 | -46.66056 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9ce3fd7-3474-3dbf-bb6e-7185ec7366f1 | -4.55124 | -46.65678 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4913fc4b-236d-356b-8bc3-b2b1c75806f9 | -4.55054 | -46.66156 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 797a5513-4519-38f2-afd2-24c476deba4a | -4.54658 | -46.65939 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 993a9e6e-d3fc-3494-8685-4f2b26793153 | -4.52814 | -46.72587 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7e6d83d-1c44-3c5f-88bc-bb823330a330 | -4.52741 | -46.73086 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18e939ef-60ff-3763-8e65-42fac20ed98f | -4.52393 | -46.72899 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1a9e676-91c8-380e-83f2-962d193ff0b5 | -4.33894 | -47.59832 | 2024-10-23 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aa6d4a25-f832-39af-8232-6b8ee4cf2dd2 | -6.51379 | -47.03704 | 2024-10-23 05:16:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acda8f99-18d6-3772-b976-4b1b1b96ae7e | -6.35008 | -47.12458 | 2024-10-23 05:16:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 199eb773-6f4e-3b4f-ae54-4c40552baf3d | -9.07542 | -47.98938 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d498e10b-d209-38ad-af46-f2154368fa07 | -9.0748 | -47.9942 | 2024-10-23 05:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e42ace15-07e7-3ddd-b161-dfb66e5fc514 | -10.09344 | -47.70876 | 2024-10-23 05:16:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c1ee27d-683a-3c9d-97a7-a12df5febc13 | -10.09278 | -47.71436 | 2024-10-23 05:16:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93f42755-889e-3ffe-ac98-ae0b8717d846 | -11.12257 | -48.10098 | 2024-10-23 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 841855e4-595a-3547-b4f2-493d88e010ef | -11.12194 | -48.10609 | 2024-10-23 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f9afd8a-b0b8-363b-8d59-8a1ec51156c5 | -11.11864 | -48.10154 | 2024-10-23 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 426be06b-d5e5-3491-aa14-11cd83a3d685 | -11.031 | -48.27439 | 2024-10-23 05:16:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e6954b6-d65d-349f-a10f-0f4cec07c7c0 | -11.03038 | -48.2795 | 2024-10-23 05:16:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b7565488-34f4-367a-bbfa-7b619d165048 | -11.02472 | -48.27359 | 2024-10-23 05:16:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 41aadc18-9a27-3ee9-95da-b94f272e6dca | -11.02412 | -48.27866 | 2024-10-23 05:16:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e959baa7-f43f-3a24-8459-d03978140cd6 | -4.40722 | -48.83768 | 2024-10-23 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63475379-0f53-3066-b518-9780ca9d5e07 | -4.4017 | -48.83688 | 2024-10-23 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 782a69e9-601e-3ee1-abfa-97cdf2aeca4f | -4.37385 | -48.47359 | 2024-10-23 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd19bbe3-742e-35e1-b157-d89f44899fea | -4.36819 | -48.47273 | 2024-10-23 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae018619-b637-3f7e-a403-198db620463e | -4.17665 | -48.60575 | 2024-10-23 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5471886-f116-3e43-8221-cb0251813a09 | -4.17208 | -48.59773 | 2024-10-23 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb201970-1a65-30b8-b2df-b2323599d56a | -4.17157 | -48.60129 | 2024-10-23 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acf7837a-4d80-39f0-9be9-71d8768b15dd | -4.17106 | -48.60489 | 2024-10-23 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6efd2569-5e9d-38f7-b95d-1d5e9353de93 | -5.49419 | -49.50726 | 2024-10-23 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 448f6d9a-944b-3ee2-901d-d0762297c119 | -5.48882 | -49.5065 | 2024-10-23 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4d462255-c513-37d1-a2e4-3339a5fd977b | -7.44925 | -49.644 | 2024-10-23 05:16:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 812019ce-2606-39e5-9efa-e9cad99164c0 | -7.4433 | -49.64682 | 2024-10-23 05:16:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abdac714-6cdc-355e-861b-be5bbd566c0e | -7.13771 | -49.50735 | 2024-10-23 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dcf9e88-785d-3240-a8f2-6f0102427c78 | -7.13221 | -49.50657 | 2024-10-23 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README56.md)
