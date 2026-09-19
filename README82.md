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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b66ff2f5-a506-383c-af24-7dda0ee3b3d9 | -8.71859 | -44.87106 | 2026-09-19 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dc4f7e5-c75d-390a-9bcd-f322aa7533d4 | -2.90458 | -57.79277 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c2204596-c2cd-3a2e-8dbe-af78cf3f6599 | -9.78666 | -45.04382 | 2026-09-19 04:57:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95ea8405-dd1f-329e-9a0b-c380e65f6d48 | -4.42751 | -55.51357 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba1d5293-0ec0-3034-8144-d9c2bb2ae9be | -7.5757 | -57.69162 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0fbe64a7-6e03-3d71-9ed9-5c144fae8a9a | -3.35271 | -59.85947 | 2026-09-19 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4692cb24-ca50-3eb4-ad17-3e83cfca02f9 | -9.80491 | -48.33727 | 2026-09-19 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa39f98c-0d04-37d8-9a2d-3b6fb6578893 | -6.93859 | -55.04358 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b026787-1616-33fd-87ee-c2a9c1d9fae6 | -9.83845 | -48.39434 | 2026-09-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2db0e626-843e-39f1-8954-b5a28de50868 | -8.61017 | -54.60649 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ef5455b-10f0-3647-898b-2c5f1479ae84 | -9.58111 | -55.10227 | 2026-09-19 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3858184-aff4-320d-9d1e-431c45ca6a59 | -6.73818 | -59.42246 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20440ba4-054e-3677-ba6f-3e63612d5fb3 | -4.42549 | -55.52626 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5900b9c2-532b-3062-9edb-c6928799f631 | -4.53498 | -54.93157 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cd63747-7cab-3b7e-ad9d-6b91bd9f26fe | -8.42132 | -54.72759 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 42ba7ccf-f894-3214-ad7c-6712c45b3f15 | -10.79448 | -50.88231 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abcdc9b2-b598-3f16-be6c-5332727c2f0e | -3.36764 | -50.44179 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84a04d12-addb-3405-a125-43b84bdce284 | -4.47747 | -55.0881 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc868a52-4f77-3e55-9ea4-871ba88a4d37 | -6.57921 | -44.15451 | 2026-09-19 04:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3071dfdf-6139-31ac-8612-f2b22c8a7f4e | -6.30591 | -55.92102 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e654de62-8820-3c2e-ae93-0f7fce8ef60b | -5.76108 | -57.45296 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 06e383f6-bb8a-3cc8-9d3d-9fe08e417c52 | -10.48794 | -46.29692 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acc74a05-82eb-31f2-8dc2-8259cf492bf2 | -8.3596 | -47.24148 | 2026-09-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00495c56-e6db-3ada-a009-7723762523ef | -10.53464 | -46.73426 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ddffb7c8-a74b-30cd-bf24-580c53b372a4 | -7.60957 | -57.61063 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 885df65a-4473-3a0d-8130-58f860df549c | -8.12331 | -44.82591 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 977e21a6-9d3d-30aa-8246-7b711814c3f8 | -10.99296 | -48.32115 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5f199f5-7173-3e2c-8da4-53c0c44c69f5 | -8.6125 | -54.59217 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b46261d-ee60-30aa-95b3-9a5ecd3a367a | -10.18131 | -48.52196 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1f649e5-1d3d-39ad-a785-564cf0737366 | -9.68168 | -48.32907 | 2026-09-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c0d34e8-2df5-3868-ab92-4d7a7adcf314 | -5.86021 | -47.27854 | 2026-09-19 04:57:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf7c6930-f0dc-3841-aba1-9292cba978b6 | -3.32897 | -59.82283 | 2026-09-19 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b96dddf-8899-3273-881a-9aa9fa29a234 | -6.7719 | -47.8613 | 2026-09-19 04:57:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be59113a-74cd-3106-9db7-f0bc826aad16 | -10.92227 | -48.41792 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54e1240a-c43a-39e1-903b-23f92690a30d | -6.93134 | -55.02312 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51fec53d-a6fa-3177-a8e2-024aef7da6a4 | -2.96083 | -57.71384 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b196787-8782-30f6-b09d-6aa80523e73e | -4.06537 | -56.24974 | 2026-09-19 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d42348c0-a9eb-3fda-a07a-3feea84ab8f6 | -6.0013 | -51.79057 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 442afa8a-36b5-32bb-89cd-ebceeaea5db9 | -10.52383 | -44.85144 | 2026-09-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 615bb3ae-cfa8-3569-b380-48e66d32f013 | -3.15114 | -53.93454 | 2026-09-19 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c60a60e-5a25-3d26-81c2-2f8f8d6a83eb | -10.36578 | -48.89416 | 2026-09-19 04:57:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd2ab04d-432d-3d2c-b068-35aea087bd67 | -9.92875 | -46.58578 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2473d5ac-e3df-3412-8bcd-64491fd6e207 | -4.77149 | -55.70594 | 2026-09-19 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5042c74c-36ad-3f2f-bee2-0b82131128ea | -2.95937 | -52.14554 | 2026-09-19 04:57:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e4dece0e-4bef-3383-96d1-03c2f0fe61cb | -7.40093 | -49.84456 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5eed8185-e451-3387-8c52-fd1600781332 | -3.15056 | -53.93822 | 2026-09-19 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a04f899-bbaf-36f8-a34e-3229ac29a003 | -7.86779 | -45.12209 | 2026-09-19 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68cb8287-24d0-376d-85fe-56b397f81852 | -11.08393 | -48.2788 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 91d861f6-822e-3b7d-af56-4a895851fb01 | -3.34131 | -59.80846 | 2026-09-19 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ee13de7-0f0c-3ecb-9f0a-5b4c8e64d80d | -7.02389 | -44.65273 | 2026-09-19 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9c185fe2-fb3c-3c6e-8ab4-388775175fa8 | -10.99664 | -48.32514 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 24c9082f-32f8-373a-a283-912749c9a868 | -3.45369 | -50.60695 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 26a9de73-5497-3096-9a8f-06faa3216f8c | -9.83922 | -50.65269 | 2026-09-19 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2eb7d6eb-21bf-38ed-9afe-1a2385de9d49 | -10.83452 | -50.92524 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ba8aeee-e31b-3fbd-b492-1718d2d0dc7b | -8.3717 | -47.21816 | 2026-09-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49c4fa6f-6ecf-399e-ae63-868124325f0e | -11.1219 | -45.30427 | 2026-09-19 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5937e18d-8a6d-35a7-9108-4646d54a1303 | -8.45155 | -54.75486 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40a055e7-5bf2-30c9-a10c-8bd7152fd1c3 | -9.94087 | -53.98471 | 2026-09-19 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9572c651-ead2-365a-94f5-eb66c8f5740e | -8.32898 | -50.86066 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40039d2f-5f2d-3d44-b335-d794392c8e62 | -10.53339 | -46.74157 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 4ed0b24f-31f0-39b4-b34d-3ff44779ddfe | -10.53663 | -46.75362 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10a88360-e707-352a-97ac-5217e07e8736 | -6.66266 | -50.90099 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76d78926-b408-3380-b152-b4a5b43620d6 | -5.87028 | -52.03902 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3050f4bf-61e4-3dd3-a6f7-6dff88b0db58 | -9.35947 | -48.28902 | 2026-09-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d679a453-26a1-3070-977f-768b9a638853 | -10.80396 | -50.89214 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2a003f4-aa28-3a12-a50e-d12d9862c1dd | -4.30087 | -56.25544 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fd16cd3-f663-381b-bd33-bef1366d7ea8 | -3.26697 | -54.2614 | 2026-09-19 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2261b140-7547-3cc5-8fb1-5b642b9f638a | -6.15912 | -62.62846 | 2026-09-19 04:57:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bf6de13-9902-35c1-9ed2-4ad227f72ebd | -6.47301 | -57.88382 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 212aef3e-69a5-3791-9223-45523df27cd4 | -3.83601 | -49.12992 | 2026-09-19 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96a81e78-cc94-3466-858b-e0778f680044 | -10.44924 | -48.68 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee95b2aa-495f-3393-a5aa-39e57a0fb798 | -9.92809 | -46.59339 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 986f6896-c582-3d61-a9fb-c083be2e174a | -4.42616 | -55.52206 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ed4fdd9-d4f9-3ae2-899d-b21887fa86c2 | -7.00719 | -49.75927 | 2026-09-19 04:57:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ffcef55-4c49-3b51-be25-3af3cdffebbc | -3.37553 | -50.45794 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e2f9cf4-3028-3dd4-afa8-25c09a8f23d6 | -5.86588 | -52.04541 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7729639b-a610-3ccf-a075-0b3ee162605a | -4.44252 | -55.0134 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cd91c72-b1d3-35fa-8377-22b47b5e52b3 | -5.38529 | -50.17673 | 2026-09-19 04:57:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5064390-3f01-3c12-afa8-0c577267949e | -8.89118 | -62.44225 | 2026-09-19 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d52bf2c-dc75-3d01-83f8-737381ebae19 | -6.33851 | -59.9598 | 2026-09-19 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5926c035-0884-3ba8-a295-b86c033bcceb | -8.14593 | -54.8059 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b845da84-15c8-3ec3-aa2f-71b28b325509 | -7.75122 | -54.75024 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5be3582f-4e4e-340e-8c1f-3319ae56b94c | -3.36138 | -50.45949 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11668493-60e0-3873-89ce-88772e2499a4 | -6.43853 | -59.97931 | 2026-09-19 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5ae92657-4eac-31cc-8a05-3d7f87c33fc4 | -7.56008 | -61.33319 | 2026-09-19 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6e3a25f-369a-3756-960c-0197341e0dfe | -5.22211 | -49.30695 | 2026-09-19 04:57:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5dacb24-34e5-3b0e-9376-ab1d97178110 | -5.86702 | -52.05982 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b911385-3714-3d82-a137-d98952978e2e | -9.49824 | -54.6655 | 2026-09-19 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5043198b-a173-34b5-bf3c-c674f3f3f9d3 | -11.33773 | -47.36433 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82bc9af8-a86d-3122-b222-585627a1261b | -8.23705 | -45.59872 | 2026-09-19 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e49793c0-4fcb-348c-83d0-88e4e42a21c4 | -6.61917 | -57.98085 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3edfb604-2de1-3fee-8fbb-391e9cebaa85 | -4.50642 | -54.97521 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7270470f-1add-38b2-953c-7d183f44ca96 | -10.93241 | -47.91233 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1870f861-dc08-33cf-876e-db3002072aa1 | -6.25448 | -55.43481 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a53d6bb-68bd-3d8d-80a3-0d788526122b | -4.51219 | -54.98415 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e4e41c1-4d0a-3a0a-8087-e3173ee1a35a | -3.03144 | -61.2429 | 2026-09-19 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0e1fa64-29c5-3d60-859d-85cb4e2fcc91 | -7.75402 | -54.75444 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33104106-a811-3fd7-88b5-3edd715be3ee | -5.86159 | -52.05152 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3c4d500-0f2c-365e-bd52-cc20955d87c5 | -3.37703 | -61.30423 | 2026-09-19 04:57:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb3bbd02-382e-3fef-bcb4-d47c40e8be2b | -3.48518 | -49.50874 | 2026-09-19 04:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README83.md)
