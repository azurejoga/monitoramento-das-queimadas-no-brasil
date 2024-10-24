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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32629116-95ba-3ae1-9aa5-49c02dc88f00 | -16.9792 | -57.5223 | 2024-10-24 07:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 75919918-1a2c-3660-8b93-feaf319bdf97 | -17.0184 | -57.5178 | 2024-10-24 07:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 6fd424ba-e28f-3f7c-ad55-2036b2570df8 | -17.0188 | -57.4973 | 2024-10-24 07:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| ad1df07c-29f5-3d54-afb7-69745ad0ecdb | -17.0381 | -57.5155 | 2024-10-24 07:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 50632463-51e9-3068-a083-52d407821a9f | -17.0384 | -57.495 | 2024-10-24 07:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| bd32013e-4cfc-3880-81ca-cae362faffa0 | -17.0387 | -57.4745 | 2024-10-24 07:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| e179ff70-870b-3f3f-9234-dcb9d87b1b12 | -19.5071 | -56.6619 | 2024-10-24 07:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 28dc0064-e230-3353-903a-8f75b55214fa | -19.5465 | -56.6983 | 2024-10-24 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 2d52ebdc-5f0f-3131-bfd8-4d305ab45c9d | -19.5469 | -56.6773 | 2024-10-24 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 6ac85a75-05c2-3949-a9a0-42d4e6deac8a | -19.5666 | -56.6954 | 2024-10-24 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| f624001c-ca98-363e-af6e-ac88c42664f4 | -19.5669 | -56.6744 | 2024-10-24 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 132.8 |
| 8cd10263-476c-3630-8f95-ed51e6ff381d | -19.5681 | -56.6114 | 2024-10-24 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.8 |
| bcd00469-890b-336c-a5ea-53a9b3b8aafe | -19.6438 | -56.8521 | 2024-10-24 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 595b767d-3092-33fe-9c9e-b55c42822956 | -19.645 | -56.7891 | 2024-10-24 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 5c3a6cc0-d353-3dfa-ae97-e464493fca28 | -19.6453 | -56.7681 | 2024-10-24 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 8e121ae8-bbe9-3bab-a25d-b64991675b50 | -19.6457 | -56.7471 | 2024-10-24 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 128.3 |
| e498755b-f8bd-3af0-934b-a073d0f687fa | -19.6461 | -56.7261 | 2024-10-24 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.0 |
| c8fbc7b9-2378-3898-ad1b-707368bc95dc | -19.6658 | -56.7443 | 2024-10-24 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.0 |
| eca58c5b-fb25-3b37-948f-cdaad9d7c4d2 | -19.6662 | -56.7233 | 2024-10-24 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 221d64cd-0be0-3a37-b1c7-5e6c70662206 | -17.0387 | -57.4745 | 2024-10-24 07:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 5529c9c5-07e7-3047-b5b5-6f63a5a3bed0 | -17.039 | -57.454 | 2024-10-24 07:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 96e6843a-2ddc-3ae4-844b-b885e9a49143 | -17.0381 | -57.5155 | 2024-10-24 07:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| b27016de-0dd2-37a1-9f61-69c1d29363a1 | -16.9596 | -57.5245 | 2024-10-24 07:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.7 |
| 35aadd20-865b-3e77-a989-76c53877e538 | -16.9792 | -57.5223 | 2024-10-24 07:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 5622217f-f7fd-3669-ae32-129a06dfc840 | -17.0184 | -57.5178 | 2024-10-24 07:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| f767ea1c-6790-3900-a04a-a5fd72a5357c | -17.0188 | -57.4973 | 2024-10-24 07:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 9b41e4e7-2caa-313b-a2ea-810904134d2a | -19.5071 | -56.6619 | 2024-10-24 07:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 7065e396-f0a6-301f-aec6-0f366fbb5ee4 | -19.5075 | -56.6409 | 2024-10-24 07:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| b3978d38-90ed-3713-854b-7b4d778e4aef | -19.5465 | -56.6983 | 2024-10-24 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.9 |
| a4c7fb63-f125-34b7-af2e-08e722552f22 | -19.5469 | -56.6773 | 2024-10-24 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 065748c8-dbce-300d-87f0-8d8286ed2510 | -19.5666 | -56.6954 | 2024-10-24 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 105.8 |
| d56c2199-8602-3511-b134-787f9b2c0d8e | -19.5669 | -56.6744 | 2024-10-24 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 7d69e7c9-5349-398b-bafa-b6210d89cb2d | -19.6438 | -56.8521 | 2024-10-24 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 6bf9c649-25c7-3263-a6cc-17bb77de1079 | -19.6453 | -56.7681 | 2024-10-24 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 2364facc-fa4c-3237-a149-d699da00ab55 | -19.6457 | -56.7471 | 2024-10-24 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 118.4 |
| daadc169-53a9-35f4-9962-5232f7a697ee | -19.6461 | -56.7261 | 2024-10-24 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.0 |
| f152dd3a-09ad-35f9-ba77-aec4dee6c78f | -19.6655 | -56.7653 | 2024-10-24 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 13100634-99b7-3bee-92af-c3f7e44afb71 | -19.6658 | -56.7443 | 2024-10-24 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.0 |
| a40e0abd-ef60-3906-ad0e-18041b08b17a | -19.6662 | -56.7233 | 2024-10-24 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| ab48c4d4-9e1b-3d2f-a2bb-bf59fc3f80b3 | -16.9596 | -57.5245 | 2024-10-24 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.3 |
| e2595db8-b154-3538-9d99-08bca4ed2ae8 | -16.9792 | -57.5223 | 2024-10-24 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| ebfb0f10-be5a-3de9-a542-fa00392cc81a | -17.0184 | -57.5178 | 2024-10-24 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 69a601de-1707-31bb-be74-6b03dd7af7b2 | -17.0188 | -57.4973 | 2024-10-24 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 935b6d31-0553-336a-b9cd-efe872e767ea | -17.0381 | -57.5155 | 2024-10-24 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 66407d17-140b-306b-8d6b-278477b933de | -17.0384 | -57.495 | 2024-10-24 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| e5352250-10e8-399e-8f3d-fcb838bc8e97 | -17.0387 | -57.4745 | 2024-10-24 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| 92fcfe85-8532-33e8-a6c5-92a0515936c4 | -17.039 | -57.454 | 2024-10-24 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| c68ff3dd-c1ce-32ae-bec0-cfdbffd5528b | -19.5071 | -56.6619 | 2024-10-24 07:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| aa80f329-bf25-301d-bfb9-e33ea46d048f | -19.5075 | -56.6409 | 2024-10-24 07:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| fada2cb3-ad58-3f0c-a8f6-f5003a9aefb2 | -19.5465 | -56.6983 | 2024-10-24 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 7a8e2ffa-2d2e-3818-8210-1ad8df0d3967 | -19.5469 | -56.6773 | 2024-10-24 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 22cf5fce-e3f2-37ff-9bfb-6f2031c107ad | -19.5666 | -56.6954 | 2024-10-24 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| ee4b043d-2a57-30ad-a11d-649c7ba7cb08 | -19.5669 | -56.6744 | 2024-10-24 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 123.5 |
| 83fb4bbb-5100-3c66-bbf1-fa32ec113265 | -19.587 | -56.6716 | 2024-10-24 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 85a01300-f7e5-3c55-afee-c2781238f68a | -19.6438 | -56.8521 | 2024-10-24 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.2 |
| e6572a39-6be0-33bc-892d-6963692d5cb1 | -19.6453 | -56.7681 | 2024-10-24 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| dd839d17-52df-35b4-a2db-25e2ca77b8de | -19.6457 | -56.7471 | 2024-10-24 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 7796aa1a-888d-323f-82e5-1969104caa1d | -19.6461 | -56.7261 | 2024-10-24 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 830691a0-869f-3cd6-9777-1c874a11148b | -19.6655 | -56.7653 | 2024-10-24 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| de5edba1-da6e-331d-ad7c-13281e43d865 | -19.6658 | -56.7443 | 2024-10-24 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| edc5e564-7b75-31ae-9043-88a489a2808c | -19.6662 | -56.7233 | 2024-10-24 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.3 |
| 1f6ef699-ba75-374b-843f-0975bf33fb16 | -16.9596 | -57.5245 | 2024-10-24 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| c38ee50e-3373-3624-8b4b-35d9aa8dea6c | -16.9792 | -57.5223 | 2024-10-24 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.2 |
| b19051f6-d987-3693-b626-1b981033a02a | -16.9795 | -57.5018 | 2024-10-24 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 9799c54c-5f65-3001-ba5a-a076517db321 | -17.0184 | -57.5178 | 2024-10-24 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| ef515d51-f0d0-3af9-aab2-a68517a5bbbe | -17.0188 | -57.4973 | 2024-10-24 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 66297ac3-70a4-390d-98a4-3b593ae95235 | -17.0381 | -57.5155 | 2024-10-24 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 46d8872e-96cc-3112-9b7f-34f392597def | -17.0387 | -57.4745 | 2024-10-24 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| 52fc2e18-4f03-36c4-b67b-98591ccd0fd9 | -17.039 | -57.454 | 2024-10-24 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 0fb1e907-32ef-3b08-a286-a0d907faa314 | -19.5071 | -56.6619 | 2024-10-24 07:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| c63d15eb-0c6d-35c7-b00e-e12fcaa1daff | -19.5465 | -56.6983 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 3d972709-3c02-3345-a154-b40ceb7a6abd | -19.5469 | -56.6773 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 45ab7963-4436-3408-9b09-888f24dcfe2f | -19.5666 | -56.6954 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 8334da30-bada-3c0a-a6dd-71672cdbe040 | -19.5669 | -56.6744 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.4 |
| c857e1c3-eb1d-3fd1-bdd9-abadf807e161 | -19.5681 | -56.6114 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 4025f025-0ba0-3eee-8add-508db5149af8 | -19.5866 | -56.6926 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 09055eb8-c066-373a-ae64-780cc0ffc191 | -19.587 | -56.6716 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 248e06d0-c5b6-3030-99db-3b2ca5cfe784 | -19.6438 | -56.8521 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 91a7661c-253d-3e89-a697-ed76e354962b | -19.6453 | -56.7681 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 8380c750-6c04-3ee2-b540-67e91fe069b0 | -19.6457 | -56.7471 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 138.5 |
| a0d967bd-674d-3432-8f7f-a6ffd044cca0 | -19.6461 | -56.7261 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.4 |
| 4a4ec93c-69fd-3891-9cde-a827345403f0 | -19.6655 | -56.7653 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 5e09092a-714e-3e85-b4d7-c8389245f3c1 | -19.6658 | -56.7443 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.9 |
| e7e8f167-dd46-34f6-8eb9-d8fe2a34d2d8 | -19.6662 | -56.7233 | 2024-10-24 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 074fcde2-3ac3-3556-8340-51fdac993f6c | -16.9596 | -57.5245 | 2024-10-24 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 5e6c5bb6-66a5-3f77-9358-5a906217d3d2 | -16.9792 | -57.5223 | 2024-10-24 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.8 |
| ed4c7f2b-4b57-3e56-857b-577a8461af72 | -16.9795 | -57.5018 | 2024-10-24 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 8748dd28-8ca8-38af-b92a-783f2f8bbe48 | -17.0184 | -57.5178 | 2024-10-24 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 98b3196e-29e5-3a2c-bd9b-70f2cf23639d | -17.0188 | -57.4973 | 2024-10-24 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 0388f4c7-edac-3b9c-bd69-b546c1b10e35 | -17.0381 | -57.5155 | 2024-10-24 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 83d35b45-bd47-35d6-936d-6a28fc4d4d4f | -17.039 | -57.454 | 2024-10-24 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 1f173a41-70c8-3d13-875c-893effd30a18 | -19.5071 | -56.6619 | 2024-10-24 07:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 0ade4dc6-77b6-3d98-914f-4fbada1c1513 | -19.5075 | -56.6409 | 2024-10-24 07:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 41dda342-d0ee-3879-a8a9-69c448348b23 | -19.5465 | -56.6983 | 2024-10-24 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 2b5aad2e-84bd-3a02-a07d-19f92843b6d7 | -19.5469 | -56.6773 | 2024-10-24 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 2823dc62-8a62-3682-909a-e43cb5abad47 | -19.5666 | -56.6954 | 2024-10-24 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 5a1ebeab-66fe-359b-ad9b-d4a17627c7c2 | -19.5669 | -56.6744 | 2024-10-24 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 1b3fba8f-d7d1-3e30-ac3a-b4a5a3aaaedd | -19.587 | -56.6716 | 2024-10-24 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 4e016256-707a-3ba5-ae01-fc9370020433 | -19.6438 | -56.8521 | 2024-10-24 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 3b13e545-d28a-3bf7-b661-a6bfa0b7f3cb | -19.6453 | -56.7681 | 2024-10-24 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.8 |


[Clique aqui para ver as próximas entradas](README112.md)
