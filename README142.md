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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d014e34-090e-3e8f-8266-b18d096d5638 | -9.5463 | -45.7708 | 2026-09-23 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a4e4fa12-83f7-30c2-aebc-4ca32602a1ab | -6.2396 | -41.6634 | 2026-09-23 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 157.6 |
| 0c879cf9-1d56-3f95-9f21-03f6fbfda597 | -4.2632 | -55.4303 | 2026-09-23 14:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a4194e32-4294-3a91-a6fc-a566f9b1f4fb | -11.6605 | -43.4476 | 2026-09-23 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 930a2485-5985-34d6-825b-b16ffd2ddcd9 | -6.3015 | -59.9387 | 2026-09-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 1396b38f-a80a-3fe3-bc02-92bfe859d905 | -9.0239 | -48.1622 | 2026-09-23 14:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 61db5227-19d7-33c9-a6af-81c903344a3d | -6.4486 | -59.9717 | 2026-09-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| cf05eaf8-0934-3c08-850b-b83051f1361e | -6.4302 | -59.9724 | 2026-09-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| be85dfa9-0529-3e5f-b5bd-18f4f61a15ea | -6.9225 | -42.9088 | 2026-09-23 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| fce646c8-faba-3be0-9530-bffde342ca3b | -6.6148 | -59.908 | 2026-09-23 14:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 157.3 |
| 0e4bcf8b-85c1-395e-9580-2fecdda5ceef | -11.4018 | -47.3628 | 2026-09-23 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 05a3beb0-58c6-3308-9c6a-59f3240a0a25 | -10.0096 | -45.1915 | 2026-09-23 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5935dd4f-43c3-367c-8517-89027da332bb | -6.9411 | -42.9306 | 2026-09-23 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| c96042bf-afd2-3440-a80f-f04537ff4586 | -7.4683 | -44.5539 | 2026-09-23 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a7b3d145-12e0-3e5f-baa0-980dd03e3665 | -6.6357 | -45.1752 | 2026-09-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 1669c5f2-5357-3f9e-83c0-6a65704b8bcf | -7.41 | -44.7198 | 2026-09-23 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| be5249ae-6f01-3db0-9bd1-7ada70f726dc | -10.5087 | -44.8748 | 2026-09-23 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 022bac11-2f87-34fb-91c7-9fc25ffd230e | -6.8216 | -59.1686 | 2026-09-23 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 2462dea1-ec27-3824-80e8-19c748277fbf | -9.5329 | -45.3861 | 2026-09-23 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 45.5 |
| e3d76375-2460-3b7c-a2a8-d2f4c8ecee8b | -6.9029 | -46.5456 | 2026-09-23 14:30:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 4d1fa4a4-115a-3e64-b75a-6763b727afee | -8.0279 | -61.3626 | 2026-09-23 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4abdb32c-27f3-3bbd-839c-9e9c68031c8c | -9.1525 | -49.9639 | 2026-09-23 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| f029713e-5ac5-3091-a502-b066f17884fd | -3.2955 | -59.4284 | 2026-09-23 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9242b22b-9633-38c8-b3f5-b69a21994e7a | -6.9223 | -42.9323 | 2026-09-23 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 14685b68-3810-3707-b625-5285c6165f7b | -6.1359 | -59.9446 | 2026-09-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| c105712d-b432-303f-a99c-9b27c6801e51 | -6.9414 | -42.907 | 2026-09-23 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| a9851095-e8a8-3993-a981-768a9e2172a1 | -7.1014 | -42.0849 | 2026-09-23 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 4f1533c4-a52c-35c7-bad5-fc688972bbc8 | -6.2208 | -41.6651 | 2026-09-23 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 178.3 |
| cba7f1c7-dade-3f93-abfe-675401041fdd | -6.3199 | -59.9381 | 2026-09-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| e8f4771d-e44f-3ea9-8821-835ae71f72d3 | -7.5704 | -57.6766 | 2026-09-23 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 845b90f9-ef08-3278-9bd8-8ebcea233213 | -11.4005 | -44.0525 | 2026-09-23 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 32bb16a2-e104-3d25-8bb6-fb39aa6366e8 | -9.831 | -48.4292 | 2026-09-23 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 1998d97b-d431-3134-aff9-36185551f2e7 | -9.3797 | -48.3232 | 2026-09-23 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 69353634-bb69-31f9-b8ae-670c3119c789 | -6.5756 | -45.5645 | 2026-09-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 3fffd452-d642-3633-a57f-46dcdba7031c | -11.6789 | -43.4921 | 2026-09-23 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 6f4427ed-6b74-3f55-a205-8e67f03be2df | -6.6515 | -59.9258 | 2026-09-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 3c60b76b-bf53-3746-a825-1891b09ea041 | -6.136 | -59.9254 | 2026-09-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| ac58364c-aaec-335d-bdba-4ba4edfdb778 | -8.5992 | -44.5301 | 2026-09-23 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 27086baf-38ad-3fa8-9c3b-33aaca174e21 | -9.6043 | -48.4529 | 2026-09-23 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 621b7be7-649d-37db-a907-5c70bd853c43 | -8.7735 | -45.6303 | 2026-09-23 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 4dd1d2a9-7aa6-394c-9612-50f53fc9f7fe | -6.5639 | -44.8628 | 2026-09-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 81c380a1-799f-3220-b357-b999451eaaf0 | -6.9228 | -42.8852 | 2026-09-23 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| acc74242-8ebb-3dc3-accc-ce7250f9409a | -11.0804 | -49.7456 | 2026-09-23 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 4dfc939a-ebc1-30fe-8281-950da8671ec7 | -8.0912 | -44.423 | 2026-09-23 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| b6ee8321-4e8a-301c-bf48-8f6562e0d112 | -6.6331 | -59.9265 | 2026-09-23 14:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 661.0 |
| ef4a45df-0cbb-36df-a9ec-d997764673d6 | -3.4635 | -58.3096 | 2026-09-23 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 255e60fa-5c5b-3232-9669-4aa7e66d8cc5 | -6.2036 | -45.3227 | 2026-09-23 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e5b52008-3e27-38c7-aaae-eafb3a7eaacd | -6.6515 | -59.9258 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 53a748b7-c39e-387d-bb6d-4c5d6ac05628 | -6.001 | -51.7903 | 2026-09-23 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 996f524d-16d7-3beb-96bc-0139a772772c | -7.6834 | -45.468 | 2026-09-23 14:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| b20e4d75-60fb-3cbc-bbaa-89c70bd1d345 | -11.3784 | -44.2195 | 2026-09-23 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 165.8 |
| f68c98ec-ee96-3728-ad27-c4ff1d9f5bda | -10.5087 | -44.8748 | 2026-09-23 14:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 4c59fff3-0e03-38c7-b455-42fdeb07fb2b | -11.3976 | -44.2167 | 2026-09-23 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 657.0 |
| e335e87c-522e-3e26-b09b-c27e12b40dde | -2.9341 | -57.7786 | 2026-09-23 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c5a98c53-2e2d-35a6-baf1-39f3f3288aa9 | -6.6332 | -59.9073 | 2026-09-23 14:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 32b39bed-9757-3a82-96f8-cb29da7c2bf1 | -6.2399 | -41.6394 | 2026-09-23 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 63d16f13-c560-30d8-8f62-aacd7978f7d8 | -10.5561 | -46.7095 | 2026-09-23 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 40bc5afd-71fa-3981-893b-b61d312ef450 | -6.9225 | -42.9088 | 2026-09-23 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| d33b8c57-9866-3fce-a89c-b88e47e002fc | -8.0279 | -61.3626 | 2026-09-23 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| dc0cdc1a-54bd-328d-99d3-1e805acf34ba | -6.3199 | -59.9381 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 1a67fd00-4f71-38f7-9248-579fb1571461 | -6.8841 | -46.5471 | 2026-09-23 14:40:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 4464e8c8-b525-3229-bbe4-6b72510fb8ef | -6.9223 | -42.9323 | 2026-09-23 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| f33b0987-99f8-34e2-bf04-d0525f69ec03 | -6.2832 | -59.9202 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8ac4db5e-70ee-3ccb-8b4d-afa824b60f5c | -3.3138 | -59.4472 | 2026-09-23 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| f51ea4bc-6879-31cd-b0d0-039d1fed63b1 | -6.922 | -42.9559 | 2026-09-23 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 63e2f253-5aa4-382a-8bbc-9ee095ba5ba1 | -2.934 | -57.798 | 2026-09-23 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| cb6304c3-3638-39f4-ad4e-c0afe78e5807 | -6.1849 | -45.3241 | 2026-09-23 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| a5a203e1-15fc-378e-9d18-7240fea843bb | -8.754 | -44.2589 | 2026-09-23 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 21895ae9-6738-3743-94fd-8695715b816b | -11.3551 | -43.3764 | 2026-09-23 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 302.4 |
| 5d07e5a2-a630-3f88-bde2-a71b70b6dda8 | -6.5962 | -59.9279 | 2026-09-23 14:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 157.2 |
| f3570af6-a3b7-3859-b6fe-15faba3930f3 | -3.4599 | -59.5209 | 2026-09-23 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 47b65936-5bb2-3a93-b029-6846ac48f577 | -5.9987 | -45.225 | 2026-09-23 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 574b1048-446d-3943-a335-ee193028b3bb | -9.9067 | -48.4211 | 2026-09-23 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 159.7 |
| b62b49e6-02ef-315e-952a-4ac45c061ac0 | -8.7584 | -49.9566 | 2026-09-23 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b32cee69-d4bf-33ec-bc96-5bc56f487c61 | -3.7167 | -54.1896 | 2026-09-23 14:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 235.2 |
| dd30f7f2-b950-3dee-aadf-beb4f41a0206 | -11.4548 | -47.6229 | 2026-09-23 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 85003203-1aa8-3659-b35e-54e6b680412c | -11.4018 | -47.3628 | 2026-09-23 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 3a6eeded-59e5-3d56-8de5-e1ed8165fa14 | -6.8216 | -59.1686 | 2026-09-23 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 522760f8-6e82-35f9-bbf9-b83325e610dc | -6.1361 | -59.9063 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4f6d842f-0510-378f-8c18-6d0b4188564c | -6.5759 | -45.5419 | 2026-09-23 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ffaa9087-6f23-336f-bf43-bcf35d00d216 | -7.5704 | -57.6766 | 2026-09-23 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 7195a415-e090-3f25-82ef-f72574563f46 | -11.6426 | -47.7984 | 2026-09-23 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| ba7ed759-ad3c-3f9e-87ac-8fced4924f5e | -9.8694 | -48.3814 | 2026-09-23 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e522cfcc-8bff-3820-9d0e-f6d38fd3dd6a | -6.9414 | -42.907 | 2026-09-23 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| b983e00a-2039-3ad5-a36d-119c34d8f4cf | -8.5803 | -44.5322 | 2026-09-23 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| dd514c4e-e2b3-37b2-95e9-b69496d48e8c | -8.7582 | -49.978 | 2026-09-23 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a8bc5fba-2499-35fc-abf0-19ff8d851d84 | -8.9205 | -45.931 | 2026-09-23 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 2c4438a8-1f6b-3b75-9b6a-9c4c4a07cb94 | -9.406 | -47.7507 | 2026-09-23 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| dcb42535-feba-39b4-b840-5f982b33cc62 | -11.6621 | -50.2169 | 2026-09-23 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 68efca09-32e0-3319-b32d-492a6e2b2087 | -6.6127 | -43.7549 | 2026-09-23 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 1fb80630-6adb-322d-8c08-ec0bdc1c0b90 | -6.8951 | -59.2235 | 2026-09-23 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 31d06cfb-604a-3754-bc67-f2b99e29271e | -6.4301 | -59.9916 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 0999de52-20fb-3972-8e2e-d873a39cd557 | -9.8307 | -48.451 | 2026-09-23 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 2133a135-aaa4-330a-bacc-be6fd8facf07 | -2.7713 | -57.0229 | 2026-09-23 14:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 19da4f97-ab34-3f74-9980-90d11cb6e980 | -6.3015 | -59.9387 | 2026-09-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 6983560f-b65a-3149-8659-52d0faa913c5 | -9.0239 | -48.1622 | 2026-09-23 14:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 356d2305-29cd-356f-9bc2-9c66849af3eb | -7.4097 | -44.7427 | 2026-09-23 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 70cda85a-8f53-3b34-b8b3-07b7d87776ba | -7.4286 | -44.7409 | 2026-09-23 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| e775f32e-876b-38cb-b355-56a10b54e9d7 | -8.4799 | -57.6085 | 2026-09-23 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| 453822ed-23e8-38fe-a17b-f21bd871f44d | -11.3972 | -44.2401 | 2026-09-23 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |


[Clique aqui para ver as próximas entradas](README143.md)
