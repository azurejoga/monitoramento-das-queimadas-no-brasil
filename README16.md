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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d40621d9-9bc5-3741-93f3-2f6606c213ae | -11.2809 | -60.503399 | 2024-10-12 01:18:40 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d5ccbabd-0c72-31a6-a1e2-1bdf31187c95 | -11.2689 | -60.494499 | 2024-10-12 01:18:40 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aadf51fc-22e3-3352-a973-bf65c9e0331a | -11.2712 | -60.505402 | 2024-10-12 01:18:40 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 54806fe1-3ca9-36a2-bd20-9f7317caf462 | -10.55 | -57.718399 | 2024-10-12 01:18:42 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca7f0c0-6774-3ba5-86a0-8a33382b3cc8 | -11.1821 | -60.616402 | 2024-10-12 01:18:42 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| efd0f2e1-e637-3b01-a1f3-5a93ccccb5f9 | -11.1844 | -60.627602 | 2024-10-12 01:18:42 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c048a443-c22c-3d6c-a70f-ac0245860005 | -10.5483 | -57.7108 | 2024-10-12 01:18:42 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1fcbfc29-bc9c-3673-af1e-a2493fdc8e8e | -10.4305 | -57.223598 | 2024-10-12 01:18:42 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4609a3a6-884b-35b8-b13d-c7e7c58e1ced | -10.5227 | -57.780998 | 2024-10-12 01:18:43 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 046018fb-3fb4-39a9-b8fd-9c744eaeb075 | -10.6568 | -58.394501 | 2024-10-12 01:18:43 | METOP-C | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 213f4e6f-1d20-33cd-a58d-2d41e66edb2c | -10.6586 | -58.402802 | 2024-10-12 01:18:43 | METOP-C | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b68991c1-c440-38b8-8cf3-1a460fe78d64 | -10.6531 | -58.7556 | 2024-10-12 01:18:44 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98c89a1a-d8e2-352e-b434-afe82df1e7a9 | -10.6549 | -58.764198 | 2024-10-12 01:18:44 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 725b24d0-f11e-3217-b49d-842c9d18f438 | -10.6568 | -58.7728 | 2024-10-12 01:18:44 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34b4c8f9-ae29-32a1-9c85-1f7c0a3b6d00 | -10.3014 | -57.709 | 2024-10-12 01:18:46 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50b53be3-bf6f-3b0c-af7a-349d369529a2 | -10.2818 | -57.713299 | 2024-10-12 01:18:47 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7115adf6-eb18-3405-8479-83248caa0211 | -10.4792 | -58.7575 | 2024-10-12 01:18:47 | METOP-C | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ff260f0-8d68-3161-8015-2345d0316e2b | -10.4694 | -58.759701 | 2024-10-12 01:18:47 | METOP-C | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 269981a0-556b-3bb6-9368-70cf046348f1 | -10.4712 | -58.7682 | 2024-10-12 01:18:47 | METOP-C | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 402f3891-ecd3-3998-961f-319f77300187 | -10.2433 | -57.818298 | 2024-10-12 01:18:48 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28159596-85db-3480-9f28-f77f98673166 | -10.1381 | -57.761002 | 2024-10-12 01:18:49 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2bc40b87-cb50-39a6-a710-d03ce4855cc8 | -10.1398 | -57.7686 | 2024-10-12 01:18:49 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aee93192-cfd4-37b5-a06e-7e42a6cd6083 | -10.1267 | -57.755501 | 2024-10-12 01:18:49 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62e425bb-7b6e-3ff4-a48e-3d30307dc6dc | -10.1283 | -57.763199 | 2024-10-12 01:18:49 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8b820c0-fbd3-34c9-b228-b3d800e591c8 | -10.13 | -57.770802 | 2024-10-12 01:18:49 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c615075-1e2e-35fb-81bf-fe30a992583e | -9.5841 | -55.791199 | 2024-10-12 01:18:51 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4f80885-264a-3c5a-b9a7-25bc8f673fa2 | -9.5857 | -55.7981 | 2024-10-12 01:18:51 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b858a78e-5221-39cc-9b61-f606de7cea7c | -9.5872 | -55.805 | 2024-10-12 01:18:51 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 56a9a5cb-2a8e-380d-891d-34e2fdf91eca | -9.5759 | -55.800301 | 2024-10-12 01:18:51 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a57048b3-e18a-37b4-b721-bedd1de88b23 | -10.4591 | -60.094799 | 2024-10-12 01:18:52 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 342cd51b-fa0f-3409-9eb9-70542de4faa0 | -10.4613 | -60.1049 | 2024-10-12 01:18:52 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 847c3075-8aa3-398d-a0e9-c7b8ff6ceaee | -9.9562 | -58.101601 | 2024-10-12 01:18:53 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9a7d3df-0ebd-3278-92c3-ebf8b7f441a1 | -9.9464 | -58.103699 | 2024-10-12 01:18:53 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05e2dee7-59be-3380-ba53-ded98a713b83 | -9.6718 | -56.957298 | 2024-10-12 01:18:54 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33c936f1-4fb6-3534-980e-bf02c45c8f10 | -10.4354 | -60.997002 | 2024-10-12 01:18:56 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2536172c-ff64-36c6-89e9-076ab5d06936 | -10.4232 | -60.987598 | 2024-10-12 01:18:56 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6582ad8e-0377-3f8d-9b2b-0886411a1715 | -10.4256 | -60.9991 | 2024-10-12 01:18:56 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9cf294fe-420b-307f-9751-f2b7074dd373 | -10.4771 | -61.2444 | 2024-10-12 01:18:56 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 364a5290-4c49-35fc-8086-73edda10ed9f | -10.1729 | -59.8564 | 2024-10-12 01:18:56 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e786b39-aae5-3038-90bc-017b0240dca8 | -10.175 | -59.8661 | 2024-10-12 01:18:56 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88dd2fc1-0c14-303e-b6e4-533e0a1fd02e | -10.4673 | -61.246399 | 2024-10-12 01:18:56 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1de8d223-feb4-3dc7-adfb-56c2c05d2ab9 | -10.3938 | -61.187599 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf506873-833c-352c-8ee6-5974206ee8f0 | -10.3963 | -61.199402 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85bc3329-0818-35b3-94d8-2245483c241d | -10.3987 | -61.211201 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8189892-55b8-391f-b112-a04559b6b6b4 | -10.4087 | -61.258598 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0be2b186-260e-323f-a5fe-3176fc6a34e6 | -10.4112 | -61.270599 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54d44243-41f4-310c-9612-b186f859dee3 | -10.3791 | -61.166199 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0fd9ce87-bf83-32d6-9ca6-701d1edeab89 | -10.384 | -61.189701 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5cd0bd-5cd5-3b37-8451-8a0ce3a5f2ce | -10.3865 | -61.2015 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c238ac1-ae99-3fd9-bbcf-61d13d935413 | -10.3889 | -61.213299 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b64f2a02-c1e6-3342-aa80-51a705c5ac0f | -10.3989 | -61.2607 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11a28e9d-d92d-3e08-945b-4d05364fc86b | -10.4014 | -61.272701 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0763434b-f960-3da5-96a6-573b686e97b3 | -10.4039 | -61.284599 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60834dfa-8557-3ddb-a91f-f61298bced11 | -10.3694 | -61.168201 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db185cca-3e43-3eb0-a1a2-7739f6898224 | -10.3792 | -61.215302 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 093473df-7fa7-3e75-869a-6392e6587319 | -10.3817 | -61.2271 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 111587f2-7019-30c5-ae4a-6e27ccb6cc00 | -10.3842 | -61.238998 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c06fa90-a809-3b6f-93e5-0b5fe8f9430d | -10.3892 | -61.262699 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd4abf64-38d6-36a1-a38e-2ede81aab70e | -10.3917 | -61.2747 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e9a69cb-396a-3afc-b6a4-b25f55072c43 | -10.3694 | -61.2174 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb6f918c-5828-3c23-a2c4-264b2e9cef65 | -10.3719 | -61.229198 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8b6b697-c9c8-37c7-ac75-3718a3a659ec | -10.3744 | -61.2411 | 2024-10-12 01:18:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42f8764a-5e11-34d9-80a6-7e65d4aab555 | -10.8571 | -63.8908 | 2024-10-12 01:18:58 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a3220d58-1f74-38e0-8160-dbc56bc06d09 | -10.8608 | -63.9091 | 2024-10-12 01:18:58 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d2b9204-2082-3f27-b28d-3e27ef00fd05 | -10.1894 | -60.894901 | 2024-10-12 01:18:59 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec57836d-63fb-3350-b2f2-64712ac9ea0d | -9.9345 | -59.937698 | 2024-10-12 01:19:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0fc056e-4ada-3583-966b-8589094ab822 | -9.8706 | -59.830601 | 2024-10-12 01:19:01 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 988124e1-436c-34be-a4bb-d0031cdd839b | -10.4973 | -62.9646 | 2024-10-12 01:19:01 | METOP-C | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c3275871-cdbc-3688-860f-0c2776e8c35e | -10.5004 | -62.980202 | 2024-10-12 01:19:01 | METOP-C | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0b87371f-daa1-307a-9277-9e149b5b3d1a | -9.8605 | -60.117699 | 2024-10-12 01:19:02 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b6acabe-1c60-3e45-a8d6-57822ca7322f | -9.8633 | -60.2743 | 2024-10-12 01:19:02 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e691f4f1-9d73-334e-bed3-bc86249593b7 | -9.8655 | -60.284401 | 2024-10-12 01:19:02 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fef2b382-79e2-300c-a910-8b2a1d2dedcb | -9.8513 | -60.2663 | 2024-10-12 01:19:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58fedcc0-8a46-36c6-a1db-b9d91988065c | -9.8535 | -60.276402 | 2024-10-12 01:19:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62fd6c0d-7575-374e-b219-9a21a560cd7b | -9.8557 | -60.286499 | 2024-10-12 01:19:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb61baa9-8d5a-375d-ad3d-7837527fc48e | -9.8438 | -60.2785 | 2024-10-12 01:19:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e91ace2-506e-3fe6-a6fd-9244125a526c | -9.8459 | -60.288601 | 2024-10-12 01:19:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a0a968d-422e-3599-9ee7-bd98f45bb090 | -6.0898 | -44.641701 | 2024-10-12 01:19:04 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f00e7847-a67a-3817-8354-168b7fe292f7 | -10.5704 | -64.024399 | 2024-10-12 01:19:04 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5c597d0a-1028-3d24-a082-2166e8f95bc5 | -9.2249 | -58.278599 | 2024-10-12 01:19:06 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c1cb3e5-f8e6-35d2-a27a-b98d609a10c1 | -9.2266 | -58.2864 | 2024-10-12 01:19:06 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3651413f-3528-35aa-8b39-f250911fc1b5 | -7.0827 | -49.243999 | 2024-10-12 01:19:06 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 494dd916-cef7-322a-b576-07ddcf89c5de | -8.4342 | -55.450001 | 2024-10-12 01:19:08 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1965033a-37e8-3f4e-8bea-ae7df00c6255 | -8.4358 | -55.456902 | 2024-10-12 01:19:08 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53b80582-d29c-3bd9-96e6-2a3810298cb1 | -8.4373 | -55.463799 | 2024-10-12 01:19:08 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dda0eb9d-9b20-38c2-9d08-ae211691ab27 | -8.4389 | -55.470798 | 2024-10-12 01:19:08 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95226975-95a7-3b99-8496-b5cd8abd0f24 | -8.426 | -55.459202 | 2024-10-12 01:19:08 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9c30c7c-549f-3b15-94d3-ea560e4699af | -8.4275 | -55.466099 | 2024-10-12 01:19:08 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acfbd3da-cfc6-3fb8-99b9-91962f911aad | -9.221 | -59.763199 | 2024-10-12 01:19:11 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0dc48ade-26f8-3ffe-8769-a2077f987e1a | -9.2231 | -59.772499 | 2024-10-12 01:19:11 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 616df1a7-22e1-3483-bd46-ecc4485d584d | -9.2112 | -59.7654 | 2024-10-12 01:19:11 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48fc6d9e-d85f-3c2d-96a7-0ac867bb2dd5 | -9.2133 | -59.7747 | 2024-10-12 01:19:11 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c546465a-7146-3829-8039-2a690be77977 | -9.3939 | -60.9011 | 2024-10-12 01:19:12 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9810cd9-0433-30fb-9410-1ddea9a67434 | -9.3963 | -60.911999 | 2024-10-12 01:19:12 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4329ada-165b-3dbc-b85b-a5c23a55e062 | -6.4265 | -48.253201 | 2024-10-12 01:19:13 | METOP-C | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 88d22a7e-5472-3e81-a95a-3661d9c77626 | -6.4307 | -48.269901 | 2024-10-12 01:19:13 | METOP-C | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4633df53-5841-389d-958e-8ed9e07c49f0 | -9.2362 | -60.355099 | 2024-10-12 01:19:13 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2fef0080-14d2-3030-beff-984ffe8f4651 | -9.2383 | -60.3652 | 2024-10-12 01:19:13 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d18ef08-6e6d-3afd-b8c4-335fb28cc9dc | -9.1851 | -60.355598 | 2024-10-12 01:19:14 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5f20c9e-36cf-3560-bebb-022282ee80e6 | -9.16 | -60.381901 | 2024-10-12 01:19:14 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
