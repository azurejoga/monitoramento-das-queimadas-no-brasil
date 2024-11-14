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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb7ea811-097f-3a48-b396-d99e2a633603 | -17.59316 | -57.49799 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 810fee96-530f-3b5a-b9d1-6dba091424d7 | -16.10244 | -60.09723 | 2024-11-14 05:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d08ef1c0-b52b-3bce-8407-d2120f9571a9 | -15.87848 | -59.29661 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 95cf87f5-3b17-30fa-8ef4-e83d76620b9f | -16.95325 | -57.63921 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7cc11dd1-02ca-3c08-a183-55e6aff40869 | -17.5899 | -57.40721 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 85ad7fd4-9abe-32df-b134-abf608ca3079 | -17.26483 | -57.47784 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 48365494-4c7e-395e-ba13-34713a9826d3 | -17.59709 | -57.47235 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 131065ad-2b61-3a16-9c5b-900dd3407630 | -16.03725 | -60.05024 | 2024-11-14 05:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd0c77dc-96b6-3f30-af41-720a20a994cf | -17.57418 | -57.53234 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| c2099177-3baf-354c-9f47-e6587165a007 | -17.63433 | -57.54239 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0b9e84dd-956c-324e-9721-3a62630ce43b | -17.60591 | -57.54889 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b060ab23-2a0c-3462-9bf3-4f3a07a88124 | -17.24089 | -57.47759 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 215eeebe-525c-31f3-a2ff-2c14a1f97aae | -17.61203 | -57.55366 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 81385eef-3f88-31fc-a2d8-74581f5d9666 | -16.00967 | -59.39188 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9be9ae3-af09-318f-bd2d-3572c9490d61 | -17.57028 | -57.53544 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2ed04902-d192-3e08-a85f-d810d2bf9c93 | -17.61706 | -57.54325 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 82fff266-432d-398f-9063-23bd0406d98c | -17.56638 | -57.53853 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 42febd76-c6fc-3806-b254-889dce11481c | -17.58864 | -57.54976 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6430d44c-aec3-31d3-b577-0c6ebb7861d4 | -17.59988 | -57.47658 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| e6cc79ae-9e35-38d5-a0ad-d5a693f1d46c | -15.64632 | -57.67168 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b0789f0-a2f4-3173-9b63-7d85d6fd6f3e | -16.94935 | -57.64228 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6192da9c-3f51-3631-8fa5-f3f5347f21f8 | -17.63226 | -57.44436 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a29a966a-9b2d-38e3-af9d-96acab8030ba | -17.58151 | -57.43968 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5ee9cef2-aff1-3ac2-bc30-8f4716a565f9 | -17.25759 | -57.48038 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 025dfb18-7814-3b5b-8fc9-385071c8f935 | -17.5966 | -57.40832 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 097eef3c-ecc7-312a-b31a-096164a05139 | -17.24313 | -57.463 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 9e6116bb-de75-355e-a978-db71e971c285 | -17.29452 | -57.30647 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0862c9b6-bc0d-3b35-8d20-6a52f2724968 | -16.95212 | -57.64646 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 70b89822-5fbe-3a19-9b1c-aa04054c7350 | -17.59367 | -57.53934 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8b569797-e82c-303d-8669-f25a7699a093 | -17.23253 | -57.48742 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6ce1452b-06f1-33ca-a9b8-869f0a479e15 | -16.19027 | -59.35817 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 559923e2-fc54-3b17-9b0f-ab382e5d2a7a | -17.29061 | -57.30958 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 054963e3-9f45-3e03-899b-a39a1576660f | -17.24591 | -57.46721 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d1ab9cb0-f8f9-3f1c-b9ba-e73199e99f43 | -17.26705 | -57.4857 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a4ddb63c-8ca9-3a90-98d1-335cb7f1de1e | -15.87294 | -59.28805 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0c60aef-0a7d-3b0f-9c0e-2d64d6f21784 | -17.23866 | -57.49218 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 56a1e3ee-913f-3fc8-a53c-7d7763da65a2 | -17.2899 | -57.4708 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b07e6768-611d-3301-a998-48ce9f1cb254 | -17.2615 | -57.47728 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 3d171dad-9c61-3d9b-abd4-93e0d3659013 | -17.60266 | -57.4808 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| dde8d8c2-f52f-3133-a466-62f7588aa343 | -17.59763 | -57.49123 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3b121866-39a2-3d1a-a5d4-33a679a13660 | -15.91474 | -59.28758 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e39adff9-613f-3ea3-bebd-be0cdf84a32b | -17.27374 | -57.48681 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 240acf6d-5b08-3264-aed6-8f85bc04d2bb | -16.21059 | -57.52129 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c86e2546-a3e6-3b0d-adc3-98067fa5eb5b | -17.59875 | -57.4839 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 3d5de7b8-4f04-3f91-b85c-f17f08d226f3 | -17.21209 | -57.22949 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8dfe542c-3f40-37b5-bbe6-82ee9a6ebdd4 | -18.33221 | -55.58943 | 2024-11-14 05:05:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 88239cf6-c4a5-3524-a379-7537096da59f | -17.57918 | -57.54442 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4fef3a3b-18b2-3cea-884c-21b19e096991 | -17.58031 | -57.53711 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5636a72f-19cc-3fdf-9f49-b912a8223564 | -17.70623 | -57.53127 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 030b7088-68cf-33b2-a830-30bb290dd921 | -17.57806 | -57.55173 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.3 |
| ce73a382-b237-3322-8299-6094ab8f0dd2 | -17.56806 | -57.52757 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| d7353572-0866-3b7d-892d-5c4a0376b472 | -17.69396 | -57.54423 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c8685b0f-36a5-3dab-add6-28f3c390cf89 | -16.18689 | -59.35757 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5c2e4f0-f95b-3bea-8ef3-2f0f8333ff28 | -17.57817 | -57.43912 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bbc63055-1a01-3d26-89ac-ace6fdf18c0e | -17.25259 | -57.46832 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| c800fb8e-0ac1-3dba-82d3-a4e64180ffb5 | -16.94602 | -57.64172 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0631e5de-abdb-31cf-9437-9ee5a7065776 | -17.59198 | -57.55031 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 006578e7-3837-37e5-a430-0ba50c861f82 | -17.65621 | -57.46716 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| c2e6af6c-86d1-396c-9c9d-a14dae9659ca | -17.25481 | -57.47617 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f5e07ecf-ed3c-3523-b13f-4f1b84a7a59e | -17.59923 | -57.54777 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6a0639fe-5f19-3b18-9176-e3612bf5d2ce | -16.00186 | -59.10124 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d1ac0cf-d09f-3839-a519-888a17569f1c | -17.59594 | -57.50221 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9d1532d8-37c2-3910-9b10-74d8b014c78d | -17.25425 | -57.47982 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ae20c1c6-8018-309d-9d7f-14f783c1a942 | -17.59142 | -57.55397 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b76a0460-90f5-3f0e-90af-62464f65b43d | -18.72802 | -55.5795 | 2024-11-14 05:05:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 968fc70e-4f5d-38e2-8160-cc84de4e4a6d | -17.29715 | -57.46825 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f8453b0d-2773-3283-85e1-9cfb97a4e4d3 | -15.93405 | -59.27575 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f94a5214-6b69-32f5-b5b8-fc550f6fd9a3 | -17.58655 | -57.40665 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 69b65d00-6ac5-3600-8fc9-a887585be166 | -17.27317 | -57.49046 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8459ae92-7816-3154-b5bf-b5d1cadf9f71 | -15.9086 | -59.28265 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d6181a90-ee76-3de4-8704-0f2134df97c8 | -17.71011 | -57.55068 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e302b3c5-9dc1-35a3-970f-ae7ea13f5bd5 | -15.6509 | -58.80762 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7d6516c-f49d-3b84-a12f-555d6bae6781 | -17.26818 | -57.4784 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 81b1425b-670f-3a21-bb85-d3d11f39ffda | -17.26873 | -57.47475 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f370103b-1072-3d95-9fda-61f819573be4 | -17.62986 | -57.54914 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 1e153a5c-8ef7-3f5c-a7a0-e51fe6117e30 | -15.90184 | -59.28144 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9df861b5-ff55-333a-87ad-1aa4d5b8b12b | -17.58808 | -57.55341 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| c5eaa6f9-1965-39a9-9977-09433d2e24e5 | -15.93068 | -59.27514 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a44c13a-aa6e-3586-96ea-f8a2acb48c4a | -15.8791 | -59.29283 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab934a54-7515-3ca3-88a9-2840e342cb76 | -17.59819 | -57.48756 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ccb03cdd-2c42-3d28-a4a1-2a5d292535d0 | -16.07577 | -59.71118 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29f24237-9a8a-31bb-b5d8-128e0479fb2d | -17.81768 | -57.37601 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5d101bc7-43da-3944-bcdc-9f3b169e9dac | -15.89846 | -59.28088 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d502f30-5257-3acc-a817-1c537fcd9a57 | -17.72189 | -57.49629 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 535cede2-3106-3e24-bbf9-491fc36121de | -16.94658 | -57.6381 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| ffab81bf-8ea4-34c1-a658-326fcdb99c43 | -17.59254 | -57.54665 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d6608e5a-8d15-3c46-bf87-67d9295edc7c | -15.41327 | -58.60649 | 2024-11-14 05:05:00 | NPP-375D | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de5d9195-40f7-3da3-90d5-8903c3bbf6fb | -17.60534 | -57.55255 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| aab16fc2-c04f-357a-b9a2-12f5765a136d | -15.91197 | -59.28326 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddb6e0fe-93db-3f8e-969b-d6d492c8a1ad | -17.70733 | -57.54646 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a5a2ed81-7cd4-36c0-974e-209798d8e9d4 | -17.58486 | -57.44024 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 86bca429-7dbf-3bd0-953a-19e2164a37e8 | -17.61259 | -57.55001 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| ea6c1f8b-70b6-3709-9a68-c0e4e0d4490d | -17.26427 | -57.48149 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| f893877c-9d09-34eb-b82d-b4a172154741 | -17.58926 | -57.50109 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7075b2f6-a2b5-3b1d-a417-8575cc8a560c | -17.6204 | -57.54381 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3c4934a3-87d3-3c4f-9df7-482a09eb33f3 | -15.92392 | -59.27399 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6aa6aafd-c717-3230-83bf-5f64fd0ebfa1 | -14.49654 | -56.91507 | 2024-11-14 05:05:00 | NPP-375D | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 406c4739-ea66-3a1f-83df-2424ca0462b4 | -17.59822 | -57.46502 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 33e1a5eb-927a-3aa6-8b12-c89b0d9dbeae | -16.00906 | -59.3956 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f0937e7-1ede-3793-9111-b81b951eeeda | -17.60041 | -57.49545 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README50.md)
