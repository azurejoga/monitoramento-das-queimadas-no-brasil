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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f523b84-d4b8-3d75-92c9-86b9156a9ab7 | -11.2374 | -60.5868 | 2024-10-03 01:50:19 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 07574296-4324-3fcd-8db6-d8876fa2686c | -11.2404 | -60.5989 | 2024-10-03 01:50:19 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4840b42c-70eb-3b3b-bd31-883baf1d34b5 | -10.6847 | -58.534302 | 2024-10-03 01:50:19 | METOP-B | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 662e7f7d-a79e-34cc-a29e-555b274ae04f | -10.689 | -58.5513 | 2024-10-03 01:50:19 | METOP-B | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c274145-c76f-325e-8c04-b1c10bcff3ae | -11.7766 | -63.659 | 2024-10-03 01:50:22 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f671eb9f-56a8-3c5a-bce4-4aa181555c54 | -11.4756 | -62.469898 | 2024-10-03 01:50:22 | METOP-B | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c0b9c24-6d7b-3530-83c0-5c9ee50e4ca5 | -11.4779 | -62.479198 | 2024-10-03 01:50:22 | METOP-B | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1f08bde7-6caf-31d3-ae3c-eb0455df57a5 | -10.1529 | -57.257301 | 2024-10-03 01:50:23 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1c1b81d-ade8-3d11-9ecf-ed0e9b1f79b6 | -10.1584 | -57.2785 | 2024-10-03 01:50:23 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54f0f3ff-5830-3891-9167-a624cadf5f7d | -12.0105 | -64.894897 | 2024-10-03 01:50:23 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 28287dbb-45b2-3876-b773-5353d383b26a | -12.0122 | -64.902199 | 2024-10-03 01:50:23 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6af09ce4-af10-375f-8d8c-369334f90af4 | -11.7326 | -63.780102 | 2024-10-03 01:50:23 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4db0f113-768b-3456-8fb9-065204736fc3 | -11.7345 | -63.788101 | 2024-10-03 01:50:23 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a6f2c5d2-0c55-3028-bee8-316df46dd4c5 | -11.7363 | -63.796001 | 2024-10-03 01:50:23 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f5b16770-2512-379b-b94a-b351f879849e | -11.7382 | -63.804001 | 2024-10-03 01:50:23 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1280ca03-efa7-384d-ae99-6f1e000dde46 | -11.2968 | -62.067101 | 2024-10-03 01:50:24 | METOP-B | PRESIDENTE MÉDICI | RONDÔNIA | Brasil | 1100254 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| da2125fe-b745-33dc-88af-4d25c47abe65 | -11.7265 | -64.065002 | 2024-10-03 01:50:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 03c67192-e15a-3a90-be21-6ac18d293f9a | -11.7284 | -64.0728 | 2024-10-03 01:50:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 91e489c4-aaee-3019-999d-8dc1d2171856 | -11.7535 | -64.181297 | 2024-10-03 01:50:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b6aca598-225f-3baa-a990-bd94af918c4a | -11.7553 | -64.189003 | 2024-10-03 01:50:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 74e2f960-9a9a-3392-b8c4-f17c75f908e5 | -11.773 | -64.2658 | 2024-10-03 01:50:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 78a4e6b0-06b1-3cc2-ade7-d40a58c85deb | -11.7748 | -64.273499 | 2024-10-03 01:50:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 905c2313-9fd7-385a-84d0-102df0a495f0 | -11.7131 | -64.051697 | 2024-10-03 01:50:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7853a0d2-a438-3bbe-870c-7b843f75e067 | -11.7149 | -64.059502 | 2024-10-03 01:50:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3649f468-7a6c-3f94-8aa1-a97752dc6aaf | -11.7167 | -64.067299 | 2024-10-03 01:50:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b006e815-1dcf-3783-acf6-5043240562bb | -11.7419 | -64.175903 | 2024-10-03 01:50:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| db6a463e-8239-3e46-a9b8-aabb464545ef | -11.7437 | -64.183601 | 2024-10-03 01:50:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 04f8435e-c8dc-3a9b-87ed-5cd05922802b | -11.765 | -64.275803 | 2024-10-03 01:50:24 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c25e05b2-22d5-3c41-a793-a182a45166a3 | -11.6126 | -63.6642 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2bf99a14-277e-3ffa-b0d9-cb9c73861edb | -11.6145 | -63.672298 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6f971e89-775a-3d7e-acda-68ff1ebd283f | -11.7015 | -64.046097 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86a8c1ba-1b2f-3337-9f65-3eac359d0948 | -11.7196 | -64.124001 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 639dab9d-6226-3619-b606-0739fbee788a | -11.7214 | -64.131798 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 708ef508-c977-32d2-acb6-3e5ab12b9a74 | -11.7534 | -64.2705 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| edb2f1c1-7ea0-3fe2-bbd1-b9986a1a582c | -11.7552 | -64.278099 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8e01e7-4078-3fa7-9e67-36d287141b55 | -11.601 | -63.658501 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e534a813-9186-3d72-97f2-53f32ad578b0 | -11.6028 | -63.666599 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e23d4740-227e-3fc5-a02d-a8ac8ec99a10 | -11.6047 | -63.674702 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e961d8a-70fe-38f7-aeb4-cca0f48306e3 | -11.7099 | -64.126404 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 51374438-1751-3767-babc-04a7169cf5fa | -11.6006 | -63.701302 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b68fa253-4cbe-39ce-91d4-d8da15ade2aa | -11.6025 | -63.7094 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c44a468f-82fb-3be8-904f-77f8fa82857b | -11.6044 | -63.7174 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b74721c3-ebd9-3fb7-ae19-6f030ded80ba | -11.6656 | -63.980301 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fdf8cafe-f049-381a-b580-f876123368d5 | -11.6674 | -63.988201 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cbb17014-94e4-3004-b540-485bcb9db989 | -11.6693 | -63.995998 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c2d8778b-f55a-315f-a96a-7b03941d989b | -11.6784 | -64.035202 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b4d650e4-41d0-3761-b638-9de7e27e3426 | -11.6802 | -64.042999 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3a782fcd-5280-3015-bc48-39370db8c2e0 | -11.6171 | -63.816101 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 735be9a1-afe1-3616-b1fc-bec86c19fdb1 | -11.619 | -63.8241 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d609b42f-ad32-31fc-9a1a-118655e3bc68 | -11.6686 | -64.037498 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 365c2989-9575-3ea0-a5e2-ad7018d92bc0 | -11.6704 | -64.045303 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9acb94a6-af54-37a2-8b33-e6a399688fa0 | -11.7224 | -64.269798 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bcea7526-58f7-325b-849c-f426a53db1df | -11.7241 | -64.277397 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 777f317b-a272-3bc7-b706-beec97e391cc | -11.6055 | -63.810501 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6a834e52-0911-3abb-a5bc-be43534224f1 | -11.6073 | -63.818501 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| df11b489-8aab-39a2-8d6d-7e79045288f9 | -11.6092 | -63.8265 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0c93b8cb-c453-3663-a867-b1d246f52855 | -11.6515 | -64.008598 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e15239be-660c-34ee-a2a3-63f684aec0a4 | -11.6533 | -64.016403 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 52aed16c-f03f-3996-8b4f-99afa09f7ddf | -11.7108 | -64.264397 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c5d9ea5c-c243-3964-9652-81a4471bd3b5 | -11.7126 | -64.272102 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b24e3a08-a791-33de-96a0-a52a24d3c64d | -11.5826 | -63.756699 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f1bf3dd6-80be-38a1-b787-f9f02c15f1f5 | -11.6417 | -64.010902 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 22822a65-b5dd-35b5-ba2c-ed2c112a7a8a | -11.6435 | -64.0187 | 2024-10-03 01:50:25 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fb402754-8447-37b7-8677-da49c4930e1b | -11.5709 | -63.750999 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 533a0674-d62c-385b-a906-5277e0d56626 | -11.5728 | -63.759102 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f0fb2fe2-241b-38c5-b3ca-dc0779715932 | -11.6155 | -63.942402 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c44a04f4-1fba-3883-92f5-e3b99f7048e3 | -11.6174 | -63.950298 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c844003-8339-39df-8724-2212cbf7d1e6 | -11.6192 | -63.958099 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6378b59c-1fca-392f-9a87-9ca47af89a1a | -11.621 | -63.966 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee18de6-5c8a-3835-98aa-05df6b8ecd2c | -11.632 | -64.013199 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 27f2b34e-9307-36e1-87a1-1113ae7db293 | -11.6338 | -64.021004 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 469c7ab3-ed59-352f-8503-efbbc6521a56 | -11.6356 | -64.0289 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| da74506f-ae47-3011-959f-a7c303880146 | -11.6877 | -64.253799 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d01efd89-86fe-3a43-87e9-ec1e704aee58 | -11.6895 | -64.261398 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eafd19fa-f4f7-3163-97f1-5213dad9150b | -11.5537 | -63.7211 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 98aaec8e-0a80-3569-9db1-a95f74b8b2f6 | -11.5556 | -63.729198 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a5639f00-88f2-3e10-8154-637bfb0fd0b0 | -11.6039 | -63.936798 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 563cd80d-d5ec-3c31-869b-3dfe46ae88f0 | -11.6058 | -63.944698 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8e833675-f959-3948-84a2-8af7fc323e2d | -11.6076 | -63.952599 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bfccedba-5135-3d4d-bf26-b293fe19ba40 | -11.6094 | -63.9604 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| da479d41-6214-3b50-b614-b48d8ab371ca | -11.6113 | -63.9683 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b061e5bf-7dc5-3269-89d4-ea054a4ed2b8 | -11.6204 | -64.007599 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8b2968c2-f7c4-33f7-a6fd-754866e924d3 | -11.6222 | -64.015503 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc5860c-76e0-370d-8bea-dad3063985d0 | -11.624 | -64.0233 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 44c14c67-3a1a-3856-b1f8-c5fc25ab0368 | -11.6259 | -64.031197 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| acbc1a91-259b-3280-a680-d7f1379446b4 | -11.6726 | -64.233002 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f80143d7-f699-3c07-a5f0-7b701c3d8977 | -11.6744 | -64.2407 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 14d4d398-a816-31cc-9a94-5a7ba770ea6f | -11.6761 | -64.248398 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ea94713-0497-30e6-86cf-2d9e15733ee5 | -11.4512 | -63.327499 | 2024-10-03 01:50:26 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a1ad738-f691-3d20-bbf0-e28ca443bf16 | -11.4532 | -63.335899 | 2024-10-03 01:50:26 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 27f857db-5db5-306b-9a45-5d7b34bab4cd | -11.5097 | -63.5769 | 2024-10-03 01:50:26 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ba3793e-19b4-333f-a9e7-0b58cbdc90dc | -11.5439 | -63.7234 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eaca7a9f-71a8-33a6-a308-feee941d4071 | -11.5458 | -63.731499 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd86a05-5553-35f6-b684-06a41c5903fa | -11.5533 | -63.763699 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 266a2ea5-43e6-3ae9-b0f9-b05e4f5fa6fe | -11.5552 | -63.771702 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e4e387a9-2c4a-3761-ad54-3b730ac51636 | -11.6015 | -63.970699 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c18bf6b0-ab3a-32dd-ada7-a497b4e63262 | -11.6197 | -64.049202 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 17d79db9-11b9-3ac3-a265-ff46bb8bf683 | -11.4999 | -63.5793 | 2024-10-03 01:50:26 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9016947c-ccf1-3976-9c29-1d0fe143ad89 | -11.6117 | -64.059303 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dbdb0bc6-4cf2-35c2-a7f1-401c43d9e2ab | -11.4959 | -63.606201 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README40.md)
