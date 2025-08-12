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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81b480ae-5bde-317a-887c-0de1561c31ab | -11.68851 | -51.59032 | 2025-08-12 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dfd46dbe-0149-36b8-b4ed-94b94ad57273 | -9.37457 | -61.52759 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f440e23-ce79-3038-a394-579edfe53299 | -9.18761 | -59.65958 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| df3409ab-4b38-3ac0-8f9a-5869ab43939c | -13.87529 | -45.5652 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38caa7ad-0325-3442-a7a9-f4fd9096904b | -14.11228 | -45.38849 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cf2e95b-9fe5-32d4-92f7-02206f4d5b6c | -8.93343 | -60.72789 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f3988c92-89a2-3555-a38e-bb48ab7d3902 | -11.72391 | -50.08545 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 145ec3e5-db18-329c-833e-381e2cda0478 | -12.57928 | -47.0779 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a72082a4-91c0-37ce-9744-bc40a68e19b1 | -12.57362 | -46.99516 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b1cd6ec9-f032-3fac-b12d-c1f314265d8a | -11.70666 | -51.59789 | 2025-08-12 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 72fb8bec-3ea8-370b-b189-bd0e550a4613 | -12.56625 | -47.0127 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ed5cfb3c-71d7-3cec-94ca-0f31dfcf05df | -11.80595 | -44.93373 | 2025-08-12 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 409622d4-0b88-31b2-861a-bf6b7bb87b76 | -14.11829 | -45.39695 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d75c0c6e-47ae-34e0-954e-55a238911676 | -11.71937 | -50.1196 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dad31a2-b577-3420-97cf-05c23edc50d2 | -10.2143 | -55.33128 | 2025-08-12 04:59:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c63e43b0-d26d-37d4-89e3-3df599bfc871 | -11.65298 | -48.3264 | 2025-08-12 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84e1ef30-f73d-3f3a-8fc4-2bf11d3a816b | -10.35156 | -50.82421 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c176b9ba-3c47-3607-9aa2-680cec648a46 | -11.69028 | -51.60479 | 2025-08-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ada0241-ffe2-32b7-95c5-5538aed3eedc | -10.31803 | -54.15598 | 2025-08-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d5dcd8f-2391-3430-9375-f573cc75cac1 | -9.37039 | -61.52818 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14b93ec7-edc4-3dcf-8e5f-47f2fda47afb | -10.34881 | -57.60144 | 2025-08-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fcc745b-29fc-36ff-9706-146dbff02e9e | -11.77864 | -49.54996 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7b2c529-7e45-3c5a-be66-369ae798f377 | -14.63964 | -45.85151 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f31ad665-086d-3775-9a95-85885de05742 | -9.26365 | -60.77986 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94e8f2e1-4af1-377d-a1f3-d824f2baacd7 | -11.4562 | -50.16828 | 2025-08-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d8bee94-1ce5-35fa-b173-e23eaf5cff00 | -9.37846 | -61.53408 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fed5d9ca-8905-3470-9e00-55632a319c0c | -13.63239 | -46.9362 | 2025-08-12 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 341d73c4-0ae9-3a59-bf7c-003e163843cd | -9.18675 | -59.66462 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c2c9752a-0840-306a-b0ca-b7cff28e5743 | -10.75507 | -48.79223 | 2025-08-12 04:59:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6fbd652-ee74-350e-a99a-9d6b1148127d | -10.35407 | -50.83451 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33706150-5e77-36d8-9d8b-5ea4ae756729 | -12.55148 | -47.04834 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8f89a51-02b8-3c28-8740-e4387520fe68 | -11.73431 | -50.10246 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58162305-9fab-363f-a82c-c1457f8dec16 | -11.46288 | -50.15026 | 2025-08-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da1b3fac-4b74-3582-a782-152535e2125f | -13.62724 | -46.93378 | 2025-08-12 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86304e13-1250-3da0-90d2-9222dd1f0ebd | -9.38362 | -61.53048 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bccb5852-ac35-3970-a580-a8c04dcec6b7 | -11.12757 | -50.46545 | 2025-08-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51995317-b836-3bc7-8309-5e7623b85e04 | -9.3748 | -61.52895 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 197462f4-771c-36df-bdad-6b134debfd73 | -12.563 | -46.99604 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e3b99d25-982e-3a18-b645-29ba2375cff5 | -11.7106 | -50.12219 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32e2d5d0-ea9e-3d3d-b174-15bed3f57a63 | -10.36987 | -50.80664 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04eb8327-d625-3411-be88-066ee2c3bd54 | -11.7721 | -49.56574 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d35dee74-b273-3058-8c3f-e8e8203c55c6 | -12.77188 | -45.45722 | 2025-08-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 022bc73c-d3d5-303a-a030-ba144c5d847f | -12.55678 | -47.00412 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb42cfb5-2b06-31c5-9757-a9b74c64bd1f | -14.12353 | -45.39429 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84a8f930-a3fa-37cc-8a98-8758441434e8 | -9.93653 | -60.48667 | 2025-08-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21e91017-714f-37ee-bb6a-488aaa02897c | -10.31748 | -54.15955 | 2025-08-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 075833f2-1b88-3759-b2a6-d568f36d06d9 | -15.67302 | -43.48941 | 2025-08-12 04:59:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2961649e-e73b-39a9-89a3-71326266cc1a | -11.66457 | -50.13129 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d62a620-c31b-3007-b52e-ff8f918febf2 | -8.92802 | -60.75951 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d17d201-f77a-3f04-b339-f9aec8bb7e6d | -10.00678 | -59.96017 | 2025-08-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5349e8d-d5da-3d43-b204-01365e066b55 | -10.97358 | -49.56895 | 2025-08-12 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b71b6606-92a7-379a-acf6-fc95009318f9 | -12.56663 | -47.00951 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 65f96c7c-caba-3418-a5dd-6d5431baa9fa | -11.72455 | -48.34772 | 2025-08-12 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52e68d97-d080-3324-8d8c-864df1e7bd33 | -9.03677 | -59.76195 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ee37844-79b7-30e8-89c1-1197f1c3c918 | -9.3826 | -61.53347 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df504120-9c66-3c4f-84af-cfcd502b9cd9 | -9.19066 | -59.66532 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 20057cb6-ce61-3f3d-bf6f-1183a4c5eb47 | -12.5564 | -47.00725 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f9a38975-4a12-3c96-95f2-a12fd0519804 | -11.70975 | -51.60315 | 2025-08-12 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f61b35b-45d7-3670-8e73-88683a025e5a | -14.69107 | -53.71709 | 2025-08-12 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d65b03c5-ffbf-342a-8ee2-70cca1368867 | -12.77857 | -45.4497 | 2025-08-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| effa556f-8b1e-37fc-acb1-acfaf5dda29e | -11.70793 | -50.12217 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fff9ef8-cc94-3269-9871-425caf8177e9 | -9.38338 | -61.52911 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce6b24f4-ae1d-3a4e-b94e-b9cbc9591a0f | -14.4526 | -47.83931 | 2025-08-12 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efeb0dc1-321c-3072-a029-7f466743aeba | -8.93276 | -60.73182 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7cd60cc5-977c-367a-94d1-704221e0d0fd | -10.18326 | -49.50891 | 2025-08-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50ca6282-262e-3f08-b634-8251eab3956c | -11.6759 | -51.59781 | 2025-08-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6268af65-e7d3-37bf-b816-df4570828219 | -13.03979 | -56.84264 | 2025-08-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b87155f5-a1f2-3818-8c19-cb898eedb6bd | -14.04097 | -47.40732 | 2025-08-12 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6c814139-f5a0-35d7-9001-4ee13f1de3de | -10.34837 | -50.8187 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67e4b292-8208-3aad-9834-2aef17e1c754 | -10.3108 | -54.1585 | 2025-08-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b2c54e0-b21c-3201-b4e5-b945e3042057 | -14.11906 | -45.38063 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a70b7299-39cc-35b4-a293-c8537bf1c244 | -8.92855 | -60.73108 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1e07925d-5f69-3cc3-ae02-7d0a41bae29c | -9.38183 | -61.53782 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65c88c51-274f-380c-86d1-c790dc110f18 | -12.54945 | -47.04551 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 832beb6a-837a-38b2-b0bf-b38981569eca | -9.18283 | -59.66396 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ed4fac6-54f1-3f8f-bc4e-a42986a449dd | -12.56151 | -47.00848 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 91b185f4-74f3-3c59-bc1e-165632f59b0f | -13.34033 | -50.24744 | 2025-08-12 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| afa9f23d-cba4-3e5a-974c-82bd955ac438 | -12.56849 | -46.99411 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3cccb113-e201-3aa8-8ef3-a1098534b37b | -12.56189 | -47.00529 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38f1b826-0907-3bdf-bdeb-297e8161e560 | -12.63783 | -45.33518 | 2025-08-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73f37d91-71a0-3b04-9247-347753f1f2cb | -11.7338 | -50.10625 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37fa8e47-8feb-34a7-a2a1-9b2718e68b05 | -11.78721 | -49.55131 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe66f135-3a48-354f-b5b0-5fd07ee54c36 | -10.35087 | -50.82907 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a839bb9f-a70f-319f-99b5-b0090ff2bcc4 | -10.35863 | -50.83021 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eacdf77d-60bd-32b3-af79-f5a4cec0a3a8 | -12.57289 | -47.00113 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 425b1abf-21dd-3425-8e7b-b69dd7faa1b0 | -13.34452 | -50.24808 | 2025-08-12 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1f08fed1-7bf9-3e10-b0e3-652eba6ddc95 | -10.96933 | -49.56836 | 2025-08-12 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a8351c4b-a04c-32eb-a8c0-ab212244bdf9 | -13.8993 | -51.83162 | 2025-08-12 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19f461f9-415c-3a01-868e-6da5963c333e | -8.93696 | -60.73258 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 12d2819a-165c-3d0a-ac7c-57e5296c066f | -8.5211 | -43.3063 | 2025-08-12 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 36ca6288-dec4-3532-a6c1-f20da8cb8560 | -17.6544 | -46.699 | 2025-08-12 05:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 91ced9a9-842d-3121-a8c2-194cb89d199c | -13.3427 | -50.2448 | 2025-08-12 05:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 82104876-5e9c-3673-8661-0b45c09960c5 | -7.1299 | -60.1182 | 2025-08-12 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| e6bc18cc-805e-3881-a723-f4b2265427d5 | -17.6549 | -46.6757 | 2025-08-12 05:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 1ab84766-ca2e-3c49-9149-d450da134737 | -13.3619 | -50.2423 | 2025-08-12 05:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 24c7e56a-2b5d-3629-98b2-d799cbba169d | -7.1483 | -60.1174 | 2025-08-12 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| ab43898e-b702-3a7f-aa98-f28ee826b9c8 | -12.555 | -47.0034 | 2025-08-12 05:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| a0540448-85c0-3632-a35c-2144e660f0a7 | -16.2961 | -52.9016 | 2025-08-12 05:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 2909d489-8813-36fc-9b28-4d7b65dee523 | -12.5742 | -47.0006 | 2025-08-12 05:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 52ae9b0d-06e5-391f-b907-f5d6ebc35146 | -17.6749 | -46.6715 | 2025-08-12 05:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 61.2 |


[Clique aqui para ver as próximas entradas](README28.md)
