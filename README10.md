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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea458aeb-5847-3c39-a904-d75f066fa4c7 | -10.20153 | -49.14971 | 2024-10-26 01:07:00 | TERRA_M-M | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bb7f421a-7b8c-3858-b477-97ed377e02b6 | -10.1991 | -47.63568 | 2024-10-26 01:07:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3dde614a-afba-347f-aefd-84de533c1842 | -10.19742 | -47.62451 | 2024-10-26 01:07:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3c64efe3-9cd1-3716-940a-675bafa177c7 | -10.05857 | -48.06126 | 2024-10-26 01:07:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 44857840-6e50-30e1-b91c-cd5ad0b8fb57 | -11.51233 | -45.83288 | 2024-10-26 01:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3d397517-6b64-3329-ade0-2bd108e7897c | -10.57523 | -45.14683 | 2024-10-26 01:07:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| c670c4e7-f453-335a-b358-76a5a1714462 | -11.53368 | -43.98849 | 2024-10-26 01:07:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 27f682ae-a0ac-3f25-8556-ea0f17cfd0cc | -10.56349 | -45.14875 | 2024-10-26 01:07:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8d345e7f-188f-304f-9941-631446be968b | -9.73 | -48.26609 | 2024-10-26 01:07:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f77a59eb-d86d-3a71-b265-5f74fae27e9f | -9.70144 | -46.26157 | 2024-10-26 01:07:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 9b92336a-ddbf-38e0-87c0-535b42da4110 | -9.63168 | -47.6097 | 2024-10-26 01:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2c5e3acd-b9f3-305c-b493-1e3b141332bd | -9.62996 | -47.59831 | 2024-10-26 01:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| a534effa-7167-3df1-ac31-c1a29e4758f5 | -9.50821 | -47.81463 | 2024-10-26 01:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| b5f5aa76-942c-3afd-9987-ad8aa9605459 | -9.50656 | -47.8035 | 2024-10-26 01:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 20b9be4d-0296-3cff-8d8c-6ebaf29cae5d | -9.49841 | -47.81628 | 2024-10-26 01:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| d206e8d8-7f58-386f-b87b-09dcf95fe4d3 | -9.49675 | -47.80511 | 2024-10-26 01:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 18979b18-153a-38bd-9625-1537c3d76ac7 | -9.48859 | -47.81782 | 2024-10-26 01:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6c62bec8-7ed1-3748-a8c0-9840b3f9e78a | -9.29663 | -46.1761 | 2024-10-26 01:07:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6930213c-f4ca-3d5c-ab96-d44db1a07154 | -9.2962 | -46.18256 | 2024-10-26 01:07:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c2e3dd6c-75dc-3085-a59d-42d7be53d6fc | -9.29401 | -46.16799 | 2024-10-26 01:07:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 58a718a8-e9e3-3743-b748-c0b79f922ca5 | -9.26677 | -47.91554 | 2024-10-26 01:07:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| be8632cb-dfe2-3b42-b6a8-0f6b7c303390 | -9.07524 | -48.00235 | 2024-10-26 01:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c1457978-9fd7-3bb1-805b-5b279bac12cc | -9.06548 | -48.00393 | 2024-10-26 01:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| faa41c05-323a-39de-b0b0-75292246eaaa | -9.05012 | -48.72277 | 2024-10-26 01:07:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 39e10283-5ecd-3095-86d4-0f8e23a0d1b7 | -8.90617 | -48.53749 | 2024-10-26 01:07:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b2613635-436a-30ce-8930-3cf5b7340ebb | -8.89668 | -48.5389 | 2024-10-26 01:07:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 2e68b367-a7f7-3fda-85d4-ab1eeb2589d1 | -8.89517 | -48.52842 | 2024-10-26 01:07:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9e52bbec-468a-3fcb-bec6-6c7d6fe5df67 | -8.81415 | -49.69799 | 2024-10-26 01:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| ba463286-3d7e-3c25-b379-b0c4b5ace759 | -8.81281 | -49.68869 | 2024-10-26 01:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 5e447275-af56-36a7-8bc9-e643b5b79688 | -8.60962 | -49.03905 | 2024-10-26 01:07:00 | TERRA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c2d672f4-12e9-3bb7-b07e-65b0e98daf4e | -8.56754 | -49.20511 | 2024-10-26 01:07:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88ef4d52-8bd8-3ba3-92b5-89f983df296a | -8.55834 | -49.20648 | 2024-10-26 01:07:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 12f787f6-05b8-3c43-b359-8a773cc87db1 | -8.54616 | -49.56498 | 2024-10-26 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| faa75f18-a831-38f2-9f03-7b876de03dd7 | -8.54482 | -49.55561 | 2024-10-26 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| e136e1dc-3623-3e7a-b4d5-2f1818987638 | -8.52814 | -50.14841 | 2024-10-26 01:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74e29b92-c7a5-3420-8e9e-16ba3d5c65c9 | -8.47498 | -47.82103 | 2024-10-26 01:07:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b0085e9b-4341-3632-953a-eb84ce00fe59 | -8.47325 | -47.80944 | 2024-10-26 01:07:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f2a67754-ec7c-3995-afb3-27d5a49bece4 | -8.39376 | -50.05031 | 2024-10-26 01:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 678468fe-6519-3d5d-9dcd-81ea8bbdaf6a | -8.36135 | -49.82053 | 2024-10-26 01:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5573547d-1086-3746-85ec-4ac4123fbe9a | -8.18772 | -49.50751 | 2024-10-26 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5a0b48e8-a908-3f34-9bbe-6dbd17182ad6 | -8.18636 | -49.49804 | 2024-10-26 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 759d275c-e871-36bc-8acb-5ddb9fa7e010 | -7.99285 | -49.69324 | 2024-10-26 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2c8d18b8-d61d-3522-8234-188380550c59 | -7.98377 | -49.69456 | 2024-10-26 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| c7da56e8-c32d-396a-8b85-65e0ca57a136 | -7.97598 | -49.70207 | 2024-10-26 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5cd7ab51-b883-38e0-a7bb-338af75d9001 | -7.97465 | -49.6927 | 2024-10-26 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| d6c57490-f355-3dba-b1a2-150925778aa0 | -7.90299 | -46.69636 | 2024-10-26 01:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 654ee1cb-b995-31d8-a68e-40864b630462 | -7.90082 | -46.68238 | 2024-10-26 01:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| a29197a4-e813-301f-a736-89e5fb70a076 | -7.89909 | -46.68925 | 2024-10-26 01:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 565b4994-026b-3627-82e3-76f6544a3113 | -7.89701 | -46.67519 | 2024-10-26 01:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d87ec87d-088f-3a51-b859-2f24cff50c2d | -7.73246 | -49.54754 | 2024-10-26 01:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 40137623-55cf-36dd-bed7-7f8a0e77068d | -7.73109 | -49.53798 | 2024-10-26 01:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7a36bada-ed10-3174-902e-d32f648cc473 | -7.71578 | -45.70419 | 2024-10-26 01:07:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 971150f0-29ff-3ca7-b3dc-7ecc9ac99e7e | -7.67219 | -47.31427 | 2024-10-26 01:07:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| e0452306-a181-339c-a55d-3541370945bc | -7.66173 | -47.31585 | 2024-10-26 01:07:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f6b35e81-65cf-3938-a2be-2038925844ce | -7.59466 | -47.08791 | 2024-10-26 01:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b34b4cf8-bfa6-34da-9f21-08da717f63d5 | -7.56173 | -46.80225 | 2024-10-26 01:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| de6d3f24-caa7-341b-9759-d6c4ee231a1d | -7.55959 | -46.78836 | 2024-10-26 01:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 02ab1e30-26c7-35e0-971f-9ea3c19e073d | -7.55768 | -46.79507 | 2024-10-26 01:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 318145ea-d375-365d-ab07-6a016bc9dfd1 | -7.54122 | -45.84457 | 2024-10-26 01:07:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 02be6ab7-4ca4-366d-9d7a-e6b9e69d36e6 | -7.53869 | -45.82811 | 2024-10-26 01:07:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 03f221e7-49ad-381b-ba4a-58c3c245279b | -7.40816 | -45.57843 | 2024-10-26 01:07:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0452e108-7634-368b-bc66-d3faebe4955b | -7.30216 | -44.97894 | 2024-10-26 01:07:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ac792313-4a00-3c18-a6a6-4b9be6ff4d71 | -7.29832 | -49.28998 | 2024-10-26 01:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 41b93d2b-d2fa-3376-b30d-2696ed0818dc | -7.15048 | -47.86467 | 2024-10-26 01:07:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cb210fb8-b190-3fb1-96a3-5bb36da40d64 | -7.14025 | -49.27518 | 2024-10-26 01:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| db97a6fd-ff63-3840-8e8f-a9ae895f45b1 | -7.12744 | -46.37659 | 2024-10-26 01:07:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c8396830-29d3-3bd8-a37f-ff6210c9345a | -7.12692 | -46.36787 | 2024-10-26 01:07:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3625d440-2975-34bd-97c0-a02c43977ebb | -7.1251 | -46.36151 | 2024-10-26 01:07:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| daa5ad72-9415-3eb4-a9b9-9c1a999abef5 | -7.11657 | -49.17701 | 2024-10-26 01:07:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c2606628-ec5e-38fe-8bdb-98da8be2c485 | -7.09349 | -49.14983 | 2024-10-26 01:07:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1c55c0a0-34b5-3d4f-8572-3e76ada0a980 | -7.09204 | -49.13983 | 2024-10-26 01:07:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a19702ac-2776-377e-9971-0e2756b5d7f7 | -7.03228 | -49.16473 | 2024-10-26 01:07:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 17874d41-0b14-3d96-9f92-a60e114d7767 | -6.89329 | -50.32095 | 2024-10-26 01:07:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d387c20-db83-341a-a4c4-e8fa835bc01e | -6.868 | -45.89249 | 2024-10-26 01:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 872610f9-dada-3323-9a22-de536a69365e | -6.85109 | -51.00782 | 2024-10-26 01:07:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8fe09418-eef8-3619-a58d-2269cf688fc8 | -6.81417 | -44.47464 | 2024-10-26 01:07:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| aeac21b5-a9f5-3119-97ae-5b148340deab | -6.797 | -50.87967 | 2024-10-26 01:07:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eeca047f-ce55-316e-b813-a1160dd16bd7 | -6.79574 | -50.87074 | 2024-10-26 01:07:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7be4a6c4-07f7-31ac-b5a4-84d0d0dacc33 | -6.66174 | -48.78602 | 2024-10-26 01:07:00 | TERRA_M-M | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4a79d12f-fe56-3908-8138-b44272afc1cf | -3.12758 | -50.61115 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 04680549-8dc5-391d-90a0-76476a27b99f | -3.12628 | -50.60182 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 6f5ff35f-18c3-3392-98a6-50efa5ace7f5 | -3.11716 | -50.60308 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2ad0c1fc-619e-3471-ba17-3d868eef9f65 | -3.10947 | -53.72596 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0f16f92c-69af-3f21-86a8-15f89c47f988 | -3.1073 | -54.99669 | 2024-10-26 01:09:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe928193-684d-3a3a-8aef-7fe9788ca8e8 | -3.10198 | -53.73284 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 3fc288f6-3ec4-3f96-baea-c132dca45403 | -3.10186 | -51.34883 | 2024-10-26 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f29e3741-24a0-3a4d-ada1-48eb1ef5c77a | -3.10066 | -53.72344 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 9b3c36e4-787f-384b-aa83-ecdf7b99830e | -3.10061 | -51.3399 | 2024-10-26 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 70164dd6-cc68-3640-8931-dc86ab43c13f | -3.09935 | -53.71405 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4db1e7dc-f20b-3504-a4cb-ba35179c5b8e | -3.09296 | -51.3501 | 2024-10-26 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1aeedc8f-1bff-30b0-89ea-9b850954de61 | -3.0917 | -51.34117 | 2024-10-26 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a04d63ff-4715-3e4f-a326-23aa259008ca | -3.08886 | -54.4351 | 2024-10-26 01:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 646c7a79-849b-3f23-8d0a-9499aa7f14f8 | -3.03066 | -52.35282 | 2024-10-26 01:09:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cf3c3bf0-2757-38d0-a91d-428b583cb75b | -3.02944 | -52.34404 | 2024-10-26 01:09:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8dc1adf2-8c44-3b1d-a718-47edf6219a8a | -3.01838 | -50.48809 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a1ec5545-ae94-3f22-b964-b0bfbf926627 | -3.01706 | -50.47857 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a16d4e61-b6c9-3adf-8ca2-84fb0b8b4da9 | -3.01442 | -54.49257 | 2024-10-26 01:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 17d9966d-64e3-32aa-9f7e-f3ffceab48ba | -3.01054 | -50.49892 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 954c53ac-1af2-31f6-920c-9124472a6dd3 | -3.00922 | -50.4894 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c59aa860-310a-3a63-aa43-1693fdc1b76a | -3.00789 | -50.47987 | 2024-10-26 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |


[Clique aqui para ver as próximas entradas](README11.md)
