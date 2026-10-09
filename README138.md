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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49978019-8d2b-389b-ba60-e0abbb37158f | -6.44736 | -55.04382 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ca23ab0-b764-315b-8903-e812d7b8e8bd | -6.53903 | -56.04713 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3ecd105-9e51-30b8-851c-9efb8f06fa34 | -3.57037 | -54.67189 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d969123d-8f1c-311e-8b87-e0660aca2b0b | -7.44272 | -63.55583 | 2026-10-09 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4df009d2-8a3a-3c32-aca6-eb377b35d328 | -5.71305 | -53.48417 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0f2cd938-dc77-3f1b-87d3-dff94c422837 | -11.00731 | -45.4218 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae6025de-2553-3dd1-8274-4ff05b567dc8 | -9.89675 | -44.78955 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03d009e8-6534-3f30-bb6d-be1c80f056cf | -3.05783 | -54.23053 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a237ad05-bc0e-3499-9377-b543fe7f3508 | -3.02283 | -54.04679 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5150a00b-9253-3da2-99eb-9f493d79822f | -3.31753 | -54.04903 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 632f5c1d-4b5a-3f89-acb8-8ccf9364b2ed | -3.01273 | -54.06482 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f70bab48-9f4f-39b3-8e0d-ffba44b744d9 | -3.9835 | -59.34485 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9eb7701-72a0-3876-9a9f-f2b584cba0c1 | -4.82163 | -45.83803 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 83af4419-611e-3640-8b6e-66d191e00f9b | -6.0639 | -53.60256 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97d838c0-dc88-392e-8d91-8a1572b88b9d | -3.74307 | -59.46993 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f471e330-c223-3d0e-b2be-6a70f2494293 | -4.05709 | -55.3255 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 267c040f-3741-3564-8360-cc5b2671aacc | -5.95156 | -55.35638 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c64b3aba-d782-390b-a6e6-29ef63d7d001 | -3.31844 | -61.26776 | 2026-10-09 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cbe077e-0221-3e63-b573-3f88f08650ba | -3.01884 | -54.09338 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc5becf3-ff15-31a4-ac09-e7c8dbf78c44 | -3.08289 | -53.96243 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e910cb44-442b-3223-abbb-55e1645852fa | -7.90205 | -54.71696 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a739199-a0f8-30ae-9fd2-40fe2f2df094 | -3.73587 | -59.44896 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc480782-31dd-3a50-8185-6a73b22e8db8 | -6.47014 | -55.47032 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50d3d54d-9290-34c5-8a4d-65f25201514b | -3.10226 | -53.93046 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e848874-180a-3b36-96d8-67b3efcc185e | -5.23587 | -45.4151 | 2026-10-09 05:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08e2c2ad-a195-3c48-a3ea-1f2630177006 | -6.1686 | -44.86265 | 2026-10-09 05:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3393507-8003-388f-8c0a-cdc6a97bf8e7 | -11.66086 | -43.68135 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1f8bcab-1393-3058-9dcb-20803dea9523 | -3.98248 | -59.35317 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7fecc600-9cb5-380c-b9bf-034d7088a4d1 | -5.70586 | -53.45794 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26af885d-cb9c-36d8-bba4-5e5c2ffab143 | -2.7317 | -57.46634 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 221bb13a-d2d6-3a73-9f1a-97242e247688 | -6.26036 | -52.87988 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b31d0663-6960-3d47-a88a-5a9e1113d11c | -2.97383 | -54.03594 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da98eca7-db19-39b9-877b-b5479f2878b3 | -5.70812 | -53.45064 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 120916e2-7dcd-3e2b-94f9-5be306e49a10 | -3.0096 | -54.08402 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db72757b-703c-3d7b-ac8f-7ab01b1d5721 | -9.89402 | -44.79187 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 641bae0e-6c3e-3b2f-874f-a8351d0b3e8e | -3.01247 | -54.08842 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b19398b-e809-3c2a-8a0f-2eeddcde73ef | -6.18437 | -52.8716 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8df55b72-b086-3aff-86fa-3f6d096893ef | -2.94067 | -54.15314 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3444201b-f98c-3cfa-9c4c-77fca8e81b23 | -3.65726 | -59.16098 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73f0a549-3b8b-3def-a542-73c42cc1f486 | -11.29734 | -46.6818 | 2026-10-09 05:04:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe332d1c-ad24-33ea-b08d-3652b0f332fe | -3.1211 | -53.79056 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93754401-bca6-350f-a930-2153fe54086e | -11.09243 | -44.0407 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a032d96f-c5a6-3fb7-92d0-c960d463a278 | -5.88101 | -53.52182 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7ac99bd6-2a9c-30cd-8aa7-636500656653 | -9.69561 | -58.09332 | 2026-10-09 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fbf0815-7971-3171-b4e7-f8712a656afe | -3.07716 | -53.95372 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db67e0bd-f848-34f3-ae49-24836c03517d | -11.40197 | -47.58599 | 2026-10-09 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af74cd3b-1282-3d27-af1e-e8891136c789 | -8.32765 | -45.01737 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c6270bb-fb5f-3ff3-8959-a2bcb1d09d42 | -3.5362 | -55.43532 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 433b582a-0f4a-3df7-9a26-ef990402dead | -2.99622 | -53.91832 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 391e7bf1-bd6a-3d5f-9b21-8f7b2db5e8fc | -4.90202 | -48.77081 | 2026-10-09 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b04b9e8-e518-3d36-8ce2-c1b3f4162fbe | -3.26493 | -54.02109 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 445b1cf3-3d5d-3b7e-8910-9567aeb243a0 | -3.28067 | -54.07843 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 591f30ce-4aa9-3127-b55c-67af33499858 | -5.92585 | -51.83663 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c683176-d75e-384d-bf90-057b73a5b057 | -6.23872 | -52.84431 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0289d206-6559-3d72-b618-8173e84268f7 | -2.81668 | -58.29258 | 2026-10-09 05:04:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ce3e64de-e6b0-3f6b-bba9-699e1ef92404 | -3.04096 | -54.15627 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a73eb8f-d19c-32ef-8a1d-39f9fa7141eb | -8.22507 | -46.413 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d30132a0-9e57-3aa4-b7bd-9a08b4cba20c | -5.71135 | -53.49471 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04b7c3db-f6ef-3413-ab2e-c32d18604428 | -4.92455 | -55.85612 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5977c824-f997-3fe1-b9a6-928fbcc8a889 | -3.0741 | -53.97273 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfe778f0-86a1-3bbc-9eda-d707c58a43c8 | -3.72643 | -57.14454 | 2026-10-09 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0894025c-7f2d-34b0-b2c6-d870468d4b1b | -3.07899 | -53.94236 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7313b2cb-0914-363b-b1ad-56879f2f2062 | -8.32517 | -45.45403 | 2026-10-09 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 149e954a-ef6f-36d2-9792-30d5a9c067a3 | -3.46446 | -59.26073 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90aa69e0-2867-32df-a505-96657342bc5f | -2.9755 | -54.11513 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7092b3c-da55-3f5f-8729-7c9555031081 | -3.08575 | -53.96679 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aad75b99-653f-3eb9-b7b4-5a2c8f569631 | -3.00609 | -54.23829 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7bb2ff7-1ca4-3170-b8e4-300957d173ca | -3.0075 | -54.04915 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9f88c51-bc73-3dd3-a73e-9f323ab50489 | -6.10345 | -53.50662 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bc93e86-7195-3bdf-9f93-42f755aed02a | -4.09397 | -48.95856 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70ed4118-2591-3018-b5e6-6238f9d6db79 | -6.17494 | -52.86652 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f425e556-6f8e-3e7b-b085-f79f98a5d500 | -6.04074 | -53.48935 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bfe8f7f-3c99-36dc-addc-d1c42b639b35 | -4.93128 | -55.8618 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88691ffe-35df-3148-9d2c-4541a09c2ec3 | -8.71971 | -45.16285 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da15fc47-2241-3e03-9161-d4217ee47b9e | -3.57488 | -54.68903 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| dc72e315-afbf-3f36-adbd-234b8f6ed436 | -3.00035 | -54.07164 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3962fa05-7ec8-34cf-aa65-32237db1b897 | -3.193 | -53.95211 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 787401de-ec34-3914-b3ff-803b72e61bd6 | -11.41554 | -47.58368 | 2026-10-09 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84dc01bf-b407-3a1f-befc-5561a422f22a | -4.63686 | -50.95756 | 2026-10-09 05:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1be4664d-7e85-31c8-b887-54f1a386473b | -3.59964 | -54.58219 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eb743cdd-c6ae-379c-9e30-4347469b6005 | -6.49632 | -43.9517 | 2026-10-09 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a39c72bd-ecaa-3cb4-8afa-58a588560ec0 | -3.09922 | -53.94946 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a61440eb-2683-32f2-84ab-5096ca971ad8 | -6.41483 | -55.19674 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ebab571-acc9-3a3a-985f-5e55cc979c50 | -3.55572 | -54.69419 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 69121c03-b2d8-3792-8aa1-7c02a7f656c2 | -3.00438 | -53.91182 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b043a6f-5eb2-315e-b968-a3abac437e8d | -8.90553 | -45.21973 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| caaaa52b-bbea-3124-b459-d4b74cd65a9a | -3.04509 | -54.15294 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50748196-7115-3104-bad3-6653b0b90d44 | -5.96458 | -55.36681 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b51228c-0978-358f-b946-cb2c3df4d605 | -4.30831 | -54.79558 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cc4d79c-235f-346c-b76b-d227fdc307f6 | -6.4531 | -55.05288 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58dd7eb6-c5f5-3eda-a7c0-9c948ddd5ef8 | -3.01346 | -54.10439 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc3da17d-2ab0-317d-ae49-44ae2d2809d6 | -6.0181 | -40.96872 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f6e0008f-d2d7-3fe0-94af-722c7a074250 | -6.18493 | -52.86811 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0c88c5d-8f76-31cf-adf1-7c5c1db9c556 | -4.74652 | -55.66904 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fd3e87bd-48c4-3f8c-9edb-0bd2cc372d15 | -5.89364 | -57.7217 | 2026-10-09 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06009fb1-a31a-390a-b97d-dbe3c7ad83c5 | -3.28765 | -54.07954 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f26943f-8a37-3621-a331-c83a4a9a377b | -3.73498 | -59.45412 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7eb925df-9387-3342-b7dd-48acd18446f8 | -6.85911 | -48.7758 | 2026-10-09 05:04:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3e7829f-e07a-3788-8830-6e3269a7e6d2 | -2.89192 | -54.16528 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d786c9d-396b-34a2-aada-c522c27d1904 | -8.75322 | -62.6259 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README139.md)
