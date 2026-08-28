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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 703e20e8-53fe-3904-8507-fa674c7303ad | -15.16519 | -41.27134 | 2026-08-28 16:05:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f487256e-92f0-3b88-b5a4-17f985590fe4 | -7.52943 | -44.45506 | 2026-08-28 16:05:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ab4d5db5-fb19-314d-99c2-f544ff218ca5 | -14.20487 | -45.28343 | 2026-08-28 16:05:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c6fe87f9-9f7a-39ac-bbc9-945f1b33ce5a | -7.09747 | -42.82855 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 05f8c9ca-c82d-3003-8d3c-4ce92c794147 | -7.62502 | -44.81308 | 2026-08-28 16:05:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f11b0fa1-b12a-371f-8bc0-9e18b3adaf10 | -8.06881 | -45.85173 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6f5d6fca-667e-3b25-aaed-62a6d052ccd7 | -14.90808 | -40.94164 | 2026-08-28 16:05:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 1a0bbb20-5232-3f3d-926e-a5fd9955f040 | -6.91823 | -38.48832 | 2026-08-28 16:05:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 31b02d0a-0d41-30db-9e82-ea71b93fe170 | -9.70597 | -48.1367 | 2026-08-28 16:05:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 04c8f0ba-f303-31c1-b218-dbfd43b11538 | -8.07589 | -45.82859 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 5625324b-86cd-3f4f-b0f5-4821a216d4f3 | -16.85376 | -42.05322 | 2026-08-28 16:05:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| aa980996-1436-3555-ab99-277048dbcc65 | -8.16435 | -46.17762 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5dea24ab-0572-3d0d-b3fc-f3170b5463bd | -14.67205 | -41.05153 | 2026-08-28 16:05:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 35697f7c-5f94-3894-944b-1f7ef5157619 | -5.96219 | -44.80527 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 1520da99-726e-3544-870d-0454d674cc1d | -7.12659 | -42.7464 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1eb0a4a5-6615-3bbc-a1ab-d3d699219a29 | -7.27504 | -49.8627 | 2026-08-28 16:05:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 5eeff199-f306-3f5a-b94a-658dc6192a88 | -8.0738 | -45.85095 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7accfc9a-de20-3b46-b35e-bdcf8d13c001 | -14.21804 | -45.30491 | 2026-08-28 16:05:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d8c314a-d1a4-3298-bfd5-6727052caa69 | -7.71678 | -43.92527 | 2026-08-28 16:05:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c8ace91-eda7-3ad4-8123-163063b2c686 | -13.60148 | -45.7757 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6f015e94-1644-3760-b0d6-3cc5835a10e6 | -8.09398 | -47.57731 | 2026-08-28 16:05:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 49869604-d21c-3f39-89bd-4579a29e82ef | -19.595 | -46.53608 | 2026-08-28 16:05:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 45b47166-c669-33df-899d-9b0fbfc1dc36 | -17.27235 | -46.02935 | 2026-08-28 16:05:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 348600af-ff9b-33fa-8033-affd46fdb817 | -12.42735 | -42.88775 | 2026-08-28 16:05:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0757a8cd-1eb6-301b-bccb-7603d865512e | -14.49773 | -40.3358 | 2026-08-28 16:05:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| 2fb705e9-14e1-3750-9ff3-c81bba4bc6e8 | -5.95701 | -44.80131 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 4526dfa3-ca27-3661-ad2c-d76abd0f1722 | -5.95036 | -44.80432 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1e886f33-4d27-3deb-acc3-87d32c8095f2 | -12.66105 | -38.78302 | 2026-08-28 16:05:00 | NOAA-20 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| fed3458b-8c9a-3764-8766-03be8652d5b9 | -8.66971 | -49.54109 | 2026-08-28 16:05:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 61c224a7-a258-334b-a0b4-d54beabe7f43 | -13.59612 | -45.77648 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1ae1d639-b6f2-317c-ae8c-c6e400b60852 | -17.82174 | -40.18597 | 2026-08-28 16:05:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a41c9375-00d8-35a3-9eab-435aca791431 | -12.38988 | -48.18899 | 2026-08-28 16:05:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.5 |
| ebc01ce5-7872-372c-86ad-beffd9815a29 | -14.18545 | -48.77421 | 2026-08-28 16:05:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 96945f81-c123-3dca-ba9c-9001c53f2571 | -8.95625 | -45.73618 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c1f6aef8-f78f-32de-8c78-750c2da3c46e | -8.06727 | -45.84016 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| fcf919cd-8b23-3611-b062-0f2964ec21d2 | -8.07187 | -45.83658 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| b7402c08-bc67-3206-b726-aba7bc340a98 | -6.4745 | -38.29213 | 2026-08-28 16:05:00 | NOAA-20 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ef4ca4e-99ee-3f75-88da-8c9edc87c8b8 | -7.20049 | -42.73488 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 20f9ad56-905a-3e1e-9c30-1d3be55a9140 | -14.24155 | -42.62112 | 2026-08-28 16:05:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6d12fb67-e037-3f4b-a804-3d02be9008f2 | -15.49302 | -41.14838 | 2026-08-28 16:05:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f7032e2b-024e-3fc2-9074-2f1aaa1a7157 | -14.21316 | -42.82088 | 2026-08-28 16:05:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 23a258d8-6b7a-3e40-8f38-3d0ceea6cb5d | -5.0168 | -37.6372 | 2026-08-28 16:05:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e31d8cf8-b369-32ad-86f7-d960a4787b14 | -6.7598 | -46.1365 | 2026-08-28 16:05:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 838e8bf9-93cd-33cc-a426-0c9ade6cc573 | -13.32782 | -48.19156 | 2026-08-28 16:05:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 25c5d9b1-0bea-389f-8da4-0a9b57f098f1 | -8.31915 | -38.7403 | 2026-08-28 16:05:00 | NOAA-20 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b5027758-12e4-398e-9e93-77963b3c6107 | -8.09221 | -45.83646 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ee0dd47-3da5-3ec7-b360-550c38126bf3 | -8.82742 | -49.64036 | 2026-08-28 16:05:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| e2c9b6d5-503f-3dae-8e66-fd14069083c0 | -9.15153 | -49.96702 | 2026-08-28 16:05:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 166c3676-0cbb-36b2-9c23-db9d8870567e | -5.95635 | -44.79679 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 23d3ed87-a516-3638-9c33-544beded3c7b | -15.58528 | -41.77596 | 2026-08-28 16:05:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 835fc4c5-0c09-3b4b-8bf8-3363589798b1 | -12.17205 | -38.37777 | 2026-08-28 16:05:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 1d9790cb-2a93-3c93-aa5d-119fc9dc9f53 | -13.32496 | -46.92583 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6eef75c3-63c3-398f-a901-eda1670708eb | -13.33121 | -46.92926 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ab6e01f1-9c5a-3e79-9963-ec03a100b2b0 | -5.34267 | -37.03799 | 2026-08-28 16:05:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 10.9 |
| f0a2ad89-d1ba-3a2f-aa3d-46b13bf98dbb | -8.50956 | -39.58186 | 2026-08-28 16:05:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8e7f6286-0fa5-3142-a282-30ccf0239dc9 | -9.48245 | -45.62905 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 48dc98b8-98df-387d-a3a8-8d66ea05f803 | -7.16915 | -39.52899 | 2026-08-28 16:05:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9a51d902-d102-3f6b-8e2c-b6e0075a2e52 | -14.60247 | -47.97504 | 2026-08-28 16:05:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 77e92b86-f8b2-34bd-a588-2d1134ffe087 | -12.78038 | -45.94383 | 2026-08-28 16:05:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9c36a62d-4bb5-31d3-bac6-a4fb63d70625 | -13.64695 | -47.74965 | 2026-08-28 16:05:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ce391ee5-a62a-32c0-82d5-67e0592d93b8 | -7.08001 | -42.20534 | 2026-08-28 16:05:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a06594e4-160c-3440-aa6f-d8df6e0556ef | -6.93674 | -42.67579 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 7284e24c-4d57-365a-9ac4-223130a64fe1 | -12.76995 | -45.94798 | 2026-08-28 16:05:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 393514df-e75c-35f8-994c-8d77ae04a84d | -7.17559 | -43.17596 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 60e50f61-3595-3c19-a9ed-3901e0f494fb | -13.56884 | -40.53273 | 2026-08-28 16:05:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| bf596a46-1a37-3aaa-9390-72d1c85eefc6 | -8.30671 | -38.74226 | 2026-08-28 16:05:00 | NOAA-20 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2c5138f1-557b-3573-8621-85b3c27a6185 | -8.07303 | -45.84521 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 6617d6ab-157c-32be-b4d6-d2b53cc6b6a6 | -14.23315 | -45.25267 | 2026-08-28 16:05:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3884f96-bf41-3c1b-b64c-fd7f9cf5cd77 | -12.09461 | -39.70519 | 2026-08-28 16:05:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 89d51717-47e2-367a-901b-1d697d286e66 | -6.84724 | -42.82963 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1ef8f6f0-dd40-3b2a-a833-220a952cd6dc | -5.95249 | -44.80186 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c0e8ba47-00d9-3659-bd89-a254ebe89d76 | -17.51788 | -42.00333 | 2026-08-28 16:05:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 9b3386c0-e21a-33c0-befb-3784062bd32b | -12.38565 | -48.20085 | 2026-08-28 16:05:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 6d7a4941-6f6f-3c83-923e-0286b8af4b53 | -6.24928 | -43.4321 | 2026-08-28 16:05:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df6b5c1f-9b13-358b-884c-7ce386dc4fc8 | -15.72605 | -41.19106 | 2026-08-28 16:05:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 343b1477-f55e-366a-a201-939db00b6570 | -11.71231 | -37.66678 | 2026-08-28 16:05:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 9abe60cf-22e6-3c1b-a433-098bbe79b8e1 | -8.08761 | -45.8401 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 48a9df87-d86a-36a6-8f28-fb6e38c61d68 | -12.25817 | -45.06844 | 2026-08-28 16:05:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd4fa6f0-0489-3e8f-a44c-e5a0fde3c524 | -12.38623 | -48.20578 | 2026-08-28 16:05:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d121e47e-00b7-3ec3-85f5-c76b70a3e935 | -13.32544 | -46.93003 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6423a466-fe53-361e-bacb-777f3a61130a | -7.58185 | -44.01667 | 2026-08-28 16:05:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6180409a-babc-3a50-8e67-d4a59933be37 | -8.96166 | -45.73833 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| cfd4f13b-b97e-383a-b53a-6e4428659bfc | -5.95182 | -44.79728 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 356312df-377c-36ba-8f78-bf06b043443c | -13.1807 | -43.47622 | 2026-08-28 16:05:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a9eaa94f-fb0f-36af-aa7a-8f2be9b2c200 | -8.95586 | -45.73328 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8b5871c3-d05a-3a2f-aa53-f46b475b3064 | -6.94114 | -45.6871 | 2026-08-28 16:05:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| adeda252-58e8-3d02-80e1-c88ab6929302 | -7.10396 | -42.19376 | 2026-08-28 16:05:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 3bffbd71-a8dd-3fd3-8195-7654003d97d5 | -15.71658 | -48.2538 | 2026-08-28 16:05:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 883d937d-a843-344f-a9d5-b991eb1e27b3 | -8.06804 | -45.84597 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 3ad12d93-b355-3b9e-9434-281c44fc2aa7 | -9.49569 | -45.65137 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 117fa6c9-87a0-38d5-83b6-2354442a2bd3 | -16.05943 | -42.13507 | 2026-08-28 16:05:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d09826a5-3256-3a05-a112-95aac967c427 | -7.74071 | -44.73552 | 2026-08-28 16:05:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1aea9a84-1a84-3ff8-b85d-bd6cd007258f | -7.08852 | -42.79404 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ce7633f8-d733-387d-b7f9-ef7c482596ce | -17.93251 | -42.60855 | 2026-08-28 16:05:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 630778b1-ff97-3f66-8b0b-93b16631aa6a | -8.9634 | -48.17223 | 2026-08-28 16:05:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 649a7cdb-7b06-35f5-9729-0589eb186868 | -13.31202 | -46.91493 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eed20582-ae09-3021-888d-9432313392ce | -16.26629 | -40.85724 | 2026-08-28 16:05:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| ddf6afb9-f05e-3aea-894e-027712e7ad2b | -8.06344 | -45.84962 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81f88e01-c712-323d-a2d3-2d1d64d79624 | -16.85947 | -46.63591 | 2026-08-28 16:05:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b86392de-c4d3-362f-9c7e-09c62e0c9f76 | -17.05591 | -41.23799 | 2026-08-28 16:05:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README90.md)
