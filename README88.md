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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8123bdf-da3a-349a-a839-d93dd7b7e93d | -16.75215 | -55.80572 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c2f3a531-51c1-3f48-9d92-8b65ccaf77f3 | -16.75196 | -55.79073 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 268070fe-b45a-3347-9b8c-3b9a2a91dff1 | -16.74874 | -55.80642 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 67b72bd6-decd-3351-a649-c05000e55a7b | -16.74825 | -55.79662 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 15988508-e0af-31c9-8b92-a98f963eb625 | -16.74479 | -55.79726 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9ffc3131-8923-3bb6-83dc-6d89eb27ad12 | -16.74102 | -55.80309 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0d380be0-6984-31eb-822c-5842f7adb884 | -16.74076 | -55.81683 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2ac75993-23a7-3631-a711-09ff1dc0c731 | -16.97218 | -56.21222 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e9ef0dba-e84c-375e-966e-50ffb396cae6 | -16.97131 | -56.21637 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3eb32911-5133-30f7-b69f-5c3cf0f78b7a | -16.96771 | -56.21079 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 293964e0-4560-3187-bff6-f3b948acb791 | -16.86013 | -55.9198 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 483cded3-851b-3bab-8bbc-e19d4182f5db | -16.85508 | -55.94366 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4ede6aa4-9ae4-3134-bfee-2520dad700cd | -16.85453 | -55.9185 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 65c0cb80-8312-348b-9adb-23c55c42335b | -16.85424 | -55.94765 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bcbd162c-89c7-3afe-818e-fa3a381dbe03 | -16.85147 | -55.90527 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| cf6a7bc9-e4e4-377b-b7c6-f1565531e010 | -16.84894 | -55.91719 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7a05a10e-e19a-3cf9-b516-75723e5f4ff3 | -16.84863 | -55.94634 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7a7174b4-19ba-3c0a-b52d-9eac7ec50475 | -16.84779 | -55.95031 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5851a701-f06e-30b2-8396-918250563480 | -16.84503 | -55.90794 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5cf20de8-6007-35ea-924d-31135f09d482 | -16.84418 | -55.91193 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 95d78a6f-e645-3ee4-9eac-2bfe1dd0dfaf | -16.84334 | -55.91589 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 74bf596d-6846-3085-8203-aeed1ec6653f | -16.84249 | -55.91986 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7c468e42-c4eb-3b7e-966c-3aebeacc8389 | -16.83943 | -55.90664 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| b31b89ff-befe-3073-ba50-6a806ebe0e87 | -16.83858 | -55.9106 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| c9845e2d-feab-3474-83c2-bfeb669da116 | -16.83689 | -55.91854 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 75390b42-640a-3d6b-b542-7de4210e3795 | -16.83616 | -55.90808 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 683db684-040a-3685-80b6-5bee80151791 | -16.83605 | -55.9225 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| bfc0b474-93d5-34dc-b440-9511ac48f3ae | -16.8352 | -55.92647 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ca3a7845-f1db-35a4-8c42-c14af4dd999e | -16.83488 | -55.95564 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 66a2bfb7-0fd1-369d-a184-a9c51981a88e | -16.833 | -55.90926 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 5979509e-4146-3549-aa96-f3223818cad1 | -16.83289 | -55.92397 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 42cba92d-f72c-38d9-896b-0dd1d5f541bf | -16.8313 | -55.91718 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| f3924bcd-0b07-3617-9033-3ba9c6a7b611 | -16.83125 | -55.93195 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| db0e36b8-bf82-3553-9e6b-0918180cc389 | -16.83046 | -55.92116 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 75e94f7f-7734-38b8-8e48-a0c09528c978 | -16.82976 | -55.91067 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| f3610779-db31-35b8-83fc-b30bac02ea67 | -16.82841 | -55.95833 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 51362a05-878c-3e2d-822d-17a06bc6d993 | -16.82812 | -55.91864 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| a8bdbd93-80e5-3a99-9498-bcf25f2670e9 | -16.82756 | -55.96233 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b1bd173d-ed7c-38fc-bc86-1d4eb8058eb0 | -16.8273 | -55.92262 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9846ac47-2613-3a82-900b-89656b160b18 | -16.82655 | -55.9119 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| dd43a2cc-ae22-3e7d-9bd6-1e3d4b700256 | -16.82565 | -55.93061 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1d64b9c8-2600-3059-b18f-4e73fde08ce5 | -16.82548 | -55.95995 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a5f4f6f6-ef4c-395f-8d0b-d00ec8504a92 | -16.82482 | -55.93462 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7303f243-7b18-31d3-b732-b70048ad39bb | -16.82108 | -55.96503 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 70f9db7b-4119-3fa3-968c-77c7c4ac97ca | -16.81669 | -55.93048 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 83fed7e6-d5c4-3d2a-acd3-3ad88bf7e739 | -16.81499 | -55.93843 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2cc1a18e-15c2-3c81-b681-964739d826aa | -16.81461 | -55.9677 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 58d8be89-0cb0-3ef9-ae9d-37a0b4b077b3 | -16.81414 | -55.9424 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c89442a7-dbce-3b93-a5d0-da99453e2536 | -16.81362 | -55.93194 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3dc8e44e-2f05-32ac-8738-0143465557f0 | -16.81279 | -55.93592 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 627d832d-5d0e-3abf-84fc-071e818159e0 | -16.81024 | -55.93315 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 532d0546-ddea-3cc4-b064-fb9a05e478f8 | -16.80852 | -55.94113 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 23c4a142-ca42-388c-a706-97c78fec33fc | -16.80766 | -55.94512 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 84e1863f-aa10-34d4-b99a-cd060d74bb20 | -16.64851 | -55.94956 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2ad00844-8f22-3156-a1e2-d531a610b433 | -16.61386 | -55.94576 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| dfedcaf9-63b2-3262-b472-2b3e85b6510a | -16.61246 | -55.94147 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6f2f72e1-4551-3023-8df5-a80743a6db6d | -16.60908 | -55.94043 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d0be1ea7-bc9e-323c-aef9-e334cea188cc | -16.60822 | -55.94444 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5e6767d4-e5b3-34af-b7a5-3a00ce8fb459 | -16.606 | -55.94416 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2fbcfa86-ab35-3b76-bfb2-54df69bb9bad | -16.60173 | -55.94715 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6c840b8e-5672-340e-bf97-af18e39a6b9a | -20.02307 | -55.98964 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fdbae995-99fb-3219-bedf-2a88a540fdf6 | -20.02232 | -55.99318 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 5d8e4d08-0f1d-309c-92cd-67ff8550c19c | -20.01854 | -55.9848 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 535bd868-8446-3f0d-9350-955ae0fd7e46 | -20.01779 | -55.98833 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 774f1b77-d9b9-34b1-8fd3-defc0ce9d5cb | -20.01703 | -55.99187 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 07e46a30-209e-3de5-b500-20decabc1d86 | -20.01325 | -55.98352 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2dd525b0-7bd8-320a-91d1-bf854eb9f503 | -20.01174 | -55.99057 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 2e0fe958-30f1-30b6-9e65-169329b4b379 | -20.00721 | -55.98574 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3be1c879-9a81-3d4a-bae6-a2c5594c7b3e | -16.49311 | -57.33078 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| e4c4189e-d620-30e9-8171-b884502d1303 | -16.49203 | -57.33576 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d7dcff98-d37a-3f40-b7e4-313baeb76149 | -16.49096 | -57.34071 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9305be65-7365-3516-9b24-6b8333cee559 | -16.48989 | -57.34567 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fc8a070c-7b78-360b-80bf-6545154f43f8 | -16.48882 | -57.35065 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0648f6f2-c1b2-38fc-8ea2-5137fd4d619d | -16.48774 | -57.35564 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7fdd32b0-ad1e-3ca7-b1db-de7faf76a502 | -16.48699 | -57.32927 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 66ade1a8-260b-3949-ae8f-86ba97e209dc | -16.48591 | -57.33423 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bfcc536b-e8cc-3952-a399-ed1e09dc67bb | -16.48557 | -57.36567 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 868c6d32-6f38-3cfe-8137-8a4c7a0b96ed | -16.48484 | -57.3392 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9b14145d-a754-345a-8515-26719c70a205 | -16.48376 | -57.34418 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 017e79e2-045b-3236-906a-1db66b39a921 | -16.48269 | -57.34916 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5d49a3ee-a5aa-3ee6-981b-bec0b8561d75 | -16.48161 | -57.35415 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ebba04f4-3b4c-3093-b527-dd5c1b51d72d | -16.48052 | -57.35916 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b20b0c72-edd1-3a79-92c6-758bc1733f3a | -16.4798 | -57.3327 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 86278102-6105-3b24-8675-3b5886f7c6d6 | -16.47943 | -57.36417 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8c9e0094-2af6-357e-b0d9-8279ed202ea1 | -16.47872 | -57.33768 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 43cc0cb3-3286-3ef5-b77b-b6beaef9e549 | -16.47835 | -57.36918 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f9528d09-7ea7-31f6-9018-f8b5d8dcfb27 | -16.47763 | -57.34267 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b3098a5d-0c6b-3e8c-9ddd-7c38a330a327 | -16.47655 | -57.34767 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 90012d7e-2cf3-319b-b50d-b88e7b8b5bcf | -16.47547 | -57.35268 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 96b1d862-d45b-39c9-969d-47099091c818 | -16.47438 | -57.35769 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| abf0da30-3d4a-3c41-82e7-362cd266059d | -16.47367 | -57.3312 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b3ca2988-92ca-36aa-b142-15fcebb4c278 | -16.47329 | -57.3627 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 46741987-60df-3da4-960e-15c3b900084f | -16.47259 | -57.33617 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6e757a4e-2e3d-37fe-962f-3c1fe82e6c9e | -16.47151 | -57.34117 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| db02b3da-2184-3882-b865-ef8112303ae8 | -16.47042 | -57.34616 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2cb284bf-6c21-3c49-8710-1bedeea328e2 | -16.46932 | -57.35121 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8b757d63-e6c1-33b3-96af-7e3a4c5e14ab | -16.46823 | -57.35624 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d3f5b996-4d52-3710-a8e3-e5374b5cadd3 | -16.46646 | -57.33468 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 411791e8-e730-3aac-9138-15f80415ec4b | -16.46537 | -57.33969 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8094ad80-2d91-3a14-918a-749c8febe98d | -16.46428 | -57.34468 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README89.md)
