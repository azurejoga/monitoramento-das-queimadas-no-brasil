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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f87c95b-fb00-3f84-8e57-fe438ba561b3 | -7.43326 | -41.24908 | 2025-11-01 03:47:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 20681dd3-432d-37e9-870c-a5d2a3ad08f5 | -2.88762 | -40.49605 | 2025-11-01 03:47:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f9c448ce-fe19-3e62-a66d-8b84e6a657d9 | -10.6377 | -42.31331 | 2025-11-01 03:47:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 17f7096f-8ebb-3355-b72c-963bc1c11fb0 | -2.79517 | -43.34933 | 2025-11-01 03:47:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 079e35f1-6edb-3d3d-82aa-50059e6abade | -2.65012 | -48.51135 | 2025-11-01 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9ab28f8d-9f42-3d4f-890f-35c8aa1ed6fa | -2.52826 | -45.84888 | 2025-11-01 03:47:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27fc6dec-9350-34df-81a4-ae3a52ef6cd7 | -2.88844 | -40.49106 | 2025-11-01 03:47:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 702195fe-bbc6-3d81-91b1-49f90fb10f1d | -7.38309 | -42.47914 | 2025-11-01 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc1d7d8f-64e8-3fea-ad86-2880ffef7e46 | -3.26339 | -45.326 | 2025-11-01 03:47:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5205ae2-a585-3da9-8c50-7f3e1427d543 | -9.7383 | -36.0869 | 2025-11-01 03:47:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b5e7278f-de1b-3d0d-a426-17eaabbd8f9b | -2.75481 | -45.395 | 2025-11-01 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eab01407-306e-362a-8cf8-105df9ef927e | -2.91229 | -40.22417 | 2025-11-01 03:47:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fc5a48ba-7a93-31aa-b757-efd49ebdcfe7 | -10.63857 | -42.30827 | 2025-11-01 03:47:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5c0af163-11c0-3c1b-b229-897acf33167c | -7.96953 | -38.2786 | 2025-11-01 03:47:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cea001cb-4ef6-371d-bf8b-2e447bb5a3f0 | -7.38319 | -41.93207 | 2025-11-01 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 852f5f0b-52f0-3d4a-b540-e9f3f1aae10f | -7.37645 | -40.80387 | 2025-11-01 03:47:00 | NOAA-20 | FRANCISCO MACEDO | PIAUÍ | Brasil | 2204154 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9d66b617-fc96-3d29-ab15-33111636bdb4 | -3.37255 | -44.2453 | 2025-11-01 03:47:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 660dda8c-799d-3ef5-88b0-6c330a09c431 | -7.90977 | -41.32955 | 2025-11-01 03:47:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d3f36dee-7184-383c-9550-f3718ba4ad65 | -9.48169 | -40.9595 | 2025-11-01 03:47:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 46c3723a-7b6b-3bca-9481-1d80531bb750 | -7.47634 | -38.70548 | 2025-11-01 03:47:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 18a25116-a4fa-304d-9f17-6f473d37fefe | -8.56613 | -40.91318 | 2025-11-01 03:47:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4a7e8047-8647-373e-b389-04ea6871105b | -9.03905 | -36.37044 | 2025-11-01 03:47:00 | NOAA-20 | CORRENTES | PERNAMBUCO | Brasil | 2604700 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1843bdf5-387f-3248-bc42-9d07e8acd954 | -3.37305 | -44.24237 | 2025-11-01 03:47:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95381e9c-04c1-3124-b7d4-61238c615f05 | -6.79962 | -47.05341 | 2025-11-01 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82e234a8-3b72-366a-b93a-3cae07ae34ce | -7.83991 | -40.25674 | 2025-11-01 03:47:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0fdb9069-3d48-3761-bf66-8c9a0362eb95 | -5.59703 | -49.0776 | 2025-11-01 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc28ab95-4dc2-3d39-aba3-dfa655bdeb97 | -10.63379 | -42.31261 | 2025-11-01 03:47:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b967b537-a500-3b01-87d5-96147b7633f5 | -6.88237 | -42.84864 | 2025-11-01 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 96eb50e6-d961-397e-b98e-a6802f155eb8 | -3.31645 | -39.35956 | 2025-11-01 03:47:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 24db133c-4833-3f2e-bfc7-76dc60b24cf1 | -8.15098 | -45.4375 | 2025-11-01 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 630a9b42-d7c2-38a8-bd47-adbd2ededa40 | -10.0111 | -36.09581 | 2025-11-01 03:47:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 578a9088-bcfd-311b-8e5a-c22c3319a851 | -10.15036 | -43.9236 | 2025-11-01 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3667c279-516c-3cda-b8e4-15b42701a576 | -8.22625 | -46.25119 | 2025-11-01 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b7c9a0c1-3c6e-3df9-b890-cde3ccbbec58 | -10.49225 | -43.3159 | 2025-11-01 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d633b289-978c-3496-913a-94fd5e0fcc40 | -7.39689 | -42.47348 | 2025-11-01 03:47:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bf3a3d76-02c5-3bac-894c-ba14448c1f37 | -8.04662 | -37.58292 | 2025-11-01 03:47:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 59055917-9410-3a04-a73b-998e7bcd4b84 | -10.63682 | -42.31837 | 2025-11-01 03:47:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 95f2f868-efe4-3bec-8d3a-4462f1467c7f | -8.82321 | -39.83417 | 2025-11-01 03:47:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c9cec866-8920-3f53-b720-d52a9bd0eb8e | -7.96896 | -38.28218 | 2025-11-01 03:47:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3d869f0d-a487-331b-b288-e49fa6f097ab | -7.04996 | -41.46901 | 2025-11-01 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b1892c5d-f4e2-33b5-922d-fd385d170ba8 | -5.16191 | -35.73135 | 2025-11-01 03:47:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bee3d7ad-4569-3263-8a06-414d4288b1a5 | -3.14131 | -39.65452 | 2025-11-01 03:47:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 232afd2e-b738-3720-815e-f2a7db4cd3a1 | -10.63466 | -42.30757 | 2025-11-01 03:47:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6c096a88-4cb8-3bb5-b9f8-7883115cdd96 | -8.15151 | -45.43454 | 2025-11-01 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c84ed75-dcc1-3f05-b236-f41a79f8cba4 | -7.50466 | -42.45287 | 2025-11-01 03:47:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9e24291b-7a9e-3983-848c-81b63e6fe806 | -8.92873 | -47.68182 | 2025-11-01 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3893d671-34c3-3828-9eea-896c39314075 | -2.52764 | -45.85273 | 2025-11-01 03:47:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac9f7ade-8f21-37d1-9ad5-f10b24fb7d87 | -8.00441 | -35.86082 | 2025-11-01 03:47:00 | NOAA-20 | RIACHO DAS ALMAS | PERNAMBUCO | Brasil | 2611705 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6f94e64b-09f9-34a3-ac46-99b0e9e35340 | -9.02446 | -47.46446 | 2025-11-01 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63a35990-031e-397e-936d-e7e18e1bbb31 | -6.80035 | -47.0493 | 2025-11-01 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b8ae759-c792-37a7-a946-2ca775746863 | -7.79311 | -46.04626 | 2025-11-01 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f125a1c1-2f30-32bf-a02c-f5d65a7b299f | -9.0282 | -47.4624 | 2025-11-01 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b46e9155-a67b-3e4c-bd51-3498952354e1 | -4.29679 | -41.4433 | 2025-11-01 03:47:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c6555148-78da-32f4-84b5-5a0ff2fe27cc | -6.92217 | -42.66499 | 2025-11-01 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cf968bbd-e5c7-3d74-bc8c-c065c2508407 | -8.82385 | -39.83021 | 2025-11-01 03:47:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ca50d355-8d13-3661-8563-7155440f5fe1 | -9.02518 | -47.46065 | 2025-11-01 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed4cb17c-29f4-3485-9c8f-8534b4a65988 | -7.50402 | -42.45668 | 2025-11-01 03:47:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 637027bd-b679-32a4-8245-bea1797c9005 | -8.23155 | -46.25212 | 2025-11-01 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 578971ba-28a7-3b72-9130-70e8d627f83b | -9.73886 | -36.08329 | 2025-11-01 03:47:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 2dd22198-61ac-3b10-8f2d-1d78961f3bbe | -6.53462 | -48.03699 | 2025-11-01 03:47:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 582fe84e-bd0a-3ce0-abc1-c77870894376 | -8.88573 | -40.75634 | 2025-11-01 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 97ddf16a-2cb0-3c53-a687-21b7edd614e8 | -2.52453 | -45.85232 | 2025-11-01 03:47:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32460c80-e2d5-3226-8e9b-59821f7bdf91 | -3.90411 | -42.54548 | 2025-11-01 03:47:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d0190ebd-58c3-37d1-8afe-92e56908b4ae | -2.52519 | -45.84847 | 2025-11-01 03:47:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6cffdb65-40a3-352a-85a0-c42cdadfcfd8 | -10.63291 | -42.31768 | 2025-11-01 03:47:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d9e976fc-44b6-3c03-8d6a-27f609c8afa6 | -8.17154 | -34.97967 | 2025-11-01 03:47:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4fb53ef4-c2fa-3afc-978e-a0ee49e02ce4 | -7.33123 | -39.31704 | 2025-11-01 03:47:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| de294362-2dab-3a02-9028-54c943cab627 | -6.04741 | -47.97339 | 2025-11-01 03:47:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 259a2937-dd84-33fa-a486-fb8fd76885fe | -5.13805 | -36.35753 | 2025-11-01 03:47:00 | NOAA-20 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c19e1415-4934-3a5e-ba52-f77bef5b6ede | -8.71265 | -41.58449 | 2025-11-01 03:47:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8155f624-4dab-3627-a8ca-689a486d18d1 | -2.89154 | -40.4967 | 2025-11-01 03:47:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 33241a0f-7ea9-3d83-95d6-c0f61934fd2c | -2.76088 | -45.39235 | 2025-11-01 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5c248be-dcd7-3430-b20b-d32951fa3c18 | -5.59594 | -49.08347 | 2025-11-01 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5030d89d-85cc-32a7-af4c-7ffd3b049408 | -6.34052 | -45.25608 | 2025-11-01 03:47:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b98c2406-cdbc-3ed2-9607-fcb793e8cc63 | -7.9656 | -38.28164 | 2025-11-01 03:47:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ab19199c-5201-3b8c-a225-8596c4aa0361 | -3.04029 | -45.82288 | 2025-11-01 03:47:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 706fa978-5c7a-3b20-bc4d-5c6abfe55b23 | -8.7088 | -41.5838 | 2025-11-01 03:47:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b6efd6f2-27c6-3aa3-91e3-e568d253402f | -7.04154 | -41.46926 | 2025-11-01 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4f08e297-f0ac-3f9c-b2ee-515e1608f2e4 | -10.15112 | -43.9193 | 2025-11-01 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21cf2967-2058-313c-886d-d9f003290f0e | -8.71183 | -41.58933 | 2025-11-01 03:47:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1160da15-86bc-3489-8408-0e29c4c89836 | -7.50298 | -38.82341 | 2025-11-01 03:47:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1fd9d0df-14d9-35cf-af50-d000fe76c627 | -4.30091 | -41.44372 | 2025-11-01 03:47:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9e3fafa4-f4b3-33ce-990c-df628f0ea677 | -3.43062 | -42.54206 | 2025-11-01 03:47:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d80c4ba-f85e-30ca-8c15-1e5a018a680e | -10.50531 | -42.40308 | 2025-11-01 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa7ee15f-ad56-3fb4-ba22-ae5fc68e39bd | -7.37539 | -40.80602 | 2025-11-01 03:47:00 | NOAA-20 | FRANCISCO MACEDO | PIAUÍ | Brasil | 2204154 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 417ac9d9-9d01-3e9f-8973-fef7ecfc1087 | -10.01054 | -36.09943 | 2025-11-01 03:47:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 78ae5231-7b14-3a7a-b641-11a4afa69fc0 | -8.56371 | -36.25945 | 2025-11-01 03:47:00 | NOAA-20 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 309ddc52-c7b5-308b-b02b-8e857af83b54 | -6.04659 | -47.97786 | 2025-11-01 03:47:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81770dc7-e5ab-3201-90c9-294e957807f7 | -2.89236 | -40.49171 | 2025-11-01 03:47:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6c96bfc3-a680-3b6b-841a-e76fcf27a7b7 | -3.88424 | -42.55567 | 2025-11-01 03:47:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cba216c8-7d2a-335a-abba-0638d4a1365b | -9.73549 | -36.08277 | 2025-11-01 03:47:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5787fb37-de38-39ad-ad72-a42b39321164 | -3.43507 | -42.54281 | 2025-11-01 03:47:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a130449a-5d5c-3c11-a630-585e3d91d68b | -3.14502 | -39.65511 | 2025-11-01 03:47:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 27aa797c-fe19-36e9-878c-b81e727d5123 | -2.91071 | -40.23376 | 2025-11-01 03:47:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 52d896f8-80e9-3e52-9903-459f92c9dc63 | -3.03967 | -45.82663 | 2025-11-01 03:47:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 834229a7-4fe5-3c72-8c87-f71fb364c614 | -8.56242 | -40.91257 | 2025-11-01 03:47:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 395e2755-b6ea-3e65-941a-4b8d6d24e005 | -7.06657 | -47.36502 | 2025-11-01 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 03d42a0d-e4d8-3209-8dfa-2a73d8635465 | -7.35903 | -47.00112 | 2025-11-01 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 453d881c-38be-34f0-93c1-f72af9097554 | -6.88306 | -42.84457 | 2025-11-01 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 9e327d37-251c-373d-b85d-bd6c5fdb03aa | -8.92795 | -47.68599 | 2025-11-01 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README12.md)
