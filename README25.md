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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 955a9fcc-9e1d-3a63-86dc-62145a5ddb70 | -3.62655 | -49.20073 | 2024-11-18 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2877ad90-febe-33f9-a47d-82b1481748c7 | -4.95727 | -44.84137 | 2024-11-18 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fb39d0b-60b4-389d-9f6e-545db4e50ffb | -5.76752 | -46.53703 | 2024-11-18 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f93e0f57-5dad-3723-ae0a-224d8dddf9e6 | -3.05964 | -54.40392 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3e19baed-5014-3929-b4d2-38364da87f8c | -4.58527 | -44.22888 | 2024-11-18 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c5412a6-776a-38b0-9057-834c14c33d3b | -4.27177 | -50.58799 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf3dcc61-f6ad-396c-8829-37cde2928a54 | -4.11039 | -51.05252 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93c481a7-ad2d-3759-98af-efd33c3dbbc2 | -3.89574 | -46.62338 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae688744-3c23-3390-896f-4b736fe83f49 | -3.05146 | -54.41317 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bd8c971e-43e2-38d6-b49f-c73bfd62cfe3 | -3.33739 | -53.31381 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30289301-53ef-36c3-a043-8b64a275f2ec | -9.30216 | -46.214 | 2024-11-18 04:12:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be17a767-dc37-3a5f-99a7-6b74aa5bc3b9 | -3.98313 | -46.7065 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8505a8dc-2719-36e4-a64f-d49bc63feff8 | -3.05234 | -54.40795 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c683a364-fad9-327a-a822-bbf0749dd457 | -4.26956 | -50.59221 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01605b37-ad39-3d4d-9edf-8cbc316a8be0 | -6.57647 | -42.00543 | 2024-11-18 04:12:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 983daaa0-0b23-38ff-a60e-e1973c76ecdc | -6.61462 | -47.35881 | 2024-11-18 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dda8b308-b4c7-3ce9-aed6-4bc00f91b353 | -9.64732 | -47.41809 | 2024-11-18 04:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a62d0fb-89ae-312f-a3ee-04d04e861030 | -7.71762 | -45.66446 | 2024-11-18 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d1b23da-a7bf-3cdf-a4b8-def7947947ce | -4.09856 | -46.2765 | 2024-11-18 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e8bd3b85-96a5-35d8-9e83-10e1fd12acfb | -6.40044 | -44.74081 | 2024-11-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 420fe9de-f511-350a-96a0-76a84fd8cb66 | -5.3346 | -40.9044 | 2024-11-18 04:12:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5f252d76-c735-372e-90a6-6b5708065069 | -3.37479 | -53.32479 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e75c8cbd-ca7a-3117-84ac-302a533bd984 | -4.7042 | -49.6265 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bcbc02c-1e7e-3a35-b765-b8c2319d9247 | -3.33657 | -53.35531 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d35d1ab5-ef5a-36bc-b61f-700225f4d4ef | -5.24093 | -44.75523 | 2024-11-18 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a43e991-de63-3d7c-9df2-17547683133f | -9.30408 | -46.20219 | 2024-11-18 04:12:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2464a907-7566-3a24-b0c1-eb2a517a4a07 | -7.09914 | -39.29955 | 2024-11-18 04:12:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f2007f93-78eb-3a0f-b49b-8a511dce7e5b | -4.72335 | -44.43687 | 2024-11-18 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ee9328c-4ae8-3984-99ff-88d0deaef3b9 | -3.05879 | -54.40894 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4f7f18fe-9e2b-34f7-80d9-bca1c9132dbb | -6.00712 | -46.39955 | 2024-11-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 640779c2-58b5-3951-82ba-05c581e5e965 | -3.37179 | -53.32917 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8606261c-e89e-3fee-9ce1-bfafd4eb7ff7 | -3.58492 | -53.78603 | 2024-11-18 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8d8b744-2689-387f-83e2-788012e571bf | -3.87726 | -54.35095 | 2024-11-18 04:12:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72ecf8ae-9f33-3425-98dc-dd918f8b4ee7 | -4.74666 | -44.9098 | 2024-11-18 04:12:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 957e69bd-df95-3b87-a305-1fd58d4ad28e | -7.18063 | -39.11729 | 2024-11-18 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ffd87478-4b1f-3894-9c89-f71359bfd415 | -3.34055 | -50.49825 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ef86d1c3-6b01-3d29-b31d-d9511cf2225e | -3.18828 | -53.23409 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62c5bdcf-b806-3420-8afe-e5be4adcfff4 | -3.18088 | -53.24136 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f1cce77-66b6-3825-9b7a-1bc400396b69 | -5.58855 | -45.20672 | 2024-11-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fabb82af-4205-36ef-91a0-bf7b645b9427 | -3.37043 | -53.31441 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5035e34-555f-3361-b118-1e95478af1e6 | -4.70344 | -49.63109 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8173ad9-1fdb-3bca-8304-7caffd9a5abd | -8.27162 | -43.9768 | 2024-11-18 04:12:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46df59bf-e2dc-38ed-a208-6c5692414db8 | -7.58444 | -39.05122 | 2024-11-18 04:12:00 | NOAA-20 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7868465a-7b4f-3e37-84e7-98099cf6ac91 | -3.9931 | -49.40525 | 2024-11-18 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba042bdb-c9e3-3184-9692-5149c901146e | -4.07152 | -46.85452 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 102bf55b-6f06-3cef-8301-b2f67c96730f | -3.58514 | -53.45555 | 2024-11-18 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85fb6227-0024-37f1-b52e-fd9b2fd789f3 | -4.95262 | -44.84837 | 2024-11-18 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12f0c3da-e4d9-3a15-9196-621c257bb5a8 | -3.94878 | -46.70103 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aa196ab7-05c9-37dc-bde8-69299d2245b1 | -5.4635 | -46.33197 | 2024-11-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42c4bbf8-7d89-34b3-b278-4ce20e82377a | -2.8477 | -54.00828 | 2024-11-18 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3da47d9d-dffc-30dc-83c2-70444c0d6958 | -3.9137 | -46.13605 | 2024-11-18 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86c12d4e-042d-3ef0-8252-7b17d30af21e | -7.53803 | -35.31514 | 2024-11-18 04:12:00 | NOAA-20 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| afea9da4-416f-37fb-a8c4-1c7f16329e8d | -4.947 | -47.80431 | 2024-11-18 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 20d452ba-3c2c-3a8c-8304-3b5fa14a8335 | -3.51271 | -50.23358 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d316e436-2e70-373d-8ad8-ba1a34985082 | -3.0601 | -54.40679 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 53a5448d-3d9e-3606-9dcd-0c5c618093fb | -3.18191 | -53.25718 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3e0a95e-440d-388f-bbb2-36d88866eb3a | -4.1109 | -51.04952 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9b7cfee-d461-3bd6-9a7b-208a31bd3eec | -3.0658 | -53.28792 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1c9f5089-df5d-3297-a155-c613ef2f82e5 | -3.18608 | -53.24689 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79986bef-6ab3-30f5-9b43-c8d76317bd3b | -4.38228 | -50.84414 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2fef2fc-033f-32bb-b178-390b3bb0935e | -6.37005 | -41.54624 | 2024-11-18 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 09195ecb-27cb-3601-81b4-57cac89f4c3e | -6.47828 | -42.3749 | 2024-11-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1f2f641d-368d-3a79-8591-3b822a115d36 | -3.95332 | -46.72111 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38897314-7001-31d5-80bf-fa7d43139b32 | -3.03142 | -54.10762 | 2024-11-18 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b67290d-ebe2-30a9-9249-fc1632adf0eb | -3.93962 | -46.70905 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f0785465-2b3c-3b25-8eba-1dfa9c697f01 | -3.65863 | -50.44143 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e85a21aa-077c-3d50-a136-a323b0039f42 | -5.08331 | -42.56478 | 2024-11-18 04:12:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7421e75d-deb2-302f-ae62-ee96412a3bb2 | -3.33799 | -49.92476 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2de03c0f-5554-3d53-9a23-709099527e6d | -5.55388 | -46.2836 | 2024-11-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4e0be6c-63ac-356e-b709-1f1c0e7d6b78 | -3.9495 | -46.72047 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab6fd5fa-8d7d-3fe3-beab-0190a74106cd | -3.18856 | -53.25415 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a69eac74-7e6b-38f4-9926-bd353982af3d | -4.03688 | -49.28005 | 2024-11-18 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2526a05f-2ae2-30f2-b986-3128ed568ceb | -4.72675 | -44.43741 | 2024-11-18 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94071671-3f4e-348e-98ca-fb4d20c638ea | -3.34278 | -49.9255 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2245bca-5a91-3d1a-a0dc-2fedfbd53a98 | -3.10049 | -53.10054 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22929e7f-e218-3345-805b-aecc5d438555 | -2.79991 | -52.99703 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edfb393b-65f6-3c7a-995c-2dd3c6eedb7c | -3.95714 | -46.72169 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6664ff55-a197-3089-b931-9d24ca165eef | -7.72015 | -45.73621 | 2024-11-18 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc2e7e8b-fc64-33f7-8d23-55dd9990931c | -4.26572 | -50.67797 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 494ca7e1-aa07-3cc4-ab9e-28aaa83d453a | -5.51177 | -41.07368 | 2024-11-18 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b873f381-9237-3565-9078-8c06332201ff | -4.90347 | -44.02909 | 2024-11-18 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c3aa88f8-f056-3b2a-9a86-ff31b8deea88 | -6.4816 | -42.3754 | 2024-11-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74e4c47f-73aa-381d-a67d-977e64a1fdd2 | -6.49697 | -42.51674 | 2024-11-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e67aebea-7bfc-30c3-8b4d-2dfaebc6e98a | -4.74045 | -44.63971 | 2024-11-18 04:12:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a192ac87-04c1-30d3-8ee0-77b36104347c | -3.52465 | -50.25211 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 825f5fdd-7113-3b2e-98c3-06299c933107 | -3.06129 | -53.27822 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09e3f338-c064-34ae-88c3-aa25562cd2f5 | -3.89193 | -46.62283 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee7facf2-0d2a-332e-a8e8-f572229d6a3b | -4.95488 | -44.50648 | 2024-11-18 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 595fe373-f3ca-3978-950d-9f2cfefb597b | -3.18015 | -53.24557 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7f2101c-b775-3c2e-9bab-660d1f37b702 | -4.37399 | -50.52046 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| da60ea3c-b2f0-370f-9271-6c4947a98bb4 | -5.4967 | -49.58461 | 2024-11-18 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2ab9ec6-137b-3f3b-835b-2c30c774d293 | -3.374 | -53.32938 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86c521e7-950e-3285-bc46-fd9cf02f8e04 | -3.55096 | -54.57593 | 2024-11-18 04:12:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1e8e5f4-6aa3-3483-8f35-64e5311d80e3 | -3.14213 | -52.98429 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a2d69e2-64ec-3ec0-985e-300fcd82e0c8 | -3.10256 | -53.10935 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e83c6d2e-8bf7-321e-b794-65643a2cb849 | -3.94497 | -46.70033 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdd36eed-7885-30d5-9f52-e66587958727 | -6.03173 | -46.45634 | 2024-11-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9689dd0-2464-3082-8ecf-71e1e6f87418 | -7.39907 | -42.76498 | 2024-11-18 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 6abdfbf4-132b-3b1a-b049-a3fda3ff1a26 | -4.10839 | -46.87069 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b53c5c0f-6df5-333b-932d-664598bce237 | -3.53291 | -50.51685 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README26.md)
