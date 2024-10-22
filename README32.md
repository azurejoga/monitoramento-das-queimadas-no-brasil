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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57aab1e3-428f-3d11-962d-aaa11a4adbeb | -17.67739 | -57.39796 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1e13eae5-e7bf-3c45-95a5-a96681ba24ab | -17.67704 | -57.40113 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 590f09d2-d24a-3476-b80e-ccf0e389d4b6 | -17.67356 | -57.43266 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fdd67463-06cc-30e8-937b-c2d72c025924 | -17.67321 | -57.43582 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1493e369-7742-3bd1-b3a8-7bfc73e75b7c | -17.66842 | -57.43202 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 31c68bff-a06e-372c-adbe-30bc2ebbe3ad | -17.66808 | -57.43518 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c4d2732c-c970-3215-99e6-7254319cf4c2 | -17.01996 | -57.33556 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 527dd1a2-f155-3b2e-84f3-2e8f76a3cdb6 | -17.0196 | -57.33867 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5befd96c-ba9c-30de-ae51-b2c472d33699 | -17.01952 | -57.49489 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cb80d964-3cd6-335e-b84a-11aaab84f136 | -17.01923 | -57.34179 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 14cbf3b3-30fe-39b8-b42e-dd1326974a1a | -17.01917 | -57.49793 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| aeb08653-fc04-3728-8b26-8a69d33e51b1 | -17.01785 | -57.46372 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 94309b20-c36c-34cc-a1e0-e6e493f19e10 | -17.01764 | -57.51161 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 31888062-afaf-3ae0-9ca2-3d4940828ca0 | -17.01751 | -57.46679 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6bfc4e1b-22c0-3d78-a06c-fae453319a2b | -17.01717 | -57.46986 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a0fb95c5-a4d7-31b2-867e-f02466cefca0 | -17.01658 | -57.33505 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7d2acdd8-b914-32a6-bc7e-3adc9f0295e7 | -17.01628 | -57.52376 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 0054a3b9-42b8-3e51-a50a-847bba7dac46 | -17.01624 | -57.33817 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b24db3a5-80ae-3e9c-90bf-fb546d5eb631 | -17.0159 | -57.3413 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| a463d8aa-8b35-3690-9356-7ff4945657c1 | -17.01538 | -57.50506 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 5337b63c-d6d4-39b6-87a5-df6dcb4d79ff | -17.01466 | -57.51113 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 808ea3f8-748e-3478-b8c6-75e32ca0ef2f | -17.01447 | -57.33806 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4fe68799-9dee-3c4a-88dc-3ae836e875f4 | -17.0141 | -57.4973 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3f4205cc-3589-328e-917c-df3d580fd591 | -17.0141 | -57.34117 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1f0f64a8-9b43-30bc-baa6-1228a2d10ade | -17.01393 | -57.51719 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 7e34c6e7-31b8-3c9e-bfb7-9da404cbd927 | -17.01376 | -57.50034 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 026734aa-683f-3dbe-8db9-b2c19baa9731 | -17.01321 | -57.52324 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| e9e06258-82bc-35fc-a418-b31cb41636e3 | -17.01316 | -57.3662 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 65117600-ffc8-3bfe-8e87-b3332694d666 | -17.01308 | -57.5064 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 086a2b1b-0703-3090-873d-44626cac1536 | -17.01258 | -57.51096 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d5355348-cf2b-3d8e-ae0f-9f5240265620 | -17.0119 | -57.51704 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 4aef58e2-4e19-347d-ae61-2fb305f37ad9 | -17.01122 | -57.52311 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| bb271873-9724-31fb-bf14-e85a1cf1a4d5 | -17.01031 | -57.50442 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6a1c8dd8-edc1-3c44-b30d-825d346f21b8 | -17.00959 | -57.51049 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c53b7456-07ef-3b4d-b177-281703c51c74 | -17.00887 | -57.51655 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 975b8089-89cf-3826-a139-495057f85472 | -17.00815 | -57.5226 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4fa789dc-3b20-39a6-8f9b-1967f38730ea | -17.00743 | -57.52864 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 706aaa08-463d-3ee0-a9f4-711cea33a5e4 | -17.00687 | -57.49013 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| eb00dd78-c05f-3abf-89a9-771153fee50c | -17.00651 | -57.49316 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e177be51-8c59-317d-90ea-7759f15d8dff | -17.00615 | -57.52247 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| b9d5eefe-22dd-3d11-914e-f90a073ce45b | -17.00548 | -57.52853 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 3ed720dd-9bd6-3c92-a883-117b9acf319b | -17.00464 | -57.48992 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a82e55fc-adaf-322d-bb60-8142e68152fb | -17.0043 | -57.49297 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| dd217a3e-c06b-303e-9b4e-056a8753c46f | -17.00381 | -57.51591 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8ba01715-ea6a-3bb6-bf1a-3ef6a1a873ee | -17.00308 | -57.52197 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 70c2b648-bcd7-3002-9c2a-156ea0d9ef66 | -17.00177 | -57.51575 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| dfb4952a-d120-36f1-ac38-46c74cffa568 | -17.00144 | -57.49254 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c2417168-405e-3974-867c-b7687e54cd56 | -17.00109 | -57.52182 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c835ff2b-9cba-362d-bf2b-95cb78256b6c | -16.95614 | -57.52831 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| ea1526ef-1bf4-3805-bec4-3551bab55c74 | -16.95544 | -57.53434 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| e66db1e7-9f00-36fa-9304-18a4dfecb4be | -16.95109 | -57.52766 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 5d964cca-2062-30d2-9fb3-9505333d5e52 | -16.95039 | -57.5337 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 1bd46e49-8812-3ab9-842d-6dc548e463f3 | -17.26344 | -57.30386 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 0cc05e27-ec80-3acf-b898-d2d26895fa50 | -17.26309 | -57.30702 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| fed0e561-d9df-3367-9d31-a6c19b38cd77 | -17.25934 | -57.29374 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1b10e3be-de8b-3c6f-a96d-2b0df84ff5d0 | -17.25899 | -57.2969 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5b809546-0b89-34bc-8d2c-5041863c3e0d | -17.25864 | -57.30006 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fea3fa11-a86d-35f9-9759-b4d41c80ba8c | -17.25829 | -57.30322 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 41124f53-176e-361c-8f3c-c77b316926e6 | -17.25523 | -57.28359 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6fd3c595-8243-3fd3-849a-873d179ede91 | -17.22884 | -57.27567 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 86ba4e5a-3301-34e7-a478-b8f0c6b7a970 | -17.22849 | -57.3237 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8fdb0036-3377-3052-b9a3-bfc80b412053 | -17.22811 | -57.28201 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 61f87afd-f0e7-369a-ae38-cc54f03c9e39 | -17.22774 | -57.28518 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fea5a24c-51c0-36cf-82bc-52134b60ce5a | -17.22335 | -57.32304 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5c3dd70a-ff6a-3075-8641-b2c0ca459a8c | -17.22332 | -57.27821 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 16d9db4c-abd2-3cc1-85bd-935dad5be84d | -17.22298 | -57.32619 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 23dde266-b0f6-3be9-bb63-d40aff1278c6 | -17.20675 | -57.50958 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d6e019eb-da0c-3103-9b4a-3c5967a2aa6d | -17.20639 | -57.51263 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bd84848a-fb61-3acb-9d30-aa21636ccad1 | -17.0785 | -57.4745 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 2924c1b1-8519-3ab5-a3bb-426ebae3e779 | -17.07814 | -57.47755 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| aa48003f-167d-37a9-992d-ef6898142ab2 | -17.07306 | -57.47692 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 713a4cdf-191d-31b9-bba9-3b8ea16e8b20 | -17.06798 | -57.47628 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b661ac96-55e3-3041-8144-8d3dbe56f54b | -17.06763 | -57.47934 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 13749cc1-ebce-3d4a-a7ab-85591989ee9d | -17.06255 | -57.47871 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1c2a4b81-1c55-3af8-97bd-15e9c1b4bad8 | -17.03483 | -57.45033 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 38c868d6-03e6-30a0-966f-302d322d5c67 | -17.02665 | -57.47725 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1063d262-c1de-340b-8ec4-61a81b370fdd | -17.02328 | -57.4613 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0adb2148-3f6b-3131-8d07-6cc12cb22cc5 | -17.02309 | -57.32322 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 98a4f034-0680-3453-815c-b790306753d2 | -17.02274 | -57.32634 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| d116b5d9-b0ac-3ad6-a844-e69c68362edc | -17.02225 | -57.4705 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e4c25867-be3c-390c-9628-fb66fe8728d3 | -17.02191 | -57.47356 | 2024-10-22 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ecef46ec-c4f9-32f9-a2df-8d86d5452919 | -17.02171 | -57.3357 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f9a9b418-6376-3e51-bc42-b7f078da5f21 | -18.65995 | -57.33311 | 2024-10-22 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bc7d8763-838e-3096-859d-7eadf2166b59 | -18.65471 | -57.33248 | 2024-10-22 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 66272f3a-1591-3737-8a64-4007a438af59 | -18.65436 | -57.33576 | 2024-10-22 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 197f4d64-7b86-38c9-b443-85555eaacbdd | -18.65401 | -57.33907 | 2024-10-22 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a07b12da-a2c2-3e8d-8f9b-59f5ddfb4b22 | -15.48135 | -59.37798 | 2024-10-22 05:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 183e11dc-fa2d-30a7-a631-a354cd41fbce | -15.11981 | -59.02666 | 2024-10-22 05:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18d8cae7-2d01-3d30-90db-12ec1d621f80 | -15.22915 | -59.60054 | 2024-10-22 05:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36da9cca-0338-3305-9de8-808ec98955e9 | -14.27487 | -60.12664 | 2024-10-22 05:38:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5daa780f-643b-3796-bc46-e3f9ff422064 | -14.27078 | -60.12604 | 2024-10-22 05:38:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5efe3abe-19fb-383b-8047-1009ce9bb6b2 | -16.08988 | -60.12133 | 2024-10-22 05:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63f8d152-aa90-3dd6-9eb6-a3f189602b60 | -16.08937 | -60.12528 | 2024-10-22 05:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 299799cd-19a2-3f01-bf62-7d4af6752fde | -16.08619 | -60.11677 | 2024-10-22 05:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6f1cfe82-ce92-3f2a-a077-23125a117734 | -16.08568 | -60.12074 | 2024-10-22 05:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 720c4473-9a44-32d5-bb28-d7d7e974f474 | -16.08517 | -60.12469 | 2024-10-22 05:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 630984e1-e36b-36a2-b228-d47b2c6b1a2c | -15.67021 | -59.75139 | 2024-10-22 05:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9003403a-94ba-3577-80f8-3bcb2d386481 | -15.66969 | -59.7555 | 2024-10-22 05:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3272e90c-9c32-37e4-9f03-133d40a70840 | -15.66782 | -59.75262 | 2024-10-22 05:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4115d883-d211-345b-8562-e1d5802ae4d7 | -15.23133 | -60.03657 | 2024-10-22 05:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README33.md)
