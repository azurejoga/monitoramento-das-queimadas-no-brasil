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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a6b818f-3e65-34db-aa04-b27c35bd6d4a | -12.913 | -47.378 | 2025-10-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| e074be40-e73c-30d8-b300-01a2d0876447 | -3.6975 | -43.2106 | 2025-10-28 14:10:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| acd12375-9d09-3c30-9161-b310997a3c26 | -7.4395 | -47.1657 | 2025-10-28 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 3e9a7a77-93ae-3155-a51f-6c030637793a | -14.3551 | -51.8064 | 2025-10-28 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7d9dd8b7-5399-3840-a035-5310751000cc | -7.7678 | -44.6855 | 2025-10-28 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| a2d8e153-ed31-39c1-ae8f-59ef1ecc9e9e | -4.864 | -42.2015 | 2025-10-28 14:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 96ebe0a4-e3e0-3bcb-bca6-b5ced0a5dcbc | -14.3744 | -51.8038 | 2025-10-28 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5764d5cb-1414-3fb6-8834-c5777ab7e8ce | -3.5833 | -43.6108 | 2025-10-28 14:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 6c42d273-7dbe-36a7-b96b-a80e990300f9 | -14.2491 | -48.1148 | 2025-10-28 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 0b6652b4-504a-3923-b272-9e7818bd1520 | -6.2567 | -41.8298 | 2025-10-28 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| c1cd4b3e-7376-35ce-b369-a516e042b68c | -4.7346 | -44.4457 | 2025-10-28 14:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| e524b51f-8c77-35a0-93ff-2f87e9547193 | -13.2258 | -47.1066 | 2025-10-28 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| cfc3d1c7-0a10-3fe3-9c4d-717372b568d4 | -6.6224 | -44.6296 | 2025-10-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 1a217a4c-5519-3721-abc1-b01e011a1b43 | -7.9884 | -46.7183 | 2025-10-28 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5ece1d01-dc1e-368b-847e-2a0b2f908101 | -2.8324 | -49.3901 | 2025-10-28 14:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| f06d91a3-ba4a-3054-9401-40eb28ad227b | -6.3866 | -45.7594 | 2025-10-28 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| e1b353b4-d563-32df-af54-23162d4388a5 | -13.2262 | -47.084 | 2025-10-28 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 2ee353eb-f597-30fc-8729-662bcf323cbe | -6.6698 | -45.5118 | 2025-10-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| ab83be8d-dd94-3eeb-bdc3-58e00d8c2442 | -7.9691 | -46.7646 | 2025-10-28 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b52b2496-81d7-3241-93d2-f134240dd932 | -4.4786 | -43.7021 | 2025-10-28 14:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 4e64968f-25fa-3988-b885-1bab168c01f3 | -3.0335 | -41.6843 | 2025-10-28 14:10:00 | GOES-19 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| ae4f41f1-4581-371f-b528-b54872b57c4c | -3.5521 | -42.5383 | 2025-10-28 14:10:00 | GOES-19 | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| a0abdab3-107e-3bd6-92e7-30279d3d453f | -4.8933 | -43.2349 | 2025-10-28 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 3425d5ec-3a31-3cc6-99f7-24e1ad763a9b | -4.3237 | -41.8078 | 2025-10-28 14:10:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 465492f1-1913-36ea-a56a-75184a23eadc | -3.0148 | -41.6851 | 2025-10-28 14:20:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 8a8d079b-d088-3893-883b-e8d0b84df18c | -15.2199 | -47.2108 | 2025-10-28 14:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| d286fce0-7f6d-3a40-8d4c-12ab161db9d1 | -8.6334 | -44.8021 | 2025-10-28 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 5e3ee14f-1b89-3e64-8343-58f0d97b13d1 | -7.7489 | -44.6873 | 2025-10-28 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| d8741f22-95bf-3e01-abdb-acf9e7b45343 | -3.8914 | -42.0712 | 2025-10-28 14:20:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| acddbe84-22fb-35ab-becc-2417c10490f8 | -13.2691 | -47.8846 | 2025-10-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 2a427689-d21f-35b5-9370-2cb1d9e0b8c1 | -13.2695 | -47.8622 | 2025-10-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 6aa9601f-059a-37b4-bced-7b0c1465ebe9 | -7.927 | -45.5353 | 2025-10-28 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 37705593-0f71-3db2-8eaa-c4ec44cd3706 | -6.0786 | -44.6733 | 2025-10-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 91b1a812-9558-352c-a009-925367168e53 | -8.6065 | -45.4212 | 2025-10-28 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 698a4a7f-f2eb-3c29-810e-77963cd93e02 | -7.8228 | -46.4217 | 2025-10-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 2d3e7850-0c2a-3de9-957e-4c54203eed12 | -7.218 | -46.8527 | 2025-10-28 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 54daa930-f113-3bcc-ac40-1c189102e633 | -14.3934 | -51.8226 | 2025-10-28 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| c8d800aa-06f9-3b65-9711-b0b1b537ef96 | -7.9467 | -45.4655 | 2025-10-28 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 5cd76f4f-fa78-39d2-9762-413622667c68 | -4.9138 | -42.9998 | 2025-10-28 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a6bdc9e5-ade9-396b-b74f-2af28c57c23e | -7.823 | -46.3993 | 2025-10-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 91328bbd-93ee-3b88-9e98-66f98ffe4481 | -7.9691 | -46.7646 | 2025-10-28 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 3c5ae2bf-0908-35e2-b750-494e52739d9a | -13.9337 | -48.4305 | 2025-10-28 14:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b0495267-c319-3666-b632-6649c9308f62 | -6.6707 | -45.4214 | 2025-10-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 882ece96-66da-3331-b38a-b64992436414 | -8.1853 | -44.4363 | 2025-10-28 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| b5d820e9-73e9-3fdb-b61f-8bff5e0ac4de | -13.9465 | -47.7595 | 2025-10-28 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 9727f340-4398-3839-9e1e-6dfddb3b5b1b | -12.3484 | -50.1779 | 2025-10-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| d5f960ee-2e83-3ab8-ac70-851170aa5732 | -4.3051 | -41.7851 | 2025-10-28 14:20:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 16cc2e3a-f37a-3d58-9f48-4acc5951f330 | -14.3744 | -51.8038 | 2025-10-28 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 36469e01-545c-3470-b512-3287843a44a1 | -13.6241 | -46.455 | 2025-10-28 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| bacdceea-ebd9-3dcc-99dd-41d19adb4c9b | -4.3049 | -41.809 | 2025-10-28 14:20:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 49084ea9-fd44-35a0-a944-224dee358656 | -7.9835 | -45.5298 | 2025-10-28 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b3eab00e-aa3b-381d-a018-b480aa233d58 | -3.9992 | -49.0508 | 2025-10-28 14:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| ce05de4b-30d8-3a1b-b77c-cb4bfc865ddb | -8.4686 | -45.888 | 2025-10-28 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e22770de-5b0b-3908-9302-80f561804968 | -3.7075 | -41.556 | 2025-10-28 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 166.1 |
| 78b1ecde-c802-3a8c-bfc7-1ebce99d6e7e | -3.6975 | -43.2106 | 2025-10-28 14:20:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ed3dd629-7ec9-3cab-aae9-e33d2a5b027d | -7.8037 | -46.4458 | 2025-10-28 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 83f041ca-2002-362f-983d-229406d76d23 | -3.4468 | -44.7176 | 2025-10-28 14:20:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 29e30d0a-c088-33cd-8f0d-602b89b0b9f3 | -8.0259 | -45.1397 | 2025-10-28 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 12cae2ab-c146-3ad2-a06c-7453787983a5 | -3.5646 | -43.6117 | 2025-10-28 14:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 9a2c44ad-8e2f-3bf3-b0bd-e92d268a5e8f | -13.2258 | -47.1066 | 2025-10-28 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 02dd0cf2-de0b-3687-a009-8228a9a5f4fd | -9.9 | -44.9069 | 2025-10-28 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1b2315d3-d4c2-3d67-8e1c-2a0510870554 | -6.6412 | -44.628 | 2025-10-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 8d700ec7-830e-39ad-9165-38a5a0c03c1e | -8.0447 | -45.1378 | 2025-10-28 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 9cfaa0a8-ef51-3c8e-952c-b034bce0ed57 | -12.8299 | -47.7254 | 2025-10-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| b7676d71-46c9-3a95-a534-238c2b165a6d | -13.9469 | -47.7371 | 2025-10-28 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 24035ebc-7d56-3aae-ad87-c3a59258c6d6 | -3.7261 | -41.579 | 2025-10-28 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 96b308f5-fa92-3daa-a379-0ea7e169a072 | -7.4583 | -47.1641 | 2025-10-28 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| b77c77e4-b6f6-3f53-9c8d-bc58ffc68dde | -5.2552 | -42.4819 | 2025-10-28 14:20:00 | GOES-19 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 244a8723-595a-3b62-bd28-9cca8f95471c | -7.9459 | -45.5335 | 2025-10-28 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 79f3fdc4-1a64-36f2-94ba-fdf0d56b32f4 | -7.8418 | -46.3976 | 2025-10-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| d9fbe9b4-0396-395a-aa64-02bc4c255ec6 | -8.0256 | -45.1625 | 2025-10-28 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 6605f265-9c0b-300f-a050-0ecd91daa2ac | -14.2491 | -48.1148 | 2025-10-28 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e90717a2-4492-3d84-981f-d527d0775068 | -7.1225 | -47.0375 | 2025-10-28 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 78d975aa-9d51-3891-ad49-ee021ca1f3ef | -3.5521 | -42.5383 | 2025-10-28 14:20:00 | GOES-19 | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 06a269a6-b807-3b2c-a4f8-b0120aceeb9d | -6.6414 | -44.6051 | 2025-10-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 2d84fb20-e893-36b1-8a97-c1c22a8c425f | -4.7346 | -44.4457 | 2025-10-28 14:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 195.8 |
| 5cc2f51c-1e71-3298-a729-b9ff3fb3b177 | -9.1846 | -44.579 | 2025-10-28 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 2e51da8e-e760-3ebb-b357-1e33074e7e40 | -3.8725 | -42.096 | 2025-10-28 14:20:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| c94fdd85-dbe8-3b80-b7d9-7acb9b522490 | -6.6224 | -44.6296 | 2025-10-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 20175e82-b491-35b0-a6db-d35ae9f875c9 | -7.0881 | -44.9547 | 2025-10-28 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 49336f79-7c73-3165-aa7d-bab2dbcc777a | -3.1769 | -42.861 | 2025-10-28 14:20:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d85ac491-2829-32cd-8d14-fe1baff4982e | -9.3933 | -44.5543 | 2025-10-28 14:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 4f0188c2-3498-3832-890b-a0779fada29e | -7.9464 | -45.4882 | 2025-10-28 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a5b63fd3-b417-31d9-84ac-e6d87b215d91 | -8.646 | -45.2806 | 2025-10-28 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 71d64a6b-4ccb-399e-b372-e320918651d5 | -9.8814 | -44.8862 | 2025-10-28 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| cf8a4e20-8fd0-327f-a91e-ef82fa0454c9 | -5.6221 | -43.3934 | 2025-10-28 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| eab13e65-a303-3879-a3ab-180bed1fc435 | -7.1227 | -47.0154 | 2025-10-28 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| de9eb4cb-6a81-3638-a5f0-cda87a321e57 | -4.4431 | -43.4259 | 2025-10-28 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 50a836f2-eea7-39ee-9462-2fbdd17ce4e3 | -8.6062 | -45.4439 | 2025-10-28 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 190.6 |
| f07f0c0a-9acd-31de-a509-c09e9fbb129c | -7.9693 | -46.7423 | 2025-10-28 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 63fabd34-3bfc-35d9-a318-80c3a8311a86 | -3.0146 | -41.709 | 2025-10-28 14:20:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 2809e604-3cdc-31de-bc74-6833bbcee602 | -8.0444 | -45.1606 | 2025-10-28 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 922f5576-f34e-3e83-8b56-e847377b7bbf | -6.0974 | -44.6718 | 2025-10-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 208.4 |
| af5ee386-d683-34f1-adb0-51927cce7086 | -6.9857 | -43.9997 | 2025-10-28 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| de0c7eb0-7ffc-3d31-99bc-3ebcc1eb2e9d | -4.3239 | -41.7839 | 2025-10-28 14:20:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 76d94a5e-3b62-3dec-8bfa-0f6ad8c3b6eb | -4.0103 | -43.9358 | 2025-10-28 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 40f6133a-359b-33d0-a183-9a9d38d6399c | -6.9669 | -44.0014 | 2025-10-28 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 64149caf-2bb3-3428-921e-9cdc57fae3d8 | 1.9056 | -50.8414 | 2025-10-28 14:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 6ccd4b93-f251-3a60-8711-3e8ee5cc4ea2 | -7.9072 | -47.2573 | 2025-10-28 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 07870a72-90b3-39eb-9a58-02796e60a3bf | -13.2262 | -47.084 | 2025-10-28 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |


[Clique aqui para ver as próximas entradas](README93.md)
