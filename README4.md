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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f04775d-d583-39a6-a655-5cac881ffe9c | -6.98094 | -42.88629 | 2026-06-04 03:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a187321b-b8e1-3482-97a0-e973ef16939c | -6.98803 | -42.88767 | 2026-06-04 03:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 43227f4d-ba52-3601-a9b6-82a8953ba808 | -5.51735 | -37.62221 | 2026-06-04 03:19:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af761fc0-c794-35b4-9af3-8ba71bd2ea94 | -6.98614 | -42.87844 | 2026-06-04 03:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bcb360cc-6b9f-3596-8a66-df169d1a18d8 | -4.36166 | -37.90058 | 2026-06-04 03:19:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6092d94e-0b21-3032-b7ad-e8b2eb70a917 | -6.98483 | -42.88533 | 2026-06-04 03:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a5cd4ee6-d76f-3289-99f9-a5bf7f1e1e80 | -5.51983 | -37.48651 | 2026-06-04 03:19:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ea5f0a80-ae14-3322-8b32-995fbf20421a | -5.52039 | -37.48336 | 2026-06-04 03:19:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 42a2a223-dfe8-3c43-92ad-0a2c9c5e8e70 | -5.51964 | -37.48609 | 2026-06-04 03:19:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9ca05926-ebf5-33df-b6a5-adb2072aab0a | -5.60877 | -37.53177 | 2026-06-04 03:19:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 507facb1-25fa-3432-ae7d-a7844bf4d275 | -12.1946 | -57.2904 | 2026-06-04 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f2b85c78-d2e0-3266-ac64-3cefdc697bd4 | -10.3842 | -49.4338 | 2026-06-04 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| ac6f9708-a9fe-3947-a015-cd5a254844da | -10.3839 | -49.4554 | 2026-06-04 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c18f9d27-d79f-3a2d-a7c7-047e5111b63c | -12.2138 | -57.2688 | 2026-06-04 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 339.9 |
| 29a28c44-0fb5-3dc7-a291-40936b8dbc92 | -12.2327 | -57.2672 | 2026-06-04 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 369.2 |
| 1b6d0a83-5e81-330d-ab2b-b7e10dd69ec0 | -11.5499 | -52.7867 | 2026-06-04 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 7653ced9-43fa-3d1b-99cf-5957d845f9a1 | -12.2133 | -57.3088 | 2026-06-04 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| cadd249f-8ebb-363c-ab1d-921bcca76be4 | -12.2136 | -57.2888 | 2026-06-04 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 574.7 |
| 00cf5a2c-d2ae-381e-99e7-541024929020 | -12.2325 | -57.2872 | 2026-06-04 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 430.8 |
| d9e1f4ac-022b-38a8-b217-4d8f96a4771c | -15.3331 | -42.3324 | 2026-06-04 03:20:00 | GOES-19 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 72591c55-83ba-370a-bafd-5ae41a7b9a86 | -15.32743 | -42.3411 | 2026-06-04 03:21:00 | NOAA-20 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| b6f7aca4-acee-388a-a80a-627a4f0a5bf3 | -15.32848 | -42.33621 | 2026-06-04 03:21:00 | NOAA-20 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a080a7c1-e2f1-32d5-aa8f-9652ce9c73d2 | -15.3295 | -42.3314 | 2026-06-04 03:21:00 | NOAA-20 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e4003f0b-a721-3597-87fb-f08dd5383d31 | -12.2325 | -57.2872 | 2026-06-04 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 368.3 |
| 5cf8d5c2-523d-3659-9130-c4e6b4e605ad | -12.2138 | -57.2688 | 2026-06-04 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 253.1 |
| 6387c5fd-60ec-33c3-b8a1-3e55cfaa4baa | -10.3839 | -49.4554 | 2026-06-04 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 6c11eae9-d8dd-3392-86da-3310c238b10a | -12.2133 | -57.3088 | 2026-06-04 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| bb770329-dc11-38a0-99e8-9c86ae9ab2a7 | -12.2327 | -57.2672 | 2026-06-04 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 265.2 |
| 1c620584-7d0a-30f0-ba06-fa1259f54880 | -12.2136 | -57.2888 | 2026-06-04 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 460.0 |
| e697b116-c58a-34f7-9314-00d50fc5f020 | -12.1946 | -57.2904 | 2026-06-04 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| cc3d80a1-3bf6-3a89-9ab4-6d1a94b0dd6f | -11.5499 | -52.7867 | 2026-06-04 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 5b85005d-f5b0-3f11-aeec-941bd37cdbf0 | -12.2325 | -57.2872 | 2026-06-04 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 216.9 |
| 7686b1e6-f18a-3406-908d-4e513c082c67 | -12.2136 | -57.2888 | 2026-06-04 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 408.1 |
| d67f7c1f-368f-3d13-8094-324e14545fe9 | -10.3842 | -49.4338 | 2026-06-04 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| e00ee155-99c3-3254-801a-bf425db64680 | -11.5499 | -52.7867 | 2026-06-04 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| aea3152d-d7b2-3885-bcb5-866764dcf4ca | -12.1946 | -57.2904 | 2026-06-04 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 14d9d848-068d-36b7-9421-5156e37db0fa | -12.2138 | -57.2688 | 2026-06-04 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 254.9 |
| 1b169093-5bff-334a-a6f4-354606343ddd | -12.2327 | -57.2672 | 2026-06-04 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 194.8 |
| dd69c5b5-98cb-3034-a0e9-2961c63827a1 | -12.2136 | -57.2888 | 2026-06-04 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 338.8 |
| 725654e1-ca75-3eee-a8c9-4298e7049128 | -12.2325 | -57.2872 | 2026-06-04 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 165.9 |
| e3bc8404-da4c-3ce4-b647-576df904e357 | -12.2327 | -57.2672 | 2026-06-04 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 160.9 |
| cbf09f48-2f0b-3d88-b26c-cb95d22e1914 | -11.5499 | -52.7867 | 2026-06-04 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| fb7138b5-547c-3c30-98da-178ce1bae162 | -12.2138 | -57.2688 | 2026-06-04 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 214.3 |
| 6491f837-032a-30e4-a9dc-e1e3a6ad80ac | -12.2325 | -57.2872 | 2026-06-04 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 177.8 |
| ccdf6d0f-e3d4-3212-a02b-32c6b383d0ea | -12.2138 | -57.2688 | 2026-06-04 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 9a211139-9d44-33f5-9f0f-81c82a5469ec | -12.1946 | -57.2904 | 2026-06-04 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 9799efdb-7b4b-3105-a9ef-dde00259b364 | -12.2136 | -57.2888 | 2026-06-04 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 267.9 |
| 196a92cb-9657-394d-8601-78cd4649fd95 | -11.5499 | -52.7867 | 2026-06-04 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 906754d8-f860-33db-a793-6e6ed8389f18 | -12.2327 | -57.2672 | 2026-06-04 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 142.5 |
| b9396689-bafc-3799-9c5f-f305bed6dcd2 | -8.57563 | -45.99793 | 2026-06-04 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6c7ae489-d73e-30e0-89f0-5f3b20055650 | -5.72559 | -45.02986 | 2026-06-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28db2d63-708f-3c05-9f1e-2b1747fd9788 | -5.611 | -37.53129 | 2026-06-04 04:08:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 28b14282-1ac1-3bce-9ac3-1d64a68b581c | -7.27643 | -46.80885 | 2026-06-04 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6f4af19e-1183-36a0-93e8-a2ac17762bf5 | -8.57185 | -45.99727 | 2026-06-04 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 55723b4d-9005-3a27-8a73-528aa70144bb | -9.92382 | -48.00481 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c37f0b0-9fb8-34e3-896e-4181bb5b1381 | -9.92446 | -47.99766 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9d6e26a-6df1-3911-aa6a-86922e4488c9 | -9.92519 | -47.99705 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e44eb07-6f93-39ff-a995-19fd8c03bc5e | -9.46699 | -46.06184 | 2026-06-04 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae7570cd-26c9-3c5e-b127-376cdd0e7afb | -7.46054 | -46.20615 | 2026-06-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c38b8410-c1ab-3338-a9a9-33aa960efcb9 | -6.62892 | -38.7266 | 2026-06-04 04:08:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 58a7716c-2aef-39dc-8159-f2480db23bf3 | -9.53199 | -47.7576 | 2026-06-04 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd0c3dc1-7e25-3674-aabb-5a5e993c0502 | -7.27237 | -46.80816 | 2026-06-04 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 232d5b48-3b72-31b0-8f51-649657b1435a | -9.52851 | -47.75302 | 2026-06-04 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c547705-2b8a-3c4f-b2ed-4df076b56ec5 | -8.28351 | -48.2285 | 2026-06-04 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d8c69ad-2446-3fe1-8da5-51d33b893797 | -8.27912 | -48.22778 | 2026-06-04 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0503fbca-f995-3a3b-850d-c996435d0ec8 | -6.76017 | -45.01028 | 2026-06-04 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5f44115-32be-3204-8a4b-3f71921e5de8 | -8.29077 | -48.23876 | 2026-06-04 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13c12f82-a94d-3575-90a5-efa9a8d52b78 | -10.00411 | -46.56974 | 2026-06-04 04:08:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75dd2cb6-697a-39f5-a4b4-df5820b30a7b | -8.57639 | -45.99337 | 2026-06-04 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d6e4b02-01a1-3518-80c2-d514e4f05a4d | -4.36657 | -37.89973 | 2026-06-04 04:08:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5d185a3c-2fbc-360d-a20e-d15d9c71a5e6 | -9.9238 | -48.00156 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 658b2940-7d3a-32eb-ac64-a5d25ab0a692 | -9.56888 | -44.5775 | 2026-06-04 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42312ff0-30c2-30c0-8937-306ef2b3ce15 | -7.34269 | -44.31137 | 2026-06-04 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 624748d6-3c49-3c4a-a8d3-c1691c5d94cc | -9.92733 | -48.00943 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6593d86a-798b-358c-9508-979046eda740 | -8.93102 | -46.855 | 2026-06-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9a66ef4-970a-3222-ad52-f6b5a4f17dc6 | -9.92247 | -48.00935 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f787e28a-bafc-3f18-aec8-9b859692bc32 | -9.53024 | -47.75795 | 2026-06-04 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08fe55e1-ae61-3ca9-9bd1-d2253c341795 | -6.76765 | -45.03357 | 2026-06-04 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 940812ab-9c1b-38bf-8a78-e340fb5d7347 | -9.9245 | -48.00093 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0403edba-759a-30c0-b6cd-06a30b5dc7d5 | -8.28714 | -48.23362 | 2026-06-04 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01106c0c-6940-3cbc-850e-3f3cf8503bbf | -9.8927 | -47.85604 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b635fa1-9f6d-3231-b82a-d19087f52d6b | -6.99023 | -42.87332 | 2026-06-04 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ffaf04dd-898b-35e8-890c-a23827b31d18 | -8.35214 | -48.14354 | 2026-06-04 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2dfe2b1c-4ecb-31ac-bf6b-80494a065152 | -6.98795 | -42.8876 | 2026-06-04 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| d7f4a705-c502-3953-830f-9349faf7f965 | -10.00736 | -46.55052 | 2026-06-04 04:08:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0105cf7f-91c0-3217-b812-dfb76da66e7c | -4.36299 | -37.89918 | 2026-06-04 04:08:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9f2505b2-f6bd-3cde-a3a8-4d3d4620ce68 | -9.3679 | -47.08603 | 2026-06-04 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d92b2f9a-97da-3691-84f1-8c5777181b85 | -7.48683 | -47.50462 | 2026-06-04 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 489edbd8-4cb3-3a97-9feb-e3ecac377023 | -9.47075 | -46.06246 | 2026-06-04 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6cc10364-8208-3b7d-9fc0-a25d6c1dfaab | -9.51345 | -50.2616 | 2026-06-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb9d4ca5-a0b4-3b58-83fa-643a59971e9c | -8.29153 | -48.23436 | 2026-06-04 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 279c92d0-9b1e-38b8-b243-c96701f46d4f | -6.98966 | -42.87689 | 2026-06-04 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 593ac257-8aa6-3a59-94d5-690f451917f7 | -9.62818 | -48.88124 | 2026-06-04 04:08:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa67da42-79da-3aaf-961e-b07eeac453bc | -8.57109 | -46.00185 | 2026-06-04 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 548e9a00-94b6-35e0-ae06-088266cfb952 | -9.93223 | -48.00625 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad77cc3e-eaa9-30a9-a2fe-57380af22a74 | -9.5148 | -50.26344 | 2026-06-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20664c37-2251-369e-b6c7-28241d0e9c75 | -7.35083 | -46.2114 | 2026-06-04 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa740478-bdf8-370d-910d-8af48b12d381 | -5.52101 | -37.48354 | 2026-06-04 04:08:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5a3ee224-a1d3-319b-9f43-c6c529da8af3 | -9.92313 | -48.0087 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e518ae3a-9bc6-3f26-85d8-ef23f73f32d6 | -9.51973 | -50.26432 | 2026-06-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README5.md)
