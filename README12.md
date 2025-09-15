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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcf67aa4-eeac-3cdb-aa71-5f80fd738c02 | -12.44681 | -44.74444 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9536ed1e-94fc-3332-939b-bd506dccaf6f | -8.90879 | -45.50465 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1658b955-1124-36a2-a170-7aecd425e454 | -11.44141 | -46.9268 | 2025-09-15 03:30:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| de890583-53b6-3da9-a17a-1b376dace27f | -7.51324 | -44.36901 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 281944c3-da16-3535-babd-c525c5900f5c | -8.95792 | -45.79619 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab346e4f-20e6-3f4d-bf2e-4a79867dd9da | -12.60266 | -45.73884 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 753a40bc-887a-3ee7-86f0-b0daa2a4ffae | -8.20631 | -45.55105 | 2025-09-15 03:30:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0abe2c65-a99d-328e-bdcc-f6ed3a1f4e9c | -11.33914 | -43.49434 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96966a99-bad8-32ab-afc6-93be54033bd3 | -9.59698 | -39.67447 | 2025-09-15 03:30:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f0b0eb52-250d-3a8b-80c8-1cd8719a134b | -8.97437 | -45.82004 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 03b5a018-a4d8-31da-b99b-6a971876dc85 | -7.87561 | -43.59359 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 36d8f7f5-dc89-382e-a23c-6d5af51e5add | -10.65394 | -46.23752 | 2025-09-15 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e318e9df-6fc0-3512-be00-c271472fddb4 | -7.87476 | -43.59827 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5dde1b33-ea81-36b7-9403-65bc056f40a0 | -8.12842 | -43.66269 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5ea6e75-61fe-36a9-a0ab-625d4d2b6f6a | -12.59968 | -45.72149 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc79344d-aab3-3a67-b69c-26d54737b407 | -8.90762 | -45.51053 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d21ea1c0-4e3d-3fcf-a429-634c15b16eaf | -7.67835 | -44.49084 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4493894-c74e-3289-ad96-fb27bfb6fbc6 | -8.91424 | -45.5122 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 98040f4b-af7b-3d10-82b3-aa990e6bbc3c | -10.73689 | -44.7722 | 2025-09-15 03:30:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3781272-7315-3fe3-8577-7e1b63567d25 | -12.0843 | -44.87582 | 2025-09-15 03:30:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6feefda2-eb4b-37a6-8619-f9f3759a06b9 | -11.47916 | -43.60339 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdfa0693-73fd-3f29-9043-ef05f8b1f883 | -7.86366 | -43.59335 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 18896dec-269e-33dc-944a-af39a6ec7cd1 | -8.64314 | -46.37527 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 134c8446-1fa3-351b-b367-704d8da13934 | -8.95917 | -45.78992 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 541de59f-b249-3810-bb3e-748e4a7fd474 | -12.09245 | -44.86689 | 2025-09-15 03:30:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e3b8aab-46b0-32eb-a5ea-8274daa2976d | -10.63614 | -44.21551 | 2025-09-15 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed0638f1-910f-3fa2-adf0-d96c5b0b87e9 | -8.5952 | -46.35857 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72eff70d-6426-3aff-91d1-285fe4e020bc | -8.91539 | -45.50636 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 39667cea-dadd-3b54-b8ea-5a7dce5405e1 | -10.74314 | -44.77322 | 2025-09-15 03:30:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2161b2a6-b104-3217-b88e-e8190f5bc4d8 | -8.91655 | -45.5005 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 57f3e988-432f-33e7-987a-79996fcfd2e6 | -11.78196 | -46.66643 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 464aa87b-7ba2-33a8-baab-fbc29c8d0ad0 | -8.59951 | -46.35294 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2da5a790-17e7-3ed5-a3ae-8a7acb01b71c | -12.43985 | -44.74787 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5a9e527-9fa9-3718-9da7-f7f3cf5c690a | -10.94018 | -45.51142 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c529103e-0d6c-34d0-864a-42932735db42 | -10.92693 | -45.57624 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 08fc3742-1f3f-3846-aae4-5f273b6f42f0 | -7.86347 | -43.59135 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 7574863d-3fc3-3686-8499-8db28ff156a0 | -11.78945 | -46.66162 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| de32af79-411b-34ba-9376-41f162d96bd1 | -7.86082 | -43.5715 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0712057a-c69e-3bf3-81be-ea00efb9a9dd | -8.95661 | -45.80278 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d499e0e-7dc1-3c54-b8dc-339a7d71ce2c | -12.58752 | -45.7091 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1499e2f1-cc4d-3b08-8b02-ceb9d31e634f | -7.85329 | -43.58185 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aec7fb1e-28bc-3ce0-b62e-66d155fd2082 | -8.83466 | -43.01793 | 2025-09-15 03:30:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cc36a787-a13f-31ff-b108-b2f8f1cb3bbe | -11.4776 | -43.61137 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed8d5a45-4e4c-34c0-901a-ff2f8c88090d | -8.20186 | -45.53763 | 2025-09-15 03:30:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f63f2de-bc3b-3e47-a460-c4525cd60bf4 | -7.88083 | -43.59943 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb0a5630-237e-32c8-ae73-e2a5aaa97f6e | -10.88527 | -45.45151 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82ba9410-c268-3681-9c86-cba44f380976 | -10.1661 | -45.3203 | 2025-09-15 03:30:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ed95524-7e6c-3b95-afff-6b5a6cace157 | -8.78705 | -46.04832 | 2025-09-15 03:30:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c81ff6b-006f-3afc-b09b-1ddacc2073bb | -11.33162 | -43.4942 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93966aba-39e9-31c4-8220-72df0db342b3 | -8.97346 | -46.21847 | 2025-09-15 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bfe19a7-31c1-3afe-b059-f09780c02faf | -7.86869 | -43.59711 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d874dd1-fc83-3f8f-a233-8b59fd5ab149 | -8.64608 | -46.37699 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f678b2f1-069b-32e6-9556-c5b4fc08bd8d | -8.61724 | -45.74749 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d443a810-484e-3fd4-be68-0c78252bebc8 | -10.9094 | -45.56651 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3f06f14-9db2-32d0-8633-10f37312932c | -8.91444 | -45.4761 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b9c2cd0-9410-3dd7-92bf-a9d67763c634 | -7.87391 | -43.60297 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1235e035-a977-37a0-a977-7b0c05763978 | -12.78917 | -47.93455 | 2025-09-15 03:30:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 79aaaa26-9ed0-3a03-8e76-0f88851ac5d2 | -10.66618 | -46.24681 | 2025-09-15 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14e8ddee-3cf3-3f7b-aa7d-510abda75b11 | -7.86885 | -43.59912 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8fbda12c-fa15-3dd3-b1c5-56782b6f2f39 | -7.86858 | -43.56332 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1a8968ee-0309-354e-b4ff-97ef165a09e1 | -12.79324 | -47.95019 | 2025-09-15 03:30:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 729c9f63-cb5d-3f69-a5f8-fe679cc738bf | -11.75525 | -46.65532 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 94d84b94-d2e9-3aca-894f-90d5f46d33eb | -7.86985 | -43.56078 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 85870af0-84fc-301f-96ca-5f0274954d7d | -9.3601 | -45.39146 | 2025-09-15 03:30:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1464ba29-9dd7-3e8e-b54a-cd515356e8e5 | -12.58811 | -45.71336 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7d1e9d1-faf1-3061-b1f9-db96f849cf52 | -12.04543 | -46.53631 | 2025-09-15 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 947dd50c-448c-3bae-8c45-4f8943d9db06 | -12.0118 | -46.66267 | 2025-09-15 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfe27367-6f91-30c2-9759-97a75d36bb53 | -7.50709 | -44.37211 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b73dba16-1585-3759-9b0a-9da3e8a32516 | -7.8773 | -43.58429 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 319.0 |
| 86377fb6-96d0-3293-a81d-a0de79aada1e | -7.88885 | -43.55971 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 615ed576-2c05-3242-89ac-c53406b6ab9d | -7.88168 | -43.59475 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| edec46ad-fd6a-3f29-b35d-705803371593 | -12.16815 | -44.09754 | 2025-09-15 03:30:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9889967c-7092-38b9-b9dc-e628e8725a91 | -12.44589 | -44.74898 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32c85ec4-a1f5-31b4-a945-5a159db59580 | -8.9133 | -45.46491 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dff0a374-654d-3ffd-9736-0e8c79f1f8cb | -8.91883 | -45.47217 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18334f59-8730-31c8-abee-faf4955c9d81 | -10.93068 | -45.49205 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b3afe8f8-ba67-36e0-b8c3-4679a2c70d75 | -7.86784 | -43.6018 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4777c964-f661-34b4-a7c8-c5f177e4fc9d | -8.98101 | -45.82222 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b5a4b413-bc1e-3bc0-ae39-6240ca6fdfb5 | -7.85596 | -43.56783 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10e92f59-00dc-339e-9637-0446a849a7a1 | -12.60221 | -45.73466 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 0dae0ef2-338b-3e47-bb1f-0fb8aa49934e | -7.86897 | -43.56541 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d2d5a199-38ba-3bad-84f0-51a0a24d69c4 | -8.7993 | -38.41526 | 2025-09-15 03:30:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dc261634-9a2d-3c75-ade7-4f26b613a354 | -8.08453 | -44.50416 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57b6fcf6-398e-3c07-9b0e-bfb69b2bf1bf | -7.87492 | -43.60025 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 81c9c38a-20e0-3713-bd31-736998a59733 | -11.7908 | -46.65502 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7d9dfb3-e99a-3db1-a918-96de07785268 | -7.86954 | -43.59245 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 5478dd43-3018-3316-86e9-6fd8444baf0d | -12.69388 | -43.47083 | 2025-09-15 03:30:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5176e3c-70f5-3321-87ed-1969dc667e30 | -7.87677 | -43.55734 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 958ea76f-24f8-333d-b8cc-77e008c93406 | -10.68704 | -46.25562 | 2025-09-15 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 54c4d400-c26f-3bf4-99d7-e91df7a299e8 | -7.86602 | -43.57734 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 787.2 |
| d24171d5-658e-39ff-abca-1b4b235b92fd | -11.12699 | -45.31894 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e7754d4-31f3-3fe8-9080-841bdc45fc02 | -11.33525 | -43.51402 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1612cafc-85fd-39e7-a719-324c401c2a75 | -7.87984 | -43.57029 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 629.7 |
| cfb8940d-77c4-3bf5-8345-4b8454d4a269 | -10.93904 | -45.51702 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd19321a-670b-347e-b387-e7b21e377f8c | -7.86262 | -43.59598 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f3ce99e-9547-315f-a9c6-918697236725 | -8.64748 | -46.36972 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fd1cfe0c-a194-3eaa-a2a3-70d77d0bfff2 | -7.85739 | -43.59027 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1bd34de9-e108-3982-9db1-0d21ac9581c4 | -10.30026 | -45.38652 | 2025-09-15 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbe724c8-1249-3d1f-9212-a06c23e9921e | -10.93001 | -45.49661 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2e2b697f-b03e-30f1-9da3-1466e11142c8 | -8.89044 | -46.17048 | 2025-09-15 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README13.md)
