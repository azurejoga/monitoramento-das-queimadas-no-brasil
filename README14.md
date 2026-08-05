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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3388337c-1833-3a87-81d8-4ec050c4a009 | -4.28393 | -48.03436 | 2026-08-05 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84f08c9e-971f-3a1a-8b81-63b2bf12fedc | -6.5504 | -55.15983 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c7d8026-fcae-3dff-9fa8-3f980d971d5b | -10.60929 | -46.37733 | 2026-08-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d40ae9c1-f476-3671-bf1b-05d6ccfc8003 | -11.51871 | -43.24764 | 2026-08-05 04:46:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 66be4e7d-a7d3-3a2a-8aec-05b97144f333 | -7.50579 | -49.74718 | 2026-08-05 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b40b849e-c0ba-38bd-9dad-97b3a160b939 | -6.24387 | -47.14464 | 2026-08-05 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4832756-d594-3a4e-82de-4db9197bb309 | -6.54886 | -55.16914 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d443c0af-0cc5-34cb-abe5-21356f293841 | -11.56179 | -47.71054 | 2026-08-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f1325ca-67e4-3454-9da8-ad941f5121b3 | -6.55192 | -55.15065 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b32f245f-6466-36aa-b4e7-6b964c40318e | -6.5656 | -56.52254 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 558e5f74-8026-30c5-b02a-57387360150c | -7.62775 | -45.31139 | 2026-08-05 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3bd5a654-cf20-3e4c-badc-70e00c84dc2b | -7.22201 | -43.35351 | 2026-08-05 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 05a22079-5327-3add-bf04-19c6fb66ed38 | -10.45896 | -50.22152 | 2026-08-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d31d7fe4-2de3-3095-98d6-6aee2cbeb0a9 | -6.56706 | -55.153 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae51fdb4-dae7-3e12-914c-76df964acd6c | -9.28544 | -60.65179 | 2026-08-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f010cbf-f864-3b43-80d3-3b3d8fe59fe1 | -11.5611 | -47.71545 | 2026-08-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c518c3c8-1922-388b-a578-9d156e86366a | -6.00997 | -47.39847 | 2026-08-05 04:46:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bfef43e-586c-3eb8-a8b7-51722baece23 | -6.53827 | -55.16266 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3758a93d-b7ab-33d6-a1eb-18fb49ecc77c | -9.18634 | -58.06608 | 2026-08-05 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8712e54e-e3d4-3662-a751-e8ae3abe63f5 | -6.90289 | -42.40506 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 487c8a8d-483d-3928-97a7-b95d21c10560 | -6.72481 | -58.92835 | 2026-08-05 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d5bf82ba-3038-3a27-90ef-6efec72140b5 | -7.98186 | -52.07675 | 2026-08-05 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac115de5-a5db-3b5f-937d-775975614187 | -10.75485 | -42.08937 | 2026-08-05 04:46:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e7517bf3-4bfd-3254-a989-bf97e2b66e10 | -8.35334 | -45.98104 | 2026-08-05 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 655e1715-fdc1-31d8-a77f-b3517534f474 | -6.33882 | -55.73055 | 2026-08-05 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eeae1f83-9708-3fff-8cd3-348d426e8a44 | -11.52357 | -43.25163 | 2026-08-05 04:46:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b5429564-ab2b-309a-8375-8b174f394c29 | -7.74415 | -45.05478 | 2026-08-05 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 1a4067fd-86d6-39c1-ade5-8780b054cfa8 | -6.56972 | -56.52321 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa323adc-e4d3-31ac-a994-f65aae60ced2 | -10.63584 | -47.487 | 2026-08-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 02298430-7fe7-3044-af9d-d50429347d38 | -11.52365 | -43.25065 | 2026-08-05 04:46:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3dadac55-4e19-3402-8253-339a6d49966c | -11.51882 | -43.24668 | 2026-08-05 04:46:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7273c17b-8cbe-309a-adcc-e8b2e2055bd9 | -11.10798 | -50.42553 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c607931b-bf68-344c-8b54-497d49194e69 | -6.00933 | -47.40285 | 2026-08-05 04:46:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae45142e-83a1-3425-b79e-32f4544617e3 | -10.46411 | -50.23372 | 2026-08-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b93b77b6-8716-39da-96f6-a71aef770c87 | -5.4332 | -47.25604 | 2026-08-05 04:46:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d949cf62-ec8d-3da7-8364-b486ee8b131d | -3.33145 | -54.67712 | 2026-08-05 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecdd0bcc-a2af-3e1f-a2a0-ad46654916a0 | -6.93664 | -41.9255 | 2026-08-05 04:46:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cccea49b-dd1e-3133-9b6e-280aaf59af7e | -10.34821 | -46.49303 | 2026-08-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8973dd2-4a4b-32a6-9695-6f07357d6bd1 | -8.49782 | -46.8603 | 2026-08-05 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 155bbe02-c25e-3cd3-ad34-fd8c435050da | -6.93618 | -41.92892 | 2026-08-05 04:46:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2005f8cf-68b7-3edd-949c-efbcecaf550f | -7.4955 | -45.84513 | 2026-08-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ca0a772-2c06-344e-93ce-6d11d8796370 | -9.48963 | -57.32637 | 2026-08-05 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| da894014-37b4-3f1f-a227-e500408d5d4e | -6.5731 | -55.16349 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37e888a1-d283-3375-af2e-b5bf7fa48a77 | -8.38457 | -48.21294 | 2026-08-05 04:46:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9922c915-ef22-394d-b9fb-6ad55f60e687 | -5.57273 | -46.73771 | 2026-08-05 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1162667-4f62-3363-973e-d70168f2e77b | -7.22765 | -43.34877 | 2026-08-05 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7dbd4055-85a9-37ac-8af0-a712c1df7789 | -8.35279 | -46.38814 | 2026-08-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45c4e452-6170-3cd1-8d13-1936bb0e8bbe | -6.57234 | -55.16813 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5c165a9-1b99-303b-852a-da8ee68bb64d | -6.50448 | -44.70093 | 2026-08-05 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8bd6efa-5ec1-3b4f-a4be-cdb9aace4651 | -10.46126 | -50.22948 | 2026-08-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3918c1ae-f3c6-335b-b513-237a5bf5ddfb | -11.11185 | -50.39955 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aaa10945-d820-346d-8be6-e48873fd082e | -8.41832 | -49.55192 | 2026-08-05 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65cc3536-da0e-364f-9df8-d9f017bb4c1a | -6.54206 | -55.16324 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f871e44-2be7-3cbc-b35e-33760e470391 | -10.27198 | -46.35247 | 2026-08-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36369116-8ec1-3c83-bf3b-281bb56414a1 | -8.34088 | -45.97911 | 2026-08-05 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77974a7c-a11a-31c2-a12a-50b1525c7c07 | -9.28603 | -60.64861 | 2026-08-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b927e2e-ba58-3b50-b90a-c225fcaf7d8c | -6.5481 | -55.17376 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc0a4f85-aed7-3dae-93df-274d0915727a | -4.28876 | -48.354 | 2026-08-05 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d0fc2ef-bf8e-3287-8728-f091dfc5067f | -6.54109 | -47.12645 | 2026-08-05 04:46:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1783cb0e-4537-3402-9494-63436682ea15 | -6.54738 | -55.15461 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 972fe2e9-38b4-325d-9d7b-8df3dcd80c97 | -6.90678 | -42.41514 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9a9260fc-cd06-32a0-8628-4ee5d55e2a8f | -11.06897 | -50.57052 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e419e30-e7bf-3b0e-a6f5-b1a6c8edbd00 | -7.74052 | -45.05161 | 2026-08-05 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2681a45e-e0c5-34ac-895f-62e043b48525 | -6.61699 | -56.36495 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 653e705d-5ef2-3b88-b8c8-be6b8783ff8e | -11.554 | -47.70942 | 2026-08-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd1a4dd4-6046-30d9-a63e-0936008ac0e7 | -6.5678 | -55.17216 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca0c5c2b-91f8-332e-99fb-b0d64eb7233d | -11.52396 | -43.24838 | 2026-08-05 04:46:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ca67fc13-b531-31ab-b677-4447ed148fa8 | -6.54283 | -55.15862 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e98ce731-8eaa-324b-a9ca-2dac77bac555 | -5.93361 | -46.35297 | 2026-08-05 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72956b55-6290-3186-a0c5-899a89db217a | -11.15602 | -50.38357 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00e37b97-e4b1-30da-9fcb-6846158abf49 | -6.15094 | -47.17675 | 2026-08-05 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0cceb209-05bf-3c60-8f00-d7790796299b | -6.95955 | -52.81792 | 2026-08-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3efa6118-dd4c-3117-becc-6b9203fbd825 | -8.50508 | -49.55701 | 2026-08-05 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6bd0389-3e1a-3a94-b8ae-a16b806b56d9 | -6.58376 | -56.54064 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc4d9211-fdb8-3758-b421-dd5115e5be46 | -7.45912 | -46.15229 | 2026-08-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b3ee003-aca5-3a45-a12d-25a8e0003854 | -7.88158 | -48.92701 | 2026-08-05 04:46:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e02dd3bd-6feb-3083-8053-92a35738d68d | -7.39392 | -45.05234 | 2026-08-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16b50d9b-8bb8-3a92-94e7-877f71aaea28 | -6.89594 | -42.41682 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7256fc70-624d-3d8a-8c79-d715ee6d74c4 | -9.14434 | -49.66303 | 2026-08-05 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 218b9312-d877-3010-b9d1-5f6914f4545a | -11.07236 | -50.57104 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d663353f-94c3-3a14-aac2-596abd99fe3d | -6.53223 | -55.15231 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2de5007a-4f5d-3b8c-9db8-899aa171e718 | -6.53146 | -55.15692 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23a8bd82-9682-34cf-a7e9-ba6b21468bb6 | -3.32971 | -54.67431 | 2026-08-05 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eda67a79-395f-3b78-a718-b5bee8b2729d | -6.65204 | -43.91085 | 2026-08-05 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1ed0a8e7-11fc-364f-ab6a-9f329a286cb8 | -6.56022 | -55.17094 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f063571-b31b-3dbc-a052-132e3f9338d4 | -10.91538 | -50.42348 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 22862156-b63a-3ce9-8eb5-dcb35cfe5ae9 | -6.89856 | -55.38351 | 2026-08-05 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 664804f4-3998-3867-81a7-67d23dbb0c2d | -8.47697 | -51.54356 | 2026-08-05 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1004d53-b121-35a6-8b20-a0e18d01532b | -11.5184 | -43.24994 | 2026-08-05 04:46:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2aa5ff05-1a21-3b69-8a15-52de758a3aca | -10.91594 | -50.41978 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 91cc4c83-ced4-3544-b569-ee4fc0f1bcb4 | -6.26604 | -49.29891 | 2026-08-05 04:46:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f9e5f32-a88a-3435-b3eb-7d05149ddb10 | -8.48993 | -46.85926 | 2026-08-05 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f0d0ef83-0b3e-316f-b172-a22ac73a2949 | -11.30637 | -44.79821 | 2026-08-05 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a8b0a9b-8aa6-34ec-87f1-43c0f81de056 | -8.34864 | -45.9842 | 2026-08-05 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 280377f9-d65f-34c8-bfea-d426a56b8592 | -6.57613 | -55.1687 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fa265d6-4da4-3c3a-9508-7ad5a7ca8bca | -6.5375 | -55.16733 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9caabf7-f337-323c-9336-37180c4ff4ac | -10.91617 | -50.30216 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68a893d2-ff72-31a9-bc70-293f996982b3 | -6.55189 | -55.17436 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c615bcc-8485-359d-bdd7-d3194ed08a79 | -10.79254 | -47.7103 | 2026-08-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bbf6dd7-a374-345c-a48e-dd2549547541 | -6.28359 | -49.29787 | 2026-08-05 04:46:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README15.md)
