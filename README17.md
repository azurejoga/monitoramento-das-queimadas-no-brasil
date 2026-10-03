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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c65c36ac-7be6-3be7-a073-20fa2fa58ce6 | -11.44059 | -43.39281 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6021ebe-864f-3ecc-8eaf-fb47ab90d47d | -5.71747 | -46.20514 | 2026-10-03 03:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4d9c0ba-e95f-3171-a38d-828198297624 | -5.7391 | -45.16298 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbc3c4d3-296c-3c85-b68f-cf56cc2d07b2 | -5.74113 | -45.15125 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 203911ba-6d8c-33d6-ae90-dcc288ab467e | -11.47996 | -43.40763 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6250519c-02d3-3b78-92a2-a31e8e4d0154 | -5.43203 | -43.44585 | 2026-10-03 03:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b387ecb-2d29-3231-8bef-3ab4e6a02cdc | -5.55551 | -43.96585 | 2026-10-03 03:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63816e29-c0fe-3eb2-b372-75e430c67f46 | -7.01339 | -43.42145 | 2026-10-03 03:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35fdca99-34fb-343e-b577-40dd07842a8f | -6.02279 | -43.59313 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f9b2a52e-14ad-3809-955e-5c9db1c55ac7 | -7.53337 | -46.64478 | 2026-10-03 03:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72fca8bd-974f-33b4-84f1-0be72293a5c6 | -4.4064 | -49.96849 | 2026-10-03 03:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17773dd6-65fa-3b2a-9e3c-a72cd62de7ef | -6.9035 | -43.68557 | 2026-10-03 03:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0264d04-dc09-3848-98a5-56585e5e2a8b | -12.85126 | -44.68468 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b7000725-f533-3665-8bc4-07a4329bf906 | -4.40354 | -49.97666 | 2026-10-03 03:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b56611bc-c82e-3259-9362-cf016679f5aa | -6.4163 | -45.86011 | 2026-10-03 03:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e396e66-f653-36e8-9992-217f4382153b | -9.72191 | -36.10634 | 2026-10-03 03:55:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 1feca956-8566-38bf-95b9-5804b8a1bd14 | -5.94763 | -43.65118 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d3c7e25d-7987-33ed-a952-b936d391bbcc | -5.9431 | -43.65038 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2820b6c3-b64d-3948-9ff3-9873614d5309 | -9.45974 | -40.37029 | 2026-10-03 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 3c07a005-7850-3f8e-9bc3-0a8c1aa1743c | -5.74177 | -45.05807 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b59e021-b5f4-30b6-843c-cd363dd1d9e8 | -11.45214 | -43.39869 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2620a408-6cc0-39b4-ad00-ae31a229c069 | -5.74262 | -45.14264 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad9ca97d-35cd-3973-93ee-7156ade0a052 | -10.28297 | -36.78118 | 2026-10-03 03:55:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7d695a12-21d6-3952-a6c9-a3a88eb2698d | -12.97663 | -41.17894 | 2026-10-03 03:55:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6db587cc-4a9a-35eb-9d18-04af6899d603 | -7.22443 | -46.04964 | 2026-10-03 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 031560ca-5fd8-31ea-a024-945a73f695b5 | -5.94229 | -43.65501 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 230f4226-4f05-3aa1-ad3a-4681899afbaa | -9.52761 | -35.75146 | 2026-10-03 03:55:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e088ea57-bcc7-3959-a359-48d47330965a | -9.46041 | -40.36628 | 2026-10-03 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 211aa48c-bea5-31d1-8eec-c1f75afca5ef | -5.94972 | -43.66598 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| efd2370a-366c-3e25-9ef0-c5a8bef91799 | -5.94391 | -43.64577 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 0fb0b681-e787-3e78-ada3-0f31a7f9bc7e | -12.86389 | -44.71344 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6768212e-6830-3024-b9c2-3ca36dcfe932 | -6.5022 | -41.74153 | 2026-10-03 03:55:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6317d214-2a79-3b45-ad4c-7fb1550e620b | -5.9524 | -43.64423 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 33c53a40-5953-3031-97d4-b5f7651fae64 | -6.15825 | -43.68662 | 2026-10-03 03:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d6a3c28-b5f7-30ea-9dff-d4325b9a2cb9 | -5.94518 | -43.66521 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 50c27954-b9ff-3f86-8e7c-e3f059e15aad | -12.8548 | -44.68975 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| dae04285-1a94-319a-b0d9-a35e10742295 | -5.95055 | -43.66126 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 51ffc2cd-17ea-3892-b958-206794a228ab | -6.50529 | -41.74729 | 2026-10-03 03:55:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 78aabca0-ceb7-3a60-9c5b-e5695dc6a1f3 | -7.12736 | -41.32857 | 2026-10-03 03:55:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7bd1685-29d2-308d-bfc0-940af043faf3 | -6.62991 | -39.76991 | 2026-10-03 03:55:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 526306b7-34f2-36bf-8cd1-01b869c710c9 | -9.45621 | -40.36969 | 2026-10-03 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 24.6 |
| b18d6e0b-9b4c-3b5e-8107-1aeee5f3a6f6 | -5.94929 | -43.66296 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| c55ca483-3dee-39ae-ae4a-56512ad8318f | -4.41172 | -49.97123 | 2026-10-03 03:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 692eef12-ec3e-3f6e-8408-afa431387474 | -5.946 | -43.66051 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 5b5b6f48-caff-3580-8f5d-7522d2c08f0e | -10.89963 | -43.83886 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c68d0444-a236-3b93-81cf-3dbe1e1f56b7 | -11.79174 | -43.58463 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3307100-71c5-35a2-926f-2671696be0e7 | -4.39825 | -49.97394 | 2026-10-03 03:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d3d25b4-3d55-3795-8149-77863870a256 | -5.73627 | -45.06 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4a176e8-e40e-32ce-af27-6a08a913ecff | -5.7381 | -45.13877 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a656bf90-30c5-3fb7-9bde-7a449330bc7a | -5.95162 | -43.64892 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9752d184-b24c-3fe3-95a3-221ff762f9f9 | -11.82743 | -43.56857 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d3e6a1ee-0239-3280-8860-4f665362b427 | -5.73509 | -45.15613 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02111311-ec65-3cd8-a7ea-2184e5bf91d8 | -6.74263 | -44.14322 | 2026-10-03 03:55:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 03d5dd79-4310-3af5-b95c-4c89f0950d16 | -5.93994 | -45.40183 | 2026-10-03 03:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61baf7cf-c32f-32e7-9c40-4821d9845e61 | -6.02202 | -43.59766 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c09807c9-48a8-307e-997a-bf5682f00034 | -12.85557 | -44.68555 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 98913371-99b5-3c3e-9a6e-4d13bd32c430 | -5.95298 | -43.64726 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b4e37b80-8c8c-3e4c-84bf-6f823df07ec9 | -9.72247 | -36.10268 | 2026-10-03 03:55:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 759523d1-fb3e-32af-b88c-d5ff0af16dca | -12.85911 | -44.69061 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 88cde1c2-deae-3903-b3d2-c654273f9f92 | -10.36298 | -39.49537 | 2026-10-03 03:55:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd3b77c3-f8df-3745-97de-8b7c331300d2 | -6.92707 | -49.62615 | 2026-10-03 03:55:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4353a35-f117-30fc-a6a3-baa475e47c40 | -5.19577 | -46.16407 | 2026-10-03 03:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15d6c3a3-ff76-354a-8a44-58a1c783f6d4 | -5.94255 | -43.64738 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 9db48478-9090-3e15-8d94-f09f0354eab1 | -9.45335 | -40.36509 | 2026-10-03 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c2f33d91-5ffe-318f-8d63-a2215e1103f7 | -5.61343 | -44.38006 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fd4e6309-c90b-3fe6-bf57-68b7c787e5e1 | -6.92051 | -49.62487 | 2026-10-03 03:55:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34e859cf-ea4c-39f0-93f1-64dfff1f8895 | -6.33688 | -43.36185 | 2026-10-03 03:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1a44e082-dd15-359c-9cfd-0d7e824d3171 | -5.94178 | -43.652 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d55bba1f-cd34-305d-b7e4-af48e026bb92 | -5.7356 | -45.15319 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06614fb8-01b9-39a7-a86e-ac73dfcfd353 | -12.97799 | -41.17082 | 2026-10-03 03:55:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 06f2797c-5cf7-36e6-9303-6dc539cbe8fe | -5.40506 | -45.19062 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52abf777-a5e7-3c4a-9c44-64a25aae68ca | -11.79914 | -43.56646 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d96e6b32-77a9-32d6-ae99-ab31e6f12786 | -5.61824 | -44.38083 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0ce49593-9ab9-3152-9f0a-5c45a63f14f3 | -12.85049 | -44.68889 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2db23554-0867-3d56-bc3f-155438d9e4c9 | -11.48339 | -43.41204 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb7010c1-36ef-3375-853e-d489c674c68d | -5.43123 | -43.45043 | 2026-10-03 03:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4830ab72-4b8d-3834-b799-fbe03e980aae | -5.17152 | -45.41675 | 2026-10-03 03:55:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a64096a8-7584-323c-b0f5-5c34b33e84f6 | -5.75637 | -42.3454 | 2026-10-03 03:55:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9e675fe-a22d-380c-86bd-fa123157efc2 | -5.79856 | -43.61092 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5c49297-ed09-356f-9291-a7cf6377222d | -4.80609 | -49.87299 | 2026-10-03 03:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce5ecd16-1a18-3bc0-b13b-9c59b52cccd8 | -11.64924 | -42.41153 | 2026-10-03 03:55:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2cb0fd1f-a3e6-3c2b-aeb9-f93c5c041571 | -10.36237 | -39.49905 | 2026-10-03 03:55:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52f28f0e-d34d-3904-86b0-2b4e2b0110c6 | -6.50442 | -41.75241 | 2026-10-03 03:55:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e8eced2f-0d43-339d-880e-098b5dd84a01 | -5.13265 | -45.58062 | 2026-10-03 03:55:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8dafe0b1-0f7a-35e8-b873-a0956985af1a | -5.74063 | -45.15411 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 544e438c-17c1-3e7e-936b-5cd381010d04 | -5.94786 | -43.64349 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 12f82955-2123-3d6b-b5fb-9ea8bb947894 | -7.88916 | -44.18747 | 2026-10-03 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ec591be-94e0-3e1e-8922-c55b00d86ad9 | -5.96125 | -43.6534 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d209c306-1bb3-35ec-a68d-af8f23348953 | -6.59366 | -43.50084 | 2026-10-03 03:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5795879d-6735-3c15-a971-6f74e16548d4 | -5.7475 | -43.27198 | 2026-10-03 03:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc4a2d5b-ea99-3a17-bae9-a2339978c557 | -10.2221 | -36.5626 | 2026-10-03 03:55:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 50849c8b-3302-396a-83d0-58b8c73f16ba | -5.75219 | -45.14733 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d13e675d-9437-3280-8df8-95dfd8852a05 | -5.55381 | -43.96243 | 2026-10-03 03:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d227f5c0-b588-3d52-8ae7-b2c32d0944e4 | -12.96335 | -41.19326 | 2026-10-03 03:55:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b683df87-e08d-3ac7-85af-7a223e66364d | -10.36636 | -39.49594 | 2026-10-03 03:55:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e82bcbe8-6d10-3294-bccc-5c884b08f957 | -12.86311 | -44.71768 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| aca5a18f-cfb1-34db-be22-ccebd1d8e9b9 | -9.46747 | -40.36748 | 2026-10-03 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f3194cb3-8857-3c4a-acf2-2a4a85a925da | -12.96267 | -41.19733 | 2026-10-03 03:55:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 8c9ca571-55ad-34a1-84fc-053c730f2910 | -6.15739 | -43.69154 | 2026-10-03 03:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad48de5f-fec6-3dc4-9340-b49b516e21ba | -5.75269 | -45.14444 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
