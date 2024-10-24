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
| 6eebb692-d7fa-3c37-8740-44032d23fa89 | -3.0745 | -53.8252 | 2024-10-24 01:15:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| c9a440f3-4705-3e52-8072-6831e5f4e8b9 | -3.0929 | -53.8247 | 2024-10-24 01:15:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 6ae61577-e564-3c39-a558-166a1c95cbf4 | -3.1101 | -54.1661 | 2024-10-24 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| e62d3344-cf00-30fb-a19d-f21929d45f1e | -3.1102 | -54.146 | 2024-10-24 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 128cecbe-0908-37a5-8f7c-34e1204900c5 | -3.1422 | -50.4562 | 2024-10-24 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1aa44cd8-f76d-30d0-8a6d-4721728b19bc | -3.1607 | -50.4556 | 2024-10-24 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| c0b6676d-fc93-3f91-bac5-abda8a8f8377 | -3.7066 | -41.6997 | 2024-10-24 01:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 128.2 |
| 23989ca7-e6be-3f71-bb47-3b819cc6baa6 | -3.7068 | -41.6758 | 2024-10-24 01:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 153.0 |
| a0d8600d-cae4-3ec2-bfa9-617a11b042d6 | -3.7255 | -41.6748 | 2024-10-24 01:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 6ddb4674-4eab-359e-aec5-8661d48cf950 | -3.6612 | -54.2715 | 2024-10-24 01:15:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 7e6a4a5d-4f26-37d4-8c0d-01ef6b20fa65 | -3.6796 | -54.271 | 2024-10-24 01:15:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| f493cdeb-76f5-3813-89ee-bc3cbf5664a4 | -4.6588 | -44.61 | 2024-10-24 01:15:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 23884bd3-0aa5-3707-a511-f50afdb216b1 | -5.2935 | -47.0129 | 2024-10-24 01:15:36 | GOES-16 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8e141da9-21e4-3764-9d1a-0f890e12b313 | -5.4373 | -47.6833 | 2024-10-24 01:15:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| f1a665ae-e504-3004-ab45-59d3a64aa25b | -6.7238 | -40.4754 | 2024-10-24 01:15:44 | GOES-16 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 0035bd46-1371-3f45-9a87-5e643dc334c3 | -6.9272 | -40.8466 | 2024-10-24 01:15:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| c3b12a38-a724-3b5d-bbc9-e669105f43da | -6.9461 | -40.8447 | 2024-10-24 01:15:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 5815a6f1-7636-3355-af63-7c4fe31c2c9d | -7.481 | -63.5577 | 2024-10-24 01:15:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 8bb890eb-3f5f-305c-89e6-d01d3c8e6fe8 | -10.0489 | -36.131 | 2024-10-24 01:16:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| ccc6b83a-8bf9-3fe1-8d0b-e8304a4a36ab | -10.1969 | -53.8822 | 2024-10-24 01:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| bcc56b89-e292-3a1f-8b45-e53572b6bb2b | -10.1971 | -53.8617 | 2024-10-24 01:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7e7bb24f-c9f9-398a-8f64-71dcb36e7833 | -12.6914 | -43.8484 | 2024-10-24 01:16:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 9a5ef1b4-eaf9-3285-9319-2385ed61f672 | -12.6918 | -43.8247 | 2024-10-24 01:16:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| db00c443-ce6a-3ac6-bc79-86c69135c34a | -13.7417 | -54.0682 | 2024-10-24 01:16:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 78d97c51-98d5-3fe1-821b-b19b42444119 | -13.742 | -54.0475 | 2024-10-24 01:16:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| f70b0d42-1b25-322e-847f-ff4d44703b96 | -13.7609 | -54.0661 | 2024-10-24 01:16:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 38cdebe7-b7df-3246-8769-16dd2b6119e6 | -13.7612 | -54.0453 | 2024-10-24 01:16:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 7a870b40-19be-3069-9589-72f33d00424c | -14.9341 | -45.1187 | 2024-10-24 01:16:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 65.5 |
| de8fe8ba-be0a-36a5-9dfb-8d14ba31fa2d | -16.94 | -57.5268 | 2024-10-24 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 804596f3-533e-3482-982b-36569e74f1e6 | -17.0207 | -57.3743 | 2024-10-24 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 1e32e459-0414-3b2b-8325-d4c6c4dd993e | -17.2579 | -57.2439 | 2024-10-24 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| ea2d15a6-e7d9-30a3-8d8d-e900f886951a | -17.2383 | -57.2462 | 2024-10-24 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 3bbfc37d-f81f-3de2-bc08-66b08a7dbd0f | -17.7637 | -57.5732 | 2024-10-24 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 6941b7f9-1919-3a54-9395-c5fae34f8e6c | -17.765 | -57.4909 | 2024-10-24 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| fa049f82-1267-30dc-bb40-95e924af5d41 | -17.7831 | -57.5914 | 2024-10-24 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| a667c4e1-38fd-3c53-b771-f203835e6588 | -17.7834 | -57.5708 | 2024-10-24 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| 14d3a6aa-85e3-3ab7-8097-f8cbd9ba4671 | -17.7844 | -57.5091 | 2024-10-24 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 4e653592-04f8-3b02-941b-49a7f1f36075 | -18.0639 | -57.3101 | 2024-10-24 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 029cf3b3-952d-3b28-839c-f80228729da9 | -18.0837 | -57.3076 | 2024-10-24 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| 22b8bc3f-a176-310d-8974-e0b89c9417ce | -23.795 | -55.2753 | 2024-10-24 01:17:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 54.9 |
| 810b47f2-c0b3-3341-9ed1-639cdc8881bb | -23.816 | -55.2713 | 2024-10-24 01:17:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| 33463522-4860-3f16-bd57-8e87ee267290 | -23.8371 | -55.2673 | 2024-10-24 01:17:17 | GOES-16 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 63.1 |
| 1b9319b6-0f19-315a-8232-31b2c27e76f1 | -23.8278 | -55.28354 | 2024-10-24 01:22:00 | TERRA_M-M | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 5331cde5-dae8-3086-958d-2361cd3cb997 | -23.8264 | -55.27159 | 2024-10-24 01:22:00 | TERRA_M-M | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| 4b10231e-d2e1-354b-958e-e4727b5ddc1b | -23.8254 | -55.27752 | 2024-10-24 01:22:00 | TERRA_M-M | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| dc415b27-8c8a-308b-9a3b-40d0a00c6122 | -23.82393 | -55.26556 | 2024-10-24 01:22:00 | TERRA_M-M | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 4224a00c-01ce-3bea-bef4-719aa56c256f | -23.81557 | -55.27882 | 2024-10-24 01:22:00 | TERRA_M-M | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| 411da8dd-53e2-307c-9299-1b71199ce7a3 | -23.80576 | -55.28024 | 2024-10-24 01:22:00 | TERRA_M-M | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 2ed3b7bb-20da-398b-9102-afdd1a65a6ed | -23.79739 | -55.29359 | 2024-10-24 01:22:00 | TERRA_M-M | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 6381682d-0cb5-3101-8f29-f78682b05b6e | -23.79596 | -55.28174 | 2024-10-24 01:22:00 | TERRA_M-M | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 59.8 |
| b872448d-707f-3579-a56d-30fbe60ac553 | -23.79452 | -55.26982 | 2024-10-24 01:22:00 | TERRA_M-M | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 5d8e8b31-9bda-3194-ac12-97c9d24e7d55 | -23.26956 | -55.20788 | 2024-10-24 01:22:00 | TERRA_M-M | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 01da250e-a5ab-3f7e-8892-d87666510cbf | -23.2662 | -55.20235 | 2024-10-24 01:22:00 | TERRA_M-M | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b6ba9fb1-d63a-3ffb-b1aa-03db83c0c82c | -20.26693 | -55.4255 | 2024-10-24 01:22:00 | TERRA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 2a18c2dc-da35-3f9f-b7cf-f0c9e8a3e503 | -20.26554 | -55.41468 | 2024-10-24 01:22:00 | TERRA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 38547e9c-bc3f-3969-8969-d42f5a0d4304 | -19.71749 | -56.73773 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 36.5 |
| be6cd0ef-7245-33b7-af0c-ca0f57bd407d | -19.71174 | -56.77693 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 6a99a39a-7bf7-3c92-9e11-383e17b08d15 | -19.71026 | -56.7643 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| a224bf62-3c50-370b-ad83-f73766d3ddfa | -19.7073 | -56.73912 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 2b77384e-d537-3244-8d82-1880b3e45ce7 | -19.70153 | -56.77831 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 58a66dbc-2943-3a1f-a130-2a5706512348 | -19.69564 | -56.72794 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 18676d6a-34ec-39b4-ac87-71e6df7bc53d | -19.67333 | -56.78846 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 01fa3245-8f6c-38f9-be16-bdef0e13e406 | -19.67181 | -56.77584 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 30.1 |
| 85f53686-21d7-3f11-a424-dd97183d2dff | -19.67074 | -56.85329 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 6ab1400e-7b34-3a5b-ba3c-89dc0afcdbaa | -19.66312 | -56.78983 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| f7d20aa9-d6aa-38d1-9364-788ed4f4490f | -19.6616 | -56.77721 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| bb2b1a2b-6aa7-32fd-be57-f8c4e023258d | -19.66048 | -56.85468 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 30.3 |
| 00521e13-5fa9-3de0-a097-09e46a07c556 | -19.66008 | -56.76462 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 32.8 |
| f32fcb40-c44f-343c-bb3a-cb6169906108 | -19.65857 | -56.75205 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| a630f414-8c7a-3031-a016-56ddb0a8eb03 | -19.65706 | -56.7395 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.2 |
| aa9cdb5a-d31b-3232-8cc1-ad047c1dd860 | -19.65555 | -56.72697 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.1 |
| 7e08d692-af49-3fed-ac25-cd89231b0f7e | -19.65441 | -56.80386 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 31.7 |
| 95490d86-274d-3b09-804d-c2e93ee02f1b | -19.6529 | -56.79121 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.5 |
| b4fdd456-f946-31b3-85bc-81a891f4106e | -19.65139 | -56.77859 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 56d64cac-b8e6-3e9c-a2d8-ae205895083c | -19.65022 | -56.85606 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 52.0 |
| 17657d0e-e8f1-3941-bec8-5893607f474c | -19.64989 | -56.76599 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| aef46179-4d68-3979-8134-fec4f60bcbba | -19.64871 | -56.84332 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 056a5dc6-17e1-3b9e-bc83-2f7e3b7cb4e5 | -19.64838 | -56.75342 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.9 |
| e2e3430f-bdf3-39cd-97fe-dd18e1cd6da4 | -19.64688 | -56.74088 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 132.3 |
| d5c39176-800a-3e5f-ac1b-bbb34e0cbf39 | -19.64569 | -56.8179 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 539ac4ed-9777-3f53-8e79-da410cce16ef | -19.64537 | -56.72835 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 34e3e452-db1d-303c-b7f8-63a2c6d04e3a | -19.64419 | -56.80523 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 34.3 |
| e4cdc7d9-585b-3478-bae9-cd714b051169 | -19.64268 | -56.79259 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 6e1e50d2-374e-363f-a63d-b4fe2b5e7ec3 | -19.63996 | -56.85744 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 34.5 |
| 0a9051bb-a1ff-3184-a5a1-8c8049a02005 | -19.63969 | -56.76737 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| cc2b042b-d384-35a5-bf55-f06d52708fa9 | -19.63845 | -56.8447 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| d49c1d9f-c104-3a44-ac07-3fce0ec15749 | -19.63819 | -56.7548 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 27.2 |
| a2244215-be69-3bc7-b0c4-6f6eea904b3c | -19.63696 | -56.83198 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| bd751da7-3fae-31ca-92ad-704f527699c6 | -19.6367 | -56.74225 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.8 |
| d2dbaea8-9eb3-3fcb-8610-dff71a0c361d | -19.63546 | -56.81928 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 22.1 |
| 760d3b79-6ecb-326a-ab93-d4ee4df35e0c | -19.62949 | -56.76875 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 31.3 |
| 0362a730-a298-3c57-b212-ff18b43830b7 | -19.6282 | -56.84608 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 2dbb7853-1c9d-3761-908e-8ccc347832f3 | -19.628 | -56.75618 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 36.4 |
| 24355d24-71c4-3c95-8c4b-a14f854fb9ac | -19.62651 | -56.74363 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| cbe59a0f-9b31-3e27-a8cb-5962d8892e73 | -19.62089 | -56.85289 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| bda8f8b8-d9dc-3c34-864c-9d8fc3da3589 | -19.61933 | -56.84019 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.0 |
| 9500e4f9-340b-3ea0-9611-50248ac75e4a | -19.61929 | -56.77013 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 0df2d7ad-a02d-311e-b60b-072e69d33976 | -19.61795 | -56.84747 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| b0dc25a9-669f-3a00-895e-86b67b5936ed | -19.61647 | -56.83475 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 3c22d506-f827-391a-82a5-2d95f94de10b | -19.58146 | -56.53647 | 2024-10-24 01:22:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |


[Clique aqui para ver as próximas entradas](README7.md)
