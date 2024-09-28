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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a01df3b-4ab4-35d7-b953-865603fd5044 | -3.12584 | -53.75095 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f7fc00d-4d8b-3a5b-b695-01dcb6cdeece | -3.12523 | -53.75467 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0df0a83d-1f6e-3804-ac57-8627da0885df | -3.12461 | -53.75839 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a517c046-da74-3cdd-a862-74b151beaa54 | -3.12088 | -53.74632 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27912b1e-89f9-3e66-9745-8195780f1d28 | -3.12026 | -53.75003 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fc5abdb-b206-3521-aa6f-07d3148f4cc9 | -3.11965 | -53.75374 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6cf3b0c4-7de9-3834-85ab-dad7fc4cf79b | -3.11903 | -53.75747 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ca4c7c9e-8864-3b63-8b7f-3e0f0e4a65df | -3.11468 | -53.74912 | 2024-09-28 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3bae92e-30ad-32e5-a5e7-70de681fa8db | -2.98383 | -54.63217 | 2024-09-28 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc2abbd4-9d06-39cf-8548-71b4b00e4b68 | -2.98309 | -54.63644 | 2024-09-28 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d438e6e0-2d47-3669-84fb-d88c3293b917 | -2.97953 | -54.6351 | 2024-09-28 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2bce90e-07d9-3270-bba3-6e61db7dea16 | -2.93716 | -53.69463 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ddc404f-7ae8-3855-9849-daa0d1fa4ac3 | -2.93656 | -53.69835 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc2cdd85-4d5d-3536-8653-b70f09100475 | -2.93599 | -53.69436 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ceda4a57-67c0-31b5-a0c2-b533bfe82983 | -2.93535 | -53.69806 | 2024-09-28 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 129feff2-3edd-31ce-bdc0-814446948454 | -2.85506 | -54.8636 | 2024-09-28 04:19:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fd3705a-c387-385c-a7ab-e943e455070f | -2.8543 | -54.868 | 2024-09-28 04:19:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c9b188a-1086-3d8a-8f9c-94c0d06d23b5 | -4.0687 | -54.09873 | 2024-09-28 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88aad888-a3a2-3e1a-a230-8ae09ae53188 | -4.06803 | -54.10258 | 2024-09-28 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 847eb7cd-a920-3183-aa41-73966104afc8 | -4.06737 | -54.10641 | 2024-09-28 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db0efcb2-c9cc-302e-8565-de9d0e228308 | -4.06467 | -54.10076 | 2024-09-28 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65e3cb9a-5d06-3633-9049-51ba93ad7415 | -4.06403 | -54.10461 | 2024-09-28 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9a0ab0f-ff22-318c-b4ec-c7b92f5b8aae | -4.06242 | -54.10162 | 2024-09-28 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44a4bc84-ebd7-3f8c-92a1-79784db0e383 | -4.8684 | -42.7584 | 2024-09-28 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b85ce230-0b95-33ba-8042-2cb52f09ac2f | -7.769 | -44.668 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 1021225c-6362-3352-876e-176d42eae3fa | -2.02328 | -48.78107 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 198f57d1-791d-3b5c-981a-f79a761cb33b | -6.24439 | -35.21007 | 2024-09-28 04:19:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ac7dc79d-c095-3686-b56b-714803c4c5d7 | -6.24389 | -35.21358 | 2024-09-28 04:19:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| eafd70c0-42dd-3566-bbc6-f4c5a962a2e5 | -6.24092 | -35.2085 | 2024-09-28 04:19:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| b208dd05-89d4-3a58-9ba1-22496a8209e5 | -6.24044 | -35.21201 | 2024-09-28 04:19:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 17f6b15f-13ad-3454-8635-8e21cb7f3339 | -6.23896 | -35.20928 | 2024-09-28 04:19:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4327c7f0-f793-31fb-b9e1-fcbcb96a19b8 | -5.07369 | -37.72343 | 2024-09-28 04:19:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 16f51445-ca08-326b-9148-5849daca6956 | -5.06921 | -37.72275 | 2024-09-28 04:19:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 919f3647-cd20-3517-8916-092190e8ca9b | -5.06856 | -37.72723 | 2024-09-28 04:19:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 15.0 |
| e69dfa7c-6172-3deb-b37b-1f0c08ad4220 | -4.60726 | -37.65918 | 2024-09-28 04:19:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d4197b05-747b-3e9f-8bf5-ec11805f9c9e | -5.08069 | -37.98407 | 2024-09-28 04:19:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4cfe1b37-f241-3475-8fdf-5de9811bb4b6 | -7.14091 | -38.77996 | 2024-09-28 04:19:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 17611820-aace-33b5-851d-9924efedc803 | -6.41354 | -38.82405 | 2024-09-28 04:19:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9dd8b08f-0cff-31b1-89f6-b5856f19a5c1 | -3.84696 | -38.45084 | 2024-09-28 04:19:00 | NOAA-21 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d4e90e59-fbda-367e-86f2-0a66b9e1f658 | -6.94041 | -39.41594 | 2024-09-28 04:19:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7b7b94ff-a1ab-3564-a693-c6520d364727 | -6.93988 | -39.41949 | 2024-09-28 04:19:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e2601232-0edf-3e7b-927f-39a28e5c34c5 | -6.93908 | -39.41848 | 2024-09-28 04:19:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b9bdb9dd-c0fa-3fce-ac82-34d5f136884e | -6.93539 | -39.67782 | 2024-09-28 04:19:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7e897b87-9652-3dcd-a50f-cd0ce316fc90 | -6.79543 | -40.14581 | 2024-09-28 04:19:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 41d2f89d-74b1-335d-b01f-a09c8c119fb5 | -9.04129 | -40.56093 | 2024-09-28 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c02b3b02-9a38-3af6-8e77-3ff2fdf17399 | -8.53607 | -40.31445 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e6bd8921-51f0-362b-8004-a3ebbf6e4819 | -8.43661 | -40.38852 | 2024-09-28 04:19:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| edb374ed-4901-3e76-81d9-1ef4e66051b6 | -9.49802 | -40.37094 | 2024-09-28 04:19:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54d72299-7992-3d71-a0eb-f1d77a97cbf0 | -3.40459 | -40.47425 | 2024-09-28 04:19:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ef9d9169-3390-3d0c-9e4d-12518a50424e | -3.40392 | -40.47856 | 2024-09-28 04:19:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5f8c5eb9-923b-3282-a8fa-bd077e7aa8c2 | -2.94838 | -40.41963 | 2024-09-28 04:19:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3a8e120-deb4-3c6a-842d-4bdbe6fcae2e | -7.06562 | -42.08723 | 2024-09-28 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| a9d86e1f-bad6-39db-a6f3-b925d11c5216 | -7.0593 | -42.05766 | 2024-09-28 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7323b4b1-7d6b-3456-80ab-690eef6dcaa9 | -6.92149 | -41.98811 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5d5d5894-f29f-3a0c-b076-0d129a4a92f2 | -6.86269 | -41.70357 | 2024-09-28 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| cae62564-6ede-3491-8e32-9aea28f9e7a0 | -6.85911 | -41.70302 | 2024-09-28 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 47.7 |
| daf6736a-50bc-3620-87ee-157b321b4bc4 | -6.7973 | -41.23823 | 2024-09-28 04:19:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e4ed5b3-a235-3c87-b3e7-a574603d9d8d | -6.79667 | -41.24254 | 2024-09-28 04:19:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5f3cbcc5-0d13-3a76-a898-ae5d631d025d | -6.793 | -41.24202 | 2024-09-28 04:19:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b996ac92-d1d6-3a82-9efa-aa8ad3d566db | -6.78932 | -41.24154 | 2024-09-28 04:19:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 87eae62b-9d21-34ce-825d-146264be6442 | -6.78756 | -41.22801 | 2024-09-28 04:19:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ed781d79-b8e7-3b44-8ca8-c724fa1f5099 | -6.78746 | -41.22945 | 2024-09-28 04:19:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fe93cb43-fa60-3e83-9640-1222be2bcdd6 | -7.30779 | -42.01921 | 2024-09-28 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dd645f36-1f08-36a2-b08f-5b024a53b068 | -7.28653 | -42.01603 | 2024-09-28 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2abc9420-90f9-3ce7-a5e2-0395a41e46cc | -8.10757 | -41.14881 | 2024-09-28 04:19:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 056e34a2-4324-38cf-a72d-fccfab3af50e | -2.80337 | -41.81346 | 2024-09-28 04:19:00 | NOAA-21 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4023ff14-bef7-311d-8dd4-103b39289237 | -4.09623 | -42.46707 | 2024-09-28 04:19:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cfab5b2b-7a71-3ff2-a378-1b44bd5a3a9d | -4.09483 | -42.46723 | 2024-09-28 04:19:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48b57d78-e03a-3be7-ad25-b77b12d33730 | -3.96569 | -41.5104 | 2024-09-28 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0eeb922f-73ad-3947-94de-4bc76ab385ce | -3.9229 | -42.26889 | 2024-09-28 04:19:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4a8984c8-d6dd-329b-afe7-ea8734105495 | -4.25764 | -43.03329 | 2024-09-28 04:19:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 661a9971-7d0a-34e4-89ba-60412363c4a6 | -4.87233 | -42.75531 | 2024-09-28 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8060e1d3-c48f-31cb-86f6-58fc85a70c62 | -4.86895 | -42.75481 | 2024-09-28 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26f68b49-9f9e-3101-9b0d-ea16e94794ea | -4.86728 | -42.76561 | 2024-09-28 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8147339-c22a-3737-b66e-c570e55c867f | -4.86522 | -42.89014 | 2024-09-28 04:19:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bdddfa7-a723-3f28-9875-495ff14dcd57 | -4.86058 | -42.78669 | 2024-09-28 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7de00257-c094-3179-88bd-9f646d3fa4f9 | -4.79793 | -43.03659 | 2024-09-28 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a58678a3-5584-34a7-aedb-c1749665dca3 | -6.10622 | -43.17585 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 77f6b113-80d6-3d34-b0ab-a53c245a8fd2 | -6.05591 | -43.18997 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e5891c2a-b9cd-326e-93fd-08a2b20cb47e | -6.03645 | -43.38411 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1c3d93e8-5178-3b34-be5e-a09a49739463 | -6.0359 | -43.38765 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a3e95494-fb18-3e53-98c8-340ee09bd093 | -5.94404 | -43.38812 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 578decf2-97f3-3640-ae60-f20d50ea7710 | -5.94124 | -43.38406 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1a45c754-4ca1-3e61-9c2d-4da074df444f | -5.9407 | -43.3876 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24617c06-22bd-323b-82b5-9aff021d52f0 | -5.9379 | -43.38354 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f7b863bb-91ca-37a1-a697-24e1a26a6d07 | -5.93722 | -43.34352 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6c609503-ba99-3d73-9dae-ba63cdbe7ba7 | -5.93333 | -43.34656 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 82c6541c-2185-3930-b7d5-b940ae9ab122 | -5.70628 | -43.16953 | 2024-09-28 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f2a9807-4f52-3383-8e88-2417735e1f6b | -5.70291 | -43.14698 | 2024-09-28 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 36050f38-8dc0-3b5e-aca0-9234549705ce | -5.70236 | -43.15057 | 2024-09-28 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0cf318bc-994d-338d-88b7-d24d5509640a | -5.52523 | -42.75471 | 2024-09-28 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 017ab67f-fac7-35af-8566-4624c37a3623 | -5.51619 | -42.74586 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ac8adbab-6c4d-33b3-ab32-731c6bec3995 | -5.93388 | -43.343 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b1cd9a2-6f17-3df9-b9eb-b9408052a740 | -5.93369 | -43.45512 | 2024-09-28 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bff7f030-ba86-3fcf-a42c-407e052480ee | -5.78412 | -43.23615 | 2024-09-28 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 315da426-0bdb-3c31-8087-79165b84e728 | -5.70372 | -43.35795 | 2024-09-28 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dd218a6-63df-3a07-b92b-7dab3dff0d8b | -5.69983 | -43.36099 | 2024-09-28 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a620ee8-a352-3cf2-bbfd-c2e97a2928a0 | -5.68739 | -43.2249 | 2024-09-28 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba1a62d1-828a-3dec-9901-b0b261040eb4 | -5.6643 | -43.37364 | 2024-09-28 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ccd19c3-0acc-3ee4-9b91-173b170ef583 | -5.65763 | -43.3726 | 2024-09-28 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README37.md)
