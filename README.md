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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffaca7c8-b5ab-358f-9760-1fee9a38cf12 | -11.1712 | -55.9319 | 2026-05-23 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 691863e3-df9e-3077-9aa2-542034cffec3 | -11.1714 | -55.9117 | 2026-05-23 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| e2728aef-8f93-326b-8f6d-39014d569a0b | -9.3045 | -45.4809 | 2026-05-23 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| e02e10df-e794-3f27-a395-e6f56feedec4 | -11.1903 | -55.9101 | 2026-05-23 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| e03f080f-24a3-3a0e-9742-a3663789a1e5 | -11.19 | -55.9303 | 2026-05-23 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fc82112c-61ac-360b-a84b-29292391ab9a | -11.4534 | -52.9212 | 2026-05-23 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| ebf64d3c-014c-379b-b61e-bfd880c76ef7 | -9.2855 | -45.483 | 2026-05-23 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| da43c778-8fa8-390c-b16e-f6b461c62249 | -9.3003 | -45.5051 | 2026-05-23 00:02:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74d66661-6f0c-3631-9507-13a3a6d0aeb1 | -11.5784 | -45.201401 | 2026-05-23 00:02:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37a48bdb-8d04-3181-95d9-aef2160540dc | -10.4848 | -42.417599 | 2026-05-23 00:02:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8f2b7c43-090a-3b19-bb1e-b8d55d56c401 | -5.9509 | -43.497799 | 2026-05-23 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 746472a5-d573-31fc-b76d-d12b4cd3809a | -11.7371 | -38.535801 | 2026-05-23 00:02:00 | METOP-C | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| de4a91fc-e5c6-33c4-8bac-a85a075106a0 | -6.3896 | -44.184299 | 2026-05-23 00:02:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2970519-6b6b-37cd-8457-7f5c543a9a8e | -11.9259 | -43.868198 | 2026-05-23 00:02:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3313d287-e3bd-3acf-95c3-1a6dc693a604 | -4.4771 | -37.821301 | 2026-05-23 00:02:00 | METOP-C | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7eb02fcb-98d1-3afb-9cc9-1af7bfc5e8a7 | -11.8444 | -43.967098 | 2026-05-23 00:02:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b04dc0ed-7148-3f25-bb53-eabc4e85b02e | -4.4753 | -37.813702 | 2026-05-23 00:02:00 | METOP-C | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9d6c3559-e3ad-35f1-aa40-a9a7d858cd08 | -9.2878 | -45.494099 | 2026-05-23 00:02:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6fe29b54-bcee-3706-8e0e-50dd58a3b415 | -11.9282 | -43.879299 | 2026-05-23 00:02:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc1d19da-b126-33cd-bb8d-1e5f46b3a7dd | -10.4829 | -42.408901 | 2026-05-23 00:02:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d445e13a-6e2d-36d9-969b-f9f5a1b5e0e4 | -6.3972 | -44.172501 | 2026-05-23 00:02:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 030f08c3-0c39-3027-8321-ea858331fd5b | -9.2851 | -45.481098 | 2026-05-23 00:02:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 52751366-1d25-36be-8aab-40a59314db6c | -6.3874 | -44.174599 | 2026-05-23 00:02:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 393bc883-84d4-3266-9d86-a0e20324be28 | -11.6615 | -43.773899 | 2026-05-23 00:02:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18dbd06e-7268-3b3e-be7b-1a681ac7a0af | -9.2905 | -45.507099 | 2026-05-23 00:02:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fcd14d37-33ad-3ae8-871a-265f4f57d709 | -11.6593 | -43.763 | 2026-05-23 00:02:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9789c74f-5f8e-329b-a7b1-b3557331726f | -6.3853 | -44.164902 | 2026-05-23 00:02:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24647075-3e08-3cc8-be67-695605120b67 | -9.2976 | -45.4921 | 2026-05-23 00:02:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8a327b0b-3566-3a60-a725-0fc1bee2bb67 | -4.6552 | -42.437 | 2026-05-23 00:02:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 42a6489a-348d-3732-9580-677882a3bcdc | -11.0515 | -46.711102 | 2026-05-23 00:02:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf7aea31-ca40-3575-848f-edea85811fbc | -11.0612 | -46.709202 | 2026-05-23 00:02:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16d564b9-5838-3dc7-9d68-1f8cc87c522a | -11.7387 | -38.542702 | 2026-05-23 00:02:00 | METOP-C | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0df4e1d3-8236-3889-83ba-0975c63f13aa | -5.949 | -43.488998 | 2026-05-23 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca3ddd02-a182-3f87-bcec-108817ff2107 | -5.1844 | -35.862202 | 2026-05-23 00:02:00 | METOP-C | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 9c5f4ceb-9e33-3423-95c1-46d164a44765 | -21.48831 | -48.63757 | 2026-05-23 00:07:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 63c5624a-0191-3ac9-9dfa-0bb709bea293 | -21.52522 | -48.62111 | 2026-05-23 00:07:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 07566b71-4e78-39d2-857a-90d86f256b71 | -21.52659 | -48.6322 | 2026-05-23 00:07:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6167cf77-2596-34ef-914f-234b848332f3 | -21.48966 | -48.64876 | 2026-05-23 00:07:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 113b5b1e-4f75-3088-b210-fc123fd42be7 | -14.17834 | -52.85915 | 2026-05-23 00:09:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 068b22ea-0041-3512-bc47-11e8c51bc2f0 | -11.66435 | -43.76599 | 2026-05-23 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 64b35b77-1033-3d15-94e5-eb69de915218 | -12.43314 | -43.72421 | 2026-05-23 00:09:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a52447bb-52a0-382a-b0db-068c5ed402b5 | -11.05843 | -46.69687 | 2026-05-23 00:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 067eda08-4824-3910-9aeb-743eca5b37a4 | -10.54892 | -49.46985 | 2026-05-23 00:09:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9a5dff10-c2c9-3de3-94dc-985cd329aa76 | -12.30809 | -47.84735 | 2026-05-23 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d9ef688c-da9e-30e4-b12d-9e15221f9f11 | -11.45271 | -52.91964 | 2026-05-23 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 9348a442-29b1-3389-a945-452fdc968cb1 | -12.29915 | -47.91266 | 2026-05-23 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d989116f-2e83-37bf-99df-36e6fb7b8f4c | -10.48788 | -42.41323 | 2026-05-23 00:09:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 9408f73b-3350-3713-ad6e-5030ad15944d | -11.65891 | -43.77441 | 2026-05-23 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4f6048fe-f147-3da9-868b-735e02d37303 | -11.05978 | -46.70641 | 2026-05-23 00:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 8ca15fd5-fa08-3f50-a8d0-40d0911c25c1 | -14.18176 | -52.8651 | 2026-05-23 00:09:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| baa81477-3ec5-3f7a-9afe-7fbc3440092f | -10.79844 | -49.4132 | 2026-05-23 00:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 97b638d6-b2e0-3745-ad89-ed94a4fa4263 | -10.64669 | -49.72158 | 2026-05-23 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 23ea8466-0b6e-309d-b485-c7bf4f4f68f4 | -11.66964 | -43.77263 | 2026-05-23 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8acfbdcd-834c-329a-a7ab-6408170a0921 | -10.88991 | -51.16113 | 2026-05-23 00:09:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3e843f94-f7a9-3a38-bfc3-9af1ef887727 | -12.30933 | -47.85632 | 2026-05-23 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 171808e3-1a18-3c3b-8ce6-c2d66f84129d | -11.07657 | -46.69423 | 2026-05-23 00:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| aec2d6fa-2644-33f1-9cbc-c39e42eda70c | -11.44155 | -52.92105 | 2026-05-23 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 8d096485-40be-3f3e-af29-fd0c5a352439 | -10.79719 | -49.40398 | 2026-05-23 00:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8dbfc7a3-8c73-3d9a-921d-82cc8a468baf | -11.92419 | -43.87161 | 2026-05-23 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1a9fbe76-247f-3407-8a91-ec0cc06b4afa | -10.73862 | -49.78885 | 2026-05-23 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 28838b28-fcc0-3766-b2d6-c71f8ec8938d | -11.66752 | -43.75917 | 2026-05-23 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 636cc569-8f69-38e2-a27f-4fba0d27e1ab | -10.64796 | -49.73098 | 2026-05-23 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 37d4f309-6ef0-3427-ae60-ac7dde89e458 | -10.65572 | -49.72033 | 2026-05-23 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4de4e73f-f85c-34b8-81fe-364414d3990b | -11.61287 | -47.09148 | 2026-05-23 00:09:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9e53c5f4-c8ff-38e9-9b4d-44f84318d1ed | -11.44342 | -52.93582 | 2026-05-23 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| ff83ef55-ad52-3ba9-b083-17a0c4de68cc | -11.58869 | -45.19199 | 2026-05-23 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 7eed0f28-6f60-3ecc-b2e1-12e9611ca493 | -12.00261 | -45.14173 | 2026-05-23 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| cb8e8732-8e14-3fe6-ada6-8c0282819212 | -11.61418 | -47.10069 | 2026-05-23 00:09:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3022b49a-edfa-387b-bc42-0138dbfe00a8 | -10.47567 | -42.41524 | 2026-05-23 00:09:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 5d003120-4ec3-3de8-8f7b-99a882c1b85b | -12.06063 | -45.26684 | 2026-05-23 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ba1b4e3e-c0c2-3593-ab86-84cf8d4a11a3 | -11.45459 | -52.93442 | 2026-05-23 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| ed3d5e59-d2aa-3452-9ccc-7a96d0bfcf35 | -12.06151 | -47.33558 | 2026-05-23 00:09:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| aadd4ee4-96e2-3ef8-9af0-d432800833bc | -11.97454 | -47.37326 | 2026-05-23 00:09:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 92c05570-9189-38b5-a591-434ebc0d3962 | -12.05265 | -47.33689 | 2026-05-23 00:09:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| b0531e6e-54e4-3383-b831-b2405e7ab603 | -11.45471 | -52.928 | 2026-05-23 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 589bf308-eced-3d0e-a753-a99cada11a25 | -11.84511 | -43.95892 | 2026-05-23 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f7923c2c-667e-3245-9e8d-9108d91a2ffb | -11.44355 | -52.92942 | 2026-05-23 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6c258a54-791d-30c7-a070-58b3b6ef43be | -11.84711 | -43.97208 | 2026-05-23 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1305bbfa-2861-3a36-a947-6c94c1b8eada | -9.3041 | -45.5036 | 2026-05-23 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e3aabb86-f7f1-3e4c-b612-6652923b277c | -11.1903 | -55.9101 | 2026-05-23 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 0914f516-9a38-37af-8691-d7a64634e260 | -11.1712 | -55.9319 | 2026-05-23 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| a7a56543-9a42-324e-816d-d4881d260e12 | -11.4534 | -52.9212 | 2026-05-23 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| eb1dc2d9-5bec-3f71-a680-bc55ff575b57 | -11.19 | -55.9303 | 2026-05-23 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b3cea1ac-c664-358e-a5bc-7025903a4513 | -9.2852 | -45.5058 | 2026-05-23 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 9ed5d451-857a-39ed-ae6e-1a5407602621 | -11.1714 | -55.9117 | 2026-05-23 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 326749a1-393d-3753-81de-08ce33ad56f0 | -9.3045 | -45.4809 | 2026-05-23 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 851cacf2-43f6-3018-a4f5-a7a1e422bd53 | -9.2855 | -45.483 | 2026-05-23 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| e7562097-fa1a-3864-9b56-285ffab77923 | -8.10425 | -46.73758 | 2026-05-23 00:11:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1a723e32-43bf-31e4-a678-824f5afa6ba9 | -6.3951 | -44.17315 | 2026-05-23 00:11:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 7d58e634-6f48-3253-818f-ae25611782e7 | -10.43322 | -52.15289 | 2026-05-23 00:11:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e43f976b-b430-3b46-87d9-3acb57bb1213 | -8.43962 | -51.5548 | 2026-05-23 00:11:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7fb7df01-31c6-3d52-a2b7-7c68bb47d8ae | -9.29929 | -45.50477 | 2026-05-23 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| ca8520ac-d4e9-3648-a2d1-4095c3a15c37 | -9.10881 | -50.54052 | 2026-05-23 00:11:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5b086ca5-9a1c-3e30-b4a2-d3f91e66d7b8 | -9.28777 | -45.495 | 2026-05-23 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 8446fd64-aafb-3887-b704-3d6ccef0d15f | -9.51181 | -46.26464 | 2026-05-23 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7bd02796-8fa7-31ae-9523-9f406d738ef5 | -11.18509 | -55.92781 | 2026-05-23 00:11:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 113f8843-11c0-3962-902a-88e4d2b5e90a | -5.77485 | -45.12822 | 2026-05-23 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1e2d9f1e-a921-3f1d-9236-632a20cc60e7 | -8.7132 | -47.91463 | 2026-05-23 00:11:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d64dea4d-72eb-3e63-95b6-b9d8529482cc | -8.72207 | -47.91334 | 2026-05-23 00:11:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a8895083-e31d-3b19-b5c4-e8d71cd695d5 | -11.18637 | -55.89739 | 2026-05-23 00:11:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |


[Clique aqui para ver as próximas entradas](README2.md)
