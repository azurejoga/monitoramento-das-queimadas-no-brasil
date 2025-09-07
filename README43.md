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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4c10c6e-3971-365d-9e78-886012fe4732 | -11.82251 | -46.77029 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97837844-69dd-3096-b543-ea2bc0610333 | -5.7612 | -45.54216 | 2025-09-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3781c33a-2a4a-3239-ba14-eada156484ab | -12.54749 | -48.06971 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 194a3bb0-253b-35e4-b3d7-664b66c5b50d | -9.45906 | -56.04935 | 2025-09-07 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cfb2a53d-0546-3503-a705-cc74ae64471f | -7.24227 | -39.17983 | 2025-09-07 04:19:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 34f9f077-9992-329e-b1fb-2ba141c09e6f | -6.07825 | -43.30981 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c9a0e303-3f3f-3d70-8a26-fac119d2499d | -11.85224 | -50.51656 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51748537-a0dd-38b2-a3d7-c8a49e8b4c07 | -11.73559 | -46.69779 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 638d6947-0452-335e-a2e5-17717c083c52 | -6.26726 | -41.39627 | 2025-09-07 04:19:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d76cac98-4b7e-3243-a3b7-2dc2b94f5065 | -6.22761 | -43.56994 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 558fa212-2ba8-38c7-86cc-a0259b8d8be4 | -6.20392 | -44.17937 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1366cb4b-3c8d-3e9c-a4bc-555a75e15a95 | -6.63211 | -53.16082 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf42e907-c1eb-3f50-9497-fd3dd767007b | -6.26079 | -42.58009 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d156efb9-01c9-3167-b8cd-1400bf0c0f96 | -6.21173 | -43.37062 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64ba6c74-d804-389a-af5c-d948a7959193 | -10.35071 | -46.45665 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ef080f1-4a18-3992-aa92-8e6db6cb42e2 | -6.1683 | -43.18374 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7376e25f-0b10-3e09-a255-a72948ac3e03 | -7.71655 | -45.35657 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccc81809-b01b-37a7-b135-609fb3547689 | -12.29742 | -47.23885 | 2025-09-07 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 267b54ce-2197-3b12-83eb-6b074353ee8b | -6.36586 | -43.53312 | 2025-09-07 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b97db71-264a-39d9-b46e-777a2727b98a | -11.25788 | -46.49965 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0468bafa-0055-317d-93be-e6f007f67287 | -6.31896 | -42.19711 | 2025-09-07 04:19:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3e0dc479-8cc8-38ca-bb80-994f4fb85aa5 | -8.1075 | -45.31208 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 179545de-8ead-3edc-b848-e675527972a6 | -11.15417 | -48.39437 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a3d7b66-5d1f-3eff-9c8d-0ebbc481cb37 | -11.40082 | -43.56618 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f90875e-f3a7-333c-b6f2-aaae4ed6371b | -7.72441 | -44.72471 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8325164-05b3-3993-a650-23910dcd74f5 | -12.84519 | -48.00977 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10336610-6d14-3d56-a82e-fbbd7ef5ec1d | -10.78664 | -47.72548 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0c2c533-1858-375e-a347-1f7c633a14b4 | -9.98989 | -51.63921 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18c307d8-a2ec-3522-9d16-5c372a951f2e | -10.31512 | -46.46539 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b461edf-9dfd-3934-b7b9-1176f65d0519 | -8.93311 | -48.65481 | 2025-09-07 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d977b191-acf8-3730-918b-460f2974f48b | -6.84052 | -52.84573 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41183913-7359-3441-86f4-113610803dd7 | -11.59264 | -47.16754 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00cf798c-37ca-3e8c-8e50-96bddbf9fde7 | -6.20977 | -42.61899 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 59239b32-84f5-3476-90f8-4d8cb0ce466c | -6.19888 | -42.62115 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc52a604-3acc-322e-a686-5170053a0dd0 | -8.18917 | -50.13876 | 2025-09-07 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe469f0f-c881-3aaa-8dbc-30da5c9ff017 | -11.15485 | -48.39022 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8b3592d9-9b8c-3501-b09e-69ab464751a0 | -6.43431 | -43.63777 | 2025-09-07 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cb7dac2-1081-319f-988a-997ade24c54c | -7.02016 | -43.22382 | 2025-09-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| acd52124-3877-31b1-a12d-4c34f63777d2 | -7.59136 | -44.66457 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7e88bd7-8c01-3265-aa40-43fec50ac3a3 | -6.20035 | -43.59115 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67bfb048-dd17-3592-ab81-4141154dff11 | -7.75444 | -50.7427 | 2025-09-07 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a83365f7-dc9f-3594-9343-a59a7051a8fa | -12.83499 | -48.00789 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 384202a9-7d16-3bda-ae64-83693baa787a | -6.07461 | -43.55328 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd9ad4a6-06d3-32e4-af26-8b53eeccfe62 | -8.42724 | -47.30661 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14f4a304-a172-3896-bdc5-deacb30b7033 | -13.18682 | -44.48708 | 2025-09-07 04:19:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d983be8c-0825-3955-914b-363c75f237c2 | -6.88151 | -45.54407 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa52a7f6-88ca-3c2c-8ec2-dea4ee1240e1 | -7.74475 | -48.82947 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7fb122e-e559-37af-97ae-75c9d5e3e2cf | -6.21644 | -42.46162 | 2025-09-07 04:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 24297796-fd0d-324b-804d-4fdf286545c6 | -10.72546 | -48.59354 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 716a20ee-3f18-333a-bca8-967a98e63183 | -6.21931 | -42.46598 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 554dab03-2445-3c1a-be1e-3ae400214c49 | -5.59596 | -45.63857 | 2025-09-07 04:19:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84c52c67-097c-3cd1-a151-2f798594c1d8 | -11.26091 | -46.39516 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 085c525f-e06b-3508-b641-aab661a9650c | -11.81919 | -46.76973 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f6aad4b-4fba-3880-912c-a065f88a00a3 | -11.83391 | -47.56373 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b8f6410-e8bc-3350-9e08-aa9a1ae64ef9 | -6.66351 | -47.73573 | 2025-09-07 04:19:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 581a1e88-6e53-318b-8e5c-d79160fb9da3 | -7.71502 | -44.71967 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a2dbd5d-edd1-3e17-b8a3-e2eee5da4ff0 | -7.23163 | -45.73665 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4ca8db8-9474-3911-bc6b-804cbe2762a8 | -8.48544 | -45.17631 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4d27cd0-8622-3724-a823-2aa80e73cd25 | -8.29564 | -45.38842 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 392e8d9f-932f-3ddb-a9e3-3cf3c1c4563b | -6.80017 | -50.84301 | 2025-09-07 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e04c8d00-d812-3591-a783-9e4bbfc01184 | -7.72979 | -50.30748 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 38fc9b08-f4ee-3f4c-bb1a-0779e9dfd57e | -12.57502 | -44.62539 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b7f35ee-18fa-36af-98ee-0a88ef6af958 | -8.69813 | -54.67677 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5881b7c9-42cc-3f0b-9766-911cda6ca548 | -6.16886 | -43.1801 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 90260c7f-bb40-3626-9307-cadd1200cf7f | -8.07715 | -45.48192 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b84c516-7ed5-32b9-a585-012ae844d6eb | -10.86841 | -47.26902 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 782fab68-8ce7-3080-9c6e-bc47b85008ca | -7.73103 | -44.72575 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 560a1de7-e214-3735-b803-3230f640bcdb | -12.22375 | -43.87027 | 2025-09-07 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 15b1644e-e6a1-35b5-be3f-a612995091da | -6.53681 | -42.60965 | 2025-09-07 04:19:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 53a633cb-b15e-346a-ae60-3a173b393cc7 | -11.63655 | -46.63786 | 2025-09-07 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 483908ff-29f8-32c2-a8cc-107f340ed2df | -5.76232 | -45.53511 | 2025-09-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bdead03-2b81-310b-a65c-0a8a989bceac | -7.71172 | -44.71914 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04874bd2-50e7-3d97-a5d3-ee3a37bddf3d | -7.75075 | -48.81669 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3e6ba481-3bef-3f32-bf40-21eef7af140a | -10.73517 | -44.35677 | 2025-09-07 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04c4debd-588e-3f68-8a91-4eb559c2770f | -5.57965 | -51.91451 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10daa437-d537-3cc2-9faf-bb58083cf96e | -6.61437 | -43.98646 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 92f67ba9-7197-3e45-9dd7-fc175b8e7895 | -7.63387 | -46.55492 | 2025-09-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e07299d-a5fc-321b-948c-edfa1b19da00 | -8.74327 | -44.87538 | 2025-09-07 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4e5ef2d-c1cc-34f9-b778-89e262c8adf6 | -6.80356 | -47.07354 | 2025-09-07 04:19:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d21c0b4c-93e5-3feb-a1e0-7eb6ddfbc6e2 | -6.16271 | -43.19761 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81b8ab09-40c1-3474-8b30-8b2e4a0a130a | -8.15474 | -44.86036 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d89afafa-987b-31a8-b9c2-751835573880 | -6.134 | -44.25714 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3240b32f-4550-3328-b2f0-f4cc96c6f239 | -11.94165 | -46.6623 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89f4d2cf-6916-3851-a8e4-cd4430b96ebe | -8.03825 | -44.04179 | 2025-09-07 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6925028-7f77-3d72-a4cf-fcc56904d402 | -6.9187 | -45.2038 | 2025-09-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f758101-f0a3-3cdf-ab18-acb3ab8ebf1b | -9.9964 | -51.62764 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88f8f503-b2ba-3f09-ad06-8494b493eb71 | -11.90009 | -46.64809 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d2b5859-c394-3807-9209-9980ec22f4de | -6.23479 | -43.30083 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21589b0b-5796-3572-896a-a7c54ff18341 | -7.02355 | -43.22435 | 2025-09-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 951d450e-9400-35de-86d8-586633162a4e | -8.11412 | -45.3345 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2aadb5df-4d45-36a9-a4b1-95ca8295ac70 | -5.85173 | -45.31215 | 2025-09-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7596f7b5-8f19-38b2-82bf-0315e3c102ab | -11.14715 | -48.39317 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 832bfe51-a5bc-35e6-9972-668f014c7431 | -6.08832 | -43.28935 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2e5200d3-c065-3733-ab3f-bb66e2190d42 | -8.15033 | -44.86679 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bb22c8e-c754-3812-be68-dc4c3a1abccf | -6.43821 | -43.63473 | 2025-09-07 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 322b5be8-6275-3dda-993e-5014d27d988f | -8.02741 | -45.43082 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3e5050d-ffd4-3bf1-afff-97e06823e544 | -9.17967 | -45.59804 | 2025-09-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ef6e14c-c740-3a47-8772-a772a4a85634 | -6.88421 | -45.59123 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c673410-f3e3-39d0-a859-6167b5858ed9 | -11.25652 | -51.12389 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a19b8658-538c-3e5c-8253-873b59e20bd2 | -11.09651 | -52.05666 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README44.md)
