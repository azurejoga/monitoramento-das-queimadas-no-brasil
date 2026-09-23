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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f957225-f455-3993-bfd1-d9699024f3b1 | -14.61752 | -45.65365 | 2026-09-23 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ec2d0cb4-d5d3-3853-906a-0fd509e81aed | -11.68468 | -43.45722 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d5e5d3e-4eb5-33b2-9cea-7a667713d18c | -10.21102 | -44.15394 | 2026-09-23 03:45:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53374c88-2dca-3411-9cfa-fa71cf46702b | -10.49981 | -44.87161 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94394be9-bd3a-38ca-b1df-57fa0e7f0a1b | -11.68188 | -43.44445 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d6dfb36-c860-31a2-a815-44f566b0684f | -11.42741 | -47.37933 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5c8a7aed-fa08-3f74-b158-dcf6c9e4bb8a | -10.70596 | -48.72508 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2f39a16d-090e-3c56-b8e1-8f986a5bd9d8 | -9.03823 | -45.01924 | 2026-09-23 03:45:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbfdd4e0-c773-3464-b7d6-fc4abb5ba4de | -15.62503 | -43.52631 | 2026-09-23 03:45:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 88e8b98a-e388-3aee-bb2b-cfb89b7fcb69 | -9.56602 | -46.53798 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 61106dd4-07cd-31f6-983d-ceec5b910f56 | -14.30132 | -42.35771 | 2026-09-23 03:45:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a0c46bae-a6a0-3d0c-9b38-54ece6f0fe29 | -11.35366 | -43.3788 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 906b5003-5c2e-3296-88d6-1d6d1e2e3b3c | -8.35978 | -45.61033 | 2026-09-23 03:45:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a2821be-f881-3a8d-8a9e-594e34188b81 | -11.46958 | -47.3697 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ed1fcf2-4d9f-314c-9719-6f46c8a73304 | -9.03735 | -45.02379 | 2026-09-23 03:45:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bc5fea5-599d-33d6-954b-963666f74667 | -11.34365 | -43.37673 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4e47196-b090-3d17-a749-27dd2674f3f8 | -11.93822 | -38.28947 | 2026-09-23 03:45:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 75a4a0fe-72ac-37b9-bebe-644b08b5d4e4 | -15.1653 | -43.57247 | 2026-09-23 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 231c1584-13b4-3806-b595-0c0f913c8e39 | -9.56501 | -46.54314 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d90c1c07-ee3c-3e45-9716-ea8fa3cbe873 | -10.00673 | -45.18679 | 2026-09-23 03:45:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 538810bc-1f7f-363a-872d-fde7036a9532 | -11.68579 | -43.45132 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 955a8aeb-7d5c-35d3-a52a-509903e2453e | -10.95475 | -43.85668 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84d5417d-9ed8-3557-9236-35c23dba3d3a | -8.5892 | -44.53788 | 2026-09-23 03:45:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba128b0f-a6aa-33cb-a052-8e7db945a5ce | -10.45336 | -44.94743 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d220a2fe-6624-3ed9-bf23-f538099921ee | -9.57846 | -46.5415 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a51ada8f-9c9a-3352-a1dd-42f7fdfb3c5d | -8.37479 | -45.59764 | 2026-09-23 03:45:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58773731-8341-3809-b944-56e284d32b22 | -12.41734 | -46.96542 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 656e4ccf-fc03-3817-a053-46b0a73aac93 | -14.60882 | -45.64023 | 2026-09-23 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5ef4dde6-ce08-3bf3-8cd9-acf8ea826b0b | -12.40597 | -46.96647 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7e29edc-c5e6-3d5f-b41c-5bd942f2face | -8.77319 | -45.63142 | 2026-09-23 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2ecd3e0-ea09-37cc-876d-af66de785750 | -12.40219 | -46.51251 | 2026-09-23 03:45:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7a312e4-a275-33da-8f9f-5625aea1b8be | -12.40125 | -46.51722 | 2026-09-23 03:45:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49814e28-008f-3a25-9922-5dba86365925 | -8.81164 | -44.27989 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 1de34358-4a9e-31b1-9e68-2fc1796695a8 | -15.49358 | -41.55222 | 2026-09-23 03:45:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8e57031a-eaa1-3bd0-8f60-2e4eb9ef557d | -8.75897 | -45.84012 | 2026-09-23 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 76c79555-dc80-37ca-89e8-fbdbf8a71e68 | -11.29299 | -44.04506 | 2026-09-23 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 301dd81a-e5de-38dd-a157-5fbec98f60b7 | -12.12381 | -47.39185 | 2026-09-23 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7825daa-77ae-36c8-9dd4-43c8643416cf | -11.66352 | -43.48677 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2cef293-228b-3f52-9330-a0a7955162f3 | -11.65684 | -43.46702 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58bbd3e0-f8b6-31cb-b014-a64a3446d5cd | -9.99849 | -39.17286 | 2026-09-23 03:45:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 3f85bde5-4f69-3365-b2c8-9ab571b5d4e8 | -8.118 | -44.43726 | 2026-09-23 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbcf4797-b453-3e36-a099-7b8fd83a437a | -14.96136 | -47.53517 | 2026-09-23 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ebb74543-bbdf-3f84-ac9c-5fb782dfa138 | -11.93461 | -38.28882 | 2026-09-23 03:45:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| de01f1d0-bfdf-31ba-b24b-c9f96a63d566 | -13.01936 | -48.64511 | 2026-09-23 03:45:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2afa18f-d221-3c52-bb3e-e9215035eb83 | -14.4109 | -42.10751 | 2026-09-23 03:45:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1d76320e-1c63-3d5a-ab07-380b7c6b4a1a | -11.6652 | -43.47787 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64f05ca8-a0d3-30ce-b114-70243c53d367 | -13.29848 | -47.89707 | 2026-09-23 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 946f9359-bb19-3fa8-b6af-78cc91f98577 | -15.62971 | -43.52728 | 2026-09-23 03:45:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 65219f2c-9bca-3574-a3dc-8f2aa52f50af | -14.7429 | -47.15328 | 2026-09-23 03:45:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db4aceb5-f5a8-37a8-a24a-b9e24782a751 | -14.99965 | -39.73861 | 2026-09-23 03:45:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| baefc5ce-cc38-314f-b9d1-29c46accb6db | -14.75551 | -47.16054 | 2026-09-23 03:45:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bb06a45-12ad-3288-891d-a3303b220836 | -12.41731 | -46.97408 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| bc5196e7-2a33-3a42-b1c5-794418664390 | -11.45042 | -47.39815 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| acbe732e-22ca-3b69-97c3-a1a74b93f63f | -11.47016 | -47.36847 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 158eeaba-1e7c-3e09-899c-d2b585ceb597 | -12.41313 | -46.96289 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c8f7d6c6-f149-3b59-a205-130ddba91fbf | -11.3481 | -43.3807 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14ccc768-a4ad-3e2b-aa4a-b7f4b27de953 | -8.59123 | -44.53694 | 2026-09-23 03:45:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76e66822-b514-38c3-a415-e2cfd9ef161d | -11.47055 | -47.36491 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2b336811-4452-3ad8-b0ce-0a2aee18c1f2 | -13.9315 | -47.8367 | 2026-09-23 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b13205d-c630-3881-b5ab-a712d1c81b5a | -8.80694 | -44.27417 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b62d009b-f658-32be-affd-5f3761db017a | -11.5223 | -45.34945 | 2026-09-23 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e37c11c-b0ac-384b-9e9b-47e3af558a6a | -11.4676 | -47.34648 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f54d49c-212c-30f9-ae2c-e94251b66607 | -14.60734 | -45.64754 | 2026-09-23 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ac2a7c01-4b42-3927-9dc8-cc3663066a71 | -13.45635 | -46.2783 | 2026-09-23 03:45:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e2a70c3-8dc0-3a77-b8e0-f9120cb002d6 | -10.71165 | -48.71071 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38972af1-4903-378d-8f0b-ca2822ef041a | -11.47287 | -47.3555 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 092d30c9-58f0-3aad-8053-33551ad7ed07 | -12.41113 | -46.97275 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 573b4626-fd2c-3fb6-94e5-5938f29cf289 | -10.44458 | -45.09488 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc983676-9b48-3aa3-9c5e-ef5e00c300bb | -8.77924 | -45.63268 | 2026-09-23 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f31906e-eaf4-3278-8d4b-8459187203b1 | -10.50128 | -44.86399 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3079381-221b-3be9-8d50-f67852747864 | -15.52767 | -41.81539 | 2026-09-23 03:45:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b4792ac3-8921-3934-9e45-5ac1696b04f5 | -10.21035 | -44.15747 | 2026-09-23 03:45:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e5bc614-b411-34a2-9fd6-69fa5d2973b4 | -10.51101 | -44.87393 | 2026-09-23 03:45:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47a8886d-e66f-3a73-8ae7-9f05df6aee18 | -8.8055 | -44.28188 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ce94e9a2-224b-3521-b9dd-c1ff0d5d78ce | -9.84099 | -46.38414 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c594fe9f-fa09-310a-a834-10431035be69 | -15.1663 | -43.5672 | 2026-09-23 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 02d95a0b-ccb2-3d6f-9fa1-04c97be466e5 | -11.2936 | -44.04177 | 2026-09-23 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c6446509-56ff-344c-92ec-1bfe2484e5dd | -8.08193 | -44.34771 | 2026-09-23 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 097ade1e-e802-3499-8a9d-1da6add49505 | -10.70097 | -48.7274 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3e4de9fb-5eb0-3465-ad93-edc2b319ec21 | -11.35156 | -44.21327 | 2026-09-23 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 536004aa-2c2f-3fe2-906b-2817d4c07b55 | -12.11859 | -45.64396 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5aa6ad33-e399-33ab-a9ef-ab0d39a7af99 | -11.47996 | -47.35363 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0ae79b4e-64cf-31b1-be61-a1784a74357b | -12.11939 | -45.63993 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cb434731-06fc-36b1-b27f-b914ef6b8f9c | -8.73549 | -47.60288 | 2026-09-23 03:45:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7d6115a-f665-322c-af97-f663ce7e4d72 | -8.80073 | -44.27655 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 82509022-ee5f-3456-bfc5-2c92a4dcf686 | -13.92403 | -47.84069 | 2026-09-23 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4583e7c9-76ab-31ea-8b8c-94432159cd3d | -8.7652 | -45.84082 | 2026-09-23 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b003788-275f-3f8a-bbe2-46a0f5454dce | -9.03666 | -44.99623 | 2026-09-23 03:45:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 760bc40d-1397-382b-87cc-ee4cf34fb3e6 | -15.63541 | -43.52308 | 2026-09-23 03:45:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f9d1e24-94bd-39d7-9c03-86b37882edfe | -8.60266 | -44.53872 | 2026-09-23 03:45:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c971ae68-13e1-33ac-af11-1107cd9e5fb0 | -11.46865 | -47.37431 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b440d3ee-4765-329e-888f-58c8b4d3dd40 | -15.62605 | -43.52113 | 2026-09-23 03:45:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 506cc1b5-9658-3b8d-a0df-68b6f0b7321a | -14.96736 | -47.53697 | 2026-09-23 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c747409a-9900-361a-9669-77bcca0bbd77 | -11.13373 | -42.78753 | 2026-09-23 03:45:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 77ba6573-ae74-38af-ad91-3a57203ebd4b | -10.54258 | -43.98124 | 2026-09-23 03:45:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cec0a32e-20fe-34ac-87ec-2191de06cd94 | -15.50682 | -39.12683 | 2026-09-23 03:45:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3c52339f-2f84-34ee-b0ca-4d618873777e | -11.15374 | -42.84233 | 2026-09-23 03:45:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2e94b846-82c2-3ba7-a346-fd1ba4b122b5 | -12.12718 | -47.38254 | 2026-09-23 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7eae88b6-138b-3a99-9189-ed10db49195a | -11.42846 | -47.37421 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8d80b2e-3000-3a28-a29a-58814bcebca2 | -14.61826 | -45.64999 | 2026-09-23 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README45.md)
