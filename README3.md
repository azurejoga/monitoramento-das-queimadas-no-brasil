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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b9fba46-6453-36fc-87b7-527aeeb9c71c | -6.8385 | -56.4542 | 2026-08-16 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 89f1f826-404f-3bf8-a4a3-af5d50befe34 | -6.7307 | -58.9405 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ccc28a42-81a3-3100-8a2b-fde9a1a3319e | -12.7972 | -41.5169 | 2026-08-16 00:50:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 040895e8-9c84-3ddc-9c92-18681e0060cb | -6.6377 | -59.0795 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 267.1 |
| 439d71bf-2a6f-3971-a771-6859941be798 | -6.6014 | -58.9844 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 43042593-24c9-324e-b4ef-e96bf972e5a4 | -6.82 | -56.4551 | 2026-08-16 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 305a0b2f-2364-3be9-b9ad-ddfdd20c618d | -6.8387 | -56.4344 | 2026-08-16 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 3ad0049c-7d16-34e0-b7b8-d6362c795002 | -14.3919 | -51.9081 | 2026-08-16 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 81467d38-74f1-396f-a94b-0c6f1103cedf | -6.0923 | -57.7238 | 2026-08-16 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d6227739-0b98-335a-9453-5cc79f6f2604 | -6.8597 | -58.9738 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 7d20f899-68e4-38af-b15e-0ae8da43d8e0 | -6.6938 | -58.942 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 19b35cd8-9da7-3c2d-906b-7e6879d83b70 | -8.9038 | -60.5962 | 2026-08-16 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5334650f-81a1-33d1-a3f2-fbc24ebf03f5 | -12.8166 | -41.5133 | 2026-08-16 00:50:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 79.5 |
| c4bab7f7-919c-3b4b-8617-7bdee64a6224 | -6.6194 | -59.0609 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 148.8 |
| d908b14c-cb2b-3a18-ab52-d1feefc9ebaf | -14.0803 | -58.7433 | 2026-08-16 00:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 29709dc1-8054-3c91-b1e1-6b29e3798d89 | -14.3923 | -51.8867 | 2026-08-16 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 1ada962c-b78b-38b4-94ad-dbf2bc7f5a22 | -6.6378 | -59.0602 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 234678a1-b595-33c7-89c3-9216e9d6b437 | -6.6937 | -58.9613 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| f63743d1-03c7-354b-99c1-e0e6f8e227a0 | -6.8202 | -56.4353 | 2026-08-16 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5e1c67e8-8313-31a7-82d1-68bc46b3f97b | -8.9039 | -60.5769 | 2026-08-16 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 2e0a13f3-aacc-3e7d-bd1d-8a12dfa141a8 | -6.7123 | -58.9412 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 196.6 |
| 93bc9a13-63be-3537-aadc-80fd221ed9ee | -6.8596 | -58.9931 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ba0a3af8-ebe1-3b04-8135-8faf0c77d95d | -6.8412 | -58.9746 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f9514abe-9c80-3805-81b6-8f7d4b705887 | -13.8034 | -53.7911 | 2026-08-16 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 1a9fd4a6-acdd-3765-bf4c-15c7a75fc063 | -6.1108 | -57.7035 | 2026-08-16 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| c99e69d1-66c9-3be9-a2ae-ce28a6707f04 | -8.9041 | -60.5577 | 2026-08-16 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| abd5b4ac-0599-37bd-a039-931d00fd59ac | -6.1107 | -57.723 | 2026-08-16 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| b21a96db-c737-34d0-bdfc-51c247ca821b | -6.6193 | -59.0802 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 211.9 |
| 7e21b6e8-5d12-3725-8151-3d4b1df53321 | -6.6198 | -58.9836 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 4eb590d6-7ebb-323a-bb6d-dfc3c9948ecb | -6.7124 | -58.9219 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| da3a8f33-43af-3e1b-bcf1-9681280bee5b | -6.6937 | -58.9613 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 7e2c298e-b27d-3a20-89ee-2d43be57f045 | -6.6378 | -59.0602 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 164.4 |
| 8881a594-7f3d-3c0f-9ccd-fb33d683558c | -14.2568 | -53.0679 | 2026-08-16 01:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 2eecbf07-b891-3d35-9074-14fe58adf01f | -6.6194 | -59.0609 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 55375644-db0f-3c72-afe8-318cc9e0bd21 | -6.6014 | -58.9844 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6b0198a6-1254-31de-8011-d86323f1bdbd | -6.3137 | -43.6178 | 2026-08-16 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 9b8f1fc3-a102-3250-9fb9-52269196c407 | -8.9038 | -60.5962 | 2026-08-16 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 0d1f1383-8d3e-3dba-9e11-a0b90fd5baed | -6.8572 | -56.4335 | 2026-08-16 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 94a70111-67e0-3b9a-acd5-d4387f68c952 | -6.8202 | -56.4353 | 2026-08-16 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 681edc96-79b4-3e3e-95cb-c1a0ab0a64fd | -8.9041 | -60.5577 | 2026-08-16 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 9f1de8b0-c5c4-3461-8d4c-a9819cdb418a | -6.7124 | -58.9219 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0ef320d4-62b6-3c10-9103-f57554a92b95 | -6.1106 | -57.7425 | 2026-08-16 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 991268b1-c3aa-31b7-b02e-b5c4b4a8d1c3 | -6.82 | -56.4551 | 2026-08-16 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| fd9eba52-33ac-3ffd-8d9c-669555cbc17f | -6.7307 | -58.9405 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f4de6859-eae1-3146-96de-a0478c9b5f49 | -6.6193 | -59.0802 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 162.7 |
| 407e5fa3-c876-3f92-839e-4fc245622d56 | -6.1108 | -57.7035 | 2026-08-16 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| ef210bb1-cacf-3313-b37c-478ed0e1d65e | -6.6377 | -59.0795 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 227.8 |
| 2dc5a849-5dd5-3722-9571-742b4603c9c2 | -6.8387 | -56.4344 | 2026-08-16 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 6ee8e626-b3eb-3d40-ae78-3faf2ec6c1f6 | -6.8597 | -58.9738 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 5de3246b-eb24-33d7-883d-9a3f24f8964f | -6.8596 | -58.9931 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| a6930765-783c-3eef-a206-2cfcd1cdbaf7 | -8.9039 | -60.5769 | 2026-08-16 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 86c3bacd-96cc-3885-8a9b-ede99d6f4e30 | -6.8385 | -56.4542 | 2026-08-16 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 14b049af-9379-3963-9e9f-aa02bad8df07 | -6.6938 | -58.942 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 57ffbbc7-c3dd-305c-aab0-78d683a479d1 | -6.1107 | -57.723 | 2026-08-16 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| a5346f35-fdb1-3670-bead-91811bc12659 | -6.7123 | -58.9412 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 175.8 |
| f34a939b-2ad8-3152-9a19-582c936951f4 | -6.0923 | -57.7238 | 2026-08-16 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 3da8c63c-c6ab-3e36-b2cf-f1892d090ea7 | -6.6198 | -58.9836 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2da99716-50db-38d2-aa84-ed2849a6d9b4 | -6.7122 | -58.9606 | 2026-08-16 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 15398500-021c-33e7-ae19-d678a21513a1 | -6.8202 | -56.4353 | 2026-08-16 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 1354f121-3d0f-3c47-a0ed-f78ebea44fb5 | -12.7972 | -41.5169 | 2026-08-16 01:10:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 43.2 |
| 0f46866d-e430-3ef8-848e-62d44a163187 | -6.6378 | -59.0602 | 2026-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 791842dc-0169-37ea-9f91-d99e7fbbd1b4 | -14.3919 | -51.9081 | 2026-08-16 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 8fac80e4-9f80-34ae-b790-2503af707445 | -8.409 | -62.6577 | 2026-08-16 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| e73131ea-ce56-3012-839f-892e550d9229 | -14.3923 | -51.8867 | 2026-08-16 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 4920f0c3-8fb8-3d70-953b-dca6bbc30bd5 | -6.0923 | -57.7238 | 2026-08-16 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 20501545-e2ea-32ad-bc3b-f149ea66c78f | -8.9038 | -60.5962 | 2026-08-16 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| cd00b285-032d-37d3-ad86-09b92309e199 | -6.7123 | -58.9412 | 2026-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 180.6 |
| 0e76255c-7686-3446-a4e9-7b73a0d63c6b | -6.1107 | -57.723 | 2026-08-16 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 0855eca2-892d-39a0-b706-8ea19d606b2a | -6.8597 | -58.9738 | 2026-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| cc781ff1-17b8-3bd6-a991-a87545a9f145 | -6.6014 | -58.9844 | 2026-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 167ed99c-184b-3f8e-8cb4-1da0fe86912c | -6.7124 | -58.9219 | 2026-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 1568c93c-6284-3e7a-bfbb-8adf51a46901 | -8.4276 | -62.657 | 2026-08-16 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| dad00557-bce7-3a35-a845-029d00beb041 | -6.6377 | -59.0795 | 2026-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 211.1 |
| 4a97eb5a-3bff-397e-b9ad-8687ea1462fd | -6.6937 | -58.9613 | 2026-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 28602a6b-78d3-3a13-90ae-82b0edb37b7d | -6.1106 | -57.7425 | 2026-08-16 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 22f4fca0-8408-3143-84c6-485b5469eb76 | -6.1108 | -57.7035 | 2026-08-16 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 47d2f532-1500-31bd-86cc-26267214f4a7 | -6.8385 | -56.4542 | 2026-08-16 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 4429605b-1b52-37d4-b563-96d61f0cc0e1 | -6.82 | -56.4551 | 2026-08-16 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 028ad753-5daf-3643-aacc-1dd1cd79a822 | -6.7307 | -58.9405 | 2026-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 07275d5c-98fb-309a-b6ad-e8587ecdabb5 | -12.7017 | -48.4753 | 2026-08-16 01:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 71f5a07f-360a-38c7-8af8-800011ab395b | -6.3137 | -43.6178 | 2026-08-16 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 6695bcd7-0cf1-3a9a-abfa-7b430515ba43 | -6.6938 | -58.942 | 2026-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 56c7aa3e-0744-3e7f-865c-c7f88bbbcec5 | -8.9039 | -60.5769 | 2026-08-16 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| e152a15c-ea23-3f31-ba06-934a4277fab0 | -6.6193 | -59.0802 | 2026-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 7ed1e4ae-9279-3a72-b641-b1face5b8af3 | -6.8572 | -56.4335 | 2026-08-16 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 93d725fe-0278-3cd4-abb6-3870120cedfe | -6.6194 | -59.0609 | 2026-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 5a6b9500-ceef-358c-b19f-780634485525 | -6.7122 | -58.9606 | 2026-08-16 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 8cf935a4-56ff-3c26-8853-f7f15c2b127a | -8.9041 | -60.5577 | 2026-08-16 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 53565845-7bec-3e68-b5fc-76f9b7fe1a37 | -6.8387 | -56.4344 | 2026-08-16 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 7a6a4480-4bea-3e88-ab84-6365cf3997ad | -8.95 | -60.52 | 2026-08-16 01:15:00 | MSG-03 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0e75f64-ab64-336b-90e1-ab8a3a97428d | -6.8202 | -56.4353 | 2026-08-16 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| b3c47aec-4e6a-3711-8881-82b5a59fe28f | -6.0923 | -57.7238 | 2026-08-16 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 642c38d9-0efc-3d9b-90c1-9e2810f3c969 | -6.6937 | -58.9613 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| c75c9bdc-6520-32cd-8023-28b02f783c43 | -7.4259 | -60.01 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 287306e0-0e90-3975-9700-43cd835b983c | -6.6194 | -59.0609 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.4 |
| cbc2ab3c-8c6e-3320-998d-ffd083aeca67 | -6.6014 | -58.9844 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 5de98d17-c111-3c05-84e3-89840bc84840 | -6.7124 | -58.9219 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5cbf63ff-baf1-3d9b-a036-9af7253aeb41 | -17.9052 | -50.3205 | 2026-08-16 01:20:00 | GOES-19 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 551fa3f2-3d05-3546-93d0-7337cb4b191d | -6.8597 | -58.9738 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.3 |
| f8aff268-b6b5-34b4-a839-828d856f4f79 | -6.6378 | -59.0602 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |


[Clique aqui para ver as próximas entradas](README4.md)
