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

## Dados Diários - Página 306

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4025d16-0d4f-3054-af92-c93df491de2a | -14.98913 | -42.66689 | 2026-10-08 16:35:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7c3e55a3-a780-31ea-8f82-4345dcb7d16e | -14.07046 | -40.33654 | 2026-10-08 16:35:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 5b4623a3-b2ec-3812-ad80-f73a4b8ba9b8 | -14.7379 | -40.28786 | 2026-10-08 16:35:00 | NOAA-20 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| c424c720-1431-375d-9bd0-9a516ce2c9a6 | -16.112 | -48.43002 | 2026-10-08 16:35:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db69415f-f642-3784-85be-a3e104ad1cb2 | -14.55338 | -44.07394 | 2026-10-08 16:35:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 47.4 |
| f45c01fe-0617-3c42-8bb8-2782ac6d3795 | -23.16481 | -47.03134 | 2026-10-08 16:35:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9bca03c5-f30c-3bd2-a65f-702ac1c83af6 | -15.34092 | -41.0479 | 2026-10-08 16:35:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 549a5a57-764d-3c3f-b851-a47644cadec2 | -15.34024 | -41.04377 | 2026-10-08 16:35:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 2e1ef640-edd3-3a60-9a77-e7660c26649d | -15.39998 | -44.3326 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8d7c624c-ecc2-3262-9a81-1b2b82d91f3c | -17.19611 | -41.41298 | 2026-10-08 16:35:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3f95feb0-4b0b-3397-b427-36c6830a7969 | -16.9323 | -42.10664 | 2026-10-08 16:35:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 61dd95a0-f21f-3f97-a3ec-9cee8d018326 | -14.02772 | -44.03037 | 2026-10-08 16:35:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 83d0ef26-906a-336f-9add-3e640f0b0b85 | -15.26402 | -42.34631 | 2026-10-08 16:35:00 | NOAA-20 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| db23c360-5ff9-3b82-86a4-d46775530a94 | -14.53382 | -41.67254 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 3f3edca2-1362-351e-9e1a-b509e0c4619f | -15.34668 | -48.04375 | 2026-10-08 16:35:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 8ad8d2b6-39a0-37ab-a355-97606d6d102e | -14.4663 | -40.72262 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 38.7 |
| b3974e3f-45a4-3a72-944f-373a23c8101d | -15.83603 | -48.18619 | 2026-10-08 16:35:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 488d1d9d-e969-3da6-a99b-41aa9c7ebc50 | -14.44578 | -43.92442 | 2026-10-08 16:35:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9a32a9c9-5d67-3502-b690-bb5164fd1d99 | -13.97087 | -44.84007 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| c1e1b48f-74dd-313d-a335-1dd3c5e9f879 | -15.62732 | -40.13209 | 2026-10-08 16:35:00 | NOAA-20 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 185.3 |
| 9fd8e29f-c741-34d5-96d8-c11b04eb5fe8 | -16.13926 | -49.42094 | 2026-10-08 16:35:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c259de05-18be-3cff-8adc-841a885048d8 | -14.53947 | -41.77244 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| f230a8aa-332f-38ad-a644-1a81f717654a | -16.92616 | -42.11153 | 2026-10-08 16:35:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b32fe264-554a-3883-9699-a618151038a2 | -17.38687 | -52.11546 | 2026-10-08 16:35:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18e913fb-5722-3c15-a1a2-de393350d05b | -16.90709 | -50.3013 | 2026-10-08 16:35:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b708ba24-40dc-3e62-8bc9-9ea916cbc70f | -16.58252 | -49.62428 | 2026-10-08 16:35:00 | NOAA-20 | SANTA BÁRBARA DE GOIÁS | GOIÁS | Brasil | 5219100 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 788f7d81-37ed-3d45-8982-3ca070717f30 | -14.20486 | -40.48669 | 2026-10-08 16:35:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ade69441-8a11-3e3f-afdb-9bd29c5fc779 | -15.87675 | -40.76265 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9dfdbc07-d345-352f-8fca-13b5488390c4 | -14.62967 | -43.6861 | 2026-10-08 16:35:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d34e1436-d01b-3709-850c-698ae170b98e | -14.78821 | -42.83541 | 2026-10-08 16:35:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2e0965a8-5857-3f92-90a5-5e87cf7754cf | -15.04473 | -40.24041 | 2026-10-08 16:35:00 | NOAA-20 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 30456466-cff2-34dd-a70c-0f62188aa6b0 | -16.31615 | -44.56428 | 2026-10-08 16:35:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 113.9 |
| d83c551c-4260-35d5-bf68-a6bdc2c4c8a3 | -16.01239 | -40.66083 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 938eb7ba-094c-3935-bd58-5fd92695ecf9 | -13.42384 | -40.8361 | 2026-10-08 16:35:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |
| f90f4922-34f4-34b8-ab99-08cc285c33ad | -13.94977 | -44.85804 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| f725c50a-4f61-3ce9-b4b6-c783bcccf90f | -16.58472 | -39.63546 | 2026-10-08 16:35:00 | NOAA-20 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 846ffd17-f54d-36e9-9cea-2557bf0bcb67 | -14.42727 | -41.1373 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 29.7 |
| c3340a20-38e8-3ebb-aa5f-1e8df7bd98f3 | -16.15612 | -43.63863 | 2026-10-08 16:35:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3cdcb73a-b1bd-3464-a865-b05ca897b8ee | -15.10934 | -41.11673 | 2026-10-08 16:35:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d0b268dd-f629-3c76-acd2-93e9bce6389b | -14.46277 | -40.81174 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 4033bb39-850d-30f4-8138-62d4e4eadaf3 | -15.69236 | -40.47161 | 2026-10-08 16:35:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| b4fb7540-2e64-3f24-a60a-dc3651163ee8 | -16.95384 | -40.05754 | 2026-10-08 16:35:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 206e7579-23be-3ba5-adf8-55c9691ed65c | -15.51722 | -42.6559 | 2026-10-08 16:35:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 5517a686-43b5-349c-aef8-30ddcb6ce78a | -23.12371 | -52.33385 | 2026-10-08 16:35:00 | NOAA-20 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 58ce124c-c3ba-3b4d-ae58-4e705dc4728b | -15.57142 | -44.52551 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 97cbc77f-48da-3cbf-8f0f-921769cae177 | -13.98469 | -44.84155 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fbf99273-19b3-38fb-aa03-b9706c1437f2 | -16.37324 | -39.80436 | 2026-10-08 16:35:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| f90340c9-a71c-3738-b721-ffdd0707a26e | -15.68771 | -40.77997 | 2026-10-08 16:35:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c550c4fe-f495-3263-be23-84c9977aa794 | -16.90995 | -40.88953 | 2026-10-08 16:35:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 2c68464c-c075-34e6-b79c-5ca81c027195 | -16.01313 | -40.64323 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 7ad0daf3-5e56-3e74-9142-0d90cd5d3b82 | -14.90189 | -40.54772 | 2026-10-08 16:35:00 | NOAA-20 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| a2c3ccdd-9257-3657-aa2b-617c48dd2c7d | -16.45388 | -41.26958 | 2026-10-08 16:35:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 60f22627-3784-3452-a47d-c8df54daa968 | -17.1053 | -41.34974 | 2026-10-08 16:35:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 225b6b6f-4d78-39b0-8826-657ed0a919c0 | -16.15349 | -43.11649 | 2026-10-08 16:35:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2e61bd7f-57c9-3ff4-a396-c61b47f63753 | -16.1946 | -44.56866 | 2026-10-08 16:35:00 | NOAA-20 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ea58e956-fa7c-32bd-9d58-b94b6834a176 | -15.34377 | -41.04315 | 2026-10-08 16:35:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 4e1e83ac-4a0e-308d-8698-070b436a84cd | -16.55258 | -49.91156 | 2026-10-08 16:35:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1ca7eb8c-4985-3092-bf84-9a5b643e9337 | -14.43494 | -40.80639 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a636eeb0-4d84-3bd1-9970-598191fd3f62 | -14.45445 | -41.23476 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 1313d6a3-75e4-30d0-a790-a966f3fe419a | -16.48891 | -41.80888 | 2026-10-08 16:35:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 5457d07e-e6c4-3519-aafe-90f38bff0c64 | -16.76453 | -40.99306 | 2026-10-08 16:35:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 8da59ffc-c8b3-36f7-ae50-5711aa4cd00f | -13.7445 | -43.51561 | 2026-10-08 16:35:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7178d5e2-6306-30a9-bfc6-de25c032aaf9 | -21.51321 | -55.0854 | 2026-10-08 16:35:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 739d6371-aa9d-3c24-9d0e-0a9b1ae57455 | -13.34088 | -38.98483 | 2026-10-08 16:35:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 7fd3d300-0212-30a5-8f03-81ca42277d2a | -15.56036 | -44.51987 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 41abe5f1-7702-3398-94f9-b4eae2052ae8 | -15.11325 | -43.63071 | 2026-10-08 16:35:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 4ccf2984-b3c3-35a5-8c4f-e630b8ecfe48 | -14.11313 | -40.27162 | 2026-10-08 16:35:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| a955b6c1-7069-3fa1-a2c3-093e6a7e028b | -15.11103 | -43.63839 | 2026-10-08 16:35:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 111.7 |
| f061a113-51ab-3067-87cf-9e485313c26e | -22.66687 | -46.77783 | 2026-10-08 16:35:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| af8e38c2-c6d2-3f47-9367-5b1eac6d6182 | -14.95316 | -42.00785 | 2026-10-08 16:35:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 4cb20726-0d88-3ebc-8671-cfa2eed5ff58 | -14.26755 | -40.70129 | 2026-10-08 16:35:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 74199f14-278c-37e7-b7ea-57e3be0bd64a | -21.06117 | -44.48293 | 2026-10-08 16:35:00 | NOAA-20 | CONCEIÇÃO DA BARRA DE MINAS | MINAS GERAIS | Brasil | 3115201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3bfc3763-93ce-3935-a996-03f4b8692188 | -16.73652 | -40.26068 | 2026-10-08 16:35:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 068d773c-8d98-37ab-a90b-6e489fd19bb0 | -18.04265 | -49.56183 | 2026-10-08 16:35:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 35bad8ed-00f2-3938-863a-0cf45d4ac643 | -15.57246 | -42.89656 | 2026-10-08 16:35:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 66e775de-2a12-32f4-a169-3ab0641b67d6 | -17.11435 | -41.34031 | 2026-10-08 16:35:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| cabe386c-dc82-3fe3-b969-cd87d5798d42 | -14.73575 | -40.2976 | 2026-10-08 16:35:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 9fb5aa7e-ad7f-374f-ae52-e2469cb2e5be | -14.26224 | -40.46735 | 2026-10-08 16:35:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 4f2ce4e4-e820-3192-a705-f84210f3856c | -14.85252 | -40.79118 | 2026-10-08 16:35:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 0ea22d46-dc10-3deb-8526-9faa47c78a07 | -20.98193 | -47.0408 | 2026-10-08 16:35:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 41da6518-c400-3e0d-a88e-83df40159048 | -17.4521 | -45.06003 | 2026-10-08 16:35:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 991f0758-5039-3ea5-a242-9571a6bef67a | -20.57866 | -43.08154 | 2026-10-08 16:35:00 | NOAA-20 | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 2d22f004-4a5a-3f87-b4a3-34ace6aaaede | -14.48006 | -40.71569 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d327c4ec-89e3-3356-aac1-21020a86589d | -18.44755 | -51.0267 | 2026-10-08 16:35:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 9f429c25-105b-386a-9ea3-f43fb5249992 | -15.70781 | -40.59136 | 2026-10-08 16:35:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 3757b00d-6b0e-3025-876e-ce695e782620 | -16.24859 | -41.73338 | 2026-10-08 16:35:00 | NOAA-20 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 092b1af0-5e89-3b0f-b850-ec1055457694 | -15.57034 | -44.51828 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fb6c1297-f90a-30dc-85f8-31fcccd76252 | -15.39165 | -44.34494 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 40.3 |
| c6c7cb33-4a20-3060-a42d-deb6a92e2d1d | -23.20161 | -51.557 | 2026-10-08 16:35:00 | NOAA-20 | PITANGUEIRAS | PARANÁ | Brasil | 4119657 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7fbe4fc3-56a7-3b90-a539-1868d92c18c4 | -15.56864 | -44.52964 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 519c644f-d481-38ec-a43b-598da00dc3f8 | -14.05347 | -43.8226 | 2026-10-08 16:35:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| b3ad7f9b-36be-3419-8918-11b32e0e5788 | -14.56203 | -41.27179 | 2026-10-08 16:35:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b7c91593-f08e-385e-b9e0-68d6d32f49c0 | -14.09675 | -40.05962 | 2026-10-08 16:35:00 | NOAA-20 | ITAGI | BAHIA | Brasil | 2915106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e0be99f6-2e92-3410-abc9-5c699a2285c2 | -15.10994 | -43.63126 | 2026-10-08 16:35:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 168.4 |
| b506aaf4-65d1-34d6-a7d9-754eaffd42a6 | -15.76296 | -50.32646 | 2026-10-08 16:35:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ea0526e2-acdc-39c8-b670-a602909355a2 | -14.77478 | -47.14554 | 2026-10-08 16:35:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3efafc9d-a798-3d07-bf50-89f2ffefab9b | -14.8368 | -48.35183 | 2026-10-08 16:35:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| bbab9a56-c831-3691-9319-0060404091e4 | -17.02772 | -41.97906 | 2026-10-08 16:35:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| ad03c0ea-b65a-3474-8d6b-1b139f414686 | -14.44297 | -40.78749 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| d850e13d-1556-3b91-bb37-c92a4164e74d | -14.53671 | -40.67189 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README307.md)
