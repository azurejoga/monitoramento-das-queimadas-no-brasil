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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d082e48-8fe6-3fad-91f9-93282adba6f1 | -7.2353 | -46.165199 | 2026-09-15 00:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 865071b6-6820-3136-a4fe-e915fb0be8ab | -11.1131 | -40.4809 | 2026-09-15 00:25:00 | METOP-C | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6e8e94c6-cc0e-33d3-b9ff-cab37e594d4f | -6.7853 | -46.4534 | 2026-09-15 00:25:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8349d8b2-9408-3881-9241-2a1610440518 | -8.7926 | -45.902199 | 2026-09-15 00:25:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8aa936d7-9596-3a26-8701-e8f014cc6407 | -6.3378 | -39.386902 | 2026-09-15 00:25:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 64400e86-2820-3e12-8911-0560b690d96e | -6.612 | -44.194698 | 2026-09-15 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 192739a8-340a-35e7-8483-1d2366b9cbc7 | -4.6798 | -42.093498 | 2026-09-15 00:25:00 | METOP-C | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bea21b2a-407a-38c9-bf1c-05ae567026eb | -15.5432 | -48.826099 | 2026-09-15 00:25:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cc45fe05-656c-3e2a-886c-614377a5b5cf | -11.1702 | -42.795101 | 2026-09-15 00:25:00 | METOP-C | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 23702ba2-504a-3b3c-a7fc-84a923d81ff7 | -5.7772 | -49.865101 | 2026-09-15 00:25:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79985e5b-0d5b-3693-b308-d01630f382b1 | -8.2925 | -41.349499 | 2026-09-15 00:25:00 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a8d4c186-04a8-3ded-8f49-67341064d92c | -6.3252 | -44.113998 | 2026-09-15 00:25:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99000db5-c80c-3250-9692-dfa013bf4abf | -11.2235 | -43.4328 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6bfed4cc-e446-3092-9d50-d7526186eb4c | -11.2219 | -43.4259 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f4943a93-a495-32b3-955f-f01a49e4f75c | -5.6036 | -44.834499 | 2026-09-15 00:25:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eaa058ff-7c95-331d-8ecc-9b24e805c237 | -12.5612 | -47.1236 | 2026-09-15 00:25:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e39e2b6e-1a2e-3f5f-886b-6685d0ad9bcb | -10.6577 | -54.1381 | 2026-09-15 00:25:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c39fa26-398e-3b7e-b73c-8df0315b6af9 | -5.4704 | -45.1087 | 2026-09-15 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 362df396-372b-3c6c-8e05-8367bacb3d18 | -15.5295 | -41.778702 | 2026-09-15 00:25:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 48559ef1-9468-3d55-8007-91dddf2e125a | -5.6088 | -43.557899 | 2026-09-15 00:25:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78b7bffc-eb81-3289-b6ec-90939244ec02 | -2.8994 | -50.394901 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afd98a07-d8a0-3644-a454-72de23bfb543 | -5.921 | -53.5284 | 2026-09-15 00:25:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 437b9d51-4cab-3b15-a43d-42316482bcea | -9.3182 | -48.7197 | 2026-09-15 00:25:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15626963-aa2f-353c-99ad-e3f6d8cab493 | -11.2299 | -43.460701 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83b75c0d-13b9-3197-86ce-9b7203c59c37 | -5.6072 | -43.550701 | 2026-09-15 00:25:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06f42c92-5126-36a1-b7ac-e7c9fde680e8 | -6.3398 | -44.132599 | 2026-09-15 00:25:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75007093-7c01-30d6-a7e1-addcc0c34069 | -15.1679 | -43.84 | 2026-09-15 00:25:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 435348f2-d579-3034-90ea-2892cd0c71e5 | -7.469 | -46.150799 | 2026-09-15 00:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fba59a16-0485-37ba-b4bd-8493ad07842a | -12.4905 | -41.410801 | 2026-09-15 00:25:00 | METOP-C | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ae155d34-b29f-33e0-a4b8-dd966d43e11e | -9.4251 | -40.2925 | 2026-09-15 00:25:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b5668555-ced6-33c6-a77f-d5a1c8588fac | -5.6158 | -45.2486 | 2026-09-15 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de1e2104-a2b0-37a2-8915-160bacae3e47 | -7.094 | -45.039299 | 2026-09-15 00:25:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb0099d-d3de-347f-ad6f-6c4ca5bb7d20 | -8.3919 | -42.211102 | 2026-09-15 00:25:00 | METOP-C | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a142fdd5-d84d-3190-809b-995c905a12e8 | -14.6816 | -48.0313 | 2026-09-15 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2d03181d-3ae5-3e14-b2f0-81d3b52323d8 | -15.5774 | -48.793598 | 2026-09-15 00:25:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ed5007b2-16e3-38d0-b256-766688a52365 | -8.08 | -50.958099 | 2026-09-15 00:25:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d474d828-9dfb-3e22-9044-38c857f822ab | -13.2196 | -51.662601 | 2026-09-15 00:25:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 947146ff-2a5c-327a-ac00-dbd05fd900ca | -18.013599 | -50.272099 | 2026-09-15 00:25:00 | METOP-C | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 34131621-6f9c-3f22-9de6-e4fba8cde35c | -7.0809 | -41.771801 | 2026-09-15 00:25:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6defd7bc-074b-32f4-b806-4e07c12a7165 | -11.1209 | -40.470001 | 2026-09-15 00:25:00 | METOP-C | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 904d3de5-01b9-3b75-bf15-da87c5f09929 | -4.3046 | -49.105 | 2026-09-15 00:25:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc8da5fe-a6ce-3a65-a3d5-10127c92eea4 | -5.4309 | -43.993698 | 2026-09-15 00:25:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8fc5a0a-a1a8-310d-89e0-cb496a9595cd | -6.9443 | -42.554798 | 2026-09-15 00:25:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 813922be-1b45-3337-b355-2003fa3c8c0b | -14.7622 | -42.942299 | 2026-09-15 00:25:00 | METOP-C | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 85a6b75b-d982-362d-abcd-b0518e59273f | -8.6571 | -49.1203 | 2026-09-15 00:25:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1f1f383-2fc5-3fa7-9db9-cfa2c5f24b9e | -7.0806 | -41.814701 | 2026-09-15 00:25:00 | METOP-C | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 477a0c6e-c198-307e-970a-82562e94ab01 | -13.5112 | -44.1665 | 2026-09-15 00:25:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd6462c0-291b-3a42-85e6-6596ebb57189 | -15.5847 | -48.830399 | 2026-09-15 00:25:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 219fe127-362a-3e5c-a47d-80ade3ba47ca | -5.4251 | -43.4328 | 2026-09-15 00:25:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| caf90176-f235-316b-9e0a-cff37ad33cb4 | -8.0945 | -43.777401 | 2026-09-15 00:25:00 | METOP-C | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 79987072-13ed-3394-8795-6b7b66441591 | -10.9739 | -48.325802 | 2026-09-15 00:25:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc1f3cb6-5443-354f-9bd1-99712505c9c0 | -17.317499 | -42.526699 | 2026-09-15 00:25:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 64580bdb-8782-321b-9047-6fa41a3a5e8b | -7.0983 | -41.801998 | 2026-09-15 00:25:00 | METOP-C | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a0a1c6d8-4196-30c3-b4ea-56cc9d28868f | -7.0758 | -42.101799 | 2026-09-15 00:25:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f52f44f6-59c9-395b-90d1-7ee4ede919b5 | -2.8821 | -50.4091 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf7d606b-2184-352a-b08c-305107477f9b | -6.255 | -41.946602 | 2026-09-15 00:25:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 51e48be1-03b7-3fb5-ab6f-3830d41ef01f | -1.7933 | -47.832401 | 2026-09-15 00:25:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e23cb49-95cb-3683-9c82-32089dc1f4a5 | -15.5847 | -48.7794 | 2026-09-15 00:25:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b1e0b1a5-cc8d-368c-b468-9b4a3dbd98e7 | -7.0213 | -44.630299 | 2026-09-15 00:25:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b723e2a4-8660-33d9-a397-42a16379e7e6 | -11.1091 | -40.463799 | 2026-09-15 00:25:00 | METOP-C | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3d6fc05e-00e9-3efc-817f-d4c19124e1b3 | -9.2473 | -48.533298 | 2026-09-15 00:25:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffc98f4b-3e99-33a5-928a-61a865f26bf9 | -15.9899 | -43.273998 | 2026-09-15 00:25:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3c510720-a3cb-3625-9659-998f193b0b95 | -15.2542 | -40.9897 | 2026-09-15 00:25:00 | METOP-C | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c98a760d-f788-3c82-8aed-3748d739f4f2 | -8.0929 | -43.770401 | 2026-09-15 00:25:00 | METOP-C | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0e3a0492-09aa-32fa-82b9-5fe49210e610 | -9.4294 | -40.310699 | 2026-09-15 00:25:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2fd4a643-97ad-3bfa-a1f3-c37cecf9fd1d | -14.8566 | -48.140099 | 2026-09-15 00:25:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a88d7010-6489-39d1-a755-04141a5cd08e | -4.3569 | -47.782799 | 2026-09-15 00:25:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd0ccbd6-56a7-38e8-b24e-1050eed08a3b | -9.1594 | -49.9869 | 2026-09-15 00:25:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05a0707c-87ee-370b-add5-c5bc3b2e8dd3 | -13.3078 | -43.716 | 2026-09-15 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6869498f-fa25-361c-81e1-e757c99cc709 | -2.9062 | -50.424999 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d8b9f48-6ab1-3bf2-9254-3d363cc180cf | -2.8972 | -50.384899 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eb5f61b-839f-37fb-9cf0-8525b8d0ab8a | -5.0301 | -43.598598 | 2026-09-15 00:25:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd7c7352-e752-3122-a9c3-0f27adec1ec8 | -10.2996 | -54.1591 | 2026-09-15 00:25:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4890b344-025e-3c85-ae0c-088497521a11 | -14.8544 | -48.1292 | 2026-09-15 00:25:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4e47f9f3-b292-3f20-8d26-ec4878395209 | -13.2259 | -51.643299 | 2026-09-15 00:25:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 414cebae-67a1-3ba6-957e-cd878c133197 | -10.7523 | -44.813999 | 2026-09-15 00:25:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 13d9236e-4851-3337-b40b-87fe8697a022 | -18.8239 | -44.510899 | 2026-09-15 00:25:00 | METOP-C | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 61efed2e-950c-3ccd-a428-7274b433a345 | -9.3628 | -50.079399 | 2026-09-15 00:25:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f23a0e78-3a8d-3523-b660-c5ccc47251d6 | -3.2497 | -47.078602 | 2026-09-15 00:25:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56fcd549-72e3-3693-aa26-7463d90d5b48 | -8.0772 | -50.945202 | 2026-09-15 00:25:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39bb568b-2c82-3a5e-920c-69c5f5f47537 | -2.916 | -50.422798 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a60a606b-5832-3bb8-9499-15011ba92ffc | -12.8509 | -44.391399 | 2026-09-15 00:25:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0583c8bb-0066-31c5-987f-ff5dc68d9a3d | -6.6751 | -46.192299 | 2026-09-15 00:25:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f163eba-aafd-3951-83a3-178956b0e785 | -12.4268 | -47.310799 | 2026-09-15 00:25:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d4fe639-8036-35c6-ab2e-088f22a480ad | -16.971001 | -49.711102 | 2026-09-15 00:25:00 | METOP-C | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7b2b5214-4038-3401-bbbd-89c1bf95fe52 | -6.3382 | -44.125702 | 2026-09-15 00:25:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ee9d11b-6187-30ac-b215-d36998cf22bb | -6.772 | -42.745098 | 2026-09-15 00:25:00 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ae0bd757-7b30-31d5-8de4-7da9cae013b7 | -9.5282 | -40.334801 | 2026-09-15 00:25:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 20ac0e68-0e77-3c1b-87c7-90f57f9955d7 | -11.2381 | -43.4515 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0ee42284-d1dd-3f02-b387-e1f4a4444657 | -8.8037 | -50.4753 | 2026-09-15 00:25:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2fdbab6-ff50-3fa7-a2e5-1355931bff4d | -16.993401 | -45.459 | 2026-09-15 00:25:00 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7cae9c12-4776-3d07-9128-50f1ae8be74a | 0.2219 | -51.352001 | 2026-09-15 00:25:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7ea0b62e-0284-39b9-8c05-56635a147b8c | -5.4111 | -48.492901 | 2026-09-15 00:25:00 | METOP-C | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| af480e5a-2242-356e-a7f0-ab3b47c9bc10 | -7.382 | -49.5205 | 2026-09-15 00:25:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4a6f9c8-d3a3-3776-b711-8fc920ac4f10 | -7.1596 | -43.526402 | 2026-09-15 00:25:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 49e55f21-6e9f-32ce-8a03-e0029d8e4e0c | -9.526 | -40.325802 | 2026-09-15 00:25:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 17cb18c7-2d4c-37bb-a661-703d577a4aa1 | -11.3257 | -47.6702 | 2026-09-15 00:25:00 | METOP-C | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afcbc870-d19b-333e-9314-20f899a271c4 | -11.8792 | -43.823601 | 2026-09-15 00:25:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 68375dd5-6f1e-3080-9c52-8593bd663196 | -12.8477 | -44.377201 | 2026-09-15 00:25:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4f12319f-ef36-3555-9ee7-b5084c05ab43 | -13.2293 | -51.660702 | 2026-09-15 00:25:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
