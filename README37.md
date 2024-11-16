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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3166fd1-9556-35ee-9117-511f34f09bba | -7.49811 | -47.35347 | 2024-11-16 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b78ddd9-4360-3ce7-9c48-b3486de4ad1c | -6.16745 | -41.16802 | 2024-11-16 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9d5f76fa-5b0b-3add-900f-72cc5c453359 | -6.66226 | -47.87723 | 2024-11-16 04:25:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d41dcec-a4ea-3d55-914c-eddd7db5d60b | -11.80473 | -47.0612 | 2024-11-16 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91baf7ed-f339-3745-9262-a917fde378f0 | -7.55279 | -35.23126 | 2024-11-16 04:25:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ffac997-7bac-35b7-95ca-2c809c6dcdd4 | 0.79567 | -50.74311 | 2024-11-16 04:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 21bf95bc-b6e3-3053-8602-fa36d206965e | -8.03894 | -43.78955 | 2024-11-16 04:25:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5e40b6dd-c32d-3c06-9620-563983c27a47 | -6.98893 | -39.66036 | 2024-11-16 04:25:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 94ce067e-7e30-3f1a-8574-6917f794e23b | -0.33775 | -49.93745 | 2024-11-16 04:25:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 447de907-c6ba-31b0-bba3-f0e8e15613d2 | -5.91029 | -46.23054 | 2024-11-16 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b83f6194-7d85-3082-bc6c-0626dff45dde | -11.80805 | -47.06173 | 2024-11-16 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11af80b8-f62b-3d7d-ab66-01d64ef8ac81 | -0.64969 | -49.39602 | 2024-11-16 04:25:00 | NPP-375D | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3aa7a94f-16d0-3972-bbbf-fa25eac902e5 | -12.69075 | -43.37611 | 2024-11-16 04:25:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c894137-d723-3674-99d2-237ac4013e96 | -11.8075 | -47.06527 | 2024-11-16 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5225374-81ac-3c99-ba00-13e381186272 | -11.80362 | -47.06826 | 2024-11-16 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4be60bb-4ccc-3d34-b6e3-3d0c08e1edbf | -6.3789 | -47.51243 | 2024-11-16 04:25:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c59835a1-a3ad-3295-8aca-54663fa1fb83 | 0.66107 | -51.76358 | 2024-11-16 04:25:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4013eae3-c190-39a4-8ec6-d334f3fd890d | -7.40111 | -40.39532 | 2024-11-16 04:25:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| aa10a681-135d-38cd-ae7d-d34214abce97 | -8.27848 | -45.96964 | 2024-11-16 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f99fc6b4-cef5-3cbe-977d-33c43ca38b7f | -6.64066 | -39.71419 | 2024-11-16 04:25:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fa0c078f-2e21-3b99-b8a3-b0f46425edbb | -8.27515 | -45.9691 | 2024-11-16 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c08df7ed-9ff5-3da5-bf10-41ee08dfb5bb | -5.48582 | -43.76413 | 2024-11-16 04:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74993035-b046-34b4-bf84-d54b78aab509 | 0.1174 | -49.84835 | 2024-11-16 04:25:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 559ff9aa-ba77-366f-8c5f-6272a1e02dd0 | -11.53264 | -45.00449 | 2024-11-16 04:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7bb59ba-119d-3914-a65b-8bd63f876f2f | -4.36492 | -50.81684 | 2024-11-16 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 565d2de6-04e5-39cd-9869-1d7d37fcb733 | 0.79062 | -50.73956 | 2024-11-16 04:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d17eae4-43e2-3ece-b727-2a76158c8b7a | -5.90059 | -42.27912 | 2024-11-16 04:25:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5c7cb20f-2bf2-3c3e-9460-f71da002f3ca | -5.90366 | -42.28419 | 2024-11-16 04:25:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a05fa000-be4d-3646-a996-674ab4aeff9c | -8.28181 | -45.97016 | 2024-11-16 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfd7fb6f-488d-3595-8664-a20054cf17eb | -5.8144 | -42.51144 | 2024-11-16 04:25:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f1e98325-cbc3-379b-bdd6-48f15581b5c5 | -11.53559 | -46.75038 | 2024-11-16 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 35366595-9afe-342d-8157-2f7478e2cf64 | -5.88888 | -46.04271 | 2024-11-16 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 264a7e1d-c82a-39c8-a5e8-909484f9ff36 | -16.09248 | -60.08961 | 2024-11-16 04:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c86b03fa-7da4-35b6-b9df-cd84c5aa852b | -17.63411 | -57.56156 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 4587a9ab-0209-3e83-bbd4-c668d4dbae3b | -17.69529 | -57.5085 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 181c8b93-b212-3982-9665-5fecf93ae1a7 | -17.63916 | -57.56271 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 4735b4d0-9b56-3c2a-9244-742ecafb45b9 | -17.35997 | -57.4387 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 23070b41-bb4b-3172-aebd-93ec28447715 | -17.65865 | -57.5446 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8f7ae313-b0e1-3080-9fed-68c3e99cda6b | -17.58308 | -57.50196 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a8c4a9e0-aedd-358e-83d9-269038e89339 | -17.70031 | -57.50963 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 11a8d0e6-e88d-3299-957a-aaf335fff3da | -17.69166 | -57.48499 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1cf1b604-faba-3d33-887c-5d59de538c77 | -15.89228 | -59.26683 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1e4d88b1-2d4a-3278-a29c-835cf05ff198 | -17.689 | -57.57723 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8e76ea50-9516-371d-ae9d-963923dd6fcc | -17.58102 | -57.58838 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 9f703a3f-32bd-3567-9bc7-a7c5e0b8c44f | -17.63853 | -57.5658 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| b8365d3b-80af-35dd-b579-3b6230792824 | -17.81054 | -57.55304 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a98c89fc-5d41-3805-bab5-57ba0c6021bf | -17.57003 | -57.5238 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b8248289-8a36-354b-8e86-f32c0d6b11d6 | -17.0712 | -57.41795 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 98a7bd23-a09d-38df-887c-a12a952049da | -17.25452 | -54.18024 | 2024-11-16 04:27:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70815902-1bbb-37fb-8be8-0cc047db4517 | -17.5766 | -57.58414 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 7e9b64d3-c012-325d-8762-cf2872e7cd2b | -17.69206 | -57.57498 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4eafdbb4-e12e-37f4-8009-5019d6d48f7a | -15.90328 | -59.27234 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 169e8bd5-df35-3200-ab01-1147cbad1ed6 | -17.61329 | -57.5601 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 921f5f57-932e-3aca-af92-1c4ed6b2671b | -17.56766 | -57.56194 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b902ae69-4f87-37fe-95a5-6de5c0357d8c | -17.57286 | -57.45733 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f406ae27-af9e-3c8a-9c7b-753c803257a6 | -17.56509 | -57.54844 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9dd7a871-0f82-3307-825b-febd44c42971 | -17.54738 | -57.53153 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8750ea13-f586-3b80-a68a-c6061c19af8c | -15.96808 | -57.28187 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de56f695-f7fd-3ec1-ad95-780a960f8880 | -17.09316 | -57.47792 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 401c0204-c84f-39d1-ac8d-5337b062ce7a | -17.54925 | -57.52232 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0e0c99fe-181b-38ff-8284-d227a41a54d3 | -17.56771 | -57.43083 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 44b5dd7a-160d-3654-9439-8b5498a04e1f | -17.66245 | -57.55188 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 7c25ac83-4b34-3fea-9ace-1462f772f86c | -15.89754 | -59.27068 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5207accc-9122-3593-ae36-b0e25ca4ef93 | -17.58304 | -57.48515 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 30f5f511-c5b3-3f4a-a0d0-44ca64d961a0 | -16.09752 | -60.09575 | 2024-11-16 04:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 887d982d-46cf-367a-97f9-02a96c57131f | -17.56952 | -57.55268 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5b8b4764-2c9a-34f6-8094-b86818308720 | -17.55429 | -57.52346 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| b719c09d-f7b6-3f12-bec5-ffa28fd9aac1 | -17.04666 | -57.43506 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ecc1488a-e692-3c22-ad08-f30602217c5e | -15.91552 | -59.2719 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 57302d31-5c6c-344e-831c-60d14fb01371 | -15.91482 | -59.27006 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f306ba59-3d6f-39cf-84a8-4659184b5814 | -17.70279 | -57.57418 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f14e85a6-5c93-3bf5-b637-3efffb3bb747 | -17.5689 | -57.55576 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 24d73e1f-b226-3113-aa8d-274a4337ee93 | -15.91398 | -59.27398 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 88e4b11b-fbc9-3703-a4ac-ad11ff9e73d7 | -17.5619 | -57.53804 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e35d945f-ffac-3c1f-be95-cc0f03169867 | -17.69667 | -57.48612 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d279ec3e-bb82-3511-8c6a-a13ce7781965 | -15.90979 | -59.27023 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cacef927-459f-34b9-a90c-90704cf1fe80 | -17.63978 | -57.55963 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 736de88d-88e0-387f-b892-8a005d7ec271 | -17.8168 | -57.37374 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 763c5827-fe69-3c3b-86ce-189b22e1ed4e | -15.97316 | -57.28317 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 259c6245-9c6b-3462-b4c9-b15395c641b8 | -17.8245 | -54.54044 | 2024-11-16 04:27:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 04bcf5a4-dd44-3fb9-b360-b91452977924 | -17.57467 | -57.57973 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 87cbd855-c411-3f25-a165-bed8a698c663 | -17.59187 | -57.49355 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b614e141-3def-37fa-96ed-0e4bbbc35e4d | -17.55119 | -57.53885 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d66791b1-fea0-3356-be19-008483fef822 | -17.36561 | -57.43678 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| fd8d1496-6d5a-3437-b0f2-89ff2a612144 | -17.57998 | -57.50045 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 48afaf94-db36-3b5b-a471-65483a8be3c9 | -17.58672 | -57.58645 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 9e9db133-997f-395b-9af3-c9e4ed7c2f4d | -17.68138 | -57.56262 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 09ad9a50-b191-314b-95c9-b0238782ed98 | -17.60008 | -57.47071 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 810ea8be-dad2-3b29-af73-6955748bee6d | -17.59178 | -57.58758 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| fbec9ed2-9cfe-3cb5-af9e-68d82214e578 | -17.59065 | -57.49087 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f9c73a42-ffe8-3614-8256-dceccc351a4a | -17.66872 | -57.54691 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9b4aa2ef-6219-3346-9eb3-286e49b30443 | -17.56662 | -57.46229 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cae9c00f-2deb-31ef-8497-4fa2272c5aee | -17.68704 | -57.56068 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a1c85156-0926-3afb-b17c-609da02db631 | -17.64103 | -57.55347 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| da04dbd5-0437-3d2d-ab53-31485ab2a857 | -17.58863 | -57.57716 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.3 |
| a5e39c3c-e351-3b98-9310-6051ec4e380c | -17.57923 | -57.47791 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ce24ae09-3876-3e16-84d8-edf09e17312d | -17.58435 | -57.49584 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 38b1ba0a-8c8f-3991-9e54-2ab3dc0acaaa | -17.23502 | -57.18797 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| da0e1770-0e3f-3abb-965d-bdd5fe22e524 | -17.66368 | -57.54575 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 17ddf711-bdd0-3d97-9375-ca0764bab612 | -17.58625 | -57.48669 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |


[Clique aqui para ver as próximas entradas](README38.md)
