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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dc2a2ab-5a76-31f1-aac9-f9fb988e120b | -13.60274 | -47.94302 | 2025-07-16 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64c01826-4244-3575-99c7-28f0c6863273 | -19.96115 | -44.85546 | 2025-07-16 04:17:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 10129242-9eb0-3f62-a4a1-c7a7474ce509 | -18.65289 | -55.71662 | 2025-07-16 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b3477991-620c-3d50-afdd-7bb269826906 | -20.03092 | -47.38309 | 2025-07-16 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79228a42-939f-3c5b-8ce6-391a10d873f0 | -18.65671 | -55.72478 | 2025-07-16 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8635b366-80c2-3488-9ed9-0d59da87b077 | -16.14714 | -46.61695 | 2025-07-16 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7eb7fa7-3517-3f79-9df6-9580706c0c9c | -20.08339 | -47.64281 | 2025-07-16 04:17:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6ee772b6-4591-35bd-bae5-9f4aa1680a1a | -20.02969 | -47.39062 | 2025-07-16 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c4927ae-cdce-3384-be46-e605b37e19e5 | -18.65217 | -55.72007 | 2025-07-16 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| de9cbb27-80d9-3b2c-8d96-e95c88d5a8a8 | -25.06065 | -50.04752 | 2025-07-16 04:17:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84852678-6f03-3d50-9a58-3ff0ef582157 | -15.2392 | -49.6613 | 2025-07-16 04:17:00 | NOAA-20 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6fc11fc-5e39-3fd7-bafb-f6ff9e704929 | -18.65553 | -55.72253 | 2025-07-16 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0e30f5e3-2299-32a7-9711-8f68ca4ef588 | -20.35744 | -46.59967 | 2025-07-16 04:17:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36f97be7-370a-3e53-ae70-767a43fa0bfa | -20.35229 | -46.54707 | 2025-07-16 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85c1418f-c89e-30e6-985d-04778430e6ab | -20.07942 | -47.64594 | 2025-07-16 04:17:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c57990e-7749-3f15-b642-c82201dadbeb | -13.91288 | -49.52608 | 2025-07-16 04:17:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a60ca65-b35e-3e23-9625-f1199d0ed182 | -16.81015 | -49.2645 | 2025-07-16 04:17:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72a0b27e-84f1-3f67-9574-4ffa235b257c | -16.25953 | -43.80843 | 2025-07-16 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.0 |
| c3b56685-9c7e-3958-867b-62b373e58870 | -25.10087 | -50.82853 | 2025-07-16 04:17:00 | NOAA-20 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b449e863-1dcf-3b15-933f-8d42c4f6b0da | -20.03425 | -47.38373 | 2025-07-16 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4364cba3-4a77-3029-88ef-0f55f46b94bf | -14.59347 | -48.11752 | 2025-07-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b06b685-a8c3-36cb-95c4-cca7e2f43500 | -18.40989 | -44.18753 | 2025-07-16 04:17:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ba41c6f-8c75-39d6-8361-cd7a68329e17 | -22.55645 | -54.9436 | 2025-07-16 04:17:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 161336bd-dd8b-3334-a50d-1c1f977810fb | -21.95753 | -57.59114 | 2025-07-16 04:17:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52780c7f-bf29-31a0-ad85-68e23cf0faa5 | -14.6099 | -48.25876 | 2025-07-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5039c0a5-af7f-38c2-8831-5eb150558060 | -14.91795 | -46.95999 | 2025-07-16 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f99a8d1a-79a5-3ab3-bac9-2f4000c25bb8 | -16.26316 | -46.9102 | 2025-07-16 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4ceed44-95a7-3c75-96e6-6988b70411e1 | -17.83616 | -44.35276 | 2025-07-16 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e4ced11-0af6-3180-89ce-3f5f3f2020ed | -21.26009 | -45.01451 | 2025-07-16 04:17:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 47b180a2-9bc3-31d1-be24-e14bd12df02a | -21.16479 | -43.75857 | 2025-07-16 04:17:00 | NOAA-20 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 06b158a7-6f16-3110-a129-36d6597b63d9 | -13.16702 | -50.77165 | 2025-07-16 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1d4ce21-cbd2-3b7c-99f7-7e001727c714 | -20.07607 | -47.64536 | 2025-07-16 04:17:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 18d2b53e-1976-37b6-b0ce-fcd43f761858 | -18.71331 | -47.39035 | 2025-07-16 04:17:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8457f0b5-4613-3a6a-bfc6-03aba34b5bb1 | -17.90825 | -54.12309 | 2025-07-16 04:17:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cf54587-db3f-3f50-b01f-a21d533b999b | -20.03363 | -47.3875 | 2025-07-16 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bb6b4006-fc97-3d17-9675-b5b2f6013692 | -14.59995 | -48.66841 | 2025-07-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| efc99074-9043-32fe-ab1f-ed86f0864c75 | -20.25143 | -44.78716 | 2025-07-16 04:17:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c84ba8b6-6d3a-38f6-a848-1a383b9663c2 | -20.31515 | -50.46414 | 2025-07-16 04:17:00 | NOAA-20 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e9944424-c1a5-3b40-84c8-95830d1c413a | -20.34956 | -46.54282 | 2025-07-16 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be6ec469-c8d5-338b-888c-7868e5c36bed | -20.96163 | -43.96995 | 2025-07-16 04:17:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ffa6b345-738c-390f-9407-05edfef32203 | -20.02179 | -47.39693 | 2025-07-16 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2a60c00-23e1-3e49-994e-610aeeff2653 | -20.36249 | -46.58927 | 2025-07-16 04:17:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 649e4f14-0fc9-3dcb-bc6c-191831607e27 | -19.78543 | -47.46903 | 2025-07-16 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49c66955-7a36-39d3-931c-67c78b943f02 | -18.74073 | -39.9227 | 2025-07-16 04:17:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d7b3b44a-d590-3222-bad2-1e44e30f4909 | -20.38549 | -44.34767 | 2025-07-16 04:17:00 | NOAA-20 | CRUCILÂNDIA | MINAS GERAIS | Brasil | 3120607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 051d35c1-1cc4-3024-b5b8-cafb9a226ed6 | -20.02574 | -47.39378 | 2025-07-16 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03670e2e-b00a-3119-a9f7-3d7d8a3e4e7d | -20.08004 | -47.64222 | 2025-07-16 04:17:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 34965ab0-59a8-388f-b04b-b1c27b6e8ae3 | -24.35637 | -50.82044 | 2025-07-16 04:17:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4e68e5ba-a0ba-3a36-b5ed-556b95caf7d0 | -25.33739 | -52.53216 | 2025-07-16 04:17:00 | NOAA-20 | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| eca015c9-e294-3cbd-a873-83a109d3496f | -18.65627 | -55.71909 | 2025-07-16 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 09c4e72f-a8ba-35b0-9a7b-87730045d415 | -20.03031 | -47.38685 | 2025-07-16 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb92e9c6-b5ef-32d4-bf21-3d7a32bb1cb3 | -18.59571 | -52.39946 | 2025-07-16 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02613a9e-1c61-3489-b5ce-e87afef10b3c | -14.59494 | -48.10893 | 2025-07-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c0a2847-0604-310f-8e11-764dc2acbca6 | -20.38893 | -44.34822 | 2025-07-16 04:17:00 | NOAA-20 | CRUCILÂNDIA | MINAS GERAIS | Brasil | 3120607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c3ed5765-f451-3635-8657-fae59df52c70 | -27.50426 | -51.35284 | 2025-07-16 04:19:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d71dc0e3-4f3e-353c-bfe5-91dcbf32240c | -21.96136 | -56.07478 | 2025-07-16 04:19:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ac3fac7-1cf2-3146-919f-6dc279720110 | -23.12744 | -50.02057 | 2025-07-16 04:19:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| f80f1cfd-1be5-3949-9b98-eb4b43d71b8b | -22.2559 | -50.03679 | 2025-07-16 04:19:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0306ffc6-7c39-3e97-ae55-655221f46aa8 | -27.21275 | -50.66138 | 2025-07-16 04:19:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 09cce751-e1b1-395e-ab07-cdfccfc81f6b | -22.39642 | -49.79435 | 2025-07-16 04:19:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 15957924-e0a4-3104-b414-faea6720a00d | -21.04264 | -55.98711 | 2025-07-16 04:19:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc1ce642-1f7f-3af6-8e97-23666b7dc13f | -23.62059 | -47.12209 | 2025-07-16 04:19:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 83235427-8b4d-3388-968e-92fea6ef6358 | -21.94472 | -46.04222 | 2025-07-16 04:19:00 | NOAA-20 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 81a5d6ec-e4e2-3ad7-a67d-c5967dddc0b6 | -22.76627 | -46.37106 | 2025-07-16 04:19:00 | NOAA-20 | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ddf5e5fa-5034-35f1-9bd6-94582d1e2170 | -23.12817 | -50.01635 | 2025-07-16 04:19:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 58019e33-96ab-3c6b-a245-a42004d26c3b | -20.62085 | -54.83769 | 2025-07-16 04:19:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1d54892-88ed-3751-b1f9-a39860544015 | -21.25875 | -50.29679 | 2025-07-16 04:19:00 | NOAA-20 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| accc6ebb-074b-3bad-949c-3da57bc112fc | -22.82827 | -42.0624 | 2025-07-16 04:19:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 70e7a293-2694-3367-8454-fc851a343257 | -23.44395 | -47.25219 | 2025-07-16 04:19:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6983b420-fc7d-3171-a9ae-cf37ac9c0f32 | -23.13095 | -50.02127 | 2025-07-16 04:19:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3fc01ac8-52ce-325d-abc4-a8fa9fafa625 | -21.04196 | -55.99031 | 2025-07-16 04:19:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 406efd07-b3da-37d3-871e-58eb7531562c | -28.75867 | -55.53277 | 2025-07-16 04:19:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 4d151663-e6fa-3ec0-81ab-eef616a4dd92 | -28.56688 | -50.46601 | 2025-07-16 04:19:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cb4b88ba-58b8-37d1-93ac-9d76206c6c89 | -28.75677 | -55.5419 | 2025-07-16 04:19:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 5cb90c7b-590a-3352-995e-9d97eec4312a | -22.83223 | -42.06298 | 2025-07-16 04:19:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4350440b-3bee-38c9-ba96-b3ab3dfe50a9 | -21.34762 | -48.63042 | 2025-07-16 04:19:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 511fe23c-01a2-3eea-bfa8-9cdd02856edf | -28.75583 | -55.54647 | 2025-07-16 04:19:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| d8e5676b-d404-3484-932e-122a616fae54 | -22.82971 | -42.06081 | 2025-07-16 04:19:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2a6efb8a-d9d7-3b56-bff8-87ab2573a03c | -21.79309 | -52.75954 | 2025-07-16 04:19:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ffa3f928-14cb-30e6-8878-412e760dcdfb | -28.76439 | -55.53653 | 2025-07-16 04:19:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.6 |
| a559dfef-7340-383e-a550-194b7ea51995 | -28.76342 | -55.5411 | 2025-07-16 04:19:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.9 |
| 706c8aed-bdc2-37e3-8ac5-962a5a55b8cf | -28.76623 | -55.53958 | 2025-07-16 04:19:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.4 |
| eda17ec8-640d-34b3-a7fd-49983b92ee8e | -21.34828 | -48.62653 | 2025-07-16 04:19:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4ce5a5e8-f058-3b05-95cd-e7158d96771a | -28.76767 | -55.54223 | 2025-07-16 04:19:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.9 |
| 198d0fa0-c231-3461-803c-77323a6209e0 | -27.82738 | -50.3049 | 2025-07-16 04:19:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 244203d2-e19a-35db-bd9e-45510df1f526 | -27.15482 | -51.04888 | 2025-07-16 04:19:00 | NOAA-20 | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c9bbc647-872e-3bf1-bcf6-38f372ad9839 | -21.52725 | -49.52701 | 2025-07-16 04:19:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 162aff76-4c65-3d69-a6d2-c6d70cffbef4 | -28.69655 | -55.97976 | 2025-07-16 04:19:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 6207b90e-7ad9-315b-8867-e9768bc45354 | -28.76291 | -55.53391 | 2025-07-16 04:19:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.4 |
| cf1b9bdc-a023-36b0-922b-6d7955a0331d | -28.20128 | -50.62557 | 2025-07-16 04:19:00 | NOAA-20 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8365d26f-78d1-31af-a368-d2194eee6566 | -23.44454 | -47.24844 | 2025-07-16 04:19:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b4c1d1be-69a2-3bdd-ab79-39134c6836af | -23.27196 | -47.52202 | 2025-07-16 04:19:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 745a2dd4-583f-378e-b9c7-3bdf9033d52e | -21.34488 | -48.62587 | 2025-07-16 04:19:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 568de328-4b3a-332e-b270-fa382e55007e | -22.64204 | -47.38105 | 2025-07-16 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 992c105e-059a-30a2-9d55-49ea1cddac52 | -23.21894 | -45.74514 | 2025-07-16 04:19:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4b62f646-e315-3df4-87aa-99e3a3f904ee | -28.76669 | -55.5468 | 2025-07-16 04:19:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.9 |
| f43cd4ea-9c5d-3102-a160-caa0e384ced5 | -21.96062 | -56.0783 | 2025-07-16 04:19:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e9294a0-9ea7-3cd7-a784-3372e4489366 | -22.39569 | -49.79858 | 2025-07-16 04:19:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e72e445f-d2bd-3fb2-9239-b34bfdc08d05 | -27.50502 | -51.3508 | 2025-07-16 04:19:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 29055262-7118-390f-a691-ce53fd4af8b5 | -21.10992 | -48.62265 | 2025-07-16 04:19:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README20.md)
