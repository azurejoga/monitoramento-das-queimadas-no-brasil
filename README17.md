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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01145098-e1d4-360a-88af-f0bb231904d0 | -12.3295 | -63.705601 | 2024-09-29 01:33:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8625162e-1390-3d48-a788-06b16d581cad | -11.2318 | -60.445301 | 2024-09-29 01:33:30 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 04b6ce66-54ad-39f3-8312-1051d31b4d64 | -11.2351 | -60.460098 | 2024-09-29 01:33:30 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1642b198-679d-3b2c-aedc-748ce2ca2e0b | -11.2368 | -60.467499 | 2024-09-29 01:33:30 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 34a1b005-ca10-3303-aa68-e887eeda9262 | -10.6872 | -58.507999 | 2024-09-29 01:33:31 | METOP-B | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bfb76f18-601b-3337-9a6d-9c25ab2e66e7 | -10.6894 | -58.516998 | 2024-09-29 01:33:31 | METOP-B | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4219527-f61d-330f-aa84-572d00f1aade | -10.6915 | -58.526001 | 2024-09-29 01:33:31 | METOP-B | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d9e71c8-799d-3cf6-8d18-74e37f096245 | -11.1566 | -60.702801 | 2024-09-29 01:33:32 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cc1836fc-354f-37c6-aa16-d61e30c67380 | -10.9838 | -60.758499 | 2024-09-29 01:33:35 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0f10df4-7c58-3688-8b36-2e13553ac286 | -10.9854 | -60.7658 | 2024-09-29 01:33:35 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 595d327a-5aba-310a-9294-f7183f8d7ca1 | -11.7259 | -64.096603 | 2024-09-29 01:33:35 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f27538d2-33d9-3993-9b13-9356b1ea3ade | -11.6836 | -64.043198 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 47db1ea9-ffed-3bdd-8246-e60317775705 | -11.5986 | -63.698601 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f79d8ef-8c01-31ed-84f2-ac5bdb35e20b | -11.6001 | -63.705898 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a3f92400-7c97-32b1-b187-cbbb8d234a29 | -11.6577 | -63.970798 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3177b9bb-1e3c-3aad-b891-b741d9a238fa | -11.6593 | -63.978298 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 679350bf-e808-3593-bae1-41ba9e9d7199 | -11.5837 | -63.724899 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a3151ad4-ca52-3694-9ad8-6081c19e8a42 | -11.5853 | -63.732201 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fdf2a3f3-8387-3d89-96d8-024249adccd6 | -11.5739 | -63.7271 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0b2e02fc-ad8f-33ed-9529-e852b051ec0c | -11.5755 | -63.734402 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7b253c26-c4ac-322e-b4e7-a5be1068da98 | -11.5771 | -63.741699 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec3e7c7-ea91-3c10-871e-f910351da535 | -11.5562 | -63.692699 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e5f49999-bee0-3852-b9d5-43e13378ac1e | -11.596 | -63.8759 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc3c118a-504b-359f-a2d4-2799adf0f7b7 | -11.5976 | -63.883301 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9eab7c7b-3079-33ed-b00f-704323f19c22 | -11.5992 | -63.890701 | 2024-09-29 01:33:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e9c8171a-bafb-33f6-8247-0466e39efe7e | -11.583 | -63.8634 | 2024-09-29 01:33:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ffba97c9-1282-3b9f-9c4b-c59634613e57 | -11.5846 | -63.8708 | 2024-09-29 01:33:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed686a8-2ae8-31ab-87ed-90fbe9abc138 | -11.5862 | -63.878101 | 2024-09-29 01:33:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e8e23bd9-7ca5-32b8-a0db-5392800e1c7b | -11.5732 | -63.865601 | 2024-09-29 01:33:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e0dcca0d-1b63-3d7d-929c-704d3cf14626 | -11.5748 | -63.873001 | 2024-09-29 01:33:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b1b59857-ffea-38f9-bcb9-59e899ca324b | -11.5454 | -63.879501 | 2024-09-29 01:33:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 67153aa8-3d88-36e6-a64f-e9daeb39085a | -10.724 | -60.75 | 2024-09-29 01:33:39 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76fded67-fe07-3a75-bc02-fb9a87a30483 | -11.6301 | -64.988899 | 2024-09-29 01:33:40 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9db6f22a-0ee9-37ea-9962-8063edd0fd16 | -11.6318 | -64.997002 | 2024-09-29 01:33:40 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 18a9ea1e-c6ee-3c90-8336-8f802e6b189a | -11.6203 | -64.990997 | 2024-09-29 01:33:40 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| adb74c01-5132-3684-b24f-2c31b2488564 | -10.9552 | -63.576401 | 2024-09-29 01:33:46 | METOP-B | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 955e67cb-49bb-3771-8017-ed4bdf0cc45a | -10.9567 | -63.583599 | 2024-09-29 01:33:46 | METOP-B | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f2c7fe96-e331-3c40-aab9-383c293f42f6 | -10.3852 | -61.163502 | 2024-09-29 01:33:46 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d7bfd51-0282-3712-af54-8c16bc8325c0 | -10.3869 | -61.1707 | 2024-09-29 01:33:46 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2839f941-607e-3ecc-8122-b131e6d75450 | -10.9985 | -63.915901 | 2024-09-29 01:33:46 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b40c7346-a2ed-342d-914b-b292639f297e | -11.2862 | -65.251404 | 2024-09-29 01:33:46 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c371d2c1-31a8-32b2-bd2c-7b27a58b9070 | -11.288 | -65.259598 | 2024-09-29 01:33:46 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 06bc44d6-c716-302b-a546-392c6726be4b | -10.8763 | -63.8741 | 2024-09-29 01:33:48 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 43634aed-c558-3215-baee-f6dd055835df | -9.3056 | -60.3242 | 2024-09-29 01:34:01 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de9ced01-a3ea-34f1-b60f-d05de3a1b6b4 | -9.3074 | -60.331902 | 2024-09-29 01:34:01 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ef0278e-ac75-3798-a9d9-e29e69b4e60c | -10.2196 | -64.5382 | 2024-09-29 01:34:01 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 46dab20d-2323-395b-8aa7-14e0ed8931f4 | -8.083 | -55.370602 | 2024-09-29 01:34:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d8070e6-ad1a-3dff-980c-2a6d68af9e53 | -9.3863 | -60.898899 | 2024-09-29 01:34:01 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb770903-bade-33ab-a165-8bf2591e59d0 | -9.2472 | -60.697102 | 2024-09-29 01:34:03 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd18f29-8c5c-3213-a97c-eee7fe144d84 | -9.2489 | -60.704601 | 2024-09-29 01:34:03 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54eb5c16-b4fd-3d27-b1f7-79f00c6a7577 | -10.0824 | -65.042397 | 2024-09-29 01:34:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d0e86b32-52c3-3cc5-a717-c85b9dd647f7 | -10.0841 | -65.050201 | 2024-09-29 01:34:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b7625950-0d35-303d-8958-ee570359a957 | -10.0709 | -65.036598 | 2024-09-29 01:34:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 42b812cf-c801-37b3-85ad-bdc09d0d50f8 | -10.0726 | -65.044502 | 2024-09-29 01:34:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ce3a7953-cd67-3c91-9e0c-9095b0162d60 | -10.0743 | -65.052299 | 2024-09-29 01:34:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 733004a4-f22d-3544-8c63-e15e79522b0d | -10.0628 | -65.0467 | 2024-09-29 01:34:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fa5c847c-632c-3c3b-842e-5d869be34e11 | -10.0645 | -65.054497 | 2024-09-29 01:34:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| edaa1b92-3e4c-3bd3-b2d1-866503e4341b | -9.9715 | -64.767197 | 2024-09-29 01:34:06 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 51cccb6b-2b0f-3ec8-9a46-682546baf1da | -9.9732 | -64.774803 | 2024-09-29 01:34:06 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 219cc40a-43e1-3a8c-8db1-fd6e9265597b | -9.0868 | -61.121899 | 2024-09-29 01:34:07 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f231b1ef-cc4a-3698-ac60-0ebacf7fa619 | -9.0884 | -61.1292 | 2024-09-29 01:34:07 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d998adde-243c-3555-b8dc-610aa4e65f11 | -9.077 | -61.124199 | 2024-09-29 01:34:07 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbb7fb8f-2141-39b0-b3f3-1725dd0d4099 | -9.2502 | -62.433701 | 2024-09-29 01:34:09 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1da04804-dece-3b0c-951a-b7b206d75310 | -9.2517 | -62.440601 | 2024-09-29 01:34:09 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c04825e2-2bfd-3476-8f90-17d9d807cd77 | -8.8635 | -61.499001 | 2024-09-29 01:34:12 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e55b76e1-f547-380d-9d64-3ea018161a1c | -9.0493 | -62.319302 | 2024-09-29 01:34:12 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 49cee91d-1d12-3126-ba90-122bf13d5d46 | -9.0509 | -62.326199 | 2024-09-29 01:34:12 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eb83a141-5604-31bb-a757-ff8e04684aff | -9.0524 | -62.333099 | 2024-09-29 01:34:12 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9cae53b0-4e80-3292-98e3-ada2c617b004 | -9.0395 | -62.321499 | 2024-09-29 01:34:12 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be90276b-a196-3fcd-af89-712f3bc63c9a | -9.0411 | -62.3284 | 2024-09-29 01:34:12 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3a354b61-f0dc-314c-b8a3-1a68af28c228 | -9.0426 | -62.3353 | 2024-09-29 01:34:12 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 761b5ba9-034c-3ada-afbf-808d825f9a87 | -9.3025 | -65.3274 | 2024-09-29 01:34:19 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 45d0a96f-a2db-3c26-90dd-19641aa37488 | -9.3042 | -65.335297 | 2024-09-29 01:34:19 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f971741-467a-3a81-b4e5-33a850150807 | -8.638 | -63.750198 | 2024-09-29 01:34:24 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 53e578e6-a3f2-3fab-b8bd-3b4fda3fd9a1 | -8.6395 | -63.757198 | 2024-09-29 01:34:24 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7bcdb288-8064-3a56-9f7c-5fa3ccd7f32e | -9.6551 | -68.536903 | 2024-09-29 01:34:24 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d6370b80-90c8-3003-8a75-503f990f9f33 | -9.366 | -67.398399 | 2024-09-29 01:34:25 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85321cf5-c50e-30e3-873c-fc5735976e4c | -9.0598 | -67.787903 | 2024-09-29 01:34:31 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8233de8-6902-3281-a69d-de3d28dcab1c | -9.062 | -67.798599 | 2024-09-29 01:34:31 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da071059-4fc2-33d6-b095-12398ea93954 | -7.7007 | -67.028397 | 2024-09-29 01:34:51 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99d029d0-0396-356e-934e-3edb928244e4 | -6.6626 | -69.9188 | 2024-09-29 01:35:18 | METOP-B | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16b98833-88e6-3f47-ba2f-bfb38c8a1925 | -6.6654 | -69.932297 | 2024-09-29 01:35:18 | METOP-B | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58f9bcdc-4545-39db-abd5-aee9d412ea84 | -2.126 | -53.653301 | 2024-09-29 01:35:31 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26d7fb4f-c893-309b-bc2c-aece325e60dc | -2.1453 | -53.6488 | 2024-09-29 01:35:31 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 128cb282-b728-3d05-a0fc-61d9fe254b22 | -2.1297 | -53.625599 | 2024-09-29 01:35:31 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80965970-d9a0-3a7f-9b63-8624f530f106 | -2.1357 | -53.6511 | 2024-09-29 01:35:31 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efd88936-1cf1-304c-8e3d-ab3a0cd7362c | -2.1417 | -53.676498 | 2024-09-29 01:35:31 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 799f40b0-94db-34c4-8bef-ebf3032431e0 | 4.3136 | -60.942501 | 2024-09-29 01:37:43 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 197be52f-57fc-32ef-84c7-b0dfff056c79 | 4.3159 | -60.932301 | 2024-09-29 01:37:43 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f7aa8bb7-fdbd-3cd6-951f-05f0f5f91bc4 | -12.85 | -62.744099 | 2024-09-29 02:27:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c9471ba-3e37-398f-88a9-fcecde572ff0 | -12.8404 | -62.7467 | 2024-09-29 02:27:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4bb8f9a3-4f24-3ca7-aecf-8523179e67ff | -12.846 | -62.767601 | 2024-09-29 02:27:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| accb263d-b020-312c-8edc-f234a3abac46 | -12.7621 | -62.608898 | 2024-09-29 02:27:23 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f546f480-4fae-3e30-89c3-6dfd6a5b98a7 | -11.5632 | -63.735802 | 2024-09-29 02:27:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 417ccbff-db96-3ab4-a037-cd31150ca5e4 | -11.5829 | -63.890301 | 2024-09-29 02:27:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 01c3a981-94e8-3553-8f30-de1eba79dc31 | -11.5684 | -63.874401 | 2024-09-29 02:27:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b7964f94-9f16-37ff-868c-ecd0f34b0200 | -11.5733 | -63.892899 | 2024-09-29 02:27:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 11844427-9af5-31b7-96e2-0905c25e096d | -10.0554 | -65.051201 | 2024-09-29 02:28:17 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| abc3dfeb-900c-37bf-bbc3-bdb0e3e3f4b5 | -10.0596 | -65.067497 | 2024-09-29 02:28:17 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c49222dc-9615-3e85-bbd1-5107ac5d8fa2 | -10.0457 | -65.053703 | 2024-09-29 02:28:17 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
