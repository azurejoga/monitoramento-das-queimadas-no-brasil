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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20f0c2b3-768c-37f1-918c-ef9eb7e4aa26 | 3.34166 | -60.86834 | 2025-12-10 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4a19891-dea9-32eb-be97-433b5cb370a7 | -1.4775 | -53.5388 | 2025-12-10 05:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2aa67d48-e1db-3ba4-af5b-6b712aae6cb8 | -1.47476 | -54.20522 | 2025-12-10 05:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 76b4f2f5-d8a2-3648-a601-b26eb8178ff6 | -1.47918 | -54.20122 | 2025-12-10 05:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 75ab9691-57bd-38cf-877d-a8ec96eed732 | -2.59471 | -54.55422 | 2025-12-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 913f5fc8-673e-3804-8ad4-e41657bafdaf | -1.59122 | -54.12096 | 2025-12-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6afd4f45-6489-3b7d-b362-65a4c5c13388 | -1.58786 | -54.12101 | 2025-12-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 163fe682-9796-3aca-8535-f75767fb1731 | -2.78013 | -54.52658 | 2025-12-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 55993012-e282-345e-a3e3-c929c905038a | -1.87788 | -54.68618 | 2025-12-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a75c9ff3-5dd3-3d0f-856a-0d120e418bc3 | -1.59418 | -54.1219 | 2025-12-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c68968ac-faac-3706-97e0-86be70ff3925 | -2.59273 | -54.55647 | 2025-12-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 193f48bc-6c42-3516-8dd8-3c2c82fa30c5 | -1.5849 | -54.12002 | 2025-12-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63136a2c-d802-323a-9c02-8ec85f3d713d | -2.77382 | -54.52598 | 2025-12-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8cb0ec48-1ff6-31e8-af6b-ddabb1fdf111 | -12.51842 | -58.35686 | 2025-12-10 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81be5d30-b20b-3823-9b50-d2a769220056 | -12.51797 | -58.36061 | 2025-12-10 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7edf8dea-13c6-35c3-8706-3b83de968c4f | -12.51238 | -58.35986 | 2025-12-10 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 232e3a24-25ef-376e-ba75-4f739acc747a | -7.86224 | -61.49814 | 2025-12-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70085345-22db-379e-8196-7963b881ed8b | -12.51193 | -58.36358 | 2025-12-10 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 795f5ab7-84c5-321e-b846-9b3d0ca12e6b | -14.30244 | -57.58194 | 2025-12-10 05:50:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| beed50ab-ce36-311c-972e-6b9d2d2b03b6 | -12.51751 | -58.36438 | 2025-12-10 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a10af2d3-a429-3b9a-a1a9-e5299662c1c7 | -12.51148 | -58.36731 | 2025-12-10 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f9743da-b161-331b-b1c9-0ff7d144ccbe | -12.51283 | -58.35614 | 2025-12-10 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ae8cad7-7e15-3f8c-91d2-9aec5e11a978 | -3.46696 | -42.01719 | 2025-12-10 05:57:00 | AQUA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 491662a9-69e2-3c16-80a5-458e3c9247b6 | -3.42871 | -41.65692 | 2025-12-10 05:57:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| d8654efe-c9ae-3f9d-a6c5-79a2497c9c08 | -2.89038 | -45.23997 | 2025-12-10 05:57:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8141d1b0-61a1-3155-b429-4d79cbca915f | -1.75861 | -45.51077 | 2025-12-10 05:57:00 | AQUA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| ade6de1f-0b87-3dd6-8fca-3b39a44fa420 | -3.68704 | -43.81743 | 2025-12-10 05:57:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8bf22581-338e-3ce2-bfe0-53529e87f06a | -3.40106 | -42.45893 | 2025-12-10 05:57:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 8a46bb2d-334f-3824-ada8-efb30874a822 | -3.43023 | -41.64668 | 2025-12-10 05:57:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 0c8bd983-1774-31e8-99a2-5edb87166b52 | -2.26461 | -47.85983 | 2025-12-10 05:57:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c13424d3-c3f4-3304-8a3e-7efe7118cf68 | -2.84903 | -45.27114 | 2025-12-10 05:57:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 9211c86f-5c53-3b1f-bc95-0f0b9f4dc57e | -3.41926 | -41.65555 | 2025-12-10 05:57:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| cec11ce3-7619-3e3a-a6b2-08b4d8ae6216 | -3.43969 | -41.64805 | 2025-12-10 05:57:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 807747b3-76ca-3ced-9c19-e1d0e5bd3249 | -3.39966 | -42.46832 | 2025-12-10 05:57:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 18c18cda-aac3-30f0-b407-40aad86c6369 | -3.68573 | -43.82617 | 2025-12-10 05:57:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e23466c1-17f8-32b6-9bd6-94042da1cabd | -3.19944 | -45.14734 | 2025-12-10 05:57:00 | AQUA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| cba0bf5d-7e9b-367e-96cf-73c664c0d95b | -2.82017 | -45.27034 | 2025-12-10 05:57:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5fcc241a-a427-3a76-b36e-c2aa531e9403 | -5.16982 | -43.11476 | 2025-12-10 05:59:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 5b2fc359-41f0-3e7d-b41e-e1269586cb25 | -7.05332 | -45.0482 | 2025-12-10 05:59:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60eb0700-5f0e-30f9-9632-af8d95cd9457 | -5.32741 | -43.55478 | 2025-12-10 05:59:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 13c5d13d-e93a-36de-8ee4-a3ab14b422dc | -6.90145 | -42.83331 | 2025-12-10 05:59:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c1eb228e-6aaf-3d33-95e4-702c0518eabd | -5.34476 | -43.43782 | 2025-12-10 05:59:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 46355dc6-9ec3-3f63-8b00-6854035d1044 | -5.33629 | -43.55604 | 2025-12-10 05:59:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b6416074-f1e9-3534-87af-281b1909e569 | -9.81705 | -47.92675 | 2025-12-10 05:59:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 7ee09f5e-e834-3d18-b77a-42887b7c3f91 | -9.82648 | -47.92824 | 2025-12-10 05:59:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 71bec3f3-89a2-3e69-a9fe-2e8dcd8bd937 | -8.67423 | -44.21887 | 2025-12-10 05:59:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2b76737c-feca-3f89-83ed-df4f25471ca0 | -5.33495 | -43.56503 | 2025-12-10 05:59:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ccaaaf4e-eed1-3df5-8cf9-fc85c238b12e | -9.81022 | -47.93054 | 2025-12-10 05:59:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 86572bfe-0ded-32e5-9693-380312d2bf76 | -5.32608 | -43.56377 | 2025-12-10 05:59:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 60662868-80c3-3552-9f86-7b6e95c0aac0 | -9.81182 | -47.9203 | 2025-12-10 05:59:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 032a0647-37dc-39d7-989d-855686d53e74 | 3.01827 | -60.1466 | 2025-12-10 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4ded9f0-0ff1-322a-9763-036ee8bb5a02 | 3.01901 | -60.1511 | 2025-12-10 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c63ec2a4-0251-339f-83ef-857ecd25d8c8 | -2.5331 | -45.2943 | 2025-12-10 07:30:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 22a14894-e168-31ce-9d7f-d0ff507e5d58 | -3.8401 | -44.3346 | 2025-12-10 07:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| ae6b9c8a-2558-3210-bae9-c3df7c46991c | -3.8215 | -44.3355 | 2025-12-10 07:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| b6ebc6e6-b24e-347f-aa2b-22679f7306a3 | -4.0129 | -42.10091 | 2025-12-10 11:55:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| d4a18d5b-6857-33c6-8158-310b55015793 | -3.43175 | -41.64925 | 2025-12-10 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 616faa9e-c22a-3a7a-915b-9ef34a3f31aa | -2.98249 | -43.87921 | 2025-12-10 11:55:00 | TERRA_M-M | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0e2b60f7-c3d6-3840-bbe1-00f28853753f | -3.74529 | -42.5546 | 2025-12-10 11:55:00 | TERRA_M-M | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 561c7d84-0f1f-3b7f-9e30-ab0365776eb4 | -2.90226 | -42.26562 | 2025-12-10 11:55:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 927611d6-5d84-3633-b99e-576e3ac0cf21 | -3.39065 | -41.9987 | 2025-12-10 11:55:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 47.4 |
| 8a7d3020-95d8-31cf-af4e-a0d06811abf9 | -4.01163 | -42.10979 | 2025-12-10 11:55:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 36.8 |
| 39f4b4cd-c985-3cc8-bca9-0501c0ba7098 | -3.41798 | -41.4257 | 2025-12-10 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| b4dd2bc2-df24-3810-a9fc-788305aa713c | -3.24471 | -43.59451 | 2025-12-10 11:55:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6a191160-051c-3589-bce5-95cb7b6b44c2 | -2.901 | -42.27439 | 2025-12-10 11:55:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 173b27df-e428-3ba2-bbd6-1c4fadefe3ee | -3.52814 | -41.49313 | 2025-12-10 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 684465ae-e580-37d6-8f11-5e5fd017446f | -3.95821 | -41.51821 | 2025-12-10 11:55:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| ca94c00c-e718-3a01-8660-3ad3a08e8eba | -3.46263 | -42.01464 | 2025-12-10 11:55:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 7980ad96-f536-379e-a376-96d9d3692b21 | -3.76159 | -42.12604 | 2025-12-10 11:55:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7f66d315-e0d1-3597-8981-95cbd33b4ab9 | -3.16964 | -42.18968 | 2025-12-10 11:55:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 85e9cc61-a779-351a-9df6-6eea2cd711ab | -3.76033 | -42.13489 | 2025-12-10 11:55:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| c973c00a-b1ce-392e-8de0-a3fef200b01a | -2.91995 | -42.58065 | 2025-12-10 11:55:00 | TERRA_M-M | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 617f7e95-82f7-379d-a5a4-650accc23d66 | -3.4251 | -40.47371 | 2025-12-10 11:55:00 | TERRA_M-M | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 925c8a3f-2e30-3ed3-ae4e-5a2d5fd77c81 | -3.38938 | -42.00757 | 2025-12-10 11:55:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 129.8 |
| de7040f7-c0a3-3528-92cd-7bb50cbac12f | -3.42282 | -41.64802 | 2025-12-10 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1d6f672a-e706-32aa-9428-01e65057fc34 | -3.44067 | -41.65049 | 2025-12-10 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a62d7f8f-b6fd-3ed1-a4ed-c8a6d40812b4 | -3.77441 | -42.6187 | 2025-12-10 11:55:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 58f4f0da-7d63-3679-81ba-73e17be67744 | -4.00404 | -42.09968 | 2025-12-10 11:55:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| dbe52b92-5ce3-3f80-8e76-607c53383470 | -3.84539 | -38.9486 | 2025-12-10 11:55:00 | TERRA_M-M | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 7baf5ff8-9b78-301a-bd39-3dd742065cdf | -3.99639 | -43.25021 | 2025-12-10 11:55:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0b3e25dd-2554-351c-a421-b58697bc8330 | -1.76065 | -45.51354 | 2025-12-10 11:55:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 555fbc08-1921-3d9a-aaef-949301d8416e | -3.17973 | -42.18211 | 2025-12-10 11:55:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| db928496-7e4a-3815-93b8-0be3cd407c90 | -3.4133 | -42.04395 | 2025-12-10 11:55:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 236db4bb-a8d5-3648-92f0-7227e185b5fe | -3.43045 | -41.65826 | 2025-12-10 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 28.9 |
| dadc4b75-cc9a-3a75-b9b9-7c27fb0ffd4b | -3.51156 | -41.41658 | 2025-12-10 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 20fa931f-452f-308e-98ec-1b2a4c5ee29e | -3.74404 | -42.56336 | 2025-12-10 11:55:00 | TERRA_M-M | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 79e6904c-ba07-3921-b4a6-1a1582ea8b31 | -2.33046 | -45.54545 | 2025-12-10 11:55:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f2b22725-dfd2-35e1-aee4-a16e2e8d7c7c | -4.00277 | -42.10857 | 2025-12-10 11:55:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| e20a6896-67da-3d67-af1b-d4d9638c63f0 | -3.39958 | -41.93655 | 2025-12-10 11:55:00 | TERRA_M-M | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b9637205-325f-31cf-9b51-e8e9fcc80599 | -3.42153 | -41.65703 | 2025-12-10 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 3c32eb01-9515-3320-8f30-93bd212fbdc1 | -3.51025 | -41.42579 | 2025-12-10 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 35b25837-c4ff-33ab-aeff-56e9c14e3763 | -3.28413 | -41.26337 | 2025-12-10 11:55:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 20da8bae-586e-3abf-8347-eb2043ade657 | -3.75148 | -42.13367 | 2025-12-10 11:55:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| a97e79f4-bea3-35c7-898a-e2e095eb0d05 | -3.602 | -39.67266 | 2025-12-10 11:55:00 | TERRA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 58c55594-21f4-3dda-87dc-c59251c70fe0 | -3.40052 | -44.17753 | 2025-12-10 11:55:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| fd612ccd-5d99-3d43-8309-66e92e9eee31 | -1.43223 | -45.66118 | 2025-12-10 11:55:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 16e6e518-ed63-3c16-9fae-2d2052e298e0 | -6.61553 | -37.3099 | 2025-12-10 11:57:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 34.8 |
| 187c8686-b2db-381b-8622-93dd14b6e8db | -9.65604 | -35.81072 | 2025-12-10 11:57:00 | TERRA_M-M | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 57.0 |
| 0fdbab1b-65c0-361b-99ed-3cacca066aa5 | -6.68638 | -41.25896 | 2025-12-10 11:57:00 | TERRA_M-M | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c82fc2d8-adae-30b0-9417-44382fea17ab | -6.23584 | -37.99432 | 2025-12-10 11:57:00 | TERRA_M-M | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 20.2 |


[Clique aqui para ver as próximas entradas](README16.md)
