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

## Dados Diários - Página 259

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27bb098e-06c2-33f0-88dc-e39b448f7789 | -11.88461 | -47.39501 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 53fa976b-cffb-3a5d-8637-1c6774277ccb | -12.302 | -47.06511 | 2026-10-09 15:58:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b0b453c7-1262-330b-ad29-33429f0daf12 | -14.44257 | -43.94104 | 2026-10-09 15:58:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 149.8 |
| ae950719-cfe0-3035-b373-01cced5ab384 | -11.58119 | -43.65494 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 4adc91a2-2b54-3cc4-8a12-49db1d502604 | -11.98166 | -43.45668 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 0f1ef744-b994-34db-a26b-17951e97db37 | -12.39535 | -44.7537 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d24e7e5-a9fb-3031-9b7c-b93d7f381253 | -16.52558 | -44.26048 | 2026-10-09 15:58:00 | NPP-375 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11eb0fe6-22d5-3536-bf5a-e7bbcef61d6f | -16.31246 | -41.31875 | 2026-10-09 15:58:00 | NPP-375 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d9e79fec-aa46-3b15-957f-7d15c50fe64f | -14.05389 | -43.83294 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| f01e887f-67d6-361b-adbd-e239004401cf | -11.95904 | -43.47137 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 968df8c8-bbac-3f60-b204-afcb83e71426 | -12.25229 | -44.75066 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| bf8ce8c3-204c-3224-9987-4fe744d3ea92 | -15.42741 | -43.30603 | 2026-10-09 15:58:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b2395b10-e52a-34ce-bf10-b79216340569 | -14.05276 | -44.81999 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b2c4ad61-a0e8-3bb5-ab39-7e4376653569 | -14.67035 | -41.79621 | 2026-10-09 15:58:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a925eecf-543b-368b-a127-12efb58b62b9 | -16.64664 | -39.74304 | 2026-10-09 15:58:00 | NPP-375 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 33251360-f5f8-3809-b83c-71d3760cbe4f | -11.65638 | -43.69418 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| e66491a5-6313-39eb-85e1-4c9f469c9a63 | -14.05535 | -44.78297 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 40564076-f306-3810-b944-875405ac8c6e | -15.00637 | -46.2607 | 2026-10-09 15:58:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 3d568e8a-fe06-3c75-aaf2-d0a7b3237618 | -11.77794 | -43.53262 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 096e6b0d-a5c2-3f34-b6f2-9a6bc6e2eb8d | -15.32951 | -40.84833 | 2026-10-09 15:58:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| e7eb1fca-c3b4-3e1c-ab45-2e0c424684eb | -11.89187 | -47.39431 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8f1641f5-cf8c-3650-82d2-e585343aaa4d | -15.25624 | -42.36816 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| 1e09a2c2-c483-3e63-bc21-20be67b5047e | -17.1024 | -41.5692 | 2026-10-09 15:58:00 | NPP-375 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.0 |
| 6a32332c-9e8b-3424-969f-632cc9317f9b | -12.19142 | -39.76978 | 2026-10-09 15:58:00 | NPP-375 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 6cb613fc-0d51-35bd-b165-a469ddbd14c7 | -11.9768 | -43.47434 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 651a3d0c-ecd4-3912-902f-0e05f173e628 | -14.58739 | -41.20022 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| a26896d6-df43-33f5-826f-4a38e042cd2e | -12.13984 | -43.30972 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c93f954c-4849-3d76-acda-d059e0f0a166 | -15.224 | -41.10205 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 41718fe1-cf6f-3eb3-8e27-504b018fe056 | -11.65603 | -38.76134 | 2026-10-09 15:58:00 | NPP-375 | BIRITINGA | BAHIA | Brasil | 2903607 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b2c9c91a-b051-361f-8b93-6deef80776a4 | -18.32351 | -42.36866 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| 351b6033-51da-3c03-beda-a7f9ba288ec1 | -14.05535 | -43.84644 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 7c70affd-365d-3306-b93c-c4b342879dce | -17.42002 | -43.58892 | 2026-10-09 15:58:00 | NPP-375 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db359c58-d161-3574-ab5c-c7b2f39995dc | -17.40018 | -39.6007 | 2026-10-09 15:58:00 | NPP-375 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 65e6649c-8bf9-32fa-8d22-4854da335885 | -13.40653 | -43.48573 | 2026-10-09 15:58:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 12f74992-71e3-323f-a910-25d8fca69b82 | -16.93309 | -42.10963 | 2026-10-09 15:58:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| fe8894db-f955-31b8-a097-d23f83ced7ca | -11.58687 | -43.65021 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 263.3 |
| 52c1cfb8-4d7a-3ed6-8b5f-5640d36b5e84 | -15.33382 | -40.84173 | 2026-10-09 15:58:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 8ff080ff-9953-396a-832d-f5d67c0ac055 | -11.9862 | -43.45652 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a610ad8b-b5e6-38d9-b7d9-c9def981a2ee | -11.59222 | -43.6497 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| a9778ded-253b-3bec-b437-28e7b3fccd57 | -15.39291 | -41.89785 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| c3cabf4c-6d87-300c-8f25-e4801b9bfc65 | -13.2655 | -44.00013 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 17a6180a-2e80-3fd3-9c52-af4e6ee2e566 | -11.56913 | -43.69953 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35250f4c-710e-38a0-bc53-486382045b8d | -12.91028 | -45.11741 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| c0d88bba-d0e3-35ca-bcd3-4e7a40ee16f6 | -12.37191 | -46.57358 | 2026-10-09 15:58:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 72d30b4e-585c-3834-9ae0-e76eb014ea52 | -15.80415 | -41.328 | 2026-10-09 15:58:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 2d20fad7-28f0-3872-b2f2-8fd1ee0178b4 | -11.98204 | -43.46985 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 06cc6db7-43b8-3621-8306-2d1461ad7ba9 | -11.97994 | -39.4808 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DO JACUÍPE | BAHIA | Brasil | 2926301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| c3cf93a4-3f49-3cae-a4c0-e0e993751553 | -13.39169 | -40.55227 | 2026-10-09 15:58:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 9d45b6b2-de9e-34af-b7fc-f111b426b815 | -17.5461 | -42.12098 | 2026-10-09 15:58:00 | NPP-375 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4026854b-e720-3f60-b2a0-90af8a367da7 | -11.57544 | -43.65567 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 3e4a9a85-1712-3a73-acf3-3b5b6778c3da | -11.62144 | -43.59757 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 0abfaf39-ea47-37d3-aa48-a19eddbe08eb | -16.07818 | -45.98251 | 2026-10-09 15:58:00 | NPP-375 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 7c210b16-1bf0-302e-b80c-bbbfe766f46f | -15.37749 | -41.90621 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| 69856b7a-526b-3055-b52a-49926aeb620e | -11.82834 | -43.60672 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d0f65689-2b46-3ea2-ae2c-67f28624181b | -15.25936 | -42.3838 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| 18240168-c4fe-3bd2-b010-671d96cfd1c0 | -16.06887 | -45.25526 | 2026-10-09 15:58:00 | NPP-375 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 470cd597-5b97-3a5a-a1bc-a658e493cbf5 | -18.05215 | -44.61565 | 2026-10-09 15:58:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d6af4886-c3f9-335c-84c5-064c28ff77e1 | -15.06967 | -39.45266 | 2026-10-09 15:58:00 | NPP-375 | JUSSARI | BAHIA | Brasil | 2918555 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 9d1a0952-a5bb-3ea2-9338-4728432a17ae | -12.14913 | -45.36562 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 609db79e-6b3f-3552-8b14-3da2ed5ba190 | -15.26444 | -42.37906 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.5 |
| c1062f18-db9c-335c-bf93-c96da0d70c0e | -14.05671 | -43.58254 | 2026-10-09 15:58:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d16a340-1bc3-3f20-9ca3-6cf53bfd3b4d | -12.13931 | -44.74195 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 84c3d413-64d9-3d77-90b4-b2d8a644ab99 | -14.26905 | -41.04091 | 2026-10-09 15:58:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2e028ad1-3232-3567-82ed-711474895e33 | -15.43331 | -43.30536 | 2026-10-09 15:58:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 072bba71-baef-326c-a1c6-9b59b0c3018d | -15.25154 | -42.37667 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.8 |
| a3eef7f5-4ade-35d3-b8dd-5edad586fe67 | -15.25073 | -42.36915 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| 4d6a497a-14d4-36a8-84a4-866458e6df99 | -15.2534 | -42.38083 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| 623e2a93-02ab-377b-8887-0c300cdb7b96 | -13.58436 | -40.01229 | 2026-10-09 15:58:00 | NPP-375 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 94b3c4b2-c1d4-3982-b94f-7351626cbbf9 | -16.0516 | -42.14941 | 2026-10-09 15:58:00 | NPP-375 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| cb2659df-f8f4-3094-b9c8-4ede15f4891d | -14.41034 | -41.03762 | 2026-10-09 15:58:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 4cd871bb-6c2a-3686-9462-9d7d7989943d | -11.78612 | -45.58022 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4891fad2-ee60-39f1-939a-41ea1c952641 | -15.63584 | -39.18225 | 2026-10-09 15:58:00 | NPP-375 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| bc6f298f-389c-3671-80b9-278464a9cea1 | -15.26312 | -42.36771 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| e434ca77-1abb-30f5-b2d7-0252a321b1a3 | -16.94473 | -42.07655 | 2026-10-09 15:58:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 564599e2-3e66-36ff-8271-432b3f220933 | -11.98452 | -43.48156 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9f805ba3-7a5b-3501-9fd2-2e44ff777893 | -15.25545 | -42.36087 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| 01c3e9d1-b6f9-33e1-bb59-c6e03bd23e29 | -12.22841 | -40.20579 | 2026-10-09 15:58:00 | NPP-375 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b049a9d3-4033-3903-ad3b-340a170287ef | -18.32368 | -42.38052 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.8 |
| d9f384f9-45e1-3819-9043-e6ac6555bab6 | -12.17103 | -42.21674 | 2026-10-09 15:58:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 64ffc899-db63-38b2-bd9b-78fef47fa0a3 | -14.05808 | -43.8381 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 1dd7769b-d6da-34b2-8e3d-c5a5eb4076e6 | -11.68354 | -46.77271 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0a96de05-4c1f-30db-8a78-6e465f6e36ec | -15.52754 | -41.01366 | 2026-10-09 15:58:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| bf70752d-a765-399e-8f18-48e5e6349a42 | -11.66167 | -43.68953 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| fa88a7b2-db31-3323-b063-0d30baa31b51 | -15.25237 | -42.38433 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.6 |
| 9b8956d4-1f94-357c-b7f5-2fc2cd840f7c | -12.21668 | -44.75793 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f2592282-fbf1-3cce-a7e1-62f7ff1efab3 | -12.19912 | -44.82491 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 88a562ce-44d1-30df-960f-77ccc60a6be6 | -16.07686 | -45.96911 | 2026-10-09 15:58:00 | NPP-375 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 7e78fdd0-d906-34b1-b7f2-d33b660a77d3 | -15.38366 | -41.91233 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 172.9 |
| db3b729e-6750-3301-8ab3-47ab97cc2932 | -15.39029 | -41.92252 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 1d1235d4-536a-399a-92b7-1aadab44e204 | -13.40559 | -43.47745 | 2026-10-09 15:58:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 32bfd34b-ca94-3275-ae5f-431f08b45af2 | -11.58065 | -43.64688 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 263.3 |
| d27bd553-63fb-317d-a214-e750aa2535db | -15.65072 | -40.95467 | 2026-10-09 15:58:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| f559017b-c719-3e3c-a2be-83e54c65b8f4 | -14.0644 | -44.80783 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 38669368-ff05-37c4-8fe8-5f8727ea1ef0 | -11.56961 | -43.70341 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4858b961-2d29-3461-a878-d59a0b5b3018 | -13.24125 | -39.76847 | 2026-10-09 15:58:00 | NPP-375 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 4981c568-ce54-3c4f-bf20-c4ba252b6d02 | -15.26099 | -42.36011 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| 9004f772-b655-36c7-8cee-db6ac66a463f | -14.27304 | -42.18792 | 2026-10-09 15:58:00 | NPP-375 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e15662be-e941-3811-83d2-96703058d021 | -14.09919 | -42.47806 | 2026-10-09 15:58:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0900f627-f963-33bb-8019-d06152b30766 | -16.07752 | -45.97581 | 2026-10-09 15:58:00 | NPP-375 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| e1362ac7-5720-383f-a65f-2103260f0cb1 | -14.46628 | -41.95556 | 2026-10-09 15:58:00 | NPP-375 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |


[Clique aqui para ver as próximas entradas](README260.md)
