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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8a43dfc-2288-35a5-b6d2-e76fcd5390cd | -6.38218 | -44.45774 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 429241ac-5624-3790-86ae-bfb084b651d6 | -9.68173 | -46.8967 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 072aa6c8-3066-3896-9e2c-53ee0d7dcdce | -6.2056 | -43.54846 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0920fc62-0df7-333f-af03-7388a421aedd | -6.06585 | -43.31448 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ecee514c-1fb2-39a7-bca8-ad38b654d635 | -6.37996 | -44.45012 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a02d3c98-418b-357b-b1cf-d71bc21d1f75 | -9.31397 | -46.72633 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| cc9a4e84-2ed0-3712-ad59-d69aaa50cac2 | -9.10144 | -46.97879 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b259316e-cb8a-310d-af66-b7d06c4d97fb | -5.76182 | -42.75465 | 2025-09-10 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| be5deba9-35ec-3631-a944-0fd8ef0d9d22 | -7.39012 | -44.83851 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ecb2f54-307c-37c6-aa9e-251c613396e4 | -5.86095 | -48.163 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 42aa8ab2-aa7e-3d7c-b185-38b2357202bb | -5.58797 | -42.91061 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9e1886c0-391d-38a9-92ae-4f5e8a7c7472 | -7.79273 | -46.06363 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd76094e-8a15-3823-9463-aa9f76448550 | -6.16583 | -42.65155 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4c74385b-837a-3dbc-9e60-484470319bea | -9.82445 | -46.02234 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00b6e7f0-b229-3cc2-a843-81b3662dc40c | -8.04798 | -48.66627 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7590cdd6-4220-35f8-b586-7f7263e47ed1 | -6.24543 | -43.42387 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dec1b401-275c-32a0-962b-10012d13a147 | -9.06204 | -49.82689 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cddf0e49-99d2-3ed8-9e0f-3e43b2184cd0 | -9.19098 | -45.59598 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7990ec61-79cb-3505-b0a4-6576f451ff57 | -8.94982 | -44.94188 | 2025-09-10 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fb6b258-22aa-3cd1-ace2-41aacc45293b | -5.64709 | -43.91904 | 2025-09-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 44e30e1a-6f03-359f-9641-b0031e537949 | -5.79738 | -45.67301 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c46676c9-4af8-36f1-91b9-42759f4174d6 | -5.71621 | -45.42319 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12589abb-d9fa-3a6f-9b0e-7157f851bbe8 | -8.02878 | -45.56614 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf22fe5a-52b2-33ef-94a9-7b2390743daf | -5.52665 | -46.49987 | 2025-09-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a882c24e-3d78-3224-9099-4a08f41e6fe6 | -9.07571 | -50.47766 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb96dbf9-dfac-3d19-904b-1ac377426724 | -8.05468 | -48.67545 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec3b42af-1f02-3cd5-874b-bf8e36a4ef7c | -8.49268 | -44.647 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cb85e76-bb93-3159-aefe-7f40c0445ea0 | -5.91519 | -45.79596 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 422269ea-c268-34a7-bd6e-d70642e522b8 | -9.09926 | -46.96973 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0b78833c-ab3b-3565-b627-cc72a5e9ecbb | -4.09534 | -41.57137 | 2025-09-10 04:14:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4fc0614a-f9ea-3ddf-a46e-858f5270abb5 | -8.00558 | -46.33528 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f475d5eb-d499-3302-9739-6482ffb607a5 | -8.04418 | -48.68854 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d197b20b-4d46-34ca-bbef-6ff686cdbd98 | -6.16953 | -45.81467 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ac28af4-e3ff-36b0-a017-120ab48bb4f7 | -6.64302 | -47.4288 | 2025-09-10 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37667912-cfc6-301c-90f0-f3e644fc1dbd | -6.49415 | -41.76064 | 2025-09-10 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e0ca9d46-6890-349e-8bcd-36031f7b624d | -9.0813 | -45.70737 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa80ed07-5f8f-34c8-85f9-7f921c3bedca | -5.86614 | -48.1566 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7fffe40c-1702-3261-a72c-dc68bfc84435 | -4.24382 | -48.26822 | 2025-09-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4d9d74e4-dc97-380c-b148-5b3011ca09c1 | -6.16476 | -42.65847 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4965826e-6068-3bda-bb58-000a9a554cc0 | -5.11922 | -44.67175 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfb8a49c-9d78-38e1-b2d6-bdec9a440d28 | -7.70193 | -47.2952 | 2025-09-10 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ee93ee7e-5e43-3971-8a8c-88c1da1e1b7e | -6.05487 | -43.31983 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c24b574-424a-31bb-bb72-b7d9c180b719 | -8.51877 | -45.70934 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca547166-9ad8-31fd-ad2a-3e50cc6509e0 | -7.48202 | -46.09587 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3148bee9-9017-3362-ae04-437778fcb230 | -6.42492 | -44.3995 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7bb6dba0-b915-33f5-9d89-447c926f4902 | -9.05473 | -40.52234 | 2025-09-10 04:14:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7ce37bfb-bb00-30f2-ba15-43f4e5f623bf | -6.61546 | -43.99431 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a872ae01-4f19-3d02-86ee-b9d2f720cd88 | -5.67366 | -43.9017 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbde593a-a857-321c-a768-fc2093bb4562 | -8.07106 | -48.62745 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 948033cb-30fb-3ccf-9ef4-a486d759d2a5 | -8.32848 | -44.86426 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 714db264-db46-3140-9335-a36e8629a652 | -4.86891 | -42.76557 | 2025-09-10 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 555af43f-9f0e-3a08-929c-4979b7d59861 | -8.49322 | -45.67039 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb2ecff0-3599-3708-ad18-24f0da9b889d | -9.51781 | -46.54586 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e22ca6d7-f9aa-3739-8ef5-67a0f7b606cc | -8.95295 | -44.93929 | 2025-09-10 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bb6471c-5f19-32d5-9bd9-ac9813771057 | -5.51009 | -42.66899 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ec6722d6-80f5-34c1-8e81-3a84c82de4b2 | -9.35821 | -46.50367 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3fdc7cbc-e693-3459-8ad7-6be7aa4daa56 | -7.55433 | -44.6632 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ae59b97-a2fa-3a40-870e-0aedf9f211c3 | -7.09676 | -44.13509 | 2025-09-10 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a90a76f-f5f5-3b0d-b8bb-baceb252ad0d | -7.18854 | -44.93147 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bbfdf0b0-a3fb-35e5-987d-b8cabc35df29 | -6.17163 | -43.37703 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3574d63c-e1a4-344c-849c-0e50694156e9 | -8.52378 | -45.72168 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 044d00c5-7ce1-34af-bb9d-df1ebbf8e7f6 | -9.51495 | -46.54137 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 570f4942-f306-304e-923d-106a6c7610d7 | -8.46323 | -47.29632 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6880946-7425-3e17-bd4b-77c7c8a0b72c | -4.5505 | -37.78687 | 2025-09-10 04:14:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dddb48f4-0877-33e7-9e7a-4b6a57345166 | -6.26467 | -43.39217 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b03ddb87-ed49-34c9-8fd4-0873f96b1273 | -6.18792 | -42.66206 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9792387e-b8a2-30d7-b83f-b249cba2c084 | -9.06504 | -46.97604 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b8952a95-b5f5-39f9-9574-bc6d9bbdbd41 | -9.31536 | -46.71742 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c6312e5-5d0f-3a7f-a1b9-d42596a0ae93 | -9.07948 | -47.0 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f37b01f-c46a-3cbf-81c3-edbcc79827da | -5.58408 | -45.03848 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 92802de4-cc6a-3325-b580-5572ffaea834 | -6.53741 | -44.78695 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 292c7400-c897-30ab-8daa-67753ac9669b | -6.84836 | -47.91895 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e64e1b9d-b0d0-3cb6-860b-0823aed297fb | -3.63505 | -49.20566 | 2025-09-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97dc2eab-5431-3821-b13b-ebd9dc73f87b | -9.71438 | -43.51754 | 2025-09-10 04:14:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58ce2b72-e0ee-354f-a215-cdbee1d4c609 | -6.17353 | -42.64565 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 85092ea5-30c0-3178-86d7-6f5f317657e2 | -7.24873 | -44.4655 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8ca92e3-dccc-30d4-abfc-2cdab17db732 | -7.86132 | -46.26081 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c405b179-8d6d-3449-a66a-3cd56d3553e3 | -6.1896 | -41.04826 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| db8d9e15-2a19-340e-b42c-c17f500c7a73 | -5.51178 | -42.67986 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a8444d55-154a-39e0-8a47-bafc92035abf | -8.65788 | -45.73929 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ac83e3a-c957-30cb-bc37-4570cac3498d | -5.45268 | -42.79422 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| df1463e2-782d-384b-bd03-b63832173cc8 | -6.99599 | -45.64988 | 2025-09-10 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5a88f85-7ac9-35c0-8259-2a01bad5d317 | -9.08786 | -46.9718 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 70252b6b-22dd-3f6b-bbe0-5d33481074d9 | -9.07444 | -45.77117 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b9ed132-ccfb-383b-8ffa-1107316c5604 | -6.37793 | -43.03559 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec6d1ead-df44-3186-8092-62819785cb35 | -5.82063 | -45.68465 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44cd7ffa-0884-3480-98ab-cc45489688d9 | -7.5482 | -44.65864 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a2c4a8c-7351-3b97-9b8c-5f8f166dad62 | -6.56816 | -43.14664 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 651b9dfd-cb55-379a-a831-e3c5f919e387 | -5.50571 | -42.67538 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4ea00532-faed-347d-ac0e-e1c0e37181ed | -7.7487 | -50.72827 | 2025-09-10 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 608d2739-ea66-3935-9311-4b4832f7c4d8 | -6.29226 | -44.22957 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9a56250-8875-36d1-9c4f-6cba1e7cf3da | -9.21697 | -50.55384 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7de24312-d934-368b-9e4b-ddf647faace3 | -9.0554 | -45.73763 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 733a6dd1-5505-358a-9e10-723e9962279b | -6.67382 | -43.83969 | 2025-09-10 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 34f0ca2c-b208-3b99-95be-d0e7d841db23 | -9.06006 | -46.98373 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 916837a1-3171-3fcc-a96c-6d1616e38e55 | -8.74784 | -47.0959 | 2025-09-10 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7dcb898d-0a27-3bc8-8f89-d441f6d58dd2 | -6.05907 | -43.137 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4838d7d0-628c-3f54-af04-c5735946d318 | -5.6813 | -43.35594 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 499419e2-f45c-3760-bf6f-253d605e248f | -8.66413 | -45.74406 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8c245594-904a-3682-b1fa-75c4d2d5df7d | -7.49788 | -48.227 | 2025-09-10 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README32.md)
