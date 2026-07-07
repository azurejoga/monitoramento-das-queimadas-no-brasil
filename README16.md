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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc85e6ee-7c42-34a1-a2a8-9309c0bea295 | -12.75869 | -44.55227 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15cc563c-ad50-340d-bb1e-201383d78c84 | -11.80726 | -52.52471 | 2026-07-07 04:44:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 936931bc-f1e2-35d7-bdfd-e3c1b6fc710a | -8.02848 | -47.0886 | 2026-07-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae42d66a-d2b8-34d2-a040-0baf2f4680e5 | -6.93291 | -43.69696 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f9d63d32-5a69-3b7d-8270-652c39829867 | -11.69946 | -44.1279 | 2026-07-07 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a182ea2-e8c0-3f3e-b7bc-eb72df9d3465 | -7.64405 | -50.02745 | 2026-07-07 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 985a46ed-7221-32bf-8e72-2e33e4ddb37e | -6.90054 | -43.70895 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 071d5fca-420d-3504-8702-e19449681b19 | -11.66888 | -44.55896 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7cc27048-12e8-370e-b10d-ee9fa650fb4b | -5.52093 | -50.02257 | 2026-07-07 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0aeda65d-482c-371e-b651-6be35344184f | -6.93114 | -43.70932 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b3ef738-2c0a-34d9-8c7e-03850596044d | -11.68247 | -44.5566 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4dcc9c16-00d4-3980-b90b-94dba91a87d1 | -11.68623 | -44.56144 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8da0e1a5-c6b0-382a-8d04-d5ef67cdb414 | -11.81066 | -52.52528 | 2026-07-07 04:44:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb6a30f9-d446-3b8b-ac17-150b930a2bac | -9.37615 | -44.7173 | 2026-07-07 04:44:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7c724f6-3f27-35a1-b8de-65abc7af71a0 | -6.92684 | -43.7087 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3867f302-23d2-348c-9c6d-e1f60a8b05ff | -10.8672 | -46.3592 | 2026-07-07 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0643e8bd-4458-3fc6-b54c-36981740257c | -8.11887 | -47.1151 | 2026-07-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4325051-846c-3950-a412-24c56e68b4c4 | -10.32106 | -49.92074 | 2026-07-07 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f289667-d27b-3ab1-bb40-f2cf7c6c7ad6 | -10.03961 | -54.57439 | 2026-07-07 04:44:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b16244f-2c4c-378a-b201-15e143660385 | -11.66453 | -44.55835 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dd8d21f-ad43-3af2-a8eb-e629ab08f237 | -6.90968 | -43.70621 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7b84cbab-2f5b-31da-a98d-7ee5832bc1f4 | -11.67207 | -44.568 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 163e74a7-dfb6-3ed3-8acd-d6d689117b83 | -11.48966 | -52.91751 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 359edf1c-336d-31fa-9e8d-b3b3cd21ddbc | -12.7581 | -44.55666 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c92e4de3-3205-3f4e-841f-7877a7c15f32 | -11.99073 | -45.1398 | 2026-07-07 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2604a0e-4b30-33e3-8cf8-3291dcdf17b8 | -12.79467 | -44.48545 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b3d77342-e449-3ae9-b9fc-1cd8c192760a | -10.12267 | -52.09566 | 2026-07-07 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a864a053-6151-3b61-bdbd-7001af3034ff | -7.00822 | -42.7734 | 2026-07-07 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7ad7130c-70ce-3b6a-9ad6-e13a22f95181 | -11.66603 | -44.58002 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a229b601-878a-3b8f-a14b-f7b149a33eb7 | -12.78461 | -44.49311 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15494b0a-7683-37b9-b9a3-399818161565 | -6.91455 | -43.70276 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 052a518c-96c8-315f-9121-2f94fbe21594 | -10.85169 | -46.38604 | 2026-07-07 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dda742ac-282d-39c9-88d5-259e255f8a0b | -6.20297 | -42.51332 | 2026-07-07 04:44:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a54ee83d-2f79-3ee9-b4a1-555539ace2fa | -11.05033 | -49.59783 | 2026-07-07 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cca42ecf-a315-35c3-96f8-fde042569186 | -7.71917 | -49.63834 | 2026-07-07 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5eb0fadb-1ee7-37cc-8f4f-22d8c0d4c11b | -11.84376 | -48.25065 | 2026-07-07 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15abfa8b-909b-3dda-aa8b-210929a16d1d | -7.01078 | -42.78799 | 2026-07-07 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 366b2326-a4bf-39ce-ac2c-b3775ade8807 | -10.32216 | -49.91372 | 2026-07-07 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec2ac831-49d4-3606-8f60-80ff348b891b | -11.92391 | -43.37566 | 2026-07-07 04:44:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a6b3ec7-f0e0-3671-ba9f-0f94552eb0f9 | -6.92861 | -43.69635 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fc4b6f5-7285-3745-ba13-5cd34d69fc07 | -8.34126 | -46.4879 | 2026-07-07 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60a44d5c-7bd2-3332-b653-b7eb97465728 | -10.90258 | -56.85382 | 2026-07-07 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac6fd582-3954-33e1-bb7f-07e81c2b2f6b | -6.90186 | -43.70989 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b1125bfb-92df-394c-859f-bfee9fe7a46f | -9.30967 | -51.9145 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba075914-5a53-3f11-b2a7-ac5971c9dcb5 | -10.82628 | -49.37535 | 2026-07-07 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 178b7347-277c-3092-a4ad-c8898f4a128d | -11.55987 | -52.79214 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6067b693-6790-3391-b0f7-e2166835394c | -11.45024 | -52.92732 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83e97375-e662-3ae9-969a-eb85fc339332 | -8.11533 | -47.11451 | 2026-07-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70068de0-18d4-3aa1-a34f-6de1d0ce4b26 | -6.90911 | -43.71028 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5b631ad1-dd2f-3751-83e1-256795aba6a8 | -12.50311 | -48.26379 | 2026-07-07 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc8a2b46-7ebf-3d45-99dd-9d3f64efaff3 | -6.90246 | -43.70586 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4eab8eba-7a1b-3dcf-9f50-ddcffc2bb897 | -11.68017 | -44.57344 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de0f88e9-2402-34f8-9982-97a383455eb9 | -11.47459 | -52.92281 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a92aa67-a0cf-3aa9-b9a4-e593ba8efdab | -11.67436 | -44.55115 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a1b1702-6550-3284-9f46-05584f4e0297 | -11.65585 | -44.55711 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25169239-8853-3184-9f55-8b3eeef60d44 | -5.80284 | -43.80482 | 2026-07-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca794de1-ffe8-39c5-9970-d19d760125c2 | -5.52425 | -50.02309 | 2026-07-07 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0458cea-8004-3dd3-9d7e-ef0e158e4b39 | -12.34016 | -48.21942 | 2026-07-07 04:44:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89f0dabd-f783-3f66-bc01-a5c315bfd853 | -11.84317 | -48.25461 | 2026-07-07 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09d7c347-544c-3682-b552-4402babf9b7e | -10.93486 | -43.07099 | 2026-07-07 04:44:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 50acc4de-bfb4-37f8-aa8c-6f33e34dde60 | -11.49029 | -52.91369 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87e94f4c-5acb-35d2-8144-bc14f68106af | -7.6479 | -50.02452 | 2026-07-07 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f904847-4220-3566-8699-894a1f89d90f | -8.1266 | -47.1121 | 2026-07-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48a42b9b-d344-3c85-abaf-bd8523ab3514 | -9.37669 | -44.71343 | 2026-07-07 04:44:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8972c44e-73d2-35bd-b2c9-c380f748431c | -11.67036 | -44.58065 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73fd9891-145c-3c7f-bc07-58a038408540 | -12.75428 | -44.55166 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0e8db1d-5c06-3546-bc4c-33a006cad493 | -11.69099 | -50.38881 | 2026-07-07 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3028b923-55c7-3366-b9bf-b3d08f41dff6 | -6.59774 | -51.69787 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e4d0783-1ef2-3e08-881a-d57408aa6fb0 | -12.51015 | -48.26489 | 2026-07-07 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4110c999-bf73-380e-8405-ca47bbf88688 | -6.20307 | -42.51533 | 2026-07-07 04:44:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a48b41e9-a59d-365a-ba41-aab755cd19e7 | -9.31306 | -51.91505 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 099e739a-546d-30a9-a097-76859e563e48 | -11.68132 | -44.56503 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e73b89d4-aa0a-39ad-ab8e-efd3aed10c92 | -8.70603 | -50.08043 | 2026-07-07 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72a45519-99fb-398e-beae-5e3f0b68dbbc | -11.66226 | -44.57519 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 084e8f98-eb5c-358f-8c4b-42b683a04cfa | -5.74602 | -46.15238 | 2026-07-07 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 419429ed-e4a4-39c8-b86a-3de409994ea9 | -6.90853 | -43.71433 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ef4c26d5-5b40-314c-98f7-1b39d216fa84 | -7.10446 | -46.51213 | 2026-07-07 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b481be2-64ef-3dd5-923e-3a00a468ea0d | -12.5106 | -48.26416 | 2026-07-07 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 997e609b-6fd7-3e61-a495-c33da3b8925e | -6.91281 | -43.71497 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b8281067-9cb3-3dc3-82d9-f0710f8d7be5 | -6.50083 | -42.23058 | 2026-07-07 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f1bc9d0b-2fb5-323d-a6da-1acb17f9f909 | -9.19521 | -45.31727 | 2026-07-07 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53a5a66a-98eb-3802-9ef1-7035201a3bae | -7.00755 | -42.77803 | 2026-07-07 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b9e1e979-d354-3449-9f97-cce60680d652 | -5.90781 | -43.85449 | 2026-07-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6748e748-65fb-34c9-98f1-633d49a2e503 | -11.68681 | -44.55721 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f912f8cc-5e2c-3250-a836-d982148ce78c | -7.63744 | -50.02639 | 2026-07-07 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0447227c-858f-3a66-b4e3-b04bea08c03b | -9.52639 | -48.16065 | 2026-07-07 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39fcbad3-7963-3460-b9c8-5b158ba50a30 | -11.67379 | -44.55537 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 26c0720b-e7aa-3f3d-a2f6-10faf7692e50 | -9.36727 | -40.42444 | 2026-07-07 04:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5af05fec-aef2-3f56-9661-1fe69b845441 | -6.20757 | -42.5141 | 2026-07-07 04:44:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 48defa91-6d75-3696-a21a-4b3a05b1942c | -11.68075 | -44.56924 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9b8ee60-a63b-34ce-a844-6262ce20ec5c | -11.68566 | -44.56565 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38f527e1-0a12-3fcd-a601-d37cb1945731 | -10.77467 | -46.62457 | 2026-07-07 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55f0aaf7-3ea9-3bba-9b1f-c907b8d945a1 | -11.56267 | -52.79653 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11c60d6c-9293-35c7-b30b-86aad391fbf7 | -11.6666 | -44.57581 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7157de17-9c9b-3975-9a60-547373b18c26 | -9.2178 | -48.55664 | 2026-07-07 04:44:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc413b8c-be96-384f-b547-d8260bb10bfd | -7.6446 | -50.02399 | 2026-07-07 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a23325e5-62b8-3e9c-8bd1-6a2df6e6d079 | -11.48685 | -52.9131 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b829ce72-823a-34ce-8afc-e7dcb332a227 | -11.66019 | -44.55773 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3e6912a-00fd-3032-87aa-7079f57c426e | -11.66774 | -44.56739 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6308dfe0-1ba2-3093-a8a9-30c348fa42ff | -5.79923 | -43.80035 | 2026-07-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README17.md)
