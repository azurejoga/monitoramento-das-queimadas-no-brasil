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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 722ef95a-0647-3b26-98ce-b4c53d7dbb61 | -2.85499 | -51.58633 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2b5ed09-4c89-3fb1-9b49-7e2e0fd08ef3 | -2.37008 | -53.67737 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f61520ae-649b-3f18-be2e-7bc6b240b6ac | -2.58986 | -51.71333 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 319db74d-408c-3dff-9c4d-916d1b30d2f9 | -4.55095 | -48.0271 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1d88cd5-4360-337d-826d-01125c158e38 | -2.60576 | -51.79253 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1946e3bd-0070-365d-a39e-6eadffe02acc | -1.62471 | -55.14124 | 2024-11-19 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 233803e1-fd0b-3353-9b3b-1a235967d4a7 | -0.84771 | -51.85766 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c529c3c9-7625-3752-b025-485cfe72170a | -1.79821 | -53.85619 | 2024-11-19 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81f813b7-93aa-399b-9e6a-d35f512b782a | -2.26342 | -51.88672 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22aadd6c-c904-3b26-a9d6-8e8b6252b26a | -3.6704 | -54.65535 | 2024-11-19 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8b1660d-0a86-33d0-9dfc-a2e50a3b27c5 | -0.85462 | -51.8635 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf5477c9-2f39-37d0-8fb0-39b5844acace | -3.70523 | -51.83024 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5478eb66-5786-37a0-9074-ba3b5d0fbaaf | -2.68704 | -51.8067 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f8697a6-26de-3014-b3bc-5717ddd75683 | -1.24998 | -51.61546 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87738d7e-4b87-3ad8-98a6-20ee0f5c74b0 | -4.579 | -48.0183 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 648733d5-9b10-3789-bba3-ba9ba69ad593 | -2.82404 | -54.00672 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dffee11-28df-3136-ae0f-18a2a934de38 | -4.55852 | -48.01216 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ea6558f0-d3ba-35d5-a247-7dd612c1f5a0 | -2.77165 | -52.60202 | 2024-11-19 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 98d2b8d2-4e74-32a8-b100-7a61c0134c87 | -3.31324 | -54.17335 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9c5523ee-76fd-3d59-950d-a963cba460b0 | -3.60643 | -54.21256 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3918e4f-debe-33e7-baa2-f5457b3bd25c | -2.60989 | -54.53816 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 857c344e-9bd4-36e5-83cf-abd1c9c97108 | -4.38373 | -47.77655 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cee02835-9bce-307b-a2fb-cae0afca07ef | -3.50458 | -54.03438 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 022e19e2-a9a2-3bbf-95f8-1f8690d5f343 | -1.97375 | -52.1524 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb73180c-b588-33d1-8b55-8782105465a1 | -2.60654 | -51.78754 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0115e55-3d1b-3c46-a0a2-b1f0312d1ca4 | -3.17194 | -54.69397 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc6d6747-c817-3cd9-a4a2-1cbaacf2526c | -3.31369 | -54.07899 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9140cadc-b53f-3d00-b3ba-bf492ed6d44e | -3.10493 | -53.75096 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0ae4cce-931f-3721-b640-1b43098125c8 | -3.14506 | -52.98108 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35fb12ef-2515-30dc-9fda-56cdcce9afc9 | -2.80334 | -54.18757 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de6133c8-266d-3136-a37b-e7a7f4d1dd38 | -1.49621 | -51.14033 | 2024-11-19 05:08:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c97025ae-8d70-366b-b6f2-265332992428 | -2.00083 | -45.34658 | 2024-11-19 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eca35791-0a10-314e-b08c-ddbeca4d2ee8 | -2.7917 | -54.06956 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d938a287-091e-3a56-bd70-5f92ccc78103 | -4.55327 | -48.01139 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0d8a2305-453b-320c-9dd1-b2176f428300 | -2.60049 | -51.79345 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b07ac8e-7106-323b-93b1-6d26d8c77870 | -3.5815 | -53.7254 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc258cb2-a583-3a47-90f3-63a994d9d43f | -0.00282 | -51.22943 | 2024-11-19 05:08:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c6a3056-56a0-310a-9dab-e028575cc055 | -2.90337 | -53.04922 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4fab8ec-58fc-38f6-8661-d73393f10e91 | -3.36371 | -54.10533 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| efa4d19e-2dba-39ae-9752-d0abe3c8d4e4 | -3.00883 | -51.44562 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 622aa259-2999-3015-9e02-4b8e47e89714 | -1.20381 | -51.76192 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15677241-936e-3f69-b103-ae24179bf2cb | -0.95328 | -51.72104 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3599e298-36ea-3384-ae89-f2edf754d8cf | -0.94482 | -51.72461 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ada639fd-0ee3-32af-826f-2e6c6629eaa2 | -2.6904 | -51.88829 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 627fd4de-9065-3424-85f7-b14b2cc8f955 | -3.71565 | -51.84231 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f7ed4f8-9dce-3bbc-b7c8-0966f4421403 | -4.18663 | -48.56222 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c8f117e-6d46-3323-b5ee-d46fda724125 | -3.05101 | -51.33162 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32e5bea8-56bc-32ff-b0f9-f31c340b2980 | -1.20767 | -51.76251 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9628678c-f61a-3352-bd7b-05d2835e00eb | -1.85361 | -47.82991 | 2024-11-19 05:08:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66b31be9-6ec2-3315-bacb-a14c65d33ea0 | -2.58662 | -47.47575 | 2024-11-19 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b41d1d80-ef53-3ec8-a992-9115e97fec64 | -1.41587 | -52.4384 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| cfb228e2-5f31-311c-85a8-cf2ff416c556 | -0.93189 | -52.50135 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79a6552e-724d-3249-ae47-83f468d319f7 | -3.82443 | -52.26128 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d08c8e58-ed7a-3407-a828-03c5278ecb1d | -3.72056 | -52.44783 | 2024-11-19 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9253bfd-930c-3c24-b39b-e7ed123a84cd | -3.99367 | -49.91415 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a112b5f-1d79-36cc-a5bd-a0f7d826c088 | -2.31905 | -45.64645 | 2024-11-19 05:08:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b6c8ca7-d5db-3303-afd1-5a2e3ecc04dc | -3.19795 | -54.3197 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbe55ea5-4676-3557-a76d-3a9411ff7480 | -0.84601 | -48.74522 | 2024-11-19 05:08:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 55c83cc4-2664-3319-935d-6ae249403baa | -0.04616 | -51.74559 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb3110dd-203f-3901-a346-48f8cfa352dd | -1.83674 | -46.28094 | 2024-11-19 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aefd572-298f-31ae-ac69-8e442f734be3 | -4.0638 | -54.05194 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49c406e0-a449-35b1-bb04-189bbeb003d5 | -3.23202 | -53.62602 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24fd2a3e-3bc8-31fb-a43c-d58bcf8c73b0 | -3.80833 | -52.39643 | 2024-11-19 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b94b40bd-af35-368a-a9c0-b23b9a288325 | -1.41657 | -52.434 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 3ad018e6-8afd-3829-8dc6-61cdef8fa2b4 | -2.14103 | -53.64348 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 489c15eb-156a-3e71-94ad-454c1ff02f24 | -1.20434 | -51.77466 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2efacda-1304-3901-9a5f-023288f27cb3 | -3.03989 | -54.40036 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4eabbab0-d61a-3e68-897e-e5d5dc2c735c | -4.39047 | -47.77787 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24242f8e-0b0f-3016-bf02-be1deb98a734 | -1.57982 | -53.80026 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7e7a5ce-08a7-381b-ab02-e17c306e7369 | -1.34388 | -55.44062 | 2024-11-19 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d65e0a73-60df-3fa7-ae96-73c6dead9a07 | -4.38275 | -47.75675 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4f43f56-2c76-3292-98b6-3a7453ce3bb3 | -3.23559 | -53.62655 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa16823a-3f5c-3ed3-860d-8f0e5a3046fd | -1.99479 | -45.34573 | 2024-11-19 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef438a00-6d96-34a3-b60d-24964a3ed490 | -3.04311 | -49.46687 | 2024-11-19 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8caa35a5-4074-30f5-82c8-21c690194d11 | -4.38564 | -47.77384 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 588f0ee6-5e2e-30d3-b9e6-4647df4ce7d5 | -3.1855 | -54.31842 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 570bff50-fa23-3f28-9fa3-781054425e81 | -1.95239 | -53.00819 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 407a162b-a1d6-38cc-9185-3add5f161c63 | -2.74945 | -54.01967 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6257825-e770-3f86-add5-28e2fb808112 | -1.41134 | -54.92382 | 2024-11-19 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1baa73db-ae54-3285-b0c2-c7ce315ebfbc | -2.80682 | -54.1881 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11e68545-cb31-3439-b3f4-5edb1b41eb44 | -3.10435 | -53.09846 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1904f47-07d1-3eed-8eba-1f2ce0256598 | -4.39531 | -47.77145 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af9f1b07-d059-3d58-a94e-ebc313a73aba | -2.8648 | -51.791 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eaee3469-b451-3778-abb5-2b53679487d9 | -1.37573 | -52.07653 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eba3de5c-e115-3676-b140-1aba880327a5 | -2.21019 | -53.7102 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4658afd-4276-3e55-9677-0a49bb1b1bf4 | -1.62984 | -52.40416 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4094da5f-d283-3bfc-bad8-295bccf1b3d1 | -2.38666 | -53.66383 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1cb4940-1dd2-3a1b-aef9-38ed978620b5 | -2.76788 | -52.60154 | 2024-11-19 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3057df78-54b4-378a-bb71-02765933de6c | -2.38251 | -53.66721 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9305508b-9c90-33c6-a851-d7e1f2d048a7 | -1.26849 | -52.1261 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eefdd11d-1f16-344b-bbb8-55da07937bf6 | -4.55667 | -48.02462 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 50c9ca60-caac-3ede-ad17-cd304f69a953 | -1.42402 | -52.43514 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad86b203-5bce-3a71-981f-9a6c4d26f3d1 | -3.04965 | -54.4057 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77bf5653-d57e-3b3b-aae1-e3102cc6f510 | -2.72161 | -51.8138 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe67c874-8872-3d5b-bb1c-5c9b3c2fb190 | -3.74718 | -54.71978 | 2024-11-19 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc75bbc3-4036-3aa0-b906-14e44b472487 | 0.38611 | -50.86063 | 2024-11-19 05:08:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98b2a7c5-e1d1-3dc7-b6ed-812774f9f456 | -4.57854 | -48.02158 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3aa2073b-6d52-3382-ac2e-8af39f77af7f | -2.74466 | -54.05053 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10141097-99e6-3c2d-b8fe-61fe2e5b7c68 | -4.99207 | -44.33158 | 2024-11-19 05:08:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee66be9a-6a75-38c8-b198-96d92fe996be | -3.49919 | -54.74331 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README41.md)
