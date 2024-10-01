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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32874132-61c9-371f-8066-9ad1895ccd2f | -2.86425 | -50.70858 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a13f27c0-08a5-3b57-86eb-9ee78e9bd095 | -2.86278 | -50.71766 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1dbd7475-941c-32c8-aa01-3c12ed768458 | -2.91409 | -50.74172 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ac285c1-a212-349d-93d6-80d5bdf4548a | -2.91359 | -50.74475 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 24d19113-c64c-3eba-8bf0-229785609af7 | -2.91258 | -50.75084 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 18e49ff6-f336-39e7-9c80-b10305d9ebc4 | -2.91207 | -50.7539 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| baf1c7e5-652f-33a4-bcbf-359e08615830 | -2.91157 | -50.75694 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ad5e770b-d4c0-341a-a497-1d06ed53d033 | -2.91113 | -50.7914 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac494307-9dba-3af4-982e-ac3f95422ebe | -2.91106 | -50.75998 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 142724bd-f68f-3826-a632-f9c21c93eb61 | -2.91056 | -50.76302 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79c14a04-65a1-3300-8143-19f2921af353 | -2.91005 | -50.76608 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56d02531-44d3-34d5-bdc7-6afe4390ddfa | -2.90947 | -50.73785 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be0344d6-01ef-30f0-9c72-bbf7e11d22bf | -2.90897 | -50.74086 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9158ece2-675a-3761-96ad-6558cebe6bfb | -2.90847 | -50.74389 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f52937a-2ef0-3997-9017-bb2bbf358c06 | -2.90796 | -50.74693 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8cffc285-1b0c-3ca7-a715-17c98b3336a7 | -2.90745 | -50.74998 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 94756814-3098-3d86-a00e-36239f25901c | -2.90694 | -50.75306 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d8ee453e-ef04-3caf-babe-2a3ce6a4b78b | -2.90644 | -50.75611 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 394fb117-c328-3d94-bf82-51b8d1261521 | -2.90593 | -50.75916 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 08329ccf-4ed4-370d-b6f2-8471fa4542d7 | -2.90542 | -50.76221 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51e882d1-6af3-3fb6-8a8b-c68b87c992c4 | -2.90492 | -50.76525 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f0d9e69-cdaa-3d11-b513-1ec070676418 | -2.90435 | -50.737 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bdf50ef4-741d-3f9e-9ca7-bc0b013b48b8 | -2.9039 | -50.77135 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09869471-f6a5-35e7-927d-7b3501d7f2f0 | -2.90385 | -50.74002 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 961980d8-a2c7-3835-98c5-4cd78e18b618 | -2.90335 | -50.74303 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 208687be-ab4c-35f9-b510-62fe32bac583 | -2.90284 | -50.74606 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 890f4e66-793b-3c3f-ba0e-c86571e94b63 | -2.90233 | -50.74913 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| bef00863-7b7b-3125-ba8e-59325cb909e9 | -2.90182 | -50.75219 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 828acbc9-15c7-3c1d-9a24-7f66be257f64 | -2.90136 | -50.78667 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 086df7a9-e326-3cd0-a6af-37c50c648afc | -2.90132 | -50.75523 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cf2754f9-1449-30ba-a8f4-9aa7fd4089c8 | -2.90081 | -50.75829 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b8c3e4d4-24da-3798-8e1b-f29d5663b8ef | -2.9003 | -50.76133 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 043b22bf-127c-3a27-84f7-13124b006044 | -2.89979 | -50.76438 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19c4366c-bbfc-36c1-89d2-aa42b8758f9b | -2.89932 | -50.79889 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69d987ec-731b-3fbc-b058-90ce48053b96 | -2.89928 | -50.76742 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cebed64b-c455-3f80-87fa-6b31b9b040f2 | -2.89923 | -50.73615 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b30180a6-9814-38cd-85a2-d922a76434cc | -2.89877 | -50.77048 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cedb7f5c-603c-3d38-9ee5-cf34f3f55051 | -2.89873 | -50.73919 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a7f9e314-bb55-3c44-8658-ca0c47db2b7c | -2.89827 | -50.77354 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ca1f7cc-5597-3411-ab33-11e2ee8e601c | -2.89822 | -50.74219 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| a580dd4e-6c04-3049-8442-c59e102b55a2 | -2.89781 | -50.80801 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 277fcb63-3bb3-3447-b5aa-61f837e445ff | -2.89776 | -50.7766 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 286f2432-f2a1-3ea2-9b91-a5985b78b396 | -2.89772 | -50.74522 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 425b9049-bccf-3be3-8440-ccaf9d4ad133 | -2.89725 | -50.77966 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f4d9073-f129-3403-b8e7-95f403c7e93e | -2.89721 | -50.74825 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 384a731d-c736-3f86-87dc-d2a9f02c6ff1 | -2.89671 | -50.75129 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f21aff83-a133-3436-a300-ac85fb2a4e9a | -2.89622 | -50.78583 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 406a9b94-5940-3f01-9e90-051b2f8e41ac | -2.8962 | -50.75433 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d769b45-81a7-39f2-8be4-3bd6ac4038a6 | -2.89569 | -50.75737 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 97255dbd-619d-3c6d-bd21-c919e460794d | -2.89518 | -50.76043 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39275795-4d9b-31b4-aa35-28e745168ffb | -2.89467 | -50.76348 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cb6a2c5-df91-3263-97b2-80da0d8c6ef6 | -2.89418 | -50.79807 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3a1506fc-bd27-369b-801f-9c83b7510c2d | -2.89416 | -50.76655 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ec4c46e-d6a5-39d6-91c5-69cd7c8b4b0a | -2.89365 | -50.76961 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d0946be-750c-3808-824e-b2526bf32367 | -2.89361 | -50.73833 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 1a32a6d4-d8a1-31c6-9a25-0d7aa2e6a18b | -2.89317 | -50.80413 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d0402146-d46e-3680-aac3-ebe83ac90b84 | -2.89314 | -50.77266 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9ebc806-2a05-30d9-b01c-fcc657315b2a | -2.8931 | -50.74135 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2a4761e3-8495-3295-a096-01d21cf3079a | -2.8926 | -50.74437 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7fe7d2af-f68f-3f27-9acf-d8788117f838 | -2.89216 | -50.8102 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c314f7b4-3d40-353d-9a86-bc6f58a7857d | -2.89212 | -50.77877 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a14e0d60-366a-3d13-8cd4-037fc4c67d25 | -2.89209 | -50.7474 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45d4c651-4767-33ed-9cb2-ef3d35ceb1e7 | -2.8916 | -50.78183 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6151f3ae-8b3a-3cf4-9642-95450f6cd175 | -2.89158 | -50.75045 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9cf7fd7e-707d-38a1-a601-e13e58782b0b | -2.89107 | -50.75349 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ce825f3-19ce-32e4-9aa0-6b5d51f03a2b | -2.89058 | -50.78798 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 493fcd5b-e03c-3336-aff3-602c0f4585dc | -2.89056 | -50.75653 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95a4213b-fbf8-389a-9117-49b2da48909e | -2.89005 | -50.75958 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 724ff52e-31c5-3142-b6c0-f6c86ebd9e55 | -2.88954 | -50.76263 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb0b7ac1-f647-3aff-96e4-c568986baeb6 | -2.88904 | -50.79722 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d6e25e74-653e-3cf9-94f1-5a4db2a4702a | -2.88903 | -50.76568 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e31745eb-8f06-31d4-936b-808570a130cf | -2.87551 | -51.6539 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 197e06c7-2642-344d-8082-7aee36b4c2f0 | -2.87516 | -50.78543 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d178c968-818f-318f-815e-21cd177c0aa7 | -2.87493 | -51.65736 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a28d3b5-fae2-34f6-bf07-9c30d9921924 | -2.87435 | -51.66082 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c3ac5c4-d017-3290-9fdf-22fec8e2fa9a | -2.87377 | -51.66431 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d82674d7-87fb-3029-b1ce-c6c656643b98 | -2.87312 | -50.79761 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5379305-7a8c-3e40-9387-77d5754d6433 | -2.87261 | -50.80064 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| accde876-0344-3d41-8a87-479fc783f885 | -2.87209 | -50.80368 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a7cc034-b475-31a0-b7da-c37ac288fbb6 | -2.87198 | -50.79134 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 592e592d-fa20-3298-81e6-a82a915208e7 | -2.87157 | -50.80677 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7630f4a-8ff3-3937-87ea-804a45cbbdd5 | -2.87149 | -50.79437 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 092a1f69-26b2-3715-ae63-1a480ca2ce07 | -2.87106 | -50.77845 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ff23fd4-7922-36fe-95f6-327823e63a28 | -2.871 | -50.7974 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 11561ded-b414-334f-8469-f27c450b59ac | -2.87054 | -50.78154 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10f467dd-7581-3594-8698-261f07768920 | -2.87052 | -50.80045 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89a51269-b0b5-372d-bbfc-ff70998ccc8b | -2.87007 | -51.65293 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f87cd6f-e3c0-3ba2-ab4d-a1f7e4b2d75d | -2.87002 | -50.78462 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c162f9f-98df-316e-a52d-d1afc4aa0aaf | -2.86953 | -50.80658 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5aae501-f730-39ab-80c6-543a5a45c934 | -2.8695 | -51.65636 | 2024-10-01 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a40f9e94-89f9-3ad8-a138-79526244f9c6 | -2.86903 | -50.80969 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48a91eab-2578-3284-9069-b5b898164ee5 | -2.86899 | -50.79071 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c159d056-d9bb-3d68-92e1-7181c6f0f908 | -2.86695 | -50.80283 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3674dd82-e2e8-3e1f-9e62-8c6fa484e19c | -2.86644 | -50.7745 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7e59dba-2b99-3b84-9ca4-8de84c67352b | -2.86643 | -50.80589 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5cd81e3-293f-38cb-8c24-d22be1904d8d | -2.86592 | -50.7776 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 942c625e-eef0-33d6-a053-fabb8ed4e296 | -2.8654 | -50.78067 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0223f501-8119-39ba-9236-33ba22f670ee | -2.86389 | -50.8088 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4ff84b6-3dc3-3b91-aafb-f8a7948700c8 | -2.86131 | -50.77362 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2d74c7e-d884-3e05-974e-dba36c44dbfb | -2.86079 | -50.77671 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README62.md)
