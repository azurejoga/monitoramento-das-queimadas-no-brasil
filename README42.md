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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f34e7b3-769d-3b0a-8b00-b606c8d8607f | -9.85033 | -48.84536 | 2025-09-08 04:02:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6842a50d-1c89-354d-8568-77e9f562abfc | -9.72483 | -43.98483 | 2025-09-08 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b2d8207-6bd3-31b2-ac9f-6a4a63c7288c | -14.51697 | -48.76711 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 25676491-cedd-3094-8517-44d0b8449617 | -14.29711 | -44.87583 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| badc6858-6acf-3a52-bbe1-bd4752700284 | -12.45977 | -44.64765 | 2025-09-08 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9906bce2-dc53-33da-8afa-e8425b9da228 | -15.28407 | -44.76887 | 2025-09-08 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cd4dc5b-3eee-32cb-aff3-0db001eba505 | -11.02663 | -45.93661 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ad08735-010f-3f6a-8190-71282401a394 | -9.19798 | -46.04195 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5aa6a611-c43f-3ae1-9ed6-c94e1d728f99 | -10.78351 | -46.01101 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e026eeb-1a5f-3849-99e5-1f1d980d6b82 | -9.06799 | -44.36974 | 2025-09-08 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 642bd2e5-039f-3cbc-8df1-36cf365dc13a | -9.70634 | -43.5152 | 2025-09-08 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b6eea7e-1d69-3b83-8251-89978e37af70 | -9.07913 | -46.98328 | 2025-09-08 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6a55cc1-60d7-327d-b2a4-5340c27c69dc | -15.29833 | -43.38341 | 2025-09-08 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cd7657d6-86fd-35b9-812a-7c6dd13bf994 | -9.81825 | -47.77101 | 2025-09-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 394532bd-94aa-3f51-88fa-da1ea43c9ff7 | -16.34097 | -43.03485 | 2025-09-08 04:02:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bda9739-3c69-3b14-9f4d-7f152359a57f | -15.19156 | -47.97939 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0728942b-15f3-300b-9715-ceb8788521ce | -13.92214 | -48.03701 | 2025-09-08 04:02:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f98fec6-5762-3960-828c-b6ee7665a7a6 | -11.35431 | -50.38202 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2e436e53-5463-3faa-ac27-7f86b7036a1e | -15.18955 | -47.96643 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac2c00fa-c668-3dee-86ef-20e10ab5f64b | -13.72628 | -46.89331 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b959e304-c838-361a-a941-14fa61f8bdac | -14.50512 | -48.75546 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98b0c6b8-f2d3-39f0-9ab9-4c5e63f71aa5 | -11.34162 | -46.57346 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec0c5c62-4791-3eda-b7c8-0530b6897d90 | -7.76919 | -50.76782 | 2025-09-08 04:02:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d0b8b0f3-d7f0-37a9-a7fc-56ae4358e33c | -9.20237 | -46.06576 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b739e59-a828-3461-be55-6c644ebd7f65 | -12.82194 | -52.94247 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 867c1233-72dc-338f-ba6e-f457b0dcd1c2 | -11.41 | -50.36884 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87ccc1b5-f6a6-3b26-98e6-bb51a7ee9106 | -14.52056 | -48.77295 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b070633f-586e-3bf7-8d1e-2c024b79fb0c | -11.4073 | -50.39272 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d363c74d-bd96-316b-bb2c-3539ee29069a | -9.85139 | -48.83938 | 2025-09-08 04:02:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 40bb2958-b2a9-35da-af53-b80dbaed50a3 | -11.3028 | -46.52801 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e99a98ba-9d13-360f-a88d-2fbdf909195d | -10.13974 | -46.19985 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b1635329-2a73-3402-ab64-b0663ce5c2f2 | -11.76131 | -50.63395 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3cb7149-04ca-3552-b19f-b68cb093200a | -11.32142 | -46.54292 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0c331a4-2cba-31c1-a752-16be4e20d3dc | -13.64533 | -43.81005 | 2025-09-08 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1d927644-8af3-3e48-be06-be9434a2da04 | -11.28108 | -46.45907 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 30149652-0329-328f-b34c-abd673d979c9 | -13.03689 | -47.14599 | 2025-09-08 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e68aba21-c6e4-32e0-9833-52000c4b2943 | -16.24993 | -43.69925 | 2025-09-08 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc18c435-7282-3a5f-b0e7-aadd36a596bf | -9.14469 | -46.06767 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f5549ec-1a64-350b-aa02-299ea9315a96 | -13.72909 | -46.90093 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e5e6ad5-dcb8-3c67-85ec-16c623fb9e5e | -13.81504 | -46.25901 | 2025-09-08 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff17f54d-15ad-34f4-bce5-a04b36cb6c33 | -9.96284 | -51.20155 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1f52298-66ff-35d6-b2d8-0ad2787b6f5f | -7.76839 | -50.7723 | 2025-09-08 04:02:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fbe01011-b525-3444-ac64-2a43b974898e | -12.89217 | -47.99647 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 376e58ed-5d7e-3e09-bd2b-efe9f9553b54 | -9.81736 | -47.7759 | 2025-09-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c6d76c9-549c-3f16-a9ac-74f7e23af8f2 | -10.17972 | -46.23785 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b0c975e-722f-372e-adba-54c3bda8458a | -12.83493 | -52.94239 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5b02bc6-646d-3221-af3b-0c320ebfe65d | -11.39279 | -43.55385 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 204a9ccd-48f0-3045-88c1-5e667744c501 | -15.29894 | -43.37971 | 2025-09-08 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ad5ce46-d5cd-3a48-8c78-b99cbc9b9b38 | -13.03135 | -47.12898 | 2025-09-08 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dfdb8d4-fc7c-33e4-9f43-aa42eef69a6b | -12.19632 | -53.90271 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28164817-9788-3b32-9376-7e2b55e7ec7d | -11.86523 | -51.07306 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f042d62-58e6-33ea-a5b0-6753e3e36232 | -14.49905 | -48.81343 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e6559d9-b854-32ff-87fb-9d573e29f462 | -14.28994 | -44.87461 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7864edc3-609f-3895-afe0-155690286d3d | -11.35304 | -50.38874 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 92b725ab-71b6-3103-83ad-2457146e4bdc | -9.82273 | -47.77397 | 2025-09-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c50a3382-b41d-3861-b176-0f7ba6225b74 | -11.60443 | -47.15625 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 141295b3-f7dc-3928-8997-b814004c6f68 | -11.40639 | -50.36808 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7008dcb0-b92a-30c1-a348-d0673ccc509b | -14.93822 | -40.67474 | 2025-09-08 04:02:00 | NOAA-20 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e05886dd-bace-32c1-afeb-8ccb4e694172 | -15.53236 | -48.34739 | 2025-09-08 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce60d8f2-4a94-3c2c-a691-a5340064a63f | -10.29105 | -48.81527 | 2025-09-08 04:02:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9ab39a2-f600-326b-9c41-e389698f78fc | -13.52184 | -42.01265 | 2025-09-08 04:02:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 51fcf6bf-79f5-3ca5-b513-e178d8e051db | -13.72344 | -46.88581 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b93cb52f-add5-395d-8ace-33c2f83331ad | -8.19211 | -47.56281 | 2025-09-08 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 148e4507-1a95-375d-b099-f67a2d3bcfe9 | -10.82045 | -47.73626 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2364a7d5-8faa-3e25-b470-c64992f1a296 | -15.38206 | -46.4205 | 2025-09-08 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d1cd552-e51c-347d-ac40-e5223906fe65 | -14.6002 | -48.09383 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a36aebaf-96d5-38b4-b5ca-f64901107441 | -12.828 | -52.94375 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b7c42f2-c2e1-319c-bbc5-7de72e80a891 | -9.14606 | -46.07109 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be303d3e-4f18-3571-a705-2695f8ca32e3 | -13.91237 | -48.01719 | 2025-09-08 04:02:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb95d8d0-5da2-3451-b437-45eafd9ed39d | -9.71679 | -43.98495 | 2025-09-08 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 357ddb35-e1e1-3d35-a2ff-7821d00d420a | -9.20562 | -46.04696 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de9b4915-d7fe-339f-8ec0-3110ba3977b8 | -11.03253 | -45.9497 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8c7e7ef-cffc-3625-bfe3-550d219632dc | -12.83406 | -52.94506 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2aa6b7a3-68fd-3af5-9617-e8af6a4645f1 | -8.87043 | -47.90605 | 2025-09-08 04:02:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e20cdf73-4968-30a1-bda6-01350db176de | -13.64187 | -43.80951 | 2025-09-08 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0dfdb0ac-ab29-3c82-8981-46ee611a1005 | -11.99936 | -47.7758 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 90803889-b8ed-3573-ae63-62ab00f45941 | -14.32221 | -44.9239 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 267d09a1-e5b9-3dfd-bbfa-b4ffd19ef560 | -11.40856 | -43.5889 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf92d1a1-b9cc-376b-9ee8-0130ea530820 | -13.00009 | -45.21263 | 2025-09-08 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a4cd0124-a905-30e7-8445-b21447613a4a | -9.79982 | -46.23056 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1020b3f-9087-338e-8b64-c8130f432077 | -15.44917 | -45.6611 | 2025-09-08 04:02:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 343a9140-68cc-302f-9b5d-5af4ec3adb09 | -11.30216 | -46.53164 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f009962-bf72-3304-ae5f-5651a1fb26e9 | -14.4692 | -48.79762 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fb9ca47-b3de-3aa7-b327-52074b7f4247 | -11.40326 | -50.3849 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5219824c-147f-3ba2-8109-21744afa807f | -11.40611 | -50.38894 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6482b57f-29f7-3845-8af9-80f9de872105 | -15.18659 | -47.98262 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78be36af-0f5d-3a30-9918-7d48c2b5d3bf | -9.57925 | -48.29318 | 2025-09-08 04:02:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 913bb52b-a139-3bca-97f1-5bbbf7d639cb | -15.09056 | -48.14371 | 2025-09-08 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 625dc43c-bed5-324d-8d5b-92297f88e072 | -12.83062 | -52.90244 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 21702c93-c750-3407-8b65-f5fec1b7ff78 | -11.40389 | -50.38153 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 77fcd254-3958-3822-84f8-eb2d22a8bf19 | -12.82888 | -52.94111 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 10f2d54b-71d7-3fbd-93f4-bd615246f853 | -11.85638 | -51.05986 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 137e905f-5722-3832-8a84-868e1d6d3850 | -13.51813 | -42.01584 | 2025-09-08 04:02:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4995f6fb-6c59-30da-9812-45cdde3fd23e | -12.93717 | -54.79147 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1f919c9-e15e-3ce9-9079-dda5c12dc5d1 | -8.18637 | -50.14771 | 2025-09-08 04:02:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d05da43e-b242-3d62-82b5-11775faa65cc | -13.54512 | -48.11565 | 2025-09-08 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 238e401f-ed48-344a-bb76-ed2696290d60 | -14.50624 | -48.79988 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbd7e3ec-ec6e-3b7d-84c7-bba20737d343 | -14.81664 | -48.10001 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 199e1d16-83c7-3dff-8612-b4aa221b8205 | -9.72041 | -43.98566 | 2025-09-08 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f7b85160-7788-3d7d-8b93-32a3170b5e77 | -12.93181 | -54.78357 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README43.md)
