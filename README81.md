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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 911c188f-3cc2-325d-89c2-dbbbcaffe78f | -9.71924 | -65.71568 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f74a30a-98d3-30f4-9385-b9fab541682d | -9.01494 | -65.69483 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 03ca2e58-4af3-3a5c-bde7-c5128d448d7c | -9.02016 | -65.71095 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c7f18dd6-829f-3a53-a308-c53584437d2b | -14.79414 | -59.62636 | 2025-08-24 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe446ba6-a8ab-348e-a080-5c4f5544f150 | -10.05258 | -59.35821 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b275a7d6-6e1b-37e4-9487-248b700c7a1b | -8.13164 | -62.86309 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9c1b001-3c89-3b59-8816-86885cd78256 | -9.81938 | -64.26893 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdbed32f-8792-3d1d-88b3-617d94c6ac1d | -9.13591 | -60.73468 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 720e7335-2045-3dab-ac83-aeab48c4486f | -20.34571 | -51.69597 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e1caa603-40dd-3b95-8bca-46fbff94cf04 | -9.16592 | -59.48282 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f5dd5c0f-34f8-3b82-8419-ff4d1cd0e51a | -11.52249 | -50.49411 | 2025-08-24 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 410bf02d-4339-396e-b98c-416fa3550660 | -9.14998 | -59.45002 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ed12b92a-5080-312f-a2f1-8fb090c23749 | -8.90899 | -62.44152 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56545b78-81b8-3823-8781-13f85ee2802c | -8.46667 | -63.92295 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e20ebf6f-24ed-39fa-99c6-ac6c664c30db | -9.02792 | -65.71236 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ddd5b784-4b64-3504-85d3-fad5478cd6bb | -9.19406 | -60.77575 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66e2fffd-cb43-370d-a986-323b75ef1825 | -16.79206 | -51.35754 | 2025-08-24 05:25:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fb9bcd74-57a1-3c5a-bfdd-254707dc6926 | -8.70468 | -62.87881 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b677c690-394a-3b0f-9661-d8add8770b4e | -9.1642 | -59.4712 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 695accee-d39f-3adb-ba1b-fa98014b4911 | -9.00985 | -65.7244 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cab21d2-4f18-3e1f-982c-aaf1b4cb1a67 | -9.52308 | -60.55814 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 830b61ab-e27f-357a-841c-fc16dbc98e6e | -10.60922 | -55.40921 | 2025-08-24 05:25:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1973899-4cb6-3f75-a8c5-6f84be5b6f9b | -17.83852 | -50.81704 | 2025-08-24 05:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0d0edab8-baf8-375e-a49c-55a88da3ec37 | -9.47719 | -63.13245 | 2025-08-24 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 199b22f3-7382-3390-a8b2-7edc85d3a4ac | -8.91686 | -62.43543 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7b51509-60a1-3bdc-9ac4-2fca96c1c067 | -9.13598 | -60.77765 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 112167fe-1410-37d5-8447-fc5027280798 | -8.88858 | -62.40555 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 650d8e3c-40b9-3a52-9147-c6d514ed1a86 | -8.47022 | -63.92354 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89ed2556-46f3-396f-8a96-6fe9e6c09837 | -11.52638 | -51.85808 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 393aa95b-0abd-38b8-beab-855ef9930b53 | -9.19039 | -59.61855 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c11c8fe9-ef1b-301b-bad3-ff5980327a17 | -11.52532 | -50.47258 | 2025-08-24 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 089f00a6-0da0-3d8a-94fa-5f65f37f2c55 | -9.21837 | -59.62242 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb7af936-c0af-3a66-83ea-8a3c7e098472 | -8.62837 | -62.62999 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7674af85-48fe-38db-9d10-fb5f1a92dd65 | -8.87493 | -63.66502 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d6e15c3-5192-3da8-b9ca-8dac3448b3b9 | -9.15739 | -59.47015 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7f83cd9f-1019-3790-9e3d-1c2c687b8593 | -9.07063 | -65.71967 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bde9d09-5948-3792-a58d-f3aa3537c95c | -18.02275 | -51.08374 | 2025-08-24 05:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 839811ef-0d82-3513-9f27-babf24eac567 | -9.02321 | -59.01583 | 2025-08-24 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8324984e-9593-3ef9-acb6-0df27fc96d56 | -20.3583 | -51.69673 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ab52180c-402b-31c1-a5d8-7deff142fede | -11.18395 | -55.02804 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ce524b2-02b8-39f0-93f5-827db0f63eec | -9.15971 | -59.50077 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f48b143-0e1e-3b19-bc00-e223e134a4ad | -9.65382 | -59.63557 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f61e2861-b3b5-3c52-8cd2-3b71dcab614a | -9.25165 | -60.92803 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4901864-f769-3573-a736-0bc51a75c13b | -9.52019 | -60.51071 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1dd7e7f-2671-397e-94ad-ae6080404975 | -9.1957 | -60.76526 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08a85be7-a752-3645-b75a-e32b98585ee6 | -15.67256 | -53.87531 | 2025-08-24 05:25:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c8e4235-9680-3266-a4d4-07fb64506d4a | -16.78584 | -51.35739 | 2025-08-24 05:25:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f9fb3ba2-f5b6-36f0-aeca-5fa8141e4da0 | -7.8096 | -63.55341 | 2025-08-24 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c6633b1-dc8e-3938-a311-6b0a55b004eb | -8.88973 | -62.39838 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77e0d709-1fa8-37d8-b098-fea50edafcc9 | -22.60749 | -52.49981 | 2025-08-24 05:25:00 | NOAA-20 | EUCLIDES DA CUNHA PAULISTA | SÃO PAULO | Brasil | 3515350 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f9f4bef0-8870-3902-9b39-239522bd8fa2 | -9.16027 | -59.49707 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88c96a07-69cd-3ade-8b31-186cc992a25c | -9.02404 | -65.71165 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5f05f6d4-df51-359c-97ca-88fbc05aba3b | -9.10434 | -61.43278 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bfc0b54-d340-3aba-bd49-0f966237e743 | -8.89834 | -62.44347 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28d6fc14-58db-3f77-a009-f6d38604e1c5 | -16.38765 | -49.64584 | 2025-08-24 05:25:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 317639d7-b9ab-3c5f-97e0-2729af92ac59 | -9.02101 | -65.70599 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4f74d77b-9ba1-37e4-999e-373f9928225d | -9.21809 | -59.61907 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad405298-1b69-39c7-acff-5cee2064fdf8 | -9.19434 | -59.61542 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc529925-895c-33d9-a922-75dcf9905c2f | -9.15403 | -59.49231 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c4ffcdb9-6c4b-32b6-aee7-0635287e4754 | -9.22177 | -59.62295 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1b2d65e-6af6-3786-974c-ef7d2ff37570 | -8.68318 | -62.87952 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0a2d537-dc44-33e1-8fee-3d796e971005 | -14.79 | -59.62979 | 2025-08-24 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc4a11b5-4fdb-3cf2-8e6c-e37f079a548b | -9.17349 | -58.30463 | 2025-08-24 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27d0690d-0f5f-39e8-9793-3f3b01f456eb | -7.80609 | -63.55283 | 2025-08-24 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39cc9a91-625f-3c17-b315-5e6a82287508 | -8.6144 | -62.60903 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32f42bdc-3264-33ef-88bb-25c597d131a4 | -7.9738 | -63.08019 | 2025-08-24 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb2251ce-51f7-38ec-a42e-a08beeed8654 | -9.19851 | -60.79079 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8fdae96-2532-379a-98b5-b8cdfc454238 | -15.29722 | -56.1604 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a8868c03-899a-3b92-8cfe-e0445a402b37 | -15.30163 | -56.16101 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c0443a1-19ea-3f88-a546-50007bd450f4 | -8.88637 | -62.39783 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fed8b24d-92de-3fcf-a28f-0433e1fefe88 | -9.03483 | -65.71866 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac356f09-573c-3d20-b021-badb7ebc9f84 | -8.90911 | -62.41947 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0cbe0e48-0bd1-3fb1-88ce-b5a9c6dca439 | -9.32925 | -63.19994 | 2025-08-24 05:25:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e25553a4-4944-3853-9d88-63b57d07c1f7 | -9.18643 | -59.62168 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de44deec-0580-33ba-bfd0-23cdf91ef24b | -9.04649 | -65.72065 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89fa915c-1c01-3ae5-9345-bcf2864d18ec | -8.99556 | -63.63643 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e81127ab-a8fa-30bb-8379-3ba411929bbc | -8.91118 | -62.44925 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ef46d8e-02a8-3a32-9f96-ed9914bd2d02 | -9.15908 | -59.45902 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 969b9cf0-bada-32b2-95f8-9c16b2e16591 | -9.99581 | -59.61864 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4af5345-a929-35bb-a968-3d903b1ebb72 | -8.89846 | -62.42142 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14c8dc9f-3bd0-3f5b-a5ff-936f2a296409 | -9.16533 | -59.46379 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de38c7fe-4676-3847-9506-7048d6fae058 | -9.47659 | -63.13614 | 2025-08-24 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 54980929-6030-310c-8596-f13157cf9bb3 | -9.13266 | -60.77713 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af999bd0-b164-39ad-85f9-32ae73918c1a | -9.01325 | -65.70462 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 21f0184e-6b1e-3392-94b0-fc5277f3539a | -11.32117 | -47.85928 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 75e6bc5a-0cec-322e-b3d5-c6d16c5dc7b4 | -11.52316 | -50.4914 | 2025-08-24 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f3ada1e-eda0-3ac6-9c04-7e8d04d4c6a0 | -8.59875 | -63.29266 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e08a5e0-acb3-3dfc-9230-a3e15d1de12c | -8.87844 | -62.42598 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67afb30f-963e-35ab-8a3c-539eea47be29 | -9.9506 | -60.18765 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33c59a13-1674-33ac-8190-96bfdae20d73 | -9.82006 | -64.26487 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15c8e40e-5f32-3245-8282-d35836a3c8f8 | -9.15533 | -59.59804 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5502c4e4-5cb2-3bce-b6fb-7e7305e0231e | -8.86745 | -63.04179 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9008676a-7066-33d9-a3e7-b1b264c069ca | -9.14838 | -59.50658 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92fa406d-07d7-3b21-9f4d-08a23ef91fab | -9.96178 | -60.18201 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c6dd8a12-b07d-3b87-8547-ea36f61ee6bb | -11.53807 | -51.8555 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 241157cb-ae1a-3f51-86ec-b29caf88f8ec | -9.02573 | -65.70177 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a6c29c73-769e-3c2e-892c-725ad566c2a9 | -11.53199 | -51.85867 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 07e3bac5-dc6b-39e6-b9f3-56fb40c22e5a | -9.52521 | -60.52235 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84df6543-3917-3335-adac-f51d0b84cb1a | -8.91246 | -62.42001 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6f09e07-5706-3d05-8d73-a05d5c424db0 | -9.01661 | -65.68512 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README82.md)
