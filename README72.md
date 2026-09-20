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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c35e2af-d15b-30ae-82cf-c261c31c404e | -8.44774 | -47.65615 | 2026-09-20 04:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3413b75a-c68f-3113-afeb-cf9dfecb754d | -13.94904 | -47.84821 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2161654d-f9ee-3e16-b900-b05cba72bcd0 | -10.5722 | -51.32281 | 2026-09-20 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5fa2720-08a7-3198-872b-bf8746260a9d | -9.13086 | -45.7126 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a638905a-c358-3eeb-9238-cf378b6623a5 | -9.26056 | -48.21235 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 616b18d3-5d78-3e93-a5bf-23bbc6266979 | -8.37799 | -47.19353 | 2026-09-20 04:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42e060ae-9044-389c-80ec-945bf1e76c10 | -7.35032 | -44.46465 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea0b71f3-74dd-30b4-94a9-a8709c7d8ab2 | -13.7367 | -48.78337 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d1e8618-9f77-3939-9220-bde4b5a79258 | -10.3913 | -48.98832 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18cfffd4-67fa-3a0e-ab8d-db068f001b8b | -9.57904 | -55.11013 | 2026-09-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6677aae-1a12-3425-9dde-f8ced6f016ae | -5.85067 | -53.54278 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4955329f-9e55-3f6f-802f-2f2e4659ec78 | -11.44527 | -45.39301 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 190edf44-6a0c-3b07-a3ae-80962bf704c3 | -13.0193 | -46.90504 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6de4008-248b-3ffa-ba6b-23ac23a922f2 | -8.38361 | -45.6367 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a338cb23-c865-341d-ae31-bbba27bfe6a2 | -11.03123 | -48.34916 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff1f7f25-d37b-3ecf-a74e-23c3ad235b86 | -9.79274 | -48.32557 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad5449d6-2418-3da7-81fe-1085400c985b | -8.05954 | -46.26636 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4ffa66a-aa36-31cc-93f4-87548b992b61 | -9.26997 | -48.23896 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2a42164-5be6-3afc-812d-aa86d99c691f | -9.79164 | -45.05643 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a652098-d7d4-33db-aa48-d20c4821bcc9 | -7.04986 | -47.49803 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0627996-00f9-3150-8912-9c813ca074ec | -5.98483 | -52.20316 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20db74a1-4035-38ac-a532-6a49ec41462b | -11.08606 | -48.30369 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab709039-e38e-34ce-b69f-af66678ede64 | -10.9996 | -48.31537 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6aa2aed-92d5-38a5-af62-3356a1d09659 | -11.48569 | -47.75784 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39134e21-e491-3afa-be8f-837b014cc635 | -8.18245 | -54.7488 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f28dd1aa-efb0-39f7-ad47-a837e32db211 | -7.15426 | -47.46035 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 108476e6-343d-3aab-a231-42817cec05bc | -7.91211 | -46.02211 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8231d97f-3621-3ab1-bf39-c2a60e9bc5c3 | -7.75777 | -44.88226 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d25a4417-75f9-3171-80d0-69f4c82d92e6 | -10.87727 | -54.09648 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 126a3bf6-9d3f-3f42-b040-3045195ac808 | -7.56263 | -45.37984 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47b91bb7-314f-32f0-8f41-42c2cf5e31d7 | -7.81957 | -45.09348 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62303ec0-7cee-3a2d-acf7-807deaf91367 | -10.87975 | -54.08236 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2df90dd-2255-3623-86e6-f1726998a512 | -12.12594 | -47.03735 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39510dc9-4fc5-384b-8b37-d380f256691f | -6.61463 | -50.06555 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 710ddaea-00d2-379f-a259-266ad9d5bfab | -6.36011 | -58.30935 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cb4532c-b683-30b9-8405-e1e272ba2e1f | -7.4289 | -44.73768 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce86ea0a-af28-3a2a-b434-04fb4d5ab703 | -8.77782 | -48.73157 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 607b0f17-9008-3243-9e27-e29bc4857daf | -6.45337 | -59.98356 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7dc5b3f-a7f9-32b1-a648-84e3062144b3 | -13.28162 | -51.32739 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d50dd8a-8feb-31a2-a4e5-8958604801ea | -9.04724 | -48.76743 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbc31722-5079-3c29-8e3a-f78af57c0c56 | -11.11053 | -54.03011 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f8b24f47-2ab7-3c68-abe8-1e830b901f19 | -12.35078 | -50.68839 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8df95212-bbd4-3360-9d5c-48eb58e57dbd | -9.7849 | -45.06674 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f327e493-13f0-33a2-b361-8771ac2a9750 | -11.02237 | -48.30072 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6696f63-80b5-3836-a235-843e3946d2fe | -8.4338 | -45.82839 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cf7c465-dea8-3c96-a7df-3117f99d92fd | -9.82642 | -49.14384 | 2026-09-20 04:40:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf8da288-455a-3d46-9f76-06b43fc276f0 | -10.55065 | -46.74706 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d313d07-8716-35c5-96c9-bf621fa90543 | -7.7687 | -44.05 | 2026-09-20 04:40:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d63416ce-a5b5-35df-b654-44b8a1a3552f | -11.86355 | -46.88013 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bbaa2f0-deca-3637-96b3-2b873eea71a7 | -9.58484 | -55.10259 | 2026-09-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6fce8f8-449a-3efb-80fe-7aaa348fc6a0 | -6.75532 | -47.92507 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebd4f80e-2035-39cd-85f4-1cff3f833eb4 | -13.01035 | -46.9659 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1a8a480-6508-3142-80da-d147671f4592 | -11.03346 | -48.31707 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19ae1f6a-fa9d-305d-8dcb-965bcf3257b6 | -5.84882 | -53.5034 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0eef9420-6397-306a-bd6c-33e003c2ccbf | -11.08773 | -48.29291 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e67c31f3-0ed8-345b-989e-c37efd7a85d7 | -8.63087 | -47.61611 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1a2bd11-fea9-368b-8ab8-b4464021f4a9 | -8.92436 | -49.99554 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e9ce3c6-6e02-375b-b70e-650b4dc875ae | -9.79229 | -45.05188 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4914ed37-e20f-33c9-b8e1-b63bba673f5d | -7.14949 | -47.42769 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3a8ebb1-5444-38ab-9504-8d2bd3fdc722 | -5.76324 | -57.45805 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d2f70b4-72f5-3f47-933c-c622bb118739 | -10.55354 | -46.75141 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d87988f-8b2c-3b99-8396-c097586de76e | -9.71025 | -45.98961 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69c5d7f8-8bb4-334c-8e41-8e47914a530e | -6.72528 | -55.08258 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c3554e7-3971-3f9f-84e4-9a661d1a589d | -9.94825 | -45.547 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5034a481-5876-3ae1-89ca-db062d322ae7 | -10.27495 | -49.99126 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e6461d6-f1e5-39aa-a22d-496810e4415e | -10.02824 | -52.12251 | 2026-09-20 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a39c650-7054-391e-adbe-a9d32e569b89 | -10.88314 | -54.08656 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6328481-f54b-38f0-add5-858c5ef5acc1 | -11.83567 | -46.85168 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4da813b-54db-3247-b036-4b65c181f6a2 | -12.75111 | -46.18192 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 0fc0d3e5-977b-3307-930b-ddbcc1b8b74f | -7.6002 | -55.71447 | 2026-09-20 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e796acf-f382-3f36-85ec-96ac9ca0c24c | -13.5815 | -51.46574 | 2026-09-20 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a58f909d-fabe-390b-82e1-0199c23fbc5e | -7.05714 | -47.53856 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8822b446-cc27-34a5-9551-c432cdb875c6 | -11.03455 | -48.34969 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b5aeb84-e515-3f51-b137-b0cba58282e2 | -9.54693 | -46.58796 | 2026-09-20 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ac1ae00-4ee8-37fa-82a6-f287ddb6f3d6 | -11.38932 | -51.41742 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d6b74ce-594f-35f4-8f46-2f906b1e182b | -12.75175 | -46.17759 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| b0415686-0f3d-3dcb-8c3e-c9774f0707db | -10.12608 | -45.55542 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| daddcd12-96fc-39f3-b93d-b590502ec41a | -7.16975 | -47.44845 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe24f273-7640-30a2-9508-19d9158ae4b2 | -9.45788 | -45.42932 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdd9aef5-fd80-39cd-a07a-f9aaa387bbcd | -11.87438 | -48.99391 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53300061-8509-33a7-b3f3-dec1edefc221 | -7.54223 | -48.68246 | 2026-09-20 04:40:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 389f291f-644c-3d52-b3be-f4c5157516ee | -10.59475 | -51.90189 | 2026-09-20 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd69bc6c-8013-3fa6-807b-15cd7874da77 | -9.3495 | -50.12008 | 2026-09-20 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9884122-91eb-3eaa-a6aa-d39d430f94ec | -8.77285 | -48.69868 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 156d0fae-c1f5-303a-b2cc-4603017939cd | -7.04248 | -45.23527 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cf63d0f-695a-3afa-a34d-64765d630302 | -10.29161 | -50.20765 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a427783-5e06-3f36-8a6b-dfe986cfa71b | -10.30152 | -50.24237 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 455b9ce3-8d91-3da7-a56e-3d2598b98f8c | -9.23679 | -46.23038 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba54251d-31d0-3555-8f17-a35ca3537067 | -11.0241 | -54.13761 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad008901-4b80-3fb6-a9a9-18e7d0cacc05 | -6.32562 | -59.93987 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf0efb64-7bba-3e35-95c9-42636632ddcd | -7.54866 | -45.42336 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21cd1c14-c252-3639-92c8-82bbc63f24ab | -8.62976 | -47.62318 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5670a462-96ce-3ba5-b5ea-1289a2eef8fa | -11.07997 | -48.32088 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a96b06fc-3e86-39f5-81d8-e06ed374cec8 | -11.27884 | -54.12309 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6af2e72-9819-3104-af2c-4e419dac81f0 | -9.41231 | -50.13787 | 2026-09-20 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e908e14c-31ad-3067-acd0-7418aa4c402b | -8.3707 | -47.19607 | 2026-09-20 04:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26c4af03-6e2f-3cfd-b719-ff00045b362d | -5.88538 | -53.6437 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4c6da5f-4e86-38b4-ac3d-909fa2e07ad8 | -11.02809 | -54.13839 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b144c954-c6c0-32f8-9b31-7b7a7a8aa98c | -7.55827 | -45.40828 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b85a1468-8318-3c9a-821e-a7f04c07037f | -8.30124 | -50.82159 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README73.md)
