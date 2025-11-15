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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b84e6656-9875-3f1e-a7bc-324c8627ce24 | -7.4554 | -42.559898 | 2025-11-15 00:18:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8f977c5b-5153-3944-b921-b8afa14d6740 | -4.504 | -44.583801 | 2025-11-15 00:18:00 | METOP-C | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49c3277a-5e11-3c35-9181-435b1b13a558 | -10.9941 | -44.6973 | 2025-11-15 00:18:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| af86549e-db8a-3800-9c01-62c8e25c5d0c | -12.4296 | -43.176399 | 2025-11-15 00:18:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2940a91-ed73-38fe-834d-ba07f769486d | -4.5525 | -43.527302 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f42d949-dc95-3658-9316-1a0c223727cd | -3.9836 | -47.665298 | 2025-11-15 00:18:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd7f8a5d-11df-3193-a888-49640cf740b1 | -7.457 | -42.566799 | 2025-11-15 00:18:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6be7b2d5-8cee-3b39-8677-5fea40bba68e | -8.3183 | -45.411499 | 2025-11-15 00:18:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bcc1b934-dc16-3647-8eed-1ef1cb37abad | -4.8548 | -40.7589 | 2025-11-15 00:18:00 | METOP-C | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1f2861ae-a806-3ebf-9dc5-3dbf71ae964a | -11.6949 | -48.394501 | 2025-11-15 00:18:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cbdad23-13ee-3365-a201-f3bcd5aa4df7 | -4.2685 | -44.590099 | 2025-11-15 00:18:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a973493-eb26-3c47-83ae-94de65ea60e8 | -2.9503 | -48.592701 | 2025-11-15 00:18:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c8d7df8-3482-3c26-9653-d4573a30110a | -5.0349 | -43.6091 | 2025-11-15 00:18:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 191bad9c-a2d4-3de6-a97c-ff5edc2dc000 | -3.2627 | -43.6124 | 2025-11-15 00:18:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb999044-370b-39dd-98ef-60e3025f61a3 | -4.6418 | -44.737999 | 2025-11-15 00:18:00 | METOP-C | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3cf8d34a-1a7e-39d2-a432-a7a3040d2656 | -6.0342 | -45.809399 | 2025-11-15 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd67cbd5-2360-3ec1-a096-1b8bc4dd8bbe | -7.0759 | -41.575802 | 2025-11-15 00:18:00 | METOP-C | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c779a08f-3fa9-3052-96ca-8d9da44d66ed | -12.0264 | -43.730701 | 2025-11-15 00:18:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4317e4-0465-3da5-8b6d-334fb8060938 | -4.8772 | -44.960098 | 2025-11-15 00:18:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00636664-63f1-3b40-aa33-e61233a8d198 | -4.9186 | -44.778 | 2025-11-15 00:18:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0c5ec04-2cab-3bc7-ba42-fd27ccf7ee95 | -8.738 | -44.239201 | 2025-11-15 00:18:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 88d88ba5-9b91-3755-a3bb-309557459a62 | -4.409 | -43.349701 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42ff8477-845f-3a6f-92c6-868ca61be47c | -5.3872 | -44.847801 | 2025-11-15 00:18:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbb7ac7c-7d9b-33e8-b11c-c3d1249f3038 | -7.8751 | -48.378101 | 2025-11-15 00:18:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50727dfa-1e4f-3ed2-b9cd-44fbca3b9d50 | -4.83 | -44.750702 | 2025-11-15 00:18:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23ec36f0-7b21-33ec-a1e1-8f2332ca9912 | -5.5123 | -40.969398 | 2025-11-15 00:18:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b879a996-d9f8-35d8-b9c1-f448af69205b | -2.4249 | -48.037601 | 2025-11-15 00:18:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65707ef2-e0a2-3828-a0c1-e7df4f31f624 | -10.3399 | -48.919998 | 2025-11-15 00:18:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a57d1584-8f17-3e3b-a691-034aef048a2c | -8.9912 | -44.175598 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5452417a-bc07-3cc4-8b96-9873ca10a131 | -12.4685 | -43.734299 | 2025-11-15 00:18:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4ac5b7ea-82d1-3e5b-b159-ae280fa436ce | -11.3168 | -49.7425 | 2025-11-15 00:18:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15e4a272-39f7-37d6-a461-5f2b8cdfe851 | -5.2329 | -44.346401 | 2025-11-15 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06455fcb-a1ff-3faa-98c8-462984b73600 | -6.0079 | -41.955299 | 2025-11-15 00:18:00 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2f3055ec-92d2-38d0-83f2-b35501bd5986 | -8.5829 | -46.060501 | 2025-11-15 00:18:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbbd009f-4baf-3328-9f16-2398c72970c1 | -3.3508 | -46.859501 | 2025-11-15 00:18:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6d755a1a-17fb-3669-b41d-169abcbab486 | -6.4619 | -35.0797 | 2025-11-15 00:18:00 | METOP-C | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4a88a8e3-dee8-3180-8d01-362d26ca713a | -4.4757 | -42.874901 | 2025-11-15 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88bbb3fe-3cf1-32c0-ba29-2ec90a98ad2e | -6.0902 | -41.5952 | 2025-11-15 00:18:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cd80a654-a3f4-352d-b60d-53aed0ea9cb5 | -2.6367 | -45.478199 | 2025-11-15 00:18:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c238a087-69d4-3778-b808-76a9059fd9f8 | -4.7331 | -47.160599 | 2025-11-15 00:18:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab9b688c-9072-3fdd-8629-75b379c09193 | -8.1902 | -44.829399 | 2025-11-15 00:18:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f560194e-0c92-36fd-a6de-6e9d2517fd31 | -9.7987 | -42.2146 | 2025-11-15 00:18:00 | METOP-C | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| faeb9d62-b17b-3e1e-aeb3-ed394a594409 | -4.2701 | -44.597401 | 2025-11-15 00:18:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a0204be-3bb9-3a3a-93bc-53a256b3ad1f | -6.1503 | -48.056599 | 2025-11-15 00:18:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1decdabf-3422-3af9-86cd-89e70c014da7 | -3.1164 | -45.277599 | 2025-11-15 00:18:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2124f6f5-6de3-38d1-a68c-770ffd87e455 | -4.6394 | -47.9384 | 2025-11-15 00:18:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37162ac5-bce1-381b-a847-15a57d2a25c7 | -20.144199 | -41.638699 | 2025-11-15 00:18:00 | METOP-C | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8923d825-7706-3651-a195-6f207b4a51b0 | -8.3072 | -43.643299 | 2025-11-15 00:18:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 52b2932f-cb75-31e5-b5e6-6d587c79851a | -3.3131 | -45.691002 | 2025-11-15 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f34fd53e-2e3f-3673-8d5e-8bd032e771db | -2.5047 | -47.800098 | 2025-11-15 00:18:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed341780-8c31-3509-97eb-320667e308d5 | -7.7099 | -42.727901 | 2025-11-15 00:18:00 | METOP-C | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 332e900d-2a74-38ac-87f5-e48dbe00d75d | -3.998 | -44.170101 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4723eaaa-9f51-3f03-b08d-2ba47543e50e | -14.6874 | -46.6008 | 2025-11-15 00:18:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6216f6fb-d166-3b21-a50d-37e67e5d6a54 | -3.991 | -44.275501 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1488d6c8-c27c-3a73-8a8b-02041edebb19 | -17.5825 | -46.677601 | 2025-11-15 00:18:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| efff9acc-ebfb-3c90-80dc-5fd48c048095 | -9.8522 | -44.166 | 2025-11-15 00:18:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 46e46389-cb75-37ee-9c35-6777fff0f36b | -3.3806 | -46.034698 | 2025-11-15 00:18:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2cea3a2f-3d17-3a27-8a8a-55916e9155c6 | -4.5873 | -44.3153 | 2025-11-15 00:18:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30b5be8d-c404-395c-aaf2-0ffb022f8386 | -4.4289 | -43.663799 | 2025-11-15 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 705edf6c-4a8f-3563-8ae0-582491c0c79d | -13.3573 | -43.7183 | 2025-11-15 00:18:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6dabf859-1e39-3a39-90b4-4da1d017eedf | -6.7194 | -42.9496 | 2025-11-15 00:18:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e3f07c74-aa68-3681-bd84-6a9690907949 | -4.8334 | -44.765598 | 2025-11-15 00:18:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8456792a-b9cc-371e-8eed-f7a34f3cd40d | -4.9066 | -44.042702 | 2025-11-15 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 639c9b4c-5bfb-358b-b109-2224841a4e6d | -7.4849 | -42.553299 | 2025-11-15 00:18:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cc073f9a-8544-39db-ad59-5e7ce410d598 | -4.5506 | -43.2029 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d544ccbe-e3a3-3676-a4ce-687cb115e96a | -4.5408 | -43.205002 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 239a32b1-d770-305a-b0fc-9d583a03de11 | -3.8881 | -43.959099 | 2025-11-15 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d78e8fb3-689f-3e48-a593-2a70bfa2bbba | -6.1453 | -48.0336 | 2025-11-15 00:18:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c06f6ed5-4306-330c-b2a1-c7905fe74048 | -7.5186 | -47.1973 | 2025-11-15 00:18:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74fa2cc7-6b46-3282-98e8-a1be774e296b | -4.6224 | -43.3815 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03991193-efe1-344c-8aee-1fe7306f8a0e | -5.2215 | -44.341202 | 2025-11-15 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e05daeed-655d-3960-8cdc-581f5c99b037 | -9.0125 | -44.179001 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fd7ef64a-a8ed-3ed5-8a86-b08a895d8d6b | -10.3026 | -44.582901 | 2025-11-15 00:18:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0029eb4c-82a5-3bd2-851b-40243f9e4035 | -3.8866 | -43.952202 | 2025-11-15 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2296ccfd-640a-3519-85f1-14a1de87d038 | -5.4796 | -40.9617 | 2025-11-15 00:18:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f29d2ff1-7150-3124-9424-d0fb6bf0f22b | -7.3381 | -43.361599 | 2025-11-15 00:18:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8411ab65-cf82-3071-99c2-931e509f1753 | -11.8304 | -49.2225 | 2025-11-15 00:18:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d100461b-1543-3790-b652-d1152c220fd3 | -12.9245 | -43.090801 | 2025-11-15 00:18:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 490aba54-13f6-32ed-a9cb-8ff77bc7ab50 | -4.544 | -43.2187 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bfec056b-4a34-35e1-b184-f45c2f915d45 | -6.3042 | -41.808601 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 79b83546-074c-3baf-b200-41d1e1018aa7 | -11.7925 | -48.0741 | 2025-11-15 00:18:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eeb8bd70-89c2-3c9f-bc71-5edcfa8c6699 | -7.6519 | -41.298901 | 2025-11-15 00:18:00 | METOP-C | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eaf5871f-509b-37a8-94a3-0103e2261a33 | -4.2587 | -44.5923 | 2025-11-15 00:18:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c954eef9-3080-3a9d-b23f-de294b3f1176 | -6.6516 | -43.514301 | 2025-11-15 00:18:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15a1da01-ff75-32db-893b-ff9b3063707a | -4.0229 | -42.474098 | 2025-11-15 00:18:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 390bde92-1e1f-397b-9cb4-35b1acfaeb4f | -8.5731 | -46.062599 | 2025-11-15 00:18:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5baa8463-2234-3baa-9592-e3017fd66237 | -7.5284 | -47.195301 | 2025-11-15 00:18:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45dac183-f961-3ebd-b56f-efb81af5c1bb | -10.3367 | -48.9048 | 2025-11-15 00:18:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c987a48-7ed8-375b-81e9-c1561be49724 | -7.1031 | -42.733101 | 2025-11-15 00:18:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 99af4054-19a8-3174-b946-120e731b8a88 | -5.1049 | -40.725201 | 2025-11-15 00:18:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ed0fb83c-d2e8-3602-bad5-2f00e19b65ba | -5.6209 | -43.921501 | 2025-11-15 00:18:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 401ce7f4-9c0a-31d7-8b2d-0b57d268e780 | -9.001 | -44.173401 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 89d80ab0-4a08-3268-b166-b58ba88fd3a9 | -11.3037 | -44.802299 | 2025-11-15 00:18:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b746c31-bafe-31db-9920-eadcd94d8623 | -9.5193 | -42.9426 | 2025-11-15 00:18:00 | METOP-C | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5438820b-7eaa-3a46-b871-758b87742a8b | -11.3056 | -44.811001 | 2025-11-15 00:18:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7b2a5cd-ced2-3141-b718-cb26ebf627ee | -5.7526 | -42.732601 | 2025-11-15 00:18:00 | METOP-C | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 11ea99b8-0087-31c2-9f9e-c5d40103ea75 | -6.0225 | -45.803101 | 2025-11-15 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b42b5b0-0533-38c8-97cb-8aae33bcfe0a | -7.3447 | -43.345299 | 2025-11-15 00:18:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2d79f531-6d7c-3bd5-879d-08694daf00c3 | -11.7046 | -48.392502 | 2025-11-15 00:18:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91154891-9348-3df1-bb1e-76db2f81f4ac | -4.2767 | -44.5807 | 2025-11-15 00:18:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
