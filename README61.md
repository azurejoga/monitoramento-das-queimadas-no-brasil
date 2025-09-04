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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9139b8e-2bd3-3905-b0ae-ff8e4e8586ac | -6.1275 | -42.94381 | 2025-09-04 04:53:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 30f661c5-7494-325b-b07b-0923d4bc9f5d | -9.69324 | -48.99763 | 2025-09-04 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7d36d97-0ebc-33c2-94d6-01166e6941a7 | -6.0801 | -43.28297 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c1cfc0f7-95f3-398b-a454-6b2ecd9a9a8d | -9.48473 | -47.61107 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d76cbb61-b3d0-34b9-b175-1a64a81c2755 | -7.94224 | -44.9468 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b88c22b3-ec88-3da0-93de-0cd95243a11d | -6.78452 | -44.45313 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6d95e323-b2c8-3d8a-bbea-f91b9c9f8d9f | -9.33732 | -55.21568 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98af29e6-de52-39bd-87f0-26598891135b | -6.26437 | -43.28136 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aff0e4bd-b984-3e25-8883-b4fe45362368 | -6.26103 | -45.1587 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3446315f-f38b-3de7-ae6d-5c3f041e5f22 | -6.26023 | -45.0967 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3666aa92-5dd3-3a40-953d-b0bb71c1020c | -7.01255 | -43.22681 | 2025-09-04 04:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1a49b8c2-6ab1-3be6-ad01-af0b63152022 | -6.25612 | -43.31083 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b1ddf8f-c44f-3a2d-8e25-09bf1be61188 | -5.02347 | -56.11205 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26a4dd36-b4c8-3a17-9de3-316fc7ba32dc | -9.32512 | -55.22528 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ab698df-abbe-3d44-ba7d-a0aae6426d08 | -6.46929 | -53.40175 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed505465-76ef-329b-8d3f-3a17bee39eb9 | -6.7412 | -58.71973 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7960590-4183-348c-9d39-5c87184d0733 | -6.26236 | -43.57946 | 2025-09-04 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f5f1a14-38b5-3224-81d3-9c2fd1937ebc | -6.27705 | -43.85099 | 2025-09-04 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfc35992-f350-3d31-b6af-1f4ca763ec4a | -5.79642 | -45.63226 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93c95807-f94c-3f3e-839f-65f5323f3d28 | -9.05197 | -54.95061 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 106225a1-7d5a-34ff-bae4-29439ac9753d | -11.09381 | -45.12604 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2065dd6a-febf-3a9b-8696-02a5457de027 | -6.88102 | -59.08725 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11b72311-8cf8-3123-823a-4fc9e6380431 | -6.17758 | -47.2822 | 2025-09-04 04:53:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 168bdef4-87fa-356c-a6f4-9193a49072c1 | -6.54096 | -42.94722 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8ea9d75-c181-37ac-907e-8da6061a85f3 | -6.78591 | -44.09718 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8c7f2ee-4c31-3158-b721-730869ee689f | -6.69233 | -48.41351 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd2036ac-0863-3ff8-a48a-7a5158478681 | -6.27222 | -43.5094 | 2025-09-04 04:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b437b2de-bdc4-3669-94e2-d6f1852e25b9 | -10.75343 | -48.27029 | 2025-09-04 04:53:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1fdf010-2e17-3819-b092-8cc3722b8114 | -4.89804 | -49.92726 | 2025-09-04 04:53:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4525f03c-765a-3004-aadd-bfacd87d396f | -6.49938 | -43.09042 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b7bb869-4dfe-333c-ad0d-38b878a1bb39 | -5.27608 | -55.95993 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8217d8fc-9c4d-3bc4-8a4b-f30d37e3ba72 | -7.70178 | -50.29145 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4c077c5-55d2-3f85-a5bc-619610d7d9b2 | -11.04984 | -45.14467 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| adaa7242-c559-3e6d-af70-f263011e7fa9 | -9.97451 | -51.63223 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf562930-a07b-35aa-b740-40cc8542e7cb | -7.71941 | -50.31806 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 86139585-fba8-3711-aa6f-0d7edc27b050 | -6.26391 | -43.28456 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b866fc31-831d-3a70-aa0c-7f4764bf9c00 | -7.69275 | -48.73309 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d28b2d70-32ed-3369-a7e9-2024660d5514 | -6.87503 | -45.5573 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 517a2394-bbd2-38e5-b6ea-db93fefa78a9 | -11.04692 | -45.40369 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b78211a-1133-37d8-80d1-b4020184de5b | -10.42763 | -50.36987 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 24bff3e3-3659-36b4-9d0d-d671e0cb1f5d | -7.93748 | -44.93988 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 06089b54-743e-3f6e-8bd4-23a28bd6c9d5 | -8.0281 | -44.07006 | 2025-09-04 04:53:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 108f4429-1958-39b0-b881-10181ea7d068 | -9.32919 | -55.22207 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4e8f1c8-0b58-3958-8431-7a2f386f468c | -7.68894 | -48.73245 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 89582fad-6e2f-3962-9c35-63e41a7d040d | -10.74977 | -46.34813 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c28a1c0-8896-362c-aa91-e55a37bff9d2 | -10.44249 | -50.26876 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fc734e2-1912-3b1a-9f83-11f222fb8a8c | -8.64941 | -54.84856 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99d36070-87ed-3cf7-bf0a-bafb20a37938 | -6.26104 | -43.31506 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7576861b-efdf-30c0-a96d-7dda09aed61b | -6.21445 | -43.39929 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa3de06e-10fb-3d87-9855-936e8ba40b27 | -11.03602 | -45.13106 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 189869f2-e94c-3be5-88e4-9f3f911c004d | -8.36434 | -48.29028 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70665bab-5379-3d70-b14b-1f14dc05f6f8 | -7.93873 | -44.93544 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4e3411be-d8d8-3291-98d5-b583c17b5b17 | -6.6327 | -56.26368 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69222baf-beca-3396-bc4c-6ac38d21f5ad | -9.32857 | -55.22586 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3814eca1-4820-3d75-98c5-2fddc8b12b65 | -7.97339 | -55.3149 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 225e7208-2964-31e6-bb49-7ff3312ff9c8 | -9.6283 | -47.84149 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51f1326f-4021-366e-b63b-c5c22ef17f37 | -4.99589 | -56.25827 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 33f4956c-e345-3022-a474-454e4158895c | -8.89491 | -45.80045 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8101edda-beea-3511-bc54-e2d879ef051f | -9.32574 | -55.2215 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 374ac560-3fc2-3e0c-bbe2-4f5e39837756 | -9.60609 | -47.04358 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 06a22cee-b4c5-3023-b00f-e06811ac7dde | -7.01208 | -43.23029 | 2025-09-04 04:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ca5251a8-4f0c-3284-b560-417ecaa447e5 | -7.71664 | -50.2402 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0764817-6afa-3f3a-adb5-447deec061e4 | -9.83331 | -46.64051 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be7e8e03-7584-3620-b8a0-fce57a848ba4 | -10.436 | -50.38826 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f72e7412-5fa9-3778-94db-67a3166a5f48 | -6.1305 | -44.14503 | 2025-09-04 04:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca3fc937-5bf7-3705-9fec-75195a9c4e65 | -10.4264 | -50.37825 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 9b1494c2-d8cd-3de3-af08-eab73af0a529 | -5.6135 | -57.36613 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fea4cb07-2376-357d-954d-81fed87b92be | -8.03904 | -45.3853 | 2025-09-04 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2fd515c9-5781-3446-a5db-4a43c15bf3bd | -11.03679 | -45.12502 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c195b124-2195-393c-b82c-62663bde4946 | -8.02765 | -44.07336 | 2025-09-04 04:53:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4b156f7-ac57-384f-abaa-df264b362c10 | -11.08872 | -45.12519 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90b7b259-89f7-3706-8f28-cddd6feccb74 | -8.0751 | -45.33804 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fee7ae6-c039-3b9c-84be-17fb9f45cd39 | -7.04064 | -43.26642 | 2025-09-04 04:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1853dab8-dfd5-30a9-8465-f30748fc90b1 | -5.38901 | -55.90854 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce1acd69-83f1-3cf1-b44d-7be2f204ec18 | -7.94243 | -44.94051 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cd302d38-a702-37c0-a67e-1d62bf6883c9 | -6.21544 | -43.39237 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fda150d3-b321-3486-a169-2ac4ee43bff2 | -5.89883 | -45.95664 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 094cbd76-101a-3920-b985-c020b26cb644 | -6.23313 | -42.43489 | 2025-09-04 04:53:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4f55c0c2-92f0-3d96-946b-bb1f5916ac48 | -8.01473 | -45.7974 | 2025-09-04 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69cf141f-a240-3833-8c9f-ff26fbe10ec6 | -6.77987 | -63.13673 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4061e34c-2008-35e5-ac7a-f78b762ce8cc | -8.47588 | -45.06244 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5456b0a1-d30d-3302-9c60-cbc34dca5396 | -6.78841 | -44.08938 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 20b83434-22e2-3593-bd7f-96dec88c5d3f | -11.03016 | -45.13628 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1170d812-f09e-3817-bb6f-fec4faf23a17 | -11.24298 | -44.95951 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecef6a0c-ecc4-352b-8ebf-892d27b581a0 | -7.67819 | -48.72594 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| df4a0408-2d0b-3e7e-8c17-25d5a8dc0fef | -6.07002 | -53.82296 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 627e3439-b90c-398b-8eaa-3e1be460eccb | -8.02899 | -44.06357 | 2025-09-04 04:53:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a78ee3b8-e3a8-3dc5-ab4f-8e818135c6b5 | -8.873 | -45.85326 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8eafc1b4-728c-342b-a822-e00f668d7e8e | -8.89213 | -45.81999 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cb75417-3f78-3b53-aa4e-2bb144810ad6 | -8.0785 | -50.20248 | 2025-09-04 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 016bcb78-1f52-3380-9505-4b1941f93d58 | -9.5447 | -49.16815 | 2025-09-04 04:53:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63d2367e-50f7-3ccc-a81a-bd52f35635e6 | -5.68645 | -45.94238 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc54be0d-70d2-3f21-bec9-f5542cf87c90 | -6.59895 | -44.06802 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec9def64-116a-36cb-9bb1-c36c01c69aeb | -5.87568 | -46.11696 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a14219f-4b19-3a9e-bf51-f39bebe7ff9b | -6.50275 | -43.57758 | 2025-09-04 04:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cd30d95-47b4-373c-9843-6839722375e0 | -6.69687 | -48.40934 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74ed10a2-0bb8-37de-a449-8675e331b30c | -6.40782 | -43.26565 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23e380c4-1fab-30e1-81ae-233bde16112c | -6.23705 | -42.61134 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a7225696-f57b-3d57-a157-35dca13b986d | -9.95971 | -51.63749 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62e6b391-454a-3cd8-8239-1f297ba70aab | -10.04194 | -48.13266 | 2025-09-04 04:53:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README62.md)
