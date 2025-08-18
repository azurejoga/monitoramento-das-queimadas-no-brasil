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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f113bdd1-ca03-3342-868a-628cecd690bf | -15.00442 | -54.78629 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51b9d356-2d8b-3af9-a0fa-ac7e9609b52c | -13.21954 | -50.74677 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b9b0063-3f39-39fd-8ff8-a5862e6985f9 | -12.93195 | -46.11372 | 2025-08-18 04:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d70575da-93cd-33af-bb79-4b03c8dc0a92 | -12.61444 | -46.90052 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a8ffa84-c869-3e45-beda-bf1a4d9822c8 | -13.0206 | -56.85336 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dca1eb0-565f-3443-9e7d-5268e7eda9cb | -13.59336 | -46.96081 | 2025-08-18 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2459cbb1-0f33-35df-bf50-950d28494d77 | -11.35832 | -55.39091 | 2025-08-18 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5df530b-c106-38b1-b2dd-41834921dd69 | -13.00549 | -56.85063 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ececa45e-c529-3c0e-9670-21deffe865cb | -15.61333 | -54.30133 | 2025-08-18 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ee8ac145-121d-3d6a-be71-6da9cc97d744 | -15.73005 | -48.41949 | 2025-08-18 04:49:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3899cad-9af2-3b90-aac0-ae632e3eb6fe | -13.58772 | -47.75445 | 2025-08-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e823ed1a-e974-303b-81c2-b0f4f99a8539 | -15.9123 | -50.15877 | 2025-08-18 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 708bde5f-8a27-3856-8c50-8b06c1649992 | -14.9887 | -54.77614 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d83ec89d-5937-354f-a40c-5c4ab608e316 | -14.63341 | -54.9088 | 2025-08-18 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a9cd0400-6b8b-3a97-a5de-febe4f226aac | -12.57091 | -47.05461 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a25f375-c393-3651-8f78-5d1f861b9a8f | -12.98579 | -56.85183 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 376a89ce-ffbe-33ab-8125-2abefdcc8ee7 | -13.22411 | -50.73968 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7282fe3e-6dd8-34af-84db-f3bd9183ef66 | -11.66904 | -51.60969 | 2025-08-18 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eda4d81-f67b-3b0b-8d5a-20da80a79521 | -17.82081 | -50.5767 | 2025-08-18 04:49:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bb6bf39-1e7d-3e50-b6da-e70a52ab9b0d | -12.61914 | -46.89731 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddda170c-b7ec-3fdf-bfa9-0ca336aa12ea | -15.11539 | -48.73202 | 2025-08-18 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f73ba68f-6ba8-30ec-a573-5ac9f006484e | -11.85187 | -51.59097 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9404b3ae-f57e-3da5-a928-42b2eed2d06f | -12.92309 | -46.11225 | 2025-08-18 04:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1fadaa15-5664-331f-8182-196f426a1578 | -16.16345 | -50.02356 | 2025-08-18 04:49:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c9013f0c-f4c3-3560-bd15-185398859e77 | -13.14057 | -57.17251 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cec64c73-2fc7-3526-a98f-4579f7c24f67 | -14.06987 | -54.07753 | 2025-08-18 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c4fa5ef-87dd-3cb7-a5da-753ae4b46270 | -12.44081 | -46.99973 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3de2f192-ff74-3de1-ad98-fe1dfc1c49ba | -16.79904 | -50.09373 | 2025-08-18 04:49:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8aec4c0e-fab2-368d-b221-ac3b4980c30c | -12.48788 | -45.5656 | 2025-08-18 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 78b38212-e10a-30fe-8d2d-d6a14a050c39 | -13.57573 | -46.99671 | 2025-08-18 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 557ca371-936a-31d4-a309-00cd1473b1c4 | -15.86843 | -50.20839 | 2025-08-18 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 15092f55-ff03-3b2b-8966-110a4c2adcc9 | -15.85702 | -50.21111 | 2025-08-18 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cd9e260-f61c-3c3a-b20e-c6f7c28eb22a | -13.60613 | -47.73957 | 2025-08-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e636444-3925-38f5-ae88-77a724f7f6bc | -13.22869 | -50.75599 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d42e55a4-70fc-3af3-9efd-72fba26e06e3 | -11.31957 | -55.21114 | 2025-08-18 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ae2dbd9-e3ed-3777-831b-6e5dd941ee2f | -15.61607 | -54.30555 | 2025-08-18 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6eb213fa-6e0f-3dc5-8277-c88348c6d436 | -13.59445 | -46.98542 | 2025-08-18 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f999c01-3af0-3c48-bb13-00f7b62a58c6 | -13.22012 | -50.76634 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 36.5 |
| a87974d6-3e52-3751-ae36-afe490bdc324 | -13.23669 | -50.74944 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c676ac9a-55ec-3024-b537-4a4e4943add7 | -14.98532 | -54.77562 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b94f208-7711-3f14-ad5a-09cd4b59e40f | -11.84684 | -51.57925 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7ff387e-df8e-3cf5-b9bf-af5e84362edb | -14.99304 | -54.79222 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b24a08f4-abb2-3279-9e0a-559086415a7c | -13.96632 | -54.08651 | 2025-08-18 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adbf320f-12a6-34f3-b3f0-82c733b721e5 | -14.06928 | -54.08117 | 2025-08-18 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c848220-df3d-31f7-ab3d-9dca9f537a7e | -12.94025 | -46.11954 | 2025-08-18 04:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f31e01f-add9-372d-8851-0889fb37fcca | -12.99793 | -56.84921 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6e739e63-478e-36b8-bb55-ea5198596f8a | -15.49571 | -48.52426 | 2025-08-18 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90e0e0d3-c8f6-37c6-aa45-677bb8caf2da | -13.21611 | -50.74623 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7dbf85a-8615-33e0-9e56-c72f2fa403f2 | -16.79514 | -50.09483 | 2025-08-18 04:49:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6f86e6bd-76d2-3de3-b0ba-d350e0a1f0c6 | -14.62723 | -54.90382 | 2025-08-18 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0590689-fa2d-3913-82e8-b0f557dac31b | -13.59597 | -46.97389 | 2025-08-18 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6089548-fe95-3448-9b7c-13431ad52f20 | -15.00104 | -54.78574 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41ddaca0-46d7-3a3c-b46b-ef6a84b5f609 | -15.85643 | -50.2153 | 2025-08-18 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aafe1da1-6c1e-3f69-8a46-93b9520d851f | -12.13231 | -47.9011 | 2025-08-18 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a42b4f59-3d0e-3d93-a9a0-1ecdcdfad729 | -15.00576 | -54.78604 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6b04461-d0b4-39b8-86aa-f17efbdc236e | -15.86302 | -50.19462 | 2025-08-18 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c7494b2-bf36-3d78-8785-5df3c754d7ed | -17.09705 | -49.87978 | 2025-08-18 04:49:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 460558ad-e188-34cf-8095-8d2359425861 | -13.2264 | -50.74784 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| eb358c41-efb7-3b22-87fb-a418d2087174 | -13.21098 | -50.75713 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| d7629086-986b-3812-b1d2-fb34ae5b0d3f | -14.18151 | -45.32101 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9211b93-9d97-36d6-b889-797c5467c01e | -13.2224 | -50.75111 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 583bab52-b943-3127-a16e-897ef05df1db | -13.0198 | -56.85812 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ffad0e6-7ee0-3742-89bc-dd1b6c4f2be6 | -13.61034 | -47.76912 | 2025-08-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b7ddea0-0bfd-3659-bf27-df543e018ef5 | -12.54094 | -48.49924 | 2025-08-18 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd772e65-b14c-30ee-8b91-faee895e043c | -15.86003 | -50.21584 | 2025-08-18 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9cfb757-f510-34c3-a3af-47e62ff4fd83 | -14.63125 | -54.90065 | 2025-08-18 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67a51827-4b3f-3f15-8415-b1a8f57e6705 | -13.14313 | -57.15777 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b68c93d8-e7c9-3ed5-874e-2cd805b0bdb1 | -15.00787 | -54.79426 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e0e6256-02ea-3ada-b5af-b62941a700f0 | -13.20755 | -50.7566 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 7a414a29-312d-3077-8d2f-358e82217504 | -14.28517 | -53.19589 | 2025-08-18 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 48e64539-47de-3b3e-b948-99a6478ce0b2 | -14.63402 | -54.90503 | 2025-08-18 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30f5a11b-7414-3ea7-a79f-d9a572ea696c | -12.6186 | -46.90139 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 383c8c62-a60c-3795-8686-d9471184ba39 | -15.61274 | -54.30497 | 2025-08-18 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8f705188-7de0-387a-befb-4d1fd90f82f5 | -15.00318 | -54.79398 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca6fbb37-9839-39cc-9a1d-f76bc8c12cdf | -18.04353 | -43.81329 | 2025-08-18 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0940cbf7-6eb2-33fa-a03a-b11523421b34 | -12.57296 | -47.05432 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b308aff-99b2-3c13-8edc-45da7cd43535 | -13.1685 | -54.92516 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c4b7f55f-bb85-3187-b429-b111ebc35dad | -13.17194 | -54.92575 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bbe3013-67a3-3465-a380-41c614bbde87 | -12.63577 | -46.90098 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cf2657d-8d44-3beb-a755-7182571d426c | -13.1713 | -54.92962 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aa7b4484-dcca-3818-88a7-beedb177d002 | -13.23269 | -50.75271 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42314879-d297-31f3-b92b-09ec0849d8d1 | -11.31179 | -55.21403 | 2025-08-18 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02c419b4-0e7b-3345-83c1-4ccb32e433a8 | -14.63681 | -54.90942 | 2025-08-18 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| afcd302e-850d-341d-9ffd-b85890287307 | -15.64606 | -49.25314 | 2025-08-18 04:49:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb32c48a-5c05-3cfa-a378-1a426039a100 | -13.1367 | -57.12639 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed2bd747-f242-352f-aeac-4afa3dad1c1d | -15.76499 | -56.29509 | 2025-08-18 04:49:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f17ee716-9e50-3141-a461-6356e97e8ece | -17.39676 | -49.22899 | 2025-08-18 04:49:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20185a98-2032-3b01-8ad5-c6ccccac5fbf | -13.45453 | -45.89222 | 2025-08-18 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7205fd25-ef2f-3a42-9cc2-81c86663e747 | -13.59218 | -47.7518 | 2025-08-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55f7a09f-9a2b-31bb-91f4-a9850ec7e366 | -12.62329 | -46.89831 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa3cf1cf-8822-3a43-9dfa-3c3025599c5b | -14.97855 | -54.77452 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 40e44221-03d7-3792-878f-350c6a64956e | -13.47493 | -55.76502 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| abbde603-a79b-358e-a79a-aa7586853f72 | -13.01783 | -56.84576 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 217134a3-626d-3abf-9917-5fc4542f3dd9 | -12.99496 | -56.8438 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a869ee6-da2b-3f3b-8b65-e8c0aaff9842 | -13.22812 | -50.75979 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 805c83de-d12c-38c0-a791-e9016b092153 | -11.53773 | -52.23836 | 2025-08-18 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf687739-372c-3013-bd06-7b8fc7566429 | -11.66238 | -51.60863 | 2025-08-18 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aefe4a9e-037f-349f-aa94-336d3249417a | -15.00257 | -54.79779 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e2a72ec-3311-335c-ad44-3dc19fc6c764 | -13.2471 | -50.79689 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1c32cbd-4592-393e-aa32-29626ed55b29 | -13.21554 | -50.75005 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README21.md)
