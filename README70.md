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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d13e920c-90d1-3107-b3c4-35a9dfa6475a | -12.96048 | -54.78756 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 653c1434-fd2e-3c07-8463-8db8a7bc3484 | -17.96466 | -44.41375 | 2025-09-06 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38b19cf6-b119-3880-b125-00e271e4212a | -11.16379 | -59.15415 | 2025-09-06 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf180b20-257b-3733-b66f-baa60950fcd3 | -15.23222 | -52.36839 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1709aa4-8bcf-32c6-92fd-e88973bd06b0 | -12.61788 | -56.9891 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 237102f2-179e-3250-aeee-60b9b45fb645 | -14.54449 | -53.13477 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ad0d1b9-fb66-3d64-8bda-064ac462d74f | -12.9736 | -54.8301 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eea32f99-27e1-3450-b361-c76d533435a9 | -13.566 | -48.12104 | 2025-09-06 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aeeed0f5-a585-3793-a584-677de2259405 | -14.34409 | -60.32382 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ee8b80b-e2f1-35f7-ac89-edcfa8743a7b | -15.84642 | -52.29078 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| becd94ec-8d3f-319c-86c8-ac43b8506f5e | -12.48793 | -53.85936 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61712497-9517-36c5-9e50-e3b9176bce71 | -12.9606 | -54.79469 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9471e1fb-4619-37e4-8463-45991ee25fba | -10.23086 | -50.54583 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e01fd92-83d0-3f8c-894c-792fc14d8218 | -13.01097 | -48.7257 | 2025-09-06 04:40:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 914ef0df-3855-3591-98ec-eb61f15e38de | -9.97453 | -51.64111 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 41b885fd-302a-3e5d-9a6b-95eb9595f59d | -13.0209 | -46.65612 | 2025-09-06 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44152414-316d-3e17-bba0-270679e56766 | -15.13294 | -52.35159 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9684a0f0-e674-3b91-a866-5ac76c95b90c | -12.48008 | -53.86228 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb716d46-f5ad-38ad-bb06-a62fb6d98dcb | -10.47632 | -53.63963 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9a4449d-e36a-3772-8c07-60abd1456259 | -12.99777 | -54.8015 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 439b837a-b91d-3b79-852b-93716903af15 | -11.62998 | -52.22693 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 465f4755-876c-3bcd-a786-62b19d0bad60 | -12.88169 | -56.95152 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d783ef49-8022-3d9d-87c3-b372541a0e2e | -13.18718 | -44.48379 | 2025-09-06 04:40:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 931a8121-dcbb-3629-9f12-5628ef58690b | -12.01337 | -47.78291 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dccf7c5c-2687-3d4a-b078-a60cdcb3fbaf | -14.84281 | -48.1957 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15820c4a-4e42-389d-9897-8eb1a7e56e86 | -10.79162 | -47.74045 | 2025-09-06 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4091a01a-26ca-36ac-9434-ff58df5ab10d | -14.57129 | -48.09101 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f789bae-9727-39a7-8c75-69478aca7557 | -12.93044 | -48.02498 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03493e72-83bc-3910-bcc5-ed23c8dba872 | -13.74021 | -46.91578 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06bf10ce-ffa6-3780-827e-45026e5eb4a9 | -9.98914 | -51.63619 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d32a5df-ce78-359f-936e-bdd14af2177d | -10.76683 | -48.27321 | 2025-09-06 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14f5979e-bd72-3c1b-863f-a6a2a6bf58d3 | -14.56968 | -49.12687 | 2025-09-06 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f11decfc-a00a-3fca-8055-ce084e2ccbb9 | -14.54047 | -53.13795 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33acfe2f-0d19-3f03-9301-98c103819f6a | -11.00658 | -45.91649 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a119b03-57ba-358f-b16a-e942b2740bde | -15.21527 | -52.35062 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e8a8a4f8-e047-3c1a-98c2-0d1c172b1994 | -11.10644 | -52.01646 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d857c068-83ae-31e1-a022-8766e1e37429 | -16.33205 | -52.96051 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0dd9bfca-67df-3f52-bd23-2a47cb067d08 | -11.10585 | -52.02011 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f97c8d16-4dd0-323e-a53d-3e3d70cae032 | -13.05681 | -47.10664 | 2025-09-06 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 966e26a4-97ab-3078-b5e4-6168656a0c45 | -15.54673 | -49.82208 | 2025-09-06 04:40:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a813401d-b270-3070-8fd1-b00b86783263 | -15.58477 | -52.91599 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f082db64-7574-3193-ac32-9daac2e25a85 | -11.64381 | -54.53996 | 2025-09-06 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 79529087-124a-3015-9793-fa29e9d08b0d | -10.47194 | -53.6215 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3250375-d541-3803-b8cb-c2ddf963ac28 | -9.70755 | -49.48657 | 2025-09-06 04:40:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 356ac3b0-6827-37fb-aac5-b5e3f6ccb268 | -13.27267 | -51.79301 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff7e1ce0-b5c4-3e78-9283-e9bddfa63f6b | -11.68179 | -52.17108 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0eb43f6f-7a01-31ab-8a73-7c062f5a2f62 | -12.96483 | -54.80717 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a35ca775-aed4-3541-9e4f-e85605e8f461 | -10.14808 | -46.23335 | 2025-09-06 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1998ba7e-78bd-3d79-a408-717bc80c0b3b | -15.57471 | -52.91412 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db2191a4-fd54-3be5-99df-5d71d238e16e | -14.5893 | -48.09442 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be7d43cf-1d8c-39c6-9d44-610762c24f11 | -16.96505 | -49.30745 | 2025-09-06 04:40:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 010529d2-0748-32fd-9058-eae5b6b73022 | -13.50686 | -50.80977 | 2025-09-06 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a7918d6-5b72-39b6-b15b-5631fbbf64b7 | -12.48509 | -53.876 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5704d609-a5d6-3390-9980-0bcbbeecf9de | -16.31642 | -52.93939 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f260c918-182e-3804-8947-e6045d43cd54 | -10.77029 | -48.27375 | 2025-09-06 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c91f11e2-3270-36f2-aa73-aee9825d97d5 | -12.95289 | -54.80976 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 754cee8e-aa68-395e-a8ec-fd261f7cc124 | -14.93814 | -55.90067 | 2025-09-06 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7775cc5-d627-3124-bcc9-8729fc204603 | -10.94917 | -44.8325 | 2025-09-06 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94eb1730-1f7a-3b49-93e2-10c51ee0d8bb | -12.51501 | -53.85126 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e1a6dcc-82c7-3cee-a4ea-86d4f69d9ff7 | -16.90325 | -45.74627 | 2025-09-06 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d802750-73c0-307d-92a0-38878131a96f | -11.64401 | -47.15205 | 2025-09-06 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6c48748-fe88-3c06-9e29-7ceac81535b3 | -14.57314 | -49.12738 | 2025-09-06 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cd890b3-894e-3bae-956c-28371b1ec4b0 | -13.26039 | -51.80559 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f7b4743-d90b-34cb-a8f4-088af29b5319 | -12.50432 | -53.84938 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cdfecc5-c3da-38a2-81bd-7a7e3a36769d | -12.01757 | -47.77931 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 465ba92b-e3ee-30cc-b42d-d2d8f2c14e85 | -15.57074 | -52.91721 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bca5f714-eabc-39c6-9355-f6dd7bd8dd43 | -11.21779 | -55.02705 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1633b7b9-7b1a-35f6-8827-0977e8363a6c | -15.35567 | -46.4057 | 2025-09-06 04:40:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fef45085-1513-3474-8932-56cda21c1581 | -11.93459 | -46.66818 | 2025-09-06 04:40:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bb12102-72ea-3bc4-bb51-65f5267cfd9b | -12.62216 | -56.98988 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbf07e3a-faaf-38b6-a0ce-0828a77cd554 | -11.60673 | -52.17769 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4cdc124-c144-3d9e-a36e-a10e60ea2c63 | -9.67964 | -51.08336 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d5ef29b-b5c4-3600-8042-357860085137 | -12.92686 | -48.02453 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3436347-e0f2-3c44-8496-93ce577a453d | -10.97937 | -46.81693 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dc5409e-9080-374c-9882-aecb3e3b2332 | -9.69127 | -51.09612 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c9f8d05-5a74-373c-b71b-1282ef3c306e | -15.58752 | -52.92029 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 406154c2-e0a1-3753-8ef8-8d983e5011e6 | -12.96483 | -54.81434 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4316bf77-6c7a-33e2-bb71-e261c31bf28d | -15.72291 | -53.58535 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8f63d52c-6bc5-31d1-8419-e125b35546c8 | -17.00279 | -49.37428 | 2025-09-06 04:40:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84c9181f-7967-3f74-b3bc-dfa5bc8904d1 | -11.36336 | -43.52128 | 2025-09-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| addb6b48-1a9d-3128-b366-c947203c761e | -12.47863 | -53.84924 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b25d7c6c-7d2f-31db-b7ec-5c26ccdebef3 | -15.84975 | -52.29134 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4086bf71-b997-34b1-88e1-556ffe4e775c | -11.63337 | -52.2275 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42ea827b-8ebd-3c0b-a82d-91349370c06a | -15.20745 | -52.35669 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 71a89ab3-9b1c-3ea6-8be5-ed9243e5046b | -11.21306 | -55.0313 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d28529f-c889-3720-844c-7c972154246a | -13.36149 | -46.83298 | 2025-09-06 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bf4fda0-b52a-3843-b60a-46b09839aa49 | -9.97616 | -51.65243 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d46d635-595f-3318-b261-6071bade7df7 | -11.68457 | -52.17533 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77f925da-f8b1-3c15-be07-0e2f843ac68b | -12.18398 | -53.90075 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f305387f-4dbf-358d-a06f-d23122ec0626 | -10.60828 | -44.33585 | 2025-09-06 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 6379ed6b-f681-3171-9ff4-d9dd03a35f34 | -12.63647 | -56.98407 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31e2116a-e35a-3dfb-9602-01ed159aa5d6 | -14.8368 | -48.18623 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3feea8f-b115-37cf-8bde-faaff49da639 | -12.97973 | -54.81699 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b74cee99-d0a8-3505-aa1e-df818e483ba6 | -13.00636 | -54.84063 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5295f91-66a0-3505-be3f-4bda28655885 | -11.61666 | -52.20202 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f45ab5a-2dcc-3d6c-ad04-a6a0c5d12e54 | -12.49295 | -53.87305 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e95c8ee8-aa3b-3f29-9d80-3d154b50c8a6 | -12.95444 | -54.80059 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58901905-3f5b-343f-80f6-6b5145251e8d | -11.81924 | -51.42893 | 2025-09-06 04:40:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da8cd66f-ac84-366c-9bf1-a9727ab17f7f | -12.95658 | -54.81758 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b7c7015-2735-37b2-92b2-5ce4c1b06903 | -16.9199 | -45.75269 | 2025-09-06 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README71.md)
