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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 637252a7-9a89-3fc9-952a-2e7ab742f3f4 | -10.85243 | -53.73723 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6820deca-4c28-3110-9fbe-07ea73ec3772 | -9.23917 | -58.74372 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91e87e84-587b-3881-a122-4b3094b4feb2 | -12.19584 | -49.63577 | 2025-06-30 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 804e1220-f2a9-3d93-b724-dc306202367b | -12.10409 | -54.58186 | 2025-06-30 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eb4c7ea-7c9e-3a67-8c83-dad944fcaa8e | -12.62598 | -54.21972 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 22ae97cd-aeaf-3b4c-947f-39a0ce18ac52 | -11.02712 | -56.27195 | 2025-06-30 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69f8abbb-baa8-30a9-8f9f-06d27e8c891b | -10.34816 | -57.50368 | 2025-06-30 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e0f1bd2-bd67-3e7e-99ea-b94eb238b968 | -10.79535 | -44.24268 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c57060f3-e388-3b17-8f28-b6aa1ae63365 | -10.80465 | -44.23948 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 52660949-2f94-3263-8341-e65219797c6e | -10.12755 | -57.77641 | 2025-06-30 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22181532-8dfd-3f89-9d88-2dde6144a36a | -12.10518 | -54.67147 | 2025-06-30 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2f24a67-04ec-3380-bf3a-1380520ad3c4 | -10.55568 | -52.05125 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cfd3ead-2632-3345-b37a-ccc5807c2ac4 | -10.87656 | -56.45304 | 2025-06-30 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 33c03142-7b5c-3a5d-a146-2ad0b004218f | -9.24356 | -58.76009 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 262d2908-0111-376c-9e81-cdfa424bc3fe | -12.6257 | -54.23345 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67383361-faf2-3b6a-88e7-e90e894b60ab | -9.35503 | -58.85294 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63f51c07-6176-3bbd-99db-fdac5d208b08 | -9.94931 | -52.17016 | 2025-06-30 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcd5f4c7-9002-3c5c-943e-f4082f899b4d | -10.85052 | -53.73893 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36c03594-c733-3695-a0d3-a30ccc53fc3c | -10.1057 | -52.19564 | 2025-06-30 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d74fef91-336d-3262-ba49-ad10b88c8556 | -9.7175 | -56.18615 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 493ce69c-d33d-39cc-8567-a64241b4423c | -12.63257 | -54.22498 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5a7a8cf3-739d-3e78-a850-12168ec6fcf5 | -9.04118 | -61.22861 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4250367b-3ee4-3250-9055-0b62b1b85593 | -12.62421 | -54.23222 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86bcd520-1872-3a88-a048-cbc3b3a86237 | -10.87107 | -53.7357 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f841796f-6261-3ff7-80c1-c3be88ee455f | -9.23103 | -58.75023 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc2e33d7-e495-347f-a7a0-2f831780f1d5 | -11.19647 | -55.91994 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62358307-fbbf-3cda-af36-b29ba55c8f0f | -13.43145 | -47.83269 | 2025-06-30 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30509bc2-57bc-3e5a-b1f6-2ab30ddfbe3c | -10.87828 | -53.73679 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ecbdf53-3303-3d29-af89-92348ecac5b4 | -10.85287 | -53.74796 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b8da353-dfa3-3662-a2c9-8cd9bca9b5f5 | -10.22777 | -54.29729 | 2025-06-30 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f1fd80f-82ba-3383-95ad-3b625a758a4e | -11.20703 | -55.91793 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5c46287-30e5-319d-8725-ca758962df61 | -10.5485 | -52.04496 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f1f249b-d40f-32dc-8bf0-45164b63ff9b | -10.85421 | -53.75052 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce9046f1-711f-351a-8f7c-010d616afd40 | -10.30203 | -57.0409 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce91a007-e980-3bd3-abde-9da434b81b72 | -10.65521 | -44.49065 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 29995c10-02a8-3607-8b5e-4b28cbef3ee3 | -9.50374 | -56.09548 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc956d62-a595-323d-9b22-888e7a84ff2e | -10.86985 | -53.7442 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac4ccf99-e421-3d33-927e-673413c56218 | -12.60691 | -57.87348 | 2025-06-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd034d82-a80f-3984-8587-7d2e2d4e9430 | -10.10953 | -51.56902 | 2025-06-30 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91ff8263-115c-39ac-a285-347352c42e79 | -10.30149 | -57.04439 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0174deb-31cb-3d4e-b68f-0faf1403dca3 | -9.25452 | -58.75795 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 007bd71a-761e-35d0-b912-73ce56104f9f | -9.24074 | -58.75572 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43baaee8-34e7-3767-8403-68930eb05baf | -10.80134 | -44.2493 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| b337faf8-de43-3ea9-af1e-602bb032305b | -9.71419 | -56.18563 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9eeb3583-e1f6-3aa9-8b45-1a4213bf2925 | -9.23447 | -58.75079 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3406fcb-a5ee-3865-84e3-cdbd0013a1de | -10.85224 | -53.75219 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb61d015-7a92-3084-bf01-3729d51a0a4b | -9.24102 | -58.73234 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a013778-f7ef-30d3-bb1c-50264b45aea1 | -11.20928 | -55.92562 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 372b0a1e-3cd7-3f15-b5d2-0c46f2a21f95 | -9.24294 | -58.76392 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14508c8f-2b26-329b-98b9-faaf086b03f6 | -9.23696 | -58.73556 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 759438a6-3eb8-33e3-9af3-9f434ac0449d | -9.23165 | -58.74641 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| beaa77bc-4376-3cdf-9b38-63ce2e50122f | -10.55194 | -52.04152 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 41f7c59b-b606-39a9-a6fd-2be8aec9ce68 | -10.87467 | -53.73625 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb842913-6720-3f81-99b6-8c86743f8976 | -10.29433 | -57.04681 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 266ad33f-d049-3a78-8787-6619291fd97b | -10.56038 | -52.0467 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57a29788-227c-3709-a03d-b9e58a358a8f | -9.23979 | -58.73993 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30ab890a-e6b4-32a7-93cd-ea5285d2db4e | -13.01453 | -53.42555 | 2025-06-30 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9704d3b5-f24b-30f4-a29d-61fe773c6803 | -10.87463 | -53.76212 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e39e453-ab96-3300-8ae5-8b2fe3d7e9c5 | -9.781 | -47.80375 | 2025-06-30 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba1247f8-34b6-3c54-9321-91076a889b6f | -12.62358 | -54.21079 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3f274050-8abb-3b5e-81fe-d55181a8e654 | -10.55844 | -52.05299 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 086fca93-d403-38ea-8a72-d98cd1efb27b | -12.62158 | -54.21151 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b69cb574-835e-3473-bf61-5f750e5a5c83 | -12.62539 | -54.22388 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0fb1374b-a86b-3104-a3f8-1a0b651b6bc1 | -10.80263 | -44.23781 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| a0e05c8f-4573-353c-82ac-74d5194d0465 | -10.55915 | -52.04785 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0934ec1-523e-33ad-83e9-caa21b62c45a | -9.09043 | -59.49149 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba6f3e12-57c1-3955-b573-360a4fd0f9e8 | -9.70757 | -56.18459 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b74e129-7371-3cdd-8014-d2f38e76dec7 | -13.08106 | -54.85508 | 2025-06-30 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76796064-c3c6-3c94-8d1d-bb75e1974962 | -10.80927 | -44.23876 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 1244ed88-91c7-317f-ab42-7689a8e3c7c0 | -10.85476 | -53.73524 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 475afc7f-7e0f-309c-82c3-5e62c20cc1df | -12.45484 | -58.57047 | 2025-06-30 05:06:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c74323d5-068a-312c-9eb0-a9cb7873afe0 | -9.24136 | -58.7519 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1133bb61-3088-3d3e-8c2d-64833e9dca71 | -12.65656 | -54.10765 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22829d41-636e-359b-a08f-92b645dc2f6d | -11.09327 | -51.84375 | 2025-06-30 05:06:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba88bfb7-a659-3c1f-9678-81d40ba0bf65 | -10.87043 | -53.76579 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa328a31-bbeb-3853-a30e-b21127a7e402 | -10.7947 | -44.2485 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 87131c45-89c6-3b30-b374-cb56a23a0c4e | -10.35147 | -57.50421 | 2025-06-30 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d162f12-ec08-3df0-9212-08168f2720d6 | -9.24481 | -58.75245 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dadaadde-b60b-371f-b401-1b77e14fe638 | -10.16046 | -53.92581 | 2025-06-30 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2058bbec-1328-3965-89f4-0681941f687f | -10.88063 | -53.77155 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cad1dca-c7f7-3bc0-9ced-4b4534e09ecd | -10.13031 | -57.78049 | 2025-06-30 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cef3a039-1cf8-312f-b23b-c10fb37fecad | -12.62333 | -54.22457 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9da0b326-3355-3222-9780-da56baf89661 | -9.8899 | -56.10618 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c644b1b-571c-3b4b-8c6a-5ea358ee4d20 | -10.30155 | -57.13017 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acb8c957-f54c-386d-ab6a-4b4c8fcf5663 | -9.53336 | -63.57595 | 2025-06-30 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4225add6-7601-3b9c-a6cb-8a92b380c5f3 | -9.08262 | -59.49442 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b82eead-d2e6-3134-871d-a538ebba16c7 | -10.29764 | -57.04735 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f9ee7a7-7081-35eb-94fa-6e7daac68f8f | -13.01077 | -53.42498 | 2025-06-30 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21ae9d75-ae55-3484-a0b5-27df1d5d4177 | -10.12812 | -57.77286 | 2025-06-30 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45f509d8-77bf-31ab-a152-f1a9233784d6 | -10.12427 | -57.77887 | 2025-06-30 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8978404-56de-3183-96ff-39048467fd19 | -10.85301 | -53.75896 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b73ae6f-a638-38bf-9493-346e86d38d3a | -10.87645 | -53.74951 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8bdbd19-a1d8-3152-89c6-c12798e0d9ae | -9.25328 | -58.76556 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa610ebd-85df-3384-b8bb-ed259b69124c | -12.09877 | -54.66644 | 2025-06-30 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29016980-404d-3b6b-9287-d5e5f4b0084d | -9.08316 | -59.49573 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ba0b3aa-ca05-3290-9140-967e8d42eac3 | -10.85721 | -53.75529 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e84a35a1-1529-39c6-b829-899afd29b35b | -12.62394 | -54.22041 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| adcd7089-ac31-349f-901b-85492e91f078 | -12.76177 | -44.4088 | 2025-06-30 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96777453-348f-3e47-a28e-d110099d786a | -10.13088 | -57.77693 | 2025-06-30 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f62e778-a51f-34ec-9645-f7d0e10925e4 | -11.1998 | -55.92047 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README12.md)
