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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30c1c704-e061-33af-a801-ff37c73635f7 | -8.58862 | -54.76793 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 31da664d-3d1a-3423-ae9c-d4870934e3c7 | -11.25948 | -50.57699 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f5b86bc-d595-36bb-82ac-57a838d31b8e | -7.55093 | -60.47672 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d165c3b8-d489-3df5-8044-4f0218a4efe5 | -6.5999 | -58.60673 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab9cf02a-6afe-376f-9053-5598bb0e1be9 | -11.66769 | -47.60922 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c004b0dd-fbcb-3628-910c-b1de7016e441 | -5.8956 | -52.25761 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36ff0570-8b64-35d6-9b3f-c1a2e2155f1b | -8.64199 | -47.30703 | 2026-09-01 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a584b975-b95f-3fef-a607-d95776894f65 | -7.94593 | -52.45708 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a46f02ef-5778-353b-9763-394f9cfa4c33 | -8.23502 | -54.93538 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c04e4de-3790-31ee-850d-b00f655deb1c | -6.91265 | -59.48233 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d36fc7ba-ee34-30aa-a62c-a821e44c76e6 | -10.32887 | -50.00088 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ca1c427-c61f-33e3-8302-f546f94df7ee | -8.69411 | -54.69044 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 847a0d4c-6915-30ec-8a39-12f3b3399a9b | -5.58356 | -42.31486 | 2026-09-01 04:40:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 95fc8dbf-f855-3b9b-851f-134063a0bf36 | -11.3025 | -50.58385 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5c63792-b3a3-3184-844d-01b1f81727e5 | -5.48896 | -57.14736 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f49e6f8-4f3d-3bbe-8e8f-2a728b5c4611 | -7.90065 | -44.24704 | 2026-09-01 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9f8b6c59-2232-330b-8271-d12d4d99a476 | -7.53154 | -61.37574 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c7865d3-3b71-3b2a-b76d-59fbcd7aaaf6 | -8.27446 | -54.93233 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| b7531269-0790-3e14-b46a-37439c7acc4f | -10.74542 | -54.0407 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d40714ce-ed54-3c00-8de8-619228c1a84b | -8.91347 | -45.04487 | 2026-09-01 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2cf82a9-df11-3a48-9412-8367909008fb | -6.14851 | -57.91113 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 951520b9-cd4a-3f26-b150-ec94bfb774d7 | -7.28934 | -49.8255 | 2026-09-01 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 181fa9ea-1bdb-3c8a-9998-86441dcbcead | -10.32984 | -49.95074 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2db6c7d-a88e-31dd-84c8-4d37450a974b | -11.91067 | -45.05511 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9472689c-a4f3-31e8-83f2-2b7c0097c978 | -11.20871 | -45.11222 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afe7d971-01c0-366c-bb87-0c1cb016a1c0 | -9.15787 | -59.54008 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 754cb588-7346-35d8-9222-f133586ff95c | -7.52802 | -55.33472 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b27450e-eac4-3ed7-96ba-9aa9e98206b6 | -8.61253 | -54.81601 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 983dd21f-0afd-30fe-ae44-119bb0ce857f | -11.17435 | -55.09087 | 2026-09-01 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bca752c7-df20-3cb0-b741-fae75967b2c0 | -8.59171 | -54.77367 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08051f5b-cf76-3520-bb20-d1c39990661c | -8.85858 | -48.82144 | 2026-09-01 04:40:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8dbd0a3-0b6b-3823-97c1-76438e1d32b7 | -5.24566 | -55.90549 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3395e05-6e82-32b2-a5fe-052e1df9f90d | -8.1434 | -54.96697 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb4f820a-2540-335b-9fa7-6b49162f6754 | -8.50492 | -55.29832 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0661ec4c-e637-3d44-821b-660a173e9f88 | -7.92807 | -44.2354 | 2026-09-01 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2570ca21-8a76-34d6-aaeb-5ce89ef5a05c | -11.37686 | -45.1825 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1b7898f-99e7-3c69-a799-fccbb26556cd | -6.21037 | -42.51845 | 2026-09-01 04:40:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5d56e471-a43c-3ec9-88f6-7941f6e2bd6a | -6.27582 | -53.33529 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 477f43f4-dfaf-3cf6-925a-8159f6c03f64 | -11.29977 | -50.60136 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3a736420-bc83-3f5e-9401-57888d7782b8 | -7.30058 | -60.56913 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c3333a7-c876-3918-afcd-0fd23b6a9e44 | -10.02777 | -44.68881 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ef63fc0a-116f-3ecb-a26e-01e7befb7f3c | -3.79179 | -59.3497 | 2026-09-01 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bc9cc06-0657-33d8-9244-d67ac562ff65 | -5.76807 | -51.67552 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d92ff846-d1d9-3483-a48e-1b8aa7332ea9 | -9.15665 | -59.5469 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2786471-2c62-34ac-9bf6-ea0aed4ce068 | -6.62382 | -53.17894 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dec06e4-b55c-3aeb-b042-486ee54344b3 | -10.8711 | -45.36462 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 64926e01-48fc-36ac-a94b-af95f48fb481 | -6.12146 | -57.67826 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5ee56c27-ce3f-3096-9100-b55fc546d257 | -4.965 | -55.84788 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0138d6cb-1f2d-33da-b367-c6d6f1cbc190 | -6.26577 | -55.42047 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1446443e-a17f-3aa7-a783-ee79a37259ec | -11.258 | -45.12376 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85877572-aa8d-3c67-b1ed-52f22bf904d9 | -11.72296 | -47.64601 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6bb74c4-e7b2-36c9-b25a-4b36e20c597d | -10.15733 | -45.74447 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 785b8b43-f67f-3dfa-8eef-84fe154e919b | -8.76938 | -46.44406 | 2026-09-01 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b78c7bac-ea0a-3743-b69a-3d097f4c2388 | -7.55168 | -60.47255 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4a635ba-824c-3844-a667-b8cec223edb6 | -10.32598 | -49.95373 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee85a8ab-1f96-334f-9f53-453b318e6c24 | -7.05555 | -52.71363 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 023af266-b672-3362-8281-8cbf1b46c409 | -5.25238 | -55.90939 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 240a5f8d-4718-3dda-af7b-2bdf7aabf1a6 | -7.02782 | -55.64356 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4e66cf9-8752-321b-9312-4113245f1e54 | -8.50204 | -55.3158 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1ef7247-5d0d-3968-90df-93fec49c22ef | -11.92325 | -45.0924 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8644bdfd-9b4a-3b42-b19f-ca81de4a59ed | -4.1494 | -60.70052 | 2026-09-01 04:40:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b516e627-d0a5-34df-9747-030f7e21a183 | -7.6243 | -55.29297 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b09467d7-1938-3105-a962-8055d24bcd3b | -8.80257 | -62.4913 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8afd284-1085-377c-8eaf-88ebaa56264f | -7.62843 | -55.29364 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed3e6e7c-e18c-344e-a5e3-87469c98e534 | -7.63184 | -55.29 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94cd7243-d2bd-3a8c-8bbd-47e9f094dfcc | -6.81536 | -43.53036 | 2026-09-01 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5c585a48-5760-3f78-8ffe-735ddca5179f | -10.20514 | -50.36094 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf01d9bf-6d58-3d49-a224-3e5b38cd9447 | -6.80579 | -59.0923 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 68c42637-db49-3228-8662-6972fd82d6c7 | -4.96872 | -55.85307 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24db562c-e45a-3e7d-a23b-59020c272c34 | -6.61151 | -58.60204 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 188417ef-d0e5-3655-a8bf-ba12c5ea624f | -7.02356 | -55.64285 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74696079-179b-38fe-9317-73c51e2b7ead | -8.41668 | -44.99969 | 2026-09-01 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 624c0112-48d8-3d37-bb21-574503364cc2 | -9.15551 | -59.54032 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb5523c9-64be-33d5-8fe2-31e4a8b5009b | -7.35645 | -60.5868 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 79eed377-5e6a-37ea-b798-2745cb9a8657 | -8.27097 | -54.92868 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 6ea8debe-0306-3c4c-ae61-c82c6630ab54 | -6.94124 | -55.63716 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82cc2f36-9678-36c1-a857-e03784226edd | -10.33207 | -49.95828 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71829ab9-b641-3c77-a186-e0cf1c509aa6 | -5.54217 | -46.59837 | 2026-09-01 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfa56b34-b6ec-32c2-b1e3-9c56c983e034 | -12.07139 | -44.98245 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d419437b-b8a8-3cfa-bde2-058d1bd74c9f | -7.08637 | -45.80856 | 2026-09-01 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 768abf32-bc1d-3487-abae-8645de0b1917 | -4.96651 | -55.83895 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 901a8af0-63d6-3dad-8df0-dd6bc8698a0f | -8.58877 | -54.76575 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5607ee1-33cd-3f53-b62f-af8e5cda0e46 | -7.1906 | -60.68336 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb6f552c-6de0-3fc3-87b2-a80cf89ec1cb | -9.4705 | -57.02506 | 2026-09-01 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6de8dd89-a230-3020-abd1-50d89b8fd12a | -9.40824 | -51.68263 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 239b5b43-98f7-3b52-bf75-4c85bd718a62 | -6.02838 | -57.68111 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18353ede-7129-3420-b7ed-17f828e4abb4 | -7.28549 | -49.82844 | 2026-09-01 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1516b6a3-f295-3ff7-aa7e-22bb32f2a4ca | -10.02356 | -44.6882 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baf07ac8-5df7-37fb-a01e-f078332ac885 | -10.33219 | -50.0014 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89c9cadf-20e0-34d1-8a0b-7030131a8c46 | -5.25682 | -55.91028 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bfff1cd1-dd36-3a86-832e-92ce479cf139 | -6.94551 | -55.63784 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8ae6848-8566-3f60-8368-6bde6fdbf37d | -7.68612 | -55.345 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae1b5606-44e5-3024-8267-22b57927938f | -5.84491 | -43.46004 | 2026-09-01 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a4c0cd4-7321-3806-9b56-26ad20bbcc03 | -7.34034 | -60.57529 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| be3a8a10-02bf-3d3d-a5aa-3214130abc96 | -10.11567 | -48.81243 | 2026-09-01 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6f7527a-a022-38e3-a30a-0b04896ca8e1 | -7.21779 | -42.74604 | 2026-09-01 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2c37cc4a-8cbf-375f-bb30-ff1258dba012 | -9.395 | -60.57809 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f905a844-026a-35c4-8599-f50dc0730325 | -10.15258 | -45.69248 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c10629c9-9c45-3e61-9c23-5ff7afab193a | -6.55899 | -58.56285 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee840966-9f86-337c-8b32-c662b078e734 | -5.60289 | -44.00193 | 2026-09-01 04:40:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README36.md)
