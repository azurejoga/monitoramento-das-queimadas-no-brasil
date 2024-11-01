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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f9b6bb2-b00e-3615-9f0c-d742e3e9e30e | -4.96532 | -49.77749 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d1dda08-9f95-3604-b005-bdfe04a32671 | -4.96471 | -49.78127 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32c82d57-6f53-3340-825f-aaff75f82e85 | -4.42878 | -49.84388 | 2024-11-01 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1abb3d94-3291-3d27-883b-9c41fa021cdd | -5.11945 | -49.66992 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc7e9844-40de-38d9-bc34-49a5ee7182e5 | -5.11885 | -49.67368 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58e8c328-c299-3116-bca6-ca8ce5880481 | -5.09756 | -49.82927 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ea2a150-2514-3c28-8eb7-a535afff3d1f | -5.09349 | -49.83251 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23fc7ba2-3307-383b-bf55-466d13424b03 | -5.52478 | -49.59166 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd1cde01-f32b-36da-b5af-050aec4d943d | -5.51216 | -50.02249 | 2024-11-01 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e004cd31-8199-3779-b2a2-18685cf36d57 | -5.30333 | -49.50747 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 164ccfa9-f679-39f6-a12e-77c93406fe35 | -5.29992 | -49.50691 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dea3f1f8-feda-3641-959d-2e90867e313d | -5.17356 | -49.85684 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53af1442-d35e-3f8d-9df6-d481fcae0467 | -5.1701 | -49.85629 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd5a5969-d1c6-3ed7-b011-0bb1e1e3408c | 0.36749 | -51.135 | 2024-11-01 04:29:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5eeb8f47-3ddc-3961-bb64-14e57bb0a83a | 0.32883 | -50.81442 | 2024-11-01 04:29:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 382600b2-a77d-39a3-bd88-f9f5ee2330a3 | 0.06648 | -51.11382 | 2024-11-01 04:29:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4ceaf27-1d1c-3238-ab0a-03063fb0a4aa | -2.2435 | -50.53207 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f88dbc1f-20e6-3d9b-9628-018448741468 | -2.23981 | -50.53148 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 983d31bf-8755-3bf5-b1f6-465850848b64 | -2.23966 | -50.43814 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d014ebdf-0157-3335-a08c-77eaa11ee818 | -2.23599 | -50.43756 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2c0288dc-7d48-357d-babe-21ff8fad5746 | -1.50158 | -51.07649 | 2024-11-01 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32030469-0f24-354f-bc32-2cd71715db5d | -1.36281 | -51.41846 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 939ca777-d670-3e6d-a5ae-c84c3af636ef | -2.22069 | -50.72296 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d022e333-cc6d-347a-a6fa-8425f77f4695 | -2.20495 | -50.82185 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8072af84-0b5a-3f98-ad41-821163deb235 | -2.16325 | -50.73844 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e61cd43-ef39-3809-a234-b846fe80daec | -2.14162 | -50.99963 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c738c297-f7c2-3862-8817-48b131761dcf | -2.09448 | -51.09742 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e36bdf9-3f56-3ba9-a9fe-e35c868111ba | -1.9395 | -50.8584 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 864094b6-ca9f-375e-a5e6-c524dcfa10f2 | -1.92676 | -50.88925 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e682f10-b786-33c0-ade1-862d4f4c09dd | -2.16255 | -50.74291 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cb8ab8b-f816-3e35-b7ef-c6f731f3d285 | -2.15615 | -50.81412 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bccfca4-0948-3459-815e-f9fc5ebcb834 | -2.11768 | -50.83298 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24890f1a-d7b7-3225-bb66-6f33a296f6b3 | -2.11697 | -50.83752 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9b1fe5b-bcd8-398c-98cd-ad075aea232f | -2.09597 | -51.09491 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| faaa69aa-f5e3-31b0-b766-19669cc9d203 | -1.81008 | -50.96272 | 2024-11-01 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2075a825-7ef7-31f2-8999-f03f4445f6ef | -2.88366 | -51.65391 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7902ab72-75a1-3221-8c24-89bf34d913fe | -2.88351 | -51.65638 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06950d2c-5717-3c8e-8d42-8cde28ce3e9d | -2.88288 | -51.65887 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63802818-4d3e-36df-9b16-7855c521aeb2 | -2.8827 | -51.66132 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c083a80-4f8d-3980-8044-a053acb3080c | -2.87868 | -51.31069 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac54c95e-b9c7-32a3-b98d-c054b3cb37e7 | -2.87792 | -51.31541 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e200909-43a5-3699-9783-51af6a5f230e | -2.87486 | -51.31007 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d5ee7fe-ee16-3bbe-bf6c-3fb826487a3f | -2.87409 | -51.31481 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24b0a617-164c-390b-8b16-522c49fc1b34 | -2.87103 | -51.30946 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91d5284c-2f70-3615-a2f3-6924b654b535 | -2.85455 | -51.7621 | 2024-11-01 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9e19a3f-c726-3dfd-94ee-356b880f6c9c | -2.85363 | -51.76437 | 2024-11-01 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa57880f-7e96-37b2-b9c0-6178792a685a | -2.83158 | -51.80489 | 2024-11-01 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2e5d539-ccee-3885-a427-8549252fd191 | -2.83078 | -51.80994 | 2024-11-01 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cff2a170-3830-3214-810e-981579a4b55b | -2.82763 | -51.80425 | 2024-11-01 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91f792e0-79b8-338b-a197-5e8ba1c7064f | -2.82683 | -51.8093 | 2024-11-01 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 05c80488-e875-3236-9f17-d06d73690e96 | -2.82627 | -51.03395 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce97f154-44b0-36d5-85fe-6cf38430d8d9 | -2.82553 | -51.03857 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8f1ff0a-935f-341c-9705-aaf2451e7d75 | -2.81571 | -51.60264 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83dc8043-c05c-3bba-ae1d-27b5d16b7e2b | -2.79402 | -51.35909 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc988268-f97c-3dd0-835c-3984839315ce | -2.2786 | -51.13869 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86f85ad7-8add-3a7c-aeef-44d2cbc68551 | -2.26126 | -50.68379 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 389d5469-16aa-3f95-9d8a-0148cc168e7b | -2.25754 | -50.68319 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d15a1956-82b5-3c9b-a43b-5bbbe07bd7d0 | -2.25684 | -50.68764 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27415a96-018b-3af2-9590-616fc36a635e | -2.2487 | -50.69088 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8d2cbce-15c0-3987-90fd-0041fefc89b9 | -2.23561 | -50.7254 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4c85387-33b3-3edd-8dd7-e022e50a1621 | -3.04577 | -51.40092 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f22274b6-965f-384e-997f-efcb42c14e58 | -3.04498 | -51.4058 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 612405c0-60df-3975-89d2-4cb68d3bf87a | -3.02941 | -51.36683 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37c01af1-7364-3fd3-90de-114b2a4f9b1a | -3.02529 | -51.09859 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2f79402-eda9-3045-b1e6-67c25d8d015f | -3.02433 | -51.44915 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f052e2c4-2de8-3cde-ba57-e923fc811463 | -3.02359 | -51.45389 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b28447a4-07b8-394b-9790-fe18055cd099 | -3.02258 | -51.4461 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b90cabc7-159e-3843-a379-e9cccb5bc7fb | -3.0218 | -51.45084 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a536e660-8f65-3e01-8ca6-99b4641531e3 | -3.00223 | -51.21789 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 268e3c06-2cb8-3025-834f-55df1a03cfe3 | -2.98635 | -51.26802 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15478fa4-8e8e-39cc-b2c9-5f1a0c38831c | -2.95438 | -51.05605 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cb51966-18c4-3eb2-ae39-cfcb51deef62 | -2.95061 | -51.05543 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dfbfa9e-3c9b-3135-aad5-834d6b4a342d | -2.89999 | -51.48346 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 84f8fdff-f6a6-3de9-a59e-c4601741b44d | -2.89821 | -51.48551 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fbac66d2-10c3-3359-a593-2d4a71c404c5 | -2.74281 | -51.73264 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28fa0101-853a-3aec-b698-1b7b2248f127 | -2.74202 | -51.73764 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ec40d68-dffd-37bd-a5fe-392dce7d909b | -2.73888 | -51.73195 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96314228-fbdc-30a8-b2cd-252222032103 | -2.73808 | -51.73698 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21d7ae9b-c548-3fb0-a220-b063d422d6dd | -2.73494 | -51.73131 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d68b8576-c09b-35d7-832b-baca6bfac7f9 | -2.73398 | -51.83096 | 2024-11-01 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae96e8be-1b5e-33f8-93fb-43d9238ff0fb | -2.7318 | -51.72567 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7c8bd47-9f79-3d51-843e-fc5238dfac1e | -2.731 | -51.73069 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c0c0a96-ea2f-3ff0-8847-4f6dda7aee87 | -2.72238 | -51.70879 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e35f9ec6-0e18-3fa3-9648-2c3b58bee694 | -2.64677 | -51.75632 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 909c479a-bf0d-3cbc-98ee-ea1124c8fb7c | -2.64641 | -51.75341 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2254c486-9168-3f3f-9f04-ff991a001268 | -2.64558 | -51.75847 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfdaf913-71ba-345a-95f9-79b1af971130 | -2.64362 | -51.75061 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ada1c43-d5c4-32fe-ab9e-fbe2ba3f760c | -2.6433 | -51.74772 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb8e3863-12c2-391a-a3ab-cc3f42d913db | -2.64247 | -51.75277 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52bb940e-efea-31ad-98fd-d9ac483b3eb7 | -2.64101 | -51.737 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9454e124-e606-3d31-9e35-660d31f84ae2 | -2.63967 | -51.74996 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11d6ba75-aba4-3539-aa5b-65a5f0637c77 | -2.63935 | -51.74709 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2beb2f5-c50a-391a-b5a5-7e53011007da | -2.63811 | -51.73418 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e58de9ef-6cef-3678-a85b-4fe3d0f02bc4 | -2.58409 | -51.92073 | 2024-11-01 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb36f088-c4be-3448-9f46-cbb1eb0613ff | -2.58353 | -51.92421 | 2024-11-01 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8807fdd4-b7c6-3094-84dc-fb7055d48136 | -2.57953 | -51.92359 | 2024-11-01 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a7699a1-52f0-336c-90be-c6ab45f33f76 | -2.56868 | -50.65409 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 250b2bbf-4701-3c7c-b8db-292085a8440f | -2.56498 | -50.65348 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49efef6a-9319-382a-8411-772454c72a97 | -2.56281 | -50.73909 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98508338-5738-3a86-ab14-bee55e89ca58 | -2.55771 | -51.23362 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README39.md)
