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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3af35e5-0faf-3954-ab6e-d80748c49c89 | -17.22209 | -57.24013 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| adc6d592-e986-3d92-aa0e-142008f987a7 | -17.22141 | -57.24387 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 576b1ce0-3fea-3517-b0b5-6f94915827a3 | -17.22126 | -57.2393 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| f2671438-cbd5-3ddd-9dbb-f3684719d869 | -17.22074 | -57.24762 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 875334f5-d655-3fc8-bae6-5a5fdd8c232a | -17.22065 | -57.49212 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| be80695f-6fbe-34d2-893d-a5e2a1ae1540 | -17.21914 | -57.25053 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2634822e-6c98-36e8-8721-337ae11bd4d9 | -17.21797 | -57.48353 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 05b481e5-d42a-32a9-8855-9f7c05f90c9f | -17.21724 | -57.48741 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ce0c6b36-8f36-3264-8aba-2d7695cb100c | -17.2153 | -57.25432 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b4356320-b994-33be-bfe7-d5352219b428 | -17.20631 | -57.47715 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 125a6ee8-bcae-30a7-9189-9a74572feb96 | -17.20218 | -57.47632 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c7a34e99-c095-302f-8c8a-757791083b42 | -17.03997 | -57.5052 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e06a58e9-ec5e-376a-9811-e70e2e902127 | -17.03637 | -57.5248 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 0a2985f2-5d8c-3d27-ac53-7aede9b8c710 | -17.03582 | -57.50436 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4e92b061-2ca0-3272-b13b-311caf86df7a | -17.03564 | -57.52872 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 78ea6ac9-2bcb-369b-847d-c7173fff24e7 | -17.0351 | -57.50827 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| eb81984d-125d-3a19-947f-b43dd77422a9 | -17.03221 | -57.52395 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 3f73c9fb-f6b2-3ba4-92b6-4cd9a4b42c8b | -17.02825 | -57.49876 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 00753a58-0f00-3a98-9dfb-98f2962777a1 | -17.02681 | -57.50658 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d6ee922c-4c93-3618-bd54-cb83f177e003 | -17.02391 | -57.52225 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 62e4f3aa-07ef-3b78-b60f-b90c826cde00 | -17.02319 | -57.52617 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| cc173f69-a065-3772-b85f-3e37985280e6 | -17.02069 | -57.49318 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0f38b07d-13d6-39f1-a6ce-9fa993395c3b | -17.01976 | -57.52141 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 1926ebdd-23d9-32b3-ab2e-bdd35e062be7 | -17.01904 | -57.52532 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 90a430d4-585a-32da-a7d1-22c2a8225b58 | -17.01654 | -57.49232 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8792b017-7cc2-3e9d-bdff-802ceb43d30f | -16.97188 | -57.5239 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 0e70ee7f-3f80-3ec7-bb43-de19e89ac9d7 | -16.96773 | -57.52305 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 24b03719-c4be-3157-84e4-8708a7d7f1f3 | -16.96357 | -57.52221 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| c6d9bfd4-4625-362b-b00c-15e441914c1d | -16.96283 | -57.52613 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 2b0c3cab-2bf1-335b-a7af-5855c4f63137 | -16.94738 | -57.53932 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 559b506c-a6b3-38de-8b40-4a42e3208d21 | -16.94663 | -57.54325 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ebfd9642-a766-3198-95a0-876a9e69eaf8 | -16.94459 | -57.69154 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 65a15f83-0741-3372-944e-08b60215625c | -16.93889 | -57.53458 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 4f1029a3-d3bb-3508-8a78-8a5bc1ab6edb | -16.93762 | -57.51799 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 18168637-267c-3f0b-b1fd-cc9ca5abd7d3 | -16.93418 | -57.51321 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 635caae9-2220-38c6-b77e-793186849008 | -16.93401 | -57.53767 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 4d646fd1-d4b3-3483-b16b-8f6d5cce4e19 | -16.93201 | -57.52501 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| f857b48f-cae1-37ec-8946-190244f76d96 | -16.92858 | -57.52023 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a25ff256-6f6b-3863-997f-fdf51a0c1202 | -16.90655 | -57.49944 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 2abb479d-5ab2-36d1-b515-0b0dbf65edbd | -16.88469 | -57.66385 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f397209f-0a9d-3c92-80ab-6a2570871c09 | -16.88394 | -57.66787 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8a47e576-e940-3766-9735-6e2c82ad5b51 | -16.88319 | -57.67189 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6b2283a2-ea92-304a-8827-0d7086ae40d8 | -16.85917 | -57.68372 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cc5a645c-ea41-34f1-97ec-aba53f434a62 | -16.85841 | -57.68775 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 123c71f5-aa88-3a1a-b03d-4bed4b9e9849 | -17.07146 | -57.42693 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e838488e-223e-3d28-b594-e7f12e1a7874 | -17.07075 | -57.4308 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6f68c5e0-8183-374f-8143-3d6ab2c285c4 | -17.06982 | -57.48295 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a38920a4-a50e-3523-802a-78381039e78b | -17.06568 | -57.4821 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 59b061ba-b33d-3dec-8227-cb94cedcd48f | -17.06167 | -57.45709 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6aeaaa74-60cd-3c5b-8725-bb39adc8bb8f | -17.06109 | -57.43685 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0265abfb-f6a8-36cb-a8fd-80a49024785b | -17.05825 | -57.45237 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 495dddcc-291b-32f0-807e-bde374cb89c0 | -17.05754 | -57.45624 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 53ec83f2-272f-38e6-b041-46bddd10f961 | -17.05741 | -57.48042 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 5fb6ea9a-05a0-3936-9231-6ec0e842b536 | -17.05483 | -57.44764 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| afc3a6c9-4095-3bb8-858d-0c336269d8f4 | -17.05327 | -57.47957 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 01d56a18-ece7-3c5d-a481-e2550c2281c4 | -17.05213 | -57.43904 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 5bd9e0fb-9191-3160-8a79-f1aea13ba87d | -17.04984 | -57.47484 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| db846b5c-7193-3a7a-b9bb-054980ebdcb8 | -17.04942 | -57.43047 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7d4bb652-b811-3a04-ac3c-9e8b1fc87400 | -17.04928 | -57.45456 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d53071a2-883f-30ad-8444-0d7771c04a56 | -17.04913 | -57.47874 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 80427f50-32d8-312b-9b39-52cc67ea4e1a | -17.04642 | -57.47011 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6a15c77c-0e1e-320f-ab7b-02d405e91f20 | -17.04586 | -57.44983 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c80924ad-fcce-3163-8c96-e6460bb172d6 | -17.04529 | -57.42964 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b1872dea-792e-3299-ada5-70be4fa23ac4 | -17.04316 | -57.44125 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b950fbf0-b19e-363f-93e6-564358300d96 | -17.04173 | -57.449 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1184cf83-0fad-3cd7-905a-76974ffc1f8a | -17.03958 | -57.46065 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5c845ee6-fdc0-3b26-b391-857da75d0e4e | -17.03934 | -57.39239 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5cc280b1-653c-35a5-a6b0-e7b1399ac5b0 | -17.03886 | -57.46454 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 05386aca-5dde-3e4e-91ec-28251a827aff | -17.03863 | -57.39624 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7d2f3f48-e8d3-3f43-b17b-4f63d9fa52fe | -17.03616 | -57.45593 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9ae9ca38-8c17-38ed-8cb4-6b3b80dfea60 | -17.03522 | -57.39157 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b05fd304-f2af-3b0f-a536-3e325e930f0c | -17.03451 | -57.3954 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9484361e-8a84-3cb8-8737-d420d95606e7 | -17.02916 | -57.47063 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b1f820a0-c086-3b11-a354-e5477bdda36c | -17.02843 | -57.47453 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9b3e07e1-3d98-395f-8a3f-41a3bafda057 | -17.02574 | -57.4659 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e11d9479-c962-3d91-a518-ef140df13903 | -17.02502 | -57.46978 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c2ec0284-235f-36ef-b74a-8d3d5cbecd72 | -17.0209 | -57.37672 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 356f91c6-c8e7-3e85-bb72-f6bf2261c85b | -17.00999 | -57.36655 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1113b6a2-26ba-3474-a556-ea35348d576d | -17.00712 | -57.3819 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1a9245dd-2fba-3979-8f06-c8a40f1b5e74 | -16.99981 | -57.35257 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 6f5aa060-2917-3845-98d5-112b23f5e865 | -16.99499 | -57.35556 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| dd13b3a1-aae5-3b5e-a1aa-4c612c73ee76 | -16.98993 | -57.38242 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 72ba29ca-e0c5-36b7-b914-8990e5a977d3 | -16.98315 | -57.38594 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e78d4ad8-93c1-311e-a2a3-fbe57f94a5ed | -16.89164 | -57.26927 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 18595ed2-256e-3486-a039-bea3eb58842d | -16.89096 | -57.27307 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e4fb6b0b-b5d5-3e89-bcf9-c8ea00425fc7 | -16.88686 | -57.27225 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9080017d-d7e2-3391-beca-8cafe684a4cb | -16.86567 | -57.27193 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bc868895-6d5a-363e-99b3-383b05e7d542 | -16.70238 | -57.45232 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5bc61537-8af6-3a32-b50c-e7829880f2ec | -29.8151 | -51.17558 | 2024-10-25 04:44:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 1e569a51-a390-3e5a-8f31-32a6bbc64cea | -29.7776 | -51.1743 | 2024-10-25 04:44:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 114f273b-1b40-365e-bc75-c42a7d83c294 | -23.64981 | -53.46595 | 2024-10-25 04:44:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a0489927-3c7e-325e-be1e-1243e71fb729 | -25.19103 | -52.78938 | 2024-10-25 04:44:00 | NPP-375D | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c4f8a1f2-10eb-3b2c-805e-6fc1fb208626 | -23.78606 | -55.30129 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| c5976efb-f6de-3c68-b23d-8f60770f89bc | -23.84949 | -55.32225 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8d70eaa0-b13a-342b-8b43-9ad05abc9bec | -23.84675 | -55.31758 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f00812e3-596c-336c-a87d-dd32a989b3fc | -23.84608 | -55.32156 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 59d9b4d4-047f-3455-90ef-fe2a69533965 | -23.84268 | -55.32085 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 0bf6abdd-3e96-3089-8891-e1a124debb69 | -23.8229 | -55.3127 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6fe9cbe6-df92-3214-b817-39d3cffb10d6 | -23.82286 | -55.29212 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6e269b6f-1c96-324e-8b14-d99a687eb83c | -23.81739 | -55.28279 | 2024-10-25 04:44:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |


[Clique aqui para ver as próximas entradas](README79.md)
