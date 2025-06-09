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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e68497e-4d8f-337a-8467-e99d20d4f677 | -4.82058 | -44.35393 | 2025-06-09 12:23:00 | TERRA_M-T | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6a29aa87-c22a-37c2-a909-76509bb8b833 | -7.27248 | -44.22169 | 2025-06-09 12:23:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d594ccb5-ba16-3ca1-aa5e-2ca6fe2646f8 | -5.46071 | -42.92632 | 2025-06-09 12:23:00 | TERRA_M-T | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 2bbed804-9960-32a5-b46e-048d141250b3 | -9.19193 | -38.81007 | 2025-06-09 12:23:00 | TERRA_M-T | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 749bf1aa-7d4b-3c8a-8eb0-2d24b81558dd | -7.01461 | -44.60883 | 2025-06-09 12:23:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 1ffd32ea-31ee-3130-a7d5-f160de0eacba | -7.01325 | -44.61853 | 2025-06-09 12:23:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| f1529e83-f8d2-3eb8-83f6-d2eee9a79775 | -6.8872 | -47.23909 | 2025-06-09 12:23:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 76a55004-d30d-302c-9b13-fbb0fa2d1b3e | -7.01598 | -44.59913 | 2025-06-09 12:23:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7e1634cb-9c4e-38c0-9972-53f42f019301 | -6.62138 | -49.72052 | 2025-06-09 12:23:00 | TERRA_M-T | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| a02b3dd0-844d-3402-804b-bf8446cdf087 | -7.66635 | -45.213 | 2025-06-09 12:23:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7f2670f4-7235-33fd-9c77-06bdbabf4247 | -6.69069 | -44.15667 | 2025-06-09 12:23:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e0e113dd-efaa-3381-8aea-840e68cc08b3 | -6.63146 | -49.722 | 2025-06-09 12:23:00 | TERRA_M-T | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 8b1140d4-3725-3bbc-af9e-5da34f21f3d0 | -9.07837 | -47.14561 | 2025-06-09 12:23:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 24a4beed-d436-380b-aeb7-616af5d07cff | -8.27146 | -49.30258 | 2025-06-09 12:23:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b35641b5-fa8e-34a2-86a8-08c7b5219d9d | -6.87161 | -44.83687 | 2025-06-09 12:23:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2bd16d64-d83c-3a36-a10c-b13dd1cd8457 | -7.27834 | -44.21854 | 2025-06-09 12:23:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b5cd6a34-7df9-37de-9eb6-77ff8f5dee8a | -13.64551 | -45.41901 | 2025-06-09 12:25:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 77a96a9d-e194-342c-b716-aef84d3b2e2d | -11.16249 | -45.76638 | 2025-06-09 12:25:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c70ebe00-f015-3887-bad1-274c133cfb12 | -11.83483 | -43.80123 | 2025-06-09 12:25:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 83fe3037-2688-3788-bb1a-403531a8f39d | -9.84507 | -48.14177 | 2025-06-09 12:25:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a94ce6a2-5463-3209-99c5-4bd75a60b1a2 | -11.8364 | -43.78883 | 2025-06-09 12:25:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 99be4a47-0172-35e5-ab24-487ceb9b4989 | -10.31446 | -47.01242 | 2025-06-09 12:25:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 6251cdc6-d7f2-3a07-b707-a7816f8826b5 | -11.16117 | -45.77594 | 2025-06-09 12:25:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 53d60213-43b0-36bc-935b-8efebf194655 | -11.15205 | -45.77467 | 2025-06-09 12:25:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6ed7f17d-d2c5-3688-aeaf-201c98c5b97b | -10.73201 | -48.82074 | 2025-06-09 12:25:00 | TERRA_M-T | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9961ca30-eb6c-3492-aef4-0155afa68768 | -10.85617 | -44.78817 | 2025-06-09 12:25:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ac032d9b-482d-362a-ac00-ad076455b079 | -12.87319 | -47.03836 | 2025-06-09 12:25:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3f5815be-0a24-3291-9d28-931de434b4d9 | -13.06863 | -49.23893 | 2025-06-09 12:25:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 056fa232-f6fd-34ff-a29c-69fb5770658d | -10.85655 | -53.77102 | 2025-06-09 12:25:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 5e692ffa-f7ff-30d0-a020-83be55202092 | -11.83965 | -43.7833 | 2025-06-09 12:25:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 66770a55-0279-3a8d-9363-0644e5a1b65b | -13.72694 | -45.2453 | 2025-06-09 12:25:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b633ef87-dc04-3bd2-82ad-b5a5cfaa5e46 | -11.58077 | -44.87063 | 2025-06-09 12:25:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1e6c73ba-dbcd-3ece-9a8f-953a2a5ec1f6 | -10.65243 | -44.40466 | 2025-06-09 12:25:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 157b10cc-127c-3154-919c-b2549cde685f | -11.83799 | -43.79568 | 2025-06-09 12:25:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 276b933b-adae-3185-894f-1f8137fd974b | -13.65502 | -45.42031 | 2025-06-09 12:25:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6081aa48-f532-30c6-a244-acbe8c96d6a9 | -13.73512 | -45.25727 | 2025-06-09 12:25:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ef5c6785-b827-381a-bbd9-2bb66df6ce14 | -13.6565 | -43.41665 | 2025-06-09 12:25:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8d2b93ca-eec8-339a-8f82-84211600c50c | -9.40567 | -48.43311 | 2025-06-09 12:25:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| be0859a4-1a8d-3c54-acc3-c0586ecfde15 | -12.10867 | -49.48748 | 2025-06-09 12:25:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c3504bea-6705-344b-85c0-0115b4dbb1fd | -9.40427 | -48.44256 | 2025-06-09 12:25:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2c095c59-9325-3bd7-8fa9-45fd51129d50 | -10.87502 | -54.29581 | 2025-06-09 12:25:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 9b6d6563-e5da-3b74-9a8f-22e514fe3ce7 | -12.54067 | -41.08776 | 2025-06-09 12:25:00 | TERRA_M-T | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| abf261f9-b0d2-3c6c-9dd4-2088ef34f5c9 | -9.41337 | -48.44388 | 2025-06-09 12:25:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2b843f3f-c0db-3c2b-9c64-aa7b7f67060a | -11.57933 | -44.88123 | 2025-06-09 12:25:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9df13cc9-6d54-3511-b0fa-7a1c488a0465 | -13.07006 | -49.22936 | 2025-06-09 12:25:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d9d4c675-d3f4-3a9e-ab03-cd7b75081047 | -13.7255 | -45.25606 | 2025-06-09 12:25:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 70051142-d617-3474-b039-962415685b6c | -11.57013 | -47.44464 | 2025-06-09 12:25:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| dade65f7-f456-3fa8-b04d-edfa63cb4515 | -10.31318 | -47.02134 | 2025-06-09 12:25:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 2f22f957-04ba-31cf-82fe-ba0f57d36c7a | -13.28039 | -39.86852 | 2025-06-09 12:25:00 | TERRA_M-T | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 7b17a7bd-5477-30b6-9d8f-26b15b3d933d | -11.57142 | -47.43568 | 2025-06-09 12:25:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| be4d9f5b-8107-367a-ab41-96ef433d0620 | -12.11016 | -49.47755 | 2025-06-09 12:25:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 685fdc37-611c-38c6-8339-988290954c3d | -10.27924 | -46.99226 | 2025-06-09 12:25:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8c0b13d5-c10a-331f-93e4-447de0c33030 | -9.84373 | -48.15095 | 2025-06-09 12:25:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bc6a5b95-9bad-3269-9525-92e3c3352f97 | -15.09027 | -44.81204 | 2025-06-09 12:27:00 | TERRA_M-T | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| da57506c-8f92-3d53-9406-7a5f664e076c | -13.51084 | -47.86491 | 2025-06-09 12:27:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e28dc55-1b51-3dd5-b8b2-bdfd3f78c2bd | -14.20685 | -45.48978 | 2025-06-09 12:27:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a72bc7d5-b951-323a-851c-064375d62429 | -14.24499 | -45.49504 | 2025-06-09 12:27:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| bcf74424-4e78-34fd-b851-f76ed1d09dd2 | -14.24641 | -45.48439 | 2025-06-09 12:27:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| f9735f69-a9e6-31f2-8c9e-ed4945ede91f | -13.51214 | -47.85588 | 2025-06-09 12:27:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 53ae0898-ec9a-3d12-96d3-69bcd4a71d5d | -14.20825 | -45.47916 | 2025-06-09 12:27:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d70021cc-5fb5-3945-930f-ba559838b950 | -15.94318 | -47.40488 | 2025-06-09 12:27:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7244d55-5855-3aa4-aa58-dce3dcfe5980 | -16.35411 | -43.61834 | 2025-06-09 12:27:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 47e60060-6046-3c6c-b356-5461d95a7dcd | -14.23687 | -45.48311 | 2025-06-09 12:27:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 733c8b2f-793c-3b25-9127-68bae3540568 | -16.37832 | -45.09953 | 2025-06-09 12:27:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 55eade0e-0485-3ed6-8385-8c03fe905783 | -13.06508 | -52.04068 | 2025-06-09 12:27:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b58d9886-a6e2-370b-860d-bdc5ad13153d | -16.35238 | -43.62713 | 2025-06-09 12:27:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ebbc927f-eba7-3fba-9acf-feb9c1e2362f | -15.36937 | -51.099 | 2025-06-09 12:27:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| eef5fd54-0aa9-34fb-aae4-e91a682bc4b4 | -14.21638 | -45.4911 | 2025-06-09 12:27:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 280.1 |
| 5f9a604f-995f-3dd8-be4e-f26c45f20055 | -16.35426 | -43.61205 | 2025-06-09 12:27:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| fa71921d-6b40-39ce-a640-9c119cd9b285 | -14.23545 | -45.49373 | 2025-06-09 12:27:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 13730cc3-12ac-3ea2-a55a-7ca0a6bd8ca1 | -14.03543 | -55.12518 | 2025-06-09 12:27:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ec0d8fad-fbc0-311b-aa0d-c8bf8ca2ba2a | -14.21779 | -45.48049 | 2025-06-09 12:27:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.7 |
| bac085e0-1506-3883-9c83-1ed94217dce1 | -13.66123 | -47.77358 | 2025-06-09 12:27:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 56706b2b-c34c-3b4c-a67a-6f99343d1410 | -14.21498 | -45.50172 | 2025-06-09 12:27:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ab1465b7-21c8-3b0a-a755-c1e70cda586a | -14.2057 | -45.4838 | 2025-06-09 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| f0731ce8-ac40-35e2-8451-1544f51c3dde | -14.2442 | -45.5002 | 2025-06-09 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| ffd76137-0a50-339b-9638-7b81fe2d67bf | -14.2247 | -45.5036 | 2025-06-09 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 47777706-4575-3a56-adf8-5da3f56eb68b | -14.2447 | -45.4769 | 2025-06-09 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 22c77768-5667-310c-bca3-c94fbf0d4373 | -14.2252 | -45.4804 | 2025-06-09 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 324.2 |
| 04747576-d1c2-3470-adac-2be5ae2579fc | -11.5775 | -44.8645 | 2025-06-09 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 8bb18a13-0e06-3813-b418-f6eec334f459 | -14.2447 | -45.4769 | 2025-06-09 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| cc9292a2-20ca-363f-860a-01889d756fe0 | -14.2052 | -45.507 | 2025-06-09 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| dc6dc592-0805-3da6-9f51-16b3c4a698f7 | -14.2442 | -45.5002 | 2025-06-09 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 86b5d690-71a9-3652-9df2-914b62d2af85 | -14.2247 | -45.5036 | 2025-06-09 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 55ee230f-ba45-390f-bec7-bd1c1966449f | -14.2252 | -45.4804 | 2025-06-09 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 299.0 |
| c91f6576-9b58-36b8-b24e-8d297ae5c8e1 | -14.2057 | -45.4838 | 2025-06-09 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 5ad80a68-0e1f-3431-b802-649f2548e73c | -11.5771 | -44.8877 | 2025-06-09 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 8f4441df-0995-38ba-a401-221088737492 | -14.2447 | -45.4769 | 2025-06-09 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| d3e78452-a730-36fc-be24-164cddddfa58 | -11.5775 | -44.8645 | 2025-06-09 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 4e4b3b67-5db8-3fd0-98da-054b0012ffda | -14.2247 | -45.5036 | 2025-06-09 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 121a58c4-9354-31a3-b84d-61dd5d20f251 | -14.2057 | -45.4838 | 2025-06-09 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 207.8 |
| e6667f2c-cc51-3d68-b559-8b6dcdf398d7 | -14.2442 | -45.5002 | 2025-06-09 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| e351175c-e79f-3671-8b8b-30f2fec15067 | -14.2052 | -45.507 | 2025-06-09 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| b52f3a5b-16a2-3706-9b37-8f34ee3a57ab | -14.2252 | -45.4804 | 2025-06-09 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 505f89a1-0786-3d6b-b67c-9da7ff09feff | -14.2057 | -45.4838 | 2025-06-09 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 12de3994-fb22-3f38-b5a4-ef4c9080db37 | -14.2052 | -45.507 | 2025-06-09 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 0b848baa-11d9-348d-818e-42df9c306a1f | -14.2447 | -45.4769 | 2025-06-09 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 6d5eb3c6-dcd7-3291-a65b-28c1753af364 | -14.2247 | -45.5036 | 2025-06-09 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| d084760f-3c7d-3228-b7f8-4836ef4e68bb | -11.5771 | -44.8877 | 2025-06-09 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| aa41f42f-99ea-3be6-9a89-d149dbe60731 | -14.2252 | -45.4804 | 2025-06-09 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 209.1 |


[Clique aqui para ver as próximas entradas](README10.md)
