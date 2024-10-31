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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddbea81c-a224-3772-a735-d29a6b8e6fba | -19.61392 | -56.69685 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 34.1 |
| 6bc52543-f271-3046-aeeb-3dbf8c957f00 | -19.60914 | -56.74829 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 256.0 |
| 58be8019-35c4-31e8-b19d-d87e2037a82d | -19.60678 | -56.72575 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 534.7 |
| 07cf6d09-2948-37f4-aa3b-a855bebec541 | -19.60501 | -56.7434 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 858.8 |
| 4c93e404-9731-3930-a0b4-797024d8a2e1 | -19.60443 | -56.70329 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.6 |
| b4cb4844-f6fd-3b6d-8d61-6aaabd9bf91e | -19.60282 | -56.72084 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 517.6 |
| 072692c1-c659-372a-bcdd-d7e68d51c1bb | -19.60063 | -56.69836 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 35.0 |
| 71023278-cd58-3b52-ba66-3a8fb6e8068e | -19.59581 | -56.74979 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2414.7 |
| a2601b03-51ea-3a88-a1b6-e358fbeb10f3 | -19.59347 | -56.72725 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1715.1 |
| 71db69ce-03fb-3fa5-bbdc-dd4b4eaa71bc | -19.59114 | -56.70479 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 14e5bfc7-923b-3e37-bc25-55286ba9b1b4 | -19.58248 | -56.7513 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 785.4 |
| 7384ec61-820b-3252-88d3-987b61d2c2e7 | -19.58016 | -56.72874 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 785.0 |
| c10e9fa0-b481-3bd6-ab71-9c752aaef2ce | -19.57786 | -56.70627 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 567a79da-8d35-3ebf-9615-a089fc1d10e9 | -19.56686 | -56.73024 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 41.2 |
| 2f63c93a-2bad-35d5-99b0-ba18f42922d1 | -19.56458 | -56.70777 | 2024-10-31 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 119.4 |
| 357125d2-efc5-3c87-8bd7-0f23ab7f34a0 | -19.54191 | -56.71716 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 678861fa-7b52-32cc-8567-abb3f8bdc295 | -19.54025 | -56.73325 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 1b301872-f6d8-3431-8945-41a72ceb2885 | -19.53801 | -56.7108 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 54f20f7c-eb03-3bc3-95fa-abe31fb1080e | -19.53038 | -49.64188 | 2024-10-31 01:09:00 | TERRA_M-M | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 525a0c56-0f86-31b8-848a-3bded82602c2 | -19.52863 | -56.71866 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 8e96e287-f8dd-3519-9b0b-7c1ded4eb071 | -19.52694 | -56.73477 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| e2aad89f-a746-3c7c-8155-538f02f9a94e | -19.52626 | -56.6963 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.0 |
| f4190be9-866c-34a9-b02e-3239c58e1075 | -19.52473 | -56.71231 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| b4673348-300e-387e-a629-9a7e1cfc4c62 | -19.51534 | -56.72013 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.1 |
| 9b660b91-9e2d-3620-b192-4c7adf98ca9a | -19.51377 | -56.60132 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 2dfb0b9e-b94d-3e05-bcf2-54bfa04c200c | -19.513 | -56.69778 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.2 |
| ab24f7c9-94ee-30f9-af4e-41fb6c6de832 | -19.5116 | -56.57937 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 5317ffd3-ff3d-3aab-a2a3-7b8447d2aadc | -19.51145 | -56.71382 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 367b013f-9466-36d7-971f-34de669ed71c | -19.50927 | -56.69144 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.9 |
| f987359e-f3bd-37d8-844e-52c244a3395d | -19.50135 | -56.58733 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.1 |
| a6d050dd-8588-3c11-82e0-8058b3a8fd23 | -19.50061 | -56.60284 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.6 |
| 1c8aac0f-e1a3-3db9-871b-84cb1b304579 | -19.49973 | -56.69926 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.0 |
| 71ebb0e6-7f98-307f-ba29-6a8ffe0292fd | -19.48878 | -56.72312 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| e837a827-0e48-37a5-a361-14ce6e210b10 | -19.47961 | -56.63423 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.7 |
| 71da6861-1743-35df-b42e-3347807d9ef5 | -19.47734 | -56.61223 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 6acdaf57-8958-34c0-9472-bfb9bd94e9b9 | -18.25641 | -55.98488 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 4e232e39-3c0d-38c5-aa6d-0a111994ca3a | -18.25444 | -55.96613 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 2960af55-eead-345b-82af-94b5040bb781 | -18.25323 | -55.99092 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 2af31a2b-d9a2-3083-8d20-654ac9059ed1 | -18.25113 | -55.97219 | 2024-10-31 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.5 |
| 3a8211c4-cddb-31c6-9d7e-27364c9442db | -17.56971 | -52.40134 | 2024-10-31 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 46.8 |
| a78d059f-ef03-3ead-bd13-3a768c549a1e | -17.56544 | -52.40847 | 2024-10-31 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 587f2fe4-6604-39b9-881d-99aefae9e50e | -17.56404 | -52.39779 | 2024-10-31 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 9d1ce46e-a602-3710-b8e1-1063cccceb23 | -2.87828 | -45.81661 | 2024-10-31 01:11:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 617ae9ad-1e40-391e-9827-30f371d21b53 | -2.87098 | -53.32855 | 2024-10-31 01:11:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d289b190-96c5-3bf2-bc84-81d806baa6ef | -2.86991 | -54.11251 | 2024-10-31 01:11:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1f73cf62-9879-390e-99dd-041c45a072d9 | -2.86789 | -45.84238 | 2024-10-31 01:11:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 680f5dc5-a6c3-388b-868d-d0f62c041bf3 | -2.86441 | -45.81877 | 2024-10-31 01:11:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 4473e00c-1fef-3526-9356-ab2c61345a30 | -2.81379 | -45.47642 | 2024-10-31 01:11:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 44280bdb-df4a-3219-b627-ed7ae7e591c9 | -2.79851 | -51.94618 | 2024-10-31 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 24405e30-de0f-3e76-8bb4-4a2778f1a375 | -2.7822 | -52.09485 | 2024-10-31 01:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| cee94964-1a53-37b7-ae5b-c325e92c15ba | -2.73602 | -51.82977 | 2024-10-31 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2b0fe577-fd5a-3226-b788-78768ac999ca | -2.6159 | -47.33926 | 2024-10-31 01:11:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 89a1886b-2ff9-362e-82a4-fee6ce81484c | -2.58282 | -51.92041 | 2024-10-31 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c56b5962-ce0c-3014-b36e-2d017f46f757 | -2.56101 | -54.00946 | 2024-10-31 01:11:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0c410858-afbf-3217-a7d5-c8b8cd395dfa | -2.51141 | -50.71376 | 2024-10-31 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7a0bd83b-e2ef-3cd4-a801-a787131ef3e5 | -2.5042 | -54.13336 | 2024-10-31 01:11:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| dfc1a828-e94f-3e7a-98da-af658b2c6790 | -2.50295 | -54.1244 | 2024-10-31 01:11:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| be538813-a934-370d-81b6-5a772eb0993a | -2.48284 | -54.04515 | 2024-10-31 01:11:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6d373f09-db69-3d3d-881b-727196d4016b | -2.40819 | -50.43027 | 2024-10-31 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b6e7a43a-ba2c-3e06-950b-bcf0cf91c425 | -2.33875 | -48.67091 | 2024-10-31 01:11:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e62b2dbf-fe4b-3fa2-9f5b-643ec0071511 | -2.27179 | -53.78817 | 2024-10-31 01:11:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 25959b19-ea92-3162-b4ed-6c4cc09b2dbc | -2.2345 | -46.70547 | 2024-10-31 01:11:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 39f6757c-4704-3968-8f66-82d8326defeb | -2.20003 | -53.72626 | 2024-10-31 01:11:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c32bdb24-6f33-3ed9-8cca-d7ac13bcadea | -2.1988 | -53.71745 | 2024-10-31 01:11:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f5683469-a1f4-3f4e-a965-6cd5d75b4098 | -2.19053 | -53.59293 | 2024-10-31 01:11:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e276a757-e780-3f9e-9365-2f10c67be787 | -2.18889 | -53.72472 | 2024-10-31 01:11:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c1956cb-b3c0-3d99-8993-940c3638681b | -2.16833 | -47.96737 | 2024-10-31 01:11:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 84a369a4-b58c-32da-8d95-1c967fbae80e | -2.16654 | -48.75196 | 2024-10-31 01:11:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4257fa21-f0f9-317a-bfd6-65df7d06294f | -2.16596 | -47.95089 | 2024-10-31 01:11:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 89fbe4a6-1bc0-3183-9056-41f1a3466b8a | -2.1626 | -53.66553 | 2024-10-31 01:11:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 57c6e5db-18c6-322d-933a-ffd1e5a2a1f3 | -2.0142 | -50.25164 | 2024-10-31 01:11:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 57ac5010-68a1-3c05-90c7-3776f6927640 | -1.97113 | -47.95793 | 2024-10-31 01:11:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 376abb3e-4871-3f0b-82eb-70d2f82e04fe | -1.95929 | -47.95963 | 2024-10-31 01:11:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| a128096f-2e6a-380a-b8ee-526b91d10343 | -1.94272 | -47.0389 | 2024-10-31 01:11:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| a285fe86-0e7b-31ac-a029-d18d1a7d9d09 | -1.89294 | -52.06107 | 2024-10-31 01:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3eca9ae6-cc50-310f-b11f-59de59e8e56a | -1.8839 | -52.06235 | 2024-10-31 01:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9aa1a979-3e8f-3cd6-9c88-2a192b9cb5f4 | -1.87508 | -51.01192 | 2024-10-31 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3e0ac0a3-41fd-35b1-80ab-3f3759f219e4 | -1.8656 | -51.01328 | 2024-10-31 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| efc12b93-941f-3aa3-a0f3-0e44f7c1ead2 | -1.84857 | -52.13939 | 2024-10-31 01:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6fbd37c9-1c75-3096-9f18-a506817d8392 | -1.846 | -52.12101 | 2024-10-31 01:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f7366ae0-5e63-3b95-8830-0d789df876d0 | -1.84471 | -52.11179 | 2024-10-31 01:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aba24456-4d13-35fd-98a9-3561d258756a | -1.83697 | -52.12227 | 2024-10-31 01:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 540b11c6-d16c-358c-af56-476b0c18e50e | -1.83569 | -52.11307 | 2024-10-31 01:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b81417da-b6c6-3ddf-af56-63f5f62a7ab4 | -1.77052 | -52.30548 | 2024-10-31 01:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8d3bb7b1-7a74-3235-858a-47ba3279fb14 | -1.74101 | -52.35597 | 2024-10-31 01:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3fa073c3-4b2b-3771-bf25-35de153c4820 | -1.64436 | -52.65707 | 2024-10-31 01:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0d86338f-3a30-30d1-88e6-f64ddb769875 | -1.64329 | -52.58419 | 2024-10-31 01:11:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 968cc125-b0ac-38dd-9f41-d05949dc497d | -1.63452 | -51.92666 | 2024-10-31 01:11:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8cdc2bf0-0d7f-3507-bdaa-fcc356afbc38 | -1.55806 | -52.03847 | 2024-10-31 01:11:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 22e612e3-6a42-35af-9e32-5edcf1b3e16d | -1.53483 | -52.1362 | 2024-10-31 01:11:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6865e1e6-2287-353f-9de4-1b888b5c330f | -1.53223 | -52.11773 | 2024-10-31 01:11:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 67c2f7ae-2e4f-3183-99f5-2c6d714a9618 | -1.53093 | -52.10849 | 2024-10-31 01:11:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2e15d1cd-96a8-342d-9063-8e5bfcfa8469 | -1.52963 | -52.09924 | 2024-10-31 01:11:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a24a019e-ed89-3f82-a13f-19224b2d908b | -1.45696 | -52.30338 | 2024-10-31 01:11:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 801b6a23-9bcb-3d65-b01c-40589c43f51e | -1.25352 | -46.61456 | 2024-10-31 01:11:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 41dfc499-312e-3126-96cc-557737ee4038 | -1.14316 | -47.30988 | 2024-10-31 01:11:00 | TERRA_M-M | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| cb85c69e-14ee-3799-858a-7fc13eb24603 | -1.06012 | -47.63268 | 2024-10-31 01:11:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 47a2cd8b-b85f-3d97-9a86-8fd5fcb8ede0 | -1.05739 | -47.63942 | 2024-10-31 01:11:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 2645f17a-b018-3892-a57c-2bbfe757714d | -1.05487 | -47.6213 | 2024-10-31 01:11:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 78930e4c-4623-3f05-b895-8f79c8ccd614 | -6.13829 | -43.97298 | 2024-10-31 01:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |


[Clique aqui para ver as próximas entradas](README8.md)
