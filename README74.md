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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f79e95f-f56a-3acc-a62a-ddd2d9aea817 | -9.67295 | -47.83911 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0346721c-96b7-3c07-89ac-004db43b0cba | -9.67074 | -47.8307 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b38f724c-d958-3b48-90eb-61c5e43f7e2a | -9.66946 | -47.83854 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1485f7f-dde9-3a8d-aff2-973d1b7338a1 | -9.46939 | -47.57958 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c19473f-60ab-3e2c-b0ee-f5aeb8b659ab | -10.85255 | -48.07331 | 2024-10-06 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2e8d664e-4731-36c5-aa9a-b1e4b2b6ac74 | -10.83205 | -48.26485 | 2024-10-06 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4189976b-286d-3de3-9b3e-97722bc4e846 | -10.69199 | -48.73595 | 2024-10-06 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5189870e-8c2e-3e86-aa8e-40540b7b8b57 | -10.68912 | -48.73103 | 2024-10-06 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3597f61-6482-36c6-991c-fbc518a24134 | -10.68774 | -48.71726 | 2024-10-06 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddef38b9-b5c6-35c4-ba16-9dab063b70ad | -10.68627 | -48.72599 | 2024-10-06 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77b4a9e4-394b-3278-8890-6d9ef874e9be | -10.68342 | -48.72098 | 2024-10-06 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bccb199-9764-39c8-bdee-51d1f66a1d74 | -10.68268 | -48.72538 | 2024-10-06 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a76582a-5cfa-3f29-843d-fb1476e4349a | -10.60059 | -48.04305 | 2024-10-06 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a67aa968-dd43-31ab-887c-7cf6201df306 | -10.59711 | -48.0424 | 2024-10-06 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3b6061d-d24b-33b3-93c4-ecdf7ef12a56 | -10.59364 | -48.04176 | 2024-10-06 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a79f79c1-aed6-3e8c-b77d-db4ea1a073b1 | -11.71677 | -47.807 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6bdbbf3-19ca-39c5-a698-66bf4f0f25fd | -11.71273 | -47.81018 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3d0de24-494c-3047-aef2-d6639447e04f | -11.70059 | -47.81976 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c628b772-2114-39ad-8016-77c87a2827c7 | -11.66531 | -47.82174 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ffd9c82-58a2-34af-a376-25e5e6db0678 | -11.66469 | -47.82553 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abdc85f4-e953-31ec-b7d1-79b4eb9693e4 | -11.62412 | -48.45361 | 2024-10-06 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19d541b4-1a0b-3aa1-aba6-07b9aa1ddd2a | -11.6236 | -48.32688 | 2024-10-06 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 281a2dfd-1d7d-3a11-b967-39be76a6333b | -11.62294 | -48.33083 | 2024-10-06 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb5cfab8-4879-3344-9ba9-87da602e5b0d | -10.87987 | -48.15367 | 2024-10-06 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b1dd256-4389-337b-b31e-82c346b77ad8 | -14.67938 | -48.77979 | 2024-10-06 04:19:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32e7d74f-5d56-3f7d-801f-26d15d174f73 | -14.67526 | -48.78316 | 2024-10-06 04:19:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2309cb28-dbc0-32d0-8ed2-7c02181036bd | -14.55684 | -48.81897 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea2c3af7-1ca7-3bd9-8bd5-47d191c654ac | -14.55617 | -48.82295 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 135a3f6b-fbf5-3627-99c0-9caf7795f430 | -14.55531 | -48.8159 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b932a2da-50f3-3c33-b95d-d525bcaa0218 | -14.55466 | -48.81987 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6f9e00d-b534-33ee-bf7f-a7366c6ac7fa | -14.55404 | -48.81446 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1bdc4f8f-573b-3b24-b98d-c97bdf74f945 | -14.554 | -48.82384 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 906e4222-d2d6-3d1e-a07e-3f9e84192268 | -14.55269 | -48.8224 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0a78206d-e7cb-31e6-be85-6f895849b152 | -14.55249 | -48.81137 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 85a88611-9d0e-3103-83b9-d80ddc0cf1fd | -14.55226 | -48.79123 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 95f36594-f44f-3983-8a73-deda765cbfdd | -14.55202 | -48.82636 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dd0011e8-901d-30fc-8435-d6057050bf35 | -14.55184 | -48.81535 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b17e266a-a7ae-3926-876b-a49218a2b86b | -14.55118 | -48.81932 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8644d071-fb87-3ffe-88fe-328d42b240b5 | -14.55099 | -48.79889 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c1f23a4-2657-303d-aca1-d2b3df0e0f60 | -14.55053 | -48.82328 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2692f49f-2ed2-3fdc-9c7b-ee518839c6ff | -14.55041 | -49.28362 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcaae437-959c-31c7-bb6d-8bac9be00b70 | -14.55033 | -48.80286 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9a0b1cd-54b3-302f-aa0f-12143a273f2c | -14.54988 | -48.82726 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b0890dd0-7cfa-3276-b237-8be42f8bb7d1 | -14.54968 | -48.80684 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 947e2780-6952-3a14-b11c-bfb2a92f994d | -14.54943 | -48.78682 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a38705c-a093-3f49-8720-db9c3a013640 | -14.54902 | -48.81082 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ff2038f-51ca-388c-99af-1439f8e662c2 | -14.54771 | -48.81877 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ab24ddd-4fcd-3608-8cf9-8b39f4490771 | -14.54753 | -48.79829 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30e93e7a-6b31-38f0-a6de-2e45bb17cccb | -14.54534 | -48.79 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3822e616-6831-3fbe-8761-f0926770456d | -14.54471 | -48.79379 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4bdc6b53-4794-30ce-a804-982c80bbafb5 | -14.54407 | -48.79767 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cd760898-a27f-36e6-b8e8-379d9e9489db | -14.5436 | -48.82211 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4432a28-a3a1-35b7-b5ca-1e74cddbb12d | -14.54252 | -48.78558 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b9981e11-114a-30b1-bcbf-c759cf27db31 | -14.54188 | -48.7894 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6fa1068-c66e-380b-b344-89fe5bf2190a | -14.54014 | -48.82146 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da5528ea-939d-3b07-b802-493f22a5348c | -14.53948 | -48.82544 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8388063e-b514-30cb-867e-19cfc6f7af1f | -14.53906 | -48.78496 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 30cfc955-40e3-3b8f-bbe7-2b10c5cd7e1b | -14.53842 | -48.78879 | 2024-10-06 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2433e160-bddb-3669-9f9f-ae5e6352cd8b | -14.51303 | -49.26828 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2adf423a-3cf8-3e39-bfa3-95c9a0db634d | -14.50949 | -49.26773 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf787b34-657d-3b1c-abde-356bc5476ea8 | -14.50526 | -49.2712 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de93cddd-2982-3b90-ba60-0f1e8b4e6ba6 | -14.4827 | -49.27562 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3747ed59-e1b1-3a56-9341-43426637449b | -14.47988 | -49.27085 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49d1a733-d8fc-3d36-ad72-38c522db6c04 | -14.47972 | -49.27239 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dbd8f7bf-2374-36a3-b545-3ed7f688af1f | -14.47918 | -49.27491 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 846deeac-ac1d-344d-9a30-9c498e655e55 | -14.47904 | -49.27646 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6120242c-bd19-3bc9-8bd7-471f897b3c79 | -14.47849 | -49.27897 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73a1fd76-1058-311a-90d6-0db67ff2b5fc | -14.47687 | -49.26771 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d200355-b2a3-3bc0-9b46-d740fe6f0cd8 | -14.47635 | -49.27022 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 046b3627-0752-3e68-89b4-a82924561d9d | -14.47619 | -49.27175 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 65dd669d-5113-3ef5-8ec3-b5642334f5e8 | -14.47565 | -49.27428 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad1ec601-723e-363f-a617-c3bf584e1e10 | -14.47552 | -49.27583 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fc79be16-f57c-3374-ab1a-d71932692652 | -14.47266 | -49.27115 | 2024-10-06 04:19:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3bced634-bfe4-35f3-a922-38ef49857047 | -15.0528 | -49.70531 | 2024-10-06 04:19:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 218e63ff-e22b-3f19-8f91-332c2cabe365 | -15.05169 | -49.47301 | 2024-10-06 04:19:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ba53727e-4eb5-3462-9b90-bccf1fd9baec | -15.07806 | -48.94495 | 2024-10-06 04:19:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98c9ad4c-8b0e-3136-b8cf-17748e92b718 | -15.05239 | -49.4689 | 2024-10-06 04:19:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 206f3875-b4b9-3cd9-ab5d-4d472f4a7301 | -15.04885 | -49.46826 | 2024-10-06 04:19:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32350730-af43-3b14-b68f-2d770ed5073b | -15.04815 | -49.47237 | 2024-10-06 04:19:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5162df10-8e35-36ad-82b5-05aadfebf926 | -15.08013 | -48.9437 | 2024-10-06 04:19:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8d722c4a-cfdf-3787-b3cb-ff82c535d1a5 | -16.10363 | -50.23895 | 2024-10-06 04:19:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee544142-c348-3b84-84ee-0c3ace6a05fc | -16.10288 | -50.24327 | 2024-10-06 04:19:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15ce0b23-9339-38e2-b05f-2bea17d9cd66 | -16.07595 | -50.24759 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b093cc5-ba5e-365a-bb88-35d681432c5d | -16.09717 | -50.2331 | 2024-10-06 04:19:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae17eb38-0edf-3f5c-8488-74b815a016a7 | -16.0674 | -50.23237 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c890566-0248-3be5-9399-10ff76870fbd | -15.75702 | -49.93738 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ff29b7b-1cc6-34d6-9c73-1f45ae76e33e | -15.75343 | -49.93673 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c53905d7-586b-3b22-b7fb-6bd2ab6fb2a7 | -16.1727 | -49.25987 | 2024-10-06 04:19:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18bdc94a-ca1d-3c97-b365-ead0b43e6d3b | -16.10003 | -50.23815 | 2024-10-06 04:19:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebcfd87c-11ff-3dbf-9346-4067e51bbf97 | -16.09643 | -50.23737 | 2024-10-06 04:19:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b7ee887-ca12-3c2e-893e-32f586818254 | -16.07575 | -50.27017 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b024c25e-0707-3444-8196-1afd9ff06124 | -16.07554 | -50.22854 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1ca5af8-46c7-3be5-81f6-f10fd76520ff | -16.09357 | -50.23233 | 2024-10-06 04:19:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4d6e15e-2188-3f44-81e3-c5e3e8d6ca68 | -16.07309 | -50.24255 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 098ee60a-768a-3e4a-8e73-2b17a4efc2c1 | -16.06661 | -50.23688 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a3b3139-6847-3512-ab53-9878837e6d15 | -3.48314 | -48.91106 | 2024-10-06 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 787edd81-6f38-384e-ba37-d698b0af996e | -3.12852 | -48.96225 | 2024-10-06 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b037141d-3664-3fb0-8af0-ba233a65df91 | -3.12741 | -48.60576 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ff9d1808-62e2-3b46-90c9-80909661fe90 | -3.12659 | -48.61086 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| a44a3435-39e8-3522-a06d-f13cdf7035dd | -3.12577 | -48.61593 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |


[Clique aqui para ver as próximas entradas](README75.md)
