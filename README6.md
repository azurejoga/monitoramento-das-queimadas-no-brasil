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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 235b219d-41b6-3973-8598-211de0ef3015 | -10.97551 | -45.08406 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| bf9129d4-c6ce-3f3d-917f-d7f18b3c1502 | -13.37359 | -54.26924 | 2026-05-01 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8a0ab41-4551-34de-822c-9ce34d534893 | -12.40403 | -57.79333 | 2026-05-01 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bdea1e2f-08b1-36dc-9bbe-774767b10954 | -12.05719 | -57.41891 | 2026-05-01 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38217a4e-06bb-3c46-bdd1-a1b57990c71d | -10.97397 | -45.09744 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| bdaec5af-5f70-3892-8fc6-f00a3dd51d90 | -12.05707 | -57.42199 | 2026-05-01 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29f81fa1-1dc7-3af5-a977-26eed96bb804 | -12.08812 | -51.22453 | 2026-05-01 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8500653a-0df0-3c2c-af08-c06e03057d6a | -11.4333 | -55.10083 | 2026-05-01 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f34de479-4282-3801-adbe-1ac44ae26278 | -13.37481 | -54.27073 | 2026-05-01 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f127d84-c568-3728-823e-fcbf5dea313a | -13.37757 | -54.26982 | 2026-05-01 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| beaeba2d-0c5a-382a-8605-8fe6082b28ea | -12.37701 | -54.75281 | 2026-05-01 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 422656f3-157a-3793-9fd3-8053bfe41435 | -12.34207 | -50.00673 | 2026-05-01 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8cafe2d-ed6a-3752-ac0b-6ce9602340af | -12.37068 | -50.03331 | 2026-05-01 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c67f48d-d364-3956-9dc1-c4951cd8ef14 | -12.37768 | -54.74803 | 2026-05-01 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5914c35-4411-3219-a0f9-9cf13b1d4508 | -12.37108 | -50.03011 | 2026-05-01 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0140c2b1-3f99-3f8c-b243-0372b818b766 | -12.37387 | -54.74744 | 2026-05-01 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae7526da-b06b-3b7e-b112-079ecc1be81a | -10.98094 | -45.09856 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2c55adc9-6945-3c2c-ba3c-83f533af9e30 | -12.3759 | -50.03402 | 2026-05-01 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 922ba5c2-2d25-346b-9fcd-8524fe4fc5e2 | -12.29244 | -57.38655 | 2026-05-01 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce304f20-80a6-33e2-8bdb-056880abb34f | -10.98328 | -45.07834 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 10d49f29-2a76-3fe1-a5d5-a2d5782cf86e | -10.98945 | -45.08636 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| d34db388-c253-3207-9902-9f6076557675 | -12.2964 | -57.3834 | 2026-05-01 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ab6fc96-5dd1-3179-97ef-8dfe37aba9af | -13.37083 | -54.27014 | 2026-05-01 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8b26158-fdeb-3bf3-81d4-322acd5ba36d | -10.98248 | -45.08524 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 500e1d76-ef69-31f8-8f34-f30340fe3f46 | -10.97323 | -45.10387 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 207518f6-6cba-3feb-bb94-25472dfbfbfc | -12.40067 | -57.79279 | 2026-05-01 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b27e24c-b4ec-3ca5-9532-15d6cb81af9e | -12.9916 | -54.68165 | 2026-05-01 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95682161-0657-3296-b31a-f4563cc4a9e0 | -10.99025 | -45.07946 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| b3efd352-b6c3-3fde-aa55-54d3e12b1a06 | -12.29188 | -57.39024 | 2026-05-01 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fea8d95b-e795-3ef3-bf9c-4a18d491a7d5 | -10.97629 | -45.07728 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7eb3316e-6bd9-369f-bc13-ad836d2b0ef5 | -14.32752 | -57.7353 | 2026-05-01 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36a46b03-34a6-344b-8e25-a3c749a6cf82 | -16.04237 | -52.36419 | 2026-05-01 05:23:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8472615d-f9a2-37aa-83c2-791ddee48faf | -19.15654 | -57.5584 | 2026-05-01 05:23:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b44a75a8-d9cf-3a70-85cc-bb354416b611 | -17.96043 | -52.90213 | 2026-05-01 05:23:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03278e90-ce23-3390-9c7b-3b4f6414ac21 | -18.50846 | -55.51174 | 2026-05-01 05:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6efe11f2-4a25-3bf9-af12-30b37bf11bbf | -18.50915 | -55.50646 | 2026-05-01 05:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 15d31d31-a772-36f3-96c1-754bfd5239e0 | -18.51311 | -55.50705 | 2026-05-01 05:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 125167d7-8bfc-3bbc-93fa-3c840ba4a474 | -20.71409 | -55.17796 | 2026-05-01 05:23:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6851e5ee-84bf-3f9d-af17-44fe39c80a02 | -14.33092 | -57.73583 | 2026-05-01 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7c41687-b002-3d03-a751-1db4deacdd38 | -14.20664 | -57.43101 | 2026-05-01 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1939c19d-9b75-3a6a-83db-5ea0fc03997a | -18.51241 | -55.51232 | 2026-05-01 05:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2df07d0a-adfe-3d1e-a167-9be0171bb1c9 | -17.01821 | -54.34662 | 2026-05-01 05:23:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13f9d324-7b12-3991-826e-91932bed6e83 | -14.2032 | -57.4305 | 2026-05-01 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8256c39-cbb5-31fa-a001-0ddf0c9b084f | -20.20649 | -46.46224 | 2026-05-01 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dcd675b-8bff-3e2d-af8c-f293be680734 | -18.51568 | -55.51817 | 2026-05-01 05:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fcbd8a1e-d3b6-307d-8e0a-5da955810711 | -19.15542 | -57.55566 | 2026-05-01 05:23:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2d0e5777-a1c7-3973-b72a-febff0f3b108 | -20.21412 | -46.45627 | 2026-05-01 05:23:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94988a6c-bc8b-33e5-be41-5664759bfd17 | -12.98756 | -54.68001 | 2026-05-01 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c93dad2d-bf4b-3264-b229-8be6b4028722 | -14.2032 | -57.42919 | 2026-05-01 05:40:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c6d45f2-8358-395b-bb9e-92646649cb68 | -12.37767 | -54.74839 | 2026-05-01 05:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c0f55e5-65c2-3549-81af-047fd3294aba | -12.99276 | -54.6813 | 2026-05-01 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 596a4d0d-e13b-3298-b66e-887f913fc08e | -12.29138 | -57.38461 | 2026-05-01 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b09a0706-c156-3c04-9931-cf834521c723 | -12.98697 | -54.68061 | 2026-05-01 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d589028-6177-3fde-967d-2d3b09acba68 | -12.29068 | -57.38991 | 2026-05-01 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ab9d6d9-a3cd-370d-82a2-3cfad5db2a37 | -12.99335 | -54.68071 | 2026-05-01 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64544bce-2075-3570-b19a-3098cd6bd293 | -12.98708 | -54.68419 | 2026-05-01 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6004a8ba-c794-3fc2-a123-e18180301041 | -12.37147 | -54.75165 | 2026-05-01 05:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdf49437-1f37-3763-b056-44c664dbd201 | -12.37718 | -54.75245 | 2026-05-01 05:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28c4b416-c830-320a-b06d-05efe8550d7d | -13.3763 | -54.26801 | 2026-05-01 05:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96c38198-f809-3001-830b-a06d48221d02 | -12.37196 | -54.74757 | 2026-05-01 05:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f5bda41-da6c-3347-a162-337ff99b6438 | -18.51005 | -55.51189 | 2026-05-01 05:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 950cb56c-96c1-324d-82b0-3d6f183c0a2e | -19.15424 | -57.55759 | 2026-05-01 05:42:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| be038b42-74e6-381a-adc1-2ef1ca9cae24 | -18.51051 | -55.50751 | 2026-05-01 05:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b0d91da6-469a-3fea-a22a-eb7f6c13a7da | -19.15459 | -57.55425 | 2026-05-01 05:42:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a1d9ba99-8d43-372b-8d61-c4a28ae6854e | -18.50879 | -55.50969 | 2026-05-01 05:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cdc6aefc-a523-35bc-bb1c-d50f1f75e55e | -10.9624 | -45.09 | 2026-05-01 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 7357a265-726c-3021-b9b2-45395aaa4ed0 | -10.962 | -45.113 | 2026-05-01 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 8e92b69a-c20b-3812-8a20-9064fd218a73 | -10.9811 | -45.1104 | 2026-05-01 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b83d141f-1904-329c-9a0b-eb63e3c74052 | -10.9819 | -45.0643 | 2026-05-01 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 1cc8f12a-fca5-3855-b829-ffd9f539fdfb | -11.0006 | -45.0847 | 2026-05-01 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7919f8fb-30e9-381f-b27e-c51ffc0e8c41 | -10.9815 | -45.0874 | 2026-05-01 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 277.0 |
| 2c36b635-3189-31e9-9daa-9cd8c1c23466 | -10.9624 | -45.09 | 2026-05-01 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 3889c0fb-e366-321f-9005-65f30a8bd4f1 | -10.9811 | -45.1104 | 2026-05-01 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| e61a42cd-c801-38df-bac9-e3d66a2f41ab | -11.0006 | -45.0847 | 2026-05-01 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| cd1791af-4a48-325c-8153-4f6a9c46fd5e | -10.9815 | -45.0874 | 2026-05-01 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 281.6 |
| 677ab506-28e3-3eb4-bff5-f0fa8f36b80d | -10.9819 | -45.0643 | 2026-05-01 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| a57d8d09-c387-3cd9-8ab5-2f02f67eac14 | -10.98099 | -45.08433 | 2026-05-01 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 242.8 |
| 625e84ff-3680-3841-ba13-0e04e339f7d2 | -10.99255 | -45.07416 | 2026-05-01 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 17e7757c-1e7a-3ccf-bc3f-6e62f1e6c19c | -10.55438 | -44.33342 | 2026-05-01 06:29:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e321b90b-fb3a-3a26-9f75-cee98d1ee40d | -10.99091 | -45.0858 | 2026-05-01 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 918de8ee-d43e-35ea-aac0-351c9fe4b19c | -10.97937 | -45.09589 | 2026-05-01 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 384408c2-e3aa-3f53-8c86-74db3a51f48a | -10.96786 | -45.10585 | 2026-05-01 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 02004965-a10b-3894-9543-2431a7a2ff02 | -10.96946 | -45.09439 | 2026-05-01 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 8efd0ad3-29c6-38fc-b533-858967450661 | -10.98262 | -45.07266 | 2026-05-01 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 792a1961-0604-3206-a877-9cc5f4314a08 | -10.97269 | -45.07123 | 2026-05-01 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| ab1f7845-b73e-3229-a79f-22064b2b018e | -10.97107 | -45.08284 | 2026-05-01 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 605a494d-ff19-3caa-a404-86dd30c10527 | -10.9819 | -45.0643 | 2026-05-01 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| bb508e96-c526-3189-adf9-fd819f413be9 | -11.0006 | -45.0847 | 2026-05-01 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 4a2db2c7-c08f-3bb2-9682-755f81178db7 | -10.9624 | -45.09 | 2026-05-01 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 8e8f00d3-98ff-3693-8a07-3ab6d8c69ca7 | -10.962 | -45.113 | 2026-05-01 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 64c26d00-6390-3162-af7c-b1efa354eadf | -10.9811 | -45.1104 | 2026-05-01 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| aac47474-f53d-3faa-81f6-57860170cbc8 | -10.9815 | -45.0874 | 2026-05-01 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 285.3 |
| 8121a745-1130-3c0e-ae8f-fbdc76b42f91 | -10.9815 | -45.0874 | 2026-05-01 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 266.0 |
| 48a47ea3-602a-378f-8a52-adef2e02d7c6 | -10.9811 | -45.1104 | 2026-05-01 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 9c87593c-7204-3496-8c8c-27e909be59fb | -10.9819 | -45.0643 | 2026-05-01 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| fe06655b-5855-35eb-860a-3abb10610b6f | -11.0006 | -45.0847 | 2026-05-01 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 9d8eb0b1-556a-3f34-bfc9-ce2b2031ab3d | -10.962 | -45.113 | 2026-05-01 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 6a62c853-1ec5-3c17-bc70-931d34c06d5a | -10.9624 | -45.09 | 2026-05-01 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| bb263023-3bd8-3042-988a-f44a6537da6f | -10.9815 | -45.0874 | 2026-05-01 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 241.7 |
| a1c3e9f5-2afe-34f1-bf94-8b51196496d0 | -10.9624 | -45.09 | 2026-05-01 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |


[Clique aqui para ver as próximas entradas](README7.md)
