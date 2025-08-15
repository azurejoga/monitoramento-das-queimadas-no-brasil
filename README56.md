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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d5ea15b-177a-3f9e-b24d-5ad1f3332719 | -6.48656 | -62.93835 | 2025-08-15 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22fa17b3-49c2-3f4f-b712-852a54793fee | -7.01375 | -59.82301 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67c6c962-8331-3b47-ae5e-57af5c33665a | -7.4667 | -59.88845 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a67c7768-bc4c-36c5-9fcb-8d7545a43552 | -6.69685 | -58.82324 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ae612fae-6dc2-38cc-8ecb-c9c88f311de0 | -7.134 | -60.12339 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 307f2073-5c01-39fd-b2f6-eacd8b76e941 | -6.89171 | -59.13283 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54596cda-0d72-3b8e-b304-ea9fac2a7986 | -7.07657 | -59.22364 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f751f488-0837-362e-b9c7-e7b49d61f17b | -7.2478 | -57.67897 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a33a58f-1b33-356e-bd17-4873441d110a | -6.66587 | -58.81394 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d87951e-f6b6-3d5c-b7d1-aa7657ce94c7 | -7.43834 | -60.02518 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32e2d408-bffa-36ee-ada0-f750659906e2 | -7.45595 | -59.9029 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f78b2e2e-c22a-31eb-b7f8-8231ac333673 | -7.24382 | -59.9945 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91a965a2-f8df-3919-bb19-2f13aa47ae5f | -5.45444 | -60.13785 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bac22639-655f-3c8c-bbcb-4ccc512ef707 | -6.08237 | -59.94836 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3f0b2d3-55d5-309b-b24a-189674405ea3 | -5.45144 | -60.13007 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 225f6df0-6e64-381a-bc3b-c4173bc16297 | -7.08602 | -59.22057 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13206164-8335-3302-b9d3-d4b3c42c1649 | -7.30188 | -60.62531 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d89413e-4052-3404-93ec-476683644b94 | -7.09142 | -60.03547 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 749009c9-33a7-3b9a-97a7-57dbccffedb6 | -7.31902 | -60.62072 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 569bb329-c941-37d0-98fc-19c5be99d667 | -7.32056 | -59.61814 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 6f213c95-d97c-3b47-8f34-c233ab68be0b | -5.45903 | -60.13486 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 947612cb-8fa6-3d9c-a86d-1f71494c6ddc | -6.93799 | -59.62872 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79b23ba2-06a8-3b0d-8f88-b9b2944f2712 | -6.89746 | -59.15602 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18c46c13-1854-350c-a870-f3f7d55bd3ee | -7.25585 | -60.0003 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f27ac99-68b3-3b24-94d6-105d56bf89b0 | -5.44529 | -60.14378 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fc44e10c-c52a-311c-82c3-792dab798157 | -7.1477 | -60.12906 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20cc817e-67f8-373a-a1a6-8534bb5e7880 | -6.94464 | -60.00717 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2be365a-5df3-3e36-bd06-4cc95f50d039 | -6.70269 | -58.84731 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 454d89bb-a524-377f-a2fe-08372e7085a2 | -7.32306 | -60.62131 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63fab6a9-d304-3f3b-8e87-b6341d5a22f9 | -5.9337 | -59.93523 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68cc5f63-e383-3d89-ad4b-369edcaffa4c | -7.143 | -60.13233 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36fb9ab0-3897-3512-bc56-a10a613891d9 | -6.48305 | -62.93781 | 2025-08-15 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 892d021a-0b55-32d4-abf0-1c671deb3452 | -7.13399 | -59.64571 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3634fd20-09e7-39e7-917d-418e19d769b5 | -6.08102 | -62.50975 | 2025-08-15 05:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c4caeba-d6ac-3cc4-a8bc-1d5f9394d95f | -7.08725 | -60.03477 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f986b445-c0bf-30f0-a0cf-84d1533fe18e | -7.13344 | -60.12717 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b82b3f4-e132-33c7-b070-3e4aa1709c8c | -7.32206 | -60.62829 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d85c505-f992-3781-8383-54d0ae032083 | -6.90314 | -59.14787 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eabb51a4-de45-3a8d-a863-b62b0a8bfa20 | -6.65434 | -58.81865 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fbb596f-0acd-377e-931a-d47d89eb9db5 | -5.81238 | -59.22697 | 2025-08-15 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4de9c06-a91d-3d78-a9b1-19b4f4a2c054 | -6.92922 | -59.53604 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b6c74a3-87e8-382b-9907-3e5bc2c047c7 | -6.90501 | -59.13478 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab0ac188-39d5-3c73-8318-d5f0d34a7229 | -7.2517 | -57.66318 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb6ef3e5-4a07-37aa-aefa-9dd16ae461f6 | -6.65121 | -59.08431 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4865a5d-c894-3d26-aad8-68731d779c88 | -6.91006 | -59.13113 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f240f6e-3562-3779-9aed-aa54ef1a32e2 | -6.88985 | -59.14593 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d83671aa-4012-3df0-9704-d7b658ce6e9d | -7.29785 | -60.62473 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b323b0a-04e0-3606-9e72-4337d5681346 | -7.09198 | -60.03156 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b01def8c-2a32-3a2e-a4e5-48ed7ef670aa | -6.48365 | -62.9339 | 2025-08-15 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3885cf25-8514-39f7-8279-729a6ae7df1e | -7.41988 | -60.03413 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f8d64f2-3717-38c3-9af2-7bf2ddf0f432 | -6.91766 | -59.1412 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68357dc9-b80b-341c-bd94-16eaa65c8cef | -7.12929 | -60.12653 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abdc52d9-d904-3352-a8aa-c9cc98cb8f71 | -6.69556 | -58.83243 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dffbee1a-62d7-3dd4-9b3c-f6ff4198ec43 | -6.66787 | -58.8207 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7c3d4919-b504-3a03-9bb0-3e04b026917f | -7.07916 | -59.23727 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bd85f8ca-be48-311a-9ad4-907722fac585 | -6.89365 | -59.151 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4010e41-bf87-38e1-81d0-a14f89c59c62 | -7.27109 | -60.63203 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d9b102a-8351-3503-80f1-54cee2cefac1 | -6.93902 | -59.52909 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32666bbb-2933-3176-ba65-9fe1cb08c5d8 | -6.64918 | -58.82251 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f5d61bc5-ca59-3389-8d97-23b918d641fa | -6.72073 | -58.81735 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53be6a07-2b82-3dae-b44e-bfc8a87c62ea | -6.64739 | -59.0792 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc5e21e6-f265-3904-bb60-dce302456346 | -6.89996 | -59.13845 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbc9fcd3-cf39-3f45-85c3-c433ee556472 | -6.89428 | -59.1466 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9cdf46d-3288-3e6c-9baf-e30eec5c4d87 | -6.87532 | -59.15282 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8e4ccea-edbd-3188-9c07-b7ac8e4f4160 | -7.0778 | -59.21488 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3abf3c86-8fde-3495-bf28-ebdaf69e86ed | -7.25618 | -57.6295 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1062226f-3b0e-343e-9424-1c0c23092901 | -6.69234 | -58.82254 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| de88b28f-2908-3617-99ce-ba1f142f5437 | -7.30642 | -60.62239 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48332ad8-970a-35c4-8eb6-7a3567ba209f | -5.92597 | -59.93025 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f65df6c-1c81-3947-9b05-30839cc712c2 | -6.67491 | -58.81522 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efef3cb1-703f-3a43-ad2b-18a7539a26ea | -7.13522 | -60.1272 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d2b7574-6c52-3776-a8eb-65e32f21b8a1 | -6.92589 | -59.14693 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1198fc6d-2dec-3900-b166-905e232143dd | -6.87854 | -59.83248 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d6c2648-b3c8-3716-96e3-6e44f8774b6b | -6.90254 | -59.63175 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2aee09d6-93e8-3ac3-94ec-437c882d0138 | -6.93682 | -59.63688 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1db4937-be59-36d8-b304-682f270bda06 | -6.89871 | -59.14724 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b99031e-ff1f-3922-8992-c431dd283762 | -6.89933 | -59.14284 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bde249e3-54ea-33b0-8085-6020174870c1 | -7.43304 | -60.03217 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caa4d8b6-9397-3651-a99a-41c286e4aa59 | -6.94057 | -59.82156 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4a262d6-f081-352f-894a-339c1a9e0c02 | -6.66891 | -59.08712 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15f7e4c9-a77c-3eef-8bf1-7852d5a59e8d | -6.95084 | -60.14323 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73bfa9f2-95f5-3804-8598-07e32fb8e81e | -5.45956 | -60.13129 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5caa5e3e-3e6d-3a96-b334-3eb804367a02 | -7.30138 | -60.62879 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec78af7e-2e8c-38a4-ab35-e047fbac41c3 | -5.44986 | -60.14081 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c54c6cea-b0ea-3f61-b553-fea31f4b4272 | -6.47895 | -62.9412 | 2025-08-15 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 63417d21-caa9-3a9d-9a39-a2dd01421eab | -5.92846 | -59.94211 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2122b3c7-4e2e-3462-9579-f9aa046d63cf | -6.89109 | -59.13715 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bb9b846-31e8-3c2f-9390-3483e07fe774 | -6.48245 | -62.94173 | 2025-08-15 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3aae2cac-ad6d-3da7-9a21-434f714c5b7e | -7.41367 | -60.01749 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 096d949a-c41d-3c21-902a-0e6ebcab5636 | -7.25848 | -60.63379 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7858208b-a07b-36a5-817a-666c8c65b6be | -6.65368 | -58.82321 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e7d3e989-927c-32b6-a9ee-f822e6c3bac6 | -6.91167 | -59.62908 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d57490a1-6dd3-353f-bef9-5d2390b55419 | -6.65819 | -58.82391 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 837f8c37-8ffd-32af-8a34-0666ebc46fe4 | -7.46189 | -59.89174 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc97fbeb-1018-3660-a0e7-d49da1a22888 | -6.9304 | -59.52773 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b665ec0e-7bd1-3fc1-b4d6-5552f9cbf068 | -6.94416 | -60.13072 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27a9418a-63c1-3cb0-a394-4e235208e41f | -7.07718 | -59.21927 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3be94b9e-6430-32b0-9be7-b22da11b44dc | -7.41897 | -60.01049 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78900466-3b62-3616-a4b9-32cf69500d5e | -7.33164 | -60.61897 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5fc5c4d-88e5-3cd6-ab52-fd36a81b49fa | -7.29735 | -60.62819 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README57.md)
