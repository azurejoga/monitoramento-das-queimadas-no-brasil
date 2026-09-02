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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3d7ad7b-45c2-3d24-aa2c-845c748d8c25 | -3.97515 | -60.02786 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ffaf7e7-41a7-3662-89db-cc53113cb059 | -6.91923 | -59.64603 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab828cb6-f717-3389-8f1c-20d420a3a486 | -6.98568 | -62.97309 | 2026-09-02 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 957adfec-0e48-307c-ab6d-8513b5686d15 | -3.62039 | -60.55022 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 248121d9-8e01-3bb5-a8b4-a0d993a348ac | -4.36725 | -47.7735 | 2026-09-02 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 4985dc64-8d96-3f4c-85dc-80c7f362a367 | -3.06983 | -61.22245 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71f8dcbd-c19e-34c9-9cca-cc9a585a47fc | -7.20463 | -60.68307 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62616589-95c0-3086-9ab5-2dca79ac23bb | -3.85203 | -52.03887 | 2026-09-02 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91291cb7-5a37-32e4-b3df-23fadb29cbda | -5.82591 | -57.63819 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 700df9ad-00ec-3768-b0bd-22f198c8ff99 | -8.12852 | -54.95087 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a7d15ff-d3d8-3d62-8b38-df25f4a8751b | -6.13771 | -62.53072 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b120462-0652-348f-83d6-bd6369bca8bc | -4.15438 | -60.72255 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edcecc4f-3f1f-3f5e-ab7e-43b7462fa988 | -6.09091 | -57.7018 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ab35a66-463b-3f8c-869e-11a29978d989 | -8.47374 | -54.71545 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d11e7013-fcda-3917-8dd3-cd15c4f4fa66 | -8.45127 | -54.71635 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bc3a6f3-042b-39a7-9ce7-733d6da6499c | -8.46394 | -54.73134 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a0a380c-14fa-3337-8868-b955ff51418d | -6.03299 | -57.682 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f0d3e48-973a-318e-a411-6b2965dd0e9f | -4.95907 | -55.85159 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f131f027-5c0a-37d2-a4df-6272365b7fa8 | -8.43184 | -54.72003 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 423cc693-a916-3d49-a1d5-95bf9cf98ed3 | -8.45855 | -54.71745 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6c7ed6a6-82c9-3010-8fb0-9608f3b9c2d6 | -7.65739 | -45.88013 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71d5d1b0-a901-3c61-97e1-ca70edc796f7 | -8.44444 | -54.735 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 14d2574e-2241-3e60-83d8-348c493890ae | -7.20377 | -60.66618 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b4145d2-92bc-3730-b912-cc718c2626bb | -1.47137 | -54.82347 | 2026-09-02 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c180485-287a-3f57-8c95-3f8890fa3e1b | -6.0828 | -57.9239 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 976a952f-a279-3da0-9376-4f63597dda26 | -5.39378 | -45.62609 | 2026-09-02 05:16:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 169bc2e6-9b28-3b4d-9ccb-df8efa6456ef | -7.2812 | -60.66245 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3933d9b3-e2e8-3b22-884a-a84e9880f456 | -7.5218 | -47.33506 | 2026-09-02 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 604dc590-c3ad-3980-bdbd-80906fdfde7b | -3.9055 | -59.65211 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6e0e301-6981-3848-8d25-5cfe107dafd3 | -3.20889 | -61.16494 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bfc511e-69ea-3fee-acd8-ce68a0accc7b | -3.76178 | -59.41824 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b21cc37-ba3f-3c93-83d4-11818d542175 | -5.95572 | -57.67681 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e06babed-78af-3030-b35d-5f9335c76884 | -2.11993 | -56.81858 | 2026-09-02 05:16:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f8d309d-1c7a-3f7f-afbd-847427a83956 | -9.66391 | -46.53373 | 2026-09-02 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 227edbfd-96d7-318e-92a5-0e773ee3a11f | -7.57863 | -60.4818 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3033d95-3f30-338a-8376-f9ec66f7331d | -3.65944 | -58.91665 | 2026-09-02 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16ce0511-872d-32e4-a415-4665d629d3ca | -6.09169 | -44.1394 | 2026-09-02 05:16:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a10877c4-36e6-3807-8e47-30547a7fad47 | -5.82977 | -57.63526 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5adc910-a469-3744-84f5-1ce8e20755df | -6.12183 | -57.74215 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c754d34-bf17-3933-bdf5-c3bb6114ccef | -6.18099 | -57.73418 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ba69163-2496-30df-860a-2218ea9ce18f | -8.47311 | -54.71965 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 7ad6c47e-c1fc-38e4-8601-d610d4d28cdd | -6.80268 | -59.45628 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2db06d3-074b-3ddc-9ec1-96354634b0ea | -5.56466 | -60.21087 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96026082-2a2d-3649-9c14-78f907d17765 | -8.44097 | -54.71041 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 996c826c-0f60-3e71-a33b-d04cdeaaa90a | -6.2016 | -53.48421 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4eaedab4-309a-3c58-8af0-bdd359f40192 | -7.18333 | -55.48706 | 2026-09-02 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b95e86f8-aa93-3c6f-8b41-39162304889b | -5.95574 | -57.69806 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 262b7fc5-e17d-385c-aefc-b8062aed3323 | -6.80169 | -59.59313 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f51e5d0-5f20-3ab9-8395-9df9808182f2 | -2.4993 | -48.13427 | 2026-09-02 05:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5b0b68c-cb19-3c19-981d-ce958532eca4 | -8.12076 | -54.95369 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bed7efff-2df1-399a-9385-b7521a21578c | -8.46282 | -54.71376 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 8255993f-42b7-39af-829b-484a0222c42e | -8.50201 | -55.30167 | 2026-09-02 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6415a398-dbdb-3165-9b1d-b6f2db817053 | -3.06673 | -61.21698 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e77b54b-5bf3-3c9f-b472-b84e5605e690 | -5.75813 | -53.3986 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fbad2d69-213b-36e7-b2e2-f9f9e301da9e | -6.69132 | -59.94722 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5c957521-056d-3e8c-82de-2187d9fab15f | -8.42885 | -54.71522 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25a0b7e4-bda4-341f-bb6b-71487274397f | -1.60778 | -55.15999 | 2026-09-02 05:16:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2865ea33-4bb1-383e-b9cb-85ef5ec30993 | -3.13337 | -61.18033 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45288f47-1ea2-3103-8376-a0c05e0bf220 | -6.18706 | -57.73868 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcd767af-9dba-389f-ac27-d3b6530f6441 | -7.20242 | -60.67435 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 893a382b-d0b8-3c19-a388-c440fb21c456 | -5.85946 | -57.555 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fdf901c-398d-30dd-ae1d-298fd818f450 | -4.97086 | -55.84236 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 763646b3-c79b-3914-8f7c-8e1b7cb5db34 | -6.05165 | -53.83345 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6618163-ed26-37f1-8b16-899222de6037 | -7.21668 | -60.67663 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e78ca3ea-d4cb-3f68-b41c-39ece2e150c6 | -3.23906 | -47.2511 | 2026-09-02 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 27944204-6a2d-353b-96ed-f085d42e5991 | -7.26094 | -61.10983 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b1456ef-f6ca-3777-8afb-545269fa7145 | -6.93758 | -59.64132 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2a1c3f3-7af7-36da-aaef-0d526fcee285 | -3.63219 | -60.54765 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eb701b5-7e7a-3873-8df8-e2c7899185b9 | -9.66455 | -46.52869 | 2026-09-02 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58ddfc1d-9128-34c5-b16c-c3c2d8d894ae | -3.06666 | -61.224 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90c7294c-dbe3-3b9a-9d83-1867d31e4da4 | -7.45225 | -59.92669 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c04362cb-8a8d-35ac-974d-a27acd3e8911 | -6.07933 | -57.71061 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3f5047f-9315-3025-97d4-7a515f3e6c60 | -8.49284 | -54.58638 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6ce0542-348d-3a75-901c-e42ab7868f36 | -8.45793 | -54.72168 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 33b2a655-dbaf-324b-bc4e-9ff8b33978c2 | -3.36508 | -59.40571 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72a884c5-2813-34be-b8ab-7b6c229e1faa | -7.65297 | -45.87696 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e04ba1c1-489f-3f73-8421-65d4fcc054c9 | -5.3358 | -60.14717 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1605f65b-d4bf-36cf-90e0-2ef685410a56 | -8.44041 | -54.71266 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2603c61c-9dab-321f-ba7e-d2a5135450e9 | -8.43076 | -54.70259 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 09b46ed7-019a-3e08-886e-e847460c8ee6 | -3.75224 | -59.3219 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04368186-9431-3700-aa56-5d43e6bec8f1 | -6.11455 | -57.63825 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6b736b97-9ff0-3d8a-8393-277d2572bc1c | -8.47436 | -54.71123 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 010317cf-aea2-3c9a-ab9c-b91d86d9fc64 | -6.05454 | -57.73857 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a8248b7-94f8-3321-9350-ee2034b49b62 | -7.54674 | -54.99751 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b39e8cf-3d4c-3a08-9300-defba85690cd | -3.80006 | -59.29031 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e1bf584-9dc6-32bc-817e-0ae85bd975a4 | -6.04592 | -53.84615 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de702c7d-5787-34c9-9b8b-aa3ccbc98ab3 | -5.95848 | -57.68078 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45868ef3-0838-340a-b5d4-bc53254f9700 | -8.43012 | -54.7068 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b26ee9fd-5059-33c5-94aa-aba4fa237c2e | -7.4561 | -46.15652 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d87fb37-7c9f-3248-88f0-10888c92dfc8 | -6.11326 | -53.45425 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e03bd50-9f1e-3f40-acac-4fce075b5403 | -5.95076 | -57.68665 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3db6cd96-a46f-3159-aeaa-1f06338c091e | -8.44105 | -54.70842 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8e0e7b5-580b-36af-8e9f-d39b453d52ab | -7.34065 | -60.58398 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d305bf5-0bd9-3758-961f-9dc17ddfbc18 | -8.44461 | -54.71097 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bc12f93-96cb-38b6-b727-a0c9289d6e6a | -6.80209 | -59.45998 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5000397-48e6-3347-abb4-74b836925f46 | -5.97716 | -53.5868 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e676aae3-753f-3190-bb59-3fd7c1661f17 | -6.15231 | -57.72254 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ae4589c-6af0-3703-aaec-c18c686a80f5 | -7.18904 | -60.6887 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f1857cd-eedb-3980-9838-1f2e348f6ad5 | -5.93612 | -50.21278 | 2026-09-02 05:16:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 438ccfec-c84d-3cda-bae2-2a0f86643803 | -7.21313 | -60.67599 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README51.md)
