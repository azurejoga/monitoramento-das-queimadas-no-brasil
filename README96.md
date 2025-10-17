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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3b4e9fe-741a-3d08-a07c-061dd2b76155 | -8.17842 | -47.03779 | 2025-10-17 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d82bd1fd-ce88-3dd8-9bd9-f596303e5216 | -8.38368 | -46.24628 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15355c65-03a4-3a6b-a9f1-f3364bfaee7d | -9.70213 | -44.56194 | 2025-10-17 04:51:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2812968f-531e-3bad-b7fc-99a219a5c36d | -10.35873 | -48.04989 | 2025-10-17 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9788274c-0fb1-3915-9dcb-8a48b0c48c3e | -9.1298 | -46.60934 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 249b2f17-4853-3469-be17-33e8a1aafd33 | -9.96804 | -50.50967 | 2025-10-17 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff9e1932-a58c-3b64-897b-ce84fe586827 | -9.01563 | -46.65734 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d8a0913-d7bb-3ce8-9d14-27bd3a240b11 | -10.64926 | -45.2998 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a5c569e-cc8d-3405-977b-18e138d89125 | -10.50626 | -43.39737 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e5844ff-eaac-357e-84c5-e1eec2808293 | -9.08402 | -48.03032 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97b98c9e-56f0-3f8a-9ab7-71e7c00d607c | -14.2413 | -54.8988 | 2025-10-17 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8cff9c48-71d4-34dd-b9d8-f938485de053 | -9.88948 | -47.67309 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ed246c6-b1cc-3be9-86e6-601cce51472b | -12.42027 | -51.30123 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8f4bdf25-1b5d-3aa3-8f91-dd09adfcf824 | -11.57952 | -48.56595 | 2025-10-17 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6befcf17-9c92-3daf-b6d4-a8f6560eef32 | -14.15556 | -44.31879 | 2025-10-17 04:51:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a534fb55-f113-3c1f-93c9-2590a6c2082b | -15.03003 | -48.76219 | 2025-10-17 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b551789f-d3c1-3587-bd86-176894ab5b81 | -14.34482 | -51.46122 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 2b921e8c-b228-3745-8203-ed778e26ddad | -8.09008 | -45.43989 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a55a04a-b812-3678-b868-4414217762ce | -8.33685 | -46.23151 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cbe82e12-9475-3e20-8f87-8ff262c2b2cc | -14.32166 | -51.47651 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 773a6d91-8ce8-3142-b5ac-2361a4661009 | -8.41809 | -44.73103 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2072934b-acd3-3fad-9e46-c3502469a0fb | -11.09385 | -45.87656 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9147d222-49f4-3d44-81f6-494b3e2c9066 | -8.56337 | -44.59074 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f20791ed-bd2c-344d-bbdd-dbfacda6a7e7 | -9.97747 | -47.01029 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1db15e1-4fb8-301b-a6e7-0d3a8ef5eadb | -11.46264 | -44.04101 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb96e5ed-0e31-3d7a-b0c5-ad2d9db73aee | -9.25455 | -45.25365 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 706fe0c7-33b4-3542-a090-0f60c69cf6fb | -9.08467 | -48.02585 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18ccadc2-b883-3ce1-879e-1aa5ade478de | -12.16889 | -45.06823 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 119c8cff-dabb-389f-bdf9-c5cca2a0f45e | -11.3557 | -45.26853 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c190729a-910b-30cd-ad9d-76dceaee43e3 | -12.78105 | -44.88047 | 2025-10-17 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88b619e4-a3bf-3c97-9c04-c76dd3c49826 | -8.09064 | -45.43588 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e165ec4-967b-3157-ad7b-c15dbf055c1f | -11.5728 | -44.05584 | 2025-10-17 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb2e85f6-cb93-363b-a609-47e72d4d158f | -13.04776 | -47.3148 | 2025-10-17 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54cbe5e3-bd07-3eb3-b47d-7fce9303bb30 | -11.46775 | -44.04104 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9477af0-e974-3e7f-bc90-62e1a11aa749 | -10.29032 | -44.03876 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 3332d07b-f68a-3bfb-bd78-f56cb6fe2301 | -10.01505 | -45.64077 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3947384-6f83-3842-a83c-1bd9386a01ab | -11.76017 | -51.15031 | 2025-10-17 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cd09582c-bd0a-30fa-a977-4eeb6045696f | -10.49818 | -43.4193 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3dd0beb-767c-39b9-99f8-47d0e3b6b407 | -10.13685 | -44.54465 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 03cf92b6-9e3b-3271-84d8-eb1174fb905c | -9.13176 | -46.62443 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 379aa820-4d2e-3e1d-a4ca-e45c1eeee807 | -8.41356 | -44.73018 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fc86689-3bd9-3431-94b8-801fc7eb1632 | -10.64295 | -45.30491 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0f11586-c21f-3ee6-b8b7-82eeaf2668cb | -12.77623 | -44.87983 | 2025-10-17 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb24d1b8-a9cd-3a41-a604-8954a56f0216 | -12.4933 | -45.48701 | 2025-10-17 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| edfbe1e5-a6c4-3a1b-a73a-f05c7c4b90e3 | -13.04366 | -47.3142 | 2025-10-17 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a7c6223-0736-35a8-84ec-c9dbb61d9b4d | -11.19437 | -51.75161 | 2025-10-17 04:51:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4c4f560-3e5a-3b93-b72a-9666c0899094 | -8.68173 | -47.0082 | 2025-10-17 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86492ffc-09e6-3c0f-8dab-9f2b841d274a | -8.58659 | -48.63174 | 2025-10-17 04:51:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d39d1223-d829-3a01-8444-9916eb0e5ad4 | -14.35387 | -51.47027 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 244c355f-cb31-39a3-8d8e-db5a96a42fb5 | -10.91904 | -47.87494 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 307c80f7-c235-3fa1-bd5c-0ccd067771b4 | -13.04608 | -47.31361 | 2025-10-17 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2fd4f1d4-946f-3af8-8b64-62605cf36859 | -8.40329 | -46.22669 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e17b3bd6-260c-3656-90ed-835e77ef2aa3 | -8.38207 | -46.31653 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 765c0906-8165-3b49-b62f-4adbd83c788a | -8.38157 | -46.32006 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 981b4fb6-af53-38a8-8c58-3bf59b2461e3 | -8.94347 | -45.24787 | 2025-10-17 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52040ba7-e022-3933-aa0e-403b5ca58118 | -14.02875 | -47.08092 | 2025-10-17 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e7fbe14-f92c-3f08-9b45-573d3e0cd675 | -10.26398 | -44.04015 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ee358e57-ea6b-3ef0-9e94-2c20d8de3e10 | -14.32333 | -51.44258 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e18de067-b7aa-3dac-8bc7-9444c0bec7ba | -10.95726 | -59.12279 | 2025-10-17 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a5d1f89-a56c-3a17-83c0-af716fde83a1 | -10.28613 | -44.03245 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 576e995a-b1d4-3140-8e49-2227eadc2dcb | -9.05371 | -46.99472 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 075d5406-60cc-3c58-a923-2f73e2be58eb | -10.50955 | -43.41248 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84df6a78-3e93-37a1-97a2-7c0de8173af5 | -12.54175 | -47.64982 | 2025-10-17 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd03d67b-8f85-3da0-ac5c-b5543e59e6b9 | -10.50541 | -43.44425 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 569c9e5e-8f1d-3d14-97eb-da9319e019ea | -9.06855 | -48.84813 | 2025-10-17 04:51:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6dbc4298-7d21-3c6b-b6b4-e16dececad60 | -14.32953 | -51.42454 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2522c5f-1971-3de8-beae-65caae02a960 | -14.93063 | -48.53209 | 2025-10-17 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eddd8d83-4257-32ae-814d-2690d8c6b742 | -8.08005 | -46.6669 | 2025-10-17 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db49074f-f411-35db-a106-641f6795adc3 | -8.39292 | -46.24045 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a31553a3-8df0-35ec-8fdb-6c9d786137b4 | -9.6213 | -49.12442 | 2025-10-17 04:51:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e4ac9de8-16f2-3f72-8703-836abe5586f4 | -8.07998 | -45.41755 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f479371f-9bd7-3e2a-ad3e-b7a7994ca47c | -11.97719 | -46.55236 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d36fa750-4d8d-3290-b515-994fe4f921e1 | -8.47487 | -44.18545 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c92e323-ace8-3937-8735-b9e12f162906 | -14.92575 | -46.71832 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34e19ee0-45df-3000-af4f-275db156dfda | -13.42213 | -48.58688 | 2025-10-17 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 936ffa12-7c68-3048-b307-18649e29b4bb | -10.98316 | -47.90628 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90c9acec-63a4-32cc-9d4e-1a53397126e0 | -12.45059 | -51.32836 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3efb5729-708e-3ae9-bbd7-1569e5465689 | -8.46123 | -44.17904 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7680f4e-3870-30ac-9880-310873902e9a | -12.31452 | -45.64053 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df65dc2e-c7e6-3ee8-9fbe-373e12423ee3 | -9.88113 | -47.67668 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2364a45-47a6-314c-92a8-0a85d6a9fad4 | -9.14133 | -46.64414 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 366ef5da-ab45-3c12-983a-9875625cdf77 | -8.4708 | -44.17982 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0ac4b6d-de16-3264-a2ef-aec55f777431 | -11.48197 | -44.20612 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a90a196e-eee8-3a53-8d74-f1dafdc0aa1d | -9.50058 | -47.26874 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a9d7243-cd95-38cc-9689-8da33b440451 | -11.57579 | -48.5654 | 2025-10-17 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dfd2d860-655c-31f5-a57f-57b0eac87b85 | -12.31515 | -45.63592 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74531632-92b7-3f5f-95f9-8e5035fdc9c3 | -12.31087 | -47.26061 | 2025-10-17 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5058c55b-1ebe-3a95-952d-4425eb6bee5a | -12.7797 | -44.89096 | 2025-10-17 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b3b32674-9371-315e-b62a-399415a146b3 | -8.08857 | -45.41931 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 956bbe5f-cb81-3aa6-bc45-3e1ee342d303 | -10.10543 | -44.62411 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 979a5ff6-3577-3904-8195-f5c90f62631e | -12.42364 | -51.30177 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73004395-34a7-3379-afbc-012e4d7ac741 | -14.17194 | -47.93654 | 2025-10-17 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c257659-9657-3689-83fa-9fe6a18955ac | -10.61681 | -42.30971 | 2025-10-17 04:51:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc717432-76de-3a6d-829e-e68e2d187a98 | -14.3318 | -51.43252 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d933d448-5797-3913-a9f0-9732d3c1b017 | -14.93012 | -46.71898 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b05db2bd-9892-36d6-ab3a-0237230ea8ef | -13.92417 | -45.62237 | 2025-10-17 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 318c329b-b9eb-39a6-896f-655dd4eb3e2e | -9.68925 | -48.94014 | 2025-10-17 04:51:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81bc5ee9-8627-385f-adcd-ad1c3f6c22dc | -13.92883 | -45.623 | 2025-10-17 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f63ac60-1b20-349d-9fb5-693a13cd3690 | -9.50911 | -47.26493 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f463ce6-c869-34c0-8a98-2d980e93a468 | -10.10384 | -44.57519 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README97.md)
