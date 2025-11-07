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
| dfaae38b-5c4b-3b2a-bcb0-b48b58fca686 | -16.11085 | -47.98059 | 2025-11-07 04:27:00 | NOAA-21 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1df5cdd-a7f6-3e59-b571-516d1c9b453f | -16.32501 | -45.61518 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3242892e-5dd4-3774-9a84-60d849d77bdc | -14.24729 | -46.85789 | 2025-11-07 04:27:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61693c72-9455-3349-9d00-6530064bcafe | -13.53946 | -44.55616 | 2025-11-07 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29863a3d-29b4-3ff0-90b4-a30e257770f2 | -13.26601 | -46.03207 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 500bf540-2c47-3c6a-aa7d-2717b655e913 | -19.03057 | -50.72784 | 2025-11-07 04:27:00 | NOAA-21 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d6ad7654-5ac4-3d12-8450-799b55e8a214 | -16.31443 | -45.61352 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08be5c65-3c86-3719-9ff2-6e68f3f4350b | -15.29198 | -48.02086 | 2025-11-07 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f53d634-7114-3e19-9f5a-8340a4fe0d4f | -18.21123 | -50.93916 | 2025-11-07 04:27:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a69672a-df20-37d3-8a52-109d689eb12f | -13.22095 | -44.55981 | 2025-11-07 04:27:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce84ff46-4cd4-333c-b0a2-447047efea93 | -14.24674 | -46.8615 | 2025-11-07 04:27:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e3aa507-b359-3588-a7be-eb20515fc284 | -17.21131 | -47.65338 | 2025-11-07 04:27:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e36d8c47-9a08-3ea5-91c0-1de14cde708d | -13.28156 | -46.05342 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c9d791d-28b7-39ee-a8cc-a9d30242b9e3 | -13.77262 | -49.34995 | 2025-11-07 04:27:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14b6ca82-da0f-31d4-aad5-35e74b361495 | -19.54235 | -44.16833 | 2025-11-07 04:27:00 | NOAA-21 | CAPIM BRANCO | MINAS GERAIS | Brasil | 3112505 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abdc3a4d-29cf-39c7-8525-14afaf7286ee | -13.27645 | -46.0412 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fe710f9-8965-3d45-97fd-95940c4c2051 | -16.33911 | -45.61739 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fecda77-8908-3331-a10f-5f658415d565 | -18.97738 | -50.03047 | 2025-11-07 04:27:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a5e5a7e1-6cac-36e3-868d-7bffc4e18b6e | -13.77855 | -49.70044 | 2025-11-07 04:27:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ad8f100-df1a-3f78-9824-ae7313947c51 | -12.67798 | -45.01407 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cfdeccf-3aa5-36e5-acdf-d7c14aa524e8 | -16.2968 | -45.61075 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21aaddfc-0943-3520-9cf8-86def097d477 | -13.77811 | -49.70095 | 2025-11-07 04:27:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73c4f844-57bd-3938-bfee-12aa48907889 | -13.27024 | -46.03642 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d2ad2bd0-ae75-3468-89e7-67d9b3564824 | -17.8888 | -48.5311 | 2025-11-07 04:27:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc0218b8-9570-33ff-9055-f8ea18b02e6b | -16.31796 | -45.61407 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a949f932-745c-38e3-bfb6-c86877bb4020 | -16.34616 | -45.61848 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1446ce59-848a-35ab-bc90-416a4f2a5592 | -13.28549 | -46.05023 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f437d577-da18-32bc-b0cd-9dbecdf83b0e | -14.63428 | -52.45641 | 2025-11-07 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8afb94cb-bdb8-35d1-bc96-d29d5bb07010 | -16.41926 | -46.55275 | 2025-11-07 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 978a0299-2656-3365-a0da-6ef97b4f47b4 | -16.88966 | -52.85768 | 2025-11-07 04:27:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ceda3129-febf-382e-a53f-d6502cf8f296 | -16.3491 | -45.62313 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7947e953-7f74-3aad-b9b4-91fd41ca0fb0 | -13.28832 | -46.05447 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0030554b-d84c-3469-9f30-bdfdb382a830 | -13.26741 | -46.03218 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 847969fb-a49e-3872-9581-192bfa3e626b | -19.84441 | -44.8941 | 2025-11-07 04:27:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51adee80-d20e-38f9-ae2d-3320f3a8f40d | -17.41665 | -49.68154 | 2025-11-07 04:27:00 | NOAA-21 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f704d25c-02eb-3321-b518-d80b9f8cf5a7 | -13.28494 | -46.05394 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3c583ec0-5ad2-3023-b432-2ff2e45cd64c | -13.27079 | -46.03271 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 525e7e2e-0e55-3288-956f-24ae9878f4be | -13.27362 | -46.03695 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 62bc8ee6-3c11-3779-9f6d-a634e1a07f0a | -20.80902 | -49.83892 | 2025-11-07 04:29:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c80da46e-08fa-34cc-afad-7a406e58fec8 | -21.16857 | -50.46374 | 2025-11-07 04:29:00 | NOAA-21 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e316c87e-9e61-32ca-ae57-76a47917a6a1 | -18.84524 | -53.58335 | 2025-11-07 04:29:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 583d29d7-cabc-3955-b0fc-788835042c63 | -19.33248 | -54.32027 | 2025-11-07 04:29:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f416f78a-aecf-332c-a5db-a3a4443e6a41 | -21.55309 | -45.74939 | 2025-11-07 04:29:00 | NOAA-21 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 23ab94bc-f14d-307a-b085-f013b3276395 | -22.10655 | -47.12611 | 2025-11-07 04:29:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5267cc95-a5e0-3f0d-9269-2e20fabe681e | -23.67245 | -49.83892 | 2025-11-07 04:29:00 | NOAA-21 | SIQUEIRA CAMPOS | PARANÁ | Brasil | 4126603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6d1f9272-2118-3cda-a743-683fd072eb41 | -23.33374 | -47.64183 | 2025-11-07 04:29:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 56d3cbe3-acae-3962-b209-959d4ccba384 | -20.39266 | -47.43925 | 2025-11-07 04:29:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc8f00ff-e903-36a2-ab09-755566871782 | -18.20602 | -56.7411 | 2025-11-07 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3d046d76-8d01-3ea9-a1aa-72c0ed86b6e8 | -23.60108 | -49.00884 | 2025-11-07 04:29:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d77c2d0a-81ee-3b0a-8f78-d5122bb6f609 | -23.52109 | -46.97304 | 2025-11-07 04:29:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 31aaaa52-c98c-32b0-8a2c-565863a7be17 | -9.435 | -59.1959 | 2025-11-07 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 0c1aa677-5f6e-3eb0-9385-e8f88f8cb9e5 | -3.3525 | -53.2315 | 2025-11-07 04:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 929a9ed9-e82f-391b-948c-412e54b51a9b | -9.4535 | -59.2143 | 2025-11-07 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 8e299066-0846-373b-9cf1-5d8df24ee3c5 | -4.2961 | -45.8938 | 2025-11-07 04:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 2c29edc1-f0cd-3b5e-baa1-1b76e1358acc | -9.4537 | -59.1949 | 2025-11-07 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 49cbc155-3dbd-397c-96b9-4c133fcf211e | -29.04624 | -50.60209 | 2025-11-07 04:31:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 64f21a3b-59f5-3ba6-a911-09170026d25f | -28.404 | -52.10935 | 2025-11-07 04:31:00 | NOAA-21 | GENTIL | RIO GRANDE DO SUL | Brasil | 4308854 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 62dfa069-5e66-3852-8f85-cda9da9cdbf7 | -9.4349 | -59.2154 | 2025-11-07 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 66890548-1bc0-3853-8eb9-94bf9c940307 | -4.2961 | -45.8938 | 2025-11-07 04:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 0bbb0e2d-ec83-312d-90c0-f3b5fc1dd08e | -3.3525 | -53.2315 | 2025-11-07 04:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| e4e5a93a-dfeb-32a5-9270-f1a98d8a5f14 | -9.4535 | -59.2143 | 2025-11-07 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 657fa870-47a2-3290-8df3-ee0949898aff | -9.4537 | -59.1949 | 2025-11-07 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 2476bf62-4618-356d-86c1-3cc409c0de0f | -9.435 | -59.1959 | 2025-11-07 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| afeac4dc-2279-324a-9536-6a0fb4291ab1 | -9.435 | -59.1959 | 2025-11-07 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 82417e38-1962-3d03-9adc-13594dd98479 | -9.4535 | -59.2143 | 2025-11-07 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a3b20641-ffc8-35cb-af44-b93984f687ca | -5.0868 | -44.7887 | 2025-11-07 04:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| a2a0aff2-f7c5-30af-b03c-9eccfcad1990 | -9.4349 | -59.2154 | 2025-11-07 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 4627484b-fd1d-36db-ba30-9a5c82d2426c | -9.4537 | -59.1949 | 2025-11-07 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ffa21750-a5bf-3fdb-9f8b-d43b7bba42fc | -4.29461 | -45.89043 | 2025-11-07 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5802a2d4-a888-3577-a4b7-50466904766c | -4.3182 | -55.84468 | 2025-11-07 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ce59570-29c8-3072-b358-0e4a4c65d95d | -3.33679 | -44.86242 | 2025-11-07 04:53:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c91ec30-d90d-344b-ba39-3f29f19841bb | -3.8281 | -52.19933 | 2025-11-07 04:53:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f75aff9-a6b2-3a41-a00b-1002a8e8472a | -3.04974 | -49.51605 | 2025-11-07 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cf69bfd-edac-3caa-afc8-be245d83196b | -3.35449 | -53.21981 | 2025-11-07 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8c13893-6d10-3e44-816c-d009f24e458a | -3.52834 | -47.54928 | 2025-11-07 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa1e98a4-785c-3694-a2b3-3a2ac024c7b1 | -3.84384 | -47.42036 | 2025-11-07 04:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b44a0fd-7087-38df-80f7-ef51d0d43e58 | -2.72907 | -47.39692 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ff5b4a4-24af-3ada-974d-3f0861679576 | -3.82865 | -52.19587 | 2025-11-07 04:53:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1431cfca-40dd-31a8-8339-b63356f4b9c9 | -5.6939 | -45.99417 | 2025-11-07 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e597fe6a-9eb1-3745-8c09-4a3fd7671cb4 | -4.82741 | -48.55283 | 2025-11-07 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 846a5dcf-204c-39da-81eb-ab02bee937b4 | -5.90833 | -43.49464 | 2025-11-07 04:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d64591f-6287-3aa0-99ae-5d4543254a91 | 2.53013 | -51.03841 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da14fc8d-55cf-372b-b57f-69bc4a2834fa | -5.09593 | -44.79553 | 2025-11-07 04:53:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 170d712e-ca11-3fd7-9052-4de4e0e428d0 | -4.49956 | -45.13777 | 2025-11-07 04:53:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d15726ed-9b26-3a47-8af7-20438c24da53 | -3.12393 | -50.14178 | 2025-11-07 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fabf2124-8412-3d29-ac51-626b6da035b6 | -3.15095 | -49.21162 | 2025-11-07 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa6873c5-250a-3cf6-99c2-1034494488dd | -4.2902 | -45.88981 | 2025-11-07 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e2694f76-7ed2-3a45-93c1-aa07b6b3bdca | -4.00577 | -49.27664 | 2025-11-07 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 447c81e2-0551-3713-9251-1cad5debdc3c | -5.27042 | -47.16376 | 2025-11-07 04:53:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c5135cb-4513-3223-935f-3b3b0d5c410c | -2.9881 | -52.82221 | 2025-11-07 04:53:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24c1d22e-e1ff-334a-b99d-437310ea3c0e | -3.35392 | -53.22337 | 2025-11-07 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2dd3376f-3ea3-3b2b-83ca-1af023c105b4 | -3.75332 | -52.07456 | 2025-11-07 04:53:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8df6ba7-8578-347f-9b61-a76f8d65ab23 | -3.60302 | -43.51735 | 2025-11-07 04:53:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1090ea81-8001-322c-aeed-e6d55cd9a1d5 | -4.29526 | -45.88607 | 2025-11-07 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2bda8ae1-1749-36e0-8d19-80096de0b5d8 | 2.56845 | -50.97935 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0887af79-3c2c-3cc2-87af-ba8ae9f1126a | -2.94529 | -49.35051 | 2025-11-07 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8fd111ae-9aaf-3823-bb29-aef73c39ebbd | -3.29749 | -45.37471 | 2025-11-07 04:53:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| debf0bbf-fa11-348c-b33a-1a6e1333ed2b | -2.90111 | -48.06393 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a2bb59c-dbf1-3575-9580-7234ad7cf296 | -3.04891 | -48.71783 | 2025-11-07 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b09b5798-ef2e-34f3-aacf-4c8b543a284f | -4.45344 | -46.43951 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README12.md)
