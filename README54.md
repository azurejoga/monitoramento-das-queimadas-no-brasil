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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b6d8340-c142-36f9-befd-12af5f783432 | -7.65792 | -42.66843 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4ada50d1-1468-39f0-b58f-adcc77bcb28b | -5.80376 | -59.21515 | 2025-08-26 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d44e011c-710a-3bbe-b5ed-7fb6c78a381f | -3.36626 | -44.18985 | 2025-08-26 04:44:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfc79ffc-7845-3981-9bb5-21546856392a | -6.3553 | -55.80541 | 2025-08-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30d7e629-9938-3ec6-a11e-ff7cfc4d48f4 | -6.31981 | -42.88929 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d560905-95d7-3ea1-8278-a4a1bf808e7e | -6.88304 | -45.65239 | 2025-08-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92eb8c00-9290-3917-9a73-7f6db6d04edf | -7.65836 | -42.66522 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c9264b2-6818-33e8-80e9-a59f64c5c4fd | -3.91941 | -47.69067 | 2025-08-26 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d57b59e-2c0a-3d1b-b2dd-1bcbe2d7df8f | -2.74628 | -48.60604 | 2025-08-26 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9843b6e5-e421-3714-9546-f1a50e78bc42 | -7.52755 | -50.53742 | 2025-08-26 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 972402a2-760a-315c-a2a6-09228bbeb307 | -7.86931 | -47.95204 | 2025-08-26 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f48bd00-fc4e-38b9-86fe-ccde73404881 | -8.10603 | -47.32708 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6195310-e245-3652-a6d9-a75e6a71787e | -7.15518 | -44.17361 | 2025-08-26 04:44:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21cd9d20-c9bc-3344-9d86-43a515f39c21 | -7.19173 | -47.56776 | 2025-08-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0664406-cb2d-3685-b4b2-72202d168d3b | -6.24142 | -60.01849 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 13c9777f-c725-3e3f-a82d-73bb3fed9b52 | -8.37761 | -48.02424 | 2025-08-26 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5e985db-db7f-3aa7-b4ca-49cb6381a707 | -8.24586 | -45.10445 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c568ac6f-098a-38b3-9002-94eb0713d8c6 | -6.26352 | -60.01566 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17edb3e6-aad9-3a52-bd9e-76051550b85c | -6.24029 | -60.02498 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ca729a3e-d0b6-3cf3-a6aa-ef5b9dad6b8d | -2.6502 | -48.05436 | 2025-08-26 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed09e480-127e-3637-b590-1866db12d403 | -6.97956 | -44.12883 | 2025-08-26 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da5e5214-7c52-3caf-a1f7-305b0c2b53fd | -7.5281 | -50.53391 | 2025-08-26 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5eb2c78c-44b9-3230-9066-f5ef0ac574e6 | -8.05855 | -47.35824 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 868bcdec-3377-3c83-9320-1e499e0a2bf0 | -7.59619 | -45.22372 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b08d8098-fa40-3556-a62e-f2eb34cb7021 | -6.24085 | -60.02175 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 74d2833c-58e4-34d3-b5b7-8c620cb96500 | -5.31027 | -60.1945 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e33b559-8778-3db1-95b7-1702996421b7 | -5.7485 | -45.3789 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 667bbe08-7068-3c6e-9162-4e11c6d824b2 | -3.53562 | -49.07323 | 2025-08-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b73c31f5-2c44-3253-b38b-3ac7643ca93f | -5.44151 | -60.15427 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ec86fe2-2d7e-3c99-9c9d-066855d47c78 | -8.23843 | -45.12535 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b41602fc-ea7b-37a0-9d8a-50cf160167a7 | -5.31506 | -60.19893 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da921919-2f87-308f-a9b2-dd25a4af3cd8 | -5.78688 | -46.1382 | 2025-08-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c65b1c01-4b7d-32eb-9f3d-96a3a74c0d73 | -3.91648 | -47.68613 | 2025-08-26 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fa8b785-a482-3767-b292-8b961c166d0d | -6.24664 | -60.01953 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 258d5d5a-1407-30c1-93d9-adc96ca27e41 | -6.08586 | -45.90736 | 2025-08-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45db15c5-ff8e-38ba-b39f-543d53f2748d | -6.89088 | -45.65706 | 2025-08-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d80ecd1-f02d-3cd0-9daf-78d480c99253 | -5.5544 | -45.20206 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b745d1bc-f130-3c59-aaa9-b6ff330c7b44 | -7.63458 | -45.234 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7032136-59c9-314f-9706-2d914c7c86c4 | -6.60941 | -47.33061 | 2025-08-26 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a882cf3-89ce-36f4-8359-16cd0d7f4112 | -2.58758 | -51.925 | 2025-08-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef144fb3-7983-3304-9996-ba59ea1e040c | -1.15819 | -54.20318 | 2025-08-26 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfdb84ce-da37-3590-ab82-a814630edee0 | -6.31115 | -59.86739 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d385c79b-d14c-3155-8200-7a744c1d411d | -6.34594 | -43.6627 | 2025-08-26 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e9a8b0f-cd11-3b58-98fa-976a0e71aaa3 | -6.25425 | -43.83277 | 2025-08-26 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d5cb2ab-764e-325e-a90c-91c16ea2e932 | -7.57871 | -47.49342 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2113de18-d375-3279-bb97-9dbed828cea8 | -8.23793 | -47.45136 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6d0592c6-b183-3862-a3a4-6eb83b47a0bd | -5.85877 | -51.75299 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9993679-1089-3027-9f2f-7bb93ee3c634 | -6.69872 | -48.38075 | 2025-08-26 04:44:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bac13867-1f43-38c1-a100-c5bdd8feb923 | -6.3894 | -45.59921 | 2025-08-26 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 39bba97b-85f0-312f-98b2-db14537cb3e8 | -8.1199 | -47.12974 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a705d64d-e394-3bc7-af6b-439622c84f58 | -7.22137 | -44.43471 | 2025-08-26 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02c94fb6-fe88-3320-a4bb-16508bfb9ef3 | -8.90773 | -44.85275 | 2025-08-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbb18487-55a4-3ba4-8503-7239a92686f0 | -7.65224 | -45.40252 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70c58b69-2024-3e62-9598-1be2a9c3b1cd | -5.56982 | -42.62833 | 2025-08-26 04:44:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ca5db263-8a41-32eb-a02e-65a30d334951 | -7.15133 | -44.17533 | 2025-08-26 04:44:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 093eddf8-b77b-3e7f-ad35-052d56333f5e | -4.89232 | -55.81123 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0bd6f91b-a32c-3ef3-97dd-9d016cd437c2 | -6.23619 | -60.01744 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7cf7aacf-a095-38ea-a328-3ecee5ecda85 | -3.25458 | -46.91461 | 2025-08-26 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2af4a30f-ca42-3ac7-a251-50bb70b363f7 | -7.74759 | -50.28166 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 60e255eb-52aa-39f4-8c5e-27b0035aef90 | -3.20304 | -49.11681 | 2025-08-26 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 424f70c5-ee67-37c6-bc5c-c3d66b24338f | -5.52301 | -60.21035 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b022a27-9918-3076-96ab-daca21c0df90 | -5.57485 | -42.62907 | 2025-08-26 04:44:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 15c63896-ff05-3e24-a443-5a2cd79ab4d3 | -7.44488 | -42.04689 | 2025-08-26 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d73548b-503d-3397-8284-4da2e040aa85 | -3.17033 | -49.47931 | 2025-08-26 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b67af58-522c-3ce3-b411-116cb0eab990 | -7.58896 | -43.95776 | 2025-08-26 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 013de138-3df0-3d61-b147-8760527b7f08 | -5.87218 | -42.41218 | 2025-08-26 04:44:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2b45ca6c-c22a-3a2a-9497-87b06148d8de | -7.73758 | -50.3019 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cac74d92-92dd-34ab-843d-2577fd290798 | -6.24369 | -60.00533 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96281287-642c-35b1-b88c-91c8bc795bb6 | -4.86008 | -47.41683 | 2025-08-26 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27014dd4-2317-315a-9470-712c78ea56b4 | -7.65229 | -42.67089 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 179d0287-71f2-3599-b396-664d3f3ccede | -6.39623 | -43.51786 | 2025-08-26 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b3c0335-604e-3c31-9699-57d820a49327 | -6.39588 | -43.52094 | 2025-08-26 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcd8933d-60b6-38f2-8d52-c08199b6d930 | -6.73412 | -51.97525 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0c04c39-236f-3130-933e-050412b8ecfa | -8.42929 | -48.25458 | 2025-08-26 04:44:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93aa031e-b77e-35a4-8e90-92b05da381f4 | -7.17042 | -45.15532 | 2025-08-26 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b649dcb3-6f66-3429-b497-2b2cef962118 | -8.28743 | -46.33435 | 2025-08-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac780c56-63f1-3bf7-a623-9b28d6c815ec | -8.11284 | -47.12413 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fdfc47c-e17e-39a1-85c8-3a88f7633413 | -4.82344 | -47.31402 | 2025-08-26 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39bef182-6ed3-3157-a341-4ae1df7dd805 | -8.24526 | -45.10869 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 371730d5-43e0-3ac0-9c17-cbefb2d83585 | -8.12058 | -47.12513 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3e221307-472e-36ea-8b71-fbec5e1ee29f | -2.89141 | -49.48248 | 2025-08-26 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dea75dce-da25-3ed3-8216-437f1e6f800c | -6.98819 | -44.1347 | 2025-08-26 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a97aa81-d9f3-372c-85e8-a6f3b356ae1f | -6.25938 | -60.00834 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4033cf3-2f2a-3a9c-9f47-1e869dc7345d | -5.79372 | -59.21361 | 2025-08-26 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 560877eb-5818-3468-b1b4-8dacf3314853 | -7.60051 | -45.22446 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0a39c71-9b24-3805-8c32-548a05dde6f3 | -6.65388 | -53.18362 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1f8a5f8-d688-3c35-a6d7-372c618f8ac8 | -7.27317 | -43.34691 | 2025-08-26 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f50e673-ce03-393b-ad05-a22ba7bb79ac | -5.4421 | -60.15088 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0777f95c-af3d-3284-bbf1-ac6990a5b050 | -5.87964 | -50.15471 | 2025-08-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 864ae512-9ba8-3250-8d91-77aa74ea0e56 | -5.5545 | -45.57056 | 2025-08-26 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d5b9bed-375a-3f59-9e3e-82e21ca4d348 | -6.23789 | -60.00763 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5546e862-659e-33bf-b873-abc3b7dd9ab1 | -3.98286 | -47.88658 | 2025-08-26 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7b8b71a8-c396-34b4-b8b0-57b6e789c3de | -3.06132 | -40.04844 | 2025-08-26 04:44:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2461f55b-4ca4-3546-82b0-90b666c15d44 | -3.37653 | -52.71307 | 2025-08-26 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a8408c0-3ed4-3aed-abf8-4ca781007834 | -5.70857 | -45.53455 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 358e96cf-77fb-3db9-b80a-d727dfb3a034 | -7.32874 | -46.10093 | 2025-08-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ecca92f-c7a2-34a1-a021-4180043efdd1 | -4.96348 | -55.81198 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7c7d579f-7ae2-3867-8aec-a527f6943e82 | -8.12907 | -47.1212 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 102e4472-ffa2-3dc0-8266-dfdd38120ba0 | -7.89556 | -45.87739 | 2025-08-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d08ebe4-d76d-3244-ac2f-9aa8648c2360 | -2.58418 | -51.92447 | 2025-08-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README55.md)
