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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfac179a-c2fd-3e36-a9b1-8ca1b97075b0 | -4.66526 | -43.14239 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c68e1548-c4f8-3476-b4d1-b35756c04107 | -6.1476 | -41.77054 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 451ab512-8def-34cf-a741-2667891cdb5e | -3.775 | -49.13944 | 2025-10-14 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| accfee4b-cfb9-3340-89b4-8a34f8187364 | -6.22587 | -41.56016 | 2025-10-14 04:23:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fab53b17-944d-32d5-8de0-fb2710cf3d25 | -6.32848 | -44.01238 | 2025-10-14 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceae217e-62dd-3961-8efa-4e9f98d78410 | -5.17487 | -42.90771 | 2025-10-14 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1de744db-057b-3ab8-97bb-b763c499eaad | -3.12855 | -50.20911 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a6542e4-fd1a-3562-982e-9f4a4755327a | 0.39026 | -51.04753 | 2025-10-14 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d349870-b92b-3bba-b6ca-20d9589ce380 | -4.8215 | -43.20566 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad040a71-7249-3d95-a453-fd1d333f9721 | -2.0682 | -52.00368 | 2025-10-14 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aabe5c2c-df36-3348-ab83-971fb7e4304d | -5.40197 | -40.88509 | 2025-10-14 04:23:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c49e586a-8166-357c-a43d-9488a7a36378 | -4.59773 | -46.34304 | 2025-10-14 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9a7c3a6c-e4be-384c-bdd7-ae5a86add2bc | -3.12455 | -50.20852 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20a5e13c-7a19-3825-853a-979bb09d9b02 | -5.57054 | -48.66825 | 2025-10-14 04:23:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ba67228-c930-36f6-8b2f-e7d09342d6bf | -4.05509 | -47.25448 | 2025-10-14 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76f2115b-72a7-3e02-b316-ce1f1986113d | -3.56581 | -43.50777 | 2025-10-14 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 723b2be3-67ee-3f64-a006-5ef745a7d2f3 | -3.09683 | -47.01949 | 2025-10-14 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2278149-ea13-3227-88ad-01e4051be851 | -3.22416 | -48.9298 | 2025-10-14 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30c2cec4-01cb-3096-ac41-32a4b745fead | -4.10742 | -50.04939 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a3b436c-e52a-372e-a0e3-eba78b966dd3 | -2.84523 | -45.45795 | 2025-10-14 04:23:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62a7fc3c-216a-301f-b87e-b8863754b1a6 | -4.66763 | -43.12681 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1783fbd0-e22a-3d65-9579-be117ad2873e | -5.25816 | -43.21304 | 2025-10-14 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73ae8f97-ce6a-3fb4-97f5-8169fd8262d4 | -6.53569 | -43.56483 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53d482ff-d06a-3c10-9363-eab9807290b2 | -3.61254 | -48.91535 | 2025-10-14 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f97f963d-9174-3979-8bc4-5a0f433a1d83 | -4.84082 | -42.77371 | 2025-10-14 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3df40aa8-e431-3561-8d52-e4ff7af0fd93 | -5.96741 | -42.29905 | 2025-10-14 04:23:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67342332-d181-301a-bba8-3b1caef8d2da | -5.67375 | -45.16344 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17c20f8a-2fab-3f01-9c35-8485928c7abb | -2.72739 | -48.35885 | 2025-10-14 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3fda609-76a0-376d-830e-61e2c28d371d | -4.28361 | -48.58492 | 2025-10-14 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f942ff1c-f230-3c65-9766-8daa439f6d55 | -7.40041 | -39.79221 | 2025-10-14 04:23:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 29.7 |
| fc87ef16-b01d-3dd1-bf5f-520d5cc560cb | -5.1086 | -43.19878 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 74f953a0-311f-33f4-b201-a638590a5a29 | -6.2973 | -42.99616 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bc1aea5-39c7-3db9-a114-c389c39bfe37 | -5.498 | -43.06553 | 2025-10-14 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 180a9bb2-a633-3ca7-9123-820edf8598fd | -4.42779 | -47.59915 | 2025-10-14 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f0c4aeb-a858-34d4-bd2b-6a1f4e785d6e | -4.00238 | -44.66702 | 2025-10-14 04:23:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cc7cc5e-e1cb-37d2-b50d-c7a594a95700 | -5.74604 | -47.47179 | 2025-10-14 04:23:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7525a68-cbe5-3497-8c52-362fd16a05ee | -3.54107 | -49.43824 | 2025-10-14 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c8281a6-828d-3f49-b368-b383b78b3be4 | -3.09888 | -51.29562 | 2025-10-14 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67cf2fe6-5d51-3619-aa08-80d9dcf6a9d1 | -5.3062 | -42.90215 | 2025-10-14 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e6d36a10-e3b2-3cf6-b0d0-0b4aa8a0a865 | -6.14257 | -41.76286 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d3d2621e-bde0-3b58-b630-bc01520f2b39 | 0.39519 | -51.03016 | 2025-10-14 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dfcf109-57e4-3f2a-ac1b-b9412b0a98b5 | -5.56803 | -41.32227 | 2025-10-14 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7c8d3a6a-714a-30ba-94d8-ad5a8bca1b83 | -3.14054 | -50.21095 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ab387f2-623b-349f-ae6b-8183ba9657e5 | -3.20971 | -49.23275 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a314d9e-439a-38b5-a201-96835f268b46 | -3.09663 | -50.37931 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ce9bb08-9669-3708-82e5-58df26369839 | -6.43928 | -41.81838 | 2025-10-14 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 61bc26a0-576c-3a0f-a767-539cf8c0d248 | -4.61428 | -49.54213 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| baddd15c-1fcd-3c88-bf6b-302cf3b6be2c | -6.14882 | -41.77335 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f482b95-87eb-3d94-bbfb-3c5d578c9ae8 | -6.6501 | -43.54943 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75ba0fd4-7b4f-3337-a65f-a6930bf0c1ec | -4.42436 | -47.59864 | 2025-10-14 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a73085c-e77b-3693-9802-a8124ae725f3 | -5.20719 | -41.65136 | 2025-10-14 04:23:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b658b16c-5a33-3f0f-886c-cd596ec3bea1 | -6.15728 | -41.76936 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 16d16847-8f97-328c-838a-cedfc874f1a6 | -4.72715 | -45.37342 | 2025-10-14 04:23:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6c28874-8fb9-332e-9e47-c74dc3016dd7 | -4.42381 | -47.75594 | 2025-10-14 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f2ac959-1fda-3693-9bae-ee2a1c2de339 | -5.26167 | -43.21358 | 2025-10-14 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 162b274e-ea5b-3316-80d5-b850686c7c0c | -5.87004 | -42.88156 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89fc7b98-e7a2-3418-a6a0-dfec3c648886 | -6.33075 | -44.02042 | 2025-10-14 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f34a7634-eff9-327f-a5f2-92acf1418cb2 | -5.01576 | -46.77077 | 2025-10-14 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 351c4b1e-fb4f-3ee0-8a5f-8174ca9a3e67 | -6.14957 | -41.76842 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f47a7059-c821-3265-aa34-7d431242e575 | -5.79742 | -43.89128 | 2025-10-14 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f677bcd-7850-303b-9590-70cfc941268f | -6.30382 | -46.93964 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f92f9620-e3a7-3b45-b9c8-934c47a49982 | -5.2065 | -41.65601 | 2025-10-14 04:23:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59786150-bb06-3767-af0a-ab9264765b78 | -6.67993 | -43.56589 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e1325af9-8138-3982-b57d-774eb893261e | -5.98904 | -42.87187 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 65d8ffdf-1d02-3366-855f-3b5bb67a0379 | -5.49268 | -44.63082 | 2025-10-14 04:23:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caf32b16-7d79-36a8-acbf-524cb93ebb2e | -4.66876 | -43.14292 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d01cfeac-5cbf-3bc8-8f0a-66f3f0b0022b | -2.80624 | -44.73655 | 2025-10-14 04:23:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 922ed7c5-19bd-3016-87ed-2dec959a0cd0 | -3.12399 | -50.21196 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94dbbab8-35e6-351d-9468-5475cfe9d35f | -5.59706 | -42.56923 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9b816cc6-d885-3a25-b453-b733649110d2 | -3.35125 | -43.513 | 2025-10-14 04:23:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ef0d1a8-cadc-3773-87e0-8ce8d8939a52 | -5.47259 | -44.64951 | 2025-10-14 04:23:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cc78e8b-51c8-340e-be22-2e285e3e085f | -6.40077 | -46.24242 | 2025-10-14 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f3fcad6-3674-31fa-9a76-df5e565b76de | -3.93536 | -42.8075 | 2025-10-14 04:23:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ff314d9c-0521-34f1-95a6-eb2f4afe46ca | -3.09605 | -50.38288 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 08f7415a-096c-3a7c-8227-9784562d4f2a | -6.95494 | -42.04132 | 2025-10-14 04:23:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5533a10c-481b-3121-8c6e-4c81ffb85c21 | -6.45693 | -44.58431 | 2025-10-14 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1437f137-59ae-39de-b58b-995c079b085a | -8.08865 | -55.18188 | 2025-10-14 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11d350cb-68ab-34ec-adeb-cb6ca6141bdc | -7.89857 | -45.00431 | 2025-10-14 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| e6f7c3e8-0ff5-3b35-b41d-2631414d2e67 | -13.5377 | -43.00563 | 2025-10-14 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c6f7acb8-583d-3a81-b992-b74a97ae4214 | -12.8641 | -50.64194 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db2bb362-fbcb-382b-bcdf-1160c3943298 | -7.90988 | -47.20395 | 2025-10-14 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a69f1f17-027b-3340-8f24-e2785e5f905f | -13.5372 | -43.0065 | 2025-10-14 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 1e6015f2-29e5-38b7-a9ed-b89e6731822c | -7.38705 | -44.07239 | 2025-10-14 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02098521-cabe-335c-995d-3f9356343a9b | -10.74081 | -47.8605 | 2025-10-14 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b666ad61-7b9e-3fb4-9917-55673e114d55 | -12.84836 | -50.64779 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07be99eb-99be-372c-86a1-f85a69d8f36f | -7.20607 | -45.48494 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8fdc9d1d-8bcd-35a2-a7e6-8f0ec2ddecdf | -12.84907 | -50.64359 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6eb7c4f-6cc3-3137-bd2f-8b2c510aa109 | -8.4362 | -46.23953 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81201ed4-45a5-35cc-a575-125eaf0ac565 | -13.84399 | -42.39058 | 2025-10-14 04:25:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 64ac0082-3b87-3084-bbcc-b4235501b37a | -12.74256 | -50.65218 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8128f0a-cb19-3044-a31b-42a9ec62d9ed | -11.31277 | -53.95299 | 2025-10-14 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f480899-daa9-3472-adda-8c65bb48a075 | -8.44379 | -46.1695 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1fe7eb05-70d1-3787-a98f-4a5f37b430be | -6.91284 | -45.0353 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0287be27-f821-3d5a-8495-c0a01501c0d7 | -8.4411 | -46.20826 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4388db78-8a17-30b0-9eb6-b7e10b4da279 | -7.15152 | -42.51311 | 2025-10-14 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5cda3689-9174-34f6-a8f8-053e35d2c27a | -7.60711 | -43.98261 | 2025-10-14 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 334bca07-a4c4-335a-9f2f-15889495bfd3 | -10.82012 | -43.99794 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b177fbd-244e-3a85-9d0e-8e458aafd8e8 | -7.75726 | -44.73762 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b96fec8a-425b-34f1-ac33-94412abe3328 | -7.45158 | -45.95533 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69171c75-8876-3319-99e1-d78aec4576b3 | -10.20559 | -48.07967 | 2025-10-14 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README30.md)
