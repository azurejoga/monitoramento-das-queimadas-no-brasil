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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad22f1af-d34c-3d71-bdfc-e8143bacf64b | -11.75672 | -45.00182 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b9d67ca-2402-3914-87a5-05ee3bb57ff9 | -15.70233 | -49.00314 | 2025-08-04 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d58bb73d-a26b-3d5c-9338-d73cff84142b | -11.76461 | -44.97548 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 371e93e2-b73e-3dfd-9c9b-258e11b540e9 | -11.22523 | -48.43297 | 2025-08-04 04:10:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb4ac170-1f00-3b52-950a-1b8397a2d93c | -16.9244 | -49.45698 | 2025-08-04 04:10:00 | NOAA-21 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 273956f3-e8c0-3e45-a3f1-471181fc5691 | -11.9256 | -44.97991 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ab67700-9a77-3f25-8f16-07d6959a6127 | -12.6931 | -48.10807 | 2025-08-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75b2a676-e549-3828-b168-f7ced15e01fb | -12.52488 | -44.75084 | 2025-08-04 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 799ce549-19fb-3723-947b-756dacc0fc62 | -11.75264 | -45.00513 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bc1c273-4b12-3075-9db3-34cc8443f2ed | -11.75047 | -44.99691 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52148725-05b1-30e7-ac90-9384a6f68ecd | -14.1636 | -43.67111 | 2025-08-04 04:10:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8515d678-b488-397e-9e71-7ca62c4d4d17 | -11.78611 | -44.99477 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a80d086c-68b3-35b5-a74f-6d842c49c128 | -13.00947 | -47.45168 | 2025-08-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5989f27-67c4-3d7d-ad57-8aa1ade6e775 | -12.41612 | -44.70648 | 2025-08-04 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bd5d21d-9e59-3266-b8a9-0a2d59db0bf5 | -15.27576 | -43.07582 | 2025-08-04 04:10:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a0d43973-f298-3d29-9a4a-f85f4d243846 | -17.37017 | -46.08666 | 2025-08-04 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77893ef7-63a1-37b1-b49c-c35324c89db9 | -11.22454 | -48.43689 | 2025-08-04 04:10:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05277fb2-5569-3024-9f63-bc9b17dc3c7d | -16.43007 | -43.72091 | 2025-08-04 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b81af4cf-4e06-3bd0-8065-a50692935ce1 | -11.82634 | -43.15755 | 2025-08-04 04:10:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.1 |
| f4a24981-5161-37dd-bad9-c091ea2b5dab | -11.93122 | -44.94546 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e75e15ad-b701-3a8a-b0eb-a21d74d9327c | -11.93867 | -44.98613 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2aad67c6-191c-3321-bc7e-f6915034457c | -14.84288 | -48.3894 | 2025-08-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47923a20-6cb4-302d-98d6-43b4e41c2c02 | -15.63478 | -47.8039 | 2025-08-04 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cb429365-b6df-3245-a3da-36b06d671a3a | -12.2341 | -43.67607 | 2025-08-04 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12b91b29-c23d-396b-b7eb-7454cc41b628 | -13.06344 | -56.90129 | 2025-08-04 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8f3c431c-e4f9-3a27-8261-34b0f1cfc245 | -15.70302 | -48.99929 | 2025-08-04 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9058b4ff-6575-34fd-b82a-c6bbbb79da45 | -12.39837 | -38.15561 | 2025-08-04 04:10:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| f77a4a6c-31e8-30cc-a043-bb71abccdbb7 | -12.43481 | -44.85435 | 2025-08-04 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89e60dde-0ee5-3ceb-b670-1ab865eba520 | -11.92878 | -44.96038 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c101bd6a-8814-31aa-92cd-affdd1be6682 | -13.68672 | -41.36777 | 2025-08-04 04:10:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9fe1b300-9839-34ce-85d6-cc3b0a08ce03 | -12.14116 | -43.38211 | 2025-08-04 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55b5b497-560c-3e55-a550-1a67fd63b734 | -17.67537 | -44.12795 | 2025-08-04 04:10:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9bc37e6-f326-32d2-9d08-bc71acbdca9f | -11.22446 | -51.53267 | 2025-08-04 04:10:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df85fbed-acef-3aa3-aeea-50ea35fc9b61 | -13.24779 | -46.96751 | 2025-08-04 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e122c6c6-e59c-3523-9b14-d243a58cd9dc | -11.75492 | -44.97006 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b59a880e-23d1-3367-8a2c-2d5872ce09e8 | -11.93907 | -44.96204 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84a81e0f-5056-39c2-b926-90c9a9b4c4a4 | -11.52997 | -44.34884 | 2025-08-04 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3651c716-efff-3073-a5b9-091223f209c0 | -13.04849 | -56.90403 | 2025-08-04 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 398cfc42-6086-3270-95ed-c41c57f005da | -12.0832 | -43.36131 | 2025-08-04 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0ccae53-80fb-30c7-b427-7ea132c7d836 | -17.46324 | -47.10443 | 2025-08-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22759b68-75f6-3c9f-ae1f-d9ce8b65a0c2 | -11.75608 | -45.00566 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3ec08d4-d15a-30ed-8310-a79d49eadde9 | -16.09584 | -48.49649 | 2025-08-04 04:10:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81f77832-5da1-3f39-b456-880a2b19a289 | -12.00644 | -44.9154 | 2025-08-04 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d395ee06-5004-3888-9a9d-28d64e1e085f | -14.66484 | -52.40372 | 2025-08-04 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| bb41f405-bf34-34d0-be49-f50c17242d60 | -11.92623 | -44.976 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1d04d9bb-2f2b-3b72-9ae2-d128f12ff843 | -18.60697 | -43.88141 | 2025-08-04 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cdb1e3b-61e2-31b5-b1ea-89a0e11b2cb7 | -11.78268 | -44.99417 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 750f9467-2d05-3049-9571-2c419ac86522 | -17.37291 | -46.09125 | 2025-08-04 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4f0ad1a8-d0cb-3e21-b953-498a068c72dc | -18.60753 | -43.87774 | 2025-08-04 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 850215ed-b10b-3660-9ab3-28abb179f96d | -13.05679 | -56.89873 | 2025-08-04 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 99b71563-cd74-35b3-a1ea-b86d090ddd35 | -14.16085 | -43.66703 | 2025-08-04 04:10:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 263de474-6481-3b16-b0b9-dd0a2cf0153f | -11.75147 | -44.96958 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfb88b63-2eab-3d56-981b-da7a7e4a1b83 | -17.61401 | -46.70938 | 2025-08-04 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb3ee2fa-1702-3cd7-bedf-970a2b02edbc | -17.35787 | -46.07644 | 2025-08-04 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee1c93b4-1f84-3ec9-8f48-6d43417bd1ac | -10.33692 | -50.06633 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4299cdf-6d12-338d-aaa3-d28a04f669af | -17.79199 | -42.91671 | 2025-08-04 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 686a2a40-a085-3da3-90eb-4ea958333f0b | -17.61122 | -46.70475 | 2025-08-04 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62f19c1c-8c03-3d46-a3c1-d19179aa68be | -14.26796 | -44.57623 | 2025-08-04 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa911ef2-c02e-31ab-9dd2-a1cce3a34ba8 | -15.63412 | -47.8012 | 2025-08-04 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da3a2dd4-be38-395e-b458-b6922ca34e1c | -10.33221 | -50.06546 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a73c6bce-1f68-3790-bf02-3cc8e8ecf1e3 | -17.4639 | -47.10051 | 2025-08-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b13997af-1599-309e-81b8-996c548ee266 | -10.33132 | -50.07055 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 634d9dde-71b2-3dea-be09-69648b1b670a | -10.24588 | -50.16613 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 04d08c82-5ea5-3ea4-8bd5-4cff4b940974 | -12.14228 | -43.37505 | 2025-08-04 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4858f86-b09c-383a-b9f3-4513cab01434 | -10.333 | -50.06928 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6ab44549-7a6b-3cd6-869f-65e417e55f02 | -16.89352 | -46.6908 | 2025-08-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ff93ac5-0f9f-3d0e-90d7-507a67b6bbd4 | -11.78484 | -45.00249 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d7739cc-fe79-345f-8654-6f65de4a97fd | -16.14281 | -50.24525 | 2025-08-04 04:10:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0ddb9e2-a1c6-3ac9-8bf5-9303bbad2f1b | -12.43882 | -44.85117 | 2025-08-04 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6fb2423-43aa-3573-9294-92f4afb08d05 | -18.18745 | -43.62485 | 2025-08-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e048623c-021d-3eb5-84ba-d6376ceed033 | -16.42675 | -43.72036 | 2025-08-04 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 12c4df38-8f9b-359e-bd93-b3ed18473264 | -11.41414 | -54.72116 | 2025-08-04 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf8a3429-b581-37f8-84e8-4a4b8431dbab | -11.5038 | -44.32979 | 2025-08-04 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a750ee6-da71-3fc5-9191-7b3526edb83c | -15.69971 | -48.9947 | 2025-08-04 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ff7ea8b-4d5b-3ac0-9777-b742a28d1cb7 | -11.7492 | -45.00456 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fa56b70-449c-3653-b03a-a663f4cfe683 | -15.69834 | -49.00232 | 2025-08-04 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 055861ce-11b3-366e-9644-41cad7f6f7f1 | -10.32661 | -50.06969 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48096670-4581-3ff5-a08c-54d666d4756a | -12.39439 | -38.15498 | 2025-08-04 04:10:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 05fa246d-687c-3d32-914d-2f45adb1245e | -17.76564 | -42.93159 | 2025-08-04 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dea64c5f-faba-3e0e-9276-789adfa85a7b | -16.13492 | -46.87904 | 2025-08-04 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6f476c3-1af2-33d8-a7cd-55fb93a9221c | -17.36127 | -46.07704 | 2025-08-04 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fed0acd6-7776-3447-9283-22ead1826792 | -11.50571 | -44.29636 | 2025-08-04 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca435984-81fe-3810-abbc-1423344e80c6 | -13.06366 | -56.90009 | 2025-08-04 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 163a3f7e-7584-391d-9094-077df61170fc | -11.75327 | -45.0013 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a9f8523-e195-3139-9eaf-875c2326cd1a | -16.08054 | -43.62971 | 2025-08-04 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 573a0cd6-8f79-3ce4-8022-86b1300cf236 | -13.05127 | -56.891 | 2025-08-04 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| d63e0d5d-debf-3c53-8d06-315b1b6627fa | -18.35506 | -43.68634 | 2025-08-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64ad5489-b0be-328a-90e2-aa78bbe5efe9 | -10.25156 | -50.16182 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 83c0ff77-e96b-314d-a2d1-47769a6d7161 | -12.58841 | -45.07364 | 2025-08-04 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a596750-863d-3ced-bf03-b64809b9df11 | -14.1603 | -43.67057 | 2025-08-04 04:10:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf158530-52c8-3bf1-b7c0-ba39c3f5813a | -10.70886 | -48.29898 | 2025-08-04 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5d946ce-ac71-34cf-b168-5d4422b26410 | -11.92816 | -44.96421 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d67001e-f145-3c1e-b6d7-8f4ab77a36e4 | -16.13847 | -46.87965 | 2025-08-04 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 613f103f-3a8c-3713-8d4e-05efb5d06ee5 | -18.61085 | -43.8783 | 2025-08-04 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88f023e0-713a-330a-be35-f66480a9008c | -11.77147 | -44.97662 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 820a3d5c-93da-3dc0-a67d-4c3a5dc54f09 | -11.92688 | -44.97207 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2873e5db-ad5d-3094-98cd-ce8e58791e29 | -12.7659 | -44.4144 | 2025-08-04 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20697f02-0e12-3e02-98ef-72e34da1066e | -17.61054 | -46.70876 | 2025-08-04 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1542259-8819-3417-a6ad-db17454eade9 | -13.69414 | -41.36503 | 2025-08-04 04:10:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6bfb6742-13cc-33f2-95d2-96017f512018 | -12.62292 | -44.88231 | 2025-08-04 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
