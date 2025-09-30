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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 508185b5-7962-3d33-b239-379a46169ab8 | -20.67185 | -50.22064 | 2025-09-30 12:59:00 | TERRA_M-T | MAGDA | SÃO PAULO | Brasil | 3528304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| e1e6ab3a-0f3f-3850-a1d5-69cb67acf6e7 | -14.59037 | -48.19878 | 2025-09-30 12:59:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 65e75f60-4c45-31f5-807f-e1f426fc50f3 | -14.85569 | -54.76074 | 2025-09-30 12:59:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 7311d9ad-c40c-36c2-bf49-dc8668427f20 | -15.91296 | -59.50123 | 2025-09-30 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ab7603aa-6931-3f00-850d-791ff8b0e0b6 | -12.95257 | -48.38752 | 2025-09-30 12:59:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 3e8dd194-8323-3eb3-a28d-c33c9a992dd3 | -17.93316 | -57.58939 | 2025-09-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.3 |
| b95302bb-2cfd-3692-bf15-eb3b0c4e3609 | -15.17212 | -52.82145 | 2025-09-30 12:59:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 33.3 |
| fd30ff4f-a53f-3921-86a1-fe950b91b0f7 | -15.85616 | -54.02057 | 2025-09-30 12:59:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 9bbf894c-da0f-3b23-a61a-fc224e88cc31 | -15.13428 | -48.37636 | 2025-09-30 12:59:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 4491ab85-6fc9-3a3e-85fc-69995e151587 | -15.25362 | -56.79192 | 2025-09-30 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| a85f4270-a6e5-39bd-95b8-a3fb973435d0 | -13.81022 | -47.89999 | 2025-09-30 12:59:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 27eac392-a5b4-3ed4-8a1a-f67d379a3810 | -14.85327 | -54.75394 | 2025-09-30 12:59:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 5c7084b9-c7bd-302b-a97f-cd85c07fefd0 | -11.8719 | -56.9531 | 2025-09-30 12:59:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 38a41929-ecff-378f-ba33-f8015a7f3938 | -17.92397 | -57.58831 | 2025-09-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.1 |
| 34f81f38-950c-3235-a3ea-d4d3103199d3 | -18.22157 | -53.33439 | 2025-09-30 12:59:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 7d6b752c-eefb-3f5b-a4bb-11ea96edc562 | -15.13068 | -48.37095 | 2025-09-30 12:59:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| f4b1c04a-1bec-3ef7-b854-78026fd216e9 | -14.59725 | -48.16412 | 2025-09-30 12:59:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 8ce4d371-bacc-3edd-bd75-69c287b11918 | -17.90693 | -57.57619 | 2025-09-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| d06a14cc-57f5-34ec-86b5-7ebcea4b5ff6 | -12.5937 | -57.91513 | 2025-09-30 12:59:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8868df96-7118-336d-bab1-7ec267152ec0 | -14.54004 | -48.35493 | 2025-09-30 12:59:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 3a600da7-aacb-30c3-9a3a-9b0edacb7c16 | -14.56194 | -48.47469 | 2025-09-30 12:59:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 782e545e-7c9d-3fa6-8afa-ec7422969c31 | -13.73911 | -54.71898 | 2025-09-30 12:59:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5212f3b4-8407-34dc-8b37-380254c4df6e | -20.68067 | -50.22691 | 2025-09-30 12:59:00 | TERRA_M-T | MAGDA | SÃO PAULO | Brasil | 3528304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.7 |
| 5f79e847-94b2-3ef7-a7ed-80b0efff498e | -11.96941 | -54.13465 | 2025-09-30 12:59:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| ce9c739d-c53c-3fcd-a09d-694f5f9bf88e | -15.24304 | -56.80072 | 2025-09-30 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1b45e1b0-ea0d-3aa7-b948-27f6c1522371 | -13.72888 | -54.71761 | 2025-09-30 12:59:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 44.4 |
| c4ce14ed-3a54-30ab-bf94-440a751a8c47 | -20.67487 | -50.1861 | 2025-09-30 12:59:00 | TERRA_M-T | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| ea98d99b-16e2-32c8-95c8-be32bc91d43c | -15.71726 | -59.51557 | 2025-09-30 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 035aed30-2c35-3a15-a765-46309340d466 | -14.51524 | -48.43182 | 2025-09-30 12:59:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 73bd93d8-4294-352c-9a43-8b252431a9da | -15.71863 | -59.50631 | 2025-09-30 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 1129d4f5-9119-3821-99b7-45cdf84067fe | -18.21544 | -53.3212 | 2025-09-30 12:59:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 6fd940b2-0b9e-33b3-86c4-1c1beb255fcb | -20.68787 | -50.22207 | 2025-09-30 12:59:00 | TERRA_M-T | MAGDA | SÃO PAULO | Brasil | 3528304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.7 |
| 8cf65053-dae9-3850-9e8e-8aa7b38e7b02 | -18.21725 | -53.30433 | 2025-09-30 12:59:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 39.3 |
| c8cc1e34-23f1-3823-ba6d-40ba1bafeb57 | -15.29202 | -56.78648 | 2025-09-30 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7bf80606-1af5-3abd-8379-d45ba844f13c | -14.84533 | -54.75928 | 2025-09-30 12:59:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 0626e93b-8218-3907-8c55-72a6ebf8b6e7 | -20.68351 | -50.19199 | 2025-09-30 12:59:00 | TERRA_M-T | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |
| 4ba020f5-e0a6-35e9-be66-a71e6882b8b5 | -16.56529 | -50.0427 | 2025-09-30 12:59:00 | TERRA_M-T | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 30.9 |
| f652cfff-1e7e-3b69-a413-d9a72ad6be71 | -12.10507 | -54.5773 | 2025-09-30 12:59:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 61151cb8-7be9-3532-a1d0-635b49c5d38c | -18.32813 | -57.09776 | 2025-09-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 0bd491a0-61c4-3b35-9693-f775db66663f | -13.72726 | -54.73008 | 2025-09-30 12:59:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 31.8 |
| c6e4f736-a811-32f8-ba00-2e8b5e690996 | -12.36906 | -57.55075 | 2025-09-30 12:59:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 50937182-9e34-3af5-bd9e-e295fcbaa613 | -18.21139 | -53.31531 | 2025-09-30 12:59:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 20.7 |
| b2d76fda-d84a-397e-a24d-94a92969f544 | -8.541 | -44.6515 | 2025-09-30 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d73ad082-8afc-34b3-b691-2b4e40f937c2 | -7.9191 | -44.6245 | 2025-09-30 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| e7f59cd0-d688-35e9-a914-809309e5b7bf | -10.0531 | -50.1978 | 2025-09-30 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 701a16e1-5a5c-3535-91e5-c16e6a15faa8 | -12.7022 | -45.2715 | 2025-09-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 88daa503-8ac6-3ffb-9a6d-6306ea68a2eb | -11.2138 | -47.2086 | 2025-09-30 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 241039c2-c2cd-3fd8-8597-66d852eac22e | -14.5323 | -48.4938 | 2025-09-30 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 5470e24d-e8f3-3224-a49d-789d96ff37af | -8.1616 | -46.3675 | 2025-09-30 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 07bd50d6-ac19-34f2-8c0c-943e32c7cd56 | -18.218 | -53.2962 | 2025-09-30 13:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 83.2 |
| cbe7f2d3-ccd0-32d4-9bd5-2b1587514769 | -10.8246 | -45.3611 | 2025-09-30 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 077dcba2-3f23-3e45-a7d5-0367ce7055dc | -7.2996 | -42.8722 | 2025-09-30 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 3042c5f3-91e4-3d91-a23c-c2de31c28339 | -12.8963 | -45.1943 | 2025-09-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 215.3 |
| 526ff7af-13f3-3001-84e1-a2c987b2734a | -12.2344 | -47.8086 | 2025-09-30 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 10c1c2cf-37d5-3575-b026-e239f93f33ca | -10.1851 | -44.8939 | 2025-09-30 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 438aef63-8a04-3684-8fa3-b225fc8ca1a0 | -7.8348 | -47.0207 | 2025-09-30 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| cb117aac-b517-3e7f-b249-3a3c5b52b22d | -9.1248 | -47.6256 | 2025-09-30 13:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 7da8fd0a-ed72-35ec-9c6c-442bc3839dc1 | -9.4007 | -54.6984 | 2025-09-30 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 6482d31b-6cbe-3827-a1b5-00db1354d529 | -8.8229 | -46.189 | 2025-09-30 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 36ec85bf-5e0c-3fb1-bb24-cb71a79ff023 | -13.8087 | -47.8927 | 2025-09-30 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 60d24058-28d6-3f2a-8e9a-e6dc501cabaf | -13.8074 | -47.9599 | 2025-09-30 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 5b661af0-29f3-3db1-b8c8-82e2da61dd3a | -15.2746 | -49.263 | 2025-09-30 13:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 70c02457-bf7e-3959-a4a0-85e0631f7bce | -14.5517 | -48.4907 | 2025-09-30 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 3f01c089-6975-30a1-858b-9f11b5e05cf9 | -11.1753 | -47.2358 | 2025-09-30 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ea407172-23e0-344d-b00f-928144ab4534 | -14.7171 | -45.2291 | 2025-09-30 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 7901ec92-0f43-34d4-853f-e8c49a4b70d5 | -9.9585 | -43.5752 | 2025-09-30 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 836bd8b3-9e16-3b3d-b42f-207efa6d5578 | -11.1548 | -54.1054 | 2025-09-30 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 1cf2c40c-37fa-309e-9b51-e6ccf063d897 | -12.8774 | -45.1742 | 2025-09-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 213.2 |
| 1486d6bd-8a9b-345f-9000-ecfae25d59b1 | -8.6479 | -46.61 | 2025-09-30 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| c5da660b-c2af-355d-bc0f-b32331beeab1 | -17.7149 | -46.6631 | 2025-09-30 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 479e5258-c403-3017-89e8-54c5e98c5f32 | -14.7166 | -45.2525 | 2025-09-30 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 445.0 |
| fc214062-dd80-34ef-95b6-7a165b96f2a9 | -10.6419 | -48.6021 | 2025-09-30 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 63ff5b12-568d-3186-9ac0-eaf284b00133 | -6.5227 | -45.2297 | 2025-09-30 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 9fe18837-e18d-3f5b-a864-c5744d31e4fe | -15.9268 | -46.2334 | 2025-09-30 13:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 6defa9f4-947e-3bd9-9a7c-df0e8b3aa566 | -7.8696 | -47.2606 | 2025-09-30 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 390fa1f8-120d-3668-a045-e8531fd8e781 | -10.9395 | -46.504 | 2025-09-30 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 76531c39-1232-363c-a199-8d233f604ffa | -10.0528 | -50.2192 | 2025-09-30 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 7ffe4667-6834-390e-b4d2-1044e9cf9ebb | -18.4862 | -44.0191 | 2025-09-30 13:00:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 961afd9b-9c24-374b-9ca8-3a2702a5faff | -10.0717 | -50.2173 | 2025-09-30 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| de7a04be-df62-3f2b-b877-729ffc9b836a | -15.9273 | -46.2101 | 2025-09-30 13:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 131.1 |
| dd47e932-c33e-3cc6-a26e-4b5f5261aeab | -11.071 | -47.8262 | 2025-09-30 13:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 5460bf7e-8b25-3ef7-950b-0671d1d2aa6c | -10.0342 | -50.1997 | 2025-09-30 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 49f214b7-84da-39b4-b164-c1a3714c9590 | -11.1735 | -54.1242 | 2025-09-30 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| f218d266-f4cd-3683-b1c4-7f7e1e83956c | -7.2999 | -42.8486 | 2025-09-30 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 9f7fe3ff-296a-3577-9a68-02a88299abef | -14.697 | -45.2561 | 2025-09-30 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 3af801b4-1aa3-3a63-a871-ebfc46f35d5f | -11.1944 | -47.2334 | 2025-09-30 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 6e4a9420-4b84-3af2-b746-5cd26489d8ab | -10.6423 | -48.5802 | 2025-09-30 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| b3767e4c-31e6-3a37-9ff7-7e10bc51c1e1 | -14.6603 | -46.9663 | 2025-09-30 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 4673cf33-be45-310e-b438-9d3eebdc2168 | -14.7367 | -45.2255 | 2025-09-30 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| f249fb73-8c55-3782-8794-5ec7653fc458 | -7.8378 | -46.7544 | 2025-09-30 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| d0bec875-e597-3299-b8d9-418cc8fcdb1b | -11.1546 | -54.126 | 2025-09-30 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 93d2c88e-0994-3eea-a267-27aba7f898db | -6.4131 | -43.0724 | 2025-09-30 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 9cd028e0-4f53-3c91-87f5-ee84d7dd19a5 | -16.7575 | -51.3482 | 2025-09-30 13:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 6d8f89cc-f94d-3ca8-96f5-06f5a8d05256 | -14.5712 | -48.4877 | 2025-09-30 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 9c87cc7b-4eb7-3b6a-9d95-1fe40d8bdefb | -10.3058 | -48.2681 | 2025-09-30 13:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 02dd211f-acff-3795-9f87-2f3c65929252 | -20.6818 | -50.2054 | 2025-09-30 13:00:00 | GOES-19 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 174.0 |
| 5188d599-b6a1-30e7-89b8-fbeff6669a7e | -12.952 | -48.4185 | 2025-09-30 13:00:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 4f95343d-1b42-35d6-a8f2-c4f652070fca | -12.9524 | -48.3963 | 2025-09-30 13:00:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| f5ca1e6a-7088-337b-adb7-fec5c8fd2221 | -7.8375 | -46.7766 | 2025-09-30 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 314.3 |
| d934594c-bb19-3899-8001-24530fee429a | -7.9194 | -44.6016 | 2025-09-30 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |


[Clique aqui para ver as próximas entradas](README113.md)
