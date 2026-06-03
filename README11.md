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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11eadb1f-a0b2-39ed-95d7-61163c61a67c | -22.96551 | -52.69552 | 2026-06-03 05:23:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2c0f1497-9460-308c-a52e-103cb86b7a92 | -15.45426 | -55.8367 | 2026-06-03 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ae5d56a-c593-3166-866c-0f147c7267c0 | -21.81085 | -49.12041 | 2026-06-03 05:23:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 59904b64-24f3-3459-8a0b-d19a8f53d931 | -11.6302 | -55.17304 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9ebee19-d8a4-36ce-b152-9bf42f5b0f22 | -11.6262 | -55.17247 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 520bad31-4ffe-35b6-95a9-1ab19cc788b5 | -11.79846 | -54.02023 | 2026-06-03 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1ca9d456-0c38-3f5f-8afb-ebbb80168666 | -21.70383 | -48.41478 | 2026-06-03 05:23:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6701309-b0d6-3817-999d-80e3873c1f68 | -11.26165 | -54.72575 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d42613b-1b23-3014-a4fc-53ed0ab37f1f | -16.14852 | -58.49078 | 2026-06-03 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 00738f20-67a6-3a89-92d5-f84465e22188 | -10.8643 | -53.7469 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03b4924e-b916-31cd-8f1c-c2ec2e40f7e1 | -14.03232 | -59.56081 | 2026-06-03 05:23:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30d416d7-6270-39f9-97db-c37a8031eb0d | -11.26638 | -53.97299 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a45bf8c6-b290-3ce6-8934-4e3b7cdbb92e | -21.29448 | -56.10469 | 2026-06-03 05:23:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1b98072-fc06-3b18-849b-b1d62a5d5cf4 | -10.86109 | -53.73769 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1f030f9-29af-31c8-809c-760e92d87867 | -10.03039 | -59.3478 | 2026-06-03 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd1a347a-8cbc-30cb-bdf8-decae960c168 | -11.62467 | -55.18306 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bca1ea23-629a-32d3-919a-d61922d7dd21 | -11.88566 | -57.83833 | 2026-06-03 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03b6b6c3-99d9-3aea-9c56-f9b032bc15be | -11.5651 | -54.57676 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 395a5b9a-5393-3211-a02d-b6e14bb3df6f | -11.26509 | -48.35722 | 2026-06-03 05:23:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 906b410f-4993-3e23-917a-9cf9bf61e931 | -11.79451 | -47.34001 | 2026-06-03 05:23:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2db675ec-7c6e-31fb-99a1-c6f9e8203342 | -14.08358 | -59.38225 | 2026-06-03 05:23:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9614c7c4-811e-354c-b615-3ad7b6ac7890 | -11.56873 | -54.58112 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c21577f4-b277-3fa8-8c35-3b1c725191b8 | -12.73884 | -54.20543 | 2026-06-03 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fda57076-e1d8-363e-b8b6-4ab30ff685de | -16.14911 | -58.48667 | 2026-06-03 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| de38a68a-d4e4-36ab-95cb-32ddccd2d12a | -12.8062 | -54.86118 | 2026-06-03 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d98d7902-f761-3b06-a626-dfb1f834d9d5 | -11.81372 | -57.35516 | 2026-06-03 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 547669b7-2c6b-3f32-8ed3-cb52e5b0f3c5 | -10.86293 | -53.74779 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5538cea-f358-310b-b05e-f76c59d85086 | -10.86981 | -53.73892 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d394a55e-080c-391f-8a83-5650b99666df | -18.7149 | -56.57635 | 2026-06-03 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| d5f1b42d-c195-3aa1-9a4c-7aaaee2dbbed | -18.71942 | -56.57322 | 2026-06-03 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e1c64d39-b597-315e-8734-2495b8dda31b | -18.46252 | -54.70637 | 2026-06-03 05:25:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a7badb6-a00f-31bc-bd4c-fdbad064dcc0 | -19.16711 | -55.18587 | 2026-06-03 05:25:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d371d271-7c75-3d73-88d9-c91f8235d6a1 | -18.72798 | -56.57066 | 2026-06-03 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 70424c21-1e73-3ae6-9523-1e58bdfb36e4 | -18.72394 | -56.57009 | 2026-06-03 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0d99a285-2012-3723-a3f0-d4ed8aecf777 | -18.72346 | -56.5738 | 2026-06-03 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 639eaff4-357a-31ec-a05e-16fe24283d3c | -19.16768 | -55.18129 | 2026-06-03 05:25:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b6b5541f-8ea1-3089-bfb0-6ba636087072 | -18.46336 | -54.70792 | 2026-06-03 05:25:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35a9bc85-8488-3d64-bbd6-42b381565d05 | -18.71894 | -56.57693 | 2026-06-03 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 894e7bce-94f1-3557-814b-1ae5cf1b4944 | -19.16601 | -55.18326 | 2026-06-03 05:25:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9698e3a8-3506-3c56-8696-d3c1a6b111de | -19.16547 | -55.18785 | 2026-06-03 05:25:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b5147441-af06-377f-9150-92f496224c6b | -11.7528 | -47.07204 | 2026-06-03 06:08:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| ea5d752c-9180-3087-890c-35449dc503cc | -5.72069 | -45.03873 | 2026-06-03 06:08:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| af73f6ea-712c-3646-af48-e2b9e2d26d79 | -11.75347 | -47.07774 | 2026-06-03 06:08:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| bff47246-c371-3ab7-87f2-a0aaa5ec0a49 | -5.7228 | -45.02557 | 2026-06-03 06:08:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| dbdadcc1-277f-37ed-bb35-5a63090a3f6a | -11.79102 | -47.33569 | 2026-06-03 06:08:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9c8d90cc-5d1d-3906-830f-86d8e98590cf | -11.75601 | -47.06289 | 2026-06-03 06:08:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| cddbb62e-8f53-33d2-8e6b-1a13d5b3d9d8 | -8.56721 | -45.99943 | 2026-06-03 06:08:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 710a62d7-c854-3239-9e8c-663b80f2a7b4 | -17.44514 | -42.62374 | 2026-06-03 06:10:00 | AQUA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b3e45ee8-e337-350a-b309-58aa7e217345 | -21.80995 | -49.11197 | 2026-06-03 06:10:00 | AQUA_M-M | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 3a2f2778-984e-30dd-a2ce-209e040c76cc | -16.57878 | -45.87403 | 2026-06-03 06:10:00 | AQUA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| bbd3e12a-05f4-34dd-a062-1e58ba7bea6f | -6.76438 | -45.00997 | 2026-06-03 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 0032ad92-d24c-3b62-9f34-b448f108075a | -8.57298 | -46.00063 | 2026-06-03 11:34:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d21d61e9-3eb3-34a3-9c80-2be94872ea90 | -14.04948 | -46.33278 | 2026-06-03 11:34:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5ac6b6c6-b0a0-3ca5-bcd2-923371bf0738 | -7.01248 | -41.67106 | 2026-06-03 11:34:00 | TERRA_M-M | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 369e5d9b-4cfe-3a55-9422-d364dec942c3 | -11.80152 | -47.33966 | 2026-06-03 11:34:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 67c727c7-1596-3ef5-9801-c2986299714e | -8.26952 | -48.23545 | 2026-06-03 11:34:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 9485998e-0b0f-39fa-864c-174492ac495f | -9.06173 | -44.78457 | 2026-06-03 11:34:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1c145952-5b81-3815-b4eb-e856114fd295 | -11.7547 | -47.07785 | 2026-06-03 11:34:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9ddb8a04-9cc4-35a7-aaa0-d42015c3eac0 | -9.2386 | -40.33837 | 2026-06-03 11:34:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| fd36c7c9-8f56-3aee-9114-28db0aee52cb | -8.06059 | -46.19522 | 2026-06-03 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e06e2a7f-22ae-3ffe-8be1-78d85eddffa9 | -11.76171 | -47.07238 | 2026-06-03 11:34:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 48e872b8-f0f4-3ce3-95dc-e1404246169f | -13.55863 | -46.65142 | 2026-06-03 11:34:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 49dae18c-99fe-31d7-9cc2-686b1293a88f | -6.98734 | -42.8768 | 2026-06-03 11:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| b0c37b55-608b-304c-b6e5-3fffb9da1cd4 | -14.06115 | -44.04271 | 2026-06-03 11:34:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 27c169a3-7e80-3184-a2db-0e93dfb21c90 | -11.07507 | -43.13829 | 2026-06-03 11:34:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| be9ae209-ad8c-3db9-a44d-89a82bc65c63 | -7.05408 | -45.06007 | 2026-06-03 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 62073d44-185d-3565-873a-87fcafcd7278 | -14.04774 | -46.34399 | 2026-06-03 11:34:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 577b025a-c778-397d-abe6-8989fbef6df0 | -6.76268 | -45.02127 | 2026-06-03 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| ed28bff8-c8fb-3247-9840-0b7471e82264 | -8.06269 | -46.18147 | 2026-06-03 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 83b8ad72-399d-39e8-b12c-c4249cfaa16e | -5.60543 | -43.36343 | 2026-06-03 11:34:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 8eabf5ee-5095-3e00-a71a-7a01c31b5194 | -16.58475 | -45.87808 | 2026-06-03 11:36:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3df3e28d-626e-3ad1-b4f5-48fbc9138078 | -18.34184 | -40.46823 | 2026-06-03 11:36:00 | TERRA_M-M | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| be8d773f-e60c-32b6-847a-a330d4d8777a | -17.50167 | -48.00119 | 2026-06-03 11:36:00 | TERRA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 252399ed-bb5f-35a6-9971-f54944e334c7 | -16.75168 | -42.35384 | 2026-06-03 11:36:00 | TERRA_M-M | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 99f8e9d8-1bd9-3c0b-9ba6-db5cb520902b | -22.78727 | -49.34058 | 2026-06-03 11:38:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 91ed3195-b5e4-384d-9a13-ffe0b753eda8 | -12.556 | -57.1798 | 2026-06-03 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 3ceaff4a-454e-387c-bbfb-427a4d55b710 | -10.363 | -46.9343 | 2026-06-03 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 58e6707d-834a-3ab4-a424-1374c6437083 | -12.7463 | -54.1969 | 2026-06-03 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 898fabd6-50a7-3400-baa5-b2dff5f7e250 | -12.537 | -57.1814 | 2026-06-03 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 7f109cf5-a521-3f4e-8443-f1b93d886ff0 | -12.556 | -57.1798 | 2026-06-03 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 3bc4b61d-4fe3-3ad6-8101-e0fbebf68ad7 | -12.537 | -57.1814 | 2026-06-03 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 076988ab-9de8-3311-966b-c638fac99e8d | -12.556 | -57.1798 | 2026-06-03 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 799c10e3-63d8-38a0-89ff-eda2b8e480ff | -12.06304 | -57.41513 | 2026-06-03 13:14:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 17148ee3-e420-3afc-9aa7-6e236abda8c1 | -11.88134 | -61.03703 | 2026-06-03 13:14:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 30.7 |
| adb35732-ae54-3617-b628-d66fe88aa495 | -12.54193 | -57.17108 | 2026-06-03 13:14:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| d19cfd34-424f-3311-beb0-7bc4e3b80e55 | -12.56072 | -57.17764 | 2026-06-03 13:14:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 133.0 |
| f2ad4c40-bad0-3109-bf53-1d15365b11b6 | -12.56188 | -57.18474 | 2026-06-03 13:14:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 41d02670-fc10-35eb-8947-05cbc52a03a2 | -14.15266 | -58.96965 | 2026-06-03 13:14:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 82617596-192d-361c-bf8a-c5309a286709 | -12.04944 | -57.42092 | 2026-06-03 13:14:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 303efd50-c700-37c9-9825-62c450e49dec | -14.16677 | -58.94465 | 2026-06-03 13:14:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| b1807c2a-0e77-38e0-91e3-9da7d1301e52 | -12.54323 | -57.17624 | 2026-06-03 13:14:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 169.9 |
| f3a46c7e-aa8f-3719-b480-233186a6f213 | -14.16349 | -58.97617 | 2026-06-03 13:14:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 4d747b8b-1ae6-3ba2-a865-7d6fe48d5da0 | -11.88096 | -61.04248 | 2026-06-03 13:14:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 25.0 |
| b03d59a7-a6bb-3d91-8ee3-6c941479763f | -12.537 | -57.1814 | 2026-06-03 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| b0fe3ffd-b421-33fe-b889-5d2f86574819 | -12.556 | -57.1798 | 2026-06-03 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 226.1 |
| 24915927-90e5-3f4e-b0b9-3421601cd9a8 | -12.537 | -57.1814 | 2026-06-03 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 988c1934-1601-30fb-9134-81dab8747fac | -12.556 | -57.1798 | 2026-06-03 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 192.5 |
| 133ef2d7-6fe6-3d11-8ecb-e7ef13b09ef0 | -12.7463 | -54.1969 | 2026-06-03 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 712b4bb9-e70e-3120-b60c-262bc71d40ef | -12.537 | -57.1814 | 2026-06-03 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 143.2 |
| e680d878-de59-3587-a37c-8f6f27e758e0 | -10.6799 | -49.9402 | 2026-06-03 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |


[Clique aqui para ver as próximas entradas](README12.md)
