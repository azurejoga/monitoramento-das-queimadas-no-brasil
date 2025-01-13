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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85633fae-c8c2-30c9-bd2c-b46d33b1dc74 | -28.75997 | -55.59873 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.5 |
| f363a8a4-b5f3-36b5-88c4-769ee1904663 | -28.75085 | -55.63379 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 650846dc-7c6c-3a34-a5c6-90fd2a9707ba | -28.76216 | -55.62793 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| c6825116-a74f-3844-aed7-59d7bd5054c7 | -28.75214 | -55.62585 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| ac42d0a1-b0c3-3ea9-a282-ec033e4648fa | -28.75882 | -55.62724 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| 4c723203-6fe7-32a1-bd1b-49e7eeb11d98 | -28.75753 | -55.63519 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 8dd06ece-55b1-3bf6-ad3b-afe200454480 | -28.74623 | -55.64103 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 39694ba0-0e20-3a46-9471-eeb0bddb8b91 | -28.74816 | -55.62912 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.2 |
| 9074b5bc-f2d4-3deb-af63-5c33d99f857b | -28.76266 | -55.6034 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 17.2 |
| b250d0ad-f034-3624-88d5-f63a93d9247f | -28.75625 | -55.64314 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.2 |
| 50665bf9-913a-34d0-a6f5-6b5ebce8fddc | -28.76408 | -55.61602 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 18.5 |
| a4151f45-984a-3061-b561-2b6812332c50 | -28.74893 | -55.64571 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.0 |
| c95a3ec4-3a21-34a4-9c93-dac40bf2874f | -28.74957 | -55.64173 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.0 |
| c6720c0a-485f-3a7e-a8d8-49a2d3318166 | -28.74687 | -55.63706 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.8 |
| e903a154-e3ac-334f-9c31-9619ccc1d16e | -28.75355 | -55.63847 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 8b7c8e97-9ae1-3028-929c-acfef37c5354 | -28.76088 | -55.63588 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 7a1c61d7-e506-3ac6-8f27-213d98ccd296 | -28.76202 | -55.60737 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 17.2 |
| 3261cf29-5862-3615-be60-48ed44bad8ab | -28.7574 | -55.61463 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 4a9447d6-c878-3a76-a98a-750c2d4a552e | -28.75291 | -55.64244 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.0 |
| ab241417-7649-3571-bda3-05fa975a8dcc | -28.76152 | -55.6319 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| c14877d1-49c8-3c0f-b552-bab0c04e2c3e | -28.75818 | -55.63121 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| c378cb62-cf3b-3fd2-b20f-4705f631a36d | -28.7488 | -55.62515 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.2 |
| 9916cfcb-6b5e-34dd-a441-51d1c7335c92 | -28.75946 | -55.62327 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.9 |
| 4c268cb7-910c-32c5-9753-1f901f6e0efd | -28.75689 | -55.63916 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 8d689aa9-0d6b-3e9f-a8de-d7f9196def19 | -28.7515 | -55.62982 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| b3800687-5a97-3328-88d7-46402f87930f | -28.76024 | -55.63985 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| e2102516-842e-3412-acfb-3addf61fb269 | -28.7599 | -55.6114 | 2025-01-13 04:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 101.3 |
| a0f4a118-2d8f-32e4-89fb-13b9f87c8a6d | -28.7592 | -55.6345 | 2025-01-13 04:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 76.7 |
| f4528cea-b412-3eee-a92e-ecd82dbc1e9e | 2.44605 | -60.65812 | 2025-01-13 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dde2824-88d7-3bd4-9c73-1e85195c67ec | 0.95311 | -59.4671 | 2025-01-13 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c2b1391-c754-3cf1-a02e-574fa4ad3034 | -1.46992 | -45.71007 | 2025-01-13 04:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6246a905-f6e7-3e07-a201-12bb2cccd1a8 | 0.55664 | -59.69841 | 2025-01-13 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edb38b50-cfcb-3b8d-af42-374dca63e082 | 1.11795 | -59.46066 | 2025-01-13 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0846d01-bd1c-3a48-8b08-8d1329c49d46 | -1.46941 | -45.71333 | 2025-01-13 04:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9b1899be-a0af-3502-95b5-9fdded4f20b8 | 1.93427 | -60.41136 | 2025-01-13 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6514975-af64-3650-b736-6aabd34a74e0 | 0.76527 | -60.09289 | 2025-01-13 04:59:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6e02180-93eb-3023-94a8-a8a5c58345ef | 0.56375 | -59.68961 | 2025-01-13 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7804d33a-5f5e-3a93-a26c-c20c4c756425 | 0.99895 | -60.55897 | 2025-01-13 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fb530f0-2cdf-3908-b9eb-34b2a12041cf | 0.61663 | -60.18869 | 2025-01-13 04:59:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ec51179-1101-3bac-8fe5-9539a0e70294 | 0.56019 | -59.69402 | 2025-01-13 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c0db8f6-4e1c-3a59-9f77-312eeb22772b | 0.95722 | -59.46647 | 2025-01-13 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6bb2343-075f-3457-ad0a-9c483d74c0d7 | -1.46411 | -45.71258 | 2025-01-13 04:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2eed584a-c97d-3f68-84b0-cfade0ba6393 | -1.4689 | -45.71659 | 2025-01-13 04:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 58ce51ad-cdb2-3904-8ef4-11778e54a505 | 0.66302 | -59.65909 | 2025-01-13 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79f05fa8-ec3c-3a53-9415-a9f123e1b1d7 | 1.9387 | -60.41051 | 2025-01-13 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d308dbbe-3e2d-36a2-95fd-63d5b4bb4324 | 0.74947 | -60.17699 | 2025-01-13 04:59:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4562d557-e9b0-3281-a707-8854b11e9d9e | 0.8527 | -59.54301 | 2025-01-13 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 835d06f8-68aa-3e52-adad-5f88824470c7 | 1.12208 | -59.46003 | 2025-01-13 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50f1a621-ab79-340e-95d2-f357dfe93588 | 0.56079 | -59.69777 | 2025-01-13 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87de6e90-747e-3a68-aeed-8c2902530eb3 | 0.5596 | -59.69027 | 2025-01-13 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1749be63-f2ad-368c-a646-dcc9373e96cc | 0.99963 | -60.56332 | 2025-01-13 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 414f79d2-b995-3b27-a731-170ba7dd6197 | 1.11383 | -59.46129 | 2025-01-13 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2454d620-07ec-3565-b22d-fa175a0370c2 | 1.179 | -60.50278 | 2025-01-13 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b923b43-10a4-3e69-990a-1fe172f8112f | 1.93803 | -60.40617 | 2025-01-13 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c09fdbcb-b9d7-3ed7-9202-22897e68d0f3 | 0.99452 | -60.55966 | 2025-01-13 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c934c16f-c0e1-3c9c-a772-1bae6fbdaaae | 1.17834 | -60.49846 | 2025-01-13 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab9612da-aeb9-39aa-bb62-67e6e84a2904 | -28.7585 | -55.6576 | 2025-01-13 05:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 66.8 |
| 7cc7dc7f-33fd-357a-9a91-69e7eb9bb033 | -28.7599 | -55.6114 | 2025-01-13 05:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 350.9 |
| fab87b9a-bf6c-3042-9360-3e0bc05113e9 | -28.7824 | -55.6063 | 2025-01-13 05:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 64.4 |
| 7873caea-085a-34e8-b796-314e92332fae | -28.7592 | -55.6345 | 2025-01-13 05:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 390.9 |
| 310a5d7c-f1d5-3a7a-bcdf-af1c78d20eef | -2.01311 | -52.07583 | 2025-01-13 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 997d52fe-1ba0-369a-839e-12ea3ca31163 | -2.42684 | -48.05768 | 2025-01-13 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a6e3d4e-9098-3a2d-883f-b29bb2162fbb | -3.8701 | -54.23173 | 2025-01-13 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b9f04df-52e2-34f1-8f35-29da08424291 | -2.60151 | -47.53254 | 2025-01-13 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 691d280c-3b9c-3d5f-9a03-8ef6b8f2bdc6 | -1.58328 | -54.78289 | 2025-01-13 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bc062b8-a257-3ef8-b752-c8ba9ddb33db | -3.04239 | -54.46759 | 2025-01-13 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 349a5bc6-0c08-3202-b3ee-5410d75e56cc | -3.15349 | -53.76002 | 2025-01-13 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 180bee19-7cbd-3d41-8d82-1f5c72f9324d | -2.42227 | -48.05695 | 2025-01-13 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 247b0489-fa68-3ec3-95be-293f55d832c9 | -1.14272 | -54.17155 | 2025-01-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1bfe188-6126-30b2-8362-ef12915f9960 | -3.3147 | -54.11768 | 2025-01-13 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d23bcf67-5da0-3eda-a321-044fe8ce8283 | -1.6725 | -54.17295 | 2025-01-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18ceb134-a324-304e-9898-c40683f7d025 | -1.66614 | -53.84472 | 2025-01-13 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ad56636-ed77-3df6-8b54-6774de707c2f | -3.34868 | -53.25284 | 2025-01-13 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02c0379f-66d1-341c-a85d-cdc458f2d63e | -2.60626 | -47.5333 | 2025-01-13 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab9c848f-0caa-3fb9-9a47-b822a75c2fa6 | -2.42699 | -48.05543 | 2025-01-13 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59ea4c0e-aa35-3691-8882-d9be4e870cf2 | -1.89649 | -54.26056 | 2025-01-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bd7431d-abc4-3900-8040-7d71b86dec62 | -4.12935 | -54.89976 | 2025-01-13 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc512916-414b-31c7-bb6c-abe90a9313c9 | -1.33317 | -53.56688 | 2025-01-13 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e1455e4-d314-3375-a615-bfa3adcdd89b | -22.21414 | -47.69723 | 2025-01-13 05:05:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b6ab722-7d01-3634-bbe2-749a68caee95 | -21.97259 | -55.35512 | 2025-01-13 05:05:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2376395-e45a-3686-a6bc-2583e09526ee | -22.2202 | -47.69831 | 2025-01-13 05:05:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| addcf8ec-c9ed-39cd-8a40-05e0f5bf5bef | -21.44325 | -48.60679 | 2025-01-13 05:05:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f1cf3966-dd91-34e2-bf2d-8c8089a7e9a1 | -20.47681 | -53.6764 | 2025-01-13 05:05:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62bf79b0-fc57-3aaa-9ce3-ed7dbfa29368 | -21.44287 | -48.61082 | 2025-01-13 05:05:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca7dd9db-e1d0-31a0-8b82-24ed405a09f4 | -28.75581 | -55.62333 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 45.8 |
| aa696ec9-43b2-33e3-a053-02abff6a1ed7 | -28.76163 | -55.60814 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 28.9 |
| 726d081b-54f8-377f-a7de-d173ef01dbc5 | -28.76118 | -55.61208 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 37.4 |
| aa245c4b-f579-34f9-8acb-d8d056b33ea9 | -28.75447 | -55.63519 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 33.6 |
| f7a46d05-4757-32a3-9d05-b517de9554cf | -28.75895 | -55.63188 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 41.1 |
| 86d9d4b3-ad82-3b70-ad05-500c57d232bd | -28.76029 | -55.62002 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 45.8 |
| 4ddfe143-60fe-33cd-a80c-72d046623d2e | -28.75536 | -55.62729 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 41.1 |
| 6a23d4f2-e246-3470-8feb-7ef337a426a4 | -28.74551 | -55.64198 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.5 |
| 4201f2b6-b704-307e-83d8-b12dc022f846 | -28.75805 | -55.63977 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 33.6 |
| 5678d427-f3f4-3453-943e-5f182af949f9 | -28.7585 | -55.63582 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 33.6 |
| 4ba8e23b-d1c4-302f-8242-1535a34bab9f | -28.75984 | -55.62398 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 45.8 |
| 8d6a30c2-befb-3b75-b479-89e4b5df0279 | -28.75848 | -55.59964 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| c9a57584-7192-329e-8995-fb7f2de4fca6 | -28.75402 | -55.63914 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 33.6 |
| b65def0e-a500-3255-81a1-cf06ebdbecb8 | -28.75761 | -55.64371 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.0 |
| 400f2f8e-ce94-3654-b3cb-a120771ae682 | -28.74595 | -55.63802 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.6 |
| 5c852cd5-606f-3e01-b25c-a9658cd5339a | -28.74954 | -55.64254 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.5 |


[Clique aqui para ver as próximas entradas](README5.md)
