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
| 7da08115-1449-3c3e-a72b-02b54a5c3f28 | -10.3916 | -56.7533 | 2026-06-26 01:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 381c0958-df68-3246-9fa0-371453044df4 | -5.7945 | -45.0586 | 2026-06-26 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| a4c2ac5c-5436-31e9-8fbe-126726679c41 | -5.7758 | -45.0599 | 2026-06-26 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 83254d2a-22e0-30a0-995f-b4fce2d077f3 | -12.7557 | -44.4959 | 2026-06-26 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 419b06fe-001e-350d-9909-36c76ac222cb | -9.8957 | -57.389099 | 2026-06-26 01:14:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dae0f6cf-8551-36e9-8476-a12359c71e4d | -12.6232 | -57.887798 | 2026-06-26 01:14:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e7fac6d6-d541-3fcc-975c-20e0cad0aff1 | -9.886 | -57.391602 | 2026-06-26 01:14:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e67a4595-c553-394f-a0ba-1933da20cf45 | -9.8994 | -57.404099 | 2026-06-26 01:14:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb37ee22-61c5-3726-98b5-6290d915536b | -10.3893 | -56.7645 | 2026-06-26 01:14:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9a7607c-fec3-3c3e-a7b0-79e30e5ce732 | -13.2642 | -54.422298 | 2026-06-26 01:14:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dbeceb5b-aaeb-31a5-9e8f-2ed4f1417f45 | -10.3852 | -56.748199 | 2026-06-26 01:14:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 068a2acc-70a3-3f3a-88a1-4580d06d0215 | -10.3949 | -56.745701 | 2026-06-26 01:14:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd4580c-3eb4-39ad-8165-512d046aa446 | -10.3867 | -56.7131 | 2026-06-26 01:14:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d716e913-234d-31da-9652-d0561fbb5557 | -10.399 | -56.762001 | 2026-06-26 01:14:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38affbaa-901b-3f64-aaad-d4679bd04cc1 | -12.7557 | -44.4959 | 2026-06-26 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| c8b09081-d3c9-38c7-af13-00693e8c4939 | -12.7562 | -44.4724 | 2026-06-26 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 657d1a21-591f-3dbc-8c85-6d48e7b65283 | -5.7945 | -45.0586 | 2026-06-26 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c3fe0f29-0e0d-383e-bf0d-0a0beac102ed | -5.7758 | -45.0599 | 2026-06-26 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 952bc61d-ba1d-3ff4-ba75-972c4e5b3604 | -12.7557 | -44.4959 | 2026-06-26 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 9202a115-a0a0-305b-898d-cc27fc9ba195 | -5.7945 | -45.0586 | 2026-06-26 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 49ec1d4d-c1d9-3687-821b-83e6ddcfcb6a | -5.7758 | -45.0599 | 2026-06-26 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 6a527d7f-2099-3b79-817e-6e786cbb0902 | -12.7562 | -44.4724 | 2026-06-26 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 74ef1325-685f-3b24-bdb6-e9463bd2f57e | -5.7945 | -45.0586 | 2026-06-26 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 5bc2b9c5-4e2a-3f49-9ac0-0045fdc4e679 | -5.7758 | -45.0599 | 2026-06-26 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 1dedf899-efeb-3532-a52e-4a25effd8c8d | -13.258 | -54.4315 | 2026-06-26 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a17f6a22-8cf1-3145-96cd-50b547f541fb | -12.6324 | -57.884201 | 2026-06-26 01:41:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 073f87c1-9fc3-350b-875c-1877550a0096 | -10.4006 | -56.758598 | 2026-06-26 01:41:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9b66165-1117-361d-a423-fa75f596888b | -10.4103 | -56.756199 | 2026-06-26 01:41:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63f34e38-6e96-3ef6-8e7a-8ad8813ec980 | -10.3907 | -56.719101 | 2026-06-26 01:41:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8825c357-4057-3248-98dc-46e2e10b72b5 | -12.635 | -57.894501 | 2026-06-26 01:41:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 66f751d2-8135-332b-a3ee-e1245e82baa1 | -10.3973 | -56.745399 | 2026-06-26 01:41:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a91ff7e-2de0-3ce8-92a2-d09e76e847d9 | -13.2822 | -54.439301 | 2026-06-26 01:41:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| febf32f2-13dc-3c6d-a2ce-3a429a257c03 | -13.7359 | -54.0387 | 2026-06-26 01:41:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1db895dc-3321-3a06-9480-5ef3f30b4793 | -13.2681 | -54.425098 | 2026-06-26 01:41:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 005f65f5-f8cb-37c5-b824-795f5f339959 | -9.8972 | -57.394299 | 2026-06-26 01:41:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19279357-af18-3aa6-acd1-d78cfb2cfba0 | -13.2637 | -54.408199 | 2026-06-26 01:41:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cebaa091-4f8b-35b8-b89e-9e42871cac8a | -13.2725 | -54.442001 | 2026-06-26 01:41:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1774266b-2669-3872-a39d-e5e7b34a465d | -9.9002 | -57.406399 | 2026-06-26 01:41:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b921725-170e-3562-8ae0-02afb382345e | -10.1661 | -56.605202 | 2026-06-26 01:41:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f37218f-b01e-3673-b5aa-242bce77faa6 | -11.5232 | -56.127201 | 2026-06-26 01:41:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff1d9e2-89b8-3f39-a57e-b3c7d41bd0dd | -13.7456 | -54.035999 | 2026-06-26 01:41:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e03ac266-4fc6-3547-9109-0f00a7fd5f01 | -13.2778 | -54.422501 | 2026-06-26 01:41:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c07ec2e8-9b59-37f2-9d30-dded8fd6b21f | -10.3875 | -56.705898 | 2026-06-26 01:41:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9e4e462-6db0-3292-9f84-2df70fac9565 | -10.4039 | -56.771702 | 2026-06-26 01:41:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31f1bc66-62eb-3709-a739-bd470d4ef86d | -5.7758 | -45.0599 | 2026-06-26 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 50b29239-5dcc-30a7-b6c3-6bf607fd2313 | -13.258 | -54.4315 | 2026-06-26 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| cf05d4cd-33b6-3aa2-8722-ba48a2fc61bd | -13.2772 | -54.4295 | 2026-06-26 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b8bcfbef-3c39-3eb6-951a-022705803cb3 | -5.7945 | -45.0586 | 2026-06-26 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a18d8200-89e3-3ee8-a9be-e57a054151bb | -12.7557 | -44.4959 | 2026-06-26 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 3aa2fca7-8942-3d7b-81db-b888a83fa2fb | -5.7758 | -45.0599 | 2026-06-26 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8c612971-0980-3ad2-9b99-25a7aa8c63d3 | -12.7557 | -44.4959 | 2026-06-26 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 734b7cd6-669d-3686-a00e-453133532443 | -13.258 | -54.4315 | 2026-06-26 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 125.4 |
| e2325760-8004-36cc-83b2-9a6cc954ca87 | -5.7945 | -45.0586 | 2026-06-26 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 798bd05b-111b-3711-a2d7-425c241d9bf4 | -13.2772 | -54.4295 | 2026-06-26 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 2bc8cd65-22eb-37d0-a390-1092920e7868 | -13.258 | -54.4315 | 2026-06-26 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 127e6e92-3b4f-374b-a385-5db9dd299f5b | -13.2772 | -54.4295 | 2026-06-26 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c0699cf7-f433-3e70-83eb-4b51fba609bc | -5.7945 | -45.0586 | 2026-06-26 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6beb0e44-1975-32e7-8c88-67296d0b7f0f | -13.2583 | -54.4109 | 2026-06-26 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a6e6cf68-e543-3ef5-b579-481204cfd08f | -12.7557 | -44.4959 | 2026-06-26 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 8d020be7-7596-399d-a87d-cb2abaa17651 | -5.7758 | -45.0599 | 2026-06-26 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| d51be022-bd4e-3e99-875d-043380328c3c | -12.7557 | -44.4959 | 2026-06-26 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| d8ecbdec-953f-35ec-9fcf-733f4905bcd0 | -5.7945 | -45.0586 | 2026-06-26 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 77a16b39-055a-3d87-863c-92f11875887d | -13.258 | -54.4315 | 2026-06-26 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 9287b8a0-751e-32dc-8f1a-d5132f2c59e4 | -13.7231 | -54.0289 | 2026-06-26 02:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 12854b4a-9b9e-398e-9768-b23fdc5a7734 | -13.7228 | -54.0496 | 2026-06-26 02:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 25bb32db-5304-373d-a156-41995d2ddddf | -5.7758 | -45.0599 | 2026-06-26 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| df3d5035-0e90-3789-931e-829e31258700 | -13.258 | -54.4315 | 2026-06-26 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 15a13614-b446-39b0-b72c-8b3991166aa8 | -5.7758 | -45.0599 | 2026-06-26 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 3b8f0d1d-8175-3b0c-af65-e0cae3169452 | -5.7945 | -45.0586 | 2026-06-26 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c8920ab0-af32-30df-851f-89b7f1b47c7f | -10.3916 | -56.7533 | 2026-06-26 02:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 2704678c-ec25-3250-ba93-03a989d56340 | -13.7423 | -54.0267 | 2026-06-26 02:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 018a341a-3445-34b5-a8ba-f56825c56d06 | -13.258 | -54.4315 | 2026-06-26 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 8b9e7a64-6353-3d37-bb08-7c9e0c164d0b | -13.7231 | -54.0289 | 2026-06-26 02:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 3e6d0ce8-8ebc-352e-90f1-f144c8c90a33 | -5.7758 | -45.0599 | 2026-06-26 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 6701f1ef-b313-3161-8905-43f92a224e13 | -10.3914 | -56.7732 | 2026-06-26 02:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| b36b1515-007f-3dc1-91aa-3ee2b4c91ddf | -13.7228 | -54.0496 | 2026-06-26 02:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 62397204-757d-3605-96f6-ec8ace0f5ef2 | -5.7945 | -45.0586 | 2026-06-26 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 4c502d81-c336-3b68-b550-1a1578835e69 | -13.742 | -54.0475 | 2026-06-26 02:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 139.6 |
| c0ab9fe9-3c9c-369e-bf6c-f77a7383fabf | -10.3916 | -56.7533 | 2026-06-26 02:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| beaecf35-0a8d-324f-8b7b-74bcfc932f57 | -5.7758 | -45.0599 | 2026-06-26 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 52eb6ecc-0aab-3ada-84b6-53bdfd19d3ce | -10.3914 | -56.7732 | 2026-06-26 02:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 215978ff-0e78-3518-99b2-65f1c19d05d5 | -13.258 | -54.4315 | 2026-06-26 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 64013b68-f580-32b5-a9fe-fd5e4a963cf4 | -10.3916 | -56.7533 | 2026-06-26 02:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 2b3aa021-9143-3496-84d9-8769188dfc85 | -5.7945 | -45.0586 | 2026-06-26 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| f0e4343a-9de0-3f12-bea6-b3dbc5ed5687 | -5.7758 | -45.0599 | 2026-06-26 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 8d5032c6-bc96-3ea9-930f-ceb13e41e185 | -4.98405 | -37.23004 | 2026-06-26 03:08:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 646bf9ff-19c7-3074-b56b-da57d4787a02 | -4.98313 | -37.23514 | 2026-06-26 03:08:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5701f89a-c439-3c0a-80ab-9fbd8ff5fe2e | -5.7758 | -45.0599 | 2026-06-26 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| a74d9c85-3e9f-3d78-b638-3aee2dcb9bca | -9.3069 | -40.2365 | 2026-06-26 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 18e10eee-ce3e-3d82-add9-3575d72276d6 | -21.30082 | -40.99019 | 2026-06-26 03:10:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f81ea8c7-a846-348f-992c-e541198a36c6 | -5.7945 | -45.0586 | 2026-06-26 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| d44cc09c-33ae-3195-aa9c-df92d32ba3d5 | -13.258 | -54.4315 | 2026-06-26 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| aa364a04-6b00-37af-8260-d0c685f55c13 | -5.7758 | -45.0599 | 2026-06-26 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 33324cb9-649c-3b1c-b9ae-75a775812146 | -5.7758 | -45.0599 | 2026-06-26 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 155888a3-dc08-38a9-b731-17bb267259eb | -10.3914 | -56.7732 | 2026-06-26 03:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 300b8894-eca8-3a2d-a98b-99cbf14ac3dd | -5.7945 | -45.0586 | 2026-06-26 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f57e35d9-3283-3e0e-8023-d143309841b8 | -11.7798 | -46.4367 | 2026-06-26 03:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a25d392b-e506-30b3-8dfa-c96c0f238ed4 | -10.3916 | -56.7533 | 2026-06-26 03:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 3c87eab4-5e83-312e-9d08-3e1643f1a4c6 | -5.7945 | -45.0586 | 2026-06-26 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a3d53492-9088-3cff-8a8e-fcb18e1a5fe3 | -11.7794 | -46.4594 | 2026-06-26 03:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |


[Clique aqui para ver as próximas entradas](README3.md)
