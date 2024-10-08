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
| f40b96db-77aa-3e47-abbe-f2be3c76b7f7 | -10.20093 | -61.96094 | 2024-10-08 04:34:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8c693c6-c7ea-33ef-a751-ef9b3f56a401 | -9.74579 | -62.33831 | 2024-10-08 04:34:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e4325459-219e-32ca-96e3-552dccbaf2b0 | -9.74378 | -62.34196 | 2024-10-08 04:34:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 64e1acbd-93a3-3b91-9b86-9e7351cd9065 | -14.9044 | -49.59024 | 2024-10-08 04:36:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3f2060ff-5cae-3569-a16c-3059d7565453 | -14.78303 | -42.8412 | 2024-10-08 04:36:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d037a78-4747-3d80-af9b-eb4a8c80a163 | -16.92187 | -57.68777 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5bfc2ff9-7f8b-3a8c-ae06-f7dbb8d7f3be | -16.69619 | -57.45824 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 13a56535-e990-3aef-843c-3d82e99c9ef5 | -16.6945 | -57.44285 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3cb6c4f0-a5c0-3b2d-b0fa-2c0ef46019c9 | -16.69165 | -57.45731 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0b27a529-2ea8-3bdd-a246-334ec77be293 | -16.67869 | -57.10799 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| efd15e57-0b08-3773-88cb-d9d1ef699bd4 | -16.15034 | -49.31426 | 2024-10-08 04:36:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6965e792-7cdd-36c3-addd-78bba744ecb7 | -16.10939 | -50.23635 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 89818f8f-8f46-39fe-ae56-24f762734761 | -13.5339 | -49.47736 | 2024-10-08 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| dcc3a99f-cabb-3b86-acd2-3f9e3554ab8c | -13.53335 | -49.48088 | 2024-10-08 04:36:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8c4f1c13-bfa7-302d-b7b4-c59f66bddf6d | -15.07876 | -48.94474 | 2024-10-08 04:36:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84fbfde6-0b01-35e8-9c1a-43b051987183 | -14.90495 | -49.58669 | 2024-10-08 04:36:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e71d1918-2e9f-3444-bf7a-55e7f52f91e6 | -14.90165 | -49.58615 | 2024-10-08 04:36:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b804c51c-e1bf-3f8a-85d0-05b8486f97c2 | -14.9011 | -49.58969 | 2024-10-08 04:36:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0767293-fa23-3f99-b1cf-386b182e17a4 | -14.78678 | -48.96369 | 2024-10-08 04:36:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3284d5cc-83d5-3114-af03-b77097312b6c | -14.49825 | -49.26859 | 2024-10-08 04:36:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb1112b6-d326-3d60-a0e8-32b88dd5da82 | -14.15396 | -49.68826 | 2024-10-08 04:36:00 | NOAA-21 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd5b0124-f322-3369-a4ef-72658076c0a9 | -14.15341 | -49.6918 | 2024-10-08 04:36:00 | NOAA-21 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7d69548-61c9-3a9d-94ee-3c625f6e4b14 | -15.07949 | -51.23991 | 2024-10-08 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 600c4aaf-6d20-34ed-8a77-4ac39bc9dff8 | -15.07674 | -51.23565 | 2024-10-08 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf54c9ad-bbda-3f94-a6ce-d3a63ab59a30 | -15.07613 | -51.23933 | 2024-10-08 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1723eb93-adce-3918-a6b5-839594e4925b | -15.07399 | -51.2314 | 2024-10-08 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9214fd8c-aec1-3ce1-b3d1-44332da6635f | -15.07217 | -51.24244 | 2024-10-08 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64e57ced-0442-3d17-af52-6f590614d7df | -15.07123 | -51.22714 | 2024-10-08 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a26090db-305a-3b38-8e1c-fd571cbc20a9 | -15.0618 | -51.22972 | 2024-10-08 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07d59be0-2a91-33db-a76b-f2569ebd1442 | -15.04635 | -51.26117 | 2024-10-08 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d49ee9ae-02d5-3e39-86b1-520068f5b389 | -15.04575 | -51.26485 | 2024-10-08 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3ac6171-3d50-377b-8d77-901c2e966bbc | -15.04405 | -51.21155 | 2024-10-08 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cef14095-8462-30dc-8b3d-045997f86e7f | -15.04299 | -51.26058 | 2024-10-08 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16186d08-45d4-3d7c-a552-6a924bc1538e | -15.04023 | -51.25632 | 2024-10-08 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| beca1abf-5d5c-3a21-9c7b-20c9cb4a8b44 | -14.84081 | -51.07868 | 2024-10-08 04:36:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a082908e-ef5c-3225-adc4-87a23d1212fc | -14.83746 | -51.07811 | 2024-10-08 04:36:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 478081cf-a571-30c2-a6c3-d5a7339a4c32 | -14.81044 | -50.80458 | 2024-10-08 04:36:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 98ccc7d4-c4f4-3262-8309-bb178d1ebd20 | -14.7951 | -50.77228 | 2024-10-08 04:36:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e21c2f34-6bfb-3e61-8a79-16a2637b7a11 | -18.55397 | -52.66357 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eda9fc25-8d01-309f-b7f4-f990ad0e4aad | -18.55332 | -52.66744 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20464cf6-9642-3bd6-83a7-31ed71ec1ef3 | -18.55253 | -52.65131 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bec5db9-212c-309e-927c-8de57e824642 | -18.5524 | -52.63134 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f3b76aea-0980-3603-9c95-71c6caea0207 | -18.55175 | -52.63521 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bcadc9c7-00f4-3606-816e-2bd15a8e674c | -18.55109 | -52.63907 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b386fc8c-97f6-3035-b1ca-f30fbdb640b4 | -18.55044 | -52.64294 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de1ba35c-3589-3feb-8a0d-a87ac2333827 | -18.54978 | -52.64682 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1523804-ce93-366e-9bbb-fc778b772137 | -18.54899 | -52.63073 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2472fab-eeef-37ff-ae04-60ea6fd05362 | -18.54834 | -52.63459 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2b69878f-10ec-3bad-aaae-c2d7ae912a7d | -18.49202 | -53.44772 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f143e578-f0ce-36ad-a997-8a1bee7f071e | -18.49062 | -53.45592 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fb39f47b-8f62-3f74-9da0-e498bb15e9a8 | -18.48991 | -53.43885 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f08dcbe0-dd7b-3106-a3d6-e7f70d71623f | -18.48921 | -53.44295 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bc016e5b-c98c-36cb-ab54-ba187534648c | -18.48851 | -53.44705 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 22272460-0a7c-35dc-95c3-b9fa112d2cb4 | -18.48843 | -53.49002 | 2024-10-08 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6fb4ef14-ab55-32af-9576-feb57ae280b0 | -17.79092 | -53.05779 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf7bf7d6-cf56-35a8-b9c8-d63833999761 | -17.78618 | -53.10704 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74f6bd0d-188c-317d-ac2c-fd5d8b636eaf | -17.77767 | -53.05132 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 77c23dd6-6a6e-32ba-9040-6f8de7f331fa | -18.0854 | -54.31802 | 2024-10-08 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff4fe4ae-7fb9-3e09-8821-19c3e8abdb2c | -18.08906 | -54.31878 | 2024-10-08 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a375d96-c696-3849-8bf2-091aced29ff1 | -18.08339 | -54.30793 | 2024-10-08 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b2e8dfe-8f74-3a70-bba4-3650914f4269 | -18.20136 | -54.45202 | 2024-10-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7fad6a97-7af4-31a0-8fd6-f86997140cc3 | -18.21615 | -54.45477 | 2024-10-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 959ff874-78af-31ad-b610-8725cb7017f4 | -18.21325 | -54.44953 | 2024-10-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a0c9bb90-6e6f-309b-a90e-58c208a84174 | -18.20875 | -54.4534 | 2024-10-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 324e317f-eb22-3d17-b23e-ecbc3402059a | -19.45536 | -44.11487 | 2024-10-08 04:36:00 | NOAA-21 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee9393c6-5ad1-3fc0-bcfc-f2dbf99b5515 | -19.45039 | -44.11884 | 2024-10-08 04:36:00 | NOAA-21 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5779d4aa-71b0-3aa6-9c0b-8c4483eaeca2 | -19.44985 | -44.12355 | 2024-10-08 04:36:00 | NOAA-21 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12eaaeb3-79b2-3ee3-8fa3-60e061a8fa6e | -19.25541 | -44.36828 | 2024-10-08 04:36:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aea3d3c-a6cc-33d8-8e5e-8e9a3318b430 | -19.25158 | -44.3634 | 2024-10-08 04:36:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1806be8b-6083-3c32-8cee-656a2854e148 | -19.82699 | -43.7998 | 2024-10-08 04:36:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78451f1f-39c2-33fb-83c4-86e1adb01b21 | -19.82564 | -43.85192 | 2024-10-08 04:36:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 513eadd4-b7ce-3216-bda5-ef1fa943da6b | -19.82247 | -43.79879 | 2024-10-08 04:36:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2db75590-1b85-3801-9d66-15d3d0c45d89 | -20.35025 | -41.8597 | 2024-10-08 04:36:00 | NOAA-21 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a4d114a3-8f62-36d0-8d68-78746794c77a | -16.67603 | -57.12178 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| b1220d3b-252b-397f-8db8-8d3c5956a9b0 | -16.67514 | -57.12638 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 1d1c8ce8-e69f-3703-80cf-3c8d4e18ae00 | -16.69658 | -57.4545 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a9977a15-5114-3c8c-b584-123e4dca7efd | -16.6926 | -57.45248 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 59318ad6-39af-342c-9837-5067b7fac44f | -16.69204 | -57.45355 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 30d42504-e4a9-382c-900d-73601e40fdba | -18.20794 | -54.45799 | 2024-10-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3aae91bb-0413-3c88-bef9-a0929c72e70a | -18.20505 | -54.45272 | 2024-10-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 922c7f80-3c09-3d8c-80a5-1ebedb264201 | -18.20424 | -54.45732 | 2024-10-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06436069-839d-3497-998d-3dc90474e4dc | -18.20055 | -54.45662 | 2024-10-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08001362-45f8-394e-8d2d-9cd110ebe7be | -20.31162 | -41.81836 | 2024-10-08 04:36:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6ad9bfce-8657-38fb-98ef-745e73928b9a | -20.31127 | -41.82176 | 2024-10-08 04:36:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0a80a155-af4d-32d3-b768-f351c75c2aa4 | -18.63414 | -42.77317 | 2024-10-08 04:36:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 25c9a940-d38a-3bbb-9d9e-01485c4c8bfc | -18.63381 | -42.7747 | 2024-10-08 04:36:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 23915e74-8674-3481-a74f-3bb55e2b9af4 | -18.5653 | -42.40467 | 2024-10-08 04:36:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76211696-8f3b-35e3-a896-288f50834f25 | -18.56464 | -42.41039 | 2024-10-08 04:36:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8180acb9-3708-3965-a9da-a76eb7fc835c | -18.56235 | -42.40448 | 2024-10-08 04:36:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| ee0f128e-d043-3257-b504-c0a0a0e6ed87 | -18.56173 | -42.41026 | 2024-10-08 04:36:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 262c61f2-eb63-3a6f-8a0a-17a975bb7539 | -18.5604 | -42.40398 | 2024-10-08 04:36:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b09dab4d-35c8-3b78-9285-ae9476d0588a | -18.55972 | -42.40981 | 2024-10-08 04:36:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fa5a2c93-a7e9-38e8-9388-e72644279ed9 | -20.29469 | -43.5332 | 2024-10-08 04:36:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1e980fe3-01bd-36bb-9beb-ba59e6df7479 | -19.97976 | -42.4534 | 2024-10-08 04:36:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cbb30256-3e89-323a-91f3-dc6fa7bd8ae3 | -19.84998 | -42.38306 | 2024-10-08 04:36:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 85ef6ae4-2b15-3948-a523-7f58019ceb06 | -19.84443 | -42.38762 | 2024-10-08 04:36:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| fe27f7b0-d25b-331c-9fad-2f2f5d51bdc9 | -19.84422 | -42.38921 | 2024-10-08 04:36:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 07e4b471-7c49-3298-ad7a-483a2f4a5d77 | -19.84414 | -42.39033 | 2024-10-08 04:36:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 9dffac65-4f7e-315f-8483-b24bdb8a3321 | -19.83925 | -42.38825 | 2024-10-08 04:36:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 59bd300c-b012-3591-8944-e4a342151280 | -19.83015 | -42.37877 | 2024-10-08 04:36:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README61.md)
