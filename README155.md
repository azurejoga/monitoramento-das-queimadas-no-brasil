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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10978e45-33b8-38cb-9d76-dc060cffc4b7 | -13.08343 | -51.13799 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ac41086b-b605-3515-96ba-81a7c3c41cc3 | -13.08274 | -51.14296 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6b82563a-3545-3814-9fd5-3793afaf32c5 | -13.07886 | -51.1424 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5ba54972-ed0c-3187-a3af-bab9851cc42b | -13.07817 | -51.14737 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea05175d-c926-3f33-b115-4a89e24aa3c3 | -13.07635 | -51.13189 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 38.6 |
| c527f6ce-5d3a-352d-b25f-0675a6504ccb | -13.07566 | -51.13686 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0715e846-1d2a-3da6-bc9e-fab309554057 | -13.07498 | -51.14184 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 009aac6b-1e9d-31e6-9cf7-5d918a6c0349 | -13.07429 | -51.14681 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cf805cd-d343-3885-9951-b9755a16c89f | -13.07247 | -51.13132 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 7555cc13-9527-3140-bfcb-24fbda49710e | -13.07178 | -51.1363 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8f3b30a0-36e4-3c22-80bd-135a9cf5962b | -13.07132 | -51.11082 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ecec64c4-2fca-32be-960d-d2d8e1c0733f | -13.07109 | -51.14128 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 05573d13-e99f-3f47-b021-b64211d40ed7 | -13.07064 | -51.11582 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| aa43e265-bce9-3a1b-ba44-c144b45fc7a0 | -13.07041 | -51.14625 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9c04e32-bc7c-3ee7-9bad-b0255fcda06c | -13.06995 | -51.1208 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 84c2f8a0-005b-3e7d-b818-0bfc100fcf6e | -13.06858 | -51.13076 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e25f28e2-c2ff-3bd8-b51f-1857d0d75639 | -13.06744 | -51.11026 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bb2f2803-1c19-3f4d-b744-a35d25a81068 | -13.06675 | -51.11525 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5744ecc1-77bf-3194-8c06-56f68c7e99d2 | -13.06606 | -51.12024 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 879262b1-588f-3df1-b03c-10b7597c03c9 | -13.06538 | -51.12522 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60fff541-b580-35cb-a7b0-45c24ed5f524 | -13.06286 | -51.11469 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 201afc64-2553-39b1-9e0d-80171408a98a | -13.06218 | -51.11967 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2fa11643-046a-3969-818d-4ccdcad9c5a7 | -13.0615 | -51.12465 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 231e8517-4899-39f0-97c9-604159b7faf1 | -13.04455 | -51.12487 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f6b29f5-39f0-3c88-a44c-849fe9ba58e1 | -13.03995 | -51.12928 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f5e4465d-e4d4-3d22-a5d4-96f180e1d11f | -13.0375 | -51.12625 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1bb90a82-ff68-3043-990f-2a58b0fd405e | -13.03607 | -51.12872 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 692c82b8-b82a-3093-9b3a-f99802be73f0 | -13.03219 | -51.12815 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1496e22b-c424-38de-8041-fb869db7647f | -13.03148 | -51.13312 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e076bcf7-37d2-385d-a1d6-19cac48a0d8f | -13.02901 | -51.12261 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4c6737b1-7a82-3456-8d15-d22d0fb0a585 | -13.0283 | -51.12759 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2d83ddbf-42d8-3825-957c-27f6db461e56 | -13.0276 | -51.13256 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e8e49a9-46ab-3aa4-aa75-4c56ebe256e8 | -13.02442 | -51.12702 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cc83849-125b-319b-89c1-eefc395f7cf8 | -13.92795 | -50.88718 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bca1194-c12a-33ef-a813-1b32cb861c78 | -13.92688 | -50.84984 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4be20552-7fae-3f78-957c-73e545a8ec1e | -13.92492 | -50.86401 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13b10ac8-6989-3ebd-9a0a-c39781e37ab2 | -13.92338 | -50.84571 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbf436d6-554c-389d-bca4-cc0d6403683a | -13.72389 | -50.89277 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61469292-69df-3f44-bddd-dce79f3ac039 | -16.11814 | -50.4504 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c13fed59-e1ff-3291-858f-33d2deb0ae8a | -16.11385 | -50.45026 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19512fc8-a116-3ca2-a35e-47ec6c587ece | -16.11338 | -50.4539 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a488319f-068c-34f5-9a5a-895247bb8666 | -16.1129 | -50.45763 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1500524-756f-36ad-b9bd-9abe11c989d0 | -16.10865 | -50.45721 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3979c29-7a7a-3e1d-a735-a1ec39221fdf | -16.1044 | -50.45676 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96763f4b-a95a-3737-ae02-5a4097cb4748 | -16.10019 | -50.45612 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b6faffa-73f5-3513-b3ef-e9f817d9048f | -16.09971 | -50.45979 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 999b1393-bbfc-3246-a4b5-f431ab33f174 | -16.09598 | -50.4554 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d326613-74e1-3cf0-8ccf-4a45302b6f6c | -16.0955 | -50.45912 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96d7b865-13e4-3ca3-9379-55b334119292 | -16.0932 | -50.4436 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c20a756a-1faa-3519-b911-c014d8290245 | -16.09274 | -50.44715 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ea2e1bf-9dc0-3e69-b97f-b269cf5f472f | -16.09227 | -50.45081 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 579ac337-86f8-38ce-8273-7cba7ea4c648 | -16.09179 | -50.45451 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b804dcbb-740f-31b4-ab9b-3bd1cd4b22f4 | -16.08118 | -50.43658 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f348d569-f239-3d85-992f-18c77612f0f6 | -10.66971 | -50.69339 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e977fd4-6dc3-3bde-a5e5-73d533db09fb | -10.66902 | -50.69826 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7eabbe1-a243-3bed-990a-0e18a278480b | -10.66516 | -50.69769 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb2e082c-093a-3b4e-9842-14e24473eae1 | -10.57417 | -51.09145 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23e5fbc3-9e2a-3e81-a810-c99b1db18f7e | -10.55974 | -51.08463 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c77698a1-0546-3988-8abd-e3f91a9d768f | -10.55974 | -51.08302 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36bf4c13-c207-3c37-8822-50fc94c1c586 | -10.55597 | -51.0841 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 042357bd-af59-3a2b-b52b-23f42c458427 | -10.55597 | -51.08248 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6a134bc-ea3b-39a5-9123-775717abd795 | -10.5522 | -51.08194 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a810e2c-0227-3aeb-a03d-1f290e66ca22 | -10.54843 | -51.0814 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff11a719-c6fe-33d8-b358-56b4fee87f8a | -10.54465 | -51.08087 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07b56410-744a-3bcc-90e9-330c785b387b | -10.54447 | -50.97618 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ba1fd1b-1a3f-3597-95ce-25fb944fd32d | -10.54379 | -50.98087 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18fdb07e-e083-3ec2-b410-dc820a6b74f8 | -10.54272 | -50.96157 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df2eb308-050d-3bff-af86-43c675303d22 | -10.54088 | -51.08033 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 629cedc7-c868-3288-8700-950ec6a07e0b | -10.54027 | -50.95169 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b71875a7-6aaf-3b8b-b00b-483acc79e99c | -10.54 | -50.98032 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eddcec27-96c0-361e-9fbd-a65fb38dea19 | -10.53959 | -50.95637 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eda0627a-d7ae-3e80-bab9-d4a13008511f | -10.53892 | -50.96103 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5a2f08fb-f02a-3926-bf31-d087946a2eab | -10.53824 | -50.96571 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d66fbd5d-6684-3b54-b59d-d004ecf60368 | -10.53757 | -50.97038 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 15efc598-a30f-3af6-bc35-c9a2471a4e45 | -10.53647 | -50.95116 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bfa0655-a89d-3c1b-885f-ba0799f5605d | -10.53621 | -50.97977 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4e166e16-4d9e-31dd-b999-6666c43a0f01 | -10.53579 | -50.95584 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68d7ddfa-1826-373f-82c6-f87ad85edfc8 | -10.53444 | -50.96518 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 927be56e-37d0-3668-86e6-a522094d3946 | -10.53024 | -51.07413 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a27f7966-e21a-349d-a2f0-0499aff425e8 | -10.52646 | -51.07359 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea3eef1a-9983-3b23-817a-d62043dffa76 | -10.51002 | -51.08079 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9dcf4a6c-f5b2-3a72-954c-5227707196fa | -10.50626 | -51.08018 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c3b2445-94d2-3a0a-b499-9a9f7957afb0 | -10.50227 | -51.10781 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f919c2c-168d-3439-b70f-f83254d300ca | -10.49785 | -51.11183 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88a151de-b5e2-33fb-83c8-906e17d21c71 | -10.48903 | -51.11981 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e59591d3-9ed2-332e-8e1e-0de0eaf17464 | -10.48837 | -51.1244 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e9b87f3-4c30-3bf7-afc4-c5f03a5425f3 | -10.48771 | -51.12899 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7bc933e-d36e-35fb-b10b-c6a5fbd5c980 | -10.48461 | -51.12384 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a901902-7dd0-30e2-bb5c-d0b5e9bc3aaa | -10.46877 | -50.83251 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdf2a665-4759-383a-afcc-d6fb311b0e91 | -10.45964 | -50.73344 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47aeebf8-a852-38f2-ad40-897bdafba07e | -10.45894 | -50.73828 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca6f58e9-50d7-3c58-8ba0-fdcc2f6c75af | -10.45579 | -50.73292 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f510a2c-1656-340e-baaf-fd71e822de11 | -10.45509 | -50.7378 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15e81a02-7125-3b35-953f-344e380ef178 | -10.45439 | -50.74265 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df0dc6c2-c957-356b-9f0c-5896c3992d22 | -10.45195 | -50.73233 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ccd877b0-ea87-3a8c-ade8-13ab088709aa | -10.45125 | -50.7372 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ca490da-350f-3dc4-88ad-134f035201fc | -10.45056 | -50.74202 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8a0c5fa-6fdb-3ea0-94ff-3435f35662b4 | -10.44812 | -50.7317 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 33382425-3041-3d8c-93f8-8963f0ab3862 | -10.44742 | -50.73655 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fed6da77-9c9b-35ad-bbcd-e56ccbd1afcd | -10.44673 | -50.74138 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README156.md)
