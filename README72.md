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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7eb9d2f-0dec-367d-b993-01b3645ddc07 | -5.22417 | -44.91712 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd6aa69c-0670-322c-8606-ceaf11b7a1cb | -3.25301 | -53.63766 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 07dd4f4f-3c2e-3156-80b3-bb77691b8ff0 | -1.0925 | -53.64342 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 619b2d8d-dc58-3abf-8ac3-2d13cb237b68 | -2.78976 | -51.6096 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9935316c-b975-3f20-aacc-a0d20e68ba4c | -3.1987 | -53.42175 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d98099dc-471b-35e4-b86e-85e4b9795a71 | -2.68829 | -54.14054 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5d8e0f5-b426-3921-a591-d8f54989868d | -5.65424 | -45.20065 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67562a1a-d75f-343f-99fb-f18e81a08f18 | -2.60345 | -53.96504 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5aa4d999-1ff3-334a-9e9e-714345eca5c3 | -2.44089 | -50.42469 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 698e0cd2-b0df-34a9-8b49-fa72c58fd284 | -1.20878 | -53.54881 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0c6e7ec-44f5-31fc-96c8-2148fc326d97 | -1.31306 | -51.9221 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1aa6d101-5b64-3144-9518-55da8cafee1e | -2.47126 | -50.3811 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cc41fb4-d577-3925-b579-d86c1e85bf20 | -1.6017 | -55.42458 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ce77247-fa1f-32a7-861a-f38fe841a853 | -3.07887 | -53.29342 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d627ae9e-bca2-3b2b-90b8-056cd9a25293 | -2.58343 | -54.24466 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 880cbcdf-ae25-37d0-a8d4-c4e98eae9337 | -2.77783 | -52.86778 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c5b874c-f196-3e53-82b6-befdb6341458 | -3.52306 | -50.47733 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c09247b-c496-3e5a-a1a5-4c612c21deca | -2.75812 | -54.08414 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abf84d00-aaec-3856-8909-a48648e2b02a | -1.14268 | -53.79908 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baff861f-4363-3c66-b0fa-c4203bae0aed | -2.58418 | -51.92073 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08cf0801-6e06-3979-9453-5fe510f09bbd | -1.624 | -52.69874 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf3df9aa-d084-34ad-95fa-82b9ecbd6049 | -1.79851 | -52.75805 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9ce8a5ce-5079-38c9-9df8-7a8b1f9f29c3 | -2.89334 | -48.27431 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb58d44b-d0f6-35ad-b180-b12edef9079f | -3.24855 | -53.62291 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca81ac94-19a6-3b22-b8d3-f9786053f62c | -3.22258 | -54.18225 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1642bc1c-4d19-3c2e-abf7-480d71395357 | -1.07882 | -53.3812 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f7ae048-c419-3c09-b4bd-b8025958b926 | -1.7694 | -52.7253 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 358379c9-d8b0-3c52-8be8-98a270ed67dd | -2.54118 | -54.05763 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c24f1961-519a-3689-ab54-fbcfa070e6b9 | -1.15157 | -53.54699 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2f4576e-7018-3cc2-8089-98a580d00514 | -2.40994 | -53.85353 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9aa9985-1fe9-3a8a-9667-e2b22966aa08 | -1.47776 | -52.65501 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bcd24d7d-cefa-37d3-bc53-a549d81bbabb | -3.09485 | -54.56346 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fd16d51-50b5-3b30-971c-a289599ec829 | -2.86505 | -54.03087 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8caeee6d-89aa-3172-81fc-7a2df3cb901b | -1.16753 | -51.93644 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1899910-9afc-3f36-88f5-cb1aa32fab75 | -2.6084 | -54.28043 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a4b33ff-571e-3716-9d70-2041c3989ed8 | -3.69134 | -47.13446 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b5ce8e5-103c-30a8-a180-5e30b49ac07f | -3.09747 | -53.26101 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a17b255b-f8ce-34d9-880e-378fff2720da | -1.66948 | -52.7347 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6654b549-38c6-386c-bdee-20da01c98aef | -1.62709 | -53.87895 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8af4fd11-9d75-3dbf-bd00-1faacd7cea23 | -1.68181 | -45.79598 | 2024-11-29 04:57:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9b5e5b6e-321c-3e21-96df-9572c2720a7f | -1.48142 | -54.44051 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3568f68e-c638-38cd-acec-597898666c5b | -2.31383 | -51.96133 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58a4bb39-b1c6-30f3-bd71-61f2b932cd96 | -2.44285 | -51.78749 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3618e9ed-5201-3870-9424-e3c36fecc326 | -3.96361 | -48.83342 | 2024-11-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60430cd9-9a0f-39a1-910e-367ec6df85d7 | -2.62306 | -51.7586 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8d3aef5-df6e-3c3b-a3f3-ecb3fc8585ee | -2.26509 | -46.44388 | 2024-11-29 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1acdb76b-4af1-37d0-9d62-5e0d219a5091 | -1.65996 | -55.23262 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a75d32f8-88e0-3387-9ac9-379f41690bc4 | -3.09476 | -54.1306 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b8b81c4-90bf-3e10-be05-c48f6e8d6997 | -1.18496 | -51.97912 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ca93d28-429c-3c3c-9a28-7596bc0794bd | -1.67001 | -52.73125 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66014d91-a05d-348f-a1c7-fd7d9317614d | -2.2378 | -51.43575 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78384ea3-edaf-3edc-8a81-038c59c44bcc | -2.71678 | -53.17344 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd92e690-ae7c-37bf-b42e-48a2d4b31b03 | -2.83083 | -52.94332 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42673201-4ca7-3118-bd0e-a78e2c1ae1c7 | -2.75162 | -60.23402 | 2024-11-29 04:57:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45d8a65b-364f-3d02-9ad4-fff76039a740 | -2.75956 | -54.12048 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| efcadb1f-a0a3-37d6-8e64-3a0e195f8dff | -3.16969 | -48.43626 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1f829b3-dfb2-3558-b756-700dc1646ba9 | 0.941 | -50.73338 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13e97525-46b5-32f2-a7d0-678c9baa442e | -2.04108 | -54.68686 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 359da3e9-b729-3738-bb9a-3563ec22f107 | -2.58445 | -54.21644 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2ba3ccb-3bcb-381b-a1fe-9d791a2c92df | -1.71709 | -52.49316 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 262f7cc6-776e-3714-a18d-d1cf12384983 | -3.70815 | -53.40229 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2306434c-afbc-37c3-8863-2dbafb4560fe | -1.96528 | -46.44056 | 2024-11-29 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 0def4793-7107-3e80-aeb1-92bcb506b529 | -3.29003 | -53.68574 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d969c053-13f5-3dc4-b3a1-0dd043bb1e5f | -2.82908 | -46.84531 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d3f10c0-aeca-3744-a6a4-f2b771bc7bd4 | -1.16371 | -53.68596 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73e5e48b-ff1a-3ac7-86de-f2a16fe316c4 | -1.38519 | -53.64004 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2889dbc8-0172-37e7-b085-966bcc6db2b7 | -2.59611 | -54.07684 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f3312be-87e6-3751-a3c1-b67b28b09c59 | -3.21834 | -53.38247 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c1aadc6-5da8-37b1-8309-dafe63e5ece2 | -2.80778 | -53.04618 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b8822db-b10c-3c7e-a5be-b35580f7c285 | -0.82009 | -51.6155 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e76f0dfe-95a8-33ff-b1ed-da72b4d254a5 | -2.88346 | -54.11137 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d3e2ff8-53a6-3c58-b72d-3ee5a9faf745 | -3.0745 | -50.96476 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9328aeae-f265-395a-84dd-b907ad2005c9 | -1.15629 | -53.62508 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55372f67-92f3-340c-a3f4-054d4a6ccc9f | -2.47012 | -48.40596 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bb725fc-c799-3d54-b4b7-e741bb7ada6b | -3.74357 | -51.8395 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc4ec67f-c1ba-31b5-999c-f94a73e13564 | -1.31535 | -52.86614 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd574379-a90f-3fee-a5d5-009f7dfe032a | -3.55133 | -51.608 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 95f914d5-c7b4-3a49-9a44-d2a16a52b939 | -1.63125 | -52.71757 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfc98e35-50e1-30ea-b608-8596d3babd20 | -1.59167 | -52.27282 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2190189-50cf-3eee-89aa-075a54e1df94 | -3.11488 | -53.75994 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf3024ee-e842-3a5c-a2af-50a1ffe10b8b | -3.6856 | -50.92629 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f2b82c3-7829-3d3b-8f8d-45d56381d5ed | -2.30199 | -51.92625 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22fa5d0f-6d9f-3908-920e-d1cb860679d2 | -1.14074 | -51.67537 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6683b132-6703-3121-872f-32cce9dee27b | -2.96788 | -53.72309 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a0f99c37-64b3-31eb-ad1e-6c0e676d017a | -2.78023 | -54.03189 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c04942e4-1991-3390-8226-564bf3585e7b | -3.82935 | -46.54922 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c253a863-5434-3464-b381-8c48e764c569 | -3.0738 | -54.56738 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1befc925-e3e9-3fa7-8e9c-840e15a26b13 | -1.45877 | -54.49789 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57608a82-31fa-3421-97c3-da9bcf6c11b6 | -4.07652 | -50.03405 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 54bdb834-af8a-3d85-a661-7cb23489369d | -2.32115 | -51.95876 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2010e1d-d283-39bd-a387-05a94e4abdb9 | -2.05636 | -56.07978 | 2024-11-29 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d1c812de-c470-36ea-ad29-c0f9e3fa4ac2 | -3.96507 | -54.61065 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c41805d-0a4d-3026-bc92-ac3127a7b312 | -1.20336 | -53.71753 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87356f45-f934-3710-acd4-a4592c112cc0 | -1.65385 | -53.81612 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3f9f4d0-9a23-3c22-806b-c2ba31753330 | -2.44565 | -53.97176 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5e52dbe-8547-3f04-b1b6-ee27acded039 | -3.70908 | -50.43755 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 886a31b8-8eeb-3fbb-bdc7-f14d6ce23e0a | -3.54161 | -50.1856 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4679fce8-0200-3260-b563-0d8da51b2c64 | 1.32787 | -50.67144 | 2024-11-29 04:57:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef0ccad4-2e02-3390-a1c7-cdb61cfc3c8b | -3.00185 | -54.7427 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db91e831-1eec-36c8-945b-1f6d22d1f51b | -1.20026 | -52.10094 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README73.md)
