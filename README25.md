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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f6b2681-78d2-3ca3-9626-97df7dc65d44 | -11.2868 | -46.2326 | 2025-07-03 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 2998e0f5-1948-3f9a-9a0e-9dd64d95c533 | -11.546 | -47.8772 | 2025-07-03 12:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 63e05482-2571-3e55-a20d-5bf226afe658 | -9.8465 | -44.6834 | 2025-07-03 12:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 85c1dba2-1cd4-34c4-a281-223a35102856 | -11.546 | -47.8772 | 2025-07-03 12:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 6fe1a998-bbac-30cb-8e9d-4242e5e17b53 | -6.694 | -43.1648 | 2025-07-03 12:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 91.8 |
| f1ecfb6b-a445-3f88-a959-bbf37b512ad8 | -6.2943 | -43.6891 | 2025-07-03 12:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 2e58a1f6-6351-3c63-9384-e0f33936e92b | -12.6636 | -45.2776 | 2025-07-03 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 799fd7f4-7d4c-3ea6-9fc8-32b86f9bdc04 | -9.8465 | -44.6834 | 2025-07-03 12:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| ce265e38-32bd-3a5b-b696-2a66f75f0447 | -6.2945 | -43.6659 | 2025-07-03 12:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ec3f2174-9647-39f4-a45b-a282a05f61a4 | -6.694 | -43.1648 | 2025-07-03 12:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 123.3 |
| e64a8be3-c6b2-3b34-909c-589e0a44be6f | -11.546 | -47.8772 | 2025-07-03 12:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 077eeae7-d628-34b2-a1b8-a8ad7faa7ad5 | -11.546 | -47.8772 | 2025-07-03 12:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 0dd6cae0-4bf7-3ed8-bdd6-e7a07372c183 | -11.2868 | -46.2326 | 2025-07-03 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 9d5a6395-e92e-313f-a413-b57d5b715f0d | -12.6636 | -45.2776 | 2025-07-03 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 1b1c3d95-38ff-3ca8-aad2-d744247ba466 | -6.694 | -43.1648 | 2025-07-03 12:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 119.8 |
| ecaf4379-8b61-37ef-8950-f787ef1c98a6 | -6.2945 | -43.6659 | 2025-07-03 12:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d98cd302-0f4b-3e05-ba03-24129327ef1c | -12.6443 | -45.2806 | 2025-07-03 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 9726f24e-acfa-3258-80c3-ad5598aa422d | -11.5651 | -47.8748 | 2025-07-03 12:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 49ea42ee-6ade-3d49-af55-6e0e7c5aeaac | -11.8651 | -44.8451 | 2025-07-03 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 3cd75ef1-2443-31f3-bdb5-e2ca2fda26e3 | -11.2868 | -46.2326 | 2025-07-03 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f2e7a815-d530-37b3-97cc-7a570e793ce3 | -11.546 | -47.8772 | 2025-07-03 12:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 6e2708d0-08be-3674-87fd-ecfd67fa3977 | -6.2945 | -43.6659 | 2025-07-03 12:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 4dc7ae1c-664d-3e84-a63e-0a6d2a3949db | -12.6443 | -45.2806 | 2025-07-03 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 9e809da0-ed8b-3379-b65c-055138872c92 | -11.3254 | -46.2048 | 2025-07-03 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 59a9aed2-98cd-3e14-ac85-5f11172290c0 | -6.675 | -43.1899 | 2025-07-03 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 169.1 |
| 2e314d78-5596-3c5d-bf14-7705f10b441b | -7.8629 | -47.8761 | 2025-07-03 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| e704a1b7-d8f4-39ae-a5c9-7b686a4e7033 | -6.694 | -43.1648 | 2025-07-03 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 122.3 |
| 547affeb-6a4a-356e-925b-f8280ac4f7ac | -12.6636 | -45.2776 | 2025-07-03 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 907fcd61-4b9e-36eb-8c9d-dd0e0f43fac9 | -11.5651 | -47.8748 | 2025-07-03 12:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 9d01f0a4-d919-3364-8342-1d1968c68959 | -6.2757 | -43.6675 | 2025-07-03 12:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| eeb6814e-3932-3a78-9691-5013e2af2995 | -6.6938 | -43.1882 | 2025-07-03 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 1bb5a9aa-e601-3aeb-9ad0-18a863e3fe3e | -11.546 | -47.8772 | 2025-07-03 13:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| c0fd3387-8743-30cb-8106-0df682bcfa74 | -6.2943 | -43.6891 | 2025-07-03 13:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 08cb193d-7d02-3f8f-ba19-af0787392294 | -12.6443 | -45.2806 | 2025-07-03 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| c985bc36-629f-368a-9b60-2d2e9c3efd83 | -6.2945 | -43.6659 | 2025-07-03 13:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 46ba4ba9-b99a-36db-b117-819f289db48a | -6.2757 | -43.6675 | 2025-07-03 13:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 2e44152b-ba5b-394c-ae21-9d05573dd402 | -12.6636 | -45.2776 | 2025-07-03 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 38873762-6e69-3ebf-ace9-e904aa7cc1cf | -11.5651 | -47.8748 | 2025-07-03 13:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e609f071-caac-3a5a-b49c-5e1ca6f0386f | -6.2945 | -43.6659 | 2025-07-03 13:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 144.1 |
| a17b6675-d237-3b7b-906a-5f757fb36f86 | -11.546 | -47.8772 | 2025-07-03 13:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 94039f87-0ae4-38ca-8cbe-30d7eb653339 | -6.2757 | -43.6675 | 2025-07-03 13:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| a0692b16-0a98-3d86-9775-fceec7ed007e | -7.1925 | -44.0038 | 2025-07-03 13:10:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 2dbf06cc-f384-3f9f-9982-ec542baec3a0 | -6.2755 | -43.6907 | 2025-07-03 13:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| b12d0b7f-fd64-332d-ba4e-c21cb0d9693d | -6.675 | -43.1899 | 2025-07-03 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 322.1 |
| 31414bbc-1a45-3d5b-99c4-1f3cf7309dd5 | -6.694 | -43.1648 | 2025-07-03 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 129.6 |
| 0f0860f2-8879-3951-a21c-a3506d508167 | -6.2943 | -43.6891 | 2025-07-03 13:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| a9bd56ad-cc72-3f59-b2b3-6023c1c08733 | -6.6938 | -43.1882 | 2025-07-03 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 101.6 |
| d033710a-4228-32b2-925d-5c7a192a6fdc | -12.6636 | -45.2776 | 2025-07-03 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 5c81128c-5c18-35e9-b118-2c757d4d7050 | -12.6443 | -45.2806 | 2025-07-03 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 7a768ff0-14a0-32d1-a431-8832daca6b8f | -6.2757 | -43.6675 | 2025-07-03 13:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 9b744c0c-7ef2-33dd-aff9-e774efb5c4ec | -6.2943 | -43.6891 | 2025-07-03 13:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 59555b73-d33f-31ac-bbb7-9e4119cb9c3d | -6.694 | -43.1648 | 2025-07-03 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 160.3 |
| 302dbc78-86ba-39a7-9aa1-e20b702edeae | -6.675 | -43.1899 | 2025-07-03 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 209.8 |
| d6b52fea-701e-3e8c-bc41-026a59e9370b | -12.6443 | -45.2806 | 2025-07-03 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| b3a1fc28-fbc6-3466-b885-161ecf2f0950 | -6.6938 | -43.1882 | 2025-07-03 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 112.1 |
| 83332f6a-5c5c-3c07-b061-a780f3875f12 | -6.2945 | -43.6659 | 2025-07-03 13:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 195.4 |
| d233d5b1-4d79-3ccf-8f64-0bc1eacd019a | -11.546 | -47.8772 | 2025-07-03 13:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 2cfbbc5e-7c6b-3a6a-87dd-2c81f8a59bc7 | -12.6636 | -45.2776 | 2025-07-03 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 1fdcff88-0e11-3c17-ba0d-ecb221fc2508 | -6.2755 | -43.6907 | 2025-07-03 13:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| fca61dfd-17f9-30a2-95b6-d193b3557681 | -7.1927 | -43.9806 | 2025-07-03 13:20:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 294340c5-89b3-3a83-bb30-0f1d9277e646 | -11.2868 | -46.2326 | 2025-07-03 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| a54d892e-3b40-3bc1-981a-43661d729fa6 | -10.6483 | -44.4861 | 2025-07-03 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 27f57a50-ad6f-3787-a60e-e5a17ba086ea | -11.546 | -47.8772 | 2025-07-03 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 28035bb3-34da-3a91-a004-7b35d052ed94 | -12.6443 | -45.2806 | 2025-07-03 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3a3a98ad-497f-32ff-b54e-826ed3725b16 | -6.2945 | -43.6659 | 2025-07-03 13:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 221.4 |
| 9209d05f-8a71-3258-9e46-9fb33c8ca758 | -7.1927 | -43.9806 | 2025-07-03 13:30:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| d003dea2-0325-30ac-9df6-810946a4ceaa | -6.694 | -43.1648 | 2025-07-03 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 161.0 |
| 5bc6b833-b222-3196-8d1d-e6f018fa8f48 | -12.6636 | -45.2776 | 2025-07-03 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| aee1272e-6047-357e-90de-e7653007adf6 | -14.2453 | -43.6658 | 2025-07-03 13:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| bf3cd6e8-b921-387a-9b62-eb59fade560d | -6.6938 | -43.1882 | 2025-07-03 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 127.7 |
| 301cfc0f-a106-397d-bcb0-2eb61d4c84c7 | -6.675 | -43.1899 | 2025-07-03 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 405.7 |
| 08b827ae-fd75-322c-a84c-5692d53999ff | -7.8629 | -47.8761 | 2025-07-03 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c831969f-bd55-366f-9c8e-37277b38face | -6.2755 | -43.6907 | 2025-07-03 13:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| de383756-d5e4-348e-88f3-9cd3a916b28c | -6.2757 | -43.6675 | 2025-07-03 13:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 225.1 |
| 0abd8171-3dac-399e-ae11-63bc73af4a47 | -6.2943 | -43.6891 | 2025-07-03 13:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 0199f998-60e6-37bf-8650-6bcd63b634cc | -6.675 | -43.1899 | 2025-07-03 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 279.5 |
| 9cde6133-ff4b-3eb9-b530-86ae591d2891 | -12.6443 | -45.2806 | 2025-07-03 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 4a51b6ca-626c-3092-96cb-a9fc6e1f5a6b | -6.2755 | -43.6907 | 2025-07-03 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 1012e27c-eb7e-349f-bc6f-8424dc7ab84b | -12.6636 | -45.2776 | 2025-07-03 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| ee2c33d5-5530-36d1-abee-a66626a9df55 | -19.1516 | -54.3901 | 2025-07-03 13:40:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 597ad2ff-0a19-3c50-a8f5-2dd3421fdf64 | -6.694 | -43.1648 | 2025-07-03 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 79dc410d-2b93-3ee2-9de0-149f10316957 | -14.2453 | -43.6658 | 2025-07-03 13:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 007aae5e-4eab-34de-86fa-f6a4ce3e909d | -7.1927 | -43.9806 | 2025-07-03 13:40:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| bd8a8a14-ad72-3a38-afac-8560011e581c | -11.546 | -47.8772 | 2025-07-03 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| d0760d79-23ad-3ddb-bde7-28273906a359 | -6.2943 | -43.6891 | 2025-07-03 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 3a335635-6bf6-38cd-a7f3-dd1e5b0493eb | -6.6938 | -43.1882 | 2025-07-03 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 88.5 |
| e18509c9-9329-3641-b897-7fe349b1f9de | -7.8629 | -47.8761 | 2025-07-03 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 38877d73-dca1-3cc2-ac41-07bf557990c7 | -6.2945 | -43.6659 | 2025-07-03 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 237.7 |
| 55dfc3f9-a1ec-3472-b815-1cac1274ac7c | -6.2757 | -43.6675 | 2025-07-03 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 246.0 |
| f4ef4db3-1a8e-3716-ba88-77f9fef5c53e | -10.6483 | -44.4861 | 2025-07-03 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 108a02c5-bb9c-3c8d-a4b8-59282a97534e | -7.1925 | -44.0038 | 2025-07-03 13:50:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 512057e0-e293-322d-9de0-506bcc9e94c0 | -10.6483 | -44.4861 | 2025-07-03 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 91573c4b-9237-3f02-8226-d03b78f5c7c3 | -11.4602 | -47.2883 | 2025-07-03 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 54ec110d-9bb6-3787-8a72-8450e643570b | -6.6938 | -43.1882 | 2025-07-03 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 40f00be6-9a46-36ff-8660-c678928ed57f | -11.5464 | -47.8551 | 2025-07-03 13:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| a730c3fd-972c-307d-8cb2-d7aee40a8f0e | -7.1927 | -43.9806 | 2025-07-03 13:50:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 904f4e7d-c87d-3b62-aa9c-0b2584af1d8e | -11.546 | -47.8772 | 2025-07-03 13:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 6bf61aaa-82d1-343f-b931-e3ca7fa88f80 | -6.675 | -43.1899 | 2025-07-03 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 156.1 |
| 78b7f909-94df-3c55-a047-5cda8541aa57 | -6.2945 | -43.6659 | 2025-07-03 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 211.8 |
| fc53ed4b-aa8a-3fcf-b3e6-0fa23292f729 | -12.6636 | -45.2776 | 2025-07-03 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |


[Clique aqui para ver as próximas entradas](README26.md)
