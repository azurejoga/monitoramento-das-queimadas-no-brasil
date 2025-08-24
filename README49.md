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
| 99c75ed5-2be1-37ea-9f73-cc041aae8018 | -15.53215 | -54.75459 | 2025-08-24 04:36:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c1000fb-15a6-3c6b-b3e2-5a9bf661e51c | -14.46101 | -48.44888 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a894a46d-2c43-3b50-a680-d5d5e5cfcbfd | -14.28745 | -60.37236 | 2025-08-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e86ffcf0-7dcd-3e86-89be-cb6c5115b4c9 | -14.80825 | -47.92347 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 195e33e2-0881-324b-87b5-61c07ab49a12 | -14.84766 | -48.31961 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b3e42cb-4bf3-35b6-b71d-86b3de98c14a | -14.33233 | -58.59576 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7c2cf51-f2c4-3ae8-8e8f-13f89887a5f1 | -19.68924 | -48.98466 | 2025-08-24 04:36:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6567684d-39d7-3937-b90f-9d6d6cab0cf7 | -14.47336 | -53.08801 | 2025-08-24 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b95db52-48b5-3f1c-af4f-cfcf5e79f673 | -18.66612 | -47.36623 | 2025-08-24 04:36:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e149624-fe2a-36cb-af35-ab6a4d413b55 | -15.09872 | -48.65768 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85fe708b-3407-3d59-b277-ad8a6eecad21 | -15.06967 | -48.69085 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fb720c9-ef49-3927-8565-b910a18dbdf3 | -20.36297 | -46.73227 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 658691b5-2f9d-3361-80fb-c55519f9ba30 | -15.6496 | -52.71494 | 2025-08-24 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56502f3c-6e4b-3969-a99b-d235801b64e4 | -17.59155 | -46.09818 | 2025-08-24 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81c1e2f2-dc3f-3373-925e-a5d912371707 | -16.48831 | -52.56178 | 2025-08-24 04:36:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e26a2e73-bb8b-3782-987f-cc95f858e553 | -14.5209 | -52.04627 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abda5709-c034-3d71-b6ab-8e94067a497e | -18.40138 | -46.84264 | 2025-08-24 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc1d9d24-b436-3de7-85a8-e5ebe151c006 | -14.50858 | -53.09859 | 2025-08-24 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f80b29d-52c7-3fce-9dbe-bdca9824eb02 | -15.23108 | -48.21224 | 2025-08-24 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1a8396e-28b5-3ab1-8c02-b445d6e4615c | -18.19544 | -46.68089 | 2025-08-24 04:36:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e2cec70-5602-3f4e-bd8f-3079b9948fc0 | -19.69268 | -48.98521 | 2025-08-24 04:36:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a83f0e48-a665-3129-9676-b3c57cf37e9f | -16.79161 | -51.35151 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 2f61026a-e1a8-30b7-af6e-e7d9911e546a | -18.92946 | -45.77755 | 2025-08-24 04:36:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a10d5bbe-9dac-3239-91aa-0b740a0e2f9e | -16.73122 | -49.07364 | 2025-08-24 04:36:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe74a688-7c66-302a-b40f-62cf761c4634 | -17.014 | -47.9548 | 2025-08-24 04:36:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 563ac393-1f22-3013-9d59-f9588618bcf2 | -14.62413 | -48.92321 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ef6aa4b-b6b8-3a0b-8e0f-95544e5a08a0 | -17.01301 | -47.95203 | 2025-08-24 04:36:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ce75d02-4eb0-3936-94bc-01aceeb9f301 | -14.52485 | -51.93615 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb6161b9-e231-3658-9d0f-f65bd07f8855 | -14.33054 | -58.59623 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b00d72f9-a621-3d49-b520-f91053d96c08 | -19.83577 | -47.53922 | 2025-08-24 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 48f218ae-1412-3852-af14-997a75235e20 | -17.59608 | -46.09386 | 2025-08-24 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfe2a8d4-3611-3675-accb-d0045546eb9a | -15.06811 | -48.52908 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d074772-6818-3026-b2c2-e8fd8a7cc775 | -14.34464 | -52.99786 | 2025-08-24 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96db0496-3259-32ca-940b-d1a0d6ca2571 | -15.29868 | -56.16192 | 2025-08-24 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e32b7d6b-1e6d-307a-8bc1-6fde9b3f2dc7 | -15.08983 | -48.69408 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7bcc03bd-3a7e-32a9-bf2a-e61938c0580b | -15.06585 | -48.52114 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87838198-327d-39a8-9409-9ce4288fd269 | -14.51746 | -52.04568 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b30f27bb-d563-3d0f-a2ee-3fafb6f00bab | -14.52142 | -51.93556 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d2c48d0-4245-36f4-8dc4-e2a0e1409f1f | -14.79806 | -55.9917 | 2025-08-24 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c387b6b-ea02-37f1-9432-081dbb58d459 | -14.39892 | -49.76896 | 2025-08-24 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e716676-60c9-326b-8fd8-d856e8c28949 | -15.05181 | -48.52268 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0992c8c6-c13f-36c7-8a7f-8f1394bedec1 | -15.13003 | -48.63265 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0485a70-3885-3b6b-bcf2-d2e3f8393543 | -14.75297 | -45.37825 | 2025-08-24 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99bc867e-7b85-3877-a521-487c33c06793 | -12.58863 | -60.35857 | 2025-08-24 04:36:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d1d7147c-0f5f-3fc6-8c8e-302f966edaa1 | -16.48967 | -46.75533 | 2025-08-24 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcc6ab73-a46a-3061-8f46-6e0f01a0d1b3 | -20.3578 | -46.74193 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59a5388d-2ad1-3d0e-8065-f8d5b6e1aa85 | -14.29671 | -60.38517 | 2025-08-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb4e2ce1-68f6-3f32-979c-a5dd5063fdbc | -14.79171 | -47.94052 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e45294cd-027f-3c17-ac89-8ce204a2eda5 | -14.49494 | -53.09175 | 2025-08-24 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e0ed74d-fe1c-3943-995d-3425ca90058f | -17.0165 | -47.95256 | 2025-08-24 04:36:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 845938cc-768a-3619-9c6c-1316b8d34b9d | -15.29596 | -56.15279 | 2025-08-24 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 8b95da46-698d-3f65-8e3e-061e620283a8 | -14.28119 | -48.029 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 982b04be-830c-317f-9f0d-27924a9b9dcf | -15.52531 | -54.74804 | 2025-08-24 04:36:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c0d7521-70cf-3dfc-b58c-aaeb58fc6ba6 | -15.10881 | -48.65926 | 2025-08-24 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0eae26a-b371-3157-99c6-2164a7628703 | -14.81342 | -47.93591 | 2025-08-24 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 97d71012-214b-3b19-ac61-43a4cc7b2788 | -14.30432 | -58.49614 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df0984b5-769b-3f5f-bf4b-2d863cc5c30f | -14.51873 | -52.03795 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 79854841-1fc8-3780-b2ed-83921cb32abf | -17.59542 | -46.09877 | 2025-08-24 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c7f1d81-d4dd-36e7-957f-b6381b6a2a26 | -18.02208 | -51.08162 | 2025-08-24 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf51e654-b82c-327a-adec-3842b7d1e9ab | -20.35974 | -46.75731 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f89c523-3cae-3b5e-bc42-7fa3e2a829f3 | -16.49396 | -46.75146 | 2025-08-24 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca5e0a54-c2f2-3da8-bd4e-ff42a2d92e46 | -20.08244 | -46.10949 | 2025-08-24 04:36:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 65f22132-bae3-34aa-862b-fa2b545d29b5 | -15.05517 | -48.52326 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04346c6e-5712-3724-b254-2096f04c1a01 | -14.28572 | -48.02207 | 2025-08-24 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 758afaf9-aa3b-3c5b-9576-86b76607f8bb | -14.37971 | -49.16753 | 2025-08-24 04:36:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00b9c9cb-149b-3ccf-b16e-19139a33aa56 | -14.77167 | -55.41633 | 2025-08-24 04:36:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68867e35-4c33-3962-96d2-cd45c9313fb3 | -14.78707 | -55.95582 | 2025-08-24 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9bbbac7-3864-3929-a25c-e7b63932ee28 | -15.32143 | -56.15765 | 2025-08-24 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 997b2d90-70a8-327d-a5b5-1188212a06f8 | -16.79377 | -51.35939 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18f90e0f-7182-3ebf-b210-44298d7e8ff5 | -16.4207 | -49.14584 | 2025-08-24 04:36:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ee8b85e-77a7-35d8-b41a-de9caf0374bf | -12.59254 | -60.36278 | 2025-08-24 04:36:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bc6f5585-a99d-3332-8b00-bf9e40473270 | -16.79826 | -51.3527 | 2025-08-24 04:36:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5313cdc2-af0d-3596-8518-2a4fde57f14d | -20.36877 | -46.74818 | 2025-08-24 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c4a2017-4d76-3522-8a02-e251d0222c6e | -14.66017 | -56.57199 | 2025-08-24 04:36:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e30a075c-5ef4-3a3d-900e-43f24c971b9c | -15.06923 | -48.52164 | 2025-08-24 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af37ea54-2793-380d-95d3-d2ba31019014 | -14.39948 | -49.76542 | 2025-08-24 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7404f72-2cbf-3d48-86f7-594a68ea4882 | -15.97255 | -48.33771 | 2025-08-24 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf12251d-6b5d-3d53-966f-6d677e59a1de | -20.59397 | -45.81947 | 2025-08-24 04:36:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d7b7643-f13d-39b2-b6df-43f0f1ae2b5e | -14.34065 | -58.59833 | 2025-08-24 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0371543-b944-3950-9fcd-1d82142e8fca | -23.62974 | -46.02726 | 2025-08-24 04:38:00 | NOAA-21 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 9b91e6ea-2b88-371b-869e-3337b110a099 | -21.33183 | -43.5695 | 2025-08-24 04:38:00 | NOAA-21 | OLIVEIRA FORTES | MINAS GERAIS | Brasil | 3145703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fcd13792-41ba-3774-bf28-b4e7e49236c6 | -22.05049 | -53.83484 | 2025-08-24 04:38:00 | NOAA-21 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a27699b4-0c7d-380f-a63d-6fbe6d90fb29 | -24.62576 | -50.24249 | 2025-08-24 04:38:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ba5ff16-7cd3-387f-8f5d-ddd15ac255a3 | -23.30877 | -45.53444 | 2025-08-24 04:38:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| c9cd8476-31d2-3c7c-bab7-b28cfe14fe91 | -20.35871 | -51.68622 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a302d92f-6590-376d-9e49-d53e7995ae78 | -20.59854 | -51.61102 | 2025-08-24 04:38:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2de50070-42cc-3ab3-8f5d-d8eca217e622 | -23.29403 | -47.6362 | 2025-08-24 04:38:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 532ccec2-2baf-3e68-9fd9-a7806e622071 | -23.35532 | -45.80186 | 2025-08-24 04:38:00 | NOAA-21 | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6d8f47e4-2e75-3e5e-a0ac-955acbca820c | -21.26197 | -50.29767 | 2025-08-24 04:38:00 | NOAA-21 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b2c68c6-7421-3a2e-9b1f-0587a51aca9d | -25.14857 | -49.53754 | 2025-08-24 04:38:00 | NOAA-21 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c682fcbc-82a6-3c3a-bbf2-2401c4774163 | -21.38452 | -43.88214 | 2025-08-24 04:38:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 11171377-5563-344e-addd-4e7b167f387d | -20.35423 | -51.69298 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 888c204b-ed38-3bab-8693-733263ef1c11 | -23.32512 | -47.84543 | 2025-08-24 04:38:00 | NOAA-21 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 81256a84-aea6-312c-b944-90b463984e9d | -20.35598 | -51.68195 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a2c1b946-fd56-3977-9fa3-7b150f4de95b | -23.20426 | -46.431 | 2025-08-24 04:38:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 519d2ca8-5857-365f-b841-e7ace7c77646 | -21.27337 | -43.74836 | 2025-08-24 04:38:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 322d1122-2817-3b04-a561-7d2c7c23c4b9 | -23.07537 | -50.03149 | 2025-08-24 04:38:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7a6b5c56-b651-38ca-b494-22defd6a1c5b | -21.69861 | -46.90884 | 2025-08-24 04:38:00 | NOAA-21 | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 140b0a32-c2f2-38d8-98dc-207e14c26cbd | -21.95045 | -48.02873 | 2025-08-24 04:38:00 | NOAA-21 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51dd6699-bd0c-3762-a902-9f2d1d6ec32d | -23.26511 | -46.78482 | 2025-08-24 04:38:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README50.md)
