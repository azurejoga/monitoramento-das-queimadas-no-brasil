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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc165764-a986-3fa8-8431-6ceb3f2e1476 | -12.56311 | -45.9683 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e15f7358-53e9-3848-8d51-7314a976f243 | -11.14506 | -42.83633 | 2026-09-22 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 838d4c8c-3c7b-3946-b9dd-6ad1817389c8 | -10.25666 | -49.98156 | 2026-09-22 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cb9aedfb-a4f4-3caa-8cdb-51e9782a5c07 | -12.7963 | -44.20831 | 2026-09-22 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c1d3647-c127-31d4-9cf9-ccbba1ff2e2c | -6.51761 | -44.05421 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a192c9d8-078d-3977-af39-316b54ebf833 | -9.59268 | -47.78192 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d35c9e01-4845-3d74-b6b5-6ffab341d5b9 | -12.01983 | -47.81501 | 2026-09-22 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6203ea1-c8bc-3f66-99c3-197ac637be20 | -8.44063 | -45.81886 | 2026-09-22 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 272db489-b235-36ad-9c43-6376059742c3 | -7.53013 | -46.21417 | 2026-09-22 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb9c6c20-bee4-33ad-a856-24b0217ba650 | -7.5372 | -47.12688 | 2026-09-22 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 524bb034-b3e6-3b10-ac6b-6d758acb4c89 | -6.89568 | -46.01562 | 2026-09-22 04:02:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 517c96a2-025c-3b67-9a42-95405b703c0c | -9.38447 | -47.766 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 133045c2-df3a-3753-a102-f57eb34f8069 | -6.58346 | -44.1538 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 45c29371-aba7-3939-bd41-df887aa79493 | -5.99131 | -44.72433 | 2026-09-22 04:02:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 761afcc3-a8f7-3816-8e71-64032674cd4e | -6.25903 | -41.69498 | 2026-09-22 04:02:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f468b332-79ba-3ed0-abca-9927a8fa0f84 | -10.51475 | -36.97052 | 2026-09-22 04:02:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 92441152-3fd7-36f0-aac7-9c2670d6412f | -6.90875 | -42.96114 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9e2d34c5-e078-310c-acb9-befb7ea51e37 | -7.557 | -42.66162 | 2026-09-22 04:02:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 44fa86a1-99f7-3c0f-83f1-4b3dbf04a67b | -12.56162 | -45.97636 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cd0850e5-da8d-3ec4-a40c-3f30cd46cfd3 | -8.79337 | -44.27702 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5654a483-3f64-3c94-bcfc-b7cb27b6497a | -11.88058 | -46.83878 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 96564ab3-7aad-3e74-a533-8fa55a87693f | -10.78222 | -50.73724 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f6e8a56-18d8-37e1-b52f-6747ca60fbf2 | -9.62409 | -43.93763 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0a593538-3a50-39dd-960f-a1498c87430a | -8.33361 | -47.53931 | 2026-09-22 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9da7a845-dad4-3c9d-a231-59a0f490ad2a | -6.66627 | -47.37677 | 2026-09-22 04:02:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ee63469-2043-33c9-8f89-7b734e2067ec | -11.87795 | -46.85292 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e0a6227b-f1f3-3792-97b2-e8c45c99af79 | -8.13121 | -46.82721 | 2026-09-22 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bd6bf73-75a3-31a7-8eae-11d6597ab497 | -9.37943 | -47.76485 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b505f4bb-b46f-34eb-a04e-196500d37f0a | -7.5316 | -45.40942 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2edf2c7-7894-38b4-9d35-a645fc46e1bb | -6.97299 | -47.50549 | 2026-09-22 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3405d40-7a17-3985-9973-67da3a5b734b | -7.41964 | -49.8435 | 2026-09-22 04:02:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de907bd1-9ba2-3f68-8880-88dd1c5b856c | -8.79025 | -44.29519 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ccdae13-9c4a-3ae0-94ff-2b2107043bba | -9.90302 | -48.44787 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c83982f1-3706-3cdd-a3db-64f800bef53f | -10.4611 | -51.31514 | 2026-09-22 04:02:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 827859a4-97a6-3d9d-9481-70557d7edde4 | -7.40135 | -44.67138 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0c11f7a-d6d0-325c-bf6c-878dc26298d9 | -10.25128 | -45.502 | 2026-09-22 04:02:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a88e3712-3f7c-3ee7-95cd-96b652c2f5f7 | -9.59324 | -47.77889 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a78fbee-19ab-3fbd-936b-5700abd551df | -6.51345 | -44.0536 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f36ee37b-47bf-3ed5-bd12-552f5562b36a | -8.92201 | -50.90494 | 2026-09-22 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c1da5142-6519-3952-998e-9303ae32448b | -10.48327 | -36.89304 | 2026-09-22 04:02:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 40f6be30-9c27-3f83-80f7-fbeffb14edbb | -6.47579 | -42.77386 | 2026-09-22 04:02:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 384669ef-35be-307d-bc47-cd09514a6cb3 | -9.611 | -43.91981 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ccbc0bd2-70b1-33d5-97f7-4829f37d503b | -6.92472 | -42.89014 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fe1689fb-076a-3e3e-b29a-0a39d79577fe | -9.49799 | -48.50884 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a57df00b-351b-3ff3-b4d9-402f3617964e | -6.01359 | -47.90554 | 2026-09-22 04:02:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 755fbe9b-6fbe-3103-9d9c-e4b168edbf9d | -5.3188 | -43.41887 | 2026-09-22 04:02:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c837686-d377-3b9c-87a4-1e31b1e43baf | -11.84694 | -46.81643 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 723468ef-081b-3fd7-bdff-fcc8481e3343 | -4.30565 | -49.125 | 2026-09-22 04:02:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e03c089a-e7a3-3104-98f6-9ebcb89ce405 | -9.05709 | -48.78189 | 2026-09-22 04:02:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49c2b51d-4c24-3583-b755-bd631f3fa04f | -10.37866 | -48.91614 | 2026-09-22 04:02:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7992dcf2-e083-3203-873c-51af068730af | -12.15221 | -47.38931 | 2026-09-22 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a2d048f-9bed-3eca-94c9-f1557e79ddd1 | -10.04914 | -44.88403 | 2026-09-22 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f98e31a9-e77e-301f-8f9a-33a5f130b5c2 | -6.59363 | -39.13988 | 2026-09-22 04:02:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 229fd56a-cb14-343d-8d10-a4212ad23898 | -4.18471 | -51.24985 | 2026-09-22 04:02:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 267aeb1e-0e8c-3756-b334-3ac48db67e19 | -7.54196 | -47.32538 | 2026-09-22 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f819550-6d94-305f-8c50-e0f1e5114198 | -8.44511 | -45.81993 | 2026-09-22 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c98c7ab-d4ab-31e2-bb55-20d4ad02aa86 | -4.1785 | -51.24538 | 2026-09-22 04:02:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61b7fba7-b0d9-3052-8019-ffbf3ac22bb2 | -6.5779 | -44.15305 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0895970f-1254-350f-9ad0-b0a49343687d | -7.48412 | -45.47068 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9dab9f0d-89e6-3ef1-9bad-934529778fb4 | -8.11684 | -49.58759 | 2026-09-22 04:02:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea75ff0e-c551-36af-bf77-3f078fbc15e8 | -8.83593 | -50.49009 | 2026-09-22 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 455615f9-051c-3cf4-9f08-649058ba3fe5 | -8.30661 | -50.38062 | 2026-09-22 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9810accb-942d-3f80-a321-64d447428e39 | -12.14279 | -47.3875 | 2026-09-22 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 15fb411a-fa05-3370-93aa-50ea431d7826 | -7.07994 | -40.08934 | 2026-09-22 04:02:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e42ef7e-fe4f-3191-b7e9-6ec7f0919c32 | -10.52014 | -44.87154 | 2026-09-22 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f466c43d-62f7-3e18-8e2f-f97946d25201 | -9.72432 | -47.76829 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfd12b25-9861-3da9-a319-a50e38c882d4 | -6.56619 | -44.90183 | 2026-09-22 04:02:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1edc75b4-959b-3078-b3cf-94dc5cd32563 | -6.91259 | -42.9618 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f05cf317-b6cb-33f1-b52e-aa4fae4f6d13 | -6.89803 | -42.95441 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 366c0542-9191-3bd0-af6a-00190cf99474 | -5.38513 | -42.9525 | 2026-09-22 04:02:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bd11c299-f691-3241-a8dc-fefd7a5d1020 | -6.71154 | -42.98278 | 2026-09-22 04:02:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5978ad35-9fed-3ae9-8d0c-e08432ac31ea | -9.54185 | -47.94449 | 2026-09-22 04:02:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 234bf9a9-50cf-3eab-9387-c492123e2a0e | -6.88124 | -41.69913 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0565905e-a31d-3258-a528-be5f3eb419f2 | -6.47423 | -42.7834 | 2026-09-22 04:02:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ec3bd22-9886-3c7b-86bf-8f3f95aa8152 | -6.7885 | -39.25999 | 2026-09-22 04:02:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ea018da0-4df3-342e-801f-70dedefd132d | -6.57664 | -44.16069 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 23a68147-20da-3771-9ca4-701dea716ec9 | -6.49771 | -37.00923 | 2026-09-22 04:02:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 25634eb6-08b0-338f-a940-38c418dbed33 | -9.89565 | -48.48772 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4fc7b1b-86b1-381b-8b32-c00f23fd67b5 | -11.93634 | -46.51341 | 2026-09-22 04:02:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37918a1f-b6e5-39f3-9ef2-b5c891b66ac6 | -10.68064 | -50.77076 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1962ffc5-b93e-3480-8ddf-dcee37764ac6 | -6.9012 | -42.94788 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| da3b0107-6a71-3237-adec-c855cf1b73bc | -11.16382 | -51.11945 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f939191-9c3e-39b8-808f-42a923539c20 | -6.93764 | -42.90692 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2030bb09-57ad-333c-b3fd-ffe372f1a198 | -10.84764 | -50.14953 | 2026-09-22 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 210534da-a10c-3a24-80c4-94c308affdca | -9.60929 | -43.92982 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c7934ced-a1b5-38d6-9550-c23e81d7ff78 | -7.26293 | -39.18238 | 2026-09-22 04:02:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a15edfb9-ccc8-3470-9eb7-e42fe475311b | -11.87603 | -46.83786 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a023881-f2c5-3a93-a29a-0d9a841be648 | -6.57864 | -44.15687 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11351ff3-7e5c-33ca-bf4e-e643c004dadd | -5.68494 | -43.42519 | 2026-09-22 04:02:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5b42d4e9-bb95-362f-b1d7-797fe0bac8f8 | -9.23856 | -46.1601 | 2026-09-22 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 10f2b831-a702-38fa-b805-aae04eaefd6a | -9.38052 | -47.7589 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 005f99c4-93b9-3abb-81c9-b900609fc03a | -7.05164 | -49.92424 | 2026-09-22 04:02:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd741d2a-8fed-3c92-b798-d4b55fd7af96 | -11.34588 | -43.38118 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1da65fca-6b60-37df-afdf-44b5673c8ec6 | -10.9097 | -47.38675 | 2026-09-22 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa7f42fa-e1ae-3c18-957a-69fbfdb1562e | -12.02074 | -47.81002 | 2026-09-22 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b52a552d-9325-3e5a-8d7f-0de6f3bca90e | -11.10613 | -48.32135 | 2026-09-22 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 328ab843-9de2-3f96-9e1d-841a1fd2920d | -7.3939 | -44.79131 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d662ec72-f1de-3f1d-8afb-8cc9c872529c | -6.67296 | -47.37624 | 2026-09-22 04:02:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9b8107b-f94d-31f4-8110-aa4890593bad | -11.15352 | -51.10741 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ecdb102d-2ee8-3b16-baf7-d58086d8b7d6 | -7.42026 | -49.85019 | 2026-09-22 04:02:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README34.md)
