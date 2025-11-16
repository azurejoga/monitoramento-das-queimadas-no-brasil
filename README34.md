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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fcf62bd-2b6f-36ee-a39e-f7b4961f92df | -8.63191 | -40.52937 | 2025-11-16 04:08:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bac3a26e-7196-333f-a9d9-8ca7c216248b | -9.7259 | -48.88471 | 2025-11-16 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c8537c0-72b3-3ea5-9750-59f33eeeee5c | -6.52907 | -39.65274 | 2025-11-16 04:08:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 44c731e0-2255-3f48-8fa4-4193ae60dc63 | -6.67279 | -42.04058 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 4034c63a-ee32-3aa0-8feb-fe1d5c34d0ab | -12.2146 | -43.68734 | 2025-11-16 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f188de3f-9598-338b-a6c7-ae731e4db6c2 | -7.15182 | -41.78354 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 006f2bae-0d70-3720-a9b2-86ae1099748e | -11.46585 | -48.16483 | 2025-11-16 04:08:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44479bfc-5b61-3ad3-ad92-894439b6325c | -6.82298 | -39.81428 | 2025-11-16 04:08:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 37085a78-072a-318d-a4f6-dbbadb485a90 | -5.68939 | -45.99134 | 2025-11-16 04:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed8a7c3d-1aa3-3902-a953-ab4ee02e094d | -10.62387 | -44.5924 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5921339-169e-3aca-a4fe-ff4ee54b22f8 | -11.81348 | -45.5461 | 2025-11-16 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2448658-9f15-3202-97c4-c49ccfa53c8e | -12.38551 | -48.09779 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 971fe972-658d-36ba-b7e0-f6fec878fc59 | -8.56953 | -46.05008 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e809213c-d303-365c-8341-10944f7f17f5 | -10.71783 | -45.02529 | 2025-11-16 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0d05108-513d-3274-96e4-0551eb9fbd0a | -4.49723 | -50.79829 | 2025-11-16 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de60ef73-3a99-3f23-941f-2a6e5875273c | -7.18391 | -39.69784 | 2025-11-16 04:08:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 499c2dc1-8ce9-3823-b43b-a2ca1828bdb6 | -10.66833 | -49.36579 | 2025-11-16 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 65081976-2b94-3f58-9ba0-c0bddc869127 | -8.57932 | -46.06107 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36bf648a-70e0-3799-8b2c-9f435ca61dab | -10.14412 | -42.13321 | 2025-11-16 04:08:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9278f72a-ac47-30b9-bb27-431f674bcd52 | -9.73036 | -43.96087 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| accc9b41-2091-3d31-adb3-a64421761951 | -10.11853 | -43.90798 | 2025-11-16 04:08:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42d0efd3-ac4a-3165-aa04-38f5417a09b7 | -5.77246 | -44.38451 | 2025-11-16 04:08:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 407f4a3a-882d-30da-b1a5-85d038647462 | -10.62324 | -44.59619 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fff062e0-e6c5-30c7-9dec-664636812e6e | -7.33824 | -43.34769 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfc930e9-d194-37c3-82ef-dae111e85e97 | -10.16955 | -44.51979 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38d00b54-bd59-356a-8664-7b8a4b305265 | -5.28598 | -44.87851 | 2025-11-16 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad782575-2808-3cb8-8b72-05f81990d0b5 | -6.39563 | -42.28862 | 2025-11-16 04:08:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eb2c3067-c214-31a7-b197-f009ce82c518 | -6.77767 | -43.54152 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53c56efe-64c7-3819-adcc-5b31ea6987a1 | -10.84587 | -44.09758 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24d308e0-3706-356b-9a38-ab8388874378 | -11.97094 | -44.96345 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0a57aa90-1774-3a97-9919-b99b36e03e26 | -8.57984 | -48.74757 | 2025-11-16 04:08:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e2a2965-bd56-3465-a73e-dedc043e100c | -10.80224 | -47.9968 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46934650-a7d5-33a7-b353-96ff46b4e969 | -9.50908 | -47.27632 | 2025-11-16 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30d0a563-b479-3762-ba45-b47d9cd0a7c4 | -9.15105 | -47.12556 | 2025-11-16 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec3c5267-79ff-320d-bff2-a13875dc225f | -6.41401 | -41.46412 | 2025-11-16 04:08:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 72b5ef04-a3eb-3983-8212-5ff526b3cc43 | -8.31452 | -45.40224 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c05823ec-86d2-36d6-a91d-887f879866d7 | -11.96598 | -44.95042 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bff104bd-fb8a-3252-abbb-6e313335970d | -7.11032 | -42.73069 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 46f47df0-5fee-36d3-8920-3331e1ae29ef | -9.60668 | -46.7439 | 2025-11-16 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc5fbb51-dd4c-3e9f-bc63-b7bf4d0dd988 | -10.61933 | -44.58123 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a8fc7a8-a4b5-34d6-a6ea-14d1de88fff4 | -12.39552 | -47.57898 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cac4e5a-187d-3b6c-b9eb-ff1c4e4757d7 | -9.73772 | -43.95834 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d2072de-b274-3915-b61a-c2a4fa78c618 | -7.10031 | -42.72908 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c644d472-c1d3-3f53-baf4-b791c6725255 | -7.71425 | -47.29311 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8012cffb-ed78-37bf-9849-cf2a9dd69cbf | -9.83897 | -44.17994 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ed49c93-564d-3349-ad0c-b643f0e202ec | -8.03345 | -41.05745 | 2025-11-16 04:08:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 68f5c376-2bfe-3354-9352-10a4404e0c3e | -9.72976 | -43.96455 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| abd51887-33c1-3895-8329-afc8b0649770 | -7.21839 | -38.77551 | 2025-11-16 04:08:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 41e55fab-f6e2-312a-9e19-21da21debbe3 | -6.67224 | -42.04406 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f4ef8cff-2540-3b42-a433-ddc004afc070 | -9.74111 | -43.9589 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a0b9d087-ebfd-3329-b4eb-4929c24e93e0 | -8.72894 | -44.10148 | 2025-11-16 04:08:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4ba3280-d2b8-3d4b-b0bb-7dc53c69684b | -7.08161 | -41.58465 | 2025-11-16 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3747e496-8e91-3627-b7d5-69cc04985456 | -10.53397 | -47.92419 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f292169-eff4-3278-bcbf-7681676ca93f | -6.67747 | -40.80285 | 2025-11-16 04:08:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d5f29723-ff74-3054-bc9d-420d0e811550 | -5.77604 | -44.38508 | 2025-11-16 04:08:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d10221ed-a064-31e1-a847-f1f17d8aa6f4 | -10.76998 | -43.98008 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80c9a63d-cb3b-3318-9343-b2ad79597db6 | -9.05725 | -44.75846 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fda9bc9c-6ec7-3260-aa17-64a40364a0a3 | -10.13933 | -48.11798 | 2025-11-16 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59f701b7-c53d-32d8-bb81-ff05deeafd2d | -9.57539 | -44.60884 | 2025-11-16 04:08:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f3d83be-8535-323f-9450-adbe597a34c8 | -6.46063 | -42.32746 | 2025-11-16 04:08:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9ec9dd60-539c-3225-bde4-f48fe0fc0137 | -6.3077 | -41.83649 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| deacdbe2-0f6b-309c-a1d9-9b0fae867079 | -6.582 | -44.67225 | 2025-11-16 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e5e8eb7-faaa-326e-a285-cf83d298b78d | -7.05516 | -42.24403 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9665d40-862e-32a2-932f-2db6a4a390c2 | -6.97072 | -41.53138 | 2025-11-16 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 56a6830e-e0a5-3ea1-91a7-f58dd72114e0 | -7.70948 | -47.2961 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 081bc8be-7d7b-38c0-8344-5866c747efe4 | -8.31818 | -45.40281 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52889b0b-aec4-3268-96c4-539c3188ea1d | -10.54271 | -47.99557 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a339ff81-7e42-33ca-b43a-8bc470125c80 | -7.22132 | -47.98044 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6400f140-4130-31a3-9f96-1f833c577118 | -12.67668 | -46.77915 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1810ebf7-207d-3f8a-8d8e-0ff8bad8f7ec | -7.01522 | -45.16756 | 2025-11-16 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e48f704-bc72-3d27-af73-29fb36197dc4 | -9.34646 | -46.59737 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 50728688-357c-3aa3-979d-878dd937a751 | -11.85253 | -47.59941 | 2025-11-16 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ba10ec0-0e69-3a2c-9b9a-d2b8de45d532 | -6.08072 | -41.61658 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c7400315-33e7-3504-b0cf-4b01988166b0 | -6.07303 | -41.62244 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0769ecd6-8cad-38ac-9164-6106a4475261 | -6.87747 | -42.94862 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c744dfa3-687e-39cc-b105-64f67c4637e1 | -5.99346 | -41.911 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf0f2674-ae1d-3a52-899d-52ad098cb118 | -10.93518 | -44.02584 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc8b48fd-9e35-3ef6-9544-7247d000eef1 | -12.40882 | -48.60605 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0956d25-0f13-3041-9a83-4ab75a52a582 | -10.80758 | -47.99047 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64cd50a2-6240-3dc6-97af-19f1430ba6e7 | -9.67618 | -37.09629 | 2025-11-16 04:08:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e23e708-df2a-3b4f-9359-b2d655aa4e41 | -7.71835 | -47.29396 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3aafb3f4-e1f2-3755-b95d-23e2561e6a1c | -12.40237 | -47.56208 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e071e6fc-99b5-385a-bcfc-010ede9e8bac | -7.18535 | -39.43985 | 2025-11-16 04:08:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b62a66a4-2677-3429-bca3-2300ae11a9a1 | -10.70494 | -44.52826 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ade3805-da0a-3915-b018-1bc95a515980 | -6.55567 | -43.24176 | 2025-11-16 04:08:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e6ed0f5a-5f28-3947-b98c-23344fc82f8b | -10.62605 | -44.6005 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79f3d210-32eb-33e2-9ca7-0138481c4b31 | -6.51371 | -39.52467 | 2025-11-16 04:08:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 89c15a2a-7208-36ca-a71a-5fda9529198a | -10.32346 | -44.2852 | 2025-11-16 04:08:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e22e64a-b0fb-37dd-af81-156e2f239b86 | -9.0579 | -44.7545 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 321defdd-bd3a-371f-9915-0d133225307d | -6.52006 | -43.3979 | 2025-11-16 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2ba63250-dfda-3174-b648-2f71184dd02e | -7.33263 | -39.96346 | 2025-11-16 04:08:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| db740fcd-76a2-38ec-ac7a-1b9ca2412116 | -6.5746 | -47.90311 | 2025-11-16 04:08:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f78d096a-b488-3c72-8071-81da5636b1d7 | -12.44214 | -47.8917 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ea38d96-03c2-36c7-a186-22612d357821 | -12.19502 | -49.62101 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bff69d4-b8de-3787-a215-3816d0371f8b | -12.77452 | -43.71418 | 2025-11-16 04:08:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a0659667-9f1c-3cb6-8668-b01bdda9730d | -7.11254 | -42.73826 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a14ced16-2fe4-33b8-9b80-0bec1a0e044f | -9.83788 | -47.04265 | 2025-11-16 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a37b660-050b-36c9-b787-fb5aef176051 | -7.04927 | -45.94648 | 2025-11-16 04:08:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe3850cb-943e-3325-8d8d-754b1a807f6c | -7.39043 | -48.65011 | 2025-11-16 04:08:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a5a6b28-7cf4-35aa-8c8c-a68dddd6f66f | -9.05781 | -44.79933 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README35.md)
