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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e22ffaec-e59e-33bf-8cbe-404cd2ecb4fd | -2.30507 | -46.66943 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f46fa886-9ab1-3bd6-adab-2b5625190e87 | -2.30451 | -46.67309 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e73e15b-abc7-3719-9085-258c56728b7e | -2.30223 | -46.66525 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9ac4862-cf0d-3bc5-a0bf-47e04ac75cd8 | -2.30167 | -46.66891 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcb02abd-09aa-30cc-8061-e49b28ff3cc1 | -2.30111 | -46.67257 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36c54df0-e689-3150-9dad-b9944a54f6c9 | -2.29998 | -46.67988 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ba7ec4f-a189-3a16-b8c1-a6103de172da | -2.29827 | -46.6684 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8062b94f-e2cc-3332-a8cb-3e577e82b22a | -2.29797 | -46.66502 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ef261ba-7cf3-3600-8cea-872485768a82 | -2.29771 | -46.67205 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d669dc18-41a5-3183-99b8-1df66348e742 | -2.29739 | -46.66867 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2326372a-2822-38b8-8c1e-91c25e6a2f4b | -2.29554 | -46.75388 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a52ab7b-5357-31f0-b5cf-58a936889a94 | -2.29441 | -46.76115 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f0ddd9b-316c-3691-9713-a3d3d0bf0ee0 | -2.29342 | -46.67182 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b213ad99-a37b-37f0-8078-62768f3081e8 | -2.29271 | -46.74973 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bd20e62-19f1-3d43-9aaf-cf176c3341fd | -2.29214 | -46.75336 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8fdfaaf-5fb5-3953-b89d-37d53ea1bc1f | -2.29117 | -46.66397 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a394869f-50e5-3224-8ef7-0c0057386e17 | -2.29102 | -46.76063 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38e1d5b3-85d9-3880-a575-25c095448a19 | -2.28987 | -46.74556 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7de28e03-a45c-3c21-b7eb-43742d899f92 | -2.28892 | -46.65615 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 973c2814-30bc-3368-8ce3-9d6c8fc1bd82 | -2.28835 | -46.6598 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c05105e7-a377-32d0-bb4a-dac38005db4e | -2.28764 | -46.76011 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30cf6376-372e-3608-8cb0-8c0217b9f459 | -2.28708 | -46.76373 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3481d790-10ef-310f-b277-49bb683de7a6 | -2.28704 | -46.7414 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f836f5d5-3c11-39ab-a747-d2c54405406e | -2.28552 | -46.65562 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42bcaba7-1f08-3a5b-bffa-80bd36e054bf | -2.28425 | -46.75959 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d5a4e98-ff41-3c91-8456-2f591579f092 | -2.28369 | -46.76321 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ced9431-ea49-3d65-b9fb-6102961cbe78 | -2.28306 | -46.75977 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cf26b9f-af8d-3873-8012-eb3b055e2392 | -2.28024 | -46.75562 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 191a0815-c736-3ce4-9966-75ec058eec68 | -2.27929 | -46.65092 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30ea1ff5-b0a4-3587-a816-db531c06d5fd | -2.27872 | -46.65458 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9473bdce-10e3-327e-9caf-7226ffd210cf | -2.27589 | -46.65039 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b96c40c-9651-3dd6-9089-3b033c428281 | -2.27532 | -46.65405 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1133a1f6-f649-3e9e-b81c-9b0d778fb835 | -2.27249 | -46.64987 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c2d0b89-1f41-3f61-93e2-44570b8ed743 | -2.27192 | -46.65353 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bccaa9fd-107a-30db-ad0a-b115a81cdc45 | -2.27175 | -46.76545 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 447d6a7c-3573-3e05-8efa-86a3c5646b26 | -2.27135 | -46.65718 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 571c1175-e359-37b7-8c72-8130c3f1fd1c | -2.27118 | -46.76907 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc327fea-72f9-342c-b544-a1b337e30e03 | -2.27064 | -46.75041 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56f98886-0f9d-3a3d-86a6-fd01bb931e7f | -2.27061 | -46.7727 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea6eb5ce-d022-3c2c-b07b-5b44fe893799 | -2.27058 | -46.79499 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 368bb0b2-e0c6-3420-99da-e099bea7f1d7 | -2.27007 | -46.75404 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 288df05a-1a52-3c94-adab-1364d9a849dd | -2.27001 | -46.79861 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07caf756-c77c-332e-94ce-0c6775a8a56f | -2.26944 | -46.80221 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6da0f6f-4197-3283-8ab7-c180bb28c64a | -2.26909 | -46.64935 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40cde00c-a9b9-3d50-a804-1c33c75a0186 | -2.2689 | -46.78358 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 400d645f-e546-3183-af29-eae1c503f23f | -2.26852 | -46.653 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79248de3-cbbe-3378-9355-abb235cd637d | -2.26795 | -46.65665 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93431412-3e9c-37be-a75b-069449334806 | -2.26776 | -46.79083 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37777c16-93b1-3050-ab1e-7d49f6f2ef98 | -2.26549 | -46.80531 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ad8d501-55ae-371d-9eb2-88e551b8fb25 | -2.26438 | -46.7903 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37522032-a3a5-3598-9096-153a1a06405f | -2.25252 | -46.79961 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5b88f0d-7074-3049-ae44-c4eddafe5146 | -2.25132 | -46.8955 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce2de785-b332-3a8b-9a2e-33cfbade63a2 | -2.24795 | -46.89498 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 441c9448-fd0a-3664-80f0-6c8bc9501f8e | -2.24689 | -46.79131 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d00df91-d72c-3bb3-996d-b513eccb2ea5 | -2.23222 | -46.79643 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1da6ad22-04a0-3f0b-b823-80d7ca443d5e | -2.22602 | -46.70246 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a712c46-b2ff-3b38-b8f3-70e43094a40c | -2.22264 | -46.79123 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f7a3f17-a88f-3fa9-b330-ce1b30fa8a85 | -2.21925 | -46.79071 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38a9d3ec-4870-3da5-89ff-abe4c07f3874 | -2.21138 | -46.88573 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 595e90ff-7990-3565-a992-09b07ccb05a9 | -2.19379 | -46.70866 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea0fe1b7-6b63-395e-872f-cd4d497f2fbb | -2.1918 | -46.9892 | 2024-10-29 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87705208-3b1e-30e1-bde9-47dd4330ed68 | -2.17913 | -46.73621 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7d2175b-0455-3949-baee-288e6f995006 | -2.17837 | -46.73283 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cd09040-a8fb-3a44-9152-4013b6fb3217 | -2.17726 | -46.71777 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9ab4a7f-2c94-3fb1-849e-d94b6faa8ae6 | -2.17669 | -46.72141 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d9a58ef-0f55-3672-a7b3-d4fde688fd95 | -2.17555 | -46.72868 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f66bb462-90ad-34fa-8717-a7f8aaa4d0ee | -3.23769 | -46.51409 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8cc22150-1b2a-362e-8ad5-e85657474a6a | -3.14587 | -46.51905 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 529b439f-fc17-31ab-9123-551cca03458b | -2.37836 | -46.55655 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f569f933-1131-3477-bde7-b60d8089e7f2 | -2.37495 | -46.55602 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2287ac11-e855-3da0-a91f-2c84d874d191 | -2.3738 | -46.5634 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4052370e-f254-3d8a-a66c-82023bcad663 | -2.34253 | -46.47135 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d2235fa-1144-3de4-b4f9-8c10cf6eae7d | -2.34025 | -46.46338 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 175119bd-e46b-30c9-8d52-9c16fe19f065 | -2.33911 | -46.47081 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2693a648-4dbe-397f-9dec-6dd02b699a1b | -2.33854 | -46.47453 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5161945c-e3e6-3036-a622-f42d77d2a920 | -2.32941 | -46.5111 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36ef5772-4e42-32af-abf0-9b7426b3195c | -2.32713 | -46.50317 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d13bfdba-480e-386d-81d0-7f0f350b6003 | -2.32656 | -46.50687 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b6bb7ca-8317-3f03-968a-1d94b68f2ca0 | -2.32599 | -46.51059 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c606af4b-b851-33cd-8c14-1d9fe6c75500 | -2.32371 | -46.50265 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 405368b6-bd8d-383f-a3d1-50bac854f7cb | -2.32346 | -46.50314 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9482cf9f-1986-3c0f-aad0-030e4c2a248e | -2.32314 | -46.50636 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1ee287d-fa08-36ab-8989-f24fa2a425c7 | -2.32287 | -46.50684 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9869dc0-185a-3c1f-b8e4-9e45d1b14b0f | -2.32257 | -46.51007 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 852bb423-b6c6-309a-84cc-7ddf2f518448 | -2.32229 | -46.51055 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 409d218d-9fa1-3fc9-9a91-8e90e339b39b | -2.32069 | -46.47615 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f04bb9f9-e2b6-3cdb-b3e9-1802519560f3 | -2.32004 | -46.50261 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e0f8017-c4de-3f67-aa24-f0ad4bc2c632 | -2.31945 | -46.50632 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f850fc88-2f69-37da-a9be-0e2d86f47f87 | -2.31887 | -46.51002 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5e18f17-889d-36ae-8443-add879b947be | -2.31662 | -46.50208 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6473491e-abf4-3fd0-be9b-06566162417b | -2.31604 | -46.50578 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e8b684a-92bb-3b96-9b3d-206703c999d3 | -2.31545 | -46.50949 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7f4c571-0771-3e39-ba7a-7c3886210e55 | -2.3132 | -46.50154 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 436e471f-a07a-3616-b50c-219bf9f30074 | -2.20925 | -46.42531 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36ecc1ab-0334-3b57-917a-58f941c0071e | -2.20298 | -46.42054 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69043f08-36b4-3f4b-9110-58e10fe552da | -2.19601 | -46.46507 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 847be080-754c-3d6d-ba52-752ca3d4ee6f | -2.19317 | -46.46083 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d4c6bd4-af9d-3e99-b0b0-4dcb22864746 | -2.19259 | -46.46454 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 386ad096-2671-3372-b170-6733ff606c78 | -2.18917 | -46.46401 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1bf2c78-628e-345c-8a5a-90300cf28146 | -2.18859 | -46.46772 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README38.md)
