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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56af4bbc-2c86-3d62-93c2-cb19a5f0af48 | -11.73158 | -49.10456 | 2025-08-22 04:19:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bda6fda-47a7-3bf0-ac5e-e8c78bc41795 | -10.71436 | -48.86021 | 2025-08-22 04:19:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee6f7cec-bb68-3da8-a3aa-31963b90f1f8 | -7.65187 | -45.24574 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1842ab25-c203-3853-8dad-6810dfd9fe23 | -5.95515 | -43.33028 | 2025-08-22 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 11c48ecb-df0c-3677-b3be-ee0c53966d59 | -8.06604 | -49.71273 | 2025-08-22 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d535f041-5fcf-3236-abcd-d54ac6cc1c62 | -6.92576 | -44.37796 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 628c1db9-8aa4-36c9-971f-5197deaabc68 | -5.85232 | -46.2243 | 2025-08-22 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21278b32-99fe-3642-8c2f-9ace0b217251 | -6.65255 | -44.40956 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c52e50fc-1d01-3026-a73d-0ee075467616 | -9.31208 | -57.02052 | 2025-08-22 04:19:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 06dd9cbd-44df-3f0e-9cdb-ebf05878e450 | -4.8328 | -55.76807 | 2025-08-22 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b18462f4-d400-3ef7-b129-5d2b39899a4e | -7.626 | -46.25901 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b1c8e23-5f3f-3efb-9818-40e0b0085460 | -8.04255 | -47.68115 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18a36c3d-d154-3046-bb1e-11e996ab342f | -7.26627 | -43.67009 | 2025-08-22 04:19:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f6f47ad-e6ba-37c8-a2f2-063e4f16f37b | -6.50677 | -44.58174 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b4802559-549f-3d7a-919d-81b56cd38a46 | -5.79048 | -45.07371 | 2025-08-22 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| df0a88f8-a9d4-336f-a6cc-ee32992fb59b | -11.1252 | -44.72083 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89c6d9d5-5802-3a52-bf34-74e7bc1d4287 | -7.62658 | -46.25543 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 671bf5c0-f859-3775-9332-a2551bde2c2c | -6.08432 | -44.13517 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f31ed789-ae96-3036-9b2c-c714c1ccf48b | -4.24769 | -54.92876 | 2025-08-22 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19f85b69-e965-3289-8209-a1a12557e725 | -7.14466 | -44.17258 | 2025-08-22 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e55718f3-5e1f-3933-9021-5dbfd080de74 | -5.79489 | -45.06731 | 2025-08-22 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 007ad0b7-27cc-37f0-8fd5-d6c9999e331f | -6.77774 | -44.32632 | 2025-08-22 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5e85d8f-748b-37bc-9c97-b766b160060e | -11.91527 | -50.53495 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ea0f396-dbe2-3364-ad57-bbc99217d120 | -6.44036 | -53.38293 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d38588ba-a78b-393b-9f7f-608e33fae9cd | -8.90776 | -47.33116 | 2025-08-22 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc65f70a-dcac-39b0-a71a-b98d894e8b9a | -6.49018 | -43.44922 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fb37c11-5be7-338e-9a10-09d754bd6dd1 | -6.52237 | -44.41749 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47e0121e-ba81-39c8-bc1e-861bc363d766 | -12.52642 | -45.60308 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d48976e1-9ccf-3f01-bbaf-366093c1ac19 | -10.97442 | -45.60678 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ce2c5c8-7c88-3242-841c-3f7438aee466 | -6.8966 | -52.86635 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e18fc5c-7ce9-31a8-8a7e-3217aa108b67 | -6.94662 | -44.28821 | 2025-08-22 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 482b04f6-9639-3762-b12a-5c07a69a994e | -7.14133 | -44.17208 | 2025-08-22 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b36160d-0a2f-3c4d-bd9f-54b95f7f26d0 | -6.48906 | -43.45643 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e03a0ef8-0cdd-3187-a2fc-ed3921111b89 | -9.17187 | -49.67015 | 2025-08-22 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e670a723-fd38-3d80-9d3c-17fd353f0469 | -6.35093 | -43.37958 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2d93e1b-f0b0-3e28-a9ac-2d4feb42e29f | -6.94806 | -44.1708 | 2025-08-22 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40e90ad9-36e8-3147-9d9a-dafccb4f33cb | -8.83153 | -52.03257 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f86579a7-c5e6-363d-90fb-a0a22a6d3ab1 | -7.6552 | -46.22712 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b845fa9-3c47-30fb-b881-b16d83d6ea1c | -6.42022 | -44.67747 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebe308db-d46b-3ba6-a898-feb17ae3f159 | -11.31703 | -44.95267 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fe0dda6-3332-38d4-b620-a1cd5dfb9d00 | -6.63651 | -47.90062 | 2025-08-22 04:19:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a7225a0e-7559-31d2-baea-52e55ccf3179 | -6.73193 | -43.13326 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14649d5d-7a5b-39c2-85c6-b8f5dd785eac | -10.85691 | -47.2555 | 2025-08-22 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcce6746-070a-3879-9226-371d965e8043 | -5.87995 | -50.15471 | 2025-08-22 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4730140-bb0d-3169-9f20-2746a9b34e42 | -6.98064 | -46.92818 | 2025-08-22 04:19:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a388d918-9de5-3f10-8a9c-a42b9a1e1844 | -12.6038 | -47.08765 | 2025-08-22 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28e945fa-716d-338e-af30-ffcfa6e34e5d | -11.96815 | -46.77386 | 2025-08-22 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd9af171-d92e-3f8c-af5d-4de09159ed56 | -6.15254 | -45.03909 | 2025-08-22 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 210146b8-b4e9-3276-a8df-03f89e5b232e | -5.96967 | -52.22782 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e628383b-052c-3888-977b-4a378d6c0b4f | -6.11422 | -44.37807 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c77e319-e717-3bc7-b735-082467aa7db9 | -11.29391 | -44.93085 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0ab1947-f085-3dd6-a55a-8c4eb27557f2 | -10.8672 | -50.84786 | 2025-08-22 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfc7d2c2-6a78-3e0b-a284-5af521196648 | -10.1854 | -47.56393 | 2025-08-22 04:19:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9887944a-1feb-36bd-b235-11f4929bc281 | -6.94142 | -44.92676 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4524b74d-758e-30a2-a8fa-ce7b86d6e766 | -6.51338 | -44.58278 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6c41af6-cc12-3f78-a1a4-5a41352a14a2 | -6.94329 | -44.28801 | 2025-08-22 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bd39eb79-6511-3f15-bf22-3dfaa4ca5da7 | -5.93757 | -42.55937 | 2025-08-22 04:19:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d60869e4-f27b-383e-83a5-bb90ba85bf31 | -8.13972 | -45.55539 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f818f4ce-5fad-327e-9464-c9b313b836a4 | -6.50237 | -44.58813 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45be74ad-159f-3621-b979-7d69bd59ef39 | -6.95004 | -44.54868 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23b3f5ba-6dc9-3f59-a3fd-d2c0c7fe85d7 | -6.58269 | -44.72473 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bdb9a42-1772-34e5-a557-8079520c59c1 | -12.00191 | -44.66457 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 223c5fa1-c34a-3759-99a5-6d54e4d792f6 | -5.52262 | -46.42353 | 2025-08-22 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45602712-5c83-37e1-819f-ab4b29389bc8 | -6.29578 | -43.88991 | 2025-08-22 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0ec2ff4-8d0d-3d1f-a1b6-30133d134329 | -6.6564 | -44.40662 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d854b1d-6ffa-362e-8027-9498c8e53f7f | -8.81199 | -45.3424 | 2025-08-22 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 60ecfc29-598c-3c7a-8595-22cadd4e0017 | -6.55025 | -42.9937 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90c2bc06-92e1-317d-9d7b-33b0205d2e3a | -5.87479 | -53.62137 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09c94e3b-504d-341e-b181-dc0443f72187 | -8.84871 | -52.04007 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a187afc0-a374-3c3b-853d-6b281860639a | -5.78772 | -45.06973 | 2025-08-22 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb51e5a0-da5f-3846-954b-75d71bf9a57a | -6.07768 | -44.13414 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39c86add-7472-3604-b3b4-971263b3067e | -10.18601 | -47.56017 | 2025-08-22 04:19:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20095399-9076-3814-840b-06c967e8685d | -7.8114 | -46.88803 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e48139f9-eca8-32ba-be20-98faa7ea1d8b | -6.20626 | -43.56934 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5a1b1c1-2313-30ec-9bc1-6655a9621586 | -7.85689 | -46.99809 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2b3e8819-ad8e-39dd-a995-2568b8996e87 | -11.30757 | -44.94753 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c144130-4c86-34d9-97f1-d6d66c6d8b8e | -6.04616 | -44.35642 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6d869ff-b23f-37ac-be16-cb16e423c92b | -7.58704 | -49.56945 | 2025-08-22 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8ccbccd-2e50-3f97-a9e1-3017b24a76f6 | -10.27839 | -46.75643 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8546bf47-9a20-313d-b79d-6b2475df8271 | -6.06544 | -44.10382 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6688931c-dbba-30aa-8d19-d0108c7b97e1 | -6.49916 | -43.4358 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90f44e53-ce09-34f2-b210-45d55b2ea7f9 | -9.69374 | -47.93219 | 2025-08-22 04:19:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47663506-4725-38d2-a6bf-cdc0ef813f80 | -7.58913 | -45.40651 | 2025-08-22 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da6ba4bf-d0ac-377d-97ad-29c75f0c9f7f | -10.28232 | -46.75333 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd375ea8-15b1-35d6-8ad2-0afc38d8b3a1 | -6.74163 | -50.95967 | 2025-08-22 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d924ce71-1465-3629-a4c1-9076abc76a48 | -6.11146 | -44.3741 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98d0b283-cc73-3b02-83ac-9098cd638a7f | -13.0288 | -46.3213 | 2025-08-22 04:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 87ffcb7e-615a-3b02-afd9-c4162e734bcb | -12.9524 | -46.2876 | 2025-08-22 04:20:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| a16d7b52-7f2f-3d76-bf6a-adf43187f88e | -16.50126 | -46.73515 | 2025-08-22 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3c0246d-2a79-3987-9111-942179cc03b6 | -14.82934 | -47.93483 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99969dda-4b93-3e10-a183-1ef19524bd12 | -13.14034 | -57.11883 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f290b898-0bde-3097-9661-c66840352213 | -18.31329 | -48.86765 | 2025-08-22 04:21:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| b679008a-8fd9-365e-9cea-c3af3f09035c | -12.99243 | -45.24197 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f9a5f4d5-6ea1-34f6-9e36-a4e13791f2da | -20.3611 | -46.51128 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdbf6812-621e-34f8-a322-1a62cbe7e54d | -13.00076 | -45.23223 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6616d338-25a5-3e77-a270-78823185a401 | -15.03019 | -54.86223 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 280df5a8-0923-3d20-8620-0070ffeb4f96 | -18.89151 | -47.25233 | 2025-08-22 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13f57e8d-611d-390e-95c5-f9cb39c8349f | -16.78251 | -47.66328 | 2025-08-22 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f4f58554-30f8-355a-b341-aececa287fa1 | -13.5949 | -47.01003 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25361fa1-67aa-355d-a454-2315be933166 | -16.18686 | -47.98613 | 2025-08-22 04:21:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README33.md)
