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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17c19544-0e10-3a19-bd19-49616b520a15 | -6.14127 | -41.76922 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3f07e380-54dc-3458-be0b-6ace315ebbd9 | -5.53857 | -41.32568 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8f2be918-f7de-3c50-85c0-f59dc73fe401 | -2.94567 | -49.34342 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e329a69a-7fe2-3a5e-9e54-9fd8e504a216 | -5.42451 | -44.21744 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8df54a98-750e-39c4-a044-f165df8ac82c | -6.21978 | -42.49402 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 36e6f708-10c6-39a7-ba57-c9a5a45b86a0 | -5.48918 | -45.83358 | 2025-10-15 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ceff842e-757d-3d54-a4f8-a80cf61ac030 | -3.52878 | -50.31018 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 201afe39-9d6c-3597-b40c-c2969c6bfe6b | -6.05503 | -41.90497 | 2025-10-15 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dc135511-1d1c-3502-a35a-37d829747311 | -6.43229 | -41.71225 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 555baeb0-5fea-3345-b305-29b71c600da0 | -7.07692 | -41.95383 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b6388390-5bcf-3754-bc81-693eaa66f0c8 | -5.67921 | -44.26068 | 2025-10-15 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1572265a-7a4e-3442-9572-1e18db3b1305 | -5.84115 | -43.95623 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76d5bb52-6741-3eba-b861-715a58c3a252 | -7.95595 | -44.14625 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c58af77-9c42-3cc8-864b-947be144d91f | -4.87929 | -42.76432 | 2025-10-15 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d44c40c1-1403-3507-821d-ead77a827bee | -4.42287 | -47.75846 | 2025-10-15 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87509227-aeea-3195-9f59-d5fce9826111 | -5.27364 | -41.04742 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 11f22af0-1faa-397b-9505-bdb842e16f78 | -5.90115 | -43.9648 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e2a5c1d-54f0-3890-9b90-a20c10bb0b04 | -4.14733 | -44.18806 | 2025-10-15 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f1b6626-96e5-396a-af7f-134cd479e8f3 | -5.44183 | -44.22459 | 2025-10-15 04:06:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 7f89c4e8-2bb1-31bd-a343-3fc231dad047 | -3.83648 | -44.54978 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a7dcebb5-ab31-3a52-847d-8409765b7f34 | -8.2264 | -43.39191 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f43f67f4-7faf-3ecb-a1d0-8c37696f35fc | -6.19263 | -42.59969 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8a14eac9-feff-30ea-8843-a4a4d6789190 | -5.91765 | -42.82953 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 494c8273-2ae0-3535-bacb-007f88499ad3 | -5.8879 | -42.88478 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e172c4b9-41a2-3ecb-95b2-de266ddc99ac | -6.1948 | -41.75291 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b604f1ee-57b0-357f-b724-4aebf850653f | -4.77066 | -45.73049 | 2025-10-15 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7fd86d27-2105-3ead-b935-392ad9e1fce8 | -5.42331 | -44.42836 | 2025-10-15 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2c5a422-9252-3867-957e-fd781dce1467 | -5.26044 | -45.61334 | 2025-10-15 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1919a3fc-c1c6-328a-87fc-523115285e2b | -7.5737 | -42.69566 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51099243-851d-36a0-98ec-6904bce9f02e | -6.33163 | -44.01454 | 2025-10-15 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6828566d-0388-3194-becf-fb1768c38c27 | -6.15065 | -41.77431 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 48a89d0e-983a-36b7-8b75-0333411dd088 | -5.34232 | -42.56456 | 2025-10-15 04:06:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 18689112-c412-3bb4-9e3f-266a56d0e5c1 | -4.72254 | -44.82127 | 2025-10-15 04:06:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7d1841e-f942-3c18-acfe-d4d251fa5335 | -5.62871 | -42.68407 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 923561f7-3e34-3174-9b29-7afca381b90c | -6.57566 | -42.96788 | 2025-10-15 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce4ca141-bfa1-3903-b0e6-c81cb2c56fef | -4.82157 | -45.4466 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cd62009-2fe6-33b0-961a-f9436c418285 | -6.17129 | -44.30534 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b73106e0-7f35-33c9-b509-9d0aebab7bae | -6.06961 | -44.30666 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94c966ad-3a52-365b-8cf6-a2a8a5098c97 | -5.35093 | -43.73852 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a94ec1f6-9293-382c-90ca-7df1e15b9c91 | -7.94961 | -44.1412 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a45cf75-d4b5-341f-93a9-50cf6a2a3b88 | -6.4234 | -44.02969 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0dbebfec-5ea7-34c6-93a8-a1c5356cfbfd | -4.90413 | -43.45659 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 439d25af-7f3d-3cc1-bada-13acb95aebce | -3.42565 | -50.25158 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 557a77f0-6f59-33d7-b279-3ef5f8669357 | -5.39713 | -40.88683 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 107f7bcb-9849-32d4-a805-eb4b61fd91f3 | -8.1802 | -40.44418 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b45e70cb-18b2-3e55-bac7-3de753b85bee | -3.93764 | -47.56554 | 2025-10-15 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edc54a07-4913-377a-a53f-3db28210aff2 | -6.23419 | -44.16815 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 10455fe4-7e4e-3c61-b692-188b67c1302a | -5.95675 | -42.30653 | 2025-10-15 04:06:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a876e682-73e8-3eda-9c33-bee9e04aa131 | -9.33246 | -46.11014 | 2025-10-15 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcda337c-ee75-33a8-9abe-f96ef71cafed | -5.95858 | -42.25242 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e1e6093e-e78e-3154-a14e-0f31cfccd68b | -3.07532 | -49.50364 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa954116-9083-3ef5-89ba-faf2252adc65 | -6.26309 | -44.34036 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f01f55ba-32db-3478-8d88-3a865347aea9 | -6.97395 | -41.68116 | 2025-10-15 04:06:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 52834aca-763c-3624-af8f-7086ecb18853 | -4.65635 | -43.12722 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 58c0948f-348c-3213-8974-98b97b877f65 | -5.62929 | -42.68044 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 29b476d0-28ca-35b1-8ccd-86d46c95f023 | -5.8764 | -42.82669 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| db4f5fe6-4fc0-3beb-9acf-fd0984b00aaf | -3.83133 | -44.55183 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 614483aa-afff-35d4-9a5b-b97313c71720 | -6.14899 | -41.74207 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe165515-0796-3171-9bf3-993a71d54e06 | -4.65289 | -43.12667 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 66904108-2b2d-3512-acf9-13470cd483ca | -6.84223 | -42.78 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4f481900-ac10-3d20-b383-a7f68ad03f8c | -5.42023 | -44.22099 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08563c02-ae13-3f07-85c9-e8f59a8b0b44 | -8.0602 | -45.92172 | 2025-10-15 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 646c5d94-c299-3bab-92ef-19886ca414c0 | -4.65228 | -43.13046 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 435b2e4b-9eae-378c-b78b-f05b104eaab4 | -6.82755 | -42.77391 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f5b9b0bb-2cba-349d-9b7f-e60fd9c8ad02 | -6.88694 | -43.96736 | 2025-10-15 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9a68ccd-1aa5-3f95-983e-fad1545db20e | -6.40508 | -42.52333 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 434f5ede-1520-3dac-9008-1d7622896306 | -4.42625 | -43.49677 | 2025-10-15 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4fd21d7-8cc2-37c8-b61e-1fac408d27b3 | -5.2731 | -41.05087 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2a144a9e-e78a-36a1-b2a0-5265a6e21614 | -4.89536 | -45.51216 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 897e532d-a6e9-326a-9718-d05af09bb0a2 | -7.57199 | -42.70632 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| df96c9de-7abb-3a74-88a0-72c54cb2b9ab | -7.08078 | -41.95089 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2012f410-95d0-3081-9a63-31f17964add8 | -6.21946 | -41.5545 | 2025-10-15 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 460abb0b-804c-3e6f-a10e-21c2852e40b9 | -8.19703 | -43.98174 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ed4065f-f1eb-3580-bc24-3c238ce4c22d | -7.15553 | -42.50531 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 293f8e83-0f5f-35fc-a7e6-fe8507074d73 | -4.15468 | -43.13222 | 2025-10-15 04:06:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 274e040c-db96-3061-a061-4a9b036d7754 | -6.58701 | -43.91594 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a851367e-6cd6-3c53-a891-42b16481333f | -5.43757 | -46.28896 | 2025-10-15 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 761f2cd7-69fc-31cd-a3a8-42e83cd418f2 | -4.42688 | -43.49284 | 2025-10-15 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3ebf601-4bc6-3f80-b604-cea2fdd5cbe7 | -5.90036 | -38.15349 | 2025-10-15 04:06:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6ed4999c-da5d-35b4-9576-50ebb72dda0b | -7.55299 | -42.71781 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ba830f9c-1eb4-3936-8212-9ecafeb57b2c | -8.22686 | -43.32447 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d52217c3-6015-3cb4-853d-426200ef619a | -5.8602 | -43.86108 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d85dd18-a16a-3dae-adc2-ef5c776a7025 | -4.77377 | -45.73628 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 75549aa5-9b89-39c1-ad82-13b4f627692c | -6.89459 | -43.96462 | 2025-10-15 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84ba1136-8535-3765-b953-4575dd17c1a1 | -4.31527 | -44.53693 | 2025-10-15 04:06:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77a73d4d-fdeb-3645-b3b3-9fe81c3ec0cb | -8.27251 | -43.41389 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 598e62fb-9845-357d-a5d1-e24f75166da2 | -3.42502 | -50.25568 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93aa3855-802d-3c12-b5c8-69c2444d5f7d | -6.85089 | -38.6759 | 2025-10-15 04:06:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a4cfa2db-8c52-38bb-9306-28f88a1e79d7 | -8.72939 | -43.86171 | 2025-10-15 04:06:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d9dc2b5-7c45-32e3-8260-392b5be548a5 | -5.91514 | -42.65099 | 2025-10-15 04:06:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1ecf9e10-cf94-3838-abf3-06eb4aafacef | -3.46524 | -48.98039 | 2025-10-15 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3acdd56-7466-3d3b-93d1-cdfa635be89f | -3.94293 | -47.5618 | 2025-10-15 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd093e11-e472-35c4-b82d-4cc408f519c5 | -8.27751 | -43.42596 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a81649e1-7905-355a-9e62-228c93022958 | -5.91088 | -43.94984 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2457ad5b-881c-3c5a-bc32-af6bc52bc155 | -4.25337 | -47.28961 | 2025-10-15 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b019e154-c843-348c-bb84-a015cde96a7b | -5.56423 | -41.316 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5d0b12a8-9693-341c-87b5-43e67e281b0e | -7.7508 | -42.45952 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 072434b7-62e7-399e-b103-dd462ae3d20c | -8.22102 | -44.09636 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0ac6616-f473-3600-ba62-33b78910b4c3 | -9.11154 | -44.67879 | 2025-10-15 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 873b6d25-1ccf-35ad-9371-9c1d20333175 | -5.3138 | -42.90023 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README36.md)
