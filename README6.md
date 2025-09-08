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
| 0b48eaa4-f1b3-3865-b191-98275e21af8a | -5.7013 | -43.8969 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64bc9d45-d348-3cf1-9d0a-312fc66b9e78 | -9.701 | -43.9855 | 2025-09-08 00:25:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f4b45e69-e3bd-3947-93e5-5d40307d2d88 | -11.4093 | -43.657799 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20c9c7e2-30f0-3cc7-a8c6-5a1f935c1d6d | -6.6035 | -53.3722 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67a0369c-9411-37a0-aa8f-7cf01727e86d | -18.014099 | -47.119801 | 2025-09-08 00:25:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e74070a0-a948-31db-9733-276968e2f0a1 | -10.2683 | -48.798901 | 2025-09-08 00:25:00 | METOP-C | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b48830b-8507-3fe5-9308-97f98ad39d44 | -14.4618 | -48.7934 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cf9cc4f9-4e47-38a3-b8da-0b92262502d0 | -3.6431 | -43.649502 | 2025-09-08 00:25:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6807033-15c5-3943-911f-0a0482152bed | -5.4391 | -42.8046 | 2025-09-08 00:25:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 34f0200d-d49f-3f02-a75b-f19b2d1f1453 | -6.5925 | -44.005699 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b7b2349-d283-3152-bce0-6a3ccb5830fc | -4.7865 | -43.552601 | 2025-09-08 00:25:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a06afb56-4ad1-3a43-b8e0-bdccfb32bdbc | -9.1572 | -46.068699 | 2025-09-08 00:25:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b76b5a4-e81a-360b-896b-b3d646d79f51 | -6.4686 | -44.004799 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46b4dd3d-0f4f-3114-a23f-08aa712f630a | -15.2803 | -43.3853 | 2025-09-08 00:25:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 8d2a339c-71e3-351e-867d-a5a2c7b2a2e1 | -9.6872 | -43.515202 | 2025-09-08 00:25:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5518ee04-0445-3b3d-b332-fd1e7bb6bb01 | -7.3738 | -43.9953 | 2025-09-08 00:25:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7a99c944-7a19-350b-a3ca-39430b9ccc4c | -11.5979 | -47.1581 | 2025-09-08 00:25:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63577037-033d-3e97-9165-3d064da3064e | -17.5152 | -43.748501 | 2025-09-08 00:25:00 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5771d9c6-e6ff-3ee3-97b3-089c273620f3 | -14.971 | -48.0308 | 2025-09-08 00:25:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9140aa2f-954a-3158-80d4-72fd47225ee5 | -5.7286 | -45.4175 | 2025-09-08 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b7017fb-454a-3a9d-8067-e51e28094965 | -5.6549 | -45.4561 | 2025-09-08 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d325baa1-3ca1-38f7-ae7f-37345d293891 | -13.8216 | -46.301102 | 2025-09-08 00:25:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cdddbd48-36e0-3a07-b9c6-cba5b0a7d2f5 | -14.2778 | -44.875999 | 2025-09-08 00:25:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 263da03a-1eda-30b0-9948-e5079a8b8681 | -20.615299 | -42.493198 | 2025-09-08 00:25:00 | METOP-C | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 876640d2-73c4-3a0b-a8ac-015a7d549878 | -16.269199 | -45.678398 | 2025-09-08 00:25:00 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e801b39e-390c-30a9-8754-d59a63efac2a | -6.9579 | -45.5704 | 2025-09-08 00:25:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0385ef2f-bb12-3040-ae8b-49b383085ec9 | -12.7976 | -48.010101 | 2025-09-08 00:25:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d562af8-b501-33eb-83c4-13e72729434d | -12.9085 | -54.770302 | 2025-09-08 00:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf91d25a-d53d-32dd-9c04-911536a0b429 | -19.486099 | -47.8834 | 2025-09-08 00:25:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a836aebc-111d-3c9c-bc41-98016fd72837 | -11.3552 | -50.4142 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 446d892e-3843-3d22-a215-5cf7788c42d3 | -19.178499 | -42.066601 | 2025-09-08 00:25:00 | METOP-C | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 775ab948-2509-3178-8730-d5777a17641c | -7.6401 | -47.948399 | 2025-09-08 00:25:00 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 306fc7ab-04cb-3019-a0f9-f0ddafb764c4 | -7.5613 | -44.003502 | 2025-09-08 00:25:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 456ac887-457e-3e17-8542-6f9c3d7bb4ee | -5.413 | -42.8256 | 2025-09-08 00:25:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d183323d-3c0e-3757-8759-eda89bdfed59 | -6.5454 | -42.948002 | 2025-09-08 00:25:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e52148d0-ae90-3fa8-bba1-44ed7b3157e3 | -6.1769 | -43.5872 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 821cd292-4c3b-3aea-9586-eda04b75d9b5 | -6.6023 | -44.003502 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 264fff9d-6dc7-3b30-8077-ca324761e23e | -8.5982 | -40.2062 | 2025-09-08 00:25:00 | METOP-C | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 40eae304-cebf-350b-b0a3-51ab651fd4a9 | -15.0734 | -48.1366 | 2025-09-08 00:25:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e04aaca7-592c-3222-bfef-10e5ed0ba5da | -11.3557 | -50.3666 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 439bd89a-9a4d-369e-b89c-8b9c85681013 | -5.5896 | -48.0965 | 2025-09-08 00:25:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 12134476-a9ff-3b50-a88f-ca2698d9ce96 | -5.8488 | -44.180302 | 2025-09-08 00:25:00 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 986cb71f-6553-39ba-aa97-bc4d7107270e | -7.4138 | -49.261002 | 2025-09-08 00:25:00 | METOP-C | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 29efdb90-896d-3fdc-97c7-ecf98192dba5 | -6.8583 | -45.5396 | 2025-09-08 00:25:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b710975-0340-3fb1-b750-9e0d1e143ec4 | -7.0032 | -44.949501 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1c2b0c3-2bc7-3e4e-8bdb-10b067a7321d | -11.3582 | -50.429501 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ede1c68b-886d-3e42-9732-cb80795db3be | -9.1687 | -46.074501 | 2025-09-08 00:25:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11f56338-64ff-39b5-8057-2e42082eccc7 | -9.1698 | -46.0331 | 2025-09-08 00:25:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cda9354f-07be-3549-8db2-b928227e7474 | -6.2068 | -42.599499 | 2025-09-08 00:25:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5616dadc-26de-3264-81d0-96bc30e23af3 | -6.1547 | -44.255299 | 2025-09-08 00:25:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 696def34-c7fd-3a05-8024-727dd9c3c954 | -6.4478 | -43.959099 | 2025-09-08 00:25:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f39c561-24ea-39eb-a1bf-258164e72d55 | -13.0806 | -42.340698 | 2025-09-08 00:25:00 | METOP-C | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c157973e-bfb6-3271-b451-80a4aa1e4053 | -16.322599 | -45.047001 | 2025-09-08 00:25:00 | METOP-C | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 31979af2-3dae-3a82-85fa-9d95cf323233 | -14.4494 | -48.782101 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bbbd307b-102c-34a3-82e9-6622cdb9675c | -6.1928 | -43.387501 | 2025-09-08 00:25:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fcb8c2c-0bc2-3976-af43-98ca2b98aa87 | -15.1323 | -47.972599 | 2025-09-08 00:25:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d0c77592-2b85-3cb5-aaa6-71d88da132ef | -17.650101 | -44.194801 | 2025-09-08 00:25:00 | METOP-C | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d8c9bca1-84bc-381b-b0b4-80e2d4462835 | -15.735 | -53.535301 | 2025-09-08 00:25:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 073a2691-9342-371c-ae99-672ebb94b352 | -7.6701 | -44.800701 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c6827a26-5c38-3ef3-91d8-ee58b875abbb | -8.608 | -40.203899 | 2025-09-08 00:25:00 | METOP-C | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| dd8330c4-87ff-3c42-abe5-c3714484030a | -6.0486 | -43.120098 | 2025-09-08 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 726eb30a-7f81-3565-80d2-ca432d4824d6 | -13.0822 | -42.347698 | 2025-09-08 00:25:00 | METOP-C | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cc060fed-0e67-3a77-9ab6-1510e2e56141 | -13.8119 | -43.864399 | 2025-09-08 00:25:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea006607-081f-3e9a-aecb-93d651309f7d | -5.4319 | -43.443199 | 2025-09-08 00:25:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9ebd0b7-f1c7-3b04-ad40-48307911c5e2 | -15.1714 | -47.9646 | 2025-09-08 00:25:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 47b09dad-0e2d-38a0-b93b-e6a9895813fb | -6.1531 | -44.248501 | 2025-09-08 00:25:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d02d9c9-7b39-3b32-82f2-3415b66706c4 | -13.8135 | -43.8717 | 2025-09-08 00:25:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e86e813b-5c58-33f7-aa25-f52a4a2b1421 | -9.98 | -51.630901 | 2025-09-08 00:25:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7607928-3f33-3924-b0b7-a6cd99ef8df1 | -6.2543 | -43.700001 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17d04f16-13bb-3cc5-b264-060d1653b2d5 | -5.7191 | -45.375401 | 2025-09-08 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0081d809-d59e-3da4-bfeb-2bc075db4cda | -6.5729 | -44.010101 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a075ce7-bf17-3381-a34b-538fa1b432d5 | -3.3208 | -44.086102 | 2025-09-08 00:25:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0eb7ca57-0fb2-3599-9a52-f8d898bcc0b7 | -14.4982 | -48.772202 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bdf2ea3c-11e9-351a-8564-d736d002b743 | -9.9641 | -51.6525 | 2025-09-08 00:25:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa1ca59b-f104-3a2d-91d4-610e550760c8 | -11.3264 | -50.372501 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c161a14-a4f7-3392-a658-1bc2717b4325 | -2.7688 | -49.624001 | 2025-09-08 00:25:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74d40a3c-1443-34b0-b6a9-92c28cfa67ca | -11.2568 | -46.472599 | 2025-09-08 00:25:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cce5f260-8f36-36ea-b1a9-597ce84bfc13 | -5.8354 | -43.8522 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7a03b50-30b3-38f4-8d49-abe5be78bf87 | -6.1759 | -42.644199 | 2025-09-08 00:25:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f7851f4e-41d4-3381-980d-7d499f2d4fee | -7.0193 | -43.258202 | 2025-09-08 00:25:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 35fedac8-74f3-3417-887f-ec51a2fb19c8 | -6.2097 | -43.281601 | 2025-09-08 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8ebdde2-3de8-38d3-a303-d8e9af178cf5 | -11.6441 | -46.8936 | 2025-09-08 00:25:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3529fae-e37c-364d-8647-2e78b050f1dd | -6.8575 | -44.263 | 2025-09-08 00:25:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8f784f9-900b-31c4-85ee-24c32a07c416 | -5.7862 | -45.672199 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11d8130d-0aa1-3f63-9e93-8c1b21c54f64 | -14.2795 | -44.883999 | 2025-09-08 00:25:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 54657a79-d7e0-3499-b86c-bb77cf20b046 | -12.1526 | -43.9431 | 2025-09-08 00:25:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc2d26eb-71c3-3947-9864-ff95595de430 | -6.2427 | -42.576099 | 2025-09-08 00:25:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8094fcf4-3c06-376d-b549-e8fb17d1c320 | -7.6566 | -50.293598 | 2025-09-08 00:25:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2857d4f6-3e4e-3d9e-8c89-4f1dafb584c1 | -12.9181 | -54.768501 | 2025-09-08 00:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4819fc9e-985d-3f32-af7e-5312d31aa26e | -17.4755 | -39.9431 | 2025-09-08 00:25:00 | METOP-C | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f3c70ba6-334d-3d0c-9823-0e973484d236 | -11.5959 | -47.148602 | 2025-09-08 00:25:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 858265f2-2333-3daa-bcf7-844d65d463ce | -7.8126 | -45.433998 | 2025-09-08 00:25:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe934be2-5e37-3fb0-9985-d526c5aaa24d | -6.0731 | -43.7192 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d1839f8-e413-3440-908e-7ec71c8b8cbc | -14.4956 | -48.7589 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d2eb1e3-3f63-3a93-85d7-49a5d5af8637 | -10.7016 | -48.577599 | 2025-09-08 00:25:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dbfccf81-cf76-351d-904c-dc910fd72483 | -13.8121 | -46.255501 | 2025-09-08 00:25:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 16820dbf-6613-3e7c-ac91-97755db1fe4a | -6.1996 | -43.5966 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d88fe31-04c2-32e6-a545-b5b216bd1d0b | -5.8719 | -43.966499 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b56f398-1c15-3d37-b834-b19ff14f297f | -6.623 | -53.368198 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e804b722-61ed-355a-af69-1ec3818ffe02 | -5.5314 | -45.683998 | 2025-09-08 00:25:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
