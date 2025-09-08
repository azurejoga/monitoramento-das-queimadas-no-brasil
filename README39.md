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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6874f01d-c939-3357-81f0-9aed4c2042fd | -9.82281 | -47.77194 | 2025-09-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f154163-1824-3918-8067-47059f5232e3 | -11.77137 | -47.5611 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a69a8fcf-0916-3537-9ce1-533f897d763e | -11.35367 | -50.38538 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0ba0df26-8660-31cd-8dac-977ee955b12d | -11.27811 | -46.42826 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8808a198-c239-3d4a-9bb2-f70066e69214 | -11.85709 | -51.05621 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f9b49be8-f966-3e19-966a-5077751e1795 | -11.99855 | -47.78019 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f9e62e26-bff9-3c93-9f7e-e45ae5baacdc | -13.64491 | -47.91664 | 2025-09-08 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fa4939c-bf9e-3053-a222-f1752f67095a | -9.9513 | -51.19545 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16b71eaf-960d-3a7c-8288-fc7a0ec9e653 | -10.14122 | -46.21556 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d10cc17b-732d-3e16-bbd3-fa2f7ce3e785 | -11.89876 | -46.65422 | 2025-09-08 04:02:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53400345-4f4f-361b-962a-cb40837938dc | -9.87747 | -46.53057 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64ca0bd7-8bca-3c76-bacd-65ea198c4f62 | -11.83493 | -46.76229 | 2025-09-08 04:02:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5209f6af-60c9-3738-9af5-a98d869a16e5 | -7.73561 | -50.30745 | 2025-09-08 04:02:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d47f49d4-c079-317a-90ec-86eaed84ba21 | -12.80989 | -48.16926 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee18110c-ae98-39ee-bd05-f9fd585e6081 | -13.8427 | -46.23868 | 2025-09-08 04:02:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afaa537e-40f4-3a02-9834-329bd41941dd | -14.99732 | -48.01392 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23ea10da-3554-3b48-901a-5113fc620979 | -11.40481 | -50.39565 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d1a3ca8c-8507-3dac-bbc7-25f658ba4c52 | -11.4164 | -43.63432 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0641937e-31cd-3c50-ba40-d96ccd954583 | -11.87544 | -50.96174 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa818db1-a43b-391e-b1be-0fcc7fc11600 | -11.27877 | -46.42456 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6751c2c-c52b-32f6-a4f7-557b2c88f0e9 | -11.22294 | -55.00887 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95af93d2-5b66-342c-b07c-5a261f26524a | -12.41208 | -47.49899 | 2025-09-08 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e56538b-3c58-39a1-8cce-4056a6ae35a8 | -13.63841 | -43.80897 | 2025-09-08 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 65f1c8c8-74ad-37f6-911b-9a2daa95f2d5 | -10.2181 | -50.52427 | 2025-09-08 04:02:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ede47e4a-7aee-35e7-8ca4-591285a3437b | -8.69933 | -45.31802 | 2025-09-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9f6d7b54-a6e2-31e2-b35d-2a12581020ca | -14.80826 | -48.24221 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f2cdf09-5a9f-3eb4-aa46-48563abd3f8c | -11.40793 | -50.38935 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| efb8d20c-4c88-3028-a563-292867684230 | -15.55567 | -42.67911 | 2025-09-08 04:02:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b3e3cc98-3cd9-3acc-a1ab-7261ae3334f7 | -9.19866 | -46.03803 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa505435-5b95-39df-be81-581e81f8877e | -16.33909 | -45.05166 | 2025-09-08 04:02:00 | NOAA-20 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abba4641-80eb-3bc7-a90a-3e578b41d45b | -14.50987 | -48.80558 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25b84fc1-b0e1-360b-817f-454d15598c2a | -10.29206 | -48.80984 | 2025-09-08 04:02:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d45fcf4b-dd1a-3dc8-b7e2-24514564ac49 | -11.31903 | -47.33593 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9c55f05-b76f-3cd8-b17d-68f9cd8582d5 | -13.72229 | -46.89223 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f9771ff-67ce-3794-9acf-f6425ddee061 | -13.83411 | -46.24196 | 2025-09-08 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 37004f86-b415-32e8-b1b6-5818e6b0c4e6 | -11.4199 | -43.63493 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 55fc2117-4391-363b-9192-03aca60e6748 | -9.72122 | -43.98417 | 2025-09-08 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 67bd6457-41b2-3ce9-8dc9-40a62dfe720c | -13.7091 | -46.87262 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b25c4af-cca3-3bff-9aa6-ae2fecbbb9bf | -14.73771 | -47.77155 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9d15196e-8e18-3ffc-a3ba-794a600441ab | -15.2876 | -44.76951 | 2025-09-08 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc2f17d4-1fd2-3046-85d9-9cc4815c60b7 | -12.93447 | -54.77105 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ddbf293-e939-3dc0-b099-837b0486eed0 | -9.84608 | -53.29867 | 2025-09-08 04:02:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1322eec1-ed0c-3e73-a37f-e106785974bb | -10.7778 | -46.01329 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a0b0b74-7005-3402-a7c5-1d9545acd298 | -9.71749 | -43.98072 | 2025-09-08 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| efeae96a-e7e6-31ac-93a4-b461f977493d | -15.00064 | -47.02335 | 2025-09-08 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e019365-2cc7-3025-8856-6350e8db8dd5 | -8.19289 | -50.1396 | 2025-09-08 04:02:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86c75283-82d9-3494-afb9-83ec30615be5 | -12.00379 | -47.77655 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 99f3050c-8113-36ca-924d-021e2d59b549 | -14.51424 | -48.7566 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 53413ef9-8d52-3d20-a409-264a051ad79e | -11.21672 | -55.01621 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2883615-2dbc-3751-a024-ca52f22c76a4 | -9.86699 | -46.59045 | 2025-09-08 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e136b4fd-1e37-34ac-918f-fc9b68c6dacc | -11.40918 | -50.38261 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 439106be-04d7-3e37-94f1-35f554cdcaaf | -11.37381 | -43.53849 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6e0b9a2-bb90-3a5b-ba1c-653314729a6d | -15.1868 | -47.95753 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9dd2dee8-96f0-3236-912b-ba5e4d2ba772 | -12.9439 | -54.79293 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bb15b5b4-1f8d-3941-bd7f-2dd4ee1266b1 | -13.0362 | -47.12587 | 2025-09-08 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48cfd1a1-78b1-3609-953a-8ee1aad9ca7c | -13.8261 | -43.86082 | 2025-09-08 04:02:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bea64614-1842-3eed-a62f-0e299081384d | -9.83762 | -47.79466 | 2025-09-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cab6558f-8466-30c0-a066-9be586902994 | -15.02492 | -45.46644 | 2025-09-08 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ef9918b-1da7-3485-82bd-4da5dd55c268 | -11.19706 | -55.00502 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| e4905001-fc0a-36e2-bb6b-bc5634022e90 | -11.39408 | -43.54601 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f285912-d4a6-3d4f-b87a-b2c3ad58ffb8 | -15.17188 | -47.96733 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f33b881-3363-33ca-aae8-5aa6e93fb5a5 | -11.03315 | -45.94618 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5d42f47-64e0-38ed-aebe-2b6d92613877 | -10.14468 | -46.22001 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2bc0a20-3a94-3410-b64e-04c4fefcde81 | -14.68958 | -48.19836 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58756bcc-e537-3ecb-9d1c-faf9d7b16ce0 | -13.8207 | -46.24974 | 2025-09-08 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfd7b53c-8129-3503-bafe-b1e2b4ceb287 | -8.82259 | -45.89656 | 2025-09-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc725a58-4da8-3ce6-a19a-3304055982cc | -13.82674 | -43.85696 | 2025-09-08 04:02:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35a7d74c-6380-3ecb-af54-90faad0f1c20 | -14.79535 | -48.23926 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 841ce1aa-5c17-3e47-8159-572aaaeeb371 | -10.14254 | -46.208 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4e674cb5-7b0d-3e06-9e65-fc94ad9a235c | -9.95712 | -51.19607 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e2731e9a-efcc-31f3-a7bf-2669ff1bbdcf | -9.58401 | -48.29408 | 2025-09-08 04:02:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3ad3159-c336-3af1-becb-c479225dcc2d | -15.42013 | -47.68396 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1beba14a-953d-304b-951f-57aee3c8a891 | -11.61017 | -47.14876 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59b0919d-3406-3aae-8e3c-b5084b960e1c | -14.804 | -48.24097 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d756e33a-47c9-3613-9941-0b965e1be66c | -12.82286 | -52.93789 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ed715d2-8e55-326a-b842-1a63c4d977a2 | -14.99307 | -48.01307 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa74bd38-952b-33d1-8aec-0badc8df4c19 | -11.41106 | -50.37251 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0112abf5-0212-3814-b28c-22ea5b5de4e9 | -11.40981 | -50.37924 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83a91258-754c-3b1f-bf79-2da799a50414 | -9.99139 | -51.67419 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 139c7830-bd1e-3d20-8408-40b28454604b | -11.65801 | -46.88085 | 2025-09-08 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b552130-6a40-3c7d-9fce-ca184995fc18 | -14.51705 | -48.79199 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0af6efe3-2d8d-34e2-b06f-a242c19b937c | -14.73845 | -47.76758 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eba4860e-37bb-3223-b84f-0d42b89114c7 | -12.8146 | -48.00093 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2005b770-4ef5-3e01-97b9-3f75ec600359 | -11.3299 | -46.56747 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acdadf3a-cf7a-31cd-a3ec-90116113780c | -11.99987 | -47.77726 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a052f3c2-a459-3073-ac5d-4c6ef9ede8b7 | -12.94251 | -54.76638 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 547dd079-99f2-3a7a-9658-9c87058cf153 | -11.01965 | -45.9297 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fed73832-a0c9-3d4e-a1f2-05ad8f3cc1d2 | -9.84464 | -48.85681 | 2025-09-08 04:02:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1ec7b486-2ba8-3cf1-86eb-35a0073cc707 | -14.99583 | -48.02187 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1b12994-cfd6-3865-b34a-7cc69966f7bf | -8.7002 | -45.31283 | 2025-09-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 5c36d408-9721-3980-a2e5-03d7a7d838bb | -10.07582 | -48.10194 | 2025-09-08 04:02:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b883946e-ecfe-32d1-8601-9eaa8f7425df | -12.1692 | -43.9449 | 2025-09-08 04:02:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9cf834f1-1424-3c03-9240-45a83a1fb4fe | -12.82792 | -52.94568 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b5332715-59a4-37db-b112-9eb3c64bfb16 | -11.20606 | -55.01925 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c686d2fd-83cf-3a83-a6c7-998d0f836394 | -11.62729 | -47.15149 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3cfcf7ce-4b80-375e-8ace-04ebd4b0eb07 | -7.67098 | -50.29448 | 2025-09-08 04:02:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 504b13c4-f9a7-30f4-ba60-d01da6ae8d0f | -14.52588 | -48.76941 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f068bca6-583e-3936-a3ba-0dca54d3537b | -11.33594 | -46.57128 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3085091d-ca6c-3ad9-8cc0-66d18b906634 | -12.80637 | -47.996 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f6c1db39-0fdb-30d9-bc91-cd1997d21f3d | -12.82985 | -52.93645 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README40.md)
