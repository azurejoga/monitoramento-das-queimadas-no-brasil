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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15088a44-f82b-3e8b-9de1-5576ae108bf2 | -7.8157 | -41.77106 | 2025-11-13 04:14:00 | NOAA-21 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0725a6cc-37f2-348c-83de-45baf6297f39 | -8.72945 | -49.59599 | 2025-11-13 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd30b34a-ff66-3c83-a575-d9b6c25cae38 | -9.85856 | -44.57554 | 2025-11-13 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84ba5fae-8976-37e4-866e-aee2a8a103d3 | -10.29214 | -44.95185 | 2025-11-13 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d073f3eb-865c-3713-ab49-bf0ade79ad27 | -9.63473 | -44.54985 | 2025-11-13 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd78ec74-1718-3857-93af-a29bc9c141bb | -6.95175 | -43.65546 | 2025-11-13 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa9ae61d-fb4b-31cc-b539-dcab00a277cf | -9.01689 | -45.4307 | 2025-11-13 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9c95a0d-c7bf-3b5d-91d4-583beec4d867 | -5.62172 | -46.91548 | 2025-11-13 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0357487-8f63-37b0-b6e5-d984cb4449b5 | -10.89019 | -44.40102 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6c4e060-10eb-38da-befd-14d03d8d772c | -7.87222 | -40.21179 | 2025-11-13 04:14:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 641fed43-4b69-3fc5-b583-7a66d6867348 | -11.73354 | -48.5312 | 2025-11-13 04:14:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab35d657-d1ff-3cab-a547-72dd96a43856 | -9.64566 | -44.54478 | 2025-11-13 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb15e19c-a43e-3cb2-93f8-e2b6f5c7aa66 | -7.25917 | -45.37054 | 2025-11-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d29e6d3d-2f70-3e36-b3af-f54f0a4a53dd | -10.91862 | -44.62883 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bae79746-f91d-37db-ae10-9f6b5dc39014 | -7.47875 | -42.55 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a9b1a588-762e-32ed-b0e1-6cf5cf83c714 | -12.60287 | -48.37014 | 2025-11-13 04:14:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ef075dc-1ee0-3b87-b5a1-5f34789a69be | -7.80085 | -42.622 | 2025-11-13 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 511a368a-8687-35b7-b591-e80b37140534 | -11.81148 | -44.25307 | 2025-11-13 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dadf7a40-4162-3327-881b-25a66d5bd11b | -7.1064 | -42.36313 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9138748d-d2c6-3784-99d6-59845f8ecbaf | -5.35502 | -46.76381 | 2025-11-13 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b598b991-28c0-37af-a754-527550cdd695 | -7.22565 | -39.95828 | 2025-11-13 04:14:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 110fc44a-d8e4-3300-8d48-4d31dc3d00aa | -10.76654 | -48.13787 | 2025-11-13 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf70d1f6-9d11-3eee-b570-6b9cdd17af88 | -12.10952 | -43.6487 | 2025-11-13 04:14:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5480add-8a9d-3c55-b780-2b2668e50360 | -6.3011 | -47.01323 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c62dfa06-1be6-3cb2-99a9-3e5c661b1303 | -6.74097 | -42.52682 | 2025-11-13 04:14:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 2dfd2569-6fdd-312d-af84-42ddaea8a60e | -10.72062 | -45.14649 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 289c5dac-4dc5-38b8-9669-e86f67817833 | -7.82975 | -41.76952 | 2025-11-13 04:14:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1d23c739-c444-3918-b1bf-ba50fd204eca | -10.50051 | -47.98632 | 2025-11-13 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6912c773-b9a1-3935-8fc6-1da4b6872dc9 | -13.17858 | -43.05448 | 2025-11-13 04:14:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3cd29e12-f992-3a02-b9b3-346ed6cfb184 | -12.65479 | -46.74309 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c6a2eab-e46b-38fa-a336-c93e6c9cfcfa | -7.90258 | -43.17212 | 2025-11-13 04:14:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 98be1393-55d8-3ede-9e1a-bc2717407a23 | -8.25717 | -48.12856 | 2025-11-13 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d40ce844-9f9d-32d2-b408-a5a656829188 | -5.72916 | -46.54929 | 2025-11-13 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b063ea80-2a94-371d-af45-e4dca07bd7f8 | -6.14791 | -43.2961 | 2025-11-13 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 37e66270-64fe-3d6e-b6eb-113ce9c18b14 | -9.6314 | -44.54932 | 2025-11-13 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbba0ef3-2ae6-363d-89dd-11a7319a0dec | -8.47096 | -47.98402 | 2025-11-13 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b77d31d8-5044-3f9a-9112-cb1b5e34e5ea | -7.22225 | -47.98365 | 2025-11-13 04:14:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ad29c8b-7b00-380b-8150-24c9b22c7ea0 | -10.49673 | -47.98568 | 2025-11-13 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d205e60-8575-372e-8331-39aa09c68507 | -10.53856 | -47.99131 | 2025-11-13 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bc698d8-68c3-37d9-8ec1-6d92cb3949e3 | -11.02264 | -44.6384 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3debb799-838c-31b7-94d2-842ef9522b92 | -7.82018 | -41.76437 | 2025-11-13 04:14:00 | NOAA-21 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c6e3ac00-5c93-3f9d-80f7-1697b4dee99a | -5.72596 | -44.83582 | 2025-11-13 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea681466-a9f0-3042-8edc-024fa05c2d7f | -12.66309 | -46.74848 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 8bb66568-ccca-3c01-a5c9-eec918c69183 | -9.74669 | -43.90817 | 2025-11-13 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eb6b7225-e15e-3c0b-9749-ba0ec8d18828 | -6.49151 | -47.01309 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f342680a-d98b-38c3-b83a-f805d073d2f5 | -7.78248 | -41.89888 | 2025-11-13 04:14:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c6bbcd4-e7bb-389b-a239-1c8c844051c7 | -10.33847 | -48.07103 | 2025-11-13 04:14:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae9c60e1-c43e-36b9-ba87-7e658059b849 | -5.57089 | -47.10585 | 2025-11-13 04:14:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e62a3c94-8824-3810-a5c2-aa5b09a533bb | -8.74566 | -44.23341 | 2025-11-13 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 119ad2dc-67a7-344a-a2ce-3623552d1d04 | -6.28798 | -41.73851 | 2025-11-13 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a147d132-0188-3e4d-b1f5-b53f655181b5 | -7.82025 | -41.78653 | 2025-11-13 04:14:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2b5c20cf-3b8a-387d-80c1-ed9ccfa933e9 | -12.41123 | -45.804 | 2025-11-13 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e76f8c05-4cea-37bf-9a81-a383650cad63 | -11.73653 | -48.5367 | 2025-11-13 04:14:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e012ab0e-cab7-396d-a450-a2f559b07e0c | -11.81533 | -44.2501 | 2025-11-13 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f581c42a-4101-3177-8f6b-3e3738dabf6d | -7.7799 | -43.79842 | 2025-11-13 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 027d41a7-2663-3913-bcb5-34d231c67cd3 | -6.64176 | -42.83337 | 2025-11-13 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fb7977da-7196-308e-8790-ea8c6caccb15 | -10.84812 | -44.94384 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4648ac89-dd19-34f0-8e0d-7055fb6c3fb9 | -7.15506 | -44.97011 | 2025-11-13 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cae843b6-a7e8-3d1f-9b0d-1b5ca30c2066 | -10.44988 | -47.33887 | 2025-11-13 04:14:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5b1e4629-077c-3b2e-a69d-b87fc9ee8c21 | -9.34593 | -46.59507 | 2025-11-13 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 115bbdf4-2bf8-3bda-bd6a-feb540d42fc5 | -6.29467 | -41.73954 | 2025-11-13 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3495911c-c42e-3db7-86a9-4bfabcc35309 | -7.50369 | -38.01281 | 2025-11-13 04:14:00 | NOAA-21 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0e97ee35-f920-37b3-95e9-62092376903e | -7.17071 | -39.36177 | 2025-11-13 04:14:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 94d3a4d5-9502-3db2-93d4-9f8813ac7744 | -7.72408 | -42.37 | 2025-11-13 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f0136d51-1a81-309a-a6c1-f80853fb6648 | -7.25855 | -45.37436 | 2025-11-13 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cde6a8d9-3c58-33c3-9818-a546f53b397e | -5.04012 | -49.9789 | 2025-11-13 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98038ce4-fc7c-3b5a-aa7a-b8899c623212 | -6.88127 | -42.85015 | 2025-11-13 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3953eabf-330c-3abc-9d8e-6548f69f60a0 | -10.92804 | -44.61232 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e89c0ef2-ccfe-3467-806c-8e54e7854e96 | -8.94339 | -49.82089 | 2025-11-13 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9a6605c-e908-3904-9dcb-bcf3c572e213 | -7.37625 | -43.48852 | 2025-11-13 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ede4046-5ea1-3a85-b729-6f38cbe5828a | -7.24286 | -39.36338 | 2025-11-13 04:14:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 27c5a46f-440e-3500-8cec-ec60bd676965 | -10.629 | -45.24593 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbbb63fb-c82d-382e-aff0-ec1c5a8053d1 | -8.86344 | -49.94314 | 2025-11-13 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9aa57ffa-cdb5-3070-afeb-6e510a724556 | -6.52757 | -41.549 | 2025-11-13 04:14:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b0857a08-58da-3235-ba59-b48b5d7ec4f6 | -7.22554 | -47.98112 | 2025-11-13 04:14:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0322fd3-0c49-3b53-822f-d6b008a1c955 | -6.14156 | -48.05348 | 2025-11-13 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c247c60b-0552-3da4-bcf7-262e9dc79eba | -12.43648 | -43.75523 | 2025-11-13 04:14:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4bd517b-7225-399a-b055-d15d04c47f16 | -12.90964 | -44.66975 | 2025-11-13 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 239f5f25-002e-3fb9-953b-776e343091d5 | -7.37103 | -43.34946 | 2025-11-13 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56656ab8-c10e-3826-91fe-a20010824e07 | -7.72741 | -42.37051 | 2025-11-13 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f986a813-2e80-3fa1-8bf7-8038130e1752 | -6.93382 | -39.60384 | 2025-11-13 04:14:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f0242949-91c6-3a48-965a-e9dba4b04807 | -9.32386 | -47.83624 | 2025-11-13 04:14:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5be0d36b-f561-36c4-9bf7-c59e576d19d0 | -7.49536 | -47.33519 | 2025-11-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0eb7b31a-5e37-3317-a679-3d2e9c19c596 | -10.17483 | -44.79021 | 2025-11-13 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a861ade1-0966-35fa-86be-d3899d71ece9 | -10.85203 | -44.94081 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53b12a5e-dbce-32a6-81bd-3a55cac542b0 | -7.81633 | -41.78962 | 2025-11-13 04:14:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6e59e39b-67b1-3796-a5d9-7ea5f75d0e87 | -12.66721 | -46.74517 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| d9156acb-90f5-30d2-8fea-005886b17bec | -7.8241 | -41.76128 | 2025-11-13 04:14:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e5cc8f62-769b-39f1-b789-e24bf7cc114f | -7.47273 | -42.56696 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 400ad3d8-b329-3583-9047-a98ddb222727 | -7.14068 | -40.6011 | 2025-11-13 04:14:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 61b4ea37-8323-3772-8022-d61219fdc418 | -5.60105 | -46.25778 | 2025-11-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c21e376-21b9-36b8-a9ed-54496fa923d6 | -12.53776 | -43.38497 | 2025-11-13 04:14:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0539d614-b004-31e6-a86c-7aa85e8609fb | -7.10531 | -42.37012 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 30968ff0-bbb4-32d5-b6e6-1d40748bcd42 | -5.72939 | -44.83633 | 2025-11-13 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1272e776-275d-34b4-b639-955d86222a04 | -10.85146 | -44.94437 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7352d034-8185-36b1-b5fc-e1cbbbd426a9 | -6.89688 | -42.06806 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1b4e2b7-b0cc-36f5-8e6d-8d8a4e37b91f | -7.08637 | -39.26568 | 2025-11-13 04:14:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 996782e7-125b-3239-81c1-30ee6acfe577 | -7.28025 | -39.35313 | 2025-11-13 04:14:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 00eda0c7-587d-3ffc-8100-f8486c97e9fa | -10.94174 | -48.00104 | 2025-11-13 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27e336bc-fde6-31ad-b0ca-c12f7724ca2a | -10.78172 | -48.14048 | 2025-11-13 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README19.md)
