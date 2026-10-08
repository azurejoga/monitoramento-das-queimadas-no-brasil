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

## Dados Diários - Página 372

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d830f97-fe53-35e7-99dd-c563deef20d2 | -3.16257 | -50.43618 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d67d2e65-f61b-3af4-bc8e-53d0bff97561 | -2.70991 | -57.47144 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c967bfd3-402e-3927-951a-bed417757d63 | -2.9986 | -43.28048 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 325ed9fb-9264-3987-8eb2-639aaefad729 | -3.0015 | -57.75169 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 046fd172-63a0-3a23-b9b3-4d7b1567cc0c | -4.75165 | -40.92347 | 2026-10-08 16:39:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4a0ce084-2a96-3371-ab23-e08d81948021 | -5.48597 | -41.21354 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| dbca5ed3-1990-3c84-901b-c4a1a22d2018 | -3.44544 | -45.09214 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2c9a274a-1e94-365f-8751-abd12ec07aec | -2.89162 | -59.20114 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ee3239cb-76ca-3a86-a9bc-3b17f3ebdfa3 | -3.30026 | -53.69292 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 926fbcdb-0a24-3b34-bf11-3d7af95a219b | -6.13925 | -51.66343 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f805587f-4045-36a1-a376-1b1589454030 | -3.55572 | -44.56089 | 2026-10-08 16:39:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 766d7675-0300-314d-a326-fd25f7114692 | -3.22256 | -53.96684 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 57224bef-69f1-3214-a3ca-d1b64aaff4c0 | -3.859 | -51.93497 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fdd857e8-dea7-350f-ad69-a7b1339b96cc | -2.81412 | -49.11607 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb329234-2bdb-38dc-966d-4f5a940708d9 | -3.31016 | -53.86044 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 39f2191b-54a1-3c89-96f3-4d62b97e8309 | -3.17218 | -48.69923 | 2026-10-08 16:39:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 38c2cae8-2de1-3f4b-a89d-443426507a42 | -5.48197 | -41.21424 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 17410f4f-fc96-3977-aabe-119680f77c3e | -3.01057 | -54.08933 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| b31ef784-e7e4-3fbb-b8fa-d2be61c9d5c2 | -3.78862 | -41.67529 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| b29ce906-e934-3172-ab4c-5d0f277bf4bc | -2.51674 | -57.24701 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 11f0a5f0-f237-310a-914f-dc7caceef484 | -6.98132 | -56.47755 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ebbef376-0db0-3ade-bb73-b7be75db34a8 | -2.08467 | -46.57482 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 0f5006c7-7fc6-3e1f-b567-47e5107647b4 | -3.85289 | -44.12696 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| e988cf6c-115b-3373-a2b7-090ee84a0a2c | -2.93163 | -54.11897 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 93af1a30-871b-394e-9b65-ff6dbdef4de8 | -4.55165 | -54.97015 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 160d423c-51fa-3667-813b-d1f04c809a79 | -3.85578 | -44.1226 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| d7ebb8a2-6a57-30fb-9b02-57893378abf2 | -5.51642 | -45.62345 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 86fb19cd-79b4-3564-9591-27c77eb19e4a | -6.74324 | -55.14713 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 2b03a417-5a4a-3daf-898d-5442a3121e01 | -4.70543 | -41.04743 | 2026-10-08 16:39:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 09bcc535-c443-3cb6-9081-72d6ca24f49e | -6.85753 | -55.78355 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e1e24c89-3f88-3e9c-b54d-aa1333990eb6 | -7.22644 | -55.09733 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 387346c9-7048-3089-8863-537ef02e4161 | -5.69813 | -53.47372 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 10006446-3b43-3915-bac6-b53477a26048 | -3.57293 | -54.49013 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 338c486c-8a9e-3228-836a-deff841e9f52 | -4.36527 | -40.40772 | 2026-10-08 16:39:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b65008a2-c068-30a7-9703-00a23e47beac | -2.58417 | -56.17132 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| fa12bb5b-1aed-37b9-9eee-32fe2a041ee3 | -3.42803 | -45.04676 | 2026-10-08 16:39:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 4839db02-bc85-3daf-b230-b009c2dcfa84 | -4.35713 | -55.22884 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 690d30fe-fc99-315b-84c5-5e8d9a48919f | -3.01249 | -54.7456 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3de8545d-3579-300c-89e6-ce880ab42a33 | -2.41651 | -56.8546 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| ecaa8610-9af7-3261-ab8a-60bf371531af | -2.50424 | -58.07343 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3d78bb23-cfed-3c45-bf31-61c677820a98 | -2.57517 | -56.17289 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| fdae4cb5-9962-3b26-b1ba-3d2e2dacaa34 | -2.45817 | -56.37801 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5e2e28e0-5089-3b7c-a20a-033c6cba626d | -3.06008 | -53.93378 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| dd22ed0e-5981-3b51-9017-e0f7c925a1ea | -3.49544 | -39.49773 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0be22d01-4985-3e6e-be08-ef0dfd2d3f6d | -5.09223 | -46.22124 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.0 |
| d2a28f0c-c137-3ca4-97e6-a017323b5c65 | -3.0978 | -53.94671 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 2231ab76-7e43-3cac-b121-5375eceed6f2 | -1.51764 | -54.51735 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2d07eb7a-c23c-3bda-b720-5ff1b921e6b2 | -1.3843 | -55.1932 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 595cd67b-06d2-3482-a237-faee6435550f | -3.89858 | -44.13559 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 3277f689-9a3c-383d-9d0f-08714db88364 | -4.33657 | -43.79382 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 9234bb89-1fbf-3dd0-b9c8-d2a2d62b51d3 | -2.09407 | -46.56987 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f5316016-882b-3c11-8613-73c6c3bf9e10 | -6.38979 | -53.28317 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 18ea46b9-451c-351b-860b-737cab2f4927 | -6.23531 | -52.84847 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 42627cf2-1cb1-3d46-857d-ee5f94d28a06 | -6.24054 | -52.85246 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 00591eee-0c82-3e0f-b194-bea3d63d1701 | -2.03677 | -54.48788 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e5c5da59-cb66-3868-a088-f522d1edfe13 | -7.33584 | -55.09071 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c5d30b23-6e9a-333c-96a4-e67637d8257c | -2.82406 | -57.60413 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| adb64170-e338-3518-80d6-3935c39a3317 | -3.28312 | -53.70535 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 9a5dd9db-6db3-3938-a6bc-3ed82a0775ef | -4.09009 | -44.11833 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| f3bebd58-a589-360c-8550-eab1b778588d | -6.04217 | -53.48335 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 6d562c81-220d-30ab-a50f-13c9983d41fc | -3.0068 | -51.11871 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| efb288e3-e5ac-3374-a830-2e440377de98 | -3.89935 | -55.64811 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 29d67f7e-b251-3152-bf68-d291461f276a | -6.15969 | -52.63943 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4cc9702b-d5b5-3f9a-81ce-09e7a6b6f7d2 | -5.30022 | -45.71851 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f4f5c1be-6437-338a-ba3b-b16733aaa679 | -2.89306 | -54.91026 | 2026-10-08 16:39:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 624b64ea-37e6-3c68-a3cc-901a966607b4 | -2.28191 | -56.66911 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 77213406-012e-3a9e-8a31-37c6baedee3d | -4.6634 | -56.2121 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 358cba59-dd95-38cb-a871-a5fed0d475dc | -3.17575 | -50.44784 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9c2b97b8-4bc4-374c-9279-a8152e25ed25 | -6.73993 | -55.12262 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 106ee7ef-e700-3578-801e-05270df3a8bc | -3.03574 | -54.096 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0cd05585-75d9-3da0-87ae-381737717ee3 | -2.96216 | -42.66793 | 2026-10-08 16:39:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2badb5b7-4e5e-37ed-890a-5a25bbda6770 | -6.95509 | -59.52134 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| dfd30909-4a05-306f-9224-1abc84e003a6 | -6.12165 | -51.96038 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e1286bc4-363d-3c5e-abfe-a1e39ce7dcab | -1.42369 | -52.84335 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f0e7621f-b535-38b6-bb16-41e0f9ee42c8 | 0.38883 | -51.16551 | 2026-10-08 16:39:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c6024d66-acc6-3451-9211-391710ffb532 | -7.2422 | -55.13347 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 41b8e720-5d63-3c4f-baf0-85ab796ae7d6 | -3.01494 | -54.1198 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d7b7832b-8680-3dc9-8f0e-5473662a4235 | -4.16037 | -43.19681 | 2026-10-08 16:39:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 07f68edd-cea7-30e8-987d-50693d3cb095 | -1.05334 | -53.59062 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e18db1fd-d033-3ccd-8ad3-46134c821822 | -5.1583 | -41.1709 | 2026-10-08 16:39:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| df2482ac-6c12-3e45-9317-a7301900ce31 | -5.92525 | -51.82808 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| c891826c-f0e4-3e1a-89a3-c81846324396 | -5.73698 | -45.15965 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7e29489c-8c12-390f-8abd-16c9f2cadc44 | -2.51312 | -56.33007 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7acb0c1-5a43-3cdb-8486-c2499fc389bb | -6.07155 | -44.64803 | 2026-10-08 16:39:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 3764e9fe-3bdf-3b14-9470-5346bbe019da | -4.16818 | -42.16422 | 2026-10-08 16:39:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 3edd24b5-b5ae-3c4b-a91b-bb4ae0f8ecbf | -3.17904 | -58.62765 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 08c1f7fd-a8d5-3c8b-bd46-daefb577c41d | -3.01012 | -54.06097 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 0bc447ce-337a-3c21-aacb-8a79b1c202bd | -3.82718 | -59.41027 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 860850ad-d75a-3a33-8f50-603c569ca00d | -3.0028 | -54.10856 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e5e8c88d-6eef-3a4b-bde7-b99357c5a3e4 | -5.87349 | -45.96011 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 4cc70476-7c50-3a6c-ada4-e04fd99b0a08 | -3.78352 | -41.66896 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| cdb609ab-786a-3526-b0f9-996089de9bab | -3.35623 | -43.0078 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1f48fca0-af8f-3085-a7fd-1886c221c81f | -2.49373 | -56.15978 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4725080e-aca9-3d22-bef6-d17793f3436a | -4.35627 | -55.21916 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 024a7ffb-1f8a-34c8-9248-05a55a40064b | -7.00218 | -59.10775 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 92d9544d-9ba2-3d98-af09-e500f3eb1b76 | -3.00312 | -54.04663 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 5f9b99d4-ba26-39e5-9321-346ea5b47f7f | -1.74662 | -57.18306 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 39dd7533-716f-337c-8c5e-d2cb8ea78341 | -3.44374 | -56.93334 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b22c9559-14c2-3b5b-9f21-2a10d65de386 | -7.21015 | -55.19451 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 22d0da08-8edb-3e94-bd28-3cccf5166417 | -6.04347 | -49.66018 | 2026-10-08 16:39:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |


[Clique aqui para ver as próximas entradas](README373.md)
