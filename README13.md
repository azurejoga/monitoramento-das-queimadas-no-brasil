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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f67492f-a2a1-3126-b8c4-5bd7f08f016c | -17.0623 | -56.089298 | 2024-10-01 00:50:43 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bf4f093f-6bd4-3558-9a62-2f0d3ca0b828 | -17.0805 | -56.1838 | 2024-10-01 00:50:43 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52271393-eb23-3c1a-b98b-d441e1d6f1ad | -17.026199 | -56.0602 | 2024-10-01 00:50:44 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6899ee51-2840-3a19-9e3b-a62a0574279f | -17.014299 | -56.050499 | 2024-10-01 00:50:44 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bf02b15a-c19b-37ae-8f92-1aaad6229251 | -17.0165 | -56.062199 | 2024-10-01 00:50:44 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a249b2f-cfe4-38f8-9878-350f917a2cea | -17.106001 | -56.691502 | 2024-10-01 00:50:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f5c88ba3-e3e6-372b-8e72-66df71661b8d | -17.1084 | -56.7043 | 2024-10-01 00:50:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 20b9f808-df21-31ff-8198-06cfc1127bf1 | -17.093901 | -56.680599 | 2024-10-01 00:50:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2029b7c7-2e10-3316-931e-17c47928fd08 | -17.0963 | -56.693501 | 2024-10-01 00:50:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2cba4735-0736-3053-9523-a8c8436ce764 | -17.0987 | -56.706299 | 2024-10-01 00:50:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 14043f97-6e45-3db7-9f9e-897a1f1a2584 | -17.101101 | -56.7192 | 2024-10-01 00:50:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c2ccf13c-69b5-3182-94b2-dea8aef09c73 | -17.081699 | -56.6698 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1aaa72e-488c-33d4-9261-dca2eb32911c | -17.084101 | -56.682598 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9706668c-1aab-32c0-aa95-cfce63d2888a | -17.0865 | -56.6954 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cc34d217-6df3-3360-860c-19829d01072c | -17.0889 | -56.708302 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f45ea532-1cf9-3393-947a-8421bc750bf6 | -17.0914 | -56.7211 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5f0a1a8c-1ac6-3bd4-a5cf-679102a0dfef | -17.071899 | -56.671799 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d271411a-d464-39bb-8f20-9450b8b7f805 | -17.074301 | -56.684502 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c2c9f85d-d549-3c7d-83d8-57a292fcf2b7 | -17.0767 | -56.697399 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45112d9d-4537-3c7c-b495-6ede8b94cd66 | -17.0791 | -56.710201 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 764e8783-2c15-35c2-90d0-33ba2f23dd0c | -17.0816 | -56.723099 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2099f73f-0996-3b06-87c3-ae8d5b8ca1f5 | -17.084 | -56.736 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7cf338d1-71f5-3896-b666-f8875dec7437 | -16.968399 | -56.1819 | 2024-10-01 00:50:45 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bee6c661-3e72-3bf5-b1e7-3b86d96392b0 | -17.062201 | -56.673698 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e4cc02a-5d46-3010-95ec-dc26e2b51021 | -17.0646 | -56.686501 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 711d6a23-cbe3-3ac7-9f0a-a6f989bee3a1 | -17.066999 | -56.699299 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d4ca920-7d49-3d56-a39d-d28d80147266 | -17.069401 | -56.7122 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1174ac3b-6d1c-3e64-86c2-337a9fd2a066 | -17.0718 | -56.724998 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fb943106-4478-3cd2-9bdd-500f77c74048 | -17.052401 | -56.675701 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b7bcf1c4-1fa3-33ef-aa6c-9b8c026f79e1 | -17.0548 | -56.688499 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ab16d5c-8286-3308-bbfb-2e097b119cc0 | -17.057199 | -56.701302 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 078da07a-036b-308a-ae59-4bbb4da14dd8 | -17.062099 | -56.727001 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ee83d664-0353-344d-9110-2322451fb11f | -17.064501 | -56.739899 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 39a3bf7f-5b94-3e3a-af68-0f6afed89efa | -16.9443 | -56.162201 | 2024-10-01 00:50:45 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 09dfdd7b-0a54-36f2-aa4c-d519c33f6276 | -17.0474 | -56.7033 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cea0cf0e-9cca-3536-91d1-981378807e91 | -17.049801 | -56.716099 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cdeae846-2318-3407-a54d-24457d08a8cd | -17.052299 | -56.729 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 060eec4c-91a7-36af-b579-6b5483897acb | -17.054701 | -56.741901 | 2024-10-01 00:50:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 169a1b5f-72db-34d9-bbef-d3206dbe336f | -16.9345 | -56.1642 | 2024-10-01 00:50:45 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 44719197-6c41-3aaf-a0d8-27c14814d304 | -16.9368 | -56.175999 | 2024-10-01 00:50:45 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae2a431f-84a4-34ab-b362-714d0bb36a58 | -16.859301 | -55.879501 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c7d0251-c3c2-3ebe-8b7d-2fc7b2ad3d5c | -16.8615 | -55.8908 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a989972c-d405-33f9-9b19-ae0ea438bda6 | -16.863701 | -55.902199 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 29349d17-c58c-3d20-8edb-6abf8cbe432c | -16.8517 | -55.892799 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 888e4498-cdad-3d6c-8c91-4c5bc89500a8 | -16.853901 | -55.904202 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ea79d3d-7fce-3790-ac6c-190a57fc1e60 | -16.8561 | -55.915501 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1bbef84-a264-3dca-a24e-ac17ced6d267 | -16.858299 | -55.926899 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aced931d-8609-3331-9398-dc707149b197 | -16.447001 | -53.909401 | 2024-10-01 00:50:46 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15cd0256-2be9-3245-9733-74ecaf75c6b1 | -16.448799 | -53.918098 | 2024-10-01 00:50:46 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 03db32ce-87a7-325a-aa97-b2dff479d225 | -16.4506 | -53.9268 | 2024-10-01 00:50:46 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b752679d-da4e-3a4c-a7c8-11df42907c27 | -16.841999 | -55.894798 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 02b0593f-7ca7-3b52-8086-c49e475567d4 | -16.8442 | -55.9062 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 331eab85-555d-3d40-ad0f-538c40db4445 | -16.846399 | -55.9175 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2f4a28ed-d636-3972-a883-6f15c649c9e8 | -16.8486 | -55.928902 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| edaf0304-9342-3b81-ac2b-b982cae0df8c | -16.435499 | -53.902802 | 2024-10-01 00:50:46 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 18a18a06-794e-39f5-9028-d82527bb9cc9 | -16.4373 | -53.911499 | 2024-10-01 00:50:46 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a6870ec-7856-3290-92f7-a8bafc766333 | -16.814699 | -55.8069 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9ff3c8f0-0f6d-3c45-ad32-01f16ae114ce | -16.836599 | -55.919498 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a90aff50-159a-3f36-95e2-aaf93e1659df | -16.8388 | -55.930901 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c54770f4-c891-3110-af1a-2c6bd2702056 | -16.802799 | -55.797798 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9d4c4af3-55bd-3597-9da6-9dd3443113d3 | -16.804899 | -55.808899 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2fee0863-63c1-39cc-85d0-ec97e5f7c93a | -16.813601 | -55.853802 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4b733c12-0954-3cc0-b475-8508f84229ed | -16.8158 | -55.865002 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dcfa3b52-e018-3dab-b426-55cd129b88e4 | -16.8246 | -55.910198 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a042ca84-db13-3cab-ba56-87f23583e4d4 | -16.826799 | -55.9216 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d7dd08cb-c697-30ff-8859-6e224f9d4ddc | -16.829 | -55.932899 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a5f19bce-334a-3925-a58f-ce0b3e5a801c | -16.8312 | -55.944302 | 2024-10-01 00:50:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b50c0de7-700c-36c8-83d7-cbeabd5ae405 | -16.7293 | -55.473202 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 759cd065-34cf-3b9a-8ab6-c97398bd24ba | -16.803801 | -55.855801 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c4f23311-82f5-3784-b3cb-5b3e823ad1cd | -16.806 | -55.867001 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bce6872a-49a8-3e4c-bce6-48263933ec4a | -16.812599 | -55.900902 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9be51fdc-02db-3889-93a7-822e5ed87c29 | -16.8148 | -55.912201 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| daff7b27-e07f-3578-a93c-1652084416fe | -16.816999 | -55.923599 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 768b92f1-96a3-3fd9-bdfe-b7972f54d711 | -16.819201 | -55.934898 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 24af0e0c-2cdb-322e-98cc-4ecfaec3e82e | -16.8214 | -55.946301 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3815f563-e7d1-37bf-b7a3-fc02c1fbf77e | -16.781099 | -55.7906 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4be28ffc-e2ea-39c0-87f3-6346983a1696 | -16.805099 | -55.9142 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3fd66e0d-9e89-3bee-b2a4-9444d9e1dc60 | -16.807301 | -55.925598 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5b1a71e9-6cd9-3fc1-80f3-11a45e4c36ca | -16.8095 | -55.936901 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 37ff1c1f-0f2d-3a74-a55a-3851e74f3b77 | -16.650299 | -55.175499 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2e125ec-32ee-3ba9-ab0e-1058eb2dc36c | -16.6523 | -55.185699 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 656055cf-ac57-33e7-882f-bb32532990da | -16.6544 | -55.1959 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c1abec91-bf4a-3b03-8d9a-c39c2c2d7d9b | -16.767 | -55.770401 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| baa54193-158d-3235-b88a-4b55e862898d | -16.7691 | -55.781502 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c473ea9a-a065-3d6d-978a-4417fddeee70 | -16.771299 | -55.792599 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9947184-a5b2-3f26-8833-6bdd0ce122ba | -16.6385 | -55.167301 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3c18bf3c-18e7-33eb-b6b6-f440190ec1eb | -16.640499 | -55.177502 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38cac3af-e256-31e3-9f7e-cdcdf7254827 | -16.6425 | -55.187698 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9e857824-c841-3bd2-a190-bf854039b7a5 | -16.6446 | -55.197899 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5106d94b-14f9-3283-8546-6d21bed9b6d5 | -16.754999 | -55.761398 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a07d525-4416-378d-8724-fb95c5677587 | -16.7572 | -55.772499 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dbc85271-9b85-335d-bbd3-55defc50f4c3 | -16.7593 | -55.7836 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e18ca3c-66a9-3c18-8355-cc7a90835074 | -16.761499 | -55.794701 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 54212c60-58cb-336c-893e-ed2e9f989948 | -16.626699 | -55.159199 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 44015123-d204-3d99-b2cf-6da0cd5bec93 | -16.6287 | -55.169399 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7625c897-4bb0-3d74-880b-2039298e1f0a | -16.630699 | -55.1796 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 665f2fc1-f5fe-3fef-aa4c-358ddca3e233 | -16.6327 | -55.1898 | 2024-10-01 00:50:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8f23af5c-f9ae-371b-a9d5-c5e5d96af17a | -16.745199 | -55.763401 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 96c9b0ff-9680-32f9-9e01-0bb8f37f3592 | -16.7474 | -55.774502 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 78270e7c-4ac8-3b59-937c-2a457d8d673f | -16.749599 | -55.785599 | 2024-10-01 00:50:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README14.md)
