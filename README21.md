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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f639a16-314d-3c3d-aa51-d4ed291df9c9 | -6.52557 | -45.5817 | 2025-08-07 05:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ad399756-e0ef-3aa6-a633-3c938c1d9a89 | -6.5264 | -45.57564 | 2025-08-07 05:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 79723383-366a-3c2c-aee0-7cce9f735a93 | -6.51053 | -56.20518 | 2025-08-07 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4da22953-874b-35a3-8e9f-3bfe260b3208 | -5.81897 | -59.22614 | 2025-08-07 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb654d89-97ba-33b6-92d2-c0376fda1ad5 | -6.53531 | -56.20895 | 2025-08-07 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0eabb7b6-d85a-36fd-8b37-93b06e875bfb | -6.64392 | -58.82691 | 2025-08-07 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a31ee05e-78f0-3d87-bbd3-4ff06435a966 | -6.92122 | -52.84809 | 2025-08-07 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2957105d-f10c-3580-9d1c-c6e3aab205af | -10.6247 | -44.767 | 2025-08-07 05:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 09ab0069-6f41-3c8f-a2bf-4563e1ffe79e | -8.9215 | -60.7297 | 2025-08-07 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d96a1150-5cc7-3000-85ac-a9dacad38a25 | -10.6441 | -44.7413 | 2025-08-07 05:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 78170d63-914d-34cd-a75f-f978254f002e | -12.5329 | -47.1639 | 2025-08-07 05:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 1187bdfe-c4de-319a-bd61-6b85fcb51a42 | -12.5333 | -47.1414 | 2025-08-07 05:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 39935259-f162-39d7-ab6c-1dc5af5f6ce8 | -10.6438 | -44.7645 | 2025-08-07 05:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 368b3959-4a23-3252-827d-ee865035f146 | -10.625 | -44.7439 | 2025-08-07 05:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| bd06cd2a-4c74-337a-8b4e-f21de483a29b | -8.9213 | -60.7489 | 2025-08-07 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 4934ce4b-1cd4-3445-882b-d2a922738665 | -7.4074 | -60.0108 | 2025-08-07 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f52ce314-3cd9-3607-beff-4db8065f4090 | -7.41038 | -60.00671 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82e2841d-6a4a-3198-86a8-51b14ce1ce51 | -9.93427 | -60.46835 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79e8cbfa-2f52-3f10-88f7-17b04b3ef5f1 | -9.02503 | -59.7554 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16c80d92-70da-35d8-a574-3f77c942ad48 | -8.91113 | -60.57655 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c829cd39-086d-315f-b1af-dccc3128efb0 | -8.90949 | -60.56526 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f433130-0a2a-3c2b-90ea-4b7fb665df19 | -8.90432 | -60.59746 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16e17975-7aa6-39f4-affa-84fdaf2b483d | -9.93262 | -60.45717 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acdfdcce-aeb5-3b3f-a679-eb570873e021 | -9.93327 | -60.50793 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2491c48f-4158-3576-a84f-05f1b68fb962 | -8.91506 | -60.57352 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6243422b-ae69-3a7a-aaed-a94faa95379b | -12.33601 | -46.05816 | 2025-08-07 05:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a6f9c27-c601-3214-8bc6-831dabe4f526 | -8.92235 | -60.57103 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0ee4eb5-8fb3-360f-8c5a-c8c6ec67b175 | -10.70823 | -48.86566 | 2025-08-07 05:21:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ccca598-0117-3b46-84c7-d28404d686cb | -13.06286 | -56.85734 | 2025-08-07 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f48cdf3-bda8-3df7-9e4e-1b0d4aa19301 | -8.90711 | -60.60159 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bac7e38e-f2a5-38c7-bb93-62a982e3aef5 | -9.92538 | -60.45963 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24bb43a8-2345-3ea7-a3af-bf5dc907f8c0 | -9.93164 | -60.49675 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56567954-8497-39e0-9080-621b5a527c32 | -11.75215 | -48.18885 | 2025-08-07 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| aaebecd2-5249-3115-9591-5c6f3ead0b66 | -8.92128 | -60.55617 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f34d869-230d-34af-ad0d-522e44d30d35 | -8.91514 | -60.55151 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df0dbb04-bdc4-3bc8-b0d3-bcad02e41fe3 | -11.75851 | -48.18964 | 2025-08-07 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f42826ab-e826-36b6-8a19-bae000e50ec9 | -9.9428 | -60.4913 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 612ac8c6-dc73-30ad-993d-bff35e2fd860 | -12.71187 | -46.38272 | 2025-08-07 05:21:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a9d1732-aca4-3116-8449-f17ac3bb5963 | -9.70818 | -61.29051 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d3fa833-5aa3-3308-a4c4-48f34e027c0e | -7.40193 | -60.00567 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5218d91e-fdbf-3bba-aca7-ae7bf71feea7 | -7.19121 | -59.83885 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 098dedbe-ff15-3d53-a5e1-d860c9b08797 | -12.3763 | -47.05035 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d0c9a85-abc7-3f61-9c4f-65f8786200e7 | -8.91572 | -60.54793 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f4a03df-00fa-3aa7-854c-3030c82d7059 | -9.93483 | -60.46481 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5977409-c9c0-3708-b1e4-fc5e5e376b09 | -8.91006 | -60.56169 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a72841b-2e31-36ee-a220-ef86384c2a64 | -7.41316 | -60.01078 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e44ae4b1-7f69-35a1-87b6-6aef303760c7 | -9.93449 | -60.47903 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22dedb0f-89b7-3976-a221-9466b6bb5dde | -8.91342 | -60.56223 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47a0269e-ac98-3a3b-8358-d6c317004ca7 | -9.46526 | -57.85124 | 2025-08-07 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a13a704-d83e-3f49-ac36-90bdaf704bf2 | -9.94011 | -60.46542 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d8a00d1-2989-3153-9b9d-4debdca9a80b | -9.59968 | -63.45978 | 2025-08-07 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d803a52-3d4a-3c3c-bee6-293e1ea053cd | -12.71049 | -46.3959 | 2025-08-07 05:21:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7ae7048b-b360-3923-9ad5-b9260f1290f4 | -14.50676 | -52.76837 | 2025-08-07 05:21:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec59fba9-6b6f-3e6c-a8a2-f5aa2b44c438 | -8.92019 | -60.74378 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1c935b81-52f4-3c3a-8716-723cd588961b | -8.92399 | -60.58232 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bf69d7e-efca-3404-9f8e-4d47032e38d3 | -8.91236 | -60.54738 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3ba4057f-069a-3bd7-8a07-c71309171986 | -10.059 | -65.00108 | 2025-08-07 05:21:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 358065fb-92e1-3326-8d38-3a04dba281e6 | -12.33703 | -46.05592 | 2025-08-07 05:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67cfe602-baef-310a-bc4b-9478833d58f2 | -10.79367 | -46.49418 | 2025-08-07 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44b4ae66-ca4d-3a27-a72a-4c42d26ca0ea | -8.90826 | -60.59443 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3e40c7c-d2dd-33cd-b8c9-3bd169ba684d | -9.93335 | -60.48611 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a7171f4-79e8-31df-83eb-94e3bf80695f | -8.91105 | -60.59855 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97b1b89f-5793-37a1-9630-2c1dcbfc3a73 | -8.91907 | -60.54847 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78b8e97b-7119-3fcb-9907-9620fe775e2b | -10.70059 | -48.86796 | 2025-08-07 05:21:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e3937e7-d91d-3875-924c-8a357c1b3388 | -8.90843 | -60.55041 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ef15cf71-0489-3231-80d3-15e2f75da7a9 | -12.52657 | -47.1446 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79e54d27-59b3-3504-8e99-19dfdce2a3c4 | -8.91686 | -60.54077 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0619a59f-3456-35ef-9e11-771fb1a54f6d | -8.91785 | -60.57765 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdc263cb-5f9d-3ce0-b4a6-cc8b03f91a5d | -13.72096 | -53.86177 | 2025-08-07 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10bbdcd9-217c-3c84-b2d4-9dd88dcd2016 | -8.91227 | -60.56939 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fef28d0-aba3-3d33-b325-ef7134f64116 | -11.75445 | -48.18966 | 2025-08-07 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b6601819-b3da-36aa-9bd7-828258e0cbcd | -9.70637 | -61.30159 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e117ced9-55fe-34e3-9c93-9cff012d13c1 | -7.41259 | -60.01432 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f221b516-7ede-35ee-ab8a-79dfb3b14ff2 | -8.65882 | -54.71294 | 2025-08-07 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c43a8d06-598a-3399-993e-0e149a78fcd3 | -11.77839 | -47.39925 | 2025-08-07 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 577ca757-2817-38d0-a27a-e4464b0917a4 | -8.91551 | -60.74321 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 547afe0b-1759-3478-921d-2b730fc2eb31 | -8.91565 | -60.75044 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eca871f8-9a2e-3676-9783-1d5157501727 | -12.52527 | -47.1451 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00fbe7c9-a964-367d-90ab-fdfc7649f705 | -8.91441 | -60.5991 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c1a377e-a837-3f0a-9dc8-24956ab34370 | -7.40415 | -60.01328 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 952b79c3-c472-323d-ae09-283e2bcb9d3b | -8.9067 | -60.56113 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c97946ca-9e7b-3eb9-8c1b-5f2e6b7447f6 | -9.93206 | -60.46072 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffa2384b-e62c-3ef6-b97f-a0318d7c9042 | -8.91219 | -60.59139 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c9f1adb-47ef-36e2-bafe-52379ba85bce | -13.72038 | -53.86633 | 2025-08-07 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 69bbb09a-7013-35b5-b66d-835e25c30034 | -12.3761 | -47.05051 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad63d965-d117-3b23-9e7c-40979cd308bd | -12.32876 | -46.05727 | 2025-08-07 05:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b50099c5-4e98-36ce-bbe1-8a0c2203b025 | -8.91047 | -60.60214 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe39e021-23a3-3109-902d-2abf7f38589f | -12.53271 | -47.15181 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 35ed2aa9-7522-3e92-b3ef-40c3b92efb53 | -9.93507 | -60.47549 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 836a5050-233c-34a2-b978-c9a5d4871c9b | -12.32899 | -46.06247 | 2025-08-07 05:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45b5a1e4-f970-30d5-be93-b1783f9408f6 | -13.66949 | -52.19598 | 2025-08-07 05:21:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed6a92ae-b178-3023-861d-670b12da259e | -11.77238 | -47.39256 | 2025-08-07 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e09d9a0c-e9da-338e-9f9c-45b80fc44163 | -8.92407 | -60.56029 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 326bf1af-1101-3df9-84a3-d46774c32483 | -8.92464 | -60.55672 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c610f743-ddae-366b-aaa3-ae70bb2f2161 | -9.93314 | -60.47544 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 658a549d-b121-3e08-a4b4-ce9c5443d9ed | -9.93954 | -60.46896 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b026038c-a811-3d35-be6b-dfafbaa494db | -8.91891 | -60.59249 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a0dee7e-d956-3c4b-a40c-e6364f34c52a | -7.40806 | -60.01027 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f9b35f22-2d3f-3b5c-9dd1-0626b5ca1192 | -8.90441 | -60.57546 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19af0369-f4cf-3c9c-a6a2-a9a3210427f8 | -8.90604 | -60.58673 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README22.md)
