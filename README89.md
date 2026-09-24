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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b33d5f6b-4c1e-3078-a8cb-8a55d8255d70 | -9.93118 | -60.71725 | 2026-09-24 07:18:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8fe22754-a8d6-3090-a9fd-d34f1789a3c7 | -12.10837 | -50.73181 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 56baa15a-1517-328d-a2f4-8c1bca1d2e88 | -13.78253 | -54.06553 | 2026-09-24 07:18:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f395f84b-6d69-37db-b674-c67b9937b5b9 | -7.89967 | -61.17041 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d745f9b7-a009-39f8-9533-a49835f6da6b | -10.91064 | -53.9548 | 2026-09-24 07:18:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b7eca9b9-86f2-3af2-89ef-31c81642297c | -11.92545 | -50.7288 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5f5a3253-08d8-38f6-a548-1af1253e8cc4 | -12.12965 | -50.75151 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 877f4080-496b-3c4f-91f5-e53bc504f53c | -13.79348 | -54.05639 | 2026-09-24 07:18:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fd547715-4039-3583-b301-2deb9b90c941 | -7.8851 | -61.16077 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 402d0b7c-7cb1-3e72-84d8-0dae556adad6 | -12.11054 | -50.71516 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 3dea5d37-901d-3446-8479-83cd658a0ed0 | -9.23649 | -47.34108 | 2026-09-24 07:18:00 | AQUA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| fbe565ab-5047-3772-9c65-23ffa2c47621 | -9.25226 | -46.23105 | 2026-09-24 07:18:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| da844baf-80d9-3ad3-b328-882053e8f2d4 | -7.88215 | -61.17875 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 88367dc4-8026-301c-aa90-27cc27c6c03a | -11.9233 | -50.74528 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5a26fbb5-99b5-3fdb-9315-1890a15459b3 | -12.13184 | -50.73491 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| c274710b-fc00-366a-9b58-4979fbf232fb | -8.1243 | -54.81707 | 2026-09-24 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0f2caf03-de33-3bd5-820c-a6297c5259e1 | -12.00074 | -52.46221 | 2026-09-24 07:18:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 5711e4ab-75c2-339a-b2dc-02cd5ca6ddf5 | -11.93715 | -50.73034 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| b7e159ea-7a34-3222-8eda-ddea09633df8 | -7.89731 | -61.16266 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 7357fec9-2a7b-39e9-9c8c-2cd8ac68de25 | -9.23636 | -47.34843 | 2026-09-24 07:18:00 | AQUA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 081e33e6-b4d7-35cc-8723-9e3ac94b2865 | -12.09879 | -50.71361 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e3e8733f-43cf-32a1-987a-f56113628f6f | -11.22244 | -51.35794 | 2026-09-24 07:18:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 7ef07522-70ff-32e8-af19-94b82210c773 | -12.14358 | -50.73646 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5d6c725f-1e5f-37bc-a270-9cdfc71a140a | -14.56385 | -54.12678 | 2026-09-24 07:18:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5f32cb4f-a542-3590-b738-2d5b2b40f377 | -11.24714 | -51.35353 | 2026-09-24 07:18:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 4b66d3e5-a871-3f6b-a9d2-8c68e592a4fb | -10.91204 | -53.94498 | 2026-09-24 07:18:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4a00ab13-e3b3-368c-af77-cf88e844eb36 | -12.12011 | -50.73336 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 3de12469-7871-385f-9875-9b24cb53cd82 | -13.7855 | -54.04452 | 2026-09-24 07:18:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ca2cb027-b102-3082-9fe9-2a5d35906a0c | -6.6146 | -59.9272 | 2026-09-24 07:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| c83db744-ef83-3d13-a814-7e4fa102cb14 | -12.1112 | -50.7215 | 2026-09-24 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 95974210-3874-393f-a618-2b657166afac | -12.1109 | -50.7429 | 2026-09-24 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| b546fdc4-5593-3f79-a40d-d12ef1134af9 | -12.13 | -50.7407 | 2026-09-24 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 79117803-8ee9-38d0-ad4f-a8f05b574dd2 | -6.6146 | -59.9272 | 2026-09-24 07:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b59e7524-3055-3ae9-95bf-e9e9e426905d | -12.13 | -50.7407 | 2026-09-24 07:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| b06ee5a9-e2ec-3c89-a107-b7635ee83016 | -12.1109 | -50.7429 | 2026-09-24 07:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 2924b749-9201-3dcc-a42d-02713b00eb33 | -6.6146 | -59.9272 | 2026-09-24 07:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| cff74447-78e9-3bf1-88bc-ee45eed4d23d | -6.6146 | -59.9272 | 2026-09-24 07:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 3b02a0e2-e7e6-3274-951e-f7a200cf9ad7 | -11.4206 | -47.3827 | 2026-09-24 08:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| f00f8f54-2375-305c-a76e-6dac7bfe7bbb | -11.4011 | -47.4074 | 2026-09-24 08:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| c930f9cf-bf6d-3b96-8dcf-c763df2cbb97 | -11.4202 | -47.405 | 2026-09-24 08:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 98bd1042-e746-3471-bffc-9e448ac04054 | -11.4015 | -47.3851 | 2026-09-24 08:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d724c2c8-86ab-3ec1-84b8-d106be6dfb2e | -11.4011 | -47.4074 | 2026-09-24 08:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 4e8563a5-54e4-313f-9bcf-fff49849c09e | -11.4015 | -47.3851 | 2026-09-24 08:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 1b836794-64d5-3093-a739-fcec5802b9dc | -6.6146 | -59.9272 | 2026-09-24 08:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| fcc7a5ad-902f-36fd-a853-1448c2aaad37 | -11.4202 | -47.405 | 2026-09-24 08:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 4a06558e-29d9-3203-b7fe-929ce946a686 | -10.11 | -50.1708 | 2026-09-24 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 5bd78248-4e74-3008-9c66-d1376181a7a0 | -6.6146 | -59.9272 | 2026-09-24 08:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| da7fd9f2-3c98-349c-a181-4d7b7950df87 | -10.1098 | -50.1921 | 2026-09-24 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 4f8a2730-a910-3902-88e8-1e1646c1f025 | -10.0909 | -50.194 | 2026-09-24 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 5affa948-6c4f-3c82-86ac-e8050a05ddc9 | -10.0911 | -50.1727 | 2026-09-24 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 4d61f861-655e-3010-b273-165e0bbde15d | -11.2281 | -51.3727 | 2026-09-24 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 6a2538e7-7de3-30c7-96f5-adc3e14cc181 | -6.6146 | -59.9272 | 2026-09-24 08:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| a54683e5-cede-3777-854f-47685aa6bcea | -9.2604 | -47.3467 | 2026-09-24 10:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 156.9 |
| b993041a-3e49-3fd6-a750-87830c29348e | -9.2793 | -47.3447 | 2026-09-24 10:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| a78aa567-8d2a-30f6-a72a-e70aa667dd2b | -9.2604 | -47.3467 | 2026-09-24 10:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 387f9ac0-279e-3717-b894-237e7ef383c2 | -9.2604 | -47.3467 | 2026-09-24 10:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| ae9c3d66-b85d-3a47-b898-82218bbe2d48 | -9.2604 | -47.3467 | 2026-09-24 11:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| d362b8ff-5161-3436-add4-5407d7cb1a3a | -7.2881 | -45.5494 | 2026-09-24 11:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| dfdbaa11-2b8d-3c06-b93a-d8d1ad8c0101 | -9.2604 | -47.3467 | 2026-09-24 11:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| dc08fd53-bd26-3ffa-8b0c-90b552349cfe | -7.2881 | -45.5494 | 2026-09-24 11:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| a5ba77d3-2c34-3c47-95d0-e347a963185b | -10.1297 | -46.0412 | 2026-09-24 11:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 5584c58d-e357-3ed3-b19b-c53315316373 | -7.4264 | -40.2278 | 2026-09-24 11:20:00 | GOES-19 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 123.9 |
| 03fc52ef-ecd2-3aaf-ab73-d6a533ee6e1e | -7.7961 | -39.86895 | 2026-09-24 11:23:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 12.1 |
| d945f11c-67b9-37f6-bd47-4c054f7307d0 | -4.89918 | -43.45707 | 2026-09-24 11:23:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6dfa6325-ea3f-3bc7-a37a-d025580d2d37 | -3.5517 | -43.45765 | 2026-09-24 11:23:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 04418691-2b75-320b-8543-03b72c15c026 | -5.19149 | -42.96871 | 2026-09-24 11:23:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f8018922-b149-37bf-b67e-0f834196790e | -3.56084 | -43.45893 | 2026-09-24 11:23:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 53f3fa11-29fd-3bba-8a60-e027796f5885 | -4.36477 | -43.25952 | 2026-09-24 11:23:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9463cfa0-2be0-3739-a922-f819894bc2a1 | -3.57775 | -40.63761 | 2026-09-24 11:23:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 23.7 |
| b0c3ab1d-84ed-3d79-b080-4a54caaeaef7 | -7.42203 | -40.22878 | 2026-09-24 11:23:00 | TERRA_M-M | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 38949da8-abfd-3c3c-a394-9e172af17e75 | -7.43146 | -40.23003 | 2026-09-24 11:23:00 | TERRA_M-M | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 153.0 |
| dee10010-3ff3-317d-b626-69042437d9b5 | -5.57361 | -42.30021 | 2026-09-24 11:23:00 | TERRA_M-M | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 40e8d0e1-2be6-31d7-b252-b2f559ad1f10 | -7.36849 | -39.18729 | 2026-09-24 11:23:00 | TERRA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 467316c8-164c-3bad-b203-91b9a89bb8a9 | -7.43286 | -40.21985 | 2026-09-24 11:23:00 | TERRA_M-M | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 18.6 |
| d077186f-2a45-3255-b2df-317715dc2461 | -3.55946 | -43.46844 | 2026-09-24 11:23:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| af5f5606-7414-364f-abe5-f5165edeecbf | -6.54946 | -43.08886 | 2026-09-24 11:23:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5cb3d431-a052-3786-af4d-810a56945d9c | -10.11924 | -50.22592 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| e52c4b67-7896-3467-ad4f-55653b2360f8 | -10.11119 | -50.21773 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 8703882b-5308-3b19-b673-b842c46c53f6 | -8.93526 | -45.94172 | 2026-09-24 11:25:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 96dded43-93eb-3ac1-b235-d38d33d31312 | -10.08804 | -50.1911 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 285.3 |
| abd25574-f665-3cc5-8432-34ec97ec10ed | -8.23737 | -38.06284 | 2026-09-24 11:25:00 | TERRA_M-M | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 71c3a81c-3398-3398-8097-2daf5ea213a3 | -9.13146 | -40.12876 | 2026-09-24 11:25:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| b94cc5cc-68bc-3959-a0f2-647e06a8ab75 | -10.07466 | -50.1889 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 611.0 |
| c76b2b15-a566-3d12-90e0-ec721bf49a61 | -9.01263 | -41.9866 | 2026-09-24 11:25:00 | TERRA_M-M | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 2ffdf223-b760-335a-a907-e2662dc8c7f4 | -8.89926 | -45.91379 | 2026-09-24 11:25:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c572a929-4026-31e0-9398-24ff4c6e1f80 | -8.50174 | -41.55285 | 2026-09-24 11:25:00 | TERRA_M-M | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 0af57997-2137-3a02-af67-da7e8de8d4ea | -10.09169 | -50.16897 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 9973d6ee-8e19-3b02-a163-8962b9780d84 | -9.24221 | -42.76643 | 2026-09-24 11:25:00 | TERRA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f62ffce1-a958-31c8-a4dd-7148a39cb3c1 | -9.54555 | -45.36923 | 2026-09-24 11:25:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2ece0ef0-a2ec-3652-91a6-e1475c9d8871 | -8.8227 | -45.94226 | 2026-09-24 11:25:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cf8ef855-383d-3f77-9d78-34a46335fba3 | -8.30652 | -44.77466 | 2026-09-24 11:25:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| dc5738c2-9689-368e-be94-25b888616224 | -10.1289 | -50.25038 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 1f3443f3-5f5f-3e64-92d3-0530627e2b56 | -8.57724 | -47.25519 | 2026-09-24 11:25:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| d7b43340-45d4-321f-b4d8-97f639a5d7f3 | -7.9325 | -44.85337 | 2026-09-24 11:25:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fd66b20c-1650-30be-ad80-b8cd7d3a64c3 | -8.30799 | -44.7645 | 2026-09-24 11:25:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d8f4ea0e-0265-3cb2-8663-db08f4532080 | -8.25081 | -48.21875 | 2026-09-24 11:25:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ef93edee-5268-32cf-967d-d777886dd55c | -10.09553 | -46.00439 | 2026-09-24 11:25:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e3486a53-edf6-3968-97c8-f13f643352d9 | -10.13265 | -50.22811 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 36efddc0-c9db-3ecf-bf54-2eaa8f139aec | -8.44046 | -47.45404 | 2026-09-24 11:25:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| fc7a0c9a-40d0-33dd-9882-26dce55f8e05 | -8.93352 | -45.95329 | 2026-09-24 11:25:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.1 |


[Clique aqui para ver as próximas entradas](README90.md)
