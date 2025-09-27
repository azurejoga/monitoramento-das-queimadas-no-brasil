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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc2dbfac-7c6d-374a-8d29-e6d39d0349ff | -9.0391 | -45.5334 | 2025-09-27 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 4dfb9c1f-eeb8-35d8-8e9b-ded3cadbbea0 | -6.7172 | -42.7629 | 2025-09-27 13:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| c3b3f4e8-e6de-3c3f-85e9-bc5198e0efa9 | -12.6495 | -51.6797 | 2025-09-27 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 236.9 |
| 95fde1fe-756c-3461-b4ed-c2b09f63522e | -6.8444 | -43.1745 | 2025-09-27 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| e53c1d05-ff31-39e6-92af-67e9af9dc226 | -11.3646 | -45.0108 | 2025-09-27 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 8cfc2f90-182e-300b-ad9f-dded4cd24f47 | -10.0062 | -46.7081 | 2025-09-27 13:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d3f612f4-a784-3d1f-8aa2-c971db8882d7 | -18.3049 | -57.0938 | 2025-09-27 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| a301e4e3-f52f-3fcd-bd78-d710cc3b9df2 | -6.5803 | -45.0889 | 2025-09-27 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 5d6917e0-245e-3ea4-b630-47705a82d419 | -11.0125 | -45.5189 | 2025-09-27 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| eedfa59d-2ad6-3cc6-8a96-695b50844ccf | -8.6439 | -44.0164 | 2025-09-27 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| f55be157-4316-3ed1-a1bb-ed402ee87c66 | -8.71 | -54.6467 | 2025-09-27 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 25f497cd-8c6b-3ccd-9024-05c136ee93ed | -5.6813 | -43.0619 | 2025-09-27 13:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| e652f415-8586-3664-9fe3-049cadd42329 | -8.8409 | -46.2544 | 2025-09-27 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 347349fe-a265-30c9-9679-a32e3bd56048 | -5.475 | -43.0774 | 2025-09-27 13:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 772d2ce4-2b35-396c-ae98-aceb8c801e1a | -5.7588 | -42.7976 | 2025-09-27 13:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 0dbe66fb-f819-347b-aaa5-e09949f5bb81 | -7.7794 | -46.9371 | 2025-09-27 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 256.7 |
| fa67c5d3-8ba6-3c2d-acd0-1b011c818e02 | -7.3849 | -47.0157 | 2025-09-27 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 7f13447e-399a-3520-86ad-13116744d622 | -14.0807 | -48.8292 | 2025-09-27 13:30:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 8c3462a0-f78c-3f53-b54c-d218d9332ae2 | -11.4417 | -44.9767 | 2025-09-27 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| f944c4f7-7489-3a83-a624-6ba26f42f6fb | -9.2871 | -48.2015 | 2025-09-27 13:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 029c9909-d3ef-3de9-9b93-44c231bf4421 | -8.6628 | -44.0142 | 2025-09-27 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 42e1cb99-c4a7-3659-9d93-0b0d088ae2ed | -11.3642 | -45.0339 | 2025-09-27 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 215.9 |
| 966f3295-d1a2-3c73-9c20-0705f09efe06 | -6.5801 | -45.1117 | 2025-09-27 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 1913027c-cc1f-3ba7-aba0-0b298c2f8d84 | -5.4937 | -43.0761 | 2025-09-27 13:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| bd3a2c49-7761-30c0-9c0a-af6b277bcc61 | -9.6162 | -47.552 | 2025-09-27 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| bad92f88-9d24-374a-ba7b-4579777bdcad | -7.1571 | -45.5158 | 2025-09-27 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 8990cae2-b6c8-3be9-b253-27544fbebd59 | -9.9772 | -43.5962 | 2025-09-27 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| b936552d-8696-38ce-bfcf-afeaf79916fc | -7.5571 | -46.6906 | 2025-09-27 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ad6f9b24-6693-336c-ae7a-88ec6753a3df | -11.6062 | -44.3257 | 2025-09-27 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 2147611e-c395-3956-ba06-8833c1b45910 | -14.0191 | -56.0927 | 2025-09-27 13:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 6d1d4dcb-b003-34ad-a943-8fbffe587254 | -17.1739 | -56.3892 | 2025-09-27 13:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 141.6 |
| 66b92d64-539f-32c4-8266-995822aa4b29 | -7.3847 | -47.0378 | 2025-09-27 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 4373a255-9da6-3428-92a7-b615b31fd910 | -6.6983 | -42.7646 | 2025-09-27 13:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 148.3 |
| 4f7d9f53-f815-387d-bc93-cce46d3a61a4 | -7.798 | -46.9576 | 2025-09-27 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 49db5165-8229-320b-8ed3-accf7b8bade9 | -6.6983 | -42.7646 | 2025-09-27 13:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| e33ef096-42e4-343c-9b7d-f777407c189d | -11.3846 | -44.9618 | 2025-09-27 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 3fcbd77e-7e4f-3bad-a71d-4f7455398f03 | -7.7794 | -46.9371 | 2025-09-27 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 307.9 |
| d0c5bd8f-d8ab-3aff-b6e8-814b23e2d2b0 | -5.9472 | -42.7118 | 2025-09-27 13:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 577ea70f-17f1-36e4-8653-6e9e8dc0cf9c | -11.4425 | -44.9303 | 2025-09-27 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ebae9ebc-ff33-3c7f-9193-56a6ec703521 | -10.0062 | -46.7081 | 2025-09-27 13:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 97001635-6e5a-3de1-aff0-bb63ebb132e7 | -8.1363 | -42.3801 | 2025-09-27 13:40:00 | GOES-19 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| ee076bf0-31cc-3fc4-8ce8-59dbc563baab | -11.4221 | -45.0025 | 2025-09-27 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 14b71e5f-da51-3e6f-ab9f-6c98a55c6fb7 | -9.0391 | -45.5334 | 2025-09-27 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 81b5ce7a-818b-34a6-84fd-c76f95ac0dae | -5.475 | -43.0774 | 2025-09-27 13:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 1f730082-9bba-3815-bc81-5b474860a1c5 | -11.385 | -44.9386 | 2025-09-27 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2a5085cc-3e3f-3f05-a396-14e687d08bde | -18.3049 | -57.0938 | 2025-09-27 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 0bcc01cf-e256-325c-a4ad-40139a008876 | -11.4413 | -44.9998 | 2025-09-27 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| d9884d3c-fa3a-3d16-ab74-16c2e975a6db | -12.6498 | -48.1509 | 2025-09-27 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 13022b50-4efb-358a-8f7b-79d66c0e2718 | -6.2087 | -42.8549 | 2025-09-27 13:40:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 00bc0e82-60c0-3960-b0ab-af92fd64e4ef | -9.9772 | -43.5962 | 2025-09-27 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 1b755133-f557-3141-8277-c554775a9b6a | -7.8547 | -45.293 | 2025-09-27 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 21e552d8-d36e-347c-bd3d-79f570437028 | -14.0191 | -56.0927 | 2025-09-27 13:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 767b84ad-6022-3faf-9279-bbfc3a2e5848 | -5.7961 | -42.8182 | 2025-09-27 13:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| cf6518c7-e77e-3ada-9679-89a2f7e2e55b | -11.4417 | -44.9767 | 2025-09-27 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 69cc95e9-93cd-3393-8f2d-14714bc7bdc7 | -8.6631 | -43.991 | 2025-09-27 13:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| f1a6d84e-19a9-377b-a9c3-5c34a8348bc1 | -5.7588 | -42.7976 | 2025-09-27 13:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 8df77271-48cf-32a9-b40a-98515f88eab8 | -7.7609 | -46.9166 | 2025-09-27 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 2fd00514-84ee-3240-b65a-f3281363f48c | -8.6442 | -43.9931 | 2025-09-27 13:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| fb13e5d5-13a8-3f6f-9124-571a5192aefb | -11.0125 | -45.5189 | 2025-09-27 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.5 |
| e4c19e40-179a-3ae2-b334-7782fce0cc13 | -20.7342 | -57.7873 | 2025-09-27 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.9 |
| b191ee6d-a8c4-31fa-9f39-fe856139877c | -14.8253 | -45.6282 | 2025-09-27 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 65abc6e9-7305-3e4e-b49b-5a03e96426ba | -9.3343 | -48.9364 | 2025-09-27 13:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5242ae8d-edb2-3c14-8d15-8cd57d26f6df | -12.6495 | -51.6797 | 2025-09-27 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 425.2 |
| 2583e60e-bb54-3ecb-b089-3509625d2ee9 | -9.334 | -48.958 | 2025-09-27 13:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| ea130437-49e5-385b-9db8-454903ac3362 | -5.7775 | -42.7961 | 2025-09-27 13:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 425a0304-9f9c-3450-80b9-dee497beba24 | -9.9776 | -43.5727 | 2025-09-27 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| b2434874-0b44-3e23-ac2c-eef8263c012c | -10.2034 | -50.2468 | 2025-09-27 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f2ae1ad8-9f52-3e7e-85eb-39ab1bf0e42c | -5.3693 | -42.3077 | 2025-09-27 13:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| e64a5b8f-8185-39a2-84e0-cae63f9c2490 | -14.0613 | -48.8321 | 2025-09-27 13:40:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 476019ae-f852-3c6f-a6f1-5589348e6b90 | -7.3849 | -47.0157 | 2025-09-27 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 3600873e-6385-3766-8d79-b92cb6851424 | -6.8444 | -43.1745 | 2025-09-27 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 7147c84a-039e-306f-9675-2d972a3f2f0f | -14.8304 | -45.3947 | 2025-09-27 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 22129d4d-786e-3b81-8f29-e9e71f5814a0 | -7.1571 | -45.5158 | 2025-09-27 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| fbfb5f78-249e-3267-842c-3ee1a8f05262 | -17.1739 | -56.3892 | 2025-09-27 13:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.5 |
| c82cf452-837e-3384-9d44-e1f7791e4a7c | -14.85 | -45.3911 | 2025-09-27 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| f7b9beff-c99a-3252-a2cc-c55c4f25de64 | -8.822 | -46.2564 | 2025-09-27 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 045ca2db-1ca2-3e36-bbf6-c70243a8e872 | -11.7006 | -44.4049 | 2025-09-27 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 11c1bb61-6058-3cb3-bebd-c159774e5a16 | -5.4937 | -43.0761 | 2025-09-27 13:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 61cc2573-b5d1-36c5-9c3e-25951e07e9d7 | -7.7797 | -46.9149 | 2025-09-27 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| a805b656-ee9a-3327-b318-69938f3f05ec | -7.8735 | -45.2911 | 2025-09-27 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| f0da19ad-bac1-3a66-abdf-c623f4a96b52 | -8.4827 | -47.8202 | 2025-09-27 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| e2922479-7315-33d3-a9f1-ee72228ee34f | -7.7792 | -46.9593 | 2025-09-27 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| b9f608af-6a46-318e-9893-b8094ea8df08 | -14.0807 | -48.8292 | 2025-09-27 13:40:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 9b07f044-712f-395e-959a-4916638c6191 | -9.6162 | -47.552 | 2025-09-27 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| b4dcb960-34bd-32a1-8652-8a643ef434f4 | -6.7172 | -42.7629 | 2025-09-27 13:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| e1057c9f-b3de-3c67-a60f-25656e8bfd61 | -7.7558 | -47.3809 | 2025-09-27 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c90a29d5-0f39-36aa-ae59-4322ec713426 | -9.2871 | -48.2015 | 2025-09-27 13:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 8e8617c2-af57-35ce-93b0-321e561ac1f0 | -7.8732 | -45.3139 | 2025-09-27 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 5476c6b5-2a6c-3ccf-8950-594d819b5b32 | -11.3451 | -45.0366 | 2025-09-27 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 215.8 |
| 19c777a5-f80c-385c-88d7-ecfd1480e688 | -8.8409 | -46.2544 | 2025-09-27 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 0a31f1f2-1984-3ba6-baa2-14155d4b5f69 | -7.1383 | -45.5174 | 2025-09-27 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a349fe89-701a-3c83-bbbd-c44f8e0df7a8 | -7.3847 | -47.0378 | 2025-09-27 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| a1b5f82c-ce4c-38df-a4b6-8007dbdc9561 | -9.3517 | -47.5801 | 2025-09-27 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 5b5c91ca-ffdf-3e6c-968c-03b41dc0ca61 | -9.6159 | -47.5741 | 2025-09-27 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 268baf7d-f24b-379e-976c-e33182208f18 | -8.4825 | -47.8421 | 2025-09-27 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| b519d0be-399d-3396-b016-0de295e4dfeb | -11.3642 | -45.0339 | 2025-09-27 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 231.3 |
| e78bee4a-985a-3a88-9530-b826c046aa07 | -11.3646 | -45.0108 | 2025-09-27 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 27bbdd9c-d106-32e1-904a-77ac298f284b | -7.3659 | -47.0394 | 2025-09-27 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| ca4f96f7-38f2-3c03-bc94-022bfd9ae997 | -7.1383 | -45.5174 | 2025-09-27 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| afe97168-ef9f-30f0-be18-8913860c9cad | -6.6983 | -42.7646 | 2025-09-27 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 124.4 |


[Clique aqui para ver as próximas entradas](README66.md)
