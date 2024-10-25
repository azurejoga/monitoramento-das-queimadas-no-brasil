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

## Dados Diários - Página 199

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44421c1f-26e6-3e1b-b7be-76cff07f0cf0 | -5.2838 | -48.3218 | 2024-10-25 19:45:35 | GOES-16 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1d8f3959-59f0-344e-b1c0-d23ee2454c8a | -5.2673 | -45.5688 | 2024-10-25 19:45:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 1df1e8ce-f98a-3a85-a9aa-c7dd2302f29d | -5.2236 | -41.7945 | 2024-10-25 19:45:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 149.5 |
| 8ade6963-7df3-38e3-be78-8057407ae8c2 | -5.2426 | -41.7692 | 2024-10-25 19:45:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 5e3bc3aa-d2a3-373f-b6fb-2d49abc0dde3 | -5.2919 | -44.8208 | 2024-10-25 19:45:35 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 40467d28-1711-39d7-b9b3-d81404f5a31b | -5.5815 | -43.7448 | 2024-10-25 19:45:37 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 88536ddd-7e9e-30cf-ab54-e252d189e643 | -5.7201 | -45.0186 | 2024-10-25 19:45:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| f44e010c-3270-3801-8c56-b958ee6f0ff0 | -5.7014 | -45.0199 | 2024-10-25 19:45:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| a4bb19fe-01a7-3f70-b256-1cfc659494fb | -5.8323 | -47.1987 | 2024-10-25 19:45:38 | GOES-16 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 16e8da5f-0442-34f7-99b6-94769d6238d0 | -5.8324 | -47.1767 | 2024-10-25 19:45:38 | GOES-16 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| a8b32232-21ea-3e0e-82d9-e7a5e4669dde | -5.8961 | -44.16 | 2024-10-25 19:45:38 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 67c89fda-a021-3515-a9e0-1a1b939657ab | -6.1324 | -47.0022 | 2024-10-25 19:45:40 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 5ecbf206-1b3f-363e-85c6-1d0adfe5f84e | -6.2931 | -47.824 | 2024-10-25 19:45:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| cc5af3da-d4f0-36ba-8ffb-f69649c37d1e | -6.2744 | -47.8253 | 2024-10-25 19:45:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| c3324cb4-72a6-38de-826f-99709fbcdc31 | -6.7045 | -43.9554 | 2024-10-25 19:45:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f588a54d-0849-30e8-84db-f4fd74cbd501 | -6.9179 | -40.0358 | 2024-10-25 19:45:44 | GOES-16 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 2d6f30d8-f47c-3484-bcb4-db63e091e343 | -6.8919 | -59.7821 | 2024-10-25 19:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.4 |
| da9c0bc6-162c-37f7-be97-2cf8a506d00f | -7.0736 | -46.3312 | 2024-10-25 19:45:45 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 9c0af935-989e-3bb8-b856-3fbb8fc3e755 | -7.0548 | -46.3327 | 2024-10-25 19:45:45 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| b43acf9b-5827-3d0d-8766-cbc3bcaaa689 | -7.1861 | -46.3217 | 2024-10-25 19:45:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 68ccbdcc-e7e1-3af9-978f-d58e1e036cc4 | -7.1357 | -49.5111 | 2024-10-25 19:45:46 | GOES-16 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 65384b85-4f74-3b96-b620-1b6cae82d199 | -7.2943 | -44.9817 | 2024-10-25 19:45:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| d2d421cf-1695-3d11-9125-3a4cb9e6836e | -7.3131 | -44.98 | 2024-10-25 19:45:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 117c1985-fde3-377c-99b5-0348bd749a88 | -7.5289 | -45.8434 | 2024-10-25 19:45:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 7b30d851-bebf-35f4-9184-ad7aae0154ec | -7.6769 | -42.8573 | 2024-10-25 19:45:48 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 7c365f69-03b7-31ed-96cb-d2951c936deb | -7.5559 | -46.8017 | 2024-10-25 19:45:48 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 3fb01218-904d-3513-bcbd-3d2e88bc39d8 | -7.5477 | -45.8417 | 2024-10-25 19:45:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 2bdc400f-ed0f-3380-bb98-b7afc07cb524 | -7.6815 | -47.3213 | 2024-10-25 19:45:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| bebfaacb-00a8-3ee3-9d4a-79cde062f13d | -7.6817 | -47.2992 | 2024-10-25 19:45:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 36d59d98-55a7-3afd-80ba-b2859f4458d5 | -9.0635 | -48.0051 | 2024-10-25 19:45:56 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 4d75201e-fec9-3151-84ee-0f0a8cfe1319 | -9.0824 | -48.0032 | 2024-10-25 19:45:57 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 146.2 |
| bbc7a9c8-ffb3-3662-8f57-4e57cfe2f9d4 | -9.5937 | -46.4418 | 2024-10-25 19:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| e051b343-60ae-36a0-9bd9-0b5a777fdda3 | -9.5073 | -47.2319 | 2024-10-25 19:45:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 22b0dae0-0fc5-33f9-9d26-78a76f1390da | -9.8201 | -47.8386 | 2024-10-25 19:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 47284bc0-7ce3-3726-aacd-871b596dcdfa | -10.5753 | -44.287 | 2024-10-25 19:46:05 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 230.1 |
| 49944ff5-16f8-3d50-8226-5f3a0a4cf582 | -10.6139 | -44.2584 | 2024-10-25 19:46:05 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 18a99b3e-7696-3b47-a7d2-9c6b1eb15402 | -10.6135 | -44.2817 | 2024-10-25 19:46:05 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 8ffd300c-cb30-3f8c-ba5c-72a870080cf2 | -10.6046 | -52.816 | 2024-10-25 19:46:05 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| a11d9538-bb9d-382d-b776-2677161a9b05 | -10.5944 | -44.2844 | 2024-10-25 19:46:05 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 69f41711-f1d5-3d23-96bb-f2879901107e | -10.5948 | -44.261 | 2024-10-25 19:46:05 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| e8dad4c4-a784-3b6c-9f1e-04b94a9712f9 | -10.6249 | -55.9757 | 2024-10-25 19:46:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 0ef34de5-a337-33ee-8d6e-47bb2365cb13 | -11.5357 | -43.9853 | 2024-10-25 19:46:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 57085258-ea63-39eb-b5f7-1a7b36ee5938 | -11.7095 | -43.9119 | 2024-10-25 19:46:11 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 06fcd196-86a7-3840-894d-fad7888f072b | -11.6707 | -43.9413 | 2024-10-25 19:46:11 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| d02e35bd-5650-39a7-a396-318dce24f695 | -11.9642 | -44.6676 | 2024-10-25 19:46:12 | GOES-16 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 2dab929d-f496-3cd2-8b1e-0c519e19a9b2 | -11.9028 | -43.8348 | 2024-10-25 19:46:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 20f079fe-5193-3c34-97a9-a9faa52bc526 | -12.4612 | -43.7921 | 2024-10-25 19:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 894e4e4c-8371-3fb6-a89e-07dead12bb7e | -19.6028 | -56.8996 | 2024-10-25 19:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.1 |
| 266b9e4e-4795-373e-b957-6df134a022af | -19.6233 | -56.8758 | 2024-10-25 19:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 9d597bef-3b04-395b-b352-9a85d2afa388 | -19.6615 | -56.9751 | 2024-10-25 19:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.6 |
| c63c3b02-00d0-37da-a59a-1c25a20b6bd3 | -19.6229 | -56.8968 | 2024-10-25 19:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 181.1 |
| f64c998f-65d0-3f60-a27f-a189daf2acec | -19.6253 | -56.7709 | 2024-10-25 19:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 1f01aa36-85da-3fa3-948e-76d71c3c8a41 | -19.6225 | -56.9178 | 2024-10-25 19:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 7a8fb410-6f62-390f-8f45-0ac8e86ed385 | -19.6438 | -56.8521 | 2024-10-25 19:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.8 |


