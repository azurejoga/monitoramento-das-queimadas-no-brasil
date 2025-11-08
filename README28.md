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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e6c0470-7b6a-3d16-99fa-2612b2a7d349 | -13.77179 | -46.92147 | 2025-11-08 04:38:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7b95628-1170-3ff1-afcd-325f8005f95d | -10.98939 | -53.98584 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8614f5ea-8cbf-307c-8971-001875ee1708 | -11.73106 | -59.30936 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d53ffcf0-21b6-34df-8183-2e015f5db386 | -9.14515 | -51.30376 | 2025-11-08 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c650cb6-b599-34bb-a05f-54bb19458788 | -7.9348 | -55.01336 | 2025-11-08 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b179526d-bf3e-3154-82c9-b3b442fa3d7b | -10.9393 | -47.63911 | 2025-11-08 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e20fc83-6239-3c3f-a813-576dd59709da | -8.32436 | -55.03434 | 2025-11-08 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a1e4f07-e897-36be-a6fd-297795b2cde5 | -8.92016 | -47.81303 | 2025-11-08 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9601ec5-fbd8-3d22-8068-76849aa7fc46 | -11.96195 | -44.34781 | 2025-11-08 04:38:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f364bd1e-0336-376f-94a4-20e5556ec0ee | -8.90408 | -47.8285 | 2025-11-08 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f533bc65-0cdd-37af-adb9-2dd775d5b9f0 | -9.45083 | -48.92673 | 2025-11-08 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96f25962-8afc-3726-a501-f52595f39279 | -9.4655 | -47.87058 | 2025-11-08 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b702f41-5f4b-30a5-907d-45c897ec0829 | -9.33632 | -47.8316 | 2025-11-08 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a717321-6786-379c-a9d2-bc409be93ea5 | -11.86504 | -62.89085 | 2025-11-08 04:38:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39a64fcc-ae55-33ed-826c-d710110e3b12 | -9.38474 | -50.72897 | 2025-11-08 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af4470c5-c662-3df7-91b1-301f168ce21f | -10.54775 | -48.2581 | 2025-11-08 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b3c34a1-1163-3e23-be09-ea61d174233c | -10.99687 | -44.85826 | 2025-11-08 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b21f503-0f33-34c4-911f-432ac798bcb9 | -13.95354 | -47.4206 | 2025-11-08 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88bb47ad-d2cd-3518-a572-be9bf12eba2b | -10.62421 | -52.18658 | 2025-11-08 04:38:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ff042c1-69d9-390d-a3bc-148bea11c106 | -16.75244 | -51.3665 | 2025-11-08 04:40:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c566c5c-2d2d-382d-9fd9-22aff350bf51 | -18.33189 | -54.28222 | 2025-11-08 04:40:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47406f64-526d-3e62-a866-42e9235356b0 | -19.48141 | -53.94473 | 2025-11-08 04:40:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91c3d63a-622e-31a6-bfd1-e5ec79ecf2e4 | -18.47842 | -53.41018 | 2025-11-08 04:40:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07b7c3f4-e417-31f7-8bfc-cd3931be0398 | -18.33555 | -54.28298 | 2025-11-08 04:40:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd454604-7050-3ef6-8d40-5eff4fc29a84 | -17.62415 | -49.33551 | 2025-11-08 04:40:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d32973a-c7ab-38e5-93d1-40fbd95f0168 | -18.33109 | -54.28673 | 2025-11-08 04:40:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b93a28c2-fa9c-3493-a5a7-fdb070c9ea71 | -17.88233 | -52.39498 | 2025-11-08 04:40:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d64ffc9-f28a-32c5-a13d-afc83693e583 | -15.76894 | -52.44254 | 2025-11-08 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6f90622-c83a-3927-a3d4-5a0333c57440 | -19.3683 | -48.61206 | 2025-11-08 04:40:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 226eb1d1-65f1-3955-a4eb-35f256b317c6 | -15.76828 | -52.44649 | 2025-11-08 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5652ebfd-a4de-3c27-afb3-f1babce2e460 | -18.47915 | -53.40598 | 2025-11-08 04:40:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd8f4ddc-253d-3190-a295-a1810de315ab | -16.87842 | -52.78588 | 2025-11-08 04:40:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bc7dfc4-6cce-3cdb-82df-81d5a212d926 | -16.79849 | -49.10114 | 2025-11-08 04:40:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9eee325f-8ea3-3653-8944-4c7afce1a26f | -18.33731 | -53.07426 | 2025-11-08 04:40:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18eb5a0c-4f9a-35cf-ad01-6bbe5cfea98c | -18.02453 | -54.13686 | 2025-11-08 04:40:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdf89b62-7704-3566-8c9e-1c13d16e4836 | -17.30754 | -48.56337 | 2025-11-08 04:40:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae0e0567-5600-397f-b661-5436f366c949 | -18.20934 | -56.74254 | 2025-11-08 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 1ed54e16-3983-36b8-96d8-000e98ed6761 | -18.51135 | -53.49341 | 2025-11-08 04:40:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9279f449-ab6f-3237-a012-8d30cfbf0b4e | -17.62752 | -49.33607 | 2025-11-08 04:40:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 697dc9b6-2fa7-3392-bd0f-c03d472f4746 | -17.21248 | -47.65595 | 2025-11-08 04:40:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56797c70-9fe4-3388-b804-020fbde747e9 | -17.87892 | -52.39433 | 2025-11-08 04:40:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3eb57d1f-112c-306c-a90c-c52ddb573a56 | -26.58141 | -51.69466 | 2025-11-08 04:42:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9f736f3e-f481-3ee4-aeee-30727e5d88b6 | -26.58081 | -51.69859 | 2025-11-08 04:42:00 | NPP-375D | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f4b7db59-d2ac-36f3-a6ab-020b77904899 | 3.53526 | -51.77983 | 2025-11-08 04:53:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd1e5ddd-d1b1-3249-9f4a-57e47e868c88 | 3.69639 | -51.29252 | 2025-11-08 04:53:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7cecd32-86bf-340f-8f9c-0a80b335b9e2 | 3.36975 | -51.29049 | 2025-11-08 04:53:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2e06920-db99-3d6d-b9b9-fbb307349e40 | 3.6997 | -51.292 | 2025-11-08 04:53:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18e57714-e971-337b-99e7-559a2c0b7e2c | 3.3692 | -51.28703 | 2025-11-08 04:53:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0a7f63e-0936-38ba-be01-2619ee4c7233 | 3.37251 | -51.28651 | 2025-11-08 04:53:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0301b3aa-5212-35a8-9080-db39a06eb376 | 3.53196 | -51.78035 | 2025-11-08 04:53:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a396c912-f7f3-362e-80c8-3ac3b4da4e04 | -4.27281 | -48.34204 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 94bc348f-1711-380a-9282-4db7613d241c | -4.68147 | -46.39875 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 588c8a6b-e922-37e0-a580-49479316801e | -4.68077 | -46.40364 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9e86b029-02e5-3581-a967-5f4f74da5b2f | -4.73863 | -45.71343 | 2025-11-08 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5fb7ac88-6548-3669-a438-fa841e3a92dc | -3.44681 | -43.14606 | 2025-11-08 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ff73896-e35a-3a00-a837-b7be0cecb775 | -3.34458 | -50.18285 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b78800f-cd10-38e0-8de4-6e8a814940c2 | -5.86204 | -44.70485 | 2025-11-08 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7c45f4c-d253-34ad-bea9-a433525a5a6f | -2.61497 | -49.22306 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2223f4ff-1832-3086-bdd3-e14c2a38dd3d | -3.15044 | -50.60592 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f473efd9-3873-300e-8fef-164df6841db0 | -3.44591 | -43.1528 | 2025-11-08 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 701696e1-148b-3810-97f6-8c9c90589403 | -2.61887 | -49.22565 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a1dce400-0742-30d9-ae85-823c0d1cbad0 | -5.25794 | -47.16879 | 2025-11-08 04:55:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e608340-dedb-309d-bdcf-1a66e092279c | -3.31651 | -50.11935 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 829c7fe2-ef99-36b5-bdfb-ec1009da7d0c | -4.72957 | -42.93594 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09b7b0ff-ad05-320f-b381-f9b7cecd4639 | -5.72755 | -46.46728 | 2025-11-08 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5285770-6aea-3a74-84c0-ebd66ee208b6 | -2.84092 | -48.10476 | 2025-11-08 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17282370-4275-3117-ab82-3d0a34049d76 | -3.68829 | -52.13306 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbf4f744-072d-32c5-870a-a4cd0259672d | -3.58224 | -51.24693 | 2025-11-08 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39d76286-8000-335d-8a55-2c19755ec157 | -3.32432 | -53.36519 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3e331b43-0a3c-31f5-86f1-c92ac14e4a3e | -3.1578 | -45.49564 | 2025-11-08 04:55:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 582a8a39-afd2-3075-8e92-73ec7c333e29 | -3.44103 | -43.14514 | 2025-11-08 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca654a05-c8bc-3ec7-83f9-8613408ab801 | -3.91902 | -51.01616 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f2688be-66df-320e-b052-b169aa085741 | -3.25216 | -52.91695 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 647cf1ef-133b-3e46-bf17-f04dde2abf98 | -4.38043 | -49.67696 | 2025-11-08 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58099206-f18a-3e6e-b915-c71fe9a90e35 | -4.15724 | -46.81611 | 2025-11-08 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a3a7b9d-6f75-37b4-b3d8-05f102e4387e | -3.5278 | -47.54533 | 2025-11-08 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1216704f-a96e-3349-b2f8-f80ef9c4268a | -3.95318 | -45.45299 | 2025-11-08 04:55:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f56d7671-9a2d-3c7b-bf6a-c69d3dfa5e2d | -5.72183 | -43.53251 | 2025-11-08 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a29a193-91e7-33b8-be92-4143f656b972 | -4.46844 | -45.32539 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fa0ba73-e56c-3e4f-850b-bafc47e5e4f8 | -3.34522 | -50.17864 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebfe74dd-b82d-3f1b-bcc1-6e1c2e9b4558 | -3.71313 | -42.71956 | 2025-11-08 04:55:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03582092-8cf1-3358-b100-8d673a89fc54 | -5.0976 | -43.99378 | 2025-11-08 04:55:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca763df4-87bd-354e-8c4c-b43dc099d1fb | 1.13227 | -52.38366 | 2025-11-08 04:55:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd2e4f70-815c-340c-9d9b-d66bdd1fdcd2 | -2.46728 | -49.90186 | 2025-11-08 04:55:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d84b871-c5a4-32e6-b008-872815954266 | -3.77095 | -49.68911 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64e4e1f7-00bb-353a-af38-9c7a57d2b77c | -1.67236 | -47.40149 | 2025-11-08 04:55:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a36bb607-084c-3d3b-b581-2d554ee0e00e | -3.16272 | -45.49637 | 2025-11-08 04:55:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a8dc573-cef0-3b55-a4b1-8c8ecefc45e6 | -4.39049 | -45.36243 | 2025-11-08 04:55:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb8cf633-f15d-3aa0-98ea-3e253bcfd76d | -4.42547 | -47.60131 | 2025-11-08 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b78d7fca-ac15-30e0-b921-8e04be16d940 | -3.14982 | -50.60991 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6253ae74-8533-3f13-9836-9ed62ac69a99 | -3.94766 | -49.02443 | 2025-11-08 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6463a0c6-6f7e-3f8d-9364-a4da0632d633 | -5.43993 | -44.66169 | 2025-11-08 04:55:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cf1d64b-658d-37e7-beb6-b75dbd06e69c | -2.79334 | -50.31353 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84b453fb-c702-3858-90e7-f49b67775089 | -3.44454 | -46.19019 | 2025-11-08 04:55:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bb211481-b401-3b07-bc78-c8fec00d199c | -2.9846 | -52.82524 | 2025-11-08 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d076a219-91db-3aa7-91ce-2ba84ea7a1f9 | -4.73173 | -42.93878 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b305f016-3b98-31e4-8e9c-dec27d6139f3 | -3.3063 | -50.16108 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f26916e5-5411-3c4e-b930-709ad7c24bb6 | -2.71238 | -49.54809 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4e323d89-9046-3f86-92b0-897b8e890224 | -4.40336 | -44.08189 | 2025-11-08 04:55:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a3c3be6-9b4c-3621-bee5-07b39b063b7f | -3.40196 | -45.43853 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README29.md)
