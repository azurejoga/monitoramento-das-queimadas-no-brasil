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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66626b7e-50fb-3d51-b199-8f8ce2051e4f | -14.25175 | -52.13616 | 2026-08-24 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc9162b1-4682-3cb3-bc5c-a9c1a4941f41 | -12.09836 | -50.61897 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c32bbc1-33d3-3a49-8e16-8f73712da670 | -13.17067 | -51.39786 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f203f39-3f6f-36b3-9ee2-b7841a3c0b83 | -11.69345 | -54.59151 | 2026-08-24 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 223769a4-0094-3e41-99fa-bec81e297216 | -12.11272 | -50.61407 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 343fd954-4488-3fbe-9c2e-e89a4cbb222a | -11.20488 | -55.08487 | 2026-08-24 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7e9b97d-5823-37eb-bf5a-ff87748b8b84 | -12.73695 | -48.38485 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fcaa530-a791-3113-ae35-fae1a5d88386 | -11.10945 | -49.88499 | 2026-08-24 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fe40920-253e-3cc9-b22a-794f4b8a3dbf | -7.48959 | -55.34138 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c39fa786-1ec7-3933-aff2-f36ff34aaffe | -9.94877 | -48.33413 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4008e3e8-35c7-3081-b8f1-e7d9a81f702b | -12.11991 | -50.61162 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10a51ee5-25e1-38ee-b0a3-be8e22cf7361 | -12.86066 | -48.47725 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d723ac2b-4083-39ae-b493-519ccf55ca27 | -20.54311 | -54.68071 | 2026-08-24 04:46:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c152ec2-de22-3b06-9a8a-76880bd40e12 | -6.60717 | -58.38163 | 2026-08-24 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e14ce6e-15fb-303e-836e-4eec75964e3f | -9.95166 | -48.33829 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 36319c1a-e240-3ca4-881e-62dfeb0619bc | -6.63266 | -58.48685 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4b70020-91e4-3662-8ae9-435c258af390 | -12.11162 | -50.59944 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1e92105-652d-39dc-af67-6979c853be9e | -8.80039 | -48.31639 | 2026-08-24 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38cacb4d-7a50-3d92-94d2-13e56b9a048f | -19.07833 | -47.13632 | 2026-08-24 04:46:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66062909-f3af-3f82-b400-a398a97196ab | -8.0856 | -50.04938 | 2026-08-24 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c4d47a0-4836-36ac-9225-71acc79c7629 | -13.6912 | -51.84084 | 2026-08-24 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 170c894d-6b90-3963-8142-c5eb03221850 | -10.73512 | -47.97689 | 2026-08-24 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7498a4fa-cd50-35fb-8dbe-675e09a8afe2 | -10.72639 | -47.96317 | 2026-08-24 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 095772c5-51a6-3eb1-b1ea-45f04e1a2512 | -6.8135 | -58.65112 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3df13daa-8c9c-3579-a7d8-7620da6b8515 | -6.38401 | -57.46636 | 2026-08-24 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 636ea544-42a0-38eb-b163-ae8532e761d4 | -8.53798 | -55.28626 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc430756-3114-3809-9c7f-22ae7a6428c3 | -10.62911 | -52.25135 | 2026-08-24 04:46:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f729b340-851a-395e-a239-5976c42ff780 | -13.1613 | -51.39268 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 33ede196-f947-36aa-9b9a-2fb8fe5ca70b | -12.86186 | -48.46906 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28853fad-f1db-3dee-b00a-4d2158921e7f | -6.63952 | -58.47845 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43dd182e-c7cf-3b03-8200-d19ebf18e55a | -12.86248 | -48.48933 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7244b082-d4a6-33ee-868c-9d802f6caffc | -6.54891 | -58.59126 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| fa3fbd45-acc7-30c3-8a54-e21e9ed3f00d | -8.92603 | -48.54384 | 2026-08-24 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85a2b733-f748-3cce-bd7f-b4285ccdddf1 | -12.11548 | -50.59653 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d092224b-cd37-3ca2-8b65-1892591b8f5c | -11.55686 | -46.96299 | 2026-08-24 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00e24990-26b8-32e8-9ac8-a1f69da65198 | -11.20385 | -55.0448 | 2026-08-24 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c55fd07-2e3f-3b74-8e52-50dfa49a7c1a | -8.8038 | -48.31691 | 2026-08-24 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c28fa23b-ac36-3b46-acec-459526b2141d | -13.17729 | -51.39896 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| faf51c57-14e0-3aaa-8af3-66d99dd1684d | -12.11604 | -50.61461 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20e576f3-47e3-353e-b007-bc3aed9eba55 | -6.61072 | -58.39171 | 2026-08-24 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b066783-2c3d-359a-8730-7b87ae57df42 | -14.01708 | -53.70594 | 2026-08-24 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1649ff4-0c2f-3b8b-ada5-e1a5ba14b1d2 | -14.40715 | -51.78138 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32949e80-51b7-3e01-82f1-910a8964c573 | -8.79071 | -48.31107 | 2026-08-24 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40911a3f-8c1f-303f-8706-d8c8ca0e244e | -8.337 | -47.70451 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f04da687-7e3c-37c1-b212-d60c9da4cf84 | -12.11106 | -50.62465 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ab8a1f9-3970-3cc4-98e1-92cd441fabae | -14.58474 | -53.03643 | 2026-08-24 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71fc19bf-ca97-37fc-810b-cf24e6cb2101 | -6.63179 | -58.48539 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc437ce9-0a63-37f3-8a7e-4520d5b39468 | -18.31711 | -47.20432 | 2026-08-24 04:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a387962b-1e8e-30de-872a-9fed87822b8e | -12.72034 | -48.39939 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41dceaa3-5c9f-3758-90ee-4e85a15a7ba4 | -6.55992 | -58.59001 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1868ac38-ee77-35ac-9fa9-c9663c56fc24 | -14.40052 | -51.78027 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a5234b3-a7da-3f89-9cdc-84b8dcb99748 | -14.44795 | -51.80284 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 383fd290-2781-308f-9be8-1c6e888768de | -8.54609 | -55.28757 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26016461-5680-3eb5-a24a-2ba442cb6619 | -11.57747 | -46.95261 | 2026-08-24 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d9d5fcf-6c78-332e-b2b0-bdcbe5d18109 | -8.58734 | -49.99061 | 2026-08-24 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b5fa205-e336-33c3-a02c-a18979000da0 | -9.95914 | -48.33548 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f7345e6-839b-35f8-8d31-59071d1a209e | -9.50725 | -60.50246 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 539c1425-46ca-34dc-836e-60ae307d9e52 | -12.10554 | -50.59492 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 585edcf3-c916-3682-a046-719604a93de0 | -12.11217 | -50.6176 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5381ed0-7d03-3925-9b20-2846a3c0a65d | -11.6868 | -54.58575 | 2026-08-24 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| caa27079-4eec-35c0-b29c-99ac41c9ddd8 | -7.22577 | -51.69015 | 2026-08-24 04:46:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41c9b621-7799-32d0-9c5e-d788c902a9af | -14.58137 | -53.03584 | 2026-08-24 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f3966fc-66e6-3d68-9ee4-d4227f7fc5b8 | -18.52771 | -47.17294 | 2026-08-24 04:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65a495a0-3dd1-3c82-ae67-2d3f50e2939f | -12.71913 | -48.40747 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2de9624e-6aff-3a75-ba5d-58b34ebae7a4 | -6.63841 | -58.48466 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75967f48-07b4-3baa-b888-8f8f7912ab7f | -15.04547 | -48.69114 | 2026-08-24 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b96716e9-c24c-3f08-b3d8-8eadfddec378 | -11.11612 | -49.88606 | 2026-08-24 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79ba8ba1-48f2-33d6-8132-998dec7bc3f0 | -8.15069 | -46.70732 | 2026-08-24 04:46:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02f23d3c-cea0-3096-b7a5-53be44a8234a | -10.79923 | -50.95198 | 2026-08-24 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55217c57-6131-3f8e-b2f9-6453d4571662 | -8.57189 | -49.98103 | 2026-08-24 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d71ed6f4-d4e4-3893-9aa2-69f65012a4a8 | -10.69172 | -47.73402 | 2026-08-24 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e39a09cf-c0b5-3900-bda5-140d5350830b | -9.50653 | -60.50634 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35dbf50f-7931-3083-b0dd-59776e4ec134 | -8.26718 | -49.30347 | 2026-08-24 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 090d8da4-15b3-3eaa-a76c-7572f45d0dd0 | -12.12211 | -50.59761 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 297cf710-de22-3185-9a40-c7e4220209aa | -14.30504 | -47.23138 | 2026-08-24 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4756123b-b639-338c-895d-5930fd7c7368 | -7.79143 | -56.28606 | 2026-08-24 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cea09152-0008-3955-a497-22509c3d2815 | -12.10002 | -50.6084 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 642591df-12c1-3a3d-905d-5ccc3b45f2ca | -10.54991 | -46.31677 | 2026-08-24 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6292df66-3b55-39ef-b7d6-1afa25a8dd30 | -8.54203 | -55.28691 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 128c11f6-0525-3b0d-ab6d-ede2dbdf7f63 | -13.10289 | -43.35001 | 2026-08-24 04:46:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0509aa2f-93dc-3454-99ef-8171160f473e | -11.86383 | -51.6874 | 2026-08-24 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 205f0915-97b7-3710-bef4-3e8ee43b32cb | -11.85167 | -51.67808 | 2026-08-24 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e58856a7-fb6b-3a9a-8742-a29d82bb9e7f | -6.80606 | -58.66293 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 54d3f7d5-2340-30b5-b150-43965e9730e8 | -13.44938 | -43.84095 | 2026-08-24 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e98dd5c-4104-37df-a531-87060e091c18 | -10.43084 | -50.46906 | 2026-08-24 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fac9b84-756d-3f63-b904-41ffc05a38b7 | -14.7881 | -48.7725 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 373a4344-7367-3c35-bf4e-e5ffce3bb5bb | -11.57683 | -46.95707 | 2026-08-24 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81a0ca63-9cd9-34e6-a437-4efbbe4f3949 | -11.00408 | -45.21861 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1337eb3e-88a7-36e8-9b94-c556fcf2f700 | -8.54326 | -55.27973 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9f46a57-9005-32c2-b0b8-77182d2157a7 | -12.10941 | -50.61354 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 8c662ffd-2923-3c0e-98c1-537fb8b412d4 | -8.57621 | -55.28189 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f1bf195-5777-32a3-ab82-2451c0fe3b4e | -19.89206 | -44.97119 | 2026-08-24 04:46:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4812cf0-c6b6-3723-8f7b-67b7c0f09705 | -13.1806 | -51.3995 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7c844139-3e11-326b-86c1-5271bd82d84c | -7.49022 | -55.33765 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d9cbd3b-ac40-3264-b802-060416b3575a | -9.46214 | -56.91566 | 2026-08-24 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d46b255-9365-3b88-a955-d888ba1a5ad0 | -8.31555 | -47.58615 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9deaa03c-a84b-3de5-8cb4-336e07970814 | -6.63896 | -58.48154 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca01cf05-0cb2-3397-a530-54c49ccc9e9c | -19.98114 | -50.38459 | 2026-08-24 04:46:00 | NOAA-20 | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ef4009bd-1e97-3841-9066-b16a954e99a1 | -8.58348 | -49.99356 | 2026-08-24 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 101eed17-78ca-318c-8104-0aa8f246b7e0 | -14.58873 | -53.03329 | 2026-08-24 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README33.md)
