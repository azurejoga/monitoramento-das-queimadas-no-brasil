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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5c9e14a-68d1-3eff-a125-67917f32d364 | -6.31683 | -43.0567 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 605c4945-7dd4-3885-8f1c-9a8ee73f889e | -6.31287 | -43.23256 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d663a33-3759-3b2d-bdde-c773ccb49151 | -6.31125 | -43.24285 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1b6be85-6cfc-35b5-b721-0319622fd011 | -6.30735 | -43.22463 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85023666-ef2c-385c-a743-71bf9ed24c94 | -6.20339 | -43.27893 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb0c4d06-4456-3edc-942a-1e439ee672a7 | -6.20063 | -43.27497 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9fb548d-6173-35d2-bbf4-87915bdd8821 | -6.18703 | -43.33994 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23487ffe-df37-328d-8872-7d6607cab67a | -6.1601 | -43.10276 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fca2ae9-357e-3863-a1ba-818e958f62f7 | -6.13376 | -43.37754 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf4a72a2-cd23-3970-82b7-652b50f88a99 | -5.81928 | -43.23558 | 2024-10-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f61694d-6baa-3a74-a890-6f11aa2fb9ce | -5.81652 | -43.23162 | 2024-10-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f0694811-802f-34e6-9a27-4dd7488f81ed | -6.31422 | -43.37838 | 2024-10-09 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 652a7d28-0e38-356c-a8e8-a9c986fa1f7e | -6.12498 | -43.3903 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f426f238-2630-3522-8ab4-b161c1cfc322 | -6.43292 | -42.09444 | 2024-10-09 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7794fb5a-af0a-3968-801e-4ef1e7e8d06c | -5.9686 | -43.36507 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dfd2a7f0-2543-34c1-bff3-9675857a3bf4 | -6.12883 | -43.38737 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d2d56bf-9e0f-3250-89f5-ed7fe1c8c277 | -6.12828 | -43.39083 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a10ab601-74cc-3268-9a87-59ab4a305928 | -7.9272 | -42.46054 | 2024-10-09 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6c558949-e948-3610-bf45-9a7b3d746b8c | -7.92333 | -42.46353 | 2024-10-09 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e4c62013-bf32-3b48-b969-d66e4fd92602 | -7.92109 | -42.45594 | 2024-10-09 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8669e6df-40f1-3dc6-9c08-6c5562c5e44e | -7.7911 | -43.09679 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| adf6883b-5197-375f-98f3-0da467de323b | -7.78942 | -43.0859 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a2bb245b-a998-3766-9ad7-fcd43eb01a0d | -7.78888 | -43.08936 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dcd9cec3-3498-3f0b-8943-6f53d920c0ee | -7.78834 | -43.09282 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aa5bb293-83bb-3d58-930f-dd469493d459 | -7.78666 | -43.08193 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b2bc2b39-cb31-3a28-b3f6-247f2f6530b5 | -7.78335 | -43.08141 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e73f2bc4-9eed-3392-8d7e-04ac10debab1 | -7.77783 | -43.07346 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dde3e923-e737-354a-9811-353867bf5f79 | -7.77627 | -43.10511 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7304669d-d33c-3b49-afc1-b1cc073c7a1c | -7.77519 | -43.11203 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6084a4dd-9adf-3a29-9a03-1c14b08af6b7 | -7.77021 | -43.10062 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fb1fd6f6-2aa6-3eba-bc49-35544e45f114 | -7.76967 | -43.10408 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0349228e-207e-3826-8418-9e478b41ba6c | -7.76913 | -43.10754 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59e4a8d4-8f64-364b-ad9a-af1d935c653b | -7.76745 | -43.09664 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| ee6a6099-7aab-38f2-970e-624fcd6e500e | -7.76691 | -43.10009 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 208491be-5312-3f38-af67-b290d17abb12 | -7.73469 | -43.0419 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 88352b92-7018-3497-b531-2fda25207345 | -7.73139 | -43.04138 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6be63728-fca1-33a1-ba74-cf07b131f754 | -7.73085 | -43.04484 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 01768857-b24d-3850-947b-cf05ebacd020 | -7.73031 | -43.0483 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a58eea06-6604-353a-a268-921b6d1e0b94 | -7.72977 | -43.05177 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7181ec1e-a1d7-3bdc-a3d7-2141f50cb607 | -7.72923 | -43.05523 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ff4132e4-241c-349c-a38a-7d10d319212a | -7.72755 | -43.04432 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0b2e8f81-cd07-3c9d-8433-6d771d037794 | -7.72701 | -43.04779 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 14ea64fd-deb1-3208-ae4e-ca090d54f94a | -7.72647 | -43.05125 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f5a98a1a-8d39-3c81-a0af-53aa4a7d6f2d | -7.72593 | -43.0547 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f0bd8a0c-62b5-31e0-88ed-494efbe2020a | -7.72371 | -43.04726 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 83fb23b4-99b8-3688-8740-bce9e33fcfed | -7.72317 | -43.05072 | 2024-10-09 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| ee7f7adf-77e6-377a-9177-7e4c0927ac80 | -7.69549 | -42.98961 | 2024-10-09 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0334eabc-9da6-30f2-a613-dfef616b11b2 | -7.69219 | -42.98909 | 2024-10-09 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 29fc1454-2cdf-3ea9-bc4f-4f0f0d12ae29 | -7.68943 | -42.98511 | 2024-10-09 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f8ca7a5d-f60b-3cab-9da2-1757983c13b8 | -7.68889 | -42.98857 | 2024-10-09 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3d2945fb-7635-3cea-8ded-d46001f92c87 | -7.68835 | -42.99203 | 2024-10-09 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| af8982f2-38d8-3e90-bab7-8c28d8520502 | -7.68612 | -42.9846 | 2024-10-09 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 8d2dc36e-1d95-3609-927d-591bcb21366a | -7.68558 | -42.98806 | 2024-10-09 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6afc3320-e527-38a1-b701-f2a9d7ab4bc8 | -7.66236 | -42.52348 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 47d985e9-c28f-32ed-a312-fd12d504df93 | -7.64988 | -42.40654 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a30e5844-80aa-3de4-bd22-fa509b54a23a | -7.64656 | -42.40601 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 912047f2-d624-3c78-99ee-e80d15d01653 | -7.62163 | -42.41293 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8fc9f534-69b4-3f41-8e36-518986f61e93 | -7.61557 | -42.43004 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f8286d7f-4994-3c79-a4a7-a5f43438f719 | -7.61448 | -42.43707 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4cc3c672-0f3a-3d0e-91f0-e2cba76778c3 | -7.61224 | -42.42952 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1dd3eeba-164d-3edf-930a-6c0a95d2c15c | -7.6117 | -42.43303 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ff1c0163-c004-37ea-ac1b-1364310beba8 | -7.516 | -42.76541 | 2024-10-09 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cc55b04c-f451-3bb7-afba-e6b618c2d63d | -7.93162 | -42.45399 | 2024-10-09 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a4c1d819-ad08-3423-a24c-429371dce884 | -7.92497 | -42.45293 | 2024-10-09 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b649e883-0f7c-35dd-8297-e2fc94692d0a | -7.66948 | -42.49942 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 227f60e2-e43c-386b-8eff-9e199490ed5b | -7.66731 | -42.51347 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 30c13544-b98c-3659-a9a3-041eb74b6991 | -7.66724 | -42.4919 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ef1f5177-980a-38bf-ba86-c3fec9acc078 | -7.66399 | -42.51295 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0449c9fa-140f-3e52-a7f3-5a8ff7fbaaaa | -7.66345 | -42.51646 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1ce56b1b-0014-3922-a4fd-8def812f93c8 | -7.66012 | -42.51595 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 49989c5c-b81f-31a9-8621-61e43d91cbc0 | -7.65742 | -42.53345 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 240eae65-4813-3d53-b7ef-af4714980ff7 | -7.65587 | -42.41085 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5b00d212-0a13-3fd2-afea-d04da8524278 | -7.6541 | -42.53294 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4f3662f9-ad58-3fe3-a28f-c0447f849538 | -7.23517 | -42.29523 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a6cde882-c4a0-3a88-94f5-80e4451a3fb0 | -7.65321 | -42.40706 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f5f0821-9c66-36e8-9781-6a495140cfbb | -7.63603 | -42.40798 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e523a66d-dc3e-3977-ac86-9370fedaf49d | -7.6255 | -42.40993 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 56adc2c2-56f5-3005-9518-c0694b2f8e29 | -7.62053 | -42.41998 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e477f981-7c03-368e-bb9e-d6b9da13b46e | -7.61999 | -42.42351 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dd827ec0-978a-31a9-83a1-5d1beb3f5729 | -7.61721 | -42.41945 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 01cf99b4-f2b5-3257-97ef-47f5d3208646 | -7.61611 | -42.42651 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 38dc1970-10f5-3d15-97fa-fc1e337687c8 | -7.51269 | -42.76489 | 2024-10-09 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 85478aaf-5ad2-3191-8208-58f98bc006a1 | -7.92884 | -42.44993 | 2024-10-09 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3990a99b-7290-3326-93b7-f023a081749f | -7.92829 | -42.45346 | 2024-10-09 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d3389876-d9d6-352f-a332-5ae8e4397de9 | -7.92551 | -42.44941 | 2024-10-09 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b62c1190-98bf-31b9-9921-f7c5bbc067e5 | -7.67063 | -42.51397 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 44c02eec-05d9-368b-941b-8eb966a9148c | -7.66677 | -42.51698 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9857d804-5381-389a-a31a-5c28c8d65906 | -7.66615 | -42.49892 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3e027405-93f9-3682-839b-d22eb51355b7 | -7.66391 | -42.49139 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7475a68d-ff6a-3a47-bc12-ef5c18cb1d1b | -7.6517 | -42.48228 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8cfff085-969d-3933-9c95-4953bb89dc76 | -7.62386 | -42.42052 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48ad913a-833d-3f4d-ba9d-20aac0a42e2d | -7.6667 | -42.4954 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b831dbbd-dbb8-3551-8d13-25894092d853 | -7.6629 | -42.51997 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| cea9184a-3cde-3f9e-b8da-1262174f0b3f | -7.66199 | -42.41542 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2397e1eb-27a9-3e05-b3dd-e81d237a23da | -7.66182 | -42.52697 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2fb3e67e-6fa0-314e-afec-5f682133f638 | -7.66067 | -42.51244 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 95155112-db17-3102-a954-a1b9e190c58e | -7.6592 | -42.41137 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6a11c326-858b-365e-928b-bbd98fc7a1e0 | -7.65796 | -42.52996 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0da3d83c-6c8e-3f1f-a6b1-34998f8de9f6 | -7.65503 | -42.4828 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cd346361-23ab-3db9-88c5-a66741fd228e | -7.64305 | -42.53838 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README72.md)
