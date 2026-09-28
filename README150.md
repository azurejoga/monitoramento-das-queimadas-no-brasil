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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 000bab97-9ed3-3778-a293-fdc188681c08 | -7.68895 | -54.7477 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| bbf7a9ee-6b7b-39db-8baf-32ef45dac1eb | -10.8836 | -61.40396 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| c4417acf-816c-3a7a-aada-5777739e9a0c | -11.87535 | -50.89567 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 44f058bf-a03e-38da-9fa2-224de7477e1b | -9.06915 | -51.40793 | 2026-09-28 17:09:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 324c9591-d706-3de4-98b4-0202ee7fe214 | -8.67086 | -45.37516 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6cb9f998-ddbe-36da-8296-69cd73cf500f | -11.03526 | -54.1344 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ccdc807c-d89c-3298-b653-81f607777cf9 | -9.32168 | -46.55691 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0671117b-4d5f-3b6c-bc52-9f8dd62e824d | -8.29545 | -54.71115 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 163.9 |
| cf5bb3b4-c53d-3567-a38f-9069ec4d6379 | -10.00941 | -50.11688 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5a4c3f28-6f78-341c-902d-4da75f275afd | -11.86534 | -47.08644 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 20ccba2b-b437-3ced-aaa2-2ab2a9043c90 | -11.2029 | -44.81504 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4316cdf8-603d-3ce2-863d-465e025e409b | -8.70495 | -46.83602 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6f11882f-5043-3ac7-aea8-301365d97a56 | -10.80357 | -57.19922 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 92f3f891-e5a6-3e34-9c66-0d9052e986e5 | -11.13161 | -50.07144 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| b74352e1-f816-3f59-9f74-36c1ef809c48 | -6.09393 | -53.51195 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0b2e9cfc-3e95-375e-90aa-138a94a163bf | -7.38016 | -64.35155 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c0a58bd8-0073-3f4f-8134-b6cd5abdf20d | -11.85147 | -50.88652 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e69aa900-44fb-31e5-9dee-506bc6074f0c | -5.73801 | -43.27709 | 2026-09-28 17:09:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| d4c99aed-8fe5-3513-8a3f-13eb38231c62 | -12.13655 | -50.33714 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| a3dbd2ed-3700-38c2-b645-1d989e3d7843 | -9.84555 | -45.21267 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ccfd379c-4249-34f0-b953-753488a36a25 | -9.43747 | -46.54025 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 45f93044-70ac-3bb7-9e08-f8a45ab74dfc | -10.92804 | -50.70826 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 72aa49e2-6f7e-3c1b-821b-7b7709d3ee32 | -11.84017 | -47.78294 | 2026-09-28 17:09:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 9f879698-cc49-303d-9f72-a9d977e014ca | -10.92062 | -50.70952 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 821340c0-2e72-3635-ae9a-63405d9a88af | -10.20134 | -49.98693 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 61b04faa-dc83-33d8-a0eb-fb2875992f76 | -11.13398 | -51.17972 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 7be54691-9963-3ab9-966e-5dd22a171ecf | -7.70297 | -44.92263 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 511438f7-da9b-32b8-b0af-9330b7329a0a | -9.97707 | -45.34279 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a14a2d43-0ecd-3b4f-b7c3-83f4a7e8e23b | -10.81944 | -57.18465 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b50d4b51-c59b-3bf6-83a5-f89a363c580b | -11.37939 | -47.43343 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 226771b0-1743-35be-b1dc-513e0deb230d | -9.74308 | -53.8686 | 2026-09-28 17:09:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c568f7b4-a69e-3fda-b2d7-f5ad63f058bb | -7.36375 | -45.40902 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 33042084-fe88-300c-9410-e3f5ff056735 | -11.30412 | -58.3368 | 2026-09-28 17:09:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6c47c062-df60-3648-b7fa-7206fbb503f3 | -8.19326 | -54.81994 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 66794bed-1ebb-3b1e-a76a-db504103970d | -10.80121 | -57.20771 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 02f59d68-acab-3633-8af7-089920f1dc94 | -10.82224 | -42.74903 | 2026-09-28 17:09:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 7e566062-f48a-3548-97f7-5545a73bba4d | -12.80972 | -54.00455 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 774697d2-4529-3840-8046-62f21c0967f1 | -11.17212 | -54.00808 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1402e88b-12e7-3788-a28c-88bfcebee682 | -10.20831 | -49.98055 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 8b1cc21a-5db6-3f0c-b975-7545235520a2 | -10.10721 | -43.95045 | 2026-09-28 17:09:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7aecd066-f5b8-394d-97e7-5d2baf31a202 | -9.29538 | -46.44127 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9b1bdf81-535a-397f-a18b-8827d6d80109 | -7.67956 | -54.75271 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9473bd9b-c8a2-3b36-b952-5dba84e8e9be | -5.2551 | -44.93662 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4cf38810-8088-3b2a-98c1-087e46e72c34 | -10.70735 | -44.42501 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| edfab9cb-960a-3cc5-a683-b1c174a2179a | -11.17657 | -44.79435 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 455a8cb2-d582-371f-8ddc-c892cb8a8e3c | -7.27052 | -45.33744 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 85a7f0ec-4dc1-30c2-b1cf-bf2394946261 | -9.16862 | -60.785 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| eac0021e-922f-3a50-be90-155532ec712f | -6.13434 | -53.05166 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cc87c158-7712-3f61-9a2d-8ed51abe3fd4 | -7.43281 | -55.63295 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c03cde0b-f200-3d7d-b25d-2f5f1edbc3bd | -8.65251 | -45.34206 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5b76e922-340b-33ce-a6bc-2bc535b9ee3f | -10.61576 | -53.99384 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f83bf534-eed4-3efe-855c-c872803e3737 | -11.56209 | -47.39583 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 99268e3a-950e-37a4-954e-17700ee8b301 | -9.54023 | -56.16038 | 2026-09-28 17:09:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7030215c-d9c3-3df5-bec8-530d73fe6cb3 | -11.44993 | -44.9165 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2843717c-6395-3348-88ad-1d8bc2f59018 | -11.48009 | -49.75551 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| eca2ff35-54c7-32aa-b823-389d5d72558e | -9.7403 | -53.87267 | 2026-09-28 17:09:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 71d223e2-8d59-3ea7-90af-ac828e394d4b | -7.38577 | -47.0145 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| acdf78ae-964e-3584-9df7-ebbce36b3e33 | -9.02652 | -61.03637 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cbcd4c45-5845-3a5f-b251-23a5af7930cb | -8.9664 | -50.97991 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3326a6bc-9be0-3b45-87ac-bcd1e093b5fb | -9.78132 | -45.8175 | 2026-09-28 17:09:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 28c22841-d7ba-3510-bab9-b11a5edbe824 | -12.1388 | -50.35078 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5c99dc1c-a419-3b58-8e23-73bdb9cae30c | -11.38508 | -45.40402 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 596c5e4b-efe5-35fe-ba9f-e3ac73e6ed2e | -10.24885 | -44.6159 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0cda9ca1-2031-3afb-90d4-0f5f4e1fa879 | -9.32905 | -45.37603 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 45fb6bc5-7a57-367a-ad50-a8c691c936cb | -10.46641 | -45.0598 | 2026-09-28 17:09:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 844f8e2d-65a1-3fbc-b732-c9ab4e04872f | -9.77098 | -44.8334 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 06db568b-7956-3643-bccf-92c8bb028932 | -12.78595 | -54.02636 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 3d880b97-feb2-3e6f-a1aa-6ba5b3cf28c3 | -10.25791 | -44.60263 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c43fba2e-65f0-319a-a167-ff833a8a443a | -9.51234 | -46.35659 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c21da393-2e8d-39c8-9a28-7d2270c95c44 | -11.08413 | -46.08318 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e3298bb6-d4c5-3298-8b5c-7b0df9c036e8 | -12.15352 | -50.38247 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| e6d70e6f-c781-3767-843a-0f8a05d1c288 | -7.27896 | -46.93424 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ffcc6c3a-e7c1-38a4-96fc-e5d1f2761e2f | -10.20385 | -50.00197 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a0637c0e-409e-3d03-983b-5f519ba50124 | -11.08359 | -46.08028 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b1459669-3968-374d-acfd-bf564aaf1ecc | -9.97305 | -50.1384 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 29c469a9-cf06-3b6e-84dd-f342eb9c837a | -8.63871 | -45.35931 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 31c81f3f-48b1-35f1-b621-ee821d48c0d8 | -11.4559 | -44.91881 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 60fff76d-6d43-3b37-81d2-5944b796c1c4 | -8.01774 | -44.97214 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 1b2c6157-3292-3f31-b385-3a1f6faff101 | -6.91019 | -47.00428 | 2026-09-28 17:09:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 974c419d-4206-3f83-b0f2-5314818090b5 | -7.01724 | -45.82989 | 2026-09-28 17:09:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26349f3a-62c6-34f0-bf66-a8913ea69113 | -9.32709 | -46.56137 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3be619ba-0289-39f1-8ca9-119c81ded3ae | -11.87625 | -47.09443 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 91908a70-c0a9-31aa-afaa-4e0cd646448a | -9.14102 | -45.60524 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 491b0a6c-bff1-3b24-a389-fd568fc0778b | -9.40538 | -46.39265 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4eca8207-347c-3ddb-b614-13f8a111caed | -10.22112 | -50.0093 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 23faf098-a035-3c7e-a197-6bcc7c197c94 | -8.97563 | -44.15311 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 75227735-69bb-3f3b-9d05-3e82abd1e837 | -10.70287 | -48.7571 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 192aaff4-365c-34e2-a8f0-7cb08fdee632 | -7.38599 | -42.12079 | 2026-09-28 17:09:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 407e4b29-8390-391d-925b-bb4e597e6dd4 | -9.37033 | -49.17854 | 2026-09-28 17:09:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 105d612f-38d9-336a-8b9b-112d048958b4 | -12.06968 | -48.53281 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| d9143447-c57a-3b71-89d1-5170f4db0110 | -10.26387 | -44.61085 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 477f41c4-5409-3aa6-b898-fe9c22db34a9 | -7.76347 | -54.78862 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9860594b-5f84-3b8b-83ec-956ebc057f99 | -8.73391 | -44.91512 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| cd7fa434-f212-3bd9-8810-771940099661 | -8.7268 | -44.90797 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0844f4f4-a3c5-3944-8121-02e0faa23cee | -8.02644 | -42.85827 | 2026-09-28 17:09:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 9dd8c4d0-1306-37ba-aee1-207f53298453 | -6.16234 | -52.90337 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c90a5dba-1279-3c4c-bf53-ad7676bab885 | -12.37997 | -50.22964 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 202baec8-3104-3354-b531-faae88474834 | -12.29302 | -50.35933 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| d636d114-afff-35a7-bdcb-fa4d7a7d97ec | -9.04702 | -61.02508 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c7cc76f5-2e09-302c-9513-def9a35b572d | -9.40539 | -46.39018 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |


[Clique aqui para ver as próximas entradas](README151.md)
