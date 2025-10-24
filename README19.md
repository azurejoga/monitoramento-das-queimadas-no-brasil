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
| 0a8c1f9b-149b-396a-bc2c-646461b896a3 | -6.29056 | -40.86756 | 2025-10-24 04:17:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| de9a3a94-94b4-3d39-85b0-133dcef42fd0 | -4.27515 | -48.33903 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e15729f9-c2e2-33ec-8eaf-e07b36454a14 | -12.27478 | -47.02426 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ac9cdc0-23dc-32c5-b551-46959fc9fca4 | -6.31304 | -41.85609 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0cf64bf6-22e3-35ee-9d0c-f1cefa1d4278 | -4.80291 | -48.23106 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3363a68f-3b79-364a-bd4f-396a452436c2 | -9.64486 | -46.89182 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36e1f45b-02b0-37e1-9a4a-b45ddf7892e6 | -2.74009 | -48.68881 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 108fd989-8c0e-310d-8bc2-e5e201e3ef46 | -2.86714 | -41.74457 | 2025-10-24 04:17:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40e5725c-c032-388d-bb15-107a047e1353 | -2.86592 | -50.72257 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d749d5c7-7786-36de-a21a-f31ed79c3251 | -5.81704 | -46.21359 | 2025-10-24 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02881dd4-6af6-3a5c-b1eb-c06ee00d50b0 | -12.05992 | -46.42673 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45b57573-00ce-3b3d-bee9-90ff61d6acd9 | -10.66527 | -54.3129 | 2025-10-24 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b404679-2fde-3304-9d32-ac73e600474f | -9.77992 | -43.8576 | 2025-10-24 04:17:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44e7192c-7560-3198-823b-d10db449b12f | -9.64135 | -46.88431 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c24f36ce-d1ff-3ca3-a373-2f9d899fcc3a | -11.06815 | -44.85873 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b676ca80-67de-3cd1-bfad-107fb44fcc99 | -5.75954 | -46.68257 | 2025-10-24 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f861cb7-05f4-31ea-868c-d8326dfe5b10 | -11.35718 | -45.95945 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c846d41c-d077-300c-a599-6db3c5f9d12f | -9.11856 | -48.898 | 2025-10-24 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b00949ba-7d95-3fc8-9710-5c70ebe7b107 | -9.19059 | -44.53983 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef262e85-cb6a-384b-be0e-3ccca01333f3 | -2.42043 | -49.28032 | 2025-10-24 04:17:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1062d99-b0b8-378f-8982-0bdab468e688 | -4.9876 | -39.87625 | 2025-10-24 04:17:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5d6ebde5-5cf9-3a2f-8a8c-66089b312d8d | -10.90632 | -48.04602 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 24346ea4-406e-3748-a012-8ea5b926def5 | -11.35657 | -45.96315 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40d1bb28-38ff-3d46-b0f9-963378977805 | -3.02454 | -49.44801 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 025b1e90-ee02-300d-b5c5-da17698e429f | -8.44664 | -49.57278 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e2a90b0-2371-3674-9c61-46ff08dd1acd | -6.15536 | -41.81725 | 2025-10-24 04:17:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8892dffb-2a79-356c-b54d-1ea27ac887db | -10.47092 | -49.09593 | 2025-10-24 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd33ddd5-18fc-379c-8e50-7f56c95b8aeb | -10.4269 | -49.36776 | 2025-10-24 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21cc7588-b82f-393e-b860-cbc612d1a041 | -9.86941 | -47.4693 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 223b1979-cc78-3ba1-9506-5f1863426928 | -11.36704 | -45.94201 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1199241-97e4-3070-b6f2-ad8d68b4426b | -2.86659 | -41.74804 | 2025-10-24 04:17:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0ee90b54-21e3-36f3-a3d5-76e1bf0f7a3a | -9.55556 | -46.70162 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db542671-8f11-31c4-8566-9b55d39adf11 | -3.47343 | -52.98756 | 2025-10-24 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e54acc49-b0ae-3375-9fb7-b387ceea4c5c | -6.0973 | -47.00331 | 2025-10-24 04:17:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0898807b-3dd8-3dd2-888a-89761075e160 | -10.04295 | -47.10004 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31755f10-13a6-3ab7-b117-287cb685b778 | -6.11787 | -41.74238 | 2025-10-24 04:17:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 03e4a6ce-0f07-3008-9073-babd3c48401e | -2.80375 | -51.34992 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fc609ad-7a2e-3332-a46c-c1b23197afe2 | -5.40723 | -46.40941 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 667c1ebe-3fa3-3eea-b5d2-591db49a77d7 | -4.85244 | -46.72621 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e0cebef-b8f8-354f-ad8f-e02255bc2ae1 | -2.4733 | -49.23858 | 2025-10-24 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1987b51-2157-366a-979a-eadaf7c09b13 | -10.11247 | -47.77591 | 2025-10-24 04:17:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 596f6a93-c359-3563-8ca7-1eac16872bac | -6.30042 | -40.87292 | 2025-10-24 04:17:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cd2c4052-46b1-3329-a180-cfd0df817c86 | -10.64234 | -42.30391 | 2025-10-24 04:17:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 730c3059-1c04-3230-bf38-675d6542c56f | -4.30754 | -41.48971 | 2025-10-24 04:17:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3c4a805-b171-3739-ae8f-b1fc1d977934 | -2.47565 | -49.22433 | 2025-10-24 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2736aacb-f27f-3111-9932-eeea1cb33d42 | -1.92352 | -52.14096 | 2025-10-24 04:17:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52e519b7-cc73-3b65-9a48-1e5b89ba6740 | -4.33444 | -42.7579 | 2025-10-24 04:17:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59196ae8-6663-3025-a06f-1db2390b8673 | -2.85683 | -50.74541 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f529158f-d2ce-3ab4-9e33-b6d22650fa62 | -9.86061 | -48.27189 | 2025-10-24 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fd39650a-3989-3912-b18c-ee0e1943504e | -2.42104 | -48.44005 | 2025-10-24 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d872fb4f-13a8-3e13-aae0-5ffd0386c73a | -1.54022 | -55.40751 | 2025-10-24 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e91d9e67-48c6-38e7-97e4-d2a310c8b90e | -12.17869 | -43.60985 | 2025-10-24 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0b87a06-700d-3505-a728-0b445803c490 | -4.27578 | -48.33521 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8baf0ba4-bfcf-3e72-ac37-3cab35f1de6d | -9.31078 | -46.96761 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a72e3e87-00e4-36e4-8740-60080d5e48bf | -10.51975 | -44.16654 | 2025-10-24 04:17:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe3fb7cf-b693-3972-9b48-0b0c51e73476 | -9.64359 | -46.8932 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0c796e5-15e7-3957-80f1-954bfc651fe8 | -11.97458 | -49.17927 | 2025-10-24 04:17:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 04f3fb9b-f0f9-3fe4-9cd7-47f8f6aa76d8 | -12.8858 | -43.43222 | 2025-10-24 04:17:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97e38a33-7a90-32fb-80d9-adca5871104c | -4.1843 | -46.22662 | 2025-10-24 04:17:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e50c6cf5-1baa-3702-936a-cceb77dace65 | -9.63642 | -46.89188 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c1a78ad-0bf4-352d-9250-feb8fe0fc2e6 | -9.18948 | -45.69227 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6aa04c2-5276-3f87-aa82-c60b0f7e083b | -11.34066 | -46.73716 | 2025-10-24 04:17:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf61e748-7013-3ea7-bb78-7cce3c3c3c71 | -9.44853 | -46.09679 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43ca7815-1aa0-305b-b1cd-5d0c0a8089a5 | -9.0873 | -47.8218 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0f8ef66-9e5c-38df-8290-6360d618a4e5 | -10.91404 | -50.16296 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f2e8e81-a68a-3724-8692-17b45eec3fc4 | -2.44608 | -47.15473 | 2025-10-24 04:17:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77c9ed73-c552-33ec-9ab8-8a03926436c0 | -11.04384 | -47.89642 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c499f14-3fcc-3ac5-938e-fb76dc3284e6 | -4.47254 | -49.10275 | 2025-10-24 04:17:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ed1eb1c-acd1-3f17-944e-4d2035d8330a | -9.61077 | -46.91303 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c822f9db-f3ed-35e7-846e-c8d36c82502f | -6.91301 | -41.54275 | 2025-10-24 04:17:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0340fa96-24ce-3e2b-9e3f-1b5953f9e5c2 | -10.64179 | -44.78232 | 2025-10-24 04:17:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a987273-cce3-3589-a809-dc97e0130290 | -2.873 | -50.71157 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6bd6f6c-968a-3be9-b10c-8b31f71dcfdb | -9.60647 | -46.91666 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 909083e3-5715-3503-b1ef-efc578d43b65 | -5.54447 | -41.36964 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 032534b6-ed37-3f56-b2e3-752da2521640 | -11.35378 | -45.95886 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9cceeab-12d2-3334-8062-0c9f248fbac8 | -6.84929 | -41.54793 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b7523bf9-2450-37cd-a7db-ee70a9de9419 | -4.29066 | -40.7052 | 2025-10-24 04:17:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 81e18262-af41-37bd-8357-5948c65c86ce | -6.84078 | -41.55787 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ff0636dc-8e4c-3350-9c50-c70bba2c8a66 | -8.83177 | -45.41714 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6019a3b2-a60c-3cb7-9f85-ddda11180b0e | -4.31446 | -45.06424 | 2025-10-24 04:17:00 | NPP-375D | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36480b68-6d3d-3afa-b8ea-139a40fb329e | -3.03142 | -49.49388 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cf4f629-366f-301e-b18c-3bee46e15f2b | -3.12981 | -49.52224 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab6e0446-afc0-345c-b80a-d4520b42d33e | -10.61723 | -42.30765 | 2025-10-24 04:17:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| deed01fa-bfae-3981-9f26-23a503ceee7e | -12.15411 | -47.01248 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3591360c-7203-3a0b-9e04-f8a9dd9efb35 | -4.87658 | -47.54564 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63e6000a-b7b0-30a9-86e3-59b076040aaf | -9.30401 | -45.19968 | 2025-10-24 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8109a3ae-2836-3e13-8d56-3beb60e8a474 | -9.60287 | -46.91608 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a6482126-e78c-3490-ae68-8a1abe676738 | -9.9681 | -46.34561 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8241cf56-c2b0-3ed3-a96d-f24d889f7532 | -3.44527 | -41.85223 | 2025-10-24 04:17:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0a980040-c9a9-3343-afc7-5672c485b4b6 | -9.60205 | -46.89878 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 74d36807-ec07-38e1-a677-47515ebee4da | -2.85423 | -50.74399 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83ac6336-98bd-3dcc-b659-22e54b6689f9 | -2.81314 | -49.13683 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81eab5b7-4947-3bf7-a7f4-149ad8eeae5d | 1.19166 | -51.05647 | 2025-10-24 04:17:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9a0f7ee-eca1-3fe5-bc43-dcf3acba9152 | -9.87019 | -47.72375 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2c44664-9d9c-3695-bde7-7fd516ed3ddc | -6.28708 | -40.86704 | 2025-10-24 04:17:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e7997a96-f98e-3d2f-abbd-65b8c3b4a69a | -4.78541 | -37.75506 | 2025-10-24 04:17:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9ec68284-e860-3d9b-88e1-d951df5e7851 | -12.22481 | -43.31076 | 2025-10-24 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97f4d651-26cf-30ec-8d67-f68af4fcde8d | -11.04304 | -47.90106 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59a0ef66-1d4d-32bc-9662-81eb298b61c6 | -12.0671 | -46.40456 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3b372dc-5be5-3d48-8dd5-f4d28fd40c88 | -10.61437 | -42.30337 | 2025-10-24 04:17:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README20.md)
