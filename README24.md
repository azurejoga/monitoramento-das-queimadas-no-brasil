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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d00ad47b-20bb-3719-9a9a-5394e610c11c | -9.87189 | -48.35968 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f88ea41b-a030-357c-8111-e687b25592aa | -9.86706 | -48.35349 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72d0248c-190d-3be9-a3f4-fd5a0d194c76 | -11.59141 | -46.87999 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75625145-8836-38e4-8907-7c7927d74588 | -12.31903 | -47.96241 | 2026-09-17 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf80df37-3436-392f-87ab-32e35b2dc631 | -8.47748 | -46.8914 | 2026-09-17 03:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| deeccf33-35a1-309b-9c38-f1aadbda9498 | -9.48134 | -47.23238 | 2026-09-17 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7567d8e8-26a8-3570-8df9-892673e560f7 | -9.75017 | -46.11598 | 2026-09-17 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cda3341-2a99-3efe-833b-3d7369e2d763 | -12.50621 | -50.86248 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 276f7884-82ee-3428-93e4-d29be3f8d20c | -12.47738 | -50.93675 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3e9ed51-44d3-377b-beef-5805ba466e09 | -8.78539 | -46.90592 | 2026-09-17 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ca463db-e424-3bbf-9add-0ba94aca984a | -7.97231 | -44.03946 | 2026-09-17 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1206629e-4699-3bba-94e4-4deddbefdf7b | -6.88478 | -45.47277 | 2026-09-17 03:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 353a28d6-9884-36cd-bbdb-356fa1a4a062 | -8.90658 | -43.88617 | 2026-09-17 03:55:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3076a376-15ff-33c4-958b-d695c67b99e1 | -8.48802 | -44.70148 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad079ae8-1d95-32b6-a970-bf265aa100cc | -14.5573 | -39.62884 | 2026-09-17 03:55:00 | NOAA-20 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ba1df469-41cb-3c8b-8173-063286db301b | -12.46629 | -50.79654 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| d3d91686-a249-3f15-97fe-07c96f15a2fb | -12.4714 | -50.90069 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1e886199-328d-33b7-9082-9aeed5fe0f31 | -7.03972 | -42.06801 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| eccc6b03-89c3-327e-a691-9f1c71cefdee | -9.30663 | -40.24855 | 2026-09-17 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 495c02fa-eef1-3458-a684-36ad549e031e | -10.04192 | -45.56636 | 2026-09-17 03:55:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 825ddeb9-a416-32ea-b96d-9c487ca5950b | -12.46856 | -50.7857 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ee936f77-837c-3bca-b8a5-2bb1d054be36 | -8.94213 | -44.3988 | 2026-09-17 03:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c692f1e-9713-3fbf-8513-1867f0789bda | -8.26466 | -42.18078 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6691e620-c8c6-3030-886b-4100bf1c50b5 | -12.7381 | -43.4544 | 2026-09-17 03:55:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e75f0eab-296f-36c0-ae2d-402ed71d9958 | -12.14228 | -48.25589 | 2026-09-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 544bc543-95fa-31b3-8b4d-8989df79adbb | -11.2728 | -43.48705 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad3a0e34-17b7-352e-b6b3-e1abc4edf508 | -9.61246 | -45.35523 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bb278bb3-81e0-34ee-836d-f4bd07354e8b | -9.57391 | -46.57491 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a37f93a-2ae6-3eb3-89c6-ecc4c0e11c7b | -7.72247 | -42.49606 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 1c2690ab-ded1-3e99-baff-8eb676536d56 | -8.85815 | -45.86445 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4406995b-b4aa-391d-afa6-8ab764388496 | -12.48582 | -50.86364 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 913f57e8-1669-3db2-a451-335638068753 | -12.44474 | -50.86612 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 06417bec-d9a4-3b34-a384-9c0b36fafa06 | -11.88239 | -47.5935 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a793b6ae-d3dd-356d-b42e-c0b415569e7f | -9.88599 | -48.38035 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1370f7bb-d5c3-3528-8765-23d46c6709ae | -11.322 | -46.78258 | 2026-09-17 03:55:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d0e9612-f6e4-345e-a506-45c5c85f9584 | -11.58656 | -46.89325 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5142b6a-30ee-3001-8b5c-96aa010ce18f | -12.45785 | -50.86889 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e0a728cf-3b9b-3eb5-ad87-c6652865f4bb | -12.50431 | -50.83918 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8c813b4d-1009-3bbb-b75e-142143819f0a | -12.43302 | -50.85772 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90a732bd-b2ff-325c-bd83-93c968675f0b | -13.3413 | -43.78065 | 2026-09-17 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6afb554d-fd92-3644-9be6-d62cf583eaab | -9.03988 | -47.7631 | 2026-09-17 03:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 39906be5-ee5e-36bc-959c-0af925144938 | -7.38286 | -44.49773 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 150f5e97-d8b6-3180-8a4a-70629da27185 | -9.9635 | -45.32127 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e4bce466-6348-3bee-8648-23cc2ba36dee | -7.43611 | -44.58036 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91dac009-0d26-3fa1-8fee-a2d041dab8b3 | -12.45622 | -50.90885 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c5501f5-a694-392f-82ff-3c42af12b9e8 | -13.73845 | -39.01538 | 2026-09-17 03:55:00 | NOAA-20 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| a819df20-68e8-3ac4-88c1-316a824f93b1 | -10.50778 | -46.28565 | 2026-09-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6227e71b-e8e8-3290-b457-c535e98ea322 | -11.19188 | -42.85332 | 2026-09-17 03:55:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3d839d66-5fed-39f1-b658-83ef039cce23 | -12.45143 | -50.83321 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5dc77791-2482-36ff-9b3a-b96948ffa0e8 | -10.79431 | -46.18713 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 204f102d-3a4c-3a2e-b011-42d8d137c476 | -7.73494 | -42.49466 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b4e0c6f9-bfe3-3938-9700-cbd3b4f8faec | -12.47341 | -50.82658 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 80e2b4c1-55a6-3d74-83b5-320fc8c89832 | -12.47722 | -50.77628 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 065ba8f4-c9b2-37b3-86d0-d31ca8bdf844 | -10.78937 | -46.18613 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 699cab83-910f-3184-a368-073513fbe42b | -8.78766 | -46.90592 | 2026-09-17 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 678d411e-6b3d-38ef-8706-7849baa183dc | -12.4915 | -50.83632 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| eb36f3f1-247d-3aae-bcf1-35cb08a5acbe | -8.85791 | -44.89582 | 2026-09-17 03:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7670493-b5fb-373a-a92f-14790cefa02a | -10.43503 | -42.73476 | 2026-09-17 03:55:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8df18934-5db8-38f0-ab45-57f4f5fd9bad | -9.59093 | -46.65898 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 121d5e7b-f5df-3bfc-b956-cea95f8b58be | -12.45032 | -50.83868 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 3e9684a4-3996-3950-81ab-23965690eee9 | -12.459 | -50.86341 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 411d0e17-57cb-39b6-a882-87f501566f62 | -8.561 | -44.55109 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f0c3753-9e2b-313a-910d-3d0ab535ae54 | -12.3251 | -47.96007 | 2026-09-17 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db83469e-a320-35be-9909-75d45ed390f5 | -10.78833 | -46.19172 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b58874bf-4549-307f-8445-aef2e08fbf2c | -9.88019 | -48.3792 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd45bf1c-2221-38d6-a10d-50f04f15262b | -11.89063 | -43.82426 | 2026-09-17 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fe9c68f-c923-3f89-b8c0-21196b834fa0 | -12.50318 | -50.84464 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bf1f5a87-ded8-3420-8622-9f9c91301cc3 | -7.12688 | -42.16925 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22bfc9a7-a3b1-369a-a684-5b14a15fece8 | -10.48877 | -45.28324 | 2026-09-17 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bdd0423-6a41-3478-a2fa-1dc463be2d82 | -8.56183 | -44.54648 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6837c06d-066a-3e18-bfd2-c0698ffca3e5 | -7.02514 | -42.07324 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4329ac61-8ec3-31cf-91f7-7f63b349f976 | -9.61566 | -45.36391 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b330850-6b92-346b-ac76-d400c4b28ce6 | -12.95336 | -48.61979 | 2026-09-17 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97e5529f-479d-3747-9c8e-4c2aed4db2ad | -8.24051 | -37.40398 | 2026-09-17 03:55:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| eae8b63c-47ce-3083-bbd6-1514d8c3c0e3 | -7.18895 | -41.80877 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eda86110-8016-3cf5-81a9-ab1f424ad153 | -8.85856 | -45.86011 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd35ceb8-d818-3314-b143-dc94bd40e936 | -11.34309 | -43.994 | 2026-09-17 03:55:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30c1315b-1c67-3cd7-b8fe-2f87c6972d82 | -14.55672 | -39.63242 | 2026-09-17 03:55:00 | NOAA-20 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e0f10b00-76fb-3aca-b819-1f3fec929462 | -12.49263 | -50.83086 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 14e78dec-56f7-39bd-9711-3c4b006fb770 | -8.85655 | -46.98526 | 2026-09-17 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9be6ca12-cc8d-3ae5-b18f-2937e3e52d36 | -7.38755 | -44.49852 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22241c62-eeb8-34af-82e0-81567c721ed3 | -12.48361 | -50.77769 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ba264c0d-ae82-37c2-b255-8090e7e021c5 | -9.49132 | -45.42903 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 7e2f3901-0b5f-31be-ad21-50362ebbee31 | -11.48124 | -45.78115 | 2026-09-17 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b49feb97-5e1b-3eaf-8c12-8541017376db | -11.89546 | -43.82117 | 2026-09-17 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d77f65b-f2a6-30d3-8f2a-0273396d7f5f | -12.42192 | -48.48333 | 2026-09-17 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dadf6ab1-730a-3832-a01a-caef195eecf9 | -9.10477 | -45.72221 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 170a948b-66a4-3e55-aa60-93c35c4de4c6 | -7.65249 | -45.84332 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea94e469-b928-3ff6-8b31-e23d735adad9 | -10.77023 | -46.20621 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60643e70-a42b-386a-8d70-95676b827d5f | -7.08484 | -42.0935 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b3bc450c-a4ee-390c-8416-a479c6b9ec75 | -6.66186 | -43.64414 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c70d24bd-8085-362b-be8e-6bc4a405d830 | -7.3834 | -44.51055 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8de111b9-0573-326e-bdf6-907c776cd8cf | -9.88527 | -48.38414 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e672784-f60c-3413-9c64-870c787f4116 | -7.10188 | -43.11481 | 2026-09-17 03:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d2be186f-5c78-3d3b-8f9c-6182cedd7672 | -9.49373 | -45.43679 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4642aa0b-0230-38c5-bee9-dbfb38653ae4 | -12.47093 | -50.93531 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1be22bb1-483c-3666-8f74-428095e30bce | -12.78591 | -47.56494 | 2026-09-17 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a126ab91-cf2f-3dc0-8f61-b73e6e2eb1f0 | -7.60438 | -46.32343 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 570df67c-b22b-3b8e-b7e9-3bc94c62bbe8 | -11.8851 | -47.60831 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf0a257f-8b1a-3f85-8391-cc7a9ec1decd | -9.45656 | -45.45672 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README25.md)
