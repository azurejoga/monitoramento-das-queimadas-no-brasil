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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f2f825d-b474-36e5-b3fc-c0ea14da1509 | -10.63122 | -46.3194 | 2026-09-28 17:09:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 20aca105-fd9f-3618-9e35-9b01b5b49caa | -7.34263 | -42.07726 | 2026-09-28 17:09:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| a7a6945c-755c-3e12-a08e-31587bd3b7d3 | -10.22336 | -49.99861 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ee31398-44f6-31cf-abaf-0d9c78973d18 | -7.25028 | -43.35011 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 10dc9a6f-e0b5-3213-a572-98c75c673221 | -8.38233 | -46.52593 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8f70d93f-57af-3b28-b9de-3ebed519df54 | -9.69265 | -58.12193 | 2026-09-28 17:09:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a2e404fe-c797-37fc-b3a5-924e533868c7 | -7.67796 | -54.74228 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ba74fd49-a373-3935-b228-e8116e376ea0 | -9.77513 | -44.82511 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 517e8548-cf7a-3c27-ad21-306d19a26c7c | -7.68454 | -54.85148 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| b799cb9f-02a3-3612-8d19-bfc9589ad99a | -11.21429 | -44.78646 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 534af98a-528d-3ba6-ac45-bff196529661 | -5.85137 | -53.82739 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c78303d-9bbe-35be-9912-656356b8552d | -6.30546 | -43.60882 | 2026-09-28 17:09:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 2340b3c9-9c30-3924-8331-219a3ac3b395 | -9.85544 | -44.95041 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 855ec7bb-7509-3b64-bb03-b964f5a1f065 | -7.599 | -46.66719 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| de7020c2-dce4-3328-9975-3f39657c4128 | -8.5268 | -45.84998 | 2026-09-28 17:09:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9b77a3ff-9d12-39f6-ab97-4b16f631cc6f | -8.67216 | -45.38218 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 2e317996-9ba7-3a40-8ef9-fe8fe68c3aaf | -9.32664 | -45.36253 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 78e4ff8e-fb5f-3fac-a819-4abad73c3719 | -11.53688 | -47.39293 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 99081c86-7a85-3644-b9f1-64d9ce4ca405 | -10.97429 | -49.67195 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 9dd7bb2e-184b-3146-aaba-9f2f155876e1 | -9.78553 | -44.81949 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d76c20e8-83f0-3063-9618-242c22bb9e6e | -6.19393 | -53.2285 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4bd19867-f838-372d-b9a1-b08af43468b1 | -5.89012 | -49.98339 | 2026-09-28 17:09:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 1f7b55bc-27c0-3779-b258-45036f4dd896 | -10.80826 | -57.2067 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f58caba3-74be-3625-a57f-499cd5969b76 | -11.76039 | -50.76666 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 91bd4b1c-9e36-3b4f-bc27-51fc317779bc | -12.81025 | -54.00808 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5da96b7c-9f39-3889-9073-753eff96534b | -7.68884 | -54.76907 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| cdd2a5ba-0c5d-3c18-8db2-0def529f72fe | -10.72179 | -49.02752 | 2026-09-28 17:09:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36dce84b-e3e4-38db-a360-4db97fa73c8c | -9.67651 | -45.57193 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 1661b3dc-2718-39f9-a262-528a913003c5 | -9.43853 | -46.54608 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 8599d0f9-06ed-3fba-b307-6e24d90c538b | -9.78133 | -46.44477 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7858c18e-3077-3c5b-b46f-e5785efc2ddf | -10.26527 | -44.61818 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| ab307d14-1cdd-3d42-8eb1-144417668bff | -8.96566 | -50.97533 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 01acace0-0fbc-3b56-b9f9-b4f85d276a9f | -9.77657 | -44.86152 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1ae08056-49b9-3649-862f-92b588aa95ab | -7.01931 | -44.61839 | 2026-09-28 17:09:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c1fc8985-af77-35e9-9021-3355ee836497 | -9.13686 | -56.55703 | 2026-09-28 17:09:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6204752a-5bea-3b0f-aae3-46421311b808 | -5.72587 | -43.28158 | 2026-09-28 17:09:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d1c563b1-3c9c-36ab-be5f-abd80edf037b | -10.83256 | -60.74296 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e7eb52df-8803-3fc9-bdd2-181a6080ca0e | -6.66512 | -45.40966 | 2026-09-28 17:09:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ef41d9f8-0fcc-3826-8205-aee85b829797 | -11.44927 | -44.91298 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 33680f86-cd19-32d5-a036-b245ef25cae3 | -8.80139 | -54.55169 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d00e38e8-36bb-3b06-b105-8a666818c408 | -7.59275 | -55.70011 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 801dd7d2-c43a-3a14-aaf7-b49da5d7588b | -8.72757 | -44.91214 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1b85827e-1173-309a-a210-8522d38b4b8b | -4.34679 | -43.25719 | 2026-09-28 17:09:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 9e9e384c-8b10-373b-95c1-7f7f21553a85 | -6.31166 | -43.60694 | 2026-09-28 17:09:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| ba71a99c-1576-3a52-935d-2aa1ccb1fd6d | -9.07441 | -46.50193 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2e31bacb-7319-39e7-9814-e5510871ca2d | -5.83946 | -53.84054 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cbf491cd-b3d5-378e-9797-9fcc1e008ae5 | -12.1698 | -59.84208 | 2026-09-28 17:09:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 493db444-66d2-3478-8a2d-4ab589c5686c | -4.9482 | -45.10794 | 2026-09-28 17:09:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 12cd0ada-0e35-3d36-96de-a6c308cbdbc9 | -6.20349 | -52.91306 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 07fdd3ae-0cfc-3462-8a9d-cf54bba85260 | -9.09615 | -49.90518 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0340d3d5-fc4a-38ee-a0a5-efcfc883b465 | -10.8245 | -57.21757 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 60d6fe8c-a005-3ffc-a549-bba3b4805980 | -6.5191 | -54.96616 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 934e7d60-e525-3869-9d07-943a61b42bda | -8.32656 | -44.1657 | 2026-09-28 17:09:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9a9096ba-4100-34e7-9228-57a152d8f74f | -10.82706 | -60.73511 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8da8c616-0463-3abb-8e2f-d6e2ee820460 | -12.78264 | -54.02688 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 8c2b3d27-82c3-3902-9fb9-1beaf8415c37 | -10.86873 | -48.51239 | 2026-09-28 17:09:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 70da437b-8340-3b86-8d6b-020bd4c3c158 | -6.87711 | -55.554 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 73a6b91b-8da5-340f-8529-42a7bb60cf5b | -12.13501 | -57.23931 | 2026-09-28 17:09:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 389e8fe2-32a8-30ee-b748-5855258a1c47 | -7.81924 | -55.13122 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 242f8d0c-c2d7-3451-8fe3-1dc44a4a74d3 | -10.95397 | -61.80083 | 2026-09-28 17:09:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b394687a-d9be-3efc-86cc-bb33879a2046 | -8.17785 | -44.43356 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5dead10f-086e-3271-afe6-60a100e33491 | -6.20928 | -52.90412 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 1919c1a3-40cc-3a71-8938-b8f46f30930b | -10.26957 | -44.6348 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 2e2ef011-e2ea-3b89-9c9e-530da20891ff | -8.28542 | -54.73405 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8c2d5f21-b1c9-31aa-bb7a-a54ad8391f92 | -5.73884 | -43.27902 | 2026-09-28 17:09:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 1d0f51e2-fd63-3a57-a054-835876b40d3d | -11.53607 | -47.38828 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 2e660aa7-4917-3c77-83f5-1e3e2d44effd | -11.18336 | -44.80054 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| ad98fd3a-9c45-3c7d-b683-8efa3cd34b48 | -11.55137 | -47.38817 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d42904ff-d48b-37d0-83c5-748fc5f4c9d8 | -11.18404 | -44.80411 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 36ccf35a-65fa-3761-a448-4388eceac2c5 | -9.74823 | -53.79161 | 2026-09-28 17:09:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d3059d90-965e-3784-ae0b-0f632b3c4cd6 | -9.13121 | -45.60235 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| fa0b008a-28c7-34cf-98ff-be280a733bd6 | -7.59328 | -55.70359 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0b106224-5c96-3f0e-aac7-f5508593cf39 | -9.3271 | -45.38213 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d414acd4-379e-3b9d-8670-2a350e6d2fad | -11.87827 | -50.89076 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 1caa8940-0a2a-3c6c-8861-0f5ca9e08f02 | -11.47148 | -49.75189 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 042b17f1-a3bc-395e-8d86-48fa1f1ec33d | -10.38688 | -46.53049 | 2026-09-28 17:09:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 63676f3a-7a0d-377d-bfec-2d5a7dc79183 | -9.98216 | -45.3518 | 2026-09-28 17:09:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 044093fc-ad37-38fd-9428-44f6b32466fc | -11.16155 | -48.32337 | 2026-09-28 17:09:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f899ff9c-bf5a-3c8f-a11c-2b011bac29a5 | -11.3974 | -45.4203 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 23055640-4aef-3693-89ff-8efabf877b47 | -9.40292 | -46.83729 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 606015ff-fc54-30cd-88ea-2644ec4febff | -11.58966 | -45.46168 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| d8152a5b-22e6-3ac2-9a8b-ef9be268b908 | -9.33134 | -45.37507 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2edf3e5b-987a-32a0-bbbc-64dd1d349547 | -10.97622 | -50.70002 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5b5a2c23-bac1-3680-b103-603dfe163fa5 | -8.83238 | -46.59168 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 37616c59-8222-3d61-80da-2fd289fd0664 | -9.78767 | -45.82294 | 2026-09-28 17:09:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3167366d-0a63-3ba1-9921-74944e2afe2e | -9.14928 | -49.96369 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b737dc13-b024-3ae0-aa48-696197a66da4 | -7.82915 | -55.1297 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 2007fd7b-37e2-3860-8fe6-487a989e27c0 | -10.70622 | -60.7376 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9341ab52-e5ff-3084-9469-28301792edbb | -9.40091 | -46.39416 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 97a5ee18-ed30-3f27-ba9d-92dbb56c2bb2 | -12.14108 | -60.76321 | 2026-09-28 17:09:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 7e35c651-393b-3862-ac29-a933efee47df | -7.38588 | -60.61288 | 2026-09-28 17:09:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d2c6bcd0-7ca8-3e55-bb0e-90771aa744b4 | -9.11271 | -49.90596 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| ef92a2a0-a14a-3e89-b54c-cf188aa1614a | -11.47878 | -46.85661 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 44cae205-3206-35b5-a679-36aff5eb93dc | -8.32736 | -44.17013 | 2026-09-28 17:09:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7fd8c970-cac3-3da8-af46-2eab7d05a547 | -8.27732 | -54.70328 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ccb9a3f3-ddf1-3ef0-8d5b-ce82183fcf35 | -10.70004 | -48.76558 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a54539a0-d2ff-37ef-96f5-d4fb2a697f76 | -10.95239 | -43.88388 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 010df254-cebe-3d6e-8133-386fc3d4f799 | -7.12472 | -47.60617 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| fd18936f-7abc-36f4-99ea-c374ddf19858 | -11.13468 | -51.18395 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 9c7126d7-2b2c-36b4-89dd-ceb0cd3f03ba | -12.7981 | -54.01722 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |


[Clique aqui para ver as próximas entradas](README157.md)
