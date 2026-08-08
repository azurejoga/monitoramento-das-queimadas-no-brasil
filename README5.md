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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddae9be9-9143-3fb0-bf6e-8f1502c749e4 | -4.36842 | -47.77172 | 2026-08-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 777fcb93-ed2f-39f2-8974-e5f93dfed61e | -4.90809 | -43.46735 | 2026-08-08 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b258444-6454-3f13-bd1c-d53f2cf9f85e | -5.06442 | -39.73763 | 2026-08-08 03:47:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f31b021c-6ef7-3a2b-9962-615cd38ab4d2 | -4.16802 | -48.77507 | 2026-08-08 03:47:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d0df8b0-a1f7-353c-a098-60dfdf5e5939 | -4.90742 | -43.46982 | 2026-08-08 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f44057a-198d-326a-8036-36c1d8d9785f | -2.41844 | -48.63607 | 2026-08-08 03:47:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87e35ac4-831e-3da6-a521-dc4ebeccdf94 | -3.05081 | -39.92584 | 2026-08-08 03:47:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e8978ea6-325c-3a3c-ab44-5d5db44898e2 | -13.38972 | -41.32363 | 2026-08-08 03:49:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c051ddec-5770-38a2-b216-53bf7e3b8816 | -8.28178 | -50.40659 | 2026-08-08 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c5bae845-e35d-3ac9-ba24-c97a7883c4e2 | -12.53874 | -46.9474 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| baa896fd-e012-352f-929f-cc4dfd61d1c0 | -11.72159 | -50.12961 | 2026-08-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d65efb07-30fe-391c-80ba-375ad28bd929 | -6.97879 | -41.49434 | 2026-08-08 03:49:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8d07f4e7-2b78-3c93-8ec2-781f32be3961 | -6.91686 | -41.95836 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 01c2b79d-022b-3233-8e2f-61c53ccafde9 | -7.07914 | -42.25824 | 2026-08-08 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7d0ff17e-c679-3b10-9759-3ab126a4a67f | -12.54392 | -46.94789 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b44aa1e7-3d85-3450-bc8b-aa853b8ba71a | -12.14128 | -48.26613 | 2026-08-08 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45aa1bf4-b5bb-3855-8442-6aae55b49643 | -6.9849 | -42.90911 | 2026-08-08 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bb6d4462-3305-3dfd-a91b-e989eeb45b1a | -6.92219 | -42.42725 | 2026-08-08 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| eb8be22c-a3e0-3249-9686-ef18f2ac247b | -6.9968 | -42.10387 | 2026-08-08 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c9e3784b-cb26-33ea-a2af-c152aa71e2be | -12.56084 | -46.93051 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5827e213-1d02-3f9f-b6a3-25f310bc566c | -8.35739 | -37.28545 | 2026-08-08 03:49:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf8a4aca-dd35-3720-9804-381781f260a2 | -6.97564 | -41.4891 | 2026-08-08 03:49:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 16db0082-f28c-3edc-9e1a-f121033be1ab | -6.86067 | -46.0031 | 2026-08-08 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79ce5ba8-cd97-3350-bcc6-accedd797dac | -11.72789 | -50.13089 | 2026-08-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0a636446-c557-348d-9ab1-7ac71203bd47 | -6.92026 | -41.96266 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8da03da1-8223-3c70-9e2d-78702e623395 | -5.52698 | -45.78256 | 2026-08-08 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09946816-f1aa-3cbe-8133-58445e8ebf8c | -11.0383 | -44.27919 | 2026-08-08 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1b75fb40-fef6-35df-ab7a-2eb505eef3fc | -6.98916 | -42.90985 | 2026-08-08 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bb18f257-c01a-3f1f-8b3e-d61bc0357835 | -6.92809 | -41.91648 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3caa881a-31d8-3649-9d44-6d37e25e2ab4 | -6.9856 | -42.90503 | 2026-08-08 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 776caa38-f82f-3aa1-920c-f4f272f471f6 | -10.50119 | -46.62907 | 2026-08-08 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00e2dc95-877a-37c1-8254-49408d9d95d1 | -11.03906 | -44.27486 | 2026-08-08 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9179906a-f320-3fcd-a2e2-3494d51ec766 | -10.26433 | -45.81245 | 2026-08-08 03:49:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d95b780-6bec-3e85-b248-b89ca36a2332 | -5.52756 | -45.77922 | 2026-08-08 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3d8e34a-2928-325b-85ea-0c2e7705b165 | -7.36653 | -42.86452 | 2026-08-08 03:49:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a082173-98e6-30af-bf01-f8fd1b8353e2 | -13.37424 | -41.35061 | 2026-08-08 03:49:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7d81d31f-f48b-3e7f-ab52-8f155fef5d07 | -10.45672 | -37.1432 | 2026-08-08 03:49:00 | NOAA-21 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| abc2e744-0b6d-3b30-a4d7-15b60a2192bd | -7.3672 | -42.86058 | 2026-08-08 03:49:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ae158a34-c069-3d4b-8c8c-f9d41e1a3c7d | -6.97652 | -41.48743 | 2026-08-08 03:49:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7920f3f0-7456-36c9-a0b9-95aab7d1f342 | -8.12324 | -45.89378 | 2026-08-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbac85a3-dbd1-3bb0-89fc-8226761a13e3 | -10.50679 | -46.36998 | 2026-08-08 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8c0bbf2-3b81-3a35-bda3-7b59f6845fd8 | -10.25805 | -45.80852 | 2026-08-08 03:49:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 86aa9962-4020-34c1-b0b2-6548efa09d36 | -6.85998 | -46.00208 | 2026-08-08 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 977972de-3936-3d2e-b2c3-15f64ff147f9 | -11.71949 | -50.13992 | 2026-08-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| af828fa0-0b79-32ef-96b6-01fed3d249b7 | -8.6216 | -50.02623 | 2026-08-08 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0d9ef94e-4196-3c89-879a-5f7f3c492d8c | -6.97569 | -41.49234 | 2026-08-08 03:49:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 250caeb2-431d-3560-b990-4c3baea28797 | -6.91565 | -41.96549 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e0c33180-4da3-38c6-9aa4-987a22f801dd | -6.89249 | -43.71527 | 2026-08-08 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa6ae036-d821-3a44-904e-5a0127252266 | -11.30419 | -44.86136 | 2026-08-08 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54bd0d67-4da0-37d5-9682-a2af631f5534 | -12.5614 | -46.92759 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0d995e5-d305-3562-a874-1fdf1d832c03 | -7.08134 | -42.26999 | 2026-08-08 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 840767ec-4b5a-3116-bba5-b6c8c55be85a | -12.54889 | -46.92114 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cca0f470-6137-3931-8b64-0fcd0c67508f | -6.97964 | -41.49268 | 2026-08-08 03:49:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 44903e48-96c8-3f48-83f5-cceb11a96f67 | -12.53929 | -46.91621 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 458447b0-99f4-32e8-a153-92eda9cac5ad | -7.18581 | -42.34478 | 2026-08-08 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 95644545-8a03-3b8b-a579-4d7a1fee79a0 | -12.54728 | -46.91886 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55f6e22d-8959-3130-a061-0f2b059a2fed | -11.30345 | -44.85865 | 2026-08-08 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c1020b1-026d-3122-94af-e7d8819af3f0 | -5.52639 | -45.7859 | 2026-08-08 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aa81147-f3ab-3561-ace2-ac981a05ed97 | -10.78392 | -46.10177 | 2026-08-08 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a5c52a6-9257-31c5-8a38-11485f6b1ec5 | -6.91102 | -41.96841 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d8ef0c0d-2794-3621-a133-6f3812ac4977 | -12.54669 | -46.92194 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cff03d2-0276-39e8-b543-50bcbb16d07d | -10.263 | -45.80923 | 2026-08-08 03:49:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 06547328-a997-3821-9248-00ac569097d9 | -12.81961 | -41.96304 | 2026-08-08 03:49:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0cc35662-f7bd-3adf-814e-f36227af1745 | -12.53135 | -46.95881 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2c8945d-55f0-3b9a-8907-6fdbb6210d09 | -11.72579 | -50.1412 | 2026-08-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e8086afd-5983-3fb9-9b5b-c24b0030d194 | -6.97169 | -41.48882 | 2026-08-08 03:49:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| aea323a0-b15c-3aed-81c9-4e61dab52b2f | -12.5409 | -46.95183 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f379a6a-f8ef-3e11-84ff-0b03f4c43d4a | -10.26821 | -45.81896 | 2026-08-08 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a657fe77-f6cd-33bb-8779-55963c62d181 | -10.46004 | -37.14373 | 2026-08-08 03:49:00 | NOAA-21 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ce822864-096f-3330-a527-66f5ef7273a6 | -12.54219 | -46.91795 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db090fe0-1f7c-3bbd-ab7a-d53580da4249 | -12.5416 | -46.92102 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9059b113-4508-378e-93c3-1d6ee03e884b | -7.77948 | -49.48649 | 2026-08-08 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 362c496d-1420-3db0-9aa3-70985bfb1dc8 | -11.72684 | -50.13603 | 2026-08-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8ae5d043-a79f-3785-a437-9b88205ec12e | -9.25646 | -46.5969 | 2026-08-08 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22c7e51d-4d51-3441-9ede-2419a408b3c6 | -9.40062 | -37.81182 | 2026-08-08 03:49:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67f406de-249e-3aa4-b63c-667ae8b1fc3e | -7.77299 | -49.48536 | 2026-08-08 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b6ffd3f-c1d7-37e0-b495-def0d30fc0e4 | -11.03469 | -44.27406 | 2026-08-08 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e1103c10-bf20-3cc4-b067-9bd119f5e917 | -6.9813 | -41.48291 | 2026-08-08 03:49:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f212dfdb-a8ea-37ea-8e77-5c1530a5d310 | -12.54448 | -46.9449 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a54ca0b-6acd-3e74-80e9-0bd66cffc7be | -12.54554 | -46.93919 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7ea0519-8b0d-3318-a25f-bf6b37ebb61c | -6.91285 | -41.95765 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db6afe6a-7eca-3ceb-aa27-a2d2eab3939f | -12.5371 | -46.91703 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38f6e129-a855-3ed3-9586-3afb8d908eae | -11.77901 | -46.39101 | 2026-08-08 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9de56371-4ddb-3dba-9dd1-698a7fed9b8a | -12.5421 | -46.92939 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc1d0518-a1c7-3a82-8f4c-841b2a38d4ef | -6.72528 | -48.1208 | 2026-08-08 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80dccf94-dca9-3709-a2a5-2da29505559d | -6.92427 | -41.96334 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5fc18f09-c5c1-387c-a8cc-18fe4b6cabf9 | -12.3523 | -48.20574 | 2026-08-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| db117150-e88a-36a5-86ca-9bca7846ccaa | -9.26174 | -46.59782 | 2026-08-08 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d46c0728-4857-3bc5-b22d-da25f7286656 | -6.91164 | -41.96479 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 629bfada-0444-3016-b819-5935bbaec109 | -13.38842 | -41.35324 | 2026-08-08 03:49:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 315df7aa-cfb6-3462-a201-803cc9473cad | -12.54492 | -46.93106 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2becbcb0-c061-37e7-be53-cf2a535aea84 | -12.54154 | -46.93241 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b286e75-50d7-36e2-8a1f-dd08cdcd2e58 | -8.33157 | -46.38771 | 2026-08-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3bee7e40-a1b5-3363-bc6b-253ac465b7ee | -9.38076 | -40.3195 | 2026-08-08 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ea4eff37-1d3e-30c8-908c-8e6a6d882794 | -6.92281 | -42.4235 | 2026-08-08 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3d2edd9c-125f-3396-9bc0-309960f553da | -7.18642 | -42.34116 | 2026-08-08 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b8050f6a-1a81-3e64-a02c-e2e262575e53 | -7.5154 | -47.56435 | 2026-08-08 03:49:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8a73912-9be2-31e2-9a98-dff8bdeaf2a0 | -6.91626 | -41.96191 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 81402af7-313a-3090-a35d-02e5cd64ae2f | -11.1679 | -43.41692 | 2026-08-08 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f14f009a-26e8-357f-9439-d5791b54475d | -12.54608 | -46.93631 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README6.md)
