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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97c0907a-d1fe-36e4-af38-31592f6ef5cc | -11.86419 | -48.03192 | 2026-10-07 16:01:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| da25c864-e276-3d30-9e55-d8eb5da2b083 | -9.93424 | -46.80392 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ef940848-12a3-3a26-a91e-2769ef7e7119 | -11.14594 | -46.15627 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9f960465-a079-34e8-b70d-7773ebd04523 | -11.094 | -47.62716 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 3d4c3dc8-533e-3db9-ab8b-caf87821f1a4 | -11.72446 | -43.66259 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d1a537da-187b-3907-86e8-06052913cc19 | -11.63774 | -43.68026 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 210.4 |
| 08d3dee1-2a91-394f-8dd4-c90fda529b79 | -8.73116 | -47.07049 | 2026-10-07 16:01:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ac2ede93-c71b-3c0c-8cfb-b0df30dcef2f | -11.15922 | -46.17607 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b45ea06c-f00e-35ec-8bef-b46b6b1f1a3a | -11.84597 | -43.55939 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 944d75b3-e2c8-35cc-9611-705518d035cb | -12.22127 | -44.73655 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 22aa8795-783d-3ff5-936c-ddf9e63c30ff | -11.85866 | -48.03716 | 2026-10-07 16:01:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| f5d74e88-db22-3c5e-9402-7c5cacb68d57 | -11.38056 | -46.6962 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9a54579c-ff50-323f-a3a3-a3a9ddf1e9b6 | -8.79209 | -36.90154 | 2026-10-07 16:01:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 717403a9-8cb8-3b95-822f-387b95c4fe8a | -11.62488 | -43.61828 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 61782481-fc0e-318d-a0b4-b3229c157f40 | -11.84971 | -44.73692 | 2026-10-07 16:01:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2412811b-9404-3c3e-931e-83680f39fc7a | -11.32885 | -42.0162 | 2026-10-07 16:01:00 | NOAA-21 | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8cc35826-85ff-3ba9-9c9c-4bf54c71e5d8 | -8.83423 | -45.81356 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9ce799fd-96b4-32ca-8fc3-d6b07f4f7935 | -12.18338 | -44.75214 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 308.2 |
| 9928328e-7b93-35d3-b83d-be7b9d6f6cf6 | -9.87343 | -44.80619 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b3866fff-9f6b-3a1f-88c3-e065b3f44dad | -14.08209 | -43.76477 | 2026-10-07 16:01:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| b4847943-9bd3-3ff4-9219-518e18e839e7 | -8.80139 | -47.21952 | 2026-10-07 16:01:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b46854d0-9e61-33cf-9797-87d20247db1a | -11.73621 | -43.64713 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 9619e262-e481-3866-84e5-a85054d46bb2 | -11.36629 | -46.71517 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4b6d85fd-1499-3ca7-ad61-7bb44eca246f | -9.64668 | -46.09638 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| eebb4d1c-8fe6-3b04-9de3-cc6a79645cfe | -9.03754 | -46.87679 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9b1267e8-29f2-30bc-affa-9bf4b6f28af2 | -11.27862 | -45.22141 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 2caa2c27-2c1f-3322-82fc-6d44bfd35831 | -12.18901 | -44.75715 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| e94a9cba-8be8-376a-b140-83d9a9b92d21 | -13.69341 | -42.13533 | 2026-10-07 16:01:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| f402b311-8365-351d-9ca3-8bd4db11fb9e | -12.44318 | -42.097 | 2026-10-07 16:01:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 13b56589-7ee7-3dec-a758-4bef937ad927 | -11.62303 | -43.6734 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 6b196031-3b6b-368b-bf52-d3e3a5727ef2 | -12.8213 | -44.67177 | 2026-10-07 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| cbd49713-914c-3ef9-9c38-bc942de437eb | -10.94275 | -45.38665 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 76019681-cb1c-3b9a-a6ca-a8217657732b | -9.15588 | -45.81547 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e6bca490-d961-36f5-ab3d-b4848019a634 | -12.26884 | -47.17476 | 2026-10-07 16:01:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c0648c2-fbd7-3df6-a509-5a777892ae3d | -8.59232 | -45.68119 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 900f78df-fe1c-3627-93e8-20339171cff0 | -11.87421 | -44.77305 | 2026-10-07 16:01:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 52ec881c-a263-3192-822f-193ed0825949 | -11.86931 | -44.77366 | 2026-10-07 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 326f7ce7-b682-37d0-ba3f-d1ef384cc3a2 | -9.87304 | -44.80784 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6da4dbe1-3fcf-32bc-98b7-30f3740cfb6b | -7.52867 | -35.1057 | 2026-10-07 16:01:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 624f7b34-94b7-36bd-afd6-53fc75018ca2 | -9.93405 | -45.91458 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 80acd1c1-9309-3eb5-8a5b-76443b54cb9b | -13.44577 | -43.45633 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 455bd6e1-923f-3f75-967c-0f4cf5cbb089 | -11.44135 | -45.57336 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| cba222c6-8a03-30a2-8363-d5cc28a1274b | -9.13131 | -45.10186 | 2026-10-07 16:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 239.7 |
| 2b6a04af-7cd5-3660-9153-5ed28a574d72 | -8.98925 | -45.94354 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 71a268f5-a4ab-3b42-97ef-e6fb9ae9d554 | -7.98552 | -35.28769 | 2026-10-07 16:01:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 430b4542-8677-3dfa-a67f-98a2e8f09e6b | -12.14014 | -43.31152 | 2026-10-07 16:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 4e1aa749-d8d9-3acf-8b1d-4e9c97f67687 | -9.92144 | -46.79961 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ade43606-9460-3cd6-9844-2efe62ff889d | -9.9369 | -45.73523 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 76570f5b-9d6e-36cc-b456-8b9f130fb8e6 | -10.85147 | -42.80984 | 2026-10-07 16:01:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bd69f342-12fa-3309-936b-b7b28f5a653e | -11.8581 | -48.03251 | 2026-10-07 16:01:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ef730fba-f458-3ba4-b128-af1ea8fdae61 | -9.81263 | -38.40953 | 2026-10-07 16:01:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| afe09ae7-aad4-3410-b292-d0f59e72125e | -9.86593 | -46.30452 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aedf13db-ddfd-3d5d-8af4-431d8f82289b | -8.94523 | -37.61535 | 2026-10-07 16:01:00 | NOAA-21 | MANARI | PERNAMBUCO | Brasil | 2609154 | 26 | 33 | nan | nan | nan | Caatinga | 23.5 |
| b3486a9d-f925-38eb-bcf2-9ce04649a812 | -8.99898 | -45.93891 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 3813fb02-2423-33fc-9550-baad125dea8e | -12.22076 | -44.71278 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 3b8f88fd-d4cd-3b19-b303-d2a43cd35927 | -8.99474 | -45.94594 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c5ae006f-a5cd-3638-a560-5c1369e404ab | -10.98108 | -45.40593 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c1c71124-4007-30d5-99c4-4624d01fd68b | -10.68391 | -41.2141 | 2026-10-07 16:01:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 69906f9d-a266-37ed-a53c-7be086d9dee7 | -8.33276 | -36.41816 | 2026-10-07 16:01:00 | NOAA-21 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 92209037-74c3-3705-9892-8840b1095d7f | -9.91084 | -44.7956 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 7212a62b-22ef-3e4c-948a-d5ebb64ae65c | -12.99447 | -47.06728 | 2026-10-07 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ee814c3b-e117-3557-86a5-355090643286 | -10.88869 | -46.66505 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 48f0ea65-81eb-3140-8ac7-e3832de400df | -9.4528 | -44.61922 | 2026-10-07 16:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b2c90163-edca-3ce7-843a-d5f914d83fe3 | -11.05518 | -45.81863 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 062330b3-ac82-3c6d-b11a-d07ba6bb110a | -13.30021 | -47.26332 | 2026-10-07 16:01:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 858ee004-0771-3b6e-8643-fed4f7dfe59f | -11.12109 | -45.95601 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| d71611fb-8348-3e23-81fb-ccad6dca6e72 | -13.39501 | -43.8769 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4f0f120a-20af-373c-a437-2cdbd99ff872 | -10.99841 | -45.42094 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1b8b0990-c477-3410-9b06-70508857412e | -12.22255 | -42.05977 | 2026-10-07 16:01:00 | NOAA-21 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 23.6 |
| fd242b25-8e5d-3859-a725-f6a3a00b038b | -11.84578 | -43.54118 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3f3f49f6-069b-3001-bcca-e24e307511f5 | -10.99511 | -45.47476 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4045c813-2c8f-37f8-a3e0-3013291e5701 | -12.2969 | -45.29652 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e0b0df6d-9fcf-3817-8470-ebaccc0e705a | -9.95538 | -43.55075 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 224.1 |
| a09da200-8c8e-30ef-bcf8-583a4938843d | -10.98725 | -45.41397 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 24c8ba17-98d8-38a4-9cba-38db7fa03a88 | -9.96701 | -43.57082 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 4b7725ae-09e2-38e2-898e-f1de88a53553 | -8.9769 | -36.82109 | 2026-10-07 16:01:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 96e3eb44-edc4-31bc-9cd7-7795eaa61907 | -11.85972 | -48.03254 | 2026-10-07 16:01:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| d7da284c-7248-3ad5-ba80-05b5fa299b52 | -11.84816 | -43.55997 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1a5d5887-c4b7-385e-81d5-8162cd9fecaf | -12.84235 | -44.62273 | 2026-10-07 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2e9e9cad-7f1a-3375-a2b6-2b4c50512680 | -9.81545 | -38.40549 | 2026-10-07 16:01:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d85a0afe-cf11-31ef-9ea8-fa66de12a5f0 | -11.2309 | -45.2871 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 1dccad46-88e0-38d0-89f0-a17a43fddfe6 | -10.64271 | -48.71524 | 2026-10-07 16:01:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| caf2a189-e50a-3f8a-b47e-c2c5a392b61e | -10.77884 | -47.17894 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 506abd67-36fc-346d-83ec-929b0332b0ca | -11.63658 | -43.60298 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 40f73437-5431-3800-af62-eb8308d19fac | -11.23625 | -45.24832 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 279ff748-981d-3783-aef2-e9a07dba466b | -11.23054 | -45.28423 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| e2b2a4d2-418b-3ae4-a1bb-a34f7c9f4dfb | -11.06161 | -45.77451 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 245a6c5a-3b37-3a6f-9122-d6744f5d751b | -9.90605 | -44.79609 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 3b23352a-8ae2-3fb2-ac04-8c4386362edb | -12.8441 | -45.58711 | 2026-10-07 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4736ca13-e7d1-3ed5-8703-1a7586aa0dd4 | -13.89251 | -49.12482 | 2026-10-07 16:01:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6a99914b-62bb-31bf-bfe6-d201bd8d9c7d | -9.40064 | -45.8119 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d47daa01-0146-39aa-a0d4-7fd80cde3641 | -11.62358 | -43.67755 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 62e79023-1cc8-3671-b5d7-372fab1cd708 | -11.6228 | -43.63712 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 6cca2f6d-e6be-38ac-b750-3dfd3d8061e6 | -11.2286 | -44.87265 | 2026-10-07 16:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 735509ee-a325-3f17-b015-a4c6eb7c3f1c | -12.22254 | -44.70806 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 234.7 |
| 183477b7-eb30-317f-a239-4c59990154c4 | -11.23691 | -44.86019 | 2026-10-07 16:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c2bf249d-8dd7-3b19-b6e7-16db7269ac09 | -9.9373 | -45.73823 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| df24bb69-c798-3dfc-afd5-55405c3825aa | -9.95157 | -43.55558 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 224.1 |
| adc6cc1e-01a3-3b10-832d-01671a06a89c | -11.6168 | -43.6611 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2af9f089-3397-30eb-a4c3-26a668606a39 | -9.82069 | -46.24218 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README155.md)
