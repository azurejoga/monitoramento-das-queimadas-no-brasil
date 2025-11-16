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
| 5c220936-1019-3d82-bdca-e58f2c2739d6 | -12.061 | -46.96854 | 2025-11-16 04:57:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f308ce73-19ef-3558-a149-4d0a8751d9ad | -9.74319 | -43.96239 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dcbf8e34-45e3-3b9d-9763-09d385174bfc | -10.04493 | -54.32955 | 2025-11-16 04:57:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf2dc756-5c6d-3666-8401-f69c9816aeb8 | -9.35252 | -46.59987 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3334f0f6-609c-37c7-92a1-00640efef0c2 | -11.97822 | -44.95854 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 54be45bf-b2ec-3a50-af2c-9c7de1b866a1 | -9.16403 | -48.05231 | 2025-11-16 04:57:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f574340-84a3-3419-a0ef-99cb53641f08 | -12.66917 | -47.161 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40cf76e0-08bf-38f4-9f16-25acb5d42acf | -12.65805 | -47.16852 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5218caed-7682-3e55-89d2-77bb7089f966 | -9.06148 | -44.74994 | 2025-11-16 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5bbe674b-528c-3222-ab68-090e07522062 | -10.86268 | -44.88584 | 2025-11-16 04:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92599b7f-5005-329a-80d1-c4e90f3d0ca5 | -7.37607 | -43.3174 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54a655ac-9bf3-335f-a79f-817ea3ac88b1 | -12.87863 | -46.44516 | 2025-11-16 04:57:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6906a77-c1b1-3580-beca-b05435131b71 | -7.26716 | -48.0214 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3befdb14-81a6-3ad4-a6d9-33818bb46d12 | -9.71441 | -48.9024 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6e7ad717-76ab-3fb2-9bc2-2f22741468ed | -10.32403 | -44.60627 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 681100a5-ece1-3d67-8e95-dd839b9e0ab8 | -10.71242 | -44.52295 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44bab5cd-c8f9-368c-b267-04c19050598f | -12.0011 | -49.27431 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0eed1fe4-d70b-3237-9e53-51597f2c1e32 | -7.0548 | -45.94296 | 2025-11-16 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 300871fb-c7c4-34fc-8cbc-2d13d6881505 | -11.91761 | -46.22209 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e860fe37-4811-386d-a581-9db3e24518f8 | -6.77963 | -43.54473 | 2025-11-16 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0b62831-e05d-387f-85eb-0a17237c888d | -6.74403 | -48.19211 | 2025-11-16 04:57:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c5f1f2e-0463-36b7-8fbf-93bb0f23eb72 | -10.5438 | -47.92364 | 2025-11-16 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f64e009-36a7-3e8b-a72c-d632105072ef | -9.57766 | -44.61171 | 2025-11-16 04:57:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bfa57f99-02ee-3718-8cf3-aec25ed55b32 | -9.50634 | -47.26975 | 2025-11-16 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45a2721f-e788-3eba-ab6d-3ce4ea69cb52 | -9.72529 | -43.96024 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 12c1bba3-3681-3df6-8499-53d612263931 | -8.10505 | -46.03479 | 2025-11-16 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1ebb16d-c149-3dc1-bd0c-10708d1f94d2 | -5.64299 | -47.74303 | 2025-11-16 04:57:00 | NOAA-21 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c34f4a0f-4f56-39ae-a129-b2afeeac22e5 | -12.02022 | -55.51171 | 2025-11-16 04:57:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11cedeed-2b9a-3b12-96a4-fe708dbb0efa | -9.81274 | -48.16902 | 2025-11-16 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8bfeb4f-4ce8-3712-b87f-1afc6862334f | -11.91075 | -46.19822 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a809bc7b-3469-33ad-a246-93671335a776 | -8.45973 | -45.13669 | 2025-11-16 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1a44ec8-b7b4-390d-8977-8c29fef0c141 | -9.51178 | -47.27111 | 2025-11-16 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a443e04-a3c2-3b74-825d-af324f28ef09 | -7.39106 | -48.64914 | 2025-11-16 04:57:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 975a6eb0-0c20-38bd-b7ab-3ed78716382f | -11.03767 | -49.53432 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20c503b5-fe5d-37c8-a00a-01afb418b45a | -6.67054 | -42.0429 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3fb7e5b7-1184-30cb-9658-c0c9cd2012d4 | -5.12801 | -55.96706 | 2025-11-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cac64eca-8059-3e9f-8f52-c399f1c0430e | -11.41469 | -43.32935 | 2025-11-16 04:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1711d1a-c87e-386f-bee5-8324eb4a0d59 | -10.93524 | -48.69028 | 2025-11-16 04:57:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5f6ff41c-1895-339b-9597-c73a9b3036c6 | -6.56977 | -47.90089 | 2025-11-16 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a6aeaacb-0b88-3ecb-bd3e-71f95747c755 | -5.12335 | -55.97407 | 2025-11-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7214a25c-fcdc-370b-a35d-f28dd0112bd4 | -12.2281 | -49.63962 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c889fee-03e8-3dbe-b6d7-b8c25e982d1d | -10.94347 | -48.69395 | 2025-11-16 04:57:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98c5a868-76f3-358a-b5da-f1cc006a5a33 | -6.71231 | -42.13054 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1894d6e5-ca39-3f44-8d8e-572c2f969b7a | -8.73124 | -44.09981 | 2025-11-16 04:57:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 03ab4159-b489-3e9b-b3de-b961fa50d9b8 | -12.69906 | -46.78601 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44a52de6-101f-362c-b837-231e0aafead9 | -12.20529 | -49.61401 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f6bf880d-ceda-3e05-a715-2ff04fe38b33 | -5.13025 | -55.97514 | 2025-11-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fc8a496-cc7d-3691-a806-2406d39fc753 | -12.6939 | -46.78532 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fb57e1c-750e-3bcf-adfb-560731ae1d07 | -7.05678 | -43.94678 | 2025-11-16 04:57:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6b49d39-2006-3a80-b5bf-6445df7519a9 | -8.09996 | -46.03417 | 2025-11-16 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e174c38-a628-3de2-9e55-ec5df07931de | -7.05105 | -43.94577 | 2025-11-16 04:57:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cb3bb3a-0c10-315a-9616-609918f661e9 | -11.85013 | -56.89663 | 2025-11-16 04:57:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac7ca589-aadc-3ed7-a4e4-d6ecc16b15eb | -11.96196 | -44.94769 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d55a7400-c951-37d3-8256-b656cc76ebea | -11.49282 | -48.51833 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67daace0-1db9-3ee1-98b9-5b60e0f220de | -6.26038 | -47.07769 | 2025-11-16 04:57:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e09adf3e-a2ec-3a12-976e-cf56af412fe6 | -6.81334 | -48.78454 | 2025-11-16 04:57:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3db857e9-e5af-3743-a1f5-8a8200228852 | -6.67698 | -42.04915 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 55b7c53e-bb64-338a-9f1b-e3b67ee3552a | -7.37411 | -43.31614 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16f85148-3871-3d4d-99ec-2599a81f3082 | -11.7914 | -45.54131 | 2025-11-16 04:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 910f3009-95d4-33e4-a1d9-ef68aa6b618d | -9.08064 | -51.15883 | 2025-11-16 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3154d2f1-e829-3c82-b860-bd2cb770747a | -9.57831 | -49.10104 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80446c9b-9a79-3f08-86c3-1ed7a75f1c85 | -5.48266 | -49.58199 | 2025-11-16 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 778afce5-a2f9-3bcb-8789-51a75296deec | -9.06248 | -44.74223 | 2025-11-16 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f605232a-5f2c-32de-92af-745ef1ac4944 | -12.68765 | -46.79387 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ea6e2e1-75b4-3c1c-908b-27de2c6a135d | -12.21405 | -49.55028 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5192bfb7-f464-35dd-b859-0e975b8c934e | -12.8689 | -46.43676 | 2025-11-16 04:57:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 495d3c01-60a6-3b13-9f5f-aac131d56c8c | -7.34914 | -43.33647 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b4d4b1f-6393-3553-bd78-5043862ddec3 | -11.91156 | -46.19181 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9832ce1-28ac-3791-841e-9ef6362b7410 | -12.38103 | -48.09729 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b4479a6-f158-39a5-b3ef-868b09220f84 | -12.67272 | -47.17371 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b95cb04-f7b7-3182-baa3-1804772e8e8e | -11.70604 | -48.86465 | 2025-11-16 04:57:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d3ffba65-8d88-30ca-b6e2-95ea59c3144d | -9.83865 | -44.17738 | 2025-11-16 04:57:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b486620-8550-3916-89d1-4ffd6afd80ac | -8.2048 | -43.56531 | 2025-11-16 04:57:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5def4c45-8b97-35cb-8796-190a29aaf51e | -9.73127 | -43.96087 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1b809b5d-9b93-3874-85d8-28200e1f31d8 | -9.74597 | -43.96788 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c91c6c9b-b10e-3efc-8505-64b9e489a7e4 | -12.69675 | -46.78749 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af71155d-0e80-3b49-95eb-0228f6fae447 | -10.00217 | -44.76422 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aacaa4f0-b756-39c1-b370-93ed270dcb4d | -10.9896 | -47.72932 | 2025-11-16 04:57:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 144d3781-4449-3494-8314-8c51a5404000 | -8.7307 | -44.10391 | 2025-11-16 04:57:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e9b80ef-e761-362e-b1ef-144813b3e194 | -10.94404 | -48.69164 | 2025-11-16 04:57:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1790c4b-bceb-388d-897c-ec1d49899b90 | -9.73724 | -43.96155 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5d4b476-f644-3e52-89c1-97199ba6391d | -12.63736 | -45.07719 | 2025-11-16 04:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 443e344d-b400-38e9-9002-b1a655e13f04 | -9.85288 | -44.71656 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3e6c392-58d8-307d-8945-41b22a386331 | -10.00168 | -44.76811 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 18adbdcf-b631-3011-ad54-b7b477da02b4 | -9.85524 | -44.71808 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd363931-cd65-3f17-a87d-51b7bc829c10 | -12.65433 | -46.74971 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bc583593-1500-3b16-b0ab-881f29080a00 | -12.1963 | -49.61683 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6ef06ff-f961-38db-9d9a-74f786876161 | -10.54707 | -47.9345 | 2025-11-16 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11e5b179-545b-35a1-842b-f71ffc1f0682 | -9.56821 | -54.89978 | 2025-11-16 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8d4bfb43-5738-3ce1-aea3-3bf569201d20 | -10.39203 | -49.05452 | 2025-11-16 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3aef973-db2f-328e-b2bf-35638821afc7 | -6.68264 | -42.05065 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8ce255db-31ec-3482-a1e1-2454f5d18767 | -12.80385 | -46.44588 | 2025-11-16 04:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ebb6dc65-bc18-3b0f-9f16-74e9d9ee74c5 | -8.31694 | -45.40854 | 2025-11-16 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2cfc1e88-43a7-3ce1-aee6-ebc25b2a246c | -11.84903 | -49.21174 | 2025-11-16 04:57:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bef381e9-3044-3708-9f72-869eef8ddab3 | -11.71112 | -48.39314 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 523d7a49-4a00-3002-95bc-773f952a2305 | -12.67737 | -47.17727 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1510ceb0-2ccd-33e7-a8e8-fbc9a68b86b6 | -11.05339 | -45.15749 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ed1358ce-871d-3b85-8cf4-76f39d6ea703 | -7.90294 | -54.82482 | 2025-11-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3394dcf2-bc54-379e-8ace-54fd7bb63ff8 | -11.85062 | -47.59846 | 2025-11-16 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 915aab36-0fa8-31c8-a904-7b9b4babc1d5 | -11.85018 | -47.59888 | 2025-11-16 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |


[Clique aqui para ver as próximas entradas](README55.md)
