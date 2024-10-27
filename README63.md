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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7e5c49c-b89b-3e24-b4dd-497f81e548f4 | -1.26587 | -53.04206 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 749682b1-fd61-3e3d-951b-468b2e05e2e3 | -1.4539 | -54.28954 | 2024-10-27 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c804a907-4a41-3f00-8b22-1d05de0fbc34 | -1.45331 | -54.29333 | 2024-10-27 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee43c54a-87a4-3d5a-9418-3906c092c32c | -1.3484 | -54.64335 | 2024-10-27 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21c67b87-83c3-37d8-b639-2e725f18c200 | -1.34343 | -54.63915 | 2024-10-27 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3834828c-1f64-3b94-b5ee-e7c6e25f3c20 | -1.33846 | -54.63503 | 2024-10-27 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3f8b9de-edf1-39b0-8bfb-2ca265d70932 | -1.11787 | -54.12854 | 2024-10-27 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b6645fe-09b6-3dc7-bc9f-67bdef89986d | -1.1173 | -54.13227 | 2024-10-27 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3fd9b26-00cd-3f0b-ba4d-ec4af6e84740 | -1.11674 | -54.13592 | 2024-10-27 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 196df699-616d-33b8-8d53-8ee6415cc790 | -1.07167 | -53.6606 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3aab101-37ce-3709-aa96-7a68988b78d9 | -1.06587 | -53.65954 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54f1fc6e-0339-3858-a404-95609e5acf23 | -1.06463 | -53.66766 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f37925d6-a061-3411-a65d-69862ebfb181 | -0.99505 | -53.69535 | 2024-10-27 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 966c5efe-e037-341d-8468-499a4b11a331 | -0.99441 | -53.69943 | 2024-10-27 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 481e736e-525a-31d9-9918-e04334fc4794 | -0.99378 | -53.70351 | 2024-10-27 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ea6c775b-cda3-3e1b-a37e-442b5658c17f | -0.98987 | -53.69044 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6be6efa-5a1e-3e2b-9485-f32550799886 | -0.98923 | -53.69462 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c652c702-efff-394c-880d-da175da13a19 | -0.9886 | -53.69863 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0419384-d7e6-3235-b0ce-f39590418b76 | -0.988 | -53.70253 | 2024-10-27 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ef59544a-8229-3e24-8350-bf1878c81eb8 | -0.98734 | -53.70674 | 2024-10-27 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc47a870-2bdf-3d38-8a79-eba653a978cd | -0.98665 | -53.71121 | 2024-10-27 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87d0bbe1-a8d4-3eb1-8e27-66731192925e | -0.98405 | -53.68969 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64cc7f29-867a-3026-9705-94b121791b34 | -0.98339 | -53.694 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe971429-3584-37d2-ad67-8086bceabe0e | -0.98276 | -53.69802 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad80dad5-2913-3579-b5dd-cff595f62f9a | -0.98218 | -53.70176 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf7f4862-b4ca-32e2-9c61-39333519e783 | -0.98157 | -53.70575 | 2024-10-27 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 362edee8-eac1-3537-812f-20b4e25edde7 | -0.98088 | -53.71017 | 2024-10-27 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e54450ff-f106-38a3-9ef1-354733e71eb4 | -0.97756 | -53.69333 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd6d4520-e803-36a1-9301-2559b2fe5888 | -0.97694 | -53.69733 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 298aa0f3-dcf6-34d2-97cf-461f78d685d6 | -0.97634 | -53.70119 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be3a5ca8-377a-34ae-a787-55798d626d15 | -0.97569 | -53.70538 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97ab1171-8ee1-3b8c-83e2-e7c8bf1a4ef4 | -0.97494 | -53.71025 | 2024-10-27 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e6c46b3-5ed3-30e9-b7fe-e6a7b4a90b60 | -2.88892 | -54.89679 | 2024-10-27 05:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a0a21da-821d-302e-81e8-83cc16d9a024 | -2.88836 | -54.90039 | 2024-10-27 05:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb76f343-5af5-30f8-b082-3260092e35ec | -2.88832 | -54.89555 | 2024-10-27 05:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a894556-bdd4-3e37-be90-8f10257968db | -2.8878 | -54.89918 | 2024-10-27 05:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8133a7f3-22ee-35af-8afa-9c280843d203 | -1.96427 | -56.02578 | 2024-10-27 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1eb3e787-1dbc-39dc-b0a6-e63b9935860c | -1.9636 | -56.03009 | 2024-10-27 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0996a089-4242-3517-977a-ee50f57cf29f | -1.96354 | -56.02672 | 2024-10-27 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96ea09cc-9ed9-3afa-8fa3-1314413118f1 | -1.96311 | -56.0296 | 2024-10-27 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df816a19-cc90-3dcb-b0bc-b85068fe5075 | -1.96268 | -56.03248 | 2024-10-27 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23a9839f-f751-30f6-9620-c9429e04fb95 | -1.37236 | -55.39562 | 2024-10-27 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fc0627c6-8834-32fb-a6e6-f65bfae3beb0 | -1.37189 | -55.39868 | 2024-10-27 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a68d45f4-d5ca-3cc7-9bc6-3109f2dbfe33 | -1.37184 | -55.86033 | 2024-10-27 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cc369ca-5367-3b0c-b07d-32b92aa09684 | -1.3714 | -55.86323 | 2024-10-27 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b655d97-efe4-32c2-b8ca-4ef8683fe251 | -1.34394 | -55.87884 | 2024-10-27 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5104cf0-de48-32f7-841e-ea9adddfbc36 | -1.34318 | -55.87941 | 2024-10-27 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78c0d90a-ab9a-3a66-8d3d-9e15afea04d5 | -1.33936 | -55.87516 | 2024-10-27 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c1e2197-db4b-398a-a772-ef09ccfc2c42 | -1.33891 | -55.87805 | 2024-10-27 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21bba318-283e-380e-9457-37771c14a10e | -1.33858 | -55.87572 | 2024-10-27 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f912b0d3-e023-33cd-9f25-9149c9bd1d1b | -1.33815 | -55.8786 | 2024-10-27 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53b34387-d754-34e5-801a-3b0f89275888 | -1.29119 | -55.71838 | 2024-10-27 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95ce121c-f061-3169-b4cd-bd99c98a408e | -1.29074 | -55.72129 | 2024-10-27 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f8ed80d-a1ed-3265-8d1e-a0251506130f | -1.29029 | -55.72422 | 2024-10-27 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba53894a-f133-3a93-949c-d249533e0a0f | -2.10498 | -56.54982 | 2024-10-27 05:40:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a756fdfd-9503-34a3-b961-a20ff5c0f408 | -2.05764 | -56.86718 | 2024-10-27 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 061d4bfc-845c-3c63-a22d-390fd860fb86 | -2.0569 | -56.87218 | 2024-10-27 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9d42690-71e8-3b2d-b645-1cd33783dd07 | -2.05646 | -56.87047 | 2024-10-27 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f9bb7b3f-70fa-3ea5-8ab5-23882c9aefa9 | -2.05288 | -56.86654 | 2024-10-27 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b525bb7c-0503-3782-ae95-3abea6507032 | 0.71077 | -59.87496 | 2024-10-27 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c3b1385-367f-331b-961e-3946d8a3a09c | 0.7051 | -59.74264 | 2024-10-27 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf114164-a53a-388d-a3c1-fadc5a6e5e83 | 0.17575 | -59.42957 | 2024-10-27 05:40:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38b3708a-8d3a-304d-ad3f-255b495d6e5d | 0.1744 | -59.42656 | 2024-10-27 05:40:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e0d52ba-87a4-33b2-9a58-131f2b58d2aa | -1.91433 | -59.98374 | 2024-10-27 05:40:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 195423b8-bdca-3d1e-8b69-78a4c89498e8 | -0.38351 | -61.08951 | 2024-10-27 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6751154f-6a4f-3a37-8c6c-13621a001fef | -0.15393 | -60.87094 | 2024-10-27 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb594302-3ce9-3e8f-b5c0-38ce45e6c37d | -0.15098 | -60.86631 | 2024-10-27 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e315a5a3-2f1d-3262-bfea-5401b70411bd | -3.48267 | -62.7808 | 2024-10-27 05:40:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74de0b6e-6426-356e-a203-48d3c72455ca | -3.4821 | -62.78448 | 2024-10-27 05:40:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b49eb30-9683-31ac-81c6-a44d1b92269d | -3.06123 | -61.66635 | 2024-10-27 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0dcff92-096d-356f-81bb-e308f866716f | -3.06062 | -61.67036 | 2024-10-27 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1832297-a588-3801-9eac-b7b891e3b4ad | -3.01784 | -61.69358 | 2024-10-27 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79828ffb-d9c1-31d9-88ed-6779a09c9512 | -3.01366 | -61.69704 | 2024-10-27 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf4ecda1-c167-3895-8574-c82916e6ee5c | -3.01303 | -61.70103 | 2024-10-27 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 452b6279-6a7b-3970-857b-9d4c04b057e0 | -2.89381 | -61.86576 | 2024-10-27 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d551bfc-45a0-39c9-9597-f9e11aa54e4a | -4.25981 | -63.14767 | 2024-10-27 05:40:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe386d4e-8eb0-314c-ab68-7438c3d11ac3 | -4.25925 | -63.15131 | 2024-10-27 05:40:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0bbdc13-6618-35a2-bf98-438856712bc7 | -4.25585 | -63.15079 | 2024-10-27 05:40:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9dac18c-e36f-370f-8cab-f756703fabd6 | -4.25529 | -63.15442 | 2024-10-27 05:40:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e70c2ea-63c8-36ca-8b76-939e62a16262 | 0.11086 | -62.54658 | 2024-10-27 05:40:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be34c65d-d3e5-3be4-ae49-822ba6ccd027 | 0.10469 | -62.55117 | 2024-10-27 05:40:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ce99e05-a00c-3d9a-bdb9-065783eb316f | 0.10133 | -62.55169 | 2024-10-27 05:40:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ef9f7a1-b258-3f90-8f9a-4d7e565cd2bd | -3.15873 | -68.14443 | 2024-10-27 05:40:00 | NPP-375D | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e3f8715-eedd-3f66-b910-154d3f699132 | -0.9815 | -53.7192 | 2024-10-27 05:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| f633db56-9897-309d-a93e-5a46dcf7af21 | -0.9815 | -53.699 | 2024-10-27 05:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 370186c3-9be8-334d-836d-be945820e35c | -0.9998 | -53.6989 | 2024-10-27 05:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2a94f093-654e-30df-8199-6949922821eb | -2.5311 | -51.1816 | 2024-10-27 05:45:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| afdb4b33-aaaf-32a5-9e46-81b792c71f3d | -2.5312 | -51.1609 | 2024-10-27 05:45:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 9ac2d453-6321-3dd0-b025-2484e36aefed | -2.5495 | -51.1812 | 2024-10-27 05:45:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3a22436c-e18c-3b46-8372-df9193a00fb7 | -2.7033 | -49.33 | 2024-10-27 05:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 2889305f-4fd2-3a18-8901-d4b321c057a0 | -2.7034 | -49.3088 | 2024-10-27 05:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 8716c258-d8a8-37c9-a99b-898770259852 | -2.8329 | -49.2626 | 2024-10-27 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| dae1bc2b-27f4-373c-9a20-79cf6ba95c13 | -2.833 | -49.2413 | 2024-10-27 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 2d300384-a23b-3ace-84eb-51d2a9034d16 | -2.8514 | -49.262 | 2024-10-27 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9a3053aa-e1c7-31ec-a371-a129386fe205 | -2.8515 | -49.2408 | 2024-10-27 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 8e0d9f87-7d0c-3fc3-b867-2db1576edeaa | -2.9215 | -50.274 | 2024-10-27 05:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 30db4777-ecea-3cc4-a875-9687785395a9 | -5.5543 | -46.9967 | 2024-10-27 05:45:37 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 442d08fb-84d2-32b0-b910-e99e181854e1 | -0.9815 | -53.7192 | 2024-10-27 05:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 887bf02c-4538-3686-b2ab-40c975f3d9e8 | -0.9815 | -53.699 | 2024-10-27 05:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| c47130dd-3921-3901-a898-b698e68033ac | -0.9998 | -53.6989 | 2024-10-27 05:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |


[Clique aqui para ver as próximas entradas](README64.md)
