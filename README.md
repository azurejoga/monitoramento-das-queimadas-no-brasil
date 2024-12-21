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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b5091e9-dd07-3c77-87fd-fafe188e3079 | -17.9234 | -39.9526 | 2024-12-21 00:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 85.2 |
| 86f56e21-f389-3158-8fbb-08232a7097be | -2.7908 | -45.8685 | 2024-12-21 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 60645d92-4ae2-33df-ab2a-8d02954c6701 | -12.3709 | -52.4701 | 2024-12-21 00:00:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 303bd8af-aa3d-3740-ad3b-b7397b5e100a | -17.9234 | -39.9526 | 2024-12-21 00:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 160.2 |
| 3fa57eb1-533e-3992-a920-2dbf531e44ca | -17.9242 | -39.9264 | 2024-12-21 00:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| 4463d3db-f250-32c9-8dd0-ad2cb1cc8fa8 | -12.39 | -52.468 | 2024-12-21 00:10:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 3cd37bd7-ff69-3235-8795-0a8f6c33fe82 | -12.3709 | -52.4701 | 2024-12-21 00:10:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 7ec9acdb-e04d-3349-9568-753f592d633f | -2.7908 | -45.8685 | 2024-12-21 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| cb43ab71-4681-30af-bc81-a9af9bf7e3ca | -12.3515 | -52.4932 | 2024-12-21 00:10:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 373025fc-94cc-3c0b-8039-17a7a690201f | -12.3706 | -52.4911 | 2024-12-21 00:10:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 1cbb2662-e32f-3928-9eae-1797aa94ce70 | -1.2943 | -53.11 | 2024-12-21 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 18e51534-5866-3e78-b63b-e657fdbcbed5 | -12.3897 | -52.489 | 2024-12-21 00:10:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| faf014bd-249e-3768-8bed-aef5bf67746b | -2.6992 | -45.5585 | 2024-12-21 00:20:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| bf9fbd63-c482-3c97-ab00-f8fb1ed073d3 | -2.7908 | -45.8685 | 2024-12-21 00:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 9b9122d6-3eee-323b-bf60-f025e72ab76c | -1.2943 | -53.1303 | 2024-12-21 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ddd55d42-c1ca-3da0-9197-e805bb87f7b4 | -12.3706 | -52.4911 | 2024-12-21 00:20:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a630a75d-3205-3c67-96cd-18e8de92775b | -2.6991 | -45.5809 | 2024-12-21 00:20:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 3477eabe-5ff6-35fe-9917-eeb13aa68d3c | -1.2943 | -53.11 | 2024-12-21 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6379e3e6-eb47-3403-b0a8-6ecb96baf389 | -4.3099 | -43.7811 | 2024-12-21 00:20:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| cae04312-3241-35fc-94cb-1bf48180f90b | -9.2403 | -60.3292 | 2024-12-21 00:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 59909c18-6fc1-363b-b986-305b4dabc62c | -9.7008 | -36.2193 | 2024-12-21 00:30:00 | GOES-16 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 138.6 |
| 67a883ad-e464-3cad-9ece-1bd4516e5335 | -1.2943 | -53.1303 | 2024-12-21 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 356d5d5b-6709-37b3-8de4-b8cfd5ba98e0 | -9.2401 | -60.3485 | 2024-12-21 00:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c104a9b9-7722-33ba-be58-2f0eeeb3017e | -1.2943 | -53.11 | 2024-12-21 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| a47798bc-6e00-3ab5-ba7d-b789b586307f | -9.2216 | -60.3302 | 2024-12-21 00:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| f1e586ca-b19b-302d-bd79-7904f7f34f55 | -9.2215 | -60.3495 | 2024-12-21 00:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 27c5e072-8b7a-3cf5-97ef-8f77a306e677 | -15.38683 | -39.38644 | 2024-12-21 00:39:00 | TERRA_M-M | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 13a5d32d-44e1-39bc-8450-f4ca65dcd6cf | -9.2403 | -60.3292 | 2024-12-21 00:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c3b831b1-443a-3d26-899c-515c66334ca0 | -2.7908 | -45.8685 | 2024-12-21 00:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 81ca0034-a79f-34d2-9733-a5f972294235 | -1.2943 | -53.1303 | 2024-12-21 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d29864a1-2383-3d90-ac0b-a4fdf176aa2c | -9.2216 | -60.3302 | 2024-12-21 00:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 0c51906b-fbec-3692-be02-cf041c76a1e9 | -9.2215 | -60.3495 | 2024-12-21 00:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 6827e49e-3244-3fd7-9fed-142f8b2110d3 | -2.6991 | -45.5809 | 2024-12-21 00:40:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 91.5 |
| a752ff9a-26a5-336e-8e5a-58178021a01f | -2.6992 | -45.5585 | 2024-12-21 00:40:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a9e95698-047d-3db3-849c-ffefd5be52f7 | -7.31747 | -39.99113 | 2024-12-21 00:41:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 90e2fb46-42e5-3214-a91d-4051dadf8936 | -7.32696 | -39.97063 | 2024-12-21 00:41:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 86da7406-5be4-352c-9183-1d6cad129e64 | -12.85305 | -43.81434 | 2024-12-21 00:41:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f7bd3636-2f4a-33ca-89f5-5f99fac127e3 | -7.32525 | -39.97748 | 2024-12-21 00:41:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 15891b86-046a-35a1-b385-43c99920044e | -7.32245 | -39.95889 | 2024-12-21 00:41:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 17.2 |
| b503130a-a96a-3518-91cb-7f6424037386 | -9.49504 | -35.94525 | 2024-12-21 00:41:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 33.9 |
| 9f770801-8956-3d47-b00d-1bd854e0bb88 | -11.00335 | -44.34467 | 2024-12-21 00:41:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d7e3d26e-5d30-39ff-9204-c109cf95baa2 | -12.85438 | -43.82366 | 2024-12-21 00:41:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd8ba63d-47d3-37cf-9538-bd5fa8843b6e | -11.85898 | -46.95262 | 2024-12-21 00:41:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1cc5335a-9074-33d9-9a00-19d5bca42ffe | -9.48483 | -35.94197 | 2024-12-21 00:41:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 34.5 |
| 30bd6f0e-3633-3d1e-a925-ceb62c4fb8ab | -2.78874 | -52.9592 | 2024-12-21 00:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 3dba64bc-9d84-3dbd-8de0-4f5a1f0be8dc | -3.3181 | -45.6285 | 2024-12-21 00:43:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 29812deb-e8c1-3e7e-ae14-3696197f5927 | -5.60918 | -42.83125 | 2024-12-21 00:43:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 0142b263-9251-3a01-9013-eaa3c4f751d5 | -4.30396 | -43.77479 | 2024-12-21 00:43:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d6f8f3f0-ddb5-3641-86e2-9e17cd9e0a97 | -2.55359 | -46.87677 | 2024-12-21 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 31a62961-1395-39e3-9e5b-f97e9a84a5ed | -1.92214 | -46.31434 | 2024-12-21 00:43:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8228c9f4-1723-3866-a582-51a331c3bf61 | -1.56137 | -46.76861 | 2024-12-21 00:43:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2fc985c8-88f2-3879-8d4a-cd4e71e1cdc5 | -3.15521 | -44.26965 | 2024-12-21 00:43:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1c35de40-60b2-38f7-a0bf-01dab6c94f70 | -2.67188 | -46.93462 | 2024-12-21 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 83ef0c76-4e63-3fa0-b57a-ee78760d278c | -5.17899 | -43.95319 | 2024-12-21 00:43:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 10baf9e5-b552-37aa-a826-9f77f0749cea | -3.47465 | -44.98025 | 2024-12-21 00:43:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f76f2a03-1a27-33b9-aa9c-8c3a0d4a177f | -5.9167 | -43.4786 | 2024-12-21 00:43:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 393bea5a-32ab-3f13-a997-1b4296d3bc16 | -2.70348 | -45.57886 | 2024-12-21 00:43:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| cc002aef-684f-31f8-89c8-79eef5829493 | -3.89808 | -40.98131 | 2024-12-21 00:43:00 | TERRA_M-M | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 74ae5b7a-73b2-37cb-af16-33c082c69e9c | -2.85413 | -46.7259 | 2024-12-21 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 277af588-d62a-3c33-a6d4-66ca842bb0c5 | -1.87679 | -45.06858 | 2024-12-21 00:43:00 | TERRA_M-M | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e0afe6f9-78e0-3bd6-a890-8ae2ff5a55ed | -3.95456 | -46.41891 | 2024-12-21 00:43:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9436f6c7-fa51-3324-8214-22cf56026d71 | -4.31378 | -43.77337 | 2024-12-21 00:43:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 31a8dfd4-1537-32d9-b9b8-768f274a0f58 | -6.41932 | -43.77739 | 2024-12-21 00:43:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8ae5e7c7-be68-300e-8c20-4a3d0d663f19 | -5.22395 | -44.90578 | 2024-12-21 00:43:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c422a735-1e4f-34ce-95e0-7d2dacbdc408 | -2.70218 | -45.56952 | 2024-12-21 00:43:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 158.9 |
| fc7382fc-5a59-31c7-9bdc-21e6ed277dfb | -4.30299 | -43.78093 | 2024-12-21 00:43:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1de8c80d-7f00-3ccf-858a-dbecab3c47fe | -2.77107 | -47.38791 | 2024-12-21 00:43:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2cc35533-c173-3302-a81d-95ece9e4cb47 | -3.83418 | -46.68224 | 2024-12-21 00:43:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 21a12e88-2634-3b2a-a427-905a0af61d5a | -2.78908 | -45.8623 | 2024-12-21 00:43:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2dca2364-98e1-3691-862c-0501976f3eb4 | -2.68073 | -46.93337 | 2024-12-21 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 87c33c5b-fae5-33e7-a9c7-85a75876f53b | -1.87996 | -45.54994 | 2024-12-21 00:43:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a103364b-e3ce-3f70-ae3d-850dca9d4371 | -2.12244 | -45.64113 | 2024-12-21 00:43:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f2ccedf6-8540-3dcb-ba4d-79d47b9974f1 | -2.78623 | -52.94099 | 2024-12-21 00:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 9f3877ea-8e40-338d-9370-7e578851865c | -3.71924 | -44.62514 | 2024-12-21 00:43:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| df820404-4525-3097-b58b-4c04512ee7c0 | -2.76344 | -47.398 | 2024-12-21 00:43:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 68e93925-a803-37f1-beda-77ade2ab00ce | -3.81131 | -46.71245 | 2024-12-21 00:43:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b0810711-01a8-3270-8330-a98c49ce2b82 | -4.09237 | -48.48263 | 2024-12-21 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 43ad76c5-4af9-3a76-9e22-496008149925 | -2.55482 | -46.88559 | 2024-12-21 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 7982a27d-68cf-37f1-9379-faf350b0b34e | -6.68427 | -46.38599 | 2024-12-21 00:43:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c8c85b6f-c1d6-36af-82fe-431abb7af9a6 | -3.46539 | -44.98158 | 2024-12-21 00:43:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dbf4a9bf-ea04-347c-8afc-4281b4cb930f | -2.13156 | -45.63984 | 2024-12-21 00:43:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ad73c8e-bef9-3b11-b38b-0942eaf37234 | -3.4557 | -42.01168 | 2024-12-21 00:43:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 567b70fd-b1f8-33ea-b0d4-d186ad5c81f4 | -2.79683 | -45.58827 | 2024-12-21 00:43:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6437db7e-759f-3e2c-80f0-3b1c4d1fd8fa | -3.81025 | -45.98194 | 2024-12-21 00:43:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8f61278e-bcec-37cd-837f-0680566fde0b | -3.80097 | -46.84567 | 2024-12-21 00:43:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6706e98a-b803-347c-806f-21215619d44f | -5.55715 | -46.35765 | 2024-12-21 00:43:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4b26aaa7-9d19-35cd-ac9b-8af523643259 | -3.29142 | -42.5317 | 2024-12-21 00:43:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 53efea50-d387-3ad7-98bb-dd02ed27a5f8 | -2.7723 | -47.39675 | 2024-12-21 00:43:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e1753d02-3dfd-3800-839c-cb81bf2ac226 | -4.10736 | -46.724 | 2024-12-21 00:43:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1bd1f5d5-a741-355a-b8b3-c63cdb88fb20 | -2.56096 | -46.92965 | 2024-12-21 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dba9af73-67cf-3ff8-9b5d-b947fabb8c7d | -2.85536 | -46.73473 | 2024-12-21 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8c64913b-0287-3860-b057-39dba1f47932 | -3.06943 | -47.48137 | 2024-12-21 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9e147728-a112-3e14-be0f-e6d2e4369a5a | -5.69135 | -46.53101 | 2024-12-21 00:43:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c0ba123-db5c-3c39-bd96-fe841c6555c4 | -2.70847 | -46.13861 | 2024-12-21 00:43:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c5999cb0-8b49-3fe3-bdb3-911cccd943b2 | -1.8754 | -45.05862 | 2024-12-21 00:43:00 | TERRA_M-M | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5784634e-3e68-34d2-940a-c6a680bca49f | -2.63177 | -48.03869 | 2024-12-21 00:43:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0ff1416d-2c18-3edb-b809-763d0840ba0c | -3.3093 | -42.27047 | 2024-12-21 00:43:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e4167955-51cd-340b-86db-5d74793800da | -5.91951 | -43.48339 | 2024-12-21 00:43:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| eab04e69-9dff-3270-8f03-b13470501aa9 | -2.65736 | -46.10627 | 2024-12-21 00:43:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a44b703b-c63d-38ce-a4c3-3ce73101501e | -4.92934 | -41.32541 | 2024-12-21 00:43:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |


[Clique aqui para ver as próximas entradas](README2.md)
