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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb1d2983-2889-31cf-9553-f8f892188ed8 | -7.99931 | -44.3932 | 2024-11-20 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73a4616c-5cb5-3c34-a775-f5bb5b20bf4b | -6.20033 | -37.43667 | 2024-11-20 03:34:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4bcbeb37-f938-3824-b8c1-636618a536f9 | -4.09511 | -44.85798 | 2024-11-20 03:34:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1368cd54-5626-3f69-bb56-567e7b21c42e | -3.87777 | -46.06562 | 2024-11-20 03:34:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6010f205-21ea-309f-8424-606be1ae733c | -2.61568 | -45.89834 | 2024-11-20 03:34:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e4d35783-02e0-3c22-98f9-65e9b2d436fc | -5.59725 | -46.18313 | 2024-11-20 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 917651ca-e83f-34a5-b911-f6ab273ac82e | -2.75417 | -45.7101 | 2024-11-20 03:34:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3b027731-335b-338b-98df-fe04a58cd017 | -2.21056 | -46.49082 | 2024-11-20 03:34:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68486723-a6a5-366d-95be-ab038beb4975 | -5.13442 | -37.38342 | 2024-11-20 03:34:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4aec5586-bf01-3ac5-a335-48654896f81a | -9.16963 | -44.73015 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f690a262-3a7b-3913-98e9-22ce8d1aa819 | -3.58097 | -43.62634 | 2024-11-20 03:34:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c3f7550-753f-3429-820b-418ce08d8e9d | -5.97152 | -45.37251 | 2024-11-20 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0d76b0d-9615-38e4-9ec5-485a86619fa9 | -3.58617 | -43.63155 | 2024-11-20 03:34:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc504966-9892-395f-bc2b-4f1e764efe38 | -2.84607 | -46.68407 | 2024-11-20 03:34:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c2cc5a79-8403-3468-ab2d-770c3a46f7ee | -5.25416 | -43.84471 | 2024-11-20 03:34:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9570195-16b1-3434-8e17-6e04f3e7b4d4 | -5.71553 | -44.81118 | 2024-11-20 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1918158b-d971-3f52-86f6-79f6f864c620 | -6.54203 | -44.18929 | 2024-11-20 03:34:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba2f6551-6cd7-33a1-8b6b-b237fdb9b8a3 | -5.71467 | -44.81601 | 2024-11-20 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d622636-79e7-321d-89ac-8364e17c80d6 | -7.27008 | -42.11049 | 2024-11-20 03:34:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 752b47f6-d447-3d39-82b0-698e252b3343 | -3.59205 | -43.63271 | 2024-11-20 03:34:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 934107d6-7196-35f0-afe0-66a7aed67ab5 | -4.15252 | -43.97649 | 2024-11-20 03:34:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 87619244-eb9c-3d74-a79e-1dca1ce2d162 | -2.2189 | -46.48501 | 2024-11-20 03:34:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 797d105a-ce25-3e42-9cee-6eecfb2eeb88 | -7.99626 | -44.3797 | 2024-11-20 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7f35dfa-f8e4-3e20-a1a2-102446e86439 | -5.69039 | -39.06372 | 2024-11-20 03:34:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1309509-52ef-3ecf-8c95-654f3a4be1b1 | -4.37149 | -40.59256 | 2024-11-20 03:34:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38ee216f-871f-3293-8cc4-4e6363aa56ef | -4.15175 | -43.98098 | 2024-11-20 03:34:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b61662a1-29ee-35f5-906e-196e0b0e9b21 | -3.38656 | -44.43777 | 2024-11-20 03:34:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ff67b3e-ec9c-3345-a274-3eddd04d195f | -2.82681 | -45.13673 | 2024-11-20 03:34:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef9259e3-6545-3eca-bddf-3a0c56243ebd | -5.97593 | -45.37183 | 2024-11-20 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbc3d09f-a4ab-3569-9e01-67b8378f5d45 | -2.99959 | -45.44149 | 2024-11-20 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 59791284-ffff-3173-abd2-e0410103351e | -9.1688 | -44.7346 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ba1e466-ae01-3498-8a73-7235cddcd1c0 | -3.38237 | -44.43784 | 2024-11-20 03:34:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cef7b3ed-c3c6-35d4-ba8a-15f3dd207121 | -3.05261 | -45.13449 | 2024-11-20 03:34:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4a607d82-5b1f-3da2-8756-bcdf18655960 | -3.22271 | -45.27766 | 2024-11-20 03:34:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd61bce9-a8e0-37eb-8b6f-907be8bd097f | -5.44738 | -44.82711 | 2024-11-20 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d21e8ef9-fa95-3057-8e3b-42ed8275faf7 | -9.57838 | -37.81499 | 2024-11-20 03:34:00 | NOAA-20 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 251e121d-5f2f-30a6-8568-d7b35c12dcbb | -4.20652 | -42.20006 | 2024-11-20 03:34:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74f10ff1-ce18-3c9b-b69e-552ab312109d | -7.15972 | -39.35755 | 2024-11-20 03:34:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cb656b22-aad9-3ce5-a8fd-73f9a5e423be | -9.57513 | -37.81585 | 2024-11-20 03:34:00 | NOAA-20 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52f44048-e08a-35e8-86e2-b690c086a4b0 | -9.57879 | -37.81651 | 2024-11-20 03:34:00 | NOAA-20 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89532f91-e279-3dcd-8114-7af21521e2ac | -3.78328 | -41.61292 | 2024-11-20 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6020f9b-da10-34e4-ab43-57098124e7b1 | -7.37675 | -34.88556 | 2024-11-20 03:34:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 145abf9e-a81f-3715-86d3-6329575d9d3a | -4.13218 | -42.83471 | 2024-11-20 03:34:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a0175a4d-f052-363d-8d18-324933cd8f27 | -3.00188 | -45.44749 | 2024-11-20 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dc6e8bf7-792d-3826-a60f-802b1bfb998b | -9.19283 | -44.73407 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91024f7e-c0eb-3ccd-9897-295d0c4e25a5 | -2.52275 | -44.99676 | 2024-11-20 03:34:00 | NOAA-20 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1796c79-8db6-3c14-8884-d4036d1b3a0d | -5.86177 | -39.70081 | 2024-11-20 03:34:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c561f56c-6919-35a7-a4af-6cb09119b6c2 | -4.53228 | -43.29723 | 2024-11-20 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3268e19b-ee6a-3306-8b05-cc03c56d9d40 | -4.48493 | -46.72041 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43cf1f38-2a2d-35ca-ba81-06935cdc6903 | -6.5825 | -35.39595 | 2024-11-20 03:34:00 | NOAA-20 | CAIÇARA | PARAÍBA | Brasil | 2503605 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fa061d9a-c507-34c8-acb6-9cb9fc80b108 | -4.44566 | -46.58778 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4ae7a98e-9a1c-32d6-b9d4-08c6dbf1caca | -6.75439 | -35.02061 | 2024-11-20 03:34:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1ae93d42-5412-36eb-94d9-5534ddff730d | -6.00937 | -38.65929 | 2024-11-20 03:34:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 2705d87a-bb5d-384b-87d9-0efdb44937ed | -3.37499 | -44.4305 | 2024-11-20 03:34:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76cdecd2-2c59-356d-bbdc-6e28de14606e | -6.80524 | -43.29668 | 2024-11-20 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4b064546-093d-351d-b8b9-aa161780152f | -7.99473 | -44.38788 | 2024-11-20 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fb3c565-c113-3781-86a4-379f1aa166bf | -6.3125 | -41.51854 | 2024-11-20 03:34:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 28aa1488-e7a2-3bc4-b7fe-9c19c5bc67c4 | -5.61363 | -35.35801 | 2024-11-20 03:34:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 56cfb6ea-4a0b-3c67-9729-807c6ca39673 | -8.31954 | -45.11488 | 2024-11-20 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d612258a-48dc-3cbb-9a57-4c6fd757bb2f | -5.14583 | -37.45744 | 2024-11-20 03:34:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 88694d01-e7aa-39bf-a2bb-ee3e1f63ea77 | -9.17122 | -44.72168 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fc0a0d6-09dc-3db2-a219-b9415636957a | -2.84235 | -46.6892 | 2024-11-20 03:34:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56ead477-741d-369c-a269-53c78f9a1a57 | -8.73798 | -44.09073 | 2024-11-20 03:34:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90baba71-4137-32ec-92f9-3f48e5a42286 | -3.38573 | -44.44259 | 2024-11-20 03:34:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0c7e311-afd3-3d2b-8d2b-6ae702b39f96 | -3.78895 | -41.61069 | 2024-11-20 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 21a732c7-9f58-31ea-8e19-6035721042ae | -3.37075 | -44.43059 | 2024-11-20 03:34:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c4859fc1-be98-371f-9e77-962609fef200 | -6.80394 | -43.30391 | 2024-11-20 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa9ba58d-829a-368c-a96f-5d058c19bf16 | -3.77866 | -41.60884 | 2024-11-20 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7f31095b-1500-3199-bdc5-910614cb1c1b | -5.4494 | -44.82336 | 2024-11-20 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5303b9e7-afdd-3b9b-845c-52cf333fe636 | -4.44448 | -46.59441 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6745e3f5-7d6f-39ba-848f-1938f1e2ca6e | -12.05663 | -38.35735 | 2024-11-20 03:36:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 960aa030-df96-37cd-a80e-5c321f240c5d | -11.87379 | -38.3494 | 2024-11-20 03:36:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 006e352f-9b54-3069-abb6-bc35d74f227b | -11.58795 | -42.97522 | 2024-11-20 03:36:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 41d3a539-b7d6-3f25-97b4-2e9c462b824e | -10.95205 | -44.90815 | 2024-11-20 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c214e15-0ab6-39ec-9c7b-78c3df13cb4f | -12.27304 | -43.52688 | 2024-11-20 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f2a37c8-1cf3-38ed-94b0-367bd417d25d | -12.85423 | -43.81977 | 2024-11-20 03:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b712b4b9-a1a9-345f-b45c-e82aa6ab17a7 | -11.587 | -42.9756 | 2024-11-20 03:36:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 45695e79-a102-3942-8f89-3a265ba5eecb | -11.10881 | -41.00854 | 2024-11-20 03:36:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 024e3ea5-937e-3ae1-b1cb-216ec400fb96 | -12.27751 | -43.53096 | 2024-11-20 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f81db3b-3006-36e0-bc5a-21e723a297c0 | -14.87293 | -43.15305 | 2024-11-20 03:36:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bdb58f1d-f2b6-32a4-8733-d55d9e20cd0d | -16.26451 | -39.55492 | 2024-11-20 03:36:00 | NOAA-20 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4831f6dc-8c56-3200-93ab-9e30ef88bbbb | -11.72749 | -37.61626 | 2024-11-20 03:36:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 21260b71-de26-35d2-a590-8a4c9afcb2db | -12.98592 | -40.92403 | 2024-11-20 03:36:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e8584bdf-f313-3270-b040-d14994b07747 | -11.98993 | -38.37246 | 2024-11-20 03:36:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ab309e0a-7a64-31f8-9117-972ca3ceec9f | -13.91174 | -42.9356 | 2024-11-20 03:36:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| adaa8603-9149-3f8c-a1d2-1e42d148a525 | -11.44816 | -43.30342 | 2024-11-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bbb4b7a-7ac7-38e2-b0d4-2f4724af5bfa | -14.4763 | -43.36525 | 2024-11-20 03:36:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 66cb2aa9-5d64-3ee5-abb1-5d85522ec42b | -11.06365 | -41.61843 | 2024-11-20 03:36:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 1ad61f81-95f9-3d65-aa17-073105dc957e | -12.27246 | -43.52991 | 2024-11-20 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa47e197-e2ff-3e40-b4f7-9214d711929b | -11.44873 | -43.30042 | 2024-11-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed08eddc-482a-37ed-a786-ecec930e4712 | -10.95131 | -44.91198 | 2024-11-20 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36ea9abf-c2ab-32c1-a204-3486dd17f142 | -12.05635 | -40.01751 | 2024-11-20 03:36:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3e3e352d-176c-37b0-89e2-aacd990a9df0 | -13.06048 | -41.136 | 2024-11-20 03:36:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6c4f3ceb-9fd1-3383-9d73-e9484383e92b | -14.86823 | -43.15208 | 2024-11-20 03:36:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5314c70a-e243-3115-b49f-668b0a737381 | -11.10958 | -41.00429 | 2024-11-20 03:36:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0c0c2727-afcb-3f6a-9996-11a37e1e6ccb | -11.43188 | -44.69186 | 2024-11-20 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 884f5e9e-9bc0-3b58-a07d-d74cbea8b229 | -14.88963 | -41.51202 | 2024-11-20 03:36:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cea2d532-1fe2-38f2-b6f0-8f5c15e09a33 | -11.06283 | -41.62304 | 2024-11-20 03:36:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 4dc4fd0f-572d-3e1f-9841-db6b630000e4 | -20.76015 | -46.77221 | 2024-11-20 03:38:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 66d8c898-9b47-3301-879d-bb7bfb47724e | -18.30524 | -42.21487 | 2024-11-20 03:38:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README20.md)
