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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0025bbd4-f299-3368-bc11-785e2f3f63e7 | -13.2829 | -45.1543 | 2026-07-09 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 376.2 |
| 16bafc1a-7b84-3954-b4c2-2c09ab4e6541 | -13.2824 | -45.1776 | 2026-07-09 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 184.1 |
| fbf4a3af-5fa6-3b74-bfc2-f78b057e8833 | -13.2829 | -45.1543 | 2026-07-09 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 311.7 |
| e511aeb2-a4ca-3149-84e6-89c562e1f559 | -13.2824 | -45.1776 | 2026-07-09 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 226.1 |
| 534869aa-babf-309a-a251-db4efdd68209 | -13.2635 | -45.1575 | 2026-07-09 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| e068e078-7802-3f3b-9106-c1a17a669678 | -13.2829 | -45.1543 | 2026-07-09 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 427.0 |
| 98f2732f-8bbe-3c52-a34f-1a097e54fb3e | -18.1047 | -53.9972 | 2026-07-09 12:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 9c690c28-1675-37b4-a2b0-396d2d244be2 | -13.2635 | -45.1575 | 2026-07-09 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 252.2 |
| 0b066eb4-09aa-3f8d-869d-a4ef810b2271 | -13.2824 | -45.1776 | 2026-07-09 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 145.3 |
| f4157747-d96b-3411-bb4a-fa77cf0bf8a1 | -13.2829 | -45.1543 | 2026-07-09 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 478.1 |
| 764aa032-4d0d-34a9-8dce-6b45052b5d89 | -4.3439 | -47.76091 | 2026-07-09 12:04:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 74b8e16a-b87f-38b9-9669-9cf556fd674b | -6.0506 | -47.73307 | 2026-07-09 12:04:00 | TERRA_M-T | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 74ccc5ee-2b2a-3fbb-894b-47a36cae0bd6 | -8.36637 | -48.23655 | 2026-07-09 12:04:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 39cc852c-e1a0-3eae-aacb-8c9e66da22b0 | -8.1313 | -47.09167 | 2026-07-09 12:04:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e326968a-4dbd-37c3-9de1-6fd6a74dc893 | -7.39997 | -49.76165 | 2026-07-09 12:04:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 47903bad-0a0a-3792-9c42-7fe460b57ba2 | -9.10106 | -51.17051 | 2026-07-09 12:04:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eb86b4fa-9fd3-32c8-bde2-ce13d66cd293 | -9.226 | -48.57796 | 2026-07-09 12:04:00 | TERRA_M-T | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eb7083a3-4eb7-3cda-954d-124f10d5e65f | -8.36496 | -48.24702 | 2026-07-09 12:04:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 9777c5b4-6849-32f7-9ac8-3ef1f6db95e8 | -8.69392 | -54.54639 | 2026-07-09 12:04:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 9c0a0c03-ddb9-312e-9b05-3dde5b1b471a | -7.6397 | -50.02295 | 2026-07-09 12:04:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6c50a23c-9e7e-332d-8eb4-36938e4fdea9 | -8.69577 | -54.53421 | 2026-07-09 12:04:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ad9d2e21-15ef-3c6b-bb62-e3b3b51d2e15 | -8.72525 | -47.83934 | 2026-07-09 12:04:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5864bdce-53ef-38fb-b94a-e7c41788aed5 | -9.23759 | -50.14656 | 2026-07-09 12:04:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2f2d2c4b-19bc-3392-8bda-63cc69d3a1e2 | -17.57096 | -54.04327 | 2026-07-09 12:06:00 | TERRA_M-T | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fbb3cd78-e702-3d25-92c0-b1a1577ef6c3 | -11.44515 | -47.58704 | 2026-07-09 12:06:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 26247024-2369-3a26-ab8e-807b5f061e6c | -16.03513 | -43.45768 | 2026-07-09 12:06:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 60436e0e-1c5d-3a8e-86b6-8954dc44bbb2 | -17.07453 | -45.39755 | 2026-07-09 12:06:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| cf3aa2de-93a7-3609-bd17-29348e177d6d | -11.65962 | -46.35419 | 2026-07-09 12:06:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b9bf8442-0672-36f8-8e65-a85d56813666 | -17.55445 | -54.03086 | 2026-07-09 12:06:00 | TERRA_M-T | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| eeb6c402-043d-39ca-ae9e-3ea28e7a2ade | -17.57238 | -54.03368 | 2026-07-09 12:06:00 | TERRA_M-T | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 23.6 |
| fff9a12d-4b9e-3cb1-ad4f-4b53fe16de19 | -11.45567 | -47.58766 | 2026-07-09 12:06:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 340426b4-0af5-3871-89b8-25b24dc8a779 | -13.09339 | -48.17125 | 2026-07-09 12:06:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 90200f57-39e2-307b-9145-9b4a5efeb384 | -13.35732 | -54.36816 | 2026-07-09 12:06:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1f618448-aecd-3880-b0c1-700c737563e6 | -18.75875 | -49.07556 | 2026-07-09 12:06:00 | TERRA_M-T | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 50f0d660-11d8-3534-8360-f3745e6f6909 | -16.03113 | -43.46247 | 2026-07-09 12:06:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| e4e5e3cf-7b45-351b-8de4-140f03b85e81 | -17.55587 | -54.02129 | 2026-07-09 12:06:00 | TERRA_M-T | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 614445b8-3cfd-370e-85d3-bcc8a6e5c243 | -18.10236 | -54.01006 | 2026-07-09 12:06:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 940619f9-7b77-3c6a-8c25-c6d8c3e22227 | -11.65764 | -46.37028 | 2026-07-09 12:06:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| fabd9f65-d1fd-32d1-9e2b-d2bc24da11ac | -13.27685 | -45.1574 | 2026-07-09 12:06:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 709.5 |
| 7cd1baa1-6d02-3663-bbe6-0423bbd70840 | -17.90322 | -54.65768 | 2026-07-09 12:06:00 | TERRA_M-T | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| de30a925-5806-3531-bfea-9a23e7e65779 | -18.10377 | -54.00056 | 2026-07-09 12:06:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 8e00d763-b80f-35ef-a526-a22c22f548fd | -14.87986 | -47.25755 | 2026-07-09 12:06:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bf770276-ffef-363a-9e5c-56a65c099f3d | -17.59018 | -46.52599 | 2026-07-09 12:06:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a699c9cc-4065-3929-bb90-be97ff72c43c | -16.52732 | -47.7354 | 2026-07-09 12:06:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c01ffbcf-948e-3d33-acd6-c67377c9fdf0 | -10.78298 | -54.09932 | 2026-07-09 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 76bfceef-6fe2-34f0-b47f-af14c4c2a9bd | -13.27445 | -45.17815 | 2026-07-09 12:06:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 228.2 |
| 5fec6bf0-40b1-3fa6-9e38-a707be929791 | -17.54691 | -54.01988 | 2026-07-09 12:06:00 | TERRA_M-T | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 97a44c58-f4a1-37b2-88f4-284c97a82a77 | -19.64807 | -47.60482 | 2026-07-09 12:08:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 54a909c3-6586-3ec2-9093-96c37e8141eb | -19.64995 | -47.58753 | 2026-07-09 12:08:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a8f9e5f6-101b-34f8-8d05-930fe2af2914 | -13.2824 | -45.1776 | 2026-07-09 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 40451864-5d77-3360-a653-3e0aef5974f0 | -18.1047 | -53.9972 | 2026-07-09 12:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 105.7 |
| c3fff2ba-5d97-3634-8b97-d54ba1d52f04 | -13.2829 | -45.1543 | 2026-07-09 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 380.6 |
| 7e3eefe0-c419-31dd-a0ed-31a62e291d95 | -13.2631 | -45.1808 | 2026-07-09 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| fd8b3726-6f46-3729-925f-bf131e510a83 | -13.2635 | -45.1575 | 2026-07-09 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 238.5 |
| 7e25012e-92db-3564-a64c-29c65c699aa1 | -8.3651 | -48.2463 | 2026-07-09 12:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 7e6042dc-cb71-30bb-8c7c-ed72c51be23d | -30.69736 | -52.5606 | 2026-07-09 12:12:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 21.0 |
| 278988fd-5c0b-3a9f-9705-b8e67e271821 | -13.2635 | -45.1575 | 2026-07-09 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 344.3 |
| fbc251ed-9fce-3b64-bf5a-6963732fe450 | -18.1047 | -53.9972 | 2026-07-09 12:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 53c7f8bb-3832-32cf-8acc-177f7ac9c803 | -13.2631 | -45.1808 | 2026-07-09 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| d0845db1-a799-37b1-b605-6ec373e62537 | -13.2829 | -45.1543 | 2026-07-09 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 431.5 |
| 29e567e5-cd46-30bd-9f57-36d1b2e553c6 | -13.2824 | -45.1776 | 2026-07-09 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 190.1 |
| 278432ac-0698-3e63-8e92-da83d8eca5ec | -8.3651 | -48.2463 | 2026-07-09 12:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 4091d8cd-cf47-3351-9aa0-7ba3beae4ffe | -8.3651 | -48.2463 | 2026-07-09 12:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 4449bc6e-de3e-3a2e-b617-8cb9f8779d97 | -13.2635 | -45.1575 | 2026-07-09 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 1483d272-0481-335a-a896-165094920d3c | -13.2829 | -45.1543 | 2026-07-09 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 646.5 |
| 3bbac91b-0353-3e0c-8ac6-816b01abf706 | -13.2631 | -45.1808 | 2026-07-09 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 8ac53023-8e88-378c-a842-b64db7638a5d | -13.2824 | -45.1776 | 2026-07-09 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 253.0 |
| 389f8cf4-d9b4-3bcf-94c8-d8be6d67928f | -13.2631 | -45.1808 | 2026-07-09 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f4361a73-ddc2-36b0-8a6b-412495729036 | -13.2824 | -45.1776 | 2026-07-09 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 230.8 |
| aa05114a-f7d8-3053-8c00-f61067a79387 | -13.2829 | -45.1543 | 2026-07-09 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 644.6 |
| 04cc8779-f95a-33eb-ad11-cc9d206aaa4d | -18.1047 | -53.9972 | 2026-07-09 12:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 94.4 |
| eb407736-8b36-3db6-82f5-2b5c64fadc1a | -13.2635 | -45.1575 | 2026-07-09 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 266.0 |
| d79d582d-62a9-3694-9e14-05660b3e6953 | -13.2635 | -45.1575 | 2026-07-09 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 478.3 |
| 596ed72f-44d5-30bc-816c-0df5a6ca817d | -13.2631 | -45.1808 | 2026-07-09 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| cd6b7b59-1374-3912-a7df-d5981a7c52eb | -13.2829 | -45.1543 | 2026-07-09 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 488.9 |
| 72ecbda0-081a-311b-a2b5-43523fde6a57 | -13.2824 | -45.1776 | 2026-07-09 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 155.1 |
| e5ae2e42-8b07-3c4a-ab72-8ae2bbdc330e | -8.711 | -54.5455 | 2026-07-09 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 18091271-d859-34b6-920c-21c96c428456 | -13.2635 | -45.1575 | 2026-07-09 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 370.1 |
| 30f1d723-d5a7-3018-9c3a-38cf8d3664e2 | -8.711 | -54.5455 | 2026-07-09 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| ea7daad2-6e44-38e7-967d-bef2bf3a8e1b | -13.2824 | -45.1776 | 2026-07-09 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 2a5bdb1f-4eae-3d02-af17-f1f7730b2b36 | -13.2829 | -45.1543 | 2026-07-09 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 938.6 |
| 69960096-0bcd-38d6-b612-f07d48e67056 | -13.2829 | -45.1543 | 2026-07-09 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 721.0 |
| 6c7cd209-daa1-31c9-ac64-e27d3d71afe2 | -8.711 | -54.5455 | 2026-07-09 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| eab56b6b-8e05-303f-ab7a-0624ccb0b5d8 | -13.2635 | -45.1575 | 2026-07-09 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 408.2 |
| 63fe1c16-5487-3933-9100-4eee71c1284d | -13.2824 | -45.1776 | 2026-07-09 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| e15a0e79-f24c-3ef9-aaa4-1f73012e0c73 | -13.2824 | -45.1776 | 2026-07-09 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 0da70606-6473-38ab-84d9-8620aa627fe9 | -13.2631 | -45.1808 | 2026-07-09 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 98706e89-77f9-3702-91c2-27b16d3bfc73 | -13.2829 | -45.1543 | 2026-07-09 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 554.4 |
| 0a7ac2bd-e984-3312-8695-fd7bbe49470f | -13.2635 | -45.1575 | 2026-07-09 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 638.6 |
| d1336ea4-88b1-336f-ac25-01529ada22e8 | -8.711 | -54.5455 | 2026-07-09 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| d640413b-911b-3119-a91a-9e775572be3d | -8.6923 | -54.5468 | 2026-07-09 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 5e9c8e41-74d5-3282-8f04-23a46a2325bd | -17.5509 | -54.0157 | 2026-07-09 13:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 9fd3603b-f7f6-3595-a17d-90db41ee66cc | -8.711 | -54.5455 | 2026-07-09 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 50fe5871-9b54-3a72-8433-671fd1d02d41 | -13.2824 | -45.1776 | 2026-07-09 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 692ea1f0-3a1b-37a0-be27-de2866d481e7 | -13.2829 | -45.1543 | 2026-07-09 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 756.4 |
| ac8d5deb-1162-3663-bef9-3fef4d3551b9 | -17.1209 | -49.9942 | 2026-07-09 13:40:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 22d6e49d-89bc-3aef-9b0d-cb8a4710f5c2 | -17.5896 | -54.0524 | 2026-07-09 13:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 6029d7e1-0559-33f6-9e2b-09d3375b600a | -13.2635 | -45.1575 | 2026-07-09 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 427.7 |
| e3664522-3af4-3b19-bcbb-ba4d32c399ec | -13.2824 | -45.1776 | 2026-07-09 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 452a1bba-2687-324f-adc8-93f842e93a29 | -13.2635 | -45.1575 | 2026-07-09 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 326.5 |


[Clique aqui para ver as próximas entradas](README14.md)
