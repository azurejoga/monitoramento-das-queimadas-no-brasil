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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9990a4c8-d63c-36b7-a275-dca1e6c27fae | -15.89281 | -43.45528 | 2025-07-02 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| aea16580-bfe9-3e81-aca3-b342cc2aeee1 | -15.89649 | -43.46144 | 2025-07-02 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 4c112e40-3bbb-3d2d-9501-74ca357f1df0 | -18.0312 | -46.0559 | 2025-07-02 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08ceae41-a8fa-34bb-aed9-79d20d73b9eb | -20.34794 | -40.3603 | 2025-07-02 03:38:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e5cb6ef5-79a8-39a9-98db-cf69a12ff3bf | -13.35715 | -46.19545 | 2025-07-02 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 676e27c2-d4ad-3113-a422-de289af09e06 | -21.45781 | -41.11634 | 2025-07-02 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6bb282ad-2701-3cc6-a287-aed078c5aab9 | -15.92239 | -43.51275 | 2025-07-02 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 73dcfc85-7a4e-3d87-afaa-446347a9300c | -16.42604 | -44.51869 | 2025-07-02 03:38:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1bd81b2-94d0-3f97-8089-fbe47bb7f1a8 | -20.23579 | -45.07518 | 2025-07-02 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO OESTE | MINAS GERAIS | Brasil | 3164605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6de997ac-cee9-3564-8ba7-311b685a1d5a | -13.41069 | -47.81994 | 2025-07-02 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 972779e0-1757-3751-ac05-55961a791ff1 | -18.41172 | -44.18626 | 2025-07-02 03:38:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 554f3444-26dd-3687-8e5c-99c260131f09 | -20.2335 | -41.89008 | 2025-07-02 03:38:00 | NOAA-20 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 026a8e31-a68c-319f-9df0-3c97bd096061 | -19.43966 | -48.55362 | 2025-07-02 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c778515c-1a1d-3d84-a8a5-c58d679cd842 | -15.89181 | -43.46047 | 2025-07-02 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| fea524ff-7091-3296-b8e7-bcbc1f8717ba | -13.41058 | -47.8187 | 2025-07-02 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0dd6285b-7ffb-38b0-a63e-030e40a05ba7 | -19.43897 | -48.54993 | 2025-07-02 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 395b954a-4e0c-3657-be0e-20938c08f5b2 | -15.92029 | -43.51528 | 2025-07-02 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27ef3a5e-d80a-3f8f-a6f4-11d187465e65 | -7.8133 | -44.0358 | 2025-07-02 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 5e863e00-e8c4-3e9d-a2ce-56d6fbfaf6a7 | -7.2028 | -43.0936 | 2025-07-02 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 3a56cc15-af8e-37dd-8752-0c65ee3f563a | -7.7944 | -44.0377 | 2025-07-02 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 315ffe40-0a60-31a8-bcb9-2161c2910911 | -7.8135 | -44.0126 | 2025-07-02 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 26193d62-6cf3-3fea-8d1c-e2d07f6eac7c | -10.883 | -56.4567 | 2025-07-02 03:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 58b13ac7-9910-34a5-9caa-5b58c39b39ed | -7.7947 | -44.0145 | 2025-07-02 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 480d5f5d-e6b6-3e8e-a471-bba49d62da02 | -7.2217 | -43.0917 | 2025-07-02 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 5aece9fc-2892-398b-ad9a-ae67aabbe3a4 | -21.50609 | -48.81505 | 2025-07-02 03:40:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51d1c7f9-d655-3176-9f6f-d442acdc7091 | -20.6644 | -48.44013 | 2025-07-02 03:40:00 | NOAA-20 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdc15804-139b-30d1-9595-26fe1da27608 | -20.65864 | -48.43847 | 2025-07-02 03:40:00 | NOAA-20 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32e29b70-df60-3484-9acf-207e56df0468 | -21.85897 | -46.69619 | 2025-07-02 03:40:00 | NOAA-20 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3de310a1-af26-33d1-9ccb-03782a1c33d2 | -20.92514 | -46.97338 | 2025-07-02 03:40:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cedb6c1-1e06-3228-a3bd-7bf60549f81c | -21.50504 | -48.81963 | 2025-07-02 03:40:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4d99a8d-a17c-3e51-9c2f-e83fff9ba1e0 | -7.8133 | -44.0358 | 2025-07-02 03:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| eccffc92-e5db-39f8-9c45-f0a4aa9cd8ff | -7.6051 | -45.7464 | 2025-07-02 03:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 2daf995f-5350-3f5d-a265-d7d2c11fa88b | -7.8135 | -44.0126 | 2025-07-02 03:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 189.2 |
| f2f1106c-3dba-3dfa-80b3-8ab50183d8b9 | -7.7944 | -44.0377 | 2025-07-02 03:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 25c16914-2ca0-3b42-847b-6ed4af0c19ad | -7.2028 | -43.0936 | 2025-07-02 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| a2f863a6-ec87-3ca1-be1a-d7fcf4c70d52 | -7.6239 | -45.7447 | 2025-07-02 03:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 54212b47-d3f0-3f36-a692-adbd734164d9 | -7.7947 | -44.0145 | 2025-07-02 03:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 700d7d0c-4a04-39cb-8822-ef121a8d5f08 | -7.7947 | -44.0145 | 2025-07-02 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 32b01915-2580-38fa-a958-a572b1610b60 | -7.7944 | -44.0377 | 2025-07-02 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8dd6ac58-6ac2-3b73-86c8-56fc8264f24b | -7.8135 | -44.0126 | 2025-07-02 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 181.8 |
| c6feeeb0-2ed5-318a-889e-5b8cf1b0210e | -7.8133 | -44.0358 | 2025-07-02 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 4090879c-fd66-3b80-a0a7-3f6bcfad51ae | -7.6051 | -45.7464 | 2025-07-02 04:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 93b3f880-3e54-3662-9814-8d75d17274cb | -7.7944 | -44.0377 | 2025-07-02 04:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 6340a6ec-f9ed-36c5-ac63-d811ea71eef9 | -7.8135 | -44.0126 | 2025-07-02 04:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 242.7 |
| 618f5810-7b30-363a-b75a-1bef1ebb1a16 | -7.7947 | -44.0145 | 2025-07-02 04:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 166.7 |
| e154d5b3-1210-3c43-aae5-78d9949cb21e | -7.8133 | -44.0358 | 2025-07-02 04:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 8d0782c7-66bd-3440-856a-81d875eabb4e | -7.7947 | -44.0145 | 2025-07-02 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 91ba2492-2778-3069-8140-3fcbcfb1612e | -7.7944 | -44.0377 | 2025-07-02 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d578689e-d8a8-3f34-b878-9f3557e8680b | -7.8135 | -44.0126 | 2025-07-02 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 4fefd32d-887b-3986-940c-73e15a9a1482 | -10.883 | -56.4567 | 2025-07-02 04:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 0eeb508c-77b7-3ff6-bc8b-51b76448f767 | -7.6051 | -45.7464 | 2025-07-02 04:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| c749e82d-a994-3619-aea3-e4c0d2b68682 | -7.8133 | -44.0358 | 2025-07-02 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 140.8 |
| a2de8e9d-178d-3c98-b366-34867466918c | -4.03671 | -48.0669 | 2025-07-02 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 17fbe49a-b07e-3a22-a97e-43c042c85f81 | -7.79464 | -44.01954 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e22b86c9-4273-38e6-b964-589cda5df049 | -4.28463 | -48.36736 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72d9476b-9d0c-3802-af08-6c14a5e0f6ac | -3.0316 | -49.43761 | 2025-07-02 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02b6c7c9-3e95-3750-8d3b-0306e7c45cb7 | -4.82999 | -37.90733 | 2025-07-02 04:25:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa498c40-a5fb-32f0-9c83-b8cfd49c14b0 | -5.41675 | -47.56928 | 2025-07-02 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdc365a9-0396-31f6-a08a-586b7d34f80b | -3.21237 | -41.84106 | 2025-07-02 04:25:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c487c31-622a-354f-b15d-6d2d711cdab3 | -6.73077 | -46.31742 | 2025-07-02 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbb09b51-7b58-3cc3-8943-c5a9d920a924 | -7.60382 | -45.75269 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f05b4bb-81b4-3771-b19b-f0ada41b4bd0 | -4.31604 | -48.07936 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b42d53c6-b858-32e6-8145-b7d3ca3750b1 | -7.18514 | -43.17198 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 29491daf-50dc-347a-bcc6-ad82527c36b6 | -6.02223 | -49.23161 | 2025-07-02 04:25:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 452dce32-63f1-3e03-bc80-a46b387b64e7 | -7.218 | -43.1769 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 87a0a37d-1f11-33eb-bf97-ef00a8cf6727 | -6.80648 | -44.75048 | 2025-07-02 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7eb08eee-cbdf-3305-8365-f446d3fdb3d0 | -7.21111 | -43.09661 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7c9e15ea-0748-3593-bc48-31d0662242d7 | -7.21605 | -43.08849 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 4895f515-620a-3405-808d-65001e13a20f | -7.62045 | -45.75529 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac43ba34-acb6-3bd0-8167-2c4bc69b5644 | -7.60769 | -45.74969 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 911a8e49-d8e2-3f51-be97-bcbc20036d25 | -6.24916 | -44.83734 | 2025-07-02 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9765e258-6b86-3308-a79f-f5de71d204bb | -6.71102 | -51.41353 | 2025-07-02 04:25:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 144400cf-cb26-356e-8b51-763243c2b3b4 | -7.81566 | -44.02638 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| bbdb18c7-fe9c-3610-adf2-64c196d7a2d2 | -7.80228 | -44.01665 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 3e55557f-74ce-3328-aef6-bf2058e3c9f4 | -6.28907 | -43.67954 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 87a987c7-8787-3fc3-b900-bca379cd1a61 | -7.61101 | -45.75021 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| abccfb63-4f5b-33af-9b75-e2ae0eb8e8f9 | -4.53931 | -48.02209 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 38ec445c-ce67-3b8d-b53e-f6a696c55ce0 | -7.25867 | -46.40064 | 2025-07-02 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6fe1e77-fb8e-38c1-bb1d-7ed840684fbd | -5.65269 | -46.59471 | 2025-07-02 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af0922d8-5998-3ea5-9cc1-438896fcbe46 | -7.78991 | -44.02694 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f1c81ee5-0dfc-32a3-8761-3aab42e2d020 | -4.10701 | -47.93569 | 2025-07-02 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51a1b80b-b545-3e79-ac99-2ed243708a23 | -7.20935 | -43.08302 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| d62900ea-5885-3442-985c-9661c929dfae | -7.81155 | -44.02982 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| ae56f31d-d1d8-3c2e-9f98-88694e042d39 | -7.20568 | -43.08247 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d011cbce-a41b-32af-bbb2-4ad863b9a80e | -5.62179 | -43.66294 | 2025-07-02 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 850bcecc-f711-3be5-b59d-6f31d9f18e2c | -7.66587 | -44.65852 | 2025-07-02 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25b8b18e-303b-3e65-a67c-e32aa27a9fbb | -7.21478 | -43.09717 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 215e669c-3cbd-3790-ab79-cd3e98761dee | -2.66368 | -47.40238 | 2025-07-02 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19f9d4ca-24f5-38ba-88af-339d5e94d23b | -5.78792 | -43.61509 | 2025-07-02 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9de2c5b2-93f0-32a3-b90e-1da0dae9c66c | -7.81625 | -44.0224 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7236fc5-6209-3881-b5d9-9848728eb069 | -4.03042 | -48.06207 | 2025-07-02 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cea3acdc-1d9a-3708-bef5-be1cdd7950db | -4.37469 | -48.0844 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb9e0bae-3ba9-3672-b333-a700697e3f5b | -7.61542 | -45.74371 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd6497f5-ab24-389a-905c-7f70df822f5a | -7.79524 | -44.01557 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f83394bc-31f8-394b-939c-5ee0b605c991 | -7.79695 | -44.02802 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e7b57121-f02a-3976-963e-b28e951e434b | -7.2917 | -45.37093 | 2025-07-02 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1c992c8-46d6-3f13-b8c0-84203ecbf63d | -7.81273 | -44.02186 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 8e8d4459-5af9-3e4e-a46b-dd183f40f019 | -7.21844 | -43.09773 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3bac7419-3951-38e5-89db-7eced80bcc57 | -4.2877 | -48.1911 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8cc20a1-f658-39c0-b7b7-e4a7bae3e059 | -6.54437 | -55.02797 | 2025-07-02 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
