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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01e15078-c1b4-3bc4-bf90-d5a1dc8e2bd4 | -2.9299 | -48.2264 | 2026-01-15 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ccdee3a-9709-3f4e-af66-097ee08fafb1 | -5.44537 | -35.61158 | 2026-01-15 04:31:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ae09cfd1-32ec-3277-b847-8059445baaad | -1.86608 | -48.0237 | 2026-01-15 04:31:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bac9155-bc9f-3f04-a8c1-e215d05d9a58 | -5.46589 | -35.55737 | 2026-01-15 04:31:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 8c75f3f6-3e08-3547-8b86-1eeccdfc9452 | -1.5038 | -45.90607 | 2026-01-15 04:31:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a66988b-01c4-3aa6-9d89-12d4b538ada9 | -1.49992 | -45.90905 | 2026-01-15 04:31:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70724475-b0a0-367e-9792-6e969046ff8b | -5.46693 | -35.55211 | 2026-01-15 04:31:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7d298b69-3307-342a-91d9-2b4cc77c0491 | -2.87075 | -45.53759 | 2026-01-15 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6beb6ea-1814-3164-a4a2-6c742b406d75 | -3.66165 | -43.51815 | 2026-01-15 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1a1cd08f-df77-3b94-bc79-ffbe6e6f42cc | -1.32496 | -47.8063 | 2026-01-15 04:31:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7995e00b-1a0e-3f14-9681-ba9ff19758ee | -3.91664 | -43.52773 | 2026-01-15 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa074314-7442-33e4-a197-8099371da601 | -0.65292 | -50.29334 | 2026-01-15 04:31:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0609c06-0fb7-3a73-89eb-7426a850b0a8 | -1.86878 | -47.98467 | 2026-01-15 04:31:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff496564-a8ba-3aa3-93be-620d59ac9f0c | -1.53622 | -47.21949 | 2026-01-15 04:31:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2a979a2-e658-364c-b68d-a401a399db63 | -1.80093 | -45.28509 | 2026-01-15 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24c867f1-ffe9-3f4d-adde-4e01d7184f05 | -2.45093 | -47.78717 | 2026-01-15 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df055a63-1ca8-3c22-99ae-7cd62d6d9b9b | -3.22894 | -41.80196 | 2026-01-15 04:31:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5468f1d1-3e69-3de3-b0c1-1a20dd0bcd14 | -1.80066 | -47.70258 | 2026-01-15 04:31:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b82415f0-d82d-3d50-8c9b-b2613edc445c | -3.6579 | -43.51762 | 2026-01-15 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 968ba663-4bde-39ea-8f79-7979740619c5 | -3.47632 | -43.33902 | 2026-01-15 04:31:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9280dbc-c34f-37fe-bbe1-13d3d61a3f1e | -3.24137 | -41.80396 | 2026-01-15 04:31:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d2139ce0-6a53-354f-9cbd-f4041219aaeb | -3.34633 | -42.15692 | 2026-01-15 04:31:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 658b06d8-220d-3077-8d14-6b1719f1ae2c | -1.52639 | -46.69501 | 2026-01-15 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29a9f474-f915-31f9-9ac9-1dbadcdae825 | -1.60358 | -48.02564 | 2026-01-15 04:31:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de967a9a-0379-3daf-91a9-8c1d7a410607 | -2.92825 | -48.23691 | 2026-01-15 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bd1294e-c0bd-3cf8-bffa-5edfd4af5fac | -2.92935 | -48.2299 | 2026-01-15 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dec6f4aa-3467-310a-bb76-60bb2a5f1f83 | -3.23723 | -41.8033 | 2026-01-15 04:31:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 04f4f096-a635-3965-918d-50f70e01bcc0 | -12.12903 | -45.57753 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa5c9d7e-400b-3076-a949-406cdd363578 | -12.67041 | -38.56651 | 2026-01-15 04:33:00 | NOAA-21 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e0fec8e7-066e-3459-a60e-a7e65df8ea1c | -7.25282 | -43.05098 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cacac1da-10f7-3f33-8949-4ab13b390301 | -12.12598 | -45.57247 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09070151-57fc-3e85-96ba-7df496f0dbc1 | -11.979 | -47.84138 | 2026-01-15 04:33:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9ea241a-9bc0-3c50-af03-70a66847b417 | -7.24369 | -43.05689 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bc122262-f54a-3508-9c00-e8b538206322 | -12.12838 | -45.58202 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32d3903b-9149-3804-9f55-6e3c8fbbeb5b | -7.22163 | -39.95032 | 2026-01-15 04:33:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e52c5609-1eeb-30f8-b3e2-c2e9722a6a6c | -10.59531 | -44.97261 | 2026-01-15 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cd1cb32-12e6-3683-a0b3-8c7ec2650883 | -7.24015 | -43.0527 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7b9cacd6-1109-3945-a663-2bf6ce9e793a | -10.34958 | -44.82683 | 2026-01-15 04:33:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab6fe29c-76fa-3aaa-8e9c-52bd55be0aaf | -6.89296 | -42.83601 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5e0f5436-02b5-3a9d-bfe1-d4d045c64666 | -12.09011 | -45.28672 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 011179b7-1158-3eb7-a7e0-60abbca597e8 | -7.24774 | -43.05751 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 54086a29-909a-3747-85dc-92bdd8522a96 | -7.86506 | -39.09734 | 2026-01-15 04:33:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5708b6f6-4bcf-3acc-8bb1-ecc6ba8e6bdb | -12.11821 | -45.62619 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9718ce4-f87b-316a-8390-912e9cb43295 | -12.51338 | -43.67924 | 2026-01-15 04:33:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 079dee7c-34da-355b-a99d-d7e8f1439029 | -8.39512 | -44.05384 | 2026-01-15 04:33:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbdd7bf6-6f2f-3657-9314-ca7f79d0cdff | -7.049 | -43.95029 | 2026-01-15 04:33:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86dda10e-d8a4-3418-bdac-4e465a0ad050 | -12.5123 | -43.68708 | 2026-01-15 04:33:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9745c400-7584-30ba-b060-b3333887b7eb | -12.09193 | -45.3013 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb63c299-aa99-3ce8-ab1e-fc65813040cf | -8.39443 | -44.0587 | 2026-01-15 04:33:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd542171-39c4-3892-9f60-c7c5718ddc3e | -5.51249 | -41.23061 | 2026-01-15 04:33:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 63874534-aefe-3e68-9ed2-ab4d45c22d71 | -7.23964 | -43.05627 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d2bc197e-4ab7-3120-ac29-4eaff24e1859 | -8.15682 | -43.18623 | 2026-01-15 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ba6d8a46-2f3b-3d6d-8ef3-3771b75ebe2d | -12.50081 | -43.67744 | 2026-01-15 04:33:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f882cab-8613-3070-ad89-94705640549d | -6.88371 | -42.84209 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dec2cf8a-f29f-3b0d-a240-54809b4ee067 | -7.24877 | -43.05037 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 45ed425e-f742-3e38-9e35-5bcb29708c59 | -12.07894 | -45.58375 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a68255b-6a36-39ba-8a8c-588478631cea | -11.97618 | -47.83722 | 2026-01-15 04:33:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53bde193-d9a7-37d5-913c-d60ab0fa0841 | -12.08923 | -45.2893 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f12296f-bfd8-36ff-9abf-752e808f8e8c | -6.88727 | -42.8463 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 05b6801f-3748-3f5d-b7e2-4e7249041c7e | -7.23154 | -43.05505 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ba76c8f0-d327-35aa-8d25-2470e84dcd06 | -8.15276 | -43.18559 | 2026-01-15 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5951ab7c-dc38-3f3c-b76d-95d4c56588b2 | -12.08762 | -45.57593 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f77bc64-331d-3f0c-be00-c6dc8a87e2ed | -12.12533 | -45.57698 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e382b5b5-9704-39bf-8a9f-ba4387304b4d | -8.35113 | -42.19413 | 2026-01-15 04:33:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6e5716b3-d407-3ae3-8af7-052ccd2e4a3c | -9.37352 | -47.07989 | 2026-01-15 04:33:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9894ef96-d88a-3b2e-b289-16fa46aa37c6 | -7.99036 | -43.3878 | 2026-01-15 04:33:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f9c393b-de86-3343-975a-e3724dd9b0a3 | -5.28378 | -45.4509 | 2026-01-15 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ced6d5af-bb50-3c10-a6f6-56d5ef66b5cb | -8.42789 | -44.01848 | 2026-01-15 04:33:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69c082e4-7b41-3ad3-ac55-3e5a38c11875 | -7.22201 | -39.94747 | 2026-01-15 04:33:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2ee53c87-c617-3e74-915f-9bff7b6f7ba2 | -7.86686 | -39.09897 | 2026-01-15 04:33:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ca931d82-58c0-35ac-8d7b-dedf3510b7f1 | -8.39899 | -44.05442 | 2026-01-15 04:33:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fb69795-732f-3174-ad94-65e8e29b2a57 | -11.97564 | -47.84082 | 2026-01-15 04:33:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aac1132d-c2f6-3473-9115-2a923cbb9c38 | -5.6203 | -44.88424 | 2026-01-15 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b6115aa-f3e0-3dda-99aa-f1dea72ede6d | -5.47962 | -43.03619 | 2026-01-15 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96cc6539-0a1c-3b47-8fd8-57f600a877bb | -10.48915 | -44.93053 | 2026-01-15 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 584aabb7-bc8b-3a24-8778-7537fad27fa9 | -9.93987 | -47.84436 | 2026-01-15 04:33:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 564689e2-d73a-317c-bbb6-abf1f9cd09fc | -7.24472 | -43.04976 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 39477199-90ad-3f65-9f08-f0d0ba51eddf | -11.97954 | -47.83779 | 2026-01-15 04:33:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6853101f-c0af-3913-b40f-a759ab7f9554 | -6.8878 | -42.84266 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fd19ef2b-c0df-39e5-b4fe-6deb06ce82df | -12.6699 | -38.57098 | 2026-01-15 04:33:00 | NOAA-21 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dc226c0e-f6a4-3469-af7c-3309c267631c | -5.45802 | -44.70623 | 2026-01-15 04:33:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b6461e3-00d7-3c4f-8b2d-210af4062715 | -8.43176 | -44.01908 | 2026-01-15 04:33:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8e8b3ec-9b8e-38aa-b139-f0c0613f243b | -7.2361 | -43.05208 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 4e3cf7eb-ebfc-356a-9c40-a44511592de6 | -8.16157 | -43.18314 | 2026-01-15 04:33:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1b9eaab8-7b7a-3e04-b49f-e27f073b5493 | -7.23559 | -43.05566 | 2026-01-15 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 658c32f7-ab3d-3d32-a2c5-15e71f2c0e48 | -7.99087 | -43.38429 | 2026-01-15 04:33:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 78d8dcbc-4c5f-3994-bd3c-05b4aa20d7b1 | -12.505 | -43.67803 | 2026-01-15 04:33:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 027ca50e-267d-376b-9463-c2012b3ac842 | -5.53986 | -45.15021 | 2026-01-15 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a1c505d-2a29-3c2d-b9bd-c0a373a6ad3d | -5.72941 | -47.93125 | 2026-01-15 04:33:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b01510f-a8d1-3b63-9fd0-816bcf934caf | -12.08882 | -45.29601 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0aa518a-c2bf-3835-871c-1625c6387534 | -5.26243 | -44.73344 | 2026-01-15 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0d88708-de76-39c6-8976-2f43028175a3 | -10.48539 | -44.92993 | 2026-01-15 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5ba3b77-53f3-3abc-b028-9c1367b0faee | -7.61304 | -47.05733 | 2026-01-15 04:33:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3e0e3d0-d34d-3107-acab-ea835249d76d | -7.04829 | -43.95502 | 2026-01-15 04:33:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c0c1809-9647-32af-87b7-fddf31e7c1c1 | -12.10294 | -45.60105 | 2026-01-15 04:33:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f526e5fb-b950-3d03-b092-bebdf3fdd98e | -7.61249 | -47.06089 | 2026-01-15 04:33:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bf5cf7b-dbc0-3f29-be6c-e459f24a908e | -6.29844 | -41.92691 | 2026-01-15 04:33:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2f4f4d6d-ac85-3114-b678-4e55d1035da1 | -7.86152 | -39.09813 | 2026-01-15 04:33:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| da69e056-205f-337a-ac18-66bbf60c6e9a | -6.93569 | -42.45739 | 2026-01-15 04:33:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa542098-7b70-342b-b562-1ebf2bd3c879 | -5.89827 | -42.55011 | 2026-01-15 04:33:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |


[Clique aqui para ver as próximas entradas](README6.md)
