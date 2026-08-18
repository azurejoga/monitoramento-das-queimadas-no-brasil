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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5e55c52-c71c-3173-93dd-82e70884d2bb | -8.59848 | -50.34749 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 07d04350-aceb-3a8f-81c1-2a5fe5e30120 | -4.60259 | -40.62404 | 2026-08-18 04:02:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 299af65a-b137-3a7d-aaa5-95836ba22468 | -8.74108 | -45.30495 | 2026-08-18 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed1294b1-c6fe-3dab-a797-5d9dcb939355 | -8.49218 | -48.82736 | 2026-08-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c1120725-da0a-3d77-9632-b582a6213a2d | -4.53479 | -42.93666 | 2026-08-18 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8528269c-4b27-3e04-a441-50c03c7820a1 | -6.1731 | -47.32894 | 2026-08-18 04:02:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 50e2e4fb-7d1b-3c29-8fb6-1cde5d8679ad | -10.85605 | -44.96766 | 2026-08-18 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ef6033e8-84ef-3d8e-8ad9-d664fca96143 | -8.36129 | -46.37181 | 2026-08-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49c0d32b-49af-3d9d-88d5-30d9afac735c | -6.53038 | -43.12413 | 2026-08-18 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cce5b71f-85af-3412-bf11-87d2b194f67b | -7.13556 | -47.51509 | 2026-08-18 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2602c8af-4834-3ec8-ad05-b56ec33e2281 | -9.06588 | -50.82871 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76a157dd-3507-34c6-a527-826621da7434 | -10.26586 | -50.40826 | 2026-08-18 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b94a1ab9-6ef3-37b9-b2e0-6625afb1384d | -9.28096 | -50.31907 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 974cdafa-569d-3a5f-a248-9e998a1ed107 | -9.77899 | -47.27814 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| efa102db-966e-3bf3-b4a9-e297ae85a2c2 | -9.07301 | -50.85302 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b917b7e-35c0-3cfc-8008-6fa6c22c0d30 | -9.84812 | -46.74952 | 2026-08-18 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 647c596f-7f6c-32f6-93fc-5eb097a04104 | -5.73695 | -43.27504 | 2026-08-18 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85928bca-bf8c-3b57-ae8e-f19c4531b7fa | -9.77521 | -46.72026 | 2026-08-18 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a2b1518-7eff-3871-a594-f716911159ca | -7.24383 | -49.88986 | 2026-08-18 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f1ff18ef-95d1-3a1d-a519-4d245398f740 | -7.45504 | -46.15786 | 2026-08-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 84caead1-9b53-3b8b-93f1-d5555b269e53 | -7.22404 | -43.2718 | 2026-08-18 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 197c713c-7e6d-304e-997e-b7fd15eac2fc | -6.17918 | -47.7842 | 2026-08-18 04:02:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fff98058-4cbc-33ea-9b63-ddb979fd80d5 | -9.46758 | -51.6522 | 2026-08-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2559a1ec-535e-3a05-a8f0-293b155db17e | -5.73671 | -44.50959 | 2026-08-18 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e02d4b46-92a3-3195-9e5b-6e34bf341c14 | -5.44793 | -41.84185 | 2026-08-18 04:02:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 89eedfc1-6156-3524-a30c-a0636b5106e9 | -9.59235 | -47.12751 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45875487-a899-3439-87d0-50829b39e1db | -8.49165 | -48.83033 | 2026-08-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5f6e21ee-c532-390e-87e8-fa690bbea73a | -7.81957 | -44.59962 | 2026-08-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ab3e2305-484a-3033-b507-4789029e3e1a | -8.34038 | -46.46745 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4973b3e1-22ce-3c7c-aad8-545d0e50e960 | -10.27469 | -50.42072 | 2026-08-18 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 98492c22-723c-3a73-80c3-212cac9c739e | -7.15801 | -43.14459 | 2026-08-18 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d328b972-d2a6-3acf-bcf0-206237ed469e | -6.53239 | -43.1117 | 2026-08-18 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 56b41ff3-9ac5-3c67-b32c-0bb404df390d | -6.30932 | -47.89107 | 2026-08-18 04:02:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65d1d02e-af7b-33ac-8fe0-e15e74d6006d | -7.14763 | -47.51432 | 2026-08-18 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d0f80ea-ea38-3626-a5ae-2f538d0f2a20 | -9.79731 | -47.30381 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a43903f-a562-3537-97a1-420619e4a8f5 | -8.59296 | -50.34647 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 8751bd1c-412d-36d1-83ca-b263130a8a55 | -8.59366 | -50.34271 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 5e246bc4-a46c-3151-8ec9-8ca45c2dc761 | -6.16179 | -47.79812 | 2026-08-18 04:02:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45852a49-6366-339b-a9f5-10bfb60cf9bc | -9.89818 | -47.7342 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 16b30ca8-fd3c-3976-bbd1-727dfb47598b | -5.17942 | -42.77657 | 2026-08-18 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc486551-6772-329e-9fac-8ddfd99c2823 | -9.04928 | -45.82387 | 2026-08-18 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6803a803-618c-31ac-abc3-5acafbc4e711 | -9.8236 | -47.28088 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab5de8dd-b093-35cb-8a7b-dbfd43bbf9e4 | -4.53546 | -42.93243 | 2026-08-18 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ab076bc-dac4-3199-a585-fe72b2280baf | -9.06654 | -50.82517 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbff8472-6a38-345a-90f0-9a46ec70c280 | -8.60952 | -50.34952 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9ee95d29-8b76-311c-90fa-05cdf39eb320 | -9.42593 | -48.26159 | 2026-08-18 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 796a5d8f-6488-3340-82e0-c11150892a9a | -6.53531 | -43.11642 | 2026-08-18 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b261fa1-5a37-3059-9158-bb347f97f707 | -10.85981 | -44.96824 | 2026-08-18 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c39a5e36-5162-3944-9c02-c70bd7052b10 | -3.50555 | -48.03583 | 2026-08-18 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e0d1d59-35fa-31e4-9448-7a0251c420ef | -8.59709 | -50.35492 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| efe8d9e6-75bc-397c-b01c-83aa72283976 | -8.36627 | -46.36831 | 2026-08-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d71df895-78fb-3bdb-b8bf-f4ccb4d98cfb | -7.12488 | -47.54953 | 2026-08-18 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 211df1ac-ceeb-3ff2-aae8-7bff781a65e3 | -3.26344 | -49.52851 | 2026-08-18 04:02:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed972496-1f95-34ba-b2ad-99a19f9c2738 | -3.6792 | -47.648 | 2026-08-18 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2a9f61d5-8cc1-3f78-8f9a-2bfe48f235cc | -7.82737 | -44.1012 | 2026-08-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f786e63-b0d7-3dbe-abe2-0fcfcfbc4d85 | -6.26941 | -43.27663 | 2026-08-18 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fed44427-5c1a-3392-b001-15dac986888b | -5.42893 | -37.59433 | 2026-08-18 04:02:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 31f67df4-8d7b-3977-85eb-892a5b4540a4 | -8.32825 | -46.48661 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f32a0241-bf2a-3d3a-88b0-60ba674fd43b | -3.43111 | -51.51309 | 2026-08-18 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 796ba1bc-2dfc-3971-a36d-c1b8c2766b91 | -5.2707 | -49.05328 | 2026-08-18 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5311782e-b0e4-3b31-a4c9-02459949b44d | -3.20756 | -49.06041 | 2026-08-18 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95680272-1da3-327e-958a-31d4d21b7849 | -4.49116 | -42.5638 | 2026-08-18 04:02:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f0dde849-9f90-3158-96f2-e4ae717ab7a7 | -10.29456 | -48.23561 | 2026-08-18 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d435da21-2877-39d9-a604-b1677e66653d | -7.53612 | -46.61646 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0b9c711-bf9a-3625-81c6-a1d5d64af066 | -4.01602 | -48.9042 | 2026-08-18 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| ec8e3f61-b5ae-3868-ac9a-5a31438cb168 | -8.59462 | -47.36712 | 2026-08-18 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8b35bef-c919-31ab-86fd-827cecd021f2 | -8.59848 | -50.34967 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 64cfb8fa-f3e4-3e0b-aec6-2a3b84ae0aa7 | -4.49628 | -42.56151 | 2026-08-18 04:02:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6715afd1-160e-3581-b04b-2c3cd8224b28 | -9.79974 | -47.31261 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b9609f6-5721-32c4-8313-fd181edc74e2 | -4.97914 | -37.23851 | 2026-08-18 04:02:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 58a78b49-5825-3f28-9c89-1b4fefa3b9bb | -8.60539 | -50.34103 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 763045e7-91e6-30b9-99fb-97e96b8ba698 | -9.59545 | -45.37659 | 2026-08-18 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30f881ca-0da9-37d2-8c5c-de9b3b4cb3c7 | -10.28095 | -50.44719 | 2026-08-18 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3448b4b-ced4-3a85-aae9-2bc48f5dda22 | -8.36696 | -46.36426 | 2026-08-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e0ff17ca-2c2b-3ed2-9b8d-571a8687dd5a | -8.604 | -50.35073 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 527d88cc-d47d-372e-bf94-75a13c09bd7f | -7.90532 | -45.00546 | 2026-08-18 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0271e04c-cd52-3e0d-a5ba-e80257e31f59 | -3.43096 | -51.51758 | 2026-08-18 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5074c6c3-2d00-3bc2-ad6c-838c50043d73 | -9.06743 | -50.85155 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76ea40c4-e3c9-367e-a5ad-ef2b37ece5ea | -9.21364 | -50.09873 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85579a51-ca04-3db8-80cd-3256a2950ba9 | -9.79532 | -47.31188 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 471e5d24-4a6f-3f49-8f36-4b183ddcb763 | -9.07546 | -50.83993 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 71d7ac97-960a-3cb7-aacd-df027050a8d7 | -5.1129 | -35.96223 | 2026-08-18 04:02:00 | NOAA-21 | SÃO BENTO DO NORTE | RIO GRANDE DO NORTE | Brasil | 2411601 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e0a352b-16c9-3f6e-8a41-8b7e003fa7a2 | -8.49374 | -48.81859 | 2026-08-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b15f8a0f-549f-3fc6-b7ed-0e8942ca1ae5 | -8.33967 | -46.47158 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ab80c910-06e1-3c51-8e1c-619b7ec5f91e | -9.46087 | -51.6233 | 2026-08-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33331fcd-8266-3fa7-ae65-c1eadff7cc90 | -5.66515 | -43.57632 | 2026-08-18 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da0ff1bb-a577-33e7-98da-60ec02d77f72 | -7.81878 | -44.60436 | 2026-08-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 61df178c-e764-3425-bf8f-2301305bb1f6 | -6.53464 | -43.12057 | 2026-08-18 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d4ee0551-a66c-3dd0-acf6-31952c1be3c4 | -7.01969 | -45.90659 | 2026-08-18 04:02:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c71f212e-f7a8-3d14-a854-cd32d5ea3980 | -9.40259 | -48.24995 | 2026-08-18 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fbc2f6a-4e3f-326c-9a9d-3012f6c2f3c6 | -8.32753 | -46.49074 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 49cc7252-9f55-3420-a4dc-eafd873d4713 | -7.20923 | -41.54211 | 2026-08-18 04:02:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8a3595ad-d8b8-3c12-a5a8-3f1d0aca3a57 | -4.97564 | -37.23799 | 2026-08-18 04:02:00 | NOAA-21 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0633643a-bdce-3a9c-96b5-b8261e4d6681 | -8.49322 | -48.82151 | 2026-08-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.1 |
| aaa01f22-0240-366a-b757-a24bb9909a56 | -9.07141 | -50.83036 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a7a7603-fb70-3eff-ab1d-665bfdf921de | -8.74326 | -45.31593 | 2026-08-18 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4aa381a-ed3f-3236-b9df-5bc5a1871c76 | -9.46835 | -51.64817 | 2026-08-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef6e271f-9fca-3977-ba86-9bd4e1619041 | -5.35726 | -39.49746 | 2026-08-18 04:02:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 813d3702-a547-3954-9083-2b32042147d9 | -9.77308 | -47.28602 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93dbdef2-5853-3c39-8faf-3e8bc50c9040 | -7.81495 | -44.60378 | 2026-08-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README10.md)
