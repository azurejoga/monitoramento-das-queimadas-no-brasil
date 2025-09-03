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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1139f7b8-4492-30aa-8fc1-ba02e7887e75 | -11.63797 | -52.04977 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 669cba98-d49e-3dfa-b02d-d33158ac0392 | -9.29224 | -47.08671 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9acf296d-acc5-33bf-967f-d6c525eedbb4 | -9.54397 | -45.83452 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc5dd956-5839-3e6f-8bd4-8b68c5d207fc | -7.16682 | -43.90245 | 2025-09-03 04:46:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20ab6cda-ceeb-3367-9ac4-1f06f54c673c | -6.94022 | -44.71487 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70039e35-cd86-3649-b3dc-161ab33f4ccd | -11.64789 | -52.05136 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a530baa0-0942-352b-b52b-1b425df06683 | -7.72352 | -50.2504 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f7494b6-e3cb-36bc-a694-95eb23c3943f | -7.43669 | -46.01334 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a34f2563-02ce-3d4e-bb1a-1c23dd07d1ef | -9.27906 | -48.55637 | 2025-09-03 04:46:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6416f3df-ddfe-3bec-81f0-e1c955a0ac4c | -8.08847 | -45.50243 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19eacf6e-95f2-348f-a04e-35b84e738454 | -7.00347 | -43.23998 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 195768f8-d241-3036-9f84-af5415f7c2ea | -8.05682 | -52.36834 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c4b627c9-eaf0-3634-afbb-d2543d28491b | -11.58744 | -52.13513 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 121690ef-d0c1-36ba-9451-6a1adf1cf3dc | -5.80535 | -43.2273 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2aa412ad-e8fc-32fa-a2dd-975f5fc58a01 | -6.78797 | -56.29968 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afb546a3-91e0-33c7-bbaf-6a635bdd17e0 | -10.92279 | -50.86383 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2728c754-e5e1-36bf-9082-7185a253b10a | -10.91374 | -50.83273 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 547bbe6a-062f-35c5-af22-dac782f66c51 | -10.94103 | -50.76629 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 196e7f14-eb83-3143-a9c3-909c362564ca | -5.70693 | -43.11149 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6414ea01-bdb4-3b01-9e2f-fd8a82366067 | -8.08471 | -47.60529 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 09cf54f2-ccfd-3ab6-97f0-ab50e641a656 | -11.19653 | -55.01673 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 53e19f17-4fd5-345d-b04f-40b09fd47272 | -9.73545 | -48.99662 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3ebad4a-58d6-3a3e-a8cc-15ac2b9f673e | -7.9407 | -46.43622 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39fd97c3-0fff-32ee-a6c7-8caf422b08d7 | -11.16386 | -49.44316 | 2025-09-03 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9c3c58d-f58d-3ac9-93bc-60005e5d631c | -11.62809 | -52.06976 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e65ddc3-3be0-365f-8562-8e6952490e7c | -9.73593 | -48.99835 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8bb1f98-dccf-3f9f-97a8-19dbfb1b4e1a | -11.67606 | -52.20007 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 344dc88d-6622-3719-a8ba-51f84a0be651 | -9.96621 | -51.62491 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ddbe732-a2e4-36b1-a14b-cdac6af54108 | -3.48291 | -59.25453 | 2025-09-03 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffe9d1cb-7c44-369d-843b-258fb040f5a7 | -10.72932 | -49.59746 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e52dbb47-ddab-3638-9ea7-63d3a06e989f | -11.80837 | -50.64162 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b21b0dd-a1c8-371b-8d42-e38219c4b12b | -6.81528 | -52.81521 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d37cf82c-5f9a-3280-828d-94a2ba3d9520 | -7.78624 | -50.96935 | 2025-09-03 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdd8a76f-5520-37b4-8d26-250f120b833b | -6.03402 | -46.01289 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 58958a07-c7de-3acd-aa08-1fa926679f1a | -11.12038 | -44.65736 | 2025-09-03 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81f6c660-c0ef-3f0b-b5da-3e984aa8a37c | -11.67105 | -52.16694 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef09dd83-9551-30ef-89d1-9a03daea8727 | -6.03454 | -46.0094 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3971aef1-018f-3b83-aba4-f5742d167f6b | -11.67657 | -52.17501 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55c61632-fda9-3629-a1de-3e7a5c0b64e5 | -10.47878 | -53.63242 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 722d16d4-3a17-3370-896c-58f3d65ac4ad | -9.95136 | -51.63328 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1f90c51-899e-3deb-aeba-76c13e0e7a19 | -5.5991 | -51.94384 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5290c92-df8d-3e71-b10a-514194bdb665 | -6.74366 | -45.15082 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9255c95-8a86-39ef-83aa-9700d93613b6 | -8.45426 | -47.34865 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 904e7237-8afc-36da-aa63-170d4a94b534 | -7.94093 | -46.55804 | 2025-09-03 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b196de07-bf9f-3110-b2e8-53449dc7683e | -6.65313 | -53.19214 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e5a6c67-eb25-3870-bb6a-799f59794b1e | -10.73794 | -44.81149 | 2025-09-03 04:46:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13dedfb0-cc8c-30d6-8767-8ef0a9a78b30 | -8.17665 | -47.42733 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78b1fb53-1155-3358-97df-af4816982718 | -11.5507 | -44.83834 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9a47b9d9-d472-31da-bb99-b073c5a38ccc | -8.54943 | -47.47482 | 2025-09-03 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 096b6f36-c4de-3310-96cb-c2b30388c2b7 | -6.28578 | -43.59325 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b29a153-cd61-3119-a30b-5c199158ff62 | -6.79956 | -52.80531 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c116d8d-e811-3ae0-87ca-89637fedb5d1 | -6.26342 | -43.29916 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6e235b9-9a70-3271-883e-77023ea03073 | -8.15117 | -54.93104 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 349e45f0-3cb4-3a45-b2f1-30e8ba1187c5 | -5.63221 | -45.19304 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2625e0c5-d1b6-3396-9d1c-5da1302591d6 | -5.93636 | -43.03256 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c7df362e-3e82-3eb6-8d30-15c5762afdd1 | -10.48435 | -53.64083 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c90ef0e7-04dc-3796-8f3f-7e96dcd5156e | -11.38593 | -43.61082 | 2025-09-03 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8e93768-461e-3261-a8ed-7554d05dafa0 | -6.95715 | -45.56426 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e55a3b0d-ae1f-33e4-a9cc-c2719b0a4be3 | -6.87568 | -45.56171 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13871ede-cf8e-3cab-bd4e-5fd2cc1e7dac | -6.43756 | -58.13017 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f638f5ff-94ff-36a9-95a4-d9096c4d4c0a | -5.44483 | -42.8226 | 2025-09-03 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b707857f-249b-3897-bfd3-086412fa2e77 | -8.01849 | -44.10719 | 2025-09-03 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6f8c10f-921c-3b68-90c6-8a59df0a38e2 | -6.5321 | -56.20917 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d059e5b-28d6-38c2-ab9f-99fadafb10f9 | -5.11259 | -56.96434 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 973d7c06-a500-3130-8349-9e993ade0edf | -11.56949 | -49.91122 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f557fe00-7916-35f2-b2f1-5c4870c07627 | -9.39578 | -48.03756 | 2025-09-03 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebbd76b0-60d4-3228-933a-753a8fc15f22 | -10.88483 | -55.74816 | 2025-09-03 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 988a3ed3-8e06-3051-b443-1e5e7d5fe1f9 | -5.7684 | -45.29618 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 051fc2e6-3831-3e3f-a313-1d6b8eaec38c | -11.02351 | -51.47212 | 2025-09-03 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6223507d-8733-3a31-9790-ed192308477d | -10.14882 | -46.27388 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21687d62-d541-3b97-b6da-581f672cf8d5 | -6.8012 | -52.81672 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78ff3d43-a8bc-39bb-bb74-b4c92dff0e4d | -6.46265 | -49.52248 | 2025-09-03 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df4d9737-ff8d-3353-a9fc-f48ab981d68b | -8.35764 | -48.31036 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 133b7f4f-587b-3bac-a41d-84c6e90ac797 | -6.83329 | -52.8107 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3cb5f0a-048f-33df-ad00-8caa61a5956f | -6.46436 | -53.40432 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e1bb945-2ef7-303e-855a-055fbb1cd315 | -7.92166 | -46.42535 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 075c66f0-a34e-3bb4-987a-b8f1c5b258be | -10.48932 | -53.6529 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c5ddde2-b0db-39b4-81ba-89fb7c89e4f3 | -9.13623 | -49.64762 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 630d00b5-ea24-3490-b853-0f4bc71b6bbf | -6.64935 | -45.90321 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b27f2c95-c569-3063-9b77-29f5aaf4607e | -11.59234 | -52.10359 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f76f890-6cfb-313f-a630-ec6ff3c83823 | -6.53755 | -42.94633 | 2025-09-03 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b1816ae-7b96-3161-bb33-b960d060e084 | -11.27117 | -48.94659 | 2025-09-03 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b1632fb-1aa4-3650-b843-5a15dd525eb2 | -7.48483 | -44.83696 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bffc224b-8d22-3763-a260-36add3d3dd53 | -7.12182 | -44.76215 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7e6bcff1-d8e8-3a71-ae9b-b94945c89ccf | -11.58577 | -52.12409 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| a11c963b-2e42-3da8-8065-e01a1198b19f | -11.04116 | -52.04044 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51b845bb-772b-346e-87a0-3e4a38f973d5 | -5.69815 | -45.9488 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| edbb4ba1-5cb4-304a-acb9-a622eb7d99eb | -6.46781 | -53.40487 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5144f5d-4b9e-3fe8-9c6e-e3451644ac7f | -11.60055 | -52.07254 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 053e9ef1-5272-31a3-a73b-de3f450680de | -6.22695 | -43.38307 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e299e557-7752-30f3-938f-c897c5e100f2 | -8.32829 | -47.39881 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7b4882c-b20f-3c50-8910-f3b30aaa8192 | -10.8438 | -47.44516 | 2025-09-03 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ede5f11e-bd7b-3e11-9dca-311f4b5f2431 | -9.95299 | -51.62282 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d52c9d0-9189-3b4f-8e84-b7ce23ab018f | -11.03498 | -45.06263 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdbf86d6-19bd-34f9-bf93-ec57e6a4494d | -7.92866 | -46.43387 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7fb36ad2-7ad0-30e4-8623-2d7fbab0775d | -8.4407 | -47.34429 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80c6f9d0-29e5-37b6-89e6-a79bf62d611b | -7.93692 | -46.55743 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdbb638c-2d78-3e11-80aa-eb0788966b44 | -8.06514 | -52.35886 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3b9f458-214e-3319-b28f-b9508774c2fa | -6.77202 | -44.47767 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 66469860-5b38-3e56-9e6a-0609c5b527be | -12.01538 | -45.57513 | 2025-09-03 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README56.md)
