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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9353ff1-f732-334b-b4b5-cde697263f06 | -16.80128 | -57.83476 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2e62d027-09a6-347c-851d-7d21c5cab4ca | -16.79617 | -57.84574 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a531e853-9794-3d2a-b824-c783ccac6b8c | -16.77962 | -57.501 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ff70a9e2-5fac-318a-baf5-6b43ff44b0c5 | -16.77898 | -57.74842 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ad2d9055-6ba7-3217-b619-20b2a3192cdd | -16.77795 | -57.82711 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0d09cc18-be46-3b36-b662-e9dbdabe590f | -16.7772 | -57.50111 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5ad5128f-f9b7-3a68-9f65-587bc285a0b1 | -16.77453 | -57.82657 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 329cd3ef-6050-34cf-ad35-c3d919b02139 | -16.77397 | -57.83041 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8f616308-c04a-31f1-b498-2404c37dce33 | -16.77319 | -57.48034 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c7ffdcf7-a347-335b-a2fe-7d6ab521354f | -16.77261 | -57.48428 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a95fb128-5d24-3b8d-8751-af71d235e6e1 | -16.77203 | -57.48822 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a5f913b9-05e6-3d2b-a0d6-6f2184fab9d0 | -16.76973 | -57.47979 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 268eed6b-1929-3ef8-906d-d52a2cf2d068 | -16.76754 | -57.73079 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 531d002a-8d51-35e9-9270-0967491a3a5d | -16.76734 | -57.56782 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 37afcfd9-47a7-3411-9a9c-7949e4f29f27 | -16.76628 | -57.47924 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f70db305-cf09-3406-b6df-a7831842b42d | -16.7657 | -57.48318 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 6d8ba450-5722-3215-87dd-4462fe6c3a8c | -17.10335 | -56.79425 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b9ac0e6a-f41e-3e90-8a36-4a5160eec53f | -17.10276 | -56.79848 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 63d2e65c-850b-3753-a520-f4dd4f60810e | -17.10217 | -56.80271 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 91f7450b-251d-3802-80e3-5af971a99b43 | -17.10069 | -56.79561 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ab39eeb7-d732-3a18-91dd-4ec5fff1879a | -17.09919 | -56.79793 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4ac48004-1bf8-321a-8711-4fe47721b2a9 | -17.0986 | -56.80215 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e66d21eb-1249-3149-acfd-7fd7b8e89e5d | -17.09765 | -56.8167 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 45b622cc-4652-3637-9635-e01acee0105b | -17.09712 | -56.79505 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9ae9b25f-9166-3e53-8bd9-5d5b4f88a581 | -17.09684 | -56.81483 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 353863cc-14a2-3538-9174-2188042aad1c | -17.09652 | -56.79927 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f3941d40-33da-39b5-8e95-78b318d47c7f | -17.09445 | -56.80582 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7aaa678d-7301-3caa-b1ab-9639d1517000 | -17.09355 | -56.7945 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 55411d81-6108-3590-ac2a-d477f62e9f6a | -17.09295 | -56.79872 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| bd85306f-db69-379f-a74c-37a32fb6ad91 | -17.09234 | -56.80295 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 57f48d1b-928f-363d-90db-4f7ecd49a07f | -17.09173 | -56.80716 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 11b738f4-08a1-3233-8f70-5af0ba6e42bf | -17.08756 | -56.81084 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 3a918405-4b19-3933-9139-9c161c6f245e | -17.08581 | -56.79763 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| da06ecaa-0da8-34e8-a521-3d7823e2bd5f | -17.0852 | -56.80185 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b365dd97-2593-3c20-b68f-7509e27bef92 | -17.0846 | -56.80606 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| ed8d43c2-a797-32fc-a79c-75ad70328f26 | -17.08399 | -56.81029 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 134d3a20-093e-30d1-852f-23caef56166c | -17.08163 | -56.80129 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b0397aa6-985a-307a-9615-6deffc0cbe49 | -17.08103 | -56.80552 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| c9fe2de1-e07f-3a20-a35f-66141aa34808 | -17.07807 | -56.80074 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5cc47c4c-76f8-369a-8a6a-7a889e42fd19 | -17.07746 | -56.80496 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 5ee84f03-1f40-35e9-a444-20406731bbc2 | -17.0739 | -56.80441 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 9971c0b7-8686-39c5-b916-ba46210ac2b7 | -17.06912 | -56.8123 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ffc8924c-cf7c-3cc4-b665-5015f366a353 | -17.06556 | -56.81174 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 62b058a1-6bac-30b0-99d9-2bbb08e625f2 | -17.06199 | -56.81119 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5ddc6daf-9ef6-3c9c-9f9d-804e2e87c357 | -17.05843 | -56.81065 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 00c5c658-55ce-3600-889d-68e6876381bd | -17.05606 | -56.80166 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ac24d285-18b7-3359-865a-2f050649c1b6 | -17.05546 | -56.80589 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ab1affd1-d1e8-3b9f-9d5a-01d4afb534eb | -17.05249 | -56.80111 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| df3d3e56-0f2d-3ce4-9146-3a14d0411999 | -17.0519 | -56.80534 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9c6a0098-f2dd-32c8-aae0-69750e7731ea | -17.0513 | -56.80955 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 3694f66c-8db9-30d9-aaed-da2148422cfd | -17.04952 | -56.79634 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cf81256e-e99d-31b5-8f4a-e86f26109fef | -17.04893 | -56.80055 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 796bb2ce-1217-34a2-9b93-b97376cfe8ea | -17.04833 | -56.80478 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 35d3609e-043a-3d39-81b4-fa384f20aff0 | -17.04773 | -56.80899 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 031d0c5b-8c68-3837-875a-781f830677d8 | -17.04713 | -56.81321 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 1161cdec-861e-3cb2-848c-e27cc01d9fc5 | -17.04 | -56.81211 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 51fe9e6a-24fd-3d9c-9b8b-6b0cbf61d589 | -17.0394 | -56.81632 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 304b202a-ad64-346f-a492-9c95aa14b7a1 | -17.03644 | -56.81155 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 24c78ffd-a52e-3ce7-b0ef-1f84a13ec468 | -17.03407 | -56.72465 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3b36a725-7b8c-3efb-ae14-2ef82570a3d6 | -17.03228 | -56.81522 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5e708b5c-fe19-38bd-aab1-6ef2da5068c8 | -17.03228 | -56.7374 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d5f9349e-1163-36f6-8165-00a4b1429935 | -17.03168 | -56.81943 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 84bc52a3-f8e6-3fea-8616-4f9bf4df7544 | -17.02989 | -56.72836 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8c4dcb10-0fe7-3f8a-b294-d58c4d6922c6 | -17.02989 | -56.70225 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 216dc306-44ac-370c-b163-d0eb6b09cfd2 | -17.0293 | -56.7326 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d75c3150-7159-3d05-a74f-fcdcdefe702b | -17.0287 | -56.73685 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9864df94-2369-38fb-82b5-55a9ba2481fe | -17.02691 | -56.72355 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5cf60537-f775-3004-a04f-ddfe5ab41a52 | -17.02396 | -56.82253 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 60970991-3841-345c-a23c-904a9b62825f | -17.01975 | -56.72243 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c5ce1199-1957-30d9-ab6b-42d1230b288c | -17.01736 | -56.71336 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 547fdcc5-bd96-3d68-899b-431457831840 | -17.01684 | -56.82143 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c014caac-e619-3171-a65e-b847656d1d2b | -17.01617 | -56.72188 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 5b3058ce-5481-3c63-92db-e478ad8cce32 | -17.01197 | -56.69948 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 532b4c57-2e20-3f63-aca2-d6350ab170ce | -17.01141 | -56.72983 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 87f053e5-ee05-3d0d-b1f3-f3d9c417ea71 | -17.00842 | -56.72503 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| ffd9c614-ba69-33a7-9cb9-3cf8f68c667f | -17.00783 | -56.72928 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 0ddbd4fc-dd2c-3a1b-a345-ce21083533b1 | -17.00615 | -56.81977 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 1fb8ce29-142b-3f68-a713-0e46143dfb71 | -17.00259 | -56.81922 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d0a64d2f-dfc2-33bf-8664-ad1f4ebdfbf4 | -17.002 | -56.82343 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 42e499f4-0696-3f21-ae28-417056251f4d | -17.00096 | -56.73454 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 4c7a0aeb-b3c8-3cec-83ef-53d33f6589a0 | -17.00068 | -56.72817 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 4c26c6e5-e24b-3626-a7c4-d5b1180ff8b0 | -17.00009 | -56.73242 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 30e843d6-6d38-3849-a8fb-27614773cbde | -16.99903 | -56.81867 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 0abf1481-bfe5-315e-a191-0dae5af28d4a | -16.998 | -56.72974 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| bce6e932-a125-3439-8772-e6acb23eb585 | -16.99651 | -56.73186 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 309f15ba-3b60-3979-9352-a97ddeaf8485 | -16.99605 | -56.81391 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0fa65af3-446b-3670-8e26-913640236e56 | -16.99572 | -56.69464 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ee3d487f-eade-3478-ac3f-a852f92c1bbe | -16.99546 | -56.81812 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| b4e35a3c-e0bb-3690-af6f-23ca4380d5e5 | -16.99483 | -56.79649 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| eba2fa5c-1707-3c24-87b9-b41ac43f5665 | -16.99381 | -56.73343 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2b9942be-d673-3446-9994-623c06f1cce4 | -16.99121 | -56.80217 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c17269b1-7ca0-3bd6-b103-b08038609039 | -16.9906 | -56.80638 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ad6572db-4db8-3960-a6a1-c9c9e58f6fc7 | -16.98963 | -56.73712 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8c8bea5a-a1ba-3275-9135-13fe23b5c126 | -16.98902 | -56.74136 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9bb4f482-a8fe-3207-aa12-b6385369c4fa | -16.98892 | -56.8128 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 3e53202e-37e3-3b98-adab-87b324c38071 | -16.98765 | -56.80162 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6a6203d3-b369-3a84-b0b4-d6050e9a1f3a | -16.98704 | -56.80582 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9788f55b-4ba9-3fe4-a12c-a23e8d514762 | -16.98643 | -56.81003 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 927c40c4-22c5-391a-b380-76cdade37fac | -16.98598 | -56.76253 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 174c817a-bd09-3dd4-8560-337e285ea75a | -16.98594 | -56.80804 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |


[Clique aqui para ver as próximas entradas](README124.md)
