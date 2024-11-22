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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e278ebc1-5003-3931-8fd9-0f2b5a4bd742 | -3.20525 | -54.25251 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a876b7af-1935-3a85-b153-8bf5d130eb67 | -3.23914 | -54.25253 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| cfed5fdf-2c79-37d3-baef-01ce037b57e8 | -2.69904 | -51.86494 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13f2c7c8-ec2b-3248-9f6f-c9670fd0bd74 | -3.32136 | -54.0924 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e3fe9e29-6587-377a-ab0c-3bc9a39d80aa | -3.66803 | -54.65777 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc686921-7527-3569-bdcc-560d3e97b5da | -3.22419 | -54.24775 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| bcdffe36-5a22-3cf0-97c9-075339c2535d | 1.38398 | -55.93895 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edfb2550-7607-3ac9-b70b-86ce8a59dcef | -2.95134 | -53.7193 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54cced35-c9ef-3596-b5e9-3b75430f5fb2 | -3.2304 | -54.24607 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 0066caa9-49b4-3517-be35-ee335a157376 | -4.10831 | -51.05101 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5f51829-d93f-3c33-9c1f-3129dfc6ca48 | -3.54287 | -50.51849 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0a25cf5-aa42-37d9-a999-912ae4779014 | 0.4641 | -51.34215 | 2024-11-22 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b170fe2b-415e-321e-970b-d7e1e677453f | -3.20455 | -54.2574 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 67787c1a-cda9-3457-aecc-54ba2b3f8659 | -3.19232 | -54.33004 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8158a863-e18a-3aa9-ac48-b1edcd678b97 | -3.5329 | -51.1039 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc4a6e95-1413-3cf9-a348-d7e6e87d526c | -3.21949 | -54.25448 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d93592e1-345f-3dde-b9fd-f5bc17351368 | -4.11718 | -51.05175 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d79f3c9-5665-32fb-8173-3ac3f3ae22bb | -3.33031 | -54.09806 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28dfaea7-8351-32b2-8d2c-2049e12d7081 | -3.63945 | -54.32312 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d732b327-59a3-38e3-866b-c56982340348 | -3.19443 | -54.32779 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fc4c1983-c04f-3503-9887-fcd249a47478 | -3.31184 | -52.86037 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6ae29a8-3f05-37ec-bc6d-0c80c496c893 | -3.50328 | -53.79911 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cda5f301-97de-342b-9982-4a3ae4b79e3a | -3.50375 | -53.81096 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b9f3abeb-48b8-3834-b5ea-703707f620a2 | -3.58113 | -54.51833 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f5b53c34-8f80-39ed-87a7-da79e6326f5f | -3.21321 | -54.25616 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 135ffdff-fba0-3abc-b6dd-5fad95197513 | -3.50821 | -53.79973 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4210c62b-8c58-3b53-a961-75a04ba64d04 | -3.2384 | -54.25758 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0e380e41-8f2a-317e-ba8d-ce25d2695888 | -2.05376 | -55.4592 | 2024-11-22 05:29:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e1c71d2-70c5-3adc-a0ab-d7db0498102b | -3.50245 | -53.8046 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 759eb054-ab03-37b9-84ff-1f00b1aec70a | -3.51728 | -54.69239 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9cc01dee-0f0e-383b-ac44-7990413e9ce6 | -0.05588 | -51.23653 | 2024-11-22 05:29:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f001b99-1c79-3b57-9cdf-81a313e5a12e | 2.37528 | -50.76498 | 2024-11-22 05:29:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aac72986-f03b-3974-899a-7e7a69d0a8d5 | -3.21072 | -54.24817 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 211ad754-1cdb-33dd-a30c-faf665e96b25 | -4.18219 | -53.57717 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ff1cb15-1d19-3b91-91b5-37ca7839eb72 | -3.18293 | -54.32847 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bc3f42d-8404-3b14-8692-5b3e71e61c9d | -2.94309 | -54.8 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e23733a-eb27-3c24-b8f1-e170c528dd31 | -4.11595 | -51.06012 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b12c7eab-dddf-3321-9e4a-3d4f9acf8bf6 | -3.57911 | -54.68322 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 25b9a33f-1ddb-304e-aca8-ce935b6c495b | -4.19226 | -53.57876 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d157ccfe-5a81-3513-9534-fcaf9fb11f26 | -3.28399 | -53.82369 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8dd5677-5383-3129-b58f-7f50e5f0ec25 | -3.21547 | -54.2488 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5e93f77d-974f-378e-85d2-33704d44d143 | -3.10362 | -53.73994 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82bb3d88-6fcc-322d-b734-952ac08f1c56 | -3.17973 | -54.3177 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fe2ed247-d23f-30fa-994a-04d242e7d148 | -3.43684 | -50.21214 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24b200f3-953e-3004-b533-ae6026ee1156 | -3.33743 | -53.33598 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b340a4a3-de33-3916-9e01-efce17634d24 | 1.38628 | -55.95395 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af2f0188-92fa-3b0f-bbb2-b235a69dea0c | -3.33788 | -53.33303 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ee8ed23-7376-31f7-819a-2f22778768b0 | -3.3446 | -50.50422 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbf18fba-73cb-39c9-8a91-e0210ec3e6b0 | -3.28316 | -53.82914 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7929a9e3-2459-3cbb-9c95-0aafd15f3ecd | -3.1003 | -53.16968 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21e9dc0a-17c6-31be-b89d-e33afa803798 | -3.85263 | -52.35217 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 926e3a5b-f91f-3214-9d90-b10d73b17180 | -3.2201 | -54.2436 | 2024-11-22 05:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| cdf5d439-4a15-3ee5-b9f0-38021ea8f8fb | -3.2384 | -54.2632 | 2024-11-22 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 6930af79-eec6-394c-803f-0bed9dfd63f4 | -3.2569 | -54.2426 | 2024-11-22 05:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0fb16e49-b310-36bc-b5d6-7ca8a73a82ed | -1.1287 | -53.3951 | 2024-11-22 05:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ef0d1e81-85ef-310f-95e5-c710e05da161 | -3.2386 | -54.223 | 2024-11-22 05:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 7a1adfa0-76c1-38a0-a33e-36e4e6ec2134 | -3.8535 | -52.3596 | 2024-11-22 05:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 8db9d50a-8a54-395c-9805-b9ccabc70bd8 | -3.22 | -54.2636 | 2024-11-22 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d84b2033-6765-336c-94e5-a8e54ba7d691 | -3.5159 | -53.8132 | 2024-11-22 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 547a6868-2117-321b-b441-3ef9e11b5a42 | -3.3452 | -50.4917 | 2024-11-22 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f61f9b10-f8b4-327e-9936-a785e9134226 | -3.2385 | -54.2431 | 2024-11-22 05:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 052172c0-5e23-3aec-8a10-c23012008245 | -3.3451 | -50.5126 | 2024-11-22 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 323de84b-ceef-37c2-bb1b-ba7eb50f7c6d | -3.2768 | -53.8199 | 2024-11-22 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 53649b67-f949-366c-bc21-13e58584830b | -1.35221 | -56.11874 | 2024-11-22 05:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a4794ab-82af-3589-8871-61fac619fd80 | -0.77434 | -51.77662 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1df1e48e-e6be-3c7e-8f6b-21ab7f8b6e92 | -0.87502 | -51.88981 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3cad17b5-ee8e-389c-b2d0-a593e3d8b4f9 | -1.62722 | -52.41253 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 228c92ab-b397-3d87-b5a4-8c8f094fc4bd | -1.81137 | -52.1622 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 13fb1582-e9c5-3a94-8aee-d7746033aee8 | -1.64039 | -52.61434 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d715bf9a-9bee-3509-b83c-8115b43339de | -1.19189 | -51.94458 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79a6f2b7-fa3f-3bde-bef9-075168f6cd80 | -1.61658 | -55.72099 | 2024-11-22 05:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abe0fb67-2529-3037-80bb-7fd2beada31e | -1.19523 | -51.95906 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4280c01b-6540-3847-91cb-056d5702a49c | -1.46062 | -52.66078 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 515dde81-aeb0-312a-b5ea-b2a16372f88d | -1.63498 | -52.68627 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03464555-e952-3bed-9b42-14dd14f8d894 | -1.25777 | -51.7639 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fcfd6b2-ed5b-35e4-ada9-55b51d574115 | -1.74556 | -52.37755 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ea1031f9-683b-3a69-8366-f7884f18e130 | -1.4484 | -55.51592 | 2024-11-22 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 158bc048-a264-3de2-be74-ddcf2d00e0d3 | -1.20862 | -53.70152 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e87c7488-449f-377b-8c65-a2eec272c319 | -2.21996 | -50.46637 | 2024-11-22 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fafe98a-74eb-36da-a0bb-b3ca1e6c5bcc | -1.61097 | -52.58797 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f74aef9c-63f4-372d-9c42-f5ccbb79a83d | -1.15496 | -53.66729 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8618827-8f2c-3844-ae5a-b2b50dbf6867 | -1.62313 | -52.61214 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4d43170-12bd-31f6-bb8e-7e600c56a359 | -0.81336 | -51.78893 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3f601873-dc1c-3748-96a2-89c3c901e1ae | -1.19828 | -51.95689 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 670bee1d-e388-37d3-a427-8895b095e708 | -1.26119 | -52.06625 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87c41359-c5f9-355b-babf-496b4e25ba37 | -1.79365 | -53.63115 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3b80e433-39a0-3441-b416-2a85d78f21c3 | -1.12229 | -53.40064 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 54ec2142-b4ca-3cd8-a080-08a475e77726 | -1.84641 | -53.69973 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59bd8366-8a10-38d4-aa72-d993f4aaee81 | -1.15177 | -53.59177 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8d7ff34-c8e8-3cd9-ab57-cda036082725 | -2.07823 | -50.32532 | 2024-11-22 05:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8a534a67-f8d5-3b0c-a31b-6af12e511c6e | -1.77921 | -53.59626 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8cf1f7b2-7c22-329b-9599-fa6cc2cb844d | -2.00863 | -54.5193 | 2024-11-22 05:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d23759a8-da40-3ee2-87db-ac6cc54aea05 | -1.79236 | -53.63173 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1acbb04f-d56d-3a89-9df6-43623afb97ce | -1.4478 | -55.51983 | 2024-11-22 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bae180ec-40b9-3f77-afb5-13076faf96a1 | -1.72829 | -52.71027 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 89061f6a-1b6b-3736-9f6a-9b6282cbf909 | -1.20027 | -51.76669 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ca8f543-e09d-3e06-bb62-091d9b43b6c7 | -2.31911 | -52.49313 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15e33be9-2896-3667-9237-b763e4354de9 | -1.74834 | -52.39452 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3278b03e-2fc9-3fce-8fce-f7a4f2f4a01d | -1.22363 | -51.79545 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b32fbb6-84b7-3e5e-8981-a3980a861ccb | -1.19918 | -51.77372 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README60.md)
