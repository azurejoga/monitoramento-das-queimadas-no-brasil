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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d991cab1-7303-3166-8897-62f07936ab0e | -18.22291 | -56.33294 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 60ca453d-135a-3dcc-af6b-6c02fb17ea0e | -18.22176 | -56.34083 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 47b7fa7d-e449-3012-8137-7f8f75e85092 | -18.21717 | -56.34815 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b8ce6e5b-4b3b-361a-a71e-d8289ff6ac87 | -18.21659 | -56.35209 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 78747337-c2d0-376e-b188-991ada1a8393 | -18.20226 | -56.37796 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e88b365e-2904-3379-a016-f358169cc29c | -18.20169 | -56.38188 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6780c4e2-1fe7-3647-9110-b02b70c74260 | -18.0703 | -56.44207 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| dae6a867-0125-3629-b840-8431b400936c | -18.06745 | -56.43762 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 26d21ce4-aebc-3135-8c38-64153167aa5a | -18.06226 | -56.40082 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2bc7610f-bc56-3744-a62b-020d6351661d | -19.62211 | -56.96378 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9a0e3a69-7c74-37b6-b0ef-218d33addbff | -19.62155 | -56.96766 | 2024-10-17 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 664c5daf-f0be-3f96-a750-26f7542953fe | -19.62097 | -56.94764 | 2024-10-17 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7a2e4a96-9598-3750-957a-a5258e47f161 | -19.6187 | -56.96321 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bcfac044-6850-39ee-8587-19983f91098f | -19.61303 | -56.97822 | 2024-10-17 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5981a042-e831-3c40-98c6-95120f9cce7e | -19.60792 | -56.98932 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 37d2d43b-19b5-310b-9b33-7bb69f8fcbba | -19.55395 | -56.9498 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b0fae4f1-7e35-35b8-a3f8-993e0c7aefcc | -19.55338 | -56.95368 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d938e676-52b1-34e6-9405-19d5153d9f9a | -19.54656 | -56.95258 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6fc12755-08cc-3649-a93e-30d70745e73e | -20.81134 | -56.58204 | 2024-10-17 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4929c5c-5509-3214-b18f-efd99cd3bcd3 | -20.80786 | -56.58144 | 2024-10-17 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66c9bd40-20fb-377c-8f79-7c434fb5cef3 | -20.80547 | -56.59816 | 2024-10-17 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1438236b-c022-3b76-8a23-f5ed65e88b8e | -17.83667 | -57.46662 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 5cd6d09b-f303-3748-9534-da2eadb29307 | -14.97823 | -57.61691 | 2024-10-17 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7a49154-dffc-31d9-b12c-5df04a7c81d4 | -14.97604 | -57.60926 | 2024-10-17 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a700763-590c-3318-935a-a66779cc5f91 | -14.87599 | -57.48742 | 2024-10-17 05:08:00 | NOAA-21 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8ad62c36-bdb2-3725-bf33-031bec98acbb | -14.86387 | -57.47814 | 2024-10-17 05:08:00 | NOAA-21 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e7b9544-6776-34ca-9850-3857fec176a9 | -16.31568 | -57.05506 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c8f52933-347d-3cae-8770-ad8547933bd9 | -16.06839 | -56.98569 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ffcf3b8-6eb6-3643-ad38-fd060ebd9c4b | -16.06783 | -56.98933 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8d0c49d-bfe9-33fa-b1d4-67285f55cc82 | -15.72379 | -57.56833 | 2024-10-17 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66cbc588-4b76-3746-a6ba-46f7232ef2f3 | -15.65342 | -57.67035 | 2024-10-17 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7fd82ef9-d813-3b9e-97a1-1e24934133c7 | -15.65286 | -57.67392 | 2024-10-17 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4e500d73-88fb-3559-bc93-25dc95eb91f6 | -17.86835 | -57.46057 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| c4f71cee-a6d2-30bf-86db-a715b96cf7b6 | -17.85779 | -57.46259 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 95ef1439-491f-3e67-9215-3220ed5d8ef7 | -17.85723 | -57.46627 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 7f5ca40c-797a-3193-859c-fc784950fa61 | -17.8539 | -57.46571 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| e137f2c2-ca97-334e-980f-12e2fe10dfdb | -17.85001 | -57.46883 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0212f274-1cd8-3e28-84b6-2fd28c4b95be | -17.84667 | -57.46828 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 642fe58f-fbf3-376e-86d9-eb89edd87e75 | -17.84611 | -57.47194 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d32fcf09-cc52-3083-9384-404ca4fc5701 | -17.84334 | -57.46772 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 73305fed-ebcd-3918-a794-40bad5a7f1e4 | -17.84278 | -57.47139 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 09d4119d-aabe-3912-b897-f8a35e535195 | -17.84056 | -57.4635 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 381cf599-1e24-3c7c-8a00-6c679d3bb65e | -17.84001 | -57.46717 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 69a31e03-15ba-3f7b-80c5-a5897a38a6b7 | -17.8339 | -57.46239 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 901dfcee-8a44-3051-a799-6c485a9740f8 | -17.83334 | -57.46606 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| bfe79ffa-87f8-370c-8ed9-37bf4a373dbe | -17.83001 | -57.46552 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6dd95c68-12a8-3d29-b41b-64432eef5df5 | -17.81945 | -57.46753 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 3e81096d-20a8-336c-943a-d03e5af9f04d | -17.81889 | -57.47119 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1e3b3a76-23ca-300a-9d08-75530807f508 | -17.81611 | -57.46697 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 7aad0a71-57e6-35d2-aafe-d804a241d49b | -17.81556 | -57.47064 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 55ab9fd8-829f-3b01-bf3c-374d37d84873 | -17.81334 | -57.46275 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 38f6c448-b32d-3552-b8c7-c705281fc74e | -17.81278 | -57.46642 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 6b0f7373-b0be-367c-8731-c28fd9677fe6 | -17.81223 | -57.47009 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d72dca20-62a5-3065-b01c-b013af693c65 | -17.81001 | -57.4622 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| d918656c-866a-3ce8-9715-929995b1af1d | -17.8 | -57.46054 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 83e4b4d8-1895-3f73-b969-f2a67087fe2b | -17.1917 | -57.48485 | 2024-10-17 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cdf3e2ad-b55c-3602-9186-d99578ec5131 | -17.18837 | -57.4843 | 2024-10-17 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e77e3ff6-bb32-387b-ab3f-3303299464be | -18.00415 | -57.3049 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a409aed4-b79f-3142-9541-d375b7245c17 | -17.97949 | -57.42198 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 582796a4-6e80-3a4a-b22e-6f919efe4346 | -17.97893 | -57.42567 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c9246326-520b-362a-826a-dbf5710cfe31 | -17.97615 | -57.42143 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6fe9d8f7-b43f-3880-9063-987d512c8481 | -17.97559 | -57.42512 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c863d98c-db1c-36a5-9a03-aea7130366b3 | -17.9589 | -57.42235 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c80ce5b6-74eb-390d-be8b-1217c2d5a2fd | -17.95888 | -57.44499 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 36f400e8-8b1d-3a7a-ae7c-fba57489eab1 | -17.95832 | -57.44867 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 048fd576-36be-3d96-94c5-d7f621200f90 | -17.94554 | -57.44277 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5505f495-e64a-37e8-888b-209afd70c1de | -17.94498 | -57.44645 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| aea7cd76-27e0-3b74-988e-bebd8270d608 | -17.94164 | -57.4459 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f46bb4ab-1b6f-3e2a-820e-4b7495f91346 | -17.94109 | -57.44959 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2750f05a-e3cd-3f4c-b2f2-bd4829df7c45 | -17.93831 | -57.44535 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 8839a525-e3b0-3430-995a-9b9a3ac0842f | -17.93775 | -57.44904 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9b5d16c0-207a-3d16-a32a-3d5ef1477374 | -17.93553 | -57.44112 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 428cce01-93a3-37af-bb49-3fa063561048 | -17.93441 | -57.44848 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| df20fab9-d880-3296-a8e3-ce6484ce838c | -17.93163 | -57.44425 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fb6a5543-c100-393b-91dc-b8a9f849c34d | -17.93109 | -57.42529 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 806f9fcd-9d3b-3fc7-bfd5-a7b7820ac35f | -17.92997 | -57.43265 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 52af6fc8-c583-37e7-afb1-64fd715cb80d | -17.92941 | -57.43633 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 131407cb-9ba0-3b87-91ef-2950e53e28e7 | -17.92886 | -57.44001 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 00432648-d1ae-3c38-b32c-fcfa160ad695 | -17.9283 | -57.4437 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a5f400c8-886f-3053-b066-2da1ce97faa0 | -17.92719 | -57.42841 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 28aeaf0b-724f-3498-ad07-6de6c1aff71a | -17.92664 | -57.43209 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6a9a3746-d9e2-3ae7-b977-356f43bcd21b | -17.92608 | -57.43578 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c025c7a6-4f36-3759-bdf8-f2dd7badb422 | -17.92552 | -57.43946 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| dec61156-8afb-351b-a641-7eeae941016c | -17.92274 | -57.43523 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3b95d4db-2bec-397f-bfba-bf6edb13c67b | -17.92218 | -57.43891 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fe0e2773-199c-30e1-8366-15645c1441d3 | -17.92163 | -57.44259 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c9ad9936-895f-3f25-8782-84c59e0d92b1 | -17.91885 | -57.43835 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ad31bc6a-e2c7-3055-ba80-94dbe1370c93 | -17.91881 | -57.25665 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cac2c6a9-fb2f-3ff0-bd2c-2dc15956b650 | -17.91773 | -57.44572 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 00a540dd-2328-3fcc-9d58-e12416c450c4 | -17.9144 | -57.44516 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 850f4034-6253-3879-b70e-890dcb1a62e1 | -17.17443 | -56.81399 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d3a65f76-11b9-3d9b-9a49-738b1f947fdc | -17.17387 | -56.81773 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d2508417-d82f-3330-9d27-582dc3a30fa1 | -17.17218 | -56.80596 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6f80fad9-9a0a-38d1-bb93-eea629dcc309 | -17.17162 | -56.8097 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f7515f72-a818-3597-96a8-da51bb4f6edc | -17.17106 | -56.81344 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0bf31199-b5c3-3cd9-bb22-d0ccd8f13e25 | -17.1705 | -56.84014 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9e08a26b-9201-3e78-a8d8-30bfdff8ad16 | -17.1705 | -56.81718 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e577dcc6-2149-323b-8db2-0a04ce29ab2c | -17.16994 | -56.84388 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 140652bf-e9bc-37a6-aeaf-7b16763b9c21 | -17.16994 | -56.82092 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| eecf4140-49ff-39a2-a035-8fdd0a0c672e | -17.16881 | -56.80542 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |


[Clique aqui para ver as próximas entradas](README48.md)
