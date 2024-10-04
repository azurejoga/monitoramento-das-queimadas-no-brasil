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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01dc7145-168b-3e26-828f-8cb43a14ec75 | -15.70478 | -57.42374 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 055fcaf3-1b23-3af5-9da4-cfe87824d1c0 | -15.70371 | -57.42933 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24dbceb4-bf01-3bd7-a023-1161d9705276 | -15.69757 | -57.41059 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28b7385c-4b15-3a3a-9fa8-85ff63cdcb45 | -15.6907 | -57.42107 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bec50dc-fb22-3348-8e59-27bfcc56324d | -15.68569 | -57.44712 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d6f3fa6-d4a0-3d98-a1db-7a024c500a37 | -15.65097 | -57.39413 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1aec7b3-1c84-3c53-90ba-e12fcc6b20d0 | -15.64961 | -57.40729 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 319c50de-6b56-3ac0-9a82-d1e499821868 | -15.64703 | -57.39558 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bccd71b-0dcd-3c4f-af92-76c5c44b2476 | -15.64595 | -57.4011 | 2024-10-04 04:34:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 197812e4-110a-3c60-8fb0-6b550f0441f5 | -17.20124 | -57.35925 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f2e3cf9a-e526-3747-98c5-11cf8aa3f13c | -17.19671 | -57.3583 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a3a012ec-e404-3968-93b5-94c68877f683 | -17.19218 | -57.35734 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 3316df6b-70e0-3d41-90d9-ebbb2713a5b2 | -17.19125 | -57.36211 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 7ccad368-5343-368f-a1d1-662e6f1dcb48 | -17.18938 | -57.37166 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fe64bb20-661d-33e4-90b9-36e77a27ddac | -17.18765 | -57.35638 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 13ba3532-51cb-3cd3-beac-4df93db7b865 | -17.18672 | -57.36115 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b0e27215-a18f-3352-83c2-3f00a789f4cc | -17.18485 | -57.3707 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3f0608af-1811-326d-841b-7e0dd5a84515 | -17.18312 | -57.35543 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 00d913f4-8558-32fe-bb2e-811467b31a06 | -17.18219 | -57.3602 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 52a4ea8a-98f7-3f33-8c69-38f40839fb56 | -16.92254 | -57.70063 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 836f1edd-f5e9-3415-b46b-af63e3966bc1 | -16.92155 | -57.7057 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3eb550b5-b708-368e-a520-4c39d4de845d | -16.91788 | -57.69964 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f8e56847-ceb5-3dec-8ae9-d3beb56b1ccf | -16.89068 | -57.68202 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1735c2f0-7931-3c56-984b-f96c5c37b48e | -16.88832 | -57.67753 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b59bff76-14f2-36f7-9c04-df9f9f570c5a | -16.87763 | -57.70692 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ac93160f-96fc-3b57-93f6-5cd741644b92 | -16.87297 | -57.70592 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 78b74e3d-d603-3055-8508-a3a5db811d4b | -16.80963 | -57.82471 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d346438a-a625-3494-ae55-34b4b9f20882 | -16.80493 | -57.8237 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 90bd4d70-6036-3607-a487-a0f5b3592044 | -16.79451 | -57.82688 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 3e630bbf-579b-3789-875f-e27e214e7535 | -16.79349 | -57.83207 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| cfbd36b9-3d5b-3444-8ba8-4e1509f8246e | -16.78409 | -57.83004 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a2cb433e-a732-39da-b32f-7a453bd502d6 | -16.78307 | -57.83524 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a7635762-ec83-3c54-978f-14003822a295 | -16.76383 | -57.75276 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 87bc723d-fc79-3f94-a4ef-b898c7d7864d | -16.76014 | -57.7466 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a0ee1dca-1373-33d2-8dc8-1bab08ce466f | -16.75077 | -57.7446 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 212d57f4-59ef-34ce-9281-5daab94871c2 | -17.02396 | -56.78114 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 38f7e4f6-4a0e-3310-b6e7-0ce7c199d1ac | -17.02187 | -56.74407 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0f9fa1a8-4212-3c03-9a75-f3d772364de6 | -17.02104 | -56.74847 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 01e088fd-890d-3e5f-9d83-4bdc2ca18812 | -17.02021 | -56.75285 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ace4b5fd-2b35-3c95-af3d-aaa096eb03cb | -17.01875 | -56.78463 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a1cd72c2-db02-371d-9976-af72c415e416 | -17.01855 | -56.76167 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f127aa82-0c28-3827-be86-e574c8bc0069 | -17.0175 | -56.74316 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| c66c1b8e-8414-35e6-8faf-c2f3032543af | -17.01667 | -56.74755 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| f0acf09c-1f1a-3a89-b2ca-03c35aba71b7 | -17.01604 | -56.77489 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4751f8f3-c912-34d5-adc2-8f6c79547e28 | -17.01584 | -56.75195 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4a4d4c24-72a7-3f2b-a117-b1fd1bbc505d | -17.0152 | -56.7793 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e1812397-23aa-30d9-b9d8-c145881b3add | -17.01437 | -56.78372 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e518bd89-b7e2-3ab9-b8de-8dab9a97fedd | -17.01333 | -56.76517 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d34f6a2d-0f65-3b32-b44b-6ba2e9635302 | -17.01314 | -56.74225 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 40e5a6db-5519-3133-89ae-673af85998be | -17.0125 | -56.76957 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7871dc32-04f5-37a9-8b7f-ca907b782f6b | -17.0123 | -56.74664 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| e784b256-a8d0-3bec-b402-d6a824a992c3 | -17.01166 | -56.77398 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3c15678c-1162-32d7-bc2d-78d3feccd4b2 | -17.01147 | -56.75105 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 602b773b-5e7d-3d91-b086-251934dad9ff | -17.01083 | -56.7784 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| f6b2ef83-24aa-34b1-8152-a4b5ada3e3f2 | -17.00999 | -56.78281 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| f0a2ae21-e6c3-3a57-a394-ff3303576125 | -17.00915 | -56.78722 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9c1fc8d2-f973-33cd-95f0-cab2f83327bf | -17.00896 | -56.76426 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3e3d732c-8e46-357b-b441-10d1429b2f59 | -17.00877 | -56.74134 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 75e6bdbd-2d2d-3e84-b517-2ed88e5e2e9f | -17.00812 | -56.76866 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0b4306c5-82fe-3c9b-a9f4-8e8a1c5f0a54 | -17.00793 | -56.74574 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| b0b76443-052c-3e33-8fd9-7aa820304c96 | -17.00729 | -56.77307 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b9501130-3bd0-32bd-98b8-52877fde53f0 | -17.0071 | -56.75014 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 80a906be-53bd-3e47-a940-572bf9423320 | -17.00645 | -56.77748 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 3cadab09-b1e8-3546-91ef-ed0aadb2bc2d | -17.00626 | -56.75454 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e091d869-64c2-32fb-995f-94a1ddd64699 | -17.00561 | -56.78189 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| e47a1d27-aa1d-33d7-b1d1-0513305bf4e5 | -17.00477 | -56.7863 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c2ce8740-59cf-32d6-b11e-7a6d7fffc4d0 | -17.00458 | -56.76335 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9fcaa25f-7107-3e0d-ada5-6e04815b6a99 | -17.00375 | -56.76775 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| aa12333c-6003-3d36-8c78-0056a455105d | -17.00356 | -56.74483 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 2c825280-13e4-3836-a9ea-794d052912de | -17.00291 | -56.77216 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 5e25e9d5-d44c-3afb-b3ce-e60704270d79 | -17.00272 | -56.74923 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c77dd012-72eb-3b73-97fe-566ff54363d7 | -17.00207 | -56.77657 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 0497d509-900c-3fa5-b899-af43dea82cf9 | -17.00189 | -56.75363 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2f5dbee0-34a8-3a51-8394-d29ced4a18ec | -17.00123 | -56.78098 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 4d5958d2-addf-359b-b103-dadd29f9d478 | -17.00021 | -56.76243 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ea0f1163-f01b-3c2e-a89f-bfbd81c3b415 | -16.99937 | -56.76683 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 271db131-afd1-31dc-8bed-5f03f9ac0467 | -16.99919 | -56.74393 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 7b7f74b9-6b46-3aa2-b1ba-a142dea659ca | -16.99853 | -56.77124 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 536188de-1bf3-37ee-b78d-000f7725da46 | -16.99836 | -56.74832 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e06bd5ba-c53b-365f-ac35-5d6f761e9336 | -16.99769 | -56.77565 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 13398354-42d8-38cc-9ddf-24b2e0b1661e | -16.99751 | -56.75272 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 590dfc8b-d4eb-3146-8618-49084af5518b | -16.99685 | -56.78007 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 4ef73763-b7e2-3d9a-b7a9-1042c87e8730 | -16.99601 | -56.78448 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 255baec9-3a19-39b5-95c3-18e94217f420 | -16.995 | -56.76591 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 326a5c40-7927-38d7-b463-68a5c0e49e2f | -16.99416 | -56.77032 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| d06a5375-dd35-380a-9d9f-f763ebbcf67d | -16.99331 | -56.77473 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| dc98a39d-ff8c-3116-9c22-bb5bf155743d | -16.99314 | -56.75181 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cb8a9037-a7a3-30ef-9e56-d7b74976bdba | -16.99247 | -56.77916 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 54d72f91-b37c-394d-8e4e-4c6445997130 | -16.9923 | -56.7562 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 74b5e346-96dc-3a3e-af5f-64b9cb2225da | -16.99062 | -56.76501 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 74c5b95d-8b86-35d2-9841-5f447dee34f4 | -16.98978 | -56.76941 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 4e894f2c-2fe8-3b9d-bd50-93136b0d5760 | -16.98894 | -56.77382 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 2a903041-3542-31ca-b22b-5b1c72b232e2 | -16.98877 | -56.7509 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1a934adc-6a58-37c5-8968-827e390273c2 | -16.98793 | -56.75529 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 35e253f3-4287-3b33-b360-79a4be6f70c3 | -16.9854 | -56.76851 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| fdb3a89f-aa94-39a9-9382-d304e6663328 | -16.91422 | -57.69358 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 00645acc-4289-3006-ae77-316d9f75c9c5 | -16.91323 | -57.69865 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 97a0a852-f0a3-3c93-bb72-1eec8652abed | -16.89197 | -57.68358 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 92ad2383-78ff-3998-b761-9635a7097e19 | -16.88972 | -57.6871 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 57bce426-febf-391a-831e-9952a6e7890b | -16.88732 | -57.68259 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |


[Clique aqui para ver as próximas entradas](README129.md)
