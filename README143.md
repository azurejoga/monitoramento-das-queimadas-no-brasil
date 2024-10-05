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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d50f7adb-3ce9-39a5-9ddf-c54cbb586a7a | -16.98936 | -56.77906 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.5 |
| 4632a218-945f-3519-b95c-bc9c1d5df95b | -16.98895 | -56.78617 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.0 |
| d891fe96-1ab9-36ed-80fd-22cc945e8065 | -16.98871 | -56.78442 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.5 |
| ce167a76-8704-33a5-93e4-7eafd1d8a3ac | -16.98852 | -56.74612 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| c850643a-e1d3-3175-a071-d87237db8032 | -16.98848 | -56.74783 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| a35e0e09-21e1-3fed-ad8d-ca4696a58b93 | -16.98833 | -56.79154 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.0 |
| d1e3db8d-b509-3062-84a9-bc048f781cd1 | -16.98805 | -56.78978 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 50e41361-780d-3ae1-98b0-ef9b3897f7cd | -16.98725 | -56.75864 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 16398eca-1331-336e-9d41-609596697dfe | -16.98602 | -56.76941 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 28b9f266-69f1-3ba1-982c-50724368652e | -16.9854 | -56.77479 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| f1f37c8e-8954-31ac-9180-4a00fd8aa7d9 | -16.98524 | -56.77306 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| cf1419cb-2989-38e1-b9f4-c44815e74e3e | -16.98479 | -56.78015 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 1eac2eac-846c-397b-9ab9-c18aa7832f6f | -16.98458 | -56.77842 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.5 |
| e7dee17a-014a-3501-8caa-09722e4d984e | -16.98417 | -56.78552 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.0 |
| e5f6db0e-ba4d-3adc-852f-f4e5e0cdaed9 | -16.98393 | -56.78379 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.5 |
| 0ca06228-610b-35f6-9ccf-b7210a41a04b | -16.98355 | -56.79089 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.0 |
| 833b1f28-6688-3745-b3f3-058534235da6 | -16.98327 | -56.78916 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 3c96ace4-0427-37d1-86f5-7560cea497da | -16.98184 | -56.76338 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 999e08b9-ad9d-3bb1-9e0c-500695b0fb84 | -16.98123 | -56.76876 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 0536c52e-e5d5-389d-987f-8d94fc7431ac | -16.98111 | -56.76704 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| bfc2eb9c-87b1-3d8e-91d3-212aa260dfaa | -16.98062 | -56.77414 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.4 |
| 267a89ea-89d2-3e82-9b0e-920bdeffeb04 | -16.98046 | -56.77242 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 05bedbf9-052b-3d5e-a4dd-0b5fd379c526 | -16.98 | -56.77951 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.4 |
| 9f8a8055-8eb6-3ef0-8cf9-beb32b06d8df | -16.9798 | -56.77779 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 1feda36d-ea2c-37e0-b0ff-120e5f8db6dd | -16.97939 | -56.78489 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1dcc7515-cac6-333b-9748-1c35e0967ef2 | -16.97915 | -56.78316 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 2df140f2-08ab-3bc6-a378-018e85b484a3 | -16.97706 | -56.76273 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| d619a103-df45-30e2-bfbd-1543b8636a79 | -16.97645 | -56.7681 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 88737f10-39a6-3b8a-8268-6c07085c58a7 | -16.97583 | -56.77348 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.4 |
| a60acb3f-3d82-352a-afdf-3db0d5d52513 | -16.97568 | -56.77177 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 60587512-f61b-33d6-98e8-463ac0a791f6 | -16.97522 | -56.77886 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.4 |
| 765130af-6090-36cf-848a-b73d16145510 | -16.97503 | -56.77715 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 8bc6808e-4a06-30a2-a624-70ddec8afb7f | -16.97227 | -56.76208 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.2 |
| b5c7f5f8-bb67-36b8-9a0e-809b166f7a06 | -16.97166 | -56.76746 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.2 |
| da8b683e-76c0-34ba-be9f-e10be5d54a43 | -16.97154 | -56.76576 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 6aeaaa9c-0d0e-34f1-bbed-82ceced797b1 | -16.97105 | -56.77283 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| d30a88be-1a02-37f1-9714-d5dd02a000c7 | -16.9709 | -56.77114 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.4 |
| c9d512ee-6d72-3346-932b-c42ff02d1c1c | -16.97044 | -56.77821 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| a14f6ec3-1117-3b76-bdf2-2631d9e38e14 | -16.97024 | -56.77652 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| c125518c-a519-3cd1-995b-d7dc3b5ec8b3 | -16.96676 | -56.76513 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 0f4a4c22-bb0f-3652-908b-0c815ea3e71b | -16.96627 | -56.7722 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 4a9a2371-9f98-3e8d-a5c2-7d4b9592e16b | -16.96611 | -56.77051 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 7139924e-62e8-3c54-8ea8-75c4094c7ce1 | -17.11707 | -56.7712 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1e22d904-5fa5-3cab-88e0-310ec4450dda | -17.11644 | -56.77661 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5f58ce1a-0ff4-32d4-a4bd-f7d68dba008d | -17.11582 | -56.782 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f2753b21-4cb5-3cad-93de-b2e043b38252 | -17.11457 | -56.79279 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| ed8d055c-fa4e-35b7-b1f7-654dfbc54746 | -17.11394 | -56.79816 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 9035d173-2948-3949-92a0-78ddf1dc6748 | -17.1129 | -56.76516 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| bafb05b2-3a08-3825-8cc2-065838357069 | -17.11227 | -56.77057 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| eac1376d-7b11-3683-ae5b-75fce8f2978b | -17.11165 | -56.77596 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4613afbc-05ef-341f-b9ec-5e74f01f9b75 | -17.11102 | -56.78137 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8d68c529-b3c2-3a09-9772-52ecfd13794d | -17.10978 | -56.79215 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| d72d0c13-6f4f-3d2f-bed8-12b221fab3c4 | -17.10916 | -56.79754 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 1188c03c-aefa-323f-8fb5-09f2cd4be3d0 | -17.10499 | -56.79152 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 68760027-57ef-3f92-a26d-284e0d1b8a31 | -17.10437 | -56.79691 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 18d81288-b003-3fc0-bbb0-1a8436683f38 | -17.10021 | -56.79087 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5dd9f588-3548-30aa-916d-8f4a77752a3e | -17.09959 | -56.79626 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| efee817a-5517-3c25-a369-73a865481608 | -17.09542 | -56.79023 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ba31c035-bf48-3cbc-9686-8b61273b3f0c | -17.09481 | -56.79561 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8556d685-2246-3fa5-a7ab-6a52c4c18395 | -17.09476 | -56.79486 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8e567603-89c3-3702-a506-1e2efc82787a | -17.09064 | -56.78959 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f27b2eda-9616-3cad-b84a-d729aa150ae2 | -17.09063 | -56.78886 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 61dc7447-e996-3ffa-8d30-718d804019b1 | -17.09002 | -56.79498 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 272d61a1-1e9d-309d-975b-a1458ea5ac5e | -17.08998 | -56.79424 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| fc053378-b41b-30d5-8704-aa20911088ab | -17.08769 | -56.77275 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c5e69b40-6b58-38e6-8963-85ec236186a0 | -17.08716 | -56.77746 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 58a596d8-f0e4-3907-9cb5-9c93736e46c3 | -17.0865 | -56.78284 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 859c9881-09ea-360d-b29b-d3ceea52c329 | -17.08647 | -56.78355 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 1551096d-f2f6-382c-a5a1-41109ef5ef2c | -17.08585 | -56.78895 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 171c148b-34c9-3e9f-8af9-dbbb8f801905 | -17.08585 | -56.78823 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2043da46-a289-3a66-ab2c-5e7a4076211b | -17.08524 | -56.79433 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9b2588ca-acc7-38c8-812e-97722f8e0f55 | -17.0852 | -56.7936 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5ad1ba3f-8ce9-30fd-8856-0b9379cabddb | -17.08302 | -56.77147 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 40ffaca6-9008-3695-b29a-8121dbd5b5fe | -17.0829 | -56.77212 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 52bbc01d-157e-3903-a273-04ae7f789ecc | -17.08237 | -56.77684 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7adaca01-d5ca-3d25-ae70-d4d91e894f96 | -17.08229 | -56.77751 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f57f5a2e-8d7a-36cd-b949-3a5226043eb0 | -17.08172 | -56.78222 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3b7a347b-bf96-3436-967a-b89ef596e793 | -17.08168 | -56.78291 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 798b223f-4706-35ea-9f20-1fd6d9675746 | -17.08107 | -56.78829 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 97a59a42-7828-3514-9d6b-fe4d16162c6e | -17.08107 | -56.78759 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 117455ea-9ceb-3401-8d48-b27940d4f7f4 | -17.08046 | -56.79367 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3b810800-6a74-376c-9dc6-9c7f8d1d7d10 | -17.08042 | -56.79295 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 83aa25dc-b247-3567-8a05-77ddb46fcaae | -17.07985 | -56.79904 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0a528af1-ce92-30e5-b565-47b49dd794e3 | -17.07977 | -56.79831 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5ffbc758-466e-31a6-9336-8f166cc6e1a3 | -17.07811 | -56.77149 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cef52fcd-23ac-3014-b335-3e080a1b783c | -17.07758 | -56.7762 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| df5d64a6-ceff-3fd1-945d-86afbf7fccd9 | -17.0775 | -56.77686 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 49fb0da7-d35d-3372-8eb3-2688de587cfa | -17.07507 | -56.79839 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 0956228b-5d52-39b4-8ae8-2748fcd5f7b7 | -17.07499 | -56.79767 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a20b668b-5434-3111-aa61-a893490a850f | -17.06479 | -56.80175 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2a40f179-6353-3130-836c-b79909634785 | -9.93821 | -57.85289 | 2024-10-05 05:31:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffaa9f2e-355b-3fcf-9401-c12177a4d05c | -9.9377 | -57.85646 | 2024-10-05 05:31:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cd780b3-8981-3d32-92a8-e1a7ea631360 | -9.91635 | -57.47684 | 2024-10-05 05:31:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8272d5f-6f90-3e81-8f8e-57a9b60d90ac | -9.72589 | -56.9802 | 2024-10-05 05:31:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc5784bf-35aa-342d-9168-efc9d0f7df61 | -9.72533 | -56.9842 | 2024-10-05 05:31:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a150331-e709-3e8a-85c7-9418e07df005 | -9.64802 | -57.19827 | 2024-10-05 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 415664df-00a6-3c4e-917b-c7a42183978a | -9.64748 | -57.20218 | 2024-10-05 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce791bd9-7895-3dc3-8bdb-3f696361e697 | -9.6433 | -57.20154 | 2024-10-05 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbe0af75-b7db-350d-94e1-8b089ae1b464 | -9.52078 | -57.99107 | 2024-10-05 05:31:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2334b563-90c9-35c7-a244-c87b64c41704 | -10.13094 | -56.75986 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README144.md)
