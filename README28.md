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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec3d3332-683f-315c-bf02-240d0070a5b7 | -11.97818 | -43.46877 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2789c7c-d80e-31df-8559-824a0b85a46e | -16.71576 | -41.88816 | 2026-10-10 03:25:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2cca1d2f-4f5c-3cac-9280-32ff978c5381 | -19.64624 | -45.931 | 2026-10-10 03:28:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccaf1e46-4900-312c-a1d1-e3a8d1db436a | -18.8486 | -41.97448 | 2026-10-10 03:28:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a573373f-4ad6-3ce0-8948-4801496d12f7 | -18.64161 | -41.33343 | 2026-10-10 03:28:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0fc6a2c8-a2ff-37b0-8d56-0ecfaec8149a | -18.31708 | -42.39379 | 2026-10-10 03:28:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 55fb6342-cbd3-3052-9604-62f7e83c7f8e | -18.08736 | -42.26036 | 2026-10-10 03:28:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8044eb4b-96ad-3755-81ae-85672fb2f036 | -18.3292 | -42.39212 | 2026-10-10 03:28:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| acf6343a-2b65-3c28-8421-76aade04c36f | -18.09135 | -42.26894 | 2026-10-10 03:28:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2154a47a-4da1-394b-9adb-445c92fe3b2e | -17.72085 | -42.05116 | 2026-10-10 03:28:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ab357846-be6c-39d0-85a1-24b1b78b992b | -18.64094 | -41.3366 | 2026-10-10 03:28:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0dab81bc-9a8f-39f4-b760-cd4691ef4d13 | -18.78336 | -46.47538 | 2026-10-10 03:28:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 537c498a-6a57-3fba-8dae-64535cd9d618 | -17.71537 | -42.04959 | 2026-10-10 03:28:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 99552741-945b-3702-95bc-f6e754d5c53f | -18.32325 | -42.36531 | 2026-10-10 03:28:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cf61b34c-78e9-33b7-a544-8090861fcbb7 | -18.08935 | -42.26273 | 2026-10-10 03:28:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6e91fc0d-3888-32a7-9630-d63713e264ed | -17.45872 | -45.08438 | 2026-10-10 03:28:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 748aeced-cbac-3ec7-965b-397a6ba062c2 | -18.08452 | -42.2579 | 2026-10-10 03:28:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8d7bc430-b036-3e29-8394-43dfeafd28f9 | -20.79306 | -41.13206 | 2026-10-10 03:28:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fa724541-5531-346e-a261-0e4b3c3139bc | -18.32242 | -42.36912 | 2026-10-10 03:28:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5a7be121-827b-339f-88a0-1cf085a89758 | -17.45517 | -45.08288 | 2026-10-10 03:28:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cb80ba3-2a8c-3fa6-b57a-e7fc1da18c3a | -17.46403 | -45.09187 | 2026-10-10 03:28:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 136efab2-070d-3682-98c9-7e3bbb2544fa | -17.45368 | -45.08924 | 2026-10-10 03:28:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b450b1a-17b4-3577-8e21-fbbf65e7593a | -17.46046 | -45.09026 | 2026-10-10 03:28:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 36e5a66a-539f-31f2-ad5c-2c446c1c8ee9 | -18.08858 | -42.26639 | 2026-10-10 03:28:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dc129408-9f03-3c8e-a360-40b658638006 | -17.95761 | -42.49142 | 2026-10-10 03:28:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 22db2014-2526-3290-8d32-3ed4c10f4c2b | -19.64478 | -45.93702 | 2026-10-10 03:28:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fffa0cd3-0f9b-3aac-9de9-add77aadd52d | -18.63573 | -41.33538 | 2026-10-10 03:28:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7c9aa6f7-ee35-3977-aeb0-8280d988a05d | -18.84939 | -41.97079 | 2026-10-10 03:28:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e0abd00d-a445-3380-a9bf-0ce461158db6 | -18.09217 | -42.26517 | 2026-10-10 03:28:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d974af49-c2a1-3110-b72a-9b86343c028c | -18.63441 | -41.34159 | 2026-10-10 03:28:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0ecfed95-c385-36ef-9358-1e0f5461b737 | -18.32265 | -42.39524 | 2026-10-10 03:28:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 64eeee8d-d6aa-3d35-8fb7-882e00838f85 | -18.3237 | -42.39035 | 2026-10-10 03:28:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b847bfbb-db9c-3061-990e-cc0ea7c80b96 | -17.45337 | -45.07708 | 2026-10-10 03:28:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0607970b-fc6b-3bb2-ab79-e4a302099692 | -17.45728 | -45.09071 | 2026-10-10 03:28:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 814d7415-5fb7-3345-8722-14d229808d03 | -12.5028 | -51.2937 | 2026-10-10 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 97503b4a-1d61-39af-87a2-9dc57dabdb9b | -11.2658 | -46.3485 | 2026-10-10 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 8abaa2f3-011a-3483-bf38-8c5a8143b76e | -11.2467 | -46.3511 | 2026-10-10 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 4e890241-9569-3c77-b549-65e226c92409 | -7.5347 | -45.3233 | 2026-10-10 03:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| ca56cf8f-394b-3e75-bc0a-c433b1bb3a4d | -14.381 | -54.9679 | 2026-10-10 03:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 9c7e72e5-e155-3476-8275-e62d4934ea74 | -3.2388 | -49.4411 | 2026-10-10 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 5e4447bb-54dc-3f26-91ed-34dca9de21b2 | -3.9915 | -54.4619 | 2026-10-10 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 22adae42-02e2-3ee3-b29e-0145637fbe68 | -3.5676 | -54.6946 | 2026-10-10 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| fffa94b9-21e1-36f2-9a67-4f456a2ae7a9 | -3.9916 | -54.4419 | 2026-10-10 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 66c36d27-7122-3a3d-aac0-6a46ad191a92 | -7.0225 | -47.6829 | 2026-10-10 03:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 3f4a8bb8-9ba2-3756-b080-88a242a40e3b | -7.535 | -45.3006 | 2026-10-10 03:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 4e4c7d75-5be6-3772-a35b-9b86322fa2e6 | -4.4025 | -49.7774 | 2026-10-10 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 12503c2e-93e3-3564-8f8e-bf49b7f6b0aa | -3.9912 | -59.356 | 2026-10-10 03:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| ba00fa4a-e0c6-3ed9-a1ff-9bc8a662e7d2 | -10.8905 | -44.8232 | 2026-10-10 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ea5ac956-4cf9-3fea-ae5a-0c088157c21b | -10.9097 | -44.8206 | 2026-10-10 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c75c3e05-57d0-3c7e-991a-468d9cf484d8 | -7.0228 | -47.661 | 2026-10-10 03:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 89172c3b-667a-33be-b750-b456923f63f4 | -14.4003 | -54.9657 | 2026-10-10 03:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ad43434a-effa-3a5c-93fb-152dc85bc0ea | -3.9911 | -59.3752 | 2026-10-10 03:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e447ec07-d9ab-30cd-ae62-56428ee55a6f | -3.2204 | -49.4205 | 2026-10-10 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 3e3f23b3-fbad-3bab-ab9b-b1ea7f1f0ba9 | -10.9953 | -45.4068 | 2026-10-10 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 00be0c97-f610-3eea-91f0-8564f8be8250 | -7.0413 | -47.6814 | 2026-10-10 03:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 1975859d-9e01-3089-b68e-b26078f308a3 | 2.727 | -60.2586 | 2026-10-10 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 62864785-81fe-33b2-a640-190f65819288 | -9.9384 | -44.8791 | 2026-10-10 03:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 92c8d649-0463-383c-8fad-b1838dc73198 | -6.4566 | -55.5008 | 2026-10-10 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 1514a797-cd7a-37cd-bf76-a817af26b96e | -10.9957 | -45.3839 | 2026-10-10 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 8263f695-62d5-3cbc-8da3-6cb173003af5 | -3.2203 | -49.4417 | 2026-10-10 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 42340f15-f4ea-3ee0-9492-230711adff2c | -3.9912 | -59.356 | 2026-10-10 03:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6bbbfb27-a9f4-332f-a7b4-322416f25af0 | -7.535 | -45.3006 | 2026-10-10 03:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 565d2089-8740-3ce0-9c99-7f3f37afdf4c | -7.0415 | -47.6595 | 2026-10-10 03:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 542fe0a0-991b-3d40-ac8f-215b7bb01e00 | -8.9967 | -45.8776 | 2026-10-10 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| c0acad47-dc5d-3cb4-9190-d43b22106695 | -7.5347 | -45.3233 | 2026-10-10 03:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 7d74d7b9-d945-3dd3-8aa1-6dc77ec8d354 | -10.8905 | -44.8232 | 2026-10-10 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| cf421cef-1cb9-3928-a2dc-b68907a2f78c | -8.9964 | -45.9002 | 2026-10-10 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 1399fbae-66ef-3971-bf5d-869de0f8810b | -14.3418 | -55.0135 | 2026-10-10 03:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| ae63ff71-ffde-3525-a48d-cb0c89937beb | -3.9911 | -59.3752 | 2026-10-10 03:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 6d8a6c6e-8d42-3cd8-9ba4-947113904ea4 | -3.2203 | -49.4417 | 2026-10-10 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4ea878c9-769c-3636-86fc-87f491fa14af | -6.4566 | -55.5008 | 2026-10-10 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 12a41141-4f28-3650-96cf-97db5b2e84f2 | 2.727 | -60.2586 | 2026-10-10 03:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| addcf003-edcc-3647-9492-b8c0e6d68fa2 | -7.0413 | -47.6814 | 2026-10-10 03:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| cbefbb91-0101-3203-a68e-71eb4358daea | -7.0225 | -47.6829 | 2026-10-10 03:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b95cd864-8895-3616-8f93-2746cd2fb950 | -12.5028 | -51.2937 | 2026-10-10 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 688c1e1b-317e-34e1-b3e5-5391daf85b40 | -4.4025 | -49.7774 | 2026-10-10 03:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 8b09a51f-bcbf-341f-b59a-cd343aec31bc | -3.5676 | -54.6946 | 2026-10-10 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 607befcf-c953-32be-b3e3-1a781ac6feff | -9.9384 | -44.8791 | 2026-10-10 03:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 3402443b-5f92-3056-94e6-79a9714f0d5f | -7.0228 | -47.661 | 2026-10-10 03:50:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 8531007e-64a7-3f7c-a796-e2536ad596be | -11.2467 | -46.3511 | 2026-10-10 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 3cbbc43a-cad6-3281-977c-724715ab2c64 | -3.2203 | -49.4417 | 2026-10-10 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3ac9234f-661d-3ec2-92cb-a4f42fda0ab5 | 2.727 | -60.2586 | 2026-10-10 03:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 149b7f3f-1f64-360a-b38a-86765af8a966 | -7.0415 | -47.6595 | 2026-10-10 03:50:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| a0f598ed-3208-3843-8a60-ec104dae2caa | -3.2204 | -49.4205 | 2026-10-10 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 461b32bb-d68d-300d-a6f5-51f29fdd6cf7 | -4.4025 | -49.7774 | 2026-10-10 03:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 8dcb5c37-81b6-3ac4-ac4b-d95e0134e0bf | -7.5347 | -45.3233 | 2026-10-10 03:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| ba589e1f-02b2-397a-a20a-a1bc46cb659b | -7.0413 | -47.6814 | 2026-10-10 03:50:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 45d9186d-c131-3952-963b-97f973240df1 | -3.9912 | -59.356 | 2026-10-10 03:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c833828a-c17a-3313-9413-bd643ee1f6b7 | -3.9911 | -59.3752 | 2026-10-10 03:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 5e5cd5fe-cfc4-3209-a33a-4aa0c1c9156a | -11.2658 | -46.3485 | 2026-10-10 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 4dfccb55-5377-31c4-b693-f5600749b464 | -10.8905 | -44.8232 | 2026-10-10 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e2334178-ad30-323d-b4b8-3114c81d0790 | -14.3418 | -55.0135 | 2026-10-10 03:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 2cd6302e-4f70-395c-890e-aafdb45a3bfb | -7.535 | -45.3006 | 2026-10-10 03:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 5878daf9-00f2-35ea-a935-98fc65811f4b | -7.0415 | -47.6595 | 2026-10-10 04:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 31244432-8f78-39bd-a864-38ed6690db4e | -3.9911 | -59.3752 | 2026-10-10 04:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| f6300179-c3c7-3651-88b7-f440f74589e5 | -10.91 | -44.7975 | 2026-10-10 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 97cf60d6-2ca1-3888-8ff0-2311a153ccad | -10.8905 | -44.8232 | 2026-10-10 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| ebdf01f2-8fbf-3f98-bf9a-bbb0e0f381be | -10.9097 | -44.8206 | 2026-10-10 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 24e1c681-be25-38a6-bddb-0d3adc9027e1 | -10.8909 | -44.8001 | 2026-10-10 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 8af98b98-2509-3e1c-8904-2d23b4e61dc7 | 2.727 | -60.2586 | 2026-10-10 04:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |


[Clique aqui para ver as próximas entradas](README29.md)
