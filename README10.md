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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec6e60ab-ee15-3043-824f-608e2a6d029c | -7.00587 | -45.6414 | 2025-09-16 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21dfebd7-3fa0-3332-9eef-7f8f316db440 | -7.06557 | -44.15485 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b279bdf-a197-309b-88e3-cfff40630d74 | -10.7251 | -44.75519 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a126b1a0-e871-398d-b3c9-d25c528fa592 | -9.46262 | -40.37667 | 2025-09-16 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 22d9669a-14f5-3850-95b8-52abcb928c0c | -10.71911 | -46.51213 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a4db5fc-c7f2-319d-8cf1-e1dcd7622947 | -8.16338 | -42.48814 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8ed46ec0-9285-3792-8c5f-bb57a25b2288 | -5.95809 | -42.80268 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4c5423d6-28f7-3374-8149-efd0dbf5f45c | -6.63392 | -44.74211 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a037f795-f9a2-3d1e-99f1-e54497bfd0a9 | -8.00121 | -45.6688 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb782bbc-33b9-3cb0-8d19-fd9fcc0189c7 | -12.11707 | -44.83022 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc3819e3-59f7-3adf-a937-c020ca1cff5b | -7.99307 | -45.66743 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edfdbf57-03b9-3bfe-95a1-c783e6688f56 | -6.50992 | -41.819 | 2025-09-16 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8407f30d-4b75-30a0-86e4-595f36656ca1 | -11.69302 | -46.87621 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfedcd6e-3bf4-3d1c-9da5-95ad9114ad66 | -11.48597 | -43.59985 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9efdd606-a786-3dec-8860-0ba28490c83e | -9.64092 | -45.86748 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06119590-8556-3cc9-9ad6-cba3af83d722 | -7.1432 | -47.98177 | 2025-09-16 04:02:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d64f1143-eb01-3b1b-9243-d830011491bf | -11.7033 | -46.8905 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c293f5b2-fd4c-3f3f-84de-3002d7ce61f5 | -8.12256 | -48.27303 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a45d2d48-20ad-3ae8-833a-36ab97ecb961 | -7.9943 | -45.66024 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c455cc4a-91d3-3121-9bbc-47bd24119a86 | -10.72062 | -44.75926 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c2ea96b8-2775-3715-97e6-b47c91be5177 | -10.65117 | -46.46505 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7fe64d93-08b9-3804-9e80-e9e108eabd00 | -11.42343 | -43.53359 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 038aa24c-8076-3219-b15f-17ea646661f2 | -6.12788 | -42.94036 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 221748df-0660-3bc7-b032-be7aa1a8dbbd | -6.46634 | -46.00315 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b08d1726-b6e0-3d78-90b2-88eafa3941f2 | -6.87946 | -45.62037 | 2025-09-16 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe957e32-a9b1-32f7-a7d9-9d3952e5fe1f | -5.42205 | -43.19004 | 2025-09-16 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e4ca182-655e-38b4-a671-be03b56da9fa | -12.11923 | -44.83973 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ab4711a-1fb0-3146-9d38-a814e5067fb6 | -8.61071 | -46.40309 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f8a3e65-50c2-33d2-8c98-afc9b9f690bd | -8.97976 | -46.25708 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 73ae8440-ab3e-38f9-9762-d179a81b5147 | -10.17573 | -46.1446 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86e61296-20f3-35c3-ae41-d9b433a59834 | -9.09717 | -44.84312 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 91a8e2c0-37ae-3eff-93cd-60c0ac119612 | -12.17266 | -43.5739 | 2025-09-16 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3329d61f-11f5-3dbd-b282-f44b1c2aea6d | -6.16327 | -41.16972 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8d95729d-2e0a-3974-b0fe-e135a8fa4372 | -9.1023 | -44.85892 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| aa5e72a1-8763-3f26-bc92-baa401651ad1 | -6.5297 | -41.83321 | 2025-09-16 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ebbea5b5-4a6f-38ab-822b-5e564b6a0dee | -7.19264 | -48.60698 | 2025-09-16 04:02:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1454b209-48ff-3013-b9c0-473883231e73 | -5.79706 | -45.92555 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e2cee08-1ada-32a5-aa47-3bf75c7a81a0 | -8.70503 | -49.41651 | 2025-09-16 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06064aeb-6234-3f6f-b2b3-6827da05a7fb | -6.15465 | -43.66675 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff1e7684-66cd-3bd4-b394-4755beffb937 | -5.12049 | -46.13214 | 2025-09-16 04:02:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c24a795-77ab-36a8-8f19-05be5ab95be1 | -5.76969 | -43.92898 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43c347e9-47e2-3c5c-ae00-9f9bf17e2379 | -5.67094 | -43.31953 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3527c637-d1eb-3b20-9c7b-941caaa8cb36 | -7.42631 | -44.87059 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8daa7bf5-71ae-3023-8339-e6a5db61b78b | -6.19034 | -43.47179 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d126388d-ada2-3a5e-a7a5-9e83482f5e15 | -9.05689 | -44.85298 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a346440e-190b-38c2-8cf7-09bb9cbdc4dd | -10.13325 | -46.14627 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a3a012e-3a13-3edb-8cb2-e140a5db45fe | -8.91046 | -46.15216 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f411368-74b0-3e4c-9e70-0ca2edfc8ca0 | -10.72192 | -44.74362 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 18867bb7-322f-3608-a146-957199dc3e22 | -6.33329 | -43.33192 | 2025-09-16 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22862f2d-0654-3fc3-a819-8d3dc9a62993 | -8.90568 | -46.15517 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c757f06e-ca13-3408-8f2b-677580c41283 | -6.96666 | -44.53804 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d255e18-663f-3ac2-9e2b-b3698cdf57f8 | -5.81133 | -44.86419 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88e54fab-49a7-3988-b7fd-2aae9502b863 | -11.70215 | -46.87295 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 598957ea-d583-39ff-96d0-68e22c835020 | -5.81169 | -43.49075 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3587cd5-cfe6-3628-a4f2-025756b03ddc | -12.12366 | -44.8131 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 231a399a-4c63-3beb-8e64-57a99c0facc4 | -8.67103 | -46.38082 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9589ad0c-31f1-386c-ac64-e40d5a3a0378 | -11.12394 | -45.34871 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b3e6d7f6-a655-34ac-b8f4-8d58dfe21d0a | -6.25641 | -43.45903 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c518d849-133b-3d3e-9534-c04a27dc8aa6 | -9.42764 | -40.47095 | 2025-09-16 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1649b67-632e-3ecf-80d8-12943888c720 | -6.2559 | -43.4605 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd31e3b6-fe11-35ce-af36-0d6778dcba69 | -9.09715 | -46.93504 | 2025-09-16 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 406e3eb7-de41-3f5e-a6b7-30c7bd6e5ebd | -5.80473 | -45.69754 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 264142e8-915b-3a2d-b955-8ebb80b63f89 | -7.42939 | -44.87622 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74b3b90f-601d-33c7-ba73-3cb5cd652d18 | -10.78268 | -45.97543 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1f46101-42c0-3de3-b6fb-67cdd471d884 | -8.93492 | -45.51298 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2072d537-e3f3-3446-8c28-ad6e914ac0e4 | -9.05056 | -47.02162 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 60ece0a4-c419-3dca-b99b-c98725571749 | -8.96583 | -44.19865 | 2025-09-16 04:02:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3827eba0-ebc6-304b-9463-f5fcdadf1cf5 | -8.67171 | -46.37685 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5bb3f614-e7b6-3237-9898-ede02878a62a | -6.16127 | -45.11731 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 631c151d-534c-3a6f-88f2-e474c8b6a507 | -11.13558 | -45.32619 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5d5b402-3d8a-39dd-912f-0e7f9cb2a5c9 | -10.71547 | -44.74446 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 27ffe649-1e82-3793-b32f-ebb4d8b8c13e | -11.12692 | -45.35419 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dd1156fb-8b0d-308f-83b4-a8d1b7fb8ee5 | -7.30187 | -43.92709 | 2025-09-16 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c204490-c65d-3059-9d78-f04d61f4d218 | -6.24656 | -44.38203 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89b208e6-9156-3148-a96c-e97cc7c623e2 | -8.66748 | -46.37623 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a40bd55c-25a0-3fa1-8e05-7f6490f9f199 | -9.17913 | -47.06293 | 2025-09-16 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 866e4254-34d0-3e56-a103-d8b29986841e | -5.84055 | -44.15814 | 2025-09-16 04:02:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81091746-4d39-3258-929e-e2ff3267adb1 | -9.85596 | -43.12487 | 2025-09-16 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d40ea814-96ed-3a95-bc41-11ca1ef9d473 | -6.10106 | -44.92315 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c414436b-001d-3d89-80be-33ed19f84c26 | -5.34553 | -44.81582 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 482a38e9-158d-377b-8623-3cea1a3ce823 | -11.43082 | -46.92532 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 271107d7-508f-32aa-9bf1-29495e020eb4 | -5.77573 | -43.91582 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 16fe2b07-16dd-386a-8520-be15dd92dddb | -7.44137 | -45.83888 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf153758-9700-3a45-9c8c-17d2dbb38ba1 | -7.00998 | -45.64217 | 2025-09-16 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5cf12894-0e7f-302d-bf44-975da472e5bc | -11.71437 | -46.90051 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d822f2cd-8433-38ab-a069-2acaa6064d51 | -11.13615 | -45.34588 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9887bb49-edc6-3974-a07d-a9a302b08bfa | -9.73304 | -48.12232 | 2025-09-16 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9580bee6-3570-3d4f-809b-fde4489c8b3c | -11.11252 | -45.34679 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 92f09bdc-7ebe-314e-8a28-f08f4d4548c1 | -11.48316 | -43.59536 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a5a7a83-1995-36c9-b8f8-22f5bbbb64c4 | -11.42268 | -41.42032 | 2025-09-16 04:02:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bc8ea12b-560b-3dbb-8539-2d1fbf93961d | -5.98403 | -45.79384 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ef50a01-4303-37d4-89e2-459df9dbdf49 | -8.20192 | -45.54885 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 786a1a65-c4b5-3a0c-a0dc-9d1284b2af4f | -9.06805 | -47.02462 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7a2b3f62-5482-3609-95ff-ceb4497537ed | -5.67474 | -51.14146 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f575efaa-84d1-3a80-98fa-b947e1a2b4cb | -9.05008 | -44.84692 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9f967e11-447c-3122-8d94-2996a2179824 | -11.63906 | -46.59072 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5c94793-9ee4-3028-9b9a-82aaed99d13d | -10.18128 | -45.31451 | 2025-09-16 04:02:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa9a8186-a108-39fc-9b90-dbecc8cce593 | -6.16263 | -41.23882 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 53301925-1e9e-3f1e-95e4-847ca9676bf4 | -10.71349 | -46.49566 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 747e21df-6293-3197-9095-67df1228bfd9 | -7.69612 | -44.66194 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README11.md)
