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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fb29215-7df6-3105-a025-e555223926b5 | -14.6625 | -53.11176 | 2025-07-17 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b8cfba2-dfe4-3ef1-8c7b-158aaeb9b5ab | -12.42757 | -50.0432 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ac709bd0-d06a-3662-ac85-c72ea788f11e | -12.48822 | -46.91513 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2018c58-4d71-300d-b111-11320a5ff55f | -15.93315 | -43.52505 | 2025-07-17 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63165c24-0560-339b-8d28-edb554435a6d | -12.48417 | -46.93567 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71c30af1-3e92-3535-8389-956aeefe2adc | -12.41707 | -50.04159 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9168e9da-47ae-36b3-8b54-100d325eaa43 | -13.12268 | -47.2644 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8bfc022-67e9-3e6f-b79f-af8d21d982ec | -12.7098 | -46.80202 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96e1961b-08a3-3247-9b93-4eb968eb798d | -12.41941 | -50.05003 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 106f16da-046f-3989-b14d-5b698259fd8a | -12.70871 | -46.80996 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6895b227-3b59-3b19-a962-f5a0703d7563 | -12.43165 | -50.03977 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fb4dd68-26b5-3e28-b3bd-620425b6bd2e | -13.61704 | -47.93349 | 2025-07-17 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6d56a55-5cd5-3756-8498-f37f9c1a83d3 | -12.40449 | -50.48476 | 2025-07-17 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| af563e3e-6b82-3f3d-9914-df2f37c7a2b8 | -12.41591 | -50.0495 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23eecae8-d39c-383e-adee-cfad7dcdaec4 | -12.49658 | -46.91634 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8824cc73-3a22-33da-9d4c-a0f4f7feae2d | -12.70926 | -46.80598 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3543c61e-8f75-3c4b-ac33-ce27fdf1872f | -12.71324 | -46.80894 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9779f64f-b545-3ac2-9534-ccc330cd6525 | -11.87534 | -55.44783 | 2025-07-17 04:49:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| f3e960fd-d9bd-3b5f-b2f9-3f6833a1f7f2 | -12.37804 | -50.37878 | 2025-07-17 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ad3d579c-622f-3596-b19e-97c7969b524b | -12.41765 | -50.03764 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0396419-f84d-3102-b199-eb74580c7001 | -12.40793 | -50.48529 | 2025-07-17 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c8791990-43b4-3163-95ff-52ff29833601 | -14.29953 | -52.02837 | 2025-07-17 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d6e9a40-9cdb-3d9e-886c-07a1ce54f41e | -12.41358 | -50.04105 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 203130da-ada3-36ca-851d-07ca01e63e6f | -13.6769 | -44.22412 | 2025-07-17 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea63fab5-1940-3a4a-a74f-0dd6b3dc23da | -12.42699 | -50.04715 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9a53b9fa-9004-3aac-b6fb-1fcfefb53917 | -12.42407 | -50.04266 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f3116c96-10c8-34a1-bc72-f5776127d916 | -12.48404 | -46.91451 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5d545d50-ebfe-3c4e-b400-4452876b4df7 | -12.7045 | -46.80933 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50050667-f34c-358f-9501-646414af81dc | -12.71293 | -46.81059 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd68e3d3-039f-34c4-96b7-2ea984b5ec93 | -12.71348 | -46.80661 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16dc7ca9-2dd8-3d24-8b13-939f26dd978f | -12.69606 | -46.8081 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a2ce8b2-097f-3da0-81dc-d3bc28c9f482 | -12.38149 | -50.37931 | 2025-07-17 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9577724-e2e8-3596-88e4-916b32679929 | -12.49607 | -46.92023 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0f65ac4-637d-31b1-acae-a98fe7d5dbb4 | -14.3236 | -48.65031 | 2025-07-17 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 663b0b1d-c307-3d80-8881-0864994ea658 | -14.5073 | -47.67717 | 2025-07-17 04:49:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf2be7be-31d6-3e07-a5a2-7a1fac08d7f0 | -12.50559 | -57.78654 | 2025-07-17 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7b629f4e-7753-3b83-949c-334989f7e8e8 | -12.49555 | -46.92413 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c30e87d0-b8f9-3be9-b5c6-2255f3b90715 | -12.47743 | -46.9228 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06b158e2-839b-3420-9762-d2213a58249e | -17.36111 | -44.14358 | 2025-07-17 04:49:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 49.3 |
| f0fd28aa-88a8-33dd-b32c-574c6403b778 | -12.99646 | -44.8646 | 2025-07-17 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4929651d-23c9-3934-a9a7-4f7cab3d5ccd | -17.36188 | -44.13643 | 2025-07-17 04:49:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 8ac345e3-c9ff-37f4-98bc-399025821a0a | -12.41137 | -50.46238 | 2025-07-17 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63b711a2-fa05-350d-8927-1f3e31df89c1 | -13.20636 | -56.63506 | 2025-07-17 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 922dc7a0-645f-38cd-9332-8921d12edfbd | -14.51589 | -47.67531 | 2025-07-17 04:49:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92ac4e18-1771-3063-b665-597d78b7664c | -12.42465 | -50.03872 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da4a4160-eea7-397d-a3a3-5a333c7fdc28 | -12.40736 | -50.46566 | 2025-07-17 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82365a46-a58f-3299-9f86-66663237b100 | -17.36686 | -44.14088 | 2025-07-17 04:49:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 008ed728-968a-351f-959a-ef747cd8e72c | -11.88061 | -58.71334 | 2025-07-17 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09534005-adec-3638-9939-6603e3ab846b | -12.37746 | -50.38263 | 2025-07-17 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6b9d42d2-828d-3227-ae56-4ccd8954824b | -12.48515 | -46.93848 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8726fd48-7179-3cd7-af70-04e5befdfac0 | -13.12729 | -47.26138 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9aee923c-6d3d-31ea-b329-6f9fd3362ace | -12.43048 | -50.04769 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87445638-00f6-3880-b957-029634e9659f | -16.26964 | -48.65981 | 2025-07-17 04:49:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76f2d47b-67ec-356d-b19d-6419f1b7926c | -12.42057 | -50.04213 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 879c5e03-3e39-3283-a00c-9113bd0a5a09 | -12.42815 | -50.03924 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bc4dd14-25d8-3b3a-9adf-9c92e16a4895 | -12.42115 | -50.03818 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 455b8941-8451-3373-ae4c-94848b1d8324 | -15.34441 | -49.42594 | 2025-07-17 04:49:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64914ceb-d758-32fe-8f80-b96e97c2fc8e | -14.52453 | -47.6731 | 2025-07-17 04:49:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a586c55b-e115-37d2-89fd-426c872fb16e | -13.68039 | -44.22074 | 2025-07-17 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e865d910-7d35-3856-bf4e-8d738aa5445e | -17.36149 | -44.14 | 2025-07-17 04:49:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 73d3c8f5-24d7-38a7-986a-e92600e56c97 | -17.15959 | -46.11591 | 2025-07-17 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4853e18d-65e0-35fb-8603-d6fc63edcac6 | -12.41999 | -50.04608 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01956af9-3e46-38ad-a672-32c13502a7e4 | -13.00481 | -44.87664 | 2025-07-17 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a46f169a-884b-332c-8d10-722c3f5f7071 | -12.4924 | -46.91573 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb0c0643-0c71-3a15-aaac-ec29fb4123e1 | -13.0209 | -45.05894 | 2025-07-17 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d35d258-2165-3ebf-9882-dc273aa701d3 | -14.4712 | -46.97215 | 2025-07-17 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cf6bd20-403f-361b-a3ee-82db661cd2a1 | -13.00063 | -44.87065 | 2025-07-17 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7feae221-5bb7-3133-933f-50a1e6da5291 | -12.5028 | -57.77869 | 2025-07-17 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cdd412de-e39b-3e56-8a8f-44d4711360cc | -12.38091 | -50.38316 | 2025-07-17 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1126368-a55c-3691-802c-b54ede2b2b0f | -16.52463 | -52.49537 | 2025-07-17 04:49:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1f2726e-bc49-37a8-a0a1-bb3b2640f1d1 | -12.50218 | -57.78225 | 2025-07-17 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f5b8435-502c-30ac-88e2-680ce547f67b | -12.70028 | -46.80871 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd2fd09e-f6bf-3ddf-9499-3926674e716d | -13.00549 | -44.87114 | 2025-07-17 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36e4c227-e3ef-3ab6-a71c-c25460888313 | -14.51644 | -47.67122 | 2025-07-17 04:49:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16d9c24d-36b9-3937-9765-75565aa18440 | -13.68004 | -44.22371 | 2025-07-17 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22bb39b6-82c1-3b08-a990-c641a2ffcac0 | -11.52205 | -54.68468 | 2025-07-17 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a768ed63-4a64-3015-9676-edd5900c2731 | -14.50782 | -47.67329 | 2025-07-17 04:49:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b7475ab-c82a-3382-ae2a-0202a86fc32b | -12.37459 | -50.37825 | 2025-07-17 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 41d18f6e-b602-3c73-b661-a113be6ec273 | -13.00132 | -44.86511 | 2025-07-17 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef5321f8-b468-360a-a78f-b8939f7922c7 | -16.80508 | -57.09024 | 2025-07-17 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 8876e1b5-f664-36f2-b065-2ab6acc8aaa0 | -12.48686 | -46.91625 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c17ebdec-0ec7-3467-be83-0fafe3949689 | -12.47935 | -46.91779 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a7f6dfc-ed54-3df7-91d1-0ffd9f88e08f | -12.42523 | -50.03476 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f72e8cd-0fbe-35f7-849e-764e0d4deaf8 | -16.52129 | -50.82834 | 2025-07-17 04:49:00 | NOAA-21 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d4ae069-9fb2-30d0-ace3-4fcacb35f47a | -12.50621 | -57.783 | 2025-07-17 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8651eb1a-44f1-3195-9a46-9d74872ea55f | -5.6754 | -43.7147 | 2025-07-17 04:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| c10bc8cc-cc46-3913-9d79-94324b0689e0 | -20.0013 | -49.0551 | 2025-07-17 04:50:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 53.4 |
| d161fd56-6e6b-3944-86c8-030af22f6f1f | -6.7194 | -44.3231 | 2025-07-17 04:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c883bfaa-00d7-3c84-a37b-af925ab3e44a | -3.3958 | -47.4785 | 2025-07-17 04:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 59a9b9a1-8bc6-3319-b906-66bf3fbaabe4 | -17.3628 | -44.1399 | 2025-07-17 04:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 97.3 |
| d72c7390-170e-3bb9-9086-bb16902f9adc | -5.6565 | -43.7393 | 2025-07-17 04:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a46d83cf-0b83-3164-ab32-59e5246d3841 | -5.6567 | -43.7161 | 2025-07-17 04:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 231.8 |
| cb31f1fc-22b7-375a-a69b-abe7e43a831b | -20.0216 | -49.0507 | 2025-07-17 04:50:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 05cba19c-25bf-37d4-8847-b3fe5f65ef5b | -18.22772 | -54.55064 | 2025-07-17 04:51:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02a0ce2d-b144-3e8f-94b1-d70b2993f683 | -22.39616 | -49.78804 | 2025-07-17 04:51:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 69be83df-54ed-34f5-8012-a306a586a682 | -23.08931 | -49.73457 | 2025-07-17 04:51:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e5d3a712-f853-3a51-8a32-8768503102fe | -20.01195 | -49.04868 | 2025-07-17 04:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b64f2969-108a-32ca-9784-5fd86219fc83 | -19.46291 | -55.44283 | 2025-07-17 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 38d04667-558c-3367-bccc-9816a3a8abf9 | -19.47488 | -49.29214 | 2025-07-17 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 445a11dd-74ae-3491-be07-9f8796957898 | -20.01148 | -49.05242 | 2025-07-17 04:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |


[Clique aqui para ver as próximas entradas](README25.md)
