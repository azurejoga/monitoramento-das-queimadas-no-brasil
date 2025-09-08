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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bc782b7-b4d5-3025-87ca-e8654ae67cbb | -11.33749 | -46.57271 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 884cc15c-0832-3534-8fea-15bc91c9b1b6 | -9.96199 | -51.20599 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5fb3878c-7b2a-3248-9d80-60d4beba7ea3 | -11.89944 | -46.65044 | 2025-09-08 04:02:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61c67295-2686-3ce5-a815-68fe8b117668 | -11.28238 | -46.45176 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| a309d612-d8e3-3711-bf34-951fc87df2d7 | -10.79793 | -47.73249 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34bfb957-d780-37b2-8a4d-f840843b2b59 | -11.15567 | -45.24605 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0186dd5-3d20-3454-b3a5-a426a6b2bdd5 | -7.7381 | -50.30893 | 2025-09-08 04:02:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a92adca7-8604-3deb-b54f-f833887f0cc5 | -14.25964 | -44.94327 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4fdfae1-2f11-3ea6-834b-6b487f1b0e6f | -10.96051 | -46.81995 | 2025-09-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2788634f-5bde-3b4a-b9f3-8c7913c5a91e | -14.78637 | -48.14318 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73df0e4c-acff-31ab-8ed4-a0e8f8000990 | -12.82281 | -52.93987 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c1d995e6-8c26-365c-952c-123b0be54631 | -13.04177 | -47.14272 | 2025-09-08 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad1650f6-cedf-35dd-8851-f9e668ce049d | -11.32402 | -47.40731 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a60e34fb-7f74-3e7a-aa57-18b7292a21f9 | -8.1934 | -50.14034 | 2025-09-08 04:02:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30ae68ba-8af6-3909-81e4-6051ac1e2769 | -16.34038 | -43.03848 | 2025-09-08 04:02:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f77b69b3-090b-3983-be46-630b4911f09b | -9.81816 | -47.77303 | 2025-09-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4fc8ea6-f614-3e91-8f28-f38553cd59b5 | -11.41076 | -43.59735 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9eeacb06-0af4-3515-890c-31a2007fe289 | -9.99047 | -51.67893 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 846797b7-47a1-378a-b043-1ec31b83df73 | -15.18563 | -48.06005 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c7aa36d-eb67-3e6b-8c48-565f58c46717 | -12.8239 | -47.99553 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01c6df1c-f897-3166-aab7-e34e2458bb6b | -9.70212 | -43.51863 | 2025-09-08 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2cab29a-b9a5-3c15-bd89-f6408a5c662e | -10.8232 | -47.74666 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87020fce-b783-3a30-b745-1024fa822fc9 | -9.8434 | -48.85571 | 2025-09-08 04:02:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 946ed011-87f6-3122-a5de-d0afeaad0c3d | -10.24148 | -46.68302 | 2025-09-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63cd7b94-d452-3055-8bd0-7dd9fd2e85ce | -11.65385 | -46.87999 | 2025-09-08 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9c93979-792c-3f00-9da8-caf5f3000072 | -14.58988 | -48.07734 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a04d40f-2043-3a4b-b4e5-eb2c48dc28aa | -13.28651 | -51.74252 | 2025-09-08 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14a6ed71-cce1-3aa4-a3c9-66d675edfb3e | -9.04716 | -50.46416 | 2025-09-08 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcc7116e-c93c-31f8-892d-fdb35d4e88e2 | -12.94792 | -54.80719 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d1222338-5e9e-31fe-849e-da7f5b09933e | -11.39059 | -43.54541 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aafcf362-58d5-3575-a793-975c347a6cb6 | -9.18455 | -46.0703 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f942ae16-2bd7-3bdc-bba0-e5977cfc6129 | -11.85584 | -47.54562 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e011d63-a20c-3de5-8a0a-f4747a0abf41 | -11.18997 | -55.00389 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b83d4836-4d86-329c-8069-1651f05ae9e7 | -13.00457 | -45.2088 | 2025-09-08 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8da92d1e-8949-32fd-b152-2592fcacdf6e | -10.14038 | -46.19616 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96676140-79e2-3e91-8b4e-b601d79f965a | -11.40806 | -50.37888 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8cbe4873-3016-3862-8807-3a3ccb9b3892 | -14.29209 | -44.86201 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffa83cf9-2ea7-393a-95a3-633d2385c7cc | -14.51034 | -48.80793 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae052b0f-3661-3539-9d34-d809d920a736 | -11.20047 | -55.01112 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f6f5b4b0-1aa5-3920-970e-fe64622995c1 | -9.33152 | -46.5227 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd6694c0-68b3-397d-8798-089a02895fec | -11.40416 | -50.39902 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0ca04bb3-e2e2-39ef-bc1c-d3ab7ddace9d | -11.44802 | -49.25066 | 2025-09-08 04:02:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 42e69c10-e9bb-37d1-a2ba-d20dad025869 | -9.72194 | -43.97991 | 2025-09-08 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fd2d62c0-2bec-3fd0-a483-613f70cd1916 | -7.73502 | -50.3106 | 2025-09-08 04:02:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2276e2a0-10ed-3b15-8663-7463b7124c28 | -9.96219 | -51.20073 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2a802e20-8089-3189-8eed-101a91683abe | -13.71648 | -46.90125 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f12db667-9749-399c-a152-2027a3d26aed | -12.00298 | -47.78092 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b6fe9013-8a05-39c6-a544-9d00fa031ff1 | -15.29221 | -43.37854 | 2025-09-08 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f53bcfd1-a447-3941-9bb7-d1f299157e70 | -12.94657 | -54.81357 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 19458138-d815-33e4-b969-0252ce510faf | -13.84655 | -46.23959 | 2025-09-08 04:02:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a43f7238-3178-31aa-8d31-a68a207473c3 | -14.27692 | -44.92896 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 504d4af6-4155-333f-bad2-3d5229e1d086 | -11.83425 | -46.76621 | 2025-09-08 04:02:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fff0205c-56a9-398c-b587-101930fd8c68 | -11.2215 | -55.01563 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e91f88a8-e551-344b-88cc-d459b3443636 | -15.02569 | -45.46203 | 2025-09-08 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db96551a-48d3-3247-87e0-62943966580f | -14.51434 | -48.78136 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64e4eecb-73bb-39c7-9cfa-97108a9d580c | -9.33081 | -46.52671 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a928654-5949-3970-b7ec-92916c6213fe | -11.77573 | -47.56194 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39a01e70-26f3-39c2-9c55-4184bc42e74d | -11.20195 | -55.00417 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0652147e-cdf4-32f3-8e2f-89a08757ab60 | -14.8005 | -48.2356 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65d74d95-2aa6-3703-82e7-02fee8b1e00c | -10.79508 | -47.739 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fe34c40c-648a-356d-92d2-7275959e42b5 | -10.13597 | -46.17311 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c2d3f37-5f6c-3b29-af37-3a2d9a284961 | -15.00235 | -48.01064 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 889fd10d-4bb9-373b-955f-d4562bab91f2 | -9.19519 | -46.03357 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e7d394d-ad9d-3528-abf4-fe27ba24eaee | -14.69348 | -44.78297 | 2025-09-08 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b68b4eb-12bf-3ccd-9dca-84c6576fbf08 | -13.82547 | -46.24546 | 2025-09-08 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c70c198-5d21-3ce7-b371-59c97b56a228 | -14.5159 | -48.77901 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d1c30cf-60d9-3568-8c49-2fd022647360 | -9.8149 | -53.32425 | 2025-09-08 04:02:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3caac85d-932b-311f-a419-fbffa822d4b0 | -13.83321 | -46.24702 | 2025-09-08 04:02:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 317613d9-2cd9-35b0-b219-7d754ae91647 | -11.28516 | -46.45994 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 5b9477c0-da31-31c2-a72b-af7e1f4dea24 | -11.41012 | -43.60128 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97537fdb-e251-34bf-bf3d-974f2e7ec505 | -11.34322 | -45.57869 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 624fbaf8-59e4-3e17-8c89-810a327a6100 | -14.60693 | -48.08148 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35424d23-ad17-3035-92dc-708391079e30 | -11.40075 | -50.39838 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| aee20675-ba7c-3ae7-844c-270fa31e7f79 | -10.70215 | -44.39434 | 2025-09-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f14878b6-c8ee-3a91-82aa-2f719bf37854 | -10.79672 | -47.72973 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e3a73949-6020-3420-935a-b05d5db82c8e | -14.80961 | -48.18636 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89425f9e-9093-3451-9961-a9fd8bc24e01 | -15.71177 | -47.5116 | 2025-09-08 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fca3f3c-4e15-39a1-b0dd-08f0f499f90a | -10.07111 | -48.10136 | 2025-09-08 04:02:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15f4c14e-b6e1-3691-a167-f73627999028 | -14.60599 | -43.92056 | 2025-09-08 04:02:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29067e77-0c98-30c8-bb23-7921b9337f95 | -14.29855 | -44.86745 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d22fab9-8051-3638-b35b-6ae6d036aecb | -15.52353 | -43.8484 | 2025-09-08 04:02:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ebd9a13-4b1d-33a8-b5aa-01bf238b4811 | -14.21745 | -53.35368 | 2025-09-08 04:02:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 811d78ec-597e-3353-a036-79c7c765aeb5 | -9.82357 | -47.76915 | 2025-09-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0954e629-a8d3-376c-b7bf-4538ed14df0b | -11.42556 | -43.64405 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9d42236b-8a99-3ab1-96de-047a8751d476 | -14.51616 | -48.79686 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b561026-5763-3281-88f7-48d24be49924 | -11.40536 | -50.36443 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d667ab8-e7ed-39e8-bb8d-5ead88c797d5 | -12.41132 | -47.50319 | 2025-09-08 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 54407eb2-93c9-3711-9e61-92cb5e769725 | -15.66479 | -48.24484 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87e7908c-882e-34d6-91e2-257da8cbdcf8 | -14.46469 | -48.79671 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b25d9a17-c990-39d1-bcee-5cd3a42039a6 | -13.82935 | -46.2462 | 2025-09-08 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6a97e49-c898-3d42-b1b6-ce16fc672edc | -11.05774 | -47.15118 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d51ff05-80e1-39e1-8420-af515639ab43 | -13.00087 | -45.20813 | 2025-09-08 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95d00ea3-8362-3b18-b225-db6ea3a863ff | -9.19731 | -46.04587 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 505a79d3-8dab-3998-a75b-f708d667eaac | -14.80604 | -48.18149 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10cd8641-d2e7-3f85-98ba-0b4231717f9e | -14.52128 | -48.77533 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4954e2f7-725a-3477-8e85-7ea1e6980b8b | -11.45186 | -49.25741 | 2025-09-08 04:02:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 75729b0a-bab3-3273-8b3d-73b45016244d | -14.60267 | -48.08046 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ac97b32-cdd3-3721-84e9-6287e0f09e4c | -8.74319 | -46.6823 | 2025-09-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f169bfc2-11f1-3216-8e8c-3d08076bf552 | -12.82437 | -52.89909 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 079588ec-41e0-3e7d-81a0-6323a9d152b5 | -11.36724 | -50.34276 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README44.md)
