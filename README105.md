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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26e08426-5125-3ef9-ad56-c0cb867fa50a | -8.90356 | -46.06683 | 2025-10-02 04:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea8489cd-3d16-3bde-a630-b65f7781b011 | -5.83026 | -44.99034 | 2025-10-02 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f5376439-d680-3bc3-8926-02f60baf82ac | -9.03327 | -46.68074 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69a86b25-d841-3166-a4d0-cec5d6a512a1 | -7.78112 | -42.51191 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c0738176-0342-31b3-9d12-32b058417ce3 | -8.68287 | -47.69238 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55964472-0f21-3b20-9485-5fa583ba6b7a | -6.32168 | -43.04118 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45755549-7f01-3aa9-bc7a-bc3a4c961621 | -6.69601 | -42.81612 | 2025-10-02 04:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 189e4a86-15d8-3946-9b90-501420306b4f | -9.0781 | -46.7141 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdd301de-030d-3334-8202-262f45c5a5c3 | -8.88792 | -46.60112 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5023180-4449-3185-a7f9-e2b46a62019b | -4.82227 | -49.66586 | 2025-10-02 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d308b39a-088e-3440-a235-9a61187f4240 | -7.59054 | -46.79246 | 2025-10-02 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8bc8ddfe-f40c-3c64-9d6e-6f1fa5c2f47b | -6.48707 | -44.29465 | 2025-10-02 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9c5b10f4-ab02-3c46-9a1e-a9c554c86d83 | -7.80202 | -46.02126 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecf4232d-41d9-3471-998d-4960761f6bfa | -6.78598 | -45.59617 | 2025-10-02 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1756d2a0-aaef-362a-9ab2-19a450bcdcf5 | -6.77339 | -45.58849 | 2025-10-02 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a410638-10c2-3cef-95b4-f8e74e256c2e | -5.24427 | -42.97986 | 2025-10-02 04:49:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 706d8e11-600d-33bb-a85f-3efee343256f | -2.73938 | -48.67456 | 2025-10-02 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c3691f5-2add-35cb-9f19-a285e729d78b | -3.80806 | -52.15633 | 2025-10-02 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c5d996b-1fb2-3f0c-baa8-48a9318ed229 | -8.57055 | -49.60494 | 2025-10-02 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8929d020-f565-3d4b-8d4d-b704cf483ab2 | -5.82807 | -42.86837 | 2025-10-02 04:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 598b5e41-7a46-3e45-b9c2-91edc7e10505 | -7.5851 | -46.79994 | 2025-10-02 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4e20362-53cc-3505-866c-e8e7adcd7b88 | -7.58567 | -46.79588 | 2025-10-02 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b564c8f6-23cc-3c79-b2f6-34bcc92f49ce | -4.62595 | -49.36771 | 2025-10-02 04:49:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c05ad9bd-b571-3bcb-bd6b-7a6cca7946d7 | -2.91688 | -51.9703 | 2025-10-02 04:49:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 788d0e00-7d5f-3a94-941d-69217f178c8e | -3.62521 | -42.77903 | 2025-10-02 04:49:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 642946e9-16e0-3306-bc15-2d5ee3bebbc7 | -7.7721 | -42.53557 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| eee1038d-db4b-322b-ac6d-11015d7758e8 | -5.98477 | -44.55804 | 2025-10-02 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84fd1c9b-3505-3803-b7b7-9c02a9b003b5 | -4.50145 | -50.51236 | 2025-10-02 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56cf4086-4a6b-33aa-89fc-7acee52cc0f5 | -5.61802 | -43.24866 | 2025-10-02 04:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b6a639f-71cd-310a-b708-33448fffac89 | -3.34917 | -43.1933 | 2025-10-02 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b580d593-184c-384b-945d-3f190b7a913d | -5.81002 | -51.86771 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57909009-2796-3165-90fb-adf21d69ecfe | -4.3124 | -48.0962 | 2025-10-02 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1e31888-fb70-3cf7-957f-50fbc1477f3d | -5.23285 | -45.20354 | 2025-10-02 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cabcf013-c34a-361c-8152-5a481eb981c2 | -1.24815 | -54.21819 | 2025-10-02 04:49:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 621c1ed7-ea63-393b-9eac-95900107fc17 | -6.76948 | -45.58309 | 2025-10-02 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8228c6e7-66eb-33f5-bd31-ffd5d1e13554 | -8.55672 | -48.64236 | 2025-10-02 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 318dc7b8-bd2b-352f-9753-4bb65ae24cd5 | -7.76478 | -42.54652 | 2025-10-02 04:49:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 883d4f64-734f-32a3-a7ae-340f6a6cfc52 | -2.74189 | -47.14293 | 2025-10-02 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 481402cd-d689-3571-9038-16e0451b5355 | -7.16952 | -41.70262 | 2025-10-02 04:49:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| acf9ffa9-de19-30b7-bab1-48789db833b9 | -7.55914 | -42.40295 | 2025-10-02 04:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c45fcdb4-351b-3156-950c-4e4170ce9127 | -4.4051 | -50.84209 | 2025-10-02 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bfce0b6-feaf-35b2-b957-a8798664dfde | -6.28051 | -44.05719 | 2025-10-02 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44e6dc0c-1015-307d-91bf-d2f64daed78e | -5.79038 | -45.75364 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba3ab1e8-b557-35a4-b1e0-2c6bdf2e0cb3 | -8.63999 | -43.98688 | 2025-10-02 04:49:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09797424-2d4d-30a4-b86d-a814517fb2c9 | -6.3863 | -43.88132 | 2025-10-02 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e732bf27-d58e-3ffa-8132-69abd970e080 | -3.62571 | -42.77572 | 2025-10-02 04:49:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7759546c-0a3e-3294-a06e-f827bcc7b40e | -4.62535 | -49.37165 | 2025-10-02 04:49:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67b08e83-cf7b-319e-b26b-998ab5552cc5 | -7.00385 | -44.50577 | 2025-10-02 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 403d83d4-4a43-36e2-98f6-df65bdfedb9c | -5.19086 | -45.39451 | 2025-10-02 04:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e37e5175-2e33-3cb9-bd65-b61e27e205cb | -8.84099 | -46.58104 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5b2f38b-0473-3b3d-8e69-e5c30dd1417b | -2.63719 | -48.04439 | 2025-10-02 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9908793f-3f5c-3534-a92a-259860c2140a | -3.46258 | -50.09807 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b992270e-8161-3fb8-b15b-bc31ea264ef5 | -7.78795 | -42.50479 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bccfef21-65c5-3f9e-bb4f-b5e451dee232 | -3.092 | -47.00732 | 2025-10-02 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b625f8d-2251-3bdf-83d2-c6140e7a0431 | -2.6492 | -54.89544 | 2025-10-02 04:49:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d87a7470-7059-31bc-a53b-90ffd0682502 | -6.46409 | -44.20301 | 2025-10-02 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 146a9d84-9a4f-34da-a869-c1e3e388bca7 | -7.3108 | -42.87922 | 2025-10-02 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 99cf8ddf-9fac-3aa4-b994-c7ae39e04cdb | -8.90541 | -46.6633 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7ca21f6-a2c3-3e53-8646-af321d51dcce | -7.03402 | -43.33868 | 2025-10-02 04:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c2be15ac-68e8-3d8d-b035-400c48f99ca3 | -7.78058 | -42.51599 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1fe2d2f2-4269-3893-ae4d-0cab4b20152c | -8.55917 | -44.66514 | 2025-10-02 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6dadea76-2005-308e-932d-8ba03faaef3b | -8.41211 | -47.75518 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a34108ef-3a6f-3940-9c6a-a0160b9b730f | -8.84602 | -46.57748 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72702007-5c12-3f43-b395-6d0ac3f0e1b9 | -7.51449 | -44.28124 | 2025-10-02 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a60290e-d1c5-36a7-941e-fa11d0b16be4 | -7.89239 | -47.27565 | 2025-10-02 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9afb1809-3af3-316a-adde-d574bb47c7a5 | -3.51732 | -49.26398 | 2025-10-02 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30899ddd-9069-31da-9e27-7a2144af1d3c | -3.80811 | -51.31611 | 2025-10-02 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ebe5d7d-fc68-367c-b5bc-ba21285e883c | -6.05181 | -42.67778 | 2025-10-02 04:49:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c249d4a5-e18f-3ed9-a5fe-182b70c3dcd6 | -8.55957 | -44.66222 | 2025-10-02 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9f0ce7d-d569-33d8-9a1b-8aab6e73a681 | -6.54871 | -43.93579 | 2025-10-02 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9ab8e16c-a488-3b25-a1ba-7c42593bfa93 | -7.791 | -42.52576 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5e498fe2-a6cb-379e-9183-676a00fdee48 | -5.6386 | -45.96927 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2367529-842b-38dd-acb4-bfb6ca11a959 | -8.89098 | -46.60417 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0716341b-be79-3b1f-85af-1f8245886e4e | -3.68692 | -49.0539 | 2025-10-02 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b209b07b-8032-3d43-8345-3f6e74f56834 | -6.76879 | -45.58462 | 2025-10-02 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd7f0c42-ad38-3707-a4d2-c14e541755b2 | -8.51411 | -47.7961 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eeaca1e7-b92f-3c3b-8625-c33ce5f5ca73 | -6.56236 | -43.87715 | 2025-10-02 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c5a2464-6705-3584-bddd-894a331bfc93 | -8.56924 | -44.66668 | 2025-10-02 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 886fa82a-07c0-32be-9292-58b7c8eb24d5 | -5.35223 | -45.96039 | 2025-10-02 04:49:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7de6e026-a746-393f-9fb9-c70da90ae090 | -8.3827 | -47.99136 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4255cf89-8055-3e35-b03f-283a35463a50 | -3.80479 | -51.31559 | 2025-10-02 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d429df75-43c1-3c19-a397-b4b6716d648b | -3.41313 | -48.88324 | 2025-10-02 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3520e37b-25b2-3b02-ad7f-433cd3560b95 | -6.58025 | -51.67713 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b4afa99-1f01-3239-9439-4be658baeae1 | -5.83456 | -43.95775 | 2025-10-02 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f889d240-ca33-3604-9f3b-0ccd1b411111 | -7.77103 | -42.54359 | 2025-10-02 04:49:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| fc207091-8504-3ff1-b9b5-e511e1b5bdda | -1.98139 | -47.98099 | 2025-10-02 04:49:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f77c451-a1b4-3a09-8b28-5d4ccd007182 | -5.41055 | -41.34259 | 2025-10-02 04:49:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f4c070dd-13c3-3867-8a00-668baf9c1ac4 | -8.89421 | -46.61361 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6dfc99c3-cecf-3d3f-8f4b-85072de2d240 | -3.10233 | -51.3548 | 2025-10-02 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1015aa3-f879-32ff-9aa3-4e6e5b389742 | -7.77375 | -42.5232 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6a51559d-ce03-3b92-89d4-da49d819c53b | -3.68613 | -52.15483 | 2025-10-02 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1eae1ab5-9559-318b-adea-f5c870d0b45e | -5.4539 | -42.84325 | 2025-10-02 04:49:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9b5322d6-7d07-32b7-a35c-b7f6d3386864 | -6.01077 | -52.38464 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a7c1f5a8-7bc7-3d0a-b73b-38951f9050b0 | -3.4997 | -50.26759 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4bb5b0c-b6a0-34cf-902b-c73701b3fa57 | -3.35329 | -43.19007 | 2025-10-02 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 616a6200-a8fb-3973-aaba-fbff80f8ab69 | -8.82801 | -44.78951 | 2025-10-02 04:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82cda592-4b9d-30ab-8aa9-dc288dd83980 | -4.62888 | -49.37223 | 2025-10-02 04:49:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f70f4d2-28df-3b7d-9ebf-fa334488954c | -9.01142 | -46.70836 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cce1c122-8181-374d-b748-37d5d2852d83 | -3.87434 | -42.52019 | 2025-10-02 04:49:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 06da58d9-1ddc-399c-b3c5-172ae483f177 | -4.32139 | -50.85883 | 2025-10-02 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README106.md)
