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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ea36f12-7c3a-32a1-8c59-b441355c36b6 | -16.69113 | -57.44372 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 85bfb1ae-e851-3f6a-8c37-9084b67976a8 | -16.6905 | -57.44832 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 96ac9aac-3069-3f1b-985c-9f8ce7799394 | -16.68923 | -57.4575 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 05d246bf-3c1b-39ed-8430-944debcffc29 | -16.66315 | -57.45356 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6cfd993b-728d-397f-8622-d087fb87aa72 | -17.10912 | -57.39221 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 654a3137-4446-3f23-a9c2-bccaa6c592d3 | -17.10785 | -57.40158 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7a5fc7ff-5904-37c7-ae90-5508798222e8 | -17.10726 | -57.37757 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 7390d1b7-6cb8-3fb3-9e03-54846ae7aaea | -17.10722 | -57.40626 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0593f3d4-70b7-3ae2-ba75-77bff6ae09ee | -17.10719 | -57.37539 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| a2aa4fff-a183-322a-a609-a2c8648a07e2 | -17.10596 | -57.4156 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3035344e-c831-3720-9370-abc6a2535f33 | -17.10587 | -57.38476 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 78cb25f8-aee2-32cb-9b17-3c40ce10777b | -17.10536 | -57.39164 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f94a90d7-69b9-353e-ac80-a360b001000f | -17.10521 | -57.38944 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 05b1f766-f64f-3175-b53c-85ffa5d2d77d | -17.10473 | -57.39633 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| df6672ae-35d9-361d-a114-582469693ec6 | -17.10455 | -57.39412 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4eb5b09e-a446-3caa-8975-e29ddeca82a8 | -17.10349 | -57.37701 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| d183c27d-3697-3a09-ba13-9b637e95c4ec | -17.10283 | -57.41035 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 801067a8-3bea-333f-89a5-300f8548d884 | -17.10276 | -57.37952 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 12ac3171-0452-3008-ba3c-674481587632 | -17.10257 | -57.40813 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| def46277-f015-3f5b-a9b9-6804ecd45901 | -17.10211 | -57.3842 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 9129ae00-7e8d-33ad-aee6-6365ce6bed0a | -17.10191 | -57.4128 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 227df589-432e-3483-87eb-6ed5ec4db462 | -17.10125 | -57.41747 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| f09d6c6d-e8ad-33be-8407-6abee1ecd994 | -17.10031 | -57.42904 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| f2153363-ca03-3e4b-8677-a21e4dde2d48 | -17.10013 | -57.39824 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 385361cd-662f-30dd-8134-ddd83840e4c1 | -17.09994 | -57.4268 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| aa29c345-f52e-3e75-8989-f2aecdbacbba | -17.09971 | -57.40512 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 926bc1f3-02cb-3c54-b6e4-437f729745c9 | -17.09947 | -57.40291 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 45a84e87-7455-3638-b75f-a26e08ee0919 | -17.0991 | -57.38114 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 95f4edf8-af6a-3412-9349-407ffa74dade | -17.09847 | -57.38583 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 105d112e-9904-32cc-9bfb-b01be50d3fd8 | -17.09845 | -57.41446 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 6f6b1421-abae-3ec8-9f18-be498997fcbb | -17.09835 | -57.38364 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3059e746-7939-3f1b-b332-1e39e8165c6d | -17.09816 | -57.41224 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| a66be262-7bed-30ec-92fe-c19e76db3a2f | -17.09782 | -57.41913 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| ef40d8d1-5bdb-3a54-bab6-be2f614b946f | -17.0975 | -57.4169 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| eabf527c-3294-3b51-b63e-adaad296d190 | -17.09637 | -57.39768 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 73cc11c7-4ace-38f6-ab44-17a32ee35b37 | -17.09595 | -57.40456 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2e5bc69b-fcf4-3891-8be8-73c4cb22a099 | -17.09572 | -57.40235 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 94035625-7ea7-3a6b-83c2-d9cbb8b45603 | -17.09532 | -57.40923 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7f778f06-e141-31b9-956b-d320355976dd | -17.09469 | -57.41391 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 446b1f22-ef86-36c1-b867-502058cac2d5 | -17.0944 | -57.41168 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9d65d5dc-98a5-335f-a696-bce07ff3cf5f | -17.09407 | -57.41858 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| e59711ec-bc54-3402-b689-9619aed73230 | -17.09344 | -57.42324 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| d82da418-b678-3fe9-b57e-eef49b7e7fe8 | -17.09243 | -57.42568 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| ffc683aa-0c6f-3c89-b270-b70462a18a04 | -17.0922 | -57.40399 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 61fa6658-9306-3165-a5b2-6148c0cfbaac | -17.09031 | -57.41802 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| d3f00187-4bd6-3fd2-bb49-0415da13cdbb | -17.08968 | -57.42269 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 15b7157c-844d-3306-b639-d2d132bcf8ba | -17.08379 | -57.40534 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c395c6ea-f854-3b96-a4ef-0afa63886f7d | -17.08314 | -57.41001 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1741df6c-dd1c-3809-b641-ac2dae94c023 | -16.83516 | -57.45317 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 7737fd48-ec66-3f7d-a3b9-12994d419064 | -16.83207 | -57.44801 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cc84cc69-e85b-3c09-97c0-d1118e206a2a | -16.82898 | -57.44283 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| d483880c-446e-3280-b2b0-14b27feba202 | -16.82342 | -57.42786 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 898dcc55-9662-3e7b-a602-9e0dfe478987 | -16.82087 | -57.44633 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 396383be-a0e5-3eec-ab96-cd49e2ce014d | -16.81968 | -57.42731 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| bad86cb0-fd5f-346a-903e-33e2ab05a454 | -16.81841 | -57.43654 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 6c639b31-b8dd-3681-95b8-91bf8c6bea49 | -16.81713 | -57.44577 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 7aad6594-2cf9-3be8-a6e5-982e7128b504 | -16.81594 | -57.42674 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 691c6cb9-b0e2-3063-b357-78e27c1e4b4d | -16.8153 | -57.43137 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 148.8 |
| 0fa051f0-a3a9-30df-b30b-f9cd77f184fd | -16.81483 | -57.37929 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| ed802c26-3639-301e-9de5-6b333de90966 | -16.81284 | -57.42157 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 7f4d7fc1-7902-3d85-a82f-b79420e57097 | -16.81093 | -57.43542 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 148.8 |
| 0dda1f5c-fe51-3285-a0f7-0d4f78cdb589 | -16.80981 | -57.38802 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f764e790-b7f2-3df8-b86b-84e43769c000 | -16.8091 | -57.42101 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2159228b-ed1b-3c95-afc2-3c4e61966902 | -16.8079 | -57.40193 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 87857de5-ca51-3e57-8c9c-dba55b3bcc01 | -16.80409 | -57.42968 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f9f77619-6e74-3ad5-8a26-a798879dc89c | -16.80105 | -57.39617 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c5e7e73c-a755-3bd1-96b8-11ed2cfabf69 | -16.79293 | -57.39968 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 0938c1f6-e08e-356e-b20b-730385623c4b | -16.78918 | -57.39912 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 879dfc20-b237-3f5d-ac34-fb643970e6ce | -16.78725 | -57.44129 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| dbb8e3a3-9854-3790-845e-d04f7458321f | -16.78481 | -57.40319 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 29476969-d33c-3ea8-bb3b-011e2428c267 | -16.78477 | -57.43149 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| debc1256-f9aa-3c53-8a9a-401d75e46e4c | -16.78289 | -57.44533 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e87a70c6-f300-3d43-82c6-beb80f8e2e1f | -16.83175 | -57.17044 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fb1982e7-a6b1-389d-bcc3-b7742f38ca15 | -16.82232 | -57.38041 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 999817dc-cbaf-3453-a01c-8497c048196d | -16.82032 | -57.42268 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b3234f14-8120-30f6-883b-6a19d81fa712 | -16.80917 | -57.39266 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 56f25812-81da-3079-a807-8d378b3dc9a2 | -16.80853 | -57.3973 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| e489a7c0-264d-3bc8-93a9-95f328696fe2 | -16.80783 | -57.43024 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 25c62981-cffe-3c56-ba9d-4bf9fb5eded1 | -16.80656 | -57.43948 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e9a6f139-ffb4-32db-95d7-2ed8b25e7487 | -16.80473 | -57.42506 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9f6c5cce-b876-3c30-ada4-acb31b440bed | -16.80416 | -57.40137 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| be7a0fb9-d4d8-301c-a92e-18b6bfce111f | -16.79356 | -57.39505 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 33f58c19-462a-363b-810c-0be55b4c8983 | -16.79036 | -57.44645 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f9089cd5-bd5d-3f66-8fdf-ed4071df1bff | -16.78981 | -57.39449 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d143b9ae-8fb4-3c21-9d01-130544c57ae0 | -16.78855 | -57.40375 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 6b05095b-00d5-3d6c-9753-0f167579ba4b | -16.78792 | -57.40838 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e2958c69-3faf-397e-a74a-11ba024b370b | -16.78729 | -57.41301 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c2de39f3-49e3-3835-bb5e-09946e948226 | -16.77981 | -57.41188 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2b6f787e-6142-3702-bb55-7e0b81bd7cd3 | -16.77354 | -57.45804 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2b7099cb-9b18-3e62-b4eb-10bb0a711f88 | -16.76856 | -57.46668 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8880ec77-59a6-37eb-b0df-32b772c5c7f1 | -16.71096 | -57.46545 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 38510af3-2cb2-3c58-9db2-c4529333d005 | -16.70723 | -57.46489 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3108ae54-3080-3859-b2ae-908eddf3878e | -16.70351 | -57.46432 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 92d7c2b4-c472-3c66-9951-e097a8477966 | -16.69978 | -57.46376 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| af60cbe7-f4ea-3016-a96f-9d0eead6d92f | -16.69915 | -57.46835 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b1646200-08a8-3355-8f80-98150bb38a9a | -16.68986 | -57.45291 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4a1eba06-2aa6-36c8-97ce-64dda0fc48e4 | -17.14445 | -56.96881 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 597452f7-556b-3b5f-a689-c9f32cdf0292 | -17.13781 | -56.81534 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 796726b0-3350-39c4-885d-bc6263b1410e | -17.1346 | -56.80974 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 274c943b-429d-35ad-869f-fd7f74302147 | -17.13324 | -56.8198 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |


[Clique aqui para ver as próximas entradas](README120.md)
