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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e582156b-e953-3800-b027-748e2cd6c587 | -18.39388 | -49.31471 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7d62b35-0d61-3e21-829d-4f7d6bd4506a | -18.39162 | -49.30666 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 019b88db-fc39-34ad-b38b-0e20454ad9de | -18.39101 | -49.31085 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55798229-b573-326c-82b6-7d48f7297dd4 | -18.39093 | -49.30987 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 048191f0-ed11-333c-b516-74955a574310 | -18.07978 | -50.26808 | 2024-09-27 04:42:00 | NOAA-21 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d82d97d-e47c-3d24-ab39-f6703ad4f0e8 | -18.81804 | -49.83721 | 2024-09-27 04:42:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1a11a7da-12cc-36f2-951f-a05011d51495 | -18.71787 | -50.54803 | 2024-09-27 04:42:00 | NOAA-21 | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| aed5f171-d763-3667-a8eb-e671749eac55 | -18.71731 | -50.55186 | 2024-09-27 04:42:00 | NOAA-21 | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 736045a5-fc44-32d2-a231-a77ea52ef7f2 | -16.11008 | -51.95077 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2cdb8f4f-dc51-3eaf-a4c9-e56dacb2ddad | -14.93929 | -51.45812 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 61ffe1d5-f9ea-3e8d-8983-0973b3a93070 | -13.57401 | -50.70386 | 2024-09-27 04:42:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b418f547-d231-37d0-bd79-b652d179763f | -13.57125 | -50.69979 | 2024-09-27 04:42:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef7ad95b-5aa5-3f7e-9e44-5cf4dcc29503 | -13.5707 | -50.70332 | 2024-09-27 04:42:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd03ae32-1319-3ae4-be4a-a8020d75e770 | -13.56961 | -50.71039 | 2024-09-27 04:42:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec61107f-c180-34d7-b25d-76c4b4ef4d45 | -14.95251 | -51.46031 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| d3623563-40d4-37e3-b103-f21570cdb350 | -14.9492 | -51.45977 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| e5ce954b-11b7-3bc3-b60f-da1d32746b29 | -14.94864 | -51.46331 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ccc1ca8a-e65c-39ee-8d9a-91ad6050198a | -14.9459 | -51.45922 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 81430e37-3dfe-34fd-824c-779471e417a1 | -14.94534 | -51.46277 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecd170d9-4475-3dd4-9020-cbdbe8f58bb5 | -14.94478 | -51.46632 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1eec88b-9bc6-3f00-8fc3-c1543d97a8ac | -14.9426 | -51.45867 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| b7c845f5-9bc6-3a70-9992-f9d32e561c73 | -14.94204 | -51.46222 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 521e4064-88ec-32c9-9b2a-278d8e500834 | -14.93873 | -51.46167 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 717f753d-f5de-3aea-8344-641cf9cddc9d | -14.93599 | -51.45757 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 6eeb90b1-27a9-3879-8a8f-976a52551552 | -14.93543 | -51.46112 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52b6d629-a2a6-33b8-abe9-0969e98fc14b | -14.93431 | -51.46822 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8109575e-8e1e-395f-a620-3c2cfb5c451e | -14.93213 | -51.46058 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66464c05-50dc-3fd8-8567-0e963bf56a9c | -14.91825 | -51.50563 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb91de3d-866c-3420-8528-db2e6e1ab5aa | -14.91495 | -51.50508 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01809763-5ad5-3b32-a537-48efe77dba08 | -14.90339 | -51.53249 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06c31190-0db4-360d-af3a-c4a38da14899 | -14.90009 | -51.53194 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00d28b07-2ba3-34ac-b587-21d94305a5ec | -14.89678 | -51.53139 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2dafcadd-61b3-3b72-8ff8-9c8b4fbb93ca | -14.87986 | -51.46665 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5672e556-8b95-37cd-b553-9b59954e7f23 | -14.87366 | -51.52754 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b69455a5-554f-38c3-9aa4-196a3c02e47d | -14.87035 | -51.52699 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cf29ca2-bc63-3f9a-b602-8bba620e6205 | -14.86995 | -51.465 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69067772-6b55-33e8-89f7-34eb16baa5ce | -14.86705 | -51.52644 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb604129-a167-31d7-a06c-7999dd77ade9 | -14.86486 | -51.5188 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1044e8d-a3cd-32a0-bbd0-93747287becb | -14.8643 | -51.52234 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 340b9f29-fb20-31fd-9485-519d51f1ad48 | -14.86374 | -51.52589 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ddba155b-da9e-3da6-9d7c-4db44e4e7945 | -14.86334 | -51.46391 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 588947e3-2b96-3c5b-bfd5-45c776be6a3d | -14.86278 | -51.46746 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1b3c1ce5-9def-31ba-9d2d-8b4eb5087510 | -14.86222 | -51.471 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 404257ec-dfb2-355e-90aa-9e704ab624c0 | -14.86004 | -51.46336 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 73ef1f66-9c11-342e-8da1-39ff0c8f15c5 | -14.85948 | -51.46691 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b769cc92-34dd-3ba1-8f82-174bd8c5c166 | -14.85892 | -51.47046 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 053cb971-f45e-3590-bcc6-e74f8157467d | -14.85836 | -51.474 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 460c73d5-2873-3423-975a-526fb95bc08a | -14.85673 | -51.46281 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| f51d48a0-c7de-3a30-934c-10fbad319c5f | -14.85618 | -51.46636 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| e45bd44c-d526-3306-b812-4b6721337250 | -16.12632 | -52.01962 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14bbdf1c-95d3-36fd-8617-2609d51ad1e1 | -14.85562 | -51.46991 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a2afe85-6102-3c80-b7d3-7ecc28d9f260 | -14.85506 | -51.47346 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed1a6784-1082-3cef-a18e-076838ea2ae7 | -14.85343 | -51.46226 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 85d6cbc2-9a08-32ac-bf58-c21ea3b06079 | -14.85287 | -51.46581 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| bf8db300-5db2-3bb8-96b6-b4b72ae1963e | -14.85231 | -51.46936 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86451711-91dd-3d98-a922-e346684c01a3 | -14.85013 | -51.46171 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| cb64c332-f628-3bb9-a107-ee971adbb075 | -14.84957 | -51.46526 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| f8f50292-6b00-3179-b6ad-784e96c2add8 | -14.84901 | -51.46881 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6779a91b-f4b8-303f-90f9-95d96bee1639 | -14.84682 | -51.46117 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 385c4796-c482-362f-a976-eb6df95ce409 | -14.84626 | -51.46471 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 1bf79f4a-f7f2-39e3-9115-99615e05271b | -14.84571 | -51.46826 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c694e128-10d4-3566-b8a4-f9972db26d0d | -14.84296 | -51.46416 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 325325af-e451-33ca-bd11-b4bd55ed7e21 | -14.8424 | -51.46771 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32e5577a-aa4d-3efb-a16e-36711610cea0 | -15.03772 | -51.21937 | 2024-09-27 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b511663d-7560-32fa-98c1-af11a443a94a | -15.03716 | -51.22292 | 2024-09-27 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f82d4ea-9820-3a4d-a9f4-3f8aafacfef4 | -15.03552 | -51.21172 | 2024-09-27 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cebabc6b-f829-3378-9154-e7b668fe3aef | -15.03275 | -51.22948 | 2024-09-27 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baf3d5d3-bdf8-345e-95f5-65a7babcd100 | -15.03222 | -51.21117 | 2024-09-27 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a83b28e0-bf17-33b1-be10-ffaa8d55d9ad | -14.94427 | -51.09856 | 2024-09-27 04:42:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8832f1e2-8399-34a7-a4c8-26d86607f1ed | -14.88809 | -51.08932 | 2024-09-27 04:42:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bf94e9f-a01e-3a17-bd28-ce1585663bf7 | -14.88534 | -51.08523 | 2024-09-27 04:42:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24324738-9327-3179-938a-8ae191439fd7 | -14.88479 | -51.08878 | 2024-09-27 04:42:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee321686-79df-3895-8425-a4661f352d0e | -14.88148 | -51.08823 | 2024-09-27 04:42:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73ef9c08-4c87-346a-a05d-731fef08d690 | -14.87818 | -51.0877 | 2024-09-27 04:42:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0eac6274-5932-3f1f-9895-b95c99cf81b9 | -14.95362 | -51.45321 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 92d8b5e1-f2e8-3f84-ad1a-661c048a8809 | -14.95306 | -51.45676 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 07471845-cf93-38ac-9d54-1087eec0853c | -14.95088 | -51.44911 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| eacf61ac-1860-3c07-a3f2-a26ed548e7c3 | -14.95032 | -51.45267 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bd37a2d0-5135-397b-b8f5-37bc24a45a6f | -14.94976 | -51.45621 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| c4af657e-49de-37d3-b783-74af4c28a2c1 | -14.94758 | -51.44856 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 016e7f07-6d10-3b20-b55d-fc8cf84329b6 | -14.94702 | -51.45211 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| db4db1c2-7f41-33be-8050-99a85dce8cb7 | -14.94646 | -51.45567 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 5b57a97a-bfeb-33ec-8f6f-3920150b6136 | -14.94483 | -51.44447 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f98923e9-aad8-3b1d-89ca-3bc78561326c | -14.94427 | -51.44802 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f527ddcf-62ff-397e-984f-c462359b243e | -14.94371 | -51.45157 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e59afe3e-50f0-3975-a313-cbfde9c57220 | -14.94315 | -51.45512 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 433f7df6-9716-30dd-8909-44f8bb7e9176 | -14.94097 | -51.44747 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 26eaf21a-333d-3f61-9bdb-55bac26aa28f | -14.94041 | -51.45102 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 3c1d3de0-c379-33a7-8135-5f280f1f86a7 | -14.93985 | -51.45457 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| d6dabb9e-29bc-3ab8-9890-4fded90713a2 | -14.93822 | -51.44337 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b78d04f-86f7-3f28-9f33-9575a5c52d33 | -14.93766 | -51.44692 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 62f089f6-3c04-3edd-8db1-6021f0d078d2 | -14.93711 | -51.45047 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| bb164b08-4f9e-3505-a695-1b34cf1a9546 | -14.93655 | -51.45402 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| af7fab80-b8e5-322f-a3c4-e53b670c4e09 | -14.93492 | -51.44282 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9126281-def5-39ae-b59b-58f8a4e51792 | -14.93436 | -51.44637 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.1 |
| bc6411c6-324f-30b1-b102-a798358a68fe | -14.9338 | -51.44992 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.1 |
| e6a256e5-81d8-338c-91a2-de804b837bf5 | -14.93325 | -51.45348 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 579276ca-62f7-3a13-a2cb-e4ea12d51816 | -14.93269 | -51.45702 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d79f3420-cebf-3dce-9ca2-8683d63fcfc7 | -14.93162 | -51.44227 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23689234-9c20-36f0-8eac-9334dafd21d7 | -14.93106 | -51.44582 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.1 |


[Clique aqui para ver as próximas entradas](README105.md)
