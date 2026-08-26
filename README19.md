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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43568211-f2a3-31f3-b433-2496aea877ed | -10.7631 | -54.01951 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5ab85bc9-c75f-3304-852c-d155ae4480bb | -12.68298 | -48.39638 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f10deb4-7d6c-38ac-ac79-da3540186bb3 | -10.76241 | -53.989 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92d964ba-0246-3f2e-a0dc-d62e49784be8 | -12.1532 | -50.59846 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66b3d81f-d879-3a9c-8429-94c0e3e47efe | -8.03873 | -45.70192 | 2026-08-26 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 57dcc969-cd03-3ec8-b34e-eefde9fa05f4 | -6.88582 | -43.74653 | 2026-08-26 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62b6423d-7132-3400-a1cd-759c02edcceb | -10.98069 | -43.71179 | 2026-08-26 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2689fc1-3ba3-343d-9795-2b302c09f4f5 | -8.29827 | -47.6166 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54cd291d-cc10-352d-aba4-747741da0218 | -12.68419 | -48.41477 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ee51b234-d84b-398a-8256-61682c91aaac | -11.72031 | -47.77334 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05a4e204-fa67-3d56-867b-16d4a1a51f45 | -9.59874 | -55.11568 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 8d68e722-5840-3a02-88f6-be89555cb288 | -11.75914 | -54.5342 | 2026-08-26 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fba468b5-0b75-3d86-beb9-42717a4fa679 | -6.96332 | -42.10304 | 2026-08-26 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 77260cf5-16c5-3ffd-8356-b50452c27c31 | -7.32056 | -42.9816 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d855e6f2-1bc6-38ac-be8e-bab01e721e06 | -13.35365 | -48.22869 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3a359cef-9405-300d-9cbd-b6de01c9b9c9 | -7.28698 | -44.08561 | 2026-08-26 04:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc7a6302-45d3-3fc7-8abf-f11f07605016 | -7.86349 | -46.10587 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34368a25-e438-343b-abb5-d9b4a5d82487 | -12.75868 | -44.25166 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c96293e8-0fa8-3b0e-99d2-aa3791d920a3 | -11.42178 | -44.53909 | 2026-08-26 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ffdfdef6-626e-301e-922f-d0088ab56ab1 | -7.12394 | -42.78999 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b10f4efe-e405-3560-ad8a-3207c42c4be8 | -9.56561 | -49.26032 | 2026-08-26 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 174e0d1c-2727-38ef-afe3-47f8ca974b3f | -12.75949 | -46.46371 | 2026-08-26 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 303a8cb5-fd3e-370a-8242-4628673648d7 | -7.86255 | -46.10671 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d73d3fd-84c2-3600-9e5e-c087f6ab294e | -7.29135 | -43.027 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eae6a3d6-421b-3d88-8760-c4d8ac2b16fe | -12.15328 | -50.59627 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01083173-3c79-3075-87e3-04a1c2274c49 | -11.28215 | -47.07327 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 107ba9d0-1b76-37ff-bc08-e7a24f09be82 | -11.76705 | -54.52975 | 2026-08-26 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba0672c0-89c6-3f16-b52c-af8f4111de9b | -12.02669 | -46.0242 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e847380-69ff-330c-85a3-21906e0fd244 | -12.0297 | -46.0299 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 74fe908b-25cd-35bf-97f7-b7e145612532 | -7.76042 | -44.76399 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ef2e1c35-9a33-36cc-bcb8-b421da7bce9a | -12.2815 | -43.14149 | 2026-08-26 04:08:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 67bc9510-b626-34bf-9704-a2ba6926e877 | -6.15031 | -53.68895 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40c68db2-187c-320e-861c-e8cc8879192d | -6.26681 | -53.36786 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0791c473-4c21-3df3-a006-089ecab42cd7 | -7.75886 | -44.76136 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9394f43b-84c7-3c33-8322-d6b9e869bfa1 | -12.78122 | -44.26803 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7880e3a9-bce2-3506-81f1-f80dc1c3d388 | -7.06152 | -45.00357 | 2026-08-26 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcf5d3ba-8ebe-3b15-921b-3c4db045e670 | -13.34835 | -48.23108 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74c84b38-b0ff-3411-8d99-4a7552bc68be | -12.65126 | -48.40805 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58de3043-5406-36a6-bdc4-193a1681395a | -7.27358 | -44.07424 | 2026-08-26 04:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 880b61c0-1afa-3920-874b-778d3e450902 | -9.17052 | -49.97612 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8a67ee1-1c75-3760-a1e9-1ab4187cc289 | -12.68593 | -48.40546 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2db7aa9-386e-38fe-bee7-aaf7144f9020 | -12.78191 | -44.26401 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83847552-b3b8-3aea-8eed-205886e5bbbb | -13.33593 | -48.22639 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8a7b1cc-7e62-33d8-803c-6c0e7891dddc | -8.01075 | -51.80481 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2274b2a4-d6cd-3410-bb88-ccbcada95d7a | -8.18302 | -45.22154 | 2026-08-26 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73c5a88e-ef81-3448-9d1a-f1eee0b089c7 | -13.35283 | -48.23146 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6768d089-a934-37b3-92eb-acc74790766b | -8.56456 | -41.59286 | 2026-08-26 04:08:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| b0683618-4360-3458-b894-e9b29d688a99 | -12.76297 | -44.26895 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 857c0b57-7e2f-3082-8157-82e3e9bf6940 | -12.67 | -48.40723 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc281cc4-1a28-3d8b-9f65-1de6a3f593d7 | -7.75959 | -44.76902 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 46c6849b-5642-336b-80e4-c725da8c091e | -7.284 | -44.08052 | 2026-08-26 04:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1c8c3da-de72-3cda-bfc1-0d36c66ce78e | -10.98418 | -43.71239 | 2026-08-26 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d35ade71-72f0-312e-b24f-8665ac50c842 | -10.55901 | -50.43793 | 2026-08-26 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 98c198f9-1d30-39e2-8b94-3889e17adddf | -11.50252 | -45.05994 | 2026-08-26 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc57e692-ccb0-30b5-9304-41d6510de16b | -9.6569 | -48.31577 | 2026-08-26 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90e2b2fb-f080-3f62-aaef-7deb355fae88 | -11.42395 | -44.54821 | 2026-08-26 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8dd7179-9cee-3b70-90c1-d315b60dd0d3 | -7.29903 | -45.36035 | 2026-08-26 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ea5b5c6-beda-39a6-9efd-e3136c32b6d2 | -12.42293 | -42.89259 | 2026-08-26 04:08:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 38c6b452-84ed-31d4-9260-9674ca159053 | -13.35904 | -48.1988 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78065f2d-6e65-3146-8e74-08da97e33a17 | -11.80787 | -47.68785 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91c68dcc-c421-319c-986f-f77de4857fba | -6.27248 | -53.37548 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 462756ae-2ad4-321e-91ae-d2f492cf0162 | -7.26971 | -45.36249 | 2026-08-26 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdc23321-8037-36f2-a30f-ca31b2030e53 | -8.11204 | -47.46997 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b51a00f9-0da1-3682-858b-e6155457a840 | -7.13659 | -43.17591 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0ae5200f-313f-3f2a-aca9-8ee57f89403e | -11.81821 | -47.66135 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7be98f67-5589-3f94-91c6-7235eb919e34 | -11.48911 | -45.09384 | 2026-08-26 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c04944c4-4b50-3f27-bbfb-80a915833ca0 | -10.75952 | -54.03709 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| ddbc903b-635f-3ffb-aa41-58f1c0fb2ac8 | -13.33417 | -48.21106 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f373df23-f970-3843-9609-718613d6bfb6 | -7.30494 | -42.96686 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7d92b7cf-e172-3b17-b4e0-c7462f5642ce | -6.96171 | -42.09135 | 2026-08-26 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d6eafea-337f-3016-b92d-6824a30fa52d | -10.27681 | -40.17422 | 2026-08-26 04:08:00 | NOAA-20 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9492a733-e9ed-3fbf-8852-789f3a75b91f | -12.15851 | -50.59733 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2094a69-6a29-3600-bb1d-3a9ca74733e1 | -8.70923 | -49.60555 | 2026-08-26 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a9060a4-2540-3870-b658-afd468c1bb95 | -6.91579 | -44.6677 | 2026-08-26 04:08:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e897ea1b-cb2f-301d-93e5-8c7cc7a73ec3 | -12.70953 | -48.37844 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ea98e86-3836-3791-816b-21ef8cfac147 | -9.01593 | -50.77457 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3751bb14-9c46-30c0-be67-efdb3519770d | -12.71932 | -48.37561 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ada4e1e-dee5-32a4-93a5-b261f09ba5ab | -7.30538 | -43.00766 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 52576dc6-b86f-3e06-9cb8-b5c63c890b5c | -6.30653 | -53.57653 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8823a207-d7ab-37ea-ad9b-8250415cf239 | -8.16878 | -46.19411 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2d767d7d-471e-3e0d-af1c-63e08d0a3f28 | -11.16235 | -54.0008 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0dbe73ed-cc78-34bf-90e0-78aa216d4f12 | -12.66747 | -48.42133 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5086ec62-c03b-3f13-b1a6-b54139b00bb1 | -7.51202 | -44.95325 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd69e7d0-2666-3c6d-9a59-6632c8e716f1 | -7.86677 | -46.10725 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19bc1e9c-8d16-383f-b066-c38a4dd9812b | -12.79584 | -48.37488 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d840ee2c-7072-3c2b-ab7e-ffb54068a1cd | -8.0682 | -47.53106 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b50d8dc-2f53-343f-a553-8529f0ef96ba | -7.75352 | -44.75785 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 159806fb-0cc4-3183-b8b6-f593ceb9c8e9 | -8.64006 | -54.75889 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0aa330be-714c-3b3f-949d-1786ac0a1f2b | -13.35721 | -48.23412 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3667d0d2-2455-362f-ad31-cfbbe68b3418 | -6.15728 | -53.69042 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9e195d2-f333-33ca-b194-9c11a3e2f4c3 | -7.26407 | -49.86624 | 2026-08-26 04:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91832ef5-1180-3fe1-b089-a8e7324fc85f | -7.30802 | -42.99177 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1f1a83aa-0af4-3111-b93d-f605036c050c | -11.01567 | -45.07109 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 74be6ce2-30e9-3afc-843d-3e8e56ff12ea | -12.75255 | -46.45678 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4224554d-f26e-3f96-8345-6d390e15a0a8 | -12.6684 | -48.41614 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 07c4b3fe-245d-3293-8d27-bf34b2ebea5a | -6.91233 | -41.53083 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 131c20ea-6a0c-3363-b16b-ebe482e81c3b | -9.44475 | -51.67808 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5916110a-e179-337c-aa02-b18d13e0d1af | -11.25061 | -47.05483 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6353b3bd-8497-3c7e-9132-740b9b579da3 | -9.01653 | -50.77142 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a02a141a-b3af-35a2-8946-e2616e275457 | -11.27806 | -47.07204 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README20.md)
