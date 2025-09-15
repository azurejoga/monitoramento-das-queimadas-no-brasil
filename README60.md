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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecc1faa2-d5d7-326e-a766-f05a6a6714e8 | -12.00165 | -46.65514 | 2025-09-15 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5287ba41-fc62-3f31-9045-0bac08d97675 | -6.97517 | -44.54058 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b48a51f9-51bf-3262-8b9c-e3c6402dc697 | -10.72569 | -44.77328 | 2025-09-15 05:10:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ef56a31-750f-3b1c-93f9-c8b87af81932 | -6.21102 | -55.66554 | 2025-09-15 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4757fdb-a136-3991-b71b-dab17582a84f | -8.78382 | -46.04176 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de6071e6-b4c1-37f3-a319-546b7c87c8fe | -10.89822 | -45.45096 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93dd95d0-23a5-3417-acc9-c4acae9cd279 | -11.08169 | -49.73964 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5112ef08-c796-3a8a-941d-a9e717b5bb48 | -9.68959 | -62.00373 | 2025-09-15 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cc664a0-15f3-3936-9dcc-bc107222e724 | -9.12135 | -46.94162 | 2025-09-15 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c35d317b-39f7-3f2c-b887-787a78be0ec2 | -7.37118 | -44.35246 | 2025-09-15 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e325637-692f-3724-8a9c-a6005df9effc | -9.00355 | -47.04913 | 2025-09-15 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98d0b699-3181-3c69-9b30-618a6a620920 | -8.97278 | -46.21791 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c44f7d6f-a029-3606-9fbc-20df29509bd6 | -9.01214 | -58.99169 | 2025-09-15 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 12c5687a-c6a3-320b-90c9-c22a5643072a | -8.78622 | -46.04076 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5891d053-6f02-3406-94fa-911c87a5b803 | -11.26538 | -50.8288 | 2025-09-15 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fe2b214-de41-326f-ab53-f03f0c4bc530 | -8.61712 | -45.74628 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7edbf877-d588-37a3-9c90-ce70f238c1e0 | -9.1772 | -47.04441 | 2025-09-15 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c024ccd-b674-3443-8e0d-fee2e8f94308 | -8.41356 | -47.22791 | 2025-09-15 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d82e7fde-7a01-3740-a5c8-57f88e3625b6 | -8.92778 | -54.44732 | 2025-09-15 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd3095d9-a567-3968-80fb-54e5cd66ecbf | -7.85641 | -46.11453 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8de35afd-0dac-327d-8bdd-7452c541134c | -6.98001 | -44.54188 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3ab167d5-92ff-330d-a0b6-5b9b36c5e54b | -12.66894 | -47.72691 | 2025-09-15 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7b4fe534-be02-30a4-964c-5fd738bbff36 | -8.45412 | -64.14255 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b12c8e47-14d9-382b-aa17-376bcf5ef73f | -10.65776 | -46.23819 | 2025-09-15 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c2c1dfb-be16-3bc6-a91d-90fcf007b128 | -8.61851 | -45.73564 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98dcb57d-9f14-38b5-adb2-37d233aab260 | -8.89925 | -46.16466 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 431ffece-29c4-3f3b-9c20-20e441b4a64f | -9.13336 | -46.95731 | 2025-09-15 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ba4490b-f464-381f-a666-e25fb6860d9d | -8.98452 | -45.82201 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4982a7c7-5e4b-301a-934a-9154195fe50e | -7.98659 | -45.66222 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5316c1f4-fd4b-366f-8514-aa65c39e6c5f | -11.26579 | -50.82649 | 2025-09-15 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 172e2e9f-52e3-3a98-a858-0c10bd350a2e | -12.44022 | -44.74691 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 844bfb55-5cf3-3b09-838f-36501c0cc128 | -7.50919 | -44.37303 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf2c0a56-466c-31d6-94d1-1cd2b90a2ac7 | -10.70154 | -50.67173 | 2025-09-15 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0775274e-f70f-3702-819a-08305c56c65f | -7.69497 | -48.86321 | 2025-09-15 05:10:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9e49fab-c8cc-3efd-a6ea-b915e8d09c2d | -7.49075 | -44.68377 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d91334a-955d-39c5-9adb-51e1971ee547 | -10.41743 | -60.46379 | 2025-09-15 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6ff66ed-45fd-3cf5-ade6-28d03e5e55cf | -8.45487 | -64.13828 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12ff8767-9472-385d-90da-d01f67a98ce6 | -8.97608 | -56.33771 | 2025-09-15 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ae76e60-7248-3488-8f6e-c2e8a81a4060 | -7.69531 | -44.67828 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0fac41a-2359-3157-a692-66379c6379c8 | -8.64383 | -45.6943 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce1f2bc1-c9fa-3332-814c-eefacea1d8c2 | -8.91111 | -45.51123 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2895a295-acb8-3f0e-a72c-ff49a8bf3200 | -9.00782 | -47.06342 | 2025-09-15 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b7303c1-dd48-3fa4-9e5b-9fd12a8b01e4 | -11.71683 | -46.48773 | 2025-09-15 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec4e0b46-3aac-3059-8118-d50be4a58631 | -8.92517 | -54.44428 | 2025-09-15 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9edb235b-6786-37b8-adb9-356de3eea034 | -6.44733 | -44.52584 | 2025-09-15 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f68c2691-1521-3154-b2f7-384d07218d12 | -11.07681 | -49.72258 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5118cb42-cc52-3cad-89e4-8a7f8314cf41 | -10.73266 | -44.77452 | 2025-09-15 05:10:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c67611fa-b892-3c10-8f43-7e0a64dc613b | -8.7377 | -70.54471 | 2025-09-15 05:10:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d36e196-b958-3afc-8f76-eaa08f31e4f6 | -9.12837 | -46.94823 | 2025-09-15 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65482999-a77b-314c-8eb7-e612ea78de32 | -7.3899 | -49.993 | 2025-09-15 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e851ba7a-9061-3859-95cd-e41cf807750b | -9.12333 | -46.93963 | 2025-09-15 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57371881-45ea-3bca-ac28-b8cbfba964e9 | -8.91399 | -45.4882 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33fca59c-895b-32f6-9bea-32e61b9a2657 | -8.62427 | -45.74182 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0094a541-6756-32b4-853e-52599c5b6183 | -11.8091 | -50.43265 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 578579c6-10fe-3418-a104-09c23492e718 | -10.88098 | -45.44536 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 292ac57f-28c1-3ea1-a250-e7e591d1e88e | -9.23492 | -45.66951 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8664d154-74fd-3984-8da4-58f665730c87 | -8.96117 | -45.79877 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f856f9f0-14be-338a-a9d8-764e6e47c442 | -10.71541 | -50.64125 | 2025-09-15 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 28348bc3-40da-3618-a83a-b5fb6f76b25b | -11.40205 | -51.36046 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6e1e378b-8bbe-3f22-984c-39d11f68f03e | -12.4441 | -44.74647 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 951dafa3-8e54-3738-9e82-65fe389b6034 | -9.00544 | -49.77031 | 2025-09-15 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d8c7b92-febd-3bfe-a231-5ddf0f1de020 | -11.39747 | -51.36727 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 745b1ed9-df29-312d-9346-d5b0c95ce996 | -11.82822 | -50.44101 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 834a09f9-6983-3f62-ac04-afd85fc59d54 | -7.63472 | -49.74696 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6b36a52f-8ee6-3024-879e-ce100f0a128f | -8.64711 | -46.37225 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4438e936-d971-35bc-ab03-eb287b91c534 | -6.97917 | -44.54805 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 50275ceb-35c7-3b4a-8bbe-2a441934fdd6 | -6.14062 | -55.78473 | 2025-09-15 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1871e51a-d05f-30cc-a21d-a231544f6207 | -11.07992 | -49.73878 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d795cba5-cb7c-3ee1-9e07-63df8566ab5c | -8.42103 | -47.2265 | 2025-09-15 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18483ee8-58ba-340d-8424-c421ef1e5b47 | -10.93377 | -45.57868 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8867a193-f78f-33ce-8be3-119163f3a6c9 | -7.64196 | -49.73115 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1228294c-c6a7-3f88-be16-914a1a1e9e9b | -7.50163 | -44.37486 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f430fb51-a417-32a4-9218-1be80dd8381a | -6.68979 | -45.5128 | 2025-09-15 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c07df18c-6023-3785-9795-8c051ecc3e04 | -8.61945 | -45.7317 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08398691-6dd1-3467-ae8e-5414bb460454 | -8.96834 | -46.05223 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 04f4c5ca-6805-3d02-a557-4fe767e412f0 | -8.91111 | -45.45763 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34b2dfec-1671-35a8-b69b-0369a79d1d66 | -10.79263 | -45.98747 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39f86594-5f82-3f40-8eb2-f36d75040e8e | -11.29763 | -51.13652 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbd121d5-354a-3752-9a2e-a202a7fb1aab | -11.08762 | -49.73412 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31454ac2-0e7c-30a6-a562-18693f54caac | -11.27707 | -50.85174 | 2025-09-15 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eab89e4d-aea4-3f5a-a891-8c3c3a60d151 | -8.97576 | -46.21993 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0b590e88-0187-379c-b392-93ad1890f3af | -8.9918 | -45.76422 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15624a75-f93a-3dc3-83d2-cebc5bc59cdd | -7.98725 | -45.66362 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b82fcd64-4821-3da9-8c99-b4d06b348a53 | -7.35713 | -44.29766 | 2025-09-15 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9976ba75-a076-3cc5-9cc1-6dfcf103402a | -10.24685 | -55.81641 | 2025-09-15 05:10:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eaddda64-174d-3337-9e20-08c82e858b71 | -11.71744 | -46.48245 | 2025-09-15 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8f47679c-75d8-3e8c-b736-17c7bf84fa3e | -7.98595 | -45.66706 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41c02882-9d6a-36d9-9acb-b4873c37804f | -10.19103 | -46.16306 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55f958ca-f350-3ebc-9948-da1924198690 | -10.92691 | -45.57915 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 798018a0-de68-365d-977f-4df06e31aa02 | -7.98081 | -45.66281 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2f82ef7-6ca4-3234-979a-947f2b617a1f | -6.52983 | -51.19241 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9eab6ca0-5819-3039-94e6-808af3fe59df | -6.66364 | -45.56261 | 2025-09-15 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79937d4b-d40e-30c0-b99d-2d813f55f591 | -11.77857 | -50.43438 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ccaa2e51-7836-388c-bca8-7c6f868fc5f4 | -7.37038 | -44.3586 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69811a1e-6a4c-35c0-84f6-8d06fad810b6 | -9.06689 | -44.82629 | 2025-09-15 05:10:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb2a00dd-cfde-3c35-8000-3ffb9e19033a | -9.69038 | -61.99917 | 2025-09-15 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9f93abb-0726-328a-a599-a0a89dc13926 | -8.59871 | -46.35565 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c514a156-9e24-392d-a39d-37d81bd752cb | -8.96383 | -45.77737 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e6d8771-f5ef-36cd-979d-388a607ba2c9 | -11.86036 | -50.50305 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2a8b11b9-6cfe-3258-9e5e-ef89859d24be | -10.88532 | -45.44429 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README61.md)
